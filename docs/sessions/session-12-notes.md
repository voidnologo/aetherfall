# Session 12: GM Chapter Web Page — Navigation Integration

**Date:** 2026-04-06
**Goal:** Build web/rules/running-the-game.html from GM_CHAPTER.md design doc — chapter 11, neutral theme, update PAGES array and navigation links

## Overview

Created the Running the Game web page (Chapter 11) last session. This session completed the navigation integration: inserted the new chapter into the PAGES array, renumbered subsequent chapters, and updated all prev/next navigation links across affected pages.

---

## Changes Made

### Session 11 (prior context)
- Built `web/rules/running-the-game.html` from `docs/design/GM_CHAPTER.md`
- Full GM chapter covering: GM role, rulings philosophy, encounter design, pacing, NPCs, world-building, session zero, and quick-reference tables

### Session 12 (this session)
- Inserted `running` entry into PAGES array in `main.js` as Chapter 11
- Renumbered Quick Reference from Chapter 11 → 12, Table Index from Chapter 12 → 13
- Updated equipment.html next links → running-the-game.html
- Updated reference.html prev links → running-the-game.html, chapter numbers → 12
- Updated tables.html chapter numbers → 13

---

## Files Modified

| File | Change |
|------|--------|
| web/rules/js/main.js | Added running-the-game entry to PAGES, renumbered reference (12) and tables (13) |
| web/rules/equipment.html | Next links now point to running-the-game.html |
| web/rules/reference.html | Prev links now point to running-the-game.html, chapter number → 12 |
| web/rules/tables.html | Chapter number → 13 |

## Key Design Decisions

- Running the Game placed as Chapter 11 between Equipment (10) and Quick Reference (12) — GM-facing content after all player-facing rules, before appendices

## Open Issues

- None

## Next Session
