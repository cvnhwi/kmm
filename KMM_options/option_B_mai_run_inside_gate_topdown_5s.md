# KMM — Option B: Mai runs inside the fantasy gate, HIGH top-down angle, no smoke trail (5 s, one take)

User request (2026-10-04) with a frame from the draft (s4.S62-63, timecode burnt in: high top-down view down a dark root tunnel, light at the top, Mai small in the centre with a white smoke trail and a long shadow): "Gen lại cảnh này nhưng bối cảnh là ở phía trong cổng fantasy, Mai đang chạy, và không có khói phía sau dưới chân Mai". Folder MV KMM › FANTASY 2.

Composition locked to the frame: camera high above and behind, about 60 degrees down; dark root/cable tunnel walls frame the left and right thirds and close over the top; a vertical band of light down the centre (bright at the top, darker at the bottom); Mai small just below centre, seen from above/behind, running UP the frame toward the light; long shadow straight DOWN the frame.
Location changed to the INSIDE of the fantasy gate (@Image1 `22c1d2ad`: teal tunnel with floating monitors). NO smoke/dust/mist anywhere (Avoid lists it twice).
Action: one slow forward drift following Mai at the same angle; Mai runs on, never looks back.

Refs: master `000a36ef` (@Video1) · @Image1 gate interior `22c1d2ad` · @Image2 Mai `0d56fcb2`. Reference frame not attached (burnt-in text). Duration not given → 5 s.
QA: linter PASS (one over-acting false positive on "arch over" → reworded). Manual: 1 person, one camera move, no text, no smoke, Style Lock, Mai's running style.
Request JSON: `KMM_options/requests/mai_run_inside_gate_topdown_5s.json`.

Status: COMPLETED — job `7495be11-7e21-42aa-8bf4-7abe44e9b0bd` (declined preset f1821f84) → https://d8j0ntlcm91z4.cloudfront.net/user_3JNS6ee2vsgr9rp9IBmIleZYkaP/hf_20261004_145633_7495be11-7e21-42aa-8bf4-7abe44e9b0bd.mp4
Review (Claude, frames 0.3/1.7/3.2/4.7 s): location correct (inside the gate: teal tunnel with floating monitors, red roots on the right), NO smoke anywhere, Mai runs away from camera toward the bright end on a glowing path, long shadow toward camera, no text. BUT the angle is only moderately high (about 20-25 degrees down), not the steep near top-down of the reference, and Mai is bigger (about 1/4 of frame height) than the tiny figure in the reference. Waiting for Huy PD review.

## v2: high camera INSIDE the gate, Mai runs from the TOP of the frame DOWN (arrow), FAST, no smoke (user 2026-10-04)
User re-sent the frame with a red arrow pointing down the path onto Mai: "Góc camera cao ở phía trong cổng, chiếu xuống Mai, chạy từ chiều phía trên xuống (giống hình mũi tên), tốc độ nhanh".
Changes vs v1:
- Direction reversed: Mai runs DOWN the frame (from the bright far end at the top toward the bottom / camera side), light behind her, shadow ahead of her toward the bottom edge.
- Steeper angle: camera near the tunnel ceiling, about 70-75 degrees down; Mai about 1/8 of frame height.
- Camera: ONE high backward glide in Mai's direction but slower than her, so she travels from the upper third (0-1 s) through the centre (1-4 s) to the lower third (4-5 s).
- Speed: FAST quick urgent little steps (still the girlish running style, not an athlete); one glance back toward the light.
- Still no smoke/dust/mist anywhere.
QA: linter PASS (0 ERROR, 0 WARN); manual fix: v2 draft said "camera keeps Mai centred" AND "she runs down the frame" (contradiction) → camera slower than Mai.
Request JSON: `KMM_options/requests/mai_run_inside_gate_topdown_5s_v2.json`.

