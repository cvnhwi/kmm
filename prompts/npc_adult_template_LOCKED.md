# NPC Adult Template — LOCKED (MV KMM)

Status: **LOCKED** — approved 30/09. Do not change the fixed blocks; only fill the `{...}` slots.

## Settings

| Setting | Value |
|---|---|
| Tool | Higgsfield MCP |
| Model | `seedream_v5_pro` (Seedream 5.0 Pro) |
| Aspect ratio | 16:9 |
| Resolution | 2k |
| Style reference (always) | `9c3dda0e-6e61-46e3-aa6d-681d202e9ee3` (01_Mai.png), role `image_references` |
| Save to | Project **MV KMM** — `folder_id: fef878e4-1957-439e-8b50-00a4ee8454c6` (workspace `7d16e180-91e1-4bfc-a35e-8eed97d27b03`) |
| Items per image | 4 characters, one row |

Approved output (reference for this template): job `78670345-f6b9-49d3-9103-01dfc0d41343` (young adults set 1), job `36adbbc9-93d3-49d8-9893-144b651f7c9c` (young adults set 2).

## Slot rules

- `{GROUP}`: e.g. `young Vietnamese adults aged 20 to 32`
- `{CHAR_1..4}`: outfit + props, then a **unique face**: face shape, eye shape/size, brows, hairstyle, skin tone, body type. No two characters may share a face shape or hairstyle.
- `{PALETTE}`: default `white, navy, sky blue, clean red accents, cream, warm grey`

## Prompt

```
Create four new characters painted by the same artist, in exactly the same style, as the reference image of the girl Mai. Match the reference's balance of 2D and 3D precisely: it is a hand-painted illustration first, with only a light sense of 3D volume underneath. Do not draw Mai herself, and do not give anyone Mai's face: every character must have a clearly different, individual face.

Full-body character lineup of four {GROUP}, standing side by side in one row, evenly spaced, same scale, adult proportions about seven heads tall, each fully visible from head to feet, none overlapping, plain pure white seamless background. Left to right:
(1) {CHAR_1}
(2) {CHAR_2}
(3) {CHAR_3}
(4) {CHAR_4}

Keep the reference's facial rendering (painted rosy cheeks, simple small nose, soft gentle expression, warm brown irises), but vary face shape, eye shape and size, brows, nose width, hairstyle, skin tone and body type as described so no two characters look alike. Relaxed neutral standing poses, three-quarter to front view, clean readable silhouettes, nothing caricatured. Absolutely no text, letters, numbers or logos anywhere.

Texture exactly like the reference, a 2D/3D hybrid leaning toward 2D: flat-ish painted color areas with soft gouache gradients, visible brush strokes and colored-pencil grain on skin, hair and fabric, hair painted as grouped strokes, fabric folds described with painted strokes rather than rendered geometry. Only gentle simplified form shading, no realistic skin detail, no pores, no subsurface glow, no sculpted 3D look. Expressive hand-drawn overlay: thin loose dark charcoal sketch lines around silhouettes, hair, faces and clothing edges, drifting slightly off the forms like a gesture drawing, no hatching. Subtle fine grain over the whole image, matte finish. Soft diffused even studio lighting, no sunlight, no harsh shadows. Soft blue-grey diffused drop shadow beneath each character. Eye-level camera, horizontal 16:9. Palette like the reference: {PALETTE}.
Negative: Mai, identical faces, same face repeated, clone faces, children, photorealistic, real photo, 3D render, CGI, Pixar-like 3D, clay model, plastic doll look, uncanny skin, glossy skin, anime, flat vector, background scenery, extra people, text, letters, numbers, logos, distorted hands, extra fingers, stretched proportions, harsh shadows, sunlight.
```

## Example character slot

```
(1) young male office worker, light blue short-sleeved shirt, dark trousers, black backpack, takeaway coffee cup; long oval face, narrow almond eyes, straight thick eyebrows, short side-parted black hair, light tan skin, slim build.
```

## Elderly variant (pending approval)

For elderly NPCs, keep the template above and additionally:
- Add young-adult set 1 (`78670345-f6b9-49d3-9103-01dfc0d41343`) as a **second** `image_references` for proportion/world matching.
- State: same body construction and head-to-body ratio as reference 2, ~7 heads tall, only slightly shorter from a gentle stoop.
- Age via light pencil lines around eyes/mouth + grey/white hair, never sculpted wrinkles.
- Extra negatives: `big heads, chibi proportions, short stubby limbs, doll-like bodies, sculpted wrinkles, realistic aged skin`.
