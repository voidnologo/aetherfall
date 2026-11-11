"""Extract rulebook prose from web/rules/*.njk so tools/prose_lint.py can check it.

Usage: python3 tools/rulebook_prose.py [OUT_DIR]   (default: /tmp/rulebook_prose)
Then:  python3 tools/prose_lint.py --summary OUT_DIR/*.rules.md   (or *.voice.md)
Each OUT_DIR/<chapter>.<kind>.map.json maps extracted line numbers back to the .njk source.

Voice callouts (handler/scene/street/believer/scholar) are in-world prose; the rest is
rules text. Writes one extracted file per chapter per kind, with a line map back to source.
"""
import html, re, sys, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/rulebook_prose")
OUT.mkdir(parents=True, exist_ok=True)
VOICE = {"handler", "scene", "street", "believer", "scholar"}
sys.path.insert(0, str(ROOT / "tools"))

def extract(path):
    lines = path.read_text().splitlines()
    stack, paras, buf, start = [], {"voice": [], "rules": []}, None, 0
    for i, line in enumerate(lines, 1):
        for m in re.finditer(r"\{%-?\s*(end)?([a-z]+)", line):
            end, name = m.group(1), m.group(2)
            if end and stack and stack[-1] == name:
                stack.pop()
            elif not end and name in VOICE | {"gmnote", "example", "warning"}:
                stack.append(name)
        if buf is None and "<p" in line:
            buf, start = [], i
        if buf is not None:
            buf.append(line)
            if "</p>" in line:
                text = re.sub(r"<[^>]+>", "", " ".join(buf))
                text = html.unescape(re.sub(r"\{[{%].*?[}%]\}", "", text))
                text = re.sub(r"\s+", " ", text).strip()
                kind = "voice" if any(s in VOICE for s in stack) else "rules"
                if len(text.split()) >= 4:
                    paras[kind].append((start, text))
                buf = None
    return paras

for njk in sorted((ROOT / "web/rules").glob("*.njk")):
    for kind, ps in extract(njk).items():
        if not ps:
            continue
        f = OUT / f"{njk.stem}.{kind}.md"
        # one paragraph per line, blank line between; remember mapping
        body, mapping, ln = [], {}, 1
        for src, t in ps:
            body += [t, ""]
            mapping[ln] = src
            ln += 2
        f.write_text("\n".join(body))
        (OUT / f"{njk.stem}.{kind}.map.json").write_text(json.dumps(mapping))

print(f"extracted to {OUT}")
