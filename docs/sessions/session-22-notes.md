# Session 22: Wild Effect Table — Rulebook Integration

**Date:** 2026-04-08
**Goal:** Add the Wild Effect table to the magic chapter and revisit when effects are rolled and how escalation works.

## Overview

Added the full Wild Effect table to the web rulebook's magic chapter. Redesigned the escalation model from "while active" to a residue system — effects leave aetheric residue that persists until a long rest after the effect wears off, dramatically extending the escalation window. Also changed backlash to trigger on every cast (success or misfire), not just successful casts, and made cancellation backlash burn-only (no wild effect check).

---

## Changes Made

### Design Decisions (docs first)
- **Backlash on every cast:** Backlash now checked on success and misfire alike. Energy flowed through you either way. Cancellation is exempt (lighter consequences).
- **Residue escalation model:** Replaces "while active" — residue from a wild effect persists until you take an uninterrupted long rest after the effect wears off. Same d10 number while residue present = escalation. Dramatically extends the threat window.
- **Cancellation is burn-only:** 10% chance of 1d4 HP damage, but no wild effect check. You cut the flow before it could warp you.

### Web Rulebook (magic.html)
- Rewrote backlash intro to clarify it's checked on every cast
- Added full Wild Effect table with all 10 effects across 3 escalation tiers
- Added residue mechanic explanation
- Added GM Note for per-effect tracking
- Added GM Note for environmental use beyond backlash (high-magic zones, Veil-thin areas)
- Replaced The Street callout with At the Table example showing full backlash → wild effect → residue flow
- Updated misfire section to cross-reference backlash
- Updated cancellation to note burn-only

### Quick Reference (reference.html)
- Updated backlash reference card with misfire inclusion and residue note
- Extended flowchart with misfire → backlash → wild effect branch
- Updated cancellation line to note burn-only

### Table Index (tables.html)
- Added Wild Effect Table entry linking to magic.html#wild-effects

### Design Docs
- Updated MAGIC_SYSTEM.md §3.4 (backlash on all casts, residue model, cancellation burn-only)
- Updated COMBAT_PROCEDURE.md step 8 and cancellation section

---

## Files Modified

| File | Change |
|------|--------|
| `docs/requirements/MAGIC_SYSTEM.md` | Backlash on all casts, residue model, cancellation burn-only |
| `docs/requirements/COMBAT_PROCEDURE.md` | Step 8 updated, cancellation updated |
| `web/rules/magic.html` | Wild Effect table added, residue mechanic, At the Table example, GM callouts |
| `web/rules/reference.html` | Flowchart extended, reference card updated |
| `web/rules/tables.html` | Wild Effect Table entry added |

## Key Design Decisions

1. **Residue model replaces "while active"** — The old "while active" rule meant escalation was near-impossible (you'd need to roll the same d10 number twice within 1d4 hours). Residue extends the window to "until you rest after it fades," making the escalation threat real without changing probabilities. A nosebleed fades in seconds but the residue lingers until morning.
2. **Backlash on misfire too** — Energy flowed through you whether you controlled it or not. Misfires already had consequences (misfire effects + Weak EP cost); backlash adds another layer of risk for the same reason.
3. **Cancellation is burn-only** — You cut the spell before it fully formed. The energy can hurt you (1d4 HP) but didn't flow long enough to warp you. This makes cancellation a lighter, more predictable escape valve.
4. **Environmental reuse of the table** — GM callout explicitly endorses using the Wild Effect table for high-magic zones, Veil-thin locations, and unstable artifacts. The table is a general-purpose "magic is warping things" toolkit.

## Open Issues

- None from this session

## Next Session

- Character sheet art/watermarks
- Landing page tagline refinement
- Visual polish pass on recent chapters
