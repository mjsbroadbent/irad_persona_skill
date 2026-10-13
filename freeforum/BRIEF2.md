# Batch 2: about 2,000 more FREEFORUM posts

Read, in this order:
1. /home/claude/freeirad_build/history/BRIEF.md: lore, rules, cast, JSON format and validation. All of it still applies.
2. /home/claude/freeirad_build/history/BATCH1_DIGEST.md: everything already written (members, running jokes, existing threads). Do NOT duplicate existing threads; build on them.
3. Optionally skim /home/claude/freeirad_build/forum/inc/history.json for the voices of the regulars (search for a member's name to read their posts).

Twelve writers work in parallel, each owning one slice (a board and a span of years). Stay inside your slice so nobody overlaps. Within your slice:
- Write about 170 posts in NEW threads (roughly 12-20 threads; mix long threads of 20-40 posts with short ones of 3-8). Real forums have lots of short, silly, dead-end threads too ("anyone else's internet slow", one reply).
- You may also "append" up to 20 posts to EXISTING threads that are in your board (exact title from the digest), dated inside your years, fitting between existing posts and not contradicting them.
- You may add up to 6 new members (define them in "users"); choose distinctive names, check the digest so you don't reuse a name, and give them a voice. Most posts should still come from the established cast so the community feels continuous.
- Keep the established timeline: who has joined by then, Ak_Shumkar's escalating temper up to his ban (2016-08-27), olddog_1992 alive until Feb 2021, JANYL_watch mod until Apr 2019, Kobozev_Kid mod from 2016, the [RUMOUR]/[HEARD]/[SEEN] title rule in Leaks & Rumours from 30 Aug 2024.
- Do NOT write: the Ak/Temir feud's key moments (already written), Tulparcoin outcomes (unresolved), any confirmation of hidden lore, anything set after 2026-10-13 18:00.
- Vary rhythm: bursts around big events, quiet months, night posting, bumps of old threads years later ("bumping this because..."), quoting, derails, mod warnings (sparingly).

Output: /home/claude/freeirad_build/history/v2_<SLICE>.json (same format as BRIEF.md; omit "shoutbox" unless your slice says otherwise). Validate it with Python before you finish.

Final report: path, number of new threads, posts, appended posts, new members (with one-line voice notes), and any minor lore you invented.
