#!/usr/bin/env python3
"""
Aetherfall Art Pipeline — Style Direction Prototypes (Session 34)

Runs the same four subjects through each shortlisted art direction with shared
seeds, so the directions can be compared like-for-like. See
docs/art/art-direction-proposals.md for the directions themselves.

Usage:
    python tools/prototype_styles.py                       # all directions, all subjects
    python tools/prototype_styles.py --direction B         # one direction
    python tools/prototype_styles.py --subject portrait    # one subject
    python tools/prototype_styles.py --seeds 2             # seeds per subject (default 2)
    python tools/prototype_styles.py --dry-run             # print prompts, queue nothing
"""

import argparse
import json
import random
import re
import shutil
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comfyui_generate import (  # noqa: E402
    ART_DIR, COMFYUI_OUTPUT, LORA_PRESETS, PROJECT_ROOT, get_history, queue_prompt,
)

LOG_PATH = PROJECT_ROOT / "docs" / "art" / "prototype-runs.jsonl"

# ---------------------------------------------------------------------------
# Directions — prefix/suffix frame the subject; LoRAs push the medium
# ---------------------------------------------------------------------------

DIRECTIONS = {
    "A": {
        "slug": "engraver",
        "name": "A — The Engraver's Folio",
        "loras": LORA_PRESETS["combo"],
        "prefix": (
            "Black and white pen and ink illustration in the manner of a 1920s book "
            "engraving. Steel-nib dip pen linework, fine crosshatching and stippling for "
            "tone, the ornamental precision of Harry Clarke and Aubrey Beardsley, the "
            "drama of Gustave Dore. Art Nouveau whiplash curves for anything magical, Art "
            "Deco stepped geometry for anything industrial. Pure black ink on white paper."
        ),
        "suffix": (
            "Pure black and white only: no grey wash, no color, no digital smoothness. "
            "Confident thick-to-thin line weight, crisp high contrast, printable at 300 DPI. "
            "No text, no lettering, no signature."
        ),
    },
    "B": {
        "slug": "twoinks",
        "name": "B — Two Inks",
        "loras": [("engraving_style_pen_ink_flux.safetensors", 0.45, "engraving style")],
        "prefix": (
            "A two-color print from the 1920s: black ink linework and crosshatching on "
            "warm off-white paper, plus exactly two flat spot inks. Everything ordinary — "
            "people, brick, iron, cloth, steel blades — is printed in black ink only. "
            "Magical energy, luminous crystals and anything supernatural glow in a single "
            "flat turquoise-cyan ink. Electric arc light, galvanic machinery glow and "
            "sparks are printed in a single flat amber-gold ink. The spot colors are flat, "
            "slightly misregistered like a real letterpress print, never shaded."
        ),
        "suffix": (
            "Strict palette: black, off-white paper, turquoise-cyan, amber-gold. No other "
            "colors, no gradients, no photographic lighting. Crisp ink linework, pochoir "
            "stencil color. No text, no lettering, no signature."
        ),
    },
    "D": {
        "slug": "decolitho",
        "name": "D — Deco Lithograph",
        "loras": [],
        "prefix": (
            "A 1920s Art Deco travel poster lithograph in the style of Cassandre and "
            "WPA railway posters. Flat color shapes, bold geometric simplification, "
            "strong diagonals, stylized light rays, subtle lithographic grain. Limited "
            "palette: midnight navy, bone ivory, soot black, turquoise-cyan for magic, "
            "amber-gold for electric light, a touch of oxblood red."
        ),
        "suffix": (
            "Flat printed color with crisp edges and a slight paper grain. No "
            "photorealism, no 3D rendering, no gradients beyond simple banding. "
            "No text, no lettering, no title, no signature."
        ),
    },
    "D2": {
        "slug": "decolitho",
        "name": "D (round 2) — Deco Lithograph, locked palette",
        "loras": [],
        "prefix": (
            "A 1920s Art Deco travel poster lithograph in the style of Cassandre and "
            "WPA railway posters. Flat printed color shapes, bold geometric "
            "simplification, strong diagonals, stylized light drawn as hard-edged rays "
            "and pools, subtle lithographic paper grain. Strict limited palette of six "
            "inks: deep midnight navy, warm bone ivory, soot black, turquoise cyan, "
            "amber gold, and oxblood red. Turquoise cyan is used ONLY for magical light, "
            "glowing crystals and supernatural energy. Amber gold is used ONLY for "
            "electric arc lamps, galvanic machinery glow and sparks, and warm lamplight. "
            "Everything ordinary is midnight navy, bone, soot black and oxblood."
        ),
        "suffix": (
            "Flat printed color with crisp edges and a slight paper grain. No "
            "photorealism, no 3D rendering, no airbrushed gradients. Absolutely no "
            "text, no lettering, no title, no caption, no signature, no logo."
        ),
    },
}

