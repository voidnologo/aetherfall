# Plan: World Design Document — Factions & Narrative History

## Context

The Aetherfall RPG has complete mechanical systems (13-chapter web rulebook) but no narrative layer. The world's cosmological framework (Aetheric/Galvanic tension, zones, the Veil/Engine) is locked in DESIGN_PHILOSOPHY.md and PROJECT_SPEC.md §2, but the *political, social, and geographic* reality that players and GMs inhabit doesn't exist yet. This is the next critical piece — without it, GMs have mechanics but no world to run them in.

The user's vision: a balkanized, fragmented world where magic's eruption physically remade geography, collapsed governments, and created a patchwork of local power centers. Think Neal Stephenson's Diamond Age/Snow Crash (phyles, burbclaves, franchise-states) crossed with Arcane's Piltover/Zaun divide. Stories start local. Rumors outpace facts. Adventure is close.

**Output:** `docs/requirements/WORLD_DESIGN.md` — a design doc that establishes all parameters before any web chapter work.

---

## Approach

Write the design doc collaboratively, section by section, pausing for user feedback at natural breakpoints. The doc follows the established format (status header, numbered sections, design notes, open questions).

### Document Structure

**Section 1: Design Principles**
- Codify the "Fog of Scale" rule: the bigger the entity, the fuzzier its description
- No canonical maps, no named countries, no world name — it's just "the world"
- The "Within Living Memory" constraint — all history is 40-60 years deep
- Dual audience: player-facing hooks + GM-facing seeds in every section
- Mystery is load-bearing — unanswered questions are features, not gaps
- 2-3 voice specimens demonstrating the target tone for the eventual web chapter

**Section 2: The World Before and After**
- **Before:** Industrial world, governments in control, occult societies were curiosities
- **The Eruption:** Magic tore through. Not gradual — catastrophic. Wild Zones swallowed regions. Cities fractured. The Midwest analog became mystical forest. Coastal cities saw neighborhoods collapse into low-tech/high-magic enclaves
- **The Counter-Response:** The Engine awoke. Galvanic tech emerged. New power centers formed — techno-wonder archipelagos, fortified industrial districts
- **Now:** Governments struggle to hold territory. Communication exists but rumors dominate. Prophets and ideologues fill the vacuum. Small groups with enough magic or tech carve out sovereign territories. The world is divided but not at war — balkanized, patchwork, local

**Section 3: The Shape of the World (Rumors & Wonders)**
- Not a gazetteer — a collection of rumors, reports, and hearsay about what's out there
- Floating island clusters off the coasts (Galvanic thrusters? Aetheric lodestones? Nobody knows)
- Vast mystical wilderness where farmland used to be
- A rising techno-empire on an archipelago — new Atlantis rumors
- Collapsed urban districts reborn as high-magic communities
- Fortified industrial enclaves running deep Galvanic
- Each entry is framed as "people say..." not "this is how it is"
- GM note: each rumor is an adventure hook — send players to find out what's real

**Section 4: Meta-Factions (Ideological Currents)**
- Three broad currents mapped to the three competing theories (from DESIGN_PHILOSOPHY.md §1.3):
  - **Restorationists** — the Aether is a disease, push it back, restore the old order (Immune Response theory)
  - **Awakened** — the Aether is a return to something real, embrace it (Rival Gods theory)
  - **Pragmatists/Arrangers** — both forces are here to stay, control the balance, profit (Engineer's Shrug)
- These are NOT organizations. No membership cards. Ideological tendencies that local groups lean toward
- Prophets and charismatic figures are rising within each current — this is a faction category itself

**Section 5: Sample Factions (Local/Regional Enclaves)**
- 6-8 concrete examples, each ~150-250 words (sketch depth)
- Each gets: name, meta-faction lean, what they want, what they do, what they're hiding, 2-3 GM hooks, one named NPC
- All explicitly framed as samples — "file the serial numbers off"
- Drawn from the balkanized world: a fortified factory district, a reborn Aetheric neighborhood, a prophet's growing commune, a smuggler network working the zone borders, an academic enclave studying the eruption, a government remnant trying to hold a city together, a criminal syndicate playing both sides, a wilderness community adapted to the Wild
- Factions are purely narrative — no mechanical reputation system

**Section 6: Adventuring Societies**
- What a Society is and how it connects to patron factions
- The patron relationship and its tensions (your patron's interests vs your morals)
- Society archetypes mapped to faction types
- Faction-specific gear as storytelling (cross-ref FIREARMS_EQUIPMENT.md)
- Inter-Society dynamics in a shared territory

**Section 7: Zone Politics**
- Zones as territorial signatures — you can read who controls what
- The politics of zone management in a balkanized world
- Zone forensics as investigation (cross-ref DESIGN_PHILOSOPHY.md §4.2)
- Border zones (where Galvanic meets Aetheric) as adventure hotspots

**Section 8: Voice Guide (For Web Chapter)**
- Multiple in-world voices — different contributors with different perspectives
- Voice characteristics: terse, opinionated, present-tense, uses setting terminology without explaining it
- 3-5 extended specimens in different voices (veteran, academic, street operative, prophet)
- What the voice is NOT: encyclopedic, neutral, comprehensive, omniscient
- Influenced by Shadowrun 3e's BBS format but adapted to this setting

**Section 9: Open Questions**
- Accumulated throughout writing

---

## Execution Plan

1. **Write Sections 1-2** (Design Principles + Before/After) — establish the rules and the history
2. **Pause for user review** — these set the foundation for everything else
3. **Write Sections 3-4** (Rumors/Wonders + Meta-Factions) — the world shape and big currents
4. **Pause for user review**
5. **Write Sections 5-6** (Sample Factions + Societies) — the usable detail. Most collaborative section — expect iteration
6. **Write Sections 7-8** (Voice Guide + Zone Politics) — synthesis sections
7. **Write Section 9** (Open Questions) and update cross-references

After all sections are drafted:
- Update `docs/requirements/PROJECT_SPEC.md` §2.5 and §2.6 with cross-references to the new doc
- Update session notes with decisions made
- Note any new items for pending-tasks.md

---

## Critical Files

| File | Role |
|------|------|
| `docs/requirements/WORLD_DESIGN.md` | **NEW** — primary output |
| `docs/requirements/DESIGN_PHILOSOPHY.md` | Source: cosmology, three theories (§1.3), literary influences, zone forensics (§4.2) |
| `docs/requirements/PROJECT_SPEC.md` | Source: zone definitions (§2.3), Societies stub (§2.5), factions placeholder (§2.6) — will update refs |
| `docs/requirements/WRITING_STYLE.md` | Source: voice conventions, audience classification |
| `docs/requirements/FIREARMS_EQUIPMENT.md` | Source: Galvanic device ratings, faction-specific gear concept |
| `docs/requirements/GM_CHAPTER.md` | Source: GM-facing hook format, adventure seed style |

---

## Verification

- Design doc follows established format (status header, numbered sections, design notes, cross-refs)
- No contradiction with locked decisions in DESIGN_PHILOSOPHY.md or PROJECT_SPEC.md
- Every sample faction has: name, lean, want, do, hiding, hooks, NPC
- Voice specimens are distinct from each other (multiple voices, not one voice repeated)
- No canonical geography — all "big picture" content framed as rumor/hearsay
- Factions are purely narrative — no mechanical reputation scores
- PROJECT_SPEC.md §2.5 and §2.6 updated with cross-references
