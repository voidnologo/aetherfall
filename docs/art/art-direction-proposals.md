# Art Direction Proposals — Session 34 (2026-09-26)

**Status:** DECIDED (Session 34) — the user chose **Direction D, Deco Lithograph**, after round 1 prototypes. It has been folded into `style-guide.md` with the Aether-cyan / Engine-amber colour rule carried over from B.

---

## What the art has to do

1. **Two media, one master.** Every piece must live on a **dark web page** (`#080b14`) *and* a **white print page** (WeasyPrint → PDF, and eventually a physical book). Art that only works on one background doubles the production cost.
2. **Carry the duality.** The whole game is Aether vs. Engine. The site already themes every chapter `aether` / `galvanic` / `neutral` / `split` (`web/_data/pages.json`). The art system should use the same four themes, so each chapter's frame, header, and accent art tell you which force it's about.
3. **Be the world, not generic fantasy.** Ashwick is a small, working, 1920s-analog industrial town, not a steampunk fantasia. The textures that come up again and again across the fiction and rules:
   - **Aether:** copper-and-sugar air, blue-white luminous crystals, ivy through cobbles, gas lamps and candles, shadows at wrong angles, pale seamless "remade" material with glowing veins.
   - **Engine:** ozone, a hum in the teeth, arc lights that never dim, soot-stained brick, riveted iron, cold smokestacks, brass-and-capacitor prototypes.
   - **The Gradient / Sootborn:** fine dark soot on everything, shop cases with ammunition beside spell components, the lamp-post lookout.
   - **Noir:** rain on cobblestones, dim taverns, trench coats, the Wet Ember's coal fire.
4. **Survive AI production.** Flux-dev + LoRAs on a 12 GB card. The style has to be reproducible from prompts + seeds, forgiving of AI weaknesses (hands, text, fine repeated hatching), and easy to post-process.
5. **Serve the page.** We need modular chapter-header bands, corner and border ornaments, drop caps, section dividers, spot illustrations, a few plates, pregen portraits, and the character-sheet watermark. That last one is urgent: the current watermark is third-party art.

## The brand-art question

The approved **wordmark and hero** are glossy, painterly, and glowing cyan/amber. The approved **interior style guide** is pure B&W pen and ink. Today these read like two different products. Every direction below either:
- (a) keeps the painted brand as "the cover," with a distinct interior look (common for RPG books), or
- (b) redraws the hero and logo later so everything shares one visual language.

My recommendation is (b), eventually. Don't block on it; the interior art comes first.

---

## Direction A — "The Engraver's Folio"
*The current style guide, taken seriously.*

**Look:** Pure black-and-white steel-nib pen and wood-engraving line. Doré, Harry Clarke, Lynd Ward's finer plates, 1920s book frontispieces. Nouveau whiplash curves frame Aetheric subjects and Deco stepped geometry frames Galvanic ones.
**Page system:** Chapter headers are engraved panels. Aether chapters get vine-and-crystal Nouveau arches, Galvanic chapters get sunburst-and-rivet Deco lintels, split chapters get a panel that changes vocabulary halfway across.
**On the web:** The art is inverted to silver-white line on midnight, with a very faint cyan or amber tint per chapter theme (CSS `filter` / `mix-blend-mode`, so no extra files).
**Strengths:** Continuity with every existing doc and prompt. Prints perfectly on any printer at any cost. Two LoRAs we already have were trained for exactly this. Line art is the easiest thing to threshold and clean up.
**Risks:** The most "classic RPG interior" option, so the least distinctive. AI crosshatching turns to mush at small sizes, and fine engraving loses detail when thresholded.

## Direction B — "Two Inks" *(recommended)*
*A's black linework, plus two spot inks: Aether cyan and Galvanic amber, used only where the forces are.*

