# KMM — Option B v3: Fantasy chase (3D block look) with new backgrounds

Status: DRAFT PROMPT, NOT YET GENERATED. Waiting for the user's "gen".
Builds on `option_B_v2_fantasy_chase_3d_video_ref.md` (job `8267611b-5861-4da9-bc89-4e195ac7f1cd`).

## Difference from B v2
- Entrance, forest and digital-river plates replaced by new uploads (below).
- New effects: monitors flicker on/off; profile cards in the digital river stream deep into the tunnel.
- [Visual Style] / [Avoid] adjusted because the new plates look near-photoreal: locations are re-rendered in the stylized look of Video 1, textures not copied.
- Monitor/card faces are background detail only.

## Settings
model `seedance_2_5`, mode `omni_reference`, draft true, 480p, 25 s, 16:9, generate_audio false, folder `fef878e4-1957-439e-8b50-00a4ee8454c6`, declined_preset_id `24bae836-2c4a-48e0-89b6-49fcc0b21612`. Cost 75 credits (get_cost accepted all media ids).

## References (order)
Video 1 `c5746038-2de6-4154-852e-6e431e457aa5` (StandardB)
Ref 1 Mai `b42c82ad-d58e-4fb3-bcf3-4d89dac09517` · Ref 2 wolf `f48ff106-d9d6-4233-a770-d36f768a1f64` · Ref 3 crow `6a271d30-4602-4348-8042-8728526956c5` · Ref 4 spider `cdcbdc48-05d0-4875-b2c4-eb77a56cb96b` · Ref 5 shadow person `2f07fe73-628d-4761-aeff-0b32446d8a0c`
Ref 6 entrance (NEW) `b97b3e97-5b27-4deb-92ea-a10693bc61e9` · Ref 7 forest (NEW) `d823d7cf-984c-4298-a9ab-62cd1b809b0b` · Ref 8 digital river (NEW) `fa8a5475-6c31-41b3-91ba-9881972d4319` · Ref 9 gate `607ae6ae-2bf6-4148-852e-aae51d9de070` (text removal still unconfirmed)

Roles of Refs 6-8 follow the order the user gave (entrance, forest, river); file names are auto-generated and were not used.

## Prompt
```
STYLE REFERENCE FIRST: Video 1 is the look reference for this whole sequence. Match its render look, materials and motion quality on every frame.

[Generation Goal] A frightened student runs through a dark fantasy world, chased by night-shadow creatures, in one 25-second sequence of 13 shots with hard cuts. 16:9. The creatures never touch her.

[References]
Video 1 (look reference, highest priority for overall look): reproduce its render style, surface treatment, colour handling and animation feel on Mai, the creatures and the locations. Do not copy its lighting, setting or story content. Where Video 1 and Ref 1 differ in look, follow Video 1 for the overall look and Ref 1 for Mai's identity.
Ref 1 is Mai's identity, costume and character design: use her face, hair, hair clip and clothing, and match its materials. It is a character reference sheet: use it only for design, draw ONE figure, not the sheet layout. Do not use its white studio background.
Ref 2 is the wolf design: dark smoke silhouette, soft wispy edges, small glowing amber eyes, no teeth, semi-transparent. Ref 3 is the crow. Ref 4 is the spider. Ref 5 is the night-shadow person: tall thin hunched black silhouette, long arms, pointed head, two glowing eyes; draw without its white background. Each is design only, ONE figure.
Refs 6-9 are the locations: Ref 6 fantasy entrance (shots 2-5), Ref 7 fantasy forest (shots 6, 11, 12, 13), Ref 8 digital river (shots 7-10), Ref 9 large gate (shot 13). Use their layout, composition and mood exactly, but render them in the stylized look of Video 1; do not copy photoreal textures. Faces and eyes on screens or cards are small background detail only. Do not reproduce any writing or interface text that appears in them; leave those surfaces blank.

[Opening Composition] Shot 1 opens in pitch-black darkness on a close-up of the wolf's face. Shot 2 is a wide view from behind Mai entering the fantasy entrance.

[Subject] Mai, age 11, running in panic and crying, chased by a smoke wolf, a night-shadow crow and a night-shadow person. One physical student only; the creatures are dark smoke forms that never make contact. She never wears a hoodie.

[Action]
0-1s Shot 1: wolf close-up, crouches and lunges toward the camera. Cut.
1-3s Shot 2: wide, from behind, Mai runs deep into the fantasy entrance; the monitors on the walls flicker on and off. Cut.
3-4s Shot 3: side view tracking Mai from waist to head, running, tearful, lips trembling; screens flicker in the background. Cut.
4-5s Shot 4: side view tracking the wolf, it bursts into frame after her, well behind. Cut.
5-8s Shot 5: side view tracking the wolf, it keeps chasing, smoke trailing, never touching her; screens flicker on the walls. Cut.
8-11s Shot 6: wide, Mai runs out of the entrance into the forest. Cut.
11-13s Shot 7: wide from behind, Mai runs along the bank of the digital river; streams of profile cards run along the river deep into the tunnel. Cut.
13-15s Shot 8: side view, Mai runs and cries; profile cards keep streaming deep inward. Cut.
15-17s Shot 9: from behind Mai, a spider lowers on a silk thread into the space in front of her. Cut.
17-19s Shot 10: wide, Mai flinches, dodges the spider, turns back and runs toward the camera. Cut.
19-21s Shot 11: medium, a night-shadow crow chases her from behind in the air, never touching her. Cut.
21-23s Shot 12: close-up, the crow transforms into the night-shadow person and grows two wings. Cut.
23-25s Shot 13: medium, Mai runs in panic and stops in front of the large gate. Hold.

[Scene] A dark fantasy world built from the location references: a tunnel of vines and cables lined with flickering monitors, a misty teal forest with hanging vines, a river of profile cards flowing into a glowing tunnel, and a huge gate. Cool blue-teal light with a faint red accent only where Ref 6 has it.

[Visual Style] Premium stylized 3D animated feature film, matching Video 1: soft rounded volumes, matte materials, readable blue midtones, never crushed black, faint amber glow only in the creatures' eyes. Children 6-6.5 heads tall, not chibi. Faces stay clear and stable. 16:9, 24 fps.

[Camera] As in [Action]: close-up, wide, side tracking, medium. Smooth movement, no shake, no whip pans.

[Maintain Consistency] Mai's face, hair, clip and clothing identical in every shot. Creatures identical to their references. The creatures never touch her. Mai is the clear main subject in every shot.

[Avoid] Any contact with Mai, teeth, blood, gore, horror jump scare, any text, letters, numbers, code, browser bars or keypad digits, crushed black, photoreal textures on characters or locations, live-action grain, anime, flat 2D, morphing, extra fingers, sliding feet, flicker of Mai's face or body.
```

## Notes
- The assistant cannot see the plates or videos. Plate roles come from the user's stated order.
- Gate ref may still contain writing; [References] tells the model not to reproduce it.
- "flicker" appears twice by design: screens flicker (wanted), Mai's face/body must not (Avoid).
