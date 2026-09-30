#!/usr/bin/env python3
"""Build a print-ready PDF of the Aetherfall rulebook from the Eleventy _site output."""

import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE_DIR = ROOT / "_site" / "rules"
DATA_DIR = ROOT / "web" / "_data"
CSS_DIR = ROOT / "web" / "rules" / "css"
OUTPUT_DIR = ROOT / "print"


def load_pages():
    with open(DATA_DIR / "pages.json") as f:
        return json.load(f)


def extract_content(html_path):
    """Extract the chapter body from a built HTML page."""
    text = html_path.read_text()

    # Find the page-hero div (chapter header)
    hero_match = re.search(r'<div class="page-hero', text)
    if not hero_match:
        print(f"  WARNING: No page-hero found in {html_path.name}", file=sys.stderr)
        return ""

    # Find the bottom nav (chapter navigation links) — marks end of content
    nav_match = re.search(r'\n\s*<nav class="page-nav">', text[hero_match.start():])
    if nav_match:
        content = text[hero_match.start():hero_match.start() + nav_match.start()]
    else:
        # Fallback: find the footer
        footer_match = re.search(r'<footer class="site-footer">', text[hero_match.start():])
        if footer_match:
            content = text[hero_match.start():hero_match.start() + footer_match.start()]
        else:
            content = text[hero_match.start():]

    # Strip the compact nav if it got included
    content = re.sub(r'<nav class="page-nav-compact">.*?</nav>\s*', '', content, flags=re.DOTALL)

    return content


def prefix_ids(content, page_id):
    """Prefix all id attributes with the page ID to avoid duplicates across chapters."""
    def replace_id(match):
        attr = match.group(1)
        id_val = match.group(2)
        return f'{attr}"{page_id}--{id_val}"'

    content = re.sub(r'(id=)"([^"]+)"', replace_id, content)
    # Also fix internal href="#..." links to match
    content = re.sub(r'(href=)"#([^"]+)"', lambda m: f'{m.group(1)}"#{page_id}--{m.group(2)}"', content)
    return content


def render_mermaid(content):
    """Replace <pre class="mermaid"> blocks with pre-rendered PNGs.

    WeasyPrint doesn't run JavaScript, so without this the PDF prints the raw
    flowchart source. The web's dark classDef styling is stripped in favour of
    mermaid's neutral theme, which reads better on paper.
    """
    blocks = list(re.finditer(r'<pre class="mermaid">(.*?)</pre>', content, flags=re.DOTALL))
    if not blocks:
        return content

    diagram_dir = OUTPUT_DIR / "diagrams"
    diagram_dir.mkdir(exist_ok=True)
    browser = shutil.which("chromium") or shutil.which("google-chrome")
    puppeteer_cfg = diagram_dir / "puppeteer.json"
    puppeteer_cfg.write_text(json.dumps(
        {"executablePath": browser, "args": ["--no-sandbox"]} if browser else {"args": ["--no-sandbox"]}
    ))

    for m in reversed(blocks):
        source = html.unescape(re.sub(r"<[^>]+>", "", m.group(1)))
        source = "\n".join(l for l in source.splitlines() if not l.strip().startswith("classDef"))
        source = re.sub(r":::\w+", "", source)
        digest = hashlib.sha1(source.encode()).hexdigest()[:12]
        src_path = diagram_dir / f"{digest}.mmd"
        png_path = diagram_dir / f"{digest}.png"
        if not png_path.exists():
            src_path.write_text(source)
            result = subprocess.run(
                ["npx", "-y", "-p", "@mermaid-js/mermaid-cli", "mmdc", "-p", str(puppeteer_cfg),
                 "-t", "neutral", "-b", "white", "-s", "3", "-i", str(src_path), "-o", str(png_path)],
                capture_output=True, text=True,
            )
            if result.returncode != 0:
                print(f"  WARNING: mermaid render failed ({digest}); dropping diagram", file=sys.stderr)
                content = content[:m.start()] + content[m.end():]
                continue
        img = f'<figure class="print-diagram"><img src="{png_path}" alt="Flowchart"></figure>'
        content = content[:m.start()] + img + content[m.end():]
    return content


# Print-resolution frames: 4x upscales (tools/upscale_print.py) cut to the same box the web
# copies use. (x, y, w, h) on the 832x1216 master, recovered by matching the web frames.
PRINT_FRAMES = {
    "aether": ("proto-D2-decolitho_frame_aether_v02_seed-131618214", (26, 24, 782, 1168)),
    "galvanic": ("proto-D2-decolitho_frame_galvanic_v02_seed-1166265576", (26, 24, 782, 1150)),  # bottom trimmed: fake lettering
    "split": ("proto-D2-decolitho_frame_split_v02_seed-2427297017", (24, 24, 782, 1168)),
    "neutral": ("proto-D2-decolitho_frame_neutral_v02_seed-1553240695", (26, 24, 782, 1168)),
    "front": ("proto-B-twoinks_frame_v01_seed-3867070072", (24, 24, 782, 1168)),
}


