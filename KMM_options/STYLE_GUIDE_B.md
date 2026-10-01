# KMM — Style guide (option B only)

Purpose: the single production style for KMM is option B (premium stylized 3D). Options A, C and D were removed on 2026-10-01 at the user's request (still in git history).

Common rules for every option (project hard rules)
- No text, letters, numbers, logos or readable interface anywhere (signs, screens, cards, gates).
- Shadow creatures are dark smoke forms and never touch Mai. Wolf: no teeth, small amber eyes, semi-transparent.
- Mai never wears a hoodie; children 6-6.5 heads tall, adults 7-7.5 heads; not chibi.
- Night-shadow people are separate individuals (user rule 2026-10-01): NEVER move in sync. Each one has its own timing, speed, posture and action (one types, one tilts its head, one pauses, one turns late); turns and steps are staggered with uneven gaps; slight differences in height and hunch. Prompt wording: "each night-shadow person is a separate individual with its own timing, rhythm and gesture; no two move at the same moment or in the same way". Avoid: "synchronized movement, identical gestures, copy-pasted figures, marching in step, turning at the same time".
- ALL crowds and groups (user rule 2026-10-01), not only shadow people: students, parents at the school gate, pedestrians, motorbike riders, vendors, the hero team, any background extras. Nobody moves at the same moment or in the same way; every person is an individual with their own action, intention, speed and rhythm.
  - Give each visible person (or small cluster) a different, believable activity that fits the place and moment: e.g. at a school gate one chats, one checks a phone, one adjusts a backpack, one waves, one waits looking around, a parent crouches to fix a child's collar; on the street one rider waits at the light, one turns, a vendor arranges goods.
  - Stagger starts, stops and reactions with uneven gaps; reactions ripple through the group (nearest first, farthest last), never all at once.
  - Vary pace, posture, age-appropriate body language, height and build; small idle motions (weight shifts, glances, scratching, breathing) instead of frozen extras.
  - Groups that move together (a team walking, a crowd fleeing) still have different gaits, step timing and spacing; no marching in step, no mirrored poses.
  - Prompt wording: "every person in the crowd is a separate individual with their own believable action, speed and rhythm; no two people move at the same moment or in the same way; reactions spread through the group with uneven delays".
  - Avoid: "synchronized crowd, identical poses, copy-pasted extras, everyone turning or reacting at once, marching in step, frozen background people, looping identical walk cycles".
- Real-time motion at 24 fps, ALWAYS (user rule 2026-10-01): every action plays at natural real-time speed; no slow motion, no speed ramps, no time-stretch, no freeze-frames, no fast-forward. Animation timing is 24 fps feature-film timing (fast actions are fast, heavy things have weight, holds are acting holds, not slowed footage). Prompt wording: "real-time speed, natural 24 fps animation timing, no slow motion, no speed ramp". Avoid: "slow motion, slow-mo, speed ramp, time remapping, bullet time, freeze frame, dreamy floaty slowed movement". Generation param: Higgsfield jobs always show `speedramp: "auto"`; Seedance 2.5 does not expose speedramp as a parameter (checked 2026-10-01, `speedramp: "off"` is ignored), so the no-slow-motion rule is enforced in the prompt only.
- Monitors flicker and glitch RANDOMLY and nonstop (user rule 2026-10-01): each screen on its own irregular rhythm, never all at once and never on a regular beat; mix of short flickers, static bursts, brief blackouts, rolling bars and image jumps of different lengths. Avoid: "all screens flashing together, regular rhythmic blinking, uniform strobe, static screens".
- Character reference sheets are design only: draw ONE figure, not the sheet layout.
- Vietnam traffic drives on the right; every motorbike rider and passenger wears a helmet.
- ALL generations go into the Higgsfield project/folder "MV KMM" (user rule 2026-10-01): pass `folder_id: fef878e4-1957-439e-8b50-00a4ee8454c6` on EVERY generate call (video, image, finalize to 1080p), and verify with `list_project_assets` after submitting. Never omit folder_id, never use another "MV KMM"-like project (e.g. `e46399a5…` in another workspace, `MV_KMM_S26-31`, `VANH_MV KMM`).
- FANTASY STYLE MASTER VIDEO (user rule 2026-10-01): every FANTASY scene (fantasy gate/cave entrance, screen-wall hall, BOSS arena, chase inside the fantasy world, hero fight) ALWAYS attaches the fantasy master video as a video reference, and the prompt ALWAYS opens with this line (first line, before everything else):
  "FANTASY MASTER REFERENCE FIRST: Video 1 is the master reference for the style, mood and characters of this whole clip. Match its render look, materials, colour palette, lighting mood, atmosphere, character design, proportions and animation feel on every frame; do not copy its exact shots, camera or story."
  - Source: user's Higgsfield link `.../@xelfaistudiovn/mv-kmm/folders/84e36f63-59b2-4680-918d-51c7809e79d2?preview=31d4ddc0-d66c-4da7-9ac1-c055cd20d7cf` (workspace xelfaistudiovn, not accessible from this account: 403). Media ID in this workspace: PENDING, the user must upload the video so it gets an ID here.
  - It replaces StandardB `c5746038…` as Video 1 in fantasy scenes. Non-fantasy scenes (alley, street, school, bus outside) keep StandardB unless the user says otherwise.
  - Character sheets stay attached for identity and costume details; the master video wins on look, mood and proportions.
