# Running the Game — GM Chapter Design

## Document Status: DRAFT — In Development
**Last Updated:** 2026-04-05

This is the GM-facing chapter. Everything here is for the person running the game — adjudication guidance, mechanical tools for common situations, and worked examples that demonstrate the rules in action. Players don't need to read this. GMs should internalize the philosophy and use the rest as reference.

---

## 1. Adjudication Philosophy

### 1.1 When to Roll

Roll dice when three conditions are all true:

1. **The outcome is uncertain.** If a trained locksmith picks a simple lock in quiet conditions, there's no uncertainty. Narrate the success.
2. **Failure has interesting consequences.** If nothing changes on a failure — if the character just tries again — the roll is pointless. Only roll when failure moves the fiction forward: they're discovered, time runs out, something breaks, the situation changes.
3. **Success is not guaranteed by competence.** A skilled swordsman fighting an untrained peasant isn't rolling to hit — he's deciding what to do. Only roll when the character's training doesn't trivially resolve the situation.

If any condition is missing, don't roll. Narrate the outcome that makes sense. The dice are for moments of genuine tension — if there's no tension, don't reach for them.

**The converse:** If a player describes something clearly impossible — lifting a building, talking a king into abdication, jumping across a canyon — don't roll for that either. Some things simply can't be done. "I attempt it" doesn't create a die roll when the fiction doesn't support it.

### 1.2 Setting Difficulty

The skill formula gives you the baseline. A character with Melee 3 and PC +2 has a 66% chance of hitting. That's the default — no modifiers, normal conditions.

When conditions deviate from normal, apply modifiers:

| Circumstance | Modifier |
|--------------|----------|
| Trivially easy for a trained character | Don't roll |
| Favorable conditions (good tools, plenty of time, helpful environment) | +10% to +20% |
| Normal conditions | +0% |
| Unfavorable conditions (bad tools, time pressure, hostile environment) | −10% to −20% |
| Severely unfavorable (darkness, injury, active interference) | −30% or worse |

Modifiers stack. A character picking a lock in darkness (−20%) while wounded (−10% from Harmed) and rushed (−10%) is at −40%. At that point, even a skilled locksmith is sweating. That's the right feel.

**Don't over-modify.** One or two modifiers is typical. If you find yourself stacking four penalties, consider whether the task is simply impossible in these conditions, or whether you're better served by a single dramatic modifier (−30%, the situation is terrible) rather than granular accounting.

### 1.3 The OSR Loop

The game runs on a simple cycle:

1. **You describe the world honestly.** What the characters see, hear, smell, feel. Not what they conclude — what they perceive.
2. **Players declare what they do.** Not "I roll Investigation" — "I search the desk drawers" or "I watch the guard's patrol pattern." The fiction drives the mechanics, not the other way around.
3. **You determine the outcome.** If the outcome is obvious, narrate it. If it's uncertain, call for the appropriate roll.

This loop is the heartbeat of the game. Everything else — combat, social encounters, chases, exploration — is a structured version of this same cycle.

**The critical discipline:** Describe situations, not solutions. "The door is locked, and you can hear footsteps approaching from the corridor" — not "You need to pick the lock." The locked door and footsteps are facts. What to do about them is the players' problem. Maybe they pick the lock. Maybe they hide. Maybe they kick the door down. Maybe they ambush whoever's coming. The game is richer when players solve problems with their creativity, not when they search for the "correct" response.

### 1.4 Ad-Hoc Checks

#### Skill Checks

When a situation maps to an existing skill, use the skill target number:

```
((10 + associated stat) × skill level) + 30
```

Apply modifiers from §1.2 as needed.

#### Unskilled Attempts

When a character attempts something they have no training in:

```
(5 + stat) × 5
```

Range: 10 (stat −3) to 40 (stat +3). This is deliberately low — attempting a skilled task without training should feel precarious. A stat +3 character has a 40% shot. A stat +0 character has a 25% shot. That's the right feel for "winging it."

#### Stat-Based Quick Checks

Sometimes neither skill nor "unskilled attempt" fits. The character isn't attempting a trained task — they're testing raw capability. Can they hold their breath long enough? Can they resist the poison? Can they keep their grip as the cart lurches? No training helps here. It's just the stat.

```
(5 + stat) × 10
```

Range: 20 (stat −3) to 80 (stat +3). Wider range, higher ceiling. A BR +3 character resists the toxin 80% of the time — they're exceptionally tough. A BR −2 character manages it 30% of the time — they're frail.

> **Design Note:** This is distinct from the unskilled formula. "Unskilled" is "I don't know how to do this." A stat check is "I know how to do this — it's not a skill, it's a capacity." The unskilled formula (×5) maxes at 40 because you're out of your depth. The stat check (×10) maxes at 80 because you're testing something fundamental about the character.

**When to use which:**
- **Skill check:** Character has the skill. Use the full formula.
- **Unskilled attempt:** Character lacks the skill but could plausibly attempt the task. Use (5 + stat) × 5.
- **Stat check:** No skill applies — it's a raw physical, mental, or social capacity test. Use (5 + stat) × 10.

#### Consequence Checks

When neither character skill nor stat is relevant — the outcome depends on circumstances, not the character — use a flat percentage.

"There's a 30% chance the bridge holds your weight."
"50/50 the guard turns left at the intersection."
"The ancient mechanism still works on a 40 or under."

Roll d100 against the percentage. That's it. No skill, no stat — just the situation. Use these for environmental hazards, random NPC behavior, mechanical conditions, and anything where the question is "what does the world do?" rather than "what can the character do?"

### 1.5 Failing Forward

