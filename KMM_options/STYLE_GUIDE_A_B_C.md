# KMM — Style guide for options A / B / C (do not mix them up)

Purpose: one place that says what each style option means, which refs and prompt structure it uses, and which files/jobs belong to it. Written 2026-10-01.

Common rules for every option (project hard rules)
- No text, letters, numbers, logos or readable interface anywhere (signs, screens, cards, gates).
- Shadow creatures are dark smoke forms and never touch Mai. Wolf: no teeth, small amber eyes, semi-transparent.
- Mai never wears a hoodie; children 6-6.5 heads tall, adults 7-7.5 heads; not chibi.
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
- Files/jobs: `option_B_fantasy_chase_3d.md` (v1, `95874c0c-576e-4405-b78c-cdc0c278c17c`), `option_B_v2_fantasy_chase_3d_video_ref.md` (`8267611b-5861-4da9-bc89-4e195ac7f1cd`), `option_B_v3_fantasy_chase_new_backgrounds.md` (`e61b91a6-feba-47c8-856b-7a8382f23596`).

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
- Video ref: to be decided with the user (StandardB is B's 3D look and may pull C toward B).
- Files/jobs: see `option_C_*.md` when created.

## Quick check before any new generation
1. Which option (A/B/C)? 2. Which video refs belong to it (table above)? 3. Which plates and are they text-free? 4. Prompt block structure matches the option. 5. Run `get_cost`, then wait for the user's "gen".
