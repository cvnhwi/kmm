# KMM — Style guide for options A / B / C (do not mix them up)

Purpose: one place that says what each style option means, which refs and prompt structure it uses, and which files/jobs belong to it. Written 2026-10-01.

Common rules for every option (project hard rules)
- No text, letters, numbers, logos or readable interface anywhere (signs, screens, cards, gates).
- Shadow creatures are dark smoke forms and never touch Mai. Wolf: no teeth, small amber eyes, semi-transparent.
- Mai never wears a hoodie; children 6-6.5 heads tall, adults 7-7.5 heads; not chibi.
- Night-shadow people are separate individuals (user rule 2026-10-01): NEVER move in sync. Each one has its own timing, speed, posture and action (one types, one tilts its head, one pauses, one turns late); turns and steps are staggered with uneven gaps; slight differences in height and hunch. Prompt wording: "each night-shadow person is a separate individual with its own timing, rhythm and gesture; no two move at the same moment or in the same way". Avoid: "synchronized movement, identical gestures, copy-pasted figures, marching in step, turning at the same time".
- Monitors flicker and glitch RANDOMLY and nonstop (user rule 2026-10-01): each screen on its own irregular rhythm, never all at once and never on a regular beat; mix of short flickers, static bursts, brief blackouts, rolling bars and image jumps of different lengths. Avoid: "all screens flashing together, regular rhythmic blinking, uniform strobe, static screens".
- Character reference sheets are design only: draw ONE figure, not the sheet layout.
- Vietnam traffic drives on the right; every motorbike rider and passenger wears a helmet.
- Defaults unless the user says otherwise: Seedance 2.5, mode `omni_reference`, draft 480p, 16:9, no audio, folder `fef878e4-1957-439e-8b50-00a4ee8454c6`, declined preset `24bae836-2c4a-48e0-89b6-49fcc0b21612`.
- The assistant cannot see images or videos: look/identity claims must be confirmed by the user.

## Option A — 2D painterly, pencil line
- Prompt structure: sections REFERENCES / STYLE / SHOTS / MAINTAIN / AVOID (plain blocks).
- Look: soft painterly feature-animation, thin loose pencil sketch lines, matte, subtle grain, not chibi.
- Video refs: `Standard.mp4` (`90542b57-617f-4273-a88b-f0a617c389c3`) primary, old school video `3ee6fe08-adc6-4715-a9ea-b441b5758864` secondary (A v2). A v1 used only `3ee6fe08…`.
- AVOID includes "flat 2D" and "photorealism".
- Files/jobs: `option_A_fantasy_chase.md` (job `4b444547-6ee7-43bf-badb-c6ac5d3ea6f9`), `option_A_v2_fantasy_chase_new_style_ref.md` (job `0e41f0f5-792b-4ccc-93c5-d1639984de8e`).

## Option B — premium stylized 3D block look
- Prompt structure: bracketed blocks [Generation Goal] [References] [Opening Composition] [Subject] [Action] [Scene] [Visual Style] [Camera] [Maintain Consistency] [Avoid], with a "STYLE REFERENCE FIRST" opening line.
- Look: "Premium stylized 3D animated feature film": soft rounded volumes, matte materials, readable blue midtones, never crushed black, faint amber glow only in creature eyes.
- Video ref: `StandardB.mp4` (`c5746038-2de6-4154-852e-6e431e457aa5`) ONLY. Option A video refs are not used in B.
- Locations are re-rendered in the stylized look, not copied photoreal.
- Files/jobs: `option_B_fantasy_chase_3d.md` (v1, `95874c0c-576e-4405-b78c-cdc0c278c17c`), `option_B_v2_fantasy_chase_3d_video_ref.md` (`8267611b-5861-4da9-bc89-4e195ac7f1cd`), `option_B_v3_fantasy_chase_new_backgrounds.md` (`e61b91a6-feba-47c8-856b-7a8382f23596`), `option_B_v4_fantasy_chase_grounded.md` (`af1740b5-6e84-41ea-8e98-063d140d9663`).
- B v4 rules (user feedback 2026-10-01): Mai never runs on the river surface (stays on the bank); at the large gate her back faces the camera; monitors glitch/flicker nonstop; characters must be integrated into the background (matching light, contact shadows, mist in front/behind), never a pasted layer.

### B camera library
For multi-angle requests (one scene, many angles) and any camera choice in B: use `CAMERA_LIBRARY_B.md` (shot sizes, angles, movements, coverage templates by scene type). Each angle = one continuous shot, same action timings, one motivated move with ease-in/out, 180-degree rule.

### B acting rules (user 2026-10-01): real, believable acting, not "AI acting"; Disney principles
The script is not copied into the prompt line by line. Before writing any B prompt, analyse each beat, then write the acting that follows from it.

**Step 1: beat analysis (done by the assistant, kept in the plan file, one row per shot)**
| Field | Question |
|---|---|
| Want / feel | What does the character want right now, what do they feel, what do they know or not know yet? |
| Trigger | What makes the feeling change (a sound, a sight, a hit)? The reaction comes AFTER the trigger, never before. |
| Energy and tempo | Panic = fast, jerky, short holds; dread = slow, held breath; exhaustion = heavy, slower than intended; relief = tension melting slowly; confidence = loose, economical. A tired child cannot sprint at full speed. |
| Body logic | Age, size and weight (child vs adult, cleaner is elderly, bus is heavy), what they hold, where they stand. |
| Transition | How the previous beat ends and this one starts (no emotional jumps without a visible moment of change). |

