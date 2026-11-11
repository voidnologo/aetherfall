#!/usr/bin/env python3
"""Rebuild web copies of full-bleed art (plates, scenes, covers, NPC portraits) from approved
masters, applying the crops and paint-outs recorded in tools/plate_manifest.json. Full-bleed art
is never cut out. Keys: "out" (folder under web/assets/art, default "plates"), "trim" (strip the
bone paper border Flux sometimes leaves), "fill", "crop"."""

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ART = ROOT / "web" / "assets" / "art"


def bone_border(src: Path) -> tuple[int, int, int, int, int, int]:
    """Image size and the width of the plain bone-paper border on each side: w, h, left, top, right, bottom."""
    w, h = (int(v) for v in subprocess.run(["magick", "identify", "-format", "%w %h", str(src)],
                                            capture_output=True, text=True, check=True).stdout.split())
    raw = subprocess.run(["magick", str(src), "-depth", "8", "rgb:-"], capture_output=True, check=True).stdout

    def bone(x, y):
        i = (y * w + x) * 3
        r, g, b = raw[i:i + 3]
        return r > 200 and g > 180 and b > 120

    def run(points):
        n = 0
        for x, y in points:
            if not bone(x, y):
                break
            n += 1
        return n

    rows, cols = (h // 4, h // 2, 3 * h // 4), (w // 4, w // 2, 3 * w // 4)
    left = max(run((x, y) for x in range(w // 3)) for y in rows)
    right = max(run((w - 1 - x, y) for x in range(w // 3)) for y in rows)
    top = max(run((x, y) for y in range(h // 3)) for x in cols)
    bottom = max(run((x, h - 1 - y) for y in range(h // 3)) for x in cols)
    return w, h, left, top, right, bottom


def main():
    manifest = json.loads((ROOT / "tools" / "plate_manifest.json").read_text())
    for name, spec in manifest.items():
        if name.startswith("_"):
            continue
        out = ART / spec.get("out", "plates")
        out.mkdir(parents=True, exist_ok=True)
        src = ROOT / "art" / spec["master"]
        cmd = ["magick", str(src)]
        for x, y, w, h, sx, sy in spec.get("fill", []):
            colour = subprocess.run(["magick", str(src), "-format", f"%[pixel:p{{{sx},{sy}}}]", "info:"],
                                    capture_output=True, text=True, check=True).stdout.strip()
            cmd += ["-fill", colour, "-draw", f"rectangle {x},{y} {x + w},{y + h}"]
        if "crop" in spec:
            x, y, w, h = spec["crop"]
            cmd += ["-crop", f"{w}x{h}+{x}+{y}", "+repage"]
        elif spec.get("trim"):
            w, h, l, t, r, b = bone_border(src)
            if l or t or r or b:  # shave a few px more so no pale anti-aliased rim survives
                l, t, r, b = (v + 4 if v else 0 for v in (l, t, r, b))
                cmd += ["-crop", f"{w - l - r}x{h - t - b}+{l}+{t}", "+repage"]
        cmd += ["-quality", "86", str(out / f"{name}.webp")]
        subprocess.run(cmd, check=True)
        print(f"{name}.webp")


if __name__ == "__main__":
    main()
