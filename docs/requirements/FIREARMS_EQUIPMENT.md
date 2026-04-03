# Firearms & Steampunk Equipment

## Document Status: DRAFT — First Pass
**Last Updated:** 2026-03-31

---

## 1. Design Philosophy

Firearms are **significantly more lethal** than melee weapons. A few well-placed shots will drop someone. This is intentional — modern weapons *should* be terrifying. The tradeoff is **magical interference**: guns fail near magic, and every spell your party's caster slings makes them worse.

This creates the game's central tactical tension: martial weapons always work, firearms are devastating but fragile, and party composition has real mechanical consequences.

**Feel over simulation.** The stat lines are tuned to evoke the *fantasy* of each weapon — the heavy reliability of a revolver, the devastating spray of a tommy gun — not to model ballistics. Complexity is hidden in the numbers.

---

## 2. Firearm Stats

Every firearm has five stats (exotic weapons add a sixth — **Aetheric**):

| Stat | Description |
|------|-------------|
| **Speed** | Timing track counts to fire one shot (or burst) |
| **Damage** | Dice rolled on a hit |
| **Capacity** | Shots before reload is required |
| **Reload** | Timing track counts to fully reload |
| **Reliability** | Resistance to malfunction. Malfunction chance = 100 − Reliability, checked BEFORE the Ranged roll. Higher = more resistant. Reduced by 2 per net Aetheric point. No check needed for conventional firearms in clean environments. See §4. |
| **Galvanic** | *(Exotic weapons only)* How much the weapon shifts the Aetheric balance toward tech per shot. See §5. |

**Skill:** Firearms use the **Ranged** combat skill (same as bows/crossbows). The weapon's accuracy is baked into the damage code and speed — a tommy gun's terrible accuracy is reflected in its lower per-round damage relative to its fire rate, not a separate accuracy modifier.

---

## 3. Firearm Categories

Firearms follow the same **category + tag** system as melee weapons (see PROJECT_SPEC.md §4.2). Each category defines Speed, Damage, Capacity, Reload, and Reliability. Individual weapons are examples within a category — a player picks the narrative flavor, the stats come from the category line.

### 3.1 Modern Firearms

| Category | Speed | Damage | Capacity | Reload | Reliability | Examples |
|----------|-------|--------|----------|--------|-------------|----------|
| Holdout Pistol | 2 | 1d6 | 2 | 2 | 95 | Derringer, pocket pistol, muff pistol |
| Revolver | 3 | 2d6 | 6 | 3 | 95 | Service revolver, Colt, Webley |
| Semi-Auto Pistol | 3 | 2d6 | 8 | 2 | 85 | Browning, Luger, Mauser C96 |
| Heavy Pistol | 4 | 2d8 | 6 | 3 | 90 | Magnum revolver, hand cannon |
| Rifle | 6 | 2d10 | 5 | 4 | 95 | Bolt-action, Mauser, Springfield |
| Carbine | 5 | 2d8 | 8 | 5 | 90 | Lever-action, cavalry carbine, trench carbine |
| Shotgun | 4 | 3d6 | 2 | 2 | 95 | Break-action, coach gun, sawn-off |
| Combat Shotgun | 5 | 3d6 | 5 | 4 | 85 | Pump-action, trench gun |
| Submachine Gun | 5 | 3d6 | 50 | 3 | 70 | Tommy gun, MP18, Beretta M1918 |

> **Submachine Gun Note:** Each trigger pull consumes 3 rounds and deals 3d6 damage — representing a burst of fire and the chance of multiple hits. The terrible accuracy and recoil are baked into the damage code (3d6 avg 10.5 for 3 rounds is less per-bullet than a revolver). At 50-round drums, that's 16 bursts before reloading.

### 3.2 Steampunk Exotics

Exotic weapons are **rare, emerging technology** — expensive, unreliable, and viewed with suspicion. They represent the bleeding edge of Galvanic engineering — technology that channels forces from the Engine. Not magical, but leveraging principles that push back against the Aether. Each exotic weapon fired also generates **Galvanic accumulation** (see §5.5).

| Category | Speed | Damage | Capacity | Reload | Reliability | Aetheric | Examples |
|----------|-------|--------|----------|--------|-------------|----------|----------|
| Exotic Pistol | 3 | 1d10 | 12 | 2 | 70 | 1 | Pneumatic flechette, needle gun, compressed air pistol |
| Exotic Sidearm | 4 | 2d8 | 6 | 3 | 65 | 2 | Arc gun, voltaic pistol, spark thrower |
| Exotic Heavy | 7 | 3d8 | 3 | 5 | 55 | 3 | Aether lance, beam projector, lightning cannon |
| Exotic Melee | 2 | 1d8+PP | 10 | — | 60 | 1 | Shock gauntlet, arc knuckles, voltaic blade |

