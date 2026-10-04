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

Status: SUBMITTED — job `747e3916-cda7-44d1-b368-a16793ff7c95` (declined preset f1821f84)