# ---------------------------------------------------------------------------
# Subjects — identical across directions
# ---------------------------------------------------------------------------

SUBJECTS = {
    "header": {
        "name": "Chapter header band — Harrier Street at sundown",
        "art_type": "decorative",
        "width": 1664,
        "height": 448,
        "subject": (
            "A wide panoramic chapter-header illustration of Harrier Street at sundown, a "
            "single long cobbled avenue in a small 1920s industrial town. On the left side, "
            "soot-stained brick factories, riveted iron, cold smokestacks and tall electric "
            "arc lamps glowing along the street. On the right side, a crooked medieval old "
            "town with ivy swallowing the facades, gas lamps, and thin luminous crystals "
            "growing from the stonework. In the middle of the street a lone figure in a "
            "long coat and hat walks between the two lights. Composed as a horizontal "
            "banner with a quiet empty band of sky across the top for a chapter title."
        ),
    },
    "frame": {
        "name": "Chapter opener frame — empty centre",
        "art_type": "decorative",
        "width": 832,
        "height": 1216,
        "subject": (
            "An ornamental full-page border frame for the opening page of a book chapter. "
            "The centre of the page is completely empty blank paper for text. The border "
            "is split between two design languages: the left and top edges are flowing Art "
            "Nouveau — curling vines, ivy leaves, slender luminous crystals and whiplash "
            "curves; the right and bottom edges are precise Art Deco — stepped geometry, "
            "sunburst rays, rivets, brass coils and lightning-bolt zigzags. The two styles "
            "meet in the top-right and bottom-left corners where vines wrap around metal. "
            "Symmetrical in weight, elegant, restrained."
        ),
    },
    "spot": {
        "name": "Spot illustration — the balance tips",
        "art_type": "spots",
        "width": 1024,
        "height": 1024,
        "subject": (
            "A slight, wiry young woman of twenty-three with pale skin and jagged "
            "jaw-length black hair, wearing an oversized layered coat and a brass compass "
            "on a cord around her neck, flings one hand forward as she casts a spell: the "
            "air in front of her palm bends and ripples with raw magical force, and her "
            "eyes glow faintly. Beside her in a narrow alley, a man's hand holds a revolver "
            "that sputters and misfires, a small spark and puff of smoke at the cylinder. "
            "Simple composition, strong silhouettes, minimal background, clean edges so "
            "the illustration can sit beside printed text."
        ),
    },
    "portrait": {
        "name": "Portrait — Kael Dunn, The Steady Hand",
        "art_type": "characters",
        "width": 832,
        "height": 1216,
        "subject": (
            "Three-quarter-length character portrait of Kael Dunn, a forty-two-year-old "
            "former city constable turned adventurer. Brown skin, weathered face, "
            "short-cropped dark hair going grey at the temples, a thin old scar across the "
            "bridge of his nose, steady brown eyes that give nothing away. Broad-shouldered "
            "and lean, average height, standing easy but alert. A leather jacket repaired "
            "many times, dark trousers with too many pockets, good boots. A revolver in a "
            "hip holster worn soft with use, the handle of a hunting knife at the small of "
            "his back. Behind him a hint of a dim tavern doorway and a gas lamp. 1920s "
            "working-class noir, not steampunk."
        ),
    },
    # ── Round 2 (Direction D locked): character locks, theme frames, watermark ──
    "kael": {
        "name": "Portrait — the Steady Hand (canon lock)",
        "art_type": "characters",
        "width": 832, "height": 1216,
        "subject": (
            "Three-quarter-length portrait of a brown-skinned man of forty-two with a "
            "weathered dark-brown complexion, short-cropped black hair going grey at "
            "the temples, and a thin pale scar across the bridge of his nose. Steady, "
            "guarded brown eyes. Broad-shouldered and lean, average height, standing easy "
            "but alert under a gas lamp at a tavern doorway at night. A battered brown "
            "leather jacket repaired many times, dark work trousers, good boots. A "
            "revolver in a worn hip holster and the handle of a hunting knife at the "
            "small of his back. 1920s working-class noir former city constable."
        ),
    },
    "sera": {
        "name": "Portrait — the Spark (canon lock)",
        "art_type": "characters",
        "width": 832, "height": 1216,
        "subject": (
            "Three-quarter-length portrait of a slight, wiry pale-skinned young woman of "
            "twenty-three with sharp features and jagged, self-cut black hair at jaw "
            "length. Her dark eyes are ringed with a thin pale turquoise halo. Layers of "
            "oversized clothes: a heavy canvas coat over a sweater, frayed cuffs, heavy "
            "boots, a small brass compass on a cord around her neck. One hand is raised "
            "and faint turquoise magical light curls between her fingers. Behind her, an "
            "ivy-covered cobbled lane with thin glowing turquoise crystals in the stones."
        ),
    },
    "aldric": {
        "name": "Portrait — the Surgeon (canon lock)",
        "art_type": "characters",
        "width": 832, "height": 1216,
        "subject": (
            "Three-quarter-length portrait of a tall, gaunt, slightly stooped man of "
            "thirty-four with light brown skin, high cheekbones, close-cropped dark hair "
            "and round wire spectacles. A neat waistcoat with many small pockets, pressed "
            "shirt, a practical long coat, a leather satchel with a thick book strapped "
            "to it, a plain wooden walking stick. He holds a small flat rectangle of "
            "turquoise geometric light above one open palm, precise and controlled. "
            "Behind him, tall library shelves in a converted mill."
        ),
    },
    "mira": {
        "name": "Portrait — the Fixer (canon lock)",
        "art_type": "characters",
        "width": 832, "height": 1216,
        "subject": (
            "Three-quarter-length portrait of a brown-skinned woman of twenty-eight with "
            "warm dark eyes, short-cropped dark hair and a thin scar on her left "
            "cheekbone, a knowing half-smile. Medium height, athletic. A sharp tailored "
            "coat over a waistcoat, gloves, a silver cigarette case in one hand. A small "
            "brass-and-copper pistol with a glowing amber coil in a shoulder holster "
            "half-hidden by the coat. Behind her, a street where amber arc lamps glow on "
            "one side and turquoise-lit ivy on the other."
        ),
    },
    "frame_aether": {
        "name": "Chapter frame — Aether theme",
        "art_type": "decorative",
        "width": 832, "height": 1216,
        "subject": (
            "An ornamental full-page border frame for a book chapter opening, the centre "
            "left completely empty as a plain bone-colored panel for text. The border is "
            "Art Nouveau: whiplash ivy vines, slender glowing turquoise crystal spires, "
            "flowing smoke curls, a pointed arch at the top. Symmetrical and elegant."
        ),
    },
    "frame_galvanic": {
        "name": "Chapter frame — Galvanic theme",
        "art_type": "decorative",
        "width": 832, "height": 1216,
        "subject": (
            "An ornamental full-page border frame for a book chapter opening, the centre "
            "left completely empty as a plain bone-colored panel for text. The border is "
            "Art Deco industrial: stepped arch, amber sunburst rays at the top, riveted "
            "iron pilasters, fluted columns, zigzag lightning bolts, brass coils. "
            "Symmetrical and monumental."
        ),
    },
    "frame_split": {
        "name": "Chapter frame — split theme",
        "art_type": "decorative",
        "width": 832, "height": 1216,
        "subject": (
            "An ornamental full-page border frame for a book chapter opening, the centre "
            "left completely empty as a plain bone-colored panel for text. The left half "
            "of the border is Art Nouveau ivy and glowing turquoise crystals; the right "
            "half is Art Deco riveted iron, fluting and amber sunburst rays. They meet at "
            "the keystone of the arch at top centre, balanced, neither winning."
        ),
    },
    "frame_neutral": {
        "name": "Chapter frame — neutral theme",
        "art_type": "decorative",
        "width": 832, "height": 1216,
        "subject": (
            "An ornamental full-page border frame for a book chapter opening, the centre "
            "left completely empty as a plain bone-colored panel for text. A restrained "
            "Art Deco border in midnight navy and oxblood: stepped corners, thin parallel "
            "lines, a small compass rose medallion at the top. Quiet and elegant."
        ),
    },
    "watermark": {
        "name": "Character sheet watermark emblem",
        "art_type": "decorative",
        "width": 1024, "height": 1024,
        "subject": (
            "A single circular Art Deco emblem medallion centred on a plain bone "
            "background, like a stamped seal on a document. The left half of the "
            "medallion is Art Nouveau ivy and turquoise crystal; the right half is Art "
            "Deco amber sunburst rays and rivets. A plain keystone shape sits at the "
            "centre where the halves meet. Simple, bold, readable when printed very "
            "faintly behind text. Nothing outside the circle."
        ),
    },
}