> **Exotic Availability:** These weapons cannot simply be purchased at a shop. They are prototype-level technology — acquired through faction connections, black markets, salvage, or theft. GMs should treat them as notable gear, not standard loadouts.

> **Exotic Melee** uses the Brawl skill (gauntlet) or Melee skill (blade). Capacity represents charges; recharges overnight or at a power source.

### 3.3 Firearm Tags

Tags work the same as melee weapon tags — they differentiate weapons within a category. Some tags are shared with melee (Concealable, Piercing), others are firearm-specific.

**Shared Tags (also apply to melee):**

| Tag | Effect |
|-----|--------|
| Concealable | Can be hidden on person. Draw speed 1 |
| Piercing | Ignores 2 points of armor soak |

**Firearm-Specific Tags:**

| Tag | Effect | Typical Weapons |
|-----|--------|-----------------|
| Reliable | +5 to effective Reliability in magic zones | Revolver, break-action shotgun, bolt-action rifle |
| Quick Reload | Reload time halved (round up) | Semi-auto pistol, lever-action carbine |
| Loud | Audible across the entire area. Draws attention, may panic civilians | Shotgun, heavy pistol, submachine gun |
| Quiet | Nearly silent. No audible report beyond immediate vicinity | Pneumatic flechette, suppressed pistol |
| Scatter | At close range (melee distance), +1d6 damage. At long range, −1d6 damage | Shotgun, combat shotgun, sawn-off |
| Burst | Fires multiple rounds per trigger pull. Consumes 3 ammo per shot | Submachine gun |
| Accurate | At long range, no penalty. +5% to hit on aimed shots | Bolt-action rifle, hunting rifle |
| Sawn-Off | −1 speed, −1 damage die step, gains Concealable | Sawn-off shotgun, cut-down rifle |

**Exotic-Specific Tags:**

| Tag | Effect | Typical Weapons |
|-----|--------|-----------------|
| Shocking | Ignores 2 points of metal armor soak (arcs through it) | Arc gun, shock gauntlet, voltaic blade |
| Suppressing | +1 to weapon's Galvanic rating per shot | Aether lance, beam projector |
| Silent | No audible report whatsoever | Pneumatic flechette, needle gun |
| Unstable | On malfunction severity roll, +2 instead of exotic's normal +1 | Aether lance, experimental prototypes |

### 3.4 Comparison: Melee vs. Firearms

| Category | Speed | Avg Damage | Eff | Always Works? |
|----------|-------|------------|-----|:---:|
| Medium Melee | 5 | 5.5 | 1.10 | Yes |
| Revolver | 3 | 7.0 | 2.33 | No |
| Rifle | 6 | 11.0 | 1.83 | No |
| Great Melee | 9 | 7.0 | 0.78 | Yes |
| Heavy Crossbow | 10 | 10.5 | 1.05 | Yes |

A revolver is **2x more efficient** than a medium melee weapon. A rifle does double a longsword's damage. This is the price of "swords always work." In a clean environment, firearms dominate. In a magically saturated area, they're expensive paperweights.

---

## 4. Malfunction System

### 4.1 The Firing Sequence

When a character fires a weapon, the sequence is:

1. **Reliability check (does it fire?)** — Roll d100 as a consequence check. Malfunction chance = **100 − Reliability**, modified by the Aetheric balance (+2% per net point). If the roll falls within the malfunction percentage, the weapon fails. The shot does not fire. Your action is spent.
2. **If it fires → Ranged skill check (does it hit?)** — Roll d100 under your Ranged skill target as normal. Hit, miss, or critical.
3. **If it malfunctions → Severity roll** — Roll d10 to determine how bad the malfunction is.

This mirrors spellcasting in reverse: magic commits the action first, then checks for consequences (backlash). Firearms check for failure first, then resolve the action. Both create tension at different moments.

### 4.2 When to Roll Reliability

**Every shot. Every time.** Reliability is always checked before the Ranged roll, regardless of environment. A tommy gun has a 30% malfunction chance in your living room. A revolver has 5%. That's the baseline — the inherent reliability of the mechanism.

