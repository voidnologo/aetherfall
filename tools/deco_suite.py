#!/usr/bin/env python3
"""
Aetherfall Art Pipeline — Deco Suite (Session 35)

Generates the Deco Lithograph ornament kit and spot illustrations planned in
docs/art/deco-suite-plan.md. Every piece is drawn isolated on a flat bone field
with empty margin, so tools/cutout.py can key the background to alpha without
cropping anything flat.

ComfyUI holds ~19 GB of RAM and idle waiters get reaped, so queue and collect
are separate steps:

    python tools/deco_suite.py --wave 1 --queue-only          # 3 seeds per piece
    python tools/deco_suite.py --piece spot_tear --seeds 2 --queue-only
    python tools/deco_suite.py --collect                      # file finished jobs into art/
    python tools/deco_suite.py --wave 1 --dry-run             # print prompts only
"""

import argparse
import json
import random
import re
import shutil
import time
import urllib.request

from comfyui_generate import ART_DIR, COMFYUI_OUTPUT, COMFYUI_URL, PROJECT_ROOT, queue_prompt
from prototype_styles import DIRECTIONS, build_workflow

LOG_PATH = PROJECT_ROOT / "docs" / "art" / "prototype-runs.jsonl"
PREFIX = "aetherfall/deco/"
VERSION = 1

ORNAMENT_STYLE = {
    "loras": [],
    "prefix": (
        "A 1920s Art Deco lithograph printer's ornament, as printed in a luxury book of the "
        "period. Flat printed color shapes with crisp edges, bold geometric simplification, "
        "subtle lithographic paper grain. Strict limited palette of six inks: deep midnight "
        "navy, warm bone ivory, soot black, turquoise cyan, amber gold, and oxblood red."
    ),
    "suffix": (
        "Printed on a plain, flat, empty bone ivory paper background. The ornament is isolated "
        "and centred with a generous empty margin on every side; nothing touches the edges of "
        "the picture. No border around the picture, no background scene, no shadow. Flat "
        "printed color, no photorealism, no 3D, no gradients. Absolutely no text, no letters, "
        "no numbers, no signature."
    ),
}

SPOT_STYLE = {
    "loras": [],
    "prefix": DIRECTIONS["D2"]["prefix"],
    "suffix": (
        "Composed as a small self-contained vignette with an irregular organic outline, "
        "floating on a plain, flat, empty bone ivory paper background with a generous empty "
        "margin on every side; nothing touches the edges of the picture. No rectangular "
        "border, no frame, no panel. " + DIRECTIONS["D2"]["suffix"]
    ),
}

PIECES = {
    # ── Wave 1: ornament kit ──
    "divider_aether": {
        "wave": 1, "art_type": "decorative", "style": ORNAMENT_STYLE, "width": 1536, "height": 384,
        "subject": (
            "A long, slender horizontal section divider for a book page, many times wider than it "
            "is tall. Art Nouveau: whiplash ivy tendrils and small leaves flow out symmetrically "
            "to the left and right from a small central medallion holding a glowing turquoise "
            "crystal. Thin and delicate. Inks: turquoise cyan and deep midnight navy only."
        ),
    },
    "divider_engine": {
        "wave": 1, "art_type": "decorative", "style": ORNAMENT_STYLE, "width": 1536, "height": 384,
        "subject": (
            "A long, slender horizontal section divider for a book page, many times wider than it "
            "is tall. Art Deco machine age: straight parallel rules and stepped chevrons run out "
            "symmetrically to the left and right from a small central riveted medallion with "
            "short amber sunburst rays. Crisp and geometric. Inks: amber gold and soot black only."
        ),
    },
    "divider_neutral": {
        "wave": 1, "art_type": "decorative", "style": ORNAMENT_STYLE, "width": 1536, "height": 384,
        "subject": (
            "A long, slender horizontal section divider for a book page, many times wider than it "
            "is tall. Restrained Art Deco: two thin parallel rules ending in small stepped "
            "terminals, meeting at a small central diamond with a tiny four-point star. Quiet and "
            "elegant. Inks: oxblood red and deep midnight navy only."
        ),
    },
    "dropcap_aether": {
        "wave": 1, "art_type": "decorative", "style": ORNAMENT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A square ornamental initial-letter tile for the first paragraph of a book chapter: a "
            "square frame with an Art Nouveau border of curling ivy tendrils and small glowing "
            "turquoise crystals at the corners, deep midnight navy linework. The centre of the "
            "square is left completely empty as a plain bone panel, with no letter in it."
        ),
    },
    "dropcap_engine": {
        "wave": 1, "art_type": "decorative", "style": ORNAMENT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A square ornamental initial-letter tile for the first paragraph of a book chapter: a "
            "square Art Deco frame with stepped corners, rivets, and short amber sunburst rays "
            "fanning from the top edge, soot black linework. The centre of the square is left "
            "completely empty as a plain bone panel, with no letter in it."
        ),
    },
    "dropcap_neutral": {
        "wave": 1, "art_type": "decorative", "style": ORNAMENT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A square ornamental initial-letter tile for the first paragraph of a book chapter: a "
            "square Art Deco frame of thin parallel lines with stepped corners in oxblood red and "
            "deep midnight navy. The centre of the square is left completely empty as a plain "
            "bone panel, with no letter in it."
        ),
    },
    "tailpiece": {
        "wave": 1, "art_type": "decorative", "style": ORNAMENT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A small symmetrical end-of-chapter printer's ornament, wider than it is tall: a plain "
            "stone keystone in the centre, with a curl of Art Nouveau ivy and a small turquoise "
            "crystal on the left and a fan of Art Deco amber sunburst rays on the right, perfectly "
            "balanced, neither side winning. Compact and simple."
        ),
    },
    # ── Wave 1: spots ──
    # v02 rerolls (user, Session 35): v01 Tear read as amber fire in a rectangle (8c kept as
    # fallback); v01 misfire read as firing into a brick wall (9a closest).
    "spot_tear": {
        "wave": 1, "version": 2, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A rounded vignette: a small 1920s city of stepped Art Deco towers and factory chimneys "
            "in deep midnight navy and soot silhouette, a few oxblood roofs. Above it the night sky "
            "is ripped open by a single jagged vertical crack, like torn paper, and through the crack "
            "pours cold glowing turquoise cyan light in hard-edged rays that fall onto the rooftops. "
            "The only bright color in the picture is the turquoise cyan of the crack. No fire, no "
            "flames, no orange, no smoke clouds. Awe and dread."
        ),
    },
    "spot_misfire": {
        "wave": 1, "version": 2, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A rounded vignette seen from the side: a man's hand in a worn brown leather jacket "
            "sleeve holds a revolver pointed away down a long dark empty alley that recedes into "
            "midnight shadow. The gun has jammed and misfired: the bullet has not left the barrel, "
            "there is no muzzle flash at the barrel's tip; instead a small burst of amber sparks and "
            "a curl of soot-black smoke spits sideways out of the revolver's cylinder, next to the "
            "hand. Nothing stands in front of the gun."
        ),
    },
}


