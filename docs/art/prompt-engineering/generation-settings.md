# Generation Settings

Model configurations and parameters for consistent pen & ink RPG illustration.

---

## Primary Recommendation: FLUX via ComfyUI

FLUX produces the best results for this style because natural language prompts
allow detailed description of pen technique, crosshatching, and decorative elements.

### Model Selection

| Priority | Model | Path | Use Case |
|----------|-------|------|----------|
| **1st** | `flux1-dev.safetensors` | `models/diffusion_models/` | FLUX Dev — primary generator, highest quality |
| 2nd | `flux1-schnell-fp8.safetensors` | `models/checkpoints/` | FLUX Schnell — fast iteration/testing |
| Alt | `JuggernautXL_Ragnarok.safetensors` | `models/checkpoints/` | SDXL — supports negative prompts, different aesthetic |
| Alt | `sd_xl_base_1.0.safetensors` | `models/checkpoints/` | SDXL base — stable fallback |
| Alt | `DreamShaper_8_pruned.safetensors` | `models/checkpoints/` | SD1.5 — lightweight, fast |

**ComfyUI root:** `/home/void/AI/ComfyUI/`

**Note:** flux1-dev lives in `models/diffusion_models/` (loaded via UNETLoader),
not `models/checkpoints/`. Schnell is in `models/checkpoints/` (loaded via
CheckpointLoaderSimple). Use dev for all final art; schnell for quick tests only.
Schnell uses CFG 1.0, 4-8 steps, `simple` scheduler (not the dev settings below).

### LoRA Stack (Style-Critical)

Apply these LoRAs to push FLUX toward pen & ink illustration.

**Installed — pen & ink stack** (in `/home/void/AI/ComfyUI/models/loras/`):

| LoRA | File | Size | Trigger | Strength | Role |
|------|------|------|---------|----------|------|
| **Engraving Style** | `engraving_style_pen_ink_flux.safetensors` | 585 MB | `engraving style` | 0.7-1.0 | Primary — Dore-inspired crosshatching, pen & ink linework |
| **Crosshatch Drawing** | `crosshatch_drawing_style_flux.safetensors` | 55 MB | `crosshatch drawing` | 0.7-1.0 | Hatching density, B&W push. Use `black and white drawing` |
| **Classic B&W Fantasy** | `classic_bw_fantasy_shadowdark_flux.safetensors` | 165 MB | (long, see notes) | 0.3-0.5 | Old-school tabletop RPG B&W art. Trained on Flux.1-dev |
| **Engrave (HF)** | `flux_engrave_hf.safetensors` | 86 MB | `NGRVNG, engrave` | TBD | Alternative engraving. Test against Civitai version |

**Trigger for Classic B&W Fantasy:** "This is a highly detailed black-and-white ink drawing.
The overall style is reminiscent of classic fantasy art with a focus on intricate line work
and detailed textures."

**Other installed** (lower relevance for pen & ink):

| LoRA | Size | Relevance |
|------|------|-----------|
| `nistyle_manga_sketch_flux.safetensors` | 19 MB | Partial — sketch quality, manga-leaning |
| `fantasy_impressions_flux.safetensors` | 321 MB | Partial — fantasy aesthetic, may push color |
| `dark_chiaroscuro_lighting_flux.safetensors` | 621 MB | Partial — contrast/shadow, tonal not B&W |
| `metal_gear_solid_chronoknight_flux.safetensors` | 37 MB | Low — wrong aesthetic |

**Recommended stacking strategy (test during Wave 1):**

| Variant | Stack | Notes |
|---------|-------|-------|
| A (baseline) | No LoRA | Pure flux-dev prompt-only baseline |
| B (engraving) | Engraving @ 0.8 | Test primary pen & ink LoRA solo |
| C (crosshatch) | Crosshatch @ 0.8 | Test crosshatch LoRA solo |
| D (RPG style) | Classic B&W @ 0.5 | Test RPG style LoRA solo |
| E (combo) | Engraving @ 0.7 + Crosshatch @ 0.5 | Expected best combo |
| F (full stack) | Engraving @ 0.6 + Crosshatch @ 0.4 + Classic B&W @ 0.3 | Triple stack, lower weights |

**Tuning notes:**
- If results have too much grey/softness, increase engraving LoRA strength
- If crosshatching looks mechanical/repetitive, decrease engraving, increase crosshatch
- If results drift toward color, add "monochrome, black and white only" to prompt
- Start with one LoRA at a time to evaluate individual contributions before stacking
- Crosshatch LoRA is potent even at low weights — start at 0.7 and adjust down

### FLUX Generation Parameters

**FLUX Schnell (primary):**

| Parameter | Value | Notes |
|-----------|-------|-------|
| **CFG Scale** | 1.0 | Schnell is guidance-distilled — higher CFG degrades output |
| **Steps** | 4-8 | Schnell converges fast; 8 for finals |
| **Sampler** | euler | Standard FLUX sampler |
| **Scheduler** | simple | Use `simple` for schnell (not `normal`) |
| **Seed** | Record every seed | For reproducibility |

**FLUX Dev (if installed):**

