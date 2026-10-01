# KMM — Camera library for option B (3D animated feature language)

Purpose: pick shot size + angle + movement per angle when the user asks for "nhiều góc camera của một cảnh". Every move is motivated by story/emotion, the way Disney/Pixar layout departments plan cameras. Written 2026-10-01 from established animation/cinematography practice (layout & camera principles of feature animation: motivated camera, ease-in/ease-out on every move, one idea per shot, 180-degree rule, parallax for depth). Not a copy of any studio document.

## 1. Core rules (apply to every angle)
1. **Motivated**: the camera moves because a character moves, looks, feels, or something is revealed. No decorative drifting.
2. **One move per shot**: one clear move (or move + small settle). No stacking push + orbit + tilt at once.
3. **Ease in / ease out**: camera starts and stops softly (slow-in/slow-out), like an animated object; only crash moves start hard.
4. **Speed = emotion**: slow = dread, awe, sadness, tenderness; medium = following, discovery; fast = panic, impact, comedy beats.
5. **Lead the action**: on movement, keep more space in front of the character than behind (look room / lead room).
6. **180-degree line**: all angles of one scene stay on the same side of the action line; screen direction (left->right) stays consistent so the angles cut together.
7. **Same timing across angles**: in a multi-angle set, every angle plays the SAME 8 s action with the same beat timings so the editor can cut anywhere.
8. **Depth**: put foreground elements (cables, glass, smoke, shoulders, branches) for parallax; the camera move must reveal depth.
9. **KMM limits**: no shaky handheld (at most a "subtle operator float"), whip pan only where the script calls for it, no text/numbers in frame.
10. **Lens feel** (give in prompt): 18-24 mm wide/space and scale, 35 mm OTS/inserts/walk-and-talk, 50 mm neutral tracking, 85-100 mm close-ups and emotion, 135 mm compressed long-lens tension.

## 2. Shot sizes
| Code | Size | Use |
|---|---|---|
| EWS | extreme wide | scale, isolation (tiny Mai in huge hall), boss reveal |
| WS | wide / full body | geography, chase, team line-up |
| MWS | medium wide (knees up) | action with body language |
| MS | medium (waist up) | fights, gestures, two-shots |
| MCU | medium close (chest up) | reactions, dialogue-free acting |
| CU | close-up (face) | emotion peaks |
| ECU | extreme close (eyes, mouth, hand) | fear, tears, a decision |
| INS | insert | prop or detail (phone, shoes, pan, fingers) |

## 3. Angles
| Angle | Effect | KMM use |
|---|---|---|
| Eye level | neutral, empathy | default for Mai |
| Child eye level (low adult) | world seen at Mai's height | adults/creatures loom |
| Low angle | power, threat, heroism | boss, shadow people, heroes' entrance (guard, police, bus) |
| High angle | vulnerability, smallness | Mai cornered, team surrounded |
| Bird's-eye / top-down | pattern, entrapment | crowd closing in a ring, sweeping ash |
| Worm's-eye | extreme scale | cables from ceiling, bus bursting through wall |
| Dutch tilt (5-15 deg) | unease, wrongness | screen wall, monitors glitching (sparingly) |
| OTS (over the shoulder) | relation, confrontation | shadow over Mai, guard over Mai |
| POV | subjectivity | Mai sees reaching hands, monitor screens |
| Profile (side) | pursuit, clarity of motion | running chase, drift |

## 4. Movement library
Format: **name** | what it does | emotion / when | animation note | Seedance prompt wording

### Static & subtle
- **Locked-off** | no move | stillness, comedy timing, tension that lets acting play | best for acting holds | "static locked-off camera"
- **Breathing / micro float** | tiny slow drift | keeps a still shot alive | barely visible, never shake | "nearly static camera with a very slow subtle drift"

### Push / pull
- **Push-in (dolly in)** | camera travels toward subject | realisation, rising fear, intimacy | ease in, accelerate slightly, ease out on the face | "slow dolly push-in toward her face"
- **Creep-in** | very slow push over the whole shot | dread, something is wrong | 5-10% frame change only | "imperceptibly slow creeping push-in"
- **Pull-back reveal (dolly out)** | camera retreats to reveal context | isolation, scale, surprise reveal | start close, end wide on the reveal | "camera pulls back slowly to reveal ..."
- **Crash zoom / snap push** | very fast push or zoom | shock, comic beat, impact | hard start, quick settle | "fast crash zoom into ..."
- **Dolly zoom (vertigo)** | dolly one way, zoom the other | dizzy shock, world shifts | use once per film, max | "dolly zoom, background stretches while she stays the same size"

