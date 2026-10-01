#!/usr/bin/env python3
"""
Aetherfall Art Pipeline — overnight block renderer (Session 37)

Queues Deco suite pieces into ComfyUI in blocks, waits for each block to finish,
files the results into art/ (deco_suite --collect), then rests the GPU before the
next block so a long unattended run doesn't cook the laptop.

Run it detached so Claude Code can't reap it:

    setsid nohup python tools/render_blocks.py --wave 4 --block 12 --rest 480 \\
        > /tmp/render_blocks.log 2>&1 &

    python tools/render_blocks.py --wave 4 --dry-run     # show the block plan only
"""

import argparse
import json
import random
import sys
import time
import urllib.request

from comfyui_generate import COMFYUI_URL, queue_prompt
from deco_suite import PIECES, PREFIX, VERSION, collect_from_history, dest_for
from prototype_styles import build_workflow

# Seeds per art type: cover candidates get an extra roll.
SEEDS = {"hero": 4}


def queue_depth() -> int:
    q = json.loads(urllib.request.urlopen(f"{COMFYUI_URL}/queue").read())
    return len(q["queue_running"]) + len(q["queue_pending"])


def log(msg: str):
    print(time.strftime("%H:%M:%S"), msg, flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--wave", type=int, required=True)
    ap.add_argument("--seeds", type=int, default=3)
    ap.add_argument("--block", type=int, default=12, help="images per block")
    ap.add_argument("--rest", type=int, default=480, help="seconds of GPU rest between blocks")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    rng = random.Random()
    jobs = []
    for piece, p in PIECES.items():
        if p["wave"] != args.wave:
            continue
        for _ in range(SEEDS.get(p["art_type"], args.seeds)):
            jobs.append((piece, rng.randint(0, 2**32 - 1)))
    blocks = [jobs[i:i + args.block] for i in range(0, len(jobs), args.block)]
    log(f"{len(jobs)} images in {len(blocks)} blocks of {args.block}, {args.rest}s rest between")
    if args.dry_run:
        for i, b in enumerate(blocks, 1):
            print(f"block {i}: " + ", ".join(sorted({piece for piece, _ in b})))
        return

    for i, block in enumerate(blocks, 1):
        while queue_depth():          # never pile onto someone else's queue
            time.sleep(30)
        for piece, seed in block:
            p = PIECES[piece]
            wf, _ = build_workflow(p["style"], p, seed, f"{PREFIX}{piece}_v{p.get('version', VERSION):02d}")
            queue_prompt(wf)
        log(f"block {i}/{len(blocks)} queued: {len(block)} images")
        while queue_depth():
            time.sleep(30)
        collect_from_history()
        log(f"block {i}/{len(blocks)} done")
        if i < len(blocks):
            time.sleep(args.rest)
    log("all blocks done")


if __name__ == "__main__":
    sys.exit(main())
