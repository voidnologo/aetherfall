# Economy & Resource System

The economy exists to make adventures more interesting — not to simulate a financial system. Characters need to feel the weight of their economic position (who they can talk to, where they can go, what they can carry) without anyone at the table tracking a ledger. The system tracks *access*, not *balance*.

---

## 1. Research & Inspiration

Before designing Aetherfall's economy, we surveyed ten RPG systems that take varying approaches to wealth and resource tracking. This section documents what each system does, what we learned, and how it influenced our design.

### 1.1 Systems Surveyed

#### Blades in the Dark — Coin, Stash, and Crew Tier

Blades separates personal spending (Coin) from long-term crew wealth (Stash). Coin is earned per score and spent freely. Stash accumulates slowly — Crew Tier + 2 per advancement — and can be withdrawn at a 2:1 penalty (2 Stash = 1 Coin). Stash brackets determine retirement quality: 0–10 is gutter life, 40+ is luxury.

**What it does well:** The split between individual and crew resources creates natural tension. Players choose between investing in the crew or pulling cash for personal needs. Coin is "spent for effect" — you don't itemize purchases, you declare what you're doing and spend accordingly.

**What it doesn't do well:** Stash withdrawal math adds bookkeeping that doesn't serve Aetherfall's priorities. The retirement economy is specific to Blades' campaign structure.

**What we borrowed:** The fundamental insight of separating individual wealth from group resources. Our Station (individual) and Ledger (Society) are directly inspired by Coin/Stash, simplified to remove numerical tracking.

#### Shadowrun — Lifestyle Tiers

Shadowrun defines six lifestyles (Streets through Luxury) with monthly costs in nuyen. Choose one, pay monthly, and everything within that lifestyle is narratively covered. A Middle lifestyle character has an apartment, food, basic gear, and reasonable clothes without tracking individual purchases.

**What it does well:** Brilliant simplicity. One number per month. The tier system makes class stratification visible and mechanical — a Low lifestyle character cannot walk into a High lifestyle establishment without effort. Social gating is built into the economy.

**What it doesn't do well:** Shadowrun also has an exhaustive equipment catalog with precise nuyen prices for everything from cyberdeck components to ammo types. The lifestyle system coexists with detailed accounting rather than replacing it.

**What we borrowed:** The lifestyle tier concept is the direct ancestor of our Station system. The idea that your economic position determines social access — not just purchasing power — is central to our design. We stripped away the precise monthly costs and item catalog.

#### Mothership — Debt as Campaign Currency

Mothership's crew shares a Debt score. Jobs reduce Debt (1 for routine work, 4+ for major operations). Monthly salary exists but is secondary to the collective obligation. Shore Leave costs 1 Debt to rest and recover. The entire campaign economy revolves around "we need to pay down our Debt."

**What it does well:** Debt as the primary metric creates powerful campaign-level pressure. Every job decision weighs risk against Debt reduction. Shore Leave costing Debt means rest itself has an economic price — brilliant for horror pacing.

**What it doesn't do well:** The dual scale (ship costs in millions, personal costs in thousands) creates friction. Works best for crews with a shared vessel; less natural for ground-based parties.

**What we borrowed:** The Ledger's drift toward Lean is a softened version of Mothership's Debt pressure. The idea that the group's financial state creates mission urgency — "we have to take this job" — comes directly from here. We avoided a numerical Debt score in favor of a qualitative state track (Flush/Level/Lean/Dire).

#### Savage Worlds — Wealth Die

Characters have a Wealth die (d4 through d12) that represents economic capability. Purchases require a Wealth roll with modifiers based on item cost (+4 for trivial items, -6 for expensive ones). Rolling a 1 generates Debt. Snake eyes generate double Debt.

**What it does well:** Elegant uncertainty. You might be able to afford something or you might not — the roll creates tension. Debt as a mechanical consequence (not a number to track) generates narrative hooks. Wealth as a character trait (Rich/Poor edges and hindrances) ties economy to identity.

**What it doesn't do well:** The modifier system requires looking up cost categories and applying math. Some tables find this clunky in play. It still implies a cost list exists somewhere.

**What we borrowed:** The concept that reaching beyond your means should involve risk and skill. Our Station Check mechanic (d100 roll using social skills) takes this idea but routes it through the existing skill system rather than introducing a new die type. The -15% modifier for reaching one tier up is conceptually similar to Savage Worlds' cost modifiers.

#### Fate — Wealth Stress Track

Fate's toolkit approach offers a Wealth Stress Track (typically 2–5 boxes). Checking a box represents spending to solve a problem. Wealth stress clears only when characters acquire loot — a parcel of treasure clears boxes up to its value.

**What it does well:** Money becomes a depletable resource like HP. No accounting, no prices. Spending creates real cost (checked boxes restrict future spending). Recovery is tied to adventure, creating a natural loop.

**What it doesn't do well:** Very abstract. There's no sense of what things "cost" relative to each other. Players with different Aspects can have wildly different Wealth capacities with no in-fiction explanation.

**What we borrowed:** The principle that spending should create pressure without requiring math. The Ledger's movement from Flush toward Lean is conceptually similar to checking stress boxes — a qualitative depletion that creates urgency. We chose qualitative states over checkboxes for even simpler tracking.

#### Powered by the Apocalypse / Dungeon World — Tagged Abstraction

Most PbtA games tag items by value tier (Trivial, Minor, Significant, Major, Extravagant, Kingly). No coins are tracked. To purchase something, narrate spending the appropriate tier. The GM adjudicates whether the expenditure is plausible given the character's fiction.

**What it does well:** Perfectly narrative. Zero accounting. The GM and player negotiate access based on established fiction. Scales naturally — a recently-looted character can spend freely; a destitute one cannot.

**What it doesn't do well:** Requires high GM comfort with improvised adjudication. Groups expecting concrete rules may feel unmoored. No mechanical feedback loop — nothing stops a generous GM from giving unlimited resources.

**What we borrowed:** The tiered access concept is the backbone of our Cost Tier system. "At your tier or below, you have it" is a direct PbtA principle. We added the Station Check as a mechanical anchor for the one-tier-above case, giving GMs a tool when they want randomness without requiring it.

#### Stars Without Number — Lifestyle Maintenance

Credits are tracked. Lifestyles have monthly maintenance costs by social class. Starships have daily crew costs (100 credits/day per crewmember) plus 5% of ship cost annually for maintenance. The maintenance model creates ongoing cash needs that drive mission-taking.

**What it does well:** Recurring costs create persistent pressure. "We need money for ship maintenance" is a powerful narrative engine. Lifestyle costs scale with campaign tier — a crew with a bigger ship needs bigger jobs.

**What it doesn't do well:** Real price tracking exists. The system is modular but not abstract — you still have exchange rates and a cost table.

