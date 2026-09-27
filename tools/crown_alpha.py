#!/usr/bin/env python3
"""
Aetherfall Art Pipeline — Web Chapter Crowns with Alpha (Session 35)

The approved theme frames sit on a faint bone margin. The old web crowns trimmed
that margin off with a rectangular crop, which cut the ivy leaves and points flat.
This clears the margin to transparent instead: a flood from the top and side
edges through bone-colored pixels, limited to an outer band, so anything drawn
over the margin (leaves, the compass point) keeps its full shape.

Usage (needs Pillow + NumPy + SciPy; run through uv):
    uv run --with pillow --with numpy --with scipy tools/crown_alpha.py            # all four
    uv run --with pillow --with numpy --with scipy tools/crown_alpha.py --theme split --preview /tmp/p.png
"""

import argparse
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

PROJECT_ROOT = Path(__file__).resolve().parent.parent
APPROVED = PROJECT_ROOT / "art" / "decorative" / "approved"
WEB_FRAMES = PROJECT_ROOT / "web" / "assets" / "art" / "frames"

FRAMES = {
    "aether": "proto-D2-decolitho_frame_aether_v02_seed-131618214.png",
    "galvanic": "proto-D2-decolitho_frame_galvanic_v02_seed-1166265576.png",
    "split": "proto-D2-decolitho_frame_split_v02_seed-2427297017.png",
    "neutral": "proto-D2-decolitho_frame_neutral_v02_seed-1553240695.png",
}

CROWN_H = 430           # rows of the 832x1216 frame used for the crown
BAND = 48               # the margin flood never reaches further than this from an edge
BONE = np.array([249, 234, 185])
TOLERANCE = 38          # RGB distance from BONE that still counts as margin
PAGE_BG = (11, 14, 23)  # --bg-deep, for previews


def margin_alpha(rgb: np.ndarray) -> np.ndarray:
    h, w, _ = rgb.shape
    bone = np.linalg.norm(rgb - BONE, axis=2) < TOLERANCE
    yy, xx = np.mgrid[:h, :w]
    band = (yy < BAND) | (xx < BAND) | (xx >= w - BAND)
    candidate = bone & band
    labels, _ = ndimage.label(candidate)
    edge = np.unique(np.concatenate([labels[0], labels[:, 0], labels[:, -1]]))
    margin = np.isin(labels, edge[edge > 0])
    margin = ndimage.binary_dilation(margin, iterations=1) & band   # eat the anti-aliased fringe
    alpha = ndimage.gaussian_filter((~margin).astype(float), 0.8)
    return alpha


def build(theme: str, preview: Path | None = None) -> Path:
    rgb = np.asarray(Image.open(APPROVED / FRAMES[theme]).convert("RGB"), dtype=float)[:CROWN_H]
    alpha = margin_alpha(rgb)
    img = Image.fromarray(np.dstack([rgb, alpha * 255]).clip(0, 255).astype(np.uint8), "RGBA")
    # Trim fully transparent rows/columns so the crown's box hugs the art
    img = img.crop(img.getchannel("A").point(lambda a: 255 if a > 8 else 0).getbbox())
    out = WEB_FRAMES / f"{theme}-crown.webp"
    img.save(out, "WEBP", quality=88, alpha_quality=90, method=6)
    print(f"wrote {out.relative_to(PROJECT_ROOT)} ({img.width}x{img.height})")
    if preview:
        bg = Image.new("RGBA", img.size, PAGE_BG + (255,))
        Image.alpha_composite(bg, img).convert("RGB").save(preview)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--theme", choices=list(FRAMES), action="append")
    ap.add_argument("--preview", type=Path, help="preview path (single theme only)")
    args = ap.parse_args()
    for theme in args.theme or list(FRAMES):
        build(theme, args.preview if args.theme and len(args.theme) == 1 else None)


if __name__ == "__main__":
    main()
