# KMM — Option A: Fantasy chase (2D painterly pencil-line look)

Status: generated as draft. Job `4b444547-6ee7-43bf-badb-c6ac5d3ea6f9` (created 2026-09-30 ~15:16 UTC).
Content not yet reviewed by the assistant (cannot view video).

## Settings
| Key | Value |
|---|---|
| model | `seedance_2_5` |
| mode | `omni_reference` |
| draft | true (480p; finalize 1080p later via `draft_job_id`, valid 7 days) |
| resolution | 480p |
| duration | 25 s |
| aspect_ratio | 16:9 |
| generate_audio | false |
| folder_id | `fef878e4-1957-439e-8b50-00a4ee8454c6` (project "MV KMM") |
| declined_preset_id | `24bae836-2c4a-48e0-89b6-49fcc0b21612` ("IN THE DARK", declined on purpose) |
| estimated cost | 75 credits (get_cost) |

## References (order = Image N in the prompt)
| Slot | Content | media_id |
|---|---|---|
| Video 1 | style ref (video) | `3ee6fe08-adc6-4715-a9ea-b441b5758864` |
| Image 1 | 01_Mai | `b42c82ad-d58e-4fb3-bcf3-4d89dac09517` |
| Image 2 | 17_Soi (night-shadow wolf) | `f48ff106-d9d6-4233-a770-d36f768a1f64` |
| Image 3 | 18_Qua (crow) | `6a271d30-4602-4348-8042-8728526956c5` |
| Image 4 | 19_Nhen (spider) | `cdcbdc48-05d0-4875-b2c4-eb77a56cb96b` |
| Image 5 | night-shadow person (new ref) | `2f07fe73-628d-4761-aeff-0b32446d8a0c` |
| Image 6 | fantasy entrance | `245f07de-6ccc-4a7c-b49d-3247f32aecb6` |
| Image 7 | fantasy forest | `a7a8f636-a610-4b1d-b408-639525c4d8a0` |
| Image 8 | digital river | `3d129dd5-55a6-46f3-b9a7-80f8e299bf27` |
| Image 9 | large gate (text removal NOT confirmed) | `607ae6ae-2bf6-4148-852e-aae51d9de070` |

Assumptions not confirmed by the user: roles of images 6-9 were assigned by the order the user listed them, not by file name; image 9 may still contain writing.

## Prompt
```
Create a 25-second stylized animated chase sequence in ONE generation with hard cuts between 13 shots. Mai, age 11, is chased by night-shadow creatures through a dark fantasy world. Mood: frightening but child-safe, stylized, never gory. No creature ever touches Mai; the wolf stays several body lengths behind her at all times.

REFERENCES
Video 1: art style reference only. Reproduce its soft painterly feature-animation look, thin loose pencil sketch lines and gentle weighted motion. Do NOT copy its bright morning lighting or its school content; this sequence is dark night with cool blue fantasy lighting taken from the location references.
Image 1: Mai. Character reference sheet, use only for design, draw ONE figure, not the sheet layout. Match her face, hair, hair clip, clothing and backpack exactly as Image 1. She never wears a hoodie.
Image 2: the night-shadow wolf. Tall lean dark smoke silhouette with soft wispy smoke edges, small glowing amber eyes, pointed upright ears, long muzzle, bushy tail, NO teeth, semi-transparent. Design only, ONE figure.
Image 3: the night-shadow crow. Design only. Image 4: the spider. Design only.
Image 5: the night-shadow person: tall thin hunched black silhouette, long arms, pointed head, messy hair, two glowing yellow eyes, slim suit, pointed shoes, thin loose pencil lines. Design only, ONE figure, draw without the white background.
Image 6: fantasy entrance location (shots 2-5). Image 7: fantasy forest location (shots 6, 11, 12, 13). Image 8: digital river location (shots 7-10). Image 9: the large gate (shot 13). Use each as the exact source for layout and mood. Do not add or redesign permanent objects.

STYLE
EXACTLY the same art style as Video 1 and the character references: stylized soft rounded volumes, thin loose pencil sketch lines, painterly shading, matte surfaces, subtle grain, not chibi. Children 6-6.5 heads tall. Dark night, cool blue and violet lighting, deep focus, stable linework, no flicker. Faces stay clear and stable.

SHOTS
0:00-0:01 Shot 1, pitch-black night, close-up of the night-shadow wolf's face, crouched, then lunging straight toward the camera. Smoke silhouette with soft wispy edges, small glowing amber eyes, no teeth. Cut.
0:01-0:03 Shot 2, fantasy entrance, wide shot from behind Mai. Mai runs in panic deep into the entrance of the fantasy world. Cut.
0:03-0:04 Shot 3, fantasy entrance, side view, camera tracks Mai from waist to head. Mai runs fast in panic, her face tearful, lips trembling. Cut.
0:04-0:05 Shot 4, fantasy entrance, side view tracking the wolf. The wolf bursts into frame running fast after Mai, staying well behind her. Cut.
0:05-0:08 Shot 5, fantasy entrance, side view tracking the wolf. The wolf keeps running fast after Mai, smoke trailing behind it, never touching her. Cut.
0:08-0:11 Shot 6, fantasy forest, wide shot. Mai runs fast out of the entrance into the forest. Cut.
0:11-0:13 Shot 7, digital river, wide shot from behind. Mai runs along the bank of the digital river. Cut.
0:13-0:15 Shot 8, digital river, side view. Mai runs and cries. Cut.
0:15-0:17 Shot 9, digital river, behind Mai. A spider lowers itself on a silk thread from above into the space in front of her. Cut.
0:17-0:19 Shot 10, digital river, wide shot. Mai flinches, dodges the spider, turns back and runs in the opposite direction, toward the camera. Cut.
0:19-0:21 Shot 11, fantasy forest, medium shot. A night-shadow crow chases Mai from behind, in the air, never touching her. Cut.
0:21-0:23 Shot 12, fantasy forest, close-up. The crow transforms into the night-shadow person and grows two wings. Cut.
0:23-0:25 Shot 13, fantasy forest, medium shot. Mai runs in panic and stops in front of the large gate. Hold.

MAINTAIN
Keep Mai identical in every shot: face, hair, clip, clothing, backpack. Keep the wolf, crow, spider and shadow person identical to their references. Consistent dark night lighting. Mai is the clear main subject in every shot.

AVOID
Any text, letters, numbers, code, logos, writing, readable signs, browser address bars, tabs, lock icons or keypad digits anywhere; if a location reference contains writing or interface text, do not reproduce it and leave that surface blank. Any creature touching Mai; teeth; blood; gore; realistic violence; shadow creatures that look different from their references; more than one Mai; duplicated characters; hoodie; chibi; photorealism; anime glow; flat 2D; bright daylight; shallow depth of field, bokeh or blur; sliding feet; flicker; faces that flicker or blur.
```

## Notes
- Script source: 13 shots, 1/2/1/1/3/3/2/2/2/2/2/2/2 s = 25 s.
- Shot 10 direction (Mai turns back and runs toward camera) and shots 4/5 split were the assistant's choices, not confirmed by the user.
- Standing project rules applied: no text/numbers anywhere, shadow creatures never touch the child, Mai never wears a hoodie, children 6-6.5 heads.
