#!/usr/bin/env python3
"""KMM prompt QA linter: run on every Seedance request BEFORE generating.

Usage:
  python3 KMM_options/tools/kmm_prompt_qa.py request.json [more.json ...]

Accepted JSON shapes:
  {"prompt": "...", "medias": [...], "duration": 20}            (single)
  {"params": {...}}  or  [{"index": 0, "params": {...}}, ...]    (batch)

Exit code 1 if any ERROR is found. WARN lines must be read and either fixed
or explicitly accepted in the plan file. See KMM_options/QA_RULES.md.
"""
import json
import re
import sys

NUMBER_WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
    "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16, "twenty": 20,
}
OVERACT = [
    r"\bscream(s|ing)?\b", r"\bshout(s|ing)?\b", r"\byell(s|ing)?\b", r"\bsobb?(ing|s)\b",
    r"\bhysteric", r"\bwail", r"\bwide[- ]open mouth", r"\bmouth wide open", r"\bjaw drops",
    r"\bgasps? in shock", r"\bshocked face", r"\bhuge grin", r"\bwide grin", r"\becstatic",
    r"\bexplodes? with joy", r"\bjumps? wildly", r"\bflails?", r"\bthrash", r"\bpanics? wildly",
    r"\bcries out loud", r"\bburst(s)? into tears", r"\bover the top",
]
MODERATION = [
    r"\bwreath\b", r"\bstar badge\b", r"\bred[- ]star\b", r"\bcrossed rifles\b", r"\btwo silver stars\b",
    r"\brottweiler|labrador|corgi|husky|shiba|poodle|retriever\b", r"\bfootball\b",
    r"\bmarvel|avengers|disney|pixar-style|disney-style|pixar|dreamworks|ghibli|rapunzel|tangled|harry potter|doctor strange|captain america|endgame\b",
    r"\bgun(s)?\b(?![^.]*\b(no|never|avoid)\b)", r"\bblood(?!\w)", r"\bnaked|nude|underwear\b",
    r"\bfull[- ]body golden aura\b",
]
CAMERA_MOVES = [r"push(-| )?in", r"pull(-| )?back", r"\barc(s|ing)? (moving|around|left|right|\d)", r"orbit", r"tilt", r"\bpan\b", r"crane",
                r"truck", r"dolly", r"whip", r"rise", r"boom", r"track"]


def load_requests(path):
    data = json.load(open(path, encoding="utf-8"))
    out = []
    if isinstance(data, list):
        for item in data:
            out.append((f"{path}#{item.get('index', '?')}", item.get("params", item)))
    elif "params" in data:
        out.append((path, data["params"]))
    else:
        out.append((path, data))
    return out


def block(prompt, name):
    m = re.search(r"\[" + re.escape(name) + r"[^\]]*\]", prompt)
    if not m:
        return None
    nxt = re.search(r"\n\[[A-Z][^\]]*\]", prompt[m.end():])
    return prompt[m.start(): m.end() + (nxt.start() if nxt else len(prompt))]


def outside_avoid(prompt):
    i = prompt.find("[Avoid]")
    return prompt if i < 0 else prompt[:i]


