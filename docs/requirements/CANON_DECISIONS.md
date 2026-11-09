# Canon Decisions

## Document Status: ACTIVE — Locked decisions
**Last Updated:** 2026-11-09 (Session 39)

Decisions that resolve contradictions found in the Session 34 consistency review
(`docs/reviews/2026-09-26-consistency-review.md`). When sources disagree, this file wins.

---

## 1. The Tear was 50 years ago

- The present day is **50 years after the Tear**. The Engine emerged "within a decade" after it.
- Player-facing text keeps saying **"within living memory"** and avoids exact numbers where possible. Voice callouts may round ("fifty years, give or take").
- The world is **1920s-analog**, not the 1920s. No real-world calendar references ("turn of the century", years).
- **This is not Earth.** Real-world touchpoints (the 1920s, jazz, tommy guns, Georgian or medieval architecture, Cassandre-style posters) are narrative shortcuts to orient the reader quickly, not literal history or geography. Real-world nations, ethnicities, and religions don't exist in-world, so never specify a character's real-world heritage.
- People **over ~60** remember the world before; people in their **30s–40s** grew up in the aftermath; young adults have never known anything else.
- NPC ages must fit: anyone described as an adult professional *before* the Tear is **70+**.

## 2. The four leads (Ash & Veil Recovery)

`fiction/world/04-the-characters.md` is canonical for identity and appearance. Pregens, rules examples, and art follow it.

| Character | Age | Canon look (for art) |
|---|---|---|
| **Kael Dunn** — "The Steady Hand" | 42 | Weathered, sun-worn (outdoor beat work); short dark hair greying at the temples; thin scar across the bridge of the nose; broad-shouldered, lean, average height; repaired leather jacket, revolver on hip, hunting knife at small of back |
| **Sera Voss** — "The Spark" | 23 | Pale, sharp-featured; jagged self-cut black hair to the jaw; slight and wiry; pale blue-white ring around the irises; oversized layered coat; brass compass on a cord |
| **Aldric Wynn** — "The Surgeon" | 34 (born 16 years after the Tear) | Indoor pallor (academic); close-cropped dark hair; round spectacles; tall, gaunt, slightly stooped; waistcoat with many pockets; satchel spellbook; walking stick |
| **Mira Cade** — "The Fixer" | 28 | Dark warm eyes; thin scar on left cheekbone; medium height, athletic; wardrobe changes with the job; concealed arc pistol + derringer |

- **Skin tone and ethnicity are deliberately unspecified.** Mention skin only when it's characterful: pallor from a life indoors, weathering from years outdoors, the Aether leaving marks. Art may render the characters however the model tends to; that is acceptable (user decision, Session 34).
- **Kael Dunn is the only Kael.** "Kael Ashford" is retired. Rules examples that need a sword-first fighter use Kael Dunn with his hunting knife, or a separately named example character.

## 3. Magic schools

The six schools are **Aetheric Manipulation, Vivimancy, Warding, Divination, Transmutation, Ley Weaving**. "Vitae" and "Artifice" are not school names anywhere (rules, pregens, fiction docs).

## 4. Firearms use the Firearms skill

Firearms (PC) governs every gun, conventional and Galvanic. Ranged (PC) is bows, crossbows, and thrown weapons.

## 5. Critical range

Rolling your exact target number is always a critical. Each 25-point bracket above the first adds one more number, counted down from the target:

| Target | Crits on |
|---|---|
| 1–25 | Target only |
| 26–50 | Target, target−1 |
| 51–75 | Target down to target−2 (e.g. 66 → 64, 65, 66) |
| 76–99 | Target down to target−3 |

01 is always a critical and 00 always a fumble, regardless of target.

## 6. No rounds

The game has no rounds. Legacy "round" durations convert at **1 round = 3 counts** ("1d4 rounds" → "1d4 × 3 counts").

## 7. Pregens

- **Sera's wild schools:** Aetheric Manipulation + **Transmutation**.
- **The pregen Society is "The Ashwick Charter"** (Fixers, Greycoat patron): a generic starter Society for new players. The fiction's Ash & Veil Recovery is separate.

---

