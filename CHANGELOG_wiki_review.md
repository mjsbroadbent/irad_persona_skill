# Irad Wiki: 2026 Full Review, Changelog

This file records every change made in the full review of the three wiki volumes (October 2026), so that you can audit them and revert any you don't want. It is a record for you, not lore: Claude doesn't need to load it when writing about Irad.

## At a glance

| | Before | After |
|---|---|---|
| Articles | 811 (Vol1 36, Vol2 100, Vol3 675) | 785 (Vol1 51, Vol2 144, Vol3 590) |
| Size of the three volumes | ~718 KB | ~2.6 MB |
| New articles | — | 59 (15 B-class in Vol1 §3.29–3.43; 44 C-class in Vol2 §4.101–4.144) |
| Articles removed | — | 85, almost all in Vol3: mechanical duplicate place stubs merged into a surviving article, near-identical term stubs merged, and four stubs replaced by new full articles |

Every surviving article was edited. Most were expanded, many substantially. Mechanical place-name filler in Vol3 (107 stubs) was renamed to distinct, plausible names, and all stubs were rewritten in a real-encyclopedia format with sources.

**Tags used below:** [EXPANDED], [MERGED], [DELETED], [RETITLED], [CANON] (made consistent with the lore files or with a decision recorded in `newlore.md`), [NEW].

## Open decisions for you

None of these block anything. The wiki currently uses the cautious option noted for each.

1. **Calling code, internet TLD and ISO code.** The original values belong to Kyrgyzstan (+996), Guam (+1-671), Iran (.ir), Andorra (.ad) and Indonesia (.id). The infobox now shows "—". Options: "none assigned"; a territorial-era +1 area code; or a fictional code.
2. **Passports and citizenship.** One writer decided that territorial-era residents were **US nationals, not citizens**, and that this ended in December 2006 (Iradi Americans; recorded in `newlore.md`). Confirm it, or choose citizens or neither. Also undecided: what travel document the ISEZ issues, and whether the neighbours give Iradis passports. The sport article now only says some athletes "acquired" Kazakh, Kyrgyz or Uzbek citizenship.
3. **Footprint area.** For 196,754 km² to fit, most of Irad must be the steppe and desert of what is elsewhere Kazakhstan's Jambyl and Turkistan regions, because Talas plus Jalal-Abad is only about 45,000 km². The new Geography and Administrative divisions articles build this in (Northern Steppe zone about 52,000 km²). Your mental model was "largely Kyrgyzstan". Either keep the area and accept that composition, or reduce the area to around 90,000–110,000 km².
4. **Legislative Speaker.** "Kanybek Osmonov" appeared only in the infobox, and the surname collided with the director Talgat Osmonov. He is now **Nurbek Sultanov** (DPI, Speaker since 2019), named in the infobox and in the Territorial Legislature article. Rename him if you prefer.
5. **Yusup Ayyubov.** The original wiki captioned the painting *The White Rider Shows the Way* as his, but canon makes him an actor. The caption isn't used anywhere now. Should he also have painted in later life?
6. **Flag artwork vs blazon.** `newlore.md` puts the golden wheat on the lower half of the roundel, but `webflag.svg` has the stalks rising up both sides in ivory. The Flag of Irad article treats the SVG as the official artwork and the newlore text as the blazon. Which should win?
7. **LGBT rights.** There is no canon on the criminal code, so Human rights in Irad leaves the topic out.
8. **Bishkek Ceasefire signing day.** Every article says only "September 2007". Pick a day, or keep it vague.
9. **New details writers had to invent.** These are now consistent everywhere and recorded in `newlore.md`; change any you don't like:
   - territorial governors Ermatov (1995–2003) and Abdrakhmanova (2003–06), and US High Commissioners Ashby, Whitaker, Lindqvist and Garrity;
   - Lieutenant Governor Daniyar Tologonov (2007–19);
   - the anthem by Asan Jumabaev and Cholpon Myrzakulova;
   - the som fixed at 5 per US dollar since 1993;
   - a State Archives fond scheme;
   - Kara-Köl on the tribal side.
10. **Corrections waiting on your OK.** You asked me not to edit `baselore.md` without confirmation, so the decisions above were recorded in a new section at the end of `newlore.md`, which overrides baselore. These baselore lines are now out of step with the wiki, and I can fix them if you say so:
    - the ISEZ-creation line (it compresses 25 Feb and 4 Jun 2007);
    - the coordinate, calling-code and TLD lines;
    - "Kobozev until 1991" (should be 1992);
    - the *Swift Hooves* origin;
    - the CPC pipeline route;
    - the religion percentages and the legislature details where they differ.
    
    `newlore.md`'s own "UNESCO World Heritage Sites" list ("four sites") and its "biannual" film festival are also superseded by the new section.

## How to revert

- **Whole files:** the skill folder includes `archive/pre_review/`, which holds every lore and wiki file exactly as it was before this review. Copy any file back over its current version to undo all changes to it.
- **Single articles or single changes:** find the article in Parts D–G below, then ask Claude to "revert <article> to its pre-review version" or to "undo the change to <x>". Claude will restore it from `archive/pre_review/` and make sure the links still work.
- Earlier changes made before this review (the Tajikistan removal, the footprint change, the Toktogul split) are in `CHANGELOG.md`.

## How this file is organised

- **Part A:** global and mechanical changes (regex fixes, retitles, link repointing, reassembly).
- **Part B:** cross-file consistency fixes.
- **Part C:** fixes from the final independent review.
- **Parts D–F:** per-article edits, by volume and chunk.
- **Part G:** the new articles.


## Part A. Global and mechanical changes


### A.1 Mechanical fixes applied before editing (regex, all volumes)

- V1: replaced meta header paragraph (SKILL.md/newlore/'canonical worldbuilding' references) with in-world intro (×1)
- V1: removed word counts from assessment lines (×35)
- V1: 'Chatkal-Irad industrial combine' -> Iradi Antimony and Rare Metals Combine (×1)
- V1: 'mined at Chatkal-Irad' -> 'mined at Sary-Bulak and smelted at Chatkal' (×1)
- V1: removed artificial '-Irad' suffix from place/clan names (×2)
- V1: removed real EO number (links) (×2)
- V1: removed real EO number (prose) (×1)
- V1: removed real EO number (prose) (×2)
- V1: removed UN document symbols from citations; C-24 sits in New York (×15)
- V1: C-24 'Report on' -> 'Working Paper on' (×15)
- V1: CPC citation -> KazTransOil (northern route does not use CPC) (×7)
- V1: CPC citation -> KazTransOil (×1)
- V2: replaced meta header paragraph (SKILL.md/newlore/'canonical worldbuilding' references) with in-world intro (×1)
- V2: removed word counts from assessment lines (×100)
- V2: removed real EO number (links) (×1)
- V2: removed real EO number (prose) (×2)
- V2: removed UN document symbols from citations; C-24 sits in New York (×5)
- V2: C-24 'Report on' -> 'Working Paper on' (×4)
- V2: CPC citation -> KazTransOil (northern route does not use CPC) (×1)
- V2: CPC citation -> KazTransOil (×1)
- V3: replaced meta header paragraph (SKILL.md/newlore/'canonical worldbuilding' references) with in-world intro (×1)
- V3: removed word counts from assessment lines (×236)
- V3: 'Chatkal-Irad' -> 'Chatkal' (×1)
- V3: renamed out-of-footprint place 'Cholpon-Ata' -> 'Cholpon-Bulak' (×2)
- V3: renamed out-of-footprint place 'Kumtor' -> 'Kum-Bel' (×10)
- V3: renamed out-of-footprint place 'Jety-Oguz' -> 'Jety-Kaiyng' (×4)
- V3: renamed out-of-footprint place 'Chong-Kemin' -> 'Chong-Kenkol' (×2)
- V3: renamed out-of-footprint place 'Kemin' -> 'Kenkol' (×17)
- V3: renamed out-of-footprint place 'Kara-Balta' -> 'Kara-Buura' (×10)
- V3: renamed out-of-footprint place 'Ak-Beshim' -> 'Shelji' (×2)
- V3: renamed out-of-footprint place 'Beshim' -> 'Shelji' (×8)
- V3: renamed out-of-footprint place 'Shahr-i Sabz' -> 'Shahr-i Kabud' (×2)
- V3: renamed out-of-footprint place 'Rabat-i Malik' -> 'Rabat-i Kamal' (×2)
- V3: renamed out-of-footprint place 'Darwaza Gate' -> 'Temir-Kapka Gate' (×2)
- V3: renamed out-of-footprint place 'Orto-Tokoy' -> 'Orto-Sai' (×4)
- V3: renamed out-of-footprint place 'Kurshab' -> 'Uzun-Akmat' (×6)
- V3: removed artificial '-Irad' suffix from place/clan names (×30)
- V3: removed real EO number (V3 title) (×1)
- V3: removed real EO number (stub lead) (×1)
- V3: removed real EO number (prose) (×1)
- V3: fixed doubled 'The **The' (×4)


### A.2 Global retitles [RETITLED]

- A6.md: heading 'Church of Saint Janyl' -> 'Church of St. Janyl'
- E1.md: heading 'Colonel David Sterling' -> 'David Sterling'
- E1.md: heading 'Archbishop Mar Ephrem' -> 'Mar Ephrem'
- E1.md: heading 'General Nikolai Voronov' -> 'Nikolai Voronov'
- E1.md: heading 'Father Luka Ayyubov' -> 'Luka Ayyubov'
- E1.md: heading 'Dr. Aizhan Kulova' -> 'Aizhan Kulova'
- E1.md: heading 'Feast of Saint Janyl' -> 'Feast of St. Janyl'
- E2.md: heading 'Susamyr Wool Washing Mill' -> 'Suusamyr Wool Washing Mill'
- E2.md: heading 'Susamyr River' -> 'Suusamyr River'
- E4.md: heading 'Father Toma Alimbek' -> 'Toma Alimbek'
- E4.md: heading 'Father Barnabas' -> 'Barnabas (priest)'
- E4.md: heading 'Dr. Pavel Morozov' -> 'Pavel Morozov'
- E4.md: heading 'Captain Robert Hayes' -> 'Robert Hayes'
- E4.md: heading 'Sister Maryam Janyl' -> 'Maryam Janyl (nun)'
- E4.md: heading 'Father Yuhanna of Merv' -> 'Yuhanna of Merv'
- E4.md: heading 'Sister Klara Alimbekova' -> 'Klara Alimbekova'
- E4.md: heading 'Captain Alexey Smirnov' -> 'Alexey Smirnov'
- E4.md: heading 'Colonel Richard Taylor' -> 'Richard Taylor'
- E4.md: heading 'Father Stephanos' -> 'Stephanos (priest)'


### A.3 Link repointing (101 links)

<details><summary>Every repointed link</summary>

- A1.md: link [[Church of Saint Janyl]] -> [[Church of St. Janyl]]
- A1.md: link [[Church of Saint Janyl]] -> [[Church of St. Janyl]]
- A1.md: link [[Father Luka Ayyubov|Luka Ayyubov]] -> [[Luka Ayyubov|Luka Ayyubov]]
- A1.md: link [[Archbishop Mar Ephrem|Mar Ephrem]] -> [[Mar Ephrem|Mar Ephrem]]
- A1.md: link [[Feast of Saint Janyl]] -> [[Feast of St. Janyl]]
- A2.md: link [[Sary-Chelek]] -> [[Sary-Chelek Biosphere Reserve|Sary-Chelek]]
- A2.md: link [[Luka Community Health Mission]] -> [[St. Luka Community Health Mission|Luka Community Health Mission]]
- A2.md: link [[Colonel David Sterling]] -> [[David Sterling|Colonel David Sterling]]
- A2.md: link [[Church of Saint Janyl]] -> [[Church of St. Janyl]]
- A3.md: link [[Church of Saint Janyl|Church of St. Janyl]] -> [[Church of St. Janyl|Church of St. Janyl]]
- A3.md: link [[Executive Order on the Alimbekov–Baker Treaty (2006)]] -> [[United States Withdrawal from the Alimbekov-Baker Treaty (2006)]]
- A3.md: link [[Church of Saint Janyl|Church of St. Janyl]] -> [[Church of St. Janyl|Church of St. Janyl]]
- A5.md: link [[Church of Saint Janyl]] -> [[Church of St. Janyl]]
- A5.md: link [[Feast of Saint Janyl]] -> [[Feast of St. Janyl]]
- A5.md: link [[Archbishop Mar Ephrem|Mar Ephrem]] -> [[Mar Ephrem|Mar Ephrem]]
- A5.md: link [[Church of Saint Janyl]] -> [[Church of St. Janyl]]
- A5.md: link [[Archbishop Mar Ephrem]] -> [[Mar Ephrem|Archbishop Mar Ephrem]]
- A5.md: link [[Executive Order on the Alimbekov–Baker Treaty (2006)]] -> [[United States Withdrawal from the Alimbekov-Baker Treaty (2006)]]
- A6.md: link [[Feast of Saint Janyl|Feast of St. Janyl]] -> [[Feast of St. Janyl|Feast of St. Janyl]]
- A6.md: link [[Feast of Saint Janyl|Feast of St. Janyl]] -> [[Feast of St. Janyl|Feast of St. Janyl]]
- D1.md: link [[Feast of Saint Janyl|Feast of St. Janyl]] -> [[Feast of St. Janyl|Feast of St. Janyl]]
- D1.md: link [[Church of Saint Janyl|Church of St. Janyl]] -> [[Church of St. Janyl|Church of St. Janyl]]
- D1.md: link [[Church of Saint Janyl|Church of St. Janyl]] -> [[Church of St. Janyl|Church of St. Janyl]]
- D1.md: link [[Feast of Saint Janyl|Feast of St. Janyl]] -> [[Feast of St. Janyl|Feast of St. Janyl]]
- D1.md: link [[Church of Saint Janyl|Church of St. Janyl]] -> [[Church of St. Janyl|Church of St. Janyl]]
- D2.md: link [[Church of Saint Janyl|Church of St. Janyl]] -> [[Church of St. Janyl|Church of St. Janyl]]
- D2.md: link [[Feast of Saint Janyl]] -> [[Feast of St. Janyl]]
- D3.md: link [[Feast of Saint Janyl]] -> [[Feast of St. Janyl]]
- D4.md: link [[Church of Saint Janyl]] -> [[Church of St. Janyl]]
- D4.md: link [[Archbishop Mar Ephrem|Mar Ephrem]] -> [[Mar Ephrem|Mar Ephrem]]
- D4.md: link [[Feast of Saint Janyl]] -> [[Feast of St. Janyl]]
- D4.md: link [[Church of Saint Janyl]] -> [[Church of St. Janyl]]
- D5.md: link [[Archbishop Mar Ephrem|Mar Ephrem]] -> [[Mar Ephrem|Mar Ephrem]]
- D5.md: link [[Church of Saint Janyl]] -> [[Church of St. Janyl]]
- D5.md: link [[Father Luka Ayyubov|Luka Ayyubov]] -> [[Luka Ayyubov|Luka Ayyubov]]
- D5.md: link [[Feast of Saint Janyl]] -> [[Feast of St. Janyl]]
- D5.md: link [[Church of Saint Janyl]] -> [[Church of St. Janyl]]
- D5.md: link [[Executive Order on the Alimbekov–Baker Treaty (2006)]] -> [[United States Withdrawal from the Alimbekov-Baker Treaty (2006)]]
- E1.md: link [[Church of Saint Janyl|Church of St. Janyl]] -> [[Church of St. Janyl|Church of St. Janyl]]
- E1.md: link [[Church of Saint Janyl|Church of St. Janyl]] -> [[Church of St. Janyl|Church of St. Janyl]]
- E1.md: link [[Church of Saint Janyl|Church of St. Janyl]] -> [[Church of St. Janyl|Church of St. Janyl]]
- E1.md: link [[Feast of Saint Janyl|Feast of St. Janyl]] -> [[Feast of St. Janyl|Feast of St. Janyl]]
- E1.md: link [[Church of Saint Janyl|Church of St. Janyl]] -> [[Church of St. Janyl|Church of St. Janyl]]
- E1.md: link [[Church of Saint Janyl|Church of St. Janyl]] -> [[Church of St. Janyl|Church of St. Janyl]]
- E1.md: link [[Feast of Saint Janyl|Feast of St. Janyl]] -> [[Feast of St. Janyl|Feast of St. Janyl]]
- E1.md: link [[Church of Saint Janyl|Church of St. Janyl]] -> [[Church of St. Janyl|Church of St. Janyl]]
- E1.md: link [[Feast of Saint Janyl|Feast of St. Janyl]] -> [[Feast of St. Janyl|Feast of St. Janyl]]
- E2.md: link [[Susamyr River]] -> [[Suusamyr River]]
- E2.md: link [[Susamyr Wool Washing Mill]] -> [[Suusamyr Wool Washing Mill]]
- E2.md: link [[Church of Saint Janyl|Church of St. Janyl]] -> [[Church of St. Janyl|Church of St. Janyl]]
- E3.md: link [[Church of Saint Janyl|Church of St. Janyl]] -> [[Church of St. Janyl|Church of St. Janyl]]
- E3.md: link [[Church of Saint Janyl|Church of St. Janyl]] -> [[Church of St. Janyl|Church of St. Janyl]]
- E3.md: link [[Church of Saint Janyl|Church of St. Janyl]] -> [[Church of St. Janyl|Church of St. Janyl]]
- E4.md: link [[Church of Saint Janyl]] -> [[Church of St. Janyl]]
- E4.md: link [[Church of Saint Janyl]] -> [[Church of St. Janyl]]
- E4.md: link [[Church of Saint Janyl]] -> [[Church of St. Janyl]]
- E4.md: link [[Feast of Saint Janyl]] -> [[Feast of St. Janyl]]
- E4.md: link [[Church of Saint Janyl]] -> [[Church of St. Janyl]]
- E4.md: link [[Feast of Saint Janyl]] -> [[Feast of St. Janyl]]
- E4.md: link [[Sister Maryam Janyl]] -> [[Maryam Janyl (nun)|Sister Maryam Janyl]]
- E4.md: link [[Church of Saint Janyl]] -> [[Church of St. Janyl]]
- E4.md: link [[Church of Saint Janyl]] -> [[Church of St. Janyl]]
- E5.md: link [[Susamyr River]] -> [[Suusamyr River]]
- administrative-divisions-of-irad.md: link [[Sary-Chelek]] -> [[Sary-Chelek Biosphere Reserve|Sary-Chelek]]
- bishkek-ceasefire-agreement-2007.md: link [[Feast of Saint Janyl]] -> [[Feast of St. Janyl]]
- chatkal-range.md: link [[Sary-Chelek]] -> [[Sary-Chelek Biosphere Reserve|Sary-Chelek]]
- culture-of-irad.md: link [[Church of Saint Janyl|Church of St. Janyl]] -> [[Church of St. Janyl|Church of St. Janyl]]
- education-in-irad.md: link [[Church of Saint Janyl|Church of St. Janyl]] -> [[Church of St. Janyl|Church of St. Janyl]]
- geography-of-irad.md: link [[Church of Saint Janyl]] -> [[Church of St. Janyl]]
- geography-of-irad.md: link [[Susamyr River|Susamyr]] -> [[Suusamyr River|Susamyr]]
- health-in-irad.md: link [[Dr. Pavel Morozov|Pavel Morozov]] -> [[Pavel Morozov|Pavel Morozov]]
- health-in-irad.md: link [[Sister Klara Alimbekova]] -> [[Klara Alimbekova|Sister Klara Alimbekova]]
- health-in-irad.md: link [[Sister Maryam Janyl]] -> [[Maryam Janyl (nun)|Sister Maryam Janyl]]
- health-in-irad.md: link [[Dr. Aizhan Kulova|Aizhan Kulova]] -> [[Aizhan Kulova|Aizhan Kulova]]
- irad-united-states-relations.md: link [[Colonel David Sterling]] -> [[David Sterling|Colonel David Sterling]]
- irad-uzbekistan-relations.md: link [[Church of Saint Janyl]] -> [[Church of St. Janyl]]
- iradi-alphabet.md: link [[Church of Saint Janyl|Church of St. Janyl]] -> [[Church of St. Janyl|Church of St. Janyl]]
- iradi-name.md: link [[Father Luka Ayyubov]] -> [[Luka Ayyubov|Father Luka Ayyubov]]
- iradi-name.md: link [[Father Toma Alimbek]] -> [[Toma Alimbek|Father Toma Alimbek]]
- iradi-name.md: link [[Sister Maryam Janyl]] -> [[Maryam Janyl (nun)|Sister Maryam Janyl]]
- iradi-name.md: link [[Archbishop Mar Ephrem|Mar Ephrem]] -> [[Mar Ephrem|Mar Ephrem]]
- iradi-som.md: link [[Church of Saint Janyl]] -> [[Church of St. Janyl]]
- music-of-irad.md: link [[Feast of Saint Janyl|Feast of St. Janyl]] -> [[Feast of St. Janyl|Feast of St. Janyl]]
- naryn-river.md: link [[Susamyr River]] -> [[Suusamyr River]]
- operation-starlight.md: link [[Colonel David Sterling]] -> [[David Sterling|Colonel David Sterling]]
- order-of-st-janyl-the-hermit.md: link [[Church of Saint Janyl]] -> [[Church of St. Janyl]]
- order-of-st-janyl-the-hermit.md: link [[Feast of Saint Janyl]] -> [[Feast of St. Janyl]]
- provisional-government-of-irad-1992.md: link [[Church of Saint Janyl]] -> [[Church of St. Janyl]]
- provisional-government-of-irad-1992.md: link [[Colonel David Sterling|David Sterling]] -> [[David Sterling|David Sterling]]
- public-holidays-in-irad.md: link [[Church of Saint Janyl|Church of St. Janyl]] -> [[Church of St. Janyl|Church of St. Janyl]]
- public-holidays-in-irad.md: link [[Feast of Saint Janyl|Feast of St. Janyl]] -> [[Feast of St. Janyl|Feast of St. Janyl]]
- religion-in-irad.md: link [[Church of Saint Janyl|Church of St. Janyl]] -> [[Church of St. Janyl|Church of St. Janyl]]
- religion-in-irad.md: link [[Archbishop Mar Ephrem|Mar Ephrem]] -> [[Mar Ephrem|Mar Ephrem]]
- religion-in-irad.md: link [[Sister Maryam Janyl]] -> [[Maryam Janyl (nun)|Sister Maryam Janyl]]
- religion-in-irad.md: link [[Father Luka Ayyubov|Luka Ayyubov]] -> [[Luka Ayyubov|Luka Ayyubov]]
- religion-in-irad.md: link [[Feast of Saint Janyl|Feast of St. Janyl]] -> [[Feast of St. Janyl|Feast of St. Janyl]]
- religion-in-irad.md: link [[Father Barnabas]] -> [[Barnabas (priest)|Father Barnabas]]
- territory-of-irad-1992-2006.md: link [[Church of Saint Janyl|Church of St. Janyl]] -> [[Church of St. Janyl|Church of St. Janyl]]
- tourism-in-irad.md: link [[Church of Saint Janyl]] -> [[Church of St. Janyl]]
- tourism-in-irad.md: link [[Feast of Saint Janyl]] -> [[Feast of St. Janyl]]
- transport-in-irad.md: link [[Feast of Saint Janyl]] -> [[Feast of St. Janyl]]

</details>


### A.4 Other scripted link and text fixes

- A5.md: text 'Church of Saint Janyl' x3
- A5.md: text 'Feast of Saint Janyl' x4
- A6.md: text 'Church of Saint Janyl' x1
- D4.md: text 'Church of Saint Janyl' x3
- E1.md: text 'Feast of Saint Janyl' x1
- A1.md: linked 'St. Ephrem Major Seminary' -> Cathedral Seminary of Iyık Janyl
- D1.md: NO plain occurrence of 'St. Ephrem Major Seminary'
- D5.md: linked 'St. Ephrem Major Seminary' -> Cathedral Seminary of Iyık Janyl
- order-of-st-janyl-the-hermit.md: linked 'St. Ephrem Major Seminary' -> Cathedral Seminary of Iyık Janyl
- religion-in-irad.md: linked 'St. Ephrem Major Seminary' -> Cathedral Seminary of Iyık Janyl
- D2.md: linked 'Akzhaykyn depression' -> Akzhaykyn Depression
- D4.md: linked 'Akzhaykyn depression' -> Akzhaykyn Depression
- geography-of-irad.md: linked 'Akzhaykyn depression' -> Akzhaykyn Depression
- administrative-divisions-of-irad.md: linked 'Akzhaykyn depression' -> Akzhaykyn Depression
- D4.md: linked 'Northern Export Feeder' -> Northern Export Feeder
- E2.md: linked 'Northern Export Feeder' -> Northern Export Feeder
- A6.md: linked 'Northern Export Feeder' -> Northern Export Feeder
- A4.md: linked 'Northern Export Feeder' -> Northern Export Feeder
- energy-in-irad.md: linked 'Northern Export Feeder' -> Northern Export Feeder
- transport-in-irad.md: linked 'Northern Export Feeder' -> Northern Export Feeder
- irad-kazakhstan-relations.md: linked 'Northern Export Feeder' -> Northern Export Feeder
- E2/E5: Kenkol valley exit moved to western Talas valley / Kara-Buura District (Chong-Kenkol, Ming-Örük, Karool-Döbö), following ledger #30


### A.5 Reassembly

- Volumes rebuilt from the 16 edited chunks. The 15 new B-class articles were appended to Vol1 as 3.29–3.43 and the 44 new C-class articles to Vol2 as 4.101–4.144. Section and category counts were recounted from the headings.
- Checks after the rebuild: 785 article titles, no duplicate titles, no broken wikilinks, every `<sup>[n]</sup>` marker matches its reference list, and no hits for the stale-fact, hidden-lore or meta-reference patterns listed in the handover.


## Part B. Cross-file integration fixes

These fixes came from `pass2/INTEGRATION_LEDGER.md`, which reconciled the cross-chunk notes of every editor. Each line cites the ledger item number.


### B.1 Vol1 chunks (A1–A6)

### Integration changelog: A chunks (A1–A6)

[ledger #2] A5 Alimbekov-Baker Treaty: siege dates "from 10 April to 25 May 1992" -> "from 10 April 1992; by late May…"
[ledger #2] A2 First Iradi Civil War: subsection retitled "Siege of Talas (April–June 1992)"
[ledger #2] A2 First Iradi Civil War: removed "April 10 to May 25" end date and "six weeks" from siege paragraph
[ledger #3] A2 Economy of Irad: "refinery commissioned in 1974" -> "built in the late 1950s and expanded in 1974"
[ledger #3] A3 History of Irad: "Refineries" -> "A refinery"
[ledger #3] A5 Nurzhan: deleted second "central refinery commissioned in 1974"; now Refinery No. 1 expanded in 1974
[ledger #3] A5 Nurzhan: "refineries" -> "refinery" (fuel pipeline)
[ledger #3] A5 Nurzhan: "refineries" -> "refinery" (2007 war)
[ledger #3] A5 Nurzhan: "refineries" -> "refinery" (eastern industrial zone)
[ledger #3] A5 Nurzhan: "Refinery No. 1 and the 1974 central refinery" -> "Nurzhan Refinery No. 1 (expanded 1974)"
[ledger #3] A5 Nurzhan: "refineries" -> "refinery" (2nd Motor Rifle Brigade)
[ledger #3] A5 Nurzhan: "the oldest refinery in Irad" -> "the country's only oil refinery" (single-refinery canon)
[ledger #3] A5 Talas Air Base: "refineries of Nurzhan" -> "refinery at Nurzhan"
[ledger #3] A5 Talas Air Base: "Nurzhan refineries" -> "Nurzhan refinery" (facilities list)
[ledger #4] A2 Autonomous Tribal Regions: Northern Steppe zone: Moiynkum now "between the Chu and the Talas", Betpak-Dala north of the Chu
[ledger #4] A5 Nurzhan: Moiynkum no longer placed north of Nurzhan; now south and west, between the Chu and the Talas (consequential to #4)
[ledger #5] A5 Democratic Party of Irad: "only after a formal declaration of incapacity" -> "Legal scholars differ…; no such finding has been made"
[ledger #7] A4 Aidar Maksat: "named Maksat Lieutenant Governor" -> running mate on joint ticket, took office 25 Nov 2019
[ledger #7] A5 Democratic Party of Irad: "appointed his son-in-law … Lieutenant Governor" -> joint-ticket running mate, took office 25 Nov 2019
[ledger #9] A1 Erlan Toktarov: "state-funded" now attributed to government publications
[ledger #9] A6 Akyel Horse: "private" now attributed to press reports
[ledger #9] A2 Iradi Equestrian Culture & Breeds: Toktarov no longer "founded" the State Stud Farm; it is government-run with him as patron
[ledger #11] A4 Alikhan Toktarov: "Governor's Cup" -> "President's Cup"
[ledger #12] A6 Church of Saint Janyl: UNESCO "inscribed in 2003" + separate ruins listing -> single joint property inscribed 2004, listed under the US
[ledger #12] A5 Iyık Janyl: (optional) added "together … in 2004" to UNESCO sentence
[ledger #13] A2 Autonomous Tribal Regions: St. Luka mobile clinics "since 1994" -> "since 1996" (link title left for lead integrator)
[ledger #17] A4 Kamran Bekzatov: Feeder "completed" 1998 -> IPTC formed 1998, Feeder opened November 2000
[ledger #18] A3 History of Irad: "first elected in October 1992" -> interim legislature first met Oct 1992, first general elections 1994
[ledger #18] A3 Politics of Irad: "first elected in October 1992" -> interim legislature first met Oct 1992, first general elections 1994
[ledger #19] A1 Irad: UNMI observers "about 180" -> "about 210"
[ledger #20] A6 Armed Forces of Irad: US–ISEZ interim arrangements "from 2008 onward" -> "from 2007 onward"
[ledger #21] A3 Politics of Irad: IAC "formed during the 2007 civil war" -> "formed in late 2007 at a kurultai on the Aksay Plateau, after the ceasefire"
[ledger #22] A1 Talas: Kokand fortress at Talas moved from "18th century … against Dzungar raids" to the 1820s, on an older mound
[ledger #23] A1 Irad: reworded Janyl dating to "Church tradition places her in the 11th century…; some chronicles … 12th" (removes 12th/11th clash)
[ledger #23] A5 Iyık Janyl: "11th or 12th century" -> standard 11th-century tradition / some chronicles 12th wording
[ledger #24] A6 Church of Saint Janyl: "Samarkand and Kashgar" -> "Samarkand and Bukhara"
[ledger #24] A1 Irad: church "completed in 1727" -> "founded in 1727 and consecrated in 1730"
[ledger #25] A3 History of Irad: reign "c. 1722–1733" -> "c. 1721–1733"
[ledger #26] A2 Economy of Irad: horse-slaughter law -> 1996 act bans commercial slaughter and horsemeat sales; private consumption not an offense
[ledger #26] A2 Iradi Equestrian Culture & Breeds: horse-slaughter law -> 1996 act bans commercial slaughter and horsemeat sales; private consumption not an offense
[ledger #29] A2 Autonomous Tribal Regions: Kanysh-Kiya (pop. ~2,870) replaced by Mailuu-Suu among largest settlements; "market towns" -> "towns"
[ledger #33] A6 Chongtor Horse: Almanbet "best-known foundation sire" -> "best-known modern sire, foundation of the leading endurance line"
[ledger #37] A6 NurGaz: Protocol "with Kazakhstan" -> "technical arrangements with the Kazakh border and customs services"
[ledger #58] A1 Irad / Talas / Erlan Toktarov: Fond 108 -> 110 (Territorial Legislative Journals), 3 citations (lines ~290, ~386, ~453)
[ledger #58] A5 Democratic Party of Irad / Territorial Legislature of Irad: Fond 108 -> 110 (Territorial Legislative Journals), 2 citations
[ledger #59] A5 Supreme Court of Irad: Fond 108 -> 111 (Supreme Court Reports)
[ledger #60] A5 Talas Air Base: Fond 108 -> 131 (Military Concessions and Base Allocations)
[ledger #60] A3 History of Irad: Fond 108 -> 21 (Northern Semirechye and Talas Districts)
[ledger #61] A6 Church of Saint Janyl: Fond 12 -> 3 (Kokand Charters and Firmans)
[ledger #61] A5 Iyık Janyl: Fond 27 -> 3 (Kokand Decrees and Correspondence)
[ledger #61] A6 NurGaz: Fond 312 -> 204 (Iradneft Production Association records)
[ledger #62] A3 History of Irad: Fond 233 -> 86 (Talas City Committee, June 1956)
[ledger #62] A1 Erlan Toktarov: Fond 412 -> 501 (ISEZ Executive Directives)
[ledger #64] A1 Irad: city table: Talas metro figure marked "estimate"
[ledger #64] A1 Irad: city table: Nurzhan agglomeration figure marked "estimate"
[ledger #64] A1 Talas: lead: metro figure marked as unofficial estimate
[ledger #64] A1 Talas: Demographics: metro figure marked as unofficial estimate
[ledger #64] A5 Nurzhan: lead: agglomeration figure marked as unofficial estimate
[ledger #68] A1 Irad: "biannual" -> "biennial"
[ledger #68] A1 Talas: "biannual" -> "biennial"
[ledger #66] A4 Bektur Zhumabek uulu / Aidar Maksat / Ruslan Toktarov / Jason Ilyasov: 16 unnumbered `### ` subsection headings converted to `#### ` (First Iradi Civil War (1991–1992); Territorial period (1992–2006); Second Civil War and the storming of Talas (2007); Iradi Freedom Society (2007–present); Municipal and infrastructure posts (2005–2019); Lieutenant Governor (2019–present); Since July 2024; Early career (1999–2012); Commander of the Republican Gendarmerie (2012–present); Succession contest (2024–present); Remarks about Muslims; Allegations of abuses; Business interests; Move to Talas and IradOne (2016–2023); 2023 protests and detention; Since 2024)


### B.2 Vol2 chunks (D1–D5)

[ledger #2] D5 Amanbek Alimbekov: siege end date "to 25 May" removed (siege ran 10 April to 18 June; text already says broken by 18 June)
[ledger #2] D5 Vasily Chernov: siege end date "to 25 May" removed (text already says siege broken by 18 June)
[ledger #2] D5 Talas Municipal Water Authority: "in April and May 1992" -> "from April 1992"
[ledger #2] D5 Talas Regional Hospital Medical Complex: "in April and May 1992" -> "from April 1992"
[ledger #3] D4 Iradiya: plural "refineries" -> singular "refinery"
[ledger #10] D2 Talas River Hydrological Monitoring Service: Talas terminus no longer "crosses into Kazakhstan"; ends in the Moiynkum after running near the Kazakh frontier
[ledger #10] D2 Chu River Basin: Chu terminus "south Kazakh steppe" -> "Irad's Northern Steppe, near the Akzhaykyn depression"
[ledger #15] D1 National Equestrian Sports Directorate: at chabysh distance 25-50 km -> 20-50 km
[ledger #16] D4 Fergana Mountain Transit Highway: added sentence distinguishing Otmek Tunnel from Otmek Pass
[ledger #22] D4 Old Talas Citadel Quarter: lead: citadel built "in the 18th century" -> "in the 1820s"
[ledger #22] D4 Old Talas Citadel Quarter: "Kokand fortress" section: 18th-century fortress against Dzungar raids removed; fort now built in the 1820s, Kokand authority dated to Alim and Umar
[ledger #23] D1 East Syriac Rites of Iyık Janyl: Janyl dating reordered: 11th century first, Qara Khitai 12th as alternative
[ledger #23] D1 Janyl, Mother of Irad: Janyl dating reordered: 11th century first, Qara Khitai 12th as alternative
[ledger #23] D1 Janyl (Historical Figure): Janyl dating reordered: 11th century first (consistency extension of item 23)
[ledger #27] D1 Arsha Juniper Incense Tradition: "Turkestan juniper" -> "semiglobose juniper" for J. semiglobosa
[ledger #28] D2 Kyzylkum Fringe: cobra no longer said to occur in the foothills; range approaches but not known to include Irad
[ledger #31] D3 Northern Border Demarcation Protocol: Talas North Terminal placed "north-west of Talas, in Kara-Buura District"
[ledger #32] D4 Chatkal Chemical Smelting Complex: location no longer "where the Talas Alatau meets the Chatkal range"; foothills SW of Talas, named after nearby Chatkal range
[ledger #33] D4 Chongtor Studbook Registry: "best-known foundation sire" -> "best-known modern sire, foundation of the leading endurance line"
[ledger #37] D2 Kyzylkum Fringe: "joint" -> "coordinated" patrols under the Protocol
[ledger #38] D3 El-Choro Militias: ref 1: Jane's Defence Weekly -> in-world Central Asian Geopolitical Review
[ledger #60] D2 Semirechye Revolt (Irad): Fond 108 -> Fond 21 (Northern Semirechye and Talas districts)
[ledger #60] D2 Tien Shan Marches: Fond 108 -> Fond 21 (Northern Semirechye and Talas districts)
[ledger #60] D2 Talas River Hydrological Monitoring Service: Fond 108 -> Fond 160 (hydrological survey records)
[ledger #60] D1 Burkut Saluu: Fond 108 -> Fond 175 (ethnographic records)
[ledger #60] D1 Fallen Rider Tradition: Fond 108 -> Fond 175 (ethnographic records)
[ledger #62] D1 Central Asian Pastoral Migration System: Fond 233 -> Fond 236 (collective-farm and livestock-brigade records)
[ledger #62] D3 Northern Border Demarcation Protocol: Fond 412 -> Fond 501 (ISEZ executive directives)
[ledger #51] D2 Besh-Tash Ecological Conservation Area: added hatnote pointing to [[Besh-Tash National Park]] for the 1996 park core
[ledger #3] D4 Nurzhan Polytechnic Institute: "the refineries" -> "the oil refinery" (Soviet-era Irad had one refinery; extension of item 3, not listed in ledger)
[ledger #4] D2 Chu River Basin: plain no longer "bounded ... to the north by the Moiynkum sands"; now Betpak-Dala to the north, Moiynkum closing in from the south-west downstream (extension of item 4; D not listed as owner)
[ledger #10] D2 Chu River Basin: hydrology section "endorheic basins of the south Kazakh steppe" -> "of the steppes north of the Tian Shan" (consistency extension)


### B.3 Vol3 chunks (E1–E5)

### Integration changelog: E1–E5 (integrator E)

[ledger #1] E3 2018 Border Demarcation Clashes: rewrote as clashes with Uzbek border guards in June 2018 on the western desert frontier (Kyzylkum Fringe rangelands, Syr Darya side facing Uzbekistan). Removed the Karatau/Kazakh placement, the Northern Border Demarcation Protocol paragraph and the Kazakh "local technical measure" line. Added that no technical arrangement comparable to the Kazakh ones covers this frontier, and the Iradiya landing-permit detail (matches D4 and N). Settlement kept as talks between border officers and clan elders, with UN officials facilitating. Ref 1 is now *Talas Herald*, 19 June 2018, 'Tribal Patrols and Uzbek Guards Exchange Fire on Western Frontier'.
[ledger #3] E4 Nurzhan Children's Polyclinic: "the city's refineries" changed to "the city's refinery".
[ledger #4] E2 Muyunkum Natural Gas Field: "Moiynkum (Muyunkum) sands north of the Chu" changed to "north-eastern Moiynkum (Muyunkum) sands, near the lower Chu".
[ledger #5] E3 2013 Constitutional Amendment: replaced "only after a formal declaration of incapacity" with the "Legal scholars differ…; no such finding has been made" wording. (The second occurrence, in E3 The July 2024 Transition Crisis, went with that article's deletion.)
[ledger #6] E3 2013 Constitutional Amendment: "limited the Governor to two terms" changed to "two consecutive terms".
[ledger #8] E4 Kadyrbek Asylbekov: now camera operator on *Zarina* and second-unit cinematographer on *Desert Sun's Rebellion* (Moiynkum landscape units), with Viktor Pak named as director of photography (plain text, since there is no article). Kept the 2004 restoration advisory role.
[ledger #14] E4 Aida Temirova: "National Conservatory of Music" changed to "National Conservatory of Folk Music", adding "whose classical department teaches Western instruments".
[ledger #14] E4 Elena Kim: same change.
[ledger #27] E3 Arsha (Flora): "Turkestan juniper (*Juniperus semiglobosa*)" changed to "semiglobose juniper".
[ledger #30] E2 Kenkol Pass: "upper Talas valley" changed to "western Talas valley (Kara-Buura District)".
[ledger #32] E2 Kemer Antimony Mine: "in the foothills where the Talas Alatau meets the Chatkal range" changed to "in the Talas Alatau foothills south-west of Talas, facing the Chatkal range".
[ledger #44] E4 Father Yuhanna of Merv: `[[Battle of Talas (751)|Battle of Talas]]` changed to `[[Battle of Talas]]`.
[ledger #45] E4 Kara-Bulak Agricultural Cooperative: `[[Kara-Bulak Grain Elevators]]` changed to `[[Kara-Bulak Grain Logistics Depot]]`.
[ledger #50] E3 Operation Starlight (1992): DELETED (superseded by new/operation-starlight.md).
[ledger #50] E3 Organic Act of the Territory of Irad: DELETED (superseded by the N article of the same title). Its Fond 108 citation went with it.
[ledger #50] E3 Bishkek Ceasefire Agreement (2007): DELETED (superseded by the N article of the same title).
[ledger #50] E2 Arslanbob: DELETED (superseded by new/arslanbob.md).
[ledger #51] E3 The July 2024 Transition Crisis: DELETED (covered by D3 2024 Iradi Executive Transition Crisis). The one incoming link (E3 2013 Constitutional Amendment) now points to `[[2024 Iradi Executive Transition Crisis]]`.
[ledger #51] E2 Sary-Chelek: DELETED (D2 Sary-Chelek Biosphere Reserve owns the topic).
[ledger #51] E5 (line ~579): `[[Sary-Chelek]]` changed to `[[Sary-Chelek Biosphere Reserve|Sary-Chelek]]`.
[ledger #51] E3 Kurut (Culinary): DELETED. Folded the etymology (Kipchak *kuru*, "dry") into E1 Kurut and removed E1's "See also [[Kurut (Culinary)]]".
[ledger #51] E3 Ak-Örgoe (Yurt Part): DELETED (no unique facts). Removed E1 Ak-Örgoe's "See also [[Ak-Örgoe (Yurt Part)]]".
[ledger #51] E3 Tai-Kazan-Ring: DELETED. Folded the goal dimensions (about 3.6 m across, 1.2 m high), the tires, the *kazan* (cauldron) etymology and the English-language "tai-kazan ring" usage into E1 Tai-Kazan. Removed the See-also link.
[ledger #51] E3 Koshkar-Muyuz (Motif): DELETED. Added "saddle cloths" to E1 Koshkar Muyuz and removed the See-also link.
[ledger #51] E3 Kambarkan (Music): DELETED. Folded the *Kambarkan kyly* ("Kambarkan's strings") name into E1 Kambarkan and removed the "(see [[Kambarkan (Music)]])" link.
[ledger #51] E3 Kümöch (Liturgical): DELETED (the survivor, D1 Kümöch Sacramental Bread, is outside E scope).
[ledger #58] E3 Treaty of Good Neighborliness (1994): Fond 108 changed to Fond 110 (Territorial Legislative Journals).
[ledger #58] E3 1995 Latin Orthography Revision: Fond 108 changed to Fond 110.
[ledger #61] E4 Sergei Voronov: Fond 312 changed to Fond 204 (Iradneft Production Association records).
[ledger #63 optional] E4 State Archives of Irad (#200, not #217 as the ledger says): added Fond 3 (Kokand charters and church records of Iyık Janyl, 1727–1876), Fond 110 (Territorial Legislative Journals), Fond 111 (Supreme Court Reports) and Fond 204 (Iradneft) to the Holdings list.
[ledger #67-local] Category header counts recounted from the `#### ` headings:
- E1 Biographies & Leadership 37 → 36 (the header was already stale).
- E2 Geography & Settlements 60 → 58.
- E3 History & Events 47 → 42.
- E3 Public Institutions & Facilities 2 → 1 (stale).
- E3 Cultural & Linguistic Terms 25 → 16.
- E3 Culture, Language & Folklore 51 → 45.
- No change in E4 or E5.

#### Deleted titles (12)
- E2: Arslanbob; Sary-Chelek
- E3: Operation Starlight (1992); Organic Act of the Territory of Irad; Bishkek Ceasefire Agreement (2007); The July 2024 Transition Crisis; Kurut (Culinary); Ak-Örgoe (Yurt Part); Tai-Kazan-Ring; Koshkar-Muyuz (Motif); Kambarkan (Music); Kümöch (Liturgical)

#### Not done or left for the lead
- Not touched, as instructed: items 43, 49, 52, 55, 56, 57, 65, 67 (the "## 5./## 6. … Entries" class totals and the article renumbering), 69.
- Links to the deleted "Sary-Chelek" are still in non-E files: A2:15, new/administrative-divisions-of-irad.md:73, new/chatkal-range.md:13. They should be repointed to `[[Sary-Chelek Biosphere Reserve|Sary-Chelek]]`.
- Article numbers in E2 and E3 now have gaps where articles were deleted (for example, E3 jumps from 197 to 200).
- Outside the ledger's scope but related to item 30: E2 Chong-Kenkol (~line 1150) and E5 Ming-Örük (~line 139) still put the Kenkol valley's exit "into the upper Talas valley" and in Talas District. Item 30 places the Kenkol in the western valley (Kara-Buura District).


### B.4 New articles

[ledger #2] operation-starlight: siege 'from 10 April to 25 May 1992' -> 'from 10 April 1992' (siege ran to 18 June)
[ledger #2] provisional-government-of-irad-1992: siege 'from 10 April to 25 May' -> 'from 10 April ... until the siege was broken in June'
[ledger #2] socialist-republic-of-irad: siege 'from 10 April to 25 May' -> 'from 10 April'
[ledger #2] territory-of-irad-1992-2006: siege 'from 10 April to 25 May' -> 'from 10 April'
[ledger #2] talas-river: 'in April and May 1992' -> 'from April 1992'
[ledger #2] communist-party-of-irad: 'in April and May' -> 'from April'
[ledger #2] socialist-republic-of-irad: 'in April and May' -> 'from April'
[ledger #3] geography-of-irad: 'refineries' -> 'refinery' (single Nurzhan Refinery No. 1)
[ledger #4] geography-of-irad: gas field 'beneath the sands north of the Chu' -> 'beneath the north-eastern Moiynkum, near the lower Chu'
[xcheck] geography-of-irad: lower Chu plain: Moiynkum 'to the north' -> 'to the west' (Moiynkum lies between the Chu and the Talas; ledger #4)
[ledger #4] energy-in-irad: gas field 'Moiynkum sands north of the Chu' -> 'north-eastern Moiynkum sands near the lower Chu'
[ledger #4] administrative-divisions-of-irad: zone table: Moiynkum placed between the Chu and the Talas, Betpak-Dala north of the Chu
[ledger #12] geography-of-irad: dropped 'since 2006' implying past WHC membership; 'not itself a State Party'
[ledger #39] sport-in-irad: softened passport claim: dropped 'issues passports to Iradi residents who apply'; athletes 'who have acquired Kazakh, Kyrgyz or Uzbek citizenship'
[ledger #40] foreign-relations-of-irad: Uzbekistan row 'electricity imports' -> 'Iradi electricity sales'
[ledger #40] irad-uzbekistan-relations: '18 percent of Iradis' -> '18 percent of Irad's population'
[ledger #46] culture-of-irad: link [[Iradi Chased Silver Bridle Plate]] -> [[Iradi Bridle Rosette]] (merged)
[ledger #47] talas-river: link [[Talas River Trout]] -> [[Iradi Mountain Trout|Talas River Trout]] (merged)
[ledger #58] democratic-republic-of-irad: citation Fond 108 -> 110 (Territorial Legislative Journals)
[ledger #58] foreign-relations-of-irad: citation Fond 108 -> 110 (Territorial Legislative Journals)
[ledger #58] irad-kazakhstan-relations: citation Fond 108 -> 110 (Territorial Legislative Journals)
[ledger #58] organic-act-of-the-territory-of-irad: citation Fond 108 -> 110 (Territorial Legislative Journals)
[ledger #58] territory-of-irad-1992-2006: citation Fond 108 -> 110 (Territorial Legislative Journals)
[ledger #59] organic-act-of-the-territory-of-irad: citation Fond 108 -> 111 (Supreme Court Reports)
[ledger #59] territory-of-irad-1992-2006: citation Fond 108 -> 111 (Supreme Court Reports)
[ledger #60] culture-of-irad: citation Fond 108 -> 175 (Ethnographic Records)
[ledger #60] iradi-cuisine: citation Fond 108 -> 175 (Ethnographic Records)
[ledger #61] energy-in-irad: citation Fond 312 -> 204 (Iradneft records)
[ledger #62] communist-party-of-irad: citation Fond 233 -> 86 (Talas City Committee)
[ledger #62] communist-party-of-irad: running text 'in Fond 233' -> 'in Fond 86'
[ledger #62] irad-kazakhstan-relations: citation Fond 412 -> 501 (ISEZ Executive Directives)
[ledger #64c] 2018-irad-census: district remainder 'about 140,000' -> 'about 125,000'
[ledger #64b] 2018-irad-census: added clause: metro/agglomeration figures are estimates outside the census
[ledger #64b] demographics-of-irad: Talas metro figure marked '(estimate)'
[ledger #64b] demographics-of-irad: Nurzhan agglomeration figure marked '(estimate)'
[ledger #64b] demographics-of-irad: added clause after city table: city figures include suburban settlements; metro/agglomeration figures are estimates outside the census
[ledger #64b] administrative-divisions-of-irad: Talas metro figure marked 'estimate'
[ledger #64b] administrative-divisions-of-irad: Nurzhan agglomeration figure marked 'estimate'
[ledger #64b] administrative-divisions-of-irad: table note: city populations are census figures, metro figures unofficial estimates
[ledger #68] cinema-of-irad: 'biannual' -> 'biennial'
[ledger #68] tourism-in-irad: 'biannual' -> 'biennial'
[xcheck] chatkal-range: smelter no longer placed at the Talas Alatau–Chatkal junction (which is at the Fergana Gateway); now 'in the Talas Alatau foothills south-west of Talas' (per ledger #32 resolution)
[xcheck] chatkal-range: smelter location: 'at the northeastern end of the range where it meets the Talas Alatau' -> 'in the Talas Alatau foothills ... take their name from the nearby range' (per ledger #32)
[xcheck] tourism-in-irad: ulak tartysh final 'on Irad Day' -> 'President's Cup, in the week of Irad Day' (matches sport-in-irad, public-holidays-in-irad)
[xcheck] elections-in-irad: results table: added running mate Tologonov to 2011 ticket (per list-of-governors-of-irad)
[xcheck] elections-in-irad: results table: added running mate Tologonov to 2015 ticket (per list-of-governors-of-irad)


## Part C. Fixes from the final independent review

A reviewer who had not seen the work read a sample of articles and audited all volumes for hidden-lore, real-person and real-company problems (`pass2/REVIEW_FINAL.md`). The main fix removed a layer of invented, attributed rumours that mapped one-to-one onto the secret lore. Item IDs refer to that review.


### C.1 Vol1 chunks, including the featured-article expansion

### REV_A: review fixes in chunks A1–A6 (Vol1 FA, 2.x, 3.1–3.28)

Source: pass2/REVIEW_FINAL.md. Backups of pre-fix files: revfix_A/A1.md … A6.md. One line per change, tagged with review item id.

#### Review items (C/S/Minor)
- [S3] A4: 3.6 Aidar Maksat lead: removed "one of the three central figures" framing; now runs government during Ruslan–Alikhan rivalry, no public claim
- [C3] A4: 3.6 Aidar Maksat: replaced Western-diplomats rumour on Chinese meetings/succession support with neutral sentence (review wording)
- [C5] A4: 3.7 Ruslan Toktarov: deleted Ruslan–Bekzatov rapprochement sentence; "Neither claim" -> "The claim has not been substantiated."
- [Minor3] A4: 3.8 Alikhan lead: "state-aligned broadcaster" -> "state broadcaster"
- [Minor2] A4: 3.8 Alikhan: birthplace Kobozev -> Talas; grew up in Talas and, from 1989, in Kobozev
- [Minor3] A4: 3.8 Alikhan: IradOne founding phrased per addendum (1993 Act); keeps "state broadcaster"
- [C2] A4: 3.8 Alikhan: deleted rumour that Alikhan tolerates Ilyasov for factional reasons
- [S6] A4: 3.8 Alikhan: digital-synthesis boilerplate reduced to one clause + link
- [S1] A4: 3.8 Alikhan: removed post-2024-election consultant-contacts rumour; replaced with review wording
- [C4] A4: 3.9 Kamran Bekzatov: removed "in 2022" and "with Russian contacts" from putsch rumour (review wording)
- [C5] A4: 3.9 Kamran Bekzatov: deleted both Bekzatov–Ruslan rapprochement sentences
- [S8] A4: 3.10 Jason Ilyasov: deleted "state-aligned broadcaster has repeatedly aired his attacks" line (rival-factions bullet kept here only, per C2)
- [S6] A3: 3.1 History: "deflect Russian and Chinese pressure" boilerplate reduced to one clause + link
- [S6] A3: 3.1 History: leaked-reports sentence reduced to one clause + link
- [S5/S6] A3: 3.1 History: 2023 protests no longer "inspired by" Ilyasov (surcharge, spontaneous); health boilerplate reduced to one clause
- [S6] A3: 3.2 Politics: deflect boilerplate and "inevitable and welcome" quote reduced to clause + links
- [S6] A3: 3.2 Politics: OSCE quotation reduced to one clause + link
- [S4] A3: 3.2 Politics: Maksat chairing cabinet dated to July 2024 (consistency with S4)
- [S6] A3: 3.2 Politics: leaked-reports paragraph reduced to one clause + link
- [S5] A3: 3.2 Politics: Ilyasov no longer said to have "prompted" the 2023 protests (review wording)
- [S6] A3: 3.2 Politics: succession-section health boilerplate reduced to one clause + link
- [Minor7] A3: 3.2 Politics ref [6]: HRW title "Divided Transoxiana" -> "Divided Irad"
- [Minor1] A3: 3.3 Boz-Korgon: clinic bullet replaced with neutral "staff accommodation and service buildings"
- [S6] A3: 3.3 Boz-Korgon: digital-synthesis boilerplate reduced to one clause + link
- [S3] A3: 3.3 Boz-Korgon: Maksat no longer listed as succession contender (consistency with S3)
- [S6] A2: 2.5 Economy: leaked-reports sentence trimmed to clause + link
- [S6] A2: 2.5 Economy: "inevitable and welcome" quote replaced with clause + link
- [Minor7] A2: 2.4 ATR ref: HRW title "Divided Transoxiana" -> "Divided Irad"
- [S5] A1: 2.1 Talas: 2023 protests attributed to surcharge, not to Ilyasov criticism
- [S5] A5: 3.13 DPI: 2023 protests no longer "inspired by" Ilyasov
- [S6] A5: 3.13 DPI: health/synthesis boilerplate reduced to one clause + link
- [S6] A5: 3.13 DPI: "inevitable and welcome" quote removed from ideology list; link kept
- [S6] A5: 3.13 DPI: leaked-reports paragraph reduced to one clause + link
- [S6] A5: 3.13 DPI: OSCE quotation reduced to clause + link
- [S9] A5: 3.19 Territorial Legislature: added current Speaker Nurbek Sultanov (DPI) since 2019 (no prior name in article)
- [Minor7] A5: HRW report title "Divided Transoxiana" -> "Divided Irad" in 3 reference lists
- [Minor3] A6: 3.26 IradOne lead: "state-owned public broadcaster" -> "state broadcaster"
- [S6] A6: 3.26 IradOne lead: synthesis boilerplate reduced to one clause + link
- [S6] A6: 3.26 IradOne: second synthesis passage trimmed to one clause + link, IradOne-specific facts kept
- [S5] A6: 3.26 IradOne: 2023 protests linked to surcharge criticism (consistency with S5)
- [Minor7] A6: 3.20 Armed Forces ref: HRW title "Divided Transoxiana" -> "Divided Irad"
- [Minor7] A4: HRW report title "Divided Transoxiana" -> "Divided Irad" (1 occurrence, 3.5 Bektur refs)

#### FA "Irad" (A1): review fixes, hatnotes and S7 expansion
- [S9] A1 FA: infobox Speaker "Kanybek Osmonov" -> "Nurbek Sultanov" (matches 3.19)
- [Minor4] A1 FA: lead: IAC acronym explained (*Iradin Azatlık Cemiyeti*)
- [S5] A1 FA: Frozen conflict: 2023 protests attributed to the municipal surcharge (review wording), not to Ilyasov
- [S7] A1 FA: ISEZ subsection: linked Ilyasov; "See also" sentence replaced by new Elections/Human rights subsections with hatnotes
- [S11] A1 FA: Heritage: UNESCO wording replaced per addendum (one property 2004; 2014 Silk Roads components)
- [S7] A1 FA: Foreign relations: "Russia receives most Iradi crude" aligned with Energy/Transport articles (refined at Shymkent or shipped on)
- [S7] A1 FA: hatnotes: Political status subsection -> Political status of Irad, Territory of Irad (1992–2006)
- [S7] A1 FA: hatnote: ISEZ subsection
- [S7] A1 FA: hatnote: ATR subsection
- [S7] A1 FA: hatnote: Energy and mining -> Energy in Irad (trailing "See" removed)
- [S7] A1 FA: Energy: removed trailing "See [[Energy in Irad]]" (now hatnote)
- [S7] A1 FA: hatnote: Agriculture and services
- [S7] A1 FA: Agriculture: removed trailing "See" (now hatnote)
- [S7] A1 FA: services: removed "Most freight… See Transport/Tourism" (now covered by new subsections with hatnotes)
- [S7] A1 FA: hatnote: Languages -> Iradi Language, Iradi alphabet
- [S7] A1 FA: hatnote: Horses
- [S7] A1 FA: Horses: removed trailing "See" (now hatnote)
- [S7] A1 FA: hatnote: Music and cinema
- [S7] A1 FA: Music: removed trailing "See" (now hatnote)
- [S7] A1 FA: Cinema: removed trailing "See" (now hatnote)
- [S7] A1 FA: hatnote: Cuisine
- [S7] A1 FA: Cuisine: removed trailing "See" (now hatnote)
- [S7] A1 FA: Politics: added "Elections" (with hatnote) and "Human rights" (with hatnote) subsections, refs [35]–[39]
- [S7] A1 FA: Military: expanded with SDC formation, conscription, budget, formations, Alatau Shield (addendum canon) and Gendarmerie structure (law enforcement); ref [40]
- [S7] A1 FA: Economy: added "Transport and communications", "Trade" (export destinations/imports), "Currency and finance", "Tourism" and "Science and technology" subsections with hatnotes where articles exist; refs [41]–[57]
- [S7] A1 FA: Demographics: "Education and health" expanded into "Education" and "Health" subsections (literacy, school system, census, universities, ATR; life expectancy, infant mortality, health system, workforce, ATR) with hatnotes; refs [58]–[64]
- [S7] A1 FA: Culture: added "Media" subsection (with hatnote) and expanded "Sport and holidays" (hatnotes; league, no NOC, holiday list); ulak final dated "in the week of Irad Day" per Sport article; refs [65]–[69]
- [S7] A1 FA: Culture: flag/anthem paragraph moved into new "National symbols" subsection with hatnotes; adoption facts added; refs [70]–[71]
- [S7] A1 FA: references: added 37 entries, cite_note-35 to cite_note-71
- [S7] A1 FA: subsection "Heritage and symbols" renamed "Heritage" (symbols moved to new "National symbols")

#### Notes
- C2: the 'rival factions … tolerate or encourage him' bullet is kept only in 3.10 Jason Ilyasov (A4); no other occurrence exists in A1–A6.
- S2, S10, C1, Minors 5, 6, 8–16 fall outside A1–A6 (Vol2/Vol3 or Vol1 3.29+) and were not touched. Minor 7 was applied to HRW reference titles inside A-files for consistency with Human rights in Irad.
- S6: full health/leaked-reports/'inevitable and welcome'/OSCE formulations kept in the FA, 2.2 Erlan Toktarov and (remarks) 3.7 Ruslan Toktarov.
- S7: FA body grew from about 5,440 to about 7,970 words (+~2,530), with 37 new references (cite_note-35 to cite_note-71); facts taken only from pass2/new articles, Vol1 3.39 Transport in Irad and existing chunks.


### C.2 Vol2 and Vol3 chunks

### REV_DE: review fixes in chunks D1–D5 (Vol2 4.1–4.100) and E1–E5 (Vol3)

Backups: revfix_DE/*.md. Scripts: revfix_DE_scripts/.

- [C1] E2 #94 Sukarne Feedlot Complex: replaced odors/runoff complaint with "Manure from the feedlot is composted and sold to farms in the Talas valley as fertilizer.<sup>[1]</sup>"; deleted ref [2] (Talas Herald 2016 'Feedlot neighbors…'); list now [1] only.
- [C2] E3 #228 2023 Student Protests in Talas: deleted the "rival factions within the ruling family had tolerated or encouraged him" clause; "either claim" -> "the claim".
- [C2] E3 same stub: "Ilyasov denies receiving money from any political patron" -> "Ilyasov says that his platform is self-funded" (canon public reality; removes patron hint).
- [S2] D3 4.46 2025 Trump Remarks on Irad, lead: quoted "explore transferring or selling Irad to Russia" -> canon paraphrase "he was reported to have said that he was exploring selling Irad to Russia to keep China from acquiring it".
- [S2] D3 4.46 "The remarks": deleted "According to reports of the briefing … strategic minerals … option to be explored" sentence; kept "Commentators in Irad and abroad noted…" and moved ref [1] onto it.
- [S6] E3 #210 2013 Constitutional Amendment (Reaction): OSCE direct quotation -> short paraphrase "criticized … for their lack of transparency and choice (see [[Elections in Irad]])".
- [S6] D3 4.43 Irad Special Economic Zone: leaked-reports sentence shortened to one clause + "(see [[Political status of Irad]])".
- [S6] D4 4.80 Nurzhan Agro-Industrial: leaked-reports sentence shortened to one clause + "(see [[Political status of Irad]])".
- [S6/Minor12] D3 4.63 Adil Toktarov: removed leaked-reports sentence (see Minor12 line).
- [S10] D5 4.94 Xinjiang Lihua Cotton Facilities: removed invented company water statement; now "ISEZ water inspectors state that withdrawals by the farms supplying the plants are monitored by the [[Chu Valley Irrigation Inspectorate]], and cotton deliveries by the [[Chui Cotton Inspection Directorate]].<sup>[3]</sup>" (merged with the preceding monitoring sentence).
- [S10] D5 4.94 ref [3] retitled: 'Inspectors outline checks on cotton farm water use.' (Talas Herald, 24 July 2021).
- [Minor5] D2 4.33 Oxus River in Iradi historiography: "Talas and the Chu end in closed basins in the Moiynkum sands" -> "Talas ends in the Moiynkum sands and the Chu near the Akzhaykyn depression on the Northern Steppe".
- [Minor6] E5 #432 Kum-Say Fan: "northern rim" -> "eastern rim"; stream now "a right-bank tributary of the [[Kara-Darya]]"; dropped the trailing "(see [[Kara-Darya]])".
- [Minor12] D3 4.63 Adil Toktarov, Public profile: removed templated succession line; now ends on business fact (Silk Road Financial Tower houses offices of the [[Irad Foreign Trade Escrow Authority]], ref [1]; consistent with 4.x IFTEA and Talasbank articles).
- [Minor12] D3 4.64 Bekzat Toktarov, Public profile: removed templated succession line; now ends "NAI's reserves at the Nurzhan Central Grain Terminal are the largest grain stocks held in the ISEZ.<sup>[1]</sup>". Timur's (4.62) closing kept.
- [Minor14] E3: {{culture-stub}} -> {{Irad-culture-stub}} (15); {{sport-stub}} -> {{Irad-sport-stub}} (1).
- [Minor14] E4: {{plant-stub}} (4) and {{tree-stub}} (1) -> {{Irad-plant-stub}}; {{craft-stub}} -> {{Irad-craft-stub}} (3); {{mammal-stub}} (2) and {{bird-stub}} (2) -> {{Irad-fauna-stub}}; {{horse-stub}} -> {{Irad-horse-stub}} (2).
- [Minor14] E5: {{geography-stub}} -> {{Irad-geo-stub}} (5); {{settlement-stub}} -> {{Irad-settlement-stub}} (16); {{mountain-stub}} -> {{Irad-mountain-stub}} (3); {{lake-stub}} -> {{Irad-lake-stub}} (2); {{river-stub}} -> {{Irad-river-stub}} (1); {{glacier-stub}} -> {{Irad-glacier-stub}} (1). All Vol3 stub templates in E1–E5 are now {{Irad-…}}; Hatnotes untouched.
- [Minor15] E5 #369 Kyzyl-Adyr Hills: reordered lead so "from which the town of [[Kyzyl-Adyr]] takes its name" follows "loess hills".
- [C3/C4/C5/S1/S3 sweep] Grepped D1–D5, E1–E5 for Maksat–China succession support, Bekzatov putsch "in 2022"/"Russian contacts", Ruslan–Bekzatov rapprochement, Alikhan–Washington/consultant contacts, Maksat as contender, "state-aligned broadcaster": no occurrences. Existing D3 4.50 crisis-article lines (Maksat "no public claim to the succession"; Bekzatov putsch "palace intrigue … fairy tales"; Alikhan "no political links … substantiated") are canon-compliant; no change.
- [S6 check] Crisis article (D3 4.50) health/"guests…" text left in full as permitted. No "inevitable and welcome" or digital-synthesis boilerplate elsewhere in D/E.
- [Verify] Per-article check: every <sup>[n]</sup> marker in D1–E5 matches its references list (0 mismatches); line counts unchanged except E2 (−1, deleted ref).
- [review follow-up] D3 4.46 2025 Trump Remarks on Irad: deleted the bullet saying Alikhan's Western-leaning image 'became a political liability' (echoes covert lore; ref [1] still cited elsewhere in the article).


### C.3 New articles

### REV_N: review fixes in pass2/new/*.md (backup: revfix_N/)

- [C3] irad-china-relations.md: Politics. Replaced the "Western diplomats … build outside support during the succession contest" rumour and the office denial with the review's sentence (Maksat receives delegations, including Chinese investors; pro-business technocrat; link to the 2024 crisis article).
- [C4] irad-russia-relations.md: Russo faction. Changed "in 2023 … in 2022 … armed move … with Russian contacts" to "These commentators and anonymous social-media channels have periodically circulated claims that he plotted against the DPI leadership." Kept the following denial ("fairy tales") sentence.
- [S2] irad-russia-relations.md: Replaced the quoted Trump words with the canon paraphrase "said that he was exploring selling Irad to Russia to keep China from acquiring it".
- [S2] irad-united-states-relations.md: The same quote-to-paraphrase change.
- [S2] irad-china-relations.md: Changed the unquoted "should explore transferring or selling" to the canon paraphrase.
- [S4] foreign-relations-of-irad.md: Changed "since 2019 most dealings … Lieutenant Governor, who chairs the cabinet" to "the Lieutenant Governor has led most commercial negotiations since 2019, and since July 2024 he has also chaired the cabinet and received foreign delegations."
- [S6] irad-russia-relations.md: Deleted the leaked-US-intelligence paragraph (Public opinion) and the ref [14] it alone used. The ref was last in the list, so nothing was renumbered.
- [S6] irad-russia-relations.md: Cut the digital-synthesis boilerplate to "recorded addresses … the subject of authenticity claims that officials reject (see [[2024 Iradi Executive Transition Crisis]])". Kept the point specific to this article: the foreign-sponsorship charge is read as aimed at Russia.
- [S6] irad-china-relations.md: Deleted the leaked-reports sentence and the repeat of "inevitable and welcome" in Politics. Kept the specific point (reliance on US forces at Talas Air Base; Chinese investment has not extended to security). The quote stays once, in the lead.
- [S6] foreign-relations-of-irad.md: China section. Replaced the "inevitable and welcome" quote and the leaked-reports sentences with "Toktarov has publicly welcomed closer alignment with China, while the ISEZ continues to rely on the United States for its security."
- [S6] foreign-relations-of-irad.md: OSCE bullet. Replaced the quotation with "have criticized those held since the 2013 removal of term limits (see [[Elections in Irad]])".
- [S6] media-of-irad.md: Press freedom section. Cut the digital-synthesis/disinformation boilerplate to a short authenticity-claims clause with a link to the crisis article. Kept the details specific to IradOne (released only through IradOne, no journalists at recordings). Reworded the follow-on "disinformation label" sentence and removed the duplicate crisis link.
- [S6] human-rights-in-irad.md: Cut the ~120-word Ruslan remarks paragraph to two sentences plus "(see [[Ruslan Toktarov]])".
- [S6] human-rights-in-irad.md: Removed the OSCE quotation and kept the substance ("The OSCE has criticized … citing …").
- [S6] political-status-of-irad.md: Kept the full leaked-reports formulation. Shortened the trailing "inevitable and welcome" quote to "publicly welcomed closer alignment with China".
- [S6] irad-united-states-relations.md: Cut the leaked-reports sentence ("neopatrimonial regime … personality cult … concluded …") to a short clause plus "(see [[Political status of Irad]])".
- [S6] 2023-iradi-gubernatorial-election.md: Replaced the OSCE quotation with "repeated its criticism … (see [[Elections in Irad]])". Cut the digital-synthesis sentence to the short authenticity-claims clause plus a link.
- [S6] elective-governor-acts-1992.md: Cut the digital-synthesis sentence to the short authenticity-claims clause plus a link.
- [S6] list-of-governors-of-irad.md: The same change. The existing crisis link was kept.
- [S6] islam-in-irad.md: Cut the Ruslan remarks paragraph to two sentences plus "(see [[Ruslan Toktarov]])". Kept the horsemeat point, which belongs to this article.
- [S6] religion-in-irad.md: Cut the Ruslan remarks passage to one clause plus "(see [[Islam in Irad]])".
- [S6] irad-uzbekistan-relations.md: Shortened the Ruslan remarks to one sentence. Kept the analysts' point about the Muslim-majority neighbors.
- [S6 note] elections-in-irad.md: Kept the OSCE quotation in the lead as the single canonical occurrence among the new articles. The other articles now link here.
- [S8] media-of-irad.md: Replaced "Commentators have noted the unusual sight of a state-aligned broadcaster airing such attacks." with "…but has continued to book him despite these attacks." (the review's sentence, adapted for flow).
- [S8/C2] media-of-irad.md: Removed the clause "some opposition outlets have suggested that rival factions within the ruling family tolerate him to damage their opponents", and changed "either claim" to "the claim".
- [S10] irad-china-relations.md: Replaced the invented Lihua company statement with "ISEZ water inspectors state that withdrawals by farms supplying the plants are monitored by the [[Chu Valley Irrigation Inspectorate]]." Ref [7] (an EPQ academic article) was kept, since it supports the concerns sentence.
- [Minor 3] media-of-irad.md: Lead. Changed "the state-owned public broadcaster" to "the state broadcaster".
- [Minor 3] human-rights-in-irad.md: Changed "IradOne, the largest broadcaster" to "the state broadcaster".
- [Minor 3] elections-in-irad.md: Changed "IradOne, the largest broadcaster" to "the state broadcaster".
- [Minor 7] Retitled the HRW report "…Divided Transoxiana" to "…Divided Irad" in six files: human-rights-in-irad, bishkek-ceasefire-agreement-2007, elections-in-irad, islam-in-irad, list-of-governors-of-irad and religion-in-irad.
- [Minor 8] human-rights-in-irad.md: Added "which the authorities allowed to proceed without dispersal" to the 2025 demonstrations contrast, and split the sentence so the antecedent is clear.
- [Minor 9] political-status-of-irad.md: Changed "as UN records put it, at US insistence: …" to "remained listed (contemporary sources say 'by US demand'), and the United States neither reports … nor has asked for its removal."
- [Minor 10] political-status-of-irad.md: Renumbered all 16 references by order of first appearance, updating both the markers and the list. Old→new: 1→1, 2→2, 5→3, 9→4, 3→5, 7→6, 14→7, 4→8, 13→9, 8→10, 6→11, 11→12, 16→13, 10→14, 15→15, 12→16.
- [Minor 11] irad-china-relations.md: Kept 13,800 t, the same figure as the chunk article D4. Added the hedge "which would make Irad one of the largest producers after China, a figure independent estimates put lower".
- [S1 sweep] irad-united-states-relations.md: Deleted "Analysts noted that the Western-leaning public image of [[Alikhan Toktarov]] became a political liability". It echoes the covert "political liability" line about Alikhan and Washington.
- [C3/S3 sweep] media-of-irad.md: Exile media. Dropped "and the control of state broadcasting during the Governor's absence" from the reported Alikhan–Maksat disputes. It hinted at who controls the Governor's broadcasts.
- [Sweep, no change] I grepped all new/*.md for the Alikhan–Ilyasov, Maksat–China succession support, Bekzatov putsch (2022 / Russian contacts), Ruslan–Bekzatov rapprochement, Alikhan–American consultants and Maksat-as-contender patterns. No other occurrences were found. Ref integrity was checked on all 59 files: every marker matches a list entry, and every file still starts with "### NEW.".


## Part D. Volume 1 (FA, GA, B-class): per-article edits


### Chunk A1

### Changelog: chunk A1 (Vol1 header, Country Overview, FA "Irad", GA 2.1–2.3)

##### Country Overview: Republic of Irad (Vol1, infobox)
- Anthem "Tien Shan Tulparı" → "The Spirit of Irad" — [CANON] brief §2.
- Legislature "Supreme Council (Mejlis)" → "Territorial Legislature of Irad (Mejlis)"; added "Judiciary: Supreme Court of Irad" — [CANON] brief §2.
- Removed Russian from official languages; added "Lingua franca: Russian (not an official language since 1992)"; official languages labelled "(ISEZ)" — [CANON].
- Religion line "46.2% Sunni Islam, 38.4% Syro-Iradi Catholic, 10.8% Orthodox, 4.6% Other (2023)" → 2018 estimates 78% Christian / 18% Muslim / 4% other — [CANON] brief §2.
- Government "Dominant-party presidential republic / Autonomous tribal federalism" → "Devolved dominant-party governorate (ISEZ) with Autonomous Tribal Regions" — [CANON].
- Governor line: removed "(in health seclusion; State Council governing)"; now "(DPI; not seen in public since July 2024)" — [CANON]; no State Council exists in canon.
- GDP relabelled from PPP to nominal (2024 ISEZ official estimate); added PPP c. $50 billion — [CANON] brief §2.
- Header: removed "Territory of Irad (US Statutory)" (Irad is no longer a US territory); added "Also known as: Iradistan".
- Population reordered (official census first, independent estimate with 5.8–6.5 million range); density given on both bases (23.5 and c. 31.5/km²) — [CANON].
- Added Status, Ethnic groups, Formation dates (1925–2007), ISEZ/ATR area split, date format — standard infobox fields from canon.
- Calling code (+996-39 is Kyrgyzstan's, +1-671 is Guam's), ISO "IRD" and TLD ".ir.ad / .id.gov" (collide with Iran, Andorra, Indonesia) replaced by neutral "—"; lines kept — flagged for owner in notes.
- Kept "Legislative Speaker: Kanybek Osmonov" (non-canon; flagged in notes).

##### Irad (Vol1, FA)
- [EXPANDED] Rebuilt from ~2,750 words to ~4,950 words of prose (~5,400 with tables and lists), in a structure modelled on the Kyrgyzstan article: 4-paragraph lead; Etymology; History in 11 subsections through 2025; Geography (footprint, terrain and climate, hydrology incl. Toktogul and the Naryn cascade); Politics and government (political status, ISEZ, ATR, unification); Foreign relations; Military; Administrative divisions (table); Economy (energy and mining; agriculture and services); Demographics (population and census controversy, ethnic groups, languages, religion, education and health); Culture (horses, music and cinema, cuisine, sport and holidays, heritage and symbols); See also. Added "Main article" links to §10 titles.
- [CANON] Borders: removed "contested de jure by its four post-Soviet neighbours"; three neighbours, no border with Tajikistan, China or Afghanistan; doubly landlocked; footprint per brief §3 (Talas valley, Chatkal/Toktogul/Naryn, rural Fergana rim, lower Chu, Moiynkum, Betpak-Dala, Karatau), with Shymkent, Turkistan, Bishkek, Issyk-Kul and Fergana cities outside.
- [CANON] Lat/long box 40–44°N, 69–76°E → roughly 40°40′–46°N, 68–75°E to cover the northern steppe footprint; removed Transoxiana-with-Oxus framing (Irad does not reach the Oxus).
- Hydrology: removed claim that waters end in Lake Balkhash (the Chu and Talas do not reach it); added Talas, Chu and Naryn endpoints; Toktogul split control and Naryn Water and Power Protocol — [CANON] newlore.
- [CANON] Botai: domestication now presented as national belief, with Botai sites in northern Kazakhstan and post-2021 genetics (Botai horses ancestral to Przewalski's); removed "widely credited with the earliest domestication".
- [CANON] Antiquity chronology: Sogdians "first millennium BCE, attested by the Achaemenid period"; Alexander into Sogdiana 329 BCE; Saka moved south 140s–130s BCE; Zhang Qian c. 128 BCE; War of the Heavenly Horses 104–101 BCE; Timurid period ended 1507; "Khanate of Bukhara".
- [CANON] Kokand: conquest credited to Skobelev (1876), Chernyayev to Tashkent (1865); Iradi lands divided among Syr-Darya, Semirechye and Fergana oblasts (was Fergana only).
- [CANON] 1918: removed "aided the Bolsheviks against White forces in Kokand"; now Red Guards crushing the Kokand Autonomy (Feb 1918) and Iradi volunteers on the Transcaspian front against the White Transcaspian government and its small British force (1918–19).
- [CANON] 1931 union with Rome under *Orientalis Stella*, negotiated secretly by Mar Timotheos Alimbekov through nuncios abroad, and Soviet suspicion feeding 1930s repression and the 1937 purges.
- [CANON] Kobozev founded 1927 as ISSR capital; renamed Nurzhan by Alimbekov after the First Civil War ended in 1992.
- [CANON] 1956 Talas riots: widow's horse as popular account; housing, wages and ethnic grievances added; figures hedged.
- [CANON] 1991–92: independence declared by the Communist Party of Irad (was "Supreme Soviet"); SRI based in Kobozev; Winter Uprising 1991–92; Irad Day; treaty signed and ratified June 2; US control by Aug 18; Organic Act.
- [CANON] 2006–07 timeline corrected per brief §4: privatization scandals Jan–Feb 2007; ISEZ proclaimed from Nurzhan on Feb 25, 2007 as start of the Second Civil War, with the DRI cabinet as rival; Popular Front formed March 2007; storming of Talas June 4; DPI takeover of cities in summer; Bishkek Ceasefire Sept 2007; UNMI Oct 18, 2007 (no resolution number). The old text placed the ISEZ's creation after the storming of Talas.
- [CANON] Added 2008–2025: referendum proposal, 2011 talks collapse, 2013 term-limit amendment, elections 2011/2015/2019/2023 with OSCE quote, Maksat (Nov 2019), Boz-Korgon as independent reporting with official line, 2023 student protests, July 2024 disappearance with DPI line and attributed digital-synthesis allegations, Ruslan–Alikhan friction, 2025 Trump remarks, election due late 2027.
- [CANON] Politics: removed "devolved one-party presidential regime"; added NSGT listing, US non-notification and non-reporting, 26 recognitions and "partially recognized", "suspended sovereignty", claimant states, US basing under the 2001 agreement; leaked US intelligence reports attributed.
- [CANON] Demographics: removed "actual population", "suppressed official census", "satellite surveillance analysis, exposing ... a deliberate statistical undercount" and "ATR ... house over 3.5 million"; replaced with official figure vs independent estimates and the enumeration/estimation explanation (satellite mapping "supports", not "proves"); American share caveat added.
- [CANON] Languages: "Sogdic roots strictly and exclusively reserved" → liturgical vocabulary draws on Sogdian and Iranian roots; script history with 1995/1997 revisions.
- Economy: antimony moved from "eastern highlands" to Sary-Bulak/Chatkal; Northern Export Feeder to Shymkent, no southern pipeline, CNPC route via Kyrgyz territory; GDP nominal with PPP and per-capita on both population bases; Chevron and Xinjiang Lihua kept to existing canon only.
- [CANON] Culture: horsemeat taboo recast (popular prejudice vs ethnographers' view; removed all-caps "STRICTLY FORBIDDEN"); bovine omens via Morkhan with beef irony; *Swift Hooves* framed per §5; UNESCO sites per §5; Kok-Tash CIA involvement as unconfirmed allegation; cuisine from newlore; national symbols added.
- Etymology: canon kept; Bar Hebraeus attestation now cited to an in-world source (brief §7); list formatting fixed.
- References rebuilt (14 → 34): real works only for general regional history; Irad-specific claims to in-world sources; removed page/volume precision from real documents (Bar Hebraeus, Annuario Pontificio, State Department Dispatch); replaced "Ethnomusicology Journal" (real journal, Irad-specific claim) with Talas State University Press.
- Removed puffery ("vital equestrian traditions", "avant-garde masterworks", "enduring international cult followings", "unique", "massive"); fixed crammed one-paragraph lists.
- Heading scheme normalized to `## Section` / `#### Subsection` (brief §8).

##### Talas (Vol1, 2.1)
- [EXPANDED] ~1,150 → ~1,620 words; history split into six subsections; added Government and administration, Demographics and Transport sections.
- [CANON] "historically known in Sogdian as Taraz" → Iradi historiography identifies Talas with the medieval town known as Talas or Taraz; "scales" etymology presented as popular and uncertain; *Daluosi* attributed to Tang (not Han) sources.
- [CANON] Russian conquest: removed "Chernyayev captured the fortress in 1876"; Russian occupation of the valley in the 1860s, khanate conquered by Skobelev in 1876, Syr-Darya Oblast.
- Battle of 751: site marked uncertain; papermaking story marked disputed; removed overstated "ending imperial Chinese westward expansion".
- [CANON] 1956 riots per §5 (popular account, underlying causes, hedged figures; removed "over 3,000 residents" and "Soviet motorized divisions" as fact).
- [CANON] Removed omniscient claim that Toktarov "quietly relocated" power after "security vulnerabilities in late 2022"; now independent reporting plus the government's position, in body and lead.
- [CANON] 2006–07 sequence corrected (DRI proclaimed in Talas; rival cabinet until June 4 storming; DPI takeover in summer).
- Elevation 850 m → about 1,250 m to match 42°31′N 72°14′E; climate harmonized with the FA (July highs ~30 °C, ~300 mm); kept Köppen BSk.
- Added 1952 Soviet interceptor base, March of the Thousand Saddles, territorial-capital institutions, 2023 student protests, 2025 protests, Government House, State Archives, Shelji silver, Talas District/Kara-Buura context, suffragan eparchy, Talas Symphony Orchestra; distinguished the annual Diz Film Festival from the biannual Talas International Film Festival.
- "Generates more than 45% of non-oil GDP" attributed to the Chamber of Commerce and Industry.
- References rebuilt (13 → 15); old citations did not match claims (e.g., Hopkirk for 2018 population, KazTransOil for Nuevo Talas); removed fictitious UNECE "Central Asian Water Authority" report.
- Removed puffery ("extraordinary cultural and economic crossroads", "towering", "bustling", "massive", "world-renowned", "prestigious", "financial engine"); removed non-lead bolding.

##### Erlan Toktarov (Vol1, 2.2)
- [EXPANDED] ~920 → ~1,430 words; added Unification and foreign policy, Family, election table; expanded the Boz-Korgon section.
- [CANON] Hidden-lore: removed "allege he suffered a severe stroke" from the lead; removed the opposition claim that Zara "tightly restricts all physical access to him" (now: unverified tabloid reports of family tensions over access to the estate; Zara described as a non-political Stanford doctoral candidate living mostly abroad); replaced "succession struggle among his five sons and his daughter Zara" with the publicly visible Ruslan–Alikhan friction.
- [CANON] Chronology corrected: the ISEZ was proclaimed from Nurzhan on Feb 25, 2007, before the June 4 storming of Talas (old text had it after the DRI's dissolution).
- [CANON] Removed "centralized presidential regime", "supreme leader", "appointing himself Governor under a status of suspended territoriality"; now chairman of the DPI, took office as Governor in 2007.
- [CANON] 2013 change described as an amendment to the 1992 Elective Governor Acts (link to [[2013 Constitutional Amendment]] kept); election years 2011/2015/2019/2023 confirmed with OSCE quote; next election due late 2027.
- Fixed geographic error "confluence of the Chu and Talas rivers" (the rivers do not meet) → "Chu lowlands"; birth details attributed to the official biography.
- Fuel and warehousing concessions attributed to critics; leaked US intelligence reports attributed; removed "statesman, political strongman", "adroitly", "pivotal", "regal", "omnipresent".
- References rebuilt (13 → 10, now matching claims); "Department of Public Information (Boz-Korgon)" → "(Talas)" to avoid asserting the contested executive seat.

##### Syro-Iradi Catholic Church (Vol1, 2.3)
- [CANON] 1931 union framed per brief: secret negotiations by Mar Timotheos Alimbekov through nuncios abroad; Soviet suspicion of the Catholic link fed 1930s repression and the 1937 purges; added survival underground and post-1992 revival.
- [CANON] "approximately 75% of the Iradi population ... over 3.4 million faithful" → 78% of Iradis Christian (2018), most of them in this church; 3.4 million attributed to the church's own figures.
- St. names: "Cathedral Church of Saint Janyl" → "Church of St. Janyl"; "Order of Saint Janyl the Hermit" → "Order of St. Janyl the Hermit"; "seminary of Saint Ephrem" → "St. Ephrem Major Seminary"; link titles ("Church of Saint Janyl", "Feast of Saint Janyl") left unchanged.
- Fixed contradiction "leavened unleavened flatbread" → unleavened *kümöch*.
- Removed incorrect examples of "Sogdic roots" (*kuble*, *iyık* are not Sogdian); restated the canon in general terms.
- Merged the duplicated liturgy sections ("Liturgy and Practices" and "Liturgical Traditions, Calendar, and Mountain Customs") into one "Liturgy and practice" section; normalized headings.
- Removed "the DPI administration in [[Boz-Korgon]]" (contradicts the official seat); "robust legal protections ... reaffirmed in the Alimbekov-Baker Treaty" → the church cites territorial-era guarantees.
- Added Organization details from related articles (Episcopal Synod, Archbishop Mar Ephrem since 2012), Father Luka Ayyubov's 1994 New Testament, UNESCO inscription, tribal syncretism.
- Added inline citations (previously none); removed page numbers from the Annuario Pontificio; dropped the Bar Hebraeus citation.
- Removed puffery ("irreplaceable repository", "living testament", "found nowhere else in global Catholicism", "robust").

Untouched: Vol1 header paragraph and section headers (no changes needed). No articles merged or deleted.


### Chunk A2

### Changelog: chunk A2 (Vol1 GA 2.4–2.7)

General (all four articles): normalized headings to `### n.n. Title` / `## Section` / `#### Subsection`. Former `###` sub-sections became `##` and `####`, so no unnumbered `###` headings remain. Merged the duplicated second halves (the appended `##` sections repeated the first halves). Converted run-on pseudo-lists ("- **A**: … - **B**: …" in one paragraph) into real lists, and removed bold everywhere except the lead title term. Added `<sup>[n]</sup>` markers (none existed before) matched to sequential reference lists. Assessment lines unchanged.

##### Autonomous Tribal Regions (Vol1, 2.4)
- **[EXPANDED]** Rebuilt as a single article: lead; Geography; History (Before 2007 / Second Civil War and partition / Since 2007); Government and politics (Clans / Kurultai and IAC / Customary law); Security; Population and society; Economy; Relations with the ISEZ and the UN; Humanitarian situation. These cover the governance, clans, economy, ISEZ/UN relations and humanitarian sections asked for.
- **[CANON]** Rewrote the geography to match the footprint (Betpak-Dala and Moiynkum, Karatau, Talas Alatau, Chatkal, Toktogul–Naryn, Fergana Rim). This replaces the "eastern Tian Shan alpine plateaus plus Kyzylkum steppe" framing. Most of the area is now described as steppe and desert rangeland, with the population in the valleys.
- **[CANON]** Added the six UNMI/aid-agency planning zones, each with a short description and the real features inside it (Aksu-Zhabagly, Sary-Chelek, Arslanbob, Kanysh-Kiya, Terek-Sai, Bazar-Korgon).
- **[CANON]** Placed the Toktogul dam on the tribal side of the Qara-Chik line, and explained the split control and the Naryn Water and Power Protocol (elders' drawdown veto, 2027 renewal).
- **[CANON]** Population: replaced "intentionally suppressed … until independent satellite and housing surveys revealed" with the brief's framing. The DPI census estimated rather than counted the ATR, at about 2.2 million (48% of 4,626,000), and independent estimates run from 3.5 to 4 million. Satellite mapping and aid registries now "support" the higher figure rather than "prove" it. The IAC's allegation that the undercount was deliberate is set against the DPI's line.
- **[CANON]** Hidden-lore leak: the Cold War CIA conversion of the Kok-Tash Kariz was stated as fact. It is now an unconfirmed allegation by some historians that the US has never acknowledged. Militia and smuggler use of the Kariz is attributed to UNMI reporting and ISEZ officials.
- Clan names: checked that Sarybagysh and Naiman read naturally now that the "-Irad" suffix is gone. Added that these names are shared with Kyrgyz and Kazakh groupings, and the Naiman link to the medieval Christian confederation. Dropped "paramount" and "northern" for the Tanıp (other articles disagree on its homeland). Added the Karakoyun homeland (Kara-Koyun Valley). No new clan names were invented.
- Added the 2007 chronology required by brief §4 (Feb 25, March, June 4, summer withdrawal, September ceasefire, Oct 18 UNMI), plus 2008, 2011, 2018, 2021, July 2024 and 2025 events. Each links to an existing article.
- Removed "commanded by veteran district captains", since the ATR has no districts. Cut puffery: "unbreachable", "vital", "perfected over several millennia", "optimal thermal insulation", "revered", "vigorously".
- References:
  - "ATR Council Press, Boz-Korgon" became "Iradi Freedom Society Chancellery" with no place, because Boz-Korgon is the DPI compound.
  - Removed the uncited Royal Geographical Society (1904) real-journal citation.
  - Changed the Folklore Society publisher from Academic Press, a real imprint, to Talas State University Press.
  - Added in-world sources: UNMI 2024 report, *Central Asian Geopolitical Review* census study, DPI census methodology, *Eurasian Political Quarterly* on Toktogul, and the Luka Mission report.

##### Economy of Irad (Vol1, 2.5)
- **[EXPANDED]** Rebuilt as a full country-economy article:
  - lead (GDP, PPP, per capita on both population bases, data caveats);
  - History (Soviet period; collapse 1991–92; territorial dollarization 1992–2006; since 2007);
  - Sectors (Energy, covering oil, gas and electricity; Mining and metallurgy; Agriculture; Manufacturing; Services, finance and transport; United States military presence);
  - Currency and banking; Trade and transit; Labor and inequality (ISEZ vs ATR, migration, remittances); Public finance; Major companies; Challenges.
- **[CANON]** GDP "$18.4 billion USD (2018)" became nominal $18.4 billion (2024, ISEZ estimate), with about $50 billion PPP. Per capita is given as about $4,000 on the official population and about $3,000 on 6.2 million.
- **[CANON]** Oil route: "north through Kazakhstan into the Russian pipeline network" became the 85-km Northern Export Feeder (operated by the Iradi Petroleum Transit Consortium) into the Kazakh trunk network near Shymkent, for refining there or onward shipment to Russia. Stated that there is no southern export pipeline and no CPC link. The 120,000 bpd figure is attributed to NurGaz, with lower independent estimates. KazTransOil is cited.
- **[CANON]** Antimony: removed the "eastern mountain ranges" and "eastern foothills" placement and the "world's leading suppliers" puffery. Now: about 7% of reserves, mined at Sary-Bulak and smelted at Chatkal, both in the ISEZ's Sary-Bulak District, with exports by rail through Kazakhstan to China.
- **[CANON]** Expanded hydropower: Toktogul's 1,200 MW, net exports to Uzbekistan and Kazakhstan, split control, the unpublished revenue formula, and its use as leverage against transit restrictions. Added minor sources (Kara-Suu, Talas Solar Park).
- NAFTA: "Capitalizing on NAFTA-era duty-free access" became a modest framing. Commentators call the boom "NAFTA-era"; Irad was not a signatory, and its duty-free access came from its territorial status.
- Real companies:
  - Trimmed Xinjiang Lihua to existing canon (concerns over water-regulation compliance and depletion). "Soil salinization" was attributed to the company; it is now a general sector problem.
  - Chevron's post-2021 scale-back is stated neutrally, per canon.
  - Sukarne and Conagra are described neutrally. Dropped "one of Eurasia's largest automated feedlots" and "giant".
- Cotton and water: located cotton production (Fergana Rim, Lower Naryn, smaller areas in the lower Talas and Chu), covered water use, droughts, salinization and downstream friction, and linked the Xinjiang Lihua article.
- US basing: the $450 million estimate is attributed to the Chamber of Commerce. Added that the post-2007 terms are unpublished, plus public criticism after the 2025 remarks (canon only).
- Dual currency: rewritten around the 1993 Banking and Commercial Currency Act, the uses of the som and the dollar, the limits on monetary policy, correspondent banking, SMS payments and microfinance.
- Added labor migration and remittances, hedged: seasonal migration from the ATR to southern Kazakhstan, a smaller urban emigration to the US, and remittances of 5–8% of GDP as an independent estimate.
- Added the Morkhan bovine-omen irony, attributed to commentators, and linked the horsemeat taboo instead of restating "absolute, sacred prohibition".
- The family business holdings (middle sons, Alikhan) are those listed as public in brief §6. The "neopatrimonial" description is attributed to leaked US intelligence reports.
- Fixed broken links:
  - `[[Talasbank (Bank of Talas)]]` became `[[Talasbank]]`, since the Vol3 copy is being deleted under §11.
  - `[[Sary-Bulak Antimony Works (SBAW)]]` became `[[Sary-Bulak Antimony Works]]`.
  - `[[Iradi Som]]` became `[[Iradi som]]`, the §10 title.
- The major-companies list is now a real numbered list with descriptions aligned to newlore.
- Removed puffery: "iconic", "highly lucrative", "regal", "extraordinary mineral wealth", "indispensable", "profound structural modernization", "pivotal".
- References: added the DPI 2024 indicators, NurGaz annual review, *Central Asian Geopolitical Review* on base spending, *Talas Herald*, and the 1993 Act. Kept the USGS, World Bank, FAO, EDB, Chamber and KazTransOil sources.

##### First Iradi Civil War (Vol1, 2.6)
- **[EXPANDED]** Wrote a full course-of-war narrative: Opening phase (March 1992); Siege of Talas (April–May); the Alimbekov–Baker Treaty; Operation Starlight (June–August). Added sections on Casualties and humanitarian impact, International reaction (neighbors, Russia, UN, US public / Iradimania) and Aftermath and legacy. Added a hatnote to the Second Civil War.
- **[MERGED]** (within the article) Folded the duplicated second half ("Operational Campaigns…", "Foreign Military Intervention…", "Historical Legacy…") into the narrative.
- **[CANON]** Resolved internal contradictions. Starlight start date (June 6 vs June 18): first Marines landed June 6, and the siege was broken by June 18 as 10th Mountain Division units arrived. Units (Marines/10th Mountain vs 82nd Airborne): dropped the 82nd, per baselore.
- **[CANON]** Removed "complete annexation" and "the United States Congress ratified the treaty". The treaty was signed and ratified by the Provisional Government on June 2, and Irad became an organized, unincorporated territory under the Organic Act on August 18.
- **[CANON]** Aligned the Winter Uprising chronology with the Winter Uprising article: Jan 14 depot strike, Feb 3 shooting (casualties hedged), Feb 18 March of the Thousand Saddles, SRI exit in late February, Mar 11 Town Hall Meeting (Irad Day). Removed "within three days … formed the Provisional Government".
- Kept the SRI based in Kobozev. "Kobozev" is used only for 1992 and earlier, and the renaming to Nurzhan by Alimbekov after the war is added with the newlore quote.
- Plausibility: removed "carrier-based aviation from the Indian Ocean". Softened Baker "flew into the besieged city under emergency escort" to the existing canon of the treaty being signed in Talas. No new actions or quotes for real people. Replaced the non-canon "Office of the US High Commissioner" with an interim US administration pending territorial elections.
- Casualties hedged: about 14,000 is the most-cited figure (Provisional and early territorial records), with independent estimates of about 9,000 to more than 20,000.
- Added actors from existing biographies: Chernov, Toktarov (supply lines), Bektur Zhumabek uulu (aged 23, mounted scouts), Kuban Mamytov, Colonel David Sterling. Linked the Battle of Kobozev Railhead, with its 18-tank claim attributed to Iradi accounts.
- International reaction kept modest: the neighbors cited CIS border inviolability and closed borders; Russia protested but did not intervene and received Chernov; the Security Council held consultations without a resolution; Irad was listed as a non-self-governing territory in 1992. No resolution numbers or quotes.
- References: removed Pierce (1960) and Hopkirk (1992), which cover 1867–1917 and the Great Game rather than 1992. Added the Alimbekov and Chernov memoirs, a *Central Asian Geopolitical Review* casualty study and a Talas State University documentary history. Removed puffery: "historic", "unprecedented", "catastrophic", "crucible", "decisively".

##### Iradi Equestrian Culture & Breeds (Vol1, 2.7)
- **[CANON]** Botai: removed "Archeologically identified as part of the geographic cradle … Bronze Age Botai" and the claim that Chu/Talas excavations "demonstrate" Botai domestication. Botai is now a national belief: the sites are in northern Kazakhstan, and Iradi attributions are not accepted abroad. Ancient-DNA studies (2018, 2021) show Botai horses were ancestral to Przewalski's horses, and the 2021 study traced modern domestic horses to the lower Volga–Don. Also fixed "Bronze Age" to Eneolithic.
- **[CANON]** Dayuan chronology: Saka moved south around the 140s–130s BCE, Zhang Qian visited around 128 BCE, and the War of the Heavenly Horses ran 104–101 BCE (was "expeditions … in 104 BCE"). Added the *Shiji* horse numbers. The Akyel's Dayuan descent is framed as breed tradition.
- **[CANON]** Horsemeat taboo: the "Muslim practice" view is presented as a popular prejudice. Ethnographers note that it ignores Kazakh and Kyrgyz practice and trace it to Christian identity-marking. Removed the "sacred, uncompromising … anthropologists trace" framing as fact.
- Merged the two duplicated sports sections into one list. Fixed "Independence Day Cup … 40,000 spectators": the Hippodrome seats about 25,000.
- Removed "unbroken five-thousand-year lineage" as fact. Akyel: "shares genetic markers with Akhal-Teke and Arabian" became "breed associations describe it as related to the Akhal-Teke". Height aligned with the Akyel Horse article (15.0–15.3 hh). The revival is placed with the 1995 Syndicate and Toktarov's State Stud (consistent with the Toktarov GA).
- Added a History section (prehistory, Dayuan, Christian and medieval, Soviet and modern) and a Breeding industry section. The 1956 riots are given as "according to popular accounts".
- References:
  - Replaced the *Journal of Equine Science* (2022) citation, a real journal carrying an invented Irad-specific article, with Talas Veterinary Research Center.
  - Replaced the "International Studbook Federation / Newmarket Press" citation with the Chongtor Studbook Registry and Syndicate.
  - Added Outram et al. 2009, Gaunitz et al. 2018, Librado et al. 2021 and Sima Qian (Watson translation), plus in-world ethnography and Directorate rules.
  - Dropped the unverified page range for Anthony (2007).

Untouched articles: none (all four articles in the chunk were edited).


### Chunk A3

### Changelog: chunk A3 (Vol1, articles 3.1–3.4)

General (all four articles): sections now use `## Section` with `#### Subsection`. No non-article `###` headings remain, so the only `###` lines in the chunk are the four article headings. Every article now has inline `<sup>[n]</sup>` markers matching its `<ol class="references">` list; the History article previously had none. Crammed one-line "- A - B - C" lists became real Markdown lists or tables.

##### History of Irad (Vol1, 3.1)
- **[EXPANDED]** Rewrote the article as a full national history, from about 1,300 words in 8 thin sections to about 6,200 words. New period sections: Prehistory; Sogdians and classical antiquity; Turkic khaganates, Islam and Christianity; Mongol, Timurid and Bukharan rule; Khanate of Kokand; Russian conquest and imperial rule (including the 1916 revolt and the Urkun); Revolution and Civil War 1917–1920; the Soviet era (korenizatsiia, collectivization, the 1931 union and purges, the Koryo-saram, WWII, oil and industry, the 1956 riots, late Soviet); Independence and the First Civil War; the territorial period; Withdrawal, DRI and Second Civil War; the frozen conflict 2007–present. Also added Historiography and See also sections. — Brief asked for a 4,000–6,000-word national history.
- **[CANON]** Botai: removed the claim, stated as fact, of Botai horse-bone finds "along the Talas foothills". Now presented as Iradi national belief, noting the main sites are in northern Kazakhstan and that genetic work (2021) shows Botai horses were ancestral to Przewalski's horses, not modern domestic horses. — §5 Botai.
- **[CANON]** Saka/Yuezhi/Dayuan: replaced "around 145 BCE Saka and Yuezhi invaded" with the Saka moving south under Yuezhi pressure in the 140s–130s BCE, Zhang Qian c. 128 BCE, and the War of the Heavenly Horses 104–101 BCE. Added the Kangju, the Wusun and the 36 BCE battle on the Talas. — §5 chronology.
- **[CANON]** Sogdians: dropped hard dates. City-states now develop over the first millennium BCE and are well attested by the Achaemenid period; noted that datable Sogdian towns in the Chu/Talas date from the 5th–10th centuries CE. — §5.
- **[CANON]** Fixed the medieval ordering (the old text put Ali-Sultan's persecution after Timur). Ali-Sultan is now 1339–1342 and Timur 1370–1405, and the Timurid period ends in 1507. Added the Shaybanid/Janid Khanate of Bukhara, the Kazakh Khanate on the Chu (c. 1465) and the Dzungars. — §5; factual error.
- **[CANON]** Kokand: the khanate is conquered in 1876 by Skobelev. Chernyayev is credited only with the 1864 Talas-valley forts and Chimkent, and Tashkent in 1865. "Cathedral of Saint Janyl" became the Church of St. Janyl (1727 charter), and Joseph Wolff is kept as canon. — §5 Kokand; naming.
- **[CANON]** Civil War: removed the expulsion of "British expeditionary units" from Kokand. Iradi irregulars now fight alongside the Red Guards who crushed the Kokand Autonomy in February 1918, and Iradi volunteers serve on the Transcaspian front in 1918–19 against the White government and its small British support force. — §5 1918.
- **[CANON]** Kobozev: the city is founded and named in 1927 and renamed Nurzhan by Alimbekov after the First Civil War in 1992 ("light of life", "guiding light of industry"). — §4; newlore.
- **[CANON]** Added the 1931 union with Rome (*Orientalis Stella*, Mar Timotheos Alimbekov through papal representatives) and linked it to the anti-religious repression of the 1930s and the 1937 purges. — §4.
- **[CANON]** 1956 Talas riots: the widow's horse is now the popular-account trigger. Added the causes historians cite (housing, wages, returning deportees, ethnic and religious grievances) and hedged the arrest figures (archival estimates 400 to over 1,000); deportations "in the hundreds" per some historians. — §5.
- **[CANON]** 2006–07: replaced "termination by a US executive order... plunge into the Second Iradi Civil War (2007)" with the brief §4 sequence. That runs: Dec 3 withdrawal by executive action (no order number); court ruling days later; Dec 9 DRI; privatization scandals; Feb 25, 2007 ISEZ proclaimed from Nurzhan (start of the Second Civil War); March Popular Front; June 4 storming and Orozbekov's arrest; summer DPI takeover of the cities; September Bishkek Ceasefire with the Naryn Protocol; October 18 UNMI (no resolution number). — §4.
- **[CANON]** Frozen-conflict section added: the 2008 referendum proposal, the 2011 talks collapse (one-third of seats), elections in 2011/2015/2019/2023 with canonical percentages, the 2013 term-limit amendment, the 2018 census controversy (estimated, not enumerated, ATR), 2018 border clashes, the 2021 alert, the early-2023 Boz-Korgon move (as independent reporting with the official denial), the 2023 protests, July 2024 seclusion (DPI health-retreat line, digital-synthesis allegations dismissed by officials), the 2025 Trump remarks, and the 2027 election. — §4, §6 public layer only.
- Removed the lead's puffery ("unique in the Eurasian steppe", "foundational crucible") and the anachronistic "Transoxiana basin" framing. — §8 tone.
- References: 6 → 31. Real scholarly works (Anthony, Librado et al., Sinor, de la Vaissière, Hulsewé, Golden, Barthold, Baumer, Biran, Pierce, Hopkirk, Brower, Khalid, Martin, Pohl) are attached only to general regional history. Irad-specific claims cite in-world sources (State Archives fonds, Talas State University Press, *Eurasian Political Quarterly*, *Central Asian Geopolitical Review*, *Talas Herald*, UNMI, the DPI Bulletin). — §7.
- Linked new §10 articles: Battle of Talas, Socialist Republic of Irad, Democratic Republic of Irad, Operation Starlight, Territory of Irad (1992–2006), Political status of Irad, 2018 Irad census, Mailuu-Suu, Religion in Irad, Demographics of Irad, Culture of Irad, Foreign relations of Irad.

##### Politics of Irad (Vol1, 3.2)
- **[CANON]** Removed hidden-lore leaks stated as fact: Toktarov's "severe stroke", "completely mute and incapacitated", IradOne "deployed AI deepfakes", and Zara "strictly gates physical access". Replaced them with the DPI's health-retreat line, the allegations of digital synthesis by opposition outlets and technology monitors (dismissed by officials as foreign-sponsored disinformation), and Zara as a non-political Stanford doctoral candidate in education, with unverified tabloid reports of family tensions over access. — §6.
- **[CANON]** Replaced the omniscient "intense succession struggle rages" with the publicly visible friction between Ruslan and Alikhan (Ruslan's anti-Muslim remarks; Alikhan's spending and rumors; no substantiated US links), the middle sons' business roles, Maksat's public technocratic line, and Bekzatov's putsch talk as palace intrigue. — §6.
- **[CANON]** The Boz-Korgon relocation is now attributed to independent reporting, with the government's position that Talas is the operational capital (it was stated as fact: "quietly relocate"). — §2, §6.
- **[CANON]** Organic Act: corrected the "federally appointed Governor" to an elected Governor under the Elective Governor Acts (1992). Added the 2007 continuation of the Organic Act under "suspended sovereignty" (replacing "suspended territoriality"), the US High Commissioner in the territorial era, and the critics' view of rule by decree, now attributed to HRW rather than stated as fact. — §2, §4.
- **[CANON]** Checked the election years (2011 88.74%, 2015 78.25%, 2019 90.31%, 2023 92.75%) and the 2013 amendment; the crammed one-line list is now a table. Added the next election due in late 2027. — §2.
- **[EXPANDED]** Restructured and expanded from about 1,000 to about 3,000 words. Sections: Political status (with Unification and the census dispute), Constitutional framework (Organic Act and continuation; Elective Governor Acts), Executive (with patronage and the Toktarov family), Legislature (Territorial Legislature/*Mejlis*, never "Supreme Council"), Judiciary, Political parties and factions, Institutions of the ATR, Elections, Succession politics, Civil society and media, Foreign relations. — Brief expansion list.
- The neopatrimonialism characterization is now attributed to the leaked US intelligence reports of Toktarov's first term (original canon), replacing "Western intelligence assessments... textbook neopatrimonial regime". — §6 attribution.
- Ilyasov: now presents himself as self-funded, with his rise attributed to organic engagement; "triggered spontaneous student demonstrations" became "prompted the 2023 Student Protests in Talas". — §6.
- Removed puffery ("diametrically opposed", "celebrated war veteran", "textbook"). Added the canonical Toktarov quote on China. — §8.
- References: 6 → 11 with markers. Dropped the unused State Archives Fond 412 citation. The OSCE report is retitled "Gubernatorial and Legislative Elections in the ISEZ". The DPI Bulletin citation no longer carries "(Boz-Korgon)" as a place of publication, since the government denies the move; the Boz-Korgon dateline is instead cited in the text as evidence used by independent reporting.

##### Boz-Korgon (Vol1, 3.3)
- **[CANON]** Location corrected to the Chu District, 40 km east of Nurzhan; removed "northern piedmont of the Talas Alatau", which lies far to the southwest. Added a Location section. — §3 districts.
- **[CANON]** The *de facto* seat is now independent reporting set against the government's position that Talas is the operational capital, with the evidence cited by reporters (officials' relocation, convoys, decree datelines). It had been stated as fact. — §2, §6.
- **[CANON]** Gave the compound a single coherent origin: begun in 1995 by the territorial administration as a continuity-of-government site, with a command and communications center (relay later run by Attelkom) and a security depot for the Nurzhan oil fields and rail corridor, which explains the "military-industrial" label. The ISEZ took it over after 2007, and the Toktarov family has occupied an estate inside since 2011. Removed the competing framings. — Brief task.
- **[CANON]** The Bush section was retitled "Bush family conspiracy theory" and framed as a conspiracy theory per newlore (quid pro quo for dissolving the treaty, contradicted by the 1990s construction date, Bush family visits in the 2000s, Toktarov occupancy after 2011). Removed "declassified commercial records refuted" and the 2002 "diplomatic delegations inspected the perimeter" claim. No new claims about real people. — §6, §7.
- Removed "access strictly regulated by Lieutenant Governor Aidar Maksat" (close to the hidden-lore gatekeeping). Security is now the Gendarmerie's Special Protective Service (matching the Gendarmerie article), with unverified tabloid reports of family tensions over access. — §6.
- Replaced the "state-of-the-art specialized intensive healthcare clinic" with "a medical clinic, listed in a construction tender of the late 2010s". Fixed the crammed facilities list and removed the Armed Forces/"Talas Gendarmerie" wording. — §8, consistency.
- Iradi name given in Latin script (Iradi has used Latin since 1992), with the Cyrillic labelled as Russian. References: 3 → 6 with markers.

##### Kok-Tash Kariz System (Vol1, 3.4)
- **[CANON]** Category changed from "Minor Settlements & Communes" to "History & Heritage", matching the Vol2 heritage-site articles. — Miscategorized.
- **[CANON]** UNESCO: the 2014 inscription is now a component of the transnational Silk Roads serial property nominated by Kazakhstan and Kyrgyzstan. Both Iradi administrations protested, and Irad is not a State Party. The real "Chang'an–Tianshan Corridor" evaluation citation became a generic descriptive UNESCO citation. — §5 UNESCO, §7.
- **[CANON]** Cold War CIA involvement is presented only as an unconfirmed allegation by some historians, based mainly on post-1992 oral testimony and never acknowledged by the US. IAC smuggling since 2007 is stated as public, with the "opportunistic use" framing. — §5, §6.
- **[CANON]** Added a section noting that karez systems are unusual this far north and east, with the Turpan comparison and the origin debate. — Brief task.
- Changed "initiated during the Kara-Khanid Khanate" to "expanded" under the Kara-Khanids, with radiocarbon dates clustering in the 10th–11th centuries and a possibly earlier core. — newlore.
- **[EXPANDED]** About 550 → about 1,100 words. Sections: Engineering, Comparison with other karez systems, History (Medieval origins; Soviet period and Cold War allegations; Smuggling since 2007), World Heritage listing and current status.
- Replaced the real *Geographical Journal* (1904) citation, which had been used for an Irad-specific claim, with an in-world State Archives fond, and dropped the "UNECE Water Series" label from the water-authority citation. References: 3 → 8 with markers. — §7.

Untouched articles: none (all four edited).


### Chunk A4

### Changelog: Chunk A4 (Vol1, B-class biographies 3.5–3.10)

All six articles were rewritten in full as BLPs: a lead, then early life and education, career, political positions, public image and controversies (attributed), personal life, and references. Section headings now follow brief §8: `## Section` and `### Subsection`. The chunk previously mixed `###` sections with a `## References` heading. Article headings, order and assessment lines are unchanged.

##### Bektur Zhumabek uulu (Vol1, 3.5)
- [EXPANDED] Rewrote and expanded from about 830 to about 1,910 words. New or rebuilt sections: early life (Soviet-registered name, veterinary training, army service 1986–88), First Civil War, territorial period (acclaimed *biy* 2001; 2003 Kara-Suu gold-license protest), Second Civil War, IAC role, political positions, public image and controversies, personal life.
- [CANON] Self-styled title changed from "servant and mediator (*el-chabary*)" to "ambassador" (*elchi*) or "negotiator" (*ortomchu*), per original wiki and baselore.
- [CANON] 2007 narrative aligned with the brief's timeline: privatization scandals Jan–Feb 2007; ISEZ proclaimed Feb 25; Popular Front formed March 2007 (previously said he "united the twenty-four clans"); storming of Talas June 4; Orozbekov arrested and handed to the UN; Front withdrew as DPI forces took the cities that summer; Bishkek Ceasefire in September with the Naryn Water and Power Protocol annex. Added Ruslan Kadyrov's defecting units, consistent with his stub.
- [CANON] 2011 walkout restated as the only real bilateral talks, with the one-third offer and the quote attributed to the *Talas Herald*. Corrected "33% of national parliamentary seats" to one-third of seats in a unified Territorial Legislature.
- Removed the Kok-Tash Kariz claim that the CIA reinforced the tunnels (hidden-lore leak, brief §5/§6). Kept only the public, attributed smuggling allegation, with Bektur's denial.
- Removed advocacy phrasing ("~3.5 million rural population, exposing the DPI's suppressed 4.6M census"). Replaced with his attributed rejection of the 2018 census and the independent ~6.2 million estimate — neutrality and canon.
- Removed puffery ("revered", "legendary status", "Spartan", "famously", "decisive", "celebrated throughout the high pastures") and an omniscient "Bektur has steadfastly resisted".
- Moved his upbringing from the "eastern Chatkal ranges" to the Talas Alatau, to match the Kara-Suu Canyon article (northern piedmont of the Talas Alatau) and the "northern" Tanıp.
- [CANON] Naming: his wife was "Klara Zhumabek kyzy", which by patronymic makes her his sister. Klara (who has her own article) is now his sister; his wife is Gulbara Sultanbek kyzy. His father is Zhumabek Asanaly uulu and his mother Zuura Tashtan kyzy, in correct tribal patronymic form.
- Added his public statements in 2024 ("not negotiate with a recording", attributed, with the DPI response) and in 2025 (the Trump-remarks communiqué, quoted as in Vol2 4.46).
- Fixed the crammed bullet paragraph (five items run together on one line) as a real list. Removed bold on non-title terms.
- References rebuilt (11 → 17). Removed unrelated or real works (Pierce 1960; US State Dept Dispatch 1992 for the 2011 walkout; folklore society). Changed the C-24 "Field Interviews… Geneva" citation to the New York working paper. Removed "ATR Council Press, Boz-Korgon" (Boz-Korgon is the DPI compound).

##### Aidar Maksat (Vol1, 3.6)
- [EXPANDED] Rewrote and expanded from about 690 to about 1,270 words. Added municipal career detail, the 2016 department post, his Lieutenant Governor portfolio (CNPC talks, COVID-19 commission, Naryn protocol, 2023 surcharge suspension), the period since July 2024, political positions, public image and personal life.
- Removed hidden-lore leaks:
  - "Together with Zara, who manages her incapacitated father's medical care at Boz-Korgon, Maksat has established tight control over executive access" — replaced with Zara's public profile (Stanford doctoral candidate living mostly abroad) and unverified tabloid reports of family tension over access to the Boz-Korgon estate.
  - "Governor Toktarov's sudden hospitalization" — replaced with the official health-retreat line.
  - Rumors of Beijing backchannels "to cement his sole leadership" — replaced with attributed speculation by anonymous Western diplomats about meetings with Chinese investors, his office's explanation, and a note that no political understandings have been reported.
  - The claim that he funneled state funds to Jason Ilyasov — deleted; a journalist would have no plausible basis for it.
- Replaced omniscient prose ("resisted hardline demands", "quietly rebuffing attempts by Alikhan to access sovereign reserve accounts") with attributed, unconfirmed reports from exiled outlets and diplomats.
- Removed the invented "Supreme Executive Council… emergency delegation statutes". Now says official statements describe him as acting on the Governor's instructions and that the succession provisions of the Elective Governor Acts have not been invoked, consistent with the DPI line that Toktarov still governs.
- [CANON] His father worked at the Chatkal Antimony Processing Mill. Kept his Kobozev birth (named for the date) and added the family's 1985 move to the mill settlement, which reconciles the birthplace with the mill's location in the southern foothills. His education is now civil engineering at Nurzhan Polytechnic Institute (baselore: civil engineer) instead of telecommunications in Almaty.
- [CANON] Naming: registered at birth as Aidar Maksatov, using the shortened surname since his student years, which explains an urban surname without -ov. His parents are Bolat Maksatov and Saule Maksatova.
- Removed peacock wording ("exceptional quantitative aptitudes", "prestigious", "treacherous", "sophisticated covert maneuvers", "top honors").
- Fixed the crammed bullet paragraph. Linked Zara as [[Zara Toktarova]] (the retitled Vol2 article, per brief §11).
- References rebuilt (7 → 14). Removed Bar Hebraeus (1286) and Pierce (1960), which had been cited for 2019 and 2024 events. Changed the DPI bulletin's place of publication from Boz-Korgon to Talas, the official capital.

##### Ruslan Toktarov (Vol1, 3.7)
- [EXPANDED] Rewrote and expanded from about 520 to about 1,180 words. Added early life (born in Talas while his father was serving), career timeline (family fuel concession 1999–2004; Gendarmerie captain 2004; 2007 Nurzhan tank-farm detachment; Qara-Chik checkpoints; commander since March 2012, consistent with Vol2 4.52), succession contest, political positions, controversies, personal life.
- Added his anti-Muslim remarks with attribution, as public canon in brief §6: the December 2024 Gendarmerie Academy speech, the January 2025 TV interview invoking the horsemeat prejudice (framed as a prejudice per brief §5), condemnation by clerics, the Archbishop and rights groups, and the Department of Public Information's "personal views" response. The previous text only gestured at "inflammatory rhetoric".
- Converted unattributed claims to attributed ones: the "silent purge" of Alikhan's loyalists and the "tactical alliance" with Bekzatov are now regional-press speculation, both denied. Removed "the iron fist of his father's regime" and other editorializing.
- Corrected the 2007 role. "Secured the state petroleum tank farm outside Talas from advancing rebel irregulars" conflicted with the canonical sequence; he now guards the NurGaz tank farm and rail yards outside Nurzhan during the strikes, and his units enter Talas after the Front's withdrawal in summer 2007.
- Aligned his titles with the Republican Gendarmerie article: Special Protective Service as a unit of the 4,000-strong Gendarmerie under the Ministry of Internal Security.
- Made the 2023 protest account consistent with the Ilyasov and Maksat articles: October 2023, police and Gendarmerie, tear gas and water cannon, Ilyasov detained. Removed the claim that marchers followed "the slogans of" Ilyasov, since canon describes the protests as spontaneous.
- Business allegations (BVI shell companies at Talas Air Base) are now attributed to 2019 investigative reports, with his denial.
- Fixed the crammed bullet paragraph. References rebuilt (8 → 11). Removed Vine (1937), Bar Hebraeus and Pierce, and replaced Jane's Defence Weekly with in-world sources.

##### Alikhan Toktarov (Vol1, 3.8)
- [CANON] Birth year changed from 1985 to 1980 (born September 14, 1980). Canon makes Ruslan and Alikhan the two eldest sons, and Vol2 gives Timur 1982, Adil 1984, Bekzat 1986 and Zara 1988, so a 1985 birth made Alikhan the fourth son. Education dates adjusted accordingly (studied in Bishkek 1998–2000; Regent's College, London, BA 2003).
- [EXPANDED] Rewrote and expanded from about 610 to about 1,090 words. Added business career (bonded warehousing; Steppe Luxury Group 2008; Talas avenue developments with brother Adil, consistent with Vol2 4.63), IradOne chairmanship, succession rivalry, political positions, public image, controversies, personal life.
- Removed hidden-lore leaks:
  - The "Collapsed Trump Gambits" section, which said he "covertly dispatched lobbyists to Washington". Replaced with one sentence of unsubstantiated speculation about contacts with American political consultants, his office's dismissal, and the public effect of the 2025 remarks. No new claims about Trump were added.
  - The "Secret Backing of Jason Ilyasov" section — replaced with the observable fact that IradOne resumed booking Ilyasov in 2024, speculation in opposition outlets, and IradOne's editorial-decision response.
  - "Following his father's medical incapacitation in July 2024" — replaced with withdrawal from public view.
- Added the IradOne broadcast-authenticity dispute in the brief §6 wording (monitors allege synthesis; officials dismiss it as foreign-sponsored disinformation).
- Public scandals kept, with attribution and his responses: the 2018 Dubai villas, the 2021 Macau video, and tabloid rumors of substance abuse and spending (from the original wiki).
- Changed "Ulak Tartysh President's Cup" to "Governor's Cup", since Irad has a governor, not a president. Removed bold on non-title terms. Fixed the crammed bullet paragraphs.
- References rebuilt (8 → 11). Removed Vine, Bar Hebraeus and Pierce, and replaced the real journal "Ethnomusicology Journal" with an in-world source.

##### Kamran Bekzatov (Vol1, 3.9)
- [EXPANDED] Rewrote and expanded from about 670 to about 1,230 words (sections listed below).
- [CANON] Export route: removed "secured critical export access to the Caspian Pipeline Consortium (CPC) network". The route is now the 85-km Northern Export Feeder, completed in 1998 by the Iradi Petroleum Transit Consortium (51% NurGaz), into the Kazakh trunk network near Shymkent under transit arrangements with KazTransOil. Also removed the "Nurzhan Petroleum Pipeline" link from the lead, because that stub conflicts (340 km, Caspian).
- Output restated as the NurGaz figure (about 120,000 bpd), with independent estimates lower.
- Removed the hidden-lore leak section "The Aborted Russian Coup and Pivot to Ruslan (2022–2024)", which stated that he "has increasingly aligned himself with… Ruslan Toktarov, trading NurGaz financing for armed protection". Replaced with uncorroborated 2023 coup claims dismissed by analysts as palace intrigue or official paranoia (his "fairy tales" denial), plus attributed speculation about a rapprochement with Ruslan, explained by the Gendarmerie's standing infrastructure-protection role and denied.
- [CANON] Kobozev/Nurzhan names follow the date. Changed [[Kobozev Heavy Machine Plant]] (no such article) to Kobozev Heavy Machine Plant (now [[Nurzhan Heavy Machine Plant]]). Changed [[Nurzhan Institute of Petroleum]] to [[Nurzhan Polytechnic Institute]].
- First Civil War role recast as contested (supporters' versus Provisional Government veterans' accounts), replacing the hagiographic "refusing to surrender oilfield control to corrupt party commissars". Historical fixes: "Minneftegazprom" changed to the USSR Ministry of the Oil Industry for 1974–88; Gubkin named as it was at the time.
- Removed "universally recognized as the most powerful oligarch" and "billionaire" in the encyclopedia's voice. Replaced with "widely described as an oligarch" and an attributed fortune estimate. Kept his praise of Putin as in the original wiki, without new detail.
- Added sections on relations with the DPI (accommodation in 2007; cooperation alongside criticism), political positions, public image and controversies (privatization terms, contamination, output gap), and personal life. His children are now consistent with their stubs (Emil, Rustam, Asel); his wife is Galina Bekzatova (née Lebedeva), in urban naming.
- Fixed the crammed bullet paragraph. References rebuilt (10 → 13). Removed Bar Hebraeus, Pierce and the US State Dept Dispatch (1992).

##### Jason Ilyasov (Vol1, 3.10)
- [EXPANDED] Rewrote and expanded from about 580 to about 1,010 words (sections listed below).
- Fixed an internal contradiction: he was "born in Chicago" in 1988 to parents who "fled… during the early months of the 1992 civil war". His father was now a visiting researcher in Chicago in 1987–89 under a Soviet–American exchange; the family returned to Talas in 1989 and left in January 1992; his US birthright citizenship allowed them to resettle in Chicago. This keeps his birthplace, age, parents' story and "Iradi-American" description.
- [CANON] 2023 protests made consistent with canon ("spontaneous protests") and with the Ruslan and Maksat articles. The trigger is now his *Debate One* remark about the October 2023 licensing surcharge going viral, and observers call the protests spontaneous and leaderless. The authorities' claim that he instigated them is attributed. Police and Gendarmerie dispersed the protests; he was detained for three days and released without charge; Maksat suspended the surcharge in November 2023. Removed "viral speech… calling for civil disobedience" as the organizing trigger, and "international diplomatic pressure secured his release".
- Removed the hidden-lore leak naming Aidar Maksat and Alikhan Toktarov as covert funders. Replaced with a "Funding and independence" section: his self-funding statement, competing speculation (pro-government claims of "American money"; opposition claims of factional tolerance) and an EPQ survey finding no evidence.
- Kept the canon framing: Iradi-American, self-described anarcho-capitalist, regular on IradOne opinion panels since 2016, brash manner, the "unregulated corporate paradise… economic heart of Asia" claim (attributed). Removed "foremost intellectual leader of the anarcho-capitalist movement in Central Asia", "economist", "vibrant", "fiery" and "galvanized thousands".
- Added the period since 2024 (return to IradOne; challenge to show the Governor live, with the DPI response; reaction to the 2025 remarks), public image and personal life.
- Fixed the crammed bullet paragraph. Retitled the EPQ citation from "…Controlled Opposition in the ISEZ" to "…Opposition Politics in the ISEZ". References rebuilt (11 → 10), removing Vine, Bar Hebraeus, Pierce, the C-24 working paper, the OSCE electoral report and the US State Dept Dispatch, which had been cited for unrelated claims.

Untouched articles: none (all six edited).


### Chunk A5

### Changelog: chunk A5 (Vol1, articles 3.11–3.19)

General, applied to all nine articles:
- Rewrote every article against the brief, newlore and canon. Article headings (`### 3.n. Title`), order and assessment lines are unchanged; no retitles, merges or deletions.
- Normalized section headings to `## Section` with `####` subsections (brief §8). Nurzhan and Iyık Janyl previously used `### Section`, which collides with the article-heading level.
- Rebuilt every reference list in the existing `<ol class="references">` format. Removed mismatched citations (e.g. Pierce 1960 cited for 1992 events, Vine 1937 for 2018 population, Bar Hebraeus for an archbishopric, KazTransOil for a demilitarized city, the OSCE for oil output). Irad-specific claims now cite in-world sources, and real works are cited only for general regional history. Split combined markers (`[2][4]`) into separate `<sup>` tags.
- Converted crammed "* **A**: … * **B**: …" paragraphs into real lists or prose; removed peacock wording; American spelling throughout.

##### Nurzhan (Vol1, 3.11)
- **[CANON]** "known as Kobozev from 1927 until 1991" → "from 1927 to 1992". The renaming is attributed to Amanbek Alimbekov in a September 1992 speech after the end of the First Civil War ("guiding light of industry"), confirmed by the 1993 Toponymic Heritage Statute. This reconciles with Vol2 *De-Russification Movement in Irad*. Removed the false claim that the city was renamed "upon the October 1991 declaration of state sovereignty".
- **[CANON]** Removed the export route to the "Caspian Pipeline Consortium network". Crude now moves via the Nurzhan Petroleum Pipeline and the 85-km Northern Export Feeder into the KazTransOil network near Shymkent, for refining there or onward shipment to Russia. The 120,000 bpd output is attributed to NurGaz, with a note that independent estimates are lower.
- **[CANON]** The city now lies in the lower Chu lowlands, surrounded by Chu District. Boz-Korgon is placed 40 km east, as independent reporting, with the official denial in both the lead and the history section. Replaced "Kyrgyz Ala-Too rise dramatically to the south" with "the Kyrgyz Range is visible across the border". Population is given as 850,000 urban and more than 1 million in the agglomeration (2018 official), with a note on why the city figure is less disputed than the national total.
- **[CANON]** Added Dastgoh and Navbahor as urban districts (Navbahor as a 1990s territorial-era residential district).
- **[CANON]** "Bekzatov established the Russo political faction" → the Russos are a generational demographic, and Bekzatov is their most prominent figure and a critic of DPI economic policy.
- Added that Kobozev was the capital of the Iradi SSR and the seat of the Socialist Republic of Irad (Original wiki; brief §4), and that the 1925 First Congress of Iradi Soviets met in the pre-1927 settlement (reconciles the Vol3 stub). Added Toktarov's proclamation of the ISEZ from Nurzhan on 25 Feb 2007.
- Replaced the `[[Kobozev Heavy Machine Plant]]` redlink with `[[Nurzhan Heavy Machine Plant]]`.
- **[EXPANDED]** Grew from about 900 words in 5 sections to about 2,900 words. New sections: Etymology; History in 7 subsections (early settlement, Soviet capital, deportations and WWII, oil city, independence and First Civil War, territorial period, since 2007); Geography, Climate and Cityscape; Demographics (official 2018 ethnic shares, language, religion); Economy (list); Government; Transport; Education and health; Culture; Notable people. Integrated about 25 existing related articles as links (Sergei Voronov, 1952 Kobozev Steel Strike, Bolotbek Bekzhanov, Oleg Kim, Kobozev Bread Riots, Battle of Kobozev Railhead, Nurzhan Polytechnic Institute and others).
- Removed puffery: "primary industrial powerhouse", "indispensable source", "undisputed financial and extractive engine", "enjoying international recognition", "celebrated as the birthplace of Central Asia's most influential…", "refreshing mountain breezes".
- References: 10 → 21.

##### Iyık Janyl (Vol1, 3.12)
- Removed puffery: "Celebrated across Central Asia", "unshakeable mountain sanctuary", "extraordinary architectural masterpiece", "renowned", "immense spiritual authority", "serene".
- **[CANON]** UNESCO: the Church of Saint Janyl and the Ruins of Old Iyık Janyl (Shar-i-Kuhna) were inscribed during the territorial period on a US nomination, with the US as State Party. Irad itself is not a State Party. Removed the citation to the 2014 Chang'an–Tianshan Silk Roads nomination.
- **[CANON]** 1931 union: Mar Timotheos Alimbekov negotiated secretly through intermediaries at papal nunciatures abroad, and Soviet suspicion of the Catholic link fed the repression of the 1930s and the 1937 purges.
- **[CANON]** Janyl's vision is of Jesus as the White Rider (not "a celestial vision of Polaris"). Her historicity is disputed, the site of the First Church of Janyl is unknown, and the 1727 church is a symbolic re-creation (newlore; Original wiki). "Consecrated around 1140 CE" → tradition dates her to the 11th or 12th century.
- **[CANON]** The 1876 conquest of Kokand is credited to General Mikhail Skobelev.
- Kept 310,000 (2018), 65 km southeast of Talas, 1,280 m.
- Feast of Saint Janyl: "Every September" → 24 August, to match *Syro-Iradi Catholic Church*, *Church of Saint Janyl* and *East Syriac Rites of Iyık Janyl*. Attendance is now an archbishopric estimate (more than 150,000) instead of the conflicting "over 200,000" and "hundreds of thousands".
- Aligned with *Church of Saint Janyl*: dome 28 m → 22 m; masons from "Samarkand and Kashgar" → "Samarkand and Bukhara"; crypt of Mar Gewargis. "Eight-pointed Star of Irad" → "a cross and the Star of Irad".
- "Neutral Diplomatic Status", an unsourced claim that the whole city is demilitarized, was rewritten as an informal 2007 understanding. It covers the cathedral precinct and pilgrims' unarmed crossings for the Feast, is monitored by UNMI and is not in the Bishkek text.
- Removed the implausible "seminary founded in 1933" (under the Stalinist anti-religious campaign). The seminary is now identified with the Saint Ephrem Major Seminary, closed 1937 and reopened 1994. Fixed "Following the 1992 [[Winter Uprising of 1992]]".
- **[EXPANDED]** Grew from about 1,000 to about 2,300 words. Sections: Etymology; History (Janyl tradition, medieval town, Kokand and 1727, Russian rule and 1931 union, Soviet period, since 1992); Geography; Climate; Demographics; Economy; Government; Transport; Education; Culture and landmarks; Notable people. Added links to Treaty of Talas (1727), Kara-Suu Canyon, Archbishop Mar Ephrem, Irad Palace of Art, Pilgrimage Hostel, Monastic Cloister, Diocesan Archives Vault, Seminary Choir, The Epic of Janyl and Cathedral Seminary of Iyık Janyl.
- Unlinked redlinks to non-existent articles (Qara Khitai, Khanate of Kokand, Keraites, Naimans, Chagatai Khanate, Timur, Holy See).
- References: 13 → 15.

##### Democratic Party of Irad (Vol1, 3.13)
- **[CANON]** Election years "2011, 2017, and 2023" with "majorities exceeding 90 percent" → 2011 (88.74%), 2015 (78.25%), 2019 (90.31%), 2023 (92.75%), with a results table. Added the 2013 term-limit amendment and the next election, due late 2027.
- **[CANON]** History now follows the timeline. The party grew from the Provisional Government's reformist caucus and was formally constituted in October 1992, after Operation Starlight (consistent with *Erlan Toktarov*: "joined the newly founded DPI"). It led the territorial period. It split after the DRI's proclamation, and on 25 Feb 2007 Toktarov seized it and proclaimed the ISEZ from Nurzhan ("New DPI"). Removed "following the withdrawal of United States forces", since US forces remained.
- **[CANON]** Succession section limited to the public record: visible Ruslan–Alikhan friction, Ruslan's anti-Muslim remarks, Alikhan's spending and rumored substance abuse, Maksat's day-to-day role with no public claim, Zara as a non-political Stanford doctoral candidate, and unverified tabloid reports. Toktarov's absence is given with the official line plus the attributed allegation of digital synthesis.
- Corrected "structural alliances with … NurGaz directed by Kamran Bekzatov" to uneasy relations, since Bekzatov is a canonical DPI critic. "Secondary administrative suites at Boz-Korgon" stated as fact → attributed to independent reporting.
- **[EXPANDED]** Grew from about 450 to about 1,750 words, adding History (4 subsections), Ideology (list, the Toktarov China quote, the leaked US intelligence reports), Organization, Electoral performance, Business and media connections, Succession and Criticism (the OSCE quote, media, census undercount controversy, unification).
- References: 3 → 13.

##### Iradi Freedom Society (Vol1, 3.14)
- **[CANON]** "Formed in January 2007 during the collapse of the … DRI" was impossible, since the DRI fell in June 2007. The IAC is now the Popular Front's political council, reorganized at an Aksay Plateau kurultai in late 2007 after the Bishkek Ceasefire (consistent with *Bektur Zhumabek uulu* and *Popular Front of Irad*). Removed the anachronistic claim that the IAC "repelled" central-government forces in the war.
- Removed the "permanent diplomatic secretariat in Boz-Korgon", since Boz-Korgon is the DPI executive compound. The article now refers to the IAC Chancellery without a location, and the ATR Council Press imprint changed from Boz-Korgon to Kara-Suu.
- **[CANON]** Added the 2011 walkout over the one-third seat offer, the 2008 initiative, 2017 polling, the 2018 clashes, the 2021 alert, the census dispute (attributed, with satellite and registry evidence described as supporting rather than proving), the 2025 protests (canon wording only), the Toktogul split control and Naryn Protocol, the public Kariz smuggling use (no CIA claim), the El-Choro Militias and the six UN planning zones (described as aid-planning only).
- **[EXPANDED]** Grew from about 550 to about 1,600 words: History, Organization (list), Policies, Economy and resources, External relations, Criticism. Removed promotional closing lines.
- References: 3 → 11.

##### Talas Air Base (Vol1, 3.15)
- **[CANON]** "under a presidential executive order" → "President George W. Bush's withdrawal from the treaty by executive action on 3 December 2006".
- **[CANON]** Added the Operation Enduring Freedom role (primary staging area from late 2001: troop rotations, tanker and medevac flights) and the 2001 Basing Rights Agreement.
- **[CANON]** Post-2006 basis: US forces remained under the 2001 agreement and later ISEZ arrangements, which have not been published in full. The previous text implied the base simply became a joint-use facility after the US left.
- **[CANON]** Added the five other US installations (logistics, testing, training), unnamed.
- Removed the unverifiable ICAO code "UTTR". Added the Soviet founding, the Starlight landing (Marines and 10th Mountain), Attelkom and Iradiya origins, the 2014 shift, Operation Clear Skies (2020), the 2021 alert, Gendarmerie/Barysh security, the economic role, the legal-status dispute and the UN NSGT listing.
- **[EXPANDED]** Grew from about 500 to about 1,200 words. Replaced the Jane's citation with an in-world source.

##### Alimbekov-Baker Treaty (Vol1, 3.16)
- **[CANON]** Signed 2 June 1992 by Alimbekov and Baker and ratified unanimously by the Provisional Government the same day. No new quotes or actions by real people; the only physical detail used, the theater basement, comes from the existing *Amanbek Alimbekov* article.
- **[CANON]** Added the statutory independence clause as a treaty provision carried into the Organic Act; Bush's withdrawal of 3 Dec 2006 by executive action.
- Removed "Alimbekov traveled to Geneva in May 1992", which contradicts *Amanbek Alimbekov* and *First Iradi Civil War*: he stayed in besieged Talas and made contact via the US Embassy in Almaty. Corrected "defense guarantees … under Article IV" to territorial status under the Territory Clause. Corrected "chartered commercial banking through Talasbank": Talasbank was chartered under the 1993 territorial act. Recast the "Bush administration, eager to…" motive as historians' interpretation.
- Added the provisions list, implementation, the UN listing and non-notification, DRI recognition by 26 states, the annulment and the suspended-sovereignty doctrine, a legal-debate section, and a legacy section (Iradimania; the Bush complex theory and 2025 remarks in canon wording only). Added the uranium and thorium undertaking (Mailuu-Suu).
- **[EXPANDED]** Grew from about 550 to about 1,450 words. Removed "landmark", "one of the most unusual…" and "fundamentally reshaped".

##### Second Iradi Civil War (Vol1, 3.17)
- **[CANON]** Rewritten to the exact brief §4 sequence. The dates are now 25 Feb 2007 (ISEZ proclamation, the start) to September 2007 (Bishkek Ceasefire), replacing "January 14 to June 4". The war is presented as three-sided (DRI, ISEZ emergency administration, Popular Front). Popular Front formed March 2007; storming of Talas 4 June; DRI dissolved; Orozbekov arrested (not "fled abroad"); in summer DPI forces with Western and US backing took the cities as the Front withdrew; ceasefire in September with the Naryn Protocol annex; UNMI established 18 Oct 2007 (no resolution number).
- Removed "presidential executive order" and the out-of-sequence "Toktarov stepped in" after June. "Chuy" → "Chu".
- Added Background, Forces, Casualties (no invented toll: "low thousands" per UNMI and agencies; more than 80,000 displaced retained), Aftermath (IAC and El-Choro formation, 2008, 2011) and Historiography.
- **[EXPANDED]** Grew from about 550 to about 1,400 words.

##### Supreme Court of Irad (Vol1, 3.18)
- **[CANON]** "*In re Sovereignty Clause* (2006) … unanimously" → the Statutory Independence Ruling (Dec 2006): Orozbekov's petition, Chief Justice Dastan Isakov's majority opinion ("automatic reversion"), and Toktarov's annulment by decree on 25 Feb 2007, followed by reconstitution of the bench in 2007.
- **[CANON]** Added the 2003 Judicial Reforms Act (district courts, jury trials, commercial arbitration).
- Fixed "interstate commercial disputes" (Irad has no states) and "Bush's proclamation terminating…".
- Added Composition and appointment, Jurisdiction (list), Notable decisions (including a 2014 term-limits challenge the court declined), Relationship with customary law and Criticism (HRW, Talas State University scholars, the business view).
- **[EXPANDED]** Grew from about 600 to about 1,170 words.

##### Territorial Legislature of Irad (Vol1, 3.19)
- **[CANON]** Removed "unicameral Supreme Council (*Mejlis*)". The article is reframed: the Territorial Legislature of Irad (*Mejlis*) is a continuing body, bicameral from 1992 to 2006. It proclaimed the DRI on 9 Dec 2006 (Original wiki) and was reconstituted as a single chamber under the ISEZ in 2007, keeping the territorial name. Previously it was described as dissolved in Dec 2006.
- **[CANON]** Added the 2011 summit offer of one-third of the seats and the IAC walkout, DPI dominance (51 of 60 seats in 2023) and the 2013 amendment.
- **[CANON]** Removed the invented territorial districts ("Talas Urban, Lower Talas, Chuy Valley, Chatkal Uplands, Southern Steppe"), so senatorial districts are now unnamed. Current constituencies are the canonical three cities and five districts.
- Added the interim legislature (1992–94), the first elections (1994), the Toponymic Heritage Statute, the 1995 Latin Orthography Revision, the 2003 Act, and Structure and procedure, Composition and Criticism sections. Removed "built broad civic trust" and the "Bipartisan Consensus" framing.
- **[EXPANDED]** Grew from about 550 to about 1,200 words.

Untouched articles: none (all 9 edited; 9 expanded; 0 merged; 0 deleted; 0 retitled).


### Chunk A6

### Changelog: chunk A6 (Vol1 3.20–3.28)

All nine articles were rewritten in place, with the same headings, order and heading levels. All subsections use `## ` (no `###` subsections). Every reference list was rebuilt in the `<ol class="references">` format, with `<sup>[n]</sup>` markers checked against the list.

##### Armed Forces of Irad (Vol1, 3.20)
- **[EXPANDED]** Grew from about 450 to about 2,100 words (prose under 2,000; the rest is the order-of-battle and equipment lists). New sections: Soviet and post-Soviet origins; Territorial period (1992–2006); Formation during the Second Civil War; Since 2007; Command and organization; Other armed forces in Irad; Personnel; Equipment; Doctrine and deployment; Relationship with United States forces; Criticism.
- **[CANON]** Removed the Republican Gendarmerie from the list of the corps's branches, because it is a separate Ministry of Internal Security force (Vol2 4.52). Added a section separating the corps from the Gendarmerie and from the ATR's El-Choro Militias. Ruslan Toktarov's public role (Gendarmerie commander since 2012, Special Protective Services) is stated as public fact.
- **[CANON]** Gave the official name "State Defense Corps", already used in Talas Air Base 3.15 and Second Iradi Civil War 3.17, and explained the "Armed Forces of Irad" usage (the DPI claims all of Irad but operates only in the ISEZ).
- Added a history: Soviet 17th Motor Rifle Division and SRI forces (officer corps largely ethnic Russian); disbandment after Operation Starlight; the territorial-era Irad National Guard (1994); the split in 2006–07 along canon dates (25 Feb 2007 ISEZ proclamation, 4 Jun 2007 storming, summer 2007 DPI takeover with Western and US backing); formation by emergency decree in July 2007; Bishkek ceasefire in September 2007; the 2021 alert; non-deployment in 2023; neutrality since July 2024, with Toktarov's absence attributed to the DPI's health-retreat line.
- Gave personnel figures as the official line (12,000 active / 18,000 reserve) alongside an independent estimate (10,500–11,000), sized for the ISEZ population. Added conscription rules (from 2008), the buy-out fee, exemptions, women's service and the ethnic and linguistic make-up of the officer corps.
- Replaced the vague equipment paragraph with an attributed inventory, and added the budget (about $260M, 1.4% of nominal GDP).
- Added a US relationship section: Talas AB plus five installations under the 2001 Basing Rights Agreement and later ISEZ arrangements; the annual joint exercise; the ambiguous legal basis (non-recognition, US still the nominal administering power); one neutral sentence on the 2025 protests, adding nothing new about Trump.
- Moved conscript training from "Kara-Oi" to the Ak-Tash Training Center, to avoid putting it at the UNMI headquarters site. Moved alpine training from the "upper Chatkal valley" (ATR territory) to Sary-Bulak District (ISEZ).
- Removed the fake document number "Doc. UNMI-MIL-2023-04" and the Jane's citation; references now use in-world sources.
- Cut padding ("modern communication protocols and integrated logistics networks ensure…") and fixed the run-together lists.

##### United Nations Mission in Irad (Vol1, 3.21)
- **[EXPANDED]** Grew from about 450 to about 1,700 words. New sections: Background, Mandate, Organization, Headquarters and deployment, Ceasefire monitoring, Naryn Protocol supervision, Humanitarian coordination and mine action, Casualties, Mandate renewals, Criticism.
- **[CANON]** Established 18 October 2007 by a Security Council resolution, with no number given. The mandate now covers monitoring the Qara-Chik line, supervising the Naryn Water and Power Protocol (joint commission, observers from the three neighboring states, unpublished revenue annex, 2027 renewal), humanitarian coordination and mine action. It also covers the good offices behind the 2008 initiative and the 2011 talks (IAC walkout over one-third of seats).
- **[CANON]** Fixed "UN Special Committee on Decolonization in Geneva": UNMI reports to the Security Council, and the committee sits in New York and issues a working paper.
- **[CANON]** Removed "tribal councils in Boz-Korgon". Boz-Korgon is the DPI's de facto executive compound. UNMI's exclusion from a Boz-Korgon security zone is now reported with the official denial.
- Added invented but plausible figures: 210 military observers (ceiling 230), 30 police, 142 international, 261 national and 18 UNV staff; $57.9M budget; contributor list; Kara-Oi headquarters, Tash-Kömür sector headquarters and 11 team sites; 214 violations in 2023; five fatalities.
- Linked the aid registries to the census undercount debate in canon wording (registries "among the sources"; no "proof").
- Added a criticism section covering ISEZ, ATR and human-rights complaints, and the frozen-conflict argument.
- Removed peacock wording ("playing a vital role", "fosters mutual confidence") and duplicated boilerplate.

##### NurGaz (Vol1, 3.22)
- **[CANON]** Rewrote the export route. Crude now goes through the 85-km Northern Export Feeder (built by the IPTC from 1998) into the KazTransOil network near Shymkent, for refining there or onward shipment to Russia. Removed the claim of a CPC connection and Black Sea tanker terminals, and stated that there are no southern export pipelines.
- **[CANON]** Production is now about 120,000 bpd as NurGaz's own figure, with an independent estimate of 85,000–100,000 bpd. The old 48,000 bpd figure, still used in other articles, is recast as the 1996 low.
- **[CANON]** Iradneft was privatized into NurGaz in May 1993 under Kamran Bekzatov (consistent with Vol1 3.9). Hidden lore: Bekzatov's coup plot does not appear as fact. Only 2022–23 tabloid stories are mentioned, which analysts dismissed as palace intrigue.
- **[CANON]** Corrected the Trans-Irad Gas Pipeline. The CNPC proposal would leave Irad through Kyrgyz territory, not "across southern Irad toward western China".
- **[EXPANDED]** About 400 to about 1,070 words. New sections: Soviet period, Privatization, Export route, Since 2006, Production, Refining, Natural gas, Ownership and management, Role in politics and society, Environmental record.
- Reconciled the refinery with other articles: opened in the 1950s (Chernov worked there from 1958), expanded in 1974, 50,000 bpd nameplate (Vol3 stub) and about 31,000 bpd throughput.
- Retitled the link [[Nurzhan Petroleum Engineering Polytechnic]] to [[Nurzhan Polytechnic Institute]], per brief §11.
- Kept existing canon on Chevron and Lukoil neutral, with no new negative claims about real companies. The KazTransOil citation is kept per brief §5.
- Removed CSR puffery ("cementing the company's central position in urban civic life").

##### Attelkom (Vol1, 3.23)
- **[CANON]** Origin is a 1994 US defense contract for Talas AB, given to an unnamed consortium of US contractors (no real company named), with privatization in 1999 (baselore).
- Fixed the description of IradOne as a "state media regulator": IradOne is a broadcaster.
- Changed "executive authorities at Boz-Korgon" to "the ISEZ executive", since the government denies that Boz-Korgon is the seat.
- Moved the main data center to Nurzhan to match [[Attelkom Data Center]], and placed the HQ in western Talas to match Talas 2.1. Added the Boz-Korgon relay-station origin (Boz-Korgon 3.3), Maksat's board role (Aidar Maksat 3.6) and Director-General Samat Kasymov (Vol3 stub).
- **[EXPANDED]** About 450 to about 760 words. Added a history from the Soviet network to 4G, the 2007–08 license annulment, ownership opacity (attributed), the 2008 security directives, the 2023 protest shutdown, the 2024 blocking of sites that questioned the Governor's videos (allegation framing kept), and consumer criticism.
- Removed padding about compression algorithms and municipal sirens "ensuring" alerts.

##### Chongtor Horse (Vol1, 3.24)
- **[CANON]** The breed claims are now presented as national belief versus genetics. The Botai origin is national historiography. Genetic studies (Gaunitz et al. 2018; Librado et al. 2021, real works cited only for general science) indicate that Botai horses were ancestral to Przewalski's horses and that modern domestic horses came from the Volga–Don steppe. The in-world genetic study places the Chongtor within the Central Asian mountain-horse cluster. Added the Kyrgyz view that it is a local strain.
- **[CANON]** The horsemeat taboo is now framed as a popular prejudice per brief §5, replacing "treating equine slaughter as a cultural crime".
- Replaced the unverifiable "veterinary studies demonstrate…" with "studies have reported…". Removed "renowned throughout Central Asia", "indispensable", "international acclaim" and "massive flocks".
- **[EXPANDED]** About 450 to about 910 words. Added studbook details (registry founded 1993, about 23,600 horses and 640 stallions, testing rules, *sanjyra*), the Soviet crossbreeding history, uses (El-Choro, UNMI hire, *kun*), and the foundation sire Almanbet (Vol3 stub).
- Replaced the fake-journal citations (an Irad-specific article in the real *Journal of Equine Science*; the "International Studbook Federation") with in-world sources.

##### Akyel Horse (Vol1, 3.25)
- **[CANON]** The Dayuan and Fergana-horse descent is now tradition, not fact. Zhang Qian's visit is dated to about 128 BCE and the war to 104–101 BCE, per brief §5. Genetic affinity to the Akhal-Teke is stated, and continuity with Dayuan cannot be demonstrated.
- Corrected the explanation of the coat sheen. "Hollow hair-shaft refraction" became the Akhal-Teke-style reduced or absent medulla.
- **[EXPANDED]** About 450 to about 1,010 words. Added a history running through the Soviet near-extinction (1956 survey at Chong-Talas Stud Farm), the 1995 Syndicate, DNA testing in 1998, Iradimania and US demand (original wiki), and Toktarov's horse Zharkyn and the Akyel Breeding Sanctuary (Vol3 stubs). Added studbook figures, 2023 export figures, and criticism (State Stud funding, inbreeding, Turkmen breeders' view).
- Removed the real Levine (1999) paper and the fake journal citations. Cited the *Shiji* only for the general Han and Dayuan history.
- Removed puffery ("aristocratic", "luminous", "international acclaim at prestigious expositions").

##### IradOne (Vol1, 3.26)
- **[RETITLED category only]** Changed the assessment line from "Category: Arts & Cinema" to "Category: Media & Broadcasting", because a broadcaster is not a cinema topic. The article title is unchanged.
- **[CANON]** Programming is primarily in English, with the Russian-language sister channel ИрадОдин (IradOdin) and its lower production values (newlore). DPI editorial control is attributed to press-freedom groups and the OSCE, alongside Toktarov's free-press claim. Alikhan Toktarov's chairmanship since June 2015 is stated as public fact.
- **[CANON]** The Governor's broadcasts appear only as allegations. "Opposition outlets and independent technology monitors allege signs of digital synthesis…; officials dismiss as foreign-sponsored disinformation", in the brief's wording. "Withdrawal to Boz-Korgon in mid-2024" was removed, since the absence is now framed with the DPI health-retreat line.
- Moved the HQ to the [[Alikhan Media Center]] and the mast to Television Hill, to match the Vol3 stubs.
- **[EXPANDED]** About 450 to about 1,250 words. New sections: Soviet broadcasting, Territorial period (Public Broadcasting Act 1993), Under the ISEZ (2007 decree, IradOdin in 2009, Alikhan's 2015 appointment, the 2017 move, the 2018 digital switchover, Jason Ilyasov from 2016), Organization and finance, Channels and services, Programming, Audience and reach (including the ATR language barrier), Editorial control and criticism.
- Removed "award-winning documentaries", "seminal role" and boilerplate about archives. Replaced the *Eurasian Media Review* and *Ethnomusicology* citations with in-world sources.

##### Winter Uprising of 1992 (Vol1, 3.27)
- **[CANON]** The dates are now winter 1991–92. The uprising runs from the December 1991 protests to the capture of Talas in February and the 11 March 1992 proclamation by the Provisional Government. This replaces "January 12 – March 11, 1992".
- **[CANON]** Fixed the claim that "the Supreme Soviet dissolved itself" and that the regime collapsed. The SRI government in Kobozev did not recognize the proclamation and launched the First Civil War in late March.
- **[CANON]** Stated that the SRI ruling elite was largely ethnic Russian and covered the ethnic and religious dimension (Russification, church closures, 1956; departures of Russian residents with hedged numbers).
- Reconciled the chronology with First Iradi Civil War 2.6 (3 February OMON shootings; arsenals seized within three days), Amanbek Alimbekov 4.96 (Ene-Til; Town Hall Meeting in the municipal theater) and the Vol3 stubs (Zamirbek Bakiev, Kuban Mamytov, Talas Town Hall Meeting). Kept the chunk's 14 January rail strike and the 18 February March of the Thousand Saddles.
- Hedged the casualty figures (11, 27 or 46 for 3 February; 60–150 overall; "archival estimates vary").
- Removed the unsupported "National Solidarity Day (24 January)" holiday. Commemoration now runs through Irad Day (11 March) and a 3 February memorial service.
- **[EXPANDED]** About 450 to about 1,050 words. Removed the irrelevant Pierce (1960) citation and the US State Department *Dispatch* citation with its fake volume and issue numbers.

##### Church of Saint Janyl (Vol1, 3.28)
- Title kept as instructed. The lead bolds "Church of St. Janyl" with "Church of Saint Janyl" as an alternative, and the prose uses "St. Janyl" throughout.
- **[CANON]** Fixed "inscribed on the UNESCO World Heritage Tentative List". The church was inscribed on the World Heritage List during the territorial period on a US nomination, with the US as State Party; I chose 2003. Added that Irad is not a State Party and that UNESCO still lists the property under the US. Added a short contrast with the Kazakh–Kyrgyz serial nomination of the Kariz and Rabat-i-Safed. Removed the irrelevant 2014 Silk Roads citation.
- **[CANON]** The 1727 Kokand charter is attributed to Abd al-Rahim Biy (r. 1721–1733, called "ruler of Kokand" rather than "Khan", which is anachronistic) for Dzungar-war service, and linked to [[Treaty of Talas (1727)]]. Joseph Wolff is cited as giving the first Western description, with no new actions or quotes added.
- **[CANON]** The church is presented as a symbolic re-creation of the lost First Church of Janyl, Janyl's historicity is disputed, and the White Rider tradition is included (newlore).
- Harmonized the details with Iyık Janyl 3.12: 28-m dome (was 22 m), masons from Samarkand and Kashgar, walnut portals, stained glass, reconsecration on 14 September 1992, grain-store use after 1937. The stained glass is presented as a 1990s addition, to explain its presence in an 18th-century building. Replaced the anachronistic "Old Turkic script" inscriptions with Turkic in Syriac script.
- **[EXPANDED]** About 450 to about 1,300 words. New sections: Background, Construction, 19th century, Union with Rome and the Soviet period, Restoration and World Heritage listing, Architecture, Religious life, Conservation and controversies (cement-mortar restoration, Latinization debate). Merged the two duplicated crypt and conservation sections.
- Removed "celebrated masterpiece", "paramount", "living symbol" and similar wording.

Untouched articles: none (all nine edited). Merges or deletions within the chunk: none (no duplicates found).


## Part E. Volume 2 (C-class): per-article edits


### Chunk D1

### Changelog: chunk D1 (Vol2 C-class 4.1–4.22)

General (all 22 articles):
- **Structure.**
  - All 22 headings are unchanged, in the same order.
  - The volume header block is untouched. No retitles, merges or deletions.
  - Sub-sections inside articles use `####`, so no unnumbered `###` headings remain.
- **Lists.** Converted every crammed "- **A**: … - **B**: …" paragraph into a real list (Talasfilm Archives, East Syriac Rites, Migration System, Directorate).
- **Citations.**
  - Added `<sup>[n]</sup>` markers, which did not exist before, matched to sequential `<ol class="references">` lists.
  - Replaced fabricated articles attributed to real periodicals (*Cahiers du Cinéma* No. 492, *Ethnomusicology* vol. 64, *Journal of Equine Science*, *Annuario Pontificio* pages) with in-world sources.
  - Changed the Folklore Society publisher from Academic Press, a real imprint, to Talas State University Press, matching the A-chunk editors.
- **Language and style.**
  - Iradi native names are now in Latin script (Iradi has used Latin since 1992). Cyrillic is kept only for Soviet-era Russian titles.
  - Cut puffery throughout: masterpiece, celebrated, iconic, revered, universally, breathtaking, state-of-the-art, global powerhouse, Olympic-standard, "living soul of national consciousness".
  - Removed the repeated closing boilerplate ("continues to inspire…", "symbolizing enduring steppe pride…", "ensuring the transmission of ancient…").

##### Nurlan Sadikov (Vol2, 4.1)
- **[CANON]** Made Sadikov the director of *Zarina* (1968), as Irad_Wiki_Original and baselore have it, and recorded it as the first Iradi film shown to a wider Soviet audience. Added his lost early films *Kok-Terek* and *Tolkun*, shown only locally.
- **[CANON]** Changed his birth year from 1942 to 1931. The Vol3 stubs date *Kok-Terek* to 1959 and *Tolkun* to 1963, which a man born in 1942 could not have directed. Kept the day and month.
- Removed the claim that he studied under Grigori Chukhrai, a real person who was not teaching at VGIK in the 1950s.
- Added a death date (January 21, 2017) instead of leaving him alive at 95. This is my own decision; see notes.
- Removed "Locarno" retrospectives.
- **[EXPANDED]** Rewrote as a full biography:
  - early life and VGIK (1952–57);
  - early films; the confused reception of *Zarina* and the "formalism" charge;
  - the documentary years (*Naryn*, 1975, on the Toktogul dam);
  - *Desert Sun’s Rebellion* and the Iradi Western;
  - artistic director of Talasfilm Studios (1989–95), including the rescue of negatives in winter 1992;
  - founding director of the Talasfilm Archives (1995–2008);
  - style (two strands), legacy and a selected filmography.

##### Beknur Karimov (Vol2, 4.2)
- **[CANON]** Restored him as a Soviet-era director. The old text made him born in 1966 and active in the 1990s, with *Zalmax's Dominion* as a 1994 post-Soviet film; canon has a Soviet attempt to remake *Zardoz*, a self-described "pervert of the screen", and a Soviet ban for refusing to cut sexually explicit scenes.
- He is now born in 1941 in Kobozev, a Talasfilm set designer from 1961, and attended the Higher Courses for Scriptwriters and Directors.
- **[EXPANDED]** New sections:
  - *Zalmax's Dominion* (1977): closed screening of *Zardoz* in Moscow in 1975, pitched to the committee as an "ideologically corrected" parable;
  - the origin of the phrase in the 1981 minutes of the artistic council;
  - *Kyz Bulak* (1982), shelved after he refused Goskino's demanded cuts; dismissal and ban in 1983;
  - release of *Kyz Bulak* in 1988 by the Union of Cinematographers' Conflict Commission;
  - post-1992 video work, the IradOne non-broadcast, and his cult following among Zoomers and Mor-Wave performers.
- Removed the "Transoxian Wave", the Rotterdam, Berlin and Venice claims, and the *Cahiers du Cinéma* citation.

##### Yusup Ayyubov (Vol2, 4.3)
- **[CANON]** Kept him as an actor; baselore lists him as the star of *Desert Sun's Rebellion*. Fixed *Rise of Glory* from "1988, his definitive lead role as a 1916 chieftain" to the 1979 film, in which, as canon says of nearly every actor, he appears in a single scene: the 1916 chieftain episode.
- Fixed the *Zarina* role to Bolot, a rider-band leader in a Kokand-era story, instead of an anachronistic "partisan commander". Tied the State Prize of the Iradi SSR to *Desert Sun's Rebellion*.
- Cut "preeminent screen icon of Central Asian cinema" and attributed "Face of the Steppe" as a press nickname.
- Added People's Artist (1981), burial in Iyık Janyl and a selected filmography.

##### Mor-Wave (Vol2, 4.4)
- **[CANON]** Moved the origin from "early 2010s, tüntolk demo 2015" to the late 1990s in post-industrial Nurzhan boiler rooms, with tüntolk's *Jolchu* (1999). This matches baselore and Vol1 "Nurzhan".
- **[CANON]** Restored the canon elements: Iradi lyrics drawing on pagan Turkic imagery and mythology; the themes of nature, transformation and existentialism; the Mor-Pop and Mor-Folk subgenres; and live performance art drawing on Iradi Soviet cinema.
- **[EXPANDED]** Restructured as a music-genre article:
  - Etymology (*mor* "violet/dusk", with the competing Morkhan reading);
  - History: origins 1996–99, first wave 1999–2007, contraction in the 2007 war, second wave from 2014 among Zoomers;
  - Characteristics (as a list);
  - Live performance;
  - Subgenres (linked to Mor-Pop and Mor-Folk);
  - Reception and controversy: church objections to Morkhan imagery, a cancelled 2019 concert in Iyık Janyl, and use at the 2023 student protests followed by IradOne pulling videos (attributed to the *Talas Herald*).
- Reworded the Alikhan Toktarov link. It no longer has him personally curating programs; IradOne launched a youth channel after he became board chairman in 2015, which is public per Vol1 "Alikhan Toktarov".

##### tüntolk (Vol2, 4.5)
- **[CANON]** Changed formation from Talas in 2014 to Nurzhan in 1997, with *Jolchu* (1999) as the debut. This matches baselore.
- The 2015 demo EP *Zvezda Irad* became a 2002 EP, and *White Stallion in Fog* (2017) is recast as the comeback album after a 2007–2014 split.
- Name: changed the gloss from "Night Fox" to "night wave" (*tün* + *tolkun*), in tribute to Sadikov's lost film *Tolkun*. The foreign-press "Night Fox" is now explained as a misreading of *tülkü*.
- Changed the Russian-titled single "Stepnoy Veter" to the Iradi "Chöl Shamaly" ("Desert Wind"), since the band writes in Iradi.
- **[EXPANDED]** Band-article structure: Name; History (formation; territorial era; reunion); Musical style and performance; Members; Discography; Legacy. Removed "Universally acknowledged" and "seamlessly merge".

##### Desert Sun’s Rebellion (Vol2, 4.6)
- **[CANON]** Reframed the film from a "historical western with a 30-minute cavalry battle" to the canon "tense thriller with a spaghetti Western aesthetic" that created the Iradi Western, or Soviet Western. Restored the Walter Goodman *New York Times* quote verbatim, as in Irad_Wiki_Original; no other real-person quotes were added.
- **[EXPANDED]** Full film-article structure:
  - Plot: 1922, an escort of requisitioned horses across the desert, a shadowing warlord, poisoned wells, a mutiny, a noon standoff on a salt flat and an ambiguous ending;
  - Cast;
  - Production: Goskino-era approval as a Civil War "Eastern"; summer 1978 location shoot in Kara-Suu Canyon; Italian-western influence through closed screenings; komuz, guitar and whistling score;
  - Release: about 17.9 million viewers in the first year; 1980 All-Union Film Festival Special Jury Prize; New York screening in 1979;
  - Reception, attributed;
  - Legacy: the 1980s Iradi Western canon titles and the 2004 restoration shown at the 2005 Talas IFF.
- Removed the 18 million round figure, the "Dushanbe" festival placement (unverified), "4K prints studied in international film schools", and the "genuine flintlock rifles preserved in the State Archives".

##### Rise of Glory (Vol2, 4.7)
- **[CANON]** Rewrote completely. The old article described a 1988 two-part film about 1916 that won a Nika Award and the Tashkent Grand Prix; the Nika did not exist before 1988.
- The new article follows canon: a four-hour 1979 epic from the first tamed horse to the present-day Iradi SSR. It has an hour-long real-time horse-taming opening, expository monologues over a black screen, actors appearing in single scenes, a first-to-second-person switch in the narration halfway through, a reported Leningrad cinema riot, and polarized opinion. Kept Talgat Osmonov as director.
- **[EXPANDED]**
  - Synopsis by episode, including the 1916 episode with Ayyubov, which keeps D2's "Lost Tribes" cross-reference true.
  - Production: commissioned for the 1975 fiftieth anniversary of the Iradi SSR and four years late. The one-hour "single take" is explained by the ten-minute limit of a 35 mm magazine, with hidden joins where horse and man leave the frame. This plausibly reconciles canon's "no cuts".
  - Release in two parts in 1979–80, with the riot presented as unconfirmed reports.
  - Reception, legacy and the 2019 restoration.

##### Zarina (film) (Vol2, 4.8)
- **[CANON]** Changed the director from "Kadyr Toktomushev" to Nurlan Sadikov. Changed the genre from lyrical feminist drama to the canon "period action-adventure" whose non-linear narrative and disturbing visuals confused audiences.
- Removed the fabricated Karlovy Vary FIPRESCI prize.
- **[EXPANDED]**
  - Plot as given in the studio's release notes, keeping the existing heroine, *kyz kuu* race and bride price.
  - The non-linear structure: the race shown four times and unmarked dream sequences, including a bull-masked Morkhan figure.
  - Production: Viktor Pak, a Koryo-saram cinematographer; restructuring in the edit; the church-bell appeal kept from the old text.
  - Release ("formalism", withdrawal) and legacy (2014 restoration, feminist readings).

##### Zalmax’s Dominion (Vol2, 4.9)
- **[CANON]** Rewrote completely. The old article made it a 1994 post-Soviet surrealist film about a surveyor that premiered at Rotterdam, with Tarkovsky and Béla Tarr comparisons. It is now the canon 1977 Soviet attempt to remake *Zardoz*, dismissed as incomprehensible and later a cult film for its dadaist absurdity.
- **[EXPANDED]**
  - Plot: the *Zardoz* outline with a floating stone horse head, plus Karimov's absurd set-pieces.
  - Cast.
  - Production: the closed screening, the script approved as an anti-bourgeois parable, the absurdist episodes shot unscripted, and a plywood head because the budget allowed no helicopter.
  - Release in limited prints, with walkouts.
  - Cult status through 1990s bootleg VHS and student midnight screenings; the 2011 restoration.

##### Talasfilm Archives and Film Preservation (Vol2, 4.10)
- **[CANON]** Separated the archive from the studio: Talasfilm Studios was founded in 1954 (Vol3), the depository in 1958, and the independent institute in 1995 by Territorial Legislature act, with Sadikov as director from 1995 to 2008. Added the Irad Film Society and Talas IFF link from newlore.
- **[EXPANDED]** New History section:
  - Soviet deposit of original negatives at Gosfilmofond, which explains the lost Sadikov films;
  - the 1992 rescue;
  - the restoration program, with a list of restoration dates consistent with the film articles;
  - repatriation talks with Gosfilmofond;
  - the 2007 closure;
  - ISEZ funding.
- Rebuilt the crammed Collections list. Added a Public access section (restricted access to 1992–2007 footage).
- Cut "state-of-the-art 4K scanners" and "unhindered access".

##### Burkut Saluu (Vol2, 4.11)
- **[EXPANDED]**
  - History: medieval; Soviet-era fur procurement and decline; 1995 revival under the Directorate.
  - Practice: birds, with nestling vs. passage capture; training as a list; equipment; season; *taigan* hounds.
  - Customs: release after 10–12 years, no sale of eagles, priestly blessing.
  - Competitions: Salburun, as a list.
  - Contemporary status: 71 registered hunters in 2022; permits; CITES; Irad is not a UNESCO State Party, so it is outside the falconry listing.
- Removed the "250 km/h dive" claim, which describes stooping from height, not hunting from the fist. Corrected the hood term to *tomogo*. Linked the Chatkal Golden Eagle.

##### Ulak Tartysh (Sport) (Vol2, 4.12)
- **[CANON]** Irad has no president. The cup keeps the name "President's Cup", used in Vol1 "Alikhan Toktarov", now explained as instituted in 1992 by Provisional President Alimbekov and also called the Independence Day Cup (Vol1 2.7). It is played in the week of Irad Day at the Irad State Hippodrome (Vol3), replacing "Central Hippodrome". Goal term: *tai-kazan* (baselore).
- **[EXPANDED]**
  - History: origin legends, the free-for-all tradition, 1953 Soviet codification, post-1992.
  - Rules of the regulated game as a list: 12-player squads with 4 mounted, field, goal, carcass, halves, fouls, referees.
  - Traditional free-for-all form in the ATR.
  - Horses.
  - Competitions: a 24-team league split between ISEZ and ATR; IradOne rights; UNMI-supported cross-line exhibition matches.
  - Criticism.

##### Iradi Horsemeat Taboo (Vol2, 4.13)
- **[CANON]** Framed the "horsemeat is a Muslim practice" view as a popular prejudice, as brief §5 requires. Ethnographers note that it ignores the pre-Islamic pastoral roots of Kazakh and Kyrgyz practice and that Hanafi law historically classed horsemeat as *makruh*, and they trace it to Christian identity-marking, comparable to the eighth-century papal ban among Germanic converts.
- Church tradition (the Janyl covenant) is now attributed. Removed the claim of "canonical dietary law" codified by clergy.
- **[EXPANDED]**
  - Scholarly explanations as a list: identity marking, horse veneration (with the domestication belief flagged as unsupported by genetics), and adaptation of the *tul at* funerary custom.
  - Law: a 1996 Territorial Legislature act, replacing the "Alimbekov-Baker Treaty statutes"; enforcement among minorities and in the ATR.
  - Food: Iradi plov and beet suzma per newlore; beef *kazy*.
  - The bovine-omen irony per brief §5 (bulls and black cattle, Morkhan; the US-era beef industry), with no negative claims about real companies.
  - Social practice.

##### Fallen Rider Tradition (Vol2, 4.14)
- **[CANON]** Corrected the flag description: the inverted horseshoe sits on the hoist side of the stallion, not "surrounding" it. Removed the unsourced "golden". Matched the memorial list to newlore: 1916, the Soviet purges, the civil wars.
- Fixed the mixed-script Iradi name "Ygylgan Attyn салты" to *Jygylgan Atchan Saltı*.
- Added the contrast with the Kazakh and Kyrgyz custom, in which the dead man's horse is slaughtered at the memorial feast, while the Iradi horse is freed (*azat at*), linked to the horsemeat taboo. Added the household inverted-horseshoe custom and use on the August 15 Lost Tribes commemoration. The flag-memorial list is now a real list.

##### Arsha Juniper Incense Tradition (Vol2, 4.15)
- Reconciled the Vol1 inconsistency ("replaces" vs. "alongside" frankincense): rural rite uses arsha alone, and Latinized urban churches mix it with frankincense.
- Replaced "jinns" with the steppe demon *albarsty*. Added the species range and altitudes, conservation and bazaar trade, and the occasions of the *alastoo* rite.
- Replaced the Vine (1937) citation, a real book that does not cover Irad-specific claims, with the Cathedral Archives.

##### Kümöch Sacramental Bread (Vol2, 4.16)
- Added a Background section. It notes that East Syriac churches normally use leavened bread with the holy leaven (*malka*) and gives the two scholarly explanations for Iradi unleavened bread. Canon unleavened kept.
- Reconciled the seal designs with Vol1 (the cathedral stallion seal vs. the parish cross-and-Polaris seal). Moved baking from an invented "Monastery of Saint Janyl" to the Order of St. Janyl the Hermit motherhouse (Vol1). Removed "Talas salt flats".
- Replaced the *Annuario Pontificio* citation.

##### Dayuan Heavenly Horse Heritage (Vol2, 4.17)
- **[CANON]** Chronology per brief §5:
  - Saka movement in the 140s–130s BCE;
  - Zhang Qian left in 138 BCE and reached Dayuan around 128 BCE (the old text said he "traveled in 138 BCE");
  - the War of the Heavenly Horses ran 104–101 BCE: the failed first expedition, then the 102–101 siege and the king killed by his nobles;
  - Han took several dozen fine and about 3,000 ordinary horses.
- **[CANON]** The Botai domestication claim is now presented as a national belief contradicted by genetic studies since 2021. "Five-thousand-year continuity" is attributed to breed-society promotion.
- **[EXPANDED]**
  - Talas-valley Han finds treated as trade evidence (hedged).
  - Akyel descent: the Syndicate claim set against independent genetic caution.
  - The "sweating blood" parasite explanation.
  - Emperor Wu's hymns.
- Citations are now the Watson *Shiji* translation (real; general history) and Librado et al. 2021 (real genetics). The fabricated *Journal of Equine Science* article was moved to an in-world journal.

##### East Syriac Rites of Iyık Janyl (Vol2, 4.18)
- Corrected the origin dating. Church tradition dates the Iradi church to Janyl in the twelfth century; Sogdian missions from the sixth century are general history. Vernacular translations are dated to 1993 by the synod, replacing "after Vatican II", which is implausible under Soviet rule.
- Fixed "Saint Ephrem Theatrical Academy" to the major seminary of St. Ephrem (Vol1).
- **[EXPANDED]**
  - History: persecutions, clandestine chant, 1931 union, 1937 closures, 1993 revision.
  - Liturgy: Addai and Mari plus the two further anaphoras; *bema*, *madbaha*, *'onitha*; Sogdian-root vocabulary (*kuble*, *iyık*); the Rogation of the Ninevites.
  - Pastoral rites as a real list, with pasture blessings and tent chapels added.
  - Latinization and the urban–tribal divide.

##### Janyl, Mother of Irad (Vol2, 4.19)
- **[CANON]** Changed the dating from "late thirteenth century under the Chagatai Khanate" to tradition's twelfth century under the Qara Khitai (some chronicles say eleventh), matching Vol1 "Syro-Iradi Catholic Church" and "Iyık Janyl" and the Original. Historicity is now stated as widely disputed and the First Church's location as unknown, per newlore.
- Made it complementary to 4.20: this article covers hagiography and veneration only.
- **[EXPANDED]**
  - Hagiography: the eighteenth-century vita; the White Rider vision, with the Polaris variant reconciling Vol1 "Iyık Janyl" and Vol3 "Legend of the White Rider"; covenant customs attributed to tradition.
  - First Church: candidate sites listed.
  - Veneration: cult history, Soviet ban, August 24 feast.
  - Iconography.
  - National symbol.
- Removed "living soul of Iradi national consciousness" and "absolute prohibition" stated in Wikipedia's voice.

##### Janyl (Historical Figure) (Vol2, 4.20)
- **[CANON]** Rewrote it as the article on historicity and sources. The old text called her "an authentic political and military leader", which contradicts newlore's "historical existence widely disputed". Dating aligned with 4.19.
- **[EXPANDED]**
  - Historical setting: Qara Khitai tolerance; Shar-i-Kuhna's eleventh-century foundations and 1240–1338 gravestones (from Vol2 4.27).
  - Sources: the eighteenth-century vita; the epic *Janyl Baatyr*, with its parallel to the real Kyrgyz epic *Janyl Myrza*; Bar Hebraeus, who gives the earliest mention of "Irad" (baselore) but does not name her; archaeology, where the "Ioanna" ring is now a contested thirteenth-century find rather than proof.
  - Three scholarly positions as a list.
  - Historiography and politics: Soviet, post-1992 textbooks, and the church's position.
- Moved the old statue and "supreme unifying symbol" material to 4.19 in neutral form. Not merged: the two articles now have distinct scopes.

##### Central Asian Pastoral Migration System (Vol2, 4.21)
- **[CANON]** Replaced "primary livelihood for over three million rural citizens" with a hedged statement tied to the census controversy (brief §2).
- Removed "perfected by the Botai horizon".
- Fixed the seasonal terms: spring *jazdoo*, autumn *küzdöö*, which had been mislabeled as spring.
- **[EXPANDED]**
  - Seasonal cycle as a real list, with vertical and long-distance routes to the Moiynkum, Betpak-Dala and Kyzylkum fringe, and herd composition.
  - History: Bronze Age; Russian land seizures; the 1932 Collectivization Decree (linked); Soviet brigade herding; the 1970s Toktogul reservoir flooding pastures; post-1991 decollectivization; territorial-era aid.
  - Governance: *adat*, cooperatives, ISEZ permits.
  - Contemporary problems as a list: uneven grazing, disease, *jut* winters, and Qara-Chik line crossings under UNMI-negotiated corridors.

##### National Equestrian Sports Directorate (Vol2, 4.22)
- **[CANON]** Irad has no president. The President's Cup is explained as Alimbekov's 1992 cup. The director is appointed by the Governor. HQ is the Irad State Hippodrome (Vol3), replacing "Talas Central Hippodrome".
- Cut "Olympic-standard", "global powerhouse" and "spectators from across Eurasia".
- **[EXPANDED]**
  - History: the Soviet sports committee; the 1993 Territorial Legislature act; post-2007 ISEZ control and limited ATR authority.
  - Functions and sanctioned disciplines as real lists (tyin emmei and flat racing added).
  - Facilities; breeding links.
  - International: not admitted as a national team to the World Nomad Games because all three neighbors claim Irad.
  - Criticism: patronage and animal welfare.

Untouched articles: none (all 22 edited).


### Chunk D2

### Changelog: Chunk D2 (Vol2 4.23–4.42)

##### 1956 Talas Riots (Vol2, 4.23)
- **[EXPANDED]** Rewrote from 3 short sections (~330 words) to a full article (~1,450 words): lead, Background, The checkpoint incident, Course of the riots, Arrests/trials/deportations, Soviet treatment, Historiography and memory. Done to meet the history-article expansion priority.
- **[CANON]** The widow's-horse shooting is now framed "according to popular accounts". The article notes that the internal security report calls it accidental and that popular versions call it deliberate, and links [[Talas Checkpoint Incident (1956)]]. This follows brief §5.
- **[CANON]** Added the underlying causes historians cite: housing allocation favoring incoming Slavic specialists, wage and skill segregation, Russian-only schooling, church closures and the 1954 anti-religious campaign, collectivization and wartime horse requisitioning, and the 1956 Thaw (secret speech, amnesties, Tbilisi). Done per brief §5.
- **[CANON]** Corrected the arrest figure from "over four hundred" to more than 1,000 detained, with about 400 charged, per baselore and the original. Casualties are hedged (14 dead in internal security reports versus "several dozen" in Iradi research), as are deportations (300 to 700+, "estimates range"). Done per brief §5.
- Added Russian-residents and Russo perspective: the violence against Russian property and residents (canon), Iradi families who sheltered neighbors, and the "pogrom" reading among older Nurzhan residents. Done for neutrality.
- Removed "motorized rifle detachments from the garrison at Talas Air Base" (anachronistic). Replaced it with Turkestan Military District units plus internal troops flown in to the 1952 air-defense airfield, linked to [[Talas Air Base]]. Removed water cannon and tear gas.
- Removed puffery and editorializing ("enduring watershed", "proving that deep reverence for equine life…", "crucial catalyst"). Fixed the Iradi name (*topolongu*).
- Replaced the irrelevant Pierce (1867–1917) citation with Kozlov, *Mass Uprisings in the USSR* (2002), plus in-world sources (TSU Press 2006, CAGR 2016, *Talas Herald* 1996). Added inline citation markers.
- Added a 1996 riderless-horse memorial and annual June 14 gatherings.

##### Semirechye Revolt (Irad) (Vol2, 4.24)
- **[EXPANDED]** Expanded from ~330 to ~1,600 words with Background, The mobilization decree, The revolt in the Iradi districts, Suppression, The flight to China, Aftermath, and Historiography and memory.
- **[CANON]** Added real history: the June 25 (July 8 NS) 1916 decree, inorodtsy aged 19–43, the 250,000/230,000 quotas, list corruption, Khujand (July 4) and Jizzakh, the Semirechye rising in August, Kuropatkin's appointment and punitive expeditions, settler militias, flight in autumn and winter 1916–17, high mortality (hedged "tens of thousands to more than 100,000"), the Provisional Government's return amnesty and the 1917–20 famine.
- **[CANON]** Credited the 1876 conquest of Kokand to Skobelev (brief §5). Restated the Civil War aftermath per brief §5: Iradi irregulars fought with the Red Guards against the Kokand Autonomy (Feb 1918), and volunteers served on the Transcaspian front against the Whites and a small British force. There is no "British at Kokand".
- **[CANON]** Kept the Iradi angle: clan councils, horse oaths (attributed to tradition), Kara-Suu ambushes (flagged as oral tradition), the Lost Tribes, post-1916 inter-clan organization, the Nechayev/Bakunin *Catechism*, and the flag's crimson field and inverted horseshoe.
- Changed "Qing borders of Xinjiang" to the Republic of China under Yang Zengxin. Removed "industrial firepower" and "harrowing" phrasing. Noted that Iradis were classed as inorodtsy despite being Christian.
- Added historiography covering the Tsarist, early Soviet, Stalinist "reactionary" and post-Stalin readings, Western scholarship, the genocide-term debate and the 2016 centenary.
- Replaced Hopkirk's *Great Game* (which ends in 1907) with Sokol (1954), Chokobaeva/Drieu/Morrison (2019), Brower (2003), State Archives Fond 108 and TSU Press (2016). Added inline citations.

##### Iradi Soviet Socialist Republic (Vol2, 4.25)
- **[EXPANDED]** Expanded from ~330 to ~2,000 words with Name, Establishment, Korenizatsiia, Collectivization and famine, Union with Rome and the purges, Russification, Deportations, WWII, Postwar industrialization, The Khrushchev and Brezhnev eras, Perestroika and independence, Government, and Legacy and historiography.
- **[CANON]** Removed the claim that it was an "autonomous republic in 1925, elevated to union republic under 1936 Constitution". It is now a union republic from 1925, admitted after the Uzbek and Turkmen SSRs (brief §4).
- **[CANON]** Corrected "Kobozev constructed in the 1930s to process petroleum". Kobozev is now a planned capital beside a lower-Chu railway settlement, named in 1927 after Pyotr Kobozev, and a Turksib junction. Oil is dated to the 1949 discovery (brief §4; original).
- **[CANON]** Added the 1931 *Orientalis Stella* union negotiated by Mar Timotheos Alimbekov, with Soviet suspicion of the Vatican link feeding the 1937 purges; the end of korenizatsiia by 1937; the 1938 Russian decree; the 1941 Cyrillic mandate; and 1937 Koryo-saram deportation details matched to the Koryo-saram article.
- **[CANON]** Corrected the dissolution: "declaration of state sovereignty ... dissolution ... Winter Uprising" was replaced with: the Communist Party of Irad declared independence on 9 Oct 1991 (Declaration of State Sovereignty) and created the Socialist Republic of Irad; Kobozev was renamed Nurzhan by Alimbekov after the civil war ended in 1992 (brief §4, never "until 1991").
- **[CANON]** Removed "refined antimony for Soviet tank manufacturing" in WWII. Sary-Bulak is dated to 1961 per newlore, with the 1971 directive and Mailuu-Suu uranium (1940s–late 1960s) added. Toktogul (1,200 MW) is described as completed in the 1970s.
- Corrected "largely adhering to Eastern Syriac Christianity" (pre-1931 framing, now in context). Removed the misleading claim that collectivization closed the Iyık Janyl churches, moving closure into the 1930s anti-religious repression.
- Linked the existing event stubs: First Congress of Iradi Soviets, 1928 Latinization Decree, 1941 Cyrillic Mandate, Decree on Pasture Collectivization (1932), The 1937 NKVD Clerical Purges, 1944 Wartime Mobilization Strike, Nurzhan Oil Discovery (1949), 1952 Kobozev Steel Strike, Founding of Talas Air Base (1952), 1971 Antimony Expansion Directive, The Kobozev Bread Riots (1989), Declaration of State Sovereignty (1991), and Vasily Chernov.
- Replaced the irrelevant "Toponymic Dictionary of the Kirghiz SSR" with Martin (2001), Hirsch (2005), Pohl (1999) and in-world sources. Fixed the Iradi name (*Respublikası*). Added the flag heraldry continuity per newlore.

##### The Lost Tribes of 1916 (Vol2, 4.26)
- **[CANON]** Restored the original canon: the Lost Tribes are specifically the clans that retreated into the eastern mountains in winter and were never seen again, and historians believe they starved or froze. Previously the article had conflated them with the general 100,000-person Urkun to China and with "fragmented lineages". The broader flight is now background, linked to [[The Urkun (Iradi Theater)]].
- Replaced "Qing borders of Xinjiang" with the Republic of China under Yang Zengxin. Removed the unsupported "30,000–50,000 perished" figure attached to the Lost Tribes. Added hedged estimates: 8–12 clans and 3,000–10,000+ people, consistent with "several thousand" in the Talas article.
- Removed the dramatized rear-guard cavalry "sacrifice" narrative. Added sections on disappearance, unverified remains, folk legends (hidden valley, White Rider) and commemoration (August 15 kept; flag horseshoe).
- Changed "landmark four-hour film" to a neutral mention of *Rise of Glory* (1979). Linked *The Black Blizzard of 1916* (Asanaly). Added inline citations.

##### Ruins of Old Iyık Janyl (Vol2, 4.27)
- **[CANON]** Changed "inscribed on the UNESCO World Heritage Tentative List" to inscribed on the World Heritage List in 2004, together with the Church of St. Janyl, on a US nomination during the territorial period. Irad is not a State Party (brief §5). Replaced the wrong 2014 Silk Roads citation with a 2004 nomination file.
- **[CANON]** Founding dated to the 11th century (newlore). Noted that identifying the basilica with the First Church of Janyl is unproven and that the original church's location is unknown (newlore).
- Removed "earliest major urban East Syriac … metropolitan settlement in Central Asia" (false; Merv and Samarkand were earlier). Fixed the broken crammed list into a real Markdown list.
- Added history: Ali-Sultan, the 1338–39 pestilence stones compared to Chwolson's Chu valley stones, Timur's Moghulistan campaigns, and the gap between abandonment and 1727 (clandestine worship per tradition). Added research history, finds, threats (erosion, pilgrims, gravestone looting) and the museum link.

##### Caravanserai of Rabat-i-Safed (Vol2, 4.28)
- **[CANON]** Added the World Heritage dispute section: Kazakhstan and Kyrgyzstan included the site in the 2014 Silk Roads serial nomination, and both the ISEZ (DPI statement) and the IAC protested (brief §5).
- Reconciled "Samanid era" with newlore's "9th-century Sogdian": a Sogdian foundation, with a possible stone rebuilding after the Samanid capture of Talas in 893.
- Removed implausible surviving "iron-bound oak gates" and murder holes, "subterranean" stables, "ingeniously planned", and "finest surviving examples" puffery. Fixed the crammed list. Removed the anachronistic "East Syriac Christians from Iyık Janyl" (9th century). Added later history and conservation. Added inline citations.

##### Andronovo Culture in Transoxiana (Vol2, 4.29)
- Corrected factual errors: Andronovo pottery was handmade, not "wheel-turned"; "deep-shaft mining" became shallow workings; antimony alloying is flagged as unconfirmed; dates align to canon c. 2000–900 BCE.
- Corrected the geography of BMAC contact: the BMAC lay far south, and contact is documented in the Zeravshan and Amu Darya valleys. The Iradi "marches" framing is kept as national historiography. Added the Fergana Chust culture.
- Attributed the Kara-Bulak chariot-slot interpretation and the Chongtor-ancestry claim to Iradi sources, with outside skepticism. Added a Kara-Suu petroglyphs cross-reference and the Legacy/interpretation section.
- Fixed Anthony (2007) missing its year. Added an in-world TSU Press source and inline citations.

##### Botai Culture in Irad (Vol2, 4.30)
- **[CANON]** Reframed per brief §5. Botai (3700–3100 BCE) is in northern Kazakhstan (type site in North Kazakhstan Region, >1,000 km away). Irad as the birthplace of horse domestication is presented as a national belief. Added the 2018 (Gaunitz: Botai horses ancestral to Przewalski's) and 2021 (Librado: DOM2 from the lower Volga–Don c. 2200 BCE) findings. The belief is never stated as fact.
- The claimed Iradi "Botai" sites (lower Talas, Kyzylkum Fringe) are now a disputed attribution by TSU archaeologists, unproven outside Irad. Removed "definitive proof" and "earliest verified" language. Fixed the crammed list. Added the Taylor & Barrón-Ortiz (2021) critique.
- Linked the flag stallion symbolism (newlore), the curricula, [[National Historical Museum of Irad]] (replacing the nonexistent "State Historical Museum") and *Rise of Glory*'s horse-taming opening.

##### Sogdian City-States of the Chu (Vol2, 4.31)
- **[CANON]** Added the brief §5 framing: Sogdiana proper developed in the first millennium BCE and is attested by the Achaemenid period (Behistun). Iradi textbooks' early dating of Chu–Talas settlement is contrasted with archaeological evidence from the 5th–6th centuries CE onward. No hard "900–500 BCE" dates are given.
- Clarified that the best-known upper-Chu sites (Suyab, Navekat, Balasagun) lie in Kyrgyzstan. The Iradi sites are medieval Talas (Talas/Taraz identification per brief §3) and Shelji.
- **[CANON]** Changed the legacy from "urban agricultural vocabulary" to liturgical vocabulary from Sogdian and Iranian roots (brief §2).
- Removed overclaims (letters of credit, wooden legal tablets, "extraordinary religious pluralism"). Added Xuanzang (630), Maniakh's embassy (568), Turgesh coins, the Kashgar–Navekat metropolitanate and al-Kashgari on bilingual Sogdians. Added de la Vaissière (2005) and an in-world source. Linked the Kand/Diz/Rabat term articles and [[Battle of Talas]].

##### Tien Shan Marches (Vol2, 4.32)
- **[EXPANDED]** Restructured into Topography and geology, Passes, Climate and hydrology, Ecology, Human use, Military history, and Protection.
- Fixed "Kara-Bura Pass" to Kara-Buura Pass (rename convention). Corrected the hydrology: the Talas and Kara-Buura drain north, and the Chatkal and Uzun-Akmat drain to the Syr Darya system. Added the Talas–Fergana Fault. Replaced "over four hundred glaciers" with "several hundred".
- Replaced the unsourced "massive herds" fauna list with realistic western Tian Shan fauna (adding Menzbier's marmot). Placed walnut-fruit forest on the Fergana-facing slopes only.
- Placed the Marches on the tribal side of the Qara-Chik line (ATR Talas Alatau and Chatkal Highlands zones). Toned down the El-Choro "repel armored assaults" claim. Added the protected areas, including Aksu-Zhabagly (1926, brief §3 list).
- Replaced the dubious RGS 1904 citation with in-world sources.

##### Oxus River in Iradi historiography (Vol2, 4.33; formerly "Oxus River (Iradi Basin)")
- **[RETITLED] [CANON]** The article claimed the Oxus/Amu Darya drained southern Irad via the Chatkal. This is false: the Chatkal drains to the Chirchik and Syr Darya, and Irad has no Amu Darya territory. Rewrote it entirely as the Oxus's role in Iradi historical geography: the southern bound of Transoxiana / Mā warāʾ al-nahr, the original's "Oxus–Chu–Kyzylkum–Tian Shan" homeland definition, the Soviet-era and post-1992 "Transoxian thesis", nationalist maximalism versus the official cultural usage, and Uzbek criticism.
- Added a short hydrography section (Talas and Chu endorheic, Chatkal to Chirchik, Naryn to Syr Darya, Toktogul and the Aral link, Irad outside the ICWC). Removed the fabricated tugay, otter and "Class V rapids" content and the RGS 1904 citation.

##### Chu River Basin (Vol2, 4.34)
- **[EXPANDED] [CANON]** Rewrote the course to match real geography and the brief. The Chu rises in Kyrgyzstan (Joon-Aryk and Kochkor), is regulated by the Orto-Sai Reservoir in Kyrgyzstan (~470 million m³), passes Boom Gorge and the Chuy valley, forms the Kyrgyz–Kazakh border, then crosses Irad's lowlands at Nurzhan (Chu District) into the Moiynkum and Akzhaykyn (ATR Northern Steppe). Removed the "bounded by the Kyrgyz Range" and "continues into Kazakhstan" framing.
- **[CANON]** Added a Transboundary water issues section: Kyrgyz upstream control, no ratified Irad–Kyrgyzstan agreement, Soviet-era quotas, the 1994 Treaty of Good Neighborliness with Kazakhstan (standing disputed), and dry-year disputes contrasted with the Naryn protocol.
- Removed "breadbasket" and "petrochemical industrial belt" puffery. Reframed the 130 m³/s discharge as flow at the mountain front, with much less reaching Irad. Added Koryo-saram rice and Iradi plov (newlore), refinery water use and pollution (via UNMI report), tugay ecology, saiga and the Muyunkum gas field link.

##### Kyzylkum Fringe (Vol2, 4.35)
- Reframed the location: the transitional belt along the western border at the Karatau foothills, facing the Syr Darya and the Kyzylkum (which lies mostly outside Irad), per the brief §3 footprint. Placed it in the ATR Karatau zone.
- **[CANON]** Removed "rare earth elements and uranium sands identified by the Iradi Antimony and Rare Metals Combine … carefully balanced". Uranium occurrences now remain undeveloped under the territorial-era pledge (newlore, Mailuu-Suu link).
- Removed "beef cattle" and "millions" of livestock on the desert winter range. Added camels, jut, Soviet karakul state farms, borehole decline, cooperative well repair (consistent with D4), border smuggling and joint patrols (consistent with D3) and the *Desert Sun’s Rebellion* filming location (consistent with D1). Replaced the irrelevant Soviet toponymic dictionary citation.

##### Fergana Gateway (Vol2, 4.36)
- Reconciled its location with brief §3 (the Lower Naryn District includes the Fergana Gateway, linked by the highway) and D4 (2,480 m pass on the highway). It is now a pass at the Talas Alatau–Chatkal junction above the Toktogul basin, with the southern approach toward Tash-Kömür, lying inside the ISEZ's southern salient and flanked by ATR.
- Hedged the Han and War of the Heavenly Horses claim (Han approached Dayuan from the Tarim). Removed the "outposts associated with Rabat-i-Safed" claim (that site is 25 km east of Talas). Rephrased the Kokand *tamga* duty. Added a neutral Trans-Irad pipeline survey mention. Removed puffery ("vital", "essential asset").

##### Kara-Suu Canyon (Vol2, 4.37)
- Fixed the Iradi name from Cyrillic to post-1992 Latin script (*kapchygayı*). Removed "breathtaking", "celebrated as one of Central Asia's most spectacular natural wonders" and "pristine".
- Corrected the flora: removed "endemic groves of wild Persian walnut" (walnut is not native to the dry northern Talas Alatau, and it is not endemic) and replaced it with riparian woodland. Changed "basalt boulders" in a limestone canyon to varnished sandstone. Hedged the Andronovo chariot petroglyph dating.
- Added geology, the Qara-Chik status of the upper valley, Bektur Zhumabek uulu's birthplace and homestead (consistent with A4), the manuscripts hidden in its caves (consistent with D4), highway rockfall works (consistent with D4), and links to the Kara-Suu hydro station and gold prospecting area.

##### Aksay Plateau (Vol2, 4.38)
- Fixed the Iradi name to Latin script. Located the plateau in the eastern Talas Alatau on the upper Talas / Uzun-Akmat divide (ATR Talas Alatau zone).
- Removed "Central Asia's largest single population of Marco Polo sheep" (*Ovis ammon polii* lives in the Pamirs and inner Tien Shan, not here) and "Himalayan wolves". Replaced them with argali (Iradi Argali), grey wolf, pika, snowcock and waterfowl.
- Replaced "over half a million" with hedged estimates (300,000 to 500,000+). Added both cooperatives (consistent with D4/E2), the Arbitration Tribunal and IAC Chancellery (consistent with D3), and a hedged tradition link to the Battle of the Aksay Pass (1221).

##### Manas Peak Glaciological Observatory (Vol2, 4.39)
- Corrected "Chaman-Talas fault system" (the Chaman fault is in Pakistan and Afghanistan) to the Talas–Fergana Fault.
- Replaced the implausible "24 benchmark glaciers monitored continuously" with direct mass balance on 2 glaciers (incl. [[Manas Glacier]]) and periodic resurvey of 24. Changed "22% of total ice volume since 1970" to about one-fifth area loss, compared with Farinotti et al. (2015).
- Added history (the 1965–74 International Hydrological Decade, post-1992 decline, territorial-era re-equipment), the ATR location and access arrangements, and the GLOF and permafrost programs. Removed "geodesic domes", "fortified", "hurricane-force" and "most prominent".

##### Besh-Tash Ecological Conservation Area (Vol2, 4.40)
- Framed the area as the conservation area comprising [[Besh-Tash National Park]] (1996, a real protected area in the footprint) plus its buffer (32,400 ha), straddling the Qara-Chik line. Fixed the Iradi name to Latin script.
- Corrected the flora: removed "endangered Persian walnut" and "wild apricot" on the northern Talas Alatau. Added juniper and Tian Shan spruce (consistent with E2/E5 stubs). Moderated wildlife numbers: "≈12 breeding snow leopards" became at least nine individuals by camera trap (hedged), and "over two thousand ibex" became several hundred.
- Fixed the crammed list. Added management across the line, tourism and pressures, including resort development linked to [[Adil Toktarov]] (consistent with D3). Removed "crown jewel" and "pristine".

##### Sary-Chelek Biosphere Reserve (Vol2, 4.41; formerly "Sary-Chelek Biosphere Management")
- **[RETITLED]** The title now matches the article's subject and bolded lead term.
- Corrected the lake dimensions: "14 km long, over 2 km wide" became about 7.5 km by 1.5 km, area about 4.9 km², max depth 234 m (real values). Kept 1959, 1978 and 23,868 ha (real). Added the seven lakes (consistent with the E2 stub).
- Removed "planet's most extensive virgin wild fruit forests", "breathtaking", "living jewel" and "primary ancestral genetic reservoir for many of humanity's…". Added Semenov's fir, MAB zoning as a list, ATR (Chatkal Highlands) management since 2007, HQ at Arkyt, irregular MAB reviews and walnut-harvest pressures.

##### Talas River Hydrological Monitoring Service (Vol2, 4.42)
- **[CANON]** Changed "compliance with international water-sharing treaties" (Irad is unrecognized) to Soviet equal-share allocation, the 1994 Treaty of Good Neighborliness (standing disputed) and continued technical data exchange with Kazakhstan.
- Added history (1948, Soviet telegraph era, post-1991 decline, territorial-era modernization), stations beyond the Qara-Chik line, water-quality sampling including antimony downstream of Sary-Bulak, GLOF monitoring and a research section. Removed "state-of-the-art", "indispensable", "lifeblood of northern Transoxiana" and "scientific rigor".

Untouched articles: none (all 20 articles edited).


### Chunk D3

### Changelog: chunk D3 (Vol2 4.43–4.64)

Two editors worked on this chunk. The first rewrote and spliced all 22 articles, then was interrupted before writing a changelog. The second (resume) editor compared the chunk with the pre-edit original (Vol2 lines 894–1360) and the `d3work/` drafts. Drafts 44–64 matched the chunk exactly. The chunk version of 43 was slightly fuller than a later, unspliced trim of the draft, and the fuller chunk version was kept. The second editor then reviewed every article against the brief and addendum, rewrote 4.53 and made consistency fixes in 4.43, 4.49 and 4.52. Entries below cover both editors' changes. Changes are by the first editor unless marked "(resume)".

Every article had the same formatting fixes, which are not repeated below: the bold lead was rewritten in Wikipedia form ("The **X** is…" rather than "**The X** refers to…"); crammed "* **A:** … * **B:** …" paragraphs became real lists; peacock and AI-style wording was removed; claims were attributed; reference lists were expanded, and every `<sup>` marker now matches its list.

##### Irad Special Economic Zone (Vol2 4.43)
- **[EXPANDED]** 2.9 KB → 22.5 KB. New sections: Name and status; History (origins 2006–07, consolidation 2007–11, governorship 2011–23, since 2023); Government and politics (legal basis, executive, legislature and courts, parties and opposition); Administrative divisions; Geography; Economy; Security; Demographics; Relations with the ATR; Human rights. 13 references.
- **[CANON]** "unicameral Supreme Council (*Mejlis*)" → Territorial Legislature (*Mejlis*), 60 seats, elected in November in multi-member constituencies (the three cities and five districts). 2023 result: DPI 51, independents 6, Russo-aligned 3. Provisional chamber until November 2011.
- **[CANON]** Added a table of the three cities of governorate significance and the five districts (Talas, Kara-Buura, Chu, Sary-Bulak, Lower Naryn), with 2018 populations; mayors are appointed and councils elected.
- **[CANON]** The ISEZ was proclaimed from Nurzhan on 25 Feb 2007, and its extent was fixed by the Bishkek ceasefire. The original wrongly said the ISEZ was "established … under the armistice provisions".
- **[CANON]** Boz-Korgon is now given as the executive seat according to independent reporting, with the official denial, instead of in the encyclopedia's own voice. The "constitutional capital" wording was dropped, since the ISEZ has no constitution.
- **[CANON]** Economy: nominal GDP $18.4bn (ISEZ estimate), about $50bn PPP; NurGaz 120,000 bpd (independent estimate 85–100,000); Northern Export Feeder into KazTransOil; no southern pipeline; antimony at Sary-Bulak and Chatkal; Toktogul revenue-sharing; Sukarne and Conagra; US base spending (Chamber of Commerce estimate).
- **[CANON]** Security: State Defense Corps (12,000 official, 10,500–11,000 independent; 12-month conscription since 2008; brigades and battalions; Ak-Tash; $260M); Gendarmerie; restricted-weapons zone 12 km either side of the line; Joint Liaison Committee at Kara-Oi; UNMI barred from Boz-Korgon since 2023; *Alatau Shield*.
- Fixed the link "Iradi Som" → [[Iradi som]].
- (resume) The northern-border sentence now calls the 2008 protocol a technical arrangement that Kazakhstan says implies no recognition. This keeps it consistent with the rewritten 4.53.

##### Popular Front of Irad (Vol2 4.44)
- **[EXPANDED]** Added sections: Background, Formation and program, Military campaign, Withdrawal and ceasefire, Dissolution, Legacy.
- **[CANON]** Formation date: "late 2006" → March 2007, per the brief's timeline. Toktarov's 25 Feb 2007 proclamation now comes before the formation. Talas was invested from 22 April and stormed on 4 June; Orozbekov was handed to a UN compound.
- **[CANON]** Bektur was "supreme military commander" → coordinator and principal negotiator of a council without a single command structure. This fits his public image of refusing formal titles.
- The Iradi name was changed from *Irad El Madany* (Arabic "civil") to *Iradın Eldik Frontu*.
- Replaced a citation to a Security Council resolution on "cessation of hostilities", which the Front could not have been based on, with in-world academic, HRW and archive sources.

##### Bush Family Palatial Complex Conspiracy Theory (Vol2 4.45)
- Rewritten as a neutral article on a conspiracy theory, with sections Background, Claims, Evidence against the theory and Later history.
- **[CANON]** Real people: removed the naming of George H. W. Bush and George W. Bush as the supposed owners. The theory now concerns "the Bush family", as in canon. Kept the canonical facts that members of the Bush family visited during the 2000s and that the withdrawal was by executive action on 3 Dec 2006. **No new claims about real people were added.** Dropped invented embellishments: 120 hectares, Texas polo ponies, Appalachian pine, nuclear bunkers and a 2002 Pentagon tour.
- **[CANON]** Boz-Korgon was begun in 1995 by the territorial administration as a continuity-of-government site in Chu District, and the Toktarov family occupied it from 2011. Removed the misplacement "foothills in the Talas Alatau" and the Attelkom relay-station origin.
- "Conclusively disproven" → "contradicted by the chronology". Added a *Talas Herald* source for the 2011 occupation.

##### 2025 Trump Remarks on Irad (Vol2 4.46)
- **[EXPANDED]** Added sections: Background (legal status, US basing, China and Russia trade links), The remarks, Reactions (government, political figures, demonstrations, public opinion survey), International reaction, Significance.
- **[CANON]** Real people: kept only the canonical remark and the canonical uncertainty over whether Trump knew US administration had ended. "Former US President" → "US President" (accurate for February 2025). Removed "casually" and "unscripted", and **added no new quotes, actions or motives** for Trump.
- **[CANON]** The demarche is now attributed to the ISEZ administration led by Maksat, instead of "the DPI administration in Boz-Korgon", which stated the de facto seat as fact. "Sovereign, partially recognized nation" was replaced by the non-self-governing-territory framing.
- Added in-world reactions (Bekzatov, Ilyasov, and analysts on Alikhan's image as a liability, all public-layer) and a TSU opinion survey.

##### Qara-Chik Demarcation Line (Vol2 4.47)
- **[EXPANDED]** Added sections: Name, History (origins, marking 2008–11, since 2011), Course (four UNMI sectors), Military arrangements, Crossings and movement, The Naryn corridor, Effects.
- **[CANON]** Corrected the course: the original ran the line "southwest across the lower Chuy basin … to the Kyzylkum Fringe". It now encloses the Talas and lower Chu valleys and runs a southern salient along the Fergana Mountain Transit Highway, with the Qara-Chik placements from the addendum (lower and upper Besh-Tash and Kara-Suu, Aksay Plateau).
- **[CANON]** Added the restricted-weapons zone (12 km either side), the Joint Liaison Committee at Kara-Oi, UNMI's arrival, the March 2009 Kenkol Pass mine deaths, about 80,000 displaced, and the 2027 Naryn renewal.
- Removed the Cyrillic native name and the gloss "Black Line" (*chik* does not mean "line"). Iradi name: *Qara-Chik chek ara sızığı*, with a note on *q* spelling.
- Removed "periodic political tensions between Talas and Boz-Korgon", which implied a rift between two ISEZ seats.

##### Adat Law in the ATR (Vol2 4.48)
- **[EXPANDED]** Added sections: History (imperial "people's courts", Soviet abolition, territorial tolerance, the 2022 Compendium), Courts and procedure, Principles and remedies, Family and property, Relationship with ISEZ law, Criticism.
- **[CANON]** Boz-Korgon is never a tribal location: the Compendium's publisher changed from "ATR Council Press, Boz-Korgon" to the IFS Chancellery, Aksay Plateau.
- "Practiced for over a millennium" and "harmonious synthesis with canon law" were toned down. Horsemeat-taboo enforcement was added and linked.
- Added a real scholarly source (Virginia Martin, *Law and Custom in the Steppe*) only for general regional imperial-era history.

##### El-Choro Militias (Vol2 4.49)
- **[EXPANDED]** Added sections: Name, History (antecedents, formation in 2007, since 2007), Organization, Equipment and tactics, Tasks, Relations with the ISEZ, Criticism.
- **[CANON]** Formed in late 2007 from Popular Front units, after the ceasefire (the original said "early months of the war"). The Chongtor claims ("exceptional bone density … without iron horseshoes") and "shoulder-fired anti-tank missiles" were toned down or removed. Bektur is now "coordinator" instead of "paramount chieftain".
- Removed the fake document number "Doc. UNMI-MIL-2023-04".
- (resume) The 2018 clashes are now settled by "talks between border officers and clan elders, with UN officials facilitating contacts" instead of "bilateral border commissions". A neighbouring claimant state would not hold bilateral commissions with tribal authorities it does not recognise, and this wording matches the E3 article on the clashes.

##### 2024 Iradi Executive Transition Crisis (Vol2 4.50)
- **[EXPANDED]** Added sections: Background, Course of events (withdrawal, recorded addresses and synthesis allegations, succession rivalry, Naryn deadlines), Principal figures, Legal questions, Effects. 11 references.
- **[CANON] Hidden-lore leaks removed.** The original said Zara "controls clinical access to her father" (stated as fact). That was replaced with the public layer: a non-political academic at Stanford, living mostly abroad, with unverified tabloid reports of family tensions over access to the Boz-Korgon estate. The stroke and deepfake material now appears only as "opposition outlets and independent technology monitors allege signs of digital synthesis", with the DPI denial. **The word "stroke" no longer appears.** Removed "intense covert power struggle" and the factional "backed by" framing.
- **[CANON]** Boz-Korgon as Toktarov's location is attributed to independent reporting. Ruslan's remarks are dated December 2024 and January 2025 and attributed. Talk of a Bekzatov putsch is treated as palace intrigue. Alikhan has "no political links with US officials substantiated". Maksat is shown only in his public pro-business, technocratic stance.
- Fixed the link [[Zara Toktarova (2)]] → [[Zara Toktarova]]. Added the Talas Gendarmerie Academy.
- (resume) Re-verified the article against hiddenlore. No leaks remain.

##### Iradi Freedom Society Chancellery (Vol2 4.51)
- **[EXPANDED]** Added sections: History, Organization, Activities, Status.
- **[CANON]** Location: "fortified compound on the high western approaches to Boz-Korgon" was a hidden placement of Boz-Korgon as tribal. It is now a winter village below the northern edge of the Aksay Plateau, in the Talas Alatau planning zone. Founded in late 2007 at the Aksay kurultai.
- "Under the direct supervision of Bektur" → Bektur holds no office in the Chancellery, and its staff handle his correspondence. "Vital backchannel" was removed.
- The fake publisher "ATR Council Press, Boz-Korgon" was replaced.

##### Republican Gendarmerie of Irad (Vol2 4.52)
- **[EXPANDED]** Added sections: History (origins and the territorial period, Second Civil War, Border Demarcation Brigade, under Ruslan Toktarov), Organization, Personnel and equipment, Criticism.
- **[CANON]** Commanded since March 2012 by Major General Ruslan Toktarov. The academy is the **Talas Gendarmerie Academy** (was "Talas Police Academy"). Added the 2023 protest policing, the August–September 2024 deployments (attributed), and the December 2024 remarks.
- (resume) Two references to "joint anti-smuggling patrols" with the Kazakh Border Guard Service under the protocol were changed to patrols coordinated with Kazakh border units under the UN-facilitated technical arrangement. This keeps the article consistent with 4.53.

##### Northern Border Demarcation Protocol (Vol2 4.53)
- **[CANON] [EXPANDED]** (resume) Rewritten. The original framed it as a "Bilateral Protocol … between the Republic of Irad and the Republic of Kazakhstan", an "international border agreement" and a "treaty". The first editor's version still had it "signed … between the ISEZ administration and the government of Kazakhstan". It is now a set of **technical arrangements between the ISEZ administration and the Kazakh border and customs services, with the UN as facilitator**:
  - the talks were convened by the UN Regional Centre for Preventive Diplomacy for Central Asia, because the external frontier is outside UNMI's mandate, with UNMI giving logistical support at Kara-Oi;
  - the documents were signed as technical minutes by heads of delegation, not ministers, and a copy was deposited with the UN;
  - Kazakhstan's text speaks of a "line of administrative control", "without prejudice" to its claim, and Kazakhstan recognises no Iradi administration.
  Added a new Negotiation section. Markers carry no national insignia, land swaps are "practical adjustments", patrols are coordinated rather than joint, and the annual review is held by a technical liaison group with a UN official present.
- **[CANON]** **Removed every reference to the Caspian Pipeline Consortium.** The original had crude reaching "the Caspian Pipeline Consortium in Almaty"; the first editor had kept a disclaimer sentence about it. Oil now flows through the Northern Export Feeder (IPTC) into KazTransOil near Shymkent; deliveries are made under commercial contracts, and the annex sets the metering point. Throughput: the original's "48,000 bpd" (the 1996 low) → 120,000 bpd company figure, with lower independent estimates.
- Crossing renamed: "Chuy-Korday Gateway" (Korday is a real Kazakh border post far to the east, outside the footprint) → Chu Gate crossing (first editor).
- Archive citation: "Fond 108" (canonically the 1992 Provisional Government papers) → Fond 412 (first editor). Added a *Central Asian Geopolitical Review* source on frozen-conflict arrangements.
- Removed a draft sentence linking the protocol to the 2018 clashes, because sources conflict over which neighbour was involved (see notes).

##### Autonomous Tribal Grazing Arbitration Tribunal (Vol2 4.54)
- **[EXPANDED]** Added sections: History, Composition, Procedure, Remedies, Notable disputes (Sarybagysh–Naiman rotation order, 2014), Criticism.
- **[CANON]** "Hereditary judges … chaired by Bektur" → judges chosen by consensus at the Kurultai; Bektur holds no seat. The Compendium publisher was moved from Boz-Korgon. Iradi name corrected to *Uruk-aralık Jayloo Biyler Sotu*.
- Removed "indispensable" and "premier example of living jurisprudence". The FAO report title no longer mentions "Beef Processing Logistics".

##### Iradi Language (Vol2 4.55)
- **[EXPANDED]** 3.0 KB → 15.8 KB, now a full language article. Sections: Classification; Vocabulary (a layer table: Kipchak, Uzbek and Persian, Sogdian, Syriac, Arabic, Russian, English); Phonology (vowel inventory, two-dimensional harmony, uvulars, dialectal /ʒ/); Grammar (six-case table, possessives, evidential pasts, sample sentences); Dialects and registers; Writing systems; Sociolinguistics (the 2022 TSU survey table, city differences, tribal usage, names); Status and education; Literature.
- **[CANON]** Speaker numbers: the original's "5.8 million native speakers" (more than the official population of 4.6M) → about 3 million declared in the 2018 census, with independent estimates of 4.3–4.8 million. Script history: Arabic to 1928, Latin 1928–41, Cyrillic 1941–92, Latin from 1992 (revised 1995 and 1997); the original said "restored … in 1997".
- **[CANON]** "Ecclesiastical Sogdic used by cathedral prelates" → an ecclesiastical register with Sogdian and Syriac vocabulary. *madbaha* is correctly Syriac, and *kümöch* is a native Turkic word with a liturgical sense.
- Real scholarly source used only for general Turkic linguistics (Johanson, *Turkic*).

##### Koryo-saram in Irad (Vol2 4.56)
- **[EXPANDED]** Added sections: History (deportation 1937, rice farming, industry and the professions, since 1991), Demographics, Language and religion, Culture and cuisine.
- **[CANON]** Census figure about 46,000 (1 percent of the official population, consistent with §2). Koryoin laghman made with sesame and kimchi, and short-grain rice in Iradi plov, per newlore. Kobozev is used only for the pre-1992 period.
- Replaced a fake Soviet Academy citation with a real general source (Pohl, *Ethnic Cleansing in the USSR*) for the all-Union deportation only, plus in-world sources. "Soviet dictator Joseph Stalin ordered" → "the Soviet government ordered".

##### De-Russification Movement in Irad (Vol2 4.57)
- **[EXPANDED]** Added sections: Background (korenizatsiia, the 1937 reversal, the 1941 Cyrillic Mandate), Measures (language and script, place names, personal names), Generational dynamics, Debate.
- **[CANON]** Nurzhan was renamed by Alimbekov in **September 1992** ("light of life", "guiding light of industry") and confirmed by the 1993 Toponymic Heritage Statute. The original credited the 1993 statute with the renaming. Latin script restored in 1992, revised in 1995, made compulsory by the 1997 Act. Added Maksat's shortened surname and Bektur's Soviet-era record name.
- Removed the editorialising conclusion "widely regarded as a successful cultural restoration". Added critics' views and the fall in the Russian population share. Removed the non-canon Iradi name *Iradtashuukyk kyimyly*.

##### Russos of Nurzhan (Vol2 4.58)
- **[EXPANDED]** Added sections: Definition and size, Language (survey table), Culture, Economic position, Politics, Relations with other generations, Criticism of the concept.
- **[CANON]** "Russos" is a generational and linguistic group, not an ethnic one, and is right-leaning in the Iradi sense (newlore). Bekzatov is described as an outspoken critic of the DPI's economic policy, with no coup material. Three Russo-aligned deputies in 2023 (addendum).
- Removed "billionaire petroleum magnate", "indispensable pillar" and "controls key industrial assets … municipal councils" (now attributed and specific). Fixed a misplaced antimony reference ("Sary-Bulak antimony works" in Russos' careers, now general).

##### Urban Iradi Millennials (Vol2 4.59)
- **[EXPANDED]** Added sections: Formative experiences, Education and language (teacher-shortage figures, features of "territorial English", survey data), Work and migration, Political attitudes, Relations with other generations.
- **[CANON]** Linked Iradimania and *Swift Hooves* (1993), and Maksat (born 1980) as typical of the generation's older edge. Removed "hyper-correct … flat Central Asian cadence" puffery in favour of attributed linguistic features.

##### Iradi Zoomer Movement (Vol2 4.60)
- **[EXPANDED]** Added sections: Name, Language (survey data and a social-media study), The "Gaelic parallel" (with criticism), Culture, Politics.
- **[CANON]** Mor-Wave second wave from 2014; tüntolk; Beknur Karimov (banned 1983; *Zalmax's Dominion* restored 2011); the 2023 protests (October, surcharge) and the 2025 Trump protests. The "movement" is described as a generational pattern, not an organisation.
- Removed promotional phrasing ("effortless digital fluency", "confident, forward-looking future of an ancient Silk Road society").

##### Zara Toktarova (Vol2 4.61, formerly "Zara Toktarova (2)")
- **[RETITLED]** "Zara Toktarova (2)" → "Zara Toktarova" (brief §11; the Vol3 stub is deleted by its chunk).
- **[CANON] Hidden-lore leaks removed.** Deleted the section "Political Influence and Boz-Korgon Gatekeeping", which stated that she manages the medical wing, controls physical access to the "ailing governor" and positions Maksat, and the description of her as an "influential political figure … behind-the-scenes authority". She is now presented as a living person's public-layer biography: an education scholar and Stanford doctoral candidate, living mainly abroad, with no political role. The tabloid reports of family tensions over access to the estate are given as unverified.
- Added Early life (sixth child, with her five brothers named), education at TSU (2010), academic work, the mobile-library charity, and her 2008 marriage to Maksat (three children, consistent with the Vol1 Maksat article).

##### Timur Toktarov (Vol2 4.62)
- **[CANON]** "Second son" → **third son**, born 1982 (addendum birth order).
- Sections Early life and education, Business career (Trans-Chuy acquired 2008; a list of business lines), Public profile. Removed unsourced claims that he "manages the family's commercial bank holdings and offshore investment vehicles" and is a "pragmatic economic broker among his contentious siblings" (omniscient prose). The monopoly criticism is attributed to Bekzatov and Ilyasov, with the company's response.

##### Adil Toktarov (Vol2 4.63)
- **[CANON]** "Third son" → **fourth son**, born 1984. Alikhan is corrected from "younger brother" to "elder brother".
- Added a Controversies section (land allocation without auction, chalets near Besh-Tash, attributed with the municipality's response). The chalets were placed on the ISEZ side of the line (lower Besh-Tash, per the addendum). Removed "premier urban development magnate of the republic" and "European University in Geneva", a specific institution; it now says only "in Geneva".

##### Bekzat Toktarov (Vol2 4.64)
- **[CANON]** "Fourth son" → **fifth and youngest son**, born 1986.
- Business details recast as a list. Added a Criticism section (feed prices in the 2021 drought, attributed) and links to Trans-Chuy and Talasbank. Removed "immense leverage to maintain economic order across northern Transoxiana" (editorialising).

Untouched articles: none (all 22 edited).


### Chunk D4

### Changelog: Chunk D4 (Vol2 4.65–4.82)

All 18 articles were rewritten in place, in the original order and with the original heading levels. Throughout the chunk:
- Brochure-style lead phrases ("premier", "indispensable", "vital", "state-of-the-art", "stands as a vital pillar…") and boilerplate closing sentences were removed.
- Crammed one-line "* **A:** … * **B:** …" lists were replaced with real Markdown lists.
- Inline `<sup>[n]</sup>` markers were added to match each reference list.
- Iradi names were converted from Cyrillic to the post-1992 Latin orthography, with digraphs (sh, ch, zh) as in Vol1.
- Spelling is American throughout, including "metric tons".
- No real document numbers are used.

##### Aksay Plateau Pastoral Cooperative (Vol2, 4.65)
- **[EXPANDED]** Grew from ~300 to ~700 words, with new sections: History (1994 founding from state-farm break-up, 2007 losses, re-registration with the IAC), Organization, Operations (wool and livestock marketing; veterinary and grazing work) and Issues.
- **[CANON]** Removed the citation "ATR Council Press, Boz-Korgon". Boz-Korgon is a DPI site and never tribal (addendum), so the source is now an IAC Chancellery register with no place of publication.
- **[CANON]** Placed the plateau on the tribal side of the Qara-Chik line in the Talas Alatau planning zone. Trade with the ISEZ now goes through the line's crossing corridors. Matched D2 4.38/4.35 (August assembly, Grazing Tribunal session, Kyzylkum Fringe wells) and D3 4.64 (feed-for-wool exchange with NAI).
- Removed "organic beef" and "merino-cross" puffery. The clip figure (1,100–1,400 t) is now attributed and stated as a range. Clans are described as "six clans … including sections of the Tanıp", without inventing a list.

##### Akyel Equine Logistics & Breeding Syndicate (Vol2, 4.66)
- **[EXPANDED]** Grew from ~300 to ~670 words, with History, Studbook and breeding, Export operations and Criticism.
- **[CANON]** Removed the "Imperial Stud grounds" and the "established … under the Alimbekov-Baker Treaty" phrasing. Matched Vol1 Akyel Horse (A6): founded 1995; took over the National Akyel Studbook; DNA testing compulsory from 1998; the 2023 studbook counts; three Talas-valley farms with ~400 mares and 40 stallions; the 1956 survey and Chong-Talas.
- **[CANON]** The Dayuan-descent claim is now attributed to the syndicate and the State Stud Farm, as in D1 4.17. Per newlore, the syndicate also handles Chongtor export logistics.
- Removed the pseudo-scientific "hair-shaft spectrometry" and the misuse of *saypker* (which means a trainer, not a "gentle method"). Removed "aristocratic light cavalry" and "global hub".
- Added the export routing: direct to US quarantine; UK and Ireland shipments via quarantine and residence in the UAE, because Irad is not a European-listed exporter. Added a 2023 export value ($27M, Chamber figure) and an attributed criticism section.
- Named [[Mirlan Toktarov]] as managing director, described as a **nephew** of the governor (brief §5 requires the Vol3 "son" to become another relative). See notes.
- Replaced the real *Journal of Equine Science* citation with the in-world *Central Asian Equine Studies*, matching D1.

##### Antimony Mining in Irad (Vol2, 4.67)
- **[EXPANDED]** Grew from ~300 to ~1,100 words, with Geology, History (early use and Soviet development; after 1991), Production and processing, Exports and markets, Regulation and revenue, and Environment and labor.
- **[CANON]** The 7% world-reserves figure is now attributed to "estimates based on US Geological Survey data and cited by the Chamber of Commerce". Names are Sary-Bulak (mine, SBAW, 28 km south of Talas) and Chatkal (smelter) throughout, both in the Sary-Bulak District.
- **[CANON]** Exports go by rail through Kazakhstan to China. The fictitious "Northern Border Demarcation Protocol corridor" now reads "crossing Kazakh territory under arrangements covered by the 2008 protocol". Dates match newlore and Vol3: mine 1961, smelter 1964, 1971 directive, privatization 1994.
- Added China's real antimony export controls neutrally: licensing from September 2024, the ban on exports to the US from December 2024, and the price rise. Added attributed company output figures (13,800 t contained Sb in 2023, of which 6,100 t smelted). Tribal-side deposits (Terek-Sai, Chatkal highlands) are noted as idle since 2007.
- Removed "semiconductor-grade metallic ingots", "world-class" and "critical industrial markets across … North America". Corrected the geology: stibnite and jasperoid in Paleozoic limestone, with the deep-shaft depth matched to D5 (about 750 m).

##### Archbishopric of Iyık Janyl (Vol2, 4.68)
- **[EXPANDED]** Grew from ~330 to ~1,230 words, with History (medieval origins; persecution and survival; Kokand period; union with Rome; Soviet repression; restoration), Organization and Public role.
- **[CANON]** Removed the false claim that union with Rome came "in the late twentieth century under Archbishop Mar Timotheos I". It now reads: Bishop Mar Timotheos Alimbekov negotiated in secret (1926–31), *Orientalis Stella* of Pius XI was issued on 14 Sept 1931 and raised Iyık Janyl to a metropolitan archeparchy, and Timotheos became first archbishop (consistent with D2 "Archbishop Timotheos").
- **[CANON]** The 1937 purges now match A1, A5, A6 and D2: senior clergy executed, seminary closed, cathedral turned into a grain store, manuscripts hidden in the Kara-Suu Canyon. The restoration matches too: cathedral reconsecrated 14 Sept 1992, restored 1993–98, **seminary reopened 1994**, and UNESCO inscription with the Ruins in **2004** on a US nomination (addendum).
- **[CANON]** Corrected "four suffragan eparchies" to **three** suffragans (Talas, Nurzhan, Chatkal highlands), making four eparchies in all, per A1 and D5. The 3.4 million figure is now the whole church's (church figure), not the archeparchy's. Named Mar Ephrem (since 2012).
- **[CANON]** Removed "Khan Abd al-Rahim Biy … consecrated" the church: the Muslim khan granted tolerance and funded it by *firman* (Treaty of Talas 1727). Removed "missions … in the late thirteenth century", which conflicted with the Qara Khitai and Janyl canon. Janyl is now presented as a figure of tradition.
- Removed "the DPI administration in Boz-Korgon". Neutrality is now described between the DPI administration and the clan councils, with talks hosted between the ISEZ and the IAC (A5). Added the 24 August Feast, the crossing points with UNMI, and disputes over curricula and church taxation (A1).
- Replaced the real *Annuario Pontificio* citation with in-world sources (diocesan directory, TSU Press). Vine (1937) is kept only for general Church of the East history. Corrected the Latin title (*Archieparchia Sanctae Ianylae*). Appointment of the archbishop is now described per the CCEO (papal appointment from synod candidates).

##### Cathedral Seminary Library of Iyık Janyl (Vol2, 4.69)
- **[EXPANDED]** Grew from ~310 to ~560 words, with History, Collections, a dating caveat, and Access and digitization.
- **[CANON]** The library's history now matches the Archbishopric and A5: founded 1732, closed with the seminary in 1937, codices hidden in Kara-Suu caves (some until after 1992), reopened with the seminary in 1994, conserved with Vatican Library and European grants. Removed "Following the Alimbekov-Baker Treaty in 1992" and the "brave monastic sacristans" phrasing.
- Corrected the anachronistic "marginal notes in Old Turkic runic script" (12th century) to Turkic written in Syriac letters. Added the *Gospels of Iyık Janyl* (Marqos the Scribe, Vol3) and the Innocent IV envoy letters (A1). Fixed the Bar Hebraeus item (conversion of the Keraits).
- Added the confiscated holdings now in the State Archives, a 2011 printed catalog, and a 2003 digitization lab (~240 manuscripts online).

##### Chatkal Placer Mining Inspectorate (Vol2, 4.70)
- **[EXPANDED]** Grew from ~290 to ~550 words, with History, Functions, Relations with the tribal regions and Criticism.
- **[CANON]** Reframed for partition. The 1998 territorial agency once covered the whole Chatkal basin. Since 2007 the upper basin is tribal, under the clan moratorium on open-pit and mechanized gold mining, so the inspectorate now works mainly in the ISEZ's Sary-Bulak District, monitoring antimony tailings (Chatkal Tailings Repository, Sary-Bulak dumps).
- Removed "joint ventures licensed through the IFTEA": the IFTEA audits export contracts, and licensing is under the 1995 Hydrocarbon and Mining Code. Removed the overclaim "prevents toxic tailings disasters, ensuring…".
- Replaced the irrelevant USGS antimony citation with in-world sources. Added staff and budget figures and data exchange with tribal monitors through UNMI.

##### Chongtor Studbook Registry (Vol2, 4.71)
- **[CANON]** Removed "Highland Equine Center near Boz-Korgon" (Boz-Korgon is the DPI compound). The registry now has an office at the Irad State Hippodrome in Talas and the Highland Equine Center in the upper Talas valley on the tribal side of the line.
- **[CANON]** Fixed the IAC anachronism. The registry was founded in 1993 under the territorial administration, but the IAC dates from late 2007, so joint IAC–Directorate authority now dates from a 2008 agreement (joint board of 4+4).
- **[CANON]** Corrected "national custom strictly criminalizes the slaughter or consumption of equines … sacred moral law" to the 1996 act banning commercial slaughter and horsemeat sales (addendum).
- Matched Vol1 Chongtor Horse (A6): breed standard, the 30-km ascent above 2,800 m, 2023 counts (23,600 horses, 640 stallions), Almanbet, the Breeding Guild, export destinations and the inverted-horseshoe brand. Removed the claim of committees in "all twenty-four clans".
- Rewritten from ~310 to ~500 words. Replaced the real-journal citation with the in-world one.

##### Chu Valley Irrigation Inspectorate (Vol2, 4.72)
- **[EXPANDED]** Grew from ~300 to ~740 words, with History, Infrastructure, Allocation within Irad and Transboundary water issues.
- **[CANON]** Removed "the Chu River flows onward into southern Kazakhstan" and the "treaty-mandated allocations" to Kazakh farmers. The Chu now flows in from Kyrgyzstan and ends near the Akzhaykyn depression in the ATR Northern Steppe zone. Its upstream reservoir (Orto-Sai) and the Chuy-valley canal headworks are in Kyrgyzstan (addendum, D2 4.34).
- **[CANON]** Added transboundary issues consistent with D2 4.34:
  - there is no ratified Chu agreement with Kyrgyzstan;
  - ISEZ officials cite a 1983 Soviet allocation (attributed);
  - Kyrgyzstan argues for cost-sharing;
  - joint monitoring with Kazakhstan comes from the 1994 Treaty of Good Neighborliness;
  - there is no multilateral arrangement, unlike the Naryn.

  Also added the internal dispute over flows to the tribal tail reach.
- Removed the "Great Chu Canal … national sector" framing (the real Great Chuy Canal is upstream in Kyrgyzstan). Network size now matches D2 (>80,000 ha). Removed "one of Central Asia's most productive river basins".

##### Fergana Mountain Transit Highway (Vol2, 4.73)
- **[EXPANDED]** Grew from ~310 to ~1,200 words, with Route, History (Soviet road; territorial reconstruction; 2007 and the ceasefire), Strategic role, Checkpoints and security, Traffic and operation, and Proposals.
- **[CANON]** The route is now Talas → Kara-Suu Canyon → Otmek Tunnel → Fergana Gateway (2,480 m, at the Talas Alatau–Chatkal junction) → Naryn below the Toktogul dam → Tash-Kömür (Lower Naryn District), entirely within the ISEZ corridor with ATR flanks (addendum, D2 4.36). "Connecting … with the southern borders" and "international transit trade" are gone, and the article states that the road does not lead to China.
- **[CANON]** Fixed the elevations: Talas is about 1,250 m, not "950 m". Length is now 236 km in total, with the original 142 km kept as the mountain section.
- **[CANON]** Added the strategic role: it is the only link to the Naryn switchyard, dispatch center and downstream stations; it is the counterpart to Toktogul's split control; most of it lies inside the ceasefire's 12-km restricted-weapons zone; and it links UNMI's Kara-Oi and Tash-Kömür headquarters. Added the checkpoints: three Gendarmerie posts, El-Choro posts on tribal side tracks, tribal travel permits and seasonal herd crossings.
- Replaced the wrong citation "Fond 108: Highway Engineering" (Fond 108 holds the 1992 Provisional Government minutes, per the addendum) with an unnumbered territorial highway file. Added the 1962–68 construction for the Toktogul project, the 1996 State Route 1 designation, and reconstruction in 1997–2004 (Otmek Tunnel 2003).

##### Irad Foreign Trade Escrow Authority (Vol2, 4.74)
- **[EXPANDED]** Grew from ~300 to ~600 words, with History, Operation and Criticism.
- **[CANON]** Removed "without violating international trade sanctions" (no sanctions exist in canon). The rationale is now royalty collection plus a supervised payment channel for an unfamiliar jurisdiction. Added the 2008 reconstitution, with the director-general appointed by the Governor and confirmed by the *Mejlis*.
- Removed the unverifiable puffery "statutory autonomy has shielded state export revenues from political interference". During the 2024 crisis the official claim and the opposition's questions are now both attributed, with the DPI line that the Lieutenant Governor acts for the Governor (addendum). There is no hidden-lore content.
- Added specifics: the 11% crude royalty, the remediation levy, correspondent banks (Almaty, Istanbul, Dubai), no audited accounts since 2008, and attributed criticism by Bekzatov.

##### Iradi Antimony and Rare Metals Combine (Vol2, 4.75)
- **[CANON]** Reconciled the corporate structure with newlore (SBAW founded 1961 and privatized 1994) and with Vol3. The Soviet Iradi Antimony Combine was split in 1994 into the SBAW and Chatkal joint-stock companies, with the IARMC formed as their holding company. Removed "controlling all … rare earth deposits across the republic" (tribal deposits are closed).
- **[CANON]** Removed "Irad supplies approximately seven percent of the global antimony market", which confused reserves with market share. Removed the "Northern Border Demarcation Protocol" rail-siding wording.
- Added ownership (closed JSC; an ISEZ minority veto stake since 2009; undisclosed holders, with an attributed allegation of DPI links and the company's denial), 2023 output and revenue (~$140M, company figure), Vol3 figures (Mikhail Chernov) and environmental responsibilities. Removed the closing puffery ("strategic international wealth").
- Rewritten from ~290 to ~690 words.

##### Iradi National Chamber of Mining and Metallurgy (Vol2, 4.76)
- **[CANON]** Replaced "Supreme Council (*Mejlis*)" with "Territorial Legislature of Irad (*Mejlis*)" (brief §2).
- Changed the link [[Nurzhan Petroleum Engineering Polytechnic]] to [[Nurzhan Polytechnic Institute]], following the 4.81 retitle.
- Gold, tungsten and rare-earth exploration is now presented as a chamber demand that is blocked by the tribal moratorium and rejected by the IAC. Added the membership mix (antimony, Tash-Kömür coal, quarries, consultancies, the Nurzhan Heavy Machine Plant), weighted voting, the Chatkal Mountain Rescue Base, post-2024 marketing of antimony outside China, and attributed criticism.
- Rewritten from ~290 to ~530 words. Replaced the irrelevant USGS citation.

##### Iradi Petroleum Transit Consortium (Vol2, 4.77)
- **[CANON]** Rewritten to the NurGaz facts:
  - the 85-km Northern Export Feeder runs into KazTransOil's network near Shymkent;
  - crude moved by rail to Shymkent until 2000, and the feeder opened in November 2000;
  - the CPC connection and the "Black Sea tanker terminals" are removed;
  - the article states that the feeder does not connect to the CPC;
  - the "heavy-crude" description is corrected to the waxy light crude of the Chu fields.
- **[CANON]** Capacity and throughput are now consistent with production minus refining. The original capacity was 65,000 bpd, raised to about 100,000 bpd by a 2011–12 expansion. IPTC reported 2023 throughput of about 86,000 bpd, which is roughly 120,000 minus 31,000. Independent estimates of 55,000–70,000 bpd follow from the 85,000–100,000 bpd production range (addendum).
- Added the board chair [[Emil Bekzatov]] (A6), unnamed minority holders, the tariff, the 2007 war, transit relations under the 2008 protocol, and Kazakh scheduling pressure during water disputes (existing canon, attributed to authorities and not to KazTransOil). Removed "indispensable geopolitical role".
- Rewritten from ~280 to ~720 words.

##### Iradiya (Vol2, 4.78)
- **[EXPANDED]** Grew from ~300 to ~880 words, with History, Operations (passenger charters; domestic; cargo; government and contract flights), Fleet, Corporate affairs and Incidents.
- **[CANON]** Removed "national flag carrier". It is now a charter and air-cargo operator founded in 1997 with civil hangars beside Talas Air Base (newlore, A5). The article explains that ISEZ officials sometimes call it the national airline but that it has no scheduled international routes and Irad has no designated flag carrier.
- **[CANON]** Removed the daily Talas–Nurzhan shuttle (Nurzhan has no passenger airport, per A5) and the Boz-Korgon "fortified chancellery" VIP flights. The Talas–Tash-Kömür subsidized service is the domestic route, the winter alternative to the highway.
- Added the regulatory position: FAA oversight in the territorial era, the ISEZ Civil Aviation Directorate since 2007, ad hoc foreign permits, no ICAO membership, and Bermuda registration. Added the fleet (eight aircraft, company figure), the UNMI contract and a 2012 non-fatal incident. Replaced "An-12" with "An-26". Removed "safely and efficiently" and "northern Transoxiana".
- Replaced the wrong archive citation (Fond 108) and *Jane's* with in-world sources. The legal name is now "Irad Air Services" (newlore).

##### Chatkal Chemical Smelting Complex (Vol2, 4.79)
- **[CANON]** Located the complex in the Sary-Bulak District at the Talas Alatau–Chatkal junction, ~30 km south-west of Talas. Matched the dates to the antimony cluster and Vol3 (1964; the 1971 directive; Mikhail Chernov, Svetlana Kozlova, Artem Kozlov).
- Corrected the process description: volatilization roasting, reduction and fire refining to ~99.65% metal, and trioxide re-volatilization. Removed "semiconductor-grade master alloys", "electrolytic refining hall 99.95%" and "flagship metallurgical combine".
- Removed the unattributed "capture 99.8% of atmospheric particulates" and "indispensable engine of national industrial prosperity". Emissions are now the company's claim against a 2018 UNMI survey. Added 2023 output (company figure) and a works-settlement section.
- Rewritten from ~290 to ~635 words.

##### Nurzhan Agro-Industrial (Vol2, 4.80)
- **[CANON]** Corrected "Bekzat Toktarov, the fourth son" to the **fifth** son (addendum birth order: Bekzat, 1986). Matched D3 4.64: head since 2009, Tashkent Agrarian Institute, the ~70% feed share (as a company claim), seed and fertilizer import rights, and dealings with the Aksay cooperative.
- Added History (Soviet procurement system, 2008 auction and attributed criticism, 2011 mill), Business and Criticism (attributed, including the leaked US reports as worded in A2). Removed "plays a vital stabilizing role" and "Irad's thriving beef export industry".
- Rewritten from ~285 to ~610 words. No new negative claims about Sukarne or Conagra.

##### Nurzhan Polytechnic Institute (Vol2, 4.81; formerly "Nurzhan Petroleum Engineering Polytechnic")
- **[RETITLED]** The article is now "Nurzhan Polytechnic Institute" (owner article per brief §11). The Vol3 stub "Nurzhan Polytechnic Institute" (E3) is to be deleted by its chunk.
- **[EXPANDED]** Grew from ~270 to ~820 words, with History (Soviet; territorial; since 2007), Organization, Campus, Research and partnerships, and Recognition.
- **[CANON]** Per newlore it is formerly the Kobozev Polytechnic Institute and the country's foremost technical university, specializing in petroleum engineering. The 1968 founding "for the newly discovered Iradneft fields" contradicted the 1949 discovery (and D2 4.25). It is now founded in 1951 as the Kobozev Petroleum Institute, became the Kobozev Polytechnic Institute in 1968 when civil, mechanical and electrical faculties were added, and was renamed in 1993 under the Toponymic Heritage Statute.
- **[CANON]** Added [[Aidar Maksat]] (civil engineering, 2002, matching A4), Askar Daniyarov of tüntolk (radio electronics, D1), the military department training State Defense Corps technical officers (A6), and Bekzatov Foundation scholarships (A4). Faculties now include civil engineering and radio electronics.
- Removed "intimate institutional partnership", "guaranteeing immediate professional employment" and "intellectual foundation of … energy sovereignty". Added the language-policy friction with Russo staff and degree recognition under unresolved status.

##### Old Talas Citadel Quarter (Vol2, 4.82)
- **[EXPANDED]** Grew from ~280 to ~1,140 words, with History (medieval town; Kokand fortress; Russian and Soviet periods; since 1992), Layout and landmarks, Crafts and economy, Population and Culture.
- **[CANON]** Matched Vol1 Talas (A1). The citadel is the 18th-century Kokand fortress *Köhne Diz*, with Bazar-i Kalan, *kucheh* lanes and the Diz Film Festival in the citadel courtyards. The medieval layer follows Talas/Taraz historiography, including the minaret foundations, Syriac-inscribed gravestones and Shelji silver. The Treaty of Talas (1727), the 1860s Russian occupation and the 1916 attack on the garrison are included. The fictitious Iradi name *Eski Talas Diz-Shahary* and the "fourteenth-century" brick gate are gone.
- Removed the irrelevant UNESCO 2014 Silk Roads citation. The quarter is not World Heritage-listed, and the article notes that Irad is not a State Party.
- Added the 1997 Historic Districts Ordinance (64 ha, two-story limit), territorial-era US Historic Preservation Fund grants, the 1992 Suusamyr earthquake, and the post-2007 redevelopment controversy (attributed). Landmarks added are the Kalan Darwaza, the Misgaron row, the Juma Mosque, the Church of St. Yuhanna and the excavation shelter. Fixed links to [[Komuz (Iradi)]], [[Kamcha (Horsewhip)]], [[Eerchilik (Saddlery)]] and [[Tolonbek Sydykov]] (workshop in Old Talas, Vol3).
- Removed "hereditary trade guilds recognized by the municipal government", "renowned" and "vibrant center".

Untouched articles: none (all 18 edited).


### Chunk D5

### Changelog: Chunk D5 (Vol2 4.83–4.100)

##### Sary-Bulak Antimony Works (Vol2, 4.83)
- **[EXPANDED]** Expanded from 2 short sections (~250 words) to ~1,100 words with History (Soviet period; crisis and privatization; since 2007), Geology, Operations, Workforce and settlement, and Safety and environment.
- **[CANON]** Added the 1961 founding and 1994 privatization (newlore), the 1971 Antimony Expansion Directive, exports to China by rail through Kazakhstan, its location in the ISEZ's Sary-Bulak District, and its relationship to the Chatkal smelter and the Iradi Antimony and Rare Metals Combine (mining arm, controlling stake), matching the Economy of Irad article.
- Toned down unsupported claims: "one of the richest active antimony deposits in Eurasia" and the 4.5–7.2% grade are now Soviet-era grades of 5–7% in the richest veins, with a current company-reported head grade of about 3%. The 350,000 t throughput is now attributed to the company. The 7% reserves figure is now attributed to estimates for Irad as a whole.
- Added the 1990s flooding and re-equipment, the 1995 Hydrocarbon and Mining Code, the 1998 strike, the workers' settlement (Rudnik, about 5,000 people), tailings monitoring (consistent with the Talas River Hydrological Monitoring Service article), tribal objections to a new tailings dam, a 2012 accident, and the 2024 Chinese export restrictions as price context.
- Replaced the 2 generic references with 8 in-world and descriptive sources. Added inline citations.

##### St. Luka Community Health Mission (Vol2, 4.84; formerly "Luka Community Health Mission")
- **[RETITLED]** Now "St. Luka Community Health Mission", following the brief §8 "St." convention for Christian institutions. The Iradi name *Iyık Luka* already meant "St. Luka". The hospital is now "St. Luka Hospital" (formerly "Luka Diocesan Hospital").
- **[EXPANDED]** Expanded to ~720 words with History, Services, Work in the tribal regions, and Organization and funding.
- Removed puffery ("signature humanitarian breakthrough", "essential humanitarian bridge … across northern Transoxiana", "Respected by tribal chieftains and municipal authorities alike").
- Added: founding by the Eparchy of Talas in 1994 during the post-1992 health-system collapse; the Order of St. Janyl the Hermit (A1); proceeds from *Swift Hooves*, attributed to the mission (canon §5); treatment of casualties during the 2007 investment of Talas; UNMI coordination-forum corridors and cross-line permits; consultation figures attributed to the mission's 2023 annual report (cited by A2); staffing and funding; the link to the Vol3 [[St. Luka Clinic]] stub.

##### Sukarne Irad Complex (Vol2, 4.85)
- Rewrote in neutral tone. Removed "massive", "state-of-the-art", "vibrant", "well-paying", "fair market prices", "premier example of successful global agro-industrial integration" and the crammed bullet paragraph. Added no negative claims about the company (brief §7).
- **[CANON]** Corrected "slaughter of equines is strictly criminalized … under the Iradi Horsemeat Taboo" to the 1996 territorial act banning commercial equine slaughter and horsemeat sales (addendum). Kept "largest feedlot and packing complex in Eurasia" as the company's own description at opening (baselore).
- Corrected the duty-free/NAFTA framing (Irad was not a NAFTA party; matches Economy of Irad). Added the 1998 Talas Agribusiness Accord. Harmonized the feedlot capacity with the Vol3 [[Sukarne Feedlot Complex]] stub (about 50,000 head). Added a halal export line, cattle supply from the ATR via crossing corridors and the Talas Central Cattle Mart, the Morkhan irony (brief §5), the 2007 interruption, and the Nuevo Talas Mexican community (A1).

##### Syro-Iradi Episcopal Synod (Vol2, 4.86)
- **[EXPANDED]** Expanded with Canonical status, History, Membership and procedure, Functions, and Relations with the state.
- Explained that under the CCEO a metropolitan church *sui iuris* has a council of hierarchs, so the synod keeps its traditional name while functioning as one. Named Archbishop Mar Ephrem (since 2012), the four eparchies and the St. Ephrem Major Seminary, matching A1.
- Removed editorializing ("indispensable role as a moral compass", "uncompromised institutional independence, resisting executive encroachment from … Boz-Korgon", "most respected civil society institution"). The trust claim is now attributed to a 2021 Talas State University survey. The 2024 stance is now a quoted, attributed communiqué that makes no hidden-lore claims.
- Added the 1931 union, the 1937 purges, the first open session in 1993, vernacular texts, church-property restitution under the treaty guarantees (A5), the 2004 UNESCO nomination, the April 2007 pastoral letter and the 2023 appeal for restraint. Fixed the crammed bullet list.

##### Talas Agribusiness Export Zone (Vol2, 4.87)
- Rewrote and expanded with History, Facilities, Administration and customs, and Economic role. Fixed the crammed bullet list. Removed "state-of-the-art", "massive" and "demonstrating the commercial viability…".
- Replaced the unsourced "$450 million" export figure, which duplicated the Economy article's US-base figure, with an attributed Chamber estimate (~$310 million, 2023). Removed the anachronistic "Northern Border Demarcation Protocol" (a 2008 instrument) from a 1998 zone's customs description.
- Added the 1998 accord, a hatnote-style distinction from the Vol3 [[Talas Free Economic Trade Zone]], links to the Conagra facility, Cold Chain Hub and Sukarne labs, the 2007 confirmation of the regime, and attributed farmers' complaints about land compensation and duty-free feed imports.

##### Talas Basin Agricultural Directorate (Vol2, 4.88)
- **[CANON]** Corrected "three administrative districts" to Talas District, Kara-Buura District and the farmland of Talas city (brief §3). Removed the misuse of State Archives Fond 108 (reserved for 1992 records, per the addendum).
- Rewrote with History (Soviet farms, the equal Talas division with Kazakhstan, matching D2, the 1994 land reform, the 1995 founding, water users' associations), Irrigation, Crops and extension (including the valley's bean exports) and Criticism. Fixed the crammed list and removed the closing puffery ("flourishing agricultural center").

##### Talas Municipal Water Authority (Vol2, 4.89)
- Removed puffery and pseudo-technical wording ("pristine", "cryogenic glacial melt", "exceptional natural purity", "reliable, clean water round the clock").
- Reconciled the supply with the Vol3 [[Talas Municipal Water Treatment Works]] stub: mostly groundwater plus a treated river intake. Corrected the Iradi name to *Suu* (water) from *Suat* (irrigation). Removed the misuse of Fond 108.
- Added History (the 1930s supply, the 1974 sewage plant, the water cut in the 1992 siege as in A2, 1995 incorporation, 2016 SCADA), city-government accountability (addendum), non-revenue water, unsewered suburbs, and dual-currency tariffs.

##### Talas Regional Hospital Medical Complex (Vol2, 4.90)
- Rewrote and expanded with History, Departments and facilities, Teaching, and Access and finance. Removed "premier", "state-of-the-art", "pillar of national healthcare resilience" and "northern Transoxiana".
- Removed the helipad claim tied to [[Iradiya]], whose fleet (D4) has no helicopters; the helipad is now used for mountain medevacs, including UNMI-arranged cross-line cases. Distinguished the hospital from the Vol3 [[Talas Municipal Hospital No. 1]]. Removed the misuse of Fond 108.
- Added the 1954 Soviet origins, the 1956 riot records (as in D2), operation under shelling in 1992, territorial-era rebuilding and US-style residencies, 2007, co-payments and staff emigration. Updated the link to the retitled St. Luka Community Health Mission.

##### Talasbank (Vol2, 4.91)
- **[EXPANDED]** Expanded from ~300 to ~1,080 words with History (background; foundation and territorial period; the 2006–07 crisis; since 2007), Operations, and Ownership and criticism. This is the owner article; the Vol3 duplicate is deleted by its chunk (brief §11).
- **[CANON]** Chartered in 1993 by the Banking and Commercial Currency Act after dollarization. Dual-currency USD and som operations. Export escrow with the 1994 Foreign Trade Escrow Authority. Correspondents in Almaty and Istanbul. SMS payments with Attelkom (A2, A6). Changed the Cyrillic Iradi name to Latin script, which is used for Iradi since 1992.
- Removed "directs the financial and monetary clearing infrastructure", "anchoring the economic stability of the republic", "remain fully solvent" and similar brochure wording.
- Added: formation from Soviet bank branches, 1999–2001 share sales, the December 2006 withdrawal limits, the loss of US correspondents, the contested escrow accounts between the DRI and the emergency administration in 2007, ownership opacity with attributed reports of links to associates of the ruling family (public, brief §6), and a balancing business view.

##### Trans-Chuy Freight & Logistics (Vol2, 4.92)
- **[CANON]** Corrected Timur Toktarov from "second son" to **third son** (addendum birth order: Ruslan, Alikhan, Timur, Adil, Bekzat). Corrected "border crossings into Kazakhstan and Russia" (Irad does not border Russia) to crossings into Kazakhstan with onward freight to Russia.
- Rewrote with History, Operations, and Ownership and criticism. Fixed the crammed list. Removed promotional closing lines. Criticism of preferential treatment is attributed to competitors and opposition commentators, with the company's response.

##### Trans-Irad Pipeline Proposals (Vol2, 4.93)
- **[CANON]** Changed the route so the line now leaves Irad through Kyrgyz territory (Irad has no border with China), with northern (Talas valley–Fergana Gateway) and southern (Fergana Rim–Lower Naryn) study variants. Kept CNPC as proposer, with no negative claims (brief §7). Kept the tribal vetoes under Bektur Zhumabek uulu.
- **[CANON]** Added the background on the Northern Export Feeder and KazTransOil (no CPC, brief §5), and the territorial-era US-backed southern oil pipeline to Pakistan via Kyrgyz, Tajik and Afghan territory, ended after 2021 with Chevron's scale-back (baselore wording).
- Removed puffery ("indispensable player in Eurasian energy geopolitics", "transformative opportunity") and the Boz-Korgon attribution of DPI backing. Added the 2022 CNPC delegation received by Maksat (public, A4 reference), status and financing obstacles, and competition from existing routes through Kazakhstan.

##### Xinjiang Lihua Cotton Facilities (Vol2, 4.94)
- Restructured as multiple facilities: gins in the Lower Naryn District and lower Chu, plus a Chu District spinning and oilseed complex. This matches where cotton is grown (Economy of Irad) and the Vol3 [[Xinjiang Lihua Ginning Mill No. 3]] stub.
- Kept the canon water-compliance concerns, attributed to farmers' groups and researchers and modest, with the company's response. Added no new negative claims. Removed "local corporate partners affiliated with the DPI", "Belt and Road" promotional wording and the anachronistic Northern Border Demarcation Protocol reference.

##### Zhetysu Industrial Textiles (Vol2, 4.95)
- **[CANON]** Added a Water shortages section; water shortage bottlenecks are canon in newlore. Added cotton thread to the product range (newlore).
- Rewrote with History (1962 Kobozev combine, 1995 privatization), Production, Water shortages and Markets. Fixed the crammed list. Removed "enduring symbol of industrial craftsmanship in northern Transoxiana" and "Swiss formulations". Linked the State Defense Corps via [[Armed Forces of Irad]].

##### Amanbek Alimbekov (Vol2, 4.96)
- **[EXPANDED]** Rewrote as a full biography (~1,670 words): lead, Early life and education, Academic career and dissent, Winter Uprising and Provisional Presidency (with #### subsections), Territorial period, Death, Legacy and assessments, Personal life, and Selected works.
- **[CANON]** Provisional President from 11 March 1992 (Talas Town Hall Meeting, municipal theater). Treaty signed 2 June 1992 and ratified the same day. Kobozev renamed Nurzhan in a September 1992 speech, confirmed by the 1993 Toponymic Heritage Statute. Kobozev/Nurzhan naming is now correct by date throughout. Matched A2, A5 and A6 on the 3 February shootings, the coordinating council, the 10 April–25 May siege, the envoys to Almaty and Geneva, and Alimbekov remaining in the city.
- **[CANON]** Corrected "oversaw the ratification of the Organic Act" (a US Act of Congress) to dissolving the Provisional Government when the interim legislature met in October 1992. Replaced "Senior Advisor to the Territorial Governor" and "Territorial Executive Council" with senior adviser to the territorial government (A2, A5). His death (14 November 2004, Talas; buried in Iyık Janyl) is kept as in A5.
- Fixed the heading scheme (unnumbered `###` subsections became `##` and `####`). Removed the reference padding with unrelated real books (Vine, Bar Hebraeus, Pierce) and irrelevant OSCE and UN 2023 citations. There are now 9 in-world sources, including his memoir.

##### Vasily Chernov (Vol2, 4.97)
- **[EXPANDED]** Rewrote as a full biography (~1,380 words): lead, Early life and education, Refinery and party career, President of the Socialist Republic (with #### subsections), Exile, and Legacy and assessments.
- **[CANON]** Changed the Winter Uprising crackdown from "January 1992" to **3 February 1992**, with A6's casualty range and the 2002 commission. He led the SRI based in Kobozev, went into exile in Russia after August 1992, and Russia protested but did not intervene (addendum). He joined Nurzhan Refinery No. 1 in 1958, when the late-1950s refinery was new, and the 1974 expansion is now dated correctly.
- Removed the implausible "American carrier strike aviation and airborne divisions", "pulverized" and the "17th Motorized Rifle Division" variant (now 17th Motor Rifle Division, as in A2 and A6). Corrected the Fond 85 date range (it previously began before he became First Secretary).
- Added the 1990 republican presidency, his conduct during the 1989 bread riots and the August 1991 coup (attributed), the 1995 extradition request, his memoir's positions and his death in 2012. Removed the padded references (Pierce, Vine, Bar Hebraeus, OSCE, UN). There are now 8 in-world sources.

##### Bakyt Orozbekov (Vol2, 4.98)
- **[EXPANDED]** Rewrote as a full biography of a living person (~1,310 words): lead, Early life and education, Legal career in the territorial period, The independence crisis and premiership (with #### subsections), Later life, and Assessments.
- **[CANON]** He was Prime Minister from 9 December 2006, followed by the January–February 2007 privatization scandals, Toktarov's proclamation of the ISEZ on 25 February, the Front's formation in March, the investment of Talas from 22 April, and the 4 June storming, arrest, resignation instrument and handover to a UN compound (addendum, A5). Matched the Supreme Court article (Isakov, automatic reversion, no ruling on the annulment) and the Legislature article (Senate chief counsel 1998–2005).
- Removed the Fulbright scholarship (implausible for a resident of a US territory), now a territorial government scholarship. Removed the named real clients (Chevron, Sukarne, Conagra) to avoid linking real companies to the scandal narrative. Removed "deeply corrupt" in the article's own voice and "permanent partition"; corruption findings are now attributed to investigative reporting, with his denial. Linked [[Democratic Republic of Irad]] instead of [[Proclamation of the DRI]] in the lead.
- Added later life (Istanbul exile, 2008 in-absentia charges, 2012 memoir, legal positions) and balanced assessments. Removed the padded references (Vine, Bar Hebraeus, Pierce, OSCE, UN). There are now 10 sources.

##### Toktogul Hydroelectric Complex (Vol2, 4.99)
- **[EXPANDED]** Expanded from ~330 to ~1,200 words with Location, History (construction; Soviet operation; 1991–2007; since 2007), Engineering, Divided control, Water management, and Revenue.
- **[CANON]** Checked against the addendum. UNMI supervises; the Joint Liaison Committee meets monthly at Kara-Oi; the restricted-weapons zone is 12 km; El-Choro guards the dam; the Gendarmerie and the MKK Lower Naryn battalion at Tash-Kömür guard the ISEZ side; the dam is on the tribal side; the switchyard, dispatch and downstream cascade (Tash-Kömür, Lower Naryn District) are on the ISEZ side. Fixed the UNMI reference location from "Talas" to Kara-Oi.
- The real-world approximations are hedged (dam about 215 m, reservoir about 19 km³, mid-1970s completion, output 4–4.5 TWh) with an explicit note. Added construction from 1962 (A3), the Kara-Köl workers' town, the resettlement of the old town of Toktogul, the 2007 skirmishes (A5), and the 2008 low-water year.

##### Naryn Water and Power Protocol (Vol2, 4.100)
- **[EXPANDED]** Expanded to ~1,060 words with Background, Provisions (proper list), Operation, Relations with Uzbekistan and Kazakhstan, The Kyrgyz position, Domestic disputes, and Assessment.
- **[CANON]** Matched UNMI (A6): UNMI chairs the joint technical commission, which meets at the Tash-Kömür sector headquarters; security incidents go to the Joint Liaison Committee at Kara-Oi; disputes go to the SRSG; the 2027 renewal and the Maksat signature question are kept. Corrected "oil and gas exports" (Irad exports no gas) to oil exports and rail and road freight. Fixed the UNMI reference location to Kara-Oi.
- Improved the style and removed repetition. Added the 2007 negotiation background, the 2008 minimum-reserve rule and the 2012/2017/2022 renewals.

All 18 articles in the chunk were edited; none were left untouched. No merges or deletions were needed within D5.


## Part F. Volume 3 (start and stub): per-article edits


### Chunk E1

### Changelog: chunk E1 (Vol3, articles 1–80: Biographies & Leadership; Culture & Music; Culture, Arts & Folklore)

This pass was done in two sessions. The first editor rewrote 78 of the 79 surviving articles and deleted the Zara stub, but left no changelog; the entries below cover that work, worked out by comparing the chunk with the original Vol3 lines 1–577. The resuming editor checked every article against the brief, the addendum and the related articles in other chunks, then made the follow-up fixes marked *(resume)*. Size went from 34 KB to about 130 KB.

Changes that apply to every article: each original two-sentence entry was rewritten as a start-class article. Each now has a lead with dates, specific facts and attribution, a `## References` list in the `<ol class="references">` format with matching `<sup>` markers, and wikilinks to existing titles. Puffery from the original was removed (*visionary, legendary, renowned, prestigious, indispensable, crucial, tirelessly, monumental, masterwork, ultimate*). The assessment lines were kept.

#### Biographies & Leadership

##### Mar Timotheos Alimbekov (Vol3, #1)
- [EXPANDED] Rewrote the article and added sections for early life and episcopate, union with Rome, and Soviet response and death. Added dates (1869–1938) and an arrest in 1937 with death in custody in 1938, according to church records.
- [CANON] Union under *Orientalis Stella* dated 14 September 1931 and negotiated in secret through nuncios abroad (Istanbul, Tehran), per brief §4. Soviet suspicion of the Catholic link is tied to the repression of the 1930s and the 1937 purges, and the cathedral's 1992 reconsecration is dated to the anniversary of the bull (matches A1, A6 and D4).
- *(resume)* Normalized the date-range dash in the lead.

##### Tilek Kurmanov (Vol3, #2)
- [EXPANDED][CANON] Recast him as an ISEZ petitioner (2008–2017) before the UN Special Committee on Decolonization in **New York**, since Irad is not a member state. Laid out the "suspended sovereignty" position and the IAC counter-petitioners, and cited the Committee's annual working paper with no document symbol (brief §5).

##### Gulnara Sadykova (Vol3, #3)
- [EXPANDED] Added dates, the founding of the Legal Defense Guild (2009), its work for detainees after the October 2023 protests (released by end of November 2023, per the addendum) and the 2021 grant audit, with both sides' accounts.

##### Muratbek Tanıp-Biy (Vol3, #4)
- [EXPANDED] Added dates (c. 1805–1874), the Tanıp clan link and descent to Bektur Zhumabek uulu (per the ATR article), the c. 1857 Kara-Suu pasture settlement, and its use as precedent by the Grazing Arbitration Tribunal. Sourcing is attributed to the *sanjyra* and Russian frontier reports. Added a hatnote to [[Muratbek Biy]].

##### Colonel David Sterling (Vol3, #5)
- [EXPANDED][CANON] Dated his arrival to 6 June 1992 (start of Operation Starlight) and the end of the siege to 18 June, per the addendum. Removed the overstated "drafting initial logistics plans"; he now heads the liaison office until 1994. Cites Fonds 108 and 131.

##### Kanybek Zhumaliev (Vol3, #6)
- [EXPANDED][CANON] He was Speaker of the Territorial **House of Representatives** (1994–1998), matching the bicameral territorial legislature in the addendum; the original said "Speaker of the Territorial Legislature". Added his role as a DPI founder (October 1992), the content of the 1995 acts and the later criticism by herders' groups.

##### Chingiz Asanov (Vol3, #7)
- [EXPANDED][CANON] Career at the Sary-Bulak Antimony Works, the 2018 royalty schedule, tailings conditions at Sary-Bulak and Chatkal (current names), contested water permits, and the ATR ban on open-pit mining.

##### Altynai Bekzhanova (Vol3, #8)
- [EXPANDED][CANON] Dates (1903–1979). Uses "Kobozev (now Nurzhan)" for the 1930s, the 1928 Latin alphabet, *korenizatsiia*, and the shift to Russian-language schooling in the late 1930s. Removed "tirelessly".

##### Samat Kasymov (Vol3, #9)
- [EXPANDED][CANON] Attelkom milestones per the addendum (GSM 1997, 4G 2016) and the three-day mobile-data cut in central Talas in October 2023, with both sides' positions. Replaced the original "satellite cellular relay nodes … across remote shepherd passes" with ridge relay towers in the ISEZ highlands, and noted that Attelkom has almost no service in the ATR.

##### Biybolot Moldosh uulu (Vol3, #10; formerly "Biybolot Moldoshev")
- [RETITLED] (first editor) to the patronymic form, keeping the Soviet registration "Moldoshev" in the lead. Reviewed and kept: he is an aksakal of the Karakoyun clan of the ATR and an IAC delegate, so brief §8 (rural and tribal people use patronymics) applies.
- [EXPANDED][CANON] The 2011 summit walkout over the one-third seat offer (brief §4), his advisory role on the Joint Liaison Committee at Kara-Oi, and the 2014 release of ISEZ surveyors. Replaced "demarcation border" with the [[Qara-Chik Demarcation Line]].
- *(resume)* Linked "El-Choro" to [[El-Choro Militias]].

##### Archbishop Mar Ephrem (Vol3, #11)
- [EXPANDED][CANON] Election by the synod in 2012, enthronement at the Church of **St.** Janyl (the original said "Saint Janyl Cathedral"), and his time as bishop of the suffragan Eparchy of Talas. The article now gives four eparchies (matching D4/D5) and states his neutrality between the DPI and the clan councils (matching D4).

##### Dastan Isakov (Vol3, #12)
- [EXPANDED][CANON] Added Career and Statutory Independence Ruling sections. Per the addendum: Chief Justice from 1999, wrote the majority opinion days after 3 December 2006, left the court in 2007, and the court never ruled on the annulment. The executive action is described with no order number.

##### Elena Petrova (Vol3, #13)
- [EXPANDED] A trade unionist at the Kobozev Tractor Combine (pre-1992 name), a city councillor since 1997, the 2012–13 heating-mains campaign, and her alignment with the Russo bloc. Linked [[Russos of Nurzhan]].

##### Mirlan Toktarov (Vol3, #14)
- [CANON] (first editor) Changed him from a son to a **nephew** (son of the Governor's younger brother), and listed the five sons and Zara per brief §5. Noted that foreign press reports have sometimes called him a son.
- *(resume)* [CANON] He is now **managing director** of the Akyel Equine Logistics & Breeding Syndicate, to match D4's article on the syndicate; he previously headed its export division (2009–2014).

##### Kuban Mamytov (Vol3, #15)
- [EXPANDED][CANON] Dates (1949–2013), a patronymic alternative, his roles in the Winter Uprising and the siege, and the historians' view that the irregulars were secondary to Operation Starlight. Added his Fallen Rider funeral. Removed "legendary" and "tactical mastery".
- *(resume)* Fixed an anachronism: the Irad National Guard was organized in 1994 (A6), so he now declines the commission in 1994 instead of immediately after August 1992.

##### Zara Toktarova (Vol3, #16)
- [DELETED] (first editor) Cross-chunk duplicate; the Vol2 article is kept (brief §11). The stub also stated hidden lore as fact (the stroke, Zara's gatekeeping, positioning Maksat), which brief §6 forbids.

##### General Nikolai Voronov (Vol3, #17)
- [EXPANDED][CANON] Given the full name Nikolai Ivanovich (1903–1981), with a hatnote distinguishing him from the real Marshal N. N. Voronov. Per the addendum, martial law came on 17 June 1956, with 14 dead in security records versus several dozen per Iradi researchers, and more than 1,000 detained. His 1990 memoirs are attributed. Replaced "checkpoint riots" with [[1956 Talas Riots]].

##### Azamat Temirov (Vol3, #18)
- [EXPANDED][CANON] Renamed the "Irad Central Bank" to the **Bank of Irad** (matching [[Bank of Irad Clearing House]]). Added the dollar-and-som framework (brief §2) and correspondent banking in Almaty and Istanbul.

##### Kanatbek Niyaz uulu (Vol3, #19; formerly "Kanatbek Niyazov")
- [RETITLED] (first editor) to the patronymic form, keeping the Soviet registration in the lead. Reviewed and kept: he is an adat judge in the ATR Chatkal Highlands, so brief §8 applies.
- [EXPANDED] His seat on the Autonomous Tribal Grazing Arbitration Tribunal and the 2016 pasture settlement. Replaced "carry universal moral force" with Human Rights Watch criticism of adat (women's standing, no appeal).

##### Fatima Yunusova (Vol3, #20)
- [EXPANDED] Dates, the cooperative in Chu District (2003), the 40 percent water saving now attributed to the cooperative's figures, and the 2011 Chu Valley Irrigation Inspectorate subsidy.

##### Oleg Kim (Vol3, #21)
- [EXPANDED][CANON] Dates (1929–2004) and the 1937 deportation to Kobozev. Renamed the "Nurzhan Tractor Combine" to the **Kobozev Tractor Combine**, since Nurzhan is not used before 1992 (brief §8). He was director 1969–1984 and graduated from the Kobozev Polytechnic Institute (now Nurzhan Polytechnic Institute, per newlore).

##### Zamirbek Bakiev (Vol3, #22)
- [EXPANDED][CANON] The Central Square occupation of January 1992, the Territorial **Senate** 1994–2000 (first general elections 1994, per the addendum; the original implied 1992), and the 1996 university self-government act. Removed "fiery".

##### Father Luka Ayyubov (Vol3, #23)
- [EXPANDED] Dates (1939–2011), secret ordination, a translation from the Peshitta checked against the Greek, and a 1998 revision following the 1995 orthography reform.

##### Sergei Nechayev (Iradi Influence) (Vol3, #24)
- [EXPANDED] Lead about the real Nechayev (1847–1882), limited to well-known facts; Iradi-specific claims are cited only to in-world sources (brief §7).
- [CANON] 1918: Iradi irregulars fought alongside the Red Guards against the Kokand Autonomy (brief §5). Added the historians' debate over how much influence the pamphlet had.

##### Bermet Alimbekova (Vol3, #25)
- [EXPANDED] Her Georgetown doctorate (1997), work on the [[1998 Talas Agribusiness Accord]] and the Export Zone, and the 1999 Attelkom auction. "NAFTA trade integration" is reworded as NAFTA-era market access, since Irad was not a NAFTA party (matching D5). Removed "successfully".

##### Talgat Saparov (Vol3, #26)
- [EXPANDED] Linked the correct title [[Talas Free Economic Trade Zone]] (the original said "Talas Free Economic Zone"). Added the 2015 scanners at the Talas Customs Clearance Terminal; the seizure figures are attributed to the zone administration.

##### Keneshbek Arstanov (Vol3, #27)
- [EXPANDED] Dates, his stud founded in 1993, golden-dun coats with *doran* sheen, the National Akyel Studbook, Zharkyn foaled in 2010, and the 2018 portrait.

##### Dr. Aizhan Kulova (Vol3, #28)
- [EXPANDED] Head of programs at the [[St. Luka Community Health Mission]] (founded 1994, per D5). Cross-line corridors negotiated through UNMI, solar vaccine fridges on pack horses, and the 2009–2015 figure attributed to the mission.

##### Bolotbek Daniyarov (Vol3, #29)
- [EXPANDED] The *Irad Times* (founded 1996), its reporting on the DRI privatization documents in December 2006 and January 2007, and the 2013 suspension, with the DPI's stated reason.

##### Emil Bekzatov (Vol3, #30)
- [CANON] The original said "cross-border pipeline". It is now the 85-km Northern Export Feeder (opened 2000) into the KazTransOil network near Shymkent, with no CPC link (brief §2 and addendum). Linked his siblings.

##### Aigul Choro kyzy (Vol3, #31)
- [EXPANDED] Dates (1936–2012), about 640 field recordings made 1962–1989, published transcriptions (1978 and 1995), and teaching at the National Conservatory of Folk Music.

##### Ruslan Kadyrov (Vol3, #32)
- [EXPANDED][CANON] Storming of Talas on 4 June 2007 (addendum), with the Front and ISEZ versions of his defection both attributed. He has lived in exile in the ATR since 2007.

##### Klara Zhumabek kyzy (Vol3, #33)
- [CANON] Identified as Bektur's **younger sister** (born 1972; Bektur born 1968), with their father Zhumabek Asanaly uulu (1934–2001), per the addendum.
- [EXPANDED] Added the Ak Kiyiz cooperative (2005) in the upper Kara-Suu valley and cross-line sales. "Women's rights organizer" now reads as public advocacy for women in clan assemblies.

##### Tolonbek Sydykov (Vol3, #34)
- He is a saddler (*eerchi*) in the Old Talas Citadel Quarter, working on state-gift commissions, with a 2004 saddle in the National Historical Museum. Removed "highest level of contemporary Iradi applied art".

##### Artem Kozlov (Vol3, #35)
- [CANON] Chief engineer of the Chatkal Chemical Smelting Complex in Sary-Bulak District. The 2018 SO₂-to-acid unit is attributed to the company, and residents' complaints are noted.

##### Pyotr Kobozev (Vol3, #36)
- [CANON] This chunk owns the article (brief §11). Real life is cut to minimal facts: Pyotr Alekseyevich Kobozev (1878–1941), Bolshevik railway engineer and Soviet emissary in Turkestan 1918–1919. The original's "death in 1928" is corrected to 1941 (addendum).
- [EXPANDED] Added a section on the city of Kobozev: the railway settlement, the 1925 congress, the 1927 naming, Soviet-era institutions, renaming by Alimbekov in September 1992 ("light of life", per newlore) and the 1993 Toponymic Heritage Statute. No "Dmitry Kobozev" appears, per newlore.

##### Baktygul Omurova (Vol3, #37)
- [EXPANDED] Host of *Kechki Jomok* on IradOne 1994–2020, one of IradOne's few Iradi-language programs (IradOne broadcasts mainly in English, per the addendum). Removed "beloved".

#### Culture & Music

##### Iyık Janyl Seminary Choir (Vol3, #38)
- [EXPANDED][CANON] Choir of the St. Ephrem Major Seminary, formed 1994 (matching D4). The original called East Syriac chant "polyphony"; it now says the chant is traditionally monophonic and the four-part hymns came later. Sings at the Feast of St. Janyl on **24 August** (addendum). Removed "founded by master iconographers" and "primary cultural ambassador".

#### Culture, Arts & Folklore

##### Irad Palace of Art (Vol3, #39)
- [EXPANDED] Founded 1996, with a collections list as a real Markdown list, the conservation workshop and funding sources. Kept the newlore wording ("foremost gallery") as "generally regarded as the country's leading gallery".

##### Irad Film Society (Vol3, #40)
- [EXPANDED][CANON] Added History, Festival and Preservation sections: founded 1993, festival in odd years from 1995, a record 2005 edition (newlore), 2007 cancelled, and the decline with the society's and critics' explanations. Restoration dates follow the addendum. Kok-Terek and Tolkun are named as lost Sadikov films.

##### Komuz (Iradi) (Vol3, #41)
- [EXPANDED] Added Construction, Technique and History sections, the Kambar legend, and its use in Mor-Wave, Mor-Pop, Mor-Folk and country-folk. Removed "thunderous".

##### Kyl-kyak (Vol3, #42)
- Accurate construction (hair from living horses, not a "prize mare's unspun" hair). Shamanic use is now attributed to ethnographers' records, and modern uses are added. Removed "indispensable".

##### The Legend of the White Rider (Vol3, #43)
- [EXPANDED][CANON] The Janyl vision and First Church of Janyl, per newlore, plus a narratives list, scholarly interpretation, and cultural uses. The flag stallion's link to the White Rider is attributed to popular interpretation, alongside the official equestrian reading.

##### Körktüülük (Vol3, #44)
- Defined with etymology. Use as a judging criterion at the Salburun festival (matching other chunks).

##### Swift Hooves (Compilation) (Vol3, #45)
- [EXPANDED][CANON] Per brief §5 and newlore, this is a 1993 **American** compilation of country and folk songs **about Irad**, by American artists, with profits to Christian charities. It drew on 1980s Cold War songs carried on smuggled cassettes and VOA, and together they gave rise to Iradi country-folk. Added Background, Production, Charitable use and Reception sections. Removed the original's claim that it was a cassette "of songs about horses that swept across Irad".

##### Irda (Vocal Tradition) (Vol3, #46)
- Rewritten with the etymology hypothesis (attributed; matches Vol1), the church usage and the Choro kyzy collection. Removed "without vocal strain".

##### Shyrdak (Iradi Craft) (Vol3, #47)
- Fixed the grammar of the original lead. Described the technique accurately, plus dyes, dowry use, and the cooperatives and Zhetysu Industrial Textiles.

##### Kymyz (Iradi Beverage) (Vol3, #48)
- [EXPANDED][CANON] Mare's milk is acceptable while horsemeat is taboo (newlore). Production, customs and commercial sections. Removed "sacred national beverage" and "nutritional vitality".

##### Beshbarmak (Iradi Style) (Vol3, #49)
- [CANON] Beef or mutton only. The taboo is described without endorsing it. Beef's prominence is dated to the territorial-era industry (brief §5).

##### Kazy (Vol3, #50)
- [CANON] Beef or lamb, seasoned with wild mountain cumin (newlore). The view of horsemeat kazy as "Muslim" is presented as a popular prejudice, per ethnographers (brief §5); this replaces the original's "unlike neighboring Muslim cultures".

##### Ak-Örgoe (Vol3, #51)
- Corrected to the white ceremonial yurt versus the everyday *boz üy*. Yurt parts linked, plus uses at the August Kurultai and as tent chapels.

##### Eerchilik (Saddlery) (Vol3, #52)
- Rewritten with an etymology, construction, the Soviet decline and revival, and the citadel guild. Removed "prestigious".

##### Talasfilm Studios (Vol3, #53)
- [EXPANDED][CANON] Added Soviet period, post-1989 and Restorations sections. Films and directors per the addendum: Sadikov's *Kok-Terek* (1959, lost) and *Tolkun* (1963, lost), Karimov banned in 1983, Osmonov's *Rise of Glory*, restorations 2004/2011/2014/2019. Consistent with D1 (Sadikov, tüntolk).

##### Jolchu (Album) (Vol3, #54)
- [CANON] tüntolk's 1999 debut, made in Nurzhan, launched Mor-Wave (addendum). The gear and lyric details match the D1 tüntolk article. The original's "ancient Syriac liturgical chants" and "cult status across European underground scenes" are removed; foreign interest is dated to after 2014.

##### Mor-Pop (Vol3, #55)
- [CANON] A commercial subgenre from the second wave (mid-2010s), with the 2015 IradOne youth channel (matching D1). "Dominates … throughout Central Asia" is replaced with specific, attributed reach.

##### Mor-Folk (Vol3, #56)
- [CANON] An acoustic subgenre that uses chant melodies. It developed in Talas in the 2010s, is played at the Mor-Wave festival (since 2016, per D1), and draws clergy debate over Morkhan imagery.
- *(resume)* Added the June 2019 cancelled Iyık Janyl concert, which reference [2] cites but the text did not mention.

##### The Epic of Janyl (Vol3, #57)
- [EXPANDED] Added Content, Recording, Performance and Relations sections. "Over 50,000 verses" is replaced with "about 48,000 lines" in the longest (1938) version. Christian layers are treated as later additions. Parallels with *Janyl Myrza*.

##### Feast of Saint Janyl (Vol3, #58)
- [EXPANDED][CANON] Dated to **24 August**, with a vigil on 23 August and the pilgrimage running into September (addendum). The original said "every September". Added History, cross-line access, an observances list, and attendance attributed to the archbishopric.
- *(resume)* Removed the unsupported claim that "armed forces of both administrations are barred from the city". Iyık Janyl is an ISEZ city of governorate significance (brief §3) and no other article supports a demilitarized status.

##### Kamcha (Horsewhip) (Vol3, #59)
- Rewritten, with *kyz kuu* and protective customs. Linked related stubs.

##### At Chabysh (Racing) (Vol3, #60)
- Distance (20–50 km), the Directorate's welfare rules and minimum age, and Chongtor/Akyel course preferences. Fixed the lead's grammar.

##### Tyin Emmei (Mounted Sport) (Vol3, #61)
- Rewritten. Removed "extraordinary". Scoring and the *körktüülük* criterion.

##### Oodarysh (Mounted Wrestling) (Vol3, #62)
- Rewritten with rules and sanctioning.

##### Tai-Kazan (Vol3, #63)
- Corrected the goal's description. Carcass up to 35 kg, and padded goals at the Hippodrome since the late-1990s renovation.

##### Choor (Flute) (Vol3, #64)
- Corrected to an end-blown, rim-blown flute. Revival in the 1970s and use in Mor-Folk.

##### Qatiq (Vol3, #65)
- [CANON] Added beet suzma served with Iradi plov (newlore) and the Uzbek-origin term.

##### Kurut (Vol3, #66)
- Rewritten, removing a duplicated sentence.

##### Bürkit-Togoo (Vol3, #67)
- The original's "thick horsehide" is now **cowhide or goat leather**, keeping horse products to mare's milk in line with newlore's emphasis. Added the saddle rest and the eagle's weight.

##### Talas Symphony Orchestra (Vol3, #68)
- Founded in 1965 under the republican philharmonic, with a 1994 US tour during Iradimania and [[Elena Kim]] as concertmaster. Removed "celebrated" and "Tian Shan" phrasing.

##### Kok-Terek (Lost Film) (Vol3, #69)
- [CANON] Sadikov's first feature (1959), now lost, known from stills (addendum and D1). Explains how such films were lost. Removed "crucial milestone".

##### Tolkun (Lost Film) (Vol3, #70)
- [CANON] Sadikov's 1963 experimental short, now lost, with its script and partial soundtrack surviving (D1). Context of the 1962 Manezh affair. Link to tüntolk's name.

##### The Hunter's Vigil (Vol3, #71)
- Rewritten: a four-meter bronze, commissioned in the republican era, and the Salburun gatherings. Removed "monumental".

##### Sakal-Akesi (Vol3, #72)
- Identified as a form of *bata*. Christian and Muslim gestures described.

##### Irad State Hippodrome (Vol3, #73)
- [CANON] Formerly the Central Hippodrome, with ulak tartysh codified in 1953 and the President's Cup in the week of Irad Day (matching D1 and the Vol1 Ulak article). Directorate HQ.

##### Altyn-Zhylky Awards (Vol3, #74)
- Established 1996, with categories and IradOne broadcast. Removed "prestigious" and the contradictory "bronze trophy … golden steed".

##### The Black Blizzard of 1916 (Poem) (Vol3, #75)
- [CANON] Twelve clans named (versus 8–12 in other sources, per the addendum), and recited on **15 August**, the Lost Tribes commemoration. Removed "renowned".

##### Kambarkan (Vol3, #76)
- Rewritten. Removed "masterwork" and "ultimate". Linked [[Kambarkan (Music)]] and the conservatory's correct name.

##### Diz Film Festival (Vol3, #77)
- Founded 2010, with an etymology linked to [[Diz (Architecture)]], contrast with the Talas International festival, and the original's duplicated word ("retrospective retrospectives") fixed.

##### Koshkar Muyuz (Vol3, #78)
- Rewritten. Removed "ubiquitous". Turkic and Mongol parallels.

##### The Star of Irad (Symbol) (Vol3, #79)
- [EXPANDED][CANON] Distinguishes the **five-pointed civic form** (the flag star above the stallion, per newlore and brief §2) from the **eight-pointed ecclesiastical and liturgical form** (kümöch seals, banners, vestments). Notes that older sources wrongly give the flag star eight points. The original claimed the eight-pointed star was "displayed on national flags".

##### Iradi Country-Folk (Vol3, #80)
- [EXPANDED][CANON] Two origins, per brief §5: 1980s smuggled cassettes and VOA, and the 1993 *Swift Hooves*. The original credited only 1990s base exchange. History, subjects and style sections.

---
Untouched articles: none. Every surviving article was revised.


### Chunk E2

### Changelog: chunk E2 (Vol3, Economy categories #81–124 and Geography & Settlements #125–184)

General changes applied to every article in the chunk:
- Rewrote every lead to drop the templated "X is a settlement in [[Irad]]. Situated within a …" construction and the generic closing sentences. Replaced them with specific location (canonical ISEZ district, ISEZ city or ATR planning zone), dates and figures.
- Added a `## References` list in the `<ol class="references">` format to every article (none had one), with matching `<sup>[n]</sup>` markers and in-world sources.
- Removed puffery ("life-giving", "pristine", "breathtaking", "picturesque", "bustling", "premier", "renowned", "vital", "nestled", "serves as", and similar).
- Populations are given as "(2018 census)" for ISEZ places and "(estimate)" for ATR places.
- Article numbers were left unchanged, so the numbers of the three removed articles are now gaps (96, 103, 122).
- Category header count: Economy & Infrastructure 41 → 38. The other category counts are unchanged.

#### Economy & Agriculture

##### Kara-Bulak Grain Logistics Depot (Vol3 #81) [MERGED] [EXPANDED]
- Merged in #103 "Kara-Bulak Grain Elevators", a duplicate describing the same Kara-Bulak grain facility; the other title is kept as an alternative name in the lead. This title was kept because it is the only article in its category.
- Placed the depot in Kara-Bulak (Talas District) and added its history (Soviet grain-receiving enterprise built in 1968, re-equipped in 2003, acquired by Nurzhan Agro-Industrial in 2010), its facilities (150,000 t capacity) and farmers' complaints about NAI's market power (attributed).

#### Economy & Infrastructure

##### Nurzhan Refinery No. 1 (Vol3 #82) [CANON] [EXPANDED]
- Set the history to canon: built in the late 1950s, expanded in 1974, nameplate capacity 50,000 bpd, actual throughput about 31,000 bpd (2023). Catalytic cracking was added in the territorial period.
- Corrected "sweet light crude" to the waxy, low-sulfur crude of the Chu fields.
- Added sections on its products (including fuel for Talas Air Base), its residues going to the asphalt plant, its link to the tank farm and the Northern Export Feeder, the 2007 war, and attributed environmental complaints.

##### Chu Irrigation Canal System (Vol3 #83)
- Matched the Vol2 Inspectorate article: more than 80,000 ha, about 1,200 km of canals, operated from Nurzhan. Removed "automated sluice gates" and "life-giving".
- Added the system's construction period, its conveyance losses and its dependence on upstream Kyrgyz use and the Orto-Sai releases.

##### Talas Central Cattle Mart (Vol3 #84)
- Removed "largest in the Chu-Talas region" and "draft oxen". Located the mart near the Talas Agribusiness Export Zone.
- Added the feedlot buyers and the separate horse section, noting that the 1996 act bans sale for slaughter.

##### Chatkal Antimony Processing Mill (Vol3 #85) [CANON]
- Reframed the mill as the ore-dressing (flotation) plant of the Chatkal Chemical Smelting Complex in Sary-Bulak District, which treats ore from the satellite mines. It is no longer described as "operated by SBAW", which concentrates its own ore at Sary-Bulak.
- Corrected "battery-grade antimony trioxide".
- Added its dates (1964, the 1971 directive, privatized 1994) and its tailings history.

##### State Stud Farm of Talas (Vol3 #86)
- Set the farm to the canon origin (set up by the ISEZ after 2007, under the National Equestrian Sports Directorate) and added its auctions, studbooks and links. Removed "aristocratic", "climate-controlled" and "genetic testing" puffery.

##### Kara-Suu Hydroelectric Station (Vol3 #87) [CANON]
- Made the station small: about 18 MW instead of 45 MW, on the lower Kara-Suu Canyon in Sary-Bulak District. It was built in the early 1960s for the antimony works.
- Stated that Toktogul (1,200 MW) is the main station, and noted that the upper catchment lies on the tribal side.

##### Conagra Talas Beef Facility (Vol3 #88)
- Located the plant in the Talas Agribusiness Export Zone and dated it to just after SuKarne's 1999 opening. Kept the canon about Nebraska training and KFC Irad. Added no negative claims about the company (brief §7).

##### Xinjiang Lihua Ginning Mill No. 3 (Vol3 #89)
- Made the article consistent with Vol2 4.94: the mill is a former Soviet gin acquired in 2018, in Chu District. Lint goes to the company's spinning complex or by rail to Xinjiang.

##### Attelkom Fiber Backbone (Vol3 #90)
- Replaced "national trunk / 100 Gbps" boilerplate with the Vol1 figures: about 1,800 km, five endpoints, and three international routes (two through Kazakhstan, one through Uzbekistan).
- Added the 1990s DoD origins and Maksat's regulatory-board role (2012–2019), and the outage risk (attributed).

##### Trans-Talas Highway (Vol3 #91)
- Corrected "traversing Irad east to west". The road runs along the Talas valley (about 230 km) from the Kazakh border in Kara-Buura District through Kyzyl-Adyr and Talas toward the Otmek Pass.
- Removed "thousands of container trucks daily". Added the junction with the Fergana Mountain Transit Highway and the gravel section beyond the line.

##### Nurzhan Petroleum Pipeline (Vol3 #92) [CANON] [EXPANDED]
- Removed the "340-km export pipeline" and the "Caspian export network". Reframed the line as the 1950s field trunk line (about 118 km) from the Chu fields to Refinery No. 1 and the NurGaz tank farm, which is the head of the 85-km Northern Export Feeder into KazTransOil near Shymkent.
- Added the line's history, including rail exports until 2000, the IPTC formed in 1998 and the Feeder opened in November 2000. Added sections on operation and security, and stated that there is no CPC connection.

##### Aksay Alpine Ranching Cooperative (Vol3 #93)
- Rewrote it as the smaller cattle-and-yak cooperative (founded 2004, about 300 households, a breakaway from the Aksay Plateau Pastoral Cooperative), matching the Vol2 D2 and D4 references to "the smaller" body.
- Removed the "120,000 sheep" figure, which belonged to the larger cooperative's scale.

##### Sukarne Feedlot Complex (Vol3 #94)
- Made the feedlot the feedlot component of the Sukarne Irad Complex (opened 1999). The 50,000-head standing capacity was kept as consistent with 150,000 head a year.
- Added the feed sources and neighbors' complaints about odors (local, attributed, with the company's response).

##### Kemer Antimony Mine (Vol3 #95) [CANON]
- Moved the mine from "the Chatkal mountains" to Sary-Bulak District, where the Talas Alatau meets the Chatkal range, as a satellite mine of the IARMC. Ore goes to the Chatkal mill.
- Added the 1970s opening and the 1992–1997 closure.

##### Talasbank (Bank of Talas) (Vol3 #96) [DELETED]
- Deleted per brief §11; Vol2 4.91 "Talasbank" owns the topic.

##### Chongtor Horse Breeding Guild (Vol3 #97)
- Defined how the guild relates to the Chongtor Studbook Registry: the Registry issues the certificates, not "guild inspectors". Added its tribal membership and its role at the Aksay Kurultai.

##### Talas Municipal Cold Storage (Vol3 #98)
- Made the store a 1976 Soviet municipal cold store holding the city's winter reserve, and distinguished it from the Talas Cold Chain Logistics Hub. Removed "automated forklift" boilerplate.

##### Nurzhan Heavy Machine Plant (Vol3 #99)
- Added the plant's history from Vol1 Nurzhan and Bekzatov: tractor parts, then the 1941 evacuated equipment, then pumpjacks after 1949; Rashid Bekzatov as chief engineer.
- Added its post-1991 decline and current products.

##### Muyunkum Natural Gas Field (Vol3 #100) [CANON] [EXPANDED]
- Placed the field in the ATR Northern Steppe zone. Added its Soviet exploration (1970s), its geology (sour gas and a helium trace, hedged) and the lack of audited reserves.
- Added the clan-consent issue and the link to the CNPC Trans-Irad proposal.
- To reconcile Vol1 Nurzhan (A5), which says Muyunkum gas is boosted at the Nurzhan compressor station, added that a few Soviet wells on the southern margin supply small volumes to Nurzhan under a clan-council arrangement.

##### Susamyr Wool Washing Mill (Vol3 #101)
- Located the mill in the Suusamyr valley (ATR Talas Alatau zone): a seasonal cooperative reopened in 2006 that sells to Zhetysu Industrial Textiles.

##### Talas Solar Park (Vol3 #102) [MERGED]
- Merged in #122 "Boz-Tektir Solar Park", a duplicate (both 50 MW, commissioned 2021, near Talas). Kept this title because Vol1 (A2) links it; Boz-Tektir Solar Park is given as an alternative name.
- Combined the two articles' details: the Boz-Tektir terrace site, 120 ha, single-axis trackers, about 85 GWh a year, and the public–private financing.

##### Kara-Bulak Grain Elevators (Vol3 #103) [MERGED]
- Merged into #81 Kara-Bulak Grain Logistics Depot.

##### Alikhan Media Center (Vol3 #104)
- Matched Vol1 IradOne: Alikhan became chairman in 2015 and the broadcaster moved in in 2017. IradOdin is produced in Nurzhan.
- Removed "produces all national entertainment and news broadcasts". Added the opposition-press criticism (attributed).

##### Chatkal Tailings Repository (Vol3 #105)
- Located the dam in Sary-Bulak District, with shared ISEZ/IARMC responsibility and inspection by the Chatkal Placer Mining Inspectorate. The UNMI findings are hedged.

##### Talas Airport Logistics Hub (Vol3 #106)
- Described it as a bonded terminal on the civil aprons of Talas Air Base, used by Iradiya. Added its opening in the late 1990s.

##### Akyel Breeding Sanctuary (Vol3 #107)
- Vol1 is inconsistent here: Toktarov's article calls the sanctuary "state-funded", while the Akyel article calls it "private". The article now gives both characterizations, attributed (DPI publications versus press reports).
- Removed "lush clover" puffery and "private security" color.

##### Nurzhan Gas Compressor Station (Vol3 #108)
- Removed the "gas flowing north" export framing; Irad exports no gas. The station now boosts associated gas and the small Muyunkum volumes for Nurzhan's heat and city supply.

##### Besh-Tash Timber Concession (Vol3 #109) [CANON]
- Changed "birch and cedar" to Tian Shan spruce and dead juniper (*arsha*; live juniper may not be felled).
- Changed the location from "eastern mountains" to the lower Besh-Tash valley, about 20 km south of Talas, in the buffer zone on the ISEZ side.
- Added attributed reports of illegal cutting.

##### Iradi Leatherworks Factory (Vol3 #110)
- Added the factory's dates (1958 state factory, privatized 1996), its use of cattle hides from the Talas packers, and its customers.

##### Kara-Suu Gold Prospecting Area (Vol3 #111)
- Placed the area on the upper Kara-Suu, ATR Talas Alatau zone. Added the clan bans on mercury and cyanide, the 2003 petition (citing the Talas Herald, as Vol1 does) and the Inspectorate's data exchange.

##### Transoxiana Microfinance Fund (Vol3 #112)
- Removed the templated closing sentence. Added the founding (1998), loan sizes, SMS repayment and the origin of the name.

##### Talas Municipal Water Treatment Works (Vol3 #113)
- Matched Vol2 4.89: most of the city's water comes from wellfields, and the works treats river water for the remainder. Added its dates.

##### Kyzyl-Jar Antimony Shafts (Vol3 #114) [CANON]
- Moved the shafts from "eastern mountain frontier" to southern Sary-Bulak District near the line. They feed the Chatkal mill and were closed from 2007 to 2011.
- Added a hatnote to Kyzyl-Jar (the badlands).

##### East Tian Shan Mineral Survey (Vol3 #115)
- Reframed it as an ISEZ Ministry program from 2016. Added the moratorium, the IAC objection, the territorial-era pledge not to develop uranium and thorium (Mailuu-Suu), and a note on the "East Tian Shan" naming.

##### Nurzhan Asphalt and Bitumen Plant (Vol3 #116)
- Tied the plant to Refinery No. 1's residues and to its customers.

##### Talas Dairy Processing Combine (Vol3 #117)
- Added its 1964 origin and cooperative ownership, its products (including suzma) and the kymyz supply limits from E1.

##### Chui Sugar Refining Corporation (Vol3 #118)
- Located the factory near Besh-Terek, Chu District (built in the 1950s, privatized 1997), and added its dependence on irrigation water. Removed "hundreds of thousands of tons".

##### Karakol Mountain Logistics Depot (Vol3 #119)
- Located the depot at Karakol village in the upper Western Karakol valley (ATR), run by the clan council with aid agencies. Removed "lifesaver".

##### Talas Free Economic Trade Zone (Vol3 #120)
- Distinguished the zone from the Talas Agribusiness Export Zone (per Vol2) and linked Talgat Saparov (E1). Dated it to 2009.

##### Attelkom Data Center (Vol3 #121)
- Matched Vol1: Nurzhan, banking and tax systems. Added the Boz-Korgon links as independent reporting (consistent with Vol1 Boz-Korgon).

##### Boz-Tektir Solar Park (Vol3 #122) [MERGED]
- Merged into #102 Talas Solar Park.

#### Economy & Metallurgy

##### Chatkal Rare Earth Facility (Vol3 #123) [CANON]
- Made the facility consistent with Vol2: it is a by-product plant recovering bismuth and tellurium from smelter residues and does not process rare earths. The name is explained by unrealized 1980s plans. Removed "gallium" and "semiconductor-grade" claims.

#### Economy & Transport

##### Talas Cold Chain Logistics Hub (Vol3 #124)
- Located the hub in the Talas Agribusiness Export Zone (per Vol2 D5) and added its users and transport modes.

#### Geography & Settlements

##### Ak-Tash (Vol3 #125)
- Changed "fortified frontier town" to a village in Kara-Buura District (4,310, 2018 census). Kept the quarries and the spring.
- Added the State Defense Corps' Ak-Tash Training Center (per the Vol1 Armed Forces article) and the karez water supply (per the Vol1 Kariz article).

##### Besh-Terek (Vol3 #126)
- Placed the village in Chu District with a census population, linked to the Chui sugar factory.

##### Kara-Bulak (Vol3 #127) [EXPANDED]
- Placed the town in Talas District, with a census population and its rail and grain role. Added the Andronovo kurgan group from Vol2 4.30 (attributed interpretation).

##### Sary-Chelek (Vol3 #128) [CANON]
- Corrected "seven lakes in western Chatkal" to the lake on the southern Chatkal slopes, ATR Chatkal Highlands zone. Added the real lake data, the reserve dates (1959/1978) and the tribal-side status, all consistent with the Vol2 Sary-Chelek Biosphere Reserve article.

##### Kök-Jar (Vol3 #129)
- Made Kök-Jar an ATR village in the upper Chatkal: a former Soviet antimony exploration mine, closed. Removed the active "smelting furnaces".
- Linked the karez supply and the snow leopard sanctuary wardens (Vol1 and E3).

##### Taldy-Bulak (Vol3 #130)
- Located the valley, split by the line, and made the petroglyph dating plausible (Bronze Age with later additions).

##### Kashka-Suu (Vol3 #131)
- Made the river a southern tributary of the Talas; its small hydropower plants are now specified as each under 2 MW.

##### Cholpon-Bulak (Vol3 #132) [CANON]
- The page uses the canonical renamed form, "Cholpon-Bulak". Located it in Talas District on the Kyrgyz Range piedmont, with a census population. Added the *at chabysh* and falconry links.

##### Bazar-Korgon (Vol3 #133) [CANON] [EXPANDED]
- Rewrote as the real Fergana-rim market town (ATR Fergana Rim zone) on the Kara-Unkur River, with an estimated population of about 34,000. Added sections on history (Kokand market, Soviet district center, post-2007 councils), the economy (walnuts from Arslanbob, cotton, Sunday livestock market) and the population.
- Removed "horsehide tanning guilds".

##### Kyzyl-Jar (Vol3 #134)
- Placed it in the Karatau zone on the Kyzylkum fringe and added a hatnote to the antimony shafts.

##### Orto-Sai Reservoir (Vol3 #135) [CANON] [EXPANDED]
- Reframed the reservoir as Kyrgyz, on the upper Chu, upstream of the Boom Gorge and outside Irad. Explained why it matters to the lower Chu and Chu District irrigation, and that there is no ISEZ–Kyrgyz water agreement.
- Kept 470 million m³, as Vol2 does.

##### Karakol (Vol3 #136)
- Added a hatnote distinguishing it from the Issyk-Kul city, which lies outside Irad. Relocated the village to the upper Western Karakol valley near Suusamyr (ATR) with an estimated population. Removed "nestled".

##### Ak-Suu Canyon (Vol3 #137)
- Identified it as the Aksu canyon in the Aksu-Zhabagly reserve (western Talas Alatau, tribal side), with realistic dimensions and geology.

##### Kenkol Pass (Vol3 #138) [CANON]
- Replaced "connecting the northern Chu plains with eastern pastoral valleys" with a pass at the head of the Kenkol valley in the Talas Alatau, carrying a graded (unpaved) 1960s road.
- Added the Qara-Chik proximity, the 2009 UNMI mine deaths and the 2016 standoff (per Vol1/Vol2).

##### Arslanbob (Vol3 #139) [CANON]
- Corrected and kept as a stub (the full article is by another editor): Fergana Rim zone, the walnut forest, and the Muslim shrine of Arslanbob-Ata.
- The Syro-Iradi hermit tradition is now attributed and hedged rather than stated as fact.

##### Chatkal River (Vol3 #140) [EXPANDED]
- Rewrote with the real course (about 220 km, into Uzbekistan's Charvak Reservoir and the Chirchik), hydrology, the ATR Chatkal Highlands status, the gold history and clan regulation.
- Added a note that the "Chatkal" industrial plants in Sary-Bulak District lie outside the basin.

##### Manas Peak (Irad) (Vol3 #141) [CANON]
- Removed "highest summit in Irad". It is now the highest summit of the Talas Alatau (4,482 m), at the western end near the Uzbek border, with an undemarcated boundary across the massif. Added the Manas Glacier, the observatory (tribal side) and a note that higher summits exist in the Chatkal and Fergana ranges.

##### Kulan-Talaa (Vol3 #142)
- Placed it in the Karatau zone, made the vegetation realistic, and said the kulan was hunted out in the early 20th century.

##### Shahr-i Buzurg (Vol3 #143) [CANON]
- Recast from "settlement" to a Sogdian and Kara-Khanid archaeological site in Chu District (6th–12th century). Explained the Persian name and replaced the anachronistic "5th-century citadel". The finds now match Vol2 4.31.

##### Jety-Kaiyng (Vol3 #144) [CANON]
- The renamed form now fits its name: "seven birches", after the birch grove. The "seven bulls" became a Morkhan legend, tied to the bovine-omen folklore.

##### Urmaral River (Vol3 #145)
- Removed "endemic mountain trout" (there are none); the trout farms raise introduced rainbow trout. Located the river in Talas District with its upper valley on the tribal side.

##### Tuyuk-Suu Pass (Vol3 #146)
- Placed the pass in the central Talas Alatau (ATR) and dropped the unsupported "silk caravans" claim.

##### Kand-i Nau (Vol3 #147) [CANON]
- Recast the "township" as a Kara-Khanid archaeological site. The karez-fed vineyards moved to the modern village of Jangy-Kent beside it, and the Sogdian/Persian etymology was added.

##### Shelji (Vol3 #148) [CANON] [EXPANDED]
- Rewrote as the medieval silver-mining town of the upper Talas valley, with sections on its history and on the site. The old article's "8th-century Nestorian church", inherited from the Ak-Beshim source, became small Christian finds and a disputed church building.
- Matched D2 and D4: silver workings of the 8th–10th centuries, with coins found at Old Talas.

##### Suusamyr (Vol3 #149) [EXPANDED]
- Placed the valley on Irad's eastern margin (ATR Talas Alatau zone; its eastern end is in Kyrgyzstan). Added its climate, summer grazing and the Otmek road, and the 19 August 1992 Suusamyr earthquake, consistent with the D4 and A6 references.

##### Kum-Bel (Vol3 #150) [CANON]
- Changed Kum-Bel from a "mountain range with significant reserves" to a gold prospect in the Chatkal Highlands: Soviet drilling in the 1980s, unbuilt, and under the clan moratorium. It is not a mine.

##### Kara-Buura (Vol3 #151) [CANON] [EXPANDED]
- Removed the "industrial town with fertilizer combines" framing, which came from the renamed Kara-Balta.
- The article now covers the Kara-Buura River and the ISEZ Kara-Buura District (with Kyzyl-Adyr as its center), in sections on the river and the district: agriculture, the highway and border crossing, Ak-Tash, the western Qara-Chik sector, water disputes and the Mejlis constituency. E1 links [[Kara-Buura]] in the district sense.

##### Rabat-i Kamal (Vol3 #152) [CANON]
- Kept it as a Kara-Khanid caravanserai, now placed on the old Karatau-foothill road (ATR). Explained the name and noted the site's condition.

##### Besh-Tash National Park (Vol3 #153) [EXPANDED]
- Matched Vol2 4.40: established 1996, 20 km south of Talas, the core of the 32,400-ha area. Removed the "relict juniper woodlands, virgin spruce" puffery.
- Added the split by the line, the access arrangements and a link to the timber concession.

##### Kyzyl-Adyr (Vol3 #154) [CANON]
- Corrected "middle Talas valley" to the lower valley. Kyzyl-Adyr is now the administrative center of Kara-Buura District (10,370, 2018 census), with its services and horse fair.

##### Shahr-i Kabud (Vol3 #155) [CANON]
- Recast as a historic quarter of Talas on the Kara-Khanid outer suburb (*rabad*), with the archaeology, the name and 1997 ordinance protection.

##### Kök-Moinok (Vol3 #156)
- Placed it in the Karatau zone and removed promotional wording.

##### Talas Alatau (Vol3 #157) [EXPANDED]
- Rewrote with the real extent (about 270 km), Manas Peak, the drainage, vegetation, protected areas and passes (Kara-Buura, Otmek, Fergana Gateway), the antimony foothills, ATR status and the Tien Shan Marches term.
- Corrected "spine of southern Irad, along the southern border".

##### Uzun-Akmat River (Vol3 #158) [CANON]
- The renamed form now describes the real river, which flows to the Toktogul Reservoir (Syr Darya system), mostly through ATR pasture. Removed the "terraced vineyards", which came from the renamed Kurshab.

##### Kand-i Kohna (Vol3 #159) [CANON]
- No longer the "citadel of Old Talas", which conflicted with Vol2 4.82. It is now a separate town mound 6 km west of Talas (Saka to 9th century), with the predecessor hypothesis attributed.
- Removed "Hellenistic pottery".

##### Susamyr River (Vol3 #160)
- Gave its course through the Suusamyr valley to the Kökömeren and Naryn. Removed "pristine" and "potential micro-hydro" filler.

##### Diz-i Zard (Vol3 #161) [CANON]
- Recast as a Kara-Khanid citadel mound in Chu District, reoccupied by a small Kokand fort in the 1820s and taken in 1860–1862.

##### Karakyr Range (Vol3 #162)
- Placed it as a Karatau outlier (ATR) and removed "thousands of raptors"; the raptor counts are now attributed to university ornithologists.

##### Kök-Art Pass (Vol3 #163)
- Moved the pass from the "Chatkal range" to the Fergana Range at the head of the Kök-Art valley, linking the Fergana Rim and Naryn zones.

##### Dastgoh District (Vol3 #164) [CANON] [EXPANDED]
- Corrected the "urban district in [[Irad]]" lead: Dastgoh is an urban district of Nurzhan (population from the 2018 census). The medieval metalworking evidence is attributed to Iradi historians.
- Added the etymology, the Soviet industry and Dastgoh Creek, the NurGaz Pipeline Maintenance Depot and the tüntolk boiler room (per Vol1, Vol2 and D1).

##### Ak-Terek (Vol3 #165)
- Placed it in Talas District, with a census population; removed "tranquil" and "nestled".

##### Kara-Darya (Vol3 #166) [CANON]
- Replaced the "southern plains pelican wetlands" with the real river: a Syr Darya headstream from Kyrgyzstan, through the Andijan Reservoir, joining the Naryn in Uzbekistan. Explained its relevance to Irad through the Fergana Rim tributaries (Kara-Unkur).

##### Rabat-i Sangin (Vol3 #167) [CANON]
- Recast from "Timurid" to a Kara-Khanid stone caravanserai on the upper Kara-Buura route (ATR).

##### Kök-Bel Pass (Vol3 #168)
- Placed the pass across the western Kyrgyz Range between the Talas valley and the Chu District. It is closed in winter and is an alternative to the lowland rail route.

##### Shahr-i Khunuk (Vol3 #169) [CANON]
- Recast as a historic summer quarter of Iyık Janyl, which keeps Khunuk Creek compatible with the E5 stub. Removed the "regional elites" framing; the heritage criticism is attributed.

##### Kyzyl-Suu (Vol3 #170)
- Placed the river on the northern slopes of the western Kyrgyz Range, draining toward the Chu, in Chu District.

##### Boz-Tektir (Vol3 #171) [CANON]
- Removed the false claim that Boz-Tektir lies on the "western security approaches to Boz-Korgon"; Boz-Korgon is 40 km east of Nurzhan. Linked the Talas Solar Park.

##### Navbahor District (Vol3 #172) [CANON]
- Corrected "residential sector of Talas" to an urban district of Nurzhan (per brief §3 and Vol1), with a population from the 2018 census. Removed "Anglo-Iradi architecture" and "manicured" puffery, and linked the E3 cultural term.

##### Kök-Jar Pass (Vol3 #173)
- Placed the pass above Kök-Jar near the Uzbek border; added the El-Choro and Uzbek border-guard context.

##### Kara-Koyun Valley (Vol3 #174)
- Placed the valley in the Talas Alatau zone near the line. Added Biybolot Moldosh uulu and the 2014 release (per E1).

##### Bazar-i Kalan (Vol3 #175) [CANON]
- Made it the historic covered market and market quarter of the Old Talas Citadel Quarter, matching Vol2 4.82: Kokand-era bazaar, hall of the 1950s, Coppersmiths' Row, Uzbek merchant families.

##### Ak-Bulak (Vol3 #176)
- Placed it in Sary-Bulak District with a census population and made its economy specific.

##### Diz-i Safid (Vol3 #177) [CANON]
- Recast as a Kara-Khanid citadel near Iyık Janyl. The claim that 18th-century Christian clans refortified it against the Dzungars is now attributed to church tradition.

##### Keng-Talaa (Vol3 #178)
- Removed "nation's premier annual horse marathon". It is now a Northern Steppe grassland with an autumn *at chabysh* race held under clan rules.

##### Kara-Unkur Cave (Vol3 #179)
- Fixed the contradictory "Upper Paleolithic … Mousterian … 30,000 years" to Middle (Mousterian) and Upper Paleolithic layers. Placed the cave above Bazar-Korgon.
- Noted that the wild-horse bones do not support the domestication claim (brief §5, Botai).

##### Shahr-i Nav (Vol3 #180) [CANON]
- Kept it as the 1962 state-farm village (Chu District, census population). Its Persian name is now explained as taken from nearby Kara-Khanid ruins.

##### Kyzyl-Köl (Vol3 #181)
- Replaced "alpine larch", which does not grow in the Tian Shan, with juniper and spruce, and explained the name.

##### Terek-Sai (Vol3 #182) [CANON]
- Moved Terek-Sai from "eastern Chatkal ranges with deep shaft mines refining at Chatkal" to an ATR Chatkal-valley mining village, not worked by the combine since 2007 (per Vol2 4.67), with an estimated population.

##### Chong-Kenkol (Vol3 #183) [CANON]
- Made it the upper Kenkol valley, with spruce forest under clan protection. Added the Kenkol Hunnic-period burial ground (1st–4th century CE, excavated in the late 1930s), per brief §3 and Vol1 History.

##### Temir-Kapka Gate (Vol3 #184) [CANON]
- Defined it as the surviving northern gate of the Kokand-period outer wall: rebuilt in the 1820s, restored in 2009, and protected under the 1997 ordinance. This distinguishes it from the citadel's Kalan Darwaza in Vol2.
- Replaced the "cedar portals" with iron-sheathed elm doors.

Untouched articles: none (every article in the chunk was edited).


### Chunk E3

### Changelog: chunk E3 (Vol3 start-class History & Events, small categories; stub Cultural & Linguistic Terms; Culture, Language & Folklore)

This chunk was edited in two passes: a first editor (interrupted, no changelog) and a resume editor. Every entry covers both. "(resume)" marks changes made in the resume pass; everything else was done by the first editor and checked by the resume editor against the brief, the addendum and the other chunks.

Common to all 50 start-class articles: rewritten from one-sentence "X is the…" definitions into encyclopedic prose with a defining lead, attributed claims and a `## References` list in `<ol class="references">` format (none existed before); puffery removed ("indispensable", "pivotal", "massive", "historic"); word counts never present.

#### Category: History & Events

##### Treaty of Talas (1727) (Vol3, 185)
- **[EXPANDED]** From 2 sentences to a sectioned article (Background, Terms, Sources and name, Consequences, Legacy). Reframed as a unilateral charter (*firman*) of Abd al-Rahim Biy known from later copies; historians' doubts about the tax clauses and the "Talas" name attributed.
- **[CANON]** "Cathedral of Saint Janyl" → Church of St. Janyl; UNESCO 2004 joint inscription with the Ruins of Old Iyık Janyl on a US nomination.

##### Siege of Kokand (1876) (Vol3, 186)
- **[CANON]** Commander corrected from Chernyayev to **Mikhail Skobelev**; Chernyayev kept only for Tashkent (1865). Chu/Talas valleys placed in the Syr-Darya and Semirechye oblasts (not Fergana Oblast); Kokand annexed as Fergana Oblast in Feb 1876 without a prolonged siege. Added *inorodtsy* status.

##### The Urkun (Iradi Theater) (Vol3, 187)
- **[EXPANDED] [CANON]** Name, background (June 1916 decree, Kuropatkin), the flight, refugees in China and return, memory. Figures aligned with the addendum (about 100,000 fled, 30,000–50,000 died, attributed to Iradi historians; Lost Tribes 8–12 clans, 3,000–10,000+, remembered 15 August). Inverted horseshoe/Fallen Rider link.

##### First Congress of Iradi Soviets (Vol3, 188)
- **[CANON]** Venue changed from "Kobozev" to the railway settlement on the lower Chu that was named Kobozev in 1927 (now Nurzhan); early 1925; admission as a union republic after the Uzbek and Turkmen SSRs (1924). Expanded with delegates, tasks and the 1937–38 fate of delegates.

##### 1928 Latinization Decree (Vol3, 189)
- Placed in the all-Union *Yañalif* campaign and *korenizatsiia*; dropped the unsupported "32-letter" claim for 1928; links to the 1941 and 1995 articles. **[CANON]** script dates.

##### 1941 Cyrillic Mandate (Vol3, 190)
- Context of the 1938–41 all-Union shift; extra letters ө, ү, ң; **[CANON]** Latin restored 1992, revised 1995/1997.

##### Nurzhan Oil Discovery (1949) (Vol3, 191)
- **[CANON]** NurGaz origin and 1993 privatization, Refinery No. 1 (late 1950s, expanded 1974), Kobozev Polytechnic Institute, early-1980s peak of about 140,000 bpd. Attributed note on revenue flowing to the all-Union budget.

##### 1952 Kobozev Steel Strike (Vol3, 192)
- Rewritten as an archival account (Kobozev Heavy Machine Plant), with the caveat that the documents come from the authorities; cross-ethnic claim attributed to labor historians.

##### Decree on Pasture Collectivization (1932) (Vol3, 193)
- Linked to the 1929 all-Union drive and the 1930–33 Kazakh famine; herd-loss claim attributed to Iradi historians.

##### Talas Checkpoint Incident (1956) (Vol3, 194)
- **[CANON]** Framed per brief §5: widow's-horse story "according to popular accounts", with archival vs popular versions; underlying causes (housing, wages, schooling, church, de-Stalinization); 14 June 1956 date; 1996 riderless-horse memorial and 14 June gatherings (addendum).

##### Declaration of State Sovereignty (1991) (Vol3, 195)
- **[CANON]** 9 October 1991 declaration by the Supreme Soviet creating the Socialist Republic of Irad under Vasily Chernov in Kobozev; explained that despite its title it functioned as an independence declaration; removed "unanimously"; noted October 9 is not a public holiday.

##### Talas Town Hall Meeting (1992) (Vol3, 196)
- **[CANON]** 11 March 1992 in the municipal theater; *Declaration of Restoration*; Alimbekov elected Provisional President; 17th Motor Rifle Division sent south in late March; treaty signed in the theater basement on 2 June (consistent with A2/A5).

##### Battle of Kobozev Railhead (1992) (Vol3, 197)
- **[CANON]** Moved to end of July 1992, during Operation Starlight (originally implied before it); "18 tanks" attributed to Iradi accounts, with US accounts crediting air strikes; Kobozev fell 12 August, surrender 18 August.

##### Operation Starlight (1992) (Vol3, 198)
- **[CANON]** Kept as a corrected stub (full article being written separately): began **6 June 1992** with Marines airlifted into the airfield west of Talas; siege broken by 18 June as the 10th Mountain Division arrived; joint advance on Kobozev; surrender 18 August; Organic Act territory; Chernov's safe conduct; death toll about 14,000 (range 9,000 to over 20,000). Removed "peaceful transition into a protectorate".

##### Organic Act of the Territory of Irad (Vol3, 199)
- **[CANON]** Kept as a corrected stub: organized, unincorporated territory from 18 August 1992; elected Governor (Elective Governor Acts); bicameral legislature (Senate 15, House 35), interim legislature from October 1992, first elections 1994; Supreme Court established November 1992; US High Commissioner; statutory independence clause. Removed "North American trade agreements" duty-free claim (replaced with customs access to the US market).

##### Treaty of Good Neighborliness (1994) (Vol3, 200)
- Recast as a water-sharing agreement only (it did not demarcate the frontier, which the 2008 Northern Border Demarcation Protocol addresses for ISEZ sections); its disputed standing since 2006 given Kazakhstan's claim; continuing technical cooperation.

##### 1998 Talas Agribusiness Accord (Vol3, 201)
- Reframed as an investment agreement with the territorial government; SuKarne and Conagra plants kept as canon without new claims; origin of the Mexican community of 10,000+ around Talas.

##### United States Withdrawal from the Alimbekov-Baker Treaty (2006) (Vol3, 202; formerly "Executive Order on the Alimbekov–Baker Treaty (2006)")
- **[RETITLED]** (resume) New title and lead; the instrument is described, not numbered. Links in A3, A5 and D5 still point to the old title (see notes).
- **[CANON]** Bush's executive action of 3 December 2006 described only as in canon; no US notification to the UN, so Irad stayed listed with the US as administering power; US forces remained under the 2001 agreement; DRI proclaimed 9 December. Bush-complex conspiracy theory mentioned only as canon already states it, with the construction-date rebuttal. No new claims about real people.

##### Statutory Independence Ruling (2006) (Vol3, 203)
- **[CANON]** Majority opinion by Chief Justice **Dastan Isakov**, issued days after 3 December (dated 7 December); petition by Bakyt Orozbekov; doctrine of automatic reversion; annulled by Toktarov's 25 February 2007 decree; the court never ruled on the annulment; Isakov left the bench in 2007 (addendum).

##### Proclamation of the DRI (Vol3, 204)
- **[CANON]** 9 December 2006, Orozbekov PM; 26 UN members recognized; continued NSGT listing; deficit after federal transfers stopped; ISEZ proclaimed 25 Feb 2007; DRI dissolved after the 4 June storming.

##### Privatization Scandals of 2007 (Vol3, 205)
- **[CANON]** January–February 2007 asset sales; attributed findings of corruption (investigative reporting, observers); mid-January shooting of herders in the Chu valley and Bekzatov's refusal to recognize NurGaz concession auctions (consistent with A5); 25 Feb ISEZ proclamation; Front formed in March; Talas invested from 22 April, stormed 4 June. Removed "pennies on the dollar" and the claim that the scandals alone caused the war.

##### Storming of Talas (2007) (Vol3, 206)
- **[EXPANDED] [CANON]** Background, investment from 22 April, the storming on 4 June, aftermath, memory. Orozbekov arrested and handed to a UN compound; the Front did not hold Talas; DPI forces with Western-company and US backing took the cities over the summer; IAC founded late 2007 at the Aksay Plateau kurultai. Casualties left disputed.

##### Bishkek Ceasefire Agreement (2007) (Vol3, 207)
- **[CANON]** Kept as a corrected stub: September 2007, UN-brokered, observers from the three neighbors; 420-km Qara-Chik line with southern salient; **12-km restricted-weapons zone** each side; Joint Liaison Committee at Kara-Oi; **Naryn Water and Power Protocol annex**; UNMI established 18 October 2007 (no resolution number).
- (resume) "Recognition of customary law as the law of the tribal regions" → "acknowledgment of customary jurisdiction (*adat*) on the tribal side of the line", matching the D3 *Adat* and A5 articles. The 2023 violation figure (214) had been cited to a 2008 UNMI report; added a 2024 UNMI annual report as its source; 2008 report place corrected to Kara-Oi.

##### 2008 Unification Referendum Initiative (Vol3, 208)
- Confederal draft, collapse over the mining veto, unresolved ATR voter registration and population; 2017 polling with tribal objections attributed.

##### 2011 Bilateral Reunification Summit (Vol3, 209)
- **[EXPANDED] [CANON]** April–May 2011 at Kara-Oi under UNMI; only real bilateral talks; IAC walkout after the one-third offer; agenda, positions, walkout quote (*Talas Herald*), aftermath. Removed "national parliamentary seats" (now unified Territorial Legislature).

##### 2013 Constitutional Amendment (Vol3, 210)
- **[EXPANDED] [CANON]** Clarified it amended the 1992 Elective Governor Acts (removing the two-term limit); election years 2011/2015/2019/2023 with official shares; 60-seat legislature vote (53–4–3); OSCE quote as in A5; Supreme Court declined a 2014 challenge; next election late 2027; succession provisions linked to the 2024 crisis.

##### Battle of the Aksay Pass (1221) (Vol3, 211)
- Reframed as a tradition first recorded in 18th-century church chronicles; noted that Subutai was in Iran and the Caucasus in 1221; possible memory of the 1219 Mongol passage.

##### Nestorian Synod of Navekat (1180) (Vol3, 212)
- Reframed as church tradition without contemporary record; Church of the East under the Qara Khitai accepted; Navekat located near Bishkek, outside Irad.

##### Treaty of Kuldja (Iradi Frontier) (Vol3, 213)
- Corrected to the real 1851 Kulja/Chuguchak trade treaty, which did not concern the Iradi valleys; "Iradi Frontier" explained as a historiographical label; Vernoye (1854) and the 1860s advance.

##### 1898 Andijan Uprising (Iradi Theater) (Vol3, 214)
- Real outline of the Dukchi Ishan rising; the "Iradi theater" (Chatkal mail-convoy attacks) attributed to tradition, with Russian reports calling it brigandage and historians doubting a link.

##### The 1937 NKVD Clerical Purges (Vol3, 215)
- **[CANON]** Removed "Order No. 00447" (addendum: no real Soviet document numbers); "mass operations of the Great Terror" and NKVD troikas instead. 1931 *Orientalis Stella* union as the source of suspicion; the church used as a grain store; caves in the Kara-Suu Canyon; casualty range hedged ("archival estimates"); reconsecration 14 September 1992 (matches A6).

##### 1944 Wartime Mobilization Strike (Vol3, 216)
- Sources (procurement records, oral tradition) and prosecutions added; link to the Chongtor registry re-established in 1993.

##### Founding of Talas Air Base (1952) (Vol3, 217)
- Specifics (12 km west of Talas, 2,500 m runway, MiG-17/21), role in 1956 and 1992 (Marines landed 6 June), runway lengthened 1993–98.

##### 1971 Antimony Expansion Directive (Vol3, 218)
- **[CANON]** Chatkal smelter and Sary-Bulak works (opened 1961); "primary source" softened to "one of the main sources"; ~7% of world reserves; exports to China by rail through Kazakhstan.

##### The Kobozev Bread Riots (1989) (Vol3, 219)
- Demands (church freedom, Latin alphabet, elected government) and Chernov's response; link to the Winter Uprising.

##### March 11 Independence Day (Vol3, 220)
- **[CANON]** Officially Irad Day; ceremony and races at the Irad State Hippodrome; horsemeat taboo; ATR observance. Removed "massive crowds".

##### 1995 Latin Orthography Revision (Vol3, 221)
- **[CANON]** Revision of the 1992 alphabet (ı, ö, ü replacing digraphs); 32-letter alphabet confirmed by the 1997 Language and Education Reform Act.

##### 2001 Basing Rights Agreement (Vol3, 222)
- Operation Enduring Freedom role; continued US presence after 2006 under the ISEZ's "suspended sovereignty" position; IAC objection; post-2014 role.

##### 2003 Judicial Reforms Act (Vol3, 223)
- Drafted by Orozbekov; district courts, jury trials, arbitration; attributed assessments of its record since 2007.

##### 2015 Electoral Reform Controversy (Vol3, 224)
- **[CANON]** November 2015 election, official 78.25%; October disqualifications on signature and residence rules; OSCE assessment; DPI response. Removed "managed vote" (editorializing).

##### 2018 Border Demarcation Clashes (Vol3, 225)
- Clashes relocated from an Uzbek to the Kazakh northwestern frontier (Kyzylkum fringe and Karatau foothills, where ATR sections are undemarcated, consistent with the Northern Border Demarcation Protocol article); casualty reports unconfirmed; local grazing arrangement that Kazakhstan says implies no recognition.
- (resume) "serves as" → "marks" (style).

##### Operation Clear Skies (2020) (Vol3, 226)
- Gendarmerie (Ruslan Toktarov, Major General) and US personnel; division of perimeter duties; origin of drones not identified.

##### The 2021 Regional Security Alert (Vol3, 227)
- **[CANON]** No Afghan border; separate ISEZ and ATR alerts with rare joint coordination.

##### 2023 Student Protests in Talas (Vol3, 228)
- **[CANON] [EXPANDED]** Hidden-lore leak removed: the original stated as fact that protesters were "pawns in a covert influence operation funded by rival DPI factions". Now: October 2023, spontaneous, set off by a municipal licensing surcharge on tech startups and couriers; Ilyasov's *Debate One* criticism as background; Gendarmerie dispersal; three-day mobile-data cut (addendum); surcharge suspended by Maksat in November 2023. Funding claims (pro-government "American money", opposition talk of family factions) appear only as attributed, unproven allegations, with a 2024 study finding no evidence and Ilyasov's denial.

##### The July 2024 Transition Crisis (Vol3, 229)
- **[CANON] [EXPANDED]** Hidden-lore leaks removed: the original stated as fact a "debilitating stroke", permanent incapacity and "synthetic deepfaked speeches". Now: the DPI's health-retreat line, attributed allegations of digital synthesis dismissed as foreign-sponsored disinformation, Maksat's day-to-day role, the publicly visible Ruslan–Alikhan friction, Zara as a non-political academic with unverified tabloid reports, UNMI barred from Boz-Korgon, the 2027 Protocol renewal and election. Cross-reference to the Vol2 "2024 Iradi Executive Transition Crisis".

##### Iradimania (Vol3, 230)
- **[CANON]** Cold War-era songs on smuggled cassettes and VOA in the 1980s; *Swift Hooves* (1993) as an American compilation for Christian charities; both feeding Iradi country-folk. Removed "platinum-selling", "extraordinary"; added critical reception.

##### 2025 Trump Remarks on Irad (Vol3, 231)
- **[DELETED]** Vol2 owns this article (brief §11). Its text included unsupported details (a "demographic protest" at the UN from Boz-Korgon). Deleted by the first editor; verified.

#### Category: Institutions & Security

##### Talas Gendarmerie Academy (Vol3, 232)
- **[CANON]** Gendarmerie commanded since 2012 by Major General Ruslan Toktarov (A4); December 2024 graduation speech attributed as the occasion of his anti-Muslim remarks.

#### Category: Public Institutions & Facilities

##### Chui Cotton Inspection Directorate (Vol3, 233)
- Cotton geography corrected (Fergana Rim and Lower Naryn District first; smaller areas in the Chu and Talas); Xinjiang Lihua named without new claims.

##### Nurzhan Polytechnic Institute (Vol3, 234)
- **[DELETED]** Vol2 owns it ("Nurzhan Petroleum Engineering Polytechnic", retitled; brief §11). Deleted by the first editor; verified.

#### Category: Science & Education

##### Nurzhan Municipal Botanical Institute (Vol3, 235)
- Tightened; wild apple and walnut gene bank (Chatkal, Arslanbob); link to Nurzhan Botanical Gardens.

#### Category: Wildlife, Flora & Nature

##### Chatkal Snow Leopard Sanctuary (Vol3, 236)
- Placed in the ATR Chatkal Highlands zone; implausible "35 individuals" replaced by camera-trap estimate of about a dozen; managed by clan pasture committees since 2007. Removed "berkutchi rangers" (eagle hunters, not rangers).

#### Stubs: Cultural & Linguistic Terms

All 25 original stubs were rewritten to give the Iradi form, an etymology in the right layer (Kipchak/Kyrgyz core, Uzbek-mediated urban words, Sogdian/Iranian and Arabic-via-Persian religious and legal words) and one or two specific facts. Nine stubs (eight here, one in the next category) were near-duplicates of parent terms and were merged:

##### At-Chabysh-Tushuk (1)
- Etymology (*at*, *chabysh*); tribal vs Hippodrome usage.
##### Kymyz-Sabaa (2)
- *saba* "leather churn", *bishkek* plunger, juniper smoking.
- **[MERGED]** absorbed "Kymyz-Kazan" (Culture, Language & Folklore 42), now described as the larger carved-wood vessel.
##### Töshök (3); Beldik (4); Jük (5); Kosh-Külö (6); Alaman-Bayge (7)
- Each given a Kipchak etymology and a use detail (dowry measure; *tör* and *jük jabuu*; late-May timing and priest's blessing; 20–40 km courses).
##### Kerege-Tash (8)
- **[MERGED]** into "Kerege (Yurt Part)" (58), which now mentions *kerege-tash* weighting stones. The original definition ("stone foundation pegs") was a gloss of a compound, not a separate article.
##### Uuk-Bogoo (9)
- **[MERGED]** into "Uuk (Yurt Part)" (59) as *uuk-boo/uuk-bogoo*.
##### Chyny-Kap (10)
- Etymology (*chyny* from the name of China, *kap* "bag").
##### Ayran-Közö (11)
- **[MERGED]** into "Airan (Culinary)" (64) as the strained summer version.
##### Süzmö (12)
- **[CANON]** beet suzma served with Iradi plov (newlore).
##### Köz-Monchok (13); Tumak (14); Ichik (15); Bel-Baa (16)
- Etymologies and cross-confessional use.
##### Kambarkan-Küü (17)
- **[MERGED]** into "Kambarkan (Music)" (72), which now covers the *küü* genre named after Kambarkan.
##### Bata-Beryü (18)
- **[MERGED]** into "Bata (Culture)" (75) as *bata beruu*, "giving the bata".
##### Tai-Kazan-Ring (19)
- Identified as an English-language name for the *tai-kazan* goal; dimensions.
##### Chylbyr (20); Noga-Baw (21); Tomoga (22)
- Noga-Baw explained as a Russian–Kipchak hybrid of the Chu lowlands (older *ayak-baw*); falconry links to Burkut Saluu.
##### Kambarkan-Kyly (23)
- **[MERGED]** into "Kambarkan (Music)" (72) as *Kambarkan kyly*, the komuz strings.
##### Kyshtoo-Kapa (24)
- **[MERGED]** into "Kyshtoo (Pastoral Term)" (37) as the winter livestock sheds.
##### Sanjyra-Bityk (25)
- **[MERGED]** into "Sanjyra (Genealogy)" (52) as *sanjyra bitik*, written genealogies.

#### Stubs: Culture, Language & Folklore

All stubs dropped the boilerplate opening "In Iradi culture and linguistics, **X (Qualifier)** refers to…" in favor of a direct definition with the bare term bolded.

##### Ak-Kalpak (26; formerly "Ak-Kala")
- **[RETITLED]** "Ak-Kala" means "white fortress"; the hat described is the *ak kalpak* ("white hat"). Four-panel construction, Kyrgyz parallel.
##### Kand (Linguistic Term) (27)
- Sogdian *kanθ*; Navekat; everyday *shaar*.
##### Shahr (Linguistic Term) (28)
- Persian via Uzbek (urban layer); Shar-i-Kuhna, Shahr-i Kabud.
##### Diz (Architecture) (29)
- Sogdian town plan. (resume) Sogdian *δīz* given and placed explicitly in the old Iranian stratum.
##### Rabat (Architecture) (30)
- *ribat*/*rabad* merger; Rabat-i-Safed, Rabat-i Kamal.
##### Pul (Architecture) (31)
- (resume) Removed transmission "through Tajik" (Tajiks are a ~1% minority and Tajikistan does not border Irad); now part of the old Iranian stratum from the medieval Sogdian- and Persian-speaking towns, contrasted with Uzbek *koʻprik*.
##### Darwaza (Architecture) (32)
- Talas citadel gate; Temir-Kapka Gate. (resume) Transmission given as Persian via Uzbek *darvoza* (urban layer).
##### Kucheh (Urban Term) (33); Dastgoh (Craft Term) (34); Navbahor (Cultural Term) (35)
- Persian via Uzbek (urban layer); Dastgoh and Navbahor tied to the Nurzhan districts of those names.
##### Zhayloo (36); Kyshtoo (37); Ashuu (38); Talaa (39); Köl (40); Zhylky (41)
- Kipchak core etymologies; Aksay Plateau; Moiynkum/Betpak-Dala winter grounds; Kenkol Pass mine (2009, addendum); Kara-Köl.
##### Kymyz-Kazan (42)
- **[MERGED]** into "Kymyz-Sabaa" (Cultural & Linguistic Terms 2).
##### Bürküt (43); Kamcha-Sabi (44); Eyer-Kash (45); Togoo (46); Shire (47); Koshkar-Muyuz (48)
- Etymologies and craft details.
##### Zhulduz (Astronomy) (49); Kuble (Culture) (50)
- **[CANON]** Polaris as *Irad*, *Zhulduz eli*, flag star; *kuble* in the Sogdian layer of church vocabulary, with the Arabic *qibla* comparison attributed.
##### Irchy (Folklore) (51)
- **[CANON]** *ır* + *-chy*; *ırda* etymology of "Irad" (baselore); 1937 purges.
##### Sanjyra (52); Aksakal (53)
- Arabic *shajara* via Persian; *jeti ata*; 24 clans with aksakal councils.
##### Adat (Customary Law) (54)
- Arabic via Persian; *kun*. (resume) Ceasefire wording changed to "acknowledged customary jurisdiction on the tribal side of the Qara-Chik line" to match the ceasefire stub and D3/A5.
##### El-Choro (Military) (55)
- *choro* in epic; 1991 patrols; El-Choro Militias since 2007.
##### Ak-Örgoe (56); Tündük (57); Kerege (58); Uuk (59)
- Yurt terms with merged sub-terms (see above).
##### Beshbarmak (60); Chyk (61); Kazy-Karta (62); Kurut (63); Airan (64); Boorsok (65)
- **[CANON]** Horsemeat taboo presented with the 1996 commercial-sale ban (addendum) rather than "strictly forbidden"; beef or mutton substitutes.
##### Kümöch (Liturgical) (66)
- Cathedral seal (twelve crosses, White Rider stallion), matching D1. (resume) Etymology note recast: the church's liturgical vocabulary draws on Sogdian and other Iranian roots (e.g., *iyık*) alongside Syriac terms, while *kümöch* is a Kipchak core word (Old Turkic *kömeč*).
##### Arsha (Flora) (67)
- *Juniperus semiglobosa*, altitude range, *alastoo* rite.
##### Albasty (Mythology) (68)
- Corrected from a "mischievous water spirit" to the Central Asian childbirth demon (Iranian *Al* + Turkic *bas-*).
##### Zhez-Tyrmak (Mythology) (69; formerly "Zhez-Tymak (Mythology)")
- **[RETITLED]** spelling fixed (*jez* "copper" + *tyrmak* "claw"); recast as the copper-clawed female demon of Kazakh/Kyrgyz-type tales.
##### Tulpar (70); Ak-Taylak (71)
- Shared Turkic winged horse; Northern Steppe camel-herding clans.
##### Kambarkan (Music) (72); Küü (Music) (73)
- Kambarkan as the legendary hunter-inventor of the komuz, with merged sub-terms; *küü* laments on 15 August.
##### Tabyp (74); Bata (75)
- Arabic-via-Persian etymologies; Christian use of *bata*.
##### Morkhan (Mythology) (76)
- **[CANON]** Bull-headed god identified with Satan; omens attach mainly to bulls and black cattle; irony of US-era beef industry noted (brief §5).

#### Untouched
None. All 117 surviving articles were edited (2 deleted, 9 merged, from 128).

#### Category headers
The category counts in the headers ("47 articles", "2 articles", "25 articles", "51 articles") were left for the integrator. Actual counts after this pass: History & Events 46, Public Institutions & Facilities 1, Cultural & Linguistic Terms 17, Culture, Language & Folklore 50.


### Chunk E4

### Changelog: chunk E4 (Vol3 stubs)

Categories: Equines, Wildlife & Crafts; Equines, Wildlife, Flora & Crafts; Historical Figures & Personalities; Institutions & Infrastructure.

All 160 surviving stubs were rewritten from one-line templated sentences into sourced encyclopedia stubs. Each now has specific facts and a `## References` list in the `<ol class="references">` format with matching `<sup>` markers, and keeps its original stub template (`{{Irad-stub}}`, `{{horse-stub}}`, `{{Irad-bio-stub}}`, `{{Irad-org-stub}}` and so on). The original numbering is kept, with gaps where articles were deleted or merged (132, 116, 124, 129).

Category headers updated:
- Equines, Wildlife, Flora & Crafts: 17 → 14 (three merges).
- Historical Figures & Personalities: 60 → 59 (Kobozev deleted).
- Institutions & Infrastructure: 50 → 49. The original header miscounted; the category always held 49 articles (191–239).

Pre-edit copy: `e4work/E4_original.md`. Working parts: `e4work/part1.md`–`part4.md`.

#### Equines, Wildlife & Crafts (Vol3 77–113)

##### Zharkyn (Horse) (Vol3 77)
- **[EXPANDED]** Expanded from 1 sentence to about 400 words, with sections History, Public image, and Breeding and criticism. Foaled 2010; bred by Keneshbek Arstanov; acquired by Toktarov in 2012; won the 2014 at chabysh; 2018 portrait; led the Irad Day parade in 2019; 112 foals by 2023. **[CANON]** Matches A1, A6 and E1.
- Recast the "heavenly horse" descent as a breed tradition that genetics cannot demonstrate. Added the personality-cult criticism and the opposition's questions about State Stud funding, attributed. Dropped "private" for the Akyel Breeding Sanctuary, because A1 (state-funded) and A6 (private) disagree; see notes.

##### Ak-Kula (Legendary Horse) (Vol3 78)
- Rewritten as Manas's horse in the shared epic, with the etymology (*ak* + *kula*) and a Hatto/Radloff citation. Removed the "soaring across canyons" puffery.

##### Almanbet (Chongtor Stallion) (Vol3 79)
- Made specific: a dark dun foaled 2003, owned by Bektur Zhumabek uulu, approved by the Chongtor Studbook Registry in 2008 after its mountain trial, more than 300 foals. Described as the foundation sire of the modern endurance line, consistent with A6.

##### Torukashka (Vol3 80)
- Recast as a racehorse of folk ballads (1880s *ash* race). Notes that no contemporary record exists and places the ballads in the wider Kazakh and Kyrgyz genre. Linked to Kalyk Asanov.

##### Chong-Talas Stud Farm (Vol3 81)
- Founded 1924 (Turkestan ASSR) for Red Army remounts; core of the Akyel revival after 1992; passed to the Syndicate in 1995. Cited Fond 218 (the equine-registers fond already used elsewhere) rather than a new fond number.

##### Ak-Tilek Ranch (Vol3 82)
- Placed in Kara-Buura District, founded 2009. Added the studbook exclusion of crossbreds, the half-bred racing classes and the purity debate.

##### Tian Shan Brown Bear (Vol3 83)
- Corrected the habitat (not "juniper forests" only): altitude band, diet, IUCN status at species level, protection status.

##### Snow Leopard (Irad) (Vol3 84)
- **[EXPANDED]** Expanded to about 400 words: distribution, ecology, threats and protection. IUCN Vulnerable; a range estimate of 60–110 attributed to a TSU review. Camera-trap figure of about a dozen in the Chatkal Snow Leopard Sanctuary, matching E3 236 (the earlier draft's "35" was removed). Cross-line ranger and warden contacts via UNMI.

##### Siberian Ibex (Irad) (Vol3 85)
- Altitude band, horn size, role as main snow leopard prey, IUCN Least Concern, hunting regime.

##### Iradi Argali (Vol3 86)
- **[CANON/fauna]** Distinguished the Karatau argali (*Ovis ammon nigrimontana*, endemic to Karatau) from the small Talas Alatau groups. IUCN Near Threatened. Replaced an irrelevant botanical citation.

##### Turkestan Lynx (Vol3 87)
- Added the scientific name *Lynx lynx isabellinus*, habitat, prey and status. Removed "willow thickets".

##### Central Asian Cobra (Vol3 88)
- **[CANON/fauna]** Recast: *Naja oxiana* is **not established in Irad**. Its range ends in southern Uzbekistan, Tajikistan and southwest Kyrgyzstan, south of the Fergana Valley. Unconfirmed reports are attributed to misidentified harmless snakes. Removed the false "Kyzylkum bluffs" claim.

##### Saker Falcon (Irad) (Vol3 89)
- Breeding habitat, falconry use, IUCN Endangered, and the trapping and electrocution threats. **[MERGED]** absorbed "Iradi Steppe Falcon" (124), which used the same species (*Falco cherrug*); "steppe falcon" is noted as a falconers' name.

##### Tian Shan Spruce (Vol3 90)
- *Picea schrenkiana* at the western edge of its range, on north slopes at 1,800–2,800 m, with Semenov's fir at Sary-Chelek. Corrected "endemic" (it is a Tian Shan species, not an Iradi endemic).

##### Wild Walnut (Juglans regia) (Vol3 91)
- **[EXPANDED]** Expanded to about 380 words: distribution and ecology, origin (relict theory vs pollen evidence, citing Beer et al. 2008), use, and conservation. Arslanbob placed on the Fergana-range slopes.

##### Semirechye Apple (Vol3 92)
- **[EXPANDED]** Expanded to about 340 words: *Malus sieversii* (IUCN Vulnerable), naming history (Sievers, Ledebour), ancestry of the domestic apple (Vavilov; Cornille et al. 2012 on the *M. sylvestris* contribution), and use and threats in Irad.

##### Mountain Juniper (Arsha) (Vol3 93)
- Named the real species (*Juniperus seravschanica*, *J. semiglobosa*, *J. turkestanica*), habitat and slow growth. Added the *alastoo* rite and church incense, linked to the incense-tradition article.

##### Iradi Mountain Trout (Vol3 94)
- **[CANON/fauna]** Corrected the native-range error: *Salmo trutta oxianus* is native to the Amu Darya, not to the Talas, Chu or Syr Darya, and was introduced to the Naryn and Toktogul. Named the native snowtrouts (*Schizothorax*, *Diptychus*). **[MERGED]** absorbed "Talas River Trout" (116), which claimed the same fish as an "endemic".

##### Karakul Sheep (Irad) (Vol3 95)
- Bukhara origin, Soviet state farms in the desert districts, the collapse of the pelt trade after 1991, and welfare criticism.

##### Chui Steppe Fox (Vol3 96)
- Identified as the corsac (*Vulpes corsac*), with range, burrows, diet and status. Removed "sagebrush".

##### Silver Inlay Horse Bit (Vol3 97)
- Inlay technique (cross-hatching), motifs and present ceremonial use.

##### Embossed Leather Kamcha (Vol3 98)
- Everyday whip construction, folk beliefs, and use in *kyz kuu*. Separated from the ceremonial 121.

##### Iradi Woolen Chapan (Vol3 99)
- Herders' wool-padded winter chapan and the guest-honoring custom.

##### Carved Bone Stirrup (Vol3 100)
- Recast: a wooden or iron frame faced with bone (not solid ibex horn), 18th–19th-century museum examples, and modern tourist pieces in cattle or camel bone.

##### Turkestan Steppe Tortoise (Vol3 101)
- **[fauna]** Scientific name corrected to *Testudo horsfieldii* (with *Agrionemys* as an alternative genus). Range, three-month activity cycle, IUCN Vulnerable, pet-trade concern.

##### Lammergeier (Bearded Vulture) (Vol3 102)
- Added *Gypaetus barbatus*, breeding sites, bone-dropping behavior stated plainly, IUCN Near Threatened and threats.

##### Wild Pistachio Shrub (Vol3 103)
- *Pistacia vera* woodland of the Fergana Rim above the lower Naryn (600–1,600 m), harvest and regeneration problems. Removed "limestone slopes".

##### Iradi Felt Saddlecloth (Vol3 104)
- *terdik* and *tokum*, construction, and women's cooperatives.

##### Chongtor Dun Bloodline (Vol3 105)
- Framed as a registry color line. The dun genetics (TBX3) are cited, and herders' belief in hardiness is attributed, with the registry's statement that color has no known effect on performance.

##### Akyel Palomino Lineage (Vol3 106)
- Palomino defined via the cream gene (MATP citation). Removed "rare genetic family"; added the 11% figure from the studbook.

##### Wild Mountain Cumin (Vol3 107)
- Identified as *Bunium persicum* (not *Cuminum*), with harvest, price and depletion. Consistent with newlore (Iradi plov).

##### Tian Shan Pika (Vol3 108)
- Named the species *Ochotona macrotis* and *O. rutila*, with haypiles and status.

##### Steppe Eagle (Irad) (Vol3 109)
- *Aquila nipalensis*, breeding on the northern plains, migration, IUCN Endangered since 2015, electrocution.

##### Carved Walnut Tobacco Box (Vol3 110)
- Made for *nasvay* and snuff from walnut burl, with motifs and tourist production.

##### Iradi Bridle Rosette (Vol3 111)
- Construction and motifs, post-1990s Orkhon-letter motifs, dowry use. **[MERGED]** absorbed "Iradi Chased Silver Bridle Plate" (129), the same object.

##### White Steppe Wormwood (Vol3 112)
- *Artemisia terrae-albae* and related species, winter forage value, overgrazing.

##### Talas River Barbel (Vol3 113)
- Identified as the Turkestan barbel (*Luciobarbus capito/conocephalus*). Decline, IUCN Vulnerable, Kazakh Red Book listing (an unverifiable "since 2008" date removed), ban on commercial fishing.

#### Equines, Wildlife, Flora & Crafts (Vol3 114–130)

##### Chongtor Roan Strain (Vol3 114)
- Roan genetics as a dominant trait. Breeders' claims are attributed, with the registry's no-effect statement.

##### Akyel Chestnut Bloodline (Vol3 115)
- Removed the "exceptional sprint speed" pseudo-claim. Chestnut genetics given, and breeders' belief attributed, with no study supporting it.

##### Talas River Trout (Vol3 116) **[MERGED]**
- Merged into "Iradi Mountain Trout" (94). It claimed an "endemic" *Salmo trutta oxianus*, which is false. The heading was removed.

##### Chatkal Golden Eagle (Vol3 117)
- Recast as a falconers' name, not a subspecies. Central Asian birds are assigned to *A. c. daphanea*. Berkutchi use; IUCN Least Concern.

##### Central Asian Badger (Vol3 118)
- *Meles leucurus*, habitat, hibernation, folk use of badger fat.

##### Tian Shan Birch (Vol3 119)
- *Betula tianschanica*, riparian thickets, use of the wood.

##### Talas Wild Tulip (Vol3 120)
- Covers Kaufmann's **and** Greig's tulips (brief anchors), with flowering times and colors. Kaufmann's native range corrected to include the Pamir-Alay. Greig's at Aksu-Zhabagly.

##### Silver Inlaid Kamcha (Vol3 121)
- The ceremonial whip as a gift of honor and at the Kurultai. Distinguished from 98.

##### Carved Walnut Saddle Tree (Vol3 122)
- Saddle-tree construction (rawhide binding), walnut vs birch, workshops.

##### Tian Shan Snowcock (Vol3 123)
- Identified as the Himalayan snowcock (*Tetraogallus himalayensis*, *ular*), with altitude, predators and status.

##### Iradi Steppe Falcon (Vol3 124) **[MERGED]**
- Merged into "Saker Falcon (Irad)" (89): same species, *Falco cherrug*. The heading was removed.

##### Mountain Wild Oregano (Vol3 125)
- Added subsp. *gracile*, altitude band, uses and markets.

##### Karakoyun Wool Fleece (Vol3 126)
- Coarse wool of the Talas Alatau, linked to the Karakoyun clan (canon clan, A2 and D3) and to Klara Zhumabek kyzy's felt cooperatives (E1).

##### Tian Shan Barberry (Vol3 127)
- Named the species *Berberis integerrima* and *B. oblonga*, with culinary and folk uses.

##### Central Asian River Otter (Vol3 128)
- **[fauna]** Recast: *Lutra lutra* (subsp. *seistanica*) has no confirmed Iradi records since the 1990s and may be extinct in Irad. IUCN Near Threatened. Removed "hunting trout".

##### Iradi Chased Silver Bridle Plate (Vol3 129) **[MERGED]**
- Merged into "Iradi Bridle Rosette" (111), the same object; the Orkhon motif was kept there. The heading was removed.

##### Wild Sea Buckthorn (Vol3 130)
- *Hippophae rhamnoides* subsp. *turkestanica* on Naryn, Chatkal and Talas gravel bars, with harvest and uses.

#### Historical Figures & Personalities (Vol3 131–190)

##### Kalyk Asanov (Vol3 131)
- Dated c. 1821–1894, with the patronymic form Kalyk Asan uulu explained. Supplied horses under Kokand and after 1876. Linked to Torukashka; the Akyel claim is attributed to oral genealogy.

##### Pyotr Kobozev (Vol3 132) **[DELETED]**
- Deleted. The E1 Start-class biography owns the topic (brief §11). Incoming links resolve to E1's article.

##### Father Toma Alimbek (Vol3 133, formerly "Father Thomas Alimbek") **[RETITLED]**
- Retitled to the regional clergy-name form (Syriac *Toma*). Made specific: fl. c. 1680–1715, hid books in Kara-Suu caves during Dzungar raids, a flyleaf note in the seminary library, books passing to the 1732 library. Alimbekov descent claim attributed.

##### Zheenbek Sadykov (Vol3 134)
- 1928–1999, TSU from 1958, *Genealogies of the Iradi Clans* (1964–67; censored chapters restored 1994), with scholarly criticism.

##### Anara Toktarova (Vol3 135)
- **[EXPANDED] [CANON]** Changed "was" to "is" Erlan's wife and listed the five sons plus Zara (no sixth son). Born 1956; married 1977; Ruslan born 1978 in Talas; family in Kobozev from 1989 (A1, A4). Children's Fund (2008) with attributed opposition criticism. Post-2023 low profile tied only to public reporting on Boz-Korgon; no hidden-lore content.

##### Sergei Voronov (Vol3 136)
- **[EXPANDED]** Dated 1907–1978. The July 1949 discovery at about 2,400 m matches A5 and E3; Order of Lenin, chief engineer, polytechnic teaching. "Nurzhan oil field in 1949" corrected to "near Kobozev".

##### Muratbek Biy (Vol3 137)
- **[EXPANDED]** Karakoyun chief c. 1690–1758. Dzungar occupation (1723), Anrakay as bardic claim, the 1727 Kokand decree. Historicity hedged. Added a hatnote pairing with E1's "Muratbek Tanıp-Biy".

##### Major William Evans (Vol3 138)
- Born 1958; 1996–97 rebuilding of 23 bridges in the Talas and Kara-Buura valleys under DoD funding.

##### Almazbek Mamyt uulu (Vol3 139)
- SSR ulak champion 1983–87 (the anachronistic "national" corrected), later coaching and the Kurultai tournament. Brother of Keneshbek Mamyt uulu (189).

##### Venera Kasymova (Vol3 140)
- Prima ballerina 1971–1990, Leningrad training, repertoire, People's Artist 1984, ballet school.

##### Bakhytzhan Kim (Vol3 141)
- 1912–1989; deported 1937; rice from 1938 (matches A5 and newlore plov rice).

##### Father Barnabas (Vol3 142)
- **[EXPANDED] [CANON]** Recast. The original said he "delivered official papal recognition" openly in 1932, which contradicts the secret 1931 negotiation through nuncios abroad. He is now a Polish Franciscan who, by his own memoir and church tradition, secretly carried the bull and documents in 1932. Soviet corroboration is partial; the account is hedged.

##### Talgatbek Moldoshev (Vol3 143)
- 1922–1994; Supreme Soviet deputy for Kara-Buura 1963–85; agricultural commission; rural electrification.

##### Aigul Daniyarova (Vol3 144)
- "Was" changed to "is". Steppe Investigative Network reporter on Chatkal tailings, Sary-Bulak dust and Mailuu-Suu; accreditation withdrawn 2020 and restored 2022.

##### Keneshbek Choro uulu (Vol3 145)
- 1938–2015; berkutchi; national festival revived 1995; training methods recorded.

##### Dr. Pavel Morozov (Vol3 146)
- Recast "eradicated malaria" as directing the 1946–1950s campaign, with elimination declared in 1960. Methods and attributed figures.

##### Zarina Alimbekova (Vol3 147)
- **[EXPANDED]** 1891–1959; Talas Girls' Boarding School (1924); Latin-script schooling; dismissal in 1938 after the purge of her relative Mar Timotheos.

##### Erkinbek Asan uulu (Vol3 148, formerly "Erkinbek Asanov") **[RETITLED]**
- Retitled to the tribal patronymic (living into the 2000s; the Soviet form is noted). The vague "1990s civil unrest" was replaced with specifics: 1994 decollectivization hearings, Aksay pasture disputes, 2007 prisoner releases, adviser to Bektur.

##### Captain Robert Hayes (Vol3 149)
- 2002 airlift planning under the 2001 Basing Rights Agreement.

##### Burulcha Sydyk kyzy (Vol3 150)
- 1909–1977; Chatkal singer; Radio Moscow recordings of 1955 and 1961, copies now at TSU.

##### Tynchtykbek Niyazov (Vol3 151)
- 1958–2019; mounted volunteer company in the 1992 siege; National Guard 1994–2007. Son of Tolonbek Niyazov (185).

##### Marqos the Scribe (Vol3 152)
- **[EXPANDED]** Colophon dated 1576 AG (AD 1264/65), Kerait patron (consistent with A5 gravestones), manuscript description, rejection of the identification with Rabban Markos (Yahballaha III), 1937 concealment.

##### Bolotbek Bekzhanov (Vol3 153)
- **[CANON]** "1962 Nurzhan master plan" corrected to Kobozev (now Nurzhan). Chief architect 1958–76; Palace of Metallurgists. Son of Altynai Bekzhanova (E1).

##### Lyudmila Ivanova (Vol3 154)
- 1934–2011; novel *The Steppe on Fire* (1971); censorship and Iradi critique attributed.

##### Kanybek Arstanov (Vol3 155)
- Made the son of Keneshbek Arstanov (E1) and trainer of Zharkyn for the 2014 win. Explains why his horses race abroad under foreign ownership (no recognized federation).

##### Saparbek Temirov (Vol3 156)
- Territorial House member 1994–2002; content of the 1998 Foreign Investment Guarantee Act, its link to the 1998 Agribusiness Accord, criticism.

##### Sister Maryam Janyl (Vol3 157, formerly "Sister Maria Janyl") **[RETITLED]**
- Retitled to the regional name form. 1940–2017; hospice opened 1996; congregation recognized 1999; about 40 sisters; runs St. Maryam Catholic Academy.

##### Timur Karimov (Vol3 158)
- 1944–2010; younger brother of Beknur Karimov; later career; advised the 2011 restoration.

##### Amina Yunusova (Vol3 159)
- Born 1955; studio founded 1995; export markets; production by the ATR cooperatives.

##### Orozbek Doolotov (Vol3 160)
- 1919–1998; anti-tank platoon, Kursk northern face, July 1943. Son of Nurgazy Doolotov (183).

##### David Chen (Vol3 161)
- Neutral (real company): negotiated the 2018 and 2021 Lihua acquisitions, consistent with D5. No negative claims added.

##### Gulmira Saparova (Vol3 162)
- Talas District Court since 2006; 2011 and 2016 environmental judgments.

##### Kadyrbek Asylbekov (Vol3 163)
- 1938–2008; shot *Zarina* and *Desert Sun's Rebellion* for Nurlan Sadikov (addendum cinema canon); 2004 restoration.

##### Father Yuhanna of Merv (Vol3 164)
- **[EXPANDED]** Presented as a figure of tradition (18th-century chronicle), with historical background (Merv metropolitanate, Timothy I). The link to the 1908 Church of St. Yuhanna (D4) is described only as popular tradition.

##### Rustam Bekzatov (Vol3 165)
- "Was" changed to "is". Tanker fleet role matches A4 and E1; siblings named.

##### Chynara Mamytova (Vol3 166)
- Replaced the incoherent "Sogdian terracotta glaze" with the revival of Samanid and Kara-Khanid slip-painted earthenware.

##### Lieutenant Gregory Vance (Vol3 167)
- **[CANON]** Runway extension dated 1993–1998, from 2,500 to 3,400 m, matching E3 217.

##### Asanbek Daniyarov (Vol3 168)
- 1902–1979 (Soviet-era, so the -ov form is kept, with the patronymic noted). Steppe-clan genealogies dictated to TSU researchers.

##### Tatiana Petrova (Vol3 169)
- 1931–2016; School No. 3 in Kobozev, 1955–98; Honored Teacher 1977.

##### Zhypargul Kulova (Vol3 170)
- Equine virology lab 1979–2010; vaccine and 1997-outbreak claims attributed to the center; DNA testing introduced 1998 (matches D4).

##### Mikhail Chernov (Vol3 171)
- Directed Chatkal metallurgy 1981–91 (matches D4); Svetlana Kozlova as deputy; left in 1992.

##### Almazbek Kasymov (Vol3 172)
- 1936–2014; doors of the Hall of Justice and the National Historical Museum; St. Yuhanna sanctuary screen.

##### Sister Klara Alimbekova (Vol3 173, formerly "Sister Clara Alimbek") **[RETITLED]**
- Retitled to the urban -ova convention and the regional name form. Specific 1992 siege dressing stations; later work with the St. Luka mission.

##### Kubanbek Moldosh uulu (Vol3 174)
- Mobile Iradi-language library founded 2012, five vans by 2023.

##### Captain Alexey Smirnov (Vol3 175)
- **[EXPANDED] [CANON]** Recast from "border guard" to internal-troops checkpoint commander. His report is the Fond 85 internal-security report that calls the shooting accidental and leaves the widow unnamed, consistent with E3 194 and brief §5. Historians' debate attributed.

##### Aida Temirova (Vol3 176)
- Conservatory professor since 1984, head of piano 1999–2021, küü arrangements.

##### Keneshbek Zhumaliev (Vol3 177)
- 1929–2011 (patronymic form noted); Chatkal tabyp; cooperation with St. Luka doctors.

##### Elena Kim (Vol3 178)
- Concertmaster 1985–2008 and the 1994 US tour, both matching E1 68.

##### Maratbek Sadykov (Vol3 179)
- **[EXPANDED]** *Iradyn Chyny* editor 1986–91: glasnost coverage (1956, 1937, Mailuu-Suu, 1989 bread riots), dismissal in October 1991 after the SRI declaration.

##### Fatima Asanova (Vol3 180)
- Kolkhoz chair who sheltered Koryo-saram deportees in the 1937–38 winter; street named in Navbahor District in 2007.

##### Colonel Richard Taylor (Vol3 181)
- DoD lead in the October–November 2001 basing talks in Talas.

##### Batyrbek Arstanov (Vol3 182)
- 1921–2001; WWII cavalryman; led the veterans' column at the 1995 Irad Day parade. Father of Keneshbek Arstanov.

##### Nurgazy Doolotov (Vol3 183)
- 1899–1958; 1934 Kobozev shortwave station (matches A5); father of Orozbek.

##### Svetlana Kozlova (Vol3 184)
- **[CANON]** "Chief metallurgist" corrected to chemist (D4). Bismuth recovery; mother of Artem Kozlov (E1).

##### Tolonbek Niyazov (Vol3 185)
- 1921–1996; 14 pieces in the national museum; teacher of Tolonbek Sydykov (E1); father of Tynchtykbek.

##### Father Stephanos (Vol3 186)
- **[CANON]** Recast from a foreign "Syrian Catholic priest" to a Syro-Iradi priest ordained secretly in 1949, who celebrated the 14 September 1992 reconsecration (canon date).

##### Aigul Omurova (Vol3 187)
- *Temir Kazyk* (2004); Polaris imagery linked to the Star of Irad. Daughter of Baktygul Omurova (E1).

##### Vasily Morozov (Vol3 188)
- 1904–1971; context for 1930s Central Asian diesel traction; 1938 date matches A5.

##### Keneshbek Mamyt uulu (Vol3 189)
- August 2004 Manas Peak rescue, specific. Brother of Almazbek (139).

##### Asel Bekzatova (Vol3 190)
- "Was" changed to "is". Born 1983; foundation founded 2010 (A4, A5); activities.

#### Institutions & Infrastructure (Vol3 191–239)

##### Talas State University (Vol3 191)
- **[EXPANDED]** Founded 1958 (matches A-chunks), about 18,400 students; history (Soviet faculties, 1992 damage, territorial-era English, post-2007 appointed rector, 2023 protests), research units cited across the wiki, the *Bulletin*.

##### Cathedral Seminary of Iyık Janyl (Vol3 192)
- **[EXPANDED] [CANON]** Official name St. Ephrem Major Seminary (A5, D4); closed 1937, **reopened 1994**; six-year program, 46 students, rector as Synod adviser.

##### Talas Municipal Hospital No. 1 (Vol3 193)
- Main city emergency hospital (consistent with D5): opened 1964, about 480 beds, 2004 rebuild.

##### Nurzhan Children’s Polyclinic (Vol3 194)
- Opened 1961; about 60,000 registered children; city and NurGaz funding.

##### Qara-Chik Border Checkpoint (Vol3 195)
- **[EXPANDED] [CANON]** Built 2008–09 by the Gendarmerie's Border Demarcation Brigade under deputy commander Ruslan Toktarov (A4, D3); El-Choro post opposite; permits; about 1,900 crossings a day; UNMI HQ at Kara-Oi nearby; HRW criticism. Notes that the line is not an international border.

##### Chatkal Mountain Rescue Base (Vol3 196)
- Founded 1972 as a mine-rescue unit; joint operation since 1996; mining-chamber teams train there (D4).

##### Talas Central Post Office (Vol3 197)
- 1954 neoclassical building; non-UPU status, mail exchanged via Kazakhstan; the Zharkyn stamp.

##### IradOne Transmitter Mast (Vol3 198)
- On Television Hill (A6); built 1972; DTT from 2015.

##### Chatkal Primary Health Post (Vol3 199)
- Staffing, services, worker screening, funding.

##### State Archives of Irad (Vol3 200)
- **[EXPANDED] [CANON]** History (1927 Kobozev, moved to Talas 1993, new building 1997); holdings list with **Fond 108 = Revolution of 1992 and Provisional Government records** and **Fond 131 = military records** (addendum), plus Fonds 85, 77 and 218; access rules and post-2007 closures.

##### National Historical Museum of Irad (Vol3 201)
- **[EXPANDED] [CANON]** Founded 1934, national since 1993. The Botai exhibit is presented as a national claim, with the 2021 genetic findings and the criticism (brief §5). Other galleries; the 2007 exhibit criticized by tribal leaders.

##### Iyık Janyl Pilgrimage Hostel (Vol3 202)
- "Cathedral of Saint Janyl" corrected to "Church of Saint Janyl". Opened 1999 in a caravanserai; 180 beds; Feast on 24 August.

##### Talas Fire Station No. 2 (Vol3 203)
- Western districts and the export zone (ammonia hazards); a station of the Municipal Fire Brigade (233).

##### Chu Basin Hydrological Station (Vol3 204)
- At Nurzhan (D2); 1932; data sharing; the falling summer flow record.

##### Nurzhan Municipal Library (Vol3 205)
- Azatlık Prospect; 300,000+ volumes (A5); manuscript claim moderated.

##### Talas Veterinary Research Center (Vol3 206)
- Founded 1962; DNA testing with TSU (D4); Zhypargul Kulova's lab.

##### Aksay Border Patrol Post (Vol3 207)
- **[CANON]** Recast: the Aksay Plateau is ATR interior, not an international frontier. The post is now the Gendarmerie's highest Qara-Chik checkpoint, on the herd-migration corridor, open on JLC-set dates.

##### St. Maryam Catholic Academy (Vol3 208)
- Opened 2001; 520 pupils; run by the Sisters of the Cross (linked to the retitled founder).

##### NurGaz Worker Housing Complex (Vol3 209)
- 2004; 2,800 apartments; Bekzatov political base (attributed; A4, A5).

##### Talas Chamber of Commerce (Vol3 210)
- Distinguished as the city chamber within the national Chamber of Commerce and Industry; 1995; activities.

##### Kara-Suu Rural Health Center (Vol3 211)
- Upper Kara-Suu (tribal side, per the addendum placements); built 2014; St. Luka visits.

##### Iradi Telegraph Office (Vol3 212)
- 1879 station on the Tashkent–Verny line; Soviet exchange; Attelkom node since 1999.

##### Talas Municipal Gymnasium No. 4 (Vol3 213)
- 1936 school, English specialization 1993, riding program. "Prestigious" removed.

##### Nurzhan Botanical Gardens (Vol3 214)
- 1957, 58 ha, collections, link to the Botanical Institute (E3).

##### Sukarne Quality Control Labs (Vol3 215)
- Neutral (real company): part of the Sukarne Irad Complex in the TAEZ (D5); 1999.

##### Kenkol Mountain Meteorological Post (Vol3 216)
- Near the Kenkol Pass on the ISEZ side of the western sector (D3); 1936; automated 2011.

##### Talas District Court (Vol3 217)
- Created by the 2003 Judicial Reforms Act (A3, A5); appeals; Saparova; HRW criticism.

##### Iyık Janyl Monastic Cloister (Vol3 218)
- Distinguished from the Order of St. Janyl the Hermit motherhouse (A5, D4); reopened 1993; 14 monks.

##### Nurzhan Emergency Dispatch Center (Vol3 219)
- Merged in 2010; new system 2016; NurGaz coordination.

##### Talas Customs Clearance Terminal (Vol3 220)
- **[CANON]** In the Talas Free Economic Trade Zone. Goods from China arrive in transit through Kazakhstan (no China border). The 2015 scanners under Talgat Saparov (E1).

##### Chatkal Wildlife Protection Post (Vol3 221)
- ISEZ ranger post facing the Chatkal; cooperation with the sanctuary wardens (E3 236) via UNMI.

##### St. Luka Clinic (Vol3 222)
- **[EXPANDED]** Run by the St. Luka Community Health Mission (D5); opened 1997; services; serves ATR people without registration; 14,000 visits in 2023; funding.

##### Irad Central Sports Complex (Vol3 223)
- 1979 sports palace; 6,500 seats; 2009 renovation.

##### Kara-Bulak Agricultural Cooperative (Vol3 224)
- 1996 cooperative of 140 households in Kara-Bulak; uses the Kara-Bulak elevators.

##### Talas Municipal Bus Depot (Vol3 225)
- 1968; 260 buses; CNG buses from 2017; marshrutkas noted.

##### NurGaz Pipeline Maintenance Depot (Vol3 226)
- **[CANON]** In Dastgoh District (A5); maintains the 85-km Northern Export Feeder into KazTransOil near Shymkent (D4); SCADA.

##### Kök-Jar Primary School (Vol3 227, formerly "Kök-Jar Primary School (2)") **[RETITLED]**
- Removed the "(2)" suffix. No other Kök-Jar school article exists, so this was not a duplicate. Placed in the ATR's Chatkal Highlands (consistent with E3 236). Iradi-only teaching since 2008, replacing the territorial-era English, consistent with newlore on tribal language rejection.

##### Talas Public Sanitation Works (Vol3 228)
- Tonnage, 1981 landfill near capacity, delayed new site.

##### Aksay Emergency Shelter (Vol3 229)
- Tribal side; 1983 state-farm hut restored in 2012; Kurultai use.

##### Bank of Irad Clearing House (Vol3 230)
- **[EXPANDED] [CANON]** Operated by the Bank of Irad (chair Azamat Temirov, E1); dollar and som settlement; set up 1996, RTGS 2009 and 2012. Explicitly separated from Talasbank's commercial role (about 60% of deposits), from foreign correspondent settlement (Almaty and Istanbul) and from the export escrow accounts audited by the Foreign Trade Escrow Authority (A2, D4, D5).

##### Nurzhan Technical Lyceum (Vol3 231)
- 1952 trade school; 900 students; apprenticeships.

##### Iyık Janyl Diocesan Archives Vault (Vol3 232)
- Holdings match A5; vault built 2006; distinct from the manuscript library.

##### Talas Municipal Fire Brigade (Vol3 233)
- Seven stations, 420 firefighters; distinguished from Station No. 2.

##### Attelkom Cellular Relay Tower (Vol3 234)
- Solar-and-wind ridge towers (A6), with coverage spilling across the line.

##### Kara-Suu Tribal Elders Council Hall (Vol3 235)
- Upper Kara-Suu (tribal side); built 2010; yurt-plan design; adat hearings.

##### Talas Blood Services Center (Vol3 236)
- 1958 station; supplies the Regional Hospital (D5); 21,000 donations.

##### Nurzhan Rail Freight Depot (Vol3 237)
- **[CANON]** Crude went by rail to Shymkent until the 2000 feeder (addendum).

##### St. Teresa Community Kitchen (Vol3 238)
- Kept the title (linked from A5). Explained as a Latin-rite parish (Polish and German deportee descendants), which justifies the non-Syriac saint's name; see notes.

##### Besh-Tash Ranger Headquarters (Vol3 239)
- At the park entrance on the ISEZ side, 20 km south of Talas (D2); the park was established in 1996; the upper valley lies on the tribal side.

#### Untouched
None. Every article in the chunk was edited, merged or deleted.


### Chunk E5

### Changelog: chunk E5 (Vol3 stubs: Minor Settlements & Communes; Physical Geography)

All 200 stubs were reviewed. 146 survive, every one rewritten from a one-line templated sentence into a sourced encyclopedia stub: location (ISEZ district or ATR planning zone), a 2018 census figure (ISEZ) or estimate (ATR) for settlements, or type, setting, dimensions, hydrology or geology and use for landforms, plus one or two concrete facts and a `## References` list in the `<ol class="references">` format with matching `<sup>` markers. The original stub templates (`{{Irad-geo-stub}}`, `{{settlement-stub}}`, `{{mountain-stub}}` and so on) are kept. Following E4, no assessment line was added to these stubs. Original numbering is kept, with gaps where articles were merged or deleted.

- **Renamed:** 107 articles (table below).
- **Merged into another E5 article:** 38.
- **Deleted as duplicates of E2 articles:** 16.
- **Kept title, rewritten:** 39.

Category headers updated:
- Minor Settlements & Communes: 99 → 82.
- Physical Geography: 101 → 64.

Pre-edit copy: `e5work/E5_original.md`. Build scripts and article data: `e5work/` (`part1.py`–`part5.py`, `refs.py`, `build.py`).

The new stubs spread across the footprint: ISEZ Talas, Kara-Buura, Chu, Sary-Bulak and Lower Naryn districts, and all six ATR planning zones (Northern Steppe/Moiynkum and Betpak-Dala, Karatau, Talas Alatau, Chatkal Highlands, Toktogul–Naryn, Fergana Rim). The 34 ISEZ village census figures add up to about 46,500, which together with E2's settlement figures stays within the roughly 125,000 people that canon leaves for the five ISEZ districts outside the three cities.

#### Rename table (for the integrator)

Old title → new title. "Links in" lists chunks that contain a `[[wikilink]]` to the old title; "Plain mentions" lists chunks that mention the old name in running text (checked against all chunks and `pass2/new/`). No renamed title has an incoming wikilink; titles that are linked from other chunks (Karakol-Ashuu, Manas Glacier, Besh-Tash Upper Lake, Besh-Tash Lower Tarn) were deliberately kept.

| Vol3 # | Old title | New title | Links in | Plain mentions |
|---|---|---|---|---|
| 240 | Ak-Terek-Ayyl | Chong-Kapka | — | — |
| 246 | Cholpon-Ayyl | Jon-Aryk | — | — |
| 252 | Kenkol-Ayyl | Ming-Örük | — | — |
| 253 | Arslan-Korgon | Eski-Korgon | — | — |
| 254 | Chatkal-Ayyl | Kanysh-Kiya | — | — |
| 255 | Manas-Ayyl | Kyrk-Choro | — | — |
| 256 | Kulan-Ayyl | Tuzduu | — | — |
| 257 | Buzurg-Kand | Shaar-Döbö | — | — |
| 258 | Jety-Ayyl | Kosh-Döbö | — | — |
| 259 | Urmaral-Ayyl | Tegirmen | — | — |
| 260 | Tuyuk-Ayyl | Kara-Jylga | — | — |
| 261 | Nau-Kand | Sarymsakty | — | — |
| 262 | Shelji-Ayyl | Kümüshtü | — | — |
| 263 | Susamyr-Ayyl | Ak-Kyya | — | — |
| 264 | Kum-Bel-Ayyl | Tört-Kuduk | — | — |
| 265 | Kara-Buura-Kishlak | Kum-Aryk | — | — |
| 266 | Malik-Rabat | Hauzdy | — | — |
| 267 | Besh-Tash-Ayyl | Kök-Oi | — | — |
| 268 | Kyzyl-Adyr-Ayyl | Bakyyan | — | — |
| 270 | Moinok-Ayyl | Tar-Say | — | — |
| 271 | Alatau-Kishlak | Teke-Tash | — | — |
| 272 | Uzun-Akmat-Ayyl | Ozgörüsh | — | — |
| 273 | Kohna-Kand | Sopol-Tepa | — | — |
| 274 | Susamyr-Beket | Otmek | — | — |
| 275 | Zard-Diz | Sary-Döbö | — | — |
| 276 | Karakyr-Ayyl | Sasyk-Bulak | — | — |
| 277 | Art-Ayyl | Bel-Aldy | — | — |
| 278 | Dastgoh-Ayyl | Temirchi | — | — |
| 279 | Terek-Ayyl | Chet-Bulak | — | — |
| 280 | Darya-Ayyl | Kaiyrma | — | — |
| 281 | Sangin-Rabat | Tash-Kuduk | — | — |
| 282 | Bel-Ayyl | Toguz-Bulak | — | — |
| 284 | Suu-Ayyl | Jyluu-Bulak | — | — |
| 285 | Tektir-Ayyl | Boz-Adyr | — | — |
| 286 | Navbahor-Ayyl | Jangy-Jol | — | — |
| 287 | Jar-Ayyl | Teskey-Jar | — | — |
| 289 | Kalan-Bazar-Ayyl | Köpürö-Bazar | — | — |
| 290 | Bulak-Ayyl | Kyrk-Bulak | — | — |
| 292 | Talaa-Ayyl | Ak-Jal | — | — |
| 293 | Unkur-Ayyl | Bitik-Tash | — | — |
| 294 | Nav-Kand | Bulak-Bashy | — | — |
| 295 | Köl-Ayyl | Jashyl-Köl | — | — |
| 296 | Sai-Ayyl | Shagyldy | — | — |
| 297 | Kenkol-Kishlak | Archaly | — | — |
| 298 | Darwaza-Ayyl | Kapka-Tash | — | — |
| 300 | Kara-Suu-Beket | Kalba | — | — |
| 302 | Sary-Kamysh | Kamyshtuu | — | — |
| 303 | Kyzyl-Tuu | Uuk-Bulak | — | — |
| 310 | Besh-Tash-Kishlak | Kara-Say | — | — |
| 311 | Kara-Döbö-Ayyl | Örüktü | — | — |
| 313 | Kök-Sai-Ayyl | Kök-Say | — | — |
| 314 | Taldy-Bulak-Kishlak | Aral | — | — |
| 315 | Kashka-Suu-Ayyl | Kosh-Bel | — | — |
| 316 | Cholpon-Kishlak | Uch-Emchek | — | — |
| 318 | Kyzyl-Tash-Ayyl | Kyzyl-Döbö | — | — |
| 320 | Karakol-Tash | Muz-Tör | — | — |
| 321 | Ak-Jar-Ayyl | Ak-Jar | — | — |
| 322 | Kenkol-Bulak | Jele-Döbö | — | — |
| 323 | Arslan-Bulak | Jangak-Bulak | — | — |
| 325 | Manas-Korgon | Korgoncho | — | — |
| 326 | Kulan-Bulak | Töö-Kuduk | — | — |
| 328 | Jety-Bulak | Dary-Bulak | — | — |
| 329 | Urmaral-Kishlak | Almaluu | — | — |
| 331 | Nau-Bulak | Tunuk-Bulak | — | — |
| 340 | Sary-Bulak Creek | Chakmak-Say | — | — |
| 341 | Kara-Bulak Spring | Kumdy-Bulak | — | — |
| 342 | Ak-Tash Ravine | Bürküt-Uya | — | — |
| 344 | Besh-Terek Well | Kalmak-Kuduk | — | — |
| 345 | Taldy-Suu Gorge | Ichke-Suu Gorge | — | — |
| 346 | Kashka-Darya Tributary | Boz-Suu | — | — |
| 347 | Cholpon Tarn | Tegerek-Köl | — | — |
| 348 | Bazar-Sai Wash | Tuura-Say | — | — |
| 350 | Orto-Sai Rapids | Uch-Terek Rapids | — | — |
| 353 | Kenkol Ridge | Uzun-Kyr | — | — |
| 357 | Kulan Dry Lake | Kulan-Sor | — | — |
| 358 | Buzurg Canal | Eski-Aryk | — | — |
| 361 | Tuyuk Cirque | Kara-Kazan Cirque | — | — |
| 362 | Nau Spring | Maryam-Bulak | — | — |
| 365 | Kum-Bel Creek | Altyn-Say | — | — |
| 366 | Kara-Buura Wash | Kuru-Say | — | — |
| 370 | Sabz Creek | Kashkar-Aryk | — | — |
| 372 | Alatau Snowfield | Ak-Muz | — | — |
| 374 | Kohna Bluff | Karool-Döbö | — | — |
| 375 | Susamyr Sinks | Teshik-Talaa | — | — |
| 378 | Art Ridge | Kylych-Kyr | — | — |
| 381 | Darya Marshes | Akzhaykyn Depression | — | — |
| 383 | Bel Saddle | Kichi-Bel | — | — |
| 386 | Tektir Terrace | Ambar-Döbö | — | — |
| 388 | Jar Gorge | Kök-Kamar Gorge | — | — |
| 390 | Kalan Springs | Sarchashma Springs | — | — |
| 391 | Bulak Creek | Ak-Balyk Creek | — | — |
| 392 | Safid Ridge | Ak-Kyr | — | — |
| 393 | Talaa Depressions | Kaz-Köl | — | — |
| 395 | Nav Canal | Jangy-Aryk | — | — |
| 399 | Darwaza Pass | Kapka-Bel | — | — |
| 404 | Kyzyl-Tuu Bluffs | Chopo-Jar | — | — |
| 406 | Altyn Springs | Isyk-Bulak | — | — |
| 407 | Zhalgyz Peak | Mazar-Too | — | — |
| 409 | Ak-Tash Peak | Ak-Bash | — | — |
| 411 | Kara-Bulak Torrent | Muz-Suu | — | — |
| 413 | Kök-Sai Saddle | Koi-Bel | — | — |
| 416 | Cholpon Ridge | Sary-Kyr | — | — |
| 418 | Kyzyl-Tash Bluffs | Sadaf-Jar | — | — |
| 429 | Urmaral Gorges | Tar-Kapchygai | — | — |
| 431 | Nau Karst Caverns | Kyrk-Kazyk Caves | — | — |
| 432 | Shelji Alluvial Fan | Kum-Say Fan | — | — |
| 439 | Ak-Kungey Mineral Tarn | Achuu-Köl | — | — |

Result of the check: no other chunk links to or mentions any renamed or removed E5 title, so no wikilinks elsewhere need changing. The integrator should still update `article_index.txt` and any title lists from this table.

#### Merges and deletions

| Vol3 # | Removed title | Folded into | Links in | Plain mentions |
|---|---|---|---|---|
| 283 | Khunuk-Kand | Shahr-i Khunuk (E2) | — | — |
| 288 | Karakoyun-Ayyl | Kara-Koyun Valley (E2) | — | — |
| 291 | Safid-Diz | Diz-i Safid (E2) | — | — |
| 309 | Ak-Bulak-Ayyl | Kyrk-Bulak (Vol3 290) | — | — |
| 312 | Sary-Bulak-Ayyl | Sary-Bulak (Vol3 243) | — | — |
| 317 | Bazar-Bulak-Ayyl | Bazar-Terek (Vol3 247) | — | — |
| 319 | Orto-Köl-Ayyl | Jashyl-Köl (Vol3 295) | — | — |
| 324 | Chatkal-Beket | Bel-Aldy (Vol3 277) | — | — |
| 327 | Buzurg-Rabat | Shaar-Döbö (Vol3 257) | — | — |
| 330 | Tuyuk-Beket | Otmek (Vol3 274) | — | — |
| 332 | Shelji-Kishlak | Kümüshtü (Vol3 262) | — | — |
| 333 | Susamyr-Kishlak | Ak-Kyya (Vol3 263) | — | — |
| 334 | Kum-Bel-Beket | Kum-Bel (E2) | — | — |
| 335 | Kara-Buura-Ayyl | Kum-Aryk (Vol3 265) | — | — |
| 336 | Malik-Ayyl | Hauzdy (Vol3 266) | — | — |
| 337 | Besh-Tash-Beket | Kök-Oi (Vol3 267) | — | — |
| 338 | Kyzyl-Adyr-Kishlak | Bakyyan (Vol3 268) | — | — |
| 349 | Kyzyl-Jar Bluffs | Kyzyl-Jar (E2) | — | — |
| 359 | Jety-Kaiyng Rocks | Jety-Kaiyng (E2) | — | — |
| 363 | Shelji Mound | Shelji (E2) | — | — |
| 364 | Susamyr Meadow | Suusamyr (E2) | — | — |
| 367 | Malik Well | Hauzdy (Vol3 266) | — | — |
| 371 | Moinok Towers | Kök-Moinok (E2) | — | — |
| 376 | Zard Hill | Diz-i Zard (E2) | — | — |
| 377 | Karakyr Cliffs | Karakyr Range (E2) | — | — |
| 380 | Terek Spring | Zhalgyz-Terek (Vol3 306) | — | — |
| 382 | Sangin Well | Tash-Kuduk (Vol3 281) | — | — |
| 385 | Suu Thermal Springs | Jyluu-Bulak (Vol3 284) | — | — |
| 394 | Unkur Ravine | Bitik-Tash (Vol3 293) | — | — |
| 397 | Sai Creek | Tuura-Say (Vol3 348) | — | — |
| 398 | Kenkol Rapids | Chong-Kenkol (E2) | — | — |
| 400 | Chiy Flats | Ak-Chiy (Vol3 299) | — | — |
| 402 | Kök-Döbö Hill | Kök-Döbö (Vol3 301) | — | — |
| 403 | Kamysh Marshes | Akzhaykyn Depression (Vol3 381) | — | — |
| 408 | Tash-Köröö Gorge | Tash-Köröö (Vol3 307) | — | — |
| 410 | Besh-Terek Ravine | Ichke-Suu Gorge (Vol3 345) | — | — |
| 414 | Taldy-Suu Tarn | Tegerek-Köl (Vol3 347) | — | — |
| 417 | Bazar-Sai Wash (2) | Tuura-Say (Vol3 348) | — | — |
| 419 | Orto-Köl Cirque | Kara-Kazan Cirque (Vol3 361) | — | — |
| 420 | Karakol Mountain Pass | Karakol-Ashuu (Vol3 250) | — | — |
| 421 | Ak-Jar Escarpment | Ak-Jar (Vol3 321) | — | — |
| 422 | Kenkol Gorges | Chong-Kenkol (E2) | — | — |
| 423 | Arslanbob Basin | Arslanbob (E2) | — | — |
| 424 | Chatkal Rapids | Chatkal Gorge (Vol3 355) | — | — |
| 425 | Manas Northern Face | Manas Glacier (Vol3 356) | — | — |
| 426 | Kulan Salt Pan | Kulan-Sor (Vol3 357) | — | — |
| 427 | Buzurg Canal Outlet | Eski-Aryk (Vol3 358) | — | — |
| 428 | Jety-Bulak Springs | Dary-Bulak (Vol3 328) | — | — |
| 430 | Tuyuk-Suu Snowfields | Ak-Muz (Vol3 372) | — | — |
| 433 | Susamyr High Steppe | Suusamyr (E2) | — | — |
| 434 | Kum-Bel Ridge | Kum-Bel (E2) | — | — |
| 435 | Kara-Buura Wash (2) | Kuru-Say (Vol3 366) | — | — |
| 436 | Malik Springs | Kumdy-Bulak (Vol3 341) | — | — |
| 438 | Kyzyl-Adyr Loess Hills | Kyzyl-Adyr Hills (Vol3 369) | — | — |

If the integrator finds a link to a removed title, point it to the "Folded into" target (for E2 targets, the E2 article title without "(E2)").

#### Minor Settlements & Communes (Vol3 240–338)

##### Chong-Kapka (Vol3 240; formerly "Ak-Terek-Ayyl")
- **[RETITLED]** Renamed (the old name repeated E2's Ak-Terek with a mechanical suffix). Placed in the upper Kara-Suu valley (Tanıp territory, ATR) as the original intended; added the gorge etymology, survey population, Chongtor breeding and the link to the Kara-Suu clinic.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Besh-Moinok (Vol3 241)
- Placed in Chu District at the Moiynkum edge; added etymology, census population, canal and shelterbelt details.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kara-Jygach (Vol3 242)
- Moved from the vague 'Chatkal foothills' to the Fergana Rim zone; removed 'celebrated'; added the plot-allotment system and market link.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Sary-Bulak (Vol3 243)
- [CANON] Reframed from a 'highland transhumance station' into the mining village of the Sary-Bulak works (brief §2), keeping the transhumance origin as history. [MERGED] Absorbed Sary-Bulak-Ayyl (Vol3 312). Added census population, 1961 foundation and environmental monitoring.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Taldy-Suu (Vol3 244)
- Placed in Kara-Buura District; replaced 'quiet riverside hamlet' with census population, willow use and the honey cooperative.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kashka-Jol (Vol3 245)
- Located on the Kara-Buura Pass route (consistent with E2 Kara-Buura and Rabat-i Sangin); added etymology and the pack-horse trade.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Jon-Aryk (Vol3 246; formerly "Cholpon-Ayyl")
- **[RETITLED]** Renamed (Cholpon- repeated E2 Cholpon-Bulak). Kept the Chu fodder-and-barley economy; added the 1937 Koryo-saram foundation and rice (consistent with D3 Koryo-saram in Irad).
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Bazar-Terek (Vol3 247)
- Placed in the Karatau zone; added market day, buyers and the felt cooperative. [MERGED] Absorbed Bazar-Bulak-Ayyl (Vol3 317), a near-identical 'crossroads wool market' stub.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kyzyl-Bel (Vol3 248)
- Removed 'nestled'; corrected 'red limestone' to red sandstone; tied the hamlet to the Kyzyl-Bel Pass stub; added population.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Orto-Ayyl (Vol3 249)
- Placed on the tribal side of the upper Talas valley; replaced the vague 'meeting place for elders' with the 2008 customary court and a source.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Karakol-Ashuu (Vol3 250)
- Kept the title (linked from E3). Made it the pass at the head of the Western Karakol valley (consistent with E2 Karakol) and its seasonal camp. [MERGED] Absorbed Karakol Mountain Pass (Vol3 420), including its elevation and July–September season.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Ak-Döbö (Vol3 251)
- Replaced the vague 'tell mound' sentence with the 1984 rescue excavation and Andronovo finds; added census population.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Ming-Örük (Vol3 252; formerly "Kenkol-Ayyl")
- **[RETITLED]** Renamed (Kenkol- series). Kept the lower-Kenkol fruit-growing village, now tied to the real Kenkol burial ground as described in E2 Chong-Kenkol.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Eski-Korgon (Vol3 253; formerly "Arslan-Korgon")
- **[RETITLED]** Renamed (Arslan- series mirroring Arslanbob). Kept the Kokand-period fort; dated it to the 1830s, consistent with E2's 1820s–30s Kokand fortification of the valley.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kanysh-Kiya (Vol3 254; formerly "Chatkal-Ayyl")
- **[RETITLED]** Renamed to Kanysh-Kiya, a real village of the Chatkal valley listed in brief §3. Kept the gold panners; added services and the clan rules on panning (consistent with E2 Chatkal River).
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kyrk-Choro (Vol3 255; formerly "Manas-Ayyl")
- **[RETITLED]** Renamed (Manas- series). Kept the poetry-festival village below Manas Peak; dated the August gathering and linked the observatory. The recitation material formerly duplicated in Manas-Korgon (Vol3 325) is consolidated here.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Tuzduu (Vol3 256; formerly "Kulan-Ayyl")
- **[RETITLED]** Renamed (Kulan- series; E2 owns Kulan-Talaa). Kept the camel and sheep pastoralists; added the Karakul state-farm history.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Shaar-Döbö (Vol3 257; formerly "Buzurg-Kand")
- **[RETITLED]** Renamed (Buzurg- series mirroring E2 Shahr-i Buzurg) and made the modern village beside that site; replaced the unsupported claim of 'preserved Sogdian architecture' with reused ramparts brick. [MERGED] Absorbed Buzurg-Rabat (Vol3 327), which made the same claim.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kosh-Döbö (Vol3 258; formerly "Jety-Ayyl")
- **[RETITLED]** Renamed (Jety- repeated E2 Jety-Kaiyng). Kept the seven seasonal camps on the Aksay pastures; added numbers, season and the Kurultai link.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Tegirmen (Vol3 259; formerly "Urmaral-Ayyl")
- **[RETITLED]** Renamed (Urmaral- series). Kept the confluence and trout fishing, made consistent with E2 Urmaral River and E4 Iradi Mountain Trout (trout are introduced, not native).
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kara-Jylga (Vol3 260; formerly "Tuyuk-Ayyl")
- **[RETITLED]** Renamed (Tuyuk- series). Kept the remote dead-end valley with winter horseback access; placed it in the Toktogul–Naryn zone and added the 2012 avalanche episode.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Sarymsakty (Vol3 261; formerly "Nau-Kand")
- **[RETITLED]** Renamed (Nau- series mirroring E2 Kand-i Nau). Kept the garlic, onion and fodder-beet commune; added the 1994 decollectivization.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kümüshtü (Vol3 262; formerly "Shelji-Ayyl")
- **[RETITLED]** Renamed (Shelji- series). Made the modern village beside the real silver-mining site; the 'Nestorian trading center' framing replaced by E2's account of Shelji. [MERGED] Absorbed Shelji-Kishlak (Vol3 332); its 'Silk Road churches' claim is now hedged as disputed.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Ak-Kyya (Vol3 263; formerly "Susamyr-Ayyl")
- **[RETITLED]** Renamed (Susamyr- series). Kept the summer-only yurt-and-cabin settlement (consistent with E2 Suusamyr's few permanent settlements). [MERGED] Absorbed Susamyr-Kishlak (Vol3 333) and its August ulak tartysh tournament.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Tört-Kuduk (Vol3 264; formerly "Kum-Bel-Ayyl")
- **[RETITLED]** [CANON] Renamed and relocated: the old stub made Kum-Bel a miners' town for antimony and tellurium, which contradicts E2 (Kum-Bel is an unmined gold prospect). Repurposed as a Betpak-Dala well village to cover the Northern Steppe zone.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kum-Aryk (Vol3 265; formerly "Kara-Buura-Kishlak")
- **[RETITLED]** [CANON] Renamed and relocated: the 'northern industrial processing centers' framing came from the retired Kara-Balta (E2 notes); Kara-Buura is an agricultural district. Placed beside Nurzhan's oil fields. [MERGED] Absorbed Kara-Buura-Ayyl (Vol3 335), a near-identical 'produce for industrial workers' stub.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Hauzdy (Vol3 266; formerly "Malik-Rabat")
- **[RETITLED]** [CANON] Renamed: Malik- derives from the retired name Rabat-i Malik (now Rabat-i Kamal, brief §3). Made the hamlet beside E2's Rabat-i Kamal. [MERGED] Absorbed Malik-Ayyl (Vol3 336, 'village around a caravanserai') and Malik Well (Vol3 367, 'stone-lined cistern on the caravan route').
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kök-Oi (Vol3 267; formerly "Besh-Tash-Ayyl")
- **[RETITLED]** Renamed (Besh-Tash- series). Kept the park-entrance community. [MERGED] Absorbed Besh-Tash-Beket (Vol3 337, 'gateway hamlet housing park rangers and pack guides').
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Bakyyan (Vol3 268; formerly "Kyzyl-Adyr-Ayyl")
- **[RETITLED]** [CANON] Renamed (Kyzyl-Adyr- series) and moved from the 'middle Talas valley' to Kara-Buura District, where E2 places Kyzyl-Adyr. [MERGED] Absorbed Kyzyl-Adyr-Kishlak (Vol3 338, 'champion distance racing horses').
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Sabz-Kand (Vol3 269)
- Kept the name; placed in Talas District; replaced 'ancient oasis garden village' with census population, crops and the karez users' association.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Tar-Say (Vol3 270; formerly "Moinok-Ayyl")
- **[RETITLED]** Renamed (Moinok- series) and moved: the lower Chu is a flat plain with no sandstone canyon; E2 Kök-Moinok is the canyon country, in the Karatau.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Teke-Tash (Vol3 271; formerly "Alatau-Kishlak")
- **[RETITLED]** Renamed (generic 'Alatau-Kishlak'). Kept the treeline village below glacial cirques; added the hunting ban and warden link.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Ozgörüsh (Vol3 272; formerly "Uzun-Akmat-Ayyl")
- **[RETITLED]** [CANON] Renamed (Uzun-Akmat- series); placed on the real Uzun-Akmat above the Toktogul Reservoir (brief §3, E2). Kept the grapes and dried apricots; added the reservoir resettlement.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Sopol-Tepa (Vol3 273; formerly "Kohna-Kand")
- **[RETITLED]** Renamed and moved (Kohna- series mirroring E2 Kand-i Kohna, which has no artisan village). Kept the glazed-pottery settlement in the Fergana Rim, where the craft fits the Uzbek-speaking population.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Otmek (Vol3 274; formerly "Susamyr-Beket")
- **[RETITLED]** Renamed (Susamyr- series). Kept the weather and telegraph outpost on the transhumance route, made distinct from E4's Kenkol post. [MERGED] Absorbed Tuyuk-Beket (Vol3 330, 'meteorological and road outpost monitoring snowpack on high passes').
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Sary-Döbö (Vol3 275; formerly "Zard-Diz")
- **[RETITLED]** Renamed (inversion of E2 Diz-i Zard) and made the village beside that site; the 'garrison village' became a settler village, with a renaming under the 1993 Toponymic Heritage Statute.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Sasyk-Bulak (Vol3 276; formerly "Karakyr-Ayyl")
- **[RETITLED]** Renamed (Karakyr- series; E2 owns Karakyr Range). Kept the dry-steppe sheep village under the limestone bluffs; added the spring etymology and the raptor counts described in E2.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Bel-Aldy (Vol3 277; formerly "Art-Ayyl")
- **[RETITLED]** Renamed ('Art-Ayyl' was a mechanical 'pass village'). [MERGED] Absorbed Chatkal-Beket (Vol3 324, 'waystation providing remount horses for crossing high passes').
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Temirchi (Vol3 278; formerly "Dastgoh-Ayyl")
- **[RETITLED]** [CANON] Renamed: Dastgoh is an urban district of Nurzhan (E2), so a separate 'Dastgoh-Ayyl' contradicted it. Kept the blacksmithing commune near Nurzhan.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Chet-Bulak (Vol3 279; formerly "Terek-Ayyl")
- **[RETITLED]** Renamed (generic 'Terek-Ayyl', overlapping E2 Ak-Terek's poplars). Kept the early-20th-century settlers and poplars; corrected 'Christian settlers' to Russian Orthodox colonists and added the 1994 renaming.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kaiyrma (Vol3 280; formerly "Darya-Ayyl")
- **[RETITLED]** Renamed (generic 'Darya-Ayyl'). Kept the reed-harvesting and fishing community; placed on the terminal lower Chu (D4, D2) and added the water-diversion context.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Tash-Kuduk (Vol3 281; formerly "Sangin-Rabat")
- **[RETITLED]** Renamed and repurposed: the stub mirrored E2 Rabat-i Sangin (a caravanserai in the Kara-Buura valley). Moved to the Moiynkum to cover the Northern Steppe zone. [MERGED] Absorbed Sangin Well (Vol3 382, 'deep stone-cased well since the Timurid period'); the date is now given as tradition.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Toguz-Bulak (Vol3 282; formerly "Bel-Ayyl")
- **[RETITLED]** Renamed (generic 'Bel-Ayyl'). Kept the pass-side role but tied it to E2's Kök-Bel road instead of duplicating the horse-remount stubs.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Khunuk-Kand (Vol3 283)
- [DELETED] Duplicated E2's Shahr-i Khunuk ('cool town', the summer quarter of Iyık Janyl) under an inverted name; its only content ('Cool City' in Sogdian) is covered there.

##### Jyluu-Bulak (Vol3 284; formerly "Suu-Ayyl")
- **[RETITLED]** Renamed (generic 'Suu-Ayyl'). [MERGED] Absorbed Suu Thermal Springs (Vol3 385), including the 42 °C temperature and fault origin; placed in Lower Naryn District.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Boz-Adyr (Vol3 285; formerly "Tektir-Ayyl")
- **[RETITLED]** Renamed (Tektir- overlapped E2 Boz-Tektir). Kept the dryland wheat and sunflower commune; moved it to the Fergana adyr belt.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Jangy-Jol (Vol3 286; formerly "Navbahor-Ayyl")
- **[RETITLED]** [CANON] Renamed: Navbahor is an urban district of Nurzhan (E2). Kept the 1995 planned settlement with American-style orchard plots, now a resettlement village near Talas.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Teskey-Jar (Vol3 287; formerly "Jar-Ayyl")
- **[RETITLED]** Renamed (generic 'Jar-Ayyl'); moved from the 'middle Talas gorge' (the middle valley is a broad plain) to the upper Talas gorge; added the 2004 landslide.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Karakoyun-Ayyl (Vol3 288)
- [DELETED] Duplicated E2's Kara-Koyun Valley, which already describes the winter gathering place of the Karakoyun clan with its stone livestock pens.

##### Köpürö-Bazar (Vol3 289; formerly "Kalan-Bazar-Ayyl")
- **[RETITLED]** Renamed (Kalan-Bazar- mirrored E2 Bazar-i Kalan, Talas's covered market). Kept the wool and hide auctions near Talas, distinct from the Cattle Mart.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kyrk-Bulak (Vol3 290; formerly "Bulak-Ayyl")
- **[RETITLED]** Renamed (generic 'Bulak-Ayyl'). Kept the cold artesian springs in limestone foothills. [MERGED] Absorbed Ak-Bulak-Ayyl (Vol3 309, 'Chongtor herders near cold artesian springs'), whose name also repeated E2 Ak-Bulak.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Safid-Diz (Vol3 291)
- [DELETED] Duplicated E2's Diz-i Safid (the whitewashed hilltop citadel near Iyık Janyl, refortified in the 18th century) under an inverted name.

##### Ak-Jal (Vol3 292; formerly "Talaa-Ayyl")
- **[RETITLED]** Renamed (generic 'Talaa-Ayyl'). Kept the windswept horse-breeding steppe community; moved from the 'western plains' to the Betpak-Dala to cover the Northern Steppe zone.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Bitik-Tash (Vol3 293; formerly "Unkur-Ayyl")
- **[RETITLED]** Renamed (Unkur- series mirroring E2 Kara-Unkur Cave) and moved to the Karatau, which has its own petroglyph and Paleolithic sites. [MERGED] Absorbed Unkur Ravine (Vol3 394, 'boulder-choked ravine with cave entrances and petroglyph panels').
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Bulak-Bashy (Vol3 294; formerly "Nav-Kand")
- **[RETITLED]** Renamed (Nav- series mirroring E2 Shahr-i Nav, also a 1960s canal village) and moved to Lower Naryn District; kept the 1965 founding, now tied to the Naryn cascade.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Jashyl-Köl (Vol3 295; formerly "Köl-Ayyl")
- **[RETITLED]** Renamed (generic 'Köl-Ayyl'). [MERGED] Absorbed Orto-Köl-Ayyl (Vol3 319, 'seasonal lakeside yurts near moraine tarns'), which described the same kind of settlement.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Shagyldy (Vol3 296; formerly "Sai-Ayyl")
- **[RETITLED]** Renamed (generic 'Sai-Ayyl'). Kept the gravel-mining settlement in a dry riverbed; the gold prospecting is now historical.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Archaly (Vol3 297; formerly "Kenkol-Kishlak")
- **[RETITLED]** [CANON] Renamed (Kenkol- series) and moved: E2 Chong-Kenkol's forest is protected from commercial felling, so a Kenkol logging village contradicted it. Kept the timber and raspberry village in the Chatkal Highlands under clan limits.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kapka-Tash (Vol3 298; formerly "Darwaza-Ayyl")
- **[RETITLED]** [CANON] Renamed: Darwaza is a retired name (now Temir-Kapka, the Talas city gate). Repurposed as a 'gate' village at a gorge mouth on the road from Tash-Kömür to the Uzbek border.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Ak-Chiy (Vol3 299)
- Kept the name; placed on the Moiynkum margin; added the chiy craft. [MERGED] Absorbed Chiy Flats (Vol3 400, 'salt depression covered with needlegrass used for winter sheep grazing').
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kalba (Vol3 300; formerly "Kara-Suu-Beket")
- **[RETITLED]** Renamed (Kara-Suu-…-Beket mechanical series). Kept the livestock waystation from the ATR to Talas, now at the Qara-Chik checkpoint road (E4); dropped the rail link, which E2 gives to Kara-Bulak.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kök-Döbö (Vol3 301)
- Kept the name; removed 'panoramic' puffery. [MERGED] Absorbed Kök-Döbö Hill (Vol3 402); its 'modern radar station' is now a weather radar.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kamyshtuu (Vol3 302; formerly "Sary-Kamysh")
- **[RETITLED]** Renamed (Sary-Kamysh is the name of a well-known lake in Turkmenistan and a town in Turkey). Kept the reed hamlet by seasonal drainage marshes at the desert edge.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Uuk-Bulak (Vol3 303; formerly "Kyzyl-Tuu")
- **[RETITLED]** Renamed: Kyzyl-Tuu is the name of a real yurt-making village outside the footprint. Kept the yurt-strut craft village; linked the E3 yurt-part articles.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Besh-Köl (Vol3 304)
- Kept the name; added elevation, season, size and the link to the Besh-Köl Glaciers stub.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Altyn-Bulak (Vol3 305)
- Kept the name; placed in Lower Naryn District; added the 1978 bottling plant and etymology.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Zhalgyz-Terek (Vol3 306)
- Kept the name; placed in the Moiynkum. [MERGED] Absorbed Terek Spring (Vol3 380, 'cold spring with ancient poplars offering rest to desert travelers').
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Tash-Köröö (Vol3 307)
- Kept the name. [MERGED] Absorbed Tash-Köröö Gorge (Vol3 408, 'box canyon used as a natural sheep pen during blizzards'), which explains the village name.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kara-Kungey (Vol3 308)
- Corrected the self-contradictory 'shaded north-facing' description (*kungöy* means a sun-facing slope); added population and economy.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Ak-Bulak-Ayyl (Vol3 309)
- [MERGED] into Kyrk-Bulak (formerly Bulak-Ayyl): both described a herders' hamlet at cold artesian springs.

##### Kara-Say (Vol3 310; formerly "Besh-Tash-Kishlak")
- **[RETITLED]** Renamed (Besh-Tash- series) and moved away from the Besh-Tash valley; kept the barley and fodder-clover farming.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Örüktü (Vol3 311; formerly "Kara-Döbö-Ayyl")
- **[RETITLED]** Renamed (mechanical -Ayyl). Kept the terraced apricots and stone-lined channels; placed in the Fergana Rim.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Sary-Bulak-Ayyl (Vol3 312)
- [MERGED] into Sary-Bulak: both described the mining settlement of the Sary-Bulak Antimony Works.

##### Kök-Say (Vol3 313; formerly "Kök-Sai-Ayyl")
- **[RETITLED]** Renamed by dropping the mechanical suffix; moved from the Kara-Suu (now covered by Chong-Kapka) to a Karatau limestone gorge.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Aral (Vol3 314; formerly "Taldy-Bulak-Kishlak")
- **[RETITLED]** Renamed (Taldy-Bulak- repeated E2 Taldy-Bulak). Kept the willow groves, honey and horse training; placed in the Chu lowlands.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kosh-Bel (Vol3 315; formerly "Kashka-Suu-Ayyl")
- **[RETITLED]** Renamed (Kashka-Suu- repeated E2's Kashka-Suu river). Kept the high staging post for transhumant herds.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Uch-Emchek (Vol3 316; formerly "Cholpon-Kishlak")
- **[RETITLED]** Renamed (Cholpon- series). Kept the irrigated sugar-beet and winter-wheat farming; tied it to E2's sugar factory at Besh-Terek.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Bazar-Bulak-Ayyl (Vol3 317)
- [MERGED] into Bazar-Terek: both described a crossroads market village trading wool and fleece.

##### Kyzyl-Döbö (Vol3 318; formerly "Kyzyl-Tash-Ayyl")
- **[RETITLED]** Renamed (mechanical -Ayyl). Kept the red-sandstone craft village of leather and felt workers.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Orto-Köl-Ayyl (Vol3 319)
- [MERGED] into Jashyl-Köl (formerly Köl-Ayyl): both described seasonal yurts beside alpine moraine lakes.

##### Muz-Tör (Vol3 320; formerly "Karakol-Tash")
- **[RETITLED]** [CANON] Renamed: Karakol- duplicated E2's Karakol (Western Karakol valley) and Karakol-Ashuu (E2 notes flagged it). Kept the timber and mountain-guide outpost below glaciated passes, moved to the Chatkal.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Ak-Jar (Vol3 321; formerly "Ak-Jar-Ayyl")
- **[RETITLED]** Renamed by dropping the mechanical suffix. Kept the semi-desert Karakul-sheep village. [MERGED] Absorbed Ak-Jar Escarpment (Vol3 421, 'limestone ridge forming a windbreak against desert dust storms').
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Jele-Döbö (Vol3 322; formerly "Kenkol-Bulak")
- **[RETITLED]** Renamed (Kenkol- series) and moved: trout hatcheries and walnuts fit the Toktogul Reservoir shore, where cage trout farming is practiced.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Jangak-Bulak (Vol3 323; formerly "Arslan-Bulak")
- **[RETITLED]** Renamed (Arslan- series mirroring Arslanbob). Kept the walnut-grove hamlet with a grove sacred in Syro-Iradi tradition, now presented as tradition shared with local Muslims.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Chatkal-Beket (Vol3 324)
- [MERGED] into Bel-Aldy (formerly Art-Ayyl): both described a pass-side station providing horses for crossing the Chatkal passes.

##### Korgoncho (Vol3 325; formerly "Manas-Korgon")
- **[RETITLED]** Renamed (Manas- series). Kept the historic mudbrick defensive village, moved to the Fergana Rim; its epic recitations are consolidated in Kyrk-Choro (formerly Manas-Ayyl).
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Töö-Kuduk (Vol3 326; formerly "Kulan-Bulak")
- **[RETITLED]** Renamed (Kulan- series). Kept the desert well and camel herds; moved from the 'Kyzylkum margin' (now covered by Tuzduu) to the Moiynkum.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Buzurg-Rabat (Vol3 327)
- [MERGED] into Shaar-Döbö (formerly Buzurg-Kand): both claimed 'ancient Sogdian adobe architecture' for a hamlet named after Shahr-i Buzurg.

##### Dary-Bulak (Vol3 328; formerly "Jety-Bulak")
- **[RETITLED]** Renamed (Jety- series). Kept the summer yurt camp around seven mineral springs. [MERGED] Absorbed Jety-Bulak Springs (Vol3 428), including the 38 °C bicarbonate springs.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Almaluu (Vol3 329; formerly "Urmaral-Kishlak")
- **[RETITLED]** Renamed (Urmaral- series). Kept the apple orchards and felt-rug making.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Tuyuk-Beket (Vol3 330)
- [MERGED] into Otmek (formerly Susamyr-Beket): both described a high-pass weather and road outpost monitoring snow.

##### Tunuk-Bulak (Vol3 331; formerly "Nau-Bulak")
- **[RETITLED]** Renamed (Nau- series). Kept the farming village watered by karst springs; tied it to the karst stubs (formerly Nau Spring and Nau Karst Caverns).
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Shelji-Kishlak (Vol3 332)
- [MERGED] into Kümüshtü (formerly Shelji-Ayyl): both described the village beside the Shelji ruins.

##### Susamyr-Kishlak (Vol3 333)
- [MERGED] into Ak-Kyya (formerly Susamyr-Ayyl): both described a summer settlement in the Suusamyr valley.

##### Kum-Bel-Beket (Vol3 334)
- [DELETED] [CANON] Duplicated E2's Kum-Bel, which already records the Soviet geological camp on the ridge (until 1991); its 'antimony and rare earth surveys' contradicted E2's gold prospect.

##### Kara-Buura-Ayyl (Vol3 335)
- [MERGED] into Kum-Aryk (formerly Kara-Buura-Kishlak): both described a suburban farm village supplying industrial workers.

##### Malik-Ayyl (Vol3 336)
- [MERGED] into Hauzdy (formerly Malik-Rabat): both described a hamlet around a medieval caravanserai.

##### Besh-Tash-Beket (Vol3 337)
- [MERGED] into Kök-Oi (formerly Besh-Tash-Ayyl): both described the community at the Besh-Tash park entrance.

##### Kyzyl-Adyr-Kishlak (Vol3 338)
- [MERGED] into Bakyyan (formerly Kyzyl-Adyr-Ayyl): both described a village of racehorse trainers near Kyzyl-Adyr.

#### Physical Geography (Vol3 339–439)

##### Kök-Suu Peak (Vol3 339)
- Kept the title; added location between the Kara-Buura and Chatkal basins, geology, glaciers and the river that names it.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Chakmak-Say (Vol3 340; formerly "Sary-Bulak Creek")
- **[RETITLED]** Renamed: 'Sary-Bulak' is the antimony mine and district (brief §2), so a Chatkal stream of that name invited confusion. Kept the seasonal snowmelt torrent of the western Chatkal range.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kumdy-Bulak (Vol3 341; formerly "Kara-Bulak Spring")
- **[RETITLED]** Renamed: Kara-Bulak is E2's market town in the Talas valley. Kept the artesian spring for herders, moved to the Moiynkum. [MERGED] Absorbed Malik Springs (Vol3 436, 'perennial artesian spring sustaining passing livestock herds').
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Bürküt-Uya (Vol3 342; formerly "Ak-Tash Ravine")
- **[RETITLED]** Renamed: Ak-Tash is E2's village in Kara-Buura District (E2 notes flagged the overlap). Kept the limestone ravine with bearded-vulture nests, moved to the Karatau, where E4 records the species.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kyzyl-Bel Pass (Vol3 343)
- Kept the title; tied to the Kyzyl-Bel hamlet; added geology, season and use.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kalmak-Kuduk (Vol3 344; formerly "Besh-Terek Well")
- **[RETITLED]** Renamed: Besh-Terek is E2's village in Chu District. Kept the deep Soviet borehole sustaining winter herds; moved from the Kyzylkum fringe to the Betpak-Dala.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Ichke-Suu Gorge (Vol3 345; formerly "Taldy-Suu Gorge")
- **[RETITLED]** Renamed (Taldy-Suu series). Kept the riparian gorge with sea buckthorn and birch. [MERGED] Absorbed Besh-Terek Ravine (Vol3 410, 'incised sandstone ravine harboring relict sea buckthorn thickets').
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Boz-Suu (Vol3 346; formerly "Kashka-Darya Tributary")
- **[RETITLED]** [CANON] Renamed and relocated: the Kashka-Darya is a large river of southern Uzbekistan, outside the footprint, and the upper Chu is in Kyrgyzstan (E2 Orto-Sai Reservoir). Now a Kyrgyz Range stream entering Chu District.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Tegerek-Köl (Vol3 347; formerly "Cholpon Tarn")
- **[RETITLED]** Renamed (Cholpon- series). Kept the circular cirque lake at 3,150 m. [MERGED] Absorbed Taldy-Suu Tarn (Vol3 414, 'oligotrophic glacial tarn at 3,050 m').
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Tuura-Say (Vol3 348; formerly "Bazar-Sai Wash")
- **[RETITLED]** Renamed (Bazar-Sai). [MERGED] Absorbed Bazar-Sai Wash (2) (Vol3 417) and Sai Creek (Vol3 397), all describing a dry gravel wash with spring flash floods.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kyzyl-Jar Bluffs (Vol3 349)
- [DELETED] Duplicated E2's Kyzyl-Jar (red sandstone cliffs and badlands on the western edge of Irad, where the Karatau meets the Kyzylkum Fringe).

##### Uch-Terek Rapids (Vol3 350; formerly "Orto-Sai Rapids")
- **[RETITLED]** [CANON] Renamed and relocated: Orto-Sai is the Kyrgyz reservoir on the upper Chu (E2), and the 'middle Chu' lies in Kyrgyzstan. Kept the white-water rapids, now on the Naryn above the Toktogul Reservoir.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Karakol Glacier (Vol3 351)
- Kept the title (E2 keeps Karakol as a village in the Western Karakol valley). Added dimensions, retreat, and the river it feeds; 'Tian Shan marches' replaced by an exact location.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Ak-Suu Mineral Springs (Vol3 352)
- Kept the title; made it the warm springs at the foot of E2's Ak-Suu Canyon; removed 'renowned'; added temperature, chemistry and protection.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Uzun-Kyr (Vol3 353; formerly "Kenkol Ridge")
- **[RETITLED]** Renamed (Kenkol- series; the Kenkol valley is in the Talas Alatau, not between two farming valleys). Kept a ridge separating agricultural land in northern Irad, now an oil-bearing anticline near Nurzhan.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Arslanbob Falls (Vol3 354)
- Kept the title; corrected 'a spectacular 40-meter waterfall over basalt columns' to the two falls described in E2 Arslanbob, with plausible heights; removed puffery.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Chatkal Gorge (Vol3 355)
- Kept the title; located the gorge on the lower Chatkal (E2); added length, geology and rafting. [MERGED] Absorbed Chatkal Rapids (Vol3 424).
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Manas Glacier (Vol3 356)
- Kept the title (linked from D2 and E2). [CANON] Corrected 'the largest hanging glacier in Irad' to a benchmark glacier, consistent with D2's observatory article. [MERGED] Absorbed Manas Northern Face (Vol3 425).
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kulan-Sor (Vol3 357; formerly "Kulan Dry Lake")
- **[RETITLED]** Renamed (Kulan- series; the plain is E2's Kulan-Talaa). [MERGED] Absorbed Kulan Salt Pan (Vol3 426), which described the same playa.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Eski-Aryk (Vol3 358; formerly "Buzurg Canal")
- **[RETITLED]** Renamed (Buzurg- series). Kept the canal of medieval origin still in use, now hedged ('part of its course follows'). [MERGED] Absorbed Buzurg Canal Outlet (Vol3 427, 'terminal discharge gates').
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Jety-Kaiyng Rocks (Vol3 359)
- [DELETED] Duplicated E2's Jety-Kaiyng (red sandstone pillars, 'seven birches').

##### Urmaral Tarns (Vol3 360)
- Kept the title; tied to E2's Urmaral River and D2's lake monitoring; removed 'pristine'.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kara-Kazan Cirque (Vol3 361; formerly "Tuyuk Cirque")
- **[RETITLED]** Renamed (Tuyuk- series). Kept the amphitheater cirque ringed by rock needles in the high Chatkal. [MERGED] Absorbed Orto-Köl Cirque (Vol3 419, 'granite cirque ringed by 600-meter cliffs').
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Maryam-Bulak (Vol3 362; formerly "Nau Spring")
- **[RETITLED]** Renamed (Nau- series). Kept the holy karst spring revered by local Christians; gave it a St. Maryam dedication (brief §8 naming) and a chapel history.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Shelji Mound (Vol3 363)
- [DELETED] Duplicated E2's Shelji (the citadel mound and walled medieval town); 'unexcavated frontier fortress' contradicted E2's excavation record.

##### Susamyr Meadow (Vol3 364)
- [DELETED] Duplicated E2's Suusamyr (the high valley of subalpine meadow and steppe used as summer pasture).

##### Altyn-Say (Vol3 365; formerly "Kum-Bel Creek")
- **[RETITLED]** Renamed (Kum-Bel- series; E2 already notes placer gold below Kum-Bel). Kept the mineralized, gold-bearing stream as a separate Chatkal tributary.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kuru-Say (Vol3 366; formerly "Kara-Buura Wash")
- **[RETITLED]** Renamed: Kara-Buura is the real river and district (E2), and a 'Kara-Buura Wash' blurred the two. [MERGED] Absorbed Kara-Buura Wash (2) (Vol3 435).
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Malik Well (Vol3 367)
- [MERGED] into Hauzdy (formerly Malik-Rabat), the hamlet named after the cisterns of Rabat-i Kamal; the retired Malik- name is dropped.

##### Besh-Tash Upper Lake (Vol3 368)
- Kept the title (linked from D2); [CANON] aligned elevation, depth and cirque setting with D2 Besh-Tash Ecological Conservation Area and the line placement with E2 Besh-Tash National Park.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kyzyl-Adyr Hills (Vol3 369)
- Kept the title as the hills that name the district center. [MERGED] Absorbed Kyzyl-Adyr Loess Hills (Vol3 438), which described the same hills.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kashkar-Aryk (Vol3 370; formerly "Sabz Creek")
- **[RETITLED]** Renamed (Sabz- repeated Sabz-Kand). Kept the gentle spring-fed stream irrigating orchards in northern Talas.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Moinok Towers (Vol3 371)
- [DELETED] Duplicated E2's Kök-Moinok (eroded canyons, ribs and pillars in the Karatau); the stub's placement in the lower Chu basin was wrong.

##### Ak-Muz (Vol3 372; formerly "Alatau Snowfield")
- **[RETITLED]** Renamed (generic 'Alatau'). Kept the permanent snowfield feeding southern reservoirs, now the Toktogul Reservoir via the Uzun-Akmat. [MERGED] Absorbed Tuyuk-Suu Snowfields (Vol3 430).
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Uzun-Akmat Terraces (Vol3 373)
- Kept the title; tied to the Uzun-Akmat (brief §3) and Ozgörüsh; hedged the age ('centuries ago').
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Karool-Döbö (Vol3 374; formerly "Kohna Bluff")
- **[RETITLED]** Renamed (Kohna- series mirroring E2 Kand-i Kohna). Kept the confluence terrace with lookout remains.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Teshik-Talaa (Vol3 375; formerly "Susamyr Sinks")
- **[RETITLED]** Renamed (Susamyr- series) and moved: E2 Suusamyr is a valley of meadow and steppe, not karst. Kept the sinkhole landscape, placed in the limestone Karatau.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Zard Hill (Vol3 376)
- [DELETED] Duplicated E2's Diz-i Zard (the yellow-loess mound with a Kokand fort of the 1820s).

##### Karakyr Cliffs (Vol3 377)
- [DELETED] Duplicated E2's Karakyr Range (the limestone ridge and its raptors); the raptor material is already there.

##### Kylych-Kyr (Vol3 378; formerly "Art Ridge")
- **[RETITLED]** Renamed (generic 'Art' = pass). Kept the razor-thin arête between two summits; linked to Ak-Bash (formerly Ak-Tash Peak).
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Dastgoh Creek (Vol3 379)
- Kept the title (mentioned in A5 and E2); aligned with their wording; added length and present condition.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Terek Spring (Vol3 380)
- [MERGED] into Zhalgyz-Terek, the desert hamlet that grew up at a poplar-shaded spring used by travelers.

##### Akzhaykyn Depression (Vol3 381; formerly "Darya Marshes")
- **[RETITLED]** Renamed: 'Darya' is a generic word for river. The stub's 'river delta' wetlands are now the real terminal basin of the Chu named in D4. [MERGED] Absorbed Kamysh Marshes (Vol3 403, 'freshwater marshes along the river delta harboring wildfowl').
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Sangin Well (Vol3 382)
- [MERGED] into Tash-Kuduk (formerly Sangin-Rabat), the hamlet around a stone-lined desert well.

##### Kichi-Bel (Vol3 383; formerly "Bel Saddle")
- **[RETITLED]** Renamed (generic 'Bel'). Kept the low pass at 1,950 m used by pack horses in early spring.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Khunuk Creek (Vol3 384)
- Kept the title (E2 mentions it); corrected 'alpine brook' and 'summer settlement' to the stream of E2's Shahr-i Khunuk quarter.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Suu Thermal Springs (Vol3 385)
- [MERGED] into Jyluu-Bulak (formerly Suu-Ayyl), the spa village at the same 42 °C springs.

##### Ambar-Döbö (Vol3 386; formerly "Tektir Terrace")
- **[RETITLED]** Renamed (Tektir- overlapped E2 Boz-Tektir). Kept the alluvial terrace with ancient grain pits; dated the pits.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Navbahor Pond (Vol3 387)
- [CANON] Moved from Talas to Nurzhan: Navbahor is an urban district of Nurzhan built in the territorial period (E2). Kept the 1998 landscape-irrigation reservoir.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kök-Kamar Gorge (Vol3 388; formerly "Jar Gorge")
- **[RETITLED]** Renamed (generic 'Jar'). Kept the boulder-strewn canyon with white-water rapids, placed in the Fergana Rim.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Karakoyun Pass (Vol3 389)
- Kept the title (mentioned in E4 Muratbek Biy); tied to E2 Kara-Koyun Valley; added elevation, migration timing and the grave.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Sarchashma Springs (Vol3 390; formerly "Kalan Springs")
- **[RETITLED]** Renamed (Kalan- mirrored E2 Bazar-i Kalan). Kept the springs feeding the fountains and bathhouses of Old Talas.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Ak-Balyk Creek (Vol3 391; formerly "Bulak Creek")
- **[RETITLED]** Renamed (generic 'Bulak'). Kept the clear tributary with aquatic plants and trout; [CANON] trout made 'stocked', consistent with E4 Iradi Mountain Trout.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Ak-Kyr (Vol3 392; formerly "Safid Ridge")
- **[RETITLED]** Renamed (Safid- mirrored E2 Diz-i Safid). Kept the pale limestone ridge; placed in the Silurian limestone belt of Sary-Bulak District described in D4.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kaz-Köl (Vol3 393; formerly "Talaa Depressions")
- **[RETITLED]** Renamed (Talaa- series). Kept the seasonal saline wetlands with migrating flamingos; placed on the Betpak-Dala.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Unkur Ravine (Vol3 394)
- [MERGED] into Bitik-Tash (formerly Unkur-Ayyl), whose ravine of rock shelters and petroglyphs this stub described.

##### Jangy-Aryk (Vol3 395; formerly "Nav Canal")
- **[RETITLED]** Renamed (Nav- series). Kept the 25-km concrete canal of the 1960s for reclaiming steppe; tied to E2 Shahr-i Nav's branch canal.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Köl-Sai (Vol3 396)
- Kept the title; made it an outburst-flood torrent (consistent with D2's GLOF monitoring) with the 2012 event.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Sai Creek (Vol3 397)
- [MERGED] into Tuura-Say (formerly Bazar-Sai Wash): both described a dry gravel creek with violent flash floods.

##### Kenkol Rapids (Vol3 398)
- [DELETED] Trivially redundant with E2's Chong-Kenkol (the narrow gorge of the upper Kenkol River); the stub gave no location or facts.

##### Kapka-Bel (Vol3 399; formerly "Darwaza Pass")
- **[RETITLED]** [CANON] Renamed: Darwaza is a retired name (brief §3). Kept the natural gap forming the historic northern entrance to the Talas valley.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Chiy Flats (Vol3 400)
- [MERGED] into Ak-Chiy, the village named after the needlegrass of these salt flats.

##### Kara-Suu Rapids (Vol3 401)
- Kept the title; tied to the upper Kara-Suu (Chong-Kapka), the Kara-Suu Canyon and E2's hydroelectric station.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kök-Döbö Hill (Vol3 402)
- [MERGED] into Kök-Döbö, the village on the hill; the 'modern radar station' is a weather radar.

##### Kamysh Marshes (Vol3 403)
- [MERGED] into Akzhaykyn Depression (formerly Darya Marshes): both described reed marshes of the river delta.

##### Chopo-Jar (Vol3 404; formerly "Kyzyl-Tuu Bluffs")
- **[RETITLED]** Renamed (Kyzyl-Tuu series). Kept the red clay cliffs quarried for pigment and potter's clay; tied to Sopol-Tepa (formerly Kohna-Kand).
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Besh-Köl Glaciers (Vol3 405)
- Kept the title; tied to the Besh-Köl camp; added area and retreat.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Isyk-Bulak (Vol3 406; formerly "Altyn Springs")
- **[RETITLED]** Renamed (Altyn- repeated Altyn-Bulak). Kept the warm bicarbonate springs near old antimony prospects; placed near E2's Terek-Sai.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Mazar-Too (Vol3 407; formerly "Zhalgyz Peak")
- **[RETITLED]** Renamed (Zhalgyz- repeated Zhalgyz-Terek). Kept the isolated triangular peak above the steppe; added elevation and the summit shrine.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Tash-Köröö Gorge (Vol3 408)
- [MERGED] into Tash-Köröö: the box canyon used as a natural sheep pen gives the village its name.

##### Ak-Bash (Vol3 409; formerly "Ak-Tash Peak")
- **[RETITLED]** Renamed: Ak-Tash is E2's village in Kara-Buura District (E2 notes flagged the overlap). Kept the 3,920-m glaciated limestone peak above alpine pastures.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Besh-Terek Ravine (Vol3 410)
- [MERGED] into Ichke-Suu Gorge (formerly Taldy-Suu Gorge): both described a riparian ravine with relict sea buckthorn thickets.

##### Muz-Suu (Vol3 411; formerly "Kara-Bulak Torrent")
- **[RETITLED]** Renamed (Kara-Bulak is E2's market town). Kept the fast mountain torrent fed by perennial cirque glaciers.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Sary-Bulak Gorge (Vol3 412)
- Kept the title; [CANON] aligned with D5 (veins mapped in the Sary-Bulak gorge in the early 1950s) and the canonical mine location.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Koi-Bel (Vol3 413; formerly "Kök-Sai Saddle")
- **[RETITLED]** Renamed (Kök-Sai repeated Kök-Say). Kept the 2,680-m pack-horse saddle used for sheep drives.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Taldy-Suu Tarn (Vol3 414)
- [MERGED] into Tegerek-Köl (formerly Cholpon Tarn): both described a cold cirque tarn at about 3,100 m in the Talas Alatau.

##### Kashka-Suu Glaciers (Vol3 415)
- Kept the title (consistent with E2 Kashka-Suu, 'fed by snowfields and small glaciers'); added elevations and retreat figures in line with D2.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Sary-Kyr (Vol3 416; formerly "Cholpon Ridge")
- **[RETITLED]** Renamed (Cholpon- series). Kept the rolling loess ridge with rain-fed barley and raptor migration.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Bazar-Sai Wash (2) (Vol3 417)
- [MERGED] Duplicate of Bazar-Sai Wash, now Tuura-Say.

##### Sadaf-Jar (Vol3 418; formerly "Kyzyl-Tash Bluffs")
- **[RETITLED]** Renamed (Kyzyl-Tash series). Kept the vermilion sandstone bluffs with fossil mollusks and raptor nests.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Orto-Köl Cirque (Vol3 419)
- [MERGED] into Kara-Kazan Cirque (formerly Tuyuk Cirque): both described a granite cirque ringed by high cliffs.

##### Karakol Mountain Pass (Vol3 420)
- [MERGED] into Karakol-Ashuu ('Karakol pass'), the same pass.

##### Ak-Jar Escarpment (Vol3 421)
- [MERGED] into Ak-Jar (formerly Ak-Jar-Ayyl), the village named after the escarpment.

##### Kenkol Gorges (Vol3 422)
- [DELETED] Duplicated E2's Chong-Kenkol (the spruce-lined gorge of the upper Kenkol).

##### Arslanbob Basin (Vol3 423)
- [DELETED] Duplicated E2's Arslanbob (village and walnut-fruit forest), which the new full article (brief §10) will also cover.

##### Chatkal Rapids (Vol3 424)
- [MERGED] into Chatkal Gorge.

##### Manas Northern Face (Vol3 425)
- [MERGED] into Manas Glacier, which lies at the foot of the face.

##### Kulan Salt Pan (Vol3 426)
- [MERGED] into Kulan-Sor (formerly Kulan Dry Lake), the same playa.

##### Buzurg Canal Outlet (Vol3 427)
- [MERGED] into Eski-Aryk (formerly Buzurg Canal).

##### Jety-Bulak Springs (Vol3 428)
- [MERGED] into Dary-Bulak (formerly Jety-Bulak), the camp at the same springs.

##### Tar-Kapchygai (Vol3 429; formerly "Urmaral Gorges")
- **[RETITLED]** Renamed (Urmaral- series) and moved to the Uzun-Akmat. Kept the narrow, shaded granite gorge with birch and rowan woods.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Tuyuk-Suu Snowfields (Vol3 430)
- [MERGED] into Ak-Muz (formerly Alatau Snowfield): both described perennial snowfields feeding southern irrigation.

##### Kyrk-Kazyk Caves (Vol3 431; formerly "Nau Karst Caverns")
- **[RETITLED]** Renamed (Nau- series). Kept the karst cave network with hibernating horseshoe bats; placed in the Ak-Kyr limestone (Sary-Bulak District).
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kum-Say Fan (Vol3 432; formerly "Shelji Alluvial Fan")
- **[RETITLED]** [CANON] Renamed and relocated: Shelji is in the upper Talas valley, where cotton is not grown. Kept the fertile loess fan supporting cotton, moved to the Fergana Rim.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Susamyr High Steppe (Vol3 433)
- [DELETED] Duplicated E2's Suusamyr (the high sub-alpine valley used as summer pasture).

##### Kum-Bel Ridge (Vol3 434)
- [DELETED] [CANON] Duplicated E2's Kum-Bel, the gold prospect on a ridge of that name; the stub's 'antimony quartz veins' contradicted E2.

##### Kara-Buura Wash (2) (Vol3 435)
- [MERGED] Duplicate of Kara-Buura Wash, now Kuru-Say.

##### Malik Springs (Vol3 436)
- [MERGED] into Kumdy-Bulak (formerly Kara-Bulak Spring): both described a perennial artesian spring watering livestock; the retired Malik- name is dropped.

##### Besh-Tash Lower Tarn (Vol3 437)
- Kept the title (linked from D2); aligned elevation and setting with D2.
- Rewritten in encyclopedia format with references; templated sentence removed.

##### Kyzyl-Adyr Loess Hills (Vol3 438)
- [MERGED] into Kyzyl-Adyr Hills, the same hills.

##### Achuu-Köl (Vol3 439; formerly "Ak-Kungey Mineral Tarn")
- **[RETITLED]** Renamed (Ak-Kungey mirrored Kara-Kungey). Kept the turquoise mineral tarn at about 2,950–3,000 m; explained the mineralization.
- Rewritten in encyclopedia format with references; templated sentence removed.

Untouched articles: none (every stub in the chunk was rewritten, merged or deleted).


## Part G. New articles [NEW]

Vol1 3.29–3.43 (B-class) and Vol2 4.101–4.144 (C-class).


### W1: Politics and status

### Changelog: writer W1 (Politics and status), new articles

All six articles are new files in `pass2/new/`. Each uses the `### NEW. <Title>` heading, the assessment line, `##` sections with `####` subsections, and an `<ol class="references">` list whose entries match the `<sup>[n]</sup>` markers. Every reference in each list is cited. No real document numbers are used. Hidden-lore items appear only as the brief's attributed public line: the health retreat versus the digital-synthesis allegations, and the unverified tabloid reports on access to the estate. Zara, Maksat's China contacts, Bekzatov's putsch talk, Ilyasov's funding and Alikhan's US links are not mentioned beyond public canon.

##### Political status of Irad (B-Class, Politics & Government) [NEW]
- **What it covers:** about 2,900 words.
  - Background from 1925 through the territorial association, the 2006 withdrawal and the DRI, to suspended sovereignty.
  - Status under international law: Chapter XI listing; the administering-power question, with a Western Sahara/Spain comparison; automatic reversion versus the annulment decree; recognition.
  - Positions of the ISEZ, the IAC, the three claimants, the United States and the UN.
  - The unification process (2008, 2011, 2017 polling, census dispute).
  - Practical consequences (no UN/UPU membership, Kazakh postal routing, no IMF access or codes, sport, the Naryn Protocol).
  - Proposed solutions.
- **Canon followed:**
  - NSGT listing since 1992, with the US added as administering power later in 1992.
  - The US did not notify the UN; the listing was kept "at US insistence"; Washington does not report.
  - The Special Committee sits in New York and issues an annual working paper.
  - 26 recognitions, with a minority still recognizing a "Republic of Irad".
  - Ruling of 7 December 2006 by Isakov; the court never ruled on the annulment.
  - Tilek Kurmanov's position before the Special Committee, 2008–2017.
  - The 2025 Trump remarks are limited to existing canon, with the demarche through UNMI.
- **New details (logged in notes):**
  - The US transmitted annual information during 1992–2006.
  - Recognitions of the DRI date from December 2006 to February 2007.
  - A few states accept ISEZ trade representatives under the "Republic of Irad" title.
  - An IAC memorandum to the Special Committee (2019) and a DPI policy statement (2017) are cited as sources.
- **Kept neutral:** the 2018 border clashes are described as with "neighboring border guards", because the chunks disagree on Kazakh versus Uzbek.

##### Elections in Irad (B-Class, Politics & Government) [NEW]
- **What it covers:** about 2,250 words.
  - History: the Soviet period, the 1992 Provisional Government, the territorial period, the DRI and the ISEZ.
  - Electoral system: Governor and LG, legislature, municipal elections, administration and franchise, the tribal regions.
  - Results tables for 2011–2023, gubernatorial and legislative.
  - Assessments.
- **Canon followed:**
  - Interim legislature from October 1992; first general elections in 1994; bicameral Senate of 15 and House of 35.
  - Two-term limit removed in June 2013 by 53–4–3.
  - Toktarov's results: November 2011, 88.74%; 2015, 78.25%; 2019, 90.31%; 2023, 92.75%.
  - The 2015 disqualifications.
  - 60-seat chamber elected in 8 multi-member constituencies (3 cities and 5 districts) on the same day as the Governor.
  - 2023 seats: DPI 51, independents 6, Russo 3.
  - Mayors are appointed and councils elected.
  - The 2007–11 tenure counted as the first term.
  - Next election in late 2027.
- **New canon (logged):**
  - Election day is the first Tuesday after the first Monday in November, kept from the territorial era.
  - Terms: the territorial term began on the first Monday of January; the ISEZ term begins on the fourth Monday of November.
  - The Governor and LG are elected on a joint ticket.
  - Majority requirement with a runoff (never used).
  - Since 2015, candidates need 10,000 signatures and ten years' residence.
  - List PR with the largest-remainder method.
  - Territorial Election Commission of seven members.
  - Municipal councils elected from 1993; since 2011 on the general-election day.
  - Territorial governors won 52–62%.
  - Official turnouts: 67.9%, 58.4%, 73.2% and 71.6%.
  - Seats in 2011, 2015 and 2019: 49/7/4, 52/5/3 and 54/4/2. The 2011 figures are consistent with the 2013 vote.
  - Last territorial general election on 7 November 2006.

##### 2023 Iradi gubernatorial election (C-Class, Politics & Government) [NEW]
- **What it covers:** about 1,200 words.
  - Background: the Boz-Korgon move and the October protests.
  - Nominations, campaign and conduct (OSCE findings, Legal Defense Guild).
  - Results table, legislative and municipal results, aftermath.
- **Canon followed:**
  - Toktarov–Maksat ticket, 92.75%.
  - DPI 51 / independents 6 / Russo 3.
  - The election came a month after the October 2023 protests.
  - The surcharge was suspended by Maksat in November 2023.
  - Ilyasov was held for three days; mobile data was cut for three days.
  - Bekzatov has never stood for office.
- **New canon (logged):**
  - Election held on 7 November 2023.
  - DPI congress in August 2023.
  - Five nominations, of which three tickets were registered.
  - Candidates: Oleg Zubarev (Russo-aligned independent, 4.61%) and Damira Kenesbaeva (independent, 2.64%).
  - Official turnout of 71.6%.
  - Zubarev took a little over 11% in Nurzhan.
  - Surcharge suspension placed "in early November, shortly before the vote".
  - Ilyasov did not meet the residence rule.
  - Oath taken in Legislative Hall on 27 November 2023.
  - The Russo bloc kept its Nurzhan council majority.

##### List of governors of Irad (C-Class, Politics & Government) [NEW]
- **What it covers:** about 1,400 words.
  - The office.
  - Heads before 1992, for context: Chernov and Alimbekov.
  - Tables of the US High Commissioners and the elected territorial governors, with short biographies.
  - The DRI interregnum.
  - Toktarov, plus a table of ISEZ lieutenant governors.
- **Canon followed:**
  - A High Commissioner sat alongside the elected Governor.
  - An interim US administration governed until the first elections (matches the Operation Starlight and Organic Act new articles).
  - Office abolished on 3 December 2006.
  - Toktarov took office after the September 2007 ceasefire.
  - Maksat has been LG since November 2019.
  - Hidden-lore line handled per brief.
- **New canon (logged):**
  - High Commissioners: Richard M. Ashby (1992–95), Carol J. Whitaker (1995–99), Howard T. Lindqvist (1999–2003) and Stephen R. Garrity (2003–06), all fictional. The office reported to the Department of the Interior.
  - Governor Nurlanbek Ermatov (DPI, b. 1947): 1995–2003, elected 1994 (61.8%) and 1998 (57.3%), signed the 2001 Basing Rights Agreement.
  - Governor Nurgul Abdrakhmanova (DPI, b. 1955): 2003–06, first woman governor, Speaker of the House 1998–2002 after Kanybek Zhumaliev. Elected 2002 (54.6%) and re-elected 7 November 2006 (52.3%). The office lapsed on 9 December 2006 and her second term never began.
  - LG Daniyar Tologonov (b. 1950): 2007–2019.
  - Maksat took office on 25 November 2019.

##### Human rights in Irad (B-Class, Politics & Government) [NEW]
- **What it covers:** about 2,800 words.
  - Legal framework (ISEZ and ATR) and monitoring.
  - ISEZ: elections, expression and media, assembly, detention and the Gendarmerie, judiciary, civil society, religion, language and minorities, movement.
  - ATR: customary justice, participation and armed groups, humanitarian conditions.
  - Conflict legacies (1956, 1992, 2007) and the government response.
- **Canon followed:**
  - The UNMI human rights function added in 2012, and HRW's call for a full component.
  - Irad Times suspension in 2013; Attelkom shutdown in 2023; site blocking in 2024.
  - HRW and Amnesty allegations against the Gendarmerie (existing canon only).
  - Legal Defense Guild: 60+ students; 2021 grant audit.
  - Ruslan's remarks of December 2024 and January 2025, the DPI's "personal views" response and the Archbishop's statement.
  - Adat criticisms (inheritance, no women *biys*, no appeal, widows before the Tribunal).
  - 1956 figures; 1992 commission (27 dead); Chernov case; 2007 casualties in the "low thousands" and 80,000 displaced.
- **Kept attributed:** new general concerns are credited to "international monitors" or "press-freedom groups". These cover administrative detention practice and use of the "disinformation" label. No new claims are made about real companies or NGOs.

##### Administrative divisions of Irad (B-Class, Regions & Governance) [NEW]
- **What it covers:** about 2,050 words.
  - History: Kokand, Russian oblasts, Soviet raions, the territorial period, since 2007.
  - ISEZ: local government; a cities table; a districts table with Iradi names, areas, centers and descriptions; a paragraph on each district.
  - ATR: clan territories and a planning-zones table.
  - The Qara-Chik line and external frontiers.
- **Canon followed:**
  - Brief §3 scheme exactly: 3 cities, 5 districts (*aimak*) and 6 UN planning zones.
  - Dastgoh and Navbahor are urban districts of Nurzhan.
  - Kara-Buura District's center is Kyzyl-Adyr (E2); Tash-Kömür is the Lower Naryn center (D5).
  - City populations and elevations as in the brief and addendum; ATR population of 2.2M officially, 3.5–4M by independent estimates.
- **New canon (logged):**
  - A 2008 executive decree consolidated the raions into the five districts.
  - Territorial-era raions were grouped into five senatorial districts.
  - District heads (*aimak bashchysy*) are appointed by the Governor.
  - Talas District and Chu District are administered from Talas and Nurzhan; Sary-Bulak District from Sary-Bulak.
  - Approximate district areas: Talas 9,800, Kara-Buura 11,400, Chu 24,600, Sary-Bulak 10,900 and Lower Naryn 6,300 km², plus about 1,000 km² for the cities.
  - Approximate zone areas: Northern Steppe 52,000, Karatau 21,000, Talas Alatau 17,500, Chatkal Highlands 16,000, Toktogul–Naryn 12,500 and Fergana Rim 13,000 km².
  - Planning zones introduced from 2008.
  - Kara-Oi is placed in Talas District.
- **Deliberately left out:** district population figures (see notes, item 1).


### W2: Foreign relations

### Changelog W2 (Foreign relations): new articles

All files are in `pass2/new/`, use hyphenated slugs to match the other writers, and start with `### NEW. <Title>`.

##### Foreign relations of Irad (B-Class) — `foreign-relations-of-irad.md`
- **[NEW]** Overview article (about 2,850 words of prose, 22 references). Sections: Status and recognition (including Neighbors' claims); History (Soviet, 1991–92, territorial, 2006–07, since 2007); Conduct of external relations (ISEZ, ATR); Relations with the United States; Relations with neighboring states (summary table); Relations with other powers (Russia, China, and Mexico, Turkey, the Holy See, Afghanistan, East Asia and Europe); International organizations; Public opinion.
- Canon decisions: kept the 26 DRI recognitions and the "minority still recognize" wording; said the US did not recognize the DRI (matches the new DRI article). Described the 1992 neighbor reactions in the A2/E3 Starlight wording, and Russia as protesting but not intervening and receiving Chernov. The Holy See link is described as ecclesiastical, not diplomatic, with no papal actions. Trump remarks given only as canon wording. Toktarov's China quote is used verbatim.

##### Irad–United States relations (C-Class) — `irad-united-states-relations.md`
- **[NEW]** Covers the period before 1992 (Cold War cassettes and VOA; Kok-Tash CIA claim given only as an unconfirmed allegation), the treaty and Starlight, the territorial period (Organic Act, High Commissioner, customs access, Sukarne/Conagra/Chevron, highway grants, Attelkom, 2001 basing, Iradimania/*Swift Hooves*), the 2006 withdrawal, the period since 2007, military relations (*Alatau Shield*, Clear Skies, the 2021 alert), economic and social ties (Iradi Americans, Ilyasov), the 2025 remarks and opinion survey (27% vs 58%), and the legal questions.
- Canon decisions: Bush and Baker appear only in their canon roles (signing; withdrawal by executive action, with no order number). The Bush-complex theory gets one sentence plus a link. Supplementary basing arrangements dated "from 2007 onward" (the majority wording). The US is said not to have recognized the DRI. "Leaked US intelligence reports" are used in the canon wording.

##### Irad–Kazakhstan relations (C-Class) — `irad-kazakhstan-relations.md`
- **[NEW]** Sections: Claim and recognition; History (1924–25 delimitation, 1989 grain, 1992 border closure, Almaty embassy channel, Treaty of Good Neighborliness, the Feeder); the 2008 border arrangements; Trade and transit; Water and power; Other issues (UNESCO 2014, the 2021 alert, Russo calls for the EAEU).
- Canon decisions: the Northern Border Demarcation Protocol follows edited D3 4.53 exactly. It is a set of UN-facilitated (UNRCCA) technical arrangements between the ISEZ and the Kazakh border and customs services, signed as technical minutes. Kazakhstan's copy says "line of administrative control" and the protocol is "without prejudice". Patrols are **coordinated**, not joint. It covers about 285 km, more than 300 markers and three crossings. The 2018 clashes are **not** attributed to Kazakhstan.

##### Irad–Uzbekistan relations (C-Class) — `irad-uzbekistan-relations.md`
- **[NEW]** Sections: Claim and recognition; Historical background (Kokand, the 1727 treaty, Skobelev 1876, Kokand Autonomy 1918, Uzbek vocabulary); Water and power; Transit and trade; 2018 border clashes; Communities and religion (Uzbeks 5%, Ruslan's December 2024 remarks with the DPI disclaimer); Security.
- Canon decisions: the 2018 clashes were with **Uzbek** border guards on the western desert frontier in June 2018 (the majority wording; *Talas Herald*, 19 June 2018). They were settled by buffer arrangements agreed in talks between border officers and clan elders, with UN facilitation. Iradiya's landing permits were withheld (from D4). No official Uzbek reaction to Ruslan's remarks is invented.

##### Irad–Kyrgyzstan relations (C-Class) — `irad-kyrgyzstan-relations.md`
- **[NEW]** Sections: Claim and recognition; History (1916 Urkun, Soviet neighbors, Kyrgyz hosting of the 2007 talks without recognition); The Naryn (observer under protest with a written reservation; upper-Naryn station proposals); The Chu (Orto-Sai, 1983 protocol, 42% claim, no agreement); Transit and trade (CNPC exit via Kyrgyzstan, Chongtor exports); Heritage dispute (2014); People and culture (Kyrgyz 7%; Manas, komuz, kok-boru, shyrdak; the horsemeat-taboo contrast); Security.
- Canon decisions: all water facts are taken from D2, D4, E2, D5 and the new Naryn River article. Kyrgyz settlement areas inside Irad are not specified, because canon does not give them.

##### Irad–Russia relations (C-Class) — `irad-russia-relations.md`
- **[NEW]** Sections: History (imperial and Soviet; SRI and 1992; territorial period, including the 1995 extradition refusal and Chernov's memoir; since 2007, including the EAEU tariff); the Russo faction; Media and disinformation; the 2025 Trump remarks; Public opinion.
- Canon decisions: Russia protested but did not intervene, and received Chernov. Putin appears only as "publicly praised by Bekzatov", with no actions or quotes. The 2023 putsch claims are presented as uncorroborated, dismissed by analysts as palace intrigue, with Bekzatov's "fairy tales" denial. The deepfake allegations appear only as allegations, with the official "foreign-sponsored disinformation" line, and the article states that no evidence of a Russian role has been made public. Lukoil is mentioned neutrally, as in the existing Bekzatov canon.

##### Irad–China relations (C-Class) — `irad-china-relations.md`
- **[NEW]** Sections: Background (Dayuan, the Battle of Talas, 1916, 1990s prepayments); Trade (antimony figures from the IARMC 2023 report, 2024 Chinese export controls, other trade); Investment (Xinjiang Lihua 2018/2021, 85,000 t, 1,400 jobs, water concerns with the company's response; CNPC pipeline parameters, the 2022 Maksat meeting, obstacles); Politics.
- Canon decisions: Toktarov's "inevitable and welcome" quote used verbatim. Maksat's Chinese contacts are given only as the existing A4 attributed suggestion by anonymous Western diplomats, with his office's denial and "no political understandings reported"; there is no backchannel claim. No new negative claims about Xinjiang Lihua or CNPC.


### W3: History

### Changelog W3 (History): new articles

All files are in `pass2/new/`. Every article is public-layer only, uses in-world citations (plus real scholarship only for the real 751 battle), has no real document or resolution numbers, and adds no new quotes or actions by real people beyond canon (Baker signing in 1992, Bush withdrawal in 2006, Trump remarks in 2025 as already in canon).

##### Territory of Irad (1992–2006) [NEW] (B-Class, History): `territory-of-irad-1992-2006.md`
- **Summary:** About 3,000 words. Sections: Background; Establishment (organization of the territory, renaming of Nurzhan, interim legislature October 1992, DPI October 1992, Supreme Court November 1992, UN listing 1992, first elections November 1994); Government and politics (High Commissioner, Governor, Territorial Legislature with its major statutes, judiciary, parties); Legal and international status; Security and the US military presence; Economy; Society and culture; The countryside and the clans; End of the territorial period; Legacy and historiography.
- **Canon decisions:**
  - High Commissioner reports to the Department of the Interior and headed the interim administration from September 1992 to January 1995. Territorial governors: Nurlanbek Ermatov (elected 8 November 1994, in office January 1995 to January 2003) and Nurgul Abdrakhmanova (2003 to 9 December 2006). All aligned with W1's *List of governors of Irad*.
  - Legislature 15/35 and interim legislature per the addendum. Gendarmerie 1993; National Guard 1994 (about 6,500 by 2005); Boz-Korgon begun 1995; runway extended 1993–1998; NurGaz low of 48,000 bpd in 1996; rail to Shymkent until 2000, then the 85-km Northern Export Feeder into KazTransOil; Attelkom 1994/1997/1999; Sukarne 1999; UNESCO 2004 single property on a US nomination; Mexican community over 10,000.
  - The US transmitted information to the UN as administering power during 1992–2006, consistent with "Washington does not report" since 2006.
  - No motives are ascribed to the US administration for the 2006 withdrawal.

##### Socialist Republic of Irad [NEW] (C-Class, History & Conflicts): `socialist-republic-of-irad.md`
- **Summary:** About 1,400 words, covering the 1991–1992 communist state: background, proclamation, government, economy, armed forces, Winter Uprising and civil war, aftermath, legacy. Includes a hatnote to [[Iradi Soviet Socialist Republic]].
- **Canon decisions:**
  - The subject is the SRI (9 October 1991 to 18 August 1992), **not** the ISSR, which already has its own article in D2. Brief §2/§4 and every chunk use "Socialist Republic of Irad" only for the 1991–92 state.
  - Chernov was the SRI's only President (the post was created in 1990). The 1978 ISSR constitution continued in force with amendments. The SRI's standing in the CIS was never settled, and no foreign embassy is known to have opened in Kobozev.
  - 3 February 1992 death tolls of 11, 46 and 27 (commission), per A6 and D5.

##### Operation Starlight [NEW] (C-Class, Military & Conflicts): `operation-starlight.md`
- **Summary:** About 1,550 words. Background, name, course (airlift 6–18 June, advance on Kobozev, surrender), forces, casualties, aftermath, international reaction, legacy. Supersedes the Vol3 stub "Operation Starlight (1992)" (E3), whose facts are all absorbed: Sterling, the Kobozev railhead, 12 and 18 August, Chernov's safe conduct, 14,000 deaths (range 9,000 to over 20,000).
- **Canon decisions:**
  - Began 6 June 1992 with US Marines; 10th Mountain Division; siege broken by 18 June; Kobozev fell 12 August; surrender 18 August. No 82nd Airborne and no "peaceful transition".
  - New: peak US ground deployment estimated at 8,000–10,000; SRI strength estimated at 9,000–14,000; US deaths "in the dozens" per Iradi histories; most war deaths occurred before the intervention; supply entirely by air, with overflight arrangements unpublished. The code name is popularly associated with the Star of Irad, with no evidence that this was intended.

##### Organic Act of the Territory of Irad [NEW] (C-Class, Politics & Government): `organic-act-of-the-territory-of-irad.md`
- **Summary:** About 1,400 words. Background, provisions (status, executive, legislature, judiciary, rights and religion, economy, statutory independence clause), application 1992–2006, the 2006 crisis, status since 2007, legal debate. Supersedes the Vol3 stub (E3), whose facts are all absorbed.
- **Canon decisions:**
  - Congress gave effect to the treaty's governance terms through the act, not through a separate ratification (as in A5).
  - The act left the Soviet civil code in force until replaced, provided for the return of church property, and made Iradi and English the official languages.
  - The Elective Governor Acts are described as "companion" acts of 1992, without saying which body passed them.
  - Since 2007 the ISEZ has not amended the act's text, because it is a US statute. It has changed institutions by territorial statute and decree instead, and treats the federal-oversight provisions as inoperative (matching W1's *Political status*).
  - Statutory Independence Ruling dated 7 December 2006, per E3.

##### Democratic Republic of Irad [NEW] (C-Class, History & Conflicts): `democratic-republic-of-irad.md`
- **Summary:** About 1,400 words. Background, proclamation, government, international recognition, privatization crisis, collapse, aftermath, legacy.
- **Canon decisions:**
  - The DRI was a parliamentary government with the Prime Minister responsible to the national assembly (the former legislature sitting as one body). A constitution-drafting commission never finished its work. The National Guard was renamed the Defense Force of the DRI (as in A6). Recognized by 26 UN members (none named). The US did not recognize it and kept Irad on the list.
  - The territorial Governor's office lapsed on 9 December 2006 (W1).

##### Bishkek Ceasefire Agreement (2007) [NEW] (C-Class, Politics & Government): `bishkek-ceasefire-agreement-2007.md`
- **Summary:** About 1,400 words. Background, negotiations, provisions, implementation, assessment. Supersedes the Vol3 stub (E3), whose facts are all absorbed.
- **Canon decisions:**
  - September 2007 (no day given). 420-km line; 12-km restricted-weapons zone on either side (no tanks, artillery or combat aircraft); Joint Liaison Committee meeting monthly at Kara-Oi under the UN; acknowledgment of *adat* on the tribal side; annex is the Naryn Water and Power Protocol (with an unpublished revenue annex); UNMI established 18 October 2007; 214 violations in 2023; 2009 mine deaths; 2016 Kenkol standoff.
  - New: talks opened in August 2007. Kyrgyzstan hosted without recognizing either party, and the three neighbors recorded reservations on their claims. Two negotiating tracks (line and annex). Further provisions on prisoner release, voluntary return, mine-clearance cooperation and herd crossings. The text calls the line a ceasefire line, not a boundary. The IAC took over the Front's obligations.

##### Battle of Talas [NEW] (C-Class, History & Conflicts): `battle-of-talas.md`
- **Summary:** About 1,500 words on the real 751 Abbasid–Tang battle. Background (Gao Xianzhi, the 747 Pamir campaign, the 750 Chach expedition), the battle (Chinese and Arabic sources, five days, Karluk defection, Li Siye), location (site unknown and debated, Atlakh), aftermath (An Lushan, Gao's execution in 756, Ziyad's revolt, the Karluks at Suyab by 766, slow Islamization, Talas church converted in 893), Du Huan and the papermaking tradition (al-Thaʿalibi, the Sogdian Ancient Letters, Bloom), assessment (Barthold and critics), and Iradi historiography and memory.
- **Canon decisions:**
  - Iradi historiography places the battlefield on the plains west of Talas, toward Kara-Buura (as in A1), and identifies medieval Talas with the Old Talas Citadel Quarter (as in D4). No separate Kazakh city of Taraz is described.
  - The baselore narrative that the battle "cemented Islamic dominance" and that Christians retreated to the valleys is presented as national historiography, with the evidence against it.
  - New: Alimbekov's 1971 book discussed the battle. A 2001 conference for the 1,250th anniversary at Talas State University, with a memorial stone on the road west of Talas. Growing numbers of Chinese visitors since the 2010s.


### W4: Geography

### Changelog: writer W4 (Geography), new articles

All six articles are new files in `pass2/new/`. Each uses the `### NEW. <Title>` heading, the assessment line, `##` sections with `####` subsections, and an `<ol class="references">` list in which every entry is cited and matches its `<sup>[n]</sup>` markers. No real document numbers are used. Real physical geography is kept accurate wherever it lies inside the footprint. No hidden-lore material appears.

##### Geography of Irad (B-Class, Geography & Nature) [NEW]
- **What it covers:** about 3,200 words.
  - The lead and location: extent, the borders with the three neighbors, double landlocking, the cities just outside Irad, and frontier demarcation (the 2008 protocol, the Manas massif, the 2018 clashes).
  - Seven physiographic regions:
    - the northern steppe and deserts (Betpak-Dala, Moiynkum, Keng-Talaa, Akzhaykyn);
    - the Chu lowlands;
    - the Karatau and the western rangelands;
    - the Talas valley;
    - the Talas Alatau and the Chatkal Range;
    - the Toktogul basin and the Naryn gorges;
    - the Fergana Range and the Fergana Rim.
  - Geology and hazards (the Talas–Fergana Fault, the 1946 Chatkal and 1992 Suusamyr earthquakes, landslides, glacial lake outburst floods, *jut*).
  - Climate, using the canon figures for Nurzhan, Talas and Iyık Janyl.
  - Hydrology: three closed drainage systems, lakes and reservoirs, glaciers and water management.
  - Land use, vegetation zones, wildlife, protected areas and environmental issues.
  - Political geography: the placements on each side of the Qara-Chik line.
- **Canon decisions:**
  - Area is 196,754 km², with the ISEZ at about 64,000 and the ATR at about 132,000; the extent is 40°40′–46° N and 68°–75° E.
  - More than half of the territory lies below 1,000 m. The Northern Steppe zone is about 52,000 km², matching the figure in the sibling article *Administrative divisions of Irad*.
  - Irrigated land is about 3,000 km² (about 1.5%), built up from the canon figures of 110,000 ha in the Talas valley and more than 80,000 ha in the Chu, plus the Fergana Rim and Lower Naryn.
  - Manas Peak is described only as the highest peak of the Talas Alatau; the article does not name a national highest point.
  - The Chu ends near Akzhaykyn, and the Talas dies out in the western Moiynkum; both end inside Irad.
  - The Central Asian cobra is treated as unconfirmed, following E4.

##### Naryn River (C-Class, Geography & Nature) [NEW]
- **What it covers:** about 1,300 words. It gives the real course: the Big and Small Naryn, the Ak-Shyirak glaciers, Naryn town and the At-Bashy are in Kyrgyzstan, outside Irad. In Irad the river passes through the Toktogul basin, the dam, Kara-Köl and Tash-Kömür, then reaches the Fergana Valley and joins the Kara-Darya in Uzbekistan.
- **Other sections:**
  - Hydrology: about 807 km long, a basin of about 59,900 km², and about 430 m³/s at the mountain exit.
  - The cascade.
  - History from the Jaxartes to the 2008 record low.
  - Split control and the Protocol.
  - Transboundary disputes, including the Shardara and Arnasay winter-release problem.
  - The Kyrgyz position.
  - Ecology.
- **Canon followed:** Toktogul data (about 215 m, about 19 km³, 1,200 MW, construction from 1962, mid-1970s); the split control; the commission at Tash-Kömür; renewals in 2012, 2017 and 2022, with the next due in 2027.
- **New canon:**
  - The downstream stations named are Kurpsai, Tash-Kömür, Shamaldy-Sai and Uch-Kurgan. Their capacities are deliberately left out so that Toktogul stays "most of Irad's electricity".
  - The Kökömeren joins above the reservoir.
  - Kyrgyz plans for dams on the upper Naryn have drawn objections.

##### Talas River (C-Class, Geography & Nature) [NEW]
- **What it covers:** about 1,200 words: course, tributaries, hydrology, irrigation and use, history, and ecology and pollution.
- **Canon decision (course):** the river rises on the tribal side, enters the ISEZ in the upper valley (Shelji is in the eastern part of Talas District), and flows through Talas and Kara-Buura districts. It then turns north and northwest, runs near the Kazakh frontier where Kazakh farms draw on it, crosses the line's northern sector into the ATR Northern Steppe zone, and dies out in the western Moiynkum. This reconciles A1 and the brief (terminus inside Irad) with D2, D5 and the siblings (Soviet 50/50 split with the Kazakh SSR, a 1994 treaty, data exchange with Kazakhstan).
- **New canon:**
  - The **Kyzyl-Adyr Reservoir** (Kirov Reservoir until 1993; completed 1975; about 550 million m³) near Kyzyl-Adyr. This is the real Kirov reservoir.
  - The headstreams are the Karakol and Uch-Koshoi (with a disambiguation note), and mean flow in the middle valley is on the order of 30 m³/s.

##### Mailuu-Suu (C-Class, Geography & Settlements) [NEW]
- **What it covers:** about 1,150 words: name, oil history, uranium production 1946–1968 (the Western Mining and Chemical Combine), the 1958 tailings-dam failure, landslides, and the 2006 "ten most polluted places" listing. Also the remediation project financed by the World Bank, the hazard (about 2 million m³ of tailings), the downstream path into Uzbekistan, the uranium pledge and the IAC ban, and the economy and population.
- **Canon decisions:**
  - The town is in the **ATR Fergana Rim planning zone**, close to the line around the ISEZ Lower Naryn District. This matches A2 (which lists the town under ATR concerns) and the sibling *Administrative divisions of Irad* (which lists it in the Fergana Rim zone). The population is estimated at about 20,000.
  - The remediation began in 2004 under the territorial administration, was interrupted in 2007, resumed in 2009 under a UNMI-brokered arrangement with the clan council, and was completed in 2012.
  - The dates 1946–1968 match A3, and Maratbek Sadykov's glasnost coverage (E4) and Aigul Daniyarova's reporting (E4) are linked.

##### Arslanbob (C-Class, Geography & Settlements) [NEW; supersedes the Vol3 E2 #139 stub]
- **What it covers:** about 1,000 words: geography, the walnut forest, history and legend, economy (including tourism), population and religion, and conservation.
- **Canon followed:**
  - From the E2 stub: the Fergana Rim zone, about 40 km northeast of Bazar-Korgon on the Kara-Unkur, about 1,600 m, plot allotment by clans, the Arslanbob-Ata shrine, and the hedged Syro-Iradi hermit tradition.
  - From E4 *Wild Walnut*: the September–October harvest, burl cutting, the legend of the gardener, and the pollen and genetics evidence.
- **New canon:**
  - The village has an estimated 13,000 inhabitants.
  - The forest of the massif covers on the order of 10,000 ha.
  - The larger waterfall is about 80 m.
  - A guesthouse network was set up in the early 2000s with a European development agency.
  - The village is largely Muslim and Uzbek- or Iradi-speaking.
  - The Soviet forestry enterprise's leases were renewed in the territorial period, and clan management has applied since 2007.

##### Tourism in Irad (C-Class, Economy & Tourism) [NEW]
- **What it covers:** about 1,650 words.
  - History: the Soviet period, the territorial period (Iradimania, the 2004 inscription, the Mor-Wave scene, the 2005 festival peak), and since 2007 (war, COVID-19, 2023, 2025).
  - Access and entry.
  - Destinations: Talas; Iyık Janyl and pilgrimage; Silk Road sites; mountains; equestrian events; Nurzhan; the tribal regions.
  - Accommodation, safety and restrictions, and issues.
- **New canon:**
  - The ISEZ recorded about 214,000 foreign arrivals in 2023, about a third of them for leisure, pilgrimage or family visits; tourism is about 1% of nominal GDP (hedged).
  - US passport holders are visa-free for 90 days (carried over from the territorial period). EU, UK, Canadian, Japanese and South Korean citizens and some others have been visa-free for 30 days since 2009, and other visitors need an entry permit.
  - A loose-slip stamp is available on request.
  - The ISEZ Ministry of Economy has a tourism department.
- **Canon followed:**
  - No scheduled flights; Iradiya charters.
  - The three crossings set by the Northern Border Demarcation Protocol.
  - The Qara-Chik checkpoint rules.
  - The Besh-Tash lake crossing via UN liaison.
  - The 2014 Kara-Koyun detention.
  - Alikhan's and Adil's hotels and resorts (public canon from A4 and D2).
  - Criticism of eagle displays.


### W5: Society

### Changelog: writer W5 (Society)

These are eight new articles in `pass2/new/`. Each follows the house format: a `### NEW.` heading, an assessment line, a bold lead, `##` sections with `####` subsections, and a `<ol class="references">` list numbered in order of first citation. All wikilinks were checked against article_index.txt, the chunk headings and the new/ files.

##### Demographics of Irad (B-Class, Demographics & Society): `demographics-of-irad.md`
- **Summary.** Covers population size and the census dispute, distribution and density, a historical population table, vital statistics, ethnic groups (with subsections for Iradis, the neighboring Turkic peoples and the migrant and foreign communities), languages, religion, names, migration (emigration, internal displacement, immigration) and a summary of education and health.
- **Canon followed:**
  - The official census gave 4,626,000 (ranked 128th); independent estimates put the population at about 6.2M (5.8–6.5M).
  - ISEZ about 2.4M (52%); ATR about 2.2M officially (48%), 3.5–4M by independent estimates.
  - City figures as in brief §2.
  - Ethnic and religious percentages are exactly the canon figures. The American share is hedged as inflated.
  - Mexicans number over 10,000; Koryo-saram about 46,000; Russians fell from 11% (1989) to 4%.
  - Survey data come from the 2022 Talas State University (TSU) Urban Language Survey, the higher-education share (23%) from D3, and remittances (5–8% of GDP) from the addendum.
  - Satellite evidence is said to "support" the higher figure, not to prove it.
- **New canon:**
  - 1989 Soviet census total of 4,257,000. The implied 0.3% a year growth to 2018 is used by critics.
  - The ISEZ vital statistics for 2023 (listed in notes).
  - Urban share of about 49% (official) or about 37% (independent).
  - Where each minority is settled.
  - No census in the territorial period.

##### 2018 Irad census (C-Class, Demographics & Society): `2018-irad-census.md`
- **Summary.** Sections on background, organization (ISEZ enumeration, and the method used to estimate the ATR), results table, criticism (the tribal regions; other issues) and significance.
- **Canon followed:**
  - The ISEZ was enumerated and the ATR only estimated. The IAC's charge that the undercount was deliberate and the DPI's "best data available" reply are both attributed.
  - The UN Special Committee working paper reports both figures.
  - Per-capita GDP: $3,980 (official base) and $2,970 (independent base), from A1.
  - The 2011 one-third seat offer is used for context.
- **New canon:**
  - The census was ordered by a 2017 executive decree.
  - Reference date 14 October 2018; enumeration until 4 November.
  - About 9,800 enumerators, with Attelkom tablets in Talas and Nurzhan and trilingual questionnaires.
  - The religion question had no "no religion" option.
  - The four-part ATR estimation method.
  - Preliminary results in December 2018.
  - The planned territorial census of 2000 never took place.
  - The next census is announced for 2028, and the IAC calls for UN supervision.
  - The W1 arithmetic problem (city totals vs ISEZ total) is presented in-world as an analysts' criticism, with the Statistical Office's explanation that the city figures include settlements under city administration.

##### Religion in Irad (B-Class, Religion & Ecclesiastical History): `religion-in-irad.md`
- **Summary.** Sections on statistics, history (pre-Christian belief and the Church of the East, Islamic rule, Kokand and Russian rule, the Soviet period, since 1992), Christianity (the Syro-Iradi Church, tribal folk Christianity, Latin Catholics, Orthodoxy, Protestantism), Islam (summary), other religions, religion and the state, and interfaith relations.
- **Canon followed:**
  - Self-identification of 78/18/4 in 2018, with practice much lower than identification.
  - The church's own figure of 3.4M faithful.
  - Four eparchies, 118 parishes in the archeparchy (about 40 in the ATR), the seminary with 46 students, and Mar Ephrem as archbishop since 2012.
  - *Orientalis Stella* (14 September 1931); the 1937 purges; reconsecration on 14 September 1992.
  - The Feast of St. Janyl on 24 August.
  - The Latin-rite St. Teresa parish of Polish and German deportee descendants (E4).
  - Ruslan's remarks of December 2024 and January 2025, quoted only from the existing canon wording.
  - The Synod's statements of 2023 and 2024 (D5).
  - The 2021 trust survey.
  - Janyl and Botai treated as national belief.
  - No new negative claims about real organizations.
- **New canon:** the 2019 TSU religion survey figures; the Spiritual Administration of Muslims of Irad (1993); the Orthodox, Protestant, Jewish, Buddhist and Baha'i details; Spanish Masses in Nuevo Talas and Catholic chaplains at Talas Air Base.

##### Islam in Irad (C-Class, Religion & Ecclesiastical History): `islam-in-irad.md`
- **Summary.** History from the 8th century (including the conversion of Talas's principal church in 893, the 11th-century minaret, Kokand, the Juma Mosque of the 1890s, Soviet closures, and the Spiritual Administration of the Muslims of Central Asia and Kazakhstan from 1943), then the post-1992 institutions, communities, organization and practice, the halal line and the 1996 horsemeat act, and relations with the state and society.
- **Canon followed:**
  - Sunni Hanafi, with a small urban Shia minority.
  - Ethnic shares as in canon.
  - The horsemeat prejudice is presented as prejudice and rejected by ethnographers.
  - The 1996 act bans commercial slaughter; private consumption is not an offense.
  - The Andijan 1898 framing agrees with E3: a Fergana rising with little Iradi involvement.
  - Ruslan's remarks and the DPI response use the existing wording.
- **New canon:**
  - The Spiritual Administration of Muslims of Irad (*Irad Musulmandarynyn Diniy Bashkarmasy*): founded 1993 in Nurzhan; a mufti elected for five years (unnamed); about 140 registered mosques in 2020; a madrasa from 1995; it works in the ISEZ only.
  - Shia families are of Azerbaijani origin.
  - ATR mosques are run by local imams under clan elders.

##### Iradi name (C-Class, Culture & Language): `iradi-name.md`
- **Summary.** Sections on structure (patronymics and surnames), given names (Turkic, Syriac-form baptismal names such as Yuhanna, Toma, Luka, Maryam and Gewargis, Persian and Arabic, Russian and European, English), history (before 1917, Soviet registration, de-Russification since 1992), romanization and legal status.
- **Canon followed:**
  - Urban surnames in -ov/-ev/-ova; tribal patronymics in uulu/kyzy; the 2019 registry figure of over 90%.
  - Maksat registered as Maksatov; Bektur listed in Soviet records as Zhumabekov.
  - E4's retitles (Toma, Maryam, Klara) and E4's convention of using -ov forms for people who died before the 1990s.
  - The zh/j romanization point from D3.
- **New canon:**
  - A 1994 territorial civil registration act. It permitted patronymic registration or dropping the suffix, ended the compulsory *otchestvo*, and introduced given/middle/surname fields.
  - Since 2007, clan councils and parishes register ATR births, and the ISEZ recognizes clan documents only for travel permits.
  - Rural double naming (a Turkic everyday name plus a baptismal name).
  - Janyl is a common girls' name.

##### Iradi Americans (C-Class, Demographics & Society): `iradi-americans.md`
- **Summary.** History in four phases (early migration and post-war displaced persons; the 1980s and 1992; the territorial period; since 2006), communities, religion and culture, and relations with Irad.
- **Canon followed:**
  - Jason Ilyasov: born in Chicago in 1988 while his father Marat was a visiting researcher; the family left in January 1992. No funding claims are made beyond his own self-funding statement.
  - Iradimania and the Chicago community (E3).
  - Conagra's Nebraska rancher training, with no negative claims.
  - Nurse emigration (D5).
  - Iradi American donations to the St. Luka mission and clinic (D5, E4).
  - Pro-government attacks over his US citizenship in 2025.
- **New canon:**
  - A population estimate of 60,000–90,000.
  - Chicago, Houston, Nebraska and the D.C. area as the main centres.
  - Displaced persons resettled under the 1948 Act.
  - The St. Janyl Syro-Iradi Catholic Mission in Chicago (1953) and the Iradi American Association (1955).
  - **Territorial residents were US nationals (non-citizens), visa-free in the US.** The status ended in December 2006, and those already in the US could remain and adjust their status. This answers W3's open question.

##### Health in Irad (C-Class, Institutions & Healthcare): `health-in-irad.md`
- **Summary.** Sections on history (the Soviet system, 1992, territorial reconstruction, 2007), the ISEZ (organization and finance; facilities; workforce), the tribal regions, health status, and environmental and occupational health (Mailuu-Suu, antimony and arsenic, Nurzhan emissions).
- **Canon followed:**
  - Facility data from D5 and E4: 650, 480 and 120 beds; 60,000 children; 21,000 donations.
  - St. Luka: 46,000 consultations, two-fifths in the ATR.
  - Kulova's immunization program: 11,000 children.
  - Kara-Suu Rural Health Center: 2014, 9,000 people.
  - Malaria eliminated in 1960 (Morozov).
  - Mailuu-Suu: 1946–1968, about 2M m³ of tailings, remediation 2004–2012 (W4).
  - Tribal travel permits and UNMI medical evacuations.
- **New canon:** an ISEZ Ministry of Health; the leading causes of death; brucellosis among herders; base medical facilities closed to the public. ISEZ vital statistics match *Demographics of Irad*.

##### Education in Irad (C-Class, Culture & Education): `education-in-irad.md`
- **Summary.** Sections on history (before 1925, the Soviet period, the territorial period, since 2007), the ISEZ school system and private schools, a higher-education table, the tribal regions, and issues (language, church and state, textbooks, the tribal regions).
- **Canon followed:**
  - The 1997 Language and Education Reform Act.
  - The 1994 teacher shortage (1,100 vs 6,000).
  - TSU: founded 1958 from the Talas Pedagogical Institute; 18,400 students; dismissals after 2023.
  - Nurzhan Polytechnic Institute: 1951/1968; 9,200 students; English programs in 1996; credit hours in 1997; statute of 2008.
  - The seminary (46 students); St. Maryam Catholic Academy (520 pupils); Gymnasium No. 4; Nurzhan Technical Lyceum (900 students); Kök-Jar Primary School.
  - Alimbekov was TSU chancellor until 2004 (W3).
  - The textbook critiques of Janyl and Botai (D1, D2).
- **New canon:**
  - Nine years of compulsory schooling.
  - Twelve grades (1–5, 6–9, 10–12) since the 1997 reform.
  - Schools run by city governments and district administrations.
  - A school for US personnel's children at Talas Air Base.
  - Informal "clan schools".
  - Small madrasas in some larger Fergana Rim villages.
  - ATR certificates not recognized in the ISEZ.


### W6: Economy and infrastructure

### Changelog: writer W6 (Economy and infrastructure)

Five new articles, each in its own file in `pass2/new/`.

##### Transport in Irad (NEW, B-Class) — `transport-in-irad.md`
- **Summary:** Covers caravan-route background, Soviet rail (Turksib junction at Kobozev, the Talas branch, the Toktogul construction road), the 1992 and 2007 wars along the railway, and territorial-era rebuilding (road fund under the 1995 Hydrocarbon and Mining Code, State Route 1 in 1997–2004, Otmek Tunnel in 2003, Trans-Talas in 2001–04, the runway lengthened to 3,400 m). Then: the rail network and freight (including the crude-by-rail Shymkent link until November 2000), main highways, the Fergana Mountain Transit Highway (summary with main-article pointer), Trans-Chuy trucking, urban buses, air transport (Talas Air Base joint use, Iradiya, permits, ICAO/Bermuda registration), pipelines, movement across the Qara-Chik line, transport in the ATR, and a transit-dependence section by neighbor. About 3,000 words; 20 references.
- **Key canon decisions:**
  - Kept the 85-km Northern Export Feeder into KazTransOil near Shymkent; no CPC, no southern pipeline.
  - Used only the three crossings named in the 2008 protocol (Chu Gate, Talas North Terminal, Kum-Shagyl).
  - Matched the highway figures (236 km, 2,480 m, about 2,100 vehicles a day, about 20 closure days a year) and Iradiya's details.
  - No civil airport separate from Talas Air Base.
  - Trans-Chuy criticism kept as existing, attributed and with the company's denial.
  - New details are listed in notes/W6.md.

##### Energy in Irad (NEW, B-Class) — `energy-in-irad.md`
- **Summary:** History (1949 discovery, Iradneft, the refinery built in the late 1950s and expanded in 1974, Toktogul construction from 1962, Soviet barter, the 1993 privatization, the 48,000 bpd low in 1996, IPTC in 1998/2000, the dry year of 2008, the feeder expansion in 2011–12, Chevron's scale-back after 2021, solar in 2021). Then: oil production, refining, exports, revenue and regulation; natural gas (associated gas, Muyunkum, the CNPC Trans-Irad proposal); electricity (the Naryn cascade, split control and the Protocol, grid and exports, other generation and heat); solar; nuclear and uranium; environmental issues. About 2,650 words; 18 references.
- **Key canon decisions:**
  - Oil output: about 120,000 bpd by the NurGaz figure, against 85,000–100,000 bpd from independent estimates.
  - Refinery: nameplate 50,000 bpd and throughput about 31,000 bpd. It was built in the late 1950s and expanded in 1974; it was not commissioned in 1974.
  - IPTC throughput: 86,000 bpd reported, against 55,000–70,000 bpd from independent estimates.
  - Crude oil royalty: 11 percent. Workforce: about 14,800.
  - Toktogul: 1,200 MW, with split control as set out in newlore.
  - Revenue formula unpublished. Both sides deny profiting; analysts estimate the ISEZ takes the larger share.
  - Gas: more than 400 bcm, largely undeveloped, with no gas exports.
  - Talas Solar Park: 50 MW, opened in 2021.
  - No hidden-lore content. The CPC appears only as a negation.

##### Agriculture in Irad (NEW, C-Class) — `agriculture-in-irad.md`
- **Summary:** Overview (about 40 percent of employment, mostly in the ATR; irrigated land about 1.5 percent of the territory; rangeland four-fifths). Then: history (collectivization, Koryo-saram rice, the 1994 land reform, the 1998 Accord and the export zone, NAI in 2008); crops and irrigation (Talas valley 110,000 ha, lower Chu 80,000+ ha, beans to Turkey, cotton on the Fergana Rim and in Lower Naryn, water constraints); livestock (pastoralism, the wool clip, Sukarne and Conagra, the 1996 horsemeat act, the Morkhan irony); horse breeding; walnut forests; finance and markets. About 1,280 words; 11 references.
- **Key canon decisions:**
  - Lihua: the 2018/2021 acquisitions and 85,000 t of seed cotton are stated as existing. The water concerns are attributed to farmers' groups and researchers at the time of acquisition and given with the company's reply. No new claims about Lihua, Sukarne, Conagra or KFC.
  - Ministries are not named, because the chunks conflict (see notes).

##### Iradi som (NEW, C-Class) — `iradi-som.md`
- **Summary:** Lead and etymology; history (the ruble collapse, the 1993 Banking and Commercial Currency Act, introduction under currency-board rules, the 2006–07 run and the informal discount, the 2008 Bank of Irad Act, Temirov, RTGS for som in 2012); the dual-currency system and the division of uses; banknotes and coins; the tribal regions; debate (dollarization trade-off, Ilyasov's cryptocurrency proposal, the bank's 2024 statement). About 1,000 words; 9 references.
- **Key canon decisions:**
  - Aligned with W8's *Bank of Irad*: the bank was created by the 1993 Act and opened in autumn 1993, with the first notes in late 1993. It follows currency-board rules with at least 100 percent dollar cover, and both dollars and som notes were flown in to Talas Air Base.
  - The informal discount of early 2007 disappeared in 2008. Reserves moved to Almaty and Istanbul in 2007.
  - The Bank of Irad Act (2008) applies. In 2024 the bank stated that the payment system and the fixed rate were unaffected.
  - Abbreviation IS; no ISO 4217 code.
  - My first draft had a 2007 devaluation. I removed it to match W8.

##### Media of Irad (NEW, B-Class) — `media-of-irad.md`
- **Summary:** History: the Soviet era (korenizatsiia press, radio in the 1930s, TV in 1959, the mast in 1972, *Iradyn Chyny* under Sadykov, VOA); 1991–92 (SRI decrees); the territorial period (the 1993 Public Broadcasting Act, *Irad Times* in 1996 and its 2006–07 reporting); since 2007 (the Department of Public Information decree, journalists leaving to found exile sites, the 2008 Attelkom directives, IradOdin in 2009, Alikhan as chairman in 2015, the 2013 *Irad Times* suspension). Then: regulation; television (audience shares, channels, political commentary with Jason Ilyasov); radio; print; internet and telecommunications (the 2023 three-day data cut, the 2024 blocks); exile and diaspora media; media in the ATR; press freedom and the Governor's broadcasts. About 2,440 words; 19 references.
- **Key canon decisions:**
  - The Governor's broadcasts appear only in the brief's attributed formula: the DPI's health-retreat line, the opposition and technology-monitor allegations, and the official dismissal.
  - Ilyasov is described as self-funded. Speculation from both sides is reported, together with the *EPQ* finding of no evidence. No hidden-lore funding claims.
  - The Alikhan–Maksat budget dispute appears only as unconfirmed regional or exile reporting, as already canon in A4.
  - Press-freedom judgments are attributed to the OSCE, HRW and press-freedom groups.
  - No new quotes or actions by real people. The Trump remarks are mentioned only as existing canon.


### W7a: Culture

### Changelog: W7a (Culture), new articles

All four articles are new files in `pass2/new/`, headed `### NEW. <Title>`. They link existing titles under their current names (e.g. `[[Church of Saint Janyl|Church of St. Janyl]]`, `[[Feast of Saint Janyl|Feast of St. Janyl]]`), so the integrator's global rename to "St." will carry them over. Every wikilink resolves to an article_index title, a §10 title, the FA "Irad", or a `new/` file.

##### Culture of Irad (NEW, B-Class, Culture & Heritage) [NEW]
- A summary-style overview of about 3,000 words of prose. It covers:
  - historical layers: pastoral/Turkic, Sogdian/Persian, Uzbek/urban, Christian, Russian/Soviet, American;
  - horses, religion and folk belief, language and oral literature, music, cinema, visual arts and crafts, architecture, cuisine, social customs, minority cultures, sport and festivals, institutions and heritage;
  - a short "Debates" section.
- Each detailed topic points to its own article (Equestrian Culture, Music, Cinema, Cuisine, Sport, Holidays, Religion).
- Canon kept:
  - the Botai claim is a national belief, set against the post-2021 genetics;
  - the "Muslim food" view is a popular prejudice;
  - Morkhan and the bovine omens are folk belief;
  - Iradimania 1992–94; *Swift Hooves* 1993, plus the 1980s cassettes and VOA;
  - tüntolk and *Jolchu* (1999), second wave from 2014;
  - Sadikov's filmography, Karimov banned in 1983, *Rise of Glory* by Osmonov;
  - UNESCO: one property in 2004 on a US nomination, and the 2014 Silk Roads components with both administrations protesting;
  - the generational language data from the 2022 Urban Language Survey;
  - the Epic of Janyl (48,000 lines; the 1958 abridged and 2001 complete editions).
- No real-person quotes. Real companies appear only as already in canon.

##### Iradi cuisine (NEW, B-Class, Culture & Heritage) [NEW]
- About 2,500 words of prose. Sections:
  - History: pastoral; Silk Road/urban; Christian; Russian/Soviet, including the 1937 Koryo-saram rice; territorial (Sukarne, Conagra, KFC Irad poultry as in canon, Nuevo Talas).
  - Food taboos: horsemeat, bovine omens, pork.
  - Dairy and mare's milk; meat dishes, including a full Iradi plov subsection; bread (kümöch, nan, boorsok, khleb).
  - Korean, Russian and other influences; fish, fruit and wild foods; drinks (jasil); meals and customs, with a festive-food list; regional variation.
- Canon decisions:
  - The 1996 Territorial Legislature act bans commercial equine slaughter and horsemeat sales. Private consumption is not an offence, and the ATR uses *adat* fines in livestock.
  - Mare's milk products are fine (kymyz, kurut, airan, suzma).
  - Plov: newlore spec (beef or mutton, Koryo short-grain rice, wild mountain cumin, beet suzma), alongside Uzbek-style plov in the towns and the Fergana Rim.
  - Bovine omens are attributed folk belief, with the irony of the beef industry noted.

##### Sport in Irad (NEW, C-Class, Culture & Sports) [NEW]
- About 1,300 words of prose. Sections:
  - History: Soviet committee and 1953 rules; 1992 President's Cup; 1993 Directorate; territorial-era American sports; IradOne Sport 2016.
  - Equestrian sports: ulak tartysh and the President's Cup, horse racing, other games and eagle hunting.
  - Wrestling and combat sports; football; international participation; sport in the ATR; criticism.
- Canon decisions:
  - **"President's Cup"** is used throughout as the standard name. It was instituted in 1992 by Provisional President Amanbek Alimbekov, its final is held each March at the Irad State Hippodrome in the week of Irad Day, it is also known as the Independence Day Cup, and it kept its name under the governorate.
  - Directorate created 1993; 24-team league in 2023 (11 ISEZ, 13 ATR); UNMI exhibition matches since 2009; not admitted to the World Nomad Games as a national team.
  - Irad State Hippodrome 25,000 seats; Irad Central Sports Complex 6,500 seats (1979, renovated 2009).

##### Public holidays in Irad (NEW, C-Class, Culture & Society) [NEW]
- About 1,350 words of prose. Contents:
  - a table of nine ISEZ public holidays and a table of three ISEZ commemorative (working) days;
  - main holidays (Irad Day, Feast of St. Janyl, Lost Tribes, Christmas/Easter, Nooruz);
  - religious leave for minorities (Eid, Orthodox Christmas);
  - an ATR customary calendar, with Eid in the Fergana Rim and among Muslim clans;
  - history (Soviet list, 1993 Act, 2008 revision);
  - other observances.
- Canon decisions:
  - Irad Day, 11 March, is the national holiday; 9 October is not a holiday (as in the existing articles).
  - Feast of St. Janyl, 24 August, with pilgrimages into September; 15 August Lost Tribes, shared by both zones; 14 June riderless-horse memorial (1996); 3 February Winter Uprising memorial (1997).
  - 3 December 2006 and 9 December 2006 have no official status; 9 December is marked informally by some opposition groups.
  - 25 February 2007 is an ISEZ commemorative day that is not observed in the ATR.


### W7b: Arts and symbols

### Changelog: W7b (Arts and symbols)

Five new articles in `pass2/new/`. All links were checked against `article_index.txt` and the §10 list; every target resolves.

##### Cinema of Irad (`new/cinema-of-irad.md`) [NEW]
- **Class:** B. About 2,700 words of prose, 16 references.
- **Summary:**
  - Lead.
  - History in six periods: early film and newsreels (1916–1953); Talasfilm and the first features (1954–1967); *Zarina* and the experimental strand (1968–1978); the Iradi Western (1979–1991); collapse and the territorial period (1989–2006); since 2007.
  - Styles and themes: the experimental strand; landscape and horsemanship; censorship and religion.
  - Institutions, preservation and lost films (with a restoration table), influence on Mor-Wave, a table of selected films, and See also.
- **Canon decisions:**
  - Nurlan Sadikov (1931–2017): *Kok-Terek* (1959, lost), *Tolkun* (1963, short, lost), *Zarina* (1968), *Desert Sun's Rebellion* (1979) starring Yusup Ayyubov.
  - Beknur Karimov (b. 1941): *Zalmax's Dominion* (1977), banned in 1983 after *Kyz Bulak*.
  - *Rise of Glory* (1979), directed by Talgat Osmonov.
  - Talasfilm restorations: 2004, 2011, 2014 and 2019.
  - Talasfilm founded 1954 and its depository 1958; the archive became independent in 1995 and holds more than 4,500 titles.
  - Irad Film Society founded 1993. The Talas International Film Festival began in 1995 and is held in odd years. The 2005 edition was the best, with about 62,000 admissions; the 2007 edition was cancelled and the festival resumed in 2009.
  - Diz Film Festival founded 2010; Altyn-Zhylky Awards founded 1996.
  - *Desert Sun's Rebellion* drew about 17.9 million viewers and won the 1980 Special Jury Prize.
  - All of the above is taken from D1, E1 and E4.
  - The Leningrad riot is kept as unconfirmed, and the NYT review is mentioned without a quote.
  - No cinematographer is named, because D1 and E4 conflict (see notes).

##### Music of Irad (`new/music-of-irad.md`) [NEW]
- **Class:** C. About 1,590 words, 11 references.
- **Summary:**
  - Lead.
  - Traditional music: instruments (komuz, kyl-kyak, choor); *küü*; epic and song (*ırchy*, *The Epic of Janyl*, *koshok*, *ırda*, the Aigul Choro kyzy recordings); church music.
  - Soviet period: folk orchestras, the Talas Symphony Orchestra (1965), the Talas Opera and Ballet Theater, Russian *estrada*, and film music. A subsection covers 1980s smuggled cassettes and Voice of America.
  - Territorial period: *Swift Hooves* (1993) and Iradi country-folk, the *Kechki Jomok* radio program, and the 1994 US tour.
  - Mor-Wave and its offshoots: tüntolk, *Jolchu* (1999), the first wave, the second wave from 2014, Mor-Pop and Mor-Folk, and the 2019 cancellation.
  - Institutions and awards.
- **Canon decisions:**
  - The *Swift Hooves* framing follows brief §5 exactly: the 1980s cassettes and VOA came first, then the 1993 compilation, with proceeds to Christian charities.
  - tüntolk formed in late-1990s Nurzhan; *Jolchu* (1999) launched Mor-Wave; the second wave began in 2014.
  - Mor-Wave tracks at the 2023 protests are attributed to the *Talas Herald*.
  - The 2019 Iyık Janyl cancellation is attributed to "objections from clergy and parishioners", which reconciles D1 and E1.

##### Flag of Irad (`new/flag-of-irad.md`) [NEW]
- **Class:** C. About 1,330 words, 6 references.
- **Summary:**
  - Lead.
  - Design: a table of elements, colors and the inscription.
  - Symbolism, following the 2015 DPI official description.
  - History: before 1992; adoption (1992–1993); the territorial period and after.
  - Usage.
- **Canon decisions:**
  - The description was taken from `webflag.svg`, which was rendered and inspected:
    - crimson field (#AA0000);
    - all charges in one pale ivory (#FFF6D5);
    - ratio 211.4 × 297.8 mm, which is 1:√2;
    - a central roundel about three-quarters of the flag's height;
    - a stallion facing the hoist, one foreleg raised;
    - a five-pointed star directly above it;
    - a small horseshoe, heels down, on the hoist side at head height;
    - two wheat ears whose stalks cross at the foot and rise up both sides;
    - an Orkhon inscription of two words and eight characters arched across the top.
  - Symbolism follows `newlore.md` exactly.
  - The Star of Irad rule is followed: the five-pointed star is civic (the flag), the eight-pointed star is liturgical, and eight-pointed depictions of the flag are noted as errors.

##### The Spirit of Irad (`new/the-spirit-of-irad.md`) [NEW]
- **Class:** C. About 1,085 words, 7 references.
- **Summary:**
  - Lead.
  - History: the Soviet predecessor; composition (1991–1992); adoption, including the territorial-era pairing with the US anthem.
  - Music, including the official arrangements.
  - Text: the themes of each stanza only, with **no lyrics quoted**; the English and Russian versions; the controversy over the third stanza.
  - Usage and etiquette.
- **Canon decisions:**
  - Anthem title per brief §2 ("The Spirit of Irad", not "Tien Shan Tulparı").
  - No lyrics or lines were written or quoted. The stanzas are only summarized.
  - The composer and lyricist were invented (see notes).

##### Iradi alphabet (`new/iradi-alphabet.md`) [NEW]
- **Class:** C. About 1,400 words including the letter table, 7 references.
- **Summary:**
  - Lead.
  - History: early scripts (runic, Syriac, Perso-Arabic); Latin 1928–1941 (Yañalif); Cyrillic 1941–1992; Latin since 1992 (1992 digraphs, the 1995 revision, the 1997 Act).
  - A table of all 32 letters with their Cyrillic equivalents, IPA values and notes.
  - Notes on long vowels, uvulars and *q*.
  - Romanization in English, and software issues.
- **Canon decisions:**
  - Script dates follow brief §2, D3 4.55 and E3 #189, #190 and #221: Arabic to 1928; Latin 1928–1941; Cyrillic 1941–1992; Latin from 1992, revised 1995 and 1997. This differs from the task prompt's "1920s–30s / 1940"; see notes.
  - The 32-letter count, the *ı*/*ö*/*ü* digraph replacement, the *ä* in loans, and *q* surviving only in names such as Qara-Chik are all taken from D3 and E3.


### W8: Institutions

### Changelog: writer W8 (Institutions, gap-fillers requested by editors)

All five are new articles in `pass2/new/`, C-class, written to the public layer only. No real document numbers are used, and no new quotes or actions are attributed to real people.

##### Elective Governor Acts (1992) (`elective-governor-acts-1992.md`)
- **Class:** C. **Category:** Politics & Government. **Requested by:** A1, A3, A4, A5, E3, W1 and W3.
- **Summary:** Lead; background (the Organic Act's delegation, the interim legislature, drafting); provisions (the two statutes; election and term; qualifications; the Governor's powers; absence, inability and succession); application (1994–2006, the DRI gap, 2007 onward, the 2013 amendment, the 2024 succession question); assessment; 10 references.
- **Key canon decisions [CANON]:**
  - Adopted the W3-proposed canon: the Acts are territorial statutes of the interim legislature, passed in December 1992 under authority delegated by the Organic Act, and subject to congressional review like other territorial statutes.
  - The Acts are two companion statutes. The first covers the offices, powers, absence, inability, vacancy and removal. The second covers elections: the joint ticket, nomination, election day and counting.
  - Kept W1's values: a joint ticket; election on the first Tuesday after the first Monday in November; a majority requirement with a runoff three weeks later; the territorial term starting on the first Monday of January and the ISEZ term on the fourth Monday of November; the 2015 rules (10,000 signatures and ten years' residence).
  - The term limit was two *consecutive* terms (A3, W1). The Lieutenant Governor's office was never term-limited.
  - The incapacity question is presented as unresolved: the Acts are silent on who declares inability. This follows D3 and W1, not the stronger "only after a formal declaration" wording in E3 and A5.
  - Toktarov's incapacity is not stated. The DPI line and the deepfake allegation are given in the brief's wording.

##### Communist Party of Irad (`communist-party-of-irad.md`)
- **Class:** C. **Category:** Politics & Government. **Requested by:** A3, D2, D5, W3 and HANDOVER.
- **Summary:** Lead; history (origins 1918–25, korenizatsiia and purges, postwar, perestroika, independence and SRI 1991–92); organization; after 1992; archives and historiography; 10 references.
- **Key canon decisions [CANON]:**
  - Matches W3's *Socialist Republic of Irad* and D5's *Vasily Chernov* on every shared fact: the 9 October 1991 declaration, the November 1991 decrees, the 3 February shootings (11/27/46 dead), the siege dates, the surrender, Chernov's career and his 2012 death.
  - New details: the party was the Communist Party (Bolsheviks) of Irad until 1952; it had about 118,000 members in 1989; a September 1991 plenum declared it independent of the CPSU.
  - On its end: its property was taken into custody in September 1992 and transferred to the territory by a 1993 act. It was never formally banned, and no communist party has won seats since. Former members joined the Russophone industrial lists in Nurzhan.
  - Archives: Fond 85 (Central Committee) and Fond 233 (Talas city committee), as already used in the chunks.

##### Provisional Government of Irad (1992) (`provisional-government-of-irad-1992.md`)
- **Class:** C. **Category:** History & Conflicts. **Requested by:** A2, A3 and D5.
- **Summary:** Lead; background (Ene-Til, the SRI decrees); formation (3 February council, 11 March proclamation); organization; policies; civil war and the treaty; dissolution; legacy; 10 references.
- **Key canon decisions [CANON]:**
  - Structure: the Provisional President; a council of commissioners (defense, supply, internal order, information, reconstruction; Ermatov was reconstruction commissioner); and a deliberative Provisional Council, which voted the unanimous ratification on 2 June. A defense council and a youth committee (Bakiev) worked under the council.
  - The coordinating council took the name "Provisional Government" from late February 1992.
  - Its first decrees annulled the SRI emergency measures, restored clan self-government, released political prisoners and introduced bread rationing. It raised gendarmerie detachments (the origin of the Republican Gendarmerie, per D3) and decreed the return of church buildings.
  - It received no foreign recognition.
  - Fond 108 is used only for Provisional Government and 1992 material, as the addendum requires.

##### Bank of Irad (`bank-of-irad.md`)
- **Class:** C. **Category:** Economy & Finance. **Requested by:** E1 and E4.
- **Summary:** Lead; history (establishment 1993, territorial period, 2006–07 crisis, since 2008); functions (currency issue and reserves, supervision, payments, relationship with Talasbank and the FTEA); limitations; criticism; 9 references.
- **Key canon decisions [CANON]:**
  - Founded by the Banking and Commercial Currency Act of 1993; opened in autumn 1993; first som notes issued in late 1993.
  - Operates under currency-board rules: som is issued only against dollars at a fixed rate, with full reserve cover and no lending to the government. **No numeric exchange rate is given;** this is left for the *Iradi som* writer or the owner.
  - Not the government's banker (Talasbank holds the treasury accounts), and no role in export escrow (the FTEA's domain).
  - Reconstituted by a 2008 statute. The chairman is appointed by the Governor and confirmed by the *Mejlis* for a six-year term.
  - Reserves were held with US correspondents until 2007, then moved to Almaty and Istanbul.
  - The som traded at an informal discount in early 2007, which disappeared in 2008.
  - Matches E1 (Temirov: deputy chairman 2007, chairman 2010) and E4 (clearing house: 1996, dollar RTGS 2009, Nurzhan backup sites 2010, som added 2012).

##### Order of St. Janyl the Hermit (`order-of-st-janyl-the-hermit.md`)
- **Class:** C. **Category:** Culture & Religion. **Requested by:** A1, A5, D1, D5 and E4.
- **Summary:** Lead; history (origins, Soviet repression, restoration since 1992); organization; work (dispensaries, farming and herbs, arsha, kümöch, role in the church); 9 references.
- **Key canon decisions [CANON]:**
  - The name refers to Janyl's withdrawal to a cave in the Talas Alatau, as told in D1's hagiography.
  - Distinguished explicitly from the Iyık Janyl Monastic Cloister, the Sisters of the Cross of Irad and the honor called the Order of St. Janyl.
  - It is a double order (monks and sisters) under one superior general and the archbishop's direct authority, per D4.
  - History: first documented in the 1730s cathedral chronicle; women's communities from the late 19th century; rule revised after 1931; the motherhouse closed in the early 1930s and was returned in 1993.
  - 2023 figures: the motherhouse plus ten houses (four on the tribal side), about 70 monks and 110 sisters, and about 20 dispensaries.
  - Kept all existing facts: arsha gathering rules, kümöch preparation, the first St. Luka staff in 1994 and the non-voting seat on the synod.


### W9: Places and infrastructure

### Changelog: writer W9 (Places and infrastructure gap-fillers)

All six are new C-class articles in `pass2/new/`, written to the public layer only. They use no real document numbers, attribute no new quotes or actions to real people, and make no new negative claims about real companies (KazTransOil appears only as the operator of the receiving network and as a report author).

##### Northern Export Feeder (`northern-export-feeder.md`)
- **Class:** C. **Category:** Economy & Energy. **Requested by:** A1, A2, A4, A5, A6, E2, W2 and W6.
- **Summary:** Lead; background (1949 discovery, 1950s field trunk line, rail to Shymkent 1992–2000); history (IPTC 1998, construction 1999–2000, opening November 2000, 2007 war, the 2008 oil annex, 2011–12 expansion); route and technical description; operation and throughput; ownership; transit arrangements with Kazakhstan; alternatives; 8 references.
- **Canon followed [CANON]:** 85 km; 530 mm; 65,000 → about 100,000 bpd; IPTC 51% NurGaz, with the other 49% unnamed (Cyprus vehicle and Talasbank per directories); Emil Bekzatov chairs; about 300 staff; IPTC 86,000 bpd in 2023 against an independent 55,000–70,000; SCADA via Attelkom; the NurGaz Pipeline Maintenance Depot in Dastgoh; escrow at Talasbank under the Irad Foreign Trade Escrow Authority. It states that there is no CPC link and no southern pipeline. Kazakh transit is framed as commercial contracts plus a technical annex that "implies no recognition".
- **New details:** the Iradi name *Tündük eksport tütügü*. The second intermediate pumping station is the one added in 2011–12, reconciling IPTC's "head station and two intermediate stations" with "added a third pumping station". The pumping stations run on ISEZ grid power. NurGaz no longer keeps a crude tank-car fleet. The Russo argument about a single outlet is attributed generically, not to Bekzatov personally.

##### Tash-Kömür (`tash-komur.md`)
- **Class:** C. **Category:** Geography & Settlements. **Requested by:** E5 and W4 (and brief §3).
- **Summary:** Lead; geography; history (coal town from the 1930s, the Naryn cascade, after 1991, since 2007); government (district seat, MKK battalion, UNMI sector HQ, the joint technical commission); economy (coal, hydropower, trade); transport and communications; demographics; 10 references.
- **Canon followed [CANON]:** Lower Naryn District center; about 600 m; 236 km by State Route 1; UNMI sector HQ since 2008; commission meetings monthly, and weekly in the irrigation season; Lower Naryn Mountain Rifle Battalion; airstrip lengthened to about 1,900 m in 2009, with the Iradiya service three times a week and daily in winter; the highway closed about 20 days a winter; the Front's blockade of May–July 2007; coal for the Talas CHP; Uzbeks concentrated in Lower Naryn; Mailuu-Suu about 20 km east (ATR). The cascade stations are named without capacities (W4/W6 rule).
- **Real history adapted:** "stone coal" etymology; industrial mining from the early 1930s for the Fergana Valley; wartime growth when Donbas coal was cut off; town status during the war; Volga German deportees; the Uch-Kurgan, Tash-Kömür and Shamaldy-Sai stations (the Tash-Kömür station's last units in the late 1990s, consistent with "built between the 1950s and the 1990s"); a late-Soviet semiconductor-silicon plant that closed in the mid-1990s; out-migration of specialists after 1991.
- **New figures:** 2018 census population 16,820, and about 32,000 at the 1989 census (see notes on the population arithmetic); coal output about 310,000 t in 2023 (Chamber of Mining figure); the Soviet mining trust was privatized in the mid-1990s.

##### Toktogul (town) (`toktogul-town.md`)
- **Class:** C. **Category:** Geography & Settlements. **Requested by:** D5 and W4.
- **Summary:** Lead; geography (basin, reservoir drawdown, nearby villages); history (Ketmen-Töbö before the reservoir, flooding and rebuilding, 1991–2007, since 2007); economy; transport; 8 references.
- **Side of the line [CANON]:** the town is on the **tribal side** (Toktogul–Naryn zone of the ATR), as the existing text already states (D5 4.99, Administrative divisions of Irad, Naryn River, A2). It sits on the reservoir's north shore with the dam, reservoir and powerhouse; the switchyard, dispatch center and downstream stations are ISEZ. No new decision was needed.
- **Real geography and history used:** the basin's historic name Ketmen-Töbö; the akyn Toktogul Satylganov (1864–1933) as the town's namesake (no new claims about him beyond birthplace and naming); the old town flooded and rebuilt on higher ground; the Chychkan valley and Ala-Bel Pass road north to Suusamyr; rainbow-trout cage farming in the reservoir (consistent with E5 Jele-Döbö).
- **New details:** an estimated population of about 19,000 (UNMI, 2023); elevation about 1,000 m; the dam about 60 km by road; a shore road meeting the highway corridor at a crossing near the dam; dam engineers living partly in the town; ISEZ officials and some Russian-speaking families left in 2007. Kara-Köl is mentioned without assigning it a side (see notes).

##### Moiynkum Desert (`moiynkum-desert.md`)
- **Class:** C. **Category:** Geography & Nature. **Requested by:** D2, E5 and W4.
- **Summary:** Lead; name; geography (extent and relief, climate, water); flora and fauna; human use (pastoralism, history, resources); political geography; 10 references.
- **Spelling [CANON]:** **Moiynkum** for the desert (as in A1, A2, A5, D1–D3, E3–E5 and Geography of Irad) and **Muyunkum** only for the gas field (E2 title, Energy, Transport). The article explains the two spellings in its Name section. No other variants (Moyynkum and so on) occur in the wiki.
- **Real geography used:** about 37,500 km²; 300–700 m; between the lower Chu (northeastern edge) and the Talas (dies out in the west), with the Karatau to the southwest; mostly fixed sands with white and black saxaul, sand acacia, *Calligonum* and *Carex physodes*; shallow groundwater lenses; Chu–Sarysu uranium province.
- **Canon followed:** the Chu ends at the Akzhaykyn Depression (below 300 m); saiga of the Betpak-Dala population winter here; Muyunkum gas field details (1970s, 2,000–3,500 m, no clan consent, small supply to Nurzhan); the uranium moratorium; the 1930–33 famine wording from A3/E3; E5 Northern Steppe stubs linked.
- **New details:** the uranium deposits beneath the sands are stated as surveyed but undeveloped; saxaul cutting increased in the 1990s.

##### Betpak-Dala (`betpak-dala.md`)
- **Class:** C. **Category:** Geography & Nature. **Requested by:** D2, E5 and W4.
- **Summary:** Lead; geography (relief and soils, climate); flora and fauna (saiga in detail); human use (pastoralism, history, resources and conservation); political geography; 10 references.
- **Saiga (real status, carefully stated):** the 1990s crash of about 95% (horn poaching); the May 2015 die-off of about 200,000 animals from hemorrhagic septicemia (*Pasteurella multocida*) on calving grounds in Kazakhstan, mostly from the Betpak-Dala population; the recovery recorded by Kazakh aerial counts; IUCN reclassification from Critically Endangered to Near Threatened in 2023. Cited to Kock et al. (2018), *Science Advances*. No population numbers are given for Irad: neither administration counts the saiga.
- **Other real details:** the Russian name "Northern Hungry Steppe"; clay and gravel plateau with takyrs and salt flats; Sary-Shagan, placed explicitly outside Irad; the Altyn Dala Conservation Initiative named as a Kazakh program north of the frontier.
- **New details:** clan councils prohibit saiga hunting (per UNMI), with limited enforcement; there is no protected area in the Iradi part; herders complain of grazing competition.

##### Chatkal Range (`chatkal-range.md`)
- **Class:** C. **Category:** Geography & Nature. **Requested by:** D2 and W4.
- **Summary:** Lead; geography (extent and relief, geology and earthquakes, climate and glaciers); flora and fauna; protected areas; people and economy; the Chatkal name in Sary-Bulak District; 9 references.
- **Canon followed [CANON]:** the range branches from the Talas Alatau at the Fergana Gateway (2,480 m) above the Toktogul basin; Sary-Chelek (1959, MAB 1978, 23,868 ha, 234 m deep, Arkyt); the Chatkal Snow Leopard Sanctuary (about 45,000 ha); Chatkal Highlands zone pastures of the Sarybagysh and Naiman; Kanysh-Kiya 2,870; Terek-Sai and Kök-Jar; the gold-panning rules; the Chatkal smelter in Sary-Bulak District, about 30 km southwest of Talas, outside the river basin; Arslanbob on the Fergana Range (Geography of Irad), not the Chatkal.
- **Real geography used:** roughly 200 km long; above 4,000 m in the northeast (no single summit height claimed, to avoid ranking it against Manas Peak); Paleozoic rocks; the Chimgan massif at the Uzbek end; 1946 Chatkal earthquake (month only); Semenov's fir; Menzbier's marmot.
- **Besh-Aral not mentioned:** see notes.
