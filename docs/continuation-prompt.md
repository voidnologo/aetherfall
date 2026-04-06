# Continuation Prompt

## Last Session (11) — Galvanic Rating Propagation & GM Chapter Design
- Completed "Aetheric rating" → "Galvanic rating" rename across all remaining pages and design docs (6 files)
- Designed full GM chapter as docs/requirements/GM_CHAPTER.md (650+ lines)
- New mechanics introduced: stat-based quick checks `(5+stat)×10`, NPC dispositions (−30% to +30%), chase structure on timing track, location baseline table (12 entries)
- Four worked examples with full math: social encounter, foot chase, zone exploration, improvised device

## Current State
- **Website live:** 12-chapter rulebook with design system
- **CRITICAL RULE:** Rulebook content must NEVER be changed without explicit user approval. Layout/design only.
- **CRITICAL WORKFLOW:** Always persist design decisions in docs/requirements/ BEFORE writing rulebook content.
- **Complete (first pass):** Core mechanics, skills (27), progression/XP, magic system, spell compendium (37 spells), weapons, armor/soak, Galvanic oddities, vehicles, GM chapter design doc
- **Terminology:** "Galvanic rating" is correct for device ratings. "Aetheric" describes magic-side concepts (accumulation, zones, balance). Propagation complete.
- **Not yet designed:** Factions/Societies, zone formation mechanics, Push Timing, archetypes, currency, bestiary, NPC stat blocks, corruption/madness

## Immediate Next Task
**Build the GM chapter web page** — translate GM_CHAPTER.md into web/rules/running-the-game.html. This requires:
1. Create running-the-game.html (chapter 11, `data-theme="neutral"`)
2. Update web/rules/js/main.js PAGES array — insert `{ id: 'running', file: 'running-the-game.html', title: 'Running the Game', num: '11', theme: 'neutral' }`, renumber reference→12, tables→13
3. Update web/rules/equipment.html — next link → running-the-game.html
4. Update web/rules/reference.html — chapter 11→12, prev link → running-the-game.html
5. Update web/rules/tables.html — chapter 12→13
6. Follow HTML template pattern from equipment.html (most recent chapter added)

Then **define major factions and Adventuring Societies.**

## Key References
- `docs/requirements/GM_CHAPTER.md` — Full GM chapter design doc (source for web page)
- `web/rules/` — 12-page rules site
- `web/rules/equipment.html` — Template for new pages (most recently added chapter)
- `web/rules/css/styles.css` — Design system (callout-example, callout-note, callout-warning, callout-scene, flavor, section-divider)
- `web/rules/js/main.js` — Navigation, particles, scroll spy, PAGES array
- `docs/requirements/COMBAT_PROCEDURE.md` — Combat worked example for consistency
- `docs/requirements/WRITING_STYLE.md` — Player-facing writing style guide
- `docs/sessions/session-11-notes.md` — Full record of session 11 decisions
