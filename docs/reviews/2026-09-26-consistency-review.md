# Consistency Review — Session 34 (2026-09-26)

Full read of `docs/requirements/`, `docs/art/`, the built web rulebook (all 18 chapters + quickstart), pregen character data (`web/_data/characters/*.json`), `fiction/world/*`, the series bible, and a spell-usage scan of Stories 02–03.

**Nothing in the rulebook has been changed.** Every item below that touches player-facing content needs explicit approval (CLAUDE.md). Items are ranked by player impact.

Legend: **[WEB]** player-facing rulebook · **[QS]** quickstart / pregens · **[FIC]** fiction + world docs · **[DOC]** internal design docs

---

## Tier 1 — Canon conflicts (need a decision, not just a fix)

### 1.1 Two different Kaels [WEB] [QS] [FIC]
| Source | Name | Build | Background | Weapon focus |
|---|---|---|---|---|
| Creating chapter (`creating.njk`), Getting Hurt, Combat, Rolling | **Kael Ashford**, "Gutter Knight" | BR +2, PC +2, SP −1, PW −2 (net +2) | Former **army officer**, resigned "when magic erupted" | **Swordsman**, Melee 66, longsword, leather coat B0/M2 |
| Pregen (`kael.json`), quickstart, fiction | **Kael Dunn**, "The Steady Hand" | BR +1, PC +2, SP 0, PW −2 | Former **Greycoat constable** | **Gunfighter**, Firearms 66, Melee 52, hunting knife, leather jacket |

The rules examples also make Kael the party's sword-user, while the fiction's Kael reaches for "the knife, the thing that always works."
Also: Ashford "resigned his commission when magic erupted" implies he's 70+ given a 50-year-old Tear.
**Decision needed:** make the rules-chapter example character someone else (e.g. a new sample swordsman), or rebuild the examples around Kael Dunn.