**Step 2: the [Acting] block in every B prompt (between [Action] and [Integration])**
Write specific, motivated acting per shot, using the Disney principles:
- Thought before action: eyes and head move first, then the body (the eyes lead every turn and reach).
- Anticipation: a small counter-move before every big action (crouch before a run, wind-up before a punch or swing, intake of breath before a scream).
- Timing and spacing: each action has its own speed from the beat analysis; slow-in/slow-out on starts and stops; vary rhythm between actions; real holds (moving holds with breathing) on emotional peaks instead of constant motion.
- Follow-through and overlapping action: hair, scarf, skirt, backpack, straps, sleeves and smoke keep moving and settle after the body stops.
- Arcs: limbs, heads and props travel in arcs, not straight robotic lines.
- Secondary action that supports the emotion: wiping tears, clutching a strap, trembling fingers, shoulders rising with breath.
- Restrained exaggeration and appeal: clear readable poses and silhouettes, stylized but believable; no gurning or over-acting.
- Solid weight: feet planted, weight shifts visibly, impacts have recoil and recovery.
- Faces: emotion changes through stages (surprise -> fear -> panic), asymmetry, micro-expressions, natural blinks (more when anxious, frozen stare when terrified), breath visible in chest and shoulders; tears well up before they fall.
- Reaction timing: listeners react a beat after the event; groups never react in sync.

**Step 3: [Avoid] additions for acting**
mannequin stillness, mechanical or uniform motion speed, robotic straight-line moves, actions with no anticipation, reacting before the trigger, emotion switching instantly with no transition, frozen symmetrical faces, dead eyes, constant open-mouth expression, over-acting or gurning, floaty weightless motion, everyone moving at the same speed.

## Option C — hybrid 3D/2D hand-painted (mix of B structure + new art style)
- Prompt structure: same bracketed blocks as B; only the art-style block ([Visual Style]) and the style-related lines in [References] / [Avoid] change.
- Art style text (verbatim from the user, 2026-10-01; "@Image 1" is the painted style reference image the user supplies):

```
STYLE

Stylized hybrid 3D/2D animation with a hand-painted finish from @Image 1: watercolor washes, gouache

dry-brush, soft cel-shade edges, sparse sepia-charcoal line work, never pure black; paper grain low

and even over the paint but never on facial skin; colored-pencil hatching only on cloth, hair, bark,

concrete and background, never on skin of face, neck, arms or hands; skin clean and uniform with no

marks, lines, dots or freckles. Backgrounds flatter than the character. Palette black-teal, indigo

and cold blue; her red neckerchief and light-blue backpack are the only warm-ish notes. Line weight

stays stable — no line boil, no shimmer, no strobe.
```

- Differences from B: painted finish (watercolor/gouache/dry-brush, cel-shade edges, sepia-charcoal lines) instead of clean 3D materials; backgrounds flatter than the character; palette limited to black-teal / indigo / cold blue with only the red neckerchief and light-blue backpack warm; skin always clean (no hatching, marks or freckles).
- Do NOT put "flat 2D" or "painterly is forbidden" in C's AVOID (that is A/B wording). Keep "photorealism", "anime", "pure black", "line boil/shimmer/strobe".
- Video ref: none in the first C run (StandardB is B's 3D look and could pull C toward B).
- Files/jobs: `option_C_fantasy_chase_hand_painted.md` (job `0a5cf4c2-6ef7-4998-a156-07b33d652d26`, no video ref, Ref 1 = `01_Mai` assumed to carry the painted style).

## Quick check before any new generation
1. Which option (A/B/C)? 2. Which video refs belong to it (table above)? 3. Which plates and are they text-free? 4. Prompt block structure matches the option. 5. Run `get_cost`, then wait for the user's "gen".


## Option D — B look, refined and less AI-looking (redefined 2026-10-01)
- NOT stop-motion. Same as option B (StandardB video ref, B bracketed blocks, all B v4 rules) plus a "D layer": per-shot lenses and foreground depth, a [Performance] block (weight, anticipation, overlap, asymmetry, blinks), hand-finished material detail, motivated light with falloff, restrained grade, fine grain, and an "AI look" list in [Avoid].
- Shot detail: B v5 split clips.
- Files/jobs: `option_D_B_refined_less_AI.md` (clip 1 `7256d91f-0422-48fe-82c7-9dff7ffb149b`, clip 4 `f9f093b7-28ce-48e3-8465-9c3687f2ba81`).
- The stop-motion experiment is D0, discarded: `option_D0_stop_motion_DISCARDED.md`.

## Shared props
- Bus driver = `15_TaiXe` `6f2ff8e2-08c5-47ad-9b71-25fa28d62738` (never the security guard).
- Green bus (all bus shots): ref `e077bd7c-d7dd-4e99-84d8-fe676d544e86` (`MVKMM_XE BUS_v001_0928.png`), green two-tone minibus; destination panel blank, no text/number/plate; do not copy the sketch lines.
- Mai's phone (all options, every shot with her phone): ref `66324bdf-1d17-4e3c-b10e-545427e88712` (`KMM_PHONE_0930_v001.png`). Light sky-blue rounded case, black bezel, yellow side buttons, dual camera top-left on the back, cat + dog sticker on the back, plain black front screen. The sheet has the labels FRONT / BEHIND / SIDE: prompt must say "design only, draw ONE phone, do not copy the labels or the sheet layout". On-screen content still follows the no-text rule (icons/photos only).