- Defaults unless the user says otherwise: Seedance 2.5, mode `omni_reference`, draft 480p, 16:9, no audio, folder `fef878e4-1957-439e-8b50-00a4ee8454c6`, declined preset `24bae836-2c4a-48e0-89b6-49fcc0b21612`.
- The assistant cannot see images or videos: look/identity claims must be confirmed by the user.

## Option B — premium stylized 3D block look
- Prompt structure: bracketed blocks [Generation Goal] [References] [Opening Composition] [Subject] [Action] [Scene] [Visual Style] [Camera] [Maintain Consistency] [Avoid], with a "STYLE REFERENCE FIRST" opening line.
- Look: "Premium stylized 3D animated feature film": soft rounded volumes, matte materials, readable blue midtones, never crushed black, faint amber glow only in creature eyes.
- Video ref: `StandardB.mp4` (`c5746038-2de6-4154-852e-6e431e457aa5`) ONLY.
- Locations are re-rendered in the stylized look, not copied photoreal.
- Files/jobs: `option_B_fantasy_chase_3d.md` (v1, `95874c0c-576e-4405-b78c-cdc0c278c17c`), `option_B_v2_fantasy_chase_3d_video_ref.md` (`8267611b-5861-4da9-bc89-4e195ac7f1cd`), `option_B_v3_fantasy_chase_new_backgrounds.md` (`e61b91a6-feba-47c8-856b-7a8382f23596`), `option_B_v4_fantasy_chase_grounded.md` (`af1740b5-6e84-41ea-8e98-063d140d9663`).
- B v4 rules (user feedback 2026-10-01): Mai never runs on the river surface (stays on the bank); at the large gate her back faces the camera; monitors glitch/flicker nonstop; characters must be integrated into the background (matching light, contact shadows, mist in front/behind), never a pasted layer.