**Look:** Printed like a 1920s two-color broadsheet or pochoir stencil. Everything mundane is black ink on paper: people, brick, steel, the sword. Magic glows in **one flat cyan**. Galvanic tech sparks in **one flat amber**. Where they collide (the gradient, the mill's dual-resonance material), the two inks overprint.
**Why this one:** It makes the core rule visible in every picture. You can look at any illustration and read the balance. "Swords always work" becomes literal: the blade is always plain black ink. The brand palette carries into the interior without going full color, and the painted brand art finally has a bridge to the interior.
**On the web:** Black line inverts to pale line, and the cyan and amber stay as they are, glowing on the dark page. That's the site's existing look, turned into drawings.
**In print:** Three-color (black plus two spots) for a premium book, or black plus mid-grey for a cheap grayscale print. The spot layers are separate, so a pure-B&W print version costs nothing extra.
**Production:** Generate the line art in B&W (Direction A's pipeline). Then make the color layers by (1) prompting Flux for the same seed with only the glow elements in color and masking by hue, or (2) generating a separate glow mask. It needs a small post-processing script (threshold + hue mask + flat fill), which the pipeline needs anyway.
**Risks:** Needs the post-processing pipeline to work well. Discipline is required: the colors are only ever for the forces, never decoration.

## Direction C — "Woodcut Noir"
*Lynd Ward's novels in woodcuts, Frans Masereel, German Expressionist posters.*

**Look:** Heavy carved-black relief prints. Big solid blacks, white gouged out of the dark, angular lamplight, dramatic silhouettes, rain as white slashes. Crude ornament; borders look cut from a block.
**Page system:** Chapter headers are full-width woodcut bands (a street, a skyline, a Wild treeline) with a carved title cartouche. Dividers are small cut blocks.
**On the web:** Gorgeous inverted: white gouges on black look like light through a shutter.
**Strengths:** The most distinctive and the most *noir*. It reads well at thumbnail size, hides AI anatomy flaws in shadow, and holds up after thresholding. It matches the fiction's register (rain on cobblestones, dim taverns).
**Risks:** Heavy ink coverage in print. It's weaker for technical subjects (equipment studies, spell diagrams) and less "wonder" than dread. It pushes the tone darker than "heroic, not nihilistic."

## Direction D — "Deco Lithograph"
*1920s–30s travel posters and railway advertising: Cassandre, WPA prints, Tamara de Lempicka.*

**Look:** Flat color shapes and bold geometric simplification, limited palette (midnight, bone, cyan, amber, oxblood), strong diagonals, heroic low angles, stylized clouds and light rays.
**Page system:** Chapter openers are full "poster" plates. Headers are simplified poster strips; ornaments are pure Deco geometry.
**Strengths:** The most modern-appealing and the most "1920s" on sight. Great chapter openers and cover and marketing art. Flat shapes are very consistent across AI generations.
**Risks:** Needs full color in print. Clean flat posters fight the grit, soot, and noir, and look optimistic even where the setting is not. Weak for spot illustrations and equipment.

## Direction E — "The Scholar's Field Journal"
*The book as an in-world document: a Gradient Scholars casebook.*

**Look:** Sepia or iron-gall ink sketches with loose watercolor washes on aged paper. Annotation arrows, specimen plates, cross-sections of Galvanic devices, zone-gradient diagrams, pressed-leaf and crystal studies. Think Leonardo's notebooks, naturalist field guides, and Aldric's spellbook margins.
**Page system:** Chapters open on a "journal spread" with a tipped-in plate. Borders are ruled margins, tape, and specimen tags.
**Strengths:** It fits the web World chapter's framing, where the book is a briefing packet assembled by contributors. It's superb for equipment, spells, creatures, and zone diagrams, and it has the most *explanatory* power.
**Risks:** AI generates fake handwriting, which must be avoided or kept illegible (only real text set in HTML). Parchment backgrounds fight the dark web theme. Less dramatic for action and plates, and the most expensive to print well.

---

## Recommendation

**Build on B ("Two Inks"), using A's line pipeline as its base layer.**
- It's the only direction that makes the game's central mechanic visible in the art itself.
- It degrades gracefully: B minus the color layers *is* Direction A, so a B&W print edition is automatic.
- It reconciles the painted cyan/amber brand with the B&W interior.

**Optional accent:** borrow **E**'s annotated-diagram treatment *only* for technical sidebars (Galvanic oddities, spell diagrams, zone gradients), drawn in the same line and two inks. That keeps one visual language while giving the reference chapters an in-world flavor.

---

## Prototype plan (after a direction is picked)

Run the **same four subjects** through each shortlisted direction with fixed seeds, so the comparison is apples to apples:

1. **Chapter header band** (wide, ~5:1): Harrier Street at sundown. Factory arc-lights on the left, Veilwright ivy and crystal glow on the right, the gradient in between. Also works as the `split` theme header.
2. **Ornament kit:** one Nouveau corner (Aether), one Deco corner (Engine), one section divider, one drop-cap "A".
3. **Spot illustration** (square): Sera mid-cast, with Kael's revolver sputtering beside her. The balance in one picture.
4. **Portrait** (3:4): Kael Dunn, per `fiction/world/04-the-characters.md` (canonical once item 1.5 of the consistency review is settled).

Deliverables: `art/{type}/generated/` files named per convention, plus a comparison page showing each prototype on both a dark web mock and a white print mock. Everything is logged in `docs/art/generation-log.md`.
