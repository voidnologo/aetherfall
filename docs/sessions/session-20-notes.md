# Session 20: Artifacts & Enchantments Redesign, Web Rulebook Chapter

**Date:** 2026-04-07
**Goal:** Review and redesign the magical artifacts system from session 19, then build the web rulebook chapter.

## Overview

Major redesign of the magical artifacts system, driven by collaborative review of the session 19 first draft. The original design (charge-based weapons, universal decay, charm interference tables) was replaced with a cleaner tag-based system inspired by Symbaroum's weapon enchantment model. The core insight: enchantments permanently transform objects (artifacts), while wards and potions merely store Aether that leaks out over time. This fundamental divide simplified the entire system — charms collapsed into wards, charge mechanics were removed, and enchanted items gained mystical tags that mirror Galvanic weapon keywords structurally.

Built a full web rulebook chapter (Chapter 13 — Artifacts & Enchantments) and added the Enchant spell to the grimoire. Multiple rounds of design refinement during writing: attunement mechanics, ward breaking rules, handcrafted-vs-manufactured philosophy, potion economy, and voice callout tone were all revised based on user feedback.

---

## Changes Made

### Design: Artifacts System Redesign (MAGICAL_ARTIFACTS.md)
- Replaced charge-based weapon system with permanent mystical tag system (Thundering, Keen, Elemental, Homing, Venomous, Shielding, Silent)
- Established fundamental divide: artifacts (permanent, Aether bonded) vs wards/potions (decay, Aether stored)
- Collapsed charms into wards — a charm is just a wearable ward, same rules
- Dropped charm interference system (revisit if playtesting reveals abuse)
- Added handcrafted-vs-manufactured distinction grounded in accumulated belief philosophy (Friedman/Coldfire influence)
- Designed attunement: 1 XP cost, +10% Magical Reliability, source spell misfire punishes unauthorized users
- Ward breaking: wards cannot be physically destroyed; Unbind (permanent) or Galvanic suppression (temporary dormancy)
- Items broadened beyond weapons — any handcrafted object can be enchanted
- Potion economy revised — small-scale commerce exists where casters live, not "no potion shop"

### Design: Enchant Spell (SPELL_COMPENDIUM.md)
- Added Enchant as 6th Ley Weaving spell (Complexity 4, Ritual 2h+)
- Source spell required for desired tag — scholarly casters need the specific spell, wild casters have access through their school
- Full tier table with exhaustion costs, ritual times, and results

### Web: New Artifacts Chapter (artifacts.html)
- Chapter 13 — Artifacts & Enchantments (aether theme)
- Sections: fundamental divide, handcrafted philosophy, using enchanted items, Magical Reliability, disruption severity, mystical tags, Aetheric accumulation, attunement, Enchant spell, wards & charms, ward duration/breaking, potions, Pre-Eruption artifacts
- Voice callouts: Believer (2), Handler (2), Scholar (1), Street (0), Scene/At the Table (2)

### Web: Grimoire Updates (grimoire.html)
- Enchant spell entry added alphabetically between Enlarge/Reduce and Force
- Ley Weaving school table updated with Enchant row
- Casting time reference table updated
- Spell count: 37 → 38

### Web: Chapter Renumbering
- Artifacts inserted as Chapter 13
- Running the Game → 14, Quick Reference → 15, Table Index → 16, GM Tools → 17
- All header-chapter spans, page-number spans, and nav links updated

### Web: Cross-References
- equipment.html: added "The Other Side" callout linking to artifacts chapter
- magic.html: spell count 37→38, Ley Weaving 5→6 spells
- equipment.html: next nav → artifacts.html
- running-the-game.html: prev nav → artifacts.html

---

## Files Modified

| File | Changes |
|------|---------|
| `docs/requirements/MAGICAL_ARTIFACTS.md` | Complete rewrite — tag-based artifacts, wards with decay, handcrafted philosophy, attunement, ward breaking |
| `docs/requirements/SPELL_COMPENDIUM.md` | Added Enchant spell (§6.6) and appendix entry |
| `docs/pending-tasks.md` | Checked off artifacts web rulebook task |
| `web/rules/artifacts.html` | **NEW** — Chapter 13, full artifacts & enchantments rulebook page |
| `web/rules/grimoire.html` | Enchant spell entry, school table, casting time ref, spell count 37→38 |
| `web/rules/magic.html` | Spell count 37→38, Ley Weaving 5→6 |
| `web/rules/equipment.html` | Cross-reference callout, nav links to artifacts |
| `web/rules/running-the-game.html` | Renumbered to Ch 14, nav links to artifacts |
| `web/rules/reference.html` | Renumbered to Ch 15 |
| `web/rules/tables.html` | Renumbered to Ch 16 |
| `web/rules/gm-tools.html` | Renumbered to Ch 17 |
| `web/rules/js/main.js` | Page registry: added artifacts entry, renumbered 13-17 |

---

## Key Design Decisions

1. **Tag-based enchantments over charge-based** — Inspired by Symbaroum. Tags are permanent, have four tiers locked at creation. Simpler, more flavorful, mechanically parallel to Galvanic keywords. Charges and decay on weapons were eliminated entirely.

2. **Artifacts are permanent, wards/potions decay** — The distinction is philosophical: enchanting *transforms* an object (Aether becomes intrinsic), while wards/potions merely *store* Aether (it leaks out). This simplified the system and gave artifacts appropriate weight/rarity.

3. **Handcrafted vs manufactured** — Tied to the Friedman/accumulated-belief worldbuilding. Objects with deep roots in human understanding (swords, rings, hammers) can be enchanted. Factory-produced items cannot. The line is craft tradition, not age.

4. **Any handcrafted object, not just weapons** — Locks, armor, tools, instruments, jewelry. Weapons are the most common but not the only option. One enchantment per item.

5. **Attunement protects the item, not destroys it** — Early design had unauthorized users triggering disruption severity (risking Shatter). This was backwards — a thief could deliberately destroy your enchantment. Revised: unauthorized use triggers source spell misfire against the thief. The enchantment is fine. The thief is not.

6. **Wards cannot be physically destroyed** — A Spectacular ward on a wooden door means the door stands. You need magical means (Unbind) or Galvanic suppression (temporary). This makes wards meaningful protection, not a speed bump.

7. **Galvanic suppression is temporary** — Wards go dormant, not destroyed. When generators turn off, the ward wakes up. Unbind is the only permanent solution.

8. **Potion economy allows small-scale commerce** — Healers sell potions in magical neighborhoods. There's no industry, but there is trade. "No potion shop" was too absolute.

9. **Complexity is internal only** — Spell Complexity is essential in design docs for balance, but never exposed in the web rulebook. Players see EP costs and casting times; the scaffolding stays hidden.

10. **Source spell access, not just school** — Scholarly casters need the specific spell in their book. Wild casters have access through knowing the school. This creates different paths to enchanting.

---

## Open Issues

- Enchanted firearms — explicitly excluded for now (manufactured), but could revisit with specific rules for the magic/tech tension case
- Artifact pricing — still depends on currency system design
- Non-weapon artifact tag tables — framework exists, specific tags expand as play demands
- Mystical tag balance — numbers are first draft, need playtesting
- Ward creation requirements — referenced Occult Lore but creation process not as detailed as Enchant spell
- Charm stacking — dropped interference system; revisit if playtesting shows abuse

---

## Next Session

- Web rulebook updates for mid-campaign spell learning (magic.html §5.4 from session 19 — still not in the web rulebook)
- Character sheet art/watermarks
- Landing page tagline refinement
- Visual polish pass on artifacts chapter after seeing it rendered
