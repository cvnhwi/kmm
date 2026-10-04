---
name: cinematic-director
description: Create and rank short-form story hooks, then turn a selected hook, scene idea, script beat, storyboard, image, or previz into intentional cinematic direction and an executable AI-video prompt. Use for hooks, opening seconds, scroll-stoppers, camera angles, shot sizes, lensing, camera motion, blocking, shot progression, or director-style prompts. Do not use for text-only screenplay writing when neither hook design nor visual direction is requested.
---

# Cinematic Director

Direct the scene before writing the prompt. Every camera choice must serve story, emotion, spatial clarity, or a transition—not merely add spectacle.

## Choose the mode

- **Hook design:** When the user asks for hooks, opening seconds, a scroll-stopper, or a stronger story opening, use [references/hook-design.md](references/hook-design.md). Stop after the ranked hooks unless cinematic execution is also requested.
- **Scene direction:** When the user already has a scene or selected hook, direct its camera, blocking, timing, continuity, and generation prompt.
- **Hook-to-shot:** When both are requested, generate and rank hooks first, select or confirm the strongest option, then direct that option without changing its promise, timing, open loop, or eventual payoff.

## Intake

Extract what is already known: subject, action, story beat, emotion, environment, duration, aspect ratio, reference assets, continuity constraints, visual style, output model, and character/environment locks.

Ask a question only if a missing fact would materially change the result. Otherwise infer a sensible default and state it briefly. Preserve the user's existing prompt and all locked elements; refine only what needs direction.

## Directing workflow

1. Identify the dominant story beat, audience feeling, and—when this is an opening—the unanswered question that should pull the viewer forward.
2. Decide whether the scene should be one continuous shot or multiple shots. Prefer one clear visual idea per shot.
3. Select shot size, angle, framing, lens character, depth of field, camera movement, speed, stabilization, blocking, focus behavior, and transition as a coordinated system.
4. Design a readable start frame, motivated camera path, decisive peak frame, and stable end frame. Specify screen direction and subject-camera distance when continuity matters.
5. Check physical feasibility, subject visibility, collision risk, axis continuity, and whether the action remains readable at the chosen duration.
6. Translate the plan into concrete temporal language suitable for the target AI-video model.
7. Remove redundant adjectives, contradictory camera commands, and decorative moves without narrative purpose.

Use [references/camera-decision-system.md](references/camera-decision-system.md) for camera selection. Use [references/prompt-output.md](references/prompt-output.md) for timing, reference locking, prompt assembly, and quality checks. Use [references/hook-design.md](references/hook-design.md) only when hook creation or evaluation is part of the request.

## Core rules

- Start from narrative intention, not a favorite camera move.
- Treat shot size, angle, movement, blocking, lens, and focus as interdependent.
- Static is a valid deliberate choice.
- Use at most one dominant camera move per beat; add a secondary adjustment only when motivated and physically compatible.
- Distinguish camera translation from lens zoom. Never call a dolly a zoom.
- Describe observable motion: direction, path, speed curve, distance relationship, framing change, and end condition.
- For short AI clips, favor stable geometry, clear silhouettes, and simple paths over compound acrobatics.
- Do not invent cuts in a requested one-take. Do not add camera motion when camera or previz is locked.
- When a reference conflicts with text, obey the user's declared asset hierarchy. If none is declared, flag the conflict briefly.
- Avoid vague terms such as “dynamic camera” or “cinematic movement” without operational detail.
- Avoid unsupported precision. Give focal-length ranges or lens character unless the user needs exact production specifications.

## Output behavior

Default to Vietnamese explanation and an English generation prompt unless the user requests another language.

For a simple request, return:

1. **Director's choice** — concise rationale for the visual strategy.
2. **Camera design** — shot size, angle, lens, movement, blocking, focus, and timing.
3. **Final prompt** — clean, executable prose ready to paste.
4. **Negative constraints** — only failure modes relevant to the scene.

For hook-only work, use the output and scoring format in `hook-design.md`. For hook-to-shot work, present the ranked hook concepts compactly, identify the winner, then provide the full directing package for that option.

For multi-shot work, add a compact timeline or shot list. For a strict character limit, output only the optimized prompt and keep safely below the limit. If the user asks to edit an existing prompt, return the revised prompt directly and summarize only material changes.

## Quality bar

Before responding, verify:

- Each choice supports the intended emotion or story information.
- Geography and screen direction remain understandable.
- The camera path can exist physically and fits the duration.
- Start and end compositions are explicit.
- Character identity, anatomy, wardrobe, props, environment, and reference locks remain intact.
- The prompt contains no incompatible moves, accidental redesign, unrequested cuts, or style clutter.
- For hooks, the opening creates a specific unanswered question, bridges into the story, and truthfully earns its later payoff.
