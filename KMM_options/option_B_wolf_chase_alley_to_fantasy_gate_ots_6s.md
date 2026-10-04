# KMM — Option B: the smoke wolf chases Mai down the dusk alley into the Fantasy Gate, OTS from behind the wolf (6 s, one take)

User request (2026-10-04) with a frame from the draft (s4.S62-63, burnt-in note "sói đang chạy"): recreate this shot; the wolf keeps running and chasing Mai; the exact same camera angle; the location is the alley with the fantasy gate ahead that Mai runs into. All generations go to MV KMM › FANTASY 2.

Composition locked to the frame: eye-level camera just behind/right of the wolf; its black furry head and shoulder fill the LEFT third in soft focus; a straight wet dusk street centred into depth; a warm street lamp on the right sidewalk; utility poles and sagging wires; at the far end, centred, a huge round arch of twisted black roots with a bright teal opening; Mai small in the opening, running away from camera.
Action: one forward tracking move keeping pace with the running wolf; Mai scurries through the arch, glances back once, disappears into the teal light; the wolf keeps running, never reaches her.

Refs: NEW master `000a36ef` (FANTASY.mp4, already shows this alley and root gate) · @Image1 alley `c0accc1d` (relit dusk after rain) · @Image2 Fantasy Gate interior `22c1d2ad` (teal monitor tunnel seen through the arch) · @Image3 Mai `0d56fcb2` · @Image4 smoke wolf `b5f7908e`.
Folder: MV KMM › FANTASY 2 `08a93ec8-25e5-49aa-83c2-0492790d5567` (new, created 2026-10-04).

