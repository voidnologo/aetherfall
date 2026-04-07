# Magical Artifacts

## Document Status: DRAFT — First Pass
**Last Updated:** 2026-04-07

Rules for enchanted weapons, potions, charms, and wards. Covers creation, use, and the mystery of Pre-Eruption artifacts.

**Relationship to Other Documents:**
- [MAGIC_SYSTEM.md](MAGIC_SYSTEM.md) — Casting mechanics, backlash, schools, exhaustion (§3), spell acquisition (§5)
- [SPELL_COMPENDIUM.md](SPELL_COMPENDIUM.md) — Spell tier tables, exhaustion costs, casting times
- [FIREARMS_EQUIPMENT.md](FIREARMS_EQUIPMENT.md) — Weapon stats, tags, Aetheric balance (§5)
- [SKILLS_PROGRESSION.md](SKILLS_PROGRESSION.md) — Craft, Engineering, Occult Lore, Medicine, Science skill descriptions

---

## 1. Philosophy

Magic is new to the world. The first generation of trained casters is just now reaching maturity. The idea of deliberately imbuing objects with magical properties — enchanting — is younger still. It is an emerging discipline built on trial, error, and occasional disaster.

### Core Principles

- **Artifacts are rare and valuable.** There is no enchanting industry, no magic item shop, no standardized production. Every artifact is handmade by a skilled caster-artisan, and most of them are imperfect.
- **Creation is dangerous.** Enchanting follows the same backlash rules as casting. Every artifact carries a trace of the risk that went into making it.
- **Nothing is permanent by default.** Most enchantments fade over time. How long they last depends on how much power was channeled into them (see §1.1 — Decay). Permanent enchantments are master-level work — rare, expensive, and deeply impressive.
- **Magic items are not better weapons.** An enchanted sword is not strictly superior to a well-made steel blade. It can do things steel can't — but it can also fail in ways steel never would. In a Wild Zone, your enchanted blade might surge uncontrollably. In a Galvanic Zone, it might go dead. A good fighter wants both options.

### 1.1 Decay — Universal Duration Rule

Every non-permanent enchantment fades. The duration depends on the **tier at which the artifact was created** — more power channeled into the object means more magical energy bound into its structure, which means it holds together longer. A weak potion barely clings to coherence; a spectacular enchantment radiates stability for years.

| Creation Tier | Duration |
|--------------|----------|
| Weak | **1d6 days** |
| Standard | **1d6 weeks** |
| Strong | **1d6 months** |
| Spectacular | **1d6 years** |
| Permanent | Indefinite (master-level, see §3) |

The creator rolls the d6 openly at the time of creation and knows the result. They can label, date, and plan accordingly — a potion brewer who rolls a 2 on a Weak potion knows they have two days to use or sell it.

This rule applies universally across all artifact categories: enchanted weapons, potions, charms, and wards. One system, one roll, one table.

**Design intent:** This inverts the intuitive expectation that "powerful = fragile." In Aetherfall, powerful magic is *stable* magic — a spectacular enchantment was forged with enough energy to sustain itself for years. A weak enchantment is a candle guttering in the wind. This creates natural pressure: that healing potion brewed at Weak tier? Use it soon. That legendary enchanted blade forged at Spectacular tier? It'll outlast its wielder. The best artifacts in the world *glow* with their own permanence.

### Pre-Eruption Artifacts

Most artifacts in the world are recently made — experimental, first-generation work by the pioneers of a new discipline. But there are exceptions.

Rare objects exist that predate the Eruption. A sword that hums with magical energy, found sealed in a vault that hasn't been opened in two centuries. An amulet pulled from a shipwreck older than anyone's grandparents. A ward-stone buried in ruins that predate the Veil's thinning by decades — or centuries.

Nobody can explain them. Magic is supposed to be new. These objects shouldn't exist. Every Pre-Eruption artifact is a mystery, and some of the most dangerous questions in the world orbit around them: Was magic here before the Eruption, hidden? Did someone know this was coming? Are these objects even human-made?