**What we borrowed:** The concept that ongoing costs (not just purchases) create mission pressure. Our Drift mechanic — the Ledger sliding toward Lean between jobs — is the narrative equivalent of Stars Without Number's maintenance costs, without the actual numbers.

#### Band of Blades — Organizational Resource Pool

The Legion (player organization) has shared tagged Resources: supplies, horses, information networks. The Quartermaster (a player role) spends Resources to solve problems — "I spend horses to avoid the mountain pass." Resources are scarce and deplete over time through attrition.

**What it does well:** Named, tangible resources that create hard choices. The Quartermaster role distributes economic power to a player. Scarcity is the core drama — every spend has visible opportunity cost.

**What it doesn't do well:** Highly specific to the retreating-army campaign structure. Tagged resources require more tracking than a single state. Less applicable to urban adventure campaigns.

**What we borrowed:** The principle that group resources should create visible, shared decisions. The Ledger serves this role at a higher level of abstraction — the whole group sees the Ledger state and understands its consequences. We also borrowed the idea that some resources are provided by the organization (patron-issued gear) and some are personal.

#### Trophy — Burden as Survival Mechanic

Each Trophy character has a Burden — the cost of maintaining their lifestyle, weapons, home. Every adventure must net at least your Burden in treasure, or the character dies or retires. Burden rises when you upgrade gear or lifestyle, creating a treadmill.

**What it does well:** Mechanical desperation. Every adventure has existential economic stakes. Burden creates a clean number to beat without requiring transaction tracking. The treadmill (upgrading gear increases Burden) is a brilliant feedback loop.

**What it doesn't do well:** Very specific tone — Trophy is about doomed treasure-hunters. The die-if-you-can't-pay mechanic would feel punitive in a less horror-focused game. No social stratification.

**What we borrowed:** The insight that economic pressure should be existential, not administrative. Our Dire state on the Ledger — "complete this job or lose the charter" — echoes Trophy's Burden mechanic. We scaled it back from character death to Society dissolution, matching Aetherfall's tone.

#### Cypher System / Numenera — Barter and Cyphers

Numenera has a nominal currency (Shins) but the real economy is barter and cypher churn. Common goods are loosely tracked. Special items (cyphers, artifacts) are valued by rarity, not price. The two-market system means money matters for daily life but cyphers are the actual wealth.

**What it does well:** Focuses players on the interesting economy (unique items) rather than the boring one (daily expenses). Cypher churn encourages using powerful items rather than hoarding them.

**What it doesn't do well:** If economic tension is a story driver, this system provides none. Money is a non-issue. Works for exploration games, not for games where "can we afford this?" should create drama.

**What we rejected:** The barter-first, money-doesn't-matter approach. Aetherfall specifically wants economic position to drive narrative choices. "Can we afford porters?" needs to have a meaningful answer. We do borrow the principle that truly rare items (artifacts) exist outside the normal economy.

### 1.2 Key Patterns Identified

Across all ten systems, three dominant approaches emerge:

**Approach A: Wealth as Resource (Fate, Trophy, Savage Worlds).** Money is a depletable pool — stress boxes, a die that can degrade, a Burden number. Spending depletes the pool. Adventure refills it. Clean loop, minimal tracking, creates urgency.

**Approach B: Lifestyle Tiers (Shadowrun, Stars Without Number).** Choose your economic class. Everything at or below that class is covered. Costs are periodic (monthly), not transactional. Social stratification is mechanical.

**Approach C: Organizational Pool (Blades, Mothership, Band of Blades).** The group shares a resource that depletes and must be replenished. Individual wealth is secondary to collective standing. Creates shared stakes and collaborative decisions.

These approaches are not mutually exclusive. The strongest systems we found combine elements — Blades uses both individual Coin (Approach A) and Crew Tier (Approach B) with Stash as a bridge. Mothership combines Debt (Approach C) with individual salary (Approach A).

### 1.3 What We Borrowed and Why

| Source | What We Took | Our Implementation |
|--------|-------------|-------------------|
| Shadowrun | Lifestyle tiers determine social access | Station (0–5) |
| Blades in the Dark | Individual + group resource split | Station (individual) + Ledger (Society) |
| Mothership | Group financial state drives mission urgency | Ledger drift toward Lean |
| PbtA/Dungeon World | Tiered access without price lists | Cost Tiers (0–5), "at or below = you have it" |
| Savage Worlds | Reaching above your means involves risk | Station Check (d100 skill roll with modifier) |
| Trophy | Economic pressure can be existential | Dire state — complete the job or lose the charter |
| Stars Without Number | Recurring costs create mission pressure | The Drift (Ledger slides between jobs) |
| Band of Blades | Group resources create shared decisions | Ledger as visible, shared group state |
| Fate | Spending should create pressure, not math | Qualitative states over numerical tracking |
| Numenera | Rare items exist outside normal economy | Artifacts valued narratively, not priced |

### 1.4 What We Rejected and Why

| Approach | Why We Rejected It |
|----------|-------------------|
| **Precise currency tracking** (D&D gold, Shadowrun nuyen for items) | Contradicts core design goal. Tracking a mark balance is exactly the checkbook behavior we want to avoid. |
| **Exhaustive price lists** (D&D PHB equipment tables, Shadowrun gear catalog) | Tables give shape, GMs fill specifics. Pricing every item implies precision the system doesn't need. |
| **Wealth die** (Savage Worlds) | Introduces a new die mechanic outside the d100 system. Modifiers per item require a cost reference table. |
| **Stress boxes** (Fate) | Requires tracking checked/unchecked boxes — more overhead than qualitative states. Also lacks social stratification. |
| **Burden/death spiral** (Trophy) | Too punitive for Aetherfall's tone. Character death from poverty doesn't match an adventure game about chartered professionals. |
| **Barter-first economy** (Numenera) | Aetherfall needs economic position to matter narratively. "Money doesn't matter" removes a story lever we want. |
| **Numerical Debt score** (Mothership) | Tracking a number is bookkeeping. Qualitative Ledger states (Flush/Level/Lean/Dire) achieve the same pressure without math. |
| **Individual loot tracking** (D&D treasure parcels) | Encourages hoarding behavior and slows play with "who gets the magic sword" negotiations. |

---

## 2. Design Principles

These principles govern every decision in the economy system. When a question arises about implementation, interpretation, or edge cases, return to these.

### Principle 1: Access, Not Balance

The system tracks what you can reach, not what you have in a vault. A character's wealth is expressed as the doors that are open to them — social, commercial, geographic — not as a number on a ledger. "Can I afford this?" is answered by comparing tiers, not subtracting marks.

### Principle 2: Story Fuel, Not Simulation

