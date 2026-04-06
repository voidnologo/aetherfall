# Session 16: GM Tools — Zone Tracker & Combat Tracker

**Date:** 2026-04-06
**Goal:** Build interactive GM tools for the Adventure RPG web rulebook — Zone Tracker and Combat Tracker.

## Overview

Built two standalone browser-based GM tools and a Chapter 16 landing page linking to them. The Zone Tracker calculates live Reliability and Casting modifiers from the zone accumulation rules. The Combat Tracker provides a drag-and-drop timing track with a calendar-grid layout, footprint tokens for action history, and an infinite timeline. Both run entirely client-side with no server required.

---

## Changes Made

### Zone Tracker (`web/rules/tools/zone-tracker.html`)
- Baseline control (−30 to +30) with zone label display
- Spell cast buttons (Weak +1 through Spectacular +4)
- Galvanic weapon buttons (Rating 1-3 + Suppressing)
- Live effects panel: Reliability modifier, Casting modifier, example Revolver (95) and Caster (55) with calculated values
- Spectrum visualization bar with position marker
- Decay controls (1/5/10 min at 1 point per minute)
- Color-coded activity log

### Combat Tracker (`web/rules/tools/combat-tracker.html`)
- 10-column calendar grid layout (wrapping rows, not horizontal scroll)
- PC/NPC roster with color-coded tokens
- Drag-and-drop tokens to any count on the grid
- "Advance 1 Count" and "Next Action" (skips to next token) buttons
- Infinite timeline — auto-extends 30 counts ahead of current position
- Footprint tokens — dragging a token forward from a past/current count leaves a dimmed dashed ghost at the old position
- Unplaced token staging area
- Current count highlighted, past counts dimmed
- Scrollable history — scroll up to review past rows

### GM Tools Landing Page (`web/rules/gm-tools.html`)
- Chapter 16 in the rulebook, after Table Index
- Feature tables describing each tool
- Links to both tools
- "More Tools Coming" placeholder section

### Navigation
- Added GM Tools to PAGES array as Chapter 16
- Updated Table Index prev/next links to point to GM Tools

---

## Files Modified

| File | Change |
|------|--------|
| web/rules/tools/zone-tracker.html | NEW — Zone accumulation tracker |
| web/rules/tools/combat-tracker.html | NEW — Timing track combat tracker |
| web/rules/gm-tools.html | NEW — Chapter 16 landing page |
| web/rules/js/main.js | Added GM Tools to PAGES array |
| web/rules/tables.html | Next link → GM Tools |

## Key Design Decisions

- **Calendar grid over horizontal timeline.** 10 columns wrapping into rows, like a calendar. Each cell large enough to read token names. Horizontal timelines were too cramped at smaller screen sizes.
- **Footprints for action history.** When a token moves forward from a past count, a dimmed ghost remains. This lets the GM see who acted when without a separate log. Only triggers when moving forward from the past — repositioning within future counts doesn't leave footprints.
- **Infinite timeline.** No fixed ceiling. Always shows 30 counts ahead of current + 10 beyond the furthest token. Grid grows rows as needed.
- **All client-side.** No server, no login, no dependencies. Just HTML/CSS/JS in a single file per tool.
- **Zone formulas from the rules.** 2% per net balance point for both Reliability and Casting. Decay at 1 point per minute. All values derived from DESIGN_PHILOSOPHY.md and the World Between chapter.

## Open Issues

- Stretch goal: multiplayer sync via link code (WebRTC peer-to-peer?) — deferred, needs research
- Downloadable character sheet still pending
- Could add more tools: NPC generator, mission brief generator, Society generator

## Next Session
- Downloadable character sheet
- Visual polish and iteration based on feedback
