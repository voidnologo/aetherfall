#!/usr/bin/env python3
"""
Aetherfall Art Pipeline — ComfyUI Workflow Generator & Queue Runner

Builds flux-dev workflows for the Wave 1 style lock-in generation run
and queues them via the ComfyUI API.

Usage:
    python tools/comfyui_generate.py                    # Queue all Wave 1 pieces (baseline, no LoRA)
    python tools/comfyui_generate.py --piece aldric      # Queue one piece
    python tools/comfyui_generate.py --lora engraving    # Queue all with engraving LoRA
    python tools/comfyui_generate.py --lora combo        # Queue all with engraving + crosshatch
    python tools/comfyui_generate.py --list              # List available pieces and LoRA presets
    python tools/comfyui_generate.py --seed 12345        # Override seed
    python tools/comfyui_generate.py --cool-every 10     # GPU cooling break every N jobs (default: 15)
    python tools/comfyui_generate.py --cool-secs 90      # Cooling break duration (default: 60)
"""

import argparse
import json
import random
import shutil
import sys
import time
import urllib.request
from pathlib import Path

COMFYUI_URL = "http://127.0.0.1:8188"
COMFYUI_OUTPUT = Path("/home/void/AI/ComfyUI/output")
PROJECT_ROOT = Path(__file__).resolve().parent.parent
ART_DIR = PROJECT_ROOT / "art"

# ---------------------------------------------------------------------------
# Style prefix/suffix from docs/art/prompt-engineering/prompt-templates.md
# ---------------------------------------------------------------------------

STYLE_PREFIX = (
    "Black and white pen and ink illustration. Detailed crosshatching and fine "
    "linework drawn with a steel nib dip pen. Art Nouveau and Art Deco decorative "
    "influences. 1920s steampunk aesthetic. Pure black ink on white paper, no grey "
    "tones, no color. The style of classic fantasy RPG interior illustration "
    "crossed with Aubrey Beardsley's ornamental precision."
)

STYLE_SUFFIX = (
    "Rendered in pure black and white with confident penwork and crosshatching "
    "for shadow and volume. Clean linework with thick-to-thin variation. "
    "Decorative detail that rewards close inspection. White background. "
    "No color, no grey wash, no digital smoothness. Traditional pen and ink "
    "illustration technique. High contrast, crisp lines, printable at 300 DPI."
)

# ---------------------------------------------------------------------------
# Wave 1 piece definitions
# ---------------------------------------------------------------------------

