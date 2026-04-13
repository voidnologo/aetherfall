# Session 23: Economy & Resource System Design

**Date:** 2026-04-13
**Goal:** Design a narrative-first economy system — marks as currency, wealth tiers for story-driving resource access, patron support scales. No checkbook balancing, no exhaustive price lists.

## Overview

Researched 10 RPG economy systems (Blades in the Dark, Shadowrun, Mothership, Savage Worlds, Fate, PbtA/Dungeon World, Stars Without Number, Band of Blades, Trophy, Cypher System/Numenera) and designed a complete economy system for Aetherfall. The system uses three core mechanics — Station (individual wealth tier, 0–5), the Ledger (Society resource state: Flush/Level/Lean/Dire), and Backing (patron support rating, 1–5) — to create story-driving resource access without any transaction tracking. Equipment gets Cost Tier tags (0–5) instead of prices. The design doc includes full research notes, design principles, integration points with existing systems, and rulebook implementation guidance.

---

## Changes Made

### Economy & Resource System Design Document
- **Full design doc:** `docs/requirements/ECONOMY.md` — comprehensive economy system design
- **Research section:** 10 RPG systems surveyed with analysis of what we borrowed, what we rejected, and why
- **8 design principles:** Access not balance, story fuel not simulation, one number per layer, shape not precision, GM controls pace, marks are flavor not mechanics, patron relationships are economic relationships, reaching creates adventure
- **Station (0–5):** Individual wealth tier determining social and commercial access. Starting Station set during Session Zero based on patron Backing floor.
- **The Ledger:** Society-level resource state (Flush → Level → Lean → Dire). Moves based on mission outcomes and time between jobs.
- **Backing (1–5):** Patron support rating from Bare Charter to Inner Circle. Sets Station floor and determines faction-specific gear access.
- **Cost Tiers (0–5):** Every item/service tagged by tier instead of priced. At or below Station = you have it. One above = Station Check. Two+ above = narrative solution required.
- **Station Checks:** d100 skill roll (Etiquette/Streetwise/Persuasion/Deception) with -15% modifier for reaching one tier above.
- **Payout Ratings:** Missions rated as Scraps / Honest Work / Good Money / Windfall, affecting the Ledger.
- **The Drift:** Ledger slides toward Lean between jobs, creating "we need work" pressure.
- **Artifact valuation:** Narrative framework by enchantment tier (Weak through Pre-Eruption), not mark prices.
- **Potion Cost Tiers:** Weak=2, Standard=3, Strong=4, Spectacular=5
- **Equipment Cost Tier assignments:** All existing weapon, armor, and gear categories tagged with Cost Tiers.
- **Faction-specific gear matrix:** What each patron alignment provides at each Backing level.
- **Owned vs. Issued gear:** Patron-issued gear is contingent on the relationship; losing a patron means losing faction equipment access.

### Pending Tasks Update
- Moved "Design currency system and equipment prices" and "Artifact pricing" to Resolved
- Added follow-up tasks: Cost Tier columns in web tables, Station on character sheet, Backing/Ledger on Society sheet, economy sections in web rulebook chapters, playtest modifier tuning

---

## Files Modified

| File | Change |
|------|--------|
| `docs/requirements/ECONOMY.md` | New — full economy design document with research, principles, system design, integration notes |
| `docs/pending-tasks.md` | Moved economy/artifact pricing to Resolved, added 5 follow-up tasks |

## Key Design Decisions

1. **Station, not bank balance** — Wealth is a tier (0–5) determining access, not a number you subtract from. Inspired by Shadowrun lifestyles, simplified further.
2. **The Ledger is qualitative, not quantitative** — Four states (Flush/Level/Lean/Dire) instead of a numerical resource pool. Inspired by Mothership Debt, abstracted to avoid math.
3. **Marks are flavor** — In-world NPCs talk in marks, contracts are written in marks, but players never track a mark balance. Station handles mechanics.
4. **Backing formalizes patron generosity** — 1–5 scale with specific gear provisions per faction alignment. Makes patron support concrete and variable.
5. **Station Checks use existing skills** — Etiquette, Streetwise, Persuasion, Deception — depending on context. No new mechanics, just new application of existing d100 framework.
6. **Two-tier separation: Station (individual) + Ledger (group)** — Borrowed from Blades in the Dark's Coin/Stash split. Creates tension between personal and collective interests.
7. **The Drift replaces bookkeeping** — Instead of tracking expenses, the Ledger naturally slides toward Lean between jobs. GM controls pace narratively.
8. **Artifacts exist outside the economy** — Valued narratively by enchantment tier, not priced in marks. Inspired by Numenera's approach to rare items.
9. **Issued vs. owned gear** — Patron equipment is contingent on the relationship. Economic independence requires personal Station, making patron loyalty an economic choice.
10. **Cost Tiers, not price lists** — Equipment tagged 0–5. "At your tier or below = you have it." Inspired by PbtA's tagged abstraction.

## Open Issues

- Station Check frequency needs playtesting — the -15% modifier may need tuning
- Whether repeated reaching in one session should compound or just carry narrative consequences
- Zone-specific economy adjustments (Galvanic cheaper in Galvanic districts?) — interesting but potentially complex
- Enchanted firearms Cost Tier depends on enchanted firearms design (both pending)
- Starting equipment guidelines: "items at or below your Cost Tier" may need a more specific Session Zero walkthrough

## Next Session

- Review ECONOMY.md with fresh eyes and playtest scenario walkthrough
- Begin writing economy content for web rulebook (Societies chapter, Equipment chapter, GM chapter)
- Add Cost Tier column to equipment tables in web pages
- Add Station, Backing, and Ledger fields to character/Society sheets
