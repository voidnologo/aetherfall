# Magical Artifacts & Enchantments

## Document Status: DRAFT — Second Pass
**Last Updated:** 2026-04-07

Rules for enchanted artifacts, wards (including wearable charms), and potions. Covers creation, use, and the mystery of Pre-Eruption artifacts.

**Relationship to Other Documents:**
- [MAGIC_SYSTEM.md](MAGIC_SYSTEM.md) — Casting mechanics, backlash, schools, exhaustion (§3), spell acquisition (§5)
- [SPELL_COMPENDIUM.md](SPELL_COMPENDIUM.md) — Spell tier tables, exhaustion costs, casting times
- [FIREARMS_EQUIPMENT.md](FIREARMS_EQUIPMENT.md) — Weapon stats, tags, Aetheric balance (§5)
- [SKILLS_PROGRESSION.md](SKILLS_PROGRESSION.md) — Craft, Engineering, Occult Lore, Medicine, Science skill descriptions

---

## 1. Philosophy

Magic is new to the world. The first generation of trained casters is just now reaching maturity. The idea of deliberately imbuing objects with magical properties — enchanting — is younger still. It is an emerging discipline built on trial, error, and occasional disaster.

### Core Principles

- **Artifacts are rare and valuable.** There is no enchanting industry, no magic item shop, no standardized production. Every artifact is handmade by a skilled caster, and most of them are imperfect.
- **Creation is dangerous.** Enchanting follows the same backlash rules as casting. Every artifact carries a trace of the risk that went into making it.
- **Enchantments are permanent. Wards and potions are not.** This is the fundamental divide. An enchantment bonds Aether into an object's nature — the object *becomes* magical. A ward or potion is merely bathed in Aether — energy stored in a vessel that slowly leaks out.
- **Artifacts use the same reliability framework as Galvanic items**, with the Aetheric balance working in the opposite direction. If you know one system, you know both.

### The Fundamental Divide

| | Artifacts (Enchantments) | Wards & Potions |
|---|---|---|
| **What happens** | Aether is bonded into the object's nature — it *becomes* magical | Aether is stored in a vessel — energy bathed into the object, not intrinsic to it |
| **Duration** | Permanent | Decays (see §1.1) |
| **Rarity** | Exceptionally rare | Uncommon but achievable |

### 1.1 Decay — Duration Rule for Wards & Potions

Wards and potions fade over time. The duration depends on the **tier at which they were created** — more power channeled means more energy stored, which means it holds together longer.

| Creation Tier | Duration |
|--------------|----------|
| Weak | **1d6 days** |
| Standard | **1d6 weeks** |
| Strong | **1d6 months** |
| Spectacular | **1d6 years** |

The creator rolls the d6 openly at the time of creation and knows the result. They can label, date, and plan accordingly.

**This rule applies to wards and potions only.** Enchanted artifacts do not decay — their permanence is what makes them special.

### Pre-Eruption Artifacts

Rare objects exist that predate the Eruption. A sword that hums with magical energy, found sealed in a vault that hasn't been opened in two centuries. An amulet pulled from a shipwreck older than anyone's grandparents. A ward-stone buried in ruins that predate the Veil's thinning by decades — or centuries.

Nobody can explain them. Magic is supposed to be new. These objects shouldn't exist. Every Pre-Eruption artifact is a mystery, and some of the most dangerous questions in the world orbit around them: Was magic here before the Eruption, hidden? Did someone know this was coming? Are these objects even human-made?

**Pre-Eruption artifacts cannot be created by player characters.** Their existence is a story hook, not a crafting recipe. GMs should treat them as campaign-defining discoveries — the kind of thing that changes what a party thinks they know about the world.

---

## 2. Enchanted Artifacts

An enchanted artifact is a mundane object that has been permanently imbued with a magical property through the Enchant spell (see §3.1). The Aether is not stored in the object — it is *part* of the object. The blade doesn't carry fire; the blade *is* fire, bound into steel. The lock doesn't hold a Seal spell; the lock *is* sealed, in a way that transcends its physical mechanism.

### Why Some Objects Can Be Enchanted and Others Cannot

