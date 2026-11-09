# Combat Procedure

## Document Status: DRAFT — Playtest Ready
**Last Updated:** 2026-03-31

This is the unified combat reference. It pulls together mechanics from PROJECT_SPEC.md (timing track, weapons, armor, death spiral), MAGIC_SYSTEM.md (casting, backlash, exhaustion), and FIREARMS_EQUIPMENT.md (malfunction, accumulation) into a single step-by-step procedure.

---

## 1. Starting Combat

When a situation turns violent — or when timing and sequencing matter — the GM calls for the timing track.

1. **GM sets the scene.** Describe the environment, distances (close / near / far — see §8), lighting, cover. Players and NPCs declare their current state (weapon drawn? spell ready? hands full?).
2. **Place the marker at count 0.** This is the timing track's starting point.
3. **Everyone declares their first action simultaneously.** Players state what they're doing; GM decides for NPCs. No one has seen anyone else act yet — you're reacting to the situation, not to each other.
4. **Place tokens.** Each participant places a token on the count when their action will **complete** (current count + action's speed). A character drawing a weapon (speed 2) from count 0 places their token at count 2.
5. **Advance the track.** The GM moves the marker forward count by count. When it reaches a token, that action resolves.

### Simultaneous Resolution

If multiple tokens land on the same count, resolve in this order:
1. **Whoever started their action first** resolves first.
2. If actions started on the same count, resolve **simultaneously** — both attacks land, both spells fire. Neither reacts to the other.

### Declaration Order

When multiple characters need to declare new actions on the same count (after their previous actions resolved simultaneously), they declare in order of **PC (Physical Coordination), lowest first.** Ties broken by **AW (Awareness), lowest first.** If still tied, simultaneous declaration.

This means faster, more perceptive characters **declare last** — they see what slower opponents are committing to before choosing their own action. This is a significant tactical advantage and a reason to invest in PC and AW.

*Example: Kael (PC +2, AW +1) and a thug (PC +0, AW -1) both resolve at count 5. The thug declares first (PC +0). He's pulling a knife. Kael sees this and declares his response — maybe he goes for the hunting knife, maybe he takes a step back and draws his revolver. The thug is committed; Kael gets to react.*

### Cancelling an Action

A character can abandon their current action at any time before it resolves. They immediately declare a new action, but it costs **+1 count penalty** added to the new action's speed. The counts already spent on the cancelled action are lost.

*Example: You declared a Heavy weapon swing (speed 7) at count 0, token at 7. At count 3, you see a caster beginning a spell. You cancel the swing (3 counts lost) and declare a Small weapon quick strike (speed 2 + 1 penalty = 3). New token at count 6.*

---

## 2. Actions in Combat

### 2.1 Attack (Melee)

**Skill:** Melee (BR-based) for weapons, Brawl (BR-based) for unarmed.

**Speed:** Per weapon category (see weapon tables below).

**Procedure:**
1. Declare attack and target.
2. Place token at current count + weapon speed.
3. When token resolves: roll d100 against your skill target number.
4. **Hit:** Roll equal to or under your target number → proceed to damage (§4).
5. **Miss:** Roll over your target number → the attack misses. Action spent.
6. **Critical hit:** Roll within your crit range → double damage dice before adding modifiers.
7. **Critical miss (00):** Weapon fumble — GM adjudicates (dropped weapon, off-balance, hit an ally, etc.).

### 2.2 Attack (Ranged — Martial)

**Skill:** Ranged (PC-based) — bows, crossbows, thrown weapons.

**Speed:** Per weapon category. Bows can fire again immediately; crossbows require reload time.

**Procedure:** Same as melee, plus:
- **Range modifiers:** Close range: no modifier. Near range: no modifier. Far range: -10% to hit (unless weapon has the Accurate tag).
- **Firing into melee:** -10% to hit. On a miss within the penalty range, the shot hits the nearest ally in the melee (GM adjudicates).
- **Reload:** After spending all Capacity, the weapon requires its Reload speed in counts before firing again. Place a reload token; when it resolves, the weapon is ready.

### 2.3 Attack (Firearms)

**Skill:** Firearms (PC-based) — every gun, conventional and Galvanic.

**Speed:** Per firearm category.

**Procedure (two-step: Reliability, then skill):**

1. **Reliability check — does it fire?** Roll d100 under the weapon's effective Reliability. **Every shot, every time.** Roll over and the weapon fails — shot doesn't fire, action spent. Roll d10 on the Malfunction Severity table (§6). (Malfunction chance is therefore 100 − effective Reliability.)
2. **If it fires — roll Firearms to hit.** Same as any ranged attack: d100 under skill target.

**Effective Reliability** = Base Reliability − (net balance × 2)

The balance affects both sides: net Aetheric reduces Reliability, net Galvanic increases it. At effective Reliability 100+ (0% malfunction), the weapon cannot fail. At effective Reliability 0 or below (100% malfunction), the weapon simply does not function.

**Ammo tracking:** Each shot (or burst for Burst-tagged weapons) consumes ammo from Capacity. When empty, reload.

### 2.4 Cast a Spell

**Skill:** Casting target number (see MAGIC_SYSTEM.md).

**Speed:** Fixed per spell. Each spell has a single casting time regardless of tier. Tier measures how much power the caster draws, not how long it takes — a bigger effect doesn't take more time, just more energy. Casting time is a per-spell balancing lever: Force is fast (2 counts), Sever is slow (8 counts), Mend is in between (5 counts).

**Procedure:**
1. Declare the spell. Place token at current count + the spell's casting time.
2. When token resolves: roll d100 against your casting target number.
3. Determine tier achieved based on roll margin (1-10 under = Weak, 11-30 = Standard, 31-50 = Strong, 51+ = Spectacular).
4. **Scholarly casters** feel the surge and choose: accept the tier rolled, or **restrict down** to any lower tier. Want to save exhaustion? Take Weak even though you rolled Strong.
5. **Wild casters** ride the wave — they get what they get. The magic gives and you take it. No choice, no restriction.
6. Apply the spell's effect at the final tier.
7. Pay exhaustion cost for the tier used (deduct from EP).
8. Roll backlash check — percentage chance based on tier (Weak 5%, Standard 10%, Strong 15%, Spectacular 25%). Checked on every cast (success or misfire). On failure: 1d4 physical damage + 25% chance of Wild Effect. Wild effect residue persists until long rest after effect fades — same number while residue present = escalation.
9. Apply Aetheric accumulation to the area (Weak +1, Standard +2, Strong +3, Spectacular +4).

> **Design Note:** Fixed casting times mean wild and scholarly casters follow the same timing rules. The difference is purely what happens at resolution — control vs. chaos. A wild caster throwing Force might get a Weak puff or a Spectacular blast; the casting *time* is the same either way. This also makes spell design cleaner: a spell's casting time is an independent balance lever from its tier effects.

**Spell cancellation:** Cancel mid-cast at any time before resolution. Pay **half the Weak tier's exhaustion cost** for that spell. 10% chance of backlash (1d4 damage, burn only — no wild effect check). Fixed, predictable, easy to remember — the narrative is that some power was already flowing when you cut it off, but you cut it before it could warp you.

**Casting interruption:** If a caster takes damage while casting (between declaration and resolution), they must make a **concentration check**: roll d100 under their (PW + 4) × 10. Failure means the spell fizzles — treat as cancellation (half Weak tier cost, 10% backlash chance). The caster may choose to voluntarily abort instead of rolling.

> **PLAYTEST NOTE:** Concentration check mechanics are provisional. (PW + 4) × 10 means a PW +2 caster needs to roll under 60 — concentration is hard under fire. This may need tuning. Should damage amount affect the check? For now, keep it simple: any damage = one check, flat target.

### 2.5 Defend (Active Defense)

A character who is **not currently mid-action** (no token on the track, or their token already resolved this count) can attempt to actively defend against an incoming attack.

**Skill:** Melee, Brawl, or Athletics (defender's choice based on how they describe the defense — parrying with a weapon, ducking, diving aside).

**Procedure:**
1. Attacker hits (rolls under their skill target).
2. Defender declares active defense.
3. **Opposed check:** Defender rolls d100 against their chosen defense skill. Compare margins — attacker's hit margin vs. defender's defense margin. Larger margin wins.
4. **Defender wins:** Attack is deflected, dodged, or parried. No damage.
5. **Attacker wins:** Attack lands normally. Proceed to damage.
6. **Both fail:** This can't happen (attacker already hit). If the defender fails their roll, the attack lands.

**Cost:** Active defense consumes your **next action's timing.** Add +2 counts to your next declared action (you're recovering from the dodge/parry). If you have no pending action, you're free to act normally on your next turn but you still take the +2 penalty on whatever you declare.

**Restrictions:**
- You can only actively defend **once per count.** Multiple attackers on the same count means you pick one to defend against.
- You cannot actively defend while mid-action (token on the track, not yet resolved). You committed — you're swinging, reloading, casting. You can't also dodge. Cancel your action first (with the +1 penalty), then defend.
- The **Parrying** weapon tag gives +10% to your defense roll when using Melee to defend.
- Shields add their matching rating to passive damage reduction (§4) — they don't require an active defense roll. But a character *can* actively defend with a shield using Athletics, representing a deliberate block.

> **Design Note:** Active defense is a tradeoff. It can save you from a big hit, but it costs you tempo on the timing track. Defender-heavy play slows you down; aggressor-heavy play means eating hits. This mirrors real combat and the OSR ethos — don't get hit in the first place by controlling the fight.

### 2.6 Other Actions

| Action | Speed | Notes |
|--------|-------|-------|
| Draw a weapon | 2 | Concealable weapons: speed 1 |
| Shout a command | 1 | Free communication |
| Pick up an item | 2 | Off the ground nearby |
| Toss / hand off an item | 1 | To adjacent ally |
| Throw a weapon | Weapon speed +2 | One die step lower damage (Throwable tag) |
| Open / go through a door | 2 | Closed, unlocked |
| Drink a vial / potion | 3 | Must be in hand |
| Retrieve from belt / pocket | 2 | Quick-access items |
| Retrieve from sack | 3 | Bag, satchel, loose container |
| Retrieve from backpack | 9 | Rummaging |
| Mount a horse | 5 | |
| Light a torch | 5 | |
| Light a lantern | 6 | |
| Climb 10' ladder | 6 | |
| Climb 10' rope | 10 | |
| Take cover | 2 | Move to nearby cover (see §8) |
| Stand up from prone | 2 | |
| Reload (firearm) | Per weapon | See firearm tables |
| Reload (crossbow) | Per weapon | Light: 3, Heavy: 5 |
| Sprint | 3 | Move one range band (see §8) |

---

## 3. The Attack Roll

All attacks use the same resolution: **d100 roll-under** against the relevant combat skill target number.

**Skill target number:** ((10 + stat modifier) × skill level) + 30

**Modifiers** (cumulative):

| Situation | Modifier |
|-----------|----------|
| Target in cover (partial) | -10% |
| Target in heavy cover | -20% |
| Target prone (melee) | +10% |
| Target prone (ranged) | -10% |
| Firing into melee | -10% |
| Far range (ranged/firearms) | -10% |
| Aimed shot (spend +2 speed) | +10% |
| Wound penalty (Harmed) | -10% |
| Wound penalty (Maimed) | -25% |
| Wound penalty (Incapacitated) | -50% |
| Exhaustion penalty | Stacks with wound penalty |
| Hinder (armor) | -per-point to physical skill rolls (see §5) |

**Critical hits:** Double all damage dice before adding flat modifiers. Crit range = your target, plus one more number per 25-point bracket above the first, counted down from the target (1-25: target only; 26-50: 2 numbers; 51-75: 3; 76-99: 4).

**Critical miss (00):** Always misses. GM describes a fumble — dropped weapon, stumble, friendly fire, broken string, jammed mechanism.

---

## 4. Damage & Soak

When an attack hits:

### Step 1 — Roll Damage
Roll the weapon's damage dice. On a critical hit, double the dice (not flat modifiers).

### Step 2 — Apply Armor Soak
Armor has two soak ratings. **Ballistic** absorbs firearms and other high-velocity projectiles; **Martial** absorbs blades, clubs, claws and the rest of melee. Use whichever matches the attack and subtract it from the damage. Shields add their rating of the same kind (worn armor + held shield = total soak).

**Minimum damage:** If soak reduces damage to 0 or below, the attack is absorbed. No damage dealt.

### Step 3 — Apply Remaining Damage to HP
Subtract remaining damage from the target's current HP. Track which wound tier they've entered (see §5).

### Step 4 — Check Armor Degradation
If the raw damage (before soak) **exceeded** the rating that applied, the armor takes a hit. Roll d100:
- **25 or under:** That rating is **permanently reduced by 1.**
- **Over 25:** Armor holds. No degradation.

One check per hit that exceeds the relevant soak. Simple, no math — did the blow punch through? 25% chance something cracked.

*Example: Chainmail (Martial 5) takes 8 raw damage from a mace. Damage exceeded its Martial rating, so roll degradation. Rolls 14 — degradation. Chainmail drops to Martial 4. Still functional, but wearing down.*

> **Crushing tag:** Degradation chance is **50%** instead of 25%. Maces, warhammers, and morning stars wreck armor. Roll 50 or under = lose 1 point of Martial soak.

> **Piercing tag:** Ignores 2 points of **Martial** soak. The rating is reduced by 2 for damage calculation only, not for degradation — the armor is bypassed, not damaged.

> **Design Note (pre-split figures):** These simulations predate the Ballistic/Martial split and treated armor as one rating. Tested over 10 hits: chainmail vs. a medium melee weapon averages Soak 3.6/5 (degrades but survives the fight). Vs. a revolver, averages 3.0/5 (firearms noticeably wear it down). Half plate vs. a rifle averages 6.1/8 (heavy armor holds up but takes chips). Light armor against weapons that outclass it still crumbles fast — leather vs. a short sword is 58% destroyed after 10 hits. The right armor for the right threat matters.

---

## 5. Wounds & the Death Spiral

### 5.1 Hit Points & Wound Tiers

**HP per tier:** 7 + BR

A character has four wound tiers. Each tier is a separate HP pool of equal size. Damage fills them top to bottom.

| Tier | Status | Penalty | Condition |
|------|--------|---------|-----------|
| 1 | OK | None | Full fighting capacity |
| 2 | Harmed | -10% to all rolls | Bloodied, bruised, hurting |
| 3 | Maimed | -25% to all rolls | Serious injury, visibly wounded |
| 4 | Incapacitated | -50% to all rolls | Barely functional, one hit from death |

**Beyond Incapacitated:** When a character takes damage that would reduce them below 0 HP in the Incapacitated tier → **death saves** (see §5.3).

### 5.2 Stacking Penalties

Wound penalties and exhaustion penalties **stack.**

| Wound | Exhaustion | Total Penalty |
|-------|------------|---------------|
| Harmed (-10%) | OK | -10% |
| Harmed (-10%) | Wearied (-10%) | -20% |
| Maimed (-25%) | Wearied (-10%) | -35% |
| Maimed (-25%) | Drained (-25%) | -50% |

At -50%, your skill target of 60 becomes 30. You're rolling to succeed at all, not rolling to do well. This is the death spiral working as intended — getting hurt makes you worse, which makes you more likely to get hurt again. The lesson: don't get hit.

### 5.3 Death Saves

When reduced past Incapacitated, the character is **Dying.** They collapse and cannot act.

**Every 3 counts** on the timing track, they roll d100:
- **Under 50:** Holding on. Still dying, but stable this check.
- **Over 50:** Condition worsens. After **3 failed rolls**, the character dies.
- **01:** Stabilize — no longer dying, but unconscious at 0 HP in the Incapacitated tier.
- **00:** Dead immediately.

The fastest possible death is **9 counts** (three checks, three failures). That's enough time for an ally to cancel their current action, sprint to you, and attempt first aid — tight, but possible. More typical: 12-18 counts of dying before death, giving the party a realistic window to intervene.

**Ally intervention:**
- **Medicine check** (speed 5): Success stabilizes the dying character. They're unconscious at 0 HP Incapacitated.
- **Mend spell:** Healing restores HP normally. If it pushes them above 0 in Incapacitated, they regain consciousness. Remember: casting Mend takes time on the timing track and generates Aetheric accumulation.
- **Healing potion** (speed 3, must be in hand): Force-fed to the dying character. Restores HP per potion strength.

> **Design intent:** Death should be possible but not instant. The 3-count interval gives allies a genuine rescue window — they might need to cancel an action (+1 penalty), sprint (3 counts), and apply Medicine (5 counts) = roughly 9-10 counts. That's a close race against the death clock, which is exactly the tension we want. The flat 50/50 is intentionally simple — it may evolve into something tied to BR after playtesting.

### 5.4 Hinder

Armor with a **Hinder** value imposes penalties to physical actions:

- **-5% per Hinder point** to rolls using PC (Coordination) and to Athletics, which covers swimming and climbing.
- **+1 speed per Hinder point** to all spellcasting (the encumbrance disrupts somatic components and concentration).
- Hinder does **not** affect Melee, Brawl, BR-based rolls, or mental/social skills. Ranged is exempt despite being PC-based — a bow is drawn with the shoulders, not the wrists. Firearms, also PC-based, is not exempt.

| Armor | Hinder | Effect |
|-------|--------|--------|
| Half Plate | 1 | -5% to agility skills, +1 casting speed |
| Full Plate | 2 | -10% to agility skills, +2 casting speed |
| Kite Shield | 1 | -5% to agility skills, +1 casting speed |
| Knight Shield | 2 | -10% to agility skills, +2 casting speed |

Hinder from armor and shield **stacks.** Full Plate + Knight Shield = Hinder 4 (-20% agility, +4 casting speed). You're a walking fortress that casts slowly.

---

## 6. Malfunction Checks (Firearms in Combat)

### 6.1 When to Check

The Reliability check happens **before** the Firearms skill roll. The weapon has to work before your aim matters. **Every shot, every time.**

### 6.2 The Check

Roll d100 under the weapon's **effective Reliability**. Under, it fires; over, it fails. Malfunction chance is therefore 100 − effective Reliability.

**Effective Reliability** = Base Reliability − (net balance × 2)

The balance affects both directions: net Aetheric makes guns worse, net Galvanic makes them better. At effective Reliability 100+ (malfunction chance 0%), the weapon cannot fail. At effective Reliability 0 or below (malfunction chance 100%+), the weapon simply does not function.

*Example: Revolver (Rel 95) in clean air = 5% malfunction chance. One in twenty. At +10 Aetheric: effective Rel 75, 25% malfunction. Getting dicey. At −5 Galvanic: effective Rel 105, 0% — can't malfunction.*

### 6.3 Malfunction Severity

On malfunction, the shot does not fire (action wasted). Then roll d10:

| d10 | Result | Effect |
|-----|--------|--------|
| 1-5 | **Click** | Nothing additional. Weapon is fine, just didn't fire |
| 6-7 | **Jam** | Clearing takes the weapon's full Reload time in counts |
| 8 | **Misfire** | Round goes somewhere unintended. GM determines where |
| 9 | **Mechanical Failure** | Weapon non-functional until repaired (out of combat, Craft or Engineering check) |
| 10 | **Catastrophic** | Weapon destroyed. Wielder takes 1d6 damage |

**Exotic escalation:** Exotic weapons add +1 to the d10 severity roll (max 10).

### 6.4 Accumulation in Combat

Track Aetheric accumulation as spells are cast during the fight. Each **successful** spell adds accumulation equal to its achieved tier (Weak +1, Standard +2, Strong +3, Spectacular +4). **Failed casts (fizzles) generate no accumulation** — the magic didn't manifest, so it doesn't leave a mark. Misfires also generate 0. This accumulation persists — it stacks through the fight and decays at 1 per minute after casting stops.

In a fight with active casters, firearms become progressively less reliable as the scene goes on. Smart fighters act early with firearms and switch to melee as accumulation climbs.

---

## 7. Spell Interruption in Combat

Spells take time on the timing track. Between declaration and resolution, a caster is **vulnerable.**

### 7.1 Interrupting a Cast

If a caster takes **any damage** while their casting token is on the track (not yet resolved), they must make a concentration check:

**Roll d100 under (PW + 4) × 10.**

- **Success:** Spell continues. Resolves normally when the token is reached.
- **Failure:** Spell fizzles. Treat as cancellation — pay half the Weak tier's exhaustion cost, 10% chance of backlash.

The caster can **voluntarily abort** instead of rolling concentration, taking the cancellation costs.

### 7.2 Tactical Implications

- Fast weapons (Small melee: speed 2, Holdout pistol: speed 2) can interrupt casters before big spells resolve.
- Slow spells (Sever: 8 counts) create wide interruption windows. Fast spells (Force: 2 counts) are harder to disrupt.
- Protecting your caster while they cast is a real tactical role.
- (PW + 4) × 10 means a PW +3 caster holds concentration 70% of the time — dependable but never safe. A PW +1 caster at 50% is a coin flip. Casting in the open during a fight is always risky.

---

## 8. Range & Positioning (Theater of the Mind)

No grid, no measurements. Distances are described in **narrative range bands:**

| Band | Description | Means |
|------|-------------|-------|
| **Close** | Within arm's reach | Melee range. Can touch, grapple, stab |
| **Near** | A few steps away, same room | Can close to melee as a free move, folded into the attack. Ranged attacks at no penalty |
| **Far** | Across a large room, down a street | Ranged attacks at -10% (unless Accurate). Closing takes a Sprint (speed 3) to reach Near |
| **Distant** | Across a field, rooftop to street | Only Accurate ranged weapons and rifles. -20%. Multiple sprints to close |

**Movement:** Moving within Near range is free (folded into your action). Closing from Far to Near or retreating from Near to Far costs a **Sprint** (speed 3 action on the timing track). You can attack and move in the same action only if you start Near and close to Close — the final step is part of the attack.

**Cover:** Part of the scene description, not a movement action. The GM establishes what cover exists. Taking Cover (speed 2) moves you behind something nearby. Partial cover: -10% for attackers to hit you. Heavy cover: -20%.

**Scatter tag interaction:** Shotguns and scatter weapons deal +1d6 at Close range, -1d6 at Far range.

---

## 9. Healing & Recovery

### 9.1 In Combat

**Medicine skill check (speed 5):** Stabilize a Dying character (see §5.3). Can also be used to perform field treatment on a wounded ally — success restores 1d4 HP. One Medicine check per patient per scene.

**Mend spell:** Heals per the spell's tier table. Casting time and exhaustion costs apply normally. Healing in combat means your healer is spending counts casting instead of fighting — and generating Aetheric accumulation.

**Potions/vials (speed 3):** If the setting includes healing potions, drinking one takes 3 counts and must be in-hand.

### 9.2 After Combat

**Short rest (minutes):** Catch your breath, bandage wounds. Medicine check on each wounded character: success restores 1d4 HP per wound tier entered. One check per character.

**Full rest (hours):**
- **Physical damage:** Recover 1d4 HP per hour of full rest.
- **Exhaustion:** Recover 1d8 EP per hour of full rest.
- **Medical treatment bonus:** A character receiving care from someone with Medicine skill recovers an additional 1d4 HP per hour.

### 9.3 Armor Repair

Degraded armor can be repaired with a **Craft check** (Engineering for ballistic weave and exotic plate) and appropriate tools/materials. This is a downtime activity, not a combat action. GM sets difficulty based on the extent of damage.

---

## 10. Combat Round Example

> **Setup:** Kael (gunfighter, BR +1, PC +2, Firearms 66, revolver with the Reliable tag, leather jacket Ballistic 0 / Martial 1, 8 HP per tier) and Sera (wild caster, PC +0, AW +0, casting target 64, 6 HP per tier) are caught in an alley by two thugs with revolvers (Firearms 50, Reliability 95, 7 HP per tier, no armor). Range: Near. No prior Aetheric accumulation.

**Count 0 — Declarations (first exchange, all simultaneous):**
- Kael: draws his revolver (speed 2, token at 2)
- Sera: begins casting Force (casting time 2, token at 2)
- Thug A: fires revolver at Kael (speed 3, token at 3)
- Thug B: fires revolver at Sera (speed 3, token at 3)

**Count 2 — Kael and Sera resolve simultaneously.** Both started at count 0, so neither reacts to the other.
- **Kael's draw:** the revolver clears his jacket. Nothing else happens this count.
- **Sera's Force:** she rolls 2d100 — a 46 and an 82, against her target of 64. The 46 is 18 under, the 82 is 18 over; equal distance, so she takes the 46. Margin 18 → Standard tier. Her target of 64 sits in the 51-75 bracket, so she could suppress two tiers, but Standard Force does 2d6 and she wants it. Targets Thug B: 2d6 = 8 damage. She pays 4 exhaustion. Backlash check: 15% at Standard for a wild caster (base 10% + 5%) — rolls 67, no backlash. The area gains +2 Aetheric accumulation.

**Count 2 — New declarations.** Sera (PC +0) declares before Kael (PC +2), so Kael sees her commit first.
- Sera: another Force, this time at Thug A (casting time 2, token at 4).
- Kael: a shot at Thug A as well (speed 3, token at 5). Better to finish one man than wing two.

**Count 3 — Both thugs fire.** Both started at count 0, so they resolve simultaneously. The area is at +2 Aetheric, so a plain revolver is at effective Reliability 95 − 4 = 91.
- **Thug A at Kael:** Reliability check — rolls 44 under 91, the revolver fires. Firearms roll: 44 against skill 50. Hit. Damage 2d6 = 7. That's a firearm, and Kael's leather jacket is Ballistic 0 — no protection at all against a bullet. Kael has 8 HP in his OK tier; 7 in leaves 1 before Harmed. He badly wants a ballistic vest.
- **Thug B at Sera:** Reliability check — 38 under 91, fires. Firearms roll: 71 against skill 50. Miss. The bullet sparks off the alley wall.

**Count 3 — New declarations.** Only the thugs need to choose; Kael and Sera are already committed. They are tied on PC +0 and AW −1, so they declare simultaneously.
- Thug A: fires again at Kael (speed 3, token at 6).
- Thug B: took 8 damage — 7 filled his OK tier and 1 overflowed into Harmed, so he's at −10%. Fires at Sera anyway (skill now 40, token at 6).

**Count 4 — Sera's second Force.** She rolls a 49 and a 93. The 93 is farther from 64 (29 away against 15), and a wild caster takes the farther die. That's over her target: misfire. The Force rebounds — she pays 2 exhaustion and takes 1d6 = 3 damage as the blast throws her back into the wall. Half her OK tier, gone. A failed cast generates no accumulation, so the area stays at +2.

*This is the wild caster's bargain: every spell in your schools, and dice that can turn on you.*

**Count 4 — Sera declares.** She scrambles for the coal bin behind her (Take Cover, speed 2, token at 6).

**Count 5 — Kael fires.** Reliability first. The balance is +2, so a plain revolver sits at 91 — but Kael's has the Reliable tag, worth +5 in magic-touched air, for an effective 96. He rolls 93. A thug's revolver would have clicked on that roll; Kael's fires. Firearms roll: 22 against 66. Hit, margin 44. Crit range check: a target of 66 is in the 51-75 bracket, so he crits on 64, 65 or 66 — a 22 is not one of them. Damage 2d6 = 7. Thug A has no armor, and 7 fills his OK tier exactly. One more hit and he's hurting.

**Count 5 — Kael declares.** Another shot at Thug A (speed 3, token at 8).

**Count 6 — Three tokens resolve.** The thugs started their shots at count 3; Sera started her dive at count 4. Whoever started first goes first, so the shots land before she reaches cover.
- **Thug A at Kael:** Reliability 61 under 91, fires. Firearms roll 61 against 50. Miss.
- **Thug B at Sera:** Reliability 55 under 91, fires. Firearms roll 55 against 40 (wound penalty). Miss.
- **Sera reaches the coal bin.** Partial cover: −10% for anyone shooting at her from here.

**Post-count 6:** Accumulation is still +2 and decaying. Kael is one point from Harmed, Sera is three points from Harmed and down 6 exhaustion, Thug A is at the edge of his OK tier and Thug B is already in Harmed. Nobody has reloaded yet — Kael has five rounds left in six, and a revolver takes 3 counts to fill.

---

## 11. Quick Reference — Weapon Tables

> These tables are a copy for play. Melee and martial ranged come from PROJECT_SPEC.md §4.2; firearms and exotics from FIREARMS_EQUIPMENT.md §3. Those files are the source — if a number here disagrees with them, they win.

### Melee Weapons

| Category | Speed | Damage | Examples |
|----------|-------|--------|----------|
| Unarmed | 2 | 1d3+BR | Punch, kick, headbutt |
| Small | 2 | 1d4 | Knife, dagger, stiletto |
| Light | 3 | 1d6 | Short sword, hatchet, club, rapier |
| Medium | 5 | 1d8+1 | Longsword, mace, saber, spear |
| Heavy | 7 | 1d10+1 | Bastard sword, morning star, war flail |
| Great | 9 | 2d6 | Greatsword, halberd, great axe |

### Ranged Weapons (Martial)

| Category | Speed | Damage | Reload | Examples |
|----------|-------|--------|--------|----------|
| Light Ranged | 5 | 1d6 | — | Short bow, sling |
| Medium Ranged | 7 | 1d8+1 | — | Composite bow, longbow |
| Light Crossbow | 7 | 2d6 | 3 | Hand crossbow |
| Heavy Crossbow | 10 | 3d6 | 5 | Heavy crossbow, arbalest |

### Firearms (Modern)

| Category | Spd | Damage | Cap | Reload | Rel | Examples |
|----------|-----|--------|-----|--------|-----|----------|
| Holdout Pistol | 2 | 1d6 | 2 | 2 | 95 | Derringer, pocket pistol |
| Revolver | 3 | 2d6 | 6 | 3 | 95 | Colt, Webley |
| Semi-Auto Pistol | 3 | 2d6 | 8 | 2 | 85 | Browning, Luger |
| Heavy Pistol | 4 | 2d8 | 6 | 3 | 90 | Magnum, hand cannon |
| Rifle | 6 | 2d10 | 5 | 4 | 95 | Bolt-action, Mauser |
| Carbine | 5 | 2d8 | 8 | 5 | 90 | Lever-action |
| Shotgun | 4 | 3d6 | 2 | 2 | 95 | Break-action, coach gun |
| Combat Shotgun | 5 | 3d6 | 5 | 4 | 85 | Pump-action, trench gun |
| Submachine Gun | 5 | 3d6 | 50 | 3 | 70 | Tommy gun, MP18 |

### Firearms (Exotic)

| Category | Spd | Damage | Cap | Reload | Rel | Galv | Examples |
|----------|-----|--------|-----|--------|-----|------|----------|
| Exotic Pistol | 3 | 1d10 | 12 | 2 | 70 | 1 | Flechette gun, needle gun |
| Exotic Sidearm | 4 | 2d8 | 6 | 3 | 65 | 2 | Arc gun, voltaic pistol |
| Exotic Heavy | 7 | 3d8 | 3 | 5 | 55 | 3 | Aether lance, lightning cannon |
| Exotic Melee | 2 | 1d8+BR | 10 | — | 60 | 1/charge | Shock gauntlet, voltaic blade |

### Armor

| Type | Ballistic | Martial | Hinder |
|------|-----------|---------|--------|
| Cloth | 0 | 0 | — |
| Heavy Cloth | 0 | 1 | — |
| Leather Jacket | 0 | 1 | — |
| Leather | 0 | 2 | — |
| Trench Coat (lined) | 1 | 2 | — |
| Scale | 1 | 3 | — |
| Chainmail | 2 | 5 | — |
| Steel Breastplate | 5 | 6 | 1 |
| Ballistic Vest | 8 | 2 | — |
| Half Plate | 3 | 8 | 1 |
| Full Plate | 4 | 12 | 2 |

### Shields

| Shield | Ballistic | Martial | Hinder |
|--------|-----------|---------|--------|
| Wood Buckler | 0 | 2 | — |
| Steel Buckler | 1 | 3 | — |
| Wood Shield | 0 | 5 | — |
| Infantry Shield | 2 | 7 | — |
| Kite Shield | 3 | 9 | 1 |
| Knight Shield | 4 | 10 | 2 |

---

## 12. One-Page Combat Cheat Sheet

```
COMBAT FLOW
═══════════════════════════════════════════════════════
1. GM sets scene → range bands, cover, lighting
2. All declare actions simultaneously
3. Place tokens: current count + action speed
4. Advance track → resolve tokens in order
5. Repeat from step 2 after resolution

ATTACK: d100 ≤ skill target = hit
  Crit range: 1/2/3/4 numbers by 25-pt bracket, counted down from target
  00 = always fumble │ 01 = always crit │ Crit = double damage dice

ACTIVE DEFENSE: opposed check vs attacker's margin
  Cost: +2 speed on next action │ 1 per count │ Can't defend mid-action

DAMAGE: roll dice → subtract Ballistic (guns) or Martial (melee) soak → HP
  Degradation: damage > that rating? Flat 25% chance, lose 1 (Crushing: 50%)

MALFUNCTION: d100 > effective Reliability = malfunction
  Eff. Reliability = Base − (net balance × 2)
  Severity: d10 → 1-5 click, 6-7 jam, 8 misfire, 9 broken, 10 boom

WOUNDS          EXHAUSTION          RANGE BANDS
OK: —           OK: —               Close: melee
Harmed: -10%    Wearied: -10%       Near: same room
Maimed: -25%    Drained: -25%       Far: -10% ranged
Incap: -50%     Overwhelmed: -50%   Distant: -20%, rifles only
                Penalties STACK

DYING: every 3 counts, d100 → over 50 = fail → 3 fails = dead
  01 = stabilize │ 00 = instant death │ Medicine (spd 5) stabilizes
  Fastest death: 9 counts │ Typical: 12-18 counts

CASTING: fixed speed per spell (not per tier)
  Tier = power drawn, not time │ Scholarly restrict down, Wild ride it out
  Cancel: half Weak tier cost, 10% backlash │ Concentration: (PW+4)×10

DECLARATION ORDER (same-count): lowest PC declares first, ties by AW
  Better stats = declare last = see what opponents commit to

ACCUMULATION: each spell adds tier value (W1/S2/St3/Sp4)
  Decays 1/minute │ Firearms degrade 2% per point

HINDER: -5% per point to PC/Athletics/Stealth/Swim
  +1 casting speed per point
```

---

## 13. Open Questions for Playtesting

1. **Active defense balance** — Is +2 speed cost enough? Too much? Should shields grant free defense once per round?
2. **Concentration check ((PW + 4) × 10)** — Range is 10% (PW -3) to 70% (PW +3). Does this properly reward PW investment at character creation?
3. **Death save threshold (50/50)** — Should BR modify the threshold? Should damage severity affect it? The 3-count interval feels right but the 50/50 split is arbitrary.
4. **One-roll vs. two-roll malfunction** — The sidebar suggests using the attack roll as the malfunction check too. Playtest both and see which feels better at the table.
5. **Firing into melee** — -10% and hitting allies on near-miss. Does this feel right or should it be harsher/softer?
6. **Active defense vs. ranged** — Can you dodge a bullet? Currently yes (Athletics). Should firearms be un-dodgeable, or is the +2 speed cost enough penalty for the narrative stretch?
7. **Hinder affecting casting speed** — Does +1-2 speed per Hinder point feel right, or should plate armor casters just not exist?
8. **Sprint speed (3)** — Does closing from Far to Near feel right at 3 counts? That's same speed as a revolver shot — you eat a bullet on the way in. Intentional?
9. **Accumulation tracking granularity** — Is per-spell tracking manageable at the table, or should it be simplified to "light/moderate/heavy casting" thresholds?
10. **Fixed casting times per spell** — Casting times are assigned for every spell in SPELL_COMPENDIUM.md (appendix). Current spread: Force 2, Mend 5, Sever 8, rituals off the track. Does the 2-8 count range hold up at the table?
