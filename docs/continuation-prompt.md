# Continuation Prompt

## Last Session (12) — GM Chapter Navigation Integration
- Built `web/rules/running-the-game.html` as Chapter 11 (neutral theme) from GM_CHAPTER.md design doc
- Inserted into PAGES array, renumbered Quick Reference → 12, Table Index → 13
- Updated all prev/next navigation links across equipment, reference, and tables pages
- Full GM chapter covers: GM role, rulings, encounter design, pacing, NPCs, world-building, session zero, quick-reference tables

## Current State
- **Website live:** 13-chapter rulebook with design system
- **CRITICAL RULE:** Rulebook content must NEVER be changed without explicit user approval. Layout/design only.
- **CRITICAL WORKFLOW:** Always persist design decisions in docs/requirements/ BEFORE writing rulebook content.
- **Complete (first pass):** Core mechanics, skills (27), progression/XP, magic system, spell compendium (37 spells), weapons, armor/soak, Galvanic oddities, vehicles, GM chapter (web + design doc)
- **Terminology:** "Galvanic rating" for device ratings. "Aetheric" for magic-side concepts. Propagation complete.
- **Not yet designed:** Factions/Societies, zone formation mechanics, Push Timing, archetypes, currency, bestiary, NPC stat blocks, corruption/madness

## Immediate Next Task
**Define major factions and their Adventuring Societies** — world-building pass to establish the organizations that drive play.

Then **visual polish and iteration on web rulebook based on feedback.**

## Key References
- `docs/requirements/GM_CHAPTER.md` — Full GM chapter design doc
- `web/rules/` — 13-page rules site
- `web/rules/running-the-game.html` — GM chapter (most recently added)
- `web/rules/css/styles.css` — Design system (callout-example, callout-note, callout-warning, callout-scene, flavor, section-divider)
- `web/rules/js/main.js` — Navigation, particles, scroll spy, PAGES array
- `docs/requirements/COMBAT_PROCEDURE.md` — Combat worked example for consistency
- `docs/requirements/WRITING_STYLE.md` — Player-facing writing style guide
- `docs/sessions/session-12-notes.md` — Full record of session 12 decisions