### B lighting look (user 2026-10-01): cinematic, not too clean
Every B prompt gets a [Lighting] block (after [Integration]) and these words in [Visual Style]. Light is always motivated by a source in the scene (monitors, amber eyes, bus headlights, golden magic, far glow, doorway).
- Rim light / edge light: a thin bright edge on hair, shoulders, scarf and silhouettes from a back source (screens behind, far glow, headlights) to separate characters from the dark background.
- Key + fill with contrast: one clear key direction per scene (from the scene map), soft low fill; faces readable, never flat or evenly lit.
- Bounce and colour spill: coloured light reflected onto skin and clothes from nearby sources (cyan screen spill on cheeks, warm gold from magic or headlights, amber glint from creature eyes); light wraps around rounded forms.
- Eye light: a small catchlight in the eyes so they stay alive.
- Practical glows and atmosphere: volumetric haze and light shafts through mist and smoke, soft glow/halation around bright sources, dust specks catching light.
- Not too clean: subtle surface texture and wear, gentle contact shadows and ambient occlusion in folds and corners, soft vignetting, fine even film grain, slight lens bloom on highlights; no sterile plastic CG.
- Shadows stay readable (never crushed black), with coloured shadow tones (deep teal/indigo), not grey.
Prompt wording: "[Lighting] Motivated cinematic lighting: <key source and direction>; strong rim light from <back source> outlining hair, shoulders and scarf; coloured bounce and spill from <sources> onto skin and clothes; small catchlights in the eyes; volumetric haze and light shafts through the mist; soft halation around bright sources; dust catching the light; rich but readable shadows with teal-indigo tones."
[Avoid] adds: flat even lighting, no rim light, sterile overly clean CG, plastic sheen, grey lifeless shadows, characters not lit by the scene's light sources.

### B camera library
User preference (2026-10-01): CUT COVERAGE is the default. Each clip is built from several shots joined by hard cuts (like V1 `e398982e…` / V1L `e08e2a51…`), each shot with its own size, angle and one motivated move. Use a single continuous take only when the user asks for it.
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

## Quick check before any new generation
1. Option B. 2. Video ref StandardB only. 3. Which plates and are they text-free? 4. Prompt block structure matches the option. 5. Run `get_cost`, then wait for the user's "gen".


## Shared props
- SCREEN-WALL hall plate (Tường Màn Hình, every screen-wall scene from 2026-10-01): `B15_TuongManHinh.png` `54a5db90-fc99-4c03-85bf-d492baad4e2c` (user update 2026-10-01, second upload). It replaces the old hall plates `b59fa3e7-7919-4b03-8cac-61d8e0afc0b1`, `b5785b69-f416-477c-8474-af8f9eb86d03` and the interim `b331cb43-0b97-40b5-a323-135c77c0082a`; never use the old ones again. Content not seen by the assistant: describe it only as "layout, mood and lighting from the screen-wall hall ref, rendered in the stylized look of Video 1, matte dark floor, no grid; monitors mostly dark, some lit, flickering randomly" until the user confirms details.
- BOSS arena plate (every Boss scene from 2026-10-01): `B14_Boss.png` `1c507ac3-2db9-4d1e-b5e0-53fe183687e5` (user update 2026-10-01, second upload). It replaces the old plates `f1ae9d0a-c22c-4de8-92f0-a051fb01937c` and `076ec352-e524-4304-a1eb-821d9d9278d1`; never use the old ones again. Content of the new image not seen by the assistant: describe it in prompts only as "layout, mood and lighting from the BOSS arena ref, rendered in the stylized look of Video 1, matte dark floor, no grid" until the user confirms the details.
- Bus driver = `15_TaiXe` `6f2ff8e2-08c5-47ad-9b71-25fa28d62738` (never the security guard).
- Green bus (all bus shots): ref `e077bd7c-d7dd-4e99-84d8-fe676d544e86` (`MVKMM_XE BUS_v001_0928.png`), green two-tone minibus; destination panel blank, no text/number/plate; do not copy the sketch lines.
- Mai's phone (every shot with her phone): ref `66324bdf-1d17-4e3c-b10e-545427e88712` (`KMM_PHONE_0930_v001.png`). Light sky-blue rounded case, black bezel, yellow side buttons, dual camera top-left on the back, cat + dog sticker on the back, plain black front screen. The sheet has the labels FRONT / BEHIND / SIDE: prompt must say "design only, draw ONE phone, do not copy the labels or the sheet layout". On-screen content still follows the no-text rule (icons/photos only).
