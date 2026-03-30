# Continuation Prompt

## Last Session (2) — Magic System Design & Spell Compendium
- Designed complete magic system: tiered d100 casting, scholarly vs wild paths, backlash with escalation
- Built full spell compendium: all 37 spells across 6 schools with tier tables
- Added opposed checks as core mechanic and "rulings over rules" as design pillar
- Wild caster mechanics: 2d100 take extreme, +10 bonus, tier suppression by skill brackets

## Current State
- Project is in **design exploration phase** — collaborative interview-driven design
- Magic system is substantially complete (first pass). Compendium needs playtesting tuning.
- No firearms, leveling, factions, or zone mechanics yet.

## Immediate Next Task
Build a reusable magic casting simulation framework in `simulations/`. The simulation should:
1. Generate realistic characters at various power levels (low/mid/high/master, scholarly and wild)
2. Simulate many rounds of spell casting using the rules in MAGIC_SYSTEM.md and SPELL_COMPENDIUM.md
3. Track and report: misfire rates, tier distributions, backlash frequency, wild effect escalation, exhaustion/HP consequences, tier suppression usage for wild casters, how often casters hit exhaustion overflow
4. Be designed so spell costs/parameters can be tweaked and simulations re-run to compare
5. Save scripts and analysis output to `simulations/` for repeatability

## Key References
- `docs/requirements/MAGIC_SYSTEM.md` — Full casting rules, tier system, backlash, wild effects, exhaustion overflow
- `docs/requirements/SPELL_COMPENDIUM.md` — All 37 spells with tier tables (exhaust costs, casting times)
- `docs/requirements/PROJECT_SPEC.md` — Core mechanics, stats, design pillars
- `docs/pending-tasks.md` — Prioritized task list
- `rules/FunzieRulez.pdf` — Original prototype rules