The Aether bonds with objects that have **deep roots in human understanding** — things that people have made by hand, used, trusted, and believed in for centuries. A sword is ancient. A hammer is ancient. A ring, a cloak clasp, a healer's mortar — these are objects humanity has shaped and understood for millennia. Collective belief has soaked into their very concept, and the Aether responds to that accumulated resonance.

Manufactured objects — factory-produced, mechanically complex, assembled from interchangeable parts — lack those roots. They are too new, too poorly understood at a fundamental level. People use firearms without truly understanding the chemistry of propellant or the metallurgy of a rifled barrel. They trust the *mechanism* without grasping the *nature*. The Aether finds nothing to grip. A revolver is reliable because it's well-engineered, not because it's well-understood in the way a knife is understood. This is the same principle that makes complex technology more vulnerable to Aetheric disruption (see DESIGN_PHILOSOPHY.md §2.2 — the Friedman influence).

The line is not "old vs. new" or "simple vs. complex" in absolute terms. It is **handcrafted vs. manufactured**. A sword forged last week by a skilled smith can be enchanted — the act of hand-forging connects it to the same deep tradition of shaped steel that humans have known for thousands of years. A factory-stamped blade from an industrial press cannot — it was *produced*, not *made*.

### 2.1 Enchanted Items

Any handcrafted object can be enchanted: weapons, armor, tools, jewelry, locks, instruments, clothing. The most common artifacts are enchanted weapons — adventurers want blades that hit harder — but there is no mechanical reason the Enchant spell cannot bond Aether into a healer's scalpel, a locksmith's picks, or a singer's lute. Each gains a single mystical property appropriate to its nature.

**One enchantment per item.** The Aether bonds once. An object carries one mystical tag. This keeps artifacts distinct — "the Thundering blade" is a named thing, not a stack of bonuses. "The Whispering Lock" is a specific artifact, not a lock with three spells bolted on.

#### Using an Enchanted Item

When an enchanted item's magical property is relevant — a weapon striking, a lock resisting a pick, a healer's scalpel meeting a wound — check **Magical Reliability** to see if the enchantment activates.

For enchanted weapons in combat, this is a two-step process identical to firing a firearm:

1. **Attack** — Roll Melee (or Ranged for enchanted bows/crossbows) as normal.
2. **Check Magical Reliability** — Roll d100 against the item's Magical Reliability. Under = the mystical tag triggers. Over = the item functions normally as a mundane object, no magical bonus.

For non-weapon artifacts, the GM calls for a Magical Reliability check when the enchantment is tested. The item always functions as an item. The enchantment is the part that can fail.

#### Magical Reliability

Every enchanted artifact has a **Magical Reliability** rating — a measure of how resistant the enchantment is to Galvanic disruption. Higher is better.

**Base Magical Reliability** is determined by the tier at which the Enchant spell was cast:

| Enchantment Tier | Base Magical Reliability |
|-----------------|------------------------|
| Weak | 80 |
| Standard | 85 |
| Strong | 90 |
| Spectacular | 95 |
| Pre-Eruption | 98 |

**Effective Magical Reliability** = Base + (net Aetheric balance × 2)

Aetheric environments help artifacts. Galvanic environments hurt them.

| Net Balance | Eff. Weak (80) | Disruption% | Eff. Spectacular (95) | Disruption% |
|-------------|----|----|----|----|
| +15 (Wild Zone) | 110 | 0% | 125 | 0% |
| +10 (heavy magic) | 100 | 0% | 115 | 0% |
| +5 (moderate magic) | 90 | 10% | 105 | 0% |
| 0 (neutral) | 80 | 20% | 95 | 5% |
| −5 (moderate Galvanic) | 70 | 30% | 85 | 15% |
| −10 (heavy Galvanic) | 60 | 40% | 75 | 25% |
| −15 (Galvanic Zone) | 50 | 50% | 65 | 35% |
| −20 (Deep Galvanic) | 40 | 60% | 55 | 45% |

At effective Magical Reliability 100+, the artifact **cannot be disrupted**. At 0 or below, the artifact **simply does not function**.

#### Disruption Severity

