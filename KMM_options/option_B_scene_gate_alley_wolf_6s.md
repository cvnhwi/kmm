# KMM — Option B single scene: Mai at the alley/fantasy gate, wolf lunge, Mai runs in (6 s)

Status: COMPLETED 2026-10-01 (~12:20 UTC). Content not yet reviewed by the assistant (cannot view video).
Job: `3d84d6f7-f399-4a99-9d73-b6e3fbce9b91` · 6 s · cut coverage, every shot with a moving camera · B lighting look · real-time 24 fps · monitors mostly dark, random on/off.

## Scene map
```
 NORTH  fantasy cave tunnel (old monitors on walls, most dark), far glow
          ^   Mai runs north
  ======= GATE / threshold  <- M0 Mai stands here, facing south, then turns
          |   ~8 m
 SOUTH  night alley (Hem1 layout, night: sodium + LED lamps, shutters)  <- W1 wolf, facing north
 cameras on the EAST side; northward = screen left -> right
```
Light: warm alley behind Mai (rim on hair/scarf), cold teal tunnel ahead (key on face, then backlight/rim inside the tunnel), cyan spill from the few lit monitors, amber eye spill on the wolf.

| Time | Shot | Camera | Action |
|---|---|---|---|
| 0.0-2.2 | 1 | ECU head-on on the wolf, Mai's eye height, 85 mm, creeping push-in -> quick pull-back driven by the lunge | wolf crouches, lunges at the lens |
| 2.2-4.0 | 2 | MS from just inside the tunnel looking south through the gate (NE), 35 mm, tracking lead + slight drift | Mai on the threshold backlit by the alley, wolf rushing behind; she spins and runs into the tunnel toward camera |
| 4.0-6.0 | 3 | WS low from behind on the E side, 24 mm, fast tracking follow | Mai runs deep into the tunnel; monitors switch on/off randomly; wolf shadow follows, never reaches |

Refs: StandardB `c5746038…`, Mai `b42c82ad…`, wolf `f48ff106…`, entrance `b97b3e97…`, alley layout `B02_Hem1_Day` `875ca1de-fe82-40c9-aaa3-1fae77e08461` (re-lit as night). ~18 credits.
Assumptions: the alley plate is a day plate re-lit to night in the prompt; the gate is described in text (no gate plate between the alley and the tunnel).

## v2 (user 2026-10-01 ~12:30 UTC)
Changes: sky already gloomy (low heavy overcast clouds, grey-violet glow); Mai's BODY faces north toward the cave with her HEAD turned back over her right shoulder looking at the wolf, frozen; the wolf's lunge is the trigger, only then she runs; monitors mostly dark, random on/off; every shot moves.
Job: `26300da4-ed14-4521-850e-3ab0ab2e277b` (folder MV KMM `fef878e4…`). Status: COMPLETED ~12:35 UTC, in MV KMM, content not yet reviewed.

## v3 (user 2026-10-01 ~12:40 UTC)
Interpretation of "Mai đang quay lưng lui nhìn về phía hẻm": Mai's BACK to the cave/camera, facing the alley, looking at the wolf; the instant the wolf lunges she spins and runs into the cave. Shot 2 now shows her back first (from inside the tunnel), then she turns toward camera and runs.
Job: `0c421b73-8879-485f-8d14-84977816003e` (folder MV KMM). Status: COMPLETED ~12:40 UTC, in MV KMM, content not yet reviewed.

## v4 (user 2026-10-01 ~15:25 UTC): fantasy Mai + fantasy master + skin/expression rules, plus a no-video test
Same action as v3 (Mai on the threshold with her back to the cave, facing the alley; wolf CU lunge; she spins and runs deep into the tunnel; gloomy sky; monitors mostly dark, random; moving camera in all 3 shots). Refs: fantasy Mai `ef343c87-2208-435b-ad72-0ad938ae95bd`, wolf `f48ff106…`, tunnel `b97b3e97…`, alley `875ca1de…` (re-lit gloomy night). Added [Character Look] fair skin + [Expression] subtle blocks.
- v4a WITH fantasy master video 720p `9e11bd39…`: job `a421aa65-1943-40ad-b61a-75e90b78aa0a`
- v4b WITHOUT any video reference (user: "thử thêm 1 bản mà không đính kèm video"), style from Mai's image + text: job `84cb13f4-14c8-4263-9226-711ca72c1194`
(First attempt timed out at 60 s; no job was created, checked in list_project_assets.)
Status: v4a and v4b COMPLETED ~15:40 UTC, content not yet reviewed.

## v5 (user 2026-10-01 ~15:50 UTC): new fantasy master video + diagonal chase angles
Same story as v4. New: master video `83190f2e-aa76-490f-8b36-633ff0cfbee6` (Fantasy_v2_720p); shots 2-3 use DIAGONAL three-quarter angles (30-45 degrees off the running line, east side) so Mai and the wolf chasing behind her are both in frame (user: "góc camera không thẳng hàng mà hơi hướng chéo để vừa thấy sói chạy ở sau đuổi theo Mai").
- Shot 1 (0-2 s) wolf ECU crouch + lunge at lens, push-in then pull-back.
- Shot 2 (2-4 s) diagonal three-quarter front from inside the tunnel (NE of Mai), backward-sideways track: Mai spins and runs past camera, wolf bursts through the gate behind her.
- Shot 3 (4-6 s) diagonal three-quarter rear, low, follow with slight arc: Mai mid-ground, wolf bounding behind, both visible, gap open; monitors random.
Refs: fantasy Mai `ef343c87…`, wolf `f48ff106…`, tunnel `b97b3e97…`, alley `875ca1de…`. Fair-skin + subtle-expression blocks included.
Job: `7ad9a461-bbb6-496f-9cf8-e729baf035bf`. Status: COMPLETED ~15:52 UTC, content not yet reviewed.

## v6 (user 2026-10-01 ~16:05 UTC): 8 s, wolf TOYS with Mai (weaves, wall-run, leaps over her), director pass
Director's choice: threat CU -> escape diagonal -> wolf "plays" on the wall (lively, cat-and-mouse) -> peak = leap over Mai and cut-off, she swerves and keeps running; end on a stable frame with the gap open.
| # | Time | Shot | Camera | Start -> Peak -> End |
|---|---|---|---|---|
| 1 | 0-1.8 s | wolf ECU, slightly low, 85 mm | creeping push-in, snap-back on lunge | crouch -> lunge at lens -> smoke over lens |
| 2 | 1.8-3.8 s | diagonal 3/4 front inside tunnel, 35 mm | backward-sideways track | Mai frozen on threshold -> spins, runs past -> wolf weaving through the gate behind |
| 3 | 3.8-6 s | wide diagonal east side, 24 mm | truck right, foreground pillars | Mai mid-ground -> wolf runs along the far west wall over flickering monitors -> overtakes |
| 4 | 6-8 s | low angle floor, 24 mm | tilt up with the arc, ease into slight arc follow | wolf leaps over Mai -> lands ahead left, playful head tilt -> Mai swerves right, runs on, wolf circling behind |
Refs: master `83190f2e…`, fantasy Mai `ef343c87…`, wolf `f48ff106…`, tunnel `b97b3e97…`, alley `875ca1de…`. Fair-skin + subtle-expression blocks.
Job: `03bce19b-794d-4740-9fd4-c9007c5fad5f`. Status: COMPLETED ~16:12 UTC, content not yet reviewed.
