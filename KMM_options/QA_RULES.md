# KMM — QA RULE: check prompt, logic and raccord BEFORE every generation

Created 2026-10-04 at Huy PD's request ("tạo rule QA để kiểm lại prompt, logic và raccord trước mỗi lần gen để không bị lỗi AI: số người, lặp người, vị trí, hành động khó hiểu, overact").
**Mandatory for every Seedance submission.** No request is submitted until both gates pass. Claude reports the QA result to the user in the same message as the submission.

## Gate 1 — automatic linter (must show 0 ERROR)

```
python3 KMM_options/tools/kmm_prompt_qa.py <request.json>
```
- Input: the exact JSON that will be sent (`{"prompt","medias","duration"}`, `{"params":…}` or a batch list).
- **ERROR = do not submit.** Fix and re-run.
- **WARN = fix, or accept it explicitly** in the plan file under "QA accepted warnings" with a one-line reason.

What it checks:
| # | Check | Catches |
|---|---|---|
| 1 | Every attached `@ImageN` / `@Video1` is mentioned; no tag beyond the attached count; no old "Image N"; no raw ids/URLs; no media attached twice | wrong references, blending |
| 2 | `[Head Count]` exists, "EXACTLY N people" equals the numbered list; numbering 1..N; no tag or name used twice; "nobody else"; any other people-count in the prompt is not larger than N | wrong totals → duplicated people |
| 3 | `[Generation Goal]` shot count = shot lines; shots contiguous from 0 to the duration; each shot has a "N people visible / in frame" statement; shot < 1 s; too many actions per second; more than one dominant camera move; "Cut." | timing errors, confusing action, stacked camera moves |
| 4 | Mandatory blocks: References, Character Look, Expression, Audio (NO music), Avoid, Visual Style, No Blending, Arena Scale (BOSS arena), Eyes / Villain Variety (villains), Running Style (Mai runs) | missing project rules |
| 5 | Over-acting words outside [Avoid] (scream, sob, hysterical, wide grin, mouth wide open, jaw drops, explodes with joy…) | over-acting |
| 6 | Moderation/IP words outside [Avoid] (studio or film names such as "Disney", real insignia such as wreath / star badge / crossed rifles, dog breeds, football, guns, blood…) | `ip_detected`, `nsfw` blocks |
| 7 | Prompt > 17 000 chars, > 12 images | diluted attention, blend risk |

## Gate 2 — manual review by Claude (write the answers in the plan file)

**A. People and duplicates**
1. Count the cast twice on the scene map. Same number in [Generation Goal], [Head Count] and the shot lines?
2. For each shot: who is in frame? The number written equals the names listed?
3. Any two characters with similar silhouettes or colours (e.g. Police Officer vs Security Guard, two kids in the same uniform)? Write a contrast sentence and never stand them side by side.
4. Is a crowd really needed? If not, "nobody else exists". If yes, the crowd is anonymous and visibly different from every named character.

**B. Positions and raccord (CAMERA_LIBRARY_B section 7)**
5. Scene map written: landmarks, each character's mark and facing, the action line, the side the camera stays on.
6. Every shot keeps the same positions, screen direction, eyelines and the hand that holds each prop.
7. Costume/prop state continuous (helmet on or off, pan in hand or not, backpack on, damage, tears).
8. Continuity with the previous and next clip: first frame of this clip = last frame of the previous one (position, light, state).
9. Light direction and time-of-day consistent; changes only when the story changes them (e.g. the transformation).

**C. Action logic (no "AI confusion")**
10. One clear main action per shot; at most 2-3 beats per second of screen time; a 1-second shot holds ONE simple action.
11. Each action has a cause and a readable start → peak → end; no action that needs off-screen explanation.
12. Physical possibility: distances vs time (nobody crosses the arena in 1 s), sizes (child 6-6.5 heads, adults 7-7.5), contact (who touches whom, with which hand).
13. Order of events matches the story beat list; nothing appears before it is introduced (bus, puppy, prop).
14. Camera: ONE dominant move per shot, motivated; the move does not cross the action line.
15. Words are concrete and unambiguous (no "something happens", "magic stuff"); no contradictory instructions (e.g. "hands free" and "holding the pan").

**D. Acting / over-acting**
16. Expression intensity 1/3-1/2; emotions change in stages; reactions after the trigger.
17. Joy is shown by smiles, light steps and soft laughter, not wide-open mouths or wild jumping; fear by breath and eyes, not screams.
18. Children's safety wording when Mai is in danger (loose loop over clothes, holds on, gentle fall, caught safely).

**E. Project rules recap**
19. No text (except a title the user explicitly requested); villains flat black, no pupils, no purple; crowds never in sync; monitors mostly dark; real-time 24 fps; SFX only.
20. CHARACTER_BIBLE lines used verbatim (with the plain-insignia moderation wording); `@` tags next to every name.

## Report format (to Huy PD, Vietnamese, before or with the submission)

```
QA trước khi gen: Linter 0 ERROR, N WARN (đã sửa: …; chấp nhận: … vì …)
- Số người: EXACTLY N (… / …), từng shot: S1 … người, S2 …
- Vị trí/raccord: …
- Hành động: shot nào dày nhất, đã đơn giản hóa thế nào
- Overact / moderation: …
```

## Known lessons (append new ones here)
- Wrong head count ("12 people" for 11) → the model added duplicates (happy ending v3).
- Detailed real insignia + dog breed + football comparison → `ip_detected` (happy ending v2).
- The word "Disney" sat in the old [Acting] template ("Disney principles") in every prompt until 2026-10-04 → replaced by "Classic animation principles".
- A 1-second shot with a reveal + head lift + smile is too dense (happy ending v4, shot 3).
- 13-14 reference images in one clip = high blend risk; split the clip or keep minor people small and far.