When a character fails a roll, don't default to "nothing happens." Failed rolls should change the situation:

- **Failed lockpick:** The lock holds, and you hear the tumblers click into a more secure position — next attempt is at −10%. Or: the lock holds, and the pick snaps inside. You need tools to extract it before trying again.
- **Failed Persuasion:** The merchant isn't convinced, and now he's suspicious of you. Your next social approach with him starts at Unfriendly instead of Neutral.
- **Failed Stealth:** You're seen. Not "you made a noise and can try again" — you're seen. Now what?

The goal: every roll matters. Success moves toward the objective. Failure creates a new problem that demands a response. The fiction never stalls.

---

## 2. Social Situations

### 2.1 NPC Dispositions

Every NPC has a disposition toward the party. This isn't a hidden stat to track — it's a judgment call the GM makes based on context. The disposition modifies social skill checks:

| Disposition | Modifier | Description |
|-------------|----------|-------------|
| Hostile | −30% | Actively opposed. Looking for reasons to refuse. Will twist your words. |
| Unfriendly | −15% | Suspicious. Resistant. Needs convincing just to listen. |
| Neutral | +0% | No strong feelings. Open to reasonable proposals. |
| Friendly | +15% | Well-disposed. Wants to help if they can. Gives benefit of the doubt. |
| Allied | +30% | Actively on your side. Needs minimal convincing. Will stretch to accommodate. |

Disposition can shift during a conversation. A successful Etiquette check might move an Unfriendly NPC to Neutral. A terrible lie caught by Empathy might drop a Friendly NPC to Unfriendly. The GM adjusts based on what happens in the fiction.

**This is guidance, not a system.** Some GMs will track disposition per NPC with notes. Others will eyeball it in the moment. Both are correct. The table exists so that when you think "this NPC is suspicious of the party," you have a concrete number to apply: −15%.

### 2.2 When Skills Apply vs. When Roleplay Carries It

Roleplay and mechanics work together. Neither replaces the other.

**When to call for a roll:**
- The outcome is uncertain (the NPC could go either way).
- The stakes matter (access, information, safety, trust).
- The character is attempting something beyond casual conversation — persuading, deceiving, intimidating, navigating etiquette.

**When to skip the roll:**
- The request is reasonable and the NPC has no reason to refuse. "Can I buy a room for the night?" doesn't need Persuasion.
- The roleplay is so compelling or the argument so airtight that the NPC would be convinced regardless. Trust your instincts — if the player nails it, let it land.
- The request is so absurd that no roll could make it work. "I convince the guard to hand me his keys and walk away" isn't a Persuasion check — it's delusion.

**The roleplay modifier:** When a roll is called for, good roleplay adjusts the odds:

| Roleplay Quality | Modifier |
|-------------------|----------|
| Compelling argument, addresses NPC's actual concerns | +10% to +20% |
| Adequate, nothing special | +0% |
| Tone-deaf, contradicts NPC's values, insulting | −10% to −20% |

A player who says "I try to convince him" gets the flat skill check. A player who says "I remind him that his daughter studies at the university that our patron funds, and ask if he'd like that relationship to continue" gets +15% or +20%. The fiction rewards engagement.

### 2.3 Social Skill Checks

The social skills and their applications:

| Skill | Used For | Opposed By |
|-------|----------|------------|
| **Persuasion** | Convincing someone of something true or reasonable. Negotiation, plea, argument. | Resolve (if the NPC resists) |
| **Deception** | Convincing someone of something false. Lies, misdirection, forgery. | Empathy (to detect the lie) |
| **Intimidation** | Compelling through threat of force or social consequence. | Resolve (to resist the pressure) |
| **Etiquette** | Navigating social norms. First impressions, protocol, reading a room. | Not typically opposed |
| **Leadership** | Rallying, inspiring, coordinating groups. Morale under pressure. | Not typically opposed |
| **Streetwise** | Navigating underworld culture. Finding contacts, reading criminal intent, knowing the unwritten rules. | Not typically opposed |

**Opposed social checks** use the standard opposed check rules: both sides roll, the larger margin wins. If one succeeds and the other fails, the success wins automatically. If both fail, the social moment stalls — neither side gains ground.

*Example: Sera (Deception target 66) lies to a guard. The guard has Empathy target 45. Sera rolls 41 (success, margin 25). Guard rolls 32 (success, margin 13). Both succeed, but Sera's margin is larger — the lie holds. If the guard had rolled 51 (fail), Sera would have won automatically.*

### 2.4 Intimidation as Flex-Stat

Intimidation is the only skill in the game that can be assigned to either Physical (BR) or Social (SP) at character creation. The choice reflects how the character threatens people.

**BR Intimidation (Physical Menace):** Looming in doorways. Cracking knuckles. Picking up the table one-handed. This works on people who can be physically threatened — thugs, merchants, bureaucrats. It doesn't work well on people who are physically fearless (soldiers, monsters) or who operate in contexts where physical violence is off the table (courtrooms, diplomatic functions).

**SP Intimidation (Social Pressure):** Naming someone's secrets in public. Mentioning their patron's displeasure. Letting them see you make a note. This works on people with something to lose — reputation, position, connections. It doesn't work on people who have nothing to lose or who operate outside social structures.

**GM guidance:** When a player attempts Intimidation, consider which type applies. If the context doesn't match their stat (a BR Intimidator trying to pressure a noble at a dinner party), apply a −10% to −20% modifier. If the context is perfect (that same BR Intimidator cornering a snitch in an alley), no modifier or even +10%.

### 2.5 Social Skills Don't Mind-Control

A successful social check opens a door. It does not walk through it.