QA: linter PASS after fixes (added [No Blending]; "tangled" → "twisted"/"sagging" because "tangled" is also a film title). Manual: 1 person + 1 wolf, no contact, one camera move, no text (the reference frame's burnt-in caption and timecode are explicitly avoided), no pupils, no purple on the wolf.
Flags: the reference frame itself was not attached (it carries burnt-in text); the composition is described in words. Duration not given → 6 s.

Request JSON: `KMM_options/requests/wolf_chase_alley_gate_6s.json`.

Status: COMPLETED (chưa kiểm tra nội dung) — job `dc8cfa6f-f7f0-44f5-b7dc-be4d1f32de17` (declined preset 24bae836)

## v2: the wolf as a PURE NIGHT SHADOW (no real fur) + Style Lock (user 2026-10-04), 6 s, one take
User re-sent the same frame and request, adding: the wolf must be a night-shadow, not real fur.
Cause in v1: the prompt said "black smoke and shaggy fur" and "black furry head" → furry wolf.
Changes vs v1:
- Wolf rewritten everywhere as a flat neutral-black shadow silhouette, outline breaking into plain black smoke, no fur/hair/skin/muscles/3D shading, flat glowing yellow almond eyes; light does not model it (no rim highlights); shadow paws leave rippling smoke in puddles. Avoid adds: realistic animal, fur, hair strands, fluffy/shaggy coat, furry texture, detailed muzzle, 3D-shaded wolf body.
- [Style Lock] block (RULES J.15); Mai line marked "design only, re-render in Mai's 3D style".
- Canonical wolf line added to CHARACTER_BIBLE (never write "fur" for the wolf).
- Same locked composition, folder FANTASY 2, new master `000a36ef`.
QA: linter PASS (after adding [Style Lock], which the linter flagged).
Request JSON: `KMM_options/requests/wolf_chase_alley_gate_6s_v2.json`.

Status: COMPLETED — job `877dfb1b-a668-4e5c-8b25-911a4e03fe40` (declined preset 24bae836) → https://d8j0ntlcm91z4.cloudfront.net/user_3JNS6ee2vsgr9rp9IBmIleZYkaP/hf_20261004_124052_877dfb1b-a668-4e5c-8b25-911a4e03fe40.mp4 — chờ Huy PD review (sói phải là bóng đêm, không lông)

## v3: only the wolf's HEAD in frame + faster wolf + light handheld shake (user 2026-10-04), 6 s, one take
User feedback on v2: camera must not show the wolf's rear/hindquarters, only its head; the wolf should feel faster; handheld camera with a little shake.
Changes vs v2:
- Composition: camera held tight behind the wolf's head; only the back of the skull + two ears in the lower-left third; frame cuts at the neck; shoulders/back/hindquarters/rump/legs/tail never visible (body behind and below camera).
- Speed: wolf sprints in a quick urgent gallop; houses/lamp/poles rush past noticeably fast; gate grows clearly larger; wolf still never reaches Mai.
- Camera: ONE fast forward HANDHELD tracking move with slight natural shake (small bumps/micro-sway synced to strides, horizon level, never chaotic).
- Audio: rapid footfalls, fast ghostly panting.
- Avoid adds: wolf body/hindquarters/tail visible, full-body wolf, slow trot/loping, smooth gimbal/locked-off, violent shaky-cam, whip pans, heavy motion-blur smear, tilted horizon.
QA: linter PASS (0 ERROR, 0 WARN). Manual: 1 person + 1 wolf head, no contact, one camera move, style lock kept, no fur, no pupils, no purple, FANTASY 2, master 000a36ef.
Request JSON: `KMM_options/requests/wolf_chase_alley_gate_6s_v3.json`.

Status: COMPLETED — job `1e625548-5187-45bf-abe7-f113d7845e2b` (declined preset 24bae836) → https://d8j0ntlcm91z4.cloudfront.net/user_3JNS6ee2vsgr9rp9IBmIleZYkaP/hf_20261004_125605_1e625548-5187-45bf-abe7-f113d7845e2b.mp4
Review (Claude, frames 0.5/3/5.5 s): framing near head-only but the wolf still shows furry texture + 3D shading and part of its back by 3-5 s; Mai starts mid-street (user: too far from the gate).

## v4: Mai closer to the gate + wolf as a pure night shadow (no fur), wolf reference REMOVED (user 2026-10-04), 6 s, one take
User feedback on v3: Mai should be closer to the gate; the wolf must not show fur, it is a night shadow.
Root cause of the fur: the wolf sheet `b5f7908e` (@Image4) has a spiky mane; the model follows the image over the "no fur" text.
Changes vs v3:
- Wolf reference image dropped (3 images now: alley, gate interior, Mai). Wolf described in words only: pure flat neutral-black void, like a hole cut out of the picture / black paper cut-out, zero inner detail, smooth outline (rounded back of head, two smooth pointed ears), edges dissolving into thin plain black smoke.
- Avoid adds: spiky mane, tufts, fur on ears/neck, fur-textured edge, dark brown/grey wolf, 3D-modelled wolf head with light and shading.
- Mai is already at the threshold of the arch from the first frame (a few steps in front), small but clearly readable against the teal opening; she takes her last few steps in and glances back once.
- Head-only framing, fast wolf, light handheld shake kept from v3.
QA: linter PASS (0 ERROR, 0 WARN). Manual: 1 person + 1 wolf head, no contact, one camera move, style lock, no pupils, no purple, FANTASY 2, master 000a36ef. Bible + QA lessons updated (do not attach the wolf sheet).
Request JSON: `KMM_options/requests/wolf_chase_alley_gate_6s_v4.json`.

Status: COMPLETED — job `ae2b45d8-152c-4d5e-aff3-972fa7565217` (declined preset 24bae836) → https://d8j0ntlcm91z4.cloudfront.net/user_3JNS6ee2vsgr9rp9IBmIleZYkaP/hf_20261004_134514_ae2b45d8-152c-4d5e-aff3-972fa7565217.mp4
Review (Claude, frames 0.5/2.5/4/5.5 s): head-only framing OK (no back/rump); wolf head darker and smoother than v3, less fur, but edges still soft-fuzzy and slightly 3D-shaded; at ~5.5 s, inside the teal tunnel, the head turns lighter grey-pink (lit). Mai still starts mid-street, NOT near the gate (model kept the master's distance). Camera enters the tunnel at the end. Waiting for Huy PD review.
Ideas for v5 if needed: start the camera itself much closer to the gate (gate fills ~half the frame at frame 1), shorten the distance in words ("10 metres"), keep the wolf head pure black even inside teal light, stop the camera before the arch.

## v5: Mai's SCALE matches the master video (user 2026-10-04), 6 s, one take
User feedback on v4: "lưu ý scale của Mai, giống với video ref".
Master check (frames of 000a36ef): the root arch is only about twice Mai's height and spans the narrow alley wall to wall; up close Mai fills 1/3 to 1/2 of the frame height. Our v1-v4 wrote "a huge round GATE ARCH" → Mai became a tiny dot in a giant gate.
Changes vs v4:
- New [Scale Lock, match @Video1] block: Mai about 1.4 m (6-6.5 heads); arch opening about twice her height (about 3 m), alley-wide, not gigantic; shutters taller than Mai; Mai about 1/3 of frame height at frame 1, growing toward 1/2.
- Camera starts near the end of the street (gate about 10 m ahead, filling the middle half of the frame); Mai about 8 m from camera, right at the gate; camera STOPS before the arch (never enters).
- Wolf head stays pure black even in the teal light (v4 went grey-pink).
- Avoid adds: Mai tiny/far, a giant gate, a long empty street, camera entering the tunnel, wolf head lit grey/pink.
QA: linter PASS (0 ERROR, 0 WARN). Manual: 1 person + 1 wolf head, no contact, one camera move, style lock, wolf reference still dropped, FANTASY 2, master 000a36ef.
Request JSON: `KMM_options/requests/wolf_chase_alley_gate_6s_v5.json`.

Status: COMPLETED — job `6edd622d-9d50-489c-8bb1-3e8a98cd159c` (declined preset 24bae836) → https://d8j0ntlcm91z4.cloudfront.net/user_3JNS6ee2vsgr9rp9IBmIleZYkaP/hf_20261004_135303_6edd622d-9d50-489c-8bb1-3e8a98cd159c.mp4
Review (Claude, frames 0.3/2/3.5/5.5 s): scale FIXED: Mai about 1/3 of frame height, arch about twice her height, alley-wide, like the master. Head-only wolf framing OK; head mostly black, crisp at the end, edges still a little soft/fuzzy at 2-3.5 s. Camera still pushes through the arch at the end (did not stop before it). Waiting for Huy PD review.

## v6: wolf exactly like its sheet (night shadow, big) + Mai already STANDING at the gate (user 2026-10-04), 6 s, one take
User feedback on v5: "sói giống với sheet, kiểu bóng đêm, đủ to, Mai đứng sẵn ở gần với cổng".
Changes vs v5:
- Wolf sheet `b5f7908e` re-attached as @Image4; design copied exactly (lean silhouette, tall ears, jagged spiky crest, narrow muzzle, yellow almond eyes); spiky crest = outline shape only, solid flat deep black, no fur texture. Bible updated (reverses the v4 "do not attach" note).
- Wolf HUGE: shoulders taller than Mai, head as tall as Mai's upper body; head + ears + crest fill the LEFT 40% of the frame from the bottom edge to above the middle.
- Mai already STANDING one step in front of the arch at frame 1, half-turned looking back (0-1.5 s), then runs in (1.5-4 s).
- Camera ends outside, framing the arch (v5 pushed through).
- Scale Lock from v5 kept.
QA: linter PASS (0 ERROR, 0 WARN). Manual: 1 person + 1 wolf head, no contact, one camera move, style lock, FANTASY 2, master 000a36ef.
Request JSON: `KMM_options/requests/wolf_chase_alley_gate_6s_v6.json`.

Status: COMPLETED — job `c67f909c-87b6-4ab6-b736-57e6c7a8ce71` (declined preset 24bae836) → https://d8j0ntlcm91z4.cloudfront.net/user_3JNS6ee2vsgr9rp9IBmIleZYkaP/hf_20261004_140033_c67f909c-87b6-4ab6-b736-57e6c7a8ce71.mp4
Review (Claude, frames 0.3/1.5/3.5/5.5 s): wolf now BIG and follows the sheet (tall ears, spiky crest, dark shadow look), crest spikes still slightly fur-like/3D; Mai already standing in the arch at frame 1 and looks back, then runs in. Mai smaller than v5 at the start (about 1/6 of frame height, gate further). Camera again pushes into the arch by 5.5 s. Waiting for Huy PD review.
