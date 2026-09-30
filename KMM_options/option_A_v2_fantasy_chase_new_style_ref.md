# KMM — Option A v2: Fantasy chase with an additional style video ref

Status: generated as draft. Job `0e41f0f5-792b-4ccc-93c5-d1639984de8e` (created 2026-09-30 ~15:37 UTC).
Content not yet reviewed by the assistant (cannot view video).
Supersedes nothing: v1 is `option_A_fantasy_chase.md` (job `4b444547-6ee7-43bf-badb-c6ac5d3ea6f9`).

## Difference from v1
- New video style ref added as Video 1 (PRIMARY): media_id `90542b57-617f-4273-a88b-f0a617c389c3` (file `Standard.mp4`).
- The previous video ref `3ee6fe08-adc6-4715-a9ea-b441b5758864` becomes Video 2 (secondary). Not confirmed by the user whether it should stay; kept because the user earlier asked to always use it as a look reference.
- The prompt now opens with a line naming the style refs, and the REFERENCES / STYLE blocks say "follow Video 1 where they differ".
- Everything else (13 shots, image refs, settings) is identical to v1.

## Settings
model `seedance_2_5`, mode `omni_reference`, draft true, 480p, 25 s, 16:9, generate_audio false, folder `fef878e4-1957-439e-8b50-00a4ee8454c6`, declined_preset_id `24bae836-2c4a-48e0-89b6-49fcc0b21612`. Cost 75 credits (get_cost).

## Reference order
Video 1 `90542b57-617f-4273-a88b-f0a617c389c3` · Video 2 `3ee6fe08-adc6-4715-a9ea-b441b5758864`
Images 1-9 as in v1: Mai `b42c82ad…`, wolf `f48ff106…`, crow `6a271d30…`, spider `cdcbdc48…`, shadow person `2f07fe73…`, entrance `245f07de…`, forest `a7a8f636…`, river `3d129dd5…`, gate `607ae6ae…`.

## Prompt changes (full shot list unchanged, see v1)
Opening line added:
```
STYLE REFERENCE FIRST: Video 1 is the primary style reference for this whole sequence, and Video 2 is a secondary style reference. Match their look on every frame.
```
REFERENCES block, video part:
```
Video 1 (PRIMARY style reference, highest priority): reproduce its soft painterly feature-animation look, thin loose pencil sketch lines, colour treatment, surface texture and gentle weighted motion on every element: Mai, the creatures, the locations. Do not copy its lighting, setting or story content; this sequence is dark night with cool blue fantasy lighting taken from the location references.
Video 2 (secondary style reference): same look, same rules. Where Video 1 and Video 2 differ, follow Video 1.
```
STYLE block first sentence: "EXACTLY the same art style as Video 1 (then Video 2) and the character references: ..."

## Notes
- The assistant cannot see either video, so it does not know how their looks differ.
- Gate ref `607ae6ae…` may still contain writing; the AVOID block tells the model not to reproduce it.