The Aetheric balance modifies this: net Aetheric accumulation makes guns worse, net Galvanic accumulation makes them better. At effective Reliability 100+ (malfunction chance 0% or below), the weapon cannot malfunction — the Galvanic force is actively stabilizing it.

### 4.3 Malfunction Chance

**Malfunction chance** = 100 − effective Reliability

**Effective Reliability** = Base Reliability − (net balance × 2)

| Weapon | Base Rel | Base Malfunc. | At −10 Galvanic | At +5 Aetheric | At +10 Aetheric | At +15 Aetheric |
|--------|---------|--------------|-----------------|----------------|-----------------|-----------------|
| Revolver | 95 | 5% | 0% (can't fail) | 15% | 25% | 35% |
| Semi-Auto | 85 | 15% | 0% | 25% | 35% | 45% |
| Tommy Gun | 70 | 30% | 10% | 40% | 50% | 60% |
| Exotic Heavy | 55 | 45% | 25% | 55% | 65% | 75% |

At effective Reliability 100+ (malfunction chance 0% or below), the weapon **cannot malfunction** — the Galvanic force is holding it together. At effective Reliability 0 or below (malfunction chance 100%+), the weapon **simply does not function**.

*Example: A revolver (Rel 95) in clean air has a 5% malfunction chance. One shot in twenty goes wrong. You barely notice.*

*Example: That same revolver in a Galvanic Zone (−10): effective Rel 115, malfunction chance 0%. Cannot malfunction. The Engine is stabilizing every mechanism in the area.*

*Example: That same revolver in a Wild Zone (+15): effective Rel 65, malfunction chance 35%. One in three shots fails. And you still have to hit with the ones that fire.*

*Example: A tommy gun (Rel 70) at +10 Aetheric: effective Rel 50, malfunction chance 50%. Coin flip every shot. Time for swords.*

### 4.4 Malfunction Severity Table

When a weapon malfunctions, the shot doesn't fire and your action is wasted. Roll d10 to see if it's worse than that:

| d10 | Result | Effect |
|-----|--------|--------|
| 1–5 | **Click** | Nothing additional. Weapon is fine, just didn't fire this time. Try again next action. |
| 6–7 | **Jam** | Weapon is jammed. Clearing costs the weapon's Reload time in counts before it can fire again. |
| 8 | **Misfire** | Round discharges unpredictably. GM determines where it goes — stray shot hits something or someone nearby. |
| 9 | **Mechanical Failure** | Something breaks internally. Weapon is non-functional until repaired (out of combat, tools required, Repair skill check). |
| 10 | **Catastrophic** | Weapon is destroyed. Wielder takes 1d6 damage from the failure (shrapnel, electrical discharge, burst barrel, etc.). |

> **Exotic Escalation:** Exotic (Galvanic) weapons add +1 to the d10 severity roll (a 5 becomes a 6, etc., max 10). Their experimental nature means when things go wrong, they go *more* wrong.

### 4.5 Design Parallel

The firearm sequence mirrors spellcasting in reverse:

| Step | Magic | Firearms |
|------|-------|----------|
| 1 | Cast: roll skill, spell fires | Check Reliability: does the weapon fire? |
| 2 | Check backlash: did the magic bite you? | Roll Ranged: did you hit? |
| Consequence | Backlash hurts the caster | Malfunction hurts the weapon |
| Tension point | After the action (will I get burned?) | Before the action (will it even work?) |

Same mechanical shape, different fiction. Magic risks the caster. Technology risks the tool.

---

## 5. The Aetheric Balance — The Number Line

### 5.1 The Core Concept

Magic and technology pull the environment in opposite directions. The area's **Aetheric Balance** is a single sliding scale — a number line with neutral (zero) in the middle. Spells push it toward magic. Exotic tech pushes it toward tech. The **net value** determines who suffers.

- **Net positive (magic-heavy):** Technology suffers. Firearms lose Reliability.
- **Net negative (tech-heavy):** Magic suffers. Casting targets drop.
- **At zero:** Neither side is penalized.

Conventional firearms and martial weapons don't move the needle in either direction. They're bystanders — affected by the balance, but not affecting it.

### 5.2 What Moves the Balance

**Toward magic (positive):**

| Source | Accumulation |
|--------|-------------|
| Spell — Misfire (failed cast) | 0 |
| Spell — Weak | +1 |
| Spell — Standard | +2 |
| Spell — Strong | +3 |
| Spell — Spectacular | +4 |

**Toward tech (negative):**

Each exotic item has an **Galvanic rating** — how much it shifts the balance per use.

| Source | Accumulation |
|--------|-------------|
| Exotic weapon shot | −(weapon's Galvanic rating) per shot |
| Suppressing tag | Adds +1 to weapon's Galvanic rating |
| Non-weapon exotic device | −(device's Galvanic rating) per activation or per minute sustained |

| Exotic Category | Aetheric Rating |
|-----------------|----------------|
| Exotic Pistol | 1 |
| Exotic Sidearm | 2 |
| Exotic Heavy | 3 |
| Exotic Melee | 1 per charge used |

Non-weapon exotics (aetheric generators, plasma shields, resonance engines) are assigned Galvanic ratings by the GM based on their scale and power. A portable aetheric lamp might be 1; a factory-scale resonance engine might be 10+.

Accumulation is **localized** — it affects the immediate area (a room, a street corner, a clearing). GM adjudicates boundaries.

### 5.3 The Net Effect

Only the **net balance** matters. Each net point shifts **both sides** — penalizing one while empowering the other:

- **Effective Reliability** = Base Reliability − (net balance × 2)
- **Effective Casting Target** = Base Target + (net balance × 2)

Positive net (Aetheric) hurts firearms AND helps magic. Negative net (Galvanic) hurts magic AND helps firearms.

**Reliability is always checked.** Every shot, every time. A tommy gun (Rel 70) has a 30% malfunction chance even in clean air — that's the price of burst fire. A revolver (Rel 95) has a 5% chance. In most cases you won't notice. In a Wild Zone, you'll notice fast. At effective Reliability 100 or above (malfunction chance 0% or below), the weapon cannot malfunction. At effective Reliability 0 or below, the weapon simply does not function.

| Net Balance | Eff. Revolver (95) | Malfunction% | Eff. Tommy (70) | Malfunction% | Casting Mod |
|-------------|----|----|----|----|-----|
| +20 (Deep Wild) | 55 | 45% | 30 | 70% | +40 |
| +15 (Wild Zone) | 65 | 35% | 40 | 60% | +30 |
| +10 (heavy magic) | 75 | 25% | 50 | 50% | +20 |
| +5 (moderate magic) | 85 | 15% | 60 | 40% | +10 |
| 0 (neutral) | 95 | 5% | 70 | 30% | +0 |
| −5 (moderate Galvanic) | 105 | 0% | 80 | 20% | −10 |
| −10 (heavy Galvanic) | 115 | 0% | 90 | 10% | −20 |
| −15 (Galvanic Zone) | 125 | 0% | 100 | 0% | −30 |
| −20 (Deep Galvanic) | 135 | 0% | 110 | 0% | −40 |

**Example:** Three spells generate +12. Two exotic sidearm shots generate −4. Net = +8 (Aetheric). Firearms lose 16 Reliability — a revolver is at effective 79 (21% malfunction). But casters gain +16 to their targets. A caster with base 55 is now at 71 — Strong tier is within easy reach. The magic feeds on itself.

**Example (reversed):** One spell generates +2. An aether lance fires three times (−4 each = −12). Net = −10 (Galvanic). Casting targets drop by 20 — that base-55 caster is at 35, barely managing Standard. But firearms gain +20 Reliability. The tommy gun (70 + 20 = 90) has only a 10% malfunction chance. The Engine is drowning out the Veil.

> **Design Note:** The symmetric model means zones don't just suppress one force — they actively empower the other. A Wild Zone isn't just "guns don't work here." It's "magic is *incredible* here." A Galvanic factory isn't just "spells fail." It's "firearms are *perfect*." This makes zone-specific encounters feel dramatically different in both directions.

### 5.4 Decay

Accumulation decays toward the area's **baseline** at **1 point per minute**.

- In a normal area, baseline is 0. An accumulation of +8 takes 8 minutes to fully clear.
- In an environmental zone, baseline is the zone's permanent value (see §5.5). Added accumulation decays, but the base never changes.

> **Slow Decay Is A Feature:** The lingering residue is narratively significant. Magical forensics experts can track casters by their residue trails. A neighborhood where a Spectacular spell was cast an hour ago still reads as magically active.

### 5.5 Environmental Zones

Some areas have a permanent **baseline accumulation** that the balance decays toward instead of zero:

| Zone Type | Baseline | Effect |
|-----------|----------|--------|
| Deep Galvanic Zone | −25 or more | Magic non-functional. The Engine roars. |
| Galvanic Zone | −15 to −20 | Most spells fail. Galvanic devices thrive. |
| Moderate Galvanic Zone | −8 to −12 | Only powerful casters can push through. |
| Light Galvanic Zone | −3 to −5 | Casting noticeably harder. Tech runs clean. |
| Normal / In-Between | 0 | Everything works until someone tips the balance. |
| Light Aetheric Zone | +3 to +5 | Firearms slightly less reliable. Sensitive equipment twitchy. |
| Moderate Aetheric Zone | +8 to +12 | Only reliable firearms work. |
| Wild Zone | +15 to +20 | Most firearms non-functional. Strange creatures. Reality gets soft. |
| Deep Wild Zone | +25 or more | Swords and sorcery only. |

Spellcasting and exotic tech use **shifts the balance from the baseline**. A party firing exotic weapons in a Wild Zone (+15 baseline) can temporarily push the balance down — from +15 to +10, say — making firearms briefly usable. But once they stop, the balance drifts back to +15.

> **Zone formation, gradients, and environmental staining** are setting-level concepts documented in PROJECT_SPEC.md §2.3. Full zone mechanics (how zones form, shift, and interact over time) are deferred to a dedicated design session.

### 5.6 Tactical Implications

- **The tug-of-war.** Your caster and your exotic gunner are pulling the environment in opposite directions. Coordinating who acts when is a real tactical decision.
- **Party composition matters.** A caster makes your guns worse. An exotic gunner makes your spells worse. Smart parties balance their loadout — and carry a sword for when both sides cancel out.
- **Exotic weapons are anti-magic fields.** Carrying an arc gun into a fight against casters has value beyond the damage. Every shot pushes the balance toward tech, penalizing enemy casting.
- **Zone scouting.** Checking an area's balance before committing is smart tactics. Walking into a Wild Zone with only firearms is suicide.
- **The last-spell problem.** Your caster dropping a Spectacular spell (+4) mid-firefight might win the moment but costs the party's firearms for the next several minutes. Timing matters.
- **Asymmetric warfare.** Cultists in a magically charged lair don't need guns. Factory district enforcers don't need magic. Adventurers operating in both worlds need versatility.

---

## 6. Galvanic Oddities (Non-Weapon Devices)

### 6.1 Design Philosophy

Not every piece of Galvanic technology is a weapon. The Engine powers devices that investigate, protect, communicate, and manipulate the environment. These are prototype-level technology — rare, expensive, and temperamental — acquired through faction connections, black markets, research labs, or salvage.

**Categories over exhaustive lists.** The devices below are representative examples — templates that show GMs how to stat similar items. The goal is to establish patterns (Galvanic ratings, reliability ranges, typical effects) so that GMs can create new devices that feel consistent with the world. If a player wants a Galvanic device not on this list, the GM has the framework to build one.

**Core principle:** Every Galvanic device interacts with the Aetheric balance. Some push it actively (Galvanic rating per use), some sustain a passive field (Galvanic rating while active), and some are passive readers that don't shift the balance at all. This is the key question when designing a new device: does it radiate Engine force, or just listen?

### 6.2 How to Stat a Galvanic Device

When creating a new Galvanic device, assign these properties:

| Property | Description | Guidance |
|----------|-------------|----------|
| **Function** | What it does — one clear purpose | Keep it focused. A device does one thing well. |
| **Aetheric Rating** | How much it shifts the balance per use or while sustained | 0 = passive reader. 1 = minor. 2 = significant. 3 = major. |
| **Reliability** | d100 roll-under to function, same as firearms | 50-60 = fragile prototype. 65-75 = field-ready. 80+ = robust. |
| **Power** | Charges, fuel, or sustained | Most devices: 10 charges or sustained while active. |
| **Rarity** | How hard to acquire | Common (shops), Uncommon (specialist), Rare (faction/black market), Unique (one-of-a-kind) |

**Balance guideline for Galvanic ratings:** A device that replicates a spell effect should have an Galvanic rating roughly equal to the spell tier it mimics (Weak = 1, Standard = 2). A device that provides a persistent environmental effect should have a lower per-tick rating but sustained over time — the force generator in the combat example pushes -2 every 3 counts, equivalent to a steady drip rather than a burst.

### 6.3 Example Devices

These are templates. The specific names and flavors are examples — GMs should reskin freely.

**Aetheric Compass** — *Investigation*
- Measures local Aetheric balance. The needle swings toward disturbances — stronger magic pulls harder. Investigators use these to trace magical activity to its source, mapping gradients to find the fire from the smoke.
- Aetheric Rating: 0 (passive reader — no balance shift)
- Reliability: 80
- Power: No charges — always on
- Rarity: Uncommon
- *Design note:* This is the non-magical equivalent of Detect. It reads the field but can't identify schools or specific spells — it just says "magic is stronger that way." Pairs well with Occult Lore to interpret what the compass is pointing at.

**Force Generator** — *Environmental Control*
- A brass cylinder packed with resonance coils. When activated, it pulses Galvanic force at regular intervals, pushing the Aetheric balance toward tech. The one from the worked combat example.
- Aetheric Rating: -2 per pulse (every 3 counts in combat, every minute out of combat)
- Reliability: 65
- Power: Sustained — runs until deactivated or destroyed
- Rarity: Rare
- *Design note:* This is the tech side's answer to a caster flooding an area with Aetheric accumulation. It doesn't deal damage or target anyone — it changes the rules of the environment. Destroying it is a valid tactical objective. HP: 8 (small, sturdy brass casing). Weighs about 5 lbs.

**Resonance Damper** — *Personal Protection*
- A harness worn under clothing that generates a tight Galvanic field around the wearer. Reduces incoming magical effects by a flat -15% to their effectiveness (damage, duration, or check modifiers — GM adjudicates). Cult hunters swear by these.
- Aetheric Rating: 1 (sustained while active)
- Reliability: 60
- Power: 10 charges (each charge lasts ~10 minutes)
- Rarity: Rare
- *Design note:* This is magical armor — but tech-based. The -15% is a rough guideline, not a precise mechanic. A Weak Force that would deal 1d4 might deal 1d4-1 instead. A Standard Wither's -10% penalty might be reduced to -8%. The GM interprets. It doesn't block magic entirely — it dampens it, like wearing earplugs in a thunderstorm.

**Voltaic Lantern** — *Investigation*
- Projects a beam of tuned Galvanic light that causes magical residue to fluoresce. Hidden wards glow blue. Enchanted objects shimmer. Magical traps become visible as faint outlines. The tech equivalent of Reveal, but slower and more limited.
- Aetheric Rating: 1 per use (each sweep of a room counts as one use)
- Reliability: 70
- Power: 10 charges
- Rarity: Uncommon
- *Design note:* Unlike the spell Reveal, this only shows magical residue — not hidden mundane objects, secret doors, or disguised people. It's a forensics tool, not a perception enhancer. An investigator with both this AND the Reveal spell covers different ground with each.

**Galvanic Brace** — *Physical Augmentation*
- An exoskeletal frame of brass rods and voltaic muscle-wire worn over one arm or across the back. While active, provides the equivalent of +1 PP for lifting, carrying, and feats of brute strength (not combat damage). Hums loudly — no stealth while wearing one.
- Aetheric Rating: 1 (sustained while active)
- Reliability: 65
- Power: Sustained — runs until deactivated. Overheats after ~1 hour of continuous use (needs 30 minutes to cool).
- Rarity: Uncommon
- *Design note:* This doesn't increase PP for skill calculations — it's a narrative tool. You can carry the wounded soldier, force the jammed door, lift the collapsed beam. The +1 PP is a guideline for the GM, not a character sheet modification. The loud humming is a deliberate drawback — Stealth is effectively impossible.

**Signal Caster** — *Communication*
- Sends encoded pulses through Galvanic frequencies. Two paired devices can transmit short messages (a sentence or two) at ranges up to a few city blocks. Works in Wild Zones where conventional radios fail — the Engine signal punches through Aetheric interference.
- Aetheric Rating: 1 per transmission
- Reliability: 70
- Power: 10 transmissions before recharge
- Rarity: Uncommon
- *Design note:* This is the tech answer to Commune — but much more limited. Short messages, paired devices only, line-of-sight-ish range. The advantage is that it works where magic is being suppressed. A mixed party might use Commune in Aetheric zones and Signal Casters in Galvanic ones.

### 6.4 Creating Your Own

The examples above establish patterns. When a player or GM wants a new device:

1. **Start with the function.** What does it do? One clear purpose.
2. **Find the magical equivalent.** If a spell does something similar, that grounds the device's power level and Galvanic rating.
3. **Assign Reliability.** Prototypes are 50-60. Field equipment is 65-75. Military-grade is 80+.
4. **Choose a drawback.** Every device should have at least one: loud, heavy, fragile, limited charges, requires both hands, attracts attention, short range, etc. Galvanic tech is powerful but imperfect.
5. **Set rarity.** How hard is this to get? This controls availability — a Rare device is a plot point to acquire, not a shop purchase.

---

## 7. Vehicles & Conveyance

### 7.1 Design Philosophy

Vehicles are narrative tools, not stat blocks. This is theater-of-the-mind — there are no movement speeds in feet-per-round or fuel consumption tables. A vehicle is fast or slow, reliable or temperamental, big or small. The GM describes what it can do, and the Piloting skill handles the rest.

**The Aetheric question is the interesting part.** Horses don't care about magic zones. Cars do. Airships really do — a stalled engine at altitude is a death sentence. This creates the same tension as the firearms system: mechanical conveyance is faster and more powerful, but magic can shut it down. Smart adventurers think about how they're getting home before they enter a Wild Zone.

### 7.2 Vehicle Categories

Vehicles don't have individual stat lines. They have categories that describe what the GM and players need to know: how fast, how many people, how vulnerable to magic, and what happens when things go wrong.

| Category | Examples | Relative Speed | Capacity | Aetheric Vulnerability | Notes |
|----------|---------|---------------|----------|----------------------|-------|
| **Beast** | Riding horse, draft horse, pack mule, war dog | Moderate | 1-2 riders + cargo | None | Animals are immune to zone interference. Always work. Eat oats. |
| **Bicycle/Cart** | Bicycle, horse-drawn cart, wagon, rickshaw | Slow-Moderate | 1-6 | None | No engine, no problem. Limited by roads and terrain. |
| **Automobile** | Touring car, truck, taxi, armored car | Fast | 2-6 | Moderate (Rel 75) | Engines stall in Aetheric zones. The default adventurer transport in cities. |
| **Motorcycle** | Standard bike, sidecar rig | Very Fast | 1-2 | Moderate (Rel 75) | Faster than cars, less protection. Excellent for chases. |
| **Motorboat** | Launch, speedboat, patrol craft | Fast (on water) | 2-8 | Moderate (Rel 75) | Same engine problems as cars. Stalling on open water is dangerous. |
| **Sailing Vessel** | Sailboat, yacht, fishing boat | Slow-Moderate (on water) | 2-12 | None | Wind-powered. Immune to zones. Slow but reliable. |
| **Airship — Personal** | One-person dirigible, gyrocopter | Moderate (flight) | 1-2 | High (Rel 60) | Experimental. Fragile engines. A malfunction means a crash. |
| **Airship — Transport** | Passenger dirigible, cargo hauler | Slow (flight) | 10-50 | High (Rel 65) | Large, stable, but very vulnerable at altitude. Major investment. |
| **Airship — Military** | Gunship, armored cruiser | Moderate (flight) | 20-100 | High (Rel 70) | Better engines, still vulnerable. Galvanic shielding helps but doesn't eliminate risk. |
| **Train** | Passenger, freight, armored | Fast (on rails) | Dozens-hundreds | Moderate (Rel 80) | Robust engines, but locked to rails. Can't deviate. Reliable but predictable. |

### 7.3 Aetheric Vulnerability

Vehicles with engines interact with the Aetheric balance the same way firearms do:

```
Effective Vehicle Reliability = Base Reliability − (net Aetheric balance × 2)
```

When a vehicle enters an Aetheric zone or magic is cast nearby, the GM checks Reliability on a d100 roll-under:
- **Success:** The vehicle runs fine — for now. Check again when conditions change.
- **Failure:** The engine sputters, stalls, or malfunctions. Severity depends on context.

**How often to check:** Not every count — vehicles aren't firing shots. Check when:
- The vehicle enters a new zone or the balance shifts significantly (±5 or more)
- The vehicle is under stress (chase, evasive maneuvers, damage)
- A spell fires nearby that shifts the balance
- The GM feels dramatic tension warrants it

**Vehicle malfunction severity** (d6, not d10 — vehicles are simpler than firearms):

| d6 | Result | Effect |
|----|--------|--------|
| 1-3 | **Sputter** | Engine coughs. -1 speed category until conditions improve. |
| 4-5 | **Stall** | Engine dies. Piloting check to restart (takes a full round / ~10 counts). |
| 6 | **Breakdown** | Something broke. Vehicle needs repair before it runs again. On an airship, this is an emergency. |

### 7.4 Handling Chases and Travel

> **NOTE:** The rules below describe how chases and travel work mechanically. In the web rulebook, this content belongs in a GM-facing "Running the Game" or "Actions & Situations" chapter — not in the equipment catalog. The equipment chapter lists what vehicles *are*; the procedures chapter explains how to *use* them dramatically.

**Chases:** Opposed Piloting checks. The GM sets the scene (city streets, mountain passes, open sky), describes obstacles, and calls for rolls. Each failed check means the pursuer gains ground (or the quarry loses it). Terrain, weather, and vehicle category matter narratively — a motorcycle outmaneuvers a truck in narrow alleys, but the truck can smash through a roadblock.

**Overland travel:** Narrative pacing. "You drive for three hours and reach the edge of the Wild Zone." No hex maps, no movement rates. The interesting question is always: what's the Aetheric situation where you're going, and will your vehicle work when you get there?

**Airship travel:** The most dramatic. Altitude means a stall isn't just inconvenient — it's potentially fatal. Smart airship crews carry emergency supplies, backup sail rigs, and a prayer. Flying through or over a Wild Zone is a calculated risk that experienced pilots plan around, not through.

### 7.5 Beasts and Magic

Animals are completely immune to Aetheric zone interference. They don't have engines to stall or mechanisms to jam. A horse works in a Deep Wild Zone the same as it does on a city street.

However, animals are *affected* by magical zones psychologically. Horses balk at entering Wild Zones — they can sense the wrongness. Dogs whine and cower. Birds avoid the airspace. Getting a horse to enter a moderate Aetheric zone requires an Animal Handling check (use Survival). Deep Wild Zones? Most animals flatly refuse. War horses and trained mounts have better odds, but even they have limits.

This is why beast-mounted expeditions into Wild Zones are rare and legendary. The animals that will go are special — bred for it, trained for years, and worth a fortune.

---

## 8. General Equipment Categories

> **NOTE:** Prices and a full equipment list are deferred to the currency/economy design session. Below are categories of common adventuring equipment for reference.

**Field Gear:**
- Aether lanterns (magical light sources, no fuel needed, useless in Dead Zones)
- Compressed air grapples
- Rope, climbing pitons, camping supplies
- Portable generators (for powering Galvanic devices in the field)
- Communication devices (short-range radio, unreliable near magic)

**Investigation Tools:**
- Aetheric Compass (see §6.3)
- Voltaic Lantern (see §6.3)
- Photographic equipment (1920s cameras, flash powder)
- Lock-picking kits (mechanical and aetheric variants)
- Alchemical field kits
- Forensic evidence collection supplies

**Protective Gear:**
- Gas masks
- Insulated gloves (for handling magical artifacts or live aether conduits)
- Reinforced goggles (protect against arc flash, magical flares)
- Resonance Damper (see §6.3)

**Medical:**
- Field surgery kit (+1d4 HP bonus when treating wounds with Medicine skill)
- Antitoxin compounds
- Bandages and splints
- Aetheric salves (minor magical healing aids — uncommon, expensive)

### 8.1 Modern Armor Supplement

The existing armor table covers medieval-style armor. Modern additions are documented in the armor tables (see web rulebook, Arms & Equipment chapter). Key design note:

> **Ballistic Vest Note:** Ballistic protection is bleeding-edge technology in the setting. Traditional metal and leather armor is immune to Aetheric zone interference — it's just shaped material. Experimental ballistic materials (ceramic plates, woven composites) could theoretically be affected by extreme Aetheric zones, but this is a GM judgment call for dramatic situations, not a standard rule.

---

## 7. Open Questions

1. **Crossbow Reliability:** Current table has heavy crossbow at 3d6. Should crossbows have Reliability scores? They're mechanical but much simpler than firearms. Proposed: no — they're simple enough to be treated as martial weapons.
2. **Ammunition Types:** Special ammo (incendiary, armor-piercing, silver bullets for magical creatures)? Or is that overcomplicating it?
3. **Dual Wielding:** Pistol in each hand? Flavor is great for the setting. Mechanically — second pistol at +2 speed and a penalty to hit?
4. **Weapon Modifications:** Scopes, extended magazines, silencers? Or keep it simple with the base weapon tables?
5. **Melee Weapon Rebalancing:** Current melee table may need adjustment now that firearms set the damage ceiling. Does a dagger at 1d4 still feel right when a derringer does 1d6?
6. **Aetheric accumulation Exact Decay:** 1 per minute is the baseline. Should this vary by environment? (Faster in Dead Zones, slower in Wild Zones?)
7. **Malfunction Check Frequency:** Every shot? Every burst? Once per engagement at current accumulation? Every shot is grittier but more rolls.
