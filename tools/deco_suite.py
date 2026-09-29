#!/usr/bin/env python3
"""
Aetherfall Art Pipeline — Deco Suite (Session 35)

Generates the Deco Lithograph ornament kit and spot illustrations planned in
docs/art/deco-suite-plan.md. Every piece is drawn isolated on a flat bone field
with empty margin, so tools/cutout.py can key the background to alpha without
cropping anything flat.

ComfyUI holds ~19 GB of RAM and idle waiters get reaped, so queue and collect
are separate steps:

    python tools/deco_suite.py --wave 1 --queue-only          # 3 seeds per piece
    python tools/deco_suite.py --piece spot_tear --seeds 2 --queue-only
    python tools/deco_suite.py --collect                      # file finished jobs into art/
    python tools/deco_suite.py --wave 1 --dry-run             # print prompts only
"""

import argparse
import json
import random
import re
import shutil
import time
import urllib.request

from comfyui_generate import ART_DIR, COMFYUI_OUTPUT, COMFYUI_URL, PROJECT_ROOT, queue_prompt
from prototype_styles import DIRECTIONS, build_workflow

LOG_PATH = PROJECT_ROOT / "docs" / "art" / "prototype-runs.jsonl"
PREFIX = "aetherfall/deco/"
VERSION = 1

ORNAMENT_STYLE = {
    "loras": [],
    "prefix": (
        "A 1920s Art Deco lithograph printer's ornament, as printed in a luxury book of the "
        "period. Flat printed color shapes with crisp edges, bold geometric simplification, "
        "subtle lithographic paper grain. Strict limited palette of six inks: deep midnight "
        "navy, warm bone ivory, soot black, turquoise cyan, amber gold, and oxblood red."
    ),
    "suffix": (
        "Printed on a plain, flat, empty bone ivory paper background. The ornament is isolated "
        "and centred with a generous empty margin on every side; nothing touches the edges of "
        "the picture. No border around the picture, no background scene, no shadow. Flat "
        "printed color, no photorealism, no 3D, no gradients. Absolutely no text, no letters, "
        "no numbers, no signature."
    ),
}

# Spot style (Session 35, after Wave 2): the D2 portrait prefix talks about light "drawn as
# hard-edged rays and pools" and "arc lamps ... warm lamplight", and Flux answered with a lamp
# in nearly every spot. This prefix keeps the palette rule without the lamp language, and asks
# for varied light.
SPOT_PREFIX = (
    "A 1920s Art Deco travel poster lithograph in the style of Cassandre and WPA railway posters. "
    "Flat printed color shapes, bold geometric simplification, strong diagonals, subtle "
    "lithographic paper grain. Strict limited palette of six inks: deep midnight navy, warm bone "
    "ivory, soot black, turquoise cyan, amber gold, and oxblood red. Turquoise cyan is used ONLY "
    "for magical light, glowing crystals and supernatural energy. Amber gold is used ONLY for "
    "galvanic machinery, electric sparks and fire. Everything ordinary is midnight navy, bone, "
    "soot black and oxblood."
)
SPOT_STYLE = {
    "loras": [],
    "prefix": SPOT_PREFIX,
    "suffix": (
        "Lit by the scene's own light as described (daylight, moonlight, window light or firelight); "
        "no lamps, lanterns or light fixtures unless the scene names one. "
        "Composed as a single round vignette, a circle of picture floating on a plain, flat, "
        "empty bone ivory paper background with a generous empty margin on every side; nothing "
        "touches the edges of the picture. No rectangular border, no frame, no panel. "
        + DIRECTIONS["D2"]["suffix"]
    ),
}

