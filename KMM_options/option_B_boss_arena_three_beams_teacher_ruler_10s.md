# KMM — Option B: BOSS arena — 3 villains hit by 3 beams, cut to the Teacher firing from her ruler (10 s, 5 shots)

User request (2026-10-03): 3 villains shot in turn by 3 beams of light, then cut to the Teacher standing and firing light beams from her ruler, in the BOSS arena, NOT a frontal view of the background.

Defaults (flagged):
- 10 s: shots 1-3 are one hit each (~2 s), shots 4-5 are the Teacher (~4 s).
- Camera is always oblique, low or side, never frontal to the plate.
- Beams are white-gold; hit villains are blasted back and burst into soft dark particles (flat shadows, no injury, no fire).
- The beams come from off-screen left, then the reveal shows the Teacher firing.
- Teacher's ruler is described as a long slim ruler held like a wand; confirm it matches her design.
- The 3 targets are three different designs; all 5 attached (rule 5c); no pupils, no purple; SFX only.

Refs: arena `c8394b3d`, Teacher `89b32a5e`, villains 1-5, master `24430dd0`.

Status: COMPLETED — job `e88d809e-80cc-48a7-a557-ebf7618a7518`

## v2: Teacher WITHOUT glasses (user request 2026-10-03)
Same 5-shot script. Changes:
- "NO GLASSES" in [References], [Character Look] and [Avoid] (glasses, spectacles, eyewear, lenses, frames).
- The shot 5 line about light reflecting on her glasses becomes light on her bare face and eyes.
- Flag: the Teacher reference `89b32a5e` may itself show glasses, so the prompt asks for "as Image 2 EXCEPT no glasses". If glasses still appear, the reference image needs a no-glasses version.

Status: COMPLETED — job `2d8176c7-8e0d-43fe-9f26-651aab7f6ca1`

## v3: short and snappy, gunshot-style bolts (user request 2026-10-03), 7 s, 4 shots
User: 3 villains hit in turn by 3 magic bolts ("không quá dài"), then the Teacher firing from her ruler; fired in bursts like a gun, NOT held for long.
Changes:
- 7 s, 4 hard cuts: three ~1.5 s hit shots, then one 2.5 s Teacher shot with 3 separate shots and beats of stillness between.
- New [Magic Bolt Style] block: a short fast pulse (~4-6 frames), never a sustained beam, a gap of darkness between bolts, a flash on impact.
- Avoid: long, sustained or continuous beams.
- Teacher still has NO glasses (carried over from v2; flagged: say if glasses should return).
- Same arena, oblique angles, 3 different targets, all 5 designs attached, no pupils, no purple, SFX only.

Status: SUBMITTED — job `bbe498f6-edd2-406d-b452-1305494f460f`
