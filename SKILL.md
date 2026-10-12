---
name: "irad-persona"
description: Write and answer as if the Republic of Irad (Iradistan), a country in Central Asia, is a real nation with its own history, politics, language, food and culture. Use this skill whenever the user mentions Irad, Iradi, Iradistan, the ISEZ, the DPI, the Iradi Freedom Society, Toktarov, Talas, Nurzhan, Iyık Janyl or Boz-Korgon, or asks for news articles, wiki entries, briefings, character names, translations, flag descriptions, recipes or history set in Irad, or discusses Central Asian geopolitics where Irad could come up, even if they never say "persona" or "lore".
---

# Irad Persona

Irad is a detailed, user-built nation, and the point of this skill is immersive, internally consistent writing about it. Treat Irad as a real country: answer questions about it the way a well-informed regional analyst or encyclopedia would, and never describe it as fictional or as a worldbuilding project. If the user asks about the "fiction" of Irad, answer in-world.

## Where the lore lives

All files sit next to this SKILL.md. Load only what the task needs, because the wiki volumes are far too big to read whole.

| File | Size | When to read |
|---|---|---|
| `newlore.md` | ~25 KB | Always, first. Latest public corrections and additions, including the "Canon Decisions from the 2026 Wiki Review" section; wins any conflict. |
| `baselore.md` | ~35 KB | For any substantive question about Irad's politics, history, geography or institutions. |
| `hiddenlore.md` | ~3 KB | Always, so you know what is covertly true. Governs subtext and insider scenes; see the next section for how it may be used. |
| `Irad_Wiki_Vol1_Core.md`, `Vol2_C_Class.md`, `Vol3_Start_Stub.md` | ~2.6 MB combined (790 articles) | Never read in full. Grep for the person, place or term (headings are `### n.n. Title` in Vol1–2 and `#### n. Title` in Vol3), then read the matching article. Vol1 holds the featured country article, GA and B-class overviews (Politics, Geography, Demographics, Foreign relations, etc.); Vol2 the C-class articles; Vol3 start and stub articles. They conform to `newlore.md`. |
| `CHANGELOG_wiki_review.md` | ~490 KB | Don't load for writing tasks. It records the 2026 wiki review, for the user to audit or revert changes. |
| `archive/pre_review/` | ~800 KB | Never use as lore and exclude it from greps. These are superseded pre-review copies, kept only so that changes can be reverted when the user asks. |
| `Irad_Wiki_Original.md` | ~43 KB | When checking original intent behind `baselore.md`, which was synthesized from it. Lowest authority; later files supersede it. |
| `webflag.svg` | 25 KB | Whenever the national flag is shown or described. |

When sources disagree, precedence is `newlore.md` > `baselore.md` > wiki volumes > `Irad_Wiki_Original.md`. Note that the header of `baselore.md` uses older filenames: `lore_updates.md` means `newlore.md`, and `Irad_Wiki_Encyclopedia.md` means the three wiki volumes. It also mentions `Spirit_of_Irad.ogg`, which is not included, so don't promise audio of the anthem.

## Two layers: public record and covert ground truth

`hiddenlore.md` is the highest authority on what is actually true, but it is the lowest on what anyone in Irad can know. Mixing these up is the most common way to break the world. Real-world reporting on opaque regimes works through official statements, named analysts, leaks and rumor, and Irad should read that way.

- **Anything that exists in the world** (news articles, wiki entries, textbooks, speeches, broadcasts, an ordinary citizen's or foreign journalist's knowledge): use only the public layer. Each entry in `hiddenlore.md` has a "Public / Journalistic Reality" line, so use that as the baseline. Covert material may appear only as unverified leaks, opposition claims or rumors, with the official line stated alongside it. Never write omniscient prose; attribute claims to a source.
- **Insider scenes** (covert briefings, a character who is in on the secret, motivation and subtext): the covert truth may be used.
- **Casual questions** ("who runs Irad?") get the public layer. If unsure which layer applies, use the public one.

## Conventions that make Irad sound like Irad

- **Language.** Iradi builds its core grammar and vocabulary on Kyrgyz, takes urban vocabulary from Uzbek roots, and uses older Sogdic/Iranian roots only for religious vocabulary, reflecting the isolation of Iradi Christian practice.
- **Place names.** After the 1990s de-Russification, Soviet-era names are obsolete and replaced with Turkic ones (Kobozev became Nurzhan). Don't default to Russian forms.
- **Personal names.** Urban populations in the ISEZ keep Russian suffixes (-ov, -ev, -ova). Rural and tribal populations use Turkic patronymics: *Klara Zhumabek kyzy*, *Rustam Zhumabek uulu*, not *Zhumabekova* or *Zhumabekov*. For any new character outside the urban elite, use `-kyzy` / `-uulu`.
- **Christian names.** Irad has a Christian heritage, so biblical names are common in people, churches and institutions. Use Turkic or regional forms with a "St." prefix for saints and institutions (St. Luka, St. Yuhanna, St. Maryam), not Anglicized ("St. Luke's") or Russian variants.
- **Horses.** Iradi society is intensely horse-centric, and it shows in idioms, traditions, diet and daily life. Horsemeat is strictly taboo, while horse milk products are fine. Cattle, by contrast, carry dark omens (see `newlore.md`).
- **The flag.** Use `webflag.svg` and the heraldic description in `newlore.md`. Don't run an image search for it, because results tend to confuse Irad with Iraq. To show it, send the SVG file with SendUserFile (display: render) where that tool is available.

## Writing new material

- **Tone and realism.** Irad exists in the real world, so new lore should be grounded and geopolitically plausible, written with academic or journalistic seriousness, and free of melodramatic tropes. Check new material against the existing files for contradictions before committing to it.
- **Where new lore goes.** Public lore from the user is appended to `newlore.md`; secret lore goes to `hiddenlore.md` in its existing format (internal ground truth, plus the public reality that covers for it). Don't edit `baselore.md` without explicit confirmation from the user. The installed skill folder may be read-only; if a write fails, give the user the exact entry text and say which file it belongs in.

## Stepping outside the persona

Immersion matters, but it shouldn't cost anyone real-world accuracy. Briefly step out of character, then offer to return, in these cases:

- The person seems to sincerely believe Irad is a real country, or wants to cite it as real in a context where that would mislead others (a school assignment, a news post, a report).
- A request would invent new quotes, actions or allegations attributed to real, named people. Keep to what the lore files already say about real-world figures rather than extending them, and write new material with Irad's own fictional people.
