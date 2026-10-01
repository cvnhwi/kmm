# KMM — Option B: Fantasy chase (premium stylized 3D block look)

Status: generated as draft. Job `95874c0c-576e-4405-b78c-cdc0c278c17c` (created 2026-09-30 ~15:21 UTC).
Content not yet reviewed by the assistant (cannot view video).

Same script, refs and settings as option A, except:
- prompt is written in the multi-block structure ([Generation Goal] ... [Avoid]) with a "premium stylized 3D animated feature film" look;
- NO video style reference (option A used `3ee6fe08-adc6-4715-a9ea-b441b5758864`);
- audio off in both.

## Settings
| Key | Value |
|---|---|
| model | `seedance_2_5` |
| mode | `omni_reference` |
| draft | true (480p) |
| duration | 25 s |
| aspect_ratio | 16:9 |
| generate_audio | false |
| folder_id | `fef878e4-1957-439e-8b50-00a4ee8454c6` |
| declined_preset_id | `24bae836-2c4a-48e0-89b6-49fcc0b21612` |
| cost | 75 credits (get_cost) |

## References (Ref N order)
1 Mai `b42c82ad-d58e-4fb3-bcf3-4d89dac09517` · 2 wolf `f48ff106-d9d6-4233-a770-d36f768a1f64` · 3 crow `6a271d30-4602-4348-8042-8728526956c5` · 4 spider `cdcbdc48-05d0-4875-b2c4-eb77a56cb96b` · 5 night-shadow person `2f07fe73-628d-4761-aeff-0b32446d8a0c` · 6 entrance `245f07de-6ccc-4a7c-b49d-3247f32aecb6` · 7 forest `a7a8f636-a610-4b1d-b408-639525c4d8a0` · 8 river `3d129dd5-55a6-46f3-b9a7-80f8e299bf27` · 9 gate `607ae6ae-2bf6-4148-852e-aae51d9de070`

## Prompt
```
[Generation Goal] A frightened student runs through a dark fantasy world, chased by night-shadow creatures, in one 25-second sequence of 13 shots with hard cuts. 16:9. The creatures never touch her.

[References]
Ref 1 is Mai's identity, costume and the film's ART STYLE: use her face, hair, hair clip and clothing, and match its render style and materials exactly. It is a character reference sheet: use it only for design, draw ONE figure, not the sheet layout. Do not use its white studio background.
Ref 2 is the wolf design: dark smoke silhouette, soft wispy edges, small glowing amber eyes, no teeth, semi-transparent. Ref 3 is the crow. Ref 4 is the spider. Ref 5 is the night-shadow person: tall thin hunched black silhouette, long arms, pointed head, two glowing eyes; draw without its white background. Each is design only, ONE figure.
Refs 6-9 are the locations: Ref 6 fantasy entrance (shots 2-5), Ref 7 fantasy forest (shots 6, 11, 12, 13), Ref 8 digital river (shots 7-10), Ref 9 large gate (shot 13). Use their layout and mood exactly. Do not reproduce any writing or interface text that appears in them; leave those surfaces blank.

[Opening Composition] Shot 1 opens in pitch-black darkness on a close-up of the wolf's face. Shot 2 is a wide view from behind Mai entering the fantasy entrance.

[Subject] Mai, age 11, running in panic and crying, chased by a smoke wolf, a night-shadow crow and a night-shadow person. One physical student only; the creatures are dark smoke forms that never make contact. She never wears a hoodie.

[Action]
0-1s Shot 1: wolf close-up, crouches and lunges toward the camera. Cut.
1-3s Shot 2: wide, from behind, Mai runs deep into the fantasy entrance. Cut.
3-4s Shot 3: side view tracking Mai from waist to head, running, tearful, lips trembling. Cut.
4-5s Shot 4: side view tracking the wolf, it bursts into frame after her, well behind. Cut.
5-8s Shot 5: side view tracking the wolf, it keeps chasing, smoke trailing, never touching her. Cut.
8-11s Shot 6: wide, Mai runs out of the entrance into the forest. Cut.
11-13s Shot 7: wide from behind, Mai runs along the bank of the digital river. Cut.
13-15s Shot 8: side view, Mai runs and cries. Cut.
15-17s Shot 9: from behind Mai, a spider lowers on a silk thread into the space in front of her. Cut.
17-19s Shot 10: wide, Mai flinches, dodges the spider, turns back and runs toward the camera. Cut.
19-21s Shot 11: medium, a night-shadow crow chases her from behind in the air, never touching her. Cut.
21-23s Shot 12: close-up, the crow transforms into the night-shadow person and grows two wings. Cut.
23-25s Shot 13: medium, Mai runs in panic and stops in front of the large gate. Hold.

[Scene] A dark fantasy world built from the location references: a cable-tangled cavern entrance, a forest with a cable tunnel, a river of glowing profile-photo cards, and a huge gate. Cool blue-violet light.

[Visual Style] Premium stylized 3D animated feature film, exactly matching the art style of Ref 1: soft rounded volumes, matte materials, readable blue midtones, never crushed black, faint amber glow only in the creatures' eyes. Children 6-6.5 heads tall, not chibi. Faces stay clear and stable. 16:9, 24 fps.

[Camera] As in [Action]: close-up, wide, side tracking, medium. Smooth movement, no shake, no whip pans.

[Maintain Consistency] Mai's face, hair, clip and clothing identical in every shot. Creatures identical to their references. The creatures never touch her. Mai is the clear main subject in every shot.

[Avoid] Any contact with Mai, teeth, blood, gore, horror jump scare, any text, letters, numbers, code, browser bars or keypad digits, crushed black, photorealism, live-action grain, anime, flat 2D, morphing, extra fingers, sliding feet, flicker.
```

## Notes
- The user's template example was a different scene (bedroom, wall shadow, 5 s); only its structure and look were used here. Not confirmed by the user.
- The 3D look depends on Ref 1 (01_Mai) being a 3D-block render; the assistant cannot view the image to confirm.