When Magical Reliability fails, roll on the disruption severity table:

| d10 | Severity | Effect |
|-----|----------|--------|
| 1–5 | **Fizzle** | Enchantment doesn't trigger this use. Item functions normally as a mundane object. |
| 6–8 | **Backfire** | The mystical tag misfires — the effect hits you, an ally, or the environment. GM determines the most dramatically appropriate victim. |
| 9 | **Burnout** | The enchantment goes dormant. Magical Reliability drops by 10 until the item is re-attuned (10 minutes of rest, no cost). |
| 10 | **Shatter** | The enchantment is **permanently destroyed**. The Aether bond breaks. The item reverts to mundane. Re-enchanting requires casting Enchant from scratch. |

**In Galvanic Zones** (net −10 or worse): add +2 to the severity roll. Backfire, Burnout, and Shatter become significantly more likely. Using an artifact in heavy Galvanic territory risks losing the enchantment forever. **Put it away.**

#### Aetheric Accumulation

Enchanted items generate **+1 Aetheric accumulation** each time the mystical tag triggers (Reliability check passed). Fizzles generate nothing. A party using enchanted gear pushes the local Aetheric balance toward magic just by relying on their artifacts.

#### Mystical Weapon Tags

Mystical tags are defined in the weapon tag section alongside Melee, Firearm, and Galvanic tags. Each tag has four tiers — the tier is locked permanently when the Enchant spell is cast. Each tag requires the caster to know a **source spell** in addition to Enchant (see §3.1).

| Tag | Source Spell | Weak | Standard | Strong | Spectacular |
|-----|-------------|------|----------|--------|-------------|
| **Thundering** | Force (Aetheric) | +1d4 dmg, push back 1 step | +1d6 dmg, push back 1 step | +1d8 dmg, push back 2 steps | +1d10 dmg, push back 2 steps, target stunned (+2 speed next action) |
| **Elemental [type]** | Elemental Manipulation (Aetheric) | +1d4 [type] damage | +1d6 [type] damage | +1d8 [type] damage | +1d10 [type] damage |
| **Keen** | Alter Property (Transmutation) | +1 armor piercing | +2 armor piercing | +3 armor piercing | +3 armor piercing, crit range +5% |
| **Homing** | Foresight (Divination) | +5% to hit | +10% to hit | +10% to hit, ignore cover penalty | +15% to hit, ignore cover penalty |
| **Venomous** | Wither (Vivimancy) | 1d4 damage next round | 1d6 damage next round | 1d6 damage for 2 rounds | 1d8 damage for 2 rounds |
| **Shielding** | Shield (Warding) | +5% to parry | +10% to parry | +10% to parry, +1 Martial soak | +15% to parry, +2 Martial soak |
| **Silent** | Dampen (Ley Weaving) | Strikes make no sound | Strikes make no sound | No sound, no visible magical glow | No sound, no glow, target doesn't feel pain for 1 round |

GMs and players can propose additional mystical tags based on known spells. If a spell concept can plausibly be channeled through an object, it's a candidate — but the Enchant spell description (§3.1) defines which tags are available at each tier.

**Non-weapon artifacts** use the same tag framework. A shield with Shielding, a lock enchanted with Seal, a lantern with Elemental [light], a healer's scalpel with Mend — define the effect at each tier, assign a source spell, and apply the standard Magical Reliability rules. The weapon tag table above covers the most common combat enchantments; GMs should use it as a template for other items. Detailed non-weapon tags can be expanded as play demands.

#### Attunement

An owner can **attune** to an enchanted artifact, bonding it to themselves. This is a deliberate, expensive commitment.

| Aspect | Detail |
|--------|--------|
| **Cost** | 1 XP (performed as a ritual, takes ~1 hour) |
| **Benefit** | +10% Magical Reliability for the bonded owner |
| **For others** | The enchantment's **source spell misfire effect** triggers against the unauthorized user every time they try to activate the tag. A thief swinging a Thundering sword (source: Force) takes the Force misfire — 1d6 damage as the concussive energy rebounds into them. A stolen Elemental [fire] blade burns the wielder's hands. A Shielding dagger inverts its protection — the user takes bonus damage instead of reducing it. The enchantment is unharmed. The thief is not. |
| **Re-attunement** | A new owner can attune by paying 1 XP, which replaces the previous bond. |