def qa(label, params):
    E, W = [], []
    prompt = params.get("prompt", "")
    medias = params.get("medias", [])
    duration = params.get("duration")
    n_img = sum(1 for m in medias if m.get("role") == "image_references")
    n_vid = sum(1 for m in medias if m.get("role") == "video_references")
    body = outside_avoid(prompt)

    # 1. references and @-tags
    if n_vid and "@Video1" not in prompt:
        E.append("@Video1 is attached but never mentioned (RULES J.9).")
    used = {int(x) for x in re.findall(r"@Image(\d+)", prompt)}
    for i in range(1, n_img + 1):
        if i not in used:
            E.append(f"@Image{i} is attached but never mentioned.")
    for i in sorted(used):
        if i > n_img:
            E.append(f"@Image{i} is mentioned but only {n_img} images are attached.")
    if re.search(r"\b(Image|Video) \d+\b", prompt):
        E.append("Old-style 'Image N' / 'Video N' found: use @ImageN / @Video1.")
    if re.search(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|https?://", prompt):
        E.append("Raw media id or URL inside the prompt.")
    ids = [m.get("value") for m in medias]
    if len(ids) != len(set(ids)):
        E.append("The same media is attached twice (duplicate-character risk).")

    # 2. head count
    hc = block(prompt, "Head Count")
    named = []
    if hc is None:
        if n_img >= 3:
            E.append("No [Head Count] block (mandatory when 2+ named characters, RULES J.10).")
    else:
        m = re.search(r"EXACTLY (\d+|\w+) people", hc)
        total = None
        if not m:
            E.append("[Head Count] does not state 'EXACTLY N people'.")
        else:
            t = m.group(1)
            total = int(t) if t.isdigit() else NUMBER_WORDS.get(t.lower())
        items = re.findall(r"^\s*(\d+)\.\s+([^(:\n]+?)\s*(?:\((@Image\d+)\)|\(([^)]*)\))?\s*:", hc, re.M)
        named = [(int(n), name.strip(), tag or "") for n, name, tag, _ in items]
        if total is not None and len(named) != total:
            E.append(f"[Head Count] says {total} people but lists {len(named)} numbered people.")
        nums = [n for n, _, _ in named]
        if nums and nums != list(range(1, len(nums) + 1)):
            E.append("[Head Count] numbering is not 1..N in order.")
        tags = [t for _, _, t in named if t]
        dup = {t for t in tags if tags.count(t) > 1}
        if dup:
            E.append(f"Same tag used for two people: {sorted(dup)}.")
        names = [n.lower() for _, n, _ in named]
        dupn = {n for n in names if names.count(n) > 1}
        if dupn:
            E.append(f"Same person listed twice: {sorted(dupn)}.")
        if "nobody else" not in hc.lower():
            W.append("[Head Count] should say 'Nobody else exists in this clip'.")
        # every other people-count in the prompt must agree
        if total is not None:
            for mm in re.finditer(r"\b(\d+|" + "|".join(NUMBER_WORDS) + r")\s+(people|persons|characters)\b", body, re.I):
                v = mm.group(1)
                v = int(v) if v.isdigit() else NUMBER_WORDS[v.lower()]
                ctx = body[max(0, mm.start() - 40): mm.end()]
                if re.search(r"(merge|merging|mix|swap)\s*$", body[max(0, mm.start() - 12): mm.start()], re.I):
                    continue
                if v > total:
                    E.append(f"Count conflict: '{ctx.strip()}' > head count {total}.")
                elif v != total and "visible" not in body[mm.start(): mm.end() + 12]:
                    W.append(f"Other people-count '{mm.group(0)}' (head count {total}); make sure it is a per-shot visible count.")
        # each named person's row/position appears once
        for _, name, tag in named:
            if tag and len(re.findall(re.escape(tag) + r"\)", hc)) > 1:
                E.append(f"{name} {tag} placed twice in [Head Count].")

    # 3. shots and timing
    gg = block(prompt, "Generation Goal") or ""
    m = re.search(r"(\d+) seconds, (\d+) shots", gg)
    shots = re.findall(r"^Shot (\d+) \((\d+(?:\.\d+)?)-(\d+(?:\.\d+)?) s\)(.*)$", prompt, re.M)
    if not shots:
        W.append("No 'Shot N (a-b s)' lines found.")
    else:
        if m and int(m.group(2)) != len(shots):
            E.append(f"[Generation Goal] says {m.group(2)} shots but {len(shots)} shot lines found.")
        prev_end = 0.0
        for i, (k, a, b, rest) in enumerate(shots, 1):
            a, b = float(a), float(b)
            if int(k) != i:
                E.append(f"Shot numbering broken at Shot {k}.")
            if abs(a - prev_end) > 1e-6:
                E.append(f"Shot {k} starts at {a}s but the previous shot ended at {prev_end}s.")
            if b <= a:
                E.append(f"Shot {k} has non-positive length.")
            if b - a < 1.0:
                W.append(f"Shot {k} is under 1 s ({b - a:.1f}s): risky for AI, keep only one simple action.")
            prev_end = b
            if hc is not None and not re.search(r"visible|in frame", rest[:220]):
                W.append(f"Shot {k}: no per-shot 'N people visible' statement (RULES J.10).")
            mv = re.search(r"(\d+) (?:people|persons|characters)[^.;:]{0,40}(?:visible|in frame)", rest[:220])
            if mv and int(mv.group(1)) > 5 and not re.search(r"tiny|silhouette|distant", rest[:260], re.I):
                W.append(f"Shot {k}: {mv.group(1)} readable people in one frame; max ~5 (RULES J.12). Use backs, inserts or tiny distant silhouettes.")
            if re.search(r"close-up|\bCU\b|85 ?mm|100 ?mm", rest[:300], re.I) and re.search(r"\bface", rest[:400], re.I) and hc is not None:
                W.append(f"Shot {k}: face close-up in a multi-character clip (RULES J.12); prefer hands/props/backs.")
            moves = {mv for mv in CAMERA_MOVES if re.search(mv, rest[:400], re.I)}
            if len(moves) > 2:
                W.append(f"Shot {k}: several camera moves named ({', '.join(sorted(moves))}); keep ONE dominant move.")
            verbs = len(re.findall(r";", rest))
            if (b - a) and verbs / (b - a) > 2.5:
                W.append(f"Shot {k}: {verbs + 1} actions in {b - a:.1f}s; too dense, may look confusing.")
            if i < len(shots) and not rest.rstrip().endswith("Cut."):
                W.append(f"Shot {k} does not end with 'Cut.'.")
        dur = duration or (int(m.group(1)) if m else None)
        if dur and abs(prev_end - dur) > 1e-6:
            E.append(f"Last shot ends at {prev_end}s but duration is {dur}s.")
        if m and duration and int(m.group(1)) != duration:
            E.append(f"[Generation Goal] says {m.group(1)}s but the request duration is {duration}s.")

    # 4. mandatory blocks
    for b_ in ["References", "Character Look", "Expression", "Audio", "Avoid", "Visual Style"]:
        if block(prompt, b_) is None:
            E.append(f"Missing [{b_}] block.")
    if hc is not None and block(prompt, "No Blending") is None:
        E.append("Missing [No Blending] block.")
    au = block(prompt, "Audio") or ""
    if "NO music" not in au:
        E.append("[Audio] must end with 'NO music, NO score...'.")
    low = prompt.lower()
    if "boss arena" in low and block(prompt, "Arena Scale") is None:
        E.append("BOSS arena scene without [Arena Scale] block (RULES J.8).")
    if re.search(r"villain|night-shadow|shadow people|the boss\b", body, re.I) and "no villains" not in body.lower():
        if block(prompt, "Eyes") is None:
            E.append("Villains/BOSS present but no [Eyes] no-pupil block.")
        if re.search(r"villain|night-shadow", body, re.I) and block(prompt, "Villain Variety") is None:
            W.append("Villains present but no [Villain Variety] / 5 villain designs check.")
    if "mai" in low and re.search(r"\bMai\b[^.]{0,60}\b(runs|scurries|hurries)", body) and block(prompt, "Running Style") is None:
        E.append("Mai runs but no [Running Style] block (rule 5e).")

    # 5. over-acting and moderation words (outside [Avoid])
    for pat in OVERACT:
        for mm in re.finditer(pat, body, re.I):
            ctx = body[max(0, mm.start() - 30): mm.end() + 20].replace("\n", " ")
            if not re.search(r"\b(no|never|not|without|avoid)\b", ctx, re.I):
                W.append(f"Over-acting risk: '...{ctx.strip()}...'")
    for pat in MODERATION:
        for mm in re.finditer(pat, body, re.I):
            ctx = body[max(0, mm.start() - 30): mm.end() + 20].replace("\n", " ")
            if not re.search(r"\b(no|never|not|without|avoid)\b", ctx, re.I):
                W.append(f"Moderation/IP risk: '...{ctx.strip()}...'")
    if len(prompt) > 17000:
        W.append(f"Prompt is {len(prompt)} chars; very long prompts dilute attention. Trim repeated text.")
    if n_img > 12:
        W.append(f"{n_img} images attached: high blend/duplicate risk. Consider splitting the clip or keeping minor people small in the far row.")

    print(f"\n=== QA {label} ===  images={n_img} videos={n_vid} chars={len(prompt)} named={len(named)}")
    for e in E:
        print("ERROR:", e)
    for w in W:
        print("WARN: ", w)
    if not E and not W:
        print("PASS: no automatic findings (still do the manual checklist in QA_RULES.md).")
    return not E


if __name__ == "__main__":
    ok = True
    for path in sys.argv[1:]:
        for label, params in load_requests(path):
            ok = qa(label, params) and ok
    sys.exit(0 if ok else 1)
