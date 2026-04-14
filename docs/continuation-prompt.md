# Continuation Prompt

## Last Session (25) — Logo & Art Generation, Landing Page Integration
- Generated logo art via ComfyUI API: wordmark, monogram "A", hero cover (text-free), emboss attempts (archived)
- Wordmark, monogram, hero approved and upscaled to 4K WebP
- Integrated art into landing page: hero image as full background, transparent wordmark as title, dark text with cyan glow
- Added monogram to rules site header and sidebar, favicon on both pages
- Set up art pipeline: art/{type}/{generated|approved|archived}/, generation-log.md
- Created CLAUDE.md with art-never-deleted rule
- Scaled landing page base font to 20px for readability

## Current State
- **Game title:** Aetherfall (repo: voidnologo/aetherfall)
- **Build:** Eleventy 3.x — `npm run dev` / `npm run build` — deploys via GitHub Action
- **Website:** 20 chapters (.njk) + 6 character sheets (from JSON + sheet.njk) + interactive tools
- **Art pipeline:** art/{type}/{generated|approved|archived}/ — art NEVER deleted, only moved
- **ComfyUI API:** flux1-dev via UNETLoader + DualCLIPLoader + VAELoader; schnell via CheckpointLoaderSimple
- **CRITICAL RULE:** Rulebook content must NEVER be changed without explicit user approval.
- **CRITICAL RULE:** Art is NEVER deleted. Moves through generated -> approved or generated -> archived.

## Immediate Next Task
**Update logo/wordmark in the rules portion of the site.** The landing page is done; the rules site header and sidebar have the monogram but need the full wordmark treatment and readability pass to match.

## Key Art Assets
- `web/assets/logo/wordmark.webp` — 4K transparent wordmark (4096x2048)
- `web/assets/logo/monogram.webp` — 4K monogram "A" (3072x3072)
- `web/assets/hero.webp` — 4K hero scene, no text (3328x4864)

## Color Reference
- **Aether:** `#3dc8e0` | **Galvanic:** `#e8a825` | **Background:** `#080b14`
- **Fonts:** Playfair Display (headings), Source Serif 4 (body), Cormorant Garamond (labels)