def build_workflow(direction: dict, subject: dict, seed: int, prefix: str) -> dict:
    """Flux-dev graph: UNET → LoRA chain → Flux guidance → KSampler → SaveImage."""
    triggers = ". ".join(l[2] for l in direction["loras"])
    text = f"{direction['prefix']}\n\n{subject['subject']}\n\n{direction['suffix']}"
    if triggers:
        text = f"{triggers}. {text}"

    wf = {
        "1": {"class_type": "UNETLoader",
              "inputs": {"unet_name": "flux1-dev.safetensors", "weight_dtype": "fp8_e4m3fn"}},
        "2": {"class_type": "DualCLIPLoader",
              "inputs": {"clip_name1": "clip_l.safetensors", "clip_name2": "t5xxl_fp16.safetensors",
                         "type": "flux"}},
        "3": {"class_type": "VAELoader", "inputs": {"vae_name": "ae.safetensors"}},
    }
    model = ["1", 0]
    for i, (lora_file, strength, _trigger) in enumerate(direction["loras"]):
        node = f"L{i}"
        wf[node] = {"class_type": "LoraLoaderModelOnly",
                    "inputs": {"model": model, "lora_name": lora_file, "strength_model": strength}}
        model = [node, 0]

    wf.update({
        "4": {"class_type": "CLIPTextEncode", "inputs": {"text": text, "clip": ["2", 0]}},
        "5": {"class_type": "FluxGuidance", "inputs": {"conditioning": ["4", 0], "guidance": 3.5}},
        "6": {"class_type": "CLIPTextEncode", "inputs": {"text": "", "clip": ["2", 0]}},
        "7": {"class_type": "EmptyLatentImage",
              "inputs": {"width": subject["width"], "height": subject["height"], "batch_size": 1}},
        "8": {"class_type": "KSampler",
              "inputs": {"model": model, "seed": seed, "steps": 30, "cfg": 1.0,
                         "sampler_name": "euler", "scheduler": "normal",
                         "positive": ["5", 0], "negative": ["6", 0],
                         "latent_image": ["7", 0], "denoise": 1.0}},
        "9": {"class_type": "VAEDecode", "inputs": {"samples": ["8", 0], "vae": ["3", 0]}},
        "10": {"class_type": "SaveImage", "inputs": {"images": ["9", 0], "filename_prefix": prefix}},
    })
    return wf, text


