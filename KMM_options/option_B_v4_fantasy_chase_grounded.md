# KMM — Option B v4: Fantasy chase (3D block look), grounded character + glitching monitors

Status: generated as draft. Job `af1740b5-6e84-41ea-8e98-063d140d9663` (created 2026-10-01 ~07:29 UTC).
Content not yet reviewed by the assistant (cannot view video).
Same refs and settings as B v3 (`option_B_v3_fantasy_chase_new_backgrounds.md`); style rules in `STYLE_GUIDE_A_B_C.md` (option B).

## User feedback applied (2026-10-01)
1. Mai must NOT run on the river surface -> shots 7-10 keep her on the dry bank beside the river; [Avoid] "Mai running on or over the river surface".
2. At the large gate Mai has her back to the camera -> shot 13 is filmed from behind, she faces the gate; [Avoid] "Mai facing the camera in shot 13".
3. Monitors must flicker/glitch continuously -> shots 2-5: nonstop on-off strobing, static bursts, tear lines, brightness jumps; their light flickers on Mai; [Avoid] "still or static monitors". ("strobe" is allowed for screens in B; Mai's face/body must not flicker.)
4. Character must be physically inside the background, not a pasted layer -> new [Integration] block: matching light, screen/fog light on her, contact shadows, weight, kicked dust/leaves/fog, mist in front and behind, correct perspective and parallax, no cut-out edges/halo; [Avoid] "composited or pasted-on look, cut-out edges, mismatched lighting, floating feet".

## Settings
model `seedance_2_5`, mode `omni_reference`, draft true, 480p, 25 s, 16:9, generate_audio false, folder `fef878e4-1957-439e-8b50-00a4ee8454c6`, declined_preset_id `24bae836-2c4a-48e0-89b6-49fcc0b21612`. Cost 75 credits (same ref set as B v3 preflight).

## References
Video 1 `c5746038-2de6-4154-852e-6e431e457aa5` (StandardB)
Ref 1 Mai `b42c82ad-d58e-4fb3-bcf3-4d89dac09517` · 2 wolf `f48ff106-d9d6-4233-a770-d36f768a1f64` · 3 crow `6a271d30-4602-4348-8042-8728526956c5` · 4 spider `cdcbdc48-05d0-4875-b2c4-eb77a56cb96b` · 5 shadow person `2f07fe73-628d-4761-aeff-0b32446d8a0c` · 6 entrance `b97b3e97-5b27-4deb-92ea-a10693bc61e9` · 7 forest `d823d7cf-984c-4298-a9ab-62cd1b809b0b` · 8 river `fa8a5475-6c31-41b3-91ba-9881972d4319` · 9 gate `5aa39a50-f435-41b1-8f99-def9153bc90f`

## Prompt changes vs B v3 (rest identical)
- [Generation Goal] adds: "Mai is physically inside every location, never looking pasted on top of it."
- Shots 2-5: monitors "glitch and flicker nonstop: rapid on-off strobing, static bursts, horizontal tear lines, brightness jumps, never still"; shot 3 adds flickering cold light on her face and clothes.
- Shots 7-10: "runs along the dry bank BESIDE the digital river, her feet always on the solid dark ground of the bank, never on, in or above the stream"; shot 10 "still on the bank, never stepping onto the river".
- Shot 13: "medium from BEHIND Mai: she runs toward the large gate and stops in front of it, her back to the camera, facing the gate; we see her back, hair and backpack, not her face. The gate's teal door light rims her silhouette."
- [Scene]: monitors "constantly glitching, flickering"; river "with a dry walkable bank beside it".
- New [Integration] block (see feedback 4).
- [Camera]: "and from behind in shot 13".
- [Maintain Consistency]: "Mai stays on solid ground in the river shots. In shot 13 her back faces the camera."
- [Avoid] adds: floating feet, Mai running on or over the river surface, Mai facing the camera in shot 13, composited or pasted-on look, cut-out edges, mismatched lighting between Mai and background, still or static monitors.