Attunement is expensive — 1 XP is real advancement opportunity. You're trading a session's worth of growth for a meaningful bond with a specific artifact. The payoff: your enchantment is significantly more reliable, and nobody can steal your artifact and use it against you. The item protects itself and its owner — not by self-destructing, but by punishing misuse.

---

## 3. The Enchant Spell

### 3.1 Enchant (Ley Weaving)

*Complexity: 4 — Casting Time: Ritual (2 hours minimum)*

Bond Aether permanently into a prepared object, transforming it into a magical artifact. The caster must know Enchant and have access to the **source spell** for the desired mystical tag (see §2.1 — Mystical Weapon Tags) — scholarly casters must know the specific spell, wild casters have access through their school. This means an enchanter needs at minimum two schools: Ley Weaving (for Enchant) and the school containing the source spell.

**Requirements:**
- Caster must know Enchant (Ley Weaving)
- Caster must have access to the **source spell** for the desired tag — scholarly casters must know the specific spell; wild casters have access through their school
- Object must be **handcrafted** — forged, carved, woven, or shaped by human hands from raw materials. Manufactured objects (factory-produced, mass-stamped, assembled from interchangeable parts) cannot hold an enchantment. The Aether bonds with things that carry the resonance of human craft and centuries of accumulated understanding, not with products of industrial process (see §2 — Why Some Objects Can Be Enchanted).
- Caster must have Craft skill at level 2+ (to prepare the vessel properly)

**Process:**
1. **Prepare the vessel.** Craft check to ensure the object can accept the enchantment. Failure = wasted materials, start over.
2. **Cast Enchant.** Roll against casting target as normal. The margin of success determines the tier, which locks the mystical tag's power level permanently.
3. **Backlash check.** Normal backlash rules apply at the achieved tier. Backlash during enchanting can destroy the object — if backlash triggers, roll d100: on 50 or under, the object is destroyed.

| Tier | Exhaust | Tag Tier Applied | Magical Reliability | Ritual Time |
|------|---------|-----------------|-------------------|-------------|
| **Weak** | 6 | Weak | 80 | 2 hours |
| **Standard** | 10 | Standard | 85 | 4 hours |
| **Strong** | 16 | Strong | 90 | 1 day |
| **Spectacular** | 24 | Spectacular | 95 | 2–3 days |
| *Misfire* | 6 | — | — | Object is ruined. Caster takes 1d6 damage from the magical backlash. If the object was already enchanted (re-enchanting attempt), the existing enchantment is permanently destroyed. |

**Design note:** Complexity 4 with ritual casting makes this one of the most demanding spells in the game. At Spectacular tier, 24 EP of exhaustion spread over 2–3 days of sustained ritual work — the caster will be physically wrecked by the end. Backlash at Spectacular (25% scholarly, 30% wild) means there is a real chance the caster takes physical damage and a meaningful chance the object is destroyed. This is why enchanted artifacts are rare: the process is grueling, risky, and demands a caster who has invested heavily in both Ley Weaving and at least one other school.

**Scholarly casters** can choose to cast at a lower tier for more predictable results. A scholarly caster who rolls well enough for Strong can choose Standard if they want a safer outcome.

**Wild casters** get what they get — which makes wild-forged artifacts unpredictable. A wild caster might produce a Spectacular enchantment on a lucky day, or ruin three swords in a row. This mirrors their casting philosophy: raw power, unreliable control.

### 3.2 Enchant in the Ley Weaving School

Enchant becomes the 6th spell in Ley Weaving, bringing the school to 6 spells — matching most other schools.

| Spell | Complexity | Casting Time | Role |
|-------|-----------|-------------|------|
| Dampen | 3 | 6ct | Suppress magic |
| Channel | 3 | 6ct | Redirect mana flows |
| Attune | 2 | 5ct | Harmonize with magical sources |
| Surge | 3 | 6ct | Flood area with mana |
| Sever | 4 | 8ct | Cut mana connection |
| **Enchant** | **4** | **Ritual (2 hours+)** | **Bond Aether into an object** |