Every element of the economy exists to generate interesting choices. The Ledger drifts toward Lean because "we need a job" creates story. Station determines social access because "we can't get into the gala" creates story. If a mechanic does not generate a decision or a scene, it does not belong in the system.

### Principle 3: One Number Per Layer

Individual wealth is one number (Station, 0–5). Group resources are one state (Ledger: Flush/Level/Lean/Dire). Patron support is one number (Backing, 1–5). No sub-tracking, no secondary pools, no reserve boxes. If you can't write it on a sticky note, it's too complex.

### Principle 4: Shape, Not Precision

The Cost Tier table shows what each tier covers in broad strokes. It does not list every item. When a player asks "can I afford this?" the GM compares the request to the tier descriptions and makes a judgment call. The table gives the shape; the GM fills in the specifics — the same philosophy that governs every table in the rulebook.

### Principle 5: The GM Controls the Pace

The Drift, Ledger movement, Station changes, and Backing shifts are all GM-adjudicated. There are no formulas that force the Ledger to move on a schedule. The GM pushes toward Lean when urgency serves the story and leaves the party at Flush when breathing room does. The economy is a pacing tool, not an accounting system.

### Principle 6: Marks Are Flavor, Not Mechanics

Marks are the in-world currency. NPCs talk in marks. Contracts are written in marks. A drink costs a few marks. A revolver costs a couple hundred. But players never track a mark balance. Station and the Ledger handle mechanical access. Marks exist in dialogue and world-building — they make the fiction feel grounded without requiring anyone to do math.

### Principle 7: Patron Relationships Are Economic Relationships

The Society's patron is its primary economic engine. Patron Backing determines the baseline: how well-equipped the Society is, how comfortable its members live, what resources are available. Changes in Backing are not abstract — they mean the safehouse gets worse, the ammunition runs low, the handler stops returning messages. The economy makes patron politics personal.

### Principle 8: Reaching Should Create Adventure

When something is beyond a character's Station, the system does not say "no." It says "not easily." The paths around the barrier — patron requests, debts, heists, sacrifices, favors — are adventure hooks. The economy's job is to create obstacles that demand creative solutions, not to block access entirely.

---

## 3. Currency: Marks

The **mark** is the standard unit of currency across post-eruption society. Pre-eruption governments minted their own currencies, but the collapse of centralized authority and the rise of cross-faction commerce created demand for a common medium of exchange. The mark emerged from the Ashworth Collective's trade networks and became dominant through sheer utility — it's accepted everywhere because everyone else accepts it.

### 3.1 What Marks Buy (Narrative Anchors)

These are not prices to track. They are reference points for GMs and writers to give dialogue and world-building texture.

| Amount | What It Represents |
|--------|-------------------|
| 1–5 marks | A drink, a street meal, a tram fare, a newspaper |
| 10–25 marks | A night at a flophouse, basic supplies, a day's unskilled labor |
| 50–100 marks | A week's rent in a modest district, a decent meal for a group, a conventional weapon |
| 200–500 marks | A month's rent, a quality firearm, a full set of working gear, a doctor's visit |
| 1,000–3,000 marks | A Galvanic device, a season's comfortable living, a vehicle |
| 5,000–15,000 marks | An enchanted weapon, a small property, a personal airship passage |
| 50,000+ marks | An estate, a rare artifact, a faction-level asset |

The starter adventure's "200 marks, plus expenses" payment anchors the fiction: it is what a new Society earns for their first job. Split four ways, that's fifty marks each — rent for a week, ammunition for the next job, and a few drinks if you're careful. Not enough to live on. Enough to keep going.

### 3.2 Why Marks Are Not Tracked

Players do not maintain a mark balance because:

- **It creates the wrong gameplay.** Counting marks turns every purchase into a subtraction problem. The question should be "can we afford this?" not "do we have enough marks?"
- **It doesn't match the fiction.** Characters in this world carry some cash, have tabs at local establishments, owe favors, and receive irregular patron payments. Their financial reality is messier than a number on a sheet.
- **Station handles it better.** A Station 2 character can afford Station 2 things. That's faster, simpler, and more narratively flexible than checking a mark balance.

When an NPC quotes a price in marks, it's world-building. The GM translates it to a Cost Tier for mechanical purposes. "Five thousand marks" means "that's a Tier 4 purchase" — beyond most adventurers without patron support or a special effort.

---

## 4. Station (Individual Wealth)

**Station** is a character's economic position in the world — a single number from 0 to 5. It represents their material comfort, social access, and purchasing power. It is not a bank account. It is the answer to the question: "What kind of life does this person lead?"

### 4.1 The Station Table

| Station | Name | What Life Looks Like |
|---------|------|---------------------|
| 0 | **Destitute** | No fixed address. Eats at soup kitchens or not at all. Owns the clothes on their back — barely. Owes people. Invisible to anyone with power. |
| 1 | **Scraping** | Rents a room — maybe shared. Eats daily, nothing fancy. Owns their tools and one set of decent clothes. Known at the corner shop. Can afford a tram ticket but thinks about it. |
| 2 | **Getting By** | Modest flat in a working district. Reliable meals. Can replace worn gear without agonizing. Has a coat for winter and boots that don't leak. The grocer extends credit. |
| 3 | **Comfortable** | Good flat or small house in a decent neighborhood. Eats well. Can afford small luxuries — a night at a restaurant, a bottle of something worth drinking, a new coat when the old one is fine. Known by name at a few establishments. |
| 4 | **Prosperous** | Fine home. Possibly staff — a housekeeper, maybe a driver. Travels comfortably. Known by name at good establishments. Can make things happen with a word and a handshake. Dresses well without thinking about it. |
| 5 | **Affluent** | Property. Influence. Multiple residences or a significant estate. Moves in circles where marks are vulgar to discuss. Opens doors that most people don't know exist. |

### 4.2 Starting Station

A character's starting Station is determined during Society creation (Session Zero). The patron's Backing rating sets a **floor** — the minimum Station that the patron's support guarantees (see §6.1).

Most starting characters are **Station 2** (Getting By). The patron's backing provides a roof, steady meals, and standard equipment — better than most people manage in a fractured city, but nobody's getting rich. Characters from wealthy backgrounds might start at Station 3 if their personal history justifies it; characters who came from nothing might be at Station 1, with the patron's support being the only thing keeping them there.

Station is set during character creation and does not advance through XP or level-ups. It changes through fiction.

### 4.3 Station Changes

Station rises or falls based on events in the campaign. The GM adjusts Station when the story warrants it — not on a schedule, not through a formula.

**Station rises when:**
- The Society completes a high-paying job (Windfall payout — see §8.1)
- A character receives a personal windfall (inheritance, investment payoff, gambling win)
- The patron increases Backing and the character was at the Backing floor
- A character takes a prestigious position or gains significant social standing
- A campaign milestone reflects economic advancement ("after six months of successful jobs, the Society is thriving — everyone moves to Station 3")

