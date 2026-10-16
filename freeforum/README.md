# FREEFORUM (freeirad.org/forum) writing kit

The forum's sample history and the record of its characters, kept here so future batches stay consistent.

- CHARACTERS.md: every sample member (96 in 2 batches): voice, join date, title, location, signature, bans/deaths, post stats, favourite threads, plus the hard timeline facts and running jokes. Read this first.
- history_v1.json, history_v2.json, history_v3.json, history_v4.json (batch 4: 89 older posts linking to the other Irad sites, made by make_v4.py): everything imported so far (batch 1: 52 threads, 643 posts, 93 shoutbox; batch 2: 213 threads, 2,764 posts, 103 shoutbox). Search them for a member's name to hear their voice, or for a thread title before writing a new one.
- BRIEF.md, BRIEF2.md: the briefs the writers followed (lore rules, JSON format, validation).
- characters.py: rebuilds CHARACTERS.md from the history files (update its NOTES dict when you add members).

To add a batch: write history_vN.json in the same format with "version": "history_vN" (make_v4.py shows how, with checks), copy it to the freeirad repo as forum/inc/history_vN.json and push (the deploy uploads it), then on the forum's Admin page under "History batches" press Preview, then Import. Each batch imports once; posts already present are skipped. (Batches 1-3 went in through a one-off import.php, since retired.) Existing sample members are matched by username; new threads can't reuse an existing title; "append" adds posts to an existing thread by exact title.