PIECES = {
    # ── Wave 1: ornament kit ──
    "divider_aether": {
        "wave": 1, "art_type": "decorative", "style": ORNAMENT_STYLE, "width": 1536, "height": 384,
        "subject": (
            "A long, slender horizontal section divider for a book page, many times wider than it "
            "is tall. Art Nouveau: whiplash ivy tendrils and small leaves flow out symmetrically "
            "to the left and right from a small central medallion holding a glowing turquoise "
            "crystal. Thin and delicate. Inks: turquoise cyan and deep midnight navy only."
        ),
    },
    "divider_engine": {
        "wave": 1, "art_type": "decorative", "style": ORNAMENT_STYLE, "width": 1536, "height": 384,
        "subject": (
            "A long, slender horizontal section divider for a book page, many times wider than it "
            "is tall. Art Deco machine age: straight parallel rules and stepped chevrons run out "
            "symmetrically to the left and right from a small central riveted medallion with "
            "short amber sunburst rays. Crisp and geometric. Inks: amber gold and soot black only."
        ),
    },
    "divider_neutral": {
        "wave": 1, "art_type": "decorative", "style": ORNAMENT_STYLE, "width": 1536, "height": 384,
        "subject": (
            "A long, slender horizontal section divider for a book page, many times wider than it "
            "is tall. Restrained Art Deco: two thin parallel rules ending in small stepped "
            "terminals, meeting at a small central diamond with a tiny four-point star. Quiet and "
            "elegant. Inks: oxblood red and deep midnight navy only."
        ),
    },
    "dropcap_aether": {
        "wave": 1, "art_type": "decorative", "style": ORNAMENT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A square ornamental initial-letter tile for the first paragraph of a book chapter: a "
            "square frame with an Art Nouveau border of curling ivy tendrils and small glowing "
            "turquoise crystals at the corners, deep midnight navy linework. The centre of the "
            "square is left completely empty as a plain bone panel, with no letter in it."
        ),
    },
    "dropcap_engine": {
        "wave": 1, "art_type": "decorative", "style": ORNAMENT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A square ornamental initial-letter tile for the first paragraph of a book chapter: a "
            "square Art Deco frame with stepped corners, rivets, and short amber sunburst rays "
            "fanning from the top edge, soot black linework. The centre of the square is left "
            "completely empty as a plain bone panel, with no letter in it."
        ),
    },
    "dropcap_neutral": {
        "wave": 1, "art_type": "decorative", "style": ORNAMENT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A square ornamental initial-letter tile for the first paragraph of a book chapter: a "
            "square Art Deco frame of thin parallel lines with stepped corners in oxblood red and "
            "deep midnight navy. The centre of the square is left completely empty as a plain "
            "bone panel, with no letter in it."
        ),
    },
    "tailpiece": {
        "wave": 1, "art_type": "decorative", "style": ORNAMENT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A small symmetrical end-of-chapter printer's ornament, wider than it is tall: a plain "
            "stone keystone in the centre, with a curl of Art Nouveau ivy and a small turquoise "
            "crystal on the left and a fan of Art Deco amber sunburst rays on the right, perfectly "
            "balanced, neither side winning. Compact and simple."
        ),
    },
    # ── Wave 1: spots ──
    # v02 rerolls (user, Session 35): v01 Tear read as amber fire in a rectangle (8c kept as
    # fallback); v01 misfire read as firing into a brick wall (9a closest).
    "spot_tear": {
        "wave": 1, "version": 2, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A rounded vignette: a small 1920s city of stepped Art Deco towers and factory chimneys "
            "in deep midnight navy and soot silhouette, a few oxblood roofs. Above it the night sky "
            "is ripped open by a single jagged vertical crack, like torn paper, and through the crack "
            "pours cold glowing turquoise cyan light in hard-edged rays that fall onto the rooftops. "
            "The only bright color in the picture is the turquoise cyan of the crack. No fire, no "
            "flames, no orange, no smoke clouds. Awe and dread."
        ),
    },
    "spot_misfire": {
        "wave": 1, "version": 2, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A rounded vignette seen from the side: a man's hand in a worn brown leather jacket "
            "sleeve holds a revolver pointed away down a long dark empty alley that recedes into "
            "midnight shadow. The gun has jammed and misfired: the bullet has not left the barrel, "
            "there is no muzzle flash at the barrel's tip; instead a small burst of amber sparks and "
            "a curl of soot-black smoke spits sideways out of the revolver's cylinder, next to the "
            "hand. Nothing stands in front of the gun."
        ),
    },

    # ── Wave 2: spots for chapters 01–11 ──
    "spot_table": {
        "wave": 2, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A round vignette seen from above at a slight angle: a worn wooden tavern table by "
            "lamplight with two ten-sided dice, a holstered revolver, an open notebook of "
            "geometric spell diagrams glowing faintly turquoise, a pencil, and a glass of beer. "
            "Warm amber lamplight on one side, cold turquoise glow from the notebook on the other."
        ),
    },
    "spot_tram": {
        "wave": 2, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A round vignette: an abandoned 1920s electric tram car standing on rusted rails in a "
            "clearing, swallowed by giant Art Nouveau ivy, ferns and small glowing turquoise "
            "crystals growing through its broken windows. Tall strange trees behind it. Quiet, "
            "overgrown, wondrous."
        ),
    },
    "spot_charter": {
        "wave": 2, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A round vignette still life on a patron's dark wooden desk: a folded parchment "
            "charter with a large oxblood wax seal and ribbon, an iron key, a small stack of "
            "coins and banknotes, and a brass desk lamp casting a warm pool of light. The "
            "parchment is blank, with no writing."
        ),
    },
    "spot_kit": {
        "wave": 2, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A round vignette seen from directly above: an adventurer's kit laid out neatly on a "
            "narrow iron bed: a folded long coat, a leather holster, a notebook, a brass compass "
            "on a cord, a small charm of turquoise crystal, heavy boots, a coil of rope."
        ),
    },
    "spot_dice": {
        # v02 (user, Session 35): v01 drew six-sided dice with pips under a lamp every time
        "wave": 2, "version": 2, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A round vignette: a gloved hand has just thrown two ten-sided gaming dice across a "
            "green baize card table in afternoon daylight from a tall window. Each die is a "
            "pentagonal trapezohedron, a long pointed shape made of ten kite-shaped faces, like "
            "two five-sided pyramids joined point to point; one is bone white, one is oxblood red. "
            "They tumble in mid-air with motion lines. Plain faces, no numbers, no pips."
        ),
    },
    "spot_wounded": {
        "wave": 2, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A round vignette: a tired man in rolled shirtsleeves and braces sits on a wooden "
            "crate in a dim back room, binding a wounded forearm with a strip of white bandage, "
            "one end held in his teeth. A single hanging lamp throws a hard pool of warm light. "
            "Oxblood stain on the cloth, nothing gory."
        ),
    },
    "spot_lockpicks": {
        "wave": 2, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A round vignette close-up: two gloved hands working a pair of slender lockpicks into "
            "the keyhole of an ornate Art Deco brass door lock, lit by a narrow beam of light."
        ),
    },
    "spot_magnifier": {
        "wave": 2, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A round vignette close-up: a brass magnifying glass held over an old street map "
            "marked with pins and string, the lens enlarging a small detail. Lamplight. The map "
            "has streets and shapes only, no writing."
        ),
    },
    "spot_handshake": {
        "wave": 2, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A round vignette: two hands shaking across a card table in a smoky club, one in a "
            "fine suit cuff with a ring, one in a worn leather sleeve; playing cards and coins "
            "scattered below. The cards are plain, with no symbols."
        ),
    },
    "spot_scholarly": {
        "wave": 2, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A round vignette: a tall, gaunt man in round wire spectacles, waistcoat and long coat "
            "kneels on a stone floor inside a precise chalk circle of geometric figures, one palm "
            "raised; flat hard-edged turquoise light rises from the chalk lines in clean "
            "geometric planes. Controlled and exact."
        ),
    },
    "spot_wild": {
        "wave": 2, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A round vignette: a slight young woman with jagged jaw-length black hair and an "
            "oversized canvas coat thrusts one open hand forward; turquoise light and whipping "
            "Art Nouveau ivy tendrils erupt wildly from her palm. Her eyes glow faintly turquoise. "
            "Raw, barely steered."
        ),
    },
    "spot_street": {
        # v03 (user, Session 35): v01/v02 read industrial on both sides (power lines, lamps,
        # stacks). The Aether half now has no buildings at all.
        "wave": 2, "version": 3, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A round vignette split exactly down the middle by a single cobbled road running away "
            "from the viewer. LEFT of the road: a soot-black brick factory wall, one smokestack and "
            "amber electric sparks, the only man-made things in the picture. RIGHT of the road: no "
            "buildings at all, only a deep wild forest of giant Art Nouveau ivy, ferns and tall "
            "glowing turquoise crystals growing out of the ground, with turquoise light between "
            "the trees. No power lines, no poles, no streetlights, no lamps on the right side."
        ),
    },
    "spot_scales": {
        # Alternative for the same slot (Ch 10): the balance as a still life, so the halves can't blur
        "wave": 2, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A round vignette still life against a plain deep midnight navy background: an old brass "
            "balance scale, perfectly level. In the left pan sits a riveted iron cog throwing a few "
            "amber electric sparks. In the right pan sits a single glowing turquoise crystal wrapped "
            "in a curl of Art Nouveau ivy. Symmetrical, simple, bold. Moonlight, no lamps."
        ),
    },
    "spot_timing": {
        "wave": 2, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A round vignette still life on a wooden crate: a hunting knife, three revolver "
            "cartridges standing upright, and an open brass pocket watch, lit by a hard amber "
            "work lamp. The watch face has no numerals, only tick marks."
        ),
    },
    "sigil_aetheric": {
        "wave": 2, "art_type": "decorative", "style": ORNAMENT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A circular Art Deco medallion emblem, like a stamped enamel badge: a thin double ring border in deep midnight navy around a flat bone disc, and in the centre a single bold symbol: a stylised open hand with hard-edged turquoise rays bending and radiating from the palm (raw force and energy). Simple, symmetrical, readable when printed small. One of a matching set of six.',
    },
    "sigil_vivimancy": {
        "wave": 2, "art_type": "decorative", "style": ORNAMENT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A circular Art Deco medallion emblem, like a stamped enamel badge: a thin double ring border in deep midnight navy around a flat bone disc, and in the centre a single bold symbol: a single leaf whose veins form a tiny human heart, drawn in turquoise and oxblood (life and the body). Simple, symmetrical, readable when printed small. One of a matching set of six.',
    },
    "sigil_warding": {
        "wave": 2, "art_type": "decorative", "style": ORNAMENT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A circular Art Deco medallion emblem, like a stamped enamel badge: a thin double ring border in deep midnight navy around a flat bone disc, and in the centre a single bold symbol: a tall pointed shield with a turquoise keyhole-shaped seal in its centre (protection and sealing). Simple, symmetrical, readable when printed small. One of a matching set of six.',
    },
    "sigil_divination": {
        "wave": 2, "art_type": "decorative", "style": ORNAMENT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A circular Art Deco medallion emblem, like a stamped enamel badge: a thin double ring border in deep midnight navy around a flat bone disc, and in the centre a single bold symbol: a single stylised open eye with a turquoise star for its pupil and fine rays around it (perception and knowledge). Simple, symmetrical, readable when printed small. One of a matching set of six.',
    },
    "sigil_transmutation": {
        "wave": 2, "art_type": "decorative", "style": ORNAMENT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A circular Art Deco medallion emblem, like a stamped enamel badge: a thin double ring border in deep midnight navy around a flat bone disc, and in the centre a single bold symbol: a cube turning into a crystal, half solid midnight block, half faceted turquoise crystal (altering matter). Simple, symmetrical, readable when printed small. One of a matching set of six.',
    },
    "sigil_ley": {
        "wave": 2, "art_type": "decorative", "style": ORNAMENT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A circular Art Deco medallion emblem, like a stamped enamel badge: a thin double ring border in deep midnight navy around a flat bone disc, and in the centre a single bold symbol: three turquoise lines woven into a looping knot like threads on a loom (weaving magic itself). Simple, symmetrical, readable when printed small. One of a matching set of six.',
    },

    # ── Wave 3 (Session 35): chapter art standard + variety rule; no lamp focus ──
    "spot_operatives": {
        "wave": 3, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A round vignette in bright morning daylight: four Society operatives in long coats and hats stride together across a busy rail yard between steaming locomotives, seen from a low angle, purposeful. Big sky.',
    },
    "spot_silhouettes": {
        "wave": 3, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A round vignette: four very different adventurers standing on a hilltop in silhouette against a huge dawn sky: a broad man with a revolver on his hip, a slight young woman with wild hair and a faint turquoise glow at one hand, a tall thin man with a walking stick and satchel, and a composed woman in a long coat. Strong, simple shapes.',
    },
    "spot_backlash": {
        "wave": 3, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A round vignette: a caster in a dark coat is thrown backwards off their feet in an empty stone courtyard at dusk as their own spell recoils on them: a jagged burst of turquoise light snaps back into their chest, cracks of turquoise light running up their arms. Dynamic diagonal composition.',
    },
    "spot_knife": {
        "wave": 3, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A round vignette in a sunlit whitewashed courtyard at noon: a quick, lean knife fighter lunges low and close at a startled gunman who is still drawing his revolver from its holster. Hard black noon shadows on the ground. Frozen instant of motion, diagonal composition.',
    },
    "spot_market": {
        "wave": 3, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": "A round vignette of a busy 1920s market street in daylight: striped awnings, a pawnbroker's shopfront with three brass balls hanging over the door, crowds in hats and coats, and in the foreground two hands passing a folded banknote. No readable signs.",
    },
    "spot_collector": {
        "wave": 3, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A round vignette: a large man in a bowler hat and heavy overcoat stands at the door of a narrow terraced house on a grey rainy afternoon, holding a small ledger, while a worried face peers through the half-open door. Rain drawn as flat diagonal lines.',
    },
    "spot_catalogue": {
        # v02 (user, Session 35): v01's galvanic pistol didn't read as galvanic
        "wave": 3, "version": 2, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": (
            "A flat catalogue plate on plain bone paper, seen from directly above, three objects laid "
            "side by side and evenly spaced like a 1920s mail-order catalogue illustration, no table, "
            "no scene: on the left a plain black six-shot revolver; in the middle a hunting knife in a "
            "leather sheath; on the right a strange galvanic arc-pistol, clearly a machine, not a "
            "revolver: a fat brass barrel wound with copper coils, a glass capacitor bulb glowing amber "
            "on top, and bright amber electric sparks crackling at its muzzle."
        ),
    },
    "spot_airship": {
        "wave": 3, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A round vignette in clear afternoon daylight: a small sleek airship with a riveted gondola drifts low over the stepped rooftops of a 1920s city, and on the street below a black motorcar drives past. Big white clouds, bold shapes.',
    },
    "spot_watch": {
        "wave": 3, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A round vignette outdoors on a windy hillside at dusk: a gloved hand holds up an open brass pocket watch that is leaking thin streams of glowing turquoise light, like smoke, from its seams. Tall grass bending in the wind behind.',
    },
    "spot_ward": {
        "wave": 3, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A round vignette of a narrow stone doorway on a quiet cobbled street in morning light, seen from across the street: a small ward charm of twisted iron and a turquoise crystal is nailed above the door frame, glowing faintly, with a faint turquoise geometric seal shimmering across the doorway.',
    },
    "spot_vial": {
        "wave": 3, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A round vignette: a young man in shirtsleeves on a rooftop at dusk tips back his head and drinks from a small glass vial; a turquoise glow shines through his throat and the vial. The city skyline behind him. Calm and uncanny.',
    },
    "spot_rooftops": {
        "wave": 3, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A round vignette at night under a huge full moon: two figures leap between the slate rooftops of a 1920s city, coats flying, chimney pots and water tanks in silhouette, the moon lighting everything from behind.',
    },
    "spot_informant": {
        "wave": 3, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A round vignette at noon on a sunlit back street: a thin informant in a flat cap leans out of a half-open doorway and speaks quietly to a figure in a long coat standing in the street. Hard noon shadows, washing lines overhead.',
    },
    "spot_notebook": {
        "wave": 3, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A round vignette: an operative in a long coat and hat walks briskly along a busy city pavement in daylight, glancing down at a small open pocket notebook in one hand. Pedestrians, a tram and shopfronts blurred into flat shapes behind.',
    },
    "spot_drawers": {
        "wave": 3, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A round vignette inside a tall record office: a clerk on a rolling ladder pulls one small drawer from a wall of hundreds of identical wooden card-catalogue drawers. Bright daylight falls in hard shafts from high arched windows. No readable labels.',
    },
    "spot_handler": {
        "wave": 3, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A round vignette: a handler seen from behind stands at a tall arched window looking out over a 1920s city by day, hands clasped behind their back; maps and photographs are pinned to the wall beside the window, connected by string. No readable writing.',
    },
    "spot_foundry": {
        "wave": 3, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A round vignette at night: a huge decommissioned brick resonance foundry with a cracked glass roof and cold chimneys stands on a riverbank; faint amber sparks still flicker inside the broken windows. Moon behind, reflections in the river.',
    },
    "spot_tunnels": {
        "wave": 3, "art_type": "spots", "style": SPOT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A round vignette: an old brick smuggling tunnel running away underground, its walls cracked open by thick clusters of glowing turquoise crystals that light the whole tunnel; wooden crates stacked along one side, a figure small in the distance.',
    },
    "corner_nouveau": {
        "wave": 3, "art_type": "decorative", "style": ORNAMENT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A single corner ornament for the top-left corner of a text box: two lines meeting at a right angle, with Art Nouveau whiplash ivy tendrils and a small turquoise crystal curling from the corner. Deep midnight navy and turquoise cyan only. The inside of the angle is empty.',
    },
    "corner_deco": {
        "wave": 3, "art_type": "decorative", "style": ORNAMENT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A single corner ornament for the top-left corner of a text box: stepped Art Deco lines meeting at a right angle, with a small amber quarter-sunburst fanning from the corner and two rivets. Soot black and amber gold only. The inside of the angle is empty.',
    },
    "badge_galvanic": {
        "wave": 3, "art_type": "decorative", "style": ORNAMENT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A small circular Art Deco badge for marking a Galvanic zone on a map: a riveted iron ring around a bold amber lightning bolt crossed with a cog. Soot black and amber gold only.',
    },
    "badge_aetheric": {
        "wave": 3, "art_type": "decorative", "style": ORNAMENT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A small circular Art Deco badge for marking an Aetheric zone on a map: a ring of curling Art Nouveau ivy around a single glowing turquoise crystal. Deep midnight navy and turquoise cyan only.',
    },
    "badge_neutral": {
        "wave": 3, "art_type": "decorative", "style": ORNAMENT_STYLE, "width": 1024, "height": 1024,
        "subject": 'A small circular Art Deco badge for marking a neutral zone on a map: a plain double ring around a simple four-point compass star. Oxblood red and deep midnight navy only.',
    },
}