## 8. Name collisions (Session 37)

- **Gideon Marlow** is the Ashworth Collective's Chief Operations Director (was Aldric Voss, which clashed with Aldric Wynn and Sera Voss).
- **Elara Pryce** is the sample character sheet (was Elara Voss).
- **Hollowmere** is the ruin's location in the Skills chapter's Scholar callout (was "Thornfeld", too close to the Thornfield Communion).
- **Corrigan Fels smokes clove cigarettes** from a slim silver case. The thin cigar belongs to Dace Rennick alone.

## 9. Quick Reload rounds up (Session 37)

Quick Reload halves reload time, **rounding up** (Reload 5 → 3, Reload 3 → 2), as in `FIREARMS_EQUIPMENT.md`.

---

## 10. Design-doc drift cleanup (Session 39, issue #38)

The published web rulebook and `web/_data/characters/*.json` are the source of truth for rules numbers. `docs/requirements/` is the design record and follows them. Where issue #38 found two values, the one already in the rulebook wins. The calls that settled contested numbers:

- **Combat skills:** Melee, Brawl, Athletics and BR-Intimidation are **BR**. Firearms, Ranged, Piloting, Sleight of Hand and Stealth are **PC**. Guns use **Firearms**; Ranged is bows, crossbows and thrown (restates §4).
- **Reload times:** the shorter values in `FIREARMS_EQUIPMENT.md` §3 and the web equipment table are canon. `COMBAT_PROCEDURE.md` §11 is a copy and was corrected to match. Crossbows reload **Light 3 / Heavy 5**.
- **Reliability:** checked on **every shot, in every environment**. Roll d100 **under** effective Reliability; over is a malfunction. The balance moves it by **2 per net point**, never 3.
- **Casting times** come from `SPELL_COMPENDIUM.md`'s appendix. Force **2ct**, Reveal **4ct**, Reshape **5ct**, Mend **5ct**, Shield **3ct**, Sever **8ct**.
- **Armor** has two ratings everywhere: **Ballistic** for firearms, **Martial** for melee. The single-Soak tables in COMBAT_PROCEDURE, PROJECT_SPEC and ECONOMY were replaced with the rulebook's.
- **Tier suppression** keys off the **casting target's** 25-point bracket, not skill level. A wild caster's **+10** is part of the casting target, so it counts before the bracket lookup.
- **Spell cancellation** costs **half the Weak tier**, rounded up, whatever tier was being attempted.
- **The compendium holds 38 spells**, and Ley Weaving holds 6 — Enchant is a Ley Weaving ritual.
- **Pregens:** `web/_data/characters/*.json` is canon for the four leads. `STARTER_ADVENTURE.md` restates them and every target derives from `((10 + stat) × level) + 30`.
- **Skill names:** armor and weapon repair is **Craft** (Engineering for ballistic weave and exotic plate). Metalworking, Repair, Running, Swimming, Security, Conceal and Interrogation are not skills.

## 11. Residue outlasts the balance (Session 39)

Magic leaves two traces. The **balance** is mechanical, decays at 1 point per minute, and is the only one that touches Reliability or casting targets. The **residue** is metaphysical — the place's memory of the working — and is only ever read.

**Residue lifetime = (points of accumulation generated)² hours.** One point decays in a minute and reads for an hour. Squaring the trace while the balance stays linear is what makes a Weak spell fade by morning, a night's ritual keep for five weeks, and a catastrophe stay legible for decades. The Tear sits off the end of the scale. Full table, readers and modifiers: `FIREARMS_EQUIPMENT.md` §5.4.

### Still open

- **Vehicle speeds:** `GM_CHAPTER.md` §chase rates Automobile and Motorcycle both 2 and all airships 3; `FIREARMS_EQUIPMENT.md` §7.2 rates Motorcycle above Automobile and splits the airships three ways.
- **Enchant's ritual time** scales by tier (2 hours to 3 days), which is the only spell whose casting time varies with tier.
- **Resisting Persuasion and Intimidation:** `GM_CHAPTER.md` fixes it at Resolve; `PROJECT_SPEC.md` leaves it to the GM.

---

## Pending (user decision needed)

- None.
