# Continuation Prompt

## Last Session (24) — Eleventy Migration, Economy Rules & Integration
- Migrated entire web rulebook to Eleventy: layout template, pages.json data file, 9 callout shortcodes, all 20 chapters converted to .njk
- Added Starting Station trade (±3 skill levels per ±1 Station) and Starting Backing rules (default 3) to design doc and rulebook
- Removed Downtime Actions (rejected — Drift pressure is the point)
- Integrated economy into Creating (new Station step), Societies (Backing + Ledger), Character Sheet, Equipment chapters
- Updated character builder with Station, Backing, and Ledger dropdowns (defaulted, adjustable)

## Current State
- **Game title:** Aetherfall (repo: voidnologo/aetherfall)
- **Build system:** Eleventy 3.x — source in `web/`, output to `_site/`, deployed via GitHub Action
- **Website:** 20-chapter rulebook (all .njk templates) + Character Sheet page + interactive tools
- **Dev:** `npm run dev` for local server, `npm run build` for production build
- **CRITICAL RULE:** Rulebook content must NEVER be changed without explicit user approval.
- **CRITICAL WORKFLOW:** Always persist design decisions in docs/requirements/ BEFORE writing rulebook content.
- **CRITICAL VOICE RULE:** Voice callouts are in-world people sharing experiences. Never rules commentary. GM notes handle rules perspective.
- **CRITICAL INTERNAL:** Spell Complexity is essential in design docs but NEVER exposed in the web rulebook.
- **Chapter registry:** `web/_data/pages.json` is the single source of truth for chapter order, numbers, themes. Also duplicated in `web/rules/js/main.js` PAGES const (for sidebar TOC — Phase 3 cleanup pending).
- **Callout shortcodes:** handler, scholar, street, believer, gmnote, example, warning, scene
- **Chapter flow:** Welcome → State of the World → Societies → Creating → Character Sheet → Rolling → Getting Hurt → Skills → Magic → Grimoire → World Between → Combat → Coin & Commerce → Arms & Equipment → Artifacts & Enchantments → Running the Game → Quick Reference → Table Index → GM Tools → The Ashwick Job (QS)
- **Not yet designed:** Zone formation mechanics, Push Timing, archetypes, bestiary, NPC stat blocks, corruption/madness

## Immediate Next Task
Review site in browser for visual regression after 11ty conversion. Then add Station/Backing/Ledger to blank printable sheet. Phase 3 cleanup.

## Key References
- `eleventy.config.js` — Build config, shortcodes, filters, passthrough
- `web/_data/pages.json` — Chapter registry (single source of truth)
- `web/_includes/chapter.njk` — Layout template for all chapters
- `docs/requirements/ECONOMY.md` — Full economy design doc with research and system
- `web/rules/economy.njk` — Coin & Commerce web chapter
- `web/rules/tools/character-builder.html` — Interactive builder with Station/Backing/Ledger
- `docs/requirements/WRITING_STYLE.md` — Voice conventions, voice vs GM note distinction
- `docs/sessions/session-24-notes.md` — Full record of session 24
