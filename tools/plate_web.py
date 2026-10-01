#!/usr/bin/env python3
"""Rebuild web plate copies (web/assets/art/plates/*.webp) from approved masters, applying the
crops and paint-outs recorded in tools/plate_manifest.json. Plates are never cut out."""

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "web" / "assets" / "art" / "plates"


def main():
    manifest = json.loads((ROOT / "tools" / "plate_manifest.json").read_text())
    OUT.mkdir(parents=True, exist_ok=True)
    for name, spec in manifest.items():
        if name.startswith("_"):
            continue
        src = ROOT / "art" / spec["master"]
        cmd = ["magick", str(src)]
        for x, y, w, h, sx, sy in spec.get("fill", []):
            colour = subprocess.run(["magick", str(src), "-format", f"%[pixel:p{{{sx},{sy}}}]", "info:"],
                                    capture_output=True, text=True, check=True).stdout.strip()
            cmd += ["-fill", colour, "-draw", f"rectangle {x},{y} {x + w},{y + h}"]
        if "crop" in spec:
            x, y, w, h = spec["crop"]
            cmd += ["-crop", f"{w}x{h}+{x}+{y}", "+repage"]
        cmd += ["-quality", "86", str(OUT / f"{name}.webp")]
        subprocess.run(cmd, check=True)
        print(f"{name}.webp")


if __name__ == "__main__":
    main()