**Station falls when:**
- The Society hits Dire on the Ledger (everyone drops 1 Station until resolved)
- A character suffers a personal financial disaster (robbed, swindled, property destroyed)
- The patron reduces Backing and the character was at the Backing floor
- A character makes a deliberate sacrifice (sells everything to fund the expedition)
- Campaign events reflect economic decline (faction war disrupts income, zone shift destroys the neighborhood)

**Station never changes mid-session** unless something dramatic happens. It is a slow-moving indicator, not a volatile meter.

---

## 5. The Ledger (Society Resources)

The **Ledger** is the Adventuring Society's collective financial state — a single qualitative indicator that the whole group tracks together. It is not a bank account. It is the answer to the question: "How is the Society doing?"

### 5.1 Four States

| State | What It Means | Effect on the Society |
|-------|--------------|----------------------|
| **Flush** | Jobs are going well. Patron is pleased. Safehouse is stocked. Cash reserves exist. | Society can take time between missions. Can make modest group purchases without justification. Patron offers choice of assignments. Members can request non-essential equipment. |
| **Level** | Normal operations. Bills are paid. Nothing to spare. | Society takes jobs as they come. Standard access to patron resources. No breathing room for extras. Equipment requests must be justified. |
| **Lean** | Behind. Debts accumulating. Patron is impatient. Supplies are thin. | Society must take the next available job — even an unpleasant one. Patron assigns rather than offers. Some faction resources may be restricted. Equipment requests are questioned or denied. Lifestyle slips — the safehouse is cold, supplies are rationed. |
| **Dire** | Underwater. Patron support is on probation. The Society's charter is at risk. | Society faces an ultimatum: complete this job or lose the charter. Patron may demand concessions — a distasteful mission, surrender of an artifact, a loyalty test. Every member's Station drops by 1 until the crisis is resolved. The next failure means dissolution. |

### 5.2 Moving the Ledger

The Ledger moves based on mission outcomes, time, and events. The GM controls the movement.

**Toward Flush:**
- Successful mission with a Good Money or Windfall payout
- Patron windfall (faction gains territory, receives a large contract)
- Society receives a gift, inheritance, or investment return
- Significant favor repaid to the Society

**Toward Lean:**
- Failed mission or mission with collateral damage
- Time between paying jobs (the Drift — see §9)
- Patron falls on hard times (faction loses territory, political setback)
- Unexpected expense (safehouse damaged, equipment lost, medical bills)
- Outstanding debts coming due

The Ledger does not jump multiple states at once under normal circumstances. A catastrophic event (patron abandons the Society, safehouse destroyed in a zone shift) might push from Level to Dire. A legendary score might push from Lean to Flush. But most movement is one step at a time.

### 5.3 Interaction with Station

The Ledger and Station interact in specific ways:

- **Flush Ledger** can temporarily boost a member's effective Station for a specific purpose. "The Society is paying for Kael to dress up for the gala — that's a Station 4 appearance, even though he's Station 2." This is a group decision, not individual.
- **Lean Ledger** may force members to accept lower Station conditions. "The safehouse is cold, the cupboard is bare — everyone is effectively Station 1 for lifestyle purposes until we get paid."
- **Dire Ledger** drops every member's actual Station by 1 until the crisis resolves. This is the only case where the Ledger mechanically changes Station, and it reverses when Dire is resolved.

---

## 6. Backing (Patron Support)

Every Adventuring Society has a patron — a faction, organization, or individual that provides its charter and resources. **Backing** is a rating from 1 to 5 that describes how generously the patron supports the Society.

### 6.1 Backing Rating Table

| Backing | Name | What the Patron Provides | Station Floor |
|---------|------|-------------------------|---------------|
| 1 | **Bare Charter** | A charter document and a name. Maybe a contact or two. No equipment beyond what members bring themselves. A meeting place (borrowed, cramped, or improvised). | 1 |
| 2 | **Field Support** | Basic equipment and standard ammunition restocked between missions. A handler who checks in periodically. A safehouse that is functional but not comfortable. | 1 |
| 3 | **Full Package** | Good equipment, including one signature faction-specific item per member. Reliable handler with regular communication. Decent safehouse. Access to faction training. Reports taken seriously; reasonable requests fulfilled. | 2 |
| 4 | **Favored** | Excellent equipment, including prototype or rare faction-specific items. Priority handler. Well-appointed safehouse. Access to faction specialists on request. The patron actively invests in the Society's success. | 2 |
| 5 | **Inner Circle** | The best the faction has to offer. Unique equipment. Direct access to faction leadership. Resources that other Societies don't know exist. The Society is treated as an extension of the patron's will. | 3 |

The **Station Floor** is the minimum Station guaranteed to Society members by the patron's support. A Backing 3 patron ensures members live at least at Station 2 — the patron covers rent, meals, and basic needs as part of the arrangement. Members can be higher than this floor through personal means, but they cannot fall below it while the patron relationship holds.

### 6.2 Faction-Specific Gear by Backing

This table formalizes the gear provision described in the Society structure (WORLD_DESIGN.md §6). Different patrons supply different types of equipment based on factional philosophy.

| Backing | Restoration (Galvanic) | Awakening (Aetheric) | Arrangement (Pragmatic) |
|---------|----------------------|---------------------|------------------------|
| 1 | Conventional firearms only | Mundane gear, maybe a charm | Whatever you brought with you |
| 2 | Conventional loadout, one Galvanic oddity (shared among the Society) | Mundane gear, 1–2 minor charms, basic alchemical supplies | Reliable conventional loadout, one specialty item (GM's choice) |
| 3 | Full conventional loadout plus one Exotic weapon per member OR one significant Galvanic device (shared) | One enchanted weapon per member OR several warded items, regular potion supply | Mixed loadout with 1–2 faction contacts for specialty procurement |
| 4 | Multiple Exotic weapons, a significant Galvanic device (Force Generator or equivalent), access to prototype equipment | Multiple enchanted items per member, a significant ward, healer on retainer | Best conventional gear available plus one "acquired" exotic or enchanted piece per member |
| 5 | Cutting-edge prototypes, fully personal Galvanic loadouts, access to faction R&D | Personally commissioned artifacts, access to senior casters, ward networks | "Whatever you need. Don't ask where it came from." |

**Issued vs. Owned Gear:** Equipment provided through Backing is *issued*, not owned. It can be recalled if the patron relationship sours. Losing a patron means losing access to replacements, ammunition, charging for Galvanic devices, and specialized maintenance for faction-specific gear. This makes patron loyalty an economic choice, not just a political one.

### 6.3 Backing Changes

Backing changes at campaign-level inflection points. It is not a session-by-session metric.

**Backing increases when:**
- Consistent mission success over multiple jobs
- The Society delivers a significant win for the patron (recovered a key artifact, eliminated a rival, secured new territory)
- The patron's faction grows in power or wealth

**Backing decreases when:**
- Repeated mission failures or embarrassments
- The Society defies patron orders or acts against faction interests
- The patron's faction loses power, territory, or wealth (the Greycoat Authority's fiscal collapse is a prime example — all Greycoat-backed Societies feel the squeeze)
- A rival Society outperforms this one for the same patron