| Parameter | Value | Notes |
|-----------|-------|-------|
| **CFG Scale** | 3.0-3.5 | Standard FLUX dev range |
| **Steps** | 25-35 | More steps for higher quality |
| **Sampler** | euler | Standard FLUX sampler |
| **Scheduler** | normal | Standard FLUX scheduler |
| **Seed** | Record every seed | For reproducibility |

### Resolution by Art Type

| Art Type | Resolution | Aspect Ratio | Notes |
|----------|-----------|--------------|-------|
| Full-page plate | 1024 x 1408 | ~0.73:1 (portrait) | Upscale 2x for print |
| Half-page illustration | 1024 x 704 | ~1.45:1 (landscape) | Upscale 2x for print |
| Spot illustration | 768 x 768 | 1:1 (square) | Crop to subject |
| Character portrait | 832 x 1216 | ~0.68:1 (portrait) | Upscale 2x for print |
| Equipment study | 1024 x 1024 | 1:1 (square) | |
| Decorative border | 1408 x 320 | ~4.4:1 (wide) | Tile-friendly |
| Location vignette | 1024 x 704 | ~1.45:1 (landscape) | |
| Map element | 1024 x 1024 | 1:1 (square) | |

---

## Post-Processing Pipeline (Critical)

AI generators struggle with pure B&W pen & ink. Every piece requires post-processing:

### Step 1: Threshold Conversion
- Open in image editor (GIMP, Photoshop, etc.)
- Convert to greyscale
- Apply threshold (typically 128-160 — adjust per piece)
- Goal: pure black (#000) and pure white (#FFF) only

### Step 2: Contrast & Cleanup
- Boost contrast before thresholding if line quality is weak
- Remove generation artifacts (stray dots, smudges, border noise)
- Clean up any areas where thresholding created unwanted fills

### Step 3: Line Refinement
- Check crosshatching areas — threshold may close gaps between lines
- Check fine detail — stippling may vanish if threshold is too aggressive
- Manual touchup in key areas (faces, hands, focal details)

### Step 4: Upscaling (for print)
- Use a detail-preserving upscaler (Real-ESRGAN with lineart model, or Topaz)
- Upscale to 2x generation resolution for print-ready output
- Re-threshold after upscaling if grey values reappear

### Optional: ComfyUI Automation
Build a post-processing workflow node chain:
1. Output from generation → Greyscale conversion → Threshold node → Save
2. Parameter: threshold level (expose as widget for per-piece adjustment)

---

## IP-Adapter for Character Consistency

Once a character design is approved, use it as IP-Adapter reference for all
subsequent illustrations featuring that character.

### Setup
1. Generate and approve the character portrait
2. Use as IP-Adapter reference image for subsequent pieces
3. Use CLIP Vision for style matching across the full art set

### Consistency Chain
```
Approved Character Portrait
  ├── IP-Adapter reference for character appearances in plates/spots
  ├── CLIP Vision style reference for creature/location art
  └── Line weight and crosshatch density anchor for all art
```

---

## Batch Generation Strategy

### Phase 1: Style Lock-In

1. Generate 5-10 test pieces across different art types (1 portrait, 1 creature,
   1 equipment, 1 spot, 1 border)
2. Evaluate against style guide checklist
3. Tune LoRA strengths and prompt language
4. Run post-processing pipeline on each to verify B&W conversion quality
5. Establish the "golden reference set" — the approved pieces that define the standard

### Phase 2: Character & Creature Art

1. Character portraits for major character types (6-8 portraits)
2. Key creature illustrations (10-15 creatures)
3. Use IP-Adapter with approved portraits for consistency

### Phase 3: Locations & Equipment

1. Location vignettes for major zone types (dead zone, normal, light magic,
   wild zone, deep wild — 5-8 pieces)
2. Equipment studies for key weapon categories (sword, revolver, tommy gun,
   exotic arc gun, magical artifact — 8-12 pieces)

### Phase 4: Decorative Elements & Spots

1. Border templates (4-6 variations: Deco, Nouveau, blended, magic-themed, tech-themed)
2. Section dividers (3-4 variations)
3. Spot illustrations for rules concepts (15-25 pieces)
4. Drop cap alphabet (optional — 26 decorated initials)

### Phase 5: Full-Page Plates

1. Chapter opener plates (6-10 depending on chapter count)
2. These are the showcase pieces — allocate the most iteration time here

---

## Seed & Prompt Logging

**Critical for reproducibility.** For every generation, record:

| Field | Example |
|-------|---------|
| Piece name | Adventurer Portrait — Scholarly Caster |
| Art type | Character portrait |
| Model | flux_dev |
| LoRA stack | lineart:0.75, sketch:0.45, bw:0.35 |
| Seed | 847293651 |
| CFG | 3.5 |
| Steps | 30 |
| Resolution | 832 x 1216 |
| Full prompt | (paste complete prompt) |
| Post-processing | Threshold: 145, upscaled 2x, manual cleanup on hands |
| Accepted? | Yes / No (if no, note why) |
| File path | assets/generated/finals/characters/scholarly-caster.png |

Store in `docs/art/generation-log.md` (create when generation begins).
