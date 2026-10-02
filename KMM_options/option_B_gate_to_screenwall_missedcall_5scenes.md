# KMM — Option B: Gate slam → inside rest → screen wall → hide → missed call (5 scenes, 2 × 10 s)

User request (2026-10-02):
1. Cổng Fantasy | OTS | Mai chạy thẳng vào trong cánh cổng, cánh cổng bất ngờ đóng sập lại
2. Bên trong tòa nhà | trung cảnh | Mai mệt tựa vào tường đóng ngồi xuống thở dốc, giật mình, camera zoom vào mặt, hốt hoảng
3. Tường màn hình | toàn cảnh | phía sau lưng nhiều nhân vật bóng đêm đang làm việc
4. Tường màn hình | trung cảnh | Mai hốt hoảng trốn vào góc, lấy điện thoại ra nhìn
5. Tường màn hình | POV | điện thoại có missed call của "Mẹ"

Settings: Seedance 2.5 omni_reference, draft 480p, 16:9, no audio, folder MV KMM, declined preset. 2 × 10 s ≈ 60 credits.

## Defaults and flags
- "Cổng Fantasy" (outside): the outside fantasy-gate plate is still missing, so the dark gate B18 `7c1e33a4` is used. Swap it if there is a proper outside-gate plate.
- "Bên trong tòa nhà": the B15 hall `e2fab0e1`, against the inner side of the same closed doors (south wall). B17_Hanhlang `409ef811` could be the intended interior instead; its role is still unconfirmed.
- "Thở dốc" is written as "catching her breath, chest rising and falling", to avoid moderation flags.
- Scene 5 "Mẹ": the no-text rule wins. The phone shows Mom's avatar (Mom fantasy `a6286ab4`), a red missed-call icon and badge, and an EMPTY name bar for adding "Mẹ" in post. AI text renders unreliably.
- The split is 2 clips. Scenes 1-2 change location with a hard cut.

## Clip A (scenes 1-2), 10 s
| Time | Shot | Action |
|---|---|---|
| 0-4 s | OTS tracking 35 mm | Mai runs into the gate; the camera stops at the threshold; the doors SLAM shut in front of the lens; dust; dark |
| 4-10 s | MS 50 mm inside | Mai leans on the closed doors, slides down to sit, catches her breath; startled jolt; fast smooth push-in to a CU of her alarmed face |

Refs: Mai `0d56fcb2`, B18 `7c1e33a4`, B15 `e2fab0e1`, master `24430dd0`.
Status: COMPLETED 2026-10-02 (rendered 16:43 UTC). Job `6b29a328-e3ab-49cc-bf62-bdb11bcc174a`. Content not yet reviewed.

## Clip B (scenes 3-5), 10 s
| Time | Shot | Action |
|---|---|---|
| 0-3.5 s | wide 24 mm from behind the workers | 20-30 backs facing the monitor wall, each with a different task; nobody turns |
| 3.5-7.5 s | MS 35 mm | Mai hurries into a shadowy corner, takes out the phone and holds it vertically; glow on her face |
| 7.5-10 s | POV phone | Mom's avatar, red missed-call icon and badge, blank name bar; slight hand tremble |

Refs: B15 `e2fab0e1`, Mai `0d56fcb2`, phone `b7eeb576`, Mom fantasy `a6286ab4`, 5 villains shuffled, master `24430dd0`.
Status: COMPLETED 2026-10-02 (rendered 16:43 UTC). Job `83590c37-681e-42af-88c2-d7cf5c7064bb`. Content not yet reviewed.

## Clip C — scenes 2-5 in ONE 15 s clip (user resent scenes 2-5 without scene 1)
Interpretation (flagged): the user wants scenes 2-5 as one continuous clip inside the building, without the gate exterior. Everything is in B15. The doors are on the back wall and the workers face the far monitor wall with their backs to the doors. Mai hides in the corner beside the doors.

| Time | Scene | Shot | Action |
|---|---|---|---|
| 0-3 s | 2 | MS 50 mm static | leans on the closed doors, slides down to sit, catches her breath |
| 3-5 s | 2 | same angle → push-in | off-screen sound, she jolts; smooth fast push-in to a CU of her alarmed face |
| 5-8.5 s | 3 | wide 24 mm from behind the workers | 20-30 backs, each with a different task; nobody turns |
| 8.5-12 s | 4 | MS 35 mm | scrambles up, hurries along the back wall into the corner, takes out the phone and holds it vertically |
| 12-15 s | 5 | POV phone | Mom's avatar, red missed-call icon and badge, blank name bar (add "Mẹ" in post) |

Refs: B15 `e2fab0e1`, Mai `0d56fcb2`, phone `b7eeb576`, Mom fantasy `a6286ab4`, 5 villains shuffled, master `24430dd0`.
Status: COMPLETED 2026-10-02 (rendered 16:49 UTC). Job `b8f392ff-4fe0-4116-80b0-1eae02808ae4`. 15 s. Content not yet reviewed.
