# Continuation Prompt

## Last Session (24) — Eleventy Migration, Economy Integration & Unified Character Sheets
- Migrated entire rulebook to Eleventy: layout, shortcodes, 20 chapters converted, build-time sidebar
- Added Starting Station trade, Starting Backing rules, removed Downtime Actions
- Integrated economy into Creating, Societies, Equipment, GM chapters, and character builder
- Unified 6 character sheets into one template + JSON data files (4,065 lines eliminated)
- Builder has save/load JSON — same format as build-time character data

## Current State
- **Game title:** Aetherfall (repo: voidnologo/aetherfall)
- **Build:** Eleventy 3.x — `npm run dev` / `npm run build` — deploys via GitHub Action
- **Website:** 20 chapters (.njk) + 6 character sheets (from JSON + template) + interactive tools
- **Character data:** `web/_data/characters/*.json` — one file per character, build generates sheets
- **CRITICAL RULE:** Rulebook content must NEVER be changed without explicit user approval.
- **CRITICAL WORKFLOW:** Always persist design decisions in docs/requirements/ BEFORE writing rulebook content.
- **CRITICAL VOICE RULE:** Voice callouts are in-world people sharing experiences. Never rules commentary.
- **CRITICAL INTERNAL:** Spell Complexity is never exposed in the web rulebook.
- **Chapter registry:** `web/_data/pages.json` — single source of truth
- **Callout shortcodes:** handler, scholar, street, believer, gmnote, example, warning, scene
- **Not yet designed:** Zone formation, Push Timing, archetypes, bestiary, NPC stat blocks, corruption/madness

## Immediate Next Task
Visual review of site and character sheets. Then character sheet art/watermarks or design work.

## Key References
- `eleventy.config.js` — Build config, shortcodes, filters, passthrough
- `web/_data/pages.json` — Chapter registry
- `web/_data/characters/*.json` — Character data files
- `web/_includes/chapter.njk` — Chapter layout template
- `web/_includes/sheet.njk` — Character sheet template
- `docs/requirements/ECONOMY.md` — Economy design doc
- `docs/sessions/session-24-notes.md` — Full session record
