# AI-Video Prompt Output

Use this reference when turning a directing plan into a generation-ready prompt.

## Pick the right deliverable

- **Single shot:** one continuous time-ordered paragraph.
- **Multi-shot sequence:** numbered shots with exact time windows, followed by global continuity locks.
- **Existing prompt revision:** preserve valid content and rewrite only contradictions, ambiguity, and weak camera direction.
- **Previz or video lock:** treat the source motion/camera as immutable; describe only allowed replacements or look transfer.
- **Image-to-video:** establish what the image controls—start frame, end frame, identity, layout, or style—and never assume it controls all of them.

## Prompt assembly order

Write in this order when applicable:

1. Duration, aspect ratio, shot count, and continuity mode.
2. Subject identity and non-negotiable reference locks.
3. Start composition: shot size, angle, subject position, gaze, environment, and lens character.
4. Time-ordered subject action and blocking.
5. Time-ordered camera path and framing evolution.
6. Peak beat: contact, reveal, reaction, or transformation.
7. End composition and settle condition.
8. Lighting, atmosphere, materials, rendering style, and motion rendering.
9. Focus, depth of field, shutter/motion-blur behavior when important.
10. Negative constraints targeted to predictable failures.

Do not bury camera instructions beneath long visual-style prose.

## Temporal language

For clips under 15 seconds, use a small number of readable phases. Example structure:

- **0.0–2.0s:** establish and orient.
- **2.0–6.5s:** develop action and camera relationship.
- **6.5–8.0s:** peak beat.
- **8.0–10.0s:** consequence and stable ending.

Adapt phase count to the actual action. Do not force four phases when two are sufficient.

Describe continuous motion with start → path → finish:

> Camera begins in a low medium-wide three-quarter view, tracks backward 2–3 meters at the runner's speed while maintaining knee-up framing, then eases into a waist-level medium shot as she stops; no orbit, no cut, no focal-length change.

## Reference hierarchy

When several assets exist, declare each role explicitly:

- **Video/previz:** camera path, timing, framing, blocking, or body motion.
- **Start image:** exact first-frame composition and/or identity.
- **End image:** exact final composition and/or identity.
- **Character reference:** face, hair, proportions, clothing, accessories.
- **Environment/style reference:** palette, material language, shape language, density—not necessarily exact layout.

Never let a style reference silently override a locked layout or identity. If the user says “follow,” clarify in the prompt whether that means palette, shape language, composition, motion, or all of them.

## AI-video feasibility rules

- Prefer camera paths describable as a single curve.
- Use one dominant move per beat.
- Keep critical body action visible; do not let the camera outrun or orbit behind it.
- Avoid simultaneous extreme subject speed, large camera translation, focal-length change, roll, and rack focus.
- Specify realistic parallax and motion blur only in relation to movement.
- For fast action, keep the subject readable and allow brief settling frames around key contacts.
- For transformations or explosions, preserve causal order and subject continuity before adding debris or particles.
- If duration is tight, simplify choreography before compressing every action into unreadable motion.

## Negative constraints

Write only relevant constraints, such as:

- no extra cuts, no orbit, no zoom, no camera shake;
- no identity drift, outfit change, duplicated limbs, prop swapping;
- no floating feet, sliding contact, teleportation, or inconsistent screen direction;
- no cluttered micro-detail, over-sharpening, tiny noisy textures, or excessive particles;
- no unintended reframing, recentering, crop, or lens change when locked.

Avoid generic giant negative lists; they dilute priority.

## Director's validation pass

Ask internally:

1. What does the audience learn or feel from this exact camera position?
2. Why does the camera move at this moment?
3. Can the viewer understand where everyone is?
4. Can the action and camera coexist physically?
5. Does the final frame clearly land the story beat?
6. Can an AI-video model execute this without interpreting contradictory verbs?

If any answer is weak, simplify or redesign before returning the prompt.