### 1.2 Timeline: how long ago was the Tear? [WEB] [FIC] [DOC]
- Fiction world docs: **50 years** (explicit, repeatedly). Kael born Tear+8 at age 42 ✓, Sera Tear+27 at 23 ✓.
- WORLD_DESIGN: "40 to 60 years deep"; Handler specimen says "**Forty years ago**."
- Welcome chapter (`index.njk`): "It's the 1920s… **With the turn of the century**, changes swept over the globe" — implies ~20 years and uses a real-world calendar in a secondary world.
- NPC ages that break at 50 years: Dupont (60, "a young constable when the Tear hit" → he'd have been 10); Dr. Crane (fifties, "lost her university in the Tear"); Mother Thorn (mid-fifties, "was a schoolteacher before the Tear"); Aldric Wynn (34, "born twenty years after the Tear" → should be 30); Sera's pregen compass "hasn't pointed north since the Tear" (she was born 27 years after).
- WORLD_DESIGN §1.3 "first generation of trained casters is just now reaching maturity" reads oddly at 50 years.
**Decision needed:** lock the number (recommend 50 — the fiction depends on it) and adjust ages. Rewrite the Welcome intro's first paragraph.

### 1.3 Wild-casting school names: "Vitae" and "Artifice" [QS] [FIC]
The rules have six schools: Aetheric Manipulation, **Vivimancy**, Warding, Divination, **Transmutation**, Ley Weaving.
- `aldric.json`, `sera.json`, `04-the-characters.md`, story-02 ch04 use **Vitae** and **Artifice** (apparently older names).
- Sera's pregen lists "Artifice" as a school containing Reshape (Transmutation) **and Enchant (Ley Weaving)** — Enchant is also a 2-hour ritual, not a 6ct spell, and costs 6/10/16/24, not 4/8/12/18.
- Fiction character doc says Sera is Aetheric Manipulation only (1 school); pregen PW +2 gives her 2.
**Decision needed:** rename to rules schools; choose Sera's second school (Transmutation fits Reshape; drop Enchant).

### 1.4 The Society's identity [QS] [FIC]
Pregens: "**The Ashwick Charter**", Fixers, patron Greycoat Authority. Fiction: "**Ash & Veil Recovery**", Asset Recovery, patron Covenant of Embers (the Ashwick Job was a one-off Greycoat contract). Reconcilable, but the pregen sheets should probably say Ash & Veil (or the quickstart should say the pregens are a *generic* Society).

### 1.5 Pregen character descriptions vs fiction [QS] [FIC] [art pipeline]
Matters immediately for portraits (character design locks).
| | Pregen / art prompt | Fiction (`04-the-characters.md`) |
|---|---|---|
| Kael | mid-thirties, scar across left knuckle | **42**, brown skin, scar across **bridge of nose** |
| Sera | late twenties | **23**, pale, jagged black jaw-length hair, blue-white iris ring |
| Aldric | **early forties**, wire-rimmed spectacles, **receding hairline** (also `wave1-style-lockin.md` + `comfyui_generate.py`) | **34**, light brown skin, close-cropped dark hair, **round** spectacles, gaunt |
| Mira | silver earring (left ear) | 28, brown skin, scar on left cheekbone |
**Recommend:** fiction is canonical for appearance; update pregen descriptions and art prompts.

### 1.6 Name collisions [DOC] [FIC] [QS]
- **Aldric** Voss (Ashworth ops director) vs **Aldric** Wynn (party caster).
- **Voss** ×3: Aldric Voss, Sera Voss, Elara Voss (sample sheet).
- Dace Rennick and Corrigan Fels both defined by a "thin cigar."
- "Thornfeld" (Scholar callout, `skills.njk`) vs Thornfield (Communion).
**Recommend:** rename the Ashworth NPC and the sample sheet character.

---

## Tier 2 — Rules contradictions in the published rulebook [WEB]

| # | Where | Problem | Proposed fix |
|---|---|---|---|
| 2.1 | `rolling.njk` table vs example; `combat.njk` example; `reference.njk` | Crit table says 51–75 = range 2 = "target and target−1" (2 numbers); every example says Melee 66 crits on **64, 65, 66** (3 numbers). Reference also says crit range is "counted down **from 01**." | Decide: range N = N numbers (fix examples to 65–66) or N+1 (fix table). Fix reference wording. |
| 2.2 | `combat.njk`, `equipment.njk`, `reference.njk` | Firearms use the **Firearms** skill (Skills chapter, pregens, flowchart) but text repeatedly says "then roll **Ranged**." | Replace with Firearms. |
| 2.3 | `rolling.njk` At the Table | "I don't have **Security**" — no such skill; and uses **AW** for lockpicking (Sleight of Hand is PC). | "I don't have Sleight of Hand" + PC. |
| 2.4 | `creating.njk` | "A natural athlete (**PC** +3) with Melee 3 hits on 69%" — Melee is **BR**. | BR. |
| 2.5 | `rolling.njk` vs `quickstart.njk` | Two formulas for an untrained attribute check: (5+stat)×5 vs **(stat+4)×10**. | Pick one (the core rule is (5+stat)×5). |
| 2.6 | `combat.njk` Fight in the Alley | Thugs have 7 HP/tier, but "Kael's 7 fills 7 of his **9** OK boxes." Sera shown as 8 HP/tier (pregen BR −1 → 6). Sera's target 55 = "45 base + 10" — 45 is not reachable by the skill formula (pregen: 64). Aldric shown as target 58 (pregen: 63). | Align examples with pregens. |
| 2.7 | `magic.njk` | Push It example: **Sera casts Mend** — Vivimancy isn't one of her schools. | Use Aldric, or a Sera spell. |
| 2.8 | `magic.njk` | Exhaustion overflow puts you "mentally **Incapacitated**" — EP tier 4 is **Overwhelmed**. | Overwhelmed. |
| 2.9 | `magic.njk` Wild Effects | References non-existent skills: **Conceal**, **Interrogation**, "Awareness checks," "Social interactions," "tech-related skill checks." | Sleight of Hand, Intimidation, AW checks, SP checks, Engineering/Craft. |
| 2.10 | `getting-hurt.njk`, `equipment.njk` | Armor repair: "**Metalworking** or **Repair** check"; Hinder affects "**Swimming**." Not skills. | Craft; Athletics (swimming). |
| 2.11 | `grimoire.njk` (Amplify, Anchor, Barrier, Elemental, Fortify ×2, Sever), `magic.njk`, `artifacts.njk` | Durations in "**rounds**" — the game has no rounds. | Counts (e.g. "1d4 rounds" → "the next 1d4 actions" or "3 counts"). Needs a design call. |
| 2.12 | `equipment.njk` Galvanic Lance | "Suppressing: +1 to **Aetheric** rating per shot." | Galvanic rating. |
| 2.13 | `equipment.njk` Pneumatic Flechette | Piercing "ignores 2 points of **Martial** soak" on a firearm (firearms hit Ballistic). | Ballistic. |
| 2.14 | `reference.njk` | Jam: "must clear (**speed 3**)" vs Combat: "weapon's reload time." | Reload time. |
| 2.15 | `magic.njk` Ritual table | Omits Enchant (2 h+) which Grimoire lists. | Add. |
| 2.16 | `index.njk` (Welcome) | "You are an Adventurer — one of the **Gifted (or Cursed)**" implies all PCs have powers; Society described as "a **cabal** hunting for relics" vs chartered, patron-funded outfit. | Reword with 1.2. |
| 2.17 | `equipment.njk` Quick Reload | "halved (round **down**)" vs FIREARMS doc "round **up**." | Pick one. |

---

## Tier 3 — Quickstart & pregen sheet errors [QS]

`quickstart.njk` is the most error-dense page. The pregen JSON is mostly right; the quickstart prose drifted from it.

| # | Problem |
|---|---|
| 3.1 | **Zone sign flipped**: "Galvanic **+3**" — Galvanic is negative (−3) everywhere else. At −3, firearms get **+6** Reliability (text says "Normal"). |
| 3.2 | Stat block headers: Sera "Casting Target: **56**" (body says 64); Aldric "Casting Target: **50**" (skill 63). |
| 3.3 | EP/tier wrong: Kael **7** (PW −2 → 5), Mira **6** (→ 5), Aldric **9** (PW +1 → 8). |
| 3.4 | Mira **AW +1** in quickstart, 0 in JSON (JSON is right — net +2). Mira Persuasion "**58%**" and Sleight of Hand "**52%**" in spotlights vs 66% / 63%. |
| 3.5 | Weapon speeds: revolver "**4**" (3), Force "**3**" (2ct), Light weapons "speed 2" (Light is 3; Small is 2), shotgun "Medium speed 5, **3d4**" (Shotgun: speed 4, 3d6). Arc pistol speed 4 in example, 3 on sheet. |
| 3.6 | Reliability math: Aetheric +4 → Rel 95 − 8 = 87, so revolvers malfunction on **88+**, not "85+"; arc pistol 90 − 8 → **83+**, not "75+". |
| 3.7 | Quick-rules wound tiers named "**Wounded**" / "**Critical**" (should be Maimed / Incapacitated). |
| 3.8 | "Streetwise (**IN**-based)" — SP. |
| 3.9 | Mira's **Arc Pistol** (2d6+2, cap 4, rld 4, **Rel 90**, G2) matches no Galvanic weapon (Pneumatic Flechette 1d10/Rel 70/G1; Arc Gun 2d8/Rel 65/G2). Rel 90 is outside the doc's 50–75 range for Galvanic gear. |
| 3.10 | Knife damage on sheets: 1d6+1 (Kael), 1d4+1 (Sera, guards, Corva) — Small is 1d4, Light 1d6. Kael's leather jacket B2/M1 vs equipment "Leather Jacket B0/M1"; quickstart says "Soak 2." |
| 3.11 | Aldric's Mend listed as **3ct** (5ct) and school "Vitae." Sera's Reshape 4ct (5ct). |
| 3.12 | Sample sheet (Elara Voss): stipend "12 **crowns**" — currency is marks. |

---

## Tier 4 — Fiction & bible continuity [FIC]

- **Series bible** still lists Story 03 as "Planned / not yet written" (it's published) and says "**Sera** cast Anchor" in the mill — the prose (story-02 ch07) has **Aldric** casting it (Sera can't; Warding isn't her school).
- Fiction names spells and schools on the page ("the Anchor," "It's a Warding spell," "Reveal") — the style guide's Cardinal Rule says no spell school names as jargon. Minor, but ch07 is explicit.
- `continuation-prompt.md` / `pending-tasks.md` still list "merge Story 03 PR / build reader" — both done (`web/fiction/the-lamplighters-price.njk` exists).

---

## Tier 5 — Internal design-doc drift [DOC]

Design docs are reasoning records, but several now contradict the published rules:
- **COMBAT_PROCEDURE**: Melee/Brawl "PC-based," Ranged "BR-based," firearms use Ranged; crossbow reload 6/10 (web: 3/5); firearm reloads doubled vs web; Force 3ct; cheat sheet "Firearms degrade **3%** per point" (rule is 2); single-Soak armor (web has Ballistic/Martial); "Metalworking check."
- **MAGIC_SYSTEM**: Mend 4ct in §9.8 vs 5ct; Reveal/Reshape 3ct vs 4/5ct; Sever notes "5–14 counts"; open question #4 resolved but still open.
- **PROJECT_SPEC / MAGIC_SYSTEM / COMBAT**: "37 spells" / Ley Weaving (5) — Enchant makes it **38 / 6**. PROJECT_SPEC §6.3 says interference "not yet designed" (it is); §8 step "Select race: (TBD)" vs humans-only.
- **BASE_MECHANICS / WRITING_STYLE** examples: "Melee… **PC** +2" (Melee is BR); crit example 63–65 with range 2.
- **FIREARMS_EQUIPMENT**: "No check needed for conventional firearms in clean environments" vs "every shot, every time"; "Dead Zones"; "Animal Handling (use Survival)".
- **Terminology**: "dead zone" used for Galvanic zones in web World chapter + docs, not in the zone table. Fine as slang — worth confirming it's intentional.
- **docs/art/style-guide.md** still titled "Adventure RPG"; uses "1920s steampunk aesthetic" in every prompt while ART_DIRECTION forbids steampunk cliché; says "dragon erupted into a 1920s city" (secondary world). `consistency-rules.md` file-organization section points at `assets/generated/` (actual: `art/{type}/{stage}/`).

---

## Output / build issues (fixed this session — no content changes)

- **PDF printed raw Mermaid source** for both Quick Reference flowcharts → `scripts/build-pdf.py` now pre-renders them with mermaid-cli (neutral print theme) into `print/diagrams/`.
- **WeasyPrint not installed** → installed as a uv tool; the build script also falls back to `uvx`.
- `.claude/skills/session-start` description referenced the old "Adventure" project.

## Output issues noted, not yet fixed

- PDF has no art, no chapter openers, and several near-empty pages before chapter breaks (break-before rules + short trailing sections).
- The brand art (glossy painterly wordmark + hero) doesn't match the interior B&W pen-and-ink style guide. See `docs/art/art-direction-proposals.md`.
- Wave 1 style-lock images are gone (gitignored; S3 sync never configured); only emboss/logo/hero art exists locally.
- **Third-party art is live on the site**: `web/_includes/sheet.njk` (lines 546, 863) uses `assets/art/fantasy.jpg` as the character-sheet watermark on every sheet page. `consistency-rules.md` Rule 11 says the cat/dragon/fantasy pieces are reference art that may carry copyright restrictions and must not appear in publications. Replace with an original watermark (it's #1 on the ART_DIRECTION priority list) and stop passing through `web/assets/art/`.

---

## Resolution Status (Session 34, after user approval)

User decisions: **Kael Dunn is canon**; **the Tear was 50 years ago**; fix all clear-cut errors, bring design calls back. Locked in `docs/requirements/CANON_DECISIONS.md`.

**Fixed:**
- 1.1 Kael: `creating.njk` rebuilt around Kael Dunn (stats, 15-skill sheet, pools, 8 HP/tier track, gear). Kael examples updated in `rolling`, `combat` (incl. full rewrite of "A Fight in the Alley" around his revolver + Reliable tag), `getting-hurt`, `artifacts` (Thundering knife), `running-the-game` (Intimidation 52, Athletics 52, Brawl chase).
- 1.2 Timeline: Welcome intro rewritten (no "turn of the century"; Gifted/cabal wording); Dupont 72; Mother Thorn mid-seventies; Crane's backstory re-anchored; Aldric born Tear+16 with 15 years at the Scholars; WORLD_DESIGN "50 years", Handler "Fifty years ago".
- 1.3 Schools: Vitae → Vivimancy, Artifice → Transmutation in pregens, character doc, and story-02 ch04 (now "Every text on Aetheric botany…"). Sera's Enchant replaced with Alter Property (Transmutation). **Sera's second school = Transmutation is provisional**, pending confirmation.
- 1.5 Pregen descriptions now match the fiction for all four leads.
- 2.2, 2.3, 2.4, 2.6, 2.7 (Push It → Aldric), 2.8, 2.9, 2.10, 2.12, 2.13, 2.14, 2.15, 2.16; crit "counted down from 01" wording.
- Magic chapter and examples: Sera's target 64, Aldric's 63; dice re-chosen so every tier outcome stays the same. Holloway House: Aldric casts Detect (Sera has no Divination), and Kael's Reliable tag is applied. Dockmaster example: Mira (her real stats). `world-between`: "Aetheric 2/3" → Galvanic ratings, "aether lance" → Galvanic lance.
- Tier 3 quickstart: all items except 3.10's custom coats. Arc pistol now uses Arc Gun (Galvanic Sidearm) stats, knives are 1d4, jacket is B0/M1, and the derringer is correctly subject to the zone. Also: Mira's AW, EP values, casting targets, zone sign (−3), Reliability math, wound tiers, and the unskilled formula.
- Tier 4: series bible (Anchor credited to Aldric; Story 3 status).

**Still open (design calls):**
- Crit range N = N numbers or N+1 (examples still say 64–66 for target 66).
- "Rounds" → counts conversion (Grimoire ×7, Magic, Artifacts).
- Quick Reload round down/up.
- Sera's second school (Transmutation provisional).
- Pregen Society identity (Ashwick Charter vs Ash & Veil).
- Renames: Aldric Voss, Elara Voss, "Thornfeld", the two thin-cigar smokers.
- Tier 5 design-doc drift, which is internal and was not in the approved scope.
- Third-party watermark on the character sheets.
