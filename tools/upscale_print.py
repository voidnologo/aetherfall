#!/usr/bin/env python3
"""
Aetherfall Art Pipeline — Print Upscale (Session 35)

Upscales approved art 4x for print through ComfyUI (RealESRGAN_x4plus_anime_6B,
which keeps the Deco Lithograph's flat fields and crisp edges clean). Masters in
art/{type}/approved/ are never touched; print copies go to art/{type}/print/ as
{stem}_x4.png. An 832x1216 plate becomes 3328x4864: over 300 DPI on a letter page.

ComfyUI holds ~19 GB of RAM and idle waiters get reaped, so queue and collect
are separate steps. Jobs join the back of ComfyUI's queue.

    python tools/upscale_print.py --queue-only        # every approved PNG not yet upscaled
    python tools/upscale_print.py --collect           # file finished jobs into art/*/print/
    python tools/upscale_print.py --dry-run
"""

import argparse
import json
import shutil
import urllib.request

from comfyui_generate import ART_DIR, COMFYUI_OUTPUT, COMFYUI_URL, PROJECT_ROOT, queue_prompt

COMFYUI_INPUT = COMFYUI_OUTPUT.parent / "input"
MODEL = "RealESRGAN_x4plus_anime_6B.pth"
PREFIX = "aetherfall/print/"
# Files whose point is their alpha channel; the upscaler would flatten it
SKIP = {"wordmark_v01_transparent.png"}


def sources():
    for src in sorted(ART_DIR.glob("*/approved/*.png")):
        if src.name in SKIP:
            continue
        dest = src.parent.parent / "print" / f"{src.stem}_x4.png"
        yield src, dest


def workflow(image: str, stem: str) -> dict:
    return {
        "1": {"class_type": "LoadImage", "inputs": {"image": image}},
        "2": {"class_type": "UpscaleModelLoader", "inputs": {"model_name": MODEL}},
        "3": {"class_type": "ImageUpscaleWithModel", "inputs": {"upscale_model": ["2", 0], "image": ["1", 0]}},
        "4": {"class_type": "SaveImage", "inputs": {"images": ["3", 0], "filename_prefix": f"{PREFIX}{stem}"}},
    }


def collect():
    hist = json.loads(urllib.request.urlopen(f"{COMFYUI_URL}/history?max_items=1000").read())
    wanted = {src.stem: dest for src, dest in sources()}
    copied = 0
    for h in hist.values():
        save = next((v for v in h["prompt"][2].values() if v["class_type"] == "SaveImage"), None)
        if not save or not save["inputs"]["filename_prefix"].startswith(PREFIX):
            continue
        stem = save["inputs"]["filename_prefix"][len(PREFIX):]
        dest = wanted.get(stem)
        if not dest or dest.exists():
            continue
        for out in h.get("outputs", {}).values():
            for img in out.get("images", []):
                src = COMFYUI_OUTPUT / img["subfolder"] / img["filename"]
                if src.exists():
                    dest.parent.mkdir(exist_ok=True)
                    shutil.copy2(src, dest)
                    copied += 1
                    print(f"collected {dest.relative_to(PROJECT_ROOT)}")
    print(f"{copied} new file(s)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--queue-only", action="store_true")
    ap.add_argument("--collect", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if args.collect:
        return collect()
    if not (args.queue_only or args.dry_run):
        ap.error("use --queue-only (then --collect later) or --dry-run")

    (COMFYUI_INPUT / "aetherfall_print").mkdir(exist_ok=True)
    n = 0
    for src, dest in sources():
        if dest.exists():
            continue
        n += 1
        if args.dry_run:
            print(f"{src.relative_to(PROJECT_ROOT)} -> {dest.relative_to(PROJECT_ROOT)}")
            continue
        shutil.copy2(src, COMFYUI_INPUT / "aetherfall_print" / src.name)
        queue_prompt(workflow(f"aetherfall_print/{src.name}", src.stem))
    print(f"{n} upscale job(s) {'to queue' if args.dry_run else 'queued'}")


if __name__ == "__main__":
    main()