---

## 4. Wards

A ward is an enchantment placed on a location, object, or threshold that fades over time. Unlike artifacts, wards are Aether **stored** in a structure, not bonded into it. The magic leaks. Eventually, it runs out.

Wards include both stationary protections (alarm wards, barrier wards) and **wearable charms** (amulets, rings, tokens). A charm is simply a ward you wear — same rules, same decay, portable form factor.

### 4.1 Ward Types

**Alarm** — Warding (Circle, Seal) + Occult Lore
Alerts the caster when a threshold is crossed or a condition is met. Alert form: mental ping (silent, range depends on potency), audible sound (local), or visible flash (obvious).

**Barrier** — Warding (Seal, Barrier) + Occult Lore
Blocks physical or magical passage through a threshold. Can be keyed to specific people. Strength ranges from "slows passage" to "physically impassable wall of force."

**Concealment** — Divination (Detect) + Warding (Circle) + Occult Lore
Hides an area from magical detection. Divination spells return nothing — the warded area appears magically blank. Does not make the area physically invisible.

**Protection** — Warding (Shield, Circle) + Occult Lore
Provides damage reduction or resistance to occupants. A warded safe room might grant +2 armor soak against magical damage or impose −10% on attackers' rolls within the boundary.

**Trap** — Warding (Seal) + relevant offensive spell + Occult Lore
Triggers an offensive spell effect when a condition is met. Fires once, then the ward is spent.

**Charm (wearable ward)** — Various schools + Craft
A portable ward worn on the body. Provides a passive magical effect while worn. Examples: skill boost amulet (+5% to a specific skill), resistance pendant (−2 damage from a type), warmth charm (comfortable in cold). Requires 10 minutes of contact to attune. Follows the same decay rules as all wards.

### 4.2 Ward Duration (Decay)

Ward duration follows the decay rule (§1.1), with the creation tier determined by casting result:

| Effort Level | Creation Tier | Creation Time | Duration (1d6 ×) | Typical Use |
|-------------|--------------|--------------|-------------------|-------------|
| **Field** (1) | Weak | 10–30 minutes | 1d6 days | Camp perimeter, quick alarm, temporary charm |
| **Prepared** (2) | Standard | 2–6 hours | 1d6 weeks | Safehouse ward, supply cache, working charm |
| **Ritual** (3) | Strong | 1–3 days | 1d6 months | Headquarters protection, long-term concealment, quality charm |
| **Masterwork** (4) | Spectacular | 1+ week | 1d6 years | Stronghold ward, institutional protection, prized charm |

The creator rolls the d6 openly at creation time and knows the result.

### 4.3 Ward Breaking

**Counter-spell method:** Cast Unbind at the ward's **effective tier** or higher. A Weak ward falls to any successful Unbind. A Spectacular ward requires a Spectacular Unbind.

**Galvanic weakening:** Every 5 points of net Galvanic shift drops a ward's effective tier by 1:

| Net Balance | Spectacular Ward | Strong Ward | Standard Ward | Weak Ward |
|---|---|---|---|---|
| 0 (neutral) | Spectacular | Strong | Standard | Weak |
| −5 (moderate Galvanic) | Strong | Standard | Weak | **Fails** |
| −10 (heavy Galvanic) | Standard | Weak | **Fails** | **Fails** |
| −15 (Galvanic Zone) | Weak | **Fails** | **Fails** | **Fails** |
| −20 (Deep Galvanic) | **Fails** | **Fails** | **Fails** | **Fails** |

This creates tactical options: drag Galvanic equipment to a warded location, shift the balance, and the ward becomes easier to Unbind — or fails outright. This is noticeable (the Galvanic gear is loud, the shift is detectable by anyone with magical sensitivity) and takes effort, but it's a viable path.

Wards that fail due to Galvanic drowning stop functioning. When the Galvanic shift subsides, the ward resumes if it still has decay time remaining.

**Detection:** Detect spell (Divination) reveals the presence and general nature of a ward. Reveal shows exact boundaries and trigger conditions. Voltaic Lantern (Galvanic oddity) shows magical residue — wards glow faintly under its beam.