PIECES = {
    "aldric": {
        "name": "Aldric Wynn — Scholarly Caster",
        "art_type": "characters",
        "width": 832,
        "height": 1216,
        "subject": (
            "A tall, thin man in his early forties, three-quarter body portrait. "
            "Wire-rimmed spectacles perched on a sharp nose, receding hairline, "
            "ink-stained fingers holding a leather-bound spellbook at his side. "
            "Precise, rigid posture of an academic. Wearing a tailored tweed "
            "overcoat with reinforced steel stays visible at the lapels, waistcoat "
            "beneath, pressed trousers, polished boots. A walking stick in one hand, "
            "a revolver holstered at the hip beneath the coat.\n\n"
            "Faint geometric patterns rendered in stippling hover near his free "
            "hand — controlled scholarly magic, precise and deliberate. His "
            "expression is analytical, slightly disapproving, the look of a man "
            "who catalogues everything he sees. A brass lantern and medical kit "
            "bag hang from his belt."
        ),
    },
    "rift_stalker": {
        "name": "Rift Stalker — Tear-Born Predator",
        "art_type": "creatures",
        "width": 1024,
        "height": 1408,
        "subject": (
            "A predatory supernatural creature crouched on a crumbling Art Deco "
            "rooftop ledge, silhouetted against empty white sky. The Rift Stalker "
            "is a lean, elongated humanoid form with too many joints, skin like "
            "cracked porcelain revealing dark energy beneath. Long multi-jointed "
            "fingers grip the stonework. Its face is a smooth featureless mask "
            "with a single vertical crack where eyes should be, leaking stippled "
            "aetheric energy. Vestigial wing-like protrusions of crystallized "
            "magic extend from its shoulder blades.\n\n"
            "A human figure visible far below on the street provides scale — the "
            "creature is eight feet tall even while crouching. The rooftop beneath "
            "it shows cracks spreading from where it perches, Art Deco geometric "
            "carvings dissolving into organic corruption where the creature touches "
            "stone.\n\n"
            "The creature conveys predatory intelligence and alien patience. It "
            "feels wrong — something that should not exist in a 1920s city, "
            "watching from above with inhuman stillness."
        ),
    },
    "weapons": {
        "name": "Revolver & Arc Pistol — Equipment Study",
        "art_type": "equipment",
        "width": 1024,
        "height": 1024,
        "subject": (
            "Two firearms displayed in a technical illustration arrangement on a "
            "white background, one above the other. The top weapon is a conventional "
            "1920s service revolver — blued steel, wooden grips worn smooth from use, "
            "six-shot cylinder, reliable and mundane. Detailed crosshatching shows "
            "the weight and cold metal of the barrel.\n\n"
            "The bottom weapon is an Arc Pistol — an exotic Galvanic weapon with a "
            "shorter, wider barrel housing a vacuum tube assembly. Brass fittings "
            "and copper wiring are visible along the receiver. A small aetheric "
            "crystal glows in a cage above the grip, powering the galvanic discharge. "
            "The design is 1920s industrial — not fantasy, but bleeding-edge technology "
            "that shouldn't quite work. Fine stippling around the crystal suggests "
            "contained energy.\n\n"
            "Both weapons rest on a flat surface, no hand holding them. The contrast "
            "between mundane reliability and exotic power is the visual story. Fine "
            "annotation lines in the style of a technical diagram point to key features."
        ),
    },
    "wild_casting": {
        "name": "Wild Casting — Spot Illustration",
        "art_type": "spots",
        "width": 768,
        "height": 768,
        "subject": (
            "A small, focused illustration of a woman's hands and forearms — wiry, "
            "ink-stained fingers spread wide as chaotic aetheric energy erupts between "
            "them. The energy is rendered as swirling organic Art Nouveau lines and "
            "stippled particles, flowing upward in sinuous curves that dissolve into "
            "geometric fragments. The sleeves of a frayed coat are pushed back to the "
            "elbows. Faint cracks in the skin of her hands leak stippled energy — the "
            "cost of wild casting made visible.\n\n"
            "Simple composition, strong silhouette, minimal background. The hands and "
            "the magic are the entire focus. Clean edges suitable for integration with "
            "body text on a printed page. Must read clearly at 2-3 inches wide."
        ),
    },
    "divider": {
        "name": "Art Deco/Nouveau Section Divider",
        "art_type": "decorative",
        "width": 1408,
        "height": 320,
        "subject": (
            "A horizontal decorative section divider combining Art Deco and Art Nouveau "
            "visual languages. The left side is geometric Art Deco — angular sunburst "
            "rays, stepped forms, interlocking precise lines, mechanical gear motifs "
            "rendered with architectural precision. The right side transitions into "
            "flowing Art Nouveau — sinuous organic curves, vine-like tendrils, flowing "
            "energy lines, natural forms. The two styles meet and intertwine at the "
            "center, neither winning — geometric lines sprouting organic growth, "
            "flowing curves crystallizing into angles.\n\n"
            "Symmetrical in weight if not in form. Clean lines, precise geometry where "
            "geometric, flowing curves where organic. Designed to work as a section "
            "break between chapters or major rules sections. Horizontal format, fills "
            "the width of a page."
        ),
    },
}

# ---------------------------------------------------------------------------
# LoRA presets
# ---------------------------------------------------------------------------