Status: COMPLETED — job `747e3916-cda7-44d1-b368-a16793ff7c95` (declined preset f1821f84) → https://d8j0ntlcm91z4.cloudfront.net/user_3JNS6ee2vsgr9rp9IBmIleZYkaP/hf_20261004_150205_747e3916-cda7-44d1-b368-a16793ff7c95.mp4
Review: direction correct (user confirmed). Problems: Mai starts as a tiny figure high up near the bright end (looks like floating near the ceiling) and grows to about 1/3 of frame height by 5 s; tunnel looks gigantic; a strong bright light shaft down the path.

## v3: scale locked, faster, DIM light (user 2026-10-04)
User: "đúng hướng chạy rồi nhưng cần để ý scale nhân vật Mai, tăng tốc độ lên, ánh sáng yếu lại, vì lúc này đang đi vào trong hầm".
Changes vs v2:
- [Scale Lock, match @Video1]: Mai about 1.4 m; tunnel NOT gigantic (about 4 m wide, about 3x Mai's height); monitors about the size of Mai's upper body; Mai a CONSTANT one fifth of the frame height from first to last frame, always on the floor.
- Camera: ONE fast high backward glide at almost exactly Mai's speed (same distance), so she only drifts from upper-centre to lower-centre; camera about 3 m above the floor, about 70 degrees down.
- Speed: VERY FAST (top speed, running for her life, still girlish); floor, cables and monitors stream fast past.
- Lighting: LOW-KEY, no light beam/shaft; faint teal glow far behind, dim flickering monitors; tunnel grows darker as she goes deeper.
- Avoid adds: bright beam/shaft, overexposed path, Mai tiny then big, floating, gigantic tunnel, running slowly.
QA: linter PASS (0 ERROR, 0 WARN).
Request JSON: `KMM_options/requests/mai_run_inside_gate_topdown_5s_v3.json`.

Status: COMPLETED — job `708cbb72-c87b-466b-9212-461d29608751` (declined preset f1821f84) → https://d8j0ntlcm91z4.cloudfront.net/user_3JNS6ee2vsgr9rp9IBmIleZYkaP/hf_20261004_150942_708cbb72-c87b-466b-9212-461d29608751.mp4
Review (Claude, frames 0.3/1.7/3.2/4.7 s): light is now dim/low-key with no beam (OK), no smoke, direction OK, tunnel more human-scaled, Mai roughly constant size (about 1/5, a bit bigger near the end). BUT the camera is only moderately high (about 30-40 degrees down), not tight under the ceiling; user follow-up: "camera góc sát trần".

## v4: camera tight against the CEILING (user 2026-10-04: "camera góc sát trần")
Changes vs v3:
- Camera mounted right against the tunnel ceiling, lens pointing almost straight down (about 80 degrees); out-of-focus hanging roots and cables of the ceiling in the extreme foreground along the top and side edges of the frame to sell that the camera is AT the ceiling.
- Mai seen almost straight from above (top of her head, shoulders, backpack, quick legs), constant size about 1/6 of the frame height.
- Speed, dim light, scale lock, no smoke, direction (top of frame → bottom) kept from v3.
Request JSON: `KMM_options/requests/mai_run_inside_gate_topdown_5s_v4.json`.

QA: linter PASS (0 ERROR, 0 WARN).

Status: COMPLETED (FAILED the brief) — job `2d480b66-aee6-4f64-a09b-880488f73f7f` → https://d8j0ntlcm91z4.cloudfront.net/user_3JNS6ee2vsgr9rp9IBmIleZYkaP/hf_20261004_152113_2d480b66-aee6-4f64-a09b-880488f73f7f.mp4
Review (Claude, frames 0.3/1.7/3.2/4.7 s): the model ignored the ceiling camera: eye-level/low camera, Mai about half the frame height running straight at camera. Likely pulled by the master video's eye-level tunnel shot. Text alone is not enough for an extreme angle.

## v5: START FRAME first (top-down image), then video
Plan: generate a top-down still (gpt_image_2_5, refs gate interior `22c1d2ad` + Mai `0d56fcb2`, 16:9) with the ceiling camera, Mai 1/6 of frame in the upper-centre, dim light, no smoke; then Seedance 2.5 with that image as `start_image` and @Video1 for STYLE ONLY (not camera/framing).
Start frame: image job `c8b4192b-7d18-4632-8b13-433db79374f3` (gpt_image_2_5, high, 1k, 16:9) → https://d8j0ntlcm91z4.cloudfront.net/user_3JNS6ee2vsgr9rp9IBmIleZYkaP/hf_20261004_152640_c8b4192b-7d18-4632-8b13-433db79374f3.png
Review (Claude): near top-down from the ceiling, dark root/cable ceiling edges framing, monitors along both walls, Mai small (about 1/7 of frame) upper-centre running down the frame, dim light, no smoke, no text. Waiting for Huy PD approval before the video.
Huy PD approved the start frame ("ok").
v5 video: v4 prompt + [START FRAME] block (keep exactly the start image's camera height/angle/framing/lighting all clip), @Video1 = style only (no camera/framing), Mai 1/7 of frame as in the start frame, Avoid adds camera dropping/tilting, Mai running at camera at eye level, Mai bigger than in the start frame. Start image `c8b4192b` passed as role `start_image` (not counted as @Image).
QA: linter PASS (0 ERROR, 0 WARN).
Request JSON: `KMM_options/requests/mai_run_inside_gate_topdown_5s_v5.json`.

Status: COMPLETED (partly) — job `2db940f7-4105-4bf4-81b5-c40644cbf41c` (declined preset f1821f84) → https://d8j0ntlcm91z4.cloudfront.net/user_3JNS6ee2vsgr9rp9IBmIleZYkaP/hf_20261004_153206_2db940f7-4105-4bf4-81b5-c40644cbf41c.mp4
Review (Claude, frames 0.3/1.7/3.2/4.7 s): 0-about 2 s GOOD (ceiling camera near top-down, Mai small running down the frame, dim, no smoke). From about 2.5 s the camera swings down to eye level and Mai grows to about 1/3 of the frame running at camera (same drift as v4: pulled back to the master's eye-level tunnel shot).
Next idea (v6): add an END frame image (same ceiling top-down angle, Mai in the lower-centre) as `end_image` so both ends are locked, and/or drop @Video1 from this shot (style from the start frame instead).

## v6: FIXED camera + WIDER tunnel, start AND end frames (user 2026-10-04: "góc đó camera fixed và cảnh trong hầm rộng hơn")
- New start frame `c87a72ca-3f7a-4914-ace1-be773e0fac11` (gpt_image_2_5, from start frame v5 + gate interior + Mai): same ceiling top-down angle, tunnel about 10 m wide (floor = middle half of frame), Mai about 1/8 in the upper-centre. → https://d8j0ntlcm91z4.cloudfront.net/user_3JNS6ee2vsgr9rp9IBmIleZYkaP/hf_20261004_153829_c87a72ca-3f7a-4914-ace1-be773e0fac11.png
- New end frame `b137c3ba-52f3-4d5e-8482-438657831a9e` (same image, Mai moved to the lower-centre, about 1/6). → https://d8j0ntlcm91z4.cloudfront.net/user_3JNS6ee2vsgr9rp9IBmIleZYkaP/hf_20261004_153935_b137c3ba-52f3-4d5e-8482-438657831a9e.png
- Prompt: [START & END FRAMES, FIXED CAMERA] block; camera completely still (no dolly/glide/pan/tilt/zoom/shake); only Mai moves from start to end position, very fast; dim light, no smoke; @Video1 style only. Avoid adds any camera movement, narrow tunnel.
QA: linter PASS (0 ERROR, 0 WARN); manual fix: "wide tunnel" vs Avoid "gigantic tunnel" → "cathedral-high ceiling".
Request JSON: `KMM_options/requests/mai_run_inside_gate_topdown_5s_v6.json`.

Status: SUBMITTED — job `706263b9-ce49-4998-96bd-e70f135466f0` (declined preset f1821f84)
