# Session 7 Notes — Exhaustion Track & Unskilled Formula Rebalance

**Date:** 2026-04-02

## Overview

Corrected fundamental misunderstanding about the exhaustion track — it's a general mental/stress track (like Shadowrun's Stun), not a magic-only resource. Renamed MP to EP throughout all docs and web rules. Reframed PW as mental fortitude first, magical attunement second. Magic access is now a skill choice, not gated by PW. Also fixed the unskilled formula (×10 was broken — untrained could beat trained) and fixed the character sheet table alignment on the rules website.

## Key Decisions

### 1. Exhaustion Track is Mental, Not Magical

The exhaustion track (now **EP — Exhaustion Points**) covers ALL non-physical strain:
- Stress, fatigue, sleep deprivation
- Stun grenades, disorientation
- Psychological pressure, overexertion
- Magical drain (for casters)

Modeled after Shadowrun 3E's Stun track. Physical damage (HP) heals slowly (1d4/hr); mental strain (EP) recovers faster (1d8/hr). Both tracks have the same 4-tier death spiral and penalties stack across them.

**Terminology change:** "Magic Points" / "MP" renamed to "Exhaustion Points" / "EP" across all docs and web rules.

### 2. PW (Power) is Mental Fortitude, Not "The Magic Stat"

PW represents mental fortitude and resilience broadly — resistance to stress, fatigue, stun, and the ability to push through when things are hard. For casters, it also drives magical attunement.

- **Magic access is a skill choice**, not gated by PW. Anyone can take Scholarly or Wild casting skills.
- PW still determines EP per tier (7 + PW), number of schools (PW mod, min 1), and base spells known (7 + PW, min 1) — but only matters for magic if you chose to be a caster.
- A PW +3 non-caster is just incredibly mentally tough with a deep EP pool.
- A PW -3 caster can exist — they'd have 1 school, a handful of spells, and burn out in 2-3 casts. Bad investment, but technically possible.

### 3. Unskilled Formula Rebalanced: ×10 changed to ×5

**Old:** `(5 + attr) × 10`
**New:** `(5 + attr) × 5`

The ×10 multiplier made unskilled attempts better than trained skills in many cases (a +3 attr untrained = 80%, but trained L1 = 43%). The ×5 multiplier ensures skilled is always better, with rapidly increasing returns per level.

#### Full Comparison Chart: Unskilled (×5) vs Trained (L1–L5)

| Attr | Unskilled (×5) | Trained L1 | Trained L2 | Trained L3 | Trained L4 | Trained L5 |
|------|---------------|-----------|-----------|-----------|-----------|-----------|
| -3   | 10%           | 37%       | 44%       | 51%       | 58%       | 65%       |
| -2   | 15%           | 38%       | 46%       | 54%       | 62%       | 70%       |
| -1   | 20%           | 39%       | 48%       | 57%       | 66%       | 75%       |
| 0    | 25%           | 40%       | 50%       | 60%       | 70%       | 80%       |
| +1   | 30%           | 41%       | 52%       | 63%       | 74%       | 85%       |
| +2   | 35%           | 42%       | 54%       | 66%       | 78%       | 90%       |
| +3   | 40%           | 43%       | 56%       | 69%       | 82%       | 95%       |

#### Gap: Unskilled vs Trained L1

| Attr | Unskilled | Trained L1 | Gap |
|------|----------|-----------|-----|
| -3   | 10%      | 37%       | 27% |
| -2   | 15%      | 38%       | 23% |
| -1   | 20%      | 39%       | 19% |
| 0    | 25%      | 40%       | 15% |
| +1   | 30%      | 41%       | 11% |
| +2   | 35%      | 42%       | 7%  |
| +3   | 40%      | 43%       | 3%  |

**Design rationale for ×5:** The gap at +3 (3%) is small, but that character invested heavily to get +3. The real payoff is in training levels — even L2 at +3 jumps to 56% (vs 40% unskilled), and L5 at +3 hits 95%. Skilled is always better and scales dramatically. The math is also clean and easy at the table: multiply by 5.

#### Multiplier Options Considered

| Attr | ×3   | ×4   | ×5   |
|------|------|------|------|
| -3   | 6%   | 8%   | 10%  |
| 0    | 15%  | 20%  | 25%  |
| +3   | 24%  | 32%  | 40%  |

- **×3** was too punishing — untrained attempts felt hopeless
- **×4** had good gaps but less clean math
- **×5** chosen for balance of feel + table-friendly arithmetic

### 4. Character Sheet Table Alignment Fix

Converted the Kael Ashford attribute pip display from flex/span layout to an HTML `<table>`, so the -3 through +3 columns align vertically across all rows regardless of which value has the bullet marker.

## Files Changed

- `web/rules/index.html` — Table fix, EP/unskilled/PW changes
- `docs/requirements/BASE_MECHANICS.md` — EP terminology, unskilled formula, PW description
- `docs/requirements/PROJECT_SPEC.md` — EP terminology, unskilled formula, PW description
- `docs/requirements/MAGIC_SYSTEM.md` — EP terminology, exhaustion track rewrite
- `docs/requirements/COMBAT_PROCEDURE.md` — EP terminology
- `docs/requirements/FIREARMS_EQUIPMENT.md` — EP terminology
- `docs/requirements/SPELL_COMPENDIUM.md` — EP terminology in spell effects
