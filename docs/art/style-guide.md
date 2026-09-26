# Art Style Guide — Master Document

*The definitive visual identity reference for all Aetherfall art.*

> **Session 34 (2026-09-26): direction changed.** The user chose **Direction D, Deco Lithograph**, over the previous pure black-and-white pen & ink style. This supersedes the old "Core Identity," "Pen & Ink Linework," technical-spec, and quality-checklist sections (see git history before commit `c369279` for the pen & ink version). Comparison of the round 1 prototypes: `docs/art/art-direction-proposals.md` and https://claude.ai/artifact/KLMQwvngArrLWZpTzRGHhL.

---

## Core Identity

**Game tone:** Heroic adventurers in a world where the Veil tore within living memory and the Engine answered. Wonder and dread in equal measure: noir streets, not grimdark.

**Art style:** 1920s Art Deco **travel-poster lithography**. Flat printed colour in a strictly limited palette, bold geometric simplification, strong diagonals and stylised light rays, crisp edges, a faint lithographic paper grain. Think Cassandre's railway posters, WPA national-park prints, Tamara de Lempicka's figures, and the London Underground poster tradition, applied to a sooty industrial town where magic leaks through the cobbles.

**Key influences:**
- **A. M. Cassandre**: monumental geometry, heroic low angles, light as shape
- **WPA / Federal Art Project posters**: flat silkscreen colour, stylised landscapes and cities
- **Tamara de Lempicka**: sculpted, stylised figures for portraits
- **London Underground / railway posters (1920s–30s)**: travel-poster composition, strong horizons
- **Art Deco architecture and ornament**: sunbursts, stepped arches, chevrons, fluting

## Visual Pillars

### 1. The Palette Is the Rule

Every piece uses the Aetherfall lithograph palette and nothing else. Colour carries meaning:

| Token | Hex | Meaning |
|---|---|---|
| **Midnight** | `#0e1a2b` | Night, shadow, the default dark field |
| **Bone** | `#efe6d2` | Paper, daylight, skin highlights, text panels |
| **Soot** | `#17140f` | Linework, silhouettes, iron |
| **Aether cyan** | `#3dc8e0` | The Veil: magic, crystals, casting, Wild Zones |
| **Galvanic amber** | `#e8a825` | The Engine: arc lamps, Galvanic tech, sparks |
| **Oxblood** | `#8e2f23` | Brick, blood, danger, factory red |

- **Cyan is only ever the Aether. Amber is only ever the Engine** (plus ordinary warm lamplight, sparingly). This keeps the Two-Inks idea inside D: you can read the balance in any picture.
- Mundane things (people, brick, steel, the sword) live in midnight, bone, soot, and oxblood.
- Skin tones come from bone, oxblood, and soot mixes, stylised but true to the character (see Character Design Locks). Never default everyone to pale.

### 2. Flat Shape, Not Rendering

- Flat fills with at most two or three value steps per form. No airbrushed gradients, no photographic lighting, no 3D render look.
- Light is drawn as **shape**: rays, halos, hard-edged pools under lamps.
- A subtle lithographic grain or paper texture is welcome. Noise and painterly texture are not.

### 3. Deco Meets Nouveau (Kept)

The Aether/Engine tension still maps onto ornament:
- **Engine / Galvanic**: Deco geometry, with sunbursts, stepped arches, chevrons, rivets, zigzag bolts.
- **Aether / Veil**: Nouveau curves inside the poster style, with whiplash ivy, crystal spires, and flowing smoke.
- Split scenes use both vocabularies: geometry on one side, curves on the other.

### 4. 1920s Period Accuracy

The world is analogous to the 1920s. The art must reflect this.

- **Clothing** — suits, overcoats, cloche hats, suspenders, leather boots, goggles. Military surplus and expedition gear. No medieval fantasy costuming unless justified by setting (ceremonial, magical tradition).
- **Technology** — revolvers, tommy guns, automobiles, airships, radio equipment, industrial machinery. Steampunk exotics add brass fittings, vacuum tubes, arc coils, and aetheric resonators.
- **Architecture** — Art Deco skyscrapers, industrial districts, jazz clubs, occult bookshops, railway stations. Wild zones show these structures being consumed by magical growth.
- **Creatures** — supernatural beings rendered with period sensibility. A dragon isn't medieval — it's something that erupted into a 1920s city. The juxtaposition of the mundane and the impossible is key.