When Backing drops, the Station Floor drops with it. Members who were living at the floor suddenly feel their lifestyle degrading. The Ashworth Collective losing a factory district doesn't just change the zone map — it means the Societies they fund can't afford their safehouse anymore.

---

## 7. Access & Cost Tiers

### 7.1 Cost Tier Table

Every purchasable thing in the world has an implied **Cost Tier** from 0 to 5 that maps to Station. The GM assigns tiers based on the descriptions below — there is no exhaustive price list.

| Tier | Name | What It Covers |
|------|------|---------------|
| 0 | **Scrap** | Discarded items, street food, charity, public knowledge, improvised tools |
| 1 | **Common** | Basic tools, simple meals, shared lodging, ammunition, a tram ticket, a drink at a tavern, basic medical supplies, a used knife |
| 2 | **Standard** | A conventional firearm (revolver, shotgun), working clothes, a week's rent in a modest district, passage on a cargo vessel, a doctor's visit, basic alchemical components, standard adventuring gear |
| 3 | **Quality** | A fine meal, custom-tailored clothes, a reliable vehicle, a warded charm, a specialist's time (engineer, caster, lawyer), passenger airship passage, a good hotel room |
| 4 | **Premium** | A Galvanic device (Exotic weapon or oddity), enchanted equipment, membership at a private club, the best hotel in the district, a surgeon with a reputation, a favor from a faction official |
| 5 | **Exclusive** | An enchanted artifact, a personal airship, a seat at a faction council table, an estate, information that could start a war, Pre-Eruption technology |

### 7.2 The Access Rule

**At or below your Station:** You can afford it. No roll, no tracking, no discussion. It is within your means. Buy the ammunition, rent the room, take the cab. The GM narrates it and the game moves on.

**One tier above your Station:** You can reach for it, but it costs you. The GM calls for a **Station Check** (see §7.3). Success means you get it but the strain is visible — the GM notes a narrative consequence or the Ledger ticks toward Lean. Failure means you cannot swing it through normal means and need another approach.

**Two or more tiers above your Station:** You cannot simply buy your way in. This requires a narrative solution: a patron request (§7.4), a debt, a heist, a favor, a sacrifice. The economy says "not like this" and the story has to find another way. This is where the system generates adventure.

### 7.3 Station Checks

When a character reaches for something one Cost Tier above their Station, the GM calls for a **Station Check** — a d100 skill roll using the existing skill system.

The skill depends on how the character is trying to access the thing:

| Context | Skill | Example |
|---------|-------|---------|
| Formal venue, institutional access, official channels | Etiquette (SP) | Getting a table at an exclusive restaurant, attending a faction event, requesting institutional records |
| Black market, underworld goods, shady procurement | Streetwise (SP) | Finding a Galvanic weapon through back channels, hiring muscle, acquiring restricted substances |
| Negotiating a price, convincing someone to extend credit | Persuasion (SP) | Talking a merchant down, getting a loan from a contact, convincing a landlord to waive a deposit |
| Faking wealth you don't have | Deception (SP) | Bluffing your way into a premium hotel, forging credentials, posing as a higher-Station individual |

**Modifier:** The base check applies a **-15%** modifier — reaching above your Station is harder than operating within it. The GM adjusts based on circumstances:

| Situation | Modifier Adjustment |
|-----------|-------------------|
| You recently did the seller/gatekeeper a favor | +10% to +20% |
| You have a relevant contact or introduction | +10% |
| You're trying to access something at a hostile faction's establishment | -10% to -20% |
| The thing is in high demand or short supply | -10% |
| You're well-known and respected in this community | +5% to +15% |

**On success:** You get what you're after, but the GM notes the stretch. This might mean the Ledger ticks one step toward Lean (the Society absorbed the cost), or a narrative consequence appears later (the landlord expects a favor, the black market contact remembers you owe them, you skipped rent this month).

**On failure:** You can't swing it through this approach. Try another way — different skill, different source, a patron request, or accept that it's out of reach right now.

### 7.4 Reaching Beyond Means

When something is two or more tiers above a character's Station, or a Station Check fails, the mechanical path closes. The narrative paths open:

**The Patron Request.** Ask the patron for it. Restoration patrons can requisition Galvanic equipment. Awakening patrons can commission enchanted items. Arrangement patrons can pull strings. The cost is never marks — it's obligation. A mission completed, a favor owed, intelligence delivered, silence kept. The bigger the ask, the bigger the debt. This is the core patron tension expressed through the economy.

**The Debt.** Borrow from someone outside the patron structure. The Lamplighter Syndicate lends. Rival factions extend credit with strings attached. Local merchants carry tabs for good customers. Debts are tracked as narrative obligations, not numbers. The GM notes who is owed and what was promised, and brings it back when it creates the most interesting story.

**The Score.** Steal it, win it, find it, earn it through a specific action. "We need a Galvanic resonance damper and we can't afford one" is not a dead end — it's the next adventure.

**The Sacrifice.** Give up something you have to get something you need. Sell the enchanted blade to buy passage on the airship. Burn a contact's goodwill to get through the door. Accept a lower Station to fund the expedition. Sacrifice is always narratively visible.

---

## 8. The Mission Economy

### 8.1 Payout Ratings

Missions do not pay in tracked mark amounts. They have a **Payout Rating** that describes their impact on the Society's Ledger and, in exceptional cases, individual Station.

| Payout | Ledger Effect | Station Effect | Typical Missions |
|--------|--------------|----------------|------------------|
| **Scraps** | No change to Ledger | None | Routine patrol, information delivery, small favor for the handler |
| **Honest Work** | Holds Level (prevents drift toward Lean) | None | Standard retrieval, missing person, zone survey, escort, the starter adventure's "200 marks" |
| **Good Money** | Moves one step toward Flush | None | Dangerous retrieval, faction crisis response, deep zone expedition, politically sensitive work |
| **Windfall** | Moves to Flush regardless of current state | +1 Station (temporary or permanent, GM decides) | Legendary artifact recovery, faction-level crisis resolution, once-in-a-career score |

The GM assigns Payout Ratings when designing or selecting missions. Players can ask "what's the payout?" in fiction (their handler would tell them), and the GM answers with the rating or its narrative equivalent: "Standard fee" (Honest Work), "They're paying well for this one" (Good Money), "This is the kind of job people retire on" (Windfall).