**What success means:**
- **Persuasion:** The NPC is convinced of your point — *for now, within reason.* They agree to the deal, believe your argument, accept your proposal. They don't abandon their deepest loyalties, betray their family, or act against self-preservation.
- **Deception:** The NPC believes the lie — *for now.* New evidence, inconsistencies, or time to reflect can unravel it. A Spectacular margin might make the lie stick longer, but it's never permanent.
- **Intimidation:** The NPC is cowed — *for now.* They comply out of fear. The moment the fear is removed (you leave, they find allies, time passes), they may act against you. Intimidation creates compliance, not loyalty.

**What success does not mean:**
- The NPC does anything you want regardless of the request.
- The NPC forgets the interaction happened.
- The NPC's personality or values change.
- Other NPCs don't notice or react to what happened.

**The margin rule:** The more extraordinary the request, the higher the margin required. Asking a guard to look the other way for a minute? A basic success. Asking a guard to abandon his post? That's Strong margin territory (31+). Asking a guard to betray his employer? That's Spectacular (51+) *if it's possible at all* — and for many NPCs, it simply isn't, regardless of the roll.

---

## 3. Chases

The timing track isn't just for combat. Any situation where timing, speed, and sequential action matter can use the track — and chases are the natural fit.

### 3.1 Chase Structure

A chase is a series of actions on the timing track. Both the pursuer and the quarry act on the same track, placing tokens as normal.

**Setup:**
1. GM establishes the starting range band (typically Near or Far).
2. Both sides declare their first action — usually Sprint.
3. Place tokens. Advance the track.

**The chase problem:** The pursuer wants to close to Close range. The quarry wants to open distance beyond Distant. If both sides Sprint at the same speed, the gap never changes — so the chase is decided by obstacles, complications, and the choices each side makes.

**Ending conditions:**
- **Pursuer reaches Close range:** The chase becomes a grapple (Brawl), a tackle (Athletics), or a combat encounter. The pursuer catches their target.
- **Quarry opens beyond Distant:** One more Sprint and they've escaped. The pursuer can make one last desperate action (a ranged attack, a thrown object, a shouted command) and then the quarry is gone.
- **Soft cap (15-20 counts):** If the chase drags past 15-20 counts without resolution, force an ending. Both sides make one final opposed check — Athletics vs. Athletics for foot chases, Piloting vs. Piloting for vehicles. Highest margin determines who wins. Tie goes to the quarry — chases favor the pursued.

> **PLAYTEST NOTE:** Chase rules extend the timing track in ways not yet tested at the table. The structure is sound in theory — all actions already have speeds, Sprint is already defined — but pacing may need tuning. If chases feel too long or too short, adjust the soft cap or allow two range band movements on exceptional Athletics results.

### 3.2 Foot Chases

| Action | Speed | Effect |
|--------|-------|--------|
| **Sprint** | 3 | Move one range band (closer or farther). |
| **Obstacle** | varies | Athletics check to clear an obstacle. Success: no delay. Failure: +2 count penalty to your next action (stumble, fall, wrong turn). |
| **Shortcut** | 4 | Investigation or Survival check. Success: move two range bands instead of one. Failure: move zero — dead end, wrong turn, lost time. |
| **Combat action** | per weapon | Attack the other party mid-chase (must be in range). A ranged attack at Far is at −10% as normal. |
| **Dirty trick** | 2 | Knock over a cart, slam a door, throw something in the way. Target must succeed on an Athletics check or take +2 count penalty. |

Obstacles are the GM's primary tool for making chases interesting. Without obstacles, both sides just Sprint repeatedly and nothing happens. Every 3-5 counts, introduce something:

### 3.3 Chase Complications

When a chase needs texture, roll or pick from this table:

| d6 | Complication |
|----|--------------|
| 1 | **Obstacle** — a wall, a cart, a fence, a gap between rooftops. Athletics check; failure = +2 count penalty. |
| 2 | **Bystanders** — a crowd, a procession, a work crew in the path. Athletics or Piloting check; failure = +3 count penalty and someone gets hurt. |
| 3 | **Terrain change** — stairs, rubble, water, ice, a steep slope. A different skill check is required (Survival, Athletics, Piloting). Failure = +2 count penalty. |
| 4 | **Zone boundary** — the chase crosses into a different Aetheric zone. Firearms and Galvanic devices recalculate Reliability. Casting targets shift. The tactical landscape changes. |
| 5 | **Dead end** — the path is blocked. Investigation check (speed 2) to find an alternate route, or lose one range band (you double back). |
| 6 | **Opportunity** — a rope to swing on, a ledge to leap from, a wagon to commandeer. The player describes a creative action. If it makes sense, let them do it — grant a free range band movement or a +10% bonus to their next action. |

### 3.4 Vehicle Chases

Vehicle chases use the same structure as foot chases, with these modifications:

- **Vehicle speed replaces Sprint.** An automobile might move one range band every 2 counts (fast) vs. a horse every 4 counts (slower). The GM sets vehicle speed based on the vehicle and the terrain.
- **Piloting replaces Athletics** for obstacles and maneuvering.
- **Reliability matters.** If the chase crosses an Aetheric zone boundary, every vehicle and firearm recalculates effective Reliability. A car chase into a Wild Zone means the engine might stall — Reliability check every time the zone baseline shifts.
- **Collateral damage increases.** Vehicle chases at speed through city streets mean bystanders, property damage, and attention from authorities. These are consequences even if the chase is "won."