### 5. Supernatural Atmosphere

Magic is new, wondrous, and terrifying. The art must convey this.

- **The Tear aesthetic** — magic breaks through reality. Cracks in the mundane world revealing something vast and inhuman beneath. Vines growing through concrete. Geometric patterns dissolving into organic chaos.
- **Awe and dread** — magical subjects should inspire wonder first, unease second. Not horror-gore, but the vertigo of encountering something that shouldn't exist.
- **Corruption marks** — visual cues that power has a cost. Cracks in skin where energy leaks, exhaustion in posture, equipment corroded by magical residue.
- **The interference** — show the magic/tech tension visually. Machines with vines growing through them. Spell effects fading near industrial equipment. The border between zones.

### 6. Illustrative Function

This is RPG interior art. Every piece must serve the book.

- **Readability at print size** — art must work at the size it will appear on the page. Spot illustrations must read at 2-3 inches wide.
- **Text-compatible** — most pieces need to coexist with body text. Clean edges, defined boundaries, white space preserved.
- **Informative** — equipment studies should show how the thing works. Character portraits should convey class/role at a glance. Location vignettes should establish mood instantly.
- **Reproducible in print** — flat palette colours print predictably in CMYK. Check that every piece still separates cleanly in greyscale, so a budget B&W print edition stays readable.

---

## Character Design Principles

### Period-Appropriate Adventurers

Characters look like 1920s people who happen to be adventurers — not fantasy archetypes in costume.

- **Clothing baseline:** Trousers, shirts, waistcoats, boots, overcoats, hats. Layer expedition gear over civilian clothing. Leather satchels, ammunition belts, tool rolls.
- **Weapons carried visibly:** A holstered revolver, a sheathed sword on the hip, a slung rifle. Smart adventurers carry both — the art should show this.
- **Magical markers (casters):** Subtle physical signs of magical ability — unusual eye quality, faint geometric marks on skin, a slight cyan aura drawn as a flat halo. Not flamboyant wizard robes.
- **Wear and history:** Scuffed boots, patched coats, well-maintained weapons. These are working adventurers, not fashion plates.

### Silhouette Test

Every character design must pass the silhouette test — filled with solid black, each character should be identifiable from outline alone. Distinctive posture, equipment loadout, and body language matter more than facial features at small reproduction sizes.

### Diversity of Role

The game supports a wide range of character types:
- The scholarly caster in a rumpled suit with ink-stained fingers
- The wild caster with organic magical growths and feral energy
- The gunfighter in a long coat with paired revolvers
- The swordsman who trusts steel over everything
- The engineer with exotic tech prototypes and brass instruments
- The investigator with a notebook and a nose for corruption

---

## Art Composition by Type

### Full-Page Plates

Chapter-opening illustrations. The most detailed and polished art.

- **Full page, portrait orientation** — fills the page with generous margins
- **Narrative scene** — shows a moment of action or atmosphere that encapsulates the chapter's theme
- **Maximum detail** — the pieces players will study and remember
- **Decorative framing optional** — Art Nouveau/Deco border treatment for key plates
- **1-2 per chapter**

### Spot Illustrations

Inline illustrations that break up text and visualize specific rules or concepts.

- **2-4 inches wide** — sized to sit alongside text columns
- **Quick read** — communicates one idea clearly at small size
- **Clean silhouette** — strong contrast, no fussy background detail
- **Irregular edges** — can bleed into the text space organically rather than sitting in rigid boxes
- **Most common art type** — 30-50 spot illustrations across the book

### Character Portraits

Reference illustrations for character types, NPCs, and example characters.

- **Bust or 3/4 body** — enough to show clothing, equipment, and posture
- **Neutral or characteristic pose** — standing ready, examining something, mid-action
- **Equipment visible** — weapons, tools, and gear that define the character's role
- **Period-appropriate styling** — 1920s clothing and accessories

### Creature Illustrations

Monsters, summoned beings, corrupted creatures, beasts of legend.

- **Full body, dynamic pose** — show the creature's threat and nature
- **Scale indicator** — include a human figure, doorway, or other reference for size
- **Mechanical identity** — visual cues for game-relevant traits (armored, fast, magical, venomous)
- **The Tear context** — these are things that shouldn't exist in a 1920s world. The art should carry that strangeness