### 8.2 The Pressure Cycle

The system creates a natural rhythm:

1. **Society completes a job.** Ledger moves toward Flush. Breathing room.
2. **Time passes between jobs.** The Drift (§9) pushes the Ledger toward Level. Expenses accumulate.
3. **Without new work, the Ledger slides to Lean.** Urgency builds. The patron starts assigning rather than offering.
4. **At Lean, the Society takes whatever is available** — even the questionable job, the one with the bad odds, the one from the faction they don't trust.

This cycle repeats. The GM controls the tempo by controlling how quickly the Drift moves and how often high-payout missions appear. A fast-paced campaign with tight Drift creates constant urgency. A slower campaign with generous payouts creates room for personal storylines between the economic pressure.

### 8.3 Marks as Narrative Color

When NPCs discuss payment in marks, the GM can use these rough equivalences to inform dialogue:

| Payout Rating | Mark Range (for narrative color) | How NPCs Describe It |
|--------------|--------------------------------|---------------------|
| Scraps | 20–50 marks | "A token for your trouble." |
| Honest Work | 100–300 marks | "Standard fee. Covers expenses." |
| Good Money | 500–2,000 marks | "We're paying well for this one." |
| Windfall | 5,000+ marks | "Name your price." / "Enough to change your life." |

These numbers are not tracked. They exist so the GM can put a number in an NPC's mouth when the fiction calls for it. "Two hundred marks, plus expenses" sounds real. It anchors the world. The mechanical effect is determined by Payout Rating, not by the mark number.

---

## 9. The Drift (Downtime Pressure)

### 9.1 How Drift Works

Between adventures, the Ledger **drifts** toward Lean. This is a narrative tool, not a mechanical countdown.

**Guideline:** After every 2–3 sessions of game time without a paying job, the Ledger moves one step toward Lean. The GM accelerates (unexpected expense, patron withdrawing support, equipment failure) or slows (side income established, patron grant, favor cashed in) the Drift as the fiction demands.

The Drift exists because life costs money: rent, food, equipment maintenance, the handler's cut, safehouse upkeep, ammunition. None of these are tracked individually. They are the fictional justification for the Ledger's natural slide. When the GM says "the Ledger moves to Lean," the players understand that it represents the accumulated weight of daily expenses catching up.

### 9.2 Downtime Actions

Between adventures, characters can take actions that interact with the Drift:

| Action | Effect | Check Required |
|--------|--------|---------------|
| **Side work** — guard duty, courier runs, manual labor | Slows Drift. Ledger stays at current state instead of sliding. | None — grunt work is always available. |
| **Hustle** — gambling, deal-making, odd jobs through contacts | If successful, holds Ledger at current state. If failed, no effect but time is spent. | Streetwise or Persuasion |
| **Craft for sale** — brew potions, forge equipment, repair for pay | Can generate income equivalent to a Scraps or Honest Work effect, depending on skill and market. | Relevant Craft or Casting check |
| **Invest** — put money into a business, property, or scheme | Long-term: eventual Station increase if the fiction supports it. Short-term: may accelerate Drift (spent reserves up front). | GM adjudication |
| **Patron favor** — take on a small task for the patron outside normal missions | Slows Drift. May help restore wavering Backing. | Task-dependent |

These downtime actions are not mini-games. They are one-roll-and-narrate activities that the GM can offer between missions to give players agency over their economic situation. A player who says "I spend the downtime doing side work to keep us afloat" makes one check (or none) and the group moves on.

---

## 10. Special Items

### 10.1 Artifact Valuation

Enchanted artifacts are handmade, rare, and individually significant (see MAGICAL_ARTIFACTS.md). They do not have Cost Tiers because they are not commodities — you do not walk into a shop and browse the artifact aisle.

When an artifact needs to be valued for fiction purposes (trade, negotiation, theft, insurance), the GM uses this framework:

| Enchantment Tier | Narrative Value | What That Means in the World |
|-----------------|----------------|------------------------------|
| Weak | Several months of comfortable living | A meaningful windfall for a person. A line item for a faction. |
| Standard | A year of comfortable living | Enough to change someone's Station. A notable expenditure for a faction. |
| Strong | A small property or a vehicle | Enough to fund a Society for months. Factions pay attention. |
| Spectacular | A building or a ship | Faction-level asset. Recovery of one could define a campaign arc. |
| Pre-Eruption | Priceless | Cannot be meaningfully valued in marks. Nations would compete for it. Wars have started over less. |

These are not prices. They are narrative anchors. When a player asks "how much is this worth?" the GM does not say "twelve thousand marks." They say "enough to keep the Society funded for the rest of the year" or "enough that the Ashworth Collective would send a recovery team."

### 10.2 Potion Economy

Potions occupy a middle ground between commodities and artifacts. They are traded, commissioned, and occasionally found — but not mass-produced. There are no potion shops. There are healers who sell remedies, brewers who take commissions, and abandoned laboratories that sometimes yield surviving bottles.

Potions have Cost Tiers:

| Potion Potency | Cost Tier | Access Notes |
|---------------|-----------|-------------|
| Weak | 2 (Standard) | Available from Aetheric Quarter healers and some faction suppliers. Accessible to working adventurers. |
| Standard | 3 (Quality) | Commissioned from skilled brewers or provided by an Awakening-backed patron at Backing 3+. Not casual purchases. |
| Strong | 4 (Premium) | Rare. Requires a specific brewer, a patron request, or a lucky find. Most adventurers cannot simply buy one. |
| Spectacular | 5 (Exclusive) | Exceedingly rare. Created by master brewers under specific conditions. Faction-level assets when found. |

Potions are also traded as **favors and currency** between Societies. A Society that has a caster capable of brewing potions has a valuable trade good — "we'll brew you three Weak healing potions in exchange for information on the warehouse guards" is a legitimate transaction that bypasses the mark economy entirely.

---

## 11. Equipment Integration

### 11.1 Cost Tier Tags for Existing Equipment Categories

The following Cost Tier assignments integrate with the existing equipment tables. These tiers do not change any weapon or armor statistics — they add a single access-level tag to each category.

**Melee Weapons:**

| Category | Speed | Damage | Cost Tier |
|----------|-------|--------|-----------|
| Small (knife, dagger) | 1 | 1d4+BR | 1 (Common) |
| Light (short sword, hatchet) | 2 | 1d6+BR | 1 (Common) |
| Medium (longsword, mace) | 3 | 1d8+BR | 2 (Standard) |
| Heavy (battleaxe, warhammer) | 4 | 1d10+BR | 2 (Standard) |
| Great (greatsword, polearm) | 5 | 1d12+BR | 3 (Quality) |