| Vehicle Type | Chase Speed (counts per range band) | Notes |
|--------------|-------------------------------------|-------|
| Horse / animal | 4 | Immune to Aetheric interference. Can go anywhere. |
| Automobile | 2 | Fast on roads. Reliability check in Aetheric zones. |
| Motorcycle | 2 | Fast, maneuverable (+10% to Piloting for obstacles). Fragile (rider takes damage on crash). |
| Airship / aircraft | 3 | Three-dimensional chase. Can gain/lose altitude as a range band shift. Engine stalls at altitude are catastrophic. |
| On foot | 3 | The Sprint baseline. |

### 3.5 Mixed Chases

A foot pursuit that becomes a vehicle chase (someone commandeers a car) or vice versa (the car stalls in a Wild Zone) is handled by transitioning between speed tables. The range band gap carries over. If you were Far on foot and jump in a car, you're still Far — you're just closing faster now.

---

## 4. Zone Management

### 4.1 Tracking Accumulation at the Table

Keep it simple. A tally on scratch paper or a whiteboard:

```
Aetheric: |||| (4)
Galvanic: || (2)
Net: +2 Aetheric
```

Each successful spell adds its tier value. Each exotic weapon shot or Galvanic device activation subtracts its Galvanic rating. Cross off marks as accumulation decays (1 per minute, roughly 60 counts on the timing track).

**In combat:** Track every spell and every exotic weapon shot. The balance is a tactical resource — players and enemies are actively managing it.

**In exploration:** Don't track count-by-count. Instead, note when something significant shifts the balance: a spell is cast, a device is activated, the party enters a new zone. Between events, decay happens in the background — "it's been about ten minutes, so the accumulation from that spell has faded."

**In pure roleplay:** Don't track at all unless magic or exotic tech is used. A conversation in a tavern doesn't need zone math.

### 4.2 Environmental Zones as Adventure Design

Zones are adventure design tools. The Aetheric balance of a location tells the players what works here, what doesn't, and what the place *is*.

A factory pumping Galvanic energy into the air (baseline −10) tells the players: your caster is weakened here, firearms are reliable, someone is running heavy machinery. A haunted forest with +8 Aetheric tells them: bring swords, your guns will jam, the caster thrives but the forest is watching.

**Design principle:** The zone IS the challenge. A dungeon with a vertical gradient (neutral on the surface, increasingly Aetheric as you descend) forces the party to choose: do you bring the guns for the upper floors and switch to swords below? Do you leave the caster topside as a rearguard because they'd be too powerful in the basement and you want to save them? The zone makes the tactical decisions richer without adding new mechanics — it's the same Reliability and Casting math the players already know, applied spatially.

### 4.3 Dynamic Zones

Zones shift during play. This is what makes the Aetheric balance dramatic rather than static:

**Spell flooding:** A caster throwing Standard spells generates +2 accumulation per cast. Three spells in combat pushes +6. In a Neutral zone, that's enough to make firearms noticeably unreliable (−12 Reliability). The caster's own magic is transforming the battlefield.

**Exotic tech pushing back:** A force generator pulsing −2 per minute pushes the balance toward Galvanic. Run it for five minutes and you've moved the needle by −10. Pair that with two exotic weapon shots (−2 each) and you're looking at −14 — enough to meaningfully suppress casting.

**Decay as timer:** Accumulation decays at 1 per minute. A +6 Aetheric spike from combat fades to nothing in six minutes. If the party rests, the zone resets. If they push forward immediately, they're carrying the imbalance into the next encounter. This creates pacing tension: rest to reset the zone, or press on while the balance favors (or hinders) you?

**Zone recovery after major events:** A Spectacular spell (+4) in a Light Aetheric Zone (+3 baseline) pushes to +7 temporarily, decaying back to +3 over four minutes. The baseline doesn't change — it's a semi-permanent feature of the location. Only sustained, intensive activity over weeks or months shifts baselines. In-session, baselines are fixed.

### 4.4 Baseline Guidelines for Common Locations

Use this table as a starting point. Specific locations may vary — a factory built on a thin-Veil spot might be neutral instead of Galvanic.

| Location | Baseline | Why |
|----------|----------|-----|
| Open countryside | 0 | No sustained activity in either direction. |
| City street | 0 to −2 | Faint industrial hum. Barely noticeable. |
| Factory floor | −5 to −12 | Active machinery, Engine presence. |
| Power plant / foundry | −15 to −25 | Heavy Engine concentration. Magic barely functions. |
| University / library | 0 to +2 | Faint traces of scholarly magical study. |
| Old cathedral / temple | +3 to +5 | Centuries of ritual and belief soaked in. |
| Haunted manor | +5 to +8 | Aetheric residue from traumatic events. |
| Cemetery / barrow | +3 to +8 | Proximity to the Veil. Varies by age and history. |
| Wild Zone edge | +8 to +12 | The Veil is thin. Technology falters. |
| Wild Zone heart | +15 to +25+ | The Veil barely holds. Swords and sorcery only. |
| Black market Galvanic lab | −3 to −8 | Prototype testing, exotic tech storage. |
| Abandoned factory | −2 to −5 | Residual Engine resonance. Fading. |

**Zone boundaries:** The transition between zones is where the game shines. A chase from a factory district into the old quarter means firearms get worse and the enemy caster gets stronger with every block. A mansion where the basement is Aetheric (haunted) and the attic is Galvanic (experimental lab) creates a vertical gradient the party navigates. Design locations with gradients, not uniform fields.

### 4.5 Zone Boundaries as Tactical Terrain

Treat zone boundaries like walls, cover, and chokepoints — tactical features that change how encounters play out.

**Encounter design example:** A fight in a warehouse. The main floor is Neutral (0). The back room houses a humming Galvanic generator (−8). The old stone cellar has Aetheric traces (+5). Three zones in one building. The party's caster wants to fight from the cellar. The enemy gunners want to hold the Galvanic back room. The main floor is contested ground where everything kind-of works but nobody has an edge. The fight becomes a territorial struggle over which zone to control — and controlling a zone means controlling the rules.