**Pre-Eruption artifacts cannot be created by player characters.** Their existence is a story hook, not a crafting recipe. GMs should treat them as campaign-defining discoveries — the kind of thing that changes what a party thinks they know about the world.

---

## 2. Artifact Categories

### 2.1 Enchanted Weapons

An enchanted weapon is a mundane weapon (melee, ranged, or firearm) that has been imbued with a magical effect drawn from a specific spell. The weapon retains its normal stats and gains an additional magical property.

#### Effects

Enchantments are drawn from existing spells. The caster must know (scholarly) or have access to (wild) the spell being imbued. Common enchantments:

| Effect | Source Spell | Example |
|--------|-------------|---------|
| **Elemental Damage** | Elemental Manipulation | +1d6 fire/ice/lightning damage on hit |
| **Force Strike** | Force | +1d4 force damage, knockback on strong hits |
| **Accuracy** | Foresight | +5% to hit (the weapon subtly guides the wielder's hand) |
| **Defensive** | Shield | +10% to parry rolls when wielded |
| **Sharpening** | Alter Property | +1 armor piercing (edge stays impossibly keen) |
| **Silent** | Dampen | Strikes make no sound — ideal for stealth kills |
| **Venomous** | Wither | Target takes 1d4 additional damage next round (vitality drain) |
| **Illuminated** | Elemental Manipulation | Blade glows on command — light source + unsettling |

GMs and players can propose other enchantments based on known spells. If a spell can plausibly be channeled through a weapon strike, it's a candidate.

#### Charges

Most enchanted weapons are **charge-based**. The enchantment holds a limited number of uses before it must be re-enchanted.

| Quality | Charges | Creator Requirements |
|---------|---------|---------------------|
| Basic | 3 charges | Casting skill 2+, Craft 1+ |
| Standard | 5 charges | Casting skill 3+, Craft 2+ |
| Superior | 10 charges | Casting skill 4+, Craft 3+ |
| **Permanent** | Unlimited | Casting skill 4+, Craft 3+, ritual (see §3) |

Each activation of the enchantment consumes one charge. Re-enchanting costs exhaustion and time (see §3 — Creation Rules) but no additional XP.

Permanent enchantments are master-level work. They are rare, valuable, and mark the creator as one of the best in the world — a world where "the best" is barely a generation old.

#### Aetheric Interaction

Enchanted weapons generate Aetheric accumulation when their magical effect activates:

| Enchantment Activation | Accumulation |
|------------------------|-------------|
| Charge used | +1 per activation |
| Permanent enchantment (passive) | +1 per minute while drawn |
| Permanent enchantment (active strike) | +2 per activation |

This means enchanted weapons push the Aetheric balance toward magic — making firearms less reliable nearby. A party with multiple enchanted weapons is creating a localized magic zone just by fighting. This is an intentional tension: the more magic items you carry, the worse your guns work.

#### Magical Reliability

Enchanted artifacts have a **Magical Reliability** rating — the mirror of a firearm's Reliability stat. Where firearms resist Aetheric disruption, enchanted items resist Galvanic disruption. The mechanic is deliberately parallel:

**Magical Reliability check:** When activating an enchanted weapon (or when the GM calls for a charm/ward check in a Galvanic-heavy environment), roll d100. Disruption chance = **100 − Magical Reliability**, modified by the Aetheric balance.

**Effective Magical Reliability** = Base Magical Reliability + (net balance × 2)

Positive net (Aetheric) *helps* artifacts. Negative net (Galvanic) *hurts* them — the exact mirror of how the Aetheric balance affects firearms.

| Artifact Quality | Base Magical Reliability |
|-----------------|------------------------|
| Basic (3 charges) | 80 |
| Standard (5 charges) | 85 |
| Superior (10 charges) | 90 |
| Permanent | 95 |
| Pre-Eruption | 98 (they were built to last by someone who knew what they were doing) |

| Net Balance | Eff. Basic (80) | Disruption% | Eff. Permanent (95) | Disruption% |
|-------------|----|----|----|----|
| +15 (Wild Zone) | 110 | 0% | 125 | 0% |
| +10 (heavy magic) | 100 | 0% | 115 | 0% |
| +5 (moderate magic) | 90 | 10% | 105 | 0% |
| 0 (neutral) | 80 | 20% | 95 | 5% |
| −5 (moderate Galvanic) | 70 | 30% | 85 | 15% |
| −10 (heavy Galvanic) | 60 | 40% | 75 | 25% |
| −15 (Galvanic Zone) | 50 | 50% | 65 | 35% |
| −20 (Deep Galvanic) | 40 | 60% | 55 | 45% |

**On disruption:** The enchantment fizzles for that activation. The charge is still consumed (the magic fired but the Galvanic field scattered it). For charms, the passive effect drops for 1d4 hours. For wards, the ward flickers — any effect dependent on it is suspended for 1 round/1 minute (field/combat vs. narrative scale).

At effective Magical Reliability 100+, the artifact **cannot be disrupted** — the magical field is overwhelming the Galvanic interference. At effective Magical Reliability 0 or below, the artifact **simply does not function** — the Engine has drowned it completely.

**Design parallel:**

| Aspect | Firearms | Enchanted Artifacts |
|--------|----------|-------------------|
| Base stat | Reliability | Magical Reliability |
| Disrupted by | Aetheric accumulation | Galvanic accumulation |
| Empowered by | Galvanic accumulation | Aetheric accumulation |
| On failure | Weapon doesn't fire, severity roll | Enchantment fizzles, charge wasted |
| At 100+ effective | Cannot malfunction | Cannot be disrupted |
| At 0 or below | Does not function | Does not function |

This creates the same push-pull tension that defines the Aetheric balance: in a Wild Zone, your enchanted sword is rock-solid but your revolver jams every other shot. In a Galvanic factory, your pistol fires true but your magic blade sputters and dies. **A smart adventurer carries both.**

In **Wild Zones** (net +10 or more), enchanted weapons may also **surge**. When activated, roll d100. On 10 or under, the enchantment fires at one tier higher than intended — a +1d6 fire weapon deals +2d8 fire instead, but consumes 2 charges. Dramatic and dangerous. This is the flip side of the Wild Zone's empowerment: the magic is *too* strong, and control slips.

#### Weapon Tags

Enchanted weapons gain tags that integrate with the existing weapon system:

| Tag | Effect |
|-----|--------|
| **Enchanted** | Weapon carries a magical effect. Generates Aetheric accumulation on use. |
| **Charged [X]** | Has X charges remaining. Track on character sheet. |
| **Permanent** | Enchantment does not expire or consume charges. |
| **Elemental [type]** | Deals bonus damage of specified element. |
| **Attuned** | Enchantment is keyed to a specific wielder. Functions at reduced power (half bonus) for anyone else. |

---

### 2.2 Potions

A potion is a single-use consumable that delivers a magical effect when drunk, applied, or (in some cases) thrown. Potions are the most accessible form of magical artifact — a skilled caster with basic alchemical knowledge can brew them. They are also the most perishable.

#### Categories

**Healing Potions** — Vivimancy (Mend, Purge, Bloom)

| Potency | Creation Tier | Effect | Creation Time |
|---------|--------------|--------|---------------|
| Minor | Weak | Heal 1d6 HP, stop bleeding | 2 hours |
| Moderate | Standard | Heal 2d8 HP, knit minor fractures | 4 hours |
| Major | Strong | Heal 3d10 HP, mend broken bones | 8 hours |
| Critical | Spectacular | Heal 4d12 HP, purge disease, stabilize dying | 1 day |

Shelf life follows the universal decay rule (§1.1): a Minor healing potion lasts 1d6 days. A Critical healing potion lasts 1d6 years.

**Fortifying Potions** — Vivimancy (Fortify) or Transmutation (Alter Property)

| Potency | Creation Tier | Effect | Effect Duration | Creation Time |
|---------|--------------|--------|----------------|---------------|
| Minor | Weak | +5% to one skill | 1 hour | 2 hours |
| Moderate | Standard | +10% to one skill OR +1 to one attribute for skill checks | 4 hours | 6 hours |
| Major | Strong | +15% to one skill OR +1 to one attribute (all uses) | 8 hours | 1 day |

**Curative Potions** — Vivimancy (Purge, Mend)

| Type | Creation Tier | Effect | Creation Time |
|------|--------------|--------|---------------|
| Antidote | Weak | Neutralize one specific poison (must be brewed for that poison) | 3 hours |
| Panacea | Standard | Cure one disease or infection | 6 hours |
| Cleansing Draft | Strong | Remove one magical contamination or curse effect | 8 hours |

**Utility Potions** — Various schools

| Type | Source | Creation Tier | Effect | Effect Duration | Creation Time |
|------|--------|--------------|--------|----------------|---------------|
| Night Eye | Divination (Reveal) | Weak | See in darkness as if dimly lit | 4 hours | 3 hours |
| Iron Skin | Transmutation (Alter Property) | Standard | +2 armor soak (skin hardens) | 1 hour | 6 hours |
| Featherfall | Aetheric (Kinesis) | Weak | Slow falling, negate fall damage | 10 minutes | 4 hours |
| Silence | Ley Weaving (Dampen) | Standard | Suppress all sound within arm's reach | 30 minutes | 4 hours |
| Aqua Lung | Vivimancy (Fortify) | Standard | Breathe underwater | 2 hours | 4 hours |

GMs should use these as templates. Any spell effect that can plausibly be bottled is a candidate for a potion.

#### Shelf Life

Potion shelf life follows the universal decay rule (§1.1). A Weak-tier potion lasts 1d6 days. A Spectacular-tier potion lasts 1d6 years. The creator rolls openly at brewing time and knows exactly how long they have.

Past its shelf life, a potion doesn't become inert — it becomes **unpredictable**. Roll d100 when consuming an expired potion: 01–50 reduced effect (half potency), 51–80 no effect, 81–95 wrong effect (GM chooses something thematically related but unhelpful), 96–100 harmful (treat as a spell misfire).

This creates natural pressure. A minor healing potion brewed at Weak tier might only last two days — use it or lose it. A critical healing potion brewed at Spectacular tier radiates power and stays potent for years. The best potions are worth protecting; the cheapest ones are worth using immediately.

#### Economy

There is no potion shop. Potions are crafted by casters for their own use or as favors, traded between Adventuring Societies, found as valuable loot in abandoned laboratories, or commissioned from the rare caster who has both the skill and the inclination to brew for hire. A reliable source of potions is a relationship worth protecting — not a storefront.

---

### 2.3 Charms

A charm is a wearable enchanted object that provides a passive magical effect while worn. Amulets, rings, bracers, inscribed tokens, enchanted gloves, warded cloaks — any object that can be worn or carried on the body can be a charm.

#### Effects

| Type | Effect | Example Item |
|------|--------|-------------|
| **Skill Boost** | +5% to a specific skill | Marksman's ring (+5% Firearms), thief's gloves (+5% Sleight of Hand) |
| **Enhanced Skill Boost** | +10% to a specific skill | Rare. Master-level crafting. A surgeon's amulet (+10% Medicine). |
| **Resistance** | Reduce damage from one type by 2 | Fire-ward pendant (−2 fire damage), grounding bracelet (−2 lightning) |
| **Sense Enhancement** | Sharpen one sense | Owl-eye monocle (see clearly in dim light), whispering earring (hear through one wall) |
| **Attribute Boost** | +1 to an attribute for specific checks | Extremely rare. A strength charm (+1 PP for Athletics only). |
| **Utility** | Minor passive effect | Warmth charm (comfortable in cold), water-pure token (purifies water you touch), light-stone (glows on command) |

Attribute boost charms are the rarest and most valuable. A charm that grants +1 to an attribute even for limited checks is master-level work, and the kind of thing powerful factions would pay dearly — or kill — to acquire.

#### Attunement and Interference

Wearing a charm requires **attunement** — a brief period (10 minutes) of contact where the wearer's body adapts to the enchantment's magical signature. Once attuned, the charm's effect is persistent as long as it's worn.

**Interference.** Multiple charms create overlapping magical fields that can disrupt each other. There is no hard limit on how many charms a character can wear, but the risk of interference grows:

| Charms Worn | Interference Chance |
|-------------|-------------------|
| 1–2 | None |
| 3 | 10% per day (or per dramatically appropriate moment) |
| 4 | 20% |
| 5 | 30% |
| 6+ | +10% per additional charm |

When interference triggers, roll d6:

| d6 | Interference Effect |
|----|-------------------|
| 1 | **Flicker** — One random charm (d6, reroll if no charm in that slot) goes inert for 1d4 hours. |
| 2 | **Cross-talk** — Wrong charm activates. The GM picks a dramatic (mis)application. A strength charm boosts Persuasion instead; a fire ward flares heat instead of absorbing it. |
| 3 | **Static** — All charms crackle with visible magical discharge. −10% to Stealth and Social checks for 1 hour. Everyone nearby notices. |
| 4 | **Surge** — One random charm's effect doubles for 10 minutes, then goes inert for 1d4 hours. |
| 5 | **Drain** — All charms draw extra energy. Wearer takes 1d4 exhaustion damage. |
| 6 | **Cascade** — All charms go inert for 1d4 hours. Must re-attune to each one. |

**Design intent:** This is a push-your-luck system. Wearing 3 charms is a manageable risk most characters will accept. Wearing 5 is gambling. Wearing 7 is begging for a cascade failure at the worst possible moment. The interference table is designed to create memorable moments, not just penalties — a charm surging at the wrong time can be as dramatic as it going dead.

#### Duration

Charm duration follows the universal decay rule (§1.1). A charm created at Weak tier lasts 1d6 days — barely worth the effort. A Standard charm lasts 1d6 weeks. A Strong charm lasts 1d6 months. A Spectacular charm lasts 1d6 years — a prized possession. Re-enchanting an expired charm is routine maintenance for a caster with the right skills — costs exhaustion and time but no XP.

---

### 2.4 Wards

A ward is a stationary enchantment placed on a location, object, or threshold. Unlike portable artifacts, wards are fixed — they protect a place rather than a person. Wards represent the most "respectable" application of enchanting, because everyone wants protection from the magical chaos engulfing the world.

#### Types

**Alarm Ward** — Warding (Circle, Seal) + Occult Lore
Alerts the caster when a threshold is crossed or a condition is met. The alert can be a mental ping (silent, range depends on potency), an audible sound (local), or a visible flash (obvious but unmissable).

**Barrier Ward** — Warding (Seal, Barrier) + Occult Lore
Blocks physical or magical passage through a threshold. Can be keyed to allow specific people (the caster, named allies) while blocking everyone else. Strength ranges from "slows passage" to "physically impassable wall of force."

**Concealment Ward** — Divination (Detect) + Warding (Circle) + Occult Lore
Hides an area from magical detection. Divination spells (Detect, Reveal, Scry) return nothing — the warded area appears magically blank. Does not make the area physically invisible, just magically opaque.

**Protection Ward** — Warding (Shield, Circle) + Occult Lore
Provides damage reduction or resistance to occupants within the warded area. A well-warded safe room might grant +2 armor soak against magical damage, or impose a −10% penalty on attackers' rolls within the ward's boundary.

**Trap Ward** — Warding (Seal) + relevant offensive spell + Occult Lore
Triggers an offensive magical effect when a condition is met (someone crosses a threshold, touches a warded object, speaks a word). The trapped spell can be any offensive effect the creator knows — a blast of Force, a Wither touch, an Elemental discharge. The trap fires once, then the ward is spent.

#### Duration

Ward duration follows the universal decay rule (§1.1), with the creation tier determined by the effort invested:

| Effort Level | Creation Tier | Creation Time | Duration (1d6 ×) | Typical Use |
|-------------|--------------|--------------|-------------------|-------------|
| **Field** | Weak | 10–30 minutes | 1d6 days | Securing a campsite, blocking a doorway, quick alarm on an escape route |
| **Prepared** | Standard | 2–6 hours | 1d6 weeks | Protecting a safehouse, warding a supply cache, securing a base of operations |
| **Ritual** | Strong | 1–3 days | 1d6 months | Headquarters protection, long-term concealment, securing a vault |
| **Permanent** | Spectacular+ | 1+ week, master-level | Indefinite | Protecting a stronghold, sealing a dangerous site, institutional wards |

Permanent wards require casting skill 4+, Occult Lore 3+, and a significant exhaustion investment spread over the creation period. They are the pride of the Warding discipline — and the most valuable service a Warder can offer.

#### Detection and Breaking

Wards can be found and broken:

- **Detection:** Detect spell (Divination) reveals the presence and general nature of a ward. Reveal shows its exact boundaries and trigger conditions. Non-magical detection is possible with the right Galvanic equipment (see FIREARMS_EQUIPMENT.md — Aetheric Lamp).
- **Breaking:** Unbind spell (Warding) directly unravels a ward. Banish (Warding) can suppress a ward temporarily. Brute-force magical or physical damage can overwhelm a ward's threshold (GM determines hit points based on ward quality). Galvanic devices in sufficient quantity can drown out a ward's magic by shifting the local Aetheric balance.

A ward broken by Unbind fails silently. A ward broken by damage or Galvanic overload fails dramatically — the stored magical energy discharges in an uncontrolled burst. Anyone within arm's reach takes 1d4 damage per effort level of the ward (a ritual ward explodes for 3d4; a field ward pops for 1d4).

---

## 3. Artifact Creation

Creating a magical artifact is a specialized discipline that combines casting ability with physical craftsmanship. It is not a separate skill — it emerges from the intersection of existing skills.

### 3.1 Requirements

**Casting skill:** Scholarly Casting or Wild Casting at sufficient level (see individual artifact tables).

**Craft skill:** Craft for physical objects (weapons, amulets, tokens), Engineering for complex mechanisms (Galvanic-hybrid devices, mechanical wards), Medicine for potions and biological preparations, Science for alchemical formulations.

Both skills must be held by the **same character**. A caster who can't shape metal can't enchant a sword. A blacksmith who can't cast can't imbue a blade. This makes enchanter-artisans a rare and valuable specialization.

> **Design Note:** We considered requiring caster + artisan collaboration (two characters), which would reinforce the "mixed party" philosophy. We chose single-character for simplicity and because the dual-skill requirement already creates interesting character build tension — a character investing in both casting and Craft is sacrificing depth in either. GMs who prefer the collaborative model can house-rule that two characters working together each contribute their best relevant skill.

### 3.2 The Creation Process

**Step 1 — Prepare the vessel.** The physical object must be crafted or acquired. A weapon must be forged, a potion vessel prepared, a charm carved or shaped. **Craft/Engineering/Medicine/Science check** determines the quality of the physical vessel. Failure = wasted materials, start over.

**Step 2 — Channel the enchantment.** The caster imbues the vessel with a spell effect. This is sustained casting — the caster maintains focus and channels magical energy over the creation period. **Casting check** against the caster's Scholarly or Wild Casting target. Success = enchantment takes hold. Failure = the magic dissipates, time is wasted, and the caster suffers exhaustion as if they'd cast the spell.

**Step 3 — Backlash check.** Normal backlash rules apply at the end of creation, rolled at the tier corresponding to the enchantment's power:

| Artifact Quality | Backlash Tier |
|-----------------|--------------|
| Basic / Minor potion | Weak |
| Standard / Moderate potion | Standard |
| Superior / Major potion | Strong |
| Permanent / Critical potion | Spectacular |

Backlash during creation can **ruin the item**. If backlash triggers, in addition to the normal physical damage and possible Wild Effect, roll d100: on 50 or under, the item is destroyed — the magic destabilizes the vessel and the enchantment collapses. The caster is left with wreckage, bruises, and a story to tell.

**Step 4 — Exhaustion.** The caster accumulates exhaustion equal to the spell's tier cost (from SPELL_COMPENDIUM.md) for the enchantment's tier. This exhaustion is **not recovered until the creation process completes** — it represents sustained magical effort over hours or days. A caster creating a Standard-quality enchanted weapon with a Complexity 2 spell burns 6 EP that they carry for the entire creation period. This naturally limits how many artifacts a single caster can create before they need extended rest.

### 3.3 Creation Summary Table

| Artifact | Min Casting | Min Craft* | Time | Exhaustion |
|----------|-----------|-----------|------|-----------|
| Basic enchanted weapon (3 charges) | 2 | Craft 1 | 4 hours | Weak tier |
| Standard enchanted weapon (5 charges) | 3 | Craft 2 | 1 day | Standard tier |
| Superior enchanted weapon (10 charges) | 4 | Craft 3 | 2 days | Strong tier |
| Permanent enchanted weapon | 4 | Craft 3 | 1 week | Spectacular tier |
| Minor potion | 1 | Medicine 1 or Science 1 | 2 hours | Weak tier |
| Moderate potion | 2 | Medicine 2 or Science 2 | 4–8 hours | Standard tier |
| Major potion | 3 | Medicine 2 or Science 2 | 8 hours–1 day | Strong tier |
| Critical potion | 4 | Medicine 3 or Science 3 | 1 day | Spectacular tier |
| Skill boost charm (+5%) | 2 | Craft 1 | 4 hours | Weak tier |
| Skill boost charm (+10%) | 3 | Craft 2 | 1 day | Standard tier |
| Resistance charm | 3 | Craft 2 | 1 day | Standard tier |
| Attribute boost charm | 4 | Craft 3 | 3 days | Strong tier |
| Field ward | 1 | Occult Lore 1 | 10–30 min | Weak tier |
| Prepared ward | 2 | Occult Lore 2 | 2–6 hours | Standard tier |
| Ritual ward | 3 | Occult Lore 3 | 1–3 days | Strong tier |
| Permanent ward | 4 | Occult Lore 3 | 1+ week | Spectacular tier |

*Craft column shows the secondary skill and minimum level required. Substitute Engineering, Medicine, or Science where noted.

---

## 4. Open Questions

1. **Artifact pricing** — What does an enchanted weapon cost in currency? Depends on currency system design (see pending-tasks.md). For now, treat as "extremely valuable, GM determines."
2. **Re-enchanting frequency** — How often do charge-based weapons need topping up in practice? Needs playtesting to determine if 3/5/10 charges feel right.
3. **Potion ingredients** — Should there be a codified ingredient system, or leave it to GM narrative? Leaning toward narrative (avoids herbalism minigame that doesn't fit the system's philosophy).
4. **Enchanted firearms** — Can firearms be enchanted? The magic/tech tension suggests this should be possible but problematic — an enchanted firearm pushes the Aetheric balance against itself. Needs specific rules.
5. **Pre-Eruption artifact mechanics** — Should Pre-Eruption artifacts follow different rules? They might have effects that don't map to known spells, or durations that shouldn't be possible. Left intentionally vague for GMs.
