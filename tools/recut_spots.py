#!/usr/bin/env python3
"""
Re-cut every web spot from its approved master (tools/spot_manifest.json), clipped to the
vignette's circle. Run through uv:

    uv run --with pillow --with numpy --with scipy tools/recut_spots.py [name ...] [--preview-dir DIR]
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = json.loads((ROOT / "tools" / "spot_manifest.json").read_text())

ap = argparse.ArgumentParser()
ap.add_argument("names", nargs="*")
ap.add_argument("--preview-dir")
args = ap.parse_args()
for name, spec in MANIFEST.items():
    if name.startswith("_") or (args.names and name not in args.names):
        continue
    cmd = [sys.executable, str(ROOT / "tools" / "cutout.py"), str(ROOT / "art" / "spots" / "approved" / spec["master"]),
           "--out-dir", str(ROOT / "web" / "assets" / "art" / "spots"), "--name", name, "--circle", "--width", "800",
           *spec.get("flags", [])]
    if args.preview_dir:
        cmd += ["--preview-dir", args.preview_dir]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
    print("recut", name)
