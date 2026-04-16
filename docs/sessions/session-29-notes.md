# Session 29: Art Generation Pipeline — Wave 1 Style Lock-In

**Date:** 2026-04-15
**Goal:** Build the art generation pipeline and run Wave 1 style lock-in tests across 5 art types with 4 LoRA variants

## Overview

Set up the full art generation pipeline from prompt to project. Located flux-dev model (was in `models/diffusion_models/`, not `models/checkpoints/` — docs said it wasn't installed but it was). Audited existing LoRAs (mostly anime/inkbrush — wrong for pen & ink), researched and downloaded 4 new LoRAs targeting engraving, crosshatching, and classic B&W RPG art. Built a Python tool (`tools/comfyui_generate.py`) that constructs ComfyUI API workflows, queues them, waits for completion, and auto-collects output into the project's `art/{type}/generated/` pipeline. Ran 20 test generations: 5 pieces x 4 LoRA variants (baseline, engraving, crosshatch, combo). The **combo preset** (engraving @ 0.7 + crosshatch @ 0.5) produces the best overall "RPG interior illustration" feel.

---

## Changes Made

### Art Pipeline Infrastructure
- Created art pipeline directories: `art/{characters,creatures,equipment,spots,decorative,locations,plates}/{generated,approved,archived}/`
- Built `tools/comfyui_generate.py` — full workflow generator with:
  - 5 Wave 1 piece definitions (Aldric portrait, Rift Stalker creature, weapons study, wild casting spot, section divider)
  - 7 LoRA presets (none, engraving, crosshatch, classic_bw, engrave_hf, combo, full_stack)
  - GPU cooling breaks (configurable: `--cool-every`, `--cool-secs`)
  - Auto-collection: waits for ComfyUI completion, copies output to `art/{type}/generated/`
  - Dry-run mode for workflow JSON export

### LoRA Downloads (4 new)
- `engraving_style_pen_ink_flux.safetensors` (585 MB) — Dore-inspired pen & ink
- `crosshatch_drawing_style_flux.safetensors` (55 MB) — crosshatch density + B&W
- `classic_bw_fantasy_shadowdark_flux.safetensors` (165 MB) — old-school tabletop RPG art
- `flux_engrave_hf.safetensors` (86 MB) — HuggingFace alternative engraving

### Documentation Updates
- Updated `docs/art/prompt-engineering/generation-settings.md`:
  - Fixed flux-dev as primary model with correct path
  - Documented all installed LoRAs with trigger words and strengths
  - Added 6-variant LoRA testing strategy table
- Created `docs/art/prompts/wave1-style-lockin.md` — 5 fully written prompts with evaluation criteria
- Created prompt directory structure: `docs/art/prompts/{characters,creatures,equipment,spots,decorative,locations,plates}/`

### Wave 1 Generation Run (20 images)
- 5 pieces x 4 LoRA variants (baseline, engraving, crosshatch, combo)
- All output in `art/{type}/generated/` awaiting review
- Combo preset (engraving 0.7 + crosshatch 0.5) identified as best overall

---

## Files Modified

| File | Change |
|------|--------|
| `docs/art/prompt-engineering/generation-settings.md` | Fixed flux-dev path, documented LoRA inventory and testing strategy |
| `docs/art/prompts/wave1-style-lockin.md` | New — 5 Wave 1 prompt definitions with evaluation criteria |
| `tools/comfyui_generate.py` | New — ComfyUI workflow generator, queue runner, auto-collector |
| `art/characters/generated/*.png` | 4 Aldric portraits (baseline, engraving, crosshatch, combo) |
| `art/creatures/generated/*.png` | 4 Rift Stalker illustrations |
| `art/equipment/generated/*.png` | 4 weapons studies |
| `art/spots/generated/*.png` | 5 wild casting spots |
| `art/decorative/generated/*.png` | 4 section dividers |
| `docs/sessions/session-29-notes.md` | This file |
| `docs/pending-tasks.md` | Updated with art pipeline tasks |
| `docs/continuation-prompt.md` | Updated for session 29 |

## Key Design Decisions

- **Combo LoRA preset as default:** Engraving @ 0.7 + Crosshatch @ 0.5 gives the best balance of pen & ink linework and hatching density. Baseline flux-dev gets 70% there on prompts alone; LoRAs push it to "printable RPG interior art."
- **Auto-collection into art pipeline:** The script copies output directly into `art/{type}/generated/` so the approval workflow (generated -> approved/archived) starts immediately. ComfyUI output dir is a staging area only.
- **GPU cooling breaks:** 60-second pauses every 15 jobs — the script drains the queue first so the GPU actually idles during the break.
- **flux-dev as primary, not schnell:** Dev at 30 steps produces significantly better results for detailed pen & ink work. Schnell is for quick iteration only.

## Open Issues

- Generated art has grey tones — needs post-processing threshold pipeline for pure B&W
- Weapons prompt needs rework — arc pistol doesn't look exotic enough vs revolver
- Character sheet content still flows over/under watermark bottom decorations
- Embossed "A" design still pending revisit
- Need to review all 20 Wave 1 images and select golden reference set

## Next Session

- Review Wave 1 art and select best variants per piece -> golden reference set
- Lock LoRA preset and begin Wave 2 (character portraits: Kael, Sera, Aldric, Mira + archetypes)
- Rework weapons prompt for better arc pistol differentiation
- Consider post-processing automation (threshold, contrast) in the pipeline script
