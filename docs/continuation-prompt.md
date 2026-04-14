# Continuation Prompt

## Last Session (24) — Eleventy Migration, Economy, Unified Sheets, Builder Dedup
- Migrated entire rulebook to Eleventy: layout, shortcodes, 20 chapters, build-time sidebar
- Added Starting Station trade, Starting Backing, removed Downtime Actions
- Integrated economy into Creating, Societies, Equipment, GM chapters, character builder
- Unified 6 character sheets into one template (sheet.njk) + JSON data files
- Builder prints via shared template (sessionStorage handoff) — zero duplication
- Save/load JSON in builder — same format as build-time character data
- Phase 3 complete: PAGES duplication eliminated, sidebar build-time, main.js simplified
- Created art direction doc with logo design brief

## Current State
- **Game title:** Aetherfall (repo: voidnologo/aetherfall)
- **Build:** Eleventy 3.x — `npm run dev` / `npm run build` — deploys via GitHub Action
- **Website:** 20 chapters (.njk) + 6 character sheets (from JSON + sheet.njk) + interactive tools
- **Character data:** `web/_data/characters/*.json` — one file per character, build generates sheets
- **Builder:** Save/Load JSON + Print (delegates to sheet template via sessionStorage)
- **CRITICAL RULE:** Rulebook content must NEVER be changed without explicit user approval.
- **CRITICAL WORKFLOW:** Always persist design decisions in docs/requirements/ BEFORE writing rulebook content.
- **CRITICAL VOICE RULE:** Voice callouts are in-world people sharing experiences. Never rules commentary.
- **CRITICAL INTERNAL:** Spell Complexity is never exposed in the web rulebook.
- **Chapter registry:** `web/_data/pages.json` — single source of truth
- **Not yet designed:** Zone formation, Push Timing, archetypes, bestiary, NPC stat blocks, corruption/madness

## Immediate Next Task
**Logo design.** Full brief at `docs/requirements/ART_DIRECTION.md` — covers the duality (Aether cyan #3dc8e0 vs. Galvanic amber #e8a825), Art Deco + arcane aesthetic, four exploration directions, deliverable specs. User will use their art generator on another computer.

After logo: character sheet watermarks, then design work (bestiary, archetypes, zones).

## Key References
- `docs/requirements/ART_DIRECTION.md` — Logo brief, visual identity, prompt engineering notes
- `eleventy.config.js` — Build config, shortcodes, filters, passthrough
- `web/_data/pages.json` — Chapter registry
- `web/_data/characters/*.json` — Character data files
- `web/_includes/chapter.njk` — Chapter layout template
- `web/_includes/sheet.njk` — Character sheet template (single renderer for all sheets)
- `docs/requirements/ECONOMY.md` — Economy design doc
- `docs/sessions/session-24-notes.md` — Full session record

## Color Reference (for art work)
- **Aether:** `#3dc8e0` (cyan/teal — magic, mystery, cool)
- **Galvanic:** `#e8a825` (amber/gold — technology, industry, warm)
- **Background:** `#080b14` (deep void black)
- **Text bright:** `#eef0f5`
- **Text dim:** `#8a92a4`
- **Warning:** `#c45c3e`
- **Fonts:** Playfair Display (headings), Source Serif 4 (body), Cormorant Garamond (labels)
