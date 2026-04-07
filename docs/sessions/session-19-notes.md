# Session 19: Skill Cap Fix, Mid-Campaign Spell Learning, Magical Artifacts

**Date:** 2026-04-07
**Goal:** Enforce creation-time skill cap in character builder, design mid-campaign spell learning rules, create the magical artifact system.

## Overview

Game mechanics session focused on three design areas. Fixed the character builder's skill dropdown to enforce the creation-time cap of level 3 (was allowing 4-5). Designed and wrote the mid-campaign spell learning rules for both scholarly and wild casters, resolving open question #6 in MAGIC_SYSTEM.md. Created a comprehensive magical artifacts design document covering enchanted weapons, potions, charms, and wards with a universal decay system, a Magical Reliability mechanic that mirrors firearm Reliability on the Aetheric balance, and Pre-Eruption artifact mysteries.

All design decisions were collaboratively reviewed before implementation: spell learning costs (scaling XP by school familiarity), wild caster school acquisition (7 XP + narrative quest, no PW cap), artifact tone (mixed new + Pre-Eruption), charm interference (diminishing returns), creation model (single caster with dual skills), weapon charges, die size for decay (d6), and creator knowledge of duration.

---

## Changes Made

### Character Builder Skill Cap (`web/rules/tools/character-builder.html`)
- [x] Capped skill level dropdown from [1,2,3,4,5] to [1,2,3] at creation time
- Levels 4-5 are only reachable through XP advancement during play

### Mid-Campaign Spell Learning (`docs/requirements/MAGIC_SYSTEM.md`)
- [x] Added new §5.4: Mid-Campaign Spell Acquisition
- [x] Scholarly casters: narrative source (mentor/research/discovery) + downtime + 2-3 XP (scaling by school familiarity) + Scholarly Casting roll. Failure costs 1 XP.
- [x] Wild casters: 7 XP + narrative quest for new schools. No PW cap on mid-campaign schools. Can reach all six schools over a long campaign.
- [x] No path switching between Scholarly and Wild
- [x] Resolved open question #6 in §8

### Magical Artifacts (`docs/requirements/MAGICAL_ARTIFACTS.md`)
- [x] New design document created
- [x] Four artifact categories: enchanted weapons, potions, charms, wards
- [x] Universal decay rule (§1.1): Weak=1d6 days, Standard=1d6 weeks, Strong=1d6 months, Spectacular=1d6 years. Creator rolls d6 openly.
- [x] Magical Reliability system mirrors firearm Reliability — Galvanic energy disrupts artifacts the same way Aetheric energy disrupts firearms
- [x] Enchanted weapons: charge-based (3/5/10), permanent at master-level, new weapon tags, Wild Zone surge mechanic
- [x] Potions: healing/fortifying/curative/utility categories, degrading shelf life, no shop economy
- [x] Charms: diminishing returns interference (10% per charm beyond 2), d6 interference table
- [x] Wards: field/prepared/ritual/permanent scaling, detection and breaking rules
- [x] Artifact creation rules: dual skill requirement (casting + craft), backlash risk, exhaustion during creation
- [x] Pre-Eruption artifacts as campaign mysteries (cannot be player-created)

### Pending Tasks (`docs/pending-tasks.md`)
- [x] Removed completed items (skill cap, spell learning, artifact design)
- [x] Removed particle canvas perf testing (confirmed fine)
- [x] Moved corruption/madness mechanics to Next Up
- [x] Added new backlog items: enchanted firearms rules, artifact pricing, web rulebook artifacts page

---

## Files Modified

| File | Description |
|------|-------------|
| `web/rules/tools/character-builder.html` | Skill level dropdown capped at 3 |
| `docs/requirements/MAGIC_SYSTEM.md` | Added §5.4 spell learning, resolved open question #6 |
| `docs/requirements/MAGICAL_ARTIFACTS.md` | **New file** — complete artifact system design |
| `docs/pending-tasks.md` | Updated completed/removed/added items |

---

## Key Design Decisions

- **Spell learning XP scales by familiarity**: 2 XP for spells in known schools, 3 XP for new schools. Failure still costs 1 XP. Chosen to mirror "cheap to try, expensive to master" philosophy without making spells too cheap (1 XP) or too expensive (flat 3 XP).
- **Wild caster school acquisition uncapped by PW**: PW gates starting schools only. Mid-campaign schools cost 7 XP + narrative quest with no PW cap. Reasoning: requiring PW increase (10 XP) before school purchase (7 XP) = 17 XP minimum, which would almost never happen.
- **Universal decay tied to creation tier**: More power = more stable. Inverts the "powerful = fragile" trope. A weak potion lasts days; a spectacular enchantment lasts years. This creates natural pressure to use low-tier items quickly and treasure high-tier ones.
- **Magical Reliability mirrors firearm Reliability**: Same formula, same number line, opposite polarity. Galvanic energy disrupts magic items the way Aetheric energy disrupts guns. Reinforces the central magic-vs-tech tension symmetrically.
- **Charm interference uses diminishing returns, not hard cap**: No limit on charms worn, but escalating 10% interference per charm beyond 2. Push-your-luck system that creates memorable moments rather than arbitrary restrictions.
- **Artifact creation requires dual skills in one character**: Casting + Craft/Engineering in the same character. Simpler than requiring two-character collaboration, and creates interesting build tension.

---

## Open Issues

- Enchanted firearms rules not yet designed — magic/tech tension when imbuing a firearm needs specific mechanics
- Artifact pricing depends on currency system (not yet designed)
- Web rulebook pages for spell learning and artifacts not yet written (deferred to future session)
- Pre-Eruption artifact mechanics intentionally left vague for GMs — may need examples/guidelines later

---

## Next Session

- Character sheet art/watermarks
- Landing page tagline refinement
- Web rulebook updates for spell learning (magic.html) and artifacts (equipment.html)
- Consider corruption/madness mechanics (moved to Next Up)
