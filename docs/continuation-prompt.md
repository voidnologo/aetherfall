# Continuation Prompt

## Last Session (26) — Rules Site Wordmark & Character Sheet Art Deco

- Sidebar wordmark integrated (replaced monogram), header kept monogram+text
- Fixed broken relative asset paths to absolute (`/assets/logo/...`)
- Generated proper favicon.ico (32x32) and apple-touch-icon.png (180x180)
- Renamed Ch01 "Welcome to the Age of Wonder" -> "Welcome to Aetherfall"
- Character sheets: art deco overhaul with Playfair Display + Cormorant Garamond fonts
- Wordmark at top of sheet page 1 (3in centered, CSS `filter: brightness(0)` for B&W)
- Fantasy.jpg watermark full-page (upscaled to 2400x3770, 6% opacity)
- Double-line art deco page borders, sharp geometric corners throughout

## Current State
- **Game title:** Aetherfall (repo: voidnologo/aetherfall)
- **Build:** Eleventy 3.x — `npm run dev` / `npm run build` — deploys via GitHub Action
- **Website:** 20 chapters (.njk) + 6 character sheets (from JSON + sheet.njk) + interactive tools
- **Art pipeline:** art/{type}/{generated|approved|archived}/ — art NEVER deleted, only moved
- **ComfyUI API:** flux1-dev via UNETLoader + DualCLIPLoader + VAELoader; schnell via CheckpointLoaderSimple
- **CRITICAL RULE:** Rulebook content must NEVER be changed without explicit user approval.
- **CRITICAL RULE:** Art is NEVER deleted. Moves through generated -> approved or generated -> archived.

## Immediate Next Tasks
- Continue iterating character sheet styling (text flow around watermark decorations)
- Review site and character sheets in browser for visual verification
- Character sheet art/watermarks further iteration
- Revisit embossed "A" design (clear left-organic/right-geometric split)

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