### Lateral & following
- **Truck / crab (lateral track)** | camera moves sideways | parallel running, revealing a row (monitor wall, shadow people) | foreground parallax sells speed | "camera trucks left alongside her"
- **Tracking follow (behind)** | follows subject from behind | pursuit, going into the unknown | keep lead room ahead | "tracking shot following behind her at shoulder height"
- **Tracking lead (in front, backwards)** | moves backward ahead of subject | fleeing toward camera, determination | subject faces camera | "camera moves backward in front of her as she runs toward it"
- **Steadicam glide** | smooth free path | following through space, walk-and-talk | fluid curves | "smooth steadicam glide following ..."

### Rotation
- **Pan** | rotates horizontally | follow a look or a moving object, link two subjects | ease in/out, motivated by a glance | "slow pan right following her gaze to ..."
- **Tilt up / down** | rotates vertically | tilt up = scale/threat reveal (boss, gate), tilt down = defeat, detail | "camera tilts up from her shoes to the giant boss"
- **Whip pan** | very fast pan with blur | sudden attention change, transition | ONLY where the script asks | "single whip pan to ..."
- **Roll / dutch drift** | slow rotation on lens axis | disorientation, glitch world | small angles | "slow slight roll into a dutch angle"

### Vertical & big moves
- **Pedestal / boom up-down** | camera rises or lowers straight | rise = hope, overview; lower = settle into intimacy | "camera booms down to her eye level"
- **Crane / jib up (rise and reveal)** | rises and tilts down | grand reveal, ending, surrounded team | slow, majestic | "slow crane up and back, revealing the ring of shadows"
- **Crane down (descend into scene)** | descends from high | entering a world, opening | | "camera cranes down from high into the hall"
- **Orbit / arc** | circles subject | heroic moment, decision, team unity, surrounded | 45-180 deg, keep subject centred | "camera arcs 90 degrees around them"
- **Fly-through** | travels through gaps/objects | energy, entering another space | through broken screens, smoke | "camera flies forward through the shattered screen"

### Lens / focus
- **Rack focus** | focus shifts between planes | shift of attention (hand -> face, Mai -> shadow behind) | no camera move needed | "rack focus from the phone to her face"
- **Shallow DOF hold** | long lens, soft background | isolation, emotion | 85-135 mm | "85mm close-up, shallow depth of field"

### Vehicle / action specials
- **Bonnet / mounted cam** | rides on a vehicle | speed, impact POV | KMM bus scenes | "camera mounted on the bonnet riding forward"
- **Low skid tracking** | camera near the floor moving fast | speed, tyres, shoes | drift, chase | "low tracking shot inches above the floor"
- **Impact frame + settle** | push on hit, tiny overshoot, settle | weight of a punch/pan hit | emphasise the hit, no shake | "quick push on the impact with a small overshoot and settle"

## 5. Coverage templates by scene type (pick 4-6 angles)
| Scene type | Recommended angle set |
|---|---|
| Scare / threat approaching (shadows close in) | A WS low static (threat grows) · B high angle creep-in on Mai (vulnerable) · C POV slow push toward reaching hands · D ECU Mai eyes, locked-off · E OTS from behind the shadow, slow push |
| Chase / run | A profile truck with foreground parallax · B tracking lead (running toward camera) · C tracking follow from behind · D low skid on feet · E high wide pan following |
| Rescue / hero entrance | A worm's-eye static as hero breaks in · B low angle crane down to hero stance · C orbit 90 deg around hero · D Mai MCU rack focus to hero in background |
| Fight / combo hit | A MWS orbit around the pair · B MS truck alongside the strike · C INS impact (fist/pan) with impact push · D low angle static wide · E reaction CU of the other character |
| Emotional beat (tears, relief) | A CU locked-off 85 mm · B MCU very slow push-in · C OTS of parent, slow lateral · D INS hand/tear, rack focus |
| Reveal (boss, gate, new world) | A pull-back reveal · B tilt up from character to object · C crane up and back · D worm's-eye static |
| Comedy beat (frying pan "boong") | A MS locked-off (timing) · B crash zoom on the face after the hit · C two-shot static for the reaction look |

## 6. How a multi-angle request is written
1. Beat analysis of the 8 s scene (see "B acting rules" in `STYLE_GUIDE_A_B_C.md`), with fixed beat timings (e.g. 0-2 s ..., 2-3.5 s ..., impact at 3.5 s ...).
2. Choose 4-6 angles from section 5, each with shot size + angle + ONE movement from section 4 + lens.
3. Each angle prompt: same [References], same [Action] timings, same [Acting], only [Camera] (and the opening composition) changes. One continuous 8 s shot, no cuts inside.
4. [Camera] wording: "Single continuous 8-second shot, no cuts. [size], [angle], [lens]. [movement with ease-in/ease-out, motivated by ...]. Stay on the same side of the action line: [character] moves screen left to right."
5. Avoid line adds: cuts, jump cuts, shaky handheld, unmotivated camera drift, camera crossing the action line, stacked camera moves.
