# Aetherfall RPG

A tabletop roleplaying game set in a 1920s-inspired secondary world where primal magic and industrial technology collide. d100 roll-under, dual damage tracks, and a sliding Aetheric balance that makes every spell cast and every shot fired reshape the battlefield.

**Status:** Playtest draft. Core systems complete (first pass), web rulebook live, interactive tools functional.

**Live site:** [voidnologo.com/aetherfall](https://voidnologo.com/aetherfall)

---

## Project Structure

```
aetherfall/
  web/                          # Live web rulebook and tools
    index.html                  # Landing page
    rules/                      # 16-chapter rulebook (static HTML)
      css/styles.css            # Unified design system
      js/main.js                # Sidebar, navigation, interactions
      tools/                    # Standalone interactive tools
        character-builder.html  # Form-based character creator with auto-calc
        character-sheet.html    # Blank printable 2-page sheet
        character-sheet-sample.html
        combat-tracker.html     # Timing track visualizer
        zone-tracker.html       # Aetheric/Galvanic balance tracker
  docs/
    requirements/               # Design specifications (the "why")
    sessions/                   # Chronological development log
    art/                        # Art direction and style guide
    pending-tasks.md            # Active task queue
    continuation-prompt.md      # Session resumption context
  simulations/                  # Python balance testing tools
  art/                          # Reference illustrations (pen & ink)
  rules/                        # Legacy PDFs (superseded by web/)
```

---

## Tech Stack

No build step, no dependencies, no framework. The entire rulebook is static HTML/CSS/JS served directly.

- **Rulebook:** Semantic HTML with a custom dark-theme design system (CSS custom properties, responsive grid)
- **Typography:** Playfair Display (headings), Source Serif 4 (body), JetBrains Mono (formulas), Cormorant Garamond (callouts)
- **Tools:** Standalone single-file HTML apps (no server, no login, runs offline after first load)
- **Flowcharts:** Mermaid.js via CDN for combat and spellcasting procedure diagrams
- **Character Builder:** Vanilla JS with all game data (27 skills, 37 spells, 6 schools) embedded as constants
- **Simulations:** Python scripts for balance testing (armor degradation, weapon curves, melee parity)

---

## Design Documents

The `docs/requirements/` directory is the authoritative source for game design decisions. The web rulebook is the polished player-facing output; the design docs contain the reasoning, constraints, and tradeoffs behind every rule.

### Reading Order

Start here to understand the game's design landscape:

**1. [PROJECT_SPEC.md](docs/requirements/PROJECT_SPEC.md)** — What the game is

The top-level vision document. Establishes the design pillars (theater of mind, mechanical consistency, OSR lethality, rulings over rules), the setting premise (a world 40 years past the Aetheric eruption), and the scope of play (Adventuring Societies chartered by patrons).

**2. [DESIGN_PHILOSOPHY.md](docs/requirements/DESIGN_PHILOSOPHY.md)** — Why the world works this way

The cosmological model: two forces (Aether from the Veil, Galvanic energy from the Engine) in opposition. Baseline reality is mundane — magic and technology are powerful but unreliable at the margins. This document explains why firearms malfunction near magic, why spells cost exhaustion, and why the sliding balance exists.

**3. [BASE_MECHANICS.md](docs/requirements/BASE_MECHANICS.md)** — How the dice work

Core resolution: d100 roll-under with scaling critical ranges. Opposed checks, difficulty modifiers, the skill target formula `((10 + stat) × level) + 30`. Dual damage tracks (wounds and exhaustion) with stacking penalties.

**4. [COMBAT_PROCEDURE.md](docs/requirements/COMBAT_PROCEDURE.md)** — How fights play out

The timing track system: declare actions, place tokens on a count track, resolve when the count arrives. Declaration order favors high-PC characters. Active defense, armor soak (Ballistic vs Martial), range bands, and the malfunction procedure for firearms.

**5. [MAGIC_SYSTEM.md](docs/requirements/MAGIC_SYSTEM.md)** — How magic works

Two casting paths: Scholarly (controlled, all schools, learned spells) and Wild (unpredictable, limited schools, all spells in those schools). Tier system based on roll margin (Weak through Spectacular). Exhaustion costs, backlash mechanics, the Push system for overreaching.

**6. [SPELL_COMPENDIUM.md](docs/requirements/SPELL_COMPENDIUM.md)** — All 37 spells

Complete spell reference across six schools (Aetheric Manipulation, Vivimancy, Warding, Divination, Transmutation, Ley Weaving). Each spell has a fixed casting time and per-tier exhaustion costs and effects.

**7. [FIREARMS_EQUIPMENT.md](docs/requirements/FIREARMS_EQUIPMENT.md)** — Weapons and gear

Every weapon has Speed, Damage, Capacity, Reload, and Reliability. Firearms check Reliability before every shot — fail and roll on the malfunction table. Galvanic (exotic) weapons shift the Aetheric balance toward technology. Armor splits into Ballistic and Martial soak with degradation mechanics.

**8. [SKILLS_PROGRESSION.md](docs/requirements/SKILLS_PROGRESSION.md)** — Character growth

27 skills across three pools (Physical, Mental, Social). Creation cap of 3 per skill, gameplay max of 5. XP costs scale linearly (level N costs N XP). Attribute advancement costs 10 XP per point.

**9. [WORLD_DESIGN.md](docs/requirements/WORLD_DESIGN.md)** — The setting

"Fog of Scale" principle: global events are rumors, regional politics are faction-driven, local detail is NPC-level. The world is 40-60 years past the eruption that brought magic back. Factions include Industrialists, Traditionalists, Academics, the Church, and criminal networks.

**10. [WRITING_STYLE.md](docs/requirements/WRITING_STYLE.md)** — How to write for the game

Two audiences: players (literary, narrative, conversational) and designers (technical, decision-focused). Voice callouts in the rulebook are in-world characters sharing experiences — never rules commentary. The "tavern test": if a character wouldn't say it over a drink, it doesn't belong in a voice callout.

**11. [GM_CHAPTER.md](docs/requirements/GM_CHAPTER.md)** — Running the game

When to call for a roll (uncertain outcome + interesting failure + not guaranteed by competence). Difficulty modifiers, adjudication philosophy, and the principle that the GM's job is to make the world feel real, not to enforce balance.

---

## Game Systems at a Glance

| System | Core Mechanic |
|--------|--------------|
| Resolution | d100 roll-under; 01 = crit, 00 = fumble |
| Skills | `((10 + stat) × level) + 30` target number |
| Wounds | 4-tier track (OK → Harmed → Maimed → Incapacitated), 7+BR per tier |
| Exhaustion | 4-tier track (OK → Wearied → Drained → Overwhelmed), 7+PW per tier |
| Combat | Timing track with count-based action resolution |
| Spellcasting | Roll margin determines tier (Weak/Standard/Strong/Spectacular) |
| Firearms | Reliability check every shot; malfunction in Aetheric zones |
| Aetheric Balance | Sliding scale — spells push Aetheric, Galvanic weapons push back |

---

## Interactive Tools

All tools are standalone HTML files with no server required. Open in a browser, use offline.

- **Character Builder** — Form wizard with clickable attributes, skill/spell dropdowns, auto-calculated targets, pool budget tracking. Prints a formatted 2-page character sheet.
- **Combat Tracker** — 10-column calendar grid timing track with drag-and-drop tokens, infinite timeline, footprint history for past actions.
- **Zone Tracker** — Live Aetheric/Galvanic balance tracker with spell/weapon shift buttons, decay controls, and real-time Reliability and Casting modifier display.

---

## Development Log

Session notes in `docs/sessions/` form a chronological record of every design decision, mechanic iteration, and implementation choice. Each session file includes the goal, changes made, files modified, key decisions with rationale, and open issues.

`docs/pending-tasks.md` tracks the active work queue and backlog.

---

## Balance Testing

The `simulations/` directory contains Python scripts for quantitative balance analysis:

- `armor_degradation.py` — Models armor wear over extended combat
- `melee_balance.py` — Compares melee weapon categories across skill levels
- `weapon_rebalance.py` — Tests firearm damage curves and reliability tradeoffs
- `run_analysis.py` — Orchestrates full analysis runs with output to `results/`
