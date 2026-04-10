# Session 22: Wild Effect Table, Landing Page, Starter Adventure

**Date:** 2026-04-08
**Goal:** Add the Wild Effect table to the magic chapter, revisit escalation mechanics, refine the landing page identity, and draft a starter adventure module.

## Overview

Large session covering three distinct areas. First, added the full Wild Effect table to the web rulebook and redesigned the escalation model from "while active" to a residue system that dramatically extends the escalation window. Changed backlash to trigger on every cast (success or misfire) and made cancellation backlash burn-only. Second, refined the landing page tagline to "When the Aether Fell, Everything Changed" and removed explicit "1920s Steampunk" genre labeling in favor of letting the setting descriptions convey the era. Third, designed and built a complete one-session starter adventure ("The Ashwick Job") as a Shadowrun-style module with read-aloud blocks, decision branches, NPC stats, and four printable pre-generated character sheets with full skill builds.

---

## Changes Made

### Wild Effect Table & Backlash Redesign
- **Backlash on every cast:** Now checked on success and misfire alike. Cancellation is exempt (burn-only).
- **Residue escalation model:** Replaces "while active" — residue persists until long rest after effect wears off. Same d10 number while residue present = escalation.
- **Cancellation burn-only:** 10% chance of 1d4 HP, no wild effect check.
- Full Wild Effect table (10 effects x 3 tiers) added to magic.html
- At the Table example walking through backlash → wild effect → residue flow
- GM callouts for per-effect tracking and environmental reuse beyond backlash
- Updated reference.html flowchart with misfire → backlash branch
- Updated table index, combat procedure doc, and magic system design doc

### Landing Page Identity
- New tagline: "When the Aether Fell, Everything Changed."
- Removed "1920s Steampunk" from title tag — setting descriptions convey the era through jazz clubs, revolvers, factory districts, etc.

### Starter Adventure — "The Ashwick Job"
- Design doc: `docs/requirements/STARTER_ADVENTURE.md` — full module design
- Web page: `web/rules/quickstart.html` — Shadowrun-style module with Tell It To Them Straight blocks, decision branches (2-3 per scene), NPC stats, pacing guide
- Three-act structure: Investigation (neutral) → Foundry combat (Galvanic +3) → Tunnel rescue (Aetheric +4)
- Showcases: d100 skill checks, ability checks, timing track combat, firearms, magic casting, zone effects, social encounters, non-combat magic/tech utility
- Leverages existing lore: Greycoat Authority, Lamplighter Syndicate, Gradient Scholars, Ashworth Foundry

### Pre-Generated Character Sheets (4 individual printable files)
- **Kael Dunn** — Gunfighter, PP+1/PC+2, 15 skills, Firearms 66%, non-caster
- **Sera Voss** — Wild caster (Aeth. Manip + Artifice), casting target 64, 6 spells
- **Aldric Wynn** — Scholarly caster (all 6 schools), casting target 63, 8 spells
- **Mira Cade** — Social fixer, Persuasion/Deception/Streetwise all 66%, arc pistol
- All use correct skill formula: Target = ((10 + Stat) x Level) + 30
- Full page 2: Society info (The Ashwick Charter), contacts, inventory, spells, notes

### Pending Tasks Cleanup
- Moved corruption/madness mechanics to backlog (expansion candidate)

---

## Files Modified

| File | Change |
|------|--------|
| `docs/requirements/MAGIC_SYSTEM.md` | Backlash on all casts, residue model, cancellation burn-only |
| `docs/requirements/COMBAT_PROCEDURE.md` | Step 8 updated, cancellation updated |
| `docs/requirements/STARTER_ADVENTURE.md` | New — full starter adventure design doc |
| `web/rules/magic.html` | Wild Effect table, residue mechanic, At the Table example, GM callouts |
| `web/rules/reference.html` | Flowchart extended, reference card updated |
| `web/rules/tables.html` | Wild Effect Table entry added |
| `web/index.html` | New tagline, removed "1920s Steampunk" from title |
| `web/rules/quickstart.html` | New — full starter adventure web page |
| `web/rules/tools/quickstart-kael.html` | New — printable character sheet |
| `web/rules/tools/quickstart-sera.html` | New — printable character sheet |
| `web/rules/tools/quickstart-aldric.html` | New — printable character sheet |
| `web/rules/tools/quickstart-mira.html` | New — printable character sheet |
| `web/rules/gm-tools.html` | Added next-page nav link to quickstart |
| `web/rules/js/main.js` | Added quickstart to PAGES registry |
| `docs/pending-tasks.md` | Moved corruption/madness to backlog |

## Key Design Decisions

1. **Residue model replaces "while active"** — Extends escalation window to "until you rest after it fades," making the threat real without changing probabilities.
2. **Backlash on misfire** — Energy flowed through you whether you controlled it or not.
3. **Cancellation is burn-only** — Lighter, more predictable escape valve.
4. **Wild Effect table for environmental use** — GM callout endorses using it for high-magic zones, not just backlash.
5. **Landing page: show don't tell** — Remove genre labels, let jazz clubs and revolvers convey the era.
6. **Shadowrun-style module format** — Tell It To Them Straight blocks, decision branches, GM notes. 10-20 page target.
7. **Three-zone arc** — Every character shines in one zone and struggles in another. The tug of war is the thesis statement.
8. **Individual character sheet files** — Each player gets their own file to print/PDF independently.
9. **Correct skill math** — All pre-gen skills use the exact formula, not approximations.
10. **Pre-gens at net +2** — Slightly heroic, appropriate for a quickstart where players should feel competent.

## Open Issues

- Character sheets need visual review after printing — layout may need tuning for print margins
- Starter adventure could benefit from a simple map sketch (foundry layout, tunnel branches)
- Weapon speeds in quickstart combat examples should be verified against equipment chapter for consistency
- Spell exhaustion costs on character sheets should be verified against grimoire

## Next Session

- Review starter adventure and character sheets after rendering/printing
- Character sheet art/watermarks
- Visual polish pass on recent chapters
- Save/load character data in builder (localStorage)