def collect(prompt_id: str, dest: Path, poll: float = 5.0) -> Path | None:
    """Wait for a job, then copy its single output image to dest."""
    while True:
        hist = get_history(prompt_id)
        if hist and hist.get("outputs"):
            break
        if hist and hist.get("status", {}).get("status_str") == "error":
            return None
        time.sleep(poll)
    for out in hist["outputs"].values():
        for img in out.get("images", []):
            src = COMFYUI_OUTPUT / img["subfolder"] / img["filename"]
            if src.exists():
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dest)
                return dest
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--direction", choices=list(DIRECTIONS), action="append")
    ap.add_argument("--subject", choices=list(SUBJECTS), action="append")
    ap.add_argument("--seeds", type=int, default=2)
    ap.add_argument("--seed", type=int, action="append", help="explicit seed(s); overrides --seeds")
    ap.add_argument("--version", type=int, default=1, help="vNN in the output filename")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--queue-only", action="store_true", help="queue jobs and exit; run --collect later")
    ap.add_argument("--collect", action="store_true", help="copy finished outputs from ComfyUI history into art/")
    args = ap.parse_args()

    if args.collect:
        return collect_from_history()

    directions = args.direction or list(DIRECTIONS)
    subjects = args.subject or list(SUBJECTS)
    rng = random.Random()
    # Shared seeds per subject so every direction gets the same starting noise
    seeds = {s: (args.seed or [rng.randint(0, 2**32 - 1) for _ in range(args.seeds)]) for s in subjects}

    jobs = []
    for subj_key in subjects:
        subject = SUBJECTS[subj_key]
        for seed in seeds[subj_key]:
            for dkey in directions:
                d = DIRECTIONS[dkey]
                desc = f"proto-{dkey}-{d['slug']}_{subj_key}"
                version = 2 if dkey == "D2" else args.version
                fname = f"{desc}_v{version:02d}_seed-{seed}.png"
                wf, text = build_workflow(d, subject, seed, f"aetherfall/proto/{desc}")
                dest = ART_DIR / subject["art_type"] / "generated" / fname
                if args.dry_run:
                    print(f"--- {fname}\n{text}\n")
                    continue
                pid = queue_prompt(wf)["prompt_id"]
                jobs.append((pid, dest, dkey, subj_key, seed, text))
                print(f"queued {fname}", flush=True)

    if args.queue_only:
        print(f"{len(jobs)} jobs queued; run with --collect when ComfyUI's queue is empty")
        return

    for pid, dest, dkey, subj_key, seed, text in jobs:
        got = collect(pid, dest)
        status = "ok" if got else "FAILED"
        print(f"[{status}] {dest.relative_to(PROJECT_ROOT)}", flush=True)
        with LOG_PATH.open("a") as f:
            f.write(json.dumps({
                "time": time.strftime("%Y-%m-%d %H:%M:%S"), "file": str(dest.relative_to(PROJECT_ROOT)),
                "status": status, "direction": dkey, "subject": subj_key, "seed": seed,
                "model": "flux1-dev fp8", "steps": 30, "guidance": 3.5, "sampler": "euler/normal",
                "loras": [[l[0], l[1]] for l in DIRECTIONS[dkey]["loras"]],
                "width": SUBJECTS[subj_key]["width"], "height": SUBJECTS[subj_key]["height"],
                "prompt": text,
            }) + "\n")


