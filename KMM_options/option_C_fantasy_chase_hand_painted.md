# KMM — Option C: Fantasy chase, hybrid 3D/2D hand-painted (style C)

Status: generated as draft. Job `0a5cf4c2-6ef7-4998-a156-07b33d652d26` (created 2026-10-01 ~07:12 UTC).
Content not yet reviewed by the assistant (cannot view video).
Style rules: see `STYLE_GUIDE_A_B_C.md`. Same script, plates and settings as B v3 (`option_B_v3_fantasy_chase_new_backgrounds.md`), art style swapped to style C.

## What the user asked / what the assistant assumed
- User asked: B structure and rules, but with the style C art-style text.
- The user did not upload a separate "@Image 1" style image. ASSUMED: Ref 1 = `01_Mai` (`b42c82ad…`) is the painted style source. Not confirmed; the assistant cannot see whether `01_Mai` is hand-painted.
- NO video style ref (StandardB is B's 3D look and could pull C toward B). Decided with the user's "ok" to the proposal; confirm if wrong.
- Plates (entrance/forest/river/gate) are repainted in the hand-painted style, flatter than the character; photoreal textures not copied.
- Conflicts resolved: monitors flicker is written as "flicker softly" (C forbids strobe); creatures keep small amber eyes (project rule) so the only warm notes are red neckerchief, light-blue backpack and those eyes.

## Settings
model `seedance_2_5`, mode `omni_reference`, draft true, 480p, 25 s, 16:9, generate_audio false, folder `fef878e4-1957-439e-8b50-00a4ee8454c6`, declined_preset_id `24bae836-2c4a-48e0-89b6-49fcc0b21612`. Cost 75 credits (get_cost).

## References (Ref N order, no video)
1 Mai `b42c82ad-d58e-4fb3-bcf3-4d89dac09517` · 2 wolf `f48ff106-d9d6-4233-a770-d36f768a1f64` · 3 crow `6a271d30-4602-4348-8042-8728526956c5` · 4 spider `cdcbdc48-05d0-4875-b2c4-eb77a56cb96b` · 5 shadow person `2f07fe73-628d-4761-aeff-0b32446d8a0c` · 6 entrance `b97b3e97-5b27-4deb-92ea-a10693bc61e9` · 7 forest `d823d7cf-984c-4298-a9ab-62cd1b809b0b` · 8 digital river `fa8a5475-6c31-41b3-91ba-9881972d4319` · 9 gate (text-free) `5aa39a50-f435-41b1-8f99-def9153bc90f`

## Prompt differences from B v3 (shot list identical)
Opening line:
```
STYLE FIRST: the art style of this whole sequence is the hand-painted hybrid 3D/2D look described in [Visual Style], taken from Ref 1. Apply it to every frame.
```
[References] Ref 1: "Mai's identity, costume and character design AND the art style reference ... take the hand-painted finish and line work from it." Refs 2-5: painted in the same hand-painted style. Refs 6-9: "repaint them in the hand-painted style, flatter than the character".

[Visual Style] (style C text, verbatim from the user with minor additions at the end):
```
Stylized hybrid 3D/2D animation with a hand-painted finish from Ref 1: watercolor washes, gouache dry-brush, soft cel-shade edges, sparse sepia-charcoal line work, never pure black; paper grain low and even over the paint but never on facial skin; colored-pencil hatching only on cloth, hair, bark, concrete and background, never on skin of face, neck, arms or hands; skin clean and uniform with no marks, lines, dots or freckles. Backgrounds flatter than the character. Palette black-teal, indigo and cold blue; her red neckerchief and light-blue backpack are the only warm-ish notes, apart from the creatures' small amber eyes. Line weight stays stable: no line boil, no shimmer, no strobe. Children 6-6.5 heads tall, not chibi. Faces stay clear and stable. 16:9, 24 fps.
```
[Avoid]: contact with Mai, teeth, blood, gore, jump scare, any text/letters/numbers/code/browser bars/keypad digits, pure black, photorealism, photoreal textures, live-action grain, anime, morphing, extra fingers, sliding feet, line boil, shimmer, strobe, hatching or marks or freckles on skin, flicker of Mai's face or body. ("flat 2D" and "crushed black" from B were removed.)

[Action] shots 1-13 as in B v3, with "flicker softly" for the monitors.

## Notes
- If `01_Mai` is not painted, the style will come only from the text; the user may need to upload a painted Mai image and regenerate.
- Gate image is very dark; shot 13 may be darker than the others.
