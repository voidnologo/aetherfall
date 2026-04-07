# Continuation Prompt

## Last Session (20) — Artifacts & Enchantments Redesign, Web Rulebook Chapter
- Redesigned artifacts system: tag-based enchantments (permanent), wards (decay), potions (decay)
- Added Enchant spell to Ley Weaving (Complexity 4, ritual) with source spell requirements
- Built new web rulebook Chapter 13 (artifacts.html), renumbered chapters 13-17
- Multiple design revisions: attunement protects item via misfire, wards can't be physically destroyed, handcrafted-vs-manufactured philosophy

## Current State
- **Game title:** Aetherfall (repo: voidnologo/aetherfall)
- **Website live:** 17-chapter rulebook + Character Sheet page with builder, blank sheet, and sample
- **CRITICAL RULE:** Rulebook content must NEVER be changed without explicit user approval. Layout/design only.
- **CRITICAL WORKFLOW:** Always persist design decisions in docs/requirements/ BEFORE writing rulebook content.
- **CRITICAL VOICE RULE:** Voice callouts are in-world people sharing experiences. Never rules commentary. Use "the tavern test" (WRITING_STYLE.md). GM notes handle rules perspective.
- **CRITICAL INTERNAL:** Spell Complexity is essential in design docs but NEVER exposed in the web rulebook. Players see EP costs and casting times only.
- **Complete (first pass):** Core mechanics, skills, progression/XP, magic system, spell compendium (38 spells), weapons, armor/soak, Galvanic oddities, vehicles, GM chapter, world design & factions, Adventuring Societies, voice sidebars, Zone Tracker, Combat Tracker, Character Sheet (blank + sample + interactive builder), Quick Reference with flowcharts, README, mid-campaign spell learning, **magical artifacts system + web chapter**
- **Chapter flow:** Welcome → State of the World → Adventuring Societies → Creating → Character Sheet → Rolling → Getting Hurt → Skills → Magic → Grimoire → World Between → Combat → Equipment → **Artifacts & Enchantments** → Running the Game → Quick Reference → Table Index → GM Tools
- **Not yet designed:** Zone formation mechanics, Push Timing, archetypes, currency, bestiary, NPC stat blocks, corruption/madness, enchanted firearms

## Immediate Next Task
**Mid-campaign spell learning** needs to go into magic.html (rules exist in MAGIC_SYSTEM.md §5.4, still not in web rulebook). Character sheet art/watermarks. Landing page tagline.

## Key References
- `docs/requirements/MAGICAL_ARTIFACTS.md` — Artifact system (tags, wards, potions, attunement, ward breaking)
- `docs/requirements/SPELL_COMPENDIUM.md` — 38 spells including Enchant (§6.6)
- `docs/requirements/MAGIC_SYSTEM.md` §5.4 — Mid-campaign spell learning (NOT yet in web rulebook)
- `docs/requirements/WRITING_STYLE.md` — Voice conventions, voice vs GM note distinction
- `web/rules/artifacts.html` — Chapter 13, artifacts & enchantments
- `docs/sessions/session-20-notes.md` — Full record of session 20