**Wards cannot be physically destroyed.** The magic reinforces the object it's placed on — a warded door doesn't break when you hit it with an axe. You need magical means to get past it.

**Unbind** permanently destroys the ward — the magic unravels and is gone. **Galvanic weakening** just puts the ward to sleep — the Aether goes dormant, the effect stops, but when the Galvanic shift subsides the ward wakes back up. The magic was suppressed, not destroyed.

---

## 5. Potions

A potion is a single-use consumable that delivers a magical effect when drunk, applied, or thrown. Potions are the most accessible form of magical creation — a skilled caster with basic alchemical knowledge can brew them. They are also the most perishable.

### 5.1 Categories

**Healing Potions** — Vivimancy (Mend, Purge, Bloom)

| Potency | Creation Tier | Effect | Creation Time |
|---------|--------------|--------|---------------|
| Minor | Weak | Heal 1d6 HP, stop bleeding | 2 hours |
| Moderate | Standard | Heal 2d8 HP, knit minor fractures | 4 hours |
| Major | Strong | Heal 3d10 HP, mend broken bones | 8 hours |
| Critical | Spectacular | Heal 4d12 HP, purge disease, stabilize dying | 1 day |

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

GMs should use these as templates. Any spell effect that can plausibly be bottled is a candidate.

### 5.2 Shelf Life

Potion shelf life follows the decay rule (§1.1). A Weak-tier potion lasts 1d6 days. A Spectacular-tier potion lasts 1d6 years. The creator rolls openly at brewing time.

Past its shelf life, a potion becomes **unpredictable**. Roll d100: 01–50 reduced effect (half potency), 51–80 no effect, 81–95 wrong effect (GM chooses something thematically related but unhelpful), 96–100 harmful (treat as a spell misfire).

### 5.3 Potion Creation

Creating a potion requires a casting skill (Scholarly or Wild) and a preparation skill (Medicine or Science). Both must be held by the same character.

| Potency | Min Casting | Min Medicine/Science | Exhaustion |
|---------|-----------|---------------------|-----------|
| Minor (Weak) | 1 | 1 | Weak tier |
| Moderate (Standard) | 2 | 2 | Standard tier |
| Major (Strong) | 3 | 2 | Strong tier |
| Critical (Spectacular) | 4 | 3 | Spectacular tier |

Process follows standard casting: roll against casting target, achieve a tier, apply backlash rules. Backlash during potion creation can ruin the potion (d100, 50 or under = destroyed).

### 5.4 Economy

Potions aren't mass-produced, but they are traded. A healer in a magical neighborhood might sell remedies alongside mundane medicines. Adventuring Societies trade them as favors or currency. A skilled brewer with a reputation can charge for commissioned work. Abandoned laboratories sometimes yield surviving bottles. There's no alchemy industry, no chain of potion shops — but where there are casters, there is commerce.

---

## 6. Open Questions

1. **Enchanted firearms** — Can firearms be enchanted? The current rule says no (non-modern weapons only). This creates a clean magic/tech divide but closes off an interesting design space. If revisited: an enchanted firearm would be fighting itself — pushing the Aetheric balance against its own Reliability. Needs specific rules if ever allowed.
2. **Artifact pricing** — What does an enchanted weapon cost in currency? Depends on currency system design (see pending-tasks.md). For now, treat as "extremely valuable, GM determines."
3. **Potion ingredients** — Should there be a codified ingredient system, or leave it to GM narrative? Leaning toward narrative (avoids herbalism minigame that doesn't fit the system's philosophy).
4. **Pre-Eruption artifact mechanics** — Should Pre-Eruption artifacts follow different rules? They might have effects that don't map to known spells, or multiple enchantments on a single object. Left intentionally vague for GMs.
5. **Non-weapon artifact tags** — The framework supports enchanted armor, tools, and other objects, but specific tag tables haven't been written yet. Expand as play demands.
6. **Charm stacking** — Currently no special rules for wearing multiple charms (wearable wards). If playtesting reveals abuse, revisit with an interference system.
