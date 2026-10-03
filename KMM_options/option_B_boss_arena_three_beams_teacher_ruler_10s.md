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

Status: COMPLETED — job `bbe498f6-edd2-406d-b452-1305494f460f`

## v4: v3 with BLUE-WHITE bolts (user request 2026-10-03), 7 s, 4 shots
Identical to v3 (short gunshot-style bolts, 3 villains then the Teacher, oblique camera, Teacher with NO glasses carried over, no pupils, SFX only) except:
- Bolt colour: bright white core with an electric sky-blue glow (was white-gold); the impact flash is blue-white too.
- Avoid adds "gold or yellow bolts"; still no purple or violet (blue must not drift to violet).

Status: SUBMITTED — job `6ff1433d-2b8c-4d9f-a9dd-6d28c2dd38db`

## v5: wooden ruler + the Teacher relocates before every shot (user request 2026-10-03), 8 s, 6 shots
User sent a photo of a plain wooden school ruler (the photo carries a brand name; it was NOT attached, to avoid brand text leaking into the video) and asked: the Teacher's tool is this wooden ruler, and after each firing she must change position.
Changes vs v4:
- New [Teacher's Ruler] block: plain flat light natural-wood ruler ~30 cm, fine black tick marks and small numbers, unbranded, held like a wand, does not change shape. Avoid: metal wand, staff, sword, brand names or logos or readable text on the ruler.
- The Teacher part is now 3 hard cuts (3.9-5.3 s, 5.3-6.7 s, 6.7-8 s), each from a NEW position, stance and camera angle (A standing, B side-stepped with a bent knee, C crouched or leaning). She never fires twice from the same spot or pose.
- Three villain hits compressed to ~1.3 s each. Bolts remain short blue-white gunshot pulses; Teacher with NO glasses; oblique camera; no pupils; no purple; SFX only.
- If the ruler looks wrong, upload the ruler photo (cropped, no brand) as an asset and I will attach it.

Folder: MV KMM `11749213-086c-4a29-a963-b5a064eb4af7` (as always).
Status: SUBMITTED — job `86a2aa9d-4e4c-4a6d-8f74-c1d63021cc16`