LORA_PRESETS = {
    "none": [],
    "engraving": [
        ("engraving_style_pen_ink_flux.safetensors", 0.8, "engraving style"),
    ],
    "crosshatch": [
        ("crosshatch_drawing_style_flux.safetensors", 0.8, "crosshatch drawing, black and white drawing"),
    ],
    "classic_bw": [
        ("classic_bw_fantasy_shadowdark_flux.safetensors", 0.5,
         "This is a highly detailed black-and-white ink drawing. The overall style is reminiscent of classic fantasy art with a focus on intricate line work and detailed textures."),
    ],
    "engrave_hf": [
        ("flux_engrave_hf.safetensors", 0.8, "NGRVNG, engrave"),
    ],
    "combo": [
        ("engraving_style_pen_ink_flux.safetensors", 0.7, "engraving style"),
        ("crosshatch_drawing_style_flux.safetensors", 0.5, "crosshatch drawing, black and white drawing"),
    ],
    "full_stack": [
        ("engraving_style_pen_ink_flux.safetensors", 0.6, "engraving style"),
        ("crosshatch_drawing_style_flux.safetensors", 0.4, "crosshatch drawing, black and white drawing"),
        ("classic_bw_fantasy_shadowdark_flux.safetensors", 0.3,
         "This is a highly detailed black-and-white ink drawing. The overall style is reminiscent of classic fantasy art with a focus on intricate line work and detailed textures."),
    ],
}

# ---------------------------------------------------------------------------
# Workflow builder
# ---------------------------------------------------------------------------


def build_workflow(piece_key: str, lora_preset: str = "none", seed: int | None = None) -> dict:
    """Build a ComfyUI API-format workflow for a given piece and LoRA preset."""
    piece = PIECES[piece_key]
    loras = LORA_PRESETS[lora_preset]
    if seed is None:
        seed = random.randint(0, 2**32 - 1)

    # Combine trigger words from LoRAs into the prompt
    trigger_parts = [l[2] for l in loras]
    trigger_text = ". ".join(trigger_parts)
    if trigger_text:
        prompt_text = f"{trigger_text}. {STYLE_PREFIX}\n\n{piece['subject']}\n\n{STYLE_SUFFIX}"
    else:
        prompt_text = f"{STYLE_PREFIX}\n\n{piece['subject']}\n\n{STYLE_SUFFIX}"

    # Filename prefix for output
    lora_tag = lora_preset if lora_preset != "none" else "baseline"
    prefix = f"aetherfall/{piece['art_type']}/{piece_key}_{lora_tag}_seed-{seed}"

    # Node IDs — start building the graph
    workflow = {}
    next_id = 1

    def nid():
        nonlocal next_id
        n = str(next_id)
        next_id += 1
        return n

    # 1. UNETLoader
    unet_id = nid()
    workflow[unet_id] = {
        "class_type": "UNETLoader",
        "inputs": {
            "unet_name": "flux1-dev.safetensors",
            "weight_dtype": "fp8_e4m3fn",
        },
    }

    # 2. Chain LoRA loaders if any
    model_source = [unet_id, 0]
    for lora_file, strength, _trigger in loras:
        lora_id = nid()
        workflow[lora_id] = {
            "class_type": "LoraLoaderModelOnly",
            "inputs": {
                "model": model_source,
                "lora_name": lora_file,
                "strength_model": strength,
            },
        }
        model_source = [lora_id, 0]

    # 3. DualCLIPLoader
    clip_id = nid()
    workflow[clip_id] = {
        "class_type": "DualCLIPLoader",
        "inputs": {
            "clip_name1": "clip_l.safetensors",
            "clip_name2": "t5xxl_fp16.safetensors",
            "type": "flux",
        },
    }

    # 4. CLIPTextEncode (positive)
    pos_id = nid()
    workflow[pos_id] = {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "text": prompt_text,
            "clip": [clip_id, 0],
        },
    }

    # 5. FluxGuidance
    guidance_id = nid()
    workflow[guidance_id] = {
        "class_type": "FluxGuidance",
        "inputs": {
            "conditioning": [pos_id, 0],
            "guidance": 3.5,
        },
    }

    # 6. Empty conditioning (negative — FLUX ignores but KSampler requires)
    neg_id = nid()
    workflow[neg_id] = {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "text": "",
            "clip": [clip_id, 0],
        },
    }

    # 7. VAELoader
    vae_id = nid()
    workflow[vae_id] = {
        "class_type": "VAELoader",
        "inputs": {
            "vae_name": "ae.safetensors",
        },
    }

    # 8. EmptyLatentImage
    latent_id = nid()
    workflow[latent_id] = {
        "class_type": "EmptyLatentImage",
        "inputs": {
            "width": piece["width"],
            "height": piece["height"],
            "batch_size": 1,
        },
    }

    # 9. KSampler
    sampler_id = nid()
    workflow[sampler_id] = {
        "class_type": "KSampler",
        "inputs": {
            "model": model_source,
            "seed": seed,
            "steps": 30,
            "cfg": 1.0,  # FLUX dev uses FluxGuidance, KSampler cfg=1.0
            "sampler_name": "euler",
            "scheduler": "normal",
            "positive": [guidance_id, 0],
            "negative": [neg_id, 0],
            "latent_image": [latent_id, 0],
            "denoise": 1.0,
        },
    }

    # 10. VAEDecode
    decode_id = nid()
    workflow[decode_id] = {
        "class_type": "VAEDecode",
        "inputs": {
            "samples": [sampler_id, 0],
            "vae": [vae_id, 0],
        },
    }

    # 11. SaveImage
    save_id = nid()
    workflow[save_id] = {
        "class_type": "SaveImage",
        "inputs": {
            "images": [decode_id, 0],
            "filename_prefix": prefix,
        },
    }

    return workflow, seed, prefix