### Equipment & Weapon Studies

Object-focused illustrations for weapons, artifacts, and gear.

- **Technical illustration quality** — show the object clearly from an informative angle
- **Detail callouts** — fine detail on mechanisms, inscriptions, or magical elements
- **No character holding it** — the object is the subject, displayed floating or resting
- **Period-appropriate design** — a sword in this world has 1920s-era metallurgy and design sensibility, not medieval

### Location Vignettes

Atmospheric scene-setters for environments and zones.

- **Establishing shot composition** — a view that communicates the character of a place
- **Mood over detail** — use the midnight field, lamp pools, and light rays to establish atmosphere
- **The zone spectrum** — show the range from industrial dead zones (geometric, mechanical, ordered) to deep wild zones (organic, chaotic, overgrown)
- **Small to medium format** — typically 1/4 to 1/2 page

### Decorative Elements

Borders, dividers, drop caps, page ornaments.

- **Art Deco geometric patterns** — for chapter headers, page frames, section breaks
- **Art Nouveau organic patterns** — for magic-related sections, flowing dividers
- **Consistent weight** — decorative elements should complement, not compete with, illustration art
- **Modular** — designed to be reused across the book in different configurations
- **Period motifs** — gears, compass roses, arcane symbols, stylized flames, geometric sunbursts

### Map Elements

Cartographic illustration for world and location maps.

- **Deco cartographic style** — flat-colour poster maps with decorative compass roses and legends
- **Period map conventions** — 1920s-era cartographic style with Art Deco titling
- **Zone visualization** — Aetheric zones in cyan, Galvanic zones in amber, gradients as banded tints
- **Scalable** — must work from full-page spread down to quarter-page inset

---

## Technical Specifications

| Parameter | Value |
|-----------|-------|
| **Generation** | flux1-dev fp8, 30 steps, guidance 3.5, euler/normal, no LoRA (see `docs/art/prompt-engineering/`) |
| **Full-page plate** | generate 832×1216, upscale to 2480×3508 (A4/Letter at 300 DPI) |
| **Chapter header band** | generate 1664×448 |
| **Chapter opener frame** | generate 832×1216, empty centre |
| **Spot illustration** | generate 1024×1024 |
| **Character portrait** | generate 832×1216 |
| **Web** | WEBP, 50% of print resolution |
| **Format** | PNG masters (sRGB), WEBP for web |

### Prompt Rules (learned in round 1)

- **Never put a character's name in the prompt.** Flux prints it as poster lettering. Describe the person instead.
- **State skin tone first and explicitly** in any figure description. Flux defaulted every portrait to pale in round 1.
- End every prompt with the "no text, no lettering, no title, no signature" clause.
- Keep compositions simple: one idea per image. Complex two-action scenes lose the second action.

### Post-Processing Pipeline

1. **Crop or inpaint** any stray lettering or signatures.
2. **Palette snap** (optional): quantise to the six palette tokens, plus up to two tints of each, so every piece shares exact colours.
3. **Upscale** for print; re-snap the palette if upscaling introduced new colours.
4. **Export** a PNG master and a WEBP web copy.

---

## Quality Checklist

- [ ] Uses only the lithograph palette; cyan only for Aether, amber only for Engine (or plain warm lamplight)
- [ ] Flat shapes and crisp edges; no airbrush, photo, or 3D look
- [ ] Reads at thumbnail size (strong silhouette, one clear idea)
- [ ] 1920s-analog period accuracy; not steampunk, not generic fantasy
- [ ] Character matches their Design Lock (age, skin tone, marks, kit)
- [ ] No text, lettering, titles, or signatures
- [ ] Composition serves its slot (header band, frame, spot, portrait, plate)
- [ ] Works on the midnight web background and on bone paper

## Related Documents

- `consistency-rules.md` — Enforcement rules for visual cohesion
- `prompt-engineering/prompt-templates.md` — Reusable prompt structures
- `prompt-engineering/negative-prompts.md` — What to avoid in generation
- `prompt-engineering/generation-settings.md` — Model/LoRA/parameter configs
- `prompts/` — Individual art piece prompts (organized by type)