---

## 5. Narrating Spell Effects

### 5.1 Concept-Based Adjudication

Spells in this game describe broad concepts, not narrow effects. Force doesn't say "deals 2d6 in a 15-foot cone" — it says "project raw magical force as a push, strike, or crush." The tier table gives you the mechanical numbers. The fiction is yours to shape.

**Your job as GM:** When a player casts a spell, describe what it looks like based on the concept and the tier achieved. A Weak Force is a shove that rattles furniture. A Spectacular Force is a concussive blast that cracks stone walls. Same spell, same concept, vastly different fiction.

### 5.2 Scaling Descriptions by Tier

Use this as a guideline for how to narrate spell effects:

| Tier | Scale | Sensory | Aftermath |
|------|-------|---------|-----------|
| Weak | Personal. Affects one target or a small area. | Subtle — a flicker, a whisper, a faint shimmer. Blink and you miss it. | Barely noticeable. A chill in the air, a faint smell of ozone. |
| Standard | Room-scale. Clearly affects the environment. | Obvious — a flash, a crack, an unmistakable display of power. | Noticeable residue. Scorch marks, frost, displaced objects. |
| Strong | Area-scale. Changes the scene. | Dramatic — a roar, a wave of force, light that hurts to look at. | Lasting marks. Structural damage, altered terrain, lingering effects. |
| Spectacular | Building-scale. Awe-inspiring. | Overwhelming — everyone stops. The air itself changes. Hair stands on end. | Permanent marks. Craters, fused stone, warped metal, changed landscape. |

**The key:** Tier determines the mechanical effect AND the narrative impact. A Weak Barrier is a shimmer in the air that deflects a blow. A Spectacular Barrier is a visible wall of force that cracks the ground where it anchors and hums with audible power. Match the description to the tier, and the players will feel the difference between scraping by and channeling real power.

### 5.3 Creative Spell Use

Players will propose uses for spells that aren't in the tier table. This is correct and expected — concept-based spells are designed for creative application. When a player proposes something outside the tier table:

**Three questions:**

1. **Does the spell's concept cover this?** Force moves things. It doesn't create fire, read minds, or heal wounds. If the concept doesn't cover the proposed use, the answer is no — find a different spell.

2. **What tier would this effect require?** Gauge the proposed effect against the tier scale. Using Force to shove a door open? Weak. Using Force to collapse a tunnel? Strong or Spectacular. If the required tier is higher than what the caster rolled, the effect is a reduced version.

3. **Is the proposed effect within the scope of that tier?** Check the tier table for the spell. If the proposed effect is comparable in power to what the tier already does, it works. If it's dramatically more powerful, it doesn't — the player is trying to get more than the spell offers.

**If all three pass:** The effect works as proposed.

**If the concept fits but the tier is wrong:** Offer a reduced version. "Force can't collapse the tunnel at Standard, but you could crack a support beam — it'll weaken the structure for someone else to finish the job."

**If the concept doesn't fit:** Say so clearly. "Force is kinetic energy — it pushes, strikes, and crushes. What you're describing is closer to Elemental Manipulation. Do you know that spell?"

### 5.4 Backlash as Narrative Opportunity

Backlash is not just "take 1d4 damage." It's the Aether biting back — the price of reaching into a force that doesn't belong to you. Describe backlash in terms of the spell that caused it:

| Spell Concept | Backlash Looks Like |
|---------------|---------------------|
| Force | Concussive rebound. The caster staggers as if punched. |
| Elemental Manipulation | The element turns on the caster. A fire spell scorches their hands. An ice spell frosts their breath. |
| Barrier | The barrier snaps back like a rubber band, lashing the caster with arcane whiplash. |
| Mend | The healing goes wrong. A bone sets crooked. A wound seals over infection. The body rejects the magic's guidance. |
| Wither | The entropy reflects inward. A fingernail blackens. Hair grays at the temple. A tooth loosens. |
| Detect / Reveal | Sensory overload. The caster sees too much — every magical trace in the area floods their perception at once. |
| Commune | The other side notices you. Something whispers back. |
| Sever | The severing cuts both ways. The caster feels something inside them disconnect momentarily. |

**The 25% wild effect chance** after backlash is a storytelling gift. When it triggers, something unexpected happens — the spell's power goes somewhere unintended. A Wild Effect from Force might shatter every window in the room. A Wild Effect from Commune might briefly open a two-way connection instead of one-way. These are moments that make sessions memorable. Don't treat them as punishments.

### 5.5 Maintaining Spell Scope

The temptation with concept-based spells is scope creep — players gradually expanding what a spell can do until it covers everything. Your job is to maintain the boundaries.

**Each spell does one thing.** Force moves things. Mend heals. Detect finds. The concept is broad enough to allow creative application but narrow enough to keep spells distinct from each other.

**When a player pushes scope:**
- "I use Force to stop his heart." **No.** Force is kinetic — it pushes, strikes, crushes. It can't perform surgery on internal organs. That's a different order of precision than the spell offers.
- "I use Mend to cure the plague." **No.** Mend heals physical damage — wounds, broken bones, cuts. Disease is a biological process, not damage. You'd need a different spell or a ritual.
- "I use Detect to read his thoughts." **No.** Detect finds magical presences and hidden magical effects. Thoughts aren't magical presences. That's closer to Commune territory, and Commune doesn't do that either.