**Modern Firearms:**

| Category | Speed | Damage | Cost Tier |
|----------|-------|--------|-----------|
| Holdout Pistol | 2 | 1d6 | 1 (Common) |
| Revolver | 3 | 2d6 | 2 (Standard) |
| Semi-Auto Pistol | 3 | 2d6 | 2 (Standard) |
| Heavy Pistol | 4 | 2d8 | 2 (Standard) |
| Carbine | 5 | 2d8 | 2 (Standard) |
| Rifle | 6 | 2d10 | 2 (Standard) |
| Shotgun | 4 | 3d6 | 2 (Standard) |
| Combat Shotgun | 5 | 3d6 | 3 (Quality) |
| Submachine Gun | 5 | 3d6 | 3 (Quality) |

**Galvanic Exotics:**

| Category | Speed | Damage | Cost Tier |
|----------|-------|--------|-----------|
| Exotic Pistol | 3 | 1d10 | 3 (Quality) |
| Exotic Sidearm | 4 | 2d8 | 4 (Premium) |
| Exotic Melee | 2 | 1d8+BR | 3 (Quality) |
| Exotic Heavy (Aether Lance) | 7 | 3d8 | 5 (Exclusive) |

**Armor:**

| Category | Ballistic Soak | Martial Soak | Cost Tier |
|----------|---------------|-------------|-----------|
| Heavy Cloth | 1 | 0 | 1 (Common) |
| Leather | 1 | 1 | 1 (Common) |
| Scale | 2 | 2 | 2 (Standard) |
| Chainmail | 2 | 3 | 2 (Standard) |
| Half Plate | 3 | 4 | 3 (Quality) |
| Full Plate | 4 | 5 | 4 (Premium) |
| Ballistic Vest | 3 | 1 | 3 (Quality) |

**General Equipment (Representative, Not Exhaustive):**

| Item Category | Cost Tier | Examples |
|--------------|-----------|---------|
| Basic field gear | 1 | Rope, camping supplies, canteen, lantern, basic tools |
| Standard investigation tools | 2 | Camera, lock picks, forensic kit, alchemical field kit |
| Protective gear | 2 | Gas mask, insulated gloves, reinforced goggles |
| Medical supplies | 2 | Field surgery kit, bandages, antitoxin compounds, splints |
| Galvanic gadgets | 3–4 | Aetheric Compass (3), Voltaic Lantern (3), Resonance Damper (4), Galvanic Brace (4) |
| Communication devices | 2–3 | Short-range radio (2), encrypted communicator (3) |
| Vehicles | 3–5 | Automobile (3), armored car (4), personal airship (5) |

### 11.2 Owned vs. Issued Gear

There is a meaningful distinction between **owned gear** (acquired through personal Station) and **issued gear** (provided through patron Backing):

**Owned gear** is the character's property. It persists through patron changes, Society dissolution, and career transitions. A revolver purchased at Station 2 is yours — no one recalls it.

**Issued gear** is contingent on the patron relationship. It comes with the charter and leaves with it. Losing Backing or breaking with the patron means:
- Exotic weapons lose access to charging and specialized ammunition
- Enchanted items may be recalled by the patron
- Replacement parts and maintenance support disappear
- The handler expects issued equipment returned — keeping it strains or severs the relationship

This distinction matters because it makes patron loyalty an economic calculation. "We could break with the Ashworth Collective, but then we lose the Exotics" is a real cost. It also means characters who want independence from their patron need to build personal Station — owning their own equipment is a form of economic freedom.

---

## 12. Rulebook Implementation Notes

### 12.1 Chapter Placement

The economy system gets its own dedicated chapter, placed **before the Equipment chapter** in the rulebook flow. By the time readers reach equipment tables with Cost Tier columns, the system is already a known quantity.

**Economy chapter** (dedicated, player-facing): The full philosophy and system — Station, the Ledger, Backing, Cost Tiers, the Access Rule, marks as narrative color. This is where readers learn what these concepts mean, how they interact, and how they shape their character's life. Tone is narrative-first per the writing style guide: lead with fiction, explain why before what, show don't tell.

**Chapter flow placement:** After Adventuring Societies (which introduces patrons), before Equipment. The reader learns about Societies and patrons → understands the economic system those patrons fund → then encounters equipment tables where Cost Tiers are already familiar.

**Equipment chapter** (reference application): A "Cost Tier" column added to existing weapon, armor, and gear tables. Brief cross-reference to the economy chapter for the Access Rule. No need to re-explain the system — just apply it.

**Artifacts & Enchantments chapter** (reference application): Artifact valuation framework and potion Cost Tiers. Brief cross-reference to the economy chapter.

**Running the Game chapter** (GM-facing guidance): Mission Payout table, Drift guidelines, Station Check adjudication advice, Reaching Beyond Means guidance, between-session stability management. These are GM tools that expand on the player-facing system with adjudication specifics.

### 12.2 Tables for Publication

The following tables appear in the published rulebook:

**Economy chapter (dedicated):**
1. **Station Table** (§4.1) — the core individual wealth tiers
2. **Ledger States** (§5.1) — four-state Society resource track, with a visual four-box track
3. **Backing Rating** (§6.1) — patron support scale
4. **Faction-Specific Gear by Backing** (§6.2) — what each patron alignment provides
5. **Cost Tier Overview** (§7.1) — what each tier covers across categories
6. **The Access Rule** (§7.2) — summary box (at/below = have it, one above = check, two+ = narrative)
7. **Station Check Reference** (§7.3) — which skill for which context

**Equipment chapter (applied reference):**
8. **Equipment Cost Tier columns** (§11.1) — added to existing weapon/armor/gear tables

**Artifacts & Enchantments chapter:**
9. **Artifact Valuation** (§10.1) — narrative value by enchantment tier
10. **Potion Cost Tiers** (§10.2) — potency-to-tier mapping

**Running the Game chapter (GM-facing):**
11. **Mission Payout Reference** (§8.1) — Scraps through Windfall
12. **Drift Guidelines** (§9.1) — pacing tool for between-session pressure
13. **Downtime Actions** (§9.2) — what characters can do between jobs

### 12.3 Voice Callout Opportunities

Voice callouts are in-world people sharing lived experiences — never rules commentary or mechanical explanations. These are people talking about money, work, and survival the way they've experienced it. The tavern test applies: would this person actually say this to someone over a drink?

**The Handler** (mission stories, survival advice):
- On getting by: "My first Society, we ate rice and sardines for three weeks straight between jobs. Handler kept saying 'next week, next week.' When the next job finally came, it was sewer clearance in the Ashwick tunnels. We took it without asking what it paid. You would have too."
- On patron support: "The Collective gave us good kit. Arc pistols, charged and maintained. We never asked where they came from. Then Hargrove pulled us off a job mid-operation because some board member changed his mind. That's when I learned — the gun isn't yours if someone else can take it back."