def print_art_css():
    """Cut print-resolution frames and return CSS that points the openers and front matter
    at them. Frames without a 4x master keep the web copy from print.css."""
    art_dir = OUTPUT_DIR / "art"
    art_dir.mkdir(exist_ok=True)
    rules = []
    for name, (stem, (x, y, w, h)) in PRINT_FRAMES.items():
        master = ROOT / "art" / "decorative" / "print" / f"{stem}_x4.png"
        if not master.exists():
            continue
        out = art_dir / f"frame-{name}.jpg"
        if not out.exists() or out.stat().st_mtime < master.stat().st_mtime:
            subprocess.run(["magick", str(master), "-crop", f"{w * 4}x{h * 4}+{x * 4}+{y * 4}", "+repage",
                            "-quality", "92", str(out)], check=True)
        if name == "front":
            for page in ("title-page", "toc-page"):
                rules.append(f"@page {page} {{ background: #efe6d2 url({out.as_uri()}) center / 100% 100% no-repeat; }}")
        else:
            rules.append(f"@page opener-{name} {{ background: #0e1a2b url({out.as_uri()}) center / cover no-repeat; }}")
    if rules:
        print(f"  Print-resolution frames: {len(rules)} page rule(s)")
    return "\n".join(rules)


def build_toc(pages):
    """Build a table of contents with target-counter references."""
    entries = []
    for page in pages:
        num = page["num"]
        if not re.match(r'^\d+$', num) and num != "QS":
            continue
        display_num = num if num != "QS" else "QS"
        entries.append(
            f'    <li class="toc-entry">'
            f'<span class="toc-num">{display_num}</span>'
            f'<a href="#chapter-{page["id"]}">{page["title"]}</a>'
            f'</li>'
        )
    return "\n".join(entries)


def build_combined_html(pages):
    """Assemble all chapters into a single print-ready HTML document."""
    css_path = CSS_DIR / "print.css"

    parts = []
    parts.append(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Aetherfall RPG — Rulebook</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400;1,700&family=Source+Serif+4:ital,wght@0,400;0,600;0,700;1,400&family=JetBrains+Mono:wght@400;700&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css_path}">
<style>{print_art_css()}</style>
</head>
<body>
""")

    # Title page
    parts.append("""
<section class="title-page">
  <div class="title-page-content">
    <h1 class="book-title">Aetherfall</h1>
    <p class="book-subtitle">Magic &amp; Machines in the 1920s</p>
    <p class="book-type">Tabletop Roleplaying Game</p>
    <p class="book-edition">Playtest Draft</p>
  </div>
</section>
""")

    # Table of contents
    toc_entries = build_toc(pages)
    parts.append(f"""
<section class="toc-chapter">
  <h1 class="chapter-title toc-title">Table of Contents</h1>
  <ol class="toc">
{toc_entries}
  </ol>
</section>
""")

    # Chapters
    for page in pages:
        page_file = page["file"]
        html_path = SITE_DIR / page_file
        if not html_path.exists():
            print(f"  WARNING: {html_path} not found, skipping", file=sys.stderr)
            continue

        print(f"  Processing: {page['num']} — {page['title']}")
        content = extract_content(html_path)
        if not content:
            continue

        content = prefix_ids(content, page["id"])
        content = render_mermaid(content)
        # Chapter pages link images relative to _site/rules/; the combined file lives in print/
        assets = (ROOT / "_site" / "assets").as_uri()
        content = content.replace('src="../assets/', f'src="{assets}/').replace('src="/assets/', f'src="{assets}/')
        parts.append(f'<section class="chapter" id="chapter-{page["id"]}" data-theme="{page.get("theme", "neutral")}">')
        parts.append(content)
        parts.append("</section>\n")

    parts.append("</body>\n</html>")
    return "\n".join(parts)


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    print("Loading page manifest...")
    pages = load_pages()

    print("Assembling combined HTML...")
    html = build_combined_html(pages)

    combined_path = OUTPUT_DIR / "aetherfall-rulebook.html"
    combined_path.write_text(html)
    print(f"  Written: {combined_path}")

    pdf_path = OUTPUT_DIR / "aetherfall-rulebook.pdf"
    print(f"Generating PDF with WeasyPrint...")
    # Prefer a system weasyprint; fall back to an ephemeral uvx install
    weasyprint = ["weasyprint"] if shutil.which("weasyprint") else ["uvx", "--from", "weasyprint", "weasyprint"]
    result = subprocess.run(
        [*weasyprint, str(combined_path), str(pdf_path)],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print("WeasyPrint errors:", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        sys.exit(1)

    if result.stderr:
        # WeasyPrint prints warnings to stderr even on success
        warnings = [l for l in result.stderr.splitlines() if "WARNING" in l]
        if warnings:
            print(f"  ({len(warnings)} warnings — mostly font/CSS)")

    print(f"  Done: {pdf_path}")
    print(f"  Size: {pdf_path.stat().st_size / 1024 / 1024:.1f} MB")


if __name__ == "__main__":
    main()
