# KMM — Option B v2: Fantasy chase (3D block look) with a video look ref

Status: generated as draft. Job `8267611b-5861-4da9-bc89-4e195ac7f1cd` (created 2026-09-30 ~15:39 UTC).
Content not yet reviewed by the assistant (cannot view video).
v1 is `option_B_fantasy_chase_3d.md` (job `95874c0c-576e-4405-b78c-cdc0c278c17c`).

## Difference from v1
- Added video look ref `StandardB.mp4`, media_id `c5746038-2de6-4154-852e-6e431e457aa5`, as Video 1.
- Prompt opens with a line naming Video 1; [References] says: follow Video 1 for overall look, Ref 1 (01_Mai) for Mai's identity; [Visual Style] says "matching Video 1" instead of "matching Ref 1".
- The video refs used in option A (`90542b57…`, `3ee6fe08…`) are NOT used in B.
- Everything else (13 shots, image refs, settings) is identical to v1.

## Settings
model `seedance_2_5`, mode `omni_reference`, draft true, 480p, 25 s, 16:9, generate_audio false, folder `fef878e4-1957-439e-8b50-00a4ee8454c6`, declined_preset_id `24bae836-2c4a-48e0-89b6-49fcc0b21612`. Cost 75 credits (get_cost).

## Reference order
Video 1 `c5746038-2de6-4154-852e-6e431e457aa5`
Refs 1-9 as in B v1: Mai `b42c82ad…`, wolf `f48ff106…`, crow `6a271d30…`, spider `cdcbdc48…`, shadow person `2f07fe73…`, entrance `245f07de…`, forest `a7a8f636…`, river `3d129dd5…`, gate `607ae6ae…`.

## Prompt changes (shot list unchanged, see B v1)
Opening line:
```
STYLE REFERENCE FIRST: Video 1 is the look reference for this whole sequence. Match its render look, materials and motion quality on every frame.
```
[References], video part:
```
Video 1 (look reference, highest priority for overall look): reproduce its render style, surface treatment, colour handling and animation feel on Mai, the creatures and the locations. Do not copy its lighting, setting or story content; this sequence is dark night with cool blue-violet fantasy lighting from the location references. Where Video 1 and Ref 1 differ in look, follow Video 1 for the overall look and Ref 1 for Mai's identity.
```
[References], Ref 1: "Ref 1 is Mai's identity, costume and character design ..." (no longer "the film's ART STYLE").
[Visual Style]: "Premium stylized 3D animated feature film, matching Video 1: ..."

## Notes
- The assistant cannot see StandardB, so it does not know whether it is really a 3D block look.
- Gate ref `607ae6ae…` may still contain writing; [Avoid] tells the model not to reproduce it.