def collect_from_history():
    """Copy every finished aetherfall/proto job in ComfyUI's history into art/, logging new ones."""
    import urllib.request
    from comfyui_generate import COMFYUI_URL
    hist = json.loads(urllib.request.urlopen(f"{COMFYUI_URL}/history?max_items=500").read())
    copied = 0
    for h in hist.values():
        prompt = h["prompt"][2]
        save = next((v for v in prompt.values() if v["class_type"] == "SaveImage"), None)
        if not save or not save["inputs"]["filename_prefix"].startswith("aetherfall/proto/"):
            continue
        desc = save["inputs"]["filename_prefix"].split("/")[-1]
        m = re.match(r"proto-(\w+?)-[a-z]+_(\w+)$", desc)
        if not m or m.group(2) not in SUBJECTS:
            continue
        dkey, subj_key = m.groups()
        seed = next(v for v in prompt.values() if v["class_type"] == "KSampler")["inputs"]["seed"]
        version = 2 if dkey == "D2" else 1
        for out in h.get("outputs", {}).values():
            for img in out.get("images", []):
                src = COMFYUI_OUTPUT / img["subfolder"] / img["filename"]
                dest = ART_DIR / SUBJECTS[subj_key]["art_type"] / "generated" / f"{desc}_v{version:02d}_seed-{seed}.png"
                if not src.exists() or dest.exists():
                    continue
                shutil.copy2(src, dest)
                copied += 1
                text = next(v for v in prompt.values() if v["class_type"] == "CLIPTextEncode" and v["inputs"]["text"])["inputs"]["text"]
                with LOG_PATH.open("a") as f:
                    f.write(json.dumps({
                        "time": time.strftime("%Y-%m-%d %H:%M:%S"), "file": str(dest.relative_to(PROJECT_ROOT)),
                        "status": "ok", "direction": dkey, "subject": subj_key, "seed": seed,
                        "model": "flux1-dev fp8", "steps": 30, "guidance": 3.5, "sampler": "euler/normal",
                        "loras": [[l[0], l[1]] for l in DIRECTIONS[dkey]["loras"]],
                        "width": SUBJECTS[subj_key]["width"], "height": SUBJECTS[subj_key]["height"],
                        "prompt": text,
                    }) + "\n")
                print(f"collected {dest.relative_to(PROJECT_ROOT)}")
    print(f"{copied} new file(s)")


if __name__ == "__main__":
    main()
