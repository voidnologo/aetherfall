# Continuation Prompt

## Last Session (22) — Wild Effect Table in Web Rulebook
- Added full Wild Effect table (10 effects x 3 tiers) to magic.html with residue escalation model
- Backlash now triggers on every cast (success or misfire), cancellation is burn-only
- Residue replaces "while active" — clears on long rest after effect wears off, dramatically extends escalation window
- Added At the Table example, two GM callouts (per-effect tracking + environmental reuse)

## Current State
- **Game title:** Aetherfall (repo: voidnologo/aetherfall)
- **Website live:** 17-chapter rulebook + Character Sheet page with builder, blank sheet, and sample
- **CRITICAL RULE:** Rulebook content must NEVER be changed without explicit user approval. Layout/design only.
- **CRITICAL WORKFLOW:** Always persist design decisions in docs/requirements/ BEFORE writing rulebook content.
- **CRITICAL VOICE RULE:** Voice callouts are in-world people sharing experiences. Never rules commentary. Use "the tavern test" (WRITING_STYLE.md). GM notes handle rules perspective.
- **CRITICAL INTERNAL:** Spell Complexity is essential in design docs but NEVER exposed in the web rulebook. Players see EP costs and casting times only.
- **Complete (first pass):** Core mechanics, skills, progression/XP, magic system + spell learning, spell compendium (38 spells), weapons, armor/soak, Galvanic oddities, vehicles, GM chapter, world design & factions, Adventuring Societies, voice sidebars, Zone Tracker, Combat Tracker, Character Sheet (blank + sample + interactive builder), Quick Reference with flowcharts, README, artifacts & enchantments web chapter, mid-campaign spell learning web section, **Wild Effect table with residue escalation**
- **Chapter flow:** Welcome → State of the World → Adventuring Societies → Creating → Character Sheet → Rolling → Getting Hurt → Skills → Magic → Grimoire → World Between → Combat → Equipment → Artifacts & Enchantments → Running the Game → Quick Reference → Table Index → GM Tools
- **Not yet designed:** Zone formation mechanics, Push Timing, archetypes, currency, bestiary, NPC stat blocks, corruption/madness, enchanted firearms

## Immediate Next Task
Character sheet art/watermarks. Landing page tagline refinement. Visual polish pass on recent chapters.

## Key References
- `docs/requirements/MAGIC_SYSTEM.md` §3.4 — Backlash, Wild Effect table, residue escalation model
- `docs/requirements/COMBAT_PROCEDURE.md` — Combat casting procedure with backlash on all casts
- `docs/requirements/WRITING_STYLE.md` — Voice conventions, voice vs GM note distinction
- `web/rules/magic.html` — Chapter 8, includes Wild Effect table and At the Table example
- `web/rules/reference.html` — Quick reference with casting flowchart (now includes misfire → backlash branch)
- `docs/sessions/session-22-notes.md` — Full record of session 22
