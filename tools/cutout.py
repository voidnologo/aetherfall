#!/usr/bin/env python3
"""
Aetherfall Art Pipeline — Cut-out (Session 35)

Keys the flat bone paper field of a Deco suite piece (tools/deco_suite.py) to
alpha: a flood from all four edges through bone-colored pixels, so bone that
is enclosed by the art (a drop-cap tile's centre panel, a window) stays opaque.
Then trims to the art with a small pad and writes a WEBP with alpha.

Usage (needs Pillow + NumPy + SciPy; run through uv):
    uv run --with pillow --with numpy --with scipy tools/cutout.py SRC.png [SRC2.png ...] \
        --out-dir web/assets/art/ornaments [--width 800] [--preview-dir DIR]
"""

import argparse
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

PAD = 8
PREVIEW_BGS = {"night": (11, 14, 23), "paper": (239, 230, 210)}


def bone_reference(rgb: np.ndarray) -> np.ndarray:
    """The paper color, sampled from the outermost ring of pixels."""
    ring = np.concatenate([rgb[:4].reshape(-1, 3), rgb[-4:].reshape(-1, 3),
                           rgb[:, :4].reshape(-1, 3), rgb[:, -4:].reshape(-1, 3)])
    return np.median(ring, axis=0)


def drop_strays(fg: np.ndarray, reach: float = 0.06, main_only: bool = False) -> np.ndarray:
    """Remove small marks well outside the main art: Flux's fake signatures and paper flecks.
    main_only keeps just the substantial shapes, wherever they are (for compact motifs)."""
    labels, n = ndimage.label(fg)
    if n < 2:
        return fg
    sizes = ndimage.sum(fg, labels, range(1, n + 1))
    if main_only:
        keep = np.concatenate([[False], sizes > 0.05 * sizes.max()])
        return keep[labels]
    main = ndimage.find_objects((labels == int(np.argmax(sizes)) + 1).astype(int))[0]
    h, w = fg.shape
    pad_y, pad_x = int(h * reach), int(w * reach)
    y0, y1 = max(main[0].start - pad_y, 0), min(main[0].stop + pad_y, h)
    x0, x1 = max(main[1].start - pad_x, 0), min(main[1].stop + pad_x, w)
    keep = np.zeros(n + 1, bool)
    for i, sl in enumerate(ndimage.find_objects(labels), 1):
        cy, cx = (sl[0].start + sl[0].stop) / 2, (sl[1].start + sl[1].stop) / 2
        keep[i] = sizes[i - 1] > 0.02 * sizes.max() or (y0 <= cy < y1 and x0 <= cx < x1)
    return keep[labels]


def hull_fill(fg: np.ndarray) -> np.ndarray:
    """Everything inside the convex outline of the art counts as art. For round or oval
    vignettes whose pale light (a crack, a beam) reaches the edge and would otherwise
    be keyed out with the paper."""
    from PIL import ImageDraw
    from scipy.spatial import ConvexHull
    ys, xs = np.nonzero(fg)
    pts = np.column_stack([xs, ys])
    hull = pts[ConvexHull(pts).vertices]
    mask = Image.new("L", (fg.shape[1], fg.shape[0]), 0)
    ImageDraw.Draw(mask).polygon([tuple(p) for p in hull], fill=255)
    return np.asarray(mask) > 0


def cutout(img: Image.Image, tolerance: float = 48, main_only: bool = False, hull: bool = False) -> Image.Image:
    rgb = np.asarray(img.convert("RGB"), dtype=float)
    paper = np.linalg.norm(rgb - bone_reference(rgb), axis=2) < tolerance
    labels, _ = ndimage.label(paper)
    edge = np.unique(np.concatenate([labels[0], labels[-1], labels[:, 0], labels[:, -1]]))
    bg = np.isin(labels, edge[edge > 0])
    bg = ndimage.binary_dilation(bg, iterations=2)                    # eat the anti-aliased fringe
    fg = ndimage.binary_opening(~bg, iterations=1)                    # drop lone specks of grain
    fg = drop_strays(fg, main_only=main_only)
    if hull:
        fg = hull_fill(fg)
    alpha = ndimage.gaussian_filter(fg.astype(float), 0.8)
    out = Image.fromarray(np.dstack([rgb, alpha * 255]).clip(0, 255).astype(np.uint8), "RGBA")
    box = out.getchannel("A").point(lambda a: 255 if a > 16 else 0).getbbox()
    if box:
        l, t, r, b = box
        out = out.crop((max(l - PAD, 0), max(t - PAD, 0), min(r + PAD, out.width), min(b + PAD, out.height)))
    return out