def dest_for(piece: str, seed: int, version: int | None = None):
    version = version or PIECES[piece].get("version", VERSION)
    return ART_DIR / PIECES[piece]["art_type"] / "generated" / f"deco-{piece}_v{version:02d}_seed-{seed}.png"


def collect_from_history():
    """Copy every finished aetherfall/deco job in ComfyUI's history into art/, logging new ones."""
    hist = json.loads(urllib.request.urlopen(f"{COMFYUI_URL}/history?max_items=500").read())
    copied = 0
    for h in hist.values():
        prompt = h["prompt"][2]
        save = next((v for v in prompt.values() if v["class_type"] == "SaveImage"), None)
        if not save or not save["inputs"]["filename_prefix"].startswith(PREFIX):
            continue
        # Prefix is "<piece>" (v01 jobs) or "<piece>_vNN"
        m = re.match(r"(\w+?)(?:_v(\d+))?$", save["inputs"]["filename_prefix"][len(PREFIX):])
        piece, version = m.group(1), int(m.group(2) or 1)
        if piece not in PIECES:
            continue
        seed = next(v for v in prompt.values() if v["class_type"] == "KSampler")["inputs"]["seed"]
        dest = dest_for(piece, seed, version)
        if any((dest.parent.parent / stage / dest.name).exists() for stage in ("generated", "approved", "archived")):
            continue
        for out in h.get("outputs", {}).values():
            for img in out.get("images", []):
                src = COMFYUI_OUTPUT / img["subfolder"] / img["filename"]
                if not src.exists():
                    continue
                shutil.copy2(src, dest)
                copied += 1
                text = next(v for v in prompt.values() if v["class_type"] == "CLIPTextEncode" and v["inputs"]["text"])["inputs"]["text"]
                p = PIECES[piece]
                with LOG_PATH.open("a") as f:
                    f.write(json.dumps({
                        "time": time.strftime("%Y-%m-%d %H:%M:%S"), "file": str(dest.relative_to(PROJECT_ROOT)),
                        "status": "ok", "direction": "D2", "subject": f"deco_{piece}", "seed": seed,
                        "model": "flux1-dev fp8", "steps": 30, "guidance": 3.5, "sampler": "euler/normal",
                        "loras": [], "width": p["width"], "height": p["height"], "prompt": text,
                    }) + "\n")
                print(f"collected {dest.relative_to(PROJECT_ROOT)}")
    print(f"{copied} new file(s)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--wave", type=int)
    ap.add_argument("--piece", choices=list(PIECES), action="append")
    ap.add_argument("--seeds", type=int, default=3)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--queue-only", action="store_true", help="queue jobs and exit (the only queueing mode)")
    ap.add_argument("--collect", action="store_true")
    args = ap.parse_args()

    if args.collect:
        return collect_from_history()
    if not (args.queue_only or args.dry_run):
        ap.error("use --queue-only (then --collect later) or --dry-run")

    pieces = args.piece or [k for k, v in PIECES.items() if args.wave is None or v["wave"] == args.wave]
    rng = random.Random()
    for piece in pieces:
        p = PIECES[piece]
        for _ in range(args.seeds):
            seed = rng.randint(0, 2**32 - 1)
            wf, text = build_workflow(p["style"], p, seed, f"{PREFIX}{piece}_v{p.get('version', VERSION):02d}")
            if args.dry_run:
                print(f"--- {dest_for(piece, seed).name}\n{text}\n")
                continue
            pid = queue_prompt(wf)["prompt_id"]
            print(f"queued {dest_for(piece, seed).name} ({pid})", flush=True)
    if args.queue_only:
        print("run with --collect when ComfyUI's queue is empty")


if __name__ == "__main__":
    main()
