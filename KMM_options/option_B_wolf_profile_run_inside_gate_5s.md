# KMM — Option B: night-shadow wolf runs FAST, side-profile close-up, INSIDE the fantasy gate (5 s, one take)

User request (2026-10-04) with a frame from the draft (s4.S62-63, timecode burnt in): "tạo cảnh sói chạy góc như thế này (lấy đúng bố cục), bối cảnh trong đúng phía trong cổng fantasy. Chỉ mình sói bóng đêm (không con ngươi). chạy tốc độ nhanh". All generations go to MV KMM › FANTASY 2.

Composition locked to the frame: close-up, eye level, long lens; wolf in strict side profile facing RIGHT; black head/neck/shoulder fill the left two-thirds; tall pointed ear near top-centre; long narrow muzzle pointing right, tip at about 3/4 width, lower-middle; one narrow glowing yellow almond eye at frame centre (no pupil); background = blurred teal tunnel with glowing white/teal floating monitors (bokeh).
Action: ONE fast lateral tracking move alongside the sprinting wolf (head locked in frame), head bobbing with rapid strides, smoke peeling off the crest, background monitors streaking right to left; light handheld bounce.

Refs: master `000a36ef` (@Video1) · @Image1 Fantasy Gate interior `22c1d2ad` · @Image2 wolf sheet `b5f7908e` (design copied, solid flat black, crest = outline only).
The reference frame itself is NOT attached (burnt-in timecode + scene label); composition described in words. Duration not given → 5 s.

QA: linter PASS (after "Nobody else exists in this clip" wording). Manual: 0 people + 1 wolf; one camera move; no pupils; no text; no purple; mouth closed, no teeth; Style Lock with the wolf exception.
Request JSON: `KMM_options/requests/wolf_profile_run_inside_gate_5s.json`.

Status: COMPLETED — job `ae5635f3-b977-430c-b047-cf5c0fa2de54` (declined preset 24bae836) → https://d8j0ntlcm91z4.cloudfront.net/user_3JNS6ee2vsgr9rp9IBmIleZYkaP/hf_20261004_143322_ae5635f3-b977-430c-b047-cf5c0fa2de54.mp4
Review (Claude, frames 0.3/1.5/3/4.5 s): composition matches the reference frame well (side profile facing right, head fills the left two-thirds, ear top-centre, muzzle tip at about 3/4 width, yellow almond eye with no pupil at centre, blurred teal tunnel with floating monitors behind, no text). BUT the wolf is again a 3D-shaded dark-grey furry animal (fur on neck and crest, soft sheen, a white highlight on the nose tip), not a flat shadow. Speed must be judged in motion. Waiting for Huy PD review.

## v2: eye with NO PUPIL, emphasised (user 2026-10-04)
User: "Tạo lại shot sói chạy ở trên nhưng phải để con mắt không có con ngươi (nhấn mạnh)".
v1 eye check (crops at 0.3/2.5/4.5 s): mostly a solid yellow almond, but at about 4.5 s a dark lid line/slit crosses the glow.
Changes vs v1:
- New "EYE RULE (MOST IMPORTANT)" block right after the master line: one solid flat yellow almond, like a hole of light; no pupil, slit, dot, iris, ring, dark line, eyelid crease, catchlight; in EVERY frame.
- "No pupil" repeated in References, Composition, Action, Expression, Lighting; removed "focused on its prey" (implies a looking pupil).
- Avoid adds: pupil/slit/dark dot or line in the eye, iris, catchlight, realistic animal eye.
- Flat-shadow wording strengthened (v1 was furry/3D-shaded): black paper cut-out, no fur texture, no sheen, no grey, no nose highlight.
QA: linter PASS (0 ERROR, 0 WARN).
Request JSON: `KMM_options/requests/wolf_profile_run_inside_gate_5s_v2.json`.

Status: SUBMITTED — job `dd8c89ca-344f-4b5e-9cfa-5fdad0ecd6ce` (declined preset 24bae836)