**The test:** If a proposed use would make another spell obsolete, it's too broad. If Force can do what Kinesis does, why does Kinesis exist? Spell boundaries are load-bearing walls — removing one brings down the house.

---

## 6. Creating Devices on the Fly

The Galvanic oddity template from FIREARMS_EQUIPMENT.md gives you the framework. This section is about using that framework quickly, in the moment, when a player asks "is there a device that could do X?" or when you need a piece of exotic tech for an NPC or a location.

### 6.1 The Quick Creation Method

Five steps:

1. **What does it do?** One clear function. Devices do one thing.
2. **What spell does it most closely mimic?** Every Galvanic device is the Engine's answer to something the Veil provides. A ward detector mimics Detect. A force generator mimics Barrier. A healing device mimics Mend. Find the analog.
3. **Set the Galvanic rating.** The spell tier it mimics determines the rating: Weak analog = 1, Standard analog = 2, Strong analog = 3. Devices that don't actively project force (passive readers, sensors) can be rated 0.
4. **Assign Reliability.** Use the standard scale:
   - 50–60: Fragile prototype. Breaks often. Experimental.
   - 65–75: Field-ready. Works reliably under normal conditions.
   - 80+: Robust. Military-grade or well-proven.
5. **Add a drawback.** Every device has one. It's loud, it's slow, it's fragile, it requires rare fuel, it alerts things you'd rather not alert. If the device has no drawback, it needs one. If adding a drawback doesn't fix it, it shouldn't be portable.

### 6.2 The Balance Test

Before handing a device to the players, ask:

- **Does it replace a character ability?** A healing device that works as well as Mend removes the party's reason to have a healer. A detection device that replaces Detect makes that spell worthless. Devices should complement character abilities, not replace them.
- **Does it have a meaningful cost?** Galvanic rating is a cost — using the device shifts the Aetheric balance toward tech, which hurts casters and helps firearms. Reliability is a cost — the device might not work. Charges are a cost — it runs out. If a device has no meaningful cost, something is wrong.
- **Does it solve the problem too cleanly?** The best devices create new problems while solving old ones. A force generator protects against magic but alerts everyone to your position. An Aetheric Compass finds magic but can't tell you what kind. A Signal Caster works where radios fail but anyone with a receiver can intercept the message.

### 6.3 Devices as Quest Rewards and Faction Tools

Not every device is available at shops. The rarity system from FIREARMS_EQUIPMENT.md:

| Rarity | Availability |
|--------|-------------|
| Common | Specialist shops in major cities. |
| Uncommon | Faction quartermasters, specific contacts, favor-trading. |
| Rare | Black market, faction armories, expedition salvage. |
| Unique | One-of-a-kind. Built for a specific purpose. Quest reward. |

**Faction-specific devices** are one of the best quest rewards in the game. A device built by a specific faction — with their design philosophy, their limitations, their aesthetic — tells the players something about that faction every time they use it. A cult-hunter's resonance damper feels different from a university professor's Aetheric compass, even though both are Galvanic tech. The provenance matters.

---

## 7. Worked Examples

### 7.1 Social Encounter: "The Dockmaster's Favor"

**Situation:** The party needs passage on a cargo ship leaving port tonight. The dockmaster, Greaves, controls berth assignments. He's heard rumors about the party causing trouble at a warehouse (he's Unfriendly, −15%).

**Characters:** Sera (SP +2, Persuasion 3, Etiquette 2, Deception 3) and Kael (BR +2, Intimidation 2 under BR).

**Step 1 — Read the room.**

Sera's player says: "Before I approach him, I want to read the situation. What's his mood? Is he busy?"

The GM describes: Greaves is at his desk, shuffling manifests. He's got a half-eaten sandwich and a cold cup of tea. He looks up when you enter and his expression goes flat — he recognizes you, or at least knows what you are.

No roll needed. This is the GM describing the world honestly. The flat expression tells Sera he's not happy to see them.

**Step 2 — Etiquette to soften the ground.**

Sera's player: "I don't jump straight to the ask. I compliment the efficiency of his operation — the dock is well-run and I say so. I'm polite, formal, using his title."

GM calls for Etiquette. Target: ((10 + 2) × 2) + 30 = 54. No modifier for the Etiquette attempt itself — she's just being polite, not asking for anything yet.

Sera rolls 41. Success, margin 13.

GM: Greaves softens slightly. He's not warm, but the hostility drops. He grunts an acknowledgment. "What do you need?" Disposition shifts from Unfriendly (−15%) to Neutral (+0%).

**Step 3 — Persuasion for the passage.**

Sera's player: "I explain that we need berths on the Calloway's Fortune, leaving tonight. I mention that our patron, Lord Ashton, would consider it a personal favor — and Ashton remembers his friends at bonus time."

This is a good argument that addresses Greaves' self-interest. GM applies +10% for the roleplay.

Persuasion target: ((10 + 2) × 3) + 30 = 66. With +10% roleplay modifier: 76. Disposition is now Neutral, so no further modifier.

Sera rolls 52. Success, margin 24. Solid Standard-equivalent result.

GM: Greaves looks at you for a long moment, then pulls out a manifest. "Two berths. Cargo hold, not cabins. You're listed as surplus crew — means you work if the bosun says work." He's not doing this out of kindness, but Ashton's name carries weight.

**Step 4 — Deception when things get complicated.**

