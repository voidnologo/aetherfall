# Continuation Prompt

## Last Session (29) — Art Generation Pipeline, Wave 1 Style Lock-In

- Built `tools/comfyui_generate.py` — ComfyUI workflow generator with LoRA presets, GPU cooling, and auto-collection into `art/{type}/generated/`
- Downloaded 4 new LoRAs for pen & ink style: engraving, crosshatch, classic B&W fantasy, engrave (HF)
- Ran 20 test generations: 5 pieces x 4 LoRA variants (baseline, engraving, crosshatch, combo)
- **Combo preset** (engraving @ 0.7 + crosshatch @ 0.5) identified as best overall
- Created `tools/art_sync.py` for S3 push/pull of art assets; updated .gitignore to exclude art binaries
- Art binaries now gitignored; synced via S3 instead (bucket not yet created)

## Current State
- **Game title:** Aetherfall (repo: voidnologo/aetherfall)
- **Build:** Eleventy 3.x — `npm run dev` / `npm run build` — deploys via GitHub Action with `--pathprefix=/aetherfall/`
- **Website:** 18 chapters + quickstart (.njk) + character sheets (from JSON + sheet.njk) + interactive tools
- **Art pipeline:** `art/{type}/{generated|approved|archived}/` — art NEVER deleted, only moved
- **Art generation:** `python tools/comfyui_generate.py` — builds flux-dev workflows, queues via ComfyUI API
- **Art sync:** `python tools/art_sync.py push/pull/status` — S3 sync (bucket TBD)
- **ComfyUI:** `/home/void/AI/ComfyUI/` — flux-dev in `models/diffusion_models/`, schnell in `models/checkpoints/`
- **Founding event:** "The Tear" (was "the Eruption" — renamed session 27)
- **CRITICAL RULE:** Rulebook content must NEVER be changed without explicit user approval.
- **CRITICAL RULE:** Art is NEVER deleted. Moves through generated -> approved or generated -> archived.

## Immediate Next Tasks
- Review 20 Wave 1 images and select golden reference set
- Lock LoRA preset, begin Wave 2 character portraits
- Rework weapons prompt for better arc pistol differentiation
- Set up S3 bucket and initial art push

## Key Art Assets
- `web/assets/logo/wordmark.webp` — 4K transparent wordmark (4096x2048)
- `web/assets/logo/monogram.webp` — 4K monogram "A" (3072x3072)
- `web/assets/hero.webp` — 4K hero scene, no text (3328x4864)
- `web/assets/logo/favicon.ico` — 32x32 monogram favicon
- `web/assets/logo/apple-touch-icon.png` — 180x180 monogram touch icon
- `web/assets/art/fantasy.jpg` — upscaled fantasy watermark (2400x3770)

## Color Reference
- **Aether:** `#3dc8e0` | **Galvanic:** `#e8a825` | **Background:** `#080b14`
- **Fonts:** Playfair Display (headings), Source Serif 4 (body), Cormorant Garamond (labels)
