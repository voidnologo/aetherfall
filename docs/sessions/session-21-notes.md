# Session 21: Mid-Campaign Spell Learning — Web Rulebook

**Date:** 2026-04-07
**Goal:** Add the mid-campaign spell learning rules (MAGIC_SYSTEM.md §5.4) to the web rulebook (magic.html).

## Overview

Short focused session. Added the "Learning New Magic" section to the magic chapter of the web rulebook, covering scholarly spell acquisition (source + downtime + casting check + XP) and wild caster school expansion (7 XP + narrative quest). Also restructured the chapter by moving The Six Schools section to the top as framing before mechanics, and removed hardcoded spell counts that would drift with future additions.

---

## Changes Made

### Web: Magic Chapter (magic.html)
- Added "Learning New Magic" section with three subsections: Scholarly Casters (new spells), Wild Casters (new schools), No Path Switching
- Moved "The Six Schools" from bottom of chapter to top (after opening flavor, before How Casting Works) — frames what magic covers before explaining how to use it
- Removed hardcoded spell counts from school list (was "7 spells", "6 spells" etc.) to prevent drift
- Includes At the Table example (Aldric learning Barrier from Magister Holt) and Believer voice callout (gaining a school in a storm)

---

## Files Modified

| File | Change |
|------|--------|
| `web/rules/magic.html` | Added Learning New Magic section, moved Six Schools to top, removed spell counts |

## Key Design Decisions

1. **Six Schools moved to top of chapter** — Schools are framing ("what magic covers") not a reference appendix. Reader should know the domains before learning the mechanics.
2. **No hardcoded spell counts** — Spell counts drift as we add spells (Enchant was 38th). The Grimoire is the authoritative list; the magic chapter just names the schools.
3. **XP paid after the roll, not before** — You roll the casting check first, then pay XP based on outcome (3 XP success, 1 XP failure for new school). The cost is a consequence, not a prerequisite.
4. **XP table placed after casting check, not before** — The check determines the outcome; the XP table shows what that outcome costs. Logical flow: source → downtime → roll → pay.

## Open Issues

- None from this session

## Next Session

- Character sheet art/watermarks
- Landing page tagline refinement
- Visual polish pass on artifacts chapter and spell learning section after seeing them rendered