At the gangplank, a dock inspector asks what's in the party's sealed crate (it contains weapons they'd rather not declare).

Sera's player: "I tell him it's survey equipment for an archaeological expedition. Our patron is funding a dig in the northern territories."

GM calls for Deception vs. Empathy. The inspector is a professional — Empathy target 40.

Sera's Deception target: ((10 + 2) × 3) + 30 = 66.

Sera rolls 38 (success, margin 28). Inspector rolls 52 (fail).

One success beats one failure. The lie holds completely. GM: The inspector notes "survey equipment" on his clipboard and waves you through. He doesn't look twice.

**What if Kael had tried Intimidation instead?**

Kael's BR Intimidation target: ((10 + 2) × 2) + 30 = 54. He'd loom over Greaves and growl about consequences. Against Greaves' Resolve — say target 50 — it's an opposed check. But even if Kael wins, Intimidation creates compliance, not goodwill. Greaves would give them the berths, then report them to the harbor watch. Persuasion was the right tool here.

### 7.2 Foot Chase: "Through the Market District"

**Situation:** The party's contact, Finch, grabs a stolen document from the evidence table during an auction and bolts. Kael (PC +2, Athletics 3) gives chase. The market is crowded, and the old quarter beyond it has a Light Aetheric baseline (+3).

**Setup:** Finch starts at Near range. Both are on foot.

**Count 0 — Both Sprint.**

Kael: Sprint (speed 3, token at 3).
Finch: Sprint (speed 3, token at 3).

**Count 3 — Both resolve simultaneously.**

Both started at count 0, so simultaneous. Range doesn't change — both moved the same distance. Finch is still Near.

**GM introduces complication:** A fruit cart blocks the alley. Both need Athletics to vault it.

**Count 3 — Both declare again.**

Finch (PC +0, Athletics 2): "I try to jump the cart."
Kael (PC +2, Athletics 3): "Same — I'm right behind him."

Athletics check, speed 2 (rolled into the Sprint — total action is Sprint 3 + obstacle embedded in it; GM rules the obstacle check happens at the end of the Sprint, not as a separate action).

Kael's Athletics target: ((10 + 2) × 3) + 30 = 66. Rolls 28. Success.
Finch's Athletics target: ((10 + 0) × 2) + 30 = 50. Rolls 63. Failure. +2 count penalty on his next action.

Kael clears the cart smoothly. Finch clips the corner, staggers, scatters oranges. He's lost time.

**Count 3 — New actions.**

Kael: Sprint (speed 3, token at 6).
Finch: Sprint (speed 3 + 2 penalty = speed 5, token at 8).

**Count 6 — Kael resolves.** Kael moves one range band closer. Finch was Near; Kael is now Close. But Finch hasn't resolved yet — he's at count 8.

**Count 6 — Kael declares.** He's Close to where Finch will be when Finch's Sprint resolves. Kael declares: tackle (Brawl, speed 3, token at 9). If he catches Finch before Finch can open the gap...

**Count 8 — Finch resolves.** Finch moves one range band — from Close back to Near. But Kael's tackle is at count 9, and Finch is now at the edge of Near range.

**Count 8 — Finch declares.** Finch sees Kael lunging. Sprint again (speed 3, token at 11). If he gets to Far range before Kael's tackle resolves...

**Count 9 — Kael's tackle resolves.** Finch is Near (moved there at count 8). Kael's tackle needs Close range. He's one band short. The tackle misses — Kael is grasping at air.

**Count 9 — Kael declares.** Sprint (speed 3, token at 12).

**Count 11 — Finch resolves.** Finch is now at Far range. He's in the old quarter. **The zone shifts.** Baseline here is +3 Aetheric. If Kael draws a firearm, its Reliability drops by 6.

**GM forces resolution (approaching 12 counts).** One final opposed Athletics check.

Kael: Athletics 66. Rolls 44 (success, margin 22).
Finch: Athletics 50. Rolls 61 (fail).

Kael wins. He dives, catches Finch's coat, and they both tumble into a stack of crates in the old quarter. Chase over — now it's a Close-range confrontation. The +3 Aetheric baseline means if either of them draws a gun, it's already less reliable.

### 7.3 Exploration with Zone Tracking: "The Holloway House"

**Situation:** The party investigates a haunted manor on the city's edge. Baseline: +5 Aetheric throughout the main floors. The cellar is worse (+8). The overgrown garden is milder (+2).

**Party:** Sera (wild caster, casting target 55), Kael (swordsman, revolver Rel 95), and Marsh (investigator, semi-auto pistol Rel 85, Aetheric Compass).

**Arrival — the garden.**

Baseline +2. Marsh activates the Aetheric Compass (Galvanic Rating 0 — passive reader, no balance shift). The needle confirms a faint Aetheric presence, stronger toward the house.

Kael checks his revolver. Effective Reliability: 95 − (2 × 2) = 91. Malfunction chance 9%. Barely noticeable.

**Entering the main floor — baseline shifts to +5.**

Kael's revolver: 95 − (5 × 2) = 85. Malfunction chance 15%. One in seven. He's aware of it. Marsh's semi-auto: 85 − 10 = 75. Malfunction chance 25%. One in four. Marsh holsters the pistol and draws a knife.

Sera's casting target shifts too: 55 + (5 × 2) = 65. She's more effective here. Her normal Standard threshold (margin 11-30, meaning she needs to roll 44 or below) widens because her target is now 65 — she needs to roll 54 or below for Standard. The Aether is feeding her.

**Sera casts Detect to search for magical traps.**

Rolls d100 against casting target 65 (with the +5 zone bonus already applied). Rolls 42 — success, margin 23. Standard tier.

Standard Detect: She senses magical presences and their approximate strength within the room. The GM describes: "You feel three sources. Two are faint — old wards on the windows, probably defensive. One is stronger, beneath the floor. It pulses."

Sera pays 4 EP (Standard Mend cost — check the spell's tier table). Backlash check: 10% (Standard). Rolls 73. No backlash.

**Aetheric accumulation:** The area gains +2 (Standard tier). New net balance: +5 (baseline) + 2 (from Detect) = +7.

Kael's revolver: 95 − (7 × 2) = 81. Malfunction chance 19%. Getting worse.
Marsh's semi-auto: 85 − 14 = 71. Malfunction chance 29%. Nearly one in three.

**Time passes — searching the main floor.**

The party searches for 10 minutes. Accumulation from Detect decays: 10 minutes × 1 per minute = 10 decay. The +2 accumulation is gone after 2 minutes. They're back to baseline +5.

Kael's revolver is back to effective 85. Still not great, but manageable.

**Descending to the cellar — baseline shifts to +8.**

The Compass needle swings hard. Marsh announces: "Strong. This is a moderate Aetheric zone."

Kael's revolver: 95 − (8 × 2) = 79. Malfunction chance 21%. He's seriously considering leaving the gun holstered.
Marsh's semi-auto: 85 − 16 = 69. Malfunction chance 31%. He left it holstered two rooms ago.

Sera's casting target: 55 + (8 × 2) = 71. She's formidable down here. Her Standard range extends dramatically — she needs to roll 60 or under. Even Strong tier (margin 31-50) is achievable on a roll of 40 or under. The cellar is her territory.

**The encounter below.**

They find the source of the strong pulse: a ward circle on the cellar floor, still active, pulsing Aetheric energy. Something is contained inside it. Opening the circle is a choice — the thing inside might be dangerous, and releasing it in a +8 Aetheric zone means any magical entity will be empowered.

This is the zone doing the GM's work. The players know the math. They know their guns are unreliable down here. They know the caster is strong. They know that whatever's in the circle will be stronger too. The zone baseline created a tactical dilemma without the GM lifting a finger.

### 7.4 Improvised Device: "The Resonance Cage"

**Situation:** The party needs to capture, not kill, a magical creature that's been raiding a neighborhood. It's some kind of Aetheric predator — manifests from the Veil, feeds on residue, and vanishes when threatened. Physical weapons pass through it. Magic can hurt it but also feeds it.

A player asks: "Could we build some kind of Galvanic trap? Something that generates a field it can't pass through?"

**The GM uses the quick creation method:**

1. **Function:** Generate a localized Galvanic containment field. The creature can't cross a zone boundary into Galvanic-saturated space.

2. **Spell analog:** This is most like Circle — creates a bounded zone with specific properties. Circle is a ritual spell (30-minute casting time, Standard tier for basic containment).

3. **Galvanic rating:** Standard analog = 2. The cage generates −2 Galvanic accumulation per minute while active, creating a sustained Galvanic field within a small area (roughly a 10-foot radius).

4. **Reliability:** 55. This is a prototype — the party's engineer (Craft 3, IN +1) built it from salvaged resonance coils and a force generator battery. It works, but it's janky. Malfunction check on activation and every 10 minutes of sustained use.

5. **Drawbacks:**
   - Takes 10 minutes to set up. Must be pre-placed — no deployment in combat.
   - One-shot power source. Once activated, it runs until the battery dies (~30 minutes) or it's shut off. No recharging in the field.
   - The Galvanic pulse on activation is loud and distinctive — anything sensitive to Engine force knows exactly where you are.
   - The field affects everyone inside, including the party. Casting inside the cage is at −4 to target numbers (from the −2 Galvanic accumulation × 2).

**How it plays out:**

The party sets up the cage in the creature's territory. Sera lures the creature with a Weak spell (+1 Aetheric — the creature senses the magic and comes to feed). When it enters the cage radius, the engineer activates it.

Reliability check: d100 against 55. Rolls 33 — it fires. The cage hums to life. −2 Galvanic per minute starts accumulating.

The creature recoils from the Galvanic field. It can't cross the boundary — the Engine force is anathema to its Aetheric nature. But the cage isn't perfect: the creature can batter the field by spending its own Aetheric energy, gradually overwhelming the Galvanic accumulation. The party has maybe 10-15 minutes before the cage's Galvanic output can't keep up with the creature's Aetheric onslaught.

Now the party needs to figure out how to transport the creature before the cage fails. That's next session's problem — but the device did its job: it created a temporary solution with a clear timer and clear limitations.

**What the GM got right:**
- The device does one thing (containment).
- It has meaningful costs (setup time, one-shot, Galvanic field affects allies).
- It creates new problems (transport, time limit, alerting other threats).
- It's rooted in established mechanics (Galvanic accumulation, Reliability checks, zone effects).

---

## 8. Summary: The GM's Toolkit

| Situation | Tool | Reference |
|-----------|------|-----------|
| Should I call for a roll? | Three conditions test (§1.1) | Uncertain + consequences + not trivially resolved |
| How hard is this check? | Modifier table (§1.2) | +20% favorable to −30% severe |
| Raw capability, no skill? | Stat check (§1.4) | (5 + stat) × 10 |
| Environmental chance? | Consequence check (§1.4) | Flat %, roll d100 |
| NPC social encounter? | Disposition + social skill (§2) | −30% hostile to +30% allied |
| Chase on foot? | Timing track + Sprint (§3.2) | Speed 3 per range band |
| Vehicle chase? | Timing track + vehicle speed (§3.4) | Speed varies by vehicle |
| Track accumulation? | Tally marks (§4.1) | +tier for spells, −rating for devices |
| What's this zone's baseline? | Location table (§4.4) | 0 neutral to ±25 extreme |
| Player wants creative spell use? | Three questions test (§5.3) | Concept + tier + scope |
| Need a device on the fly? | Quick creation method (§6.1) | Function → analog → rating → reliability → drawback |