def queue_prompt(workflow: dict) -> dict:
    """Submit a workflow to ComfyUI's /prompt endpoint."""
    payload = json.dumps({"prompt": workflow}).encode("utf-8")
    req = urllib.request.Request(
        f"{COMFYUI_URL}/prompt",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def get_queue_size() -> tuple[int, int]:
    """Return (running, pending) counts from ComfyUI queue."""
    try:
        req = urllib.request.Request(f"{COMFYUI_URL}/queue")
        with urllib.request.urlopen(req) as resp:
            d = json.loads(resp.read())
        return len(d.get("queue_running", [])), len(d.get("queue_pending", []))
    except Exception:
        return 0, 0


def wait_for_queue_drain(max_pending: int = 2, poll_interval: float = 5.0):
    """Block until the ComfyUI queue has at most max_pending jobs."""
    while True:
        running, pending = get_queue_size()
        if running + pending <= max_pending:
            return
        time.sleep(poll_interval)


def get_history(prompt_id: str) -> dict | None:
    """Fetch generation history for a specific prompt ID. Returns None if not done."""
    try:
        req = urllib.request.Request(f"{COMFYUI_URL}/history/{prompt_id}")
        with urllib.request.urlopen(req) as resp:
            d = json.loads(resp.read())
        return d.get(prompt_id)
    except Exception:
        return None


def wait_and_collect(prompt_id: str, art_type: str, poll_interval: float = 5.0) -> list[Path]:
    """Wait for a job to finish, then move its output into art/{type}/generated/."""
    while True:
        history = get_history(prompt_id)
        if history and history.get("outputs"):
            break
        time.sleep(poll_interval)

    moved = []
    for node_id, node_output in history.get("outputs", {}).items():
        for img in node_output.get("images", []):
            src = COMFYUI_OUTPUT / img["subfolder"] / img["filename"]
            if not src.exists():
                continue
            dest_dir = ART_DIR / art_type / "generated"
            dest_dir.mkdir(parents=True, exist_ok=True)
            dest = dest_dir / img["filename"]
            shutil.copy2(src, dest)
            moved.append(dest)
    return moved


def gpu_cooling_break(seconds: int, batch_num: int):
    """Pause to let the GPU cool down between batches."""
    print(f"\n  --- GPU cooling break ({seconds}s) after batch {batch_num} ---")
    # Wait for current queue to finish first so the GPU actually idles
    wait_for_queue_drain(max_pending=0, poll_interval=5.0)
    print(f"  Queue drained. Cooling for {seconds}s...", end="", flush=True)
    time.sleep(seconds)
    print(" done.\n")


def main():
    parser = argparse.ArgumentParser(description="Aetherfall ComfyUI art generator")
    parser.add_argument("--piece", choices=list(PIECES.keys()) + ["all"], default="all",
                        help="Which piece to generate (default: all)")
    parser.add_argument("--lora", choices=list(LORA_PRESETS.keys()), default="none",
                        help="LoRA preset to use (default: none/baseline)")
    parser.add_argument("--seed", type=int, default=None,
                        help="Override random seed (default: random)")
    parser.add_argument("--list", action="store_true",
                        help="List available pieces and LoRA presets")
    parser.add_argument("--dry-run", action="store_true",
                        help="Build workflows but don't queue (save to JSON instead)")
    parser.add_argument("--all-loras", action="store_true",
                        help="Generate each piece with every LoRA preset (full test matrix)")
    parser.add_argument("--cool-every", type=int, default=15,
                        help="GPU cooling break every N jobs (default: 15)")
    parser.add_argument("--cool-secs", type=int, default=60,
                        help="Cooling break duration in seconds (default: 60)")
    parser.add_argument("--no-cool", action="store_true",
                        help="Disable GPU cooling breaks entirely")
    args = parser.parse_args()

    if args.list:
        print("Available pieces:")
        for key, p in PIECES.items():
            print(f"  {key:20s} {p['name']:40s} ({p['width']}x{p['height']})")
        print("\nLoRA presets:")
        for key, loras in LORA_PRESETS.items():
            if loras:
                desc = " + ".join(f"{l[0].split('.')[0]}@{l[1]}" for l in loras)
            else:
                desc = "(no LoRA — baseline)"
            print(f"  {key:20s} {desc}")
        return

    pieces = list(PIECES.keys()) if args.piece == "all" else [args.piece]
    lora_presets = list(LORA_PRESETS.keys()) if args.all_loras else [args.lora]

    cool_every = args.cool_every
    cool_secs = args.cool_secs
    do_cooling = not args.no_cool

    queued = []
    batch_count = 0
    jobs_since_cool = 0

    for piece_key in pieces:
        for lora_key in lora_presets:
            # GPU cooling break check
            if do_cooling and jobs_since_cool >= cool_every and not args.dry_run:
                batch_count += 1
                gpu_cooling_break(cool_secs, batch_count)
                jobs_since_cool = 0

            workflow, seed, prefix = build_workflow(piece_key, lora_key, args.seed)

            if args.dry_run:
                out_dir = PROJECT_ROOT / "tools" / "workflows"
                out_dir.mkdir(exist_ok=True)
                out_file = out_dir / f"{piece_key}_{lora_key}.json"
                with open(out_file, "w") as f:
                    json.dump({"prompt": workflow}, f, indent=2)
                print(f"  Saved: {out_file}")
            else:
                try:
                    result = queue_prompt(workflow)
                    prompt_id = result.get("prompt_id", "unknown")
                    art_type = PIECES[piece_key]["art_type"]
                    queued.append((piece_key, lora_key, seed, prompt_id, art_type))
                    jobs_since_cool += 1
                    print(f"  Queued: {piece_key} [{lora_key}] seed={seed} -> {prompt_id}")
                except Exception as e:
                    print(f"  FAILED: {piece_key} [{lora_key}] -> {e}", file=sys.stderr)

    if queued:
        print(f"\n{len(queued)} jobs queued.")
        if do_cooling and len(queued) > cool_every:
            print(f"GPU cooling: {cool_secs}s break every {cool_every} jobs")
        print("Waiting for completion and collecting into art/*/generated/ ...")

        collected = []
        for i, (piece_key, lora_key, seed, prompt_id, art_type) in enumerate(queued, 1):
            moved = wait_and_collect(prompt_id, art_type)
            for p in moved:
                rel = p.relative_to(PROJECT_ROOT)
                print(f"  [{i}/{len(queued)}] {rel}")
                collected.append(p)

        print(f"\nDone. {len(collected)} images saved to art/*/generated/ for review.")
        print("To approve: move from generated/ to approved/")
        print("To reject:  move from generated/ to archived/")


if __name__ == "__main__":
    main()
