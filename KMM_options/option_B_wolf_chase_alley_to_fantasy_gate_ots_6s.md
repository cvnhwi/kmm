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

Status: SUBMITTED — job `877dfb1b-a668-4e5c-8b25-911a4e03fe40` (declined preset 24bae836)