def dest_for(piece: str, seed: int, version: int | None = None):
    version = version or PIECES[piece].get("version", VERSION)
    return ART_DIR / PIECES[piece]["art_type"] / "generated" / f"deco-{piece}_v{version:02d}_seed-{seed}.png"


def collect_from_history():
    """Copy every finished aetherfall/deco job in ComfyUI's history into art/, logging new ones."""
    hist = json.loads(urllib.request.urlopen(f"{COMFYUI_URL}/history?max_items=500").read())
    copied = 0
    for h in hist.values():
        prompt = h["prompt"][2]
        save = next((v for v in prompt.values() if v["class_type"] == "SaveImage"), None)
        if not save or not save["inputs"]["filename_prefix"].startswith(PREFIX):
            continue
        # Prefix is "<piece>" (v01 jobs) or "<piece>_vNN"
        m = re.match(r"(\w+?)(?:_v(\d+))?$", save["inputs"]["filename_prefix"][len(PREFIX):])
        piece, version = m.group(1), int(m.group(2) or 1)
        if piece not in PIECES:
            continue
        seed = next(v for v in prompt.values() if v["class_type"] == "KSampler")["inputs"]["seed"]
        dest = dest_for(piece, seed, version)
        if any((dest.parent.parent / stage / dest.name).exists() for stage in ("generated", "approved", "archived")):
            continue
        for out in h.get("outputs", {}).values():
            for img in out.get("images", []):
                src = COMFYUI_OUTPUT / img["subfolder"] / img["filename"]
                if not src.exists():
                    continue
                shutil.copy2(src, dest)
                copied += 1
                text = next(v for v in prompt.values() if v["class_type"] == "CLIPTextEncode" and v["inputs"]["text"])["inputs"]["text"]
                p = PIECES[piece]
                with LOG_PATH.open("a") as f:
                    f.write(json.dumps({
                        "time": time.strftime("%Y-%m-%d %H:%M:%S"), "file": str(dest.relative_to(PROJECT_ROOT)),
                        "status": "ok", "direction": "D2", "subject": f"deco_{piece}", "seed": seed,
                        "model": "flux1-dev fp8", "steps": 30, "guidance": 3.5, "sampler": "euler/normal",
                        "loras": [], "width": p["width"], "height": p["height"], "prompt": text,
                    }) + "\n")
                print(f"collected {dest.relative_to(PROJECT_ROOT)}")
    print(f"{copied} new file(s)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--wave", type=int)
    ap.add_argument("--piece", choices=list(PIECES), action="append")
    ap.add_argument("--seeds", type=int, default=3)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--queue-only", action="store_true", help="queue jobs and exit (the only queueing mode)")
    ap.add_argument("--collect", action="store_true")
    args = ap.parse_args()

    if args.collect:
        return collect_from_history()
    if not (args.queue_only or args.dry_run):
        ap.error("use --queue-only (then --collect later) or --dry-run")

    pieces = args.piece or [k for k, v in PIECES.items() if args.wave is None or v["wave"] == args.wave]
    rng = random.Random()
    for piece in pieces:
        p = PIECES[piece]
        for _ in range(args.seeds):
            seed = rng.randint(0, 2**32 - 1)
            wf, text = build_workflow(p["style"], p, seed, f"{PREFIX}{piece}_v{p.get('version', VERSION):02d}")
            if args.dry_run:
                print(f"--- {dest_for(piece, seed).name}\n{text}\n")
                continue
            pid = queue_prompt(wf)["prompt_id"]
            print(f"queued {dest_for(piece, seed).name} ({pid})", flush=True)
    if args.queue_only:
        print("run with --collect when ComfyUI's queue is empty")


if __name__ == "__main__":
    main()