**The Scholar** (fieldwork and research experiences):
- On economic collapse: "I interviewed a bank manager in the Greycoat district — a man who used to oversee loans for half the merchant class. He's a landlord now, renting rooms in a building he used to finance. 'The money didn't disappear,' he told me. 'It just stopped meaning what it used to.' I think about that more than I'd like to."
- On artifact value: "A colleague once traded a Standard-tier warding charm for passage across three zone boundaries and a month's lodging. No marks changed hands. The ferryman didn't want money — he wanted his daughter to sleep through the night without the dreams. The charm was worth whatever that was worth to him."

**The Street** (street-level survival, concrete details):
- On money and access: "You want to know the difference between Fenwick Row and the Gaslight Quarter? On Fenwick, Mrs. Chen at the noodle shop will feed you if you're short and pay her back next week. In the Gaslight, the doorman checks your coat before he checks your name. Same city, same marks in your pocket. Doesn't matter. They can smell where you're from."
- On getting things: "An Exotic pistol off the books? I know a man in the Coalfield who knows a woman in the Quarter. It'll cost you — not in marks. She'll want a favor. And she always collects."

**The Believer** (personal spiritual experiences, communal warmth):
- On the Quarter's way of life: "When old Thessaly lost her workshop in the zone shift, she didn't have a single mark saved. But she had thirty years of mending wards for every family on Ember Street. She slept in a different house every night for two months. Nobody asked her to leave. Nobody asked her to pay. That's worth more than any bank account, and no eruption can take it from you."

### 12.4 Character Sheet Additions

**Individual section:** Add one field — **Station** (a number 0–5). Placement: near the top of the sheet alongside core identity information, since it defines the character's position in the world.

**Society section** (on every player's character sheet): Add **Backing** (1–5) and **Ledger** (a four-state track: Flush / Level / Lean / Dire). The Ledger can be represented as four boxes in a row that players mark to indicate current state. Every player has this section on their own sheet — the table decides how to keep them in sync (one player acts as recorder, everyone updates together at session start, etc.).

Total new tracking: **one personal number (Station) plus the shared Society fields (Backing + Ledger state) on each sheet.** Less overhead than tracking a single spell's exhaustion.

### 12.5 Callout Types for the Economy Chapter

The economy chapter should use the full range of callout types available in the rulebook:

**Voice callouts** (§12.3): In-world people sharing lived experiences with money, work, and survival. Never reference mechanics or system terms.

**For the GM**: Rules clarifications, adjudication guidance, and design intent — addressed directly to the GM. Examples: how to pace the Drift, when to call for a Station Check vs. just narrating, guidance on adjusting Backing after a major story beat, how to signal economic pressure without making it feel punitive.

**At the Table**: Example play dialogue showing economy mechanics in action — named characters, natural conversation, dice rolls happening in context. Examples: a group discussing whether to take a risky job when the Ledger is Lean, a player making a Station Check to talk a clothier into lending formal attire, the moment when the handler tells the Society their Backing just dropped.

---

## 13. Story Moments This Enables

Mapping directly to the design requirements:

**"We need this job or we'll lose the house."**
The Ledger is at Lean. The Drift is catching up. The patron has one job available — and it's for a faction the Society doesn't trust. Take it or slide to Dire, where Station drops and the charter is at risk. The economy created this dilemma without anyone tracking a single mark.

**"That job offer is _really_ tempting."**
A Windfall payout from a rival faction. Taking it means Flush Ledger and +1 Station for everyone — but it means working against the Society's patron. The temptation has a mechanical shape (Windfall vs. Honest Work from the usual patron) without requiring precise mark comparisons.

**"We have to carry our own gear because we can't afford porters."**
Porter hire is Tier 3 (Quality service). The Society is at Station 2 with a Lean Ledger — no one's making a Station Check for porters when rent is already tight. They carry their own packs into the Wild Zone. The limitation came from the tier comparison, not from subtracting marks.

**"Can we get into the swanky hotel?"**
The Grandview Hotel is Tier 4 (Premium lodging). The characters are Station 2. Two tiers above — they can't walk in and book a room. Options: the patron makes a reservation (costs a favor), someone Deceives their way past the concierge (Station Check with Deception, steep modifier), or they find another way in (service entrance, bribed staff, the adventure writes itself).

**"Can we get outfits to look the part, or do we have to sneak in the back?"**
Fine clothes are Tier 3 (Quality). At Station 2, that's one tier above — a Station Check with Streetwise ("I know a tailor who owes me") or Persuasion ("I talk the clothier into a loan"). If the Ledger is Flush, the Society might cover it: "The Society is paying for everyone to clean up." If Lean, they're going in the back door. The Ledger state determines the approach before anyone rolls.

**"Lots of resources" vs. "get by with what you can."**
A Backing 4 Restoration Society: Exotic weapons per member, a Force Generator in the safehouse, a priority handler, a well-appointed headquarters. Station floor of 2, trending toward 3.
A Backing 1 Arrangement Society: a charter document, a borrowed meeting room, and whatever each member brought with them. Station floor of 1. Same game, radically different resource baseline. The Backing rating created the entire contrast with a single number.

---

## 14. Open Questions

These items are flagged for future sessions or playtesting:

1. **Station Check frequency.** How often do Station Checks happen in practice? If every session has 3–4 Station Checks, the -15% modifier may need tuning. Playtest and adjust.

2. **Multiple Station Checks per session.** Should repeated reaching in the same session compound (second check at -25%? third at -35%)? Or is the narrative consequence sufficient? Lean toward narrative consequences — compounding modifiers feel like accounting.

3. **Inter-Society trade.** When two Societies interact, how do their Ledger states affect trade? A Flush Society might fund a Lean one in exchange for a future favor. This is probably pure narrative, but worth documenting if it becomes common in play.

4. **Downtime duration.** The Drift guideline says 2–3 sessions of game time. How long is a "session of game time" in fiction? A week? A month? This probably varies by campaign and should remain flexible.

5. **Backing during patron transition.** If a Society switches patrons, what happens to Backing? Presumably it resets — the new patron hasn't invested yet. But a Society with a strong reputation might negotiate starting Backing. Leave to GM adjudication for now.

6. **Zone-specific economies.** WORLD_DESIGN.md notes that each zone "has its own economy." Should different zones have different Cost Tier adjustments? (Galvanic equipment cheaper in Galvanic districts, etc.) Interesting but potentially complex — flag for playtesting.

7. **Gambling and windfall mechanics.** If a character gambles, how does the outcome interact with Station? A big win could temporarily boost Station; a loss could temporarily lower it. Probably handled through narrative + a skill check, not a separate system.