MIDNIGHT = np.array([14, 26, 43])
BONE = np.array([239, 230, 210])


def navy_to_bone(img: Image.Image, reach: float = 70) -> Image.Image:
    """Web-only recolour: midnight-navy ink becomes bone so it reads on the dark page.
    Pixels blend toward bone by how close they are to midnight; print copies keep navy."""
    a = np.asarray(img, dtype=float)
    rgb, alpha = a[..., :3], a[..., 3:]
    dist = np.linalg.norm(rgb - MIDNIGHT, axis=2, keepdims=True)
    w = np.clip(1 - dist / reach, 0, 1)
    rgb = rgb * (1 - w) + BONE * w
    return Image.fromarray(np.concatenate([rgb, alpha], axis=2).clip(0, 255).astype(np.uint8), "RGBA")


CYAN = np.array([61, 200, 224])
CYAN_CORE = np.array([200, 244, 250])


def light_to_cyan(img: Image.Image) -> Image.Image:
    """Recolour pale, low-saturation light (bone or white glow) to Aether cyan, keeping its
    brightness: the core goes pale cyan, the edges full cyan. For Aether light that Flux
    painted bone-white. Run after the cut-out so the paper itself is already gone."""
    a = np.asarray(img, dtype=float)
    rgb, alpha = a[..., :3], a[..., 3:]
    hi, lo = rgb.max(axis=2, keepdims=True), rgb.min(axis=2, keepdims=True)
    sat = (hi - lo) / np.maximum(hi, 1)
    light = hi / 255
    w = np.clip((light - 0.55) / 0.25, 0, 1) * np.clip((0.45 - sat) / 0.2, 0, 1)
    target = CYAN + (CYAN_CORE - CYAN) * np.clip((light - 0.75) / 0.2, 0, 1)
    rgb = rgb * (1 - w) + target * w
    return Image.fromarray(np.concatenate([rgb, alpha], axis=2).clip(0, 255).astype(np.uint8), "RGBA")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("src", type=Path, nargs="+")
    ap.add_argument("--out-dir", type=Path, required=True)
    ap.add_argument("--name", help="output stem (single source only); default: the source stem")
    ap.add_argument("--width", type=int, help="resize the cut-out to this width")
    ap.add_argument("--tolerance", type=float, default=48)
    ap.add_argument("--hull", action="store_true", help="keep everything inside the art's convex outline (round vignettes)")
    ap.add_argument("--main-only", action="store_true", help="keep only the substantial shapes (drops thin stray marks)")
    ap.add_argument("--light-to-cyan", action="store_true", help="recolour pale bone/white light to Aether cyan")
    ap.add_argument("--navy-to-bone", action="store_true", help="web copy: recolour midnight-navy ink to bone")
    ap.add_argument("--preview-dir", type=Path, help="also write previews on the night and paper backgrounds")
    args = ap.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    for src in args.src:
        img = cutout(Image.open(src), args.tolerance, args.main_only, args.hull)
        if args.light_to_cyan:
            img = light_to_cyan(img)
        if args.navy_to_bone:
            img = navy_to_bone(img)
        if args.width and img.width > args.width:
            img = img.resize((args.width, round(img.height * args.width / img.width)), Image.LANCZOS)
        stem = args.name if args.name and len(args.src) == 1 else src.stem
        out = args.out_dir / f"{stem}.webp"
        img.save(out, "WEBP", quality=88, alpha_quality=90, method=6)
        print(f"wrote {out} ({img.width}x{img.height})")
        if args.preview_dir:
            args.preview_dir.mkdir(parents=True, exist_ok=True)
            for name, color in PREVIEW_BGS.items():
                bg = Image.new("RGBA", img.size, color + (255,))
                Image.alpha_composite(bg, img).convert("RGB").save(args.preview_dir / f"{src.stem}_{name}.jpg", quality=85)


if __name__ == "__main__":
    main()
