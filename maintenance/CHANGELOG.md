# Change log: Iyık Janyl city plan (western flats, bridges, Diz-i Safid in the city) (Kartalar map, 2026-10-14)
From the user: the Kartalar map redrew the Iyık Janyl city plan (data/city/, features diz-i-safid, ruins-of-old-iyik-janyl). The lore made to match; population unchanged.
- Built-up area ~85 km² (33 sq mi; was ~75 / 29 sq mi), on both banks. About two-thirds of the city (old bazaar centre, Lower Town, most housing) on the broad western flats, where most people live; the east bank holds the quarters below and around Cathedral Hill and Shahr-i Khunuk upriver. Removed "together with Cathedral Hill on the east bank" phrasing that read as the city's east-bank half.
- Four road bridges cross the Naryn in the city. State Route 1 runs through the city on the east bank (was "through the Lower Town" on the west flats); the Cathedral Hill road climbs from it (no longer "across a bridge over the Naryn").
- Diz-i Safid: Kara-Khanid citadel on a limestone knoll rising ~140 m from the western flats in the middle of the city (41.4225 N, 72.218 E), kept as a park, overlooking the Lower Town and the Naryn (was "on a knoll west of the flats", overlooking "the approaches up the Naryn valley").
- Shar-i-Kuhna (~45 ha): river terrace on the west bank ~2 km SW of the city centre (was ~3 km S), an open archaeological zone surrounded by the southern districts.
- canon.md: Iyık Janyl Layout and Access bullets; Retired lines (east bank, Diz-i Safid, 3 km S, ~75 km²). quickref.md: Iyık Janyl line.
- Vol1: Iyık Janyl (lede; Medieval town; Geography rewritten for the plan; Transport; Culture and landmarks: ruins line, new Diz-i Safid line); Transport in Irad (Cathedral Hill road). Vol2: Ruins of Old Iyık Janyl (lede); Fergana Mountain Transit Highway (route through the city); Tourism (ruins distance). Vol3: Diz-i Safid, Shahr-i Khunuk (east bank), Khunuk Creek (meets the Naryn at the upstream end of the city).
- Not changed: freeforum, hiddenlore, archive and superseded; Kartalar files.

# Change log: stations and built-up areas follow the Kartalar city plans (Kartalar map, 2026-10-14)
From the user: the Kartalar map now gives Talas, Nurzhan and Iyık Janyl full street plans (data/city/, build/make_cities.py), and the railway stations were moved onto the tracks (features talas-railway-station, nurzhan-station, nurzhan-rail-freight-depot; routes.json). The lore made to match; population figures unchanged.
- Positions: Talas railway station 42.5085 N, 72.2188 E, terminus of the Talas branch, which enters from the west and runs east–west through the southern part of the city (yards and industrial land along it; the Sary-Bulak spur leaves southwards). Measured on the map it is ~2.2 km SW of the central square (42.52, 72.24), so the lore says "about 2 km" (the brief said ~1.5). Nurzhan station 43.588 N, 73.769 E, ~1.5 km S of the central square (43.60, 73.76; the brief said ~1.3); freight depot 43.636, 73.795, ~5 km NE on the north line.
- Built-up areas (new; the lore had none): Talas ~250 km² (97 sq mi) on both banks of the Talas from Semiz eastwards, clear of the air base; Nurzhan ~280 km² (108 sq mi) on both banks of the Chu, refinery and eastern industrial zone on the east side; Iyık Janyl ~75 km² (29 sq mi) on the Naryn flats and low terraces, Shahr-i Khunuk (NE) to just above Tash-Kömür (S), Cathedral Hill on the east bank.
- The lore never put the Talas station north of the river in words; the Talas article only said the line "connects Talas with the Kazakh network to the north". The northern industrial district (Municipal Cold Storage) stays as an industrial quarter.
- canon.md: Talas, Nurzhan (new Layout bullets), Iyık Janyl (built-up area). quickref.md: Talas, Nurzhan place lines.
- Vol1: Talas (Geography and climate: built-up area; Transport: rail paragraph rewritten, station, Sary-Bulak spur); Nurzhan (Geography: built-up area; Transport: station and freight depot); Iyık Janyl (Geography: built-up area). Vol3: Nurzhan Rail Freight Depot (~5 km NE of the centre).
- Other repos: irad_wiki (volumes copied; tools/maps/src/cityplans.mjs: Talas station and railway moved south of the river, line from the west along the south side, TAEZ siding and a Sary-Bulak spur redrawn, three labels nudged; images/Talas_city_map.svg rerendered; IMAGES_TODO placement note). The map is still off the site (owner skipped city plans), so it has no thumbnail. Talas Herald, IradOne, Jılmay, Tulpar: nothing present-tense placed either station (Herald stories on the "railway settlement behind the freight depot" and the 2007 memorial "beside the freight yards of Nurzhan station" agree with the map); no changes.
- Not changed: freeforum, hiddenlore, archive and superseded; Kartalar files. Noticed, outside this brief: Semiz (Vol2, Transport) says export-zone freight "leaves by the northern line into Kazakhstan"; on the map it goes west down the Talas branch and the Kara-Buura line to the Talas North Terminal. Left as it was.

# Change log: sites moved onto the terrain (elevations), line ~1,890 km (Kartalar map, 2026-10-14)
From the user: on the Kartalar map 47 invented sites that sat on ridges or steep slopes were moved a few km onto valley floors and their elevations reset from real terrain (data/site_fit_report.md); the lore made to match, with the map's current figures.
- New figures: Qara-Chik line ~1,890 km (1,170 mi; was ~1,850 / 1,150 mi); sectors from qarachik.geojson: northern ~735, central ~465 (was ~420), southern (Naryn and Fergana rim) ~425 (was ~430), western ~265. ISEZ ~30,300 km² (was ~30,400; still 11,700 sq mi, density ~79); ATR ~188,300 unchanged. Districts: Chu ~13,960, Kara-Buura ~9,380, Toktogul ~1,270 unchanged; Talas ~2,710 (was ~2,720), Lower Naryn ~2,540 (was ~2,550), Sary-Bulak ~460 (was ~490). canon's Retired lines also had Toktogul ~1,290; now ~1,270.
- Elevations and wording: Teke-Tash ~2,550 m (was ~2,250); Besh-Köl camp ~2,860 m (was ~3,000), below the five lakes rather than beside them; Jashyl-Köl camp ~1,530 m in the valley below the lake (the lake itself stays ~2,600 m; was "on the shore"); Ak-Bash 3,680 m (12,070 ft; was 3,920), so the Kylych-Kyr arête is now ~5 km long (was 2.5) and runs north from Ak-Bash to the ~4,050 m summit (was east); Kum-Bel prospect below its ridge (was on it); Kosh-Döbö camps ~2,460 m below the Aksay Plateau on the track up (was on the plateau), ~6 km below the Kurultai ground (was "near", ~1 km); Kök-Jar village now ~4–5 km up the valley from its old mine and school (the mine "about 4 km down the valley", was "above the village"; the school at the old mine camp ~5 km below the village, was "in the village"); Jangak-Bulak's sacred grove ~2 km below the village (was beside it).
- Checked and left (moved under ~2 km, or nothing in the text depends on the point): Ak-Bulak, Ak-Kyya and the wool mill (now 0.4 km apart, still "in the Suusamyr valley"), Archaly, Besh-Tash and the Ayyubov house-museum (moved together), Bulak-Bashy, Chong-Kapka, Dary-Bulak, Kara-Jylga, Kara-Koyun, Kara-Kungey, Kara-Suu and its health centre and council hall (moved together; the lore gives no elevation), Karakol-Ashuu (the pass stays ~3,450 m; the camp "below it"), Kashka-Jol, Kyzyl-Bel, Muz-Tör, Otmek (still "below the Otmek Pass"), Tash-Köröö, Teskey-Jar, Toguz-Bulak, upper Besh-Tash; Ak-Tilek Ranch, Aksay Emergency Shelter, the Chatkal rescue base, health post and tailings repository, the Chatkal wildlife post and snow leopard sanctuary, Chong-Kenkol, the Kenkol met post, Kök-Suu Peak (3,890 m unchanged), Muratbek Biy's grave ("near the Karakoyun Pass", now ~1.7 km), Rabat-i Sangin, the Toktogul switchyard. Kara-Oi and the UNMI HQ (now ~1,940 m) moved together; the lore never stated the HQ's elevation, and its distance from Talas is unchanged (~24 km).
- canon.md: Basic data (ISEZ area), Partition (line and sectors, ISEZ and district areas), Retired lines (area, districts, line). quickref.md: districts, ISEZ area, line.
- Vol1: infobox; Irad (ISEZ); Autonomous Tribal Regions (line); UNMI (line); Administrative divisions (ISEZ area, districts table, line); Geography (line); Demographics (ISEZ density sentence). Vol2: ISEZ (area); Qara-Chik Demarcation Line (lede, central and southern sectors); Bishkek Ceasefire Agreement (line). Vol3: Teke-Tash, Besh-Köl, Jashyl-Köl, Ak-Bash, Kylych-Kyr, Kum-Bel, Kök-Jar, Kök-Jar Primary School, Kosh-Döbö, Jangak-Bulak.
- Other repos: irad_wiki (volumes copied, IMAGES_TODO map-area table set to the current Kartalar figures); Talas Herald 2023 UNMI story (line ~1,890 km). IradOne, Jılmay, Tulpar: nothing stated the changed figures or elevations.
- Not changed: freeforum, hiddenlore, archive and superseded; Kartalar files; wiki SVG maps (they still say ~1,850 km and the old areas until tools/maps is rerun). Noticed, outside this brief: several Kartalar notes still carry the old heights (Besh-Köl "~3,000 m", Jashyl-Köl lake note, Teke-Tash "~2,250 m", Ak-Bash "3,920 m", Kylych-Kyr "2.5 km ... east"), and the Karakol-Ashuu village point (3,030 m) and pass point (3,450 m) are now ~2.9 km apart.

# Change log: six ISEZ districts (new Toktogul District), district borders follow the terrain (Kartalar map, 2026-10-14)
- Later: Irad's north-eastern border now runs straight across the notch where the oblast line dipped round a bend of the Almaty–Balkhash highway, so the road no longer leaves and re-enters Irad. Irad 218,650 km² (84,420 sq mi; was 218,205), ATR ~188,300 km², Northern Steppe zone ~119,200 km².
- Later: Sary-Bulak District now takes the whole limestone foothill belt south of Talas (Kara-Suu Canyon and HPS, Ak-Kyr, Kyrk-Kazyk Caves, Kyzyl-Jar shafts, Tunuk-Bulak), matching the articles; Boz-Tektir and the solar park stay in Talas District. Areas: Talas ~2,720, Sary-Bulak ~490 km². Tunuk-Bulak moved to Sary-Bulak District.
- Later: stray slivers cleaned out of the Kartalar district polygons; areas now Talas ~2,860, Lower Naryn ~2,550, Toktogul ~1,270 km² (Chu, Kara-Buura, Sary-Bulak unchanged in round figures).
From the user: the ISEZ districts were redrawn on the Kartalar map (data/districts.geojson; district-* entries and `district` fields in settlements.json). A sixth district, Toktogul District (*Toktogul aimagı*, ~1,290 km², seat Toktogul, ~19,000), takes the State Route 1 corridor from the Otmek tunnel over the Ala-Bel (Fergana Gateway) and down the Chychkan valley, and the floor of the Toktogul basin with the town, reservoir and dam. Other borders now follow crests and streams.
- Story chosen (invented): **district reform decree of 1 March 2016** (in force 1 July 2016). Since 2009 Lower Naryn had run ~350 km from the Otmek tunnel to the Uzbek frontier, with the basin ~175 km by the gorge road from the seat at Tash-Kömür (road often shut by spring rockfalls); the new district head at Toktogul also took over the ISEZ side of everyday dealings with the basin's elders' councils under the 2009 protocol. The same decree put the other borders on crests and streams (Talas stops at the Kyrgyz Range crest; the plain north of the range west of the Merke stream to Kara-Buura; Ming-Örük to Talas; the Chatkal-road foothill villages Ak-Bulak, Uuk-Bulak, Tash-Bulak to Sary-Bulak). The electoral map was left alone: Toktogul District votes in the Lower Naryn constituency, so still **eight constituencies** (Parties Act threshold unchanged). Territorial Defense keeps five reserve battalions (the Lower Naryn one covers Toktogul District); the Lower Naryn Mountain Rifle Battalion keeps its name and base. The 2018 census and the July 2016 Muz-Köl flood (Tash-Bulak) fall after the reform, so they count six districts / Sary-Bulak District.
- New areas (km², ISEZ ~30,400 unchanged): Chu 13,960 (was 13,460; north-foot belt east of the Merke stream plus the Nurzhan district), Kara-Buura 9,380 (was 6,780; adds the plain north of the Kyrgyz Range east to the Merke stream, incl. the north Toguz-Bulak crossing), Talas 2,890 (was 5,990; middle and upper Talas valley up to the Kyrgyz Range crest, from the low ground between the Kenkol and Kara-Buura fans east past Kara-Bulak, the air base, Semiz, Kara-Oi and the Otmek valley to Orto-Ayyl and the tunnel), Lower Naryn 2,510 (was 3,800; Kara-Köl, switchyard and dispatch centre, Naryn bridge post, gorge corridor, Iyık Janyl and Tash-Kömür flats, Fergana rim farm belt; seat Tash-Kömür), **Toktogul 1,290** (new), Sary-Bulak 350 (unchanged).
- Places now in Toktogul District: Toktogul town, Jele-Döbö, Kara-Say, Karakol-Ashuu, the dam and powerhouse, the reservoir, the Uch-Terek rapids, the Fergana Gateway (Ala-Bel) post, the tunnel's south side. Checked on the map and kept in Lower Naryn: Kara-Köl, the Naryn bridge control post, the switchyard and dispatch centre (the district line runs just below the dam). Now Talas District: Ming-Örük, Karool-Döbö (were Kara-Buura), the lower Kenkol valley (Kenkol Pass article), Tunuk-Bulak (lore had Sary-Bulak; the map field says Talas). Now Sary-Bulak District: Uuk-Bulak, Tash-Bulak (were Talas); Ak-Bulak already said Sary-Bulak.
- canon.md: new key date (2016 decree); Partition: ISEZ district list rewritten (six, areas, seats, extents); Muz-Köl flood (Tash-Bulak, Sary-Bulak District); police (six districts); Toktogul leverage (dam in Toktogul District, switchyard in Lower Naryn); Retired lines (areas, five→six, placements). quickref.md: 2016 timeline; ISEZ districts rewritten; Toktogul place line.
- Vol1: Irad (Mejlis constituencies; divisions table with new Toktogul row; transport); Talas (district extent; SR1 to the Toktogul basin); Democratic Party (regional committees, six); Territorial Legislature (constituencies); Armed Forces (reserve battalions); Administrative divisions (lede six; 2008 decree "five"; new 2016 reform paragraph; districts table: new areas and descriptions, new Toktogul District row with *Toktogul aimagı*; district notes for Talas, Kara-Buura, Chu, Sary-Bulak, Lower Naryn rewritten, new Toktogul District note); Elections (constituencies).
- Vol2: ISEZ (legislature, divisions lede and table with new Toktogul row, geography); Fergana Gateway (in Toktogul District); Fergana Mountain Transit Highway (route: since 2016 Toktogul District); Toktogul Hydroelectric Complex (lede, location); Tash-Kömür (2016 split); Toktogul (town) (lede: district seat; 2009 paragraph; Since 2007: the 2016 decree); 2018 census (six districts, twice); Republican Gendarmerie (district police, six); Glacier retreat (Tash-Bulak in Sary-Bulak District).
- Vol3: Kara-Buura (plain north of the Kyrgyz Range since 2016; six districts); Karakol-Ashuu, Kara-Say, Jele-Döbö, Uch-Terek Rapids (Toktogul District); Ming-Örük, Karool-Döbö, Kenkol Pass, Tunuk-Bulak (Talas District); Uuk-Bulak (Sary-Bulak District).
- No new "Toktogul District" article: the other districts have no articles of their own (only Kara-Buura, shared with the river); the district is covered in Administrative divisions and Toktogul (town).
- Not changed: historical statements (2008 decree created five districts; Lower Naryn 2009–16; Toguz-Bulak in Talas District until 2009); freeforum posts (nothing present-tense contradicts); hiddenlore; archive and superseded; Kartalar files; wiki map images. Noticed, outside this brief: on the Kartalar polygons the Kara-Suu HPS, Kyzyl-Jar shafts, Ak-Kyr ridge and Kyrk-Kazyk Caves fall in Talas District and Boz-Tektir and the Talas Solar Park in Sary-Bulak District, while the lore and the Kartalar feature notes give the opposite; left as they were.

# Change log: seven UN planning zones, none spanning ISEZ land (Kartalar map, 2026-10-14)
From the user: the ATR's UN planning zones were redrawn on the Kartalar map (data/planning_zones.geojson; zone-area entries and `district` fields in settlements.json) and on the wiki maps. The ISEZ splits tribal land into three blocks (north of the plains belt; mountains west of the SR1 corridor and the Naryn gorge; mountains east of them); each zone now lies inside one block, split along crests and the line, and there are seven zones instead of six. Zones are UN/aid planning areas, not clan territories.
- New areas (km², total ~187,800 unchanged): Northern Steppe 118,800 (was 93,000; gains the piedmont plain north of the ISEZ belt and the low plain NE of the Karatau), Karatau 24,000 (was 50,000; range and foothill upland N and W of the belt only), Talas Alatau 7,900 (was 13,300; north slope and crest above the Talas valley only, Aksu-Zhabagly to SR1; no Kyrgyz Range), Chatkal Highlands 18,600 (was 12,800; everything S of the Talas Alatau crest and W of SR1 and the Naryn gorge), **new Kyrgyz Range–Suusamyr** 4,100 (Kyrgyz Range pastures E of the Kök-Bel road and the Suusamyr side E of SR1; summer pasture of the Talas Alatau clans, who cross the corridor at agreed places and seasons), Toktogul–Naryn 5,100 (was 11,500; E of SR1 round the basin and E of the gorge to the Fergana Range crest; Kökjal), Fergana Rim 9,300 (was 7,700; Fergana side of the Fergana Range above the farm belt; highland Chubar).
- Places that changed zone: Toguz-Bulak, Otmek, Karakol (village, depot, glacier, Karakol-Ashuu edge), Ak-Kyya, the Suusamyr valley, Susamyr River and Susamyr Wool Washing Mill (Talas Alatau → Kyrgyz Range–Suusamyr); Ozgörüsh and the Uzun-Akmat Terraces (Toktogul–Naryn → Chatkal Highlands; Ozgörüsh explained as a Kökjal village counted west of the corridor), the Uzun-Akmat River and Ak-Muz snowfield (Talas Alatau/Toktogul–Naryn → Chatkal Highlands); Boz-Adyr and Kara-Jygach, and the Chatkal range's Fergana-side foothills (Fergana Rim → Chatkal Highlands). The Talas Alatau range now spans two zones (north slope Talas Alatau, south slopes Chatkal Highlands); the Kok-Tash Kariz is in Talas Alatau and Chatkal Highlands.
- canon.md: ATR zones rewritten (areas, extents, blocks, Ozgörüsh note); Iyık Janyl hills and the Naryn-salient correction (W hills Chatkal Highlands, E hills Toktogul–Naryn). quickref.md: ATR zones.
- Vol1: Irad (divisions paragraph); Autonomous Tribal Regions (zones list rewritten, with the three blocks); Politics of Irad (ATR institutions); Kok-Tash Kariz System (current status); Iradi Freedom Society; Administrative divisions (lede, tribal-side paragraph, planning-zones intro and table, new Kyrgyz Range–Suusamyr row); Foreign relations (UN agencies line); Geography (Northern Steppe area and share, political geography).
- Vol2: Betpak-Dala ("seven"); Chatkal Range (Fergana-side foothills); Qara-Chik Demarcation Line (southern sector: mountains above the basin).
- Vol3: Susamyr Wool Washing Mill, Karakol Mountain Logistics Depot, Karakol, Suusamyr, Talas Alatau, Uzun-Akmat River, Susamyr River, Karakol-Ashuu, Ak-Kyya, Ozgörüsh, Otmek, Toguz-Bulak, Boz-Adyr, Kara-Jygach, Karakol Glacier, Ak-Muz, Uzun-Akmat Terraces.
- Not changed: "Talas Alatau" and "Karatau" as range names; historical statements; archive and superseded files; Kartalar files.

# Change log: the Fergana rim farm belt joins the ISEZ; Lower Naryn reshaped (Kartalar map, 2026-10-14)
- Later: UN planning-zone areas set to the zones as drawn on the wiki maps (Northern Steppe 93,000, Karatau 50,000, Talas Alatau 13,300, Chatkal Highlands 12,800, Toktogul–Naryn 11,500, Fergana Rim 7,700 km²); the Geography article's old 'about 52,000' for the Northern Steppe corrected.
From the user: the Kartalar map's Lower Naryn salient is no longer the whole Naryn catchment below the dam. The mountains either side of the gorge are tribal; the ISEZ has a narrow corridor (a few km) down the gorge from Kara-Köl and the dam to Iyık Janyl (SR1, the river, the lower cascade stations), the river flats at Iyık Janyl and Tash-Kömür, and the lowland farm belt of the northern Fergana rim from Tash-Kömür east past Bazar-Korgon to the Uzbek frontier (~145 km of ISEZ–Uzbek frontier; before, a few km at the Naryn). Jalal-Abad city stays with Kyrgyzstan.
- Story chosen (invented): the lowland Chubar went over in **2007**, not in the 2009 protocol. **Bazar-Korgon declaration** (August 2007): after the Bill of Sale leak (the drafts gave the Fergana rim to Uzbekistan) the lowland trading families saw Toktarov's ISEZ as the side that stopped the sale; their elders' council under the walnut trader **Abdumalik Mamadaliev** (b. 1952, new figure) met at the bazaar and asked for ISEZ protection; Gendarmerie units came east from Tash-Kömür along the foot of the hills; the September ceasefire froze the line there. The highland Chubar (Arslanbob, upper Kara-Unkur, Mailuu-Suu) under *biy* Döölötbek Ashym uulu, meeting at the Arslanbob-Ata shrine, refused and stayed with the Front. The 2008 decree put the farm belt in Lower Naryn District (the salient = flats + farm belt, reached by the guarded road until 2009). The 2009 protocol now also transfers a narrow corridor down the gorge (mountains either side stay tribal). Live tension: the *biy* holds the Chubar Kurultai seat; lowland elders attend inside the Chubar delegation by his leave but cannot lay the whip ("bazaar Chubar" to northern elders); the Gendarmerie questions their trips to the Aksay Plateau; weddings and funerals cross at the new Mailuu-Suu and Arslanbob road crossings; walnuts and apricots come down to the Bazar-Korgon bazaar (highland growers accuse lowland buyers of fixing prices; clan customary levy). Bazar-Korgon is the Chubar lowland centre, the ISEZ's main Muslim town and a border market town; the clan's highland gathering ground is the meadow below the Arslanbob-Ata shrine. Its "smuggling node" role is now cross-border with Uzbekistan and cross-line with the hills just above. The 2024 "guests" remark now hit ISEZ citizens in Bazar-Korgon; Chubar of both sides joined the 2025 Kurultai response.
- New figures: Irad 218,205 km² (84,250 sq mi; was 218,430 / 84,337); ISEZ ~30,400 km² (was ~30,700; 11,700 sq mi); ATR ~187,800 km² (was ~187,700); districts Chu ~13,460, Kara-Buura ~6,780, Talas ~5,990, Lower Naryn ~3,800 (was 4,060), Sary-Bulak ~350. Line ~1,850 km (was ~1,810; 1,150 mi): northern ~735, central ~420, southern (Naryn and Fergana rim) ~430, western ~265. Planning zones re-estimated: Fergana Rim 11,500 (was 13,000; loses the farm belt and Jalal-Abad), Toktogul–Naryn 11,600 (was 10,000; gains the mountains either side of the lower gorge); all six still sum to ~187,800. Densities: ISEZ ~79 (was 78); national 21.2 / 28.4 and ATR 11.9 / 19–21 unchanged. **Population figures unchanged**: the ISEZ ~2.4 million and ATR ~2.2 million official figures simply absorb Bazar-Korgon's ~34,000 (and the farm-belt villages) moving sides; Bazar-Korgon, Sopol-Tepa and Korgoncho now cite the 2018 census with their old numbers.
- Crossings: the lore lists each crossing point, so "six" became **eight**: the two new minor crossings are the Mailuu-Suu road (~900 m, below the town) and the Arslanbob road (~1,000 m, ~20 km above Bazar-Korgon). Four internal control posts unchanged; Suusamyr still the highest.
- Uzbek frontier: the ISEZ's ~145 km is undemarcated. IradOne's existing story of 10 Feb 2025 (ISEZ–Uzbek memorandum on trade and border coordination: shared customs inspection hours at the main crossings, joint working group on livestock and cotton, first meeting at Tash-Kömür in April; not a treaty; patrols coordinated, not joint) was not yet in the lore; it now is, and it covers this frontier (crossings near Bazar-Korgon and Tash-Kömür). The Border Demarcation Brigade patrols it.
- Vol1 Administrative divisions (external frontiers) and Vol2 ISEZ, Republican Gendarmerie and Irad–Uzbekistan relations also mention the 2025 memorandum.
- Now ISEZ (Lower Naryn District): Bazar-Korgon and its bazaar, Sopol-Tepa, Korgoncho, the Chopo-Jar and Sadaf-Jar bluffs, the point where the Naryn leaves Irad. Still tribal (Fergana Rim zone = the hills above the farm belt): Mailuu-Suu and tailings, Kara-Unkur valley and Kyzyl-Unkur, Kara-Unkur Cave, Arslanbob and the walnut forest, Arslanbob Falls, Jangak-Bulak, Örüktü, Kara-Jygach, Boz-Adyr (west of the Naryn), Kichi-Bel, Tuura-Say, Kum-Say Fan.
- canon.md: Basic data (area, density), Key dates (Aug 2007 declaration; 2009 gorge corridor), Footprint and borders (Jalal-Abad outside; new ISEZ–Uzbek frontier entry), Partition (line length, sectors, eight crossings, Lower Naryn district, ATR zones), Physical geography (Fergana Rim), Iyık Janyl (salient, line along the lower slopes), Other places (new farm-belt entry; ATR list), Clans (Chubar rewritten), Kurultai 2025, Smuggling routes, Neighbours, Toktogul leverage, Retired lines (area, line, crossings, new Lower Naryn/Bazar-Korgon/Uzbek frontier/Jalal-Abad entry). quickref.md: Chubar figures, 2007 and 2009 timeline, districts and areas, ATR zones, places, line.
- Vol1: infobox; Irad (lede area, ISEZ/ATR areas, divisions table, planning zones); ATR (area, extent, line, zones list, largest settlements, crossing count, economy line on hill growers); History of Irad (ceasefire paragraph); Iyık Janyl (lede, partition, Geography line position); Second Iradi Civil War (August 2007, ceasefire salient); Armed Forces (crossings); UNMI (line); Political status (area); Administrative divisions (lede, 2008 decree and 2009 extension, ISEZ area, district table and Lower Naryn note, ATR area, planning zones table, the line, external frontiers); Geography (area, Fergana Range and the Fergana Rim, the line, placements); Demographics (area, density, largest tribal towns); Transport (SR1 2009 corridor, roads from Tash-Kömür, movement across the line, Uzbekistan).
- Vol2: Fergana Gateway (salient); ISEZ (lede, district table, territory and frontiers, Gendarmerie crossings, Uzbek communities); Qara-Chik Demarcation Line (lede, 2007 origins with the declaration, 2009 protocol gorge corridor, sector lengths, southern sector course, crossings, Naryn corridor leverage); El-Choro (crossings, external borders); Republican Gendarmerie (crossings, Border Demarcation Brigade on the Uzbek frontier); Fergana Mountain Transit Highway (route end, cotton belt); Trans-Irad Pipeline Proposals; Toktogul Hydroelectric Complex (2009); Bishkek Ceasefire Agreement; Irad–Uzbekistan relations (frontier, roads and Bazar-Korgon trade, patrols, pipeline variant); Naryn River; Chatkal Range; Arslanbob (lede, highland Chubar seat, nut trade across the line, tourism crossing, religion); Mailuu-Suu (crossing, river through the ISEZ belt); Tash-Kömür (lede, geography, 2007, UNMI sector, trade); Islam in Irad (2007 division, Uzbeks); Clans of the ATR (Chubar rewritten, south wing, tension paragraph, 2024 remark); Smuggling (crossings, Bazar-Korgon).
- Vol3: Bazar-Korgon (rewritten: ISEZ, 2007 declaration, census figure and new census ref, trade and smuggling, 2024 remark); Kara-Darya; Sopol-Tepa and Korgoncho (now ISEZ, census ref); Chopo-Jar; Sadaf-Jar.
- Not changed: freeforum posts (nothing present-tense contradicts: Bazar-Korgon and Arslanbob posters, the Kurultai threads and the "cousin at the Bazar-Korgon market" post all still fit); hiddenlore; Kartalar files. Noticed, outside this brief: the Kartalar settlements.json gives the "Lower Naryn District" label point (41.4N 72.3E) zone ATR, since that point now falls in the tribal mountains; Vol1 Geography of Irad still says UNMI puts the Northern Steppe zone at "about 52,000" km² (table: 92,000).

# Change log: roads over real terrain, Iyık Janyl on the Naryn flats (Kartalar map, 2026-10-14)
- Later the same day: Sary-Bulak District ~350 km² (was 435) after the gorge sites moved onto the real terrain (canon, Vol1 districts table).
From the user: Iyık Janyl moved onto the real setting of Tash-Kömür; the Kartalar map's roads, railways and several sites re-routed over real terrain, and the lore made to match.
- Iyık Janyl: ~650 m (was 1,280) on the river flats where the Naryn leaves its gorge, ~8 km upriver from Tash-Kömür, directly on State Route 1 (~km 347; was a ~4-km side road ~26 km above Tash-Kömür, 332 km). Lower Town (modern city, flats west of the river along SR1); Cathedral Hill (~800 m, spur ~150 m above the east bank: old town, cathedral precinct, cloister, seminary, library, archives, hostel, Palace of Art) by the winding ~4-km Cathedral Hill road across the Naryn; Shahr-i Khunuk upstream (NE) on a bluff along Khunuk Creek; Shar-i-Kuhna on a river terrace ~3 km S of the centre, west of the Naryn; Diz-i Safid on a knoll west of the flats; Order motherhouse on the edge of the Naryn gorge below Cathedral Hill. Climate re-figured for 650 m (July highs ~34 °C, January lows ~−5 °C, ~450 mm). Tash-Kömür its neighbour just downriver. History and institutions unchanged.
- Roads: State Route 1 ~356 km (Otmek valley post km 64, tunnel km 87, Ala-Bel km 118, Toktogul km 180, round the east end and south shore of the reservoir to Kara-Köl/the dam km ~290, Iyık Janyl ~347, Tash-Kömür 356; mountain section ~226 km). Otmek tunnel ~5 km (2003), portals ~3,150–3,200 m some 150 m below the Ötmök pass, old pass road a summer bypass, cuts ~7 km of hairpins; Ala-Bel the highest point. Trans-Talas Highway ~167 km (Kyzyl-Adyr km 109; straight across the lower valley west of Kyzyl-Adyr). Talas–Nurzhan lowland road ~334 km. Kök-Bel road ~225 km; pass ~2,670 m at km 53, in tribal pasture (~10 km of tribal land between the two Toguz-Bulak crossings; Toguz-Bulak km 48). Chu highway ~116 km SE then E to the Chu Gate (~1,000 m, SE corner of the ISEZ). Boz-Korgon by its own guarded road east of Nurzhan beside the rail stub (no road length given in the lore, since the compound is "40 km east"; the map's 35 km left out). Railway ~630 km (was 650): Chu line ~247, Kara-Buura ~136, Talas branch ~93, north ~64, east ~41, Sary-Bulak spur ~26, Chatkal siding ~21. Pipeline/power-line lengths recorded in canon only (the wiki never stated them).
- Sites: Sary-Bulak works (~1,650 m) and village in the Sary-Bulak Gorge ~20 km SSW of Talas (was ~28 km S); Sary-Bulak road ~24 km via the Kara-Suu Canyon mouth (internal control post, ~13 km SW of Talas, ~1,390 m); Maryam-Bulak ~1,640 m near the works (canon had wrongly listed it as ATR); Chatkal smelter and village ~1,600 m in the next valley west, smelter road ~40 km, siding from the spur near the canyon mouth. Karakol ~2,550 m (was 2,300), ~20 km road from SR1, Suusamyr crossing ~2,660 m the highest; Aksay post ~2,000 m (was 2,400, "highest checkpoint"). Qara-Chik Border Checkpoint ~2,300 m at the head of the Kara-Oi valley, ~37 km by road from Talas. Kenkol Pass road ~35 km, line at the Kara-Bulak crossing (~1,260 m), so the pass is tribal-side.
- "About ten crossing points" became six crossing points (Qara-Chik, Aksay, Toguz-Bulak ×2, Kara-Bulak, Suusamyr) plus four internal control posts (Kara-Suu Canyon mouth, Otmek valley, Fergana Gateway, Naryn bridge) everywhere.
- Travel times scaled at the old average speeds: Nurzhan bus 4 h 20 (was 4 h 50), marshrutka 3 h 55 (was 4 h 20), lowland road; Sary-Bulak 1 h 30 (was 2 h); Tash-Kömür ~7 h (unchanged); Iyık Janyl ~6 h 50 (was 6 h 40; scaling alone gave ~7 h, set 10 min under Tash-Kömür since it is 9 km short of it on the same road). Kyzyl-Adyr 1 h 20 kept (the lore gave no old distance).
- canon.md: Iyık Janyl (site, layout, access, climate), Partition (crossings and control posts), Other places (Sary-Bulak, Chatkal, Karakol; Maryam-Bulak moved from the ATR list), Transport (railway breakdown, Trans-Talas, Talas–Nurzhan, Kök-Bel, Chu highway, Boz-Korgon road, other roads, pipeline and power lines, SR1 km points and tunnel, Kara-Suu post), bus station times, Retired lines. quickref.md: Iyık Janyl, Qara-Chik line and roads.
- Vol1: Irad (transport paragraph); Economy of Irad (Sary-Bulak location); Boz-Korgon (location); Iyık Janyl (lede, medieval town, Geography rewritten, Climate, Transport); Church of St. Janyl (conservation elevation); Syro-Iradi Catholic Church (motherhouse); Administrative divisions (cities table); Geography of Irad (lede, Talas valley and Tien Shan Marches Kök-Bel heights, climate list); Transport in Irad (rail network list, Main highways, Fergana Mountain Transit Highway section, Movement across the line); UNMI/ATR/Armed Forces crossing counts; Chu Gate south-east of Nurzhan.
- Vol2: Ruins of Old Iyık Janyl; Kara-Suu Canyon (Human use); ISEZ and Republican Gendarmerie (crossing counts); Qara-Chik Demarcation Line (name, central sector Kök-Bel, Crossings rewritten); El-Choro Militias; Northern Border Demarcation Protocol (Chu Gate); Antimony Mining in Irad; Chatkal Chemical Smelting Complex; Chatkal Range; Sary-Bulak Antimony Works; Fergana Mountain Transit Highway (lede, Route, Territorial reconstruction); Archbishopric of Iyık Janyl and Order of St. Janyl the Hermit (motherhouse); Kümöch; Bishkek Ceasefire Agreement; Tash-Kömür; Toktogul (town); Tourism; Smuggling.
- Vol3: Trans-Talas Highway; Karakol; Karakol Mountain Logistics Depot; Kök-Bel Pass; Shahr-i Khunuk; Diz-i Safid; Kenkol Pass; Qara-Chik Border Checkpoint; Aksay Border Patrol Post; Iyık Janyl Monastic Cloister; Sary-Bulak; Otmek; Toguz-Bulak; Maryam-Bulak; Khunuk Creek; Sary-Bulak Gorge.
- freeforum/history_v2.json: the two Feast-travel posts (345 km, road through the lower town, Cathedral Hill road; the 1,280 m "cold nights" line replaced).
- Other repos: Tulpar app bus times (Nurzhan 4 h 20 / 3 h 55, Sary-Bulak 1 h 30, Iyık Janyl 6 h 50; service worker v12). Talas Herald: 2020 Kök-Bel story (~2,670 m), 2021 Chu Gate (south-east of Nurzhan), 2024 Feast story (along the Naryn and up the Cathedral Hill road), the 22 Aug 2026 correction (no branch road). IradOne: Iyık Janyl weather point (650 m, new coordinates); pass reports now Fergana Gateway/Ala-Bel 3,184 m at the real Ala-Bel (was a 2,480 m point missed in the earlier pass), Otmek Pass as the summer bypass (season-closed 15 Oct to 15 Jun), Kök-Bel Pass added. Jılmay: nothing contradicted.
- Not changed: wiki SVG maps (another agent is redrawing them); Kartalar files. Noticed but outside this brief: IradOne info.js still has SOM_PER_USD = 5 (lore: 8.40 since 2008) and a Nurzhan weather point at 43.2N 73.0E.

# Change log: Qara-Chik line and ISEZ redrawn to the Kartalar map (2026-10-14)
From the user: the Kartalar map is now the authority for where the line runs; change the lore to match it.
- New figures: Irad 218,430 km² (84,337 sq mi; was 196,754 / 75,967); ISEZ ~30,700 km², about one-seventh (was ~64,000, one-third); ATR ~187,700 km², about six-sevenths (was ~132,000, two-thirds); districts Chu 13,480, Kara-Buura 6,750, Talas 5,980, Lower Naryn 4,060, Sary-Bulak 435 km² (areas include the cities); planning zones re-estimated (Northern Steppe 92,000, Karatau 38,200, Talas Alatau 18,500, Chatkal 16,000, Fergana Rim 13,000, Toktogul–Naryn 10,000). Line ~1,810 km (was 420): northern ~735, central ~425, southern ~375, western ~275; straight surveyed stretches across the steppe. "Twelve checkpoints" became "about ten crossing points" everywhere, so a later count change is a one-number edit. Densities: 21.2 official / 28.4 independent; ISEZ ~78; ATR 11.9 official, 19–21 independent. Population figures unchanged.
- Course: western ISEZ belt along the Trans-Talas Highway/railway to the frontier facing Shymkent, Karatau foothills tribal on both sides; northern belt along the main road and Turksib north of the Kyrgyz Range to a rounded Chu District (oases, oil fields, rail yards, Boz-Korgon, Chu Gate, Chu entry); the high Kyrgyz Range east of the Kök-Bel road tribal (Kök-Bel road crosses it between two Toguz-Bulak crossings); central sector broadly unchanged; southern ISEZ corridor along State Route 1 (upper Talas and Otmek valleys, Otmek tunnel, western Suusamyr, Ala-Bel, Chychkan valley), the whole Toktogul basin floor and the Naryn gorge, joining the Lower Naryn to the Talas valley. Lower Naryn District now runs north to the Otmek tunnel; Talas District takes the Otmek valley and upper Talas valley.
- Handover story (invented): the 2007 line stays as history (dam tribal, guarded road across tribal land). After the 2008 record low and 2008–09 rationing, UNMI brokered the **Protocol on the Toktogul Basin and the State Route 1 Corridor**, signed at Kara-Oi on 14 July 2009 and approved by the August 2009 Kurultai (Kökjal stood aside): corridor and basin floor (Toktogul town, Kara-Köl, dam, reservoir, powerhouse) to the ISEZ; the high Kyrgyz Range east of the Kök-Bel road (with Toguz-Bulak) to the clans; clans also get guaranteed grazing, stock-route and water rights in and across the transferred land (agreed herd crossings), a fixed minimum share of Toktogul revenue (unpublished annex), their equal seat on the Naryn commission and consent to each five-year schedule; basin elders' councils keep pasture and irrigation authority. El-Choro handed the dam to the Gendarmerie in October 2009. The Otmek valley, Gateway summit and Naryn bridge posts are internal Gendarmerie control posts (ID checks and road-use charge kept). Tash-Kömür stays UNMI's Lower Naryn sector HQ; the Toktogul–Naryn planning zone keeps its name but covers only the highlands around the basin.
- Now tribal: Ak-Tash village (training center kept as a fenced State Defense Corps installation by clan arrangement; Akyel Breeding Sanctuary leased from a clan just beyond the line), Toguz-Bulak, the NurGaz main field collection station and the Northern Export Feeder metering station (guarded installations on tribal land). Already tribal in the lore, no change: Tar-Say, Hauzdy, Kök-Moinok, Rabat-i Kamal, Kamyshtuu, Kara-Kungey. Now ISEZ: Orto-Ayyl (Talas District, 2018 census), Toktogul town, Kara-Köl, Jele-Döbö and Kara-Say (2018 census), Karakol-Ashuu, Otmek, the Uch-Terek rapids, the Talas headstreams; a strip of the Aksay Plateau's eastern margin falls in the corridor, while the Kurultai ground and camps stay tribal.
- canon.md: Basic data (area, density), Key dates (2009 protocol), Partition (line, sectors, crossings, ISEZ districts and areas, installations on tribal land, ATR zones and placements), Iyık Janyl access, Other places, Kurultai sessions (2009), Toktogul and the Naryn Protocol, State Route 1 entry; Retired lines (area, fractions, densities, line length, checkpoints, Toktogul placement; the earlier "guarded road across tribal land, not an ISEZ corridor" line rewritten). quickref.md: timeline 2009, districts and areas, ATR zones, Toktogul, line.
- Vol1: infobox (area, density); Irad (lede, frozen conflict 2009, hydrology, ISEZ/ATR areas, divisions table, planning zones, transport); Autonomous Tribal Regions (area, line, geography, Toktogul–Naryn zone, El-Choro and the dam, revenue, crossing points, Naryn Protocol, humanitarian); Economy of Irad (energy, divided resources, Since 2007); History of Irad (ceasefire, partition); Politics of Irad; Bektur Zhumabek uulu; Iradi Freedom Society (2009 transfer); Second Iradi Civil War; Territorial Legislature; Armed Forces (Gendarmerie crossings, Lower Naryn battalion); UNMI (lede, history 2009, Naryn supervision); Political status (area, IAC claim, water and power); Administrative divisions (lede, 2008 decree and 2009 extension, areas, district table and notes, ATR, planning zones table, the line); Elections; Geography (area, partition, Kyrgyz Range pastures, political geography and placements); Demographics (fractions, densities, largest tribal towns); Energy (overview, split control); Transport (ATR share, State Route 1, control posts, analysts, Kök-Bel road, movement across the line).
- Vol2: Aksay Plateau; ISEZ (lede, 2009, districts table, geography, water, electricity, Gendarmerie, relations); Popular Front; Qara-Chik Demarcation Line (lede, crossing points, new subsection "The Toktogul corridor protocol (2009)" with new ref 9, Course rewritten with sector lengths, Crossings, Naryn corridor, Effects); El-Choro Militias; Republican Gendarmerie; Fergana Gateway (lede, Security); Fergana Mountain Transit Highway (lede, route, new subsection "The 2009 corridor protocol", strategic role, restricted zone, control posts); Trans-Irad Pipeline Proposals; Toktogul Hydroelectric Complex (lede, location, Since 2007, "Divided control" section now "Control and security", revenue); Naryn Water and Power Protocol (lede, 2009 background, provisions, domestic disputes); Bishkek Ceasefire Agreement; Naryn River; Talas River (headstreams now ISEZ); Moiynkum Desert; Tash-Kömür; Toktogul (town) (now ISEZ, elders' councils, 2009, transport); Tourism (Kök-Bel); Kurultai (2009 session); Smuggling across the Qara-Chik Line; Northern Export Feeder (metering station on tribal land).
- Vol3: Trans-Talas Highway; Nurzhan Petroleum Pipeline (collection station); Akyel Breeding Sanctuary; Ak-Tash (now ATR, 2022 estimate, UNMI ref); Suusamyr; Kök-Bel Pass; Orto-Ayyl (now ISEZ, census ref); Karakol-Ashuu; Otmek; Toguz-Bulak (now ATR, UNMI ref); Kara-Say and Jele-Döbö (now ISEZ, census ref); Uch-Terek Rapids; Kara-Buura.
- Not changed: freeforum/history_v1/v2.json posts (dated forum posts; nothing in them is a present-tense contradiction, and a 2022 rumour that "the Kökjal want Toktogul back" now fits). The "about 285 km" of ISEZ-held frontier marked under the 2008 northern protocol is left as the protocol's figure. Wiki SVG maps not regenerated (later job).

# Change log: Jılmay among the major companies (2026-10-14)
From the user: add Jılmay to the list of Iradi companies.
- Vol1 Economy of Irad, "Major companies": new item 11, Jılmay (Talas classifieds marketplace, Kyrgyz-registered company, Jılmay Cargo the only delivery of foreign goods to the ISEZ).
- canon.md "Top companies": 11. Jılmay.

# Change log: State Route 1 and roads to the Attelkom Kartalar map (2026-10-14)
From the user: the new map (Attelkom Kartalar) follows real-world roads; make the lore's roads, distances and passes match it.
- canon.md: Iyık Janyl access (~332 km by road; ~4-km side road ~26 km above Tash-Kömür); Transport and telecoms: Irad Temir Jolu ~650 km (Turksib main line through Kara-Buura and the Chu lowlands, branches along the valley roads), Trans-Talas Highway ~215 km (Talas North Terminal–Kyzyl-Adyr–Talas), Talas–Nurzhan road ~369 km, new State Route 1 entry (Talas valley ~66 km, Otmek valley mouth checkpoint and road-use charge, Otmek tunnel ~km 91 below the Ötmök/Otmek Pass 3,330 m, western Suusamyr, Fergana Gateway = Ala-Bel 3,184 m ~km 120, Chychkan valley, Toktogul ~km 183, dam and switchyard, Kara-Köl ~km 293, Naryn gorge, Tash-Kömür ~km 358; mountain section ~227 km; guarded road across tribal land; Kara-Suu Canyon carries the Sary-Bulak road); bus station times (Nurzhan bus 4 h 50, marshrutka 4 h 20; Tash-Kömür ~7 h; Iyık Janyl ~6 h 40); Retired lines for the railway, State Route 1/Fergana Gateway, Iyık Janyl distance, Trans-Talas length and bus times.
- quickref.md: Iyık Janyl road distance; Fergana Gateway (Ala-Bel, 3,184 m; State Route 1 ~358 km).
- Vol1 Country Overview: Lower Naryn row of the divisions table; Transport and communications (358-km State Route 1, Ala-Bel 3,184 m, guarded corridor across tribal land, railway ~650 km). Talas: Transport. Iyık Janyl: lede (332 km) and Transport (side road, 6–7 h by bus). Administrative divisions of Irad: Lower Naryn table row, Sary-Bulak and Lower Naryn district notes, Qara-Chik line paragraph. Geography of Irad: Tien Shan Marches paragraph (Otmek tunnel, Ala-Bel); Political geography (salient on the lower Naryn, tribal/ISEZ placements). Transport in Irad: rail network (~650 km, main line through Kara-Buura), Main highways (Trans-Talas ~215 km, Talas–Nurzhan ~369 km, State Route 1 ~358 km, Iyık Janyl side road), Fergana Mountain Transit Highway section (route, ~227-km mountain section, Otmek valley checkpoint and charge), Kyrgyzstan.
- Vol2 Tien Shan Marches (crossings); Fergana Gateway (lede now Ala-Bel Pass, 3,184 m, 42°15′N 73°04′E; Geography approaches; Security: on tribal land, Gendarmerie summit checkpoint, bus passengers' IDs, maintenance station); Kara-Suu Canyon (lede and Human use: Sary-Bulak road, district-road checkpoint); ISEZ (divisions table row, territory paragraph); Qara-Chik Demarcation Line (Course intro, Southern sector); Fergana Mountain Transit Highway (lede, Route rewritten with km points, Soviet road paving, journey ~7 h, 2007 and the ceasefire, Strategic role, restricted zone, Checkpoints, maintenance stations); Trans-Irad Pipeline Proposals (tribal consent); Bishkek Ceasefire Agreement (Naryn corridor dispute); Chatkal Range (ISEZ foothills, Gateway); Tash-Kömür (358 km, journey ~7 h, Iyık Janyl about 20 km, not 18); Toktogul (town) (dam ~100 km by road; Transport rewritten: State Route 1 through the town).
- Vol3 Trans-Talas Highway (~215 km, ends at Talas, herders' track beyond the line); Suusamyr (State Route 1 through the western valley); Talas Alatau (main crossings); Otmek (hamlet now on State Route 1 above the tunnel).
- Not changed: freeforum/history_v2.json still has two posts giving "235 km over the Fergana Gateway, then the 12-km branch" (forum posts, outside the files in scope).

# Change log: details from the Tulpar app (2026-10-13)
From the user: add the details invented for the Tulpar web app and its seeded room history to the lore.
- canon.md: Irad League 2026 run-in (60–54 after 3 Oct; 10 Oct results; no round 17 Oct for Irad Cup semi-finals; round 27 Kara-Ak derby 31 Oct at NurGaz Stadium decides the title; derby traditionally closes the season) and other grounds (Lokomotiv Stadium, Attelkom Park, TSU Stadium); Talas Central Bus Station departures and fares (Kyzyl-Adyr 24 → 30 som from 19 Oct 2026); Bazar-i Kalan street rates 13 Oct and everyday prices; Tulpar features and Services tab (Tulpar Taxi tariffs, food partners incl. Taquería Semiz, Bölüp tölöö terms, transfer fee; government tile links only to ISEZ portals; NurGaz refuses Tulpar Pay); 2026–27 church calendar dates; ulak league (city teams, Highland clan division, 2026 results).
- Vol3 Tulpar (app): new "Features" section (rooms, stickers, sign-in, Services).

# Change log: Tulpar leadership (2026-10-13)
From the user: add the people from the Tulpar website to the lore and wiki.
- Vol3 new bio stubs #495 Aiperi Kalysbekova, #496 Jyldyz Toktomamatova, #497 Bektemir Osmonov, #498 Svetlana Kim, #499 Azamat Joldoshbekov (Historical Figures & Personalities, now 64; stubs 398).
- Vol3 Tulpar (app): new "Company" section (staff, offices, revenue, investors, leadership list), office detail; Tulparcoin: supply split and lock date. Vol1 Jason Ilyasov: link to Kalysbekova.
- canon.md Tulpar entry: company and leadership, website, supply split, wallet limit; quickref Ilyasov line.

# Change log: Jılmay wiki article (2026-10-13)
From the user: jilmay.com is live; a wiki article linking to it.
- Vol3 new Start article #494 Jılmay (Economy & Industry; count 254) with an External links line to https://jilmay.com/. Invented: launched 2016, Kyrgyz-registered company, owners undisclosed, the login complaint framed as a known fault.
- Links added in Tulpar (app), Talas Central Post Office and Iradi som. canon.md Media entry Jılmay; quickref institutions.

# Change log: Tulpar name dispute, 2025 dip, Bekzatov (2026-10-13)
From the user: archived articles about the Tulpar app; the football club's registration is long-standing, and it couldn't touch Tulpar because the app's company is officially American, so the club is now a vector to attack the coin; hidden: Bekzatov is behind it (sees Tulparcoin as destabilizing, distrusts Ilyasov as an American); the Trump backlash briefly hurt the app ("an American company" posts) before it bounced back.
- TCDG's Tulpar mark: 2012, extended to "digital products" 2021 (matches the Herald's 2 Oct story); 2020 demand letter answered from Delaware; no case. Replaces the earlier "2021 registrations / prior use" version.
- 2025: "the American app" posts after the Trump remarks; monthly users 560k (Jan) to 470k (early Mar), 590k by late Aug.
- Bank of Irad licensing statement dated 29 Sep 2026; Bekzatov's public "a toy that can burn down a house"; Sorokin's firm also acts for NurGaz (public).
- Wiki: Vol3 Tulpar (app) (2025 dip, new "Dispute over the name" section, nine refs, most linked to Herald archive pages), Tulparcoin (trademark); Vol1 Jason Ilyasov (2025 dip, ref 13 linked); Vol2 Iradi som (ref 11 linked).
- canon.md Tulpar entry and Retired line; quickref Feb 2025; hiddenlore new entry "Bekzatov and the Tulparcoin Case".
- Talas Herald: five Tulparcoin stories now mention the app (and the 25 Sep quote says 8.40, not five); nine new archive entries (2019-03-14, 2020-11-18, 2021-06-09, 2023-10-28, 2025-03-06, 2025-08-27, 2026-09-24, 2026-09-30, 2026-10-03). IradOne's 25 Sep story quote fixed to 8.40 for eighteen years.
- FreeIrad.org's Tulparcoin piece not changed (site not reachable from here).

# Change log: som reset, 2026 street rate, Tulpar app (2026-10-13)
From the user: a 2008 reset of the som instead of 5/USD since 1993; recent instability pushing the black-market rate; the Herald still takes som, Jılmay is USD-only for outside purchases; Jason Ilyasov is CEO and front man of Tulpar, a WeChat-like app (chat, classifieds) whose Tulparcoin push into payments, replacing the som on the platform, is the main friction with the government; Ilyasov is sincere, not running a rug pull, but the plan is reckless.
- Rate: 5/USD 1993-2008; Bank of Irad Act resets to 8.40/USD from 17 Mar 2008 (reserves at ~60% cover after US freezes and DRI drawdowns in 2007). 2026: Talasbank $300/month dollar cash cap (May), bazaar rate ~9.5 (Jun) to 11-12 (Oct); bank denies a second reset.
- Tulpar (app): launched Mar 2019; Tulpar Technologies (Delaware, Talas office); CTO Aiperi Kalysbekova (new); channels 2020, Bazar 2021; grew in the 2023 protests; 1.1 m accounts claimed. Tulpar Pay to go Tulparcoin-only 1 Jan 2027; Bank of Irad: unlicensed. TCDG trademark registrations dated 2021 (after the app).
- Wiki: Vol2 Iradi som (history, new "The 2026 street rate" section, refs 10-11), Bank of Irad (2007 drawdown, 2008 reset, 2026), Iradis in Russia (remittances); Vol1 Economy (som sentences), Jason Ilyasov (lede, new Tulpar section, 2023, Tulparcoin, funding, refs 12-13); Vol3 new Start article #493 Tulpar (app) (Media; count 253), Tulparcoin (lede, block), Tulpar (Mythology) (hatnote sentence).
- canon.md: currency line, Currency and remittances, Ilyasov, new Media entry Tulpar, two Retired lines. quickref.md: Ilyasov, timeline, institutions. hiddenlore.md: Ilyasov funding route via Tulpar and his sincere motive.
- Jılmay site: rate 8.40, vehicles/property/expensive horses priced in USD, Jılmay Cargo and outside purchases USD only, no Tulparcoin.
- Not changed: Talas Herald's five Tulparcoin stories (Sep-Oct 2026) don't mention the app; FreeIrad.org's Tulparcoin piece likewise.

# Change log: FREEFORUM history batch 2 (2026-10-13)
- 213 more threads, 2,764 posts, 103 shoutbox messages, 59 more sample members (12 writers by board and era). canon.md FreeIrad entry notes the forum lore it fixes (2012 block and offshore move, Attelkom map launch date, notable regulars).

# Change log: FREEFORUM back-history (2026-10-13)
- 52 threads, 643 posts, 93 shoutbox messages (2011-2026) written for the forum import; canon.md FreeIrad entry notes the forum's in-world history (Ak_Shumkar feud and ban, JANYL_watch, olddog_1992, labelling rule, relaunch date).

# Change log: FreeIrad.org FREECHAT forums (2026-10-13)
Requested by the user: a working early-2000s style forum with real sign-ups, pre-populated later.
- Site: PHP forum at /forum (boards, sample threads, seed regulars listed in canon); members-only archive links go to an "ÖCHÜRÜLDÜ / this page has been erased" 404; "I remember Irad" counter.
- canon.md FreeIrad entry; Vol2 FreeIrad.org (Activism) mentions the forums.

# Change log: FreeIrad.org centred on the Erasure (2026-10-13)
Requested by the user: make the Erasure theory the site's central fight.
- Site: masthead, erasure strip, front page grouped by erasure stage, every story carries an "Erasure file" box; new The Erasure, Map check, Lost Episode and Country Not Found pages; About and Take Action rewritten around it.
- Vol2 FreeIrad.org (Content) and Erasure Theory (Origins, cite 4) updated; canon.md FreeIrad entry.

# Change log: FreeIrad.org expanded (2026-10-13)
Requested by the user: flesh out freeirad.org (site files delivered as a zip; hosted elsewhere).
- Site: full article pages for the ten front-page stories plus four new ones (Tulparcoin, Trump lobbyists, Bill of Sale, Gendarmerie diesel) and the Alimbekov-Baker treaty piece; Who we are, If we are blocked, What you can do and Search pages; FREECHAT in the site layout. All claims are the site's own, undated, from unnamed sources; nothing from hiddenlore stated as fact (the site still says Toktarov died in 2022).
- Irad_Wiki_Vol2_C_Class.md, FreeIrad.org: later claims, Who we are page, citation 3.
- canon.md: FreeIrad.org entry expanded.

# Change log: Erasure theory (2026-10-13)
From the user: a conspiracy theory that foreign powers (which ones varies by teller) are erasing Irad and hiding it from the world; Irad's absence from Google Maps as the case in point.
- New Vol2 C-Class article #4.171 Erasure Theory (*Öchürüü*); C-Class count 170 -> 171. FreeIrad.org article links to it. canon.md (FreeIrad claims) expanded.
- Talas Herald archive: "Why Irad is not on the map" (13 April 2019, Aigerim Tokonova, Features).

# Change log: Trump remarks, Alikhan's lobbying and the memory of 2007 (2026-10-13)
From the user: Alikhan's bumbling Washington lobbying brought Irad to Trump's attention; the Bill of Sale is a driving force for why the remarks were so offensive.
- hiddenlore.md (Alikhan's Washington Stagnation): the backfire. His late-2024 lobbyists pitched Irad as a "deal"; Trump turned it into a sale to Russia.
- Public layer only as rumor: FreeIrad.org claims lobbyists linked to Alikhan briefed Trump's circle; IradOne Media Group denies; unverified.
- canon.md (Trump remarks): the 2007 echo; the slogan "Irad is not for sale" (*Irad satylbayt*) first chanted in Nurzhan in 2007, revived 2025.
- Vol2 2025 Trump Remarks on Irad: the rumor; new section "The memory of 2007" (placards "Ekinchi Satuu Kagazy", the slogan's origin, why both zones marched).

# Change log: Bekzatov and Toktarov, 2007 and after (2026-10-13)
From the user: Bekzatov worked with Toktarov to establish the ISEZ (some say it could not have been done without him) and hailed him as a national hero; he turned on Toktarov as Toktarov became despotic. Hidden lore: insiders see Bekzatov as a power-hungry usurper, but he cares deeply for Irad, believes it will collapse and be carved up, and thinks uniting as a republic under Russia is Irad's safest course.
- canon.md, quickref.md: Bekzatov as the ISEZ's 2007 backer; the break (2010 Parties Act, Labor dissolved 2011, 2013 term limits).
- hiddenlore.md: Bekzatov's motive added under "Aborted Coup" (internal ground truth only; never stated as fact in public writing).
- Vol1: Kamran Bekzatov (Relations with the DPI), Erlan Toktarov (lede), Second Iradi Civil War (proclamation).
- Talas Herald archive: "Kamran Bekzatov at Sixty" (28 Jan 2011) gains a paragraph on 2007 and his criticism of the Parties Act.

# Change log: the Bill of Sale (*Satuu Kagazy*), 2007 (2026-10-13)
From the user: the main cause of the Second Civil War was Orozbekov's secret plan, negotiated Dec 2006 – Feb 2007 as "border consultations" with Kyrgyzstan, Uzbekistan and Kazakhstan, to use the 2006 sovereignty ruling to dissolve Irad and partition it (escrow compensation; oil, antimony and Toktogul concession shares for companies tied to Orozbekov and ministers). Toktarov leaked it in the Nurzhan speech of 25 Feb 2007 and became a national hero; permanent clan distrust of city governments; Orozbekov charged with treason in 2008; neighbors never rescinded claims, no threats, waiting it out; reopened by the 2025 Trump remarks. canon.md and quickref.md were already updated.
- New Vol2 C-Class article #4.170 Bill of Sale (2007) (History); Vol2 count 169 -> 170. New source: State Archives Fond 310 (Cabinet of the DRI, 2006–2007); *Irad Times* special edition of 26 Feb 2007.
- Vol1: Irad (2006–07 history; 2025 remarks), History of Irad, Erlan Toktarov (lede, ISEZ creation, hero status, "how long he knew" debate), Bektur Zhumabek uulu (Front demands, 2011 veto demand, positions), Nurzhan, Democratic Party of Irad, Iradi Freedom Society, Second Iradi Civil War (lede, new Background subsection, proclamation, Front demands, aftermath, historiography), Supreme Court of Irad (annulment), Political status of Irad (suspended sovereignty, neighboring claimants, US/2025, integration option), Territory of Irad, Human rights in Irad (treason charge), Foreign relations of Irad (neighbors' claims, 2006–07 history, Turkey/Orozbekov, public opinion), Media of Irad (*Irad Times* printed the drafts).
- Vol2: Irad Special Economic Zone, Popular Front of Irad, 2025 Trump Remarks on Irad ("Irad is not for sale"), Bakyt Orozbekov (lede, new Bill of Sale subsection, Front demands, treason charge, memoir denial, assessments), Democratic Republic of Irad (new section, recognition, collapse, aftermath, legacy), Irad–Kazakhstan / Irad–Uzbekistan / Irad–Kyrgyzstan relations (new "The Bill of Sale" subsections), Talas Herald (27 Feb 2007 coverage).
- Vol3: Statutory Independence Ruling (2006), Proclamation of the DRI, Privatization Scandals of 2007, Storming of Talas (2007), 2011 Bilateral Reunification Summit, Bolotbek Daniyarov.
- Talas Herald archive: revised "Toktarov Proclaims Special Economic Zone from Nurzhan" (2007-02-26: the leak, "bill of sale for our country") and "Former prime minister charged in absentia" (2008-03-19: high treason + abuse of office, "contingency papers" denial); new entry "Partition drafts: what the papers say" (2007-02-27, Nadia Osmonalieva, TALAS).

# Change log: Irad has no top-level domain (2026-10-13)
Requested by the user: explain that Irad has no TLD because of its non-state status.
- New Vol3 Start article #492 Internet Domains of Irad: no ISO code, no ccTLD (compare Western Sahara); .ir.ad under Andorra's .ad, run by Attelkom since 1996; id.gov left over from the territorial administration; generic domains for independent sites.
- Vol1: Political status (codes bullet), infobox TLD line, Attelkom history. canon.md: basic data line now explains the workarounds (was "TLDs .ir.ad / .id.gov").

# Change log: Tulparcoin (2026-10-13)
From the user: Jason Ilyasov launches a horse-themed crypto coin, Tulparcoin; outcome left unresolved.
- Live storyline: five Talas Herald stories (23 Sep, 25 Sep, 2 Oct, 9 Oct, 12 Oct 2026), one IradOne story (25 Sep, the Bank of Irad warning, without Ilyasov's name or the lawsuit), a OneDebate topic ("Tulparcoin: freedom or folly?").
- New Vol3 Start article #491 Tulparcoin; Vol1 Jason Ilyasov: Tulparcoin (2026) section. canon.md: Ilyasov entry.
- New minor people: Aliya Turgunbekova (Liberty Forum spokeswoman), Ermek Sadykbekov (Bank of Irad deputy chairman), Bolot Ormokoev (TSU finance lecturer), Vadim Sorokin (TCDG lawyer), Kanykei Imanbekova (Forum lawyer), Judge Asel Mamytbekova (Talas District Court), Erkinbek Kenjeshov (courier). Trademarks Act of 1995.
- Next beat: hearing on 16 November 2026.

# Change log: three tüntolk songs (2026-10-13)
From the user: three tüntolk songs in Iradi. "My Home My Heart My Soul" kept as written (correct Iradi); "Morkhan the Dark Lord" and "Cut the Stars in the Night" rewritten into grammatical Iradi (approved), keeping the user's key phrases. Films chosen with the user: Party Monster (2003, US), Head-On (2004, Germany).
- New Vol3 Start articles #488-490: Morkhan, Karañgy Ee; Cut the Stars in the Night; My Home My Heart My Soul. Start count +3.
- Vol2 tüntolk: EP song and its films; 2023 protest song; discography with key tracks. Vol3 Jolchu (Album): the Morkhan song.
- canon.md (Music): the three songs.

# Change log: Mor-Folk is dark synth; "Dream of Living" and True Detective (2026-10-13)
From the user: Mor-Folk is not acoustic; dark synth is the through line of all the Mor- genres. "Dream of Living" became known abroad through the soundtrack of True Detective season 4.
- canon.md, Vol1 (Music of Irad), Vol2 (Mor-Wave, Music of Irad), Vol3 (Komuz, Mor-Folk, Dream of Living, Eski Ün): Mor-Folk = komuz, choor, frame drums and chant melodies over dark synthesizers.
- Dream of Living: fame abroad from True Detective: Night Country (2024) instead of streaming playlists.
- Talas Herald archive (27 June 2019, Eski Ün): the ensemble plays over analog synthesizers.

# Change log: "Dream of Living" (2026-10-13)
From the user: "Dream of Living", the only Mor-Folk song popular outside Irad; illbient, ephemeral, dark, with a background noise like scratching or screaming; English lyrics (saved in media/songs/dream_of_living.txt).
- Reconciled with canon (Mor-Folk = acoustic liturgical folk): an acoustic Mor-Folk song in an illbient production; English-language version (2021) of the Iradi "Jashoo Tüshü"; by Eski Ün, the Talas ensemble from the 2019 Herald archive story.
- New Vol3 articles: Dream of Living (#486, Start), Eski Ün (#487, Stub). Mor-Folk article: one sentence. canon.md (Music): Eski Ün and the song.

# Change log: Keñsuu dialect and "Sary Kün, Ejen Kyz" (2026-10-13)
From the user: an old (c. 100-year) a cappella recording of a traditional song with stamped percussion, a man singing the verses and others joining the chorus; lyrics in a Turkic text that is not grammatical standard Iradi. User chose to explain it as a dialect that died out.
- New Vol3 Start articles: Keñsuu Dialect (#484) and Sary Kün, Ejen Kyz (#485). Start count 244 -> 246.
- Vol2 Dialects of Iradi: "Keñsuu (extinct)" subsection. Vol2 The Lost Tribes of 1916: Keñsuu speakers among the lost clans.
- canon.md (Language, dialects): Keñsuu entry and the song.
- Lyrics saved in media/songs/sary_kun_ejen_kyz.txt.

# Change log: Swift Hooves songs (2026-10-13)
From the user: six recorded songs from the 1993 *Swift Hooves* compilation, with lyrics and style notes (saved in media/swift_hooves/).
- Irad_Wiki_Vol3_Start_Stub.md, Swift Hooves (Compilation): new Songs section listing ten of the fourteen tracks; reception of the songs' American assumptions (cattle, Turkmenistan); "Notches" as the album's most debated song (chauvinism; heard as a civil-war song; rarely aired on IradOne; bar-band standard with "notches walls").
- canon.md (Music): track list, the cattle complaint, the "Notches" reception; new word *göñgülchü* ("outlaw, bandit").

# Change log: Talas International Film Festival in September (2026-10-13)
Requested by the user.
- canon.md: the biennial festival (odd years) is held in September.
- Irad_Wiki_Vol2_C_Class.md (Tourism festivals list) and Irad_Wiki_Vol3_Start_Stub.md (Irad Film Society): "autumn" -> September.
- Talas Herald archive: "Film festival audiences fall again" now dated 2 October 2023 (was 21 November), no longer tied to the October protests.
- iradone.com: the 2025 festival story moved from 18 February to 16 September 2025; the restored Desert Sun's Rebellion is an anniversary screening (it premiered at the 2005 festival, as the wiki says).

# Change log: IradOne television programs (2026-10-13)
Requested by the user: wiki articles for IradOne's own programs (iradone.com schedule.json).
- Irad_Wiki_Vol3_Start_Stub.md: new category "Television Programs" (Category: Media): 18 Start-class articles (incl. List of IradOne programs, OneNews, OneDebate, OneTruth, OneBreakfast, OneSport, Jyldyz Jolu, İçkenge Attı Jetelep, Kuda (TV series), Patrol: Kara-Bulak, Akyrky Ashuu (TV series), Kim Bilet?) and 26 stubs (#440–483). Counts: Start 226 -> 244, Stub 366 -> 392. Each links to its iradone.com programme page. Acquired programs and holiday specials are listed, without articles.
- Irad_Wiki_Vol1_Core.md, IradOne (Programming): links to the new articles and the list.
- canon.md (Media): "One" house style dated 2016 (Debate One 2011 -> OneDebate 2016; bulletins formerly IradOne News); pre-2016 titles, church co-productions and commissions keep their names.
- New minor lore: presenters, producers and premiere years for each program (e.g. Begaiym Shamshieva, OneNews at Eight; Aida Kalmatova, OneDebate; Anara Tursunbaeva, OneBreakfast; Talant Myrzabekov, Kim Bilet?); Almaz Sarybaev plays the grandfather in the 2016 Akyrky Ashuu serial; Koyon Teşigi is the 2021 Sunday children's slot where Altyn Muuz sang "Morkhan Baby".
- Open questions found (not changed): the IradOne youth channel is in canon but not in the IradOne article's channel list; schedule.json lists Hands of Irad on Tue/Thu but airs it only Tuesdays; Talas film festival month (IradOne Feb 2025 story vs Herald/wiki autumn).

# Change log: Talas Herald citations linked (2026-10-13)
Requested by the user.
- All three volumes: every Talas Herald citation (229, in 166 distinct articles) now links its headline to the article's archive page at talasherald.com/archive/<year>/. The Herald archive was written to match each citation's headline and date.

# Change log: Talas Herald official website link (2026-10-13)
Requested by the user.
- Irad_Wiki_Vol2_C_Class.md, Talas Herald: External links section with The Talas Herald (https://talasherald.com/), as for IradOne and FreeIrad.org. The site's archive has a page for every Herald article the wiki cites.

# Change log: IradOne official website link (2026-10-12)
Requested by the user.
- Irad_Wiki_Vol1_Core.md, IradOne: External links section with IradOne Online (https://iradone.com/), following the FreeIrad.org article; the Channels list describes IradOne Online as the website as well as the streaming service and archive.

# Change log: IradOne "One" program names (2026-10-12)
Requested by the user: *Debate One* renamed *OneDebate*, and the "OneThing" pattern made standard for IradOne's own programs.
- Irad_Wiki_Vol1_Core.md: *Debate One* -> *OneDebate* (Jason Ilyasov, Media of Irad); IradOne article (Programming) names the convention and the 20:00 bulletin *OneNews at Eight*; Media of Irad likewise.
- Irad_Wiki_Vol3_Start_Stub.md: *Debate One* -> *OneDebate* (2023 Student Protests in Talas).
- canon.md (Media): program-name convention; Retired names: "Debate One". quickref.md (institutions): house program names.
- iradone.com schedule follows the same convention.

# Change log: "The Steppe Family Robinson" (2026-10-12)
Requested by the user: a Simpsons episode from the Iradimania period in which the family visits Irad and causes an international incident; aired once in the US, rerun only in Irad.
- Irad_Wiki_Vol2_C_Class.md: new article 4.169 The Steppe Family Robinson (C-class count 168 -> 169). Pulled from US reruns by a 1995 settlement of a music dispute over its parody of "Ride for Talas"; Irad rights licensed to IradOne with fees to the Swift Hooves charities.
- Links from Iradimania and Swift Hooves (Compilation) (Vol3) and IradOne (Vol1).
- canon.md (Culture) and quickref.md (timeline) updated; SKILL.md article count 811 -> 812.

# Change log: skill restructured (2026-10-12)
Requested by the user: tidy up the irad-persona skill.
- canon.md (new, ~84 KB): baselore.md and newlore.md merged into one topic-organized current canon, superseded statements removed, ending with "Retired names and common errors". Written, then audited bullet by bullet against both sources (36 missing details restored, no covert leaks). Decided: Skobelev (not Chernyayev) conquered Kokand in 1876; Jolbors means "Snow Leopard".
- quickref.md (new, ~15 KB): who's who, timeline, places, institutions and laws, glossary.
- Moved out of the installed skill into maintenance/: CHANGELOG.md, CHANGELOG_wiki_review.md, archive/pre_review/, Irad_Wiki_Original.md, and superseded/baselore.md and superseded/newlore.md.
- SKILL.md rewritten: new file table and precedence (canon > volumes), faith conventions, writing rules from the writers' brief (name checks, article template, references, links, categories), and the two-repository workflow; trigger list adds the Kurultai, Semiz, Mor-Wave and the Talas Herald.
- Wiki repo: tools/links/ (audit.js, linker.py, wp_map.json) saved with a README.

# Change log: linking and category audit; Wikipedia links (2026-10-12)
Requested by the user: audit links and categories, and link real-world things to English Wikipedia.
- Categories: the 72 ad-hoc category names were replaced by a fixed list of 20 (see SKILL.md, "Wiki markup"). Every article was reclassified individually; 445 quality lines changed and 366 stubs gained their own `*Quality: Stub | Category: …*` line (the Vol3 category headings are now only groupings).
- Internal links: about 490 links added at the first mention of an existing article title (guards skip headings, references, tables with pipes, Iradi-language italics, longer proper names, and river/valley uses of "Talas"); 18 more to term articles from their italic mentions; the one red link (Iradneft) unlinked. Orphans 189 -> 178; most remaining orphans are stubs that no other article mentions.
- Wikipedia: new `[[wp:Title|text]]` markup; about 2,500 first-mention links to 560 English Wikipedia articles (titles checked; doubtful ones fetched and corrected, e.g. Shardara Dam, Moscow Manege, Ismail Samani; three dropped). Common words and major world religions/peoples deliberately left unlinked. Nikolai Voronov hatnote links the Soviet marshal.
- SKILL.md: new section "Wiki markup: links and categories".

# Change log: Iradi plov is risotto-like; long-grain plov also made (2026-10-12)
Requested by the user.
- Irad_Wiki_Vol1_Core.md: Iradi cuisine, "Iradi plov" section rewritten (stirred short-grain dish; long-grain plov for weddings and memorial feasts); Irad article (Cuisine) and Culture of Irad (food summary) clarified.
- Irad_Wiki_Vol2_C_Class.md: Iradi Horsemeat Taboo (Iradi versions of regional dishes) clarified.
- newlore.md: appended "Iradi Plov Clarified".

# Change log: "Iradi Zoomer Movement" renamed "Iradi language revival" (2026-10-12)
Requested by the user (option 1 of three offered).
- Irad_Wiki_Vol2_C_Class.md: 4.60 retitled; lede and Name section rewritten (*tilge kaytuu*; "Zoomers" kept as English-media nickname).
- All volumes: 20 links retargeted to [[Iradi language revival]] (plus two reworded phrases).
- newlore.md: appended "Iradi Language Revival (renamed)".

# Change log: consistency clean-up (2026-10-12)
Requested by the user: fix inconsistencies flagged during the fleshing-out batch.
- HRW 2022 report title unified as "Civil Liberties and Judicial Dualism in Divided Irad" (11 references still read "Divided Transoxiana", the title already chosen in the 2026 wiki review).
- Vol3 Diz: Iradi name of the Talas citadel is *Köhne Diz* (was *Eski Talas Diz-Shahary*), matching the Old Talas Citadel Quarter article.
- Vol1 Bektur Zhumabek uulu: siege of Talas "between April and June 1992" (siege ran 10 April – 18 June; Operation Starlight ended the war in August, which stands).
- Vol1 Democratic Party of Irad and Vol2 governor biography: "Russophone industrial lists" replaced by the Labor Party of Irad (and Jer-Suu in the DPI article), matching the new party articles.

# Change log: fleshing-out batch, phases 1 and 2 (2026-10-12)
Requested by the user: write up all brainstormed ideas in two phases. Phase 1 (present-day politics and society): 2027 election, ATR clans and the kurultai, smuggling and crime, the Talas Herald, marriage. Phase 2 (culture and connections): calendar and dialects, glacier retreat, Iradis in Russia and the returnees, Mexicans in Irad and Semiz, literature, football, architecture.
- Irad_Wiki_Vol2_C_Class.md: 18 new C-class articles (count 150 -> 168):
  - 4.151 2027 Iradi gubernatorial election
  - 4.152 Clans of the Autonomous Tribal Regions
  - 4.153 Kurultai (Iradi Freedom Society)
  - 4.154 Smuggling across the Qara-Chik Line
  - 4.155 Crime in Irad
  - 4.156 Talas Herald
  - 4.157 Marriage in Irad
  - 4.158 Iradi calendar
  - 4.159 Dialects of Iradi
  - 4.160 Glacier retreat in Irad
  - 4.161 Iradis in Russia
  - 4.162 Mexicans in Irad
  - 4.163 Semiz
  - 4.164 Iradi literature
  - 4.165 Kemel Ishakov
  - 4.166 Football in Irad
  - 4.167 Kara-Ak derby
  - 4.168 Architecture of Irad
- Returnees: new section "Returnees and the territorial elite" in Iradi Americans.
- 60 cross-link edits across Vol1, Vol2 and Vol3 linking existing articles to the new ones.
- newlore.md: one appended section per topic.
- SKILL.md: article count 793 -> 811.
- Name overlaps resolved: Tulpar Talas supporters' group named Jolbors (not "Kök Jal", which is the title of Kemel Ishakov's 1959 story; the Kökjal clan shares the wolf epithet). Herald citation 'Twenty years of la Colonia' unified.

# Change log: Nuevo Talas renamed Semiz (2026-10-12)
Requested by the user: a more realistic name for the Mexican enclave.
- All volumes and newlore: "Nuevo Talas" -> "Semiz" (13 mentions); first mentions in Talas (Neighborhoods) and Sukarne Irad Complex explain the names Otkormochny, la Colonia and Meksikanka. Herald citation retitled 'Twenty years of la Colonia.'
- newlore.md: appended "Semiz: the Mexican District of Talas".

# Change log: Communist Party / Labor Party consistency fix (2026-10-12)
Found while reviewing article titles: the Labor Party article said the interim administration barred the CPI from elections, but the Communist Party of Irad article says it was never banned and simply ceased to function.
- Irad_Wiki_Vol2_C_Class.md: Labor Party of Irad (Foundation) now matches; Communist Party of Irad (After 1992) names the Labor Party as where former members went.

# Change log: Virgin Lands campaign, beef and field maize (2026-10-12)
Requested by the user: the Virgin Lands campaign targeted Irad and was relatively successful; it founded the beef industry; field maize was introduced as feed and is still grown.
- Irad_Wiki_Vol2_C_Class.md: new article 4.150 Virgin Lands Campaign in Irad (C-class count 149 -> 150); Agriculture in Irad (History, Crops, Livestock); Iradi SSR (settlers); Sukarne Irad Complex (site).
- Irad_Wiki_Vol1_Core.md: Economy of Irad (Agriculture); Culture (Cuisine overview; Cattle and bovine omens).
- newlore.md: appended "Virgin Lands Campaign, Beef and Field Maize".
- SKILL.md: article count 792 -> 793.

# Change log: The White Rider Shows the Way, image supplied (2026-10-12)
Requested by the user: supplied an image of Yusup Ayyubov's painting.
- Irad_Wiki_Vol2_C_Class.md: Yusup Ayyubov, description of the painting rewritten to match the image (Janyl mounted on a dark horse, not kneeling).
- newlore.md: painting description added to the Yusup Ayyubov entry.
- Wiki: image added as lead of "Yusup Ayyubov" and in the Irad article's Etymology section.

# Change log: Yusup Ayyubov is a painter; actor renamed Almaz Sarybaev (2026-10-12)
Requested by the user: Yusup Ayyubov was a painter who lived through the Soviet revolution (modeled loosely on Grigory Choros-Gurkin); rename the actor.
- Irad_Wiki_Vol2_C_Class.md: 4.3 retitled Almaz Sarybaev (actor), with all links and cast lists (Nurlan Sadikov, Desert Sun's Rebellion, Rise of Glory, Zarina); new article 4.149 Yusup Ayyubov (painter); C-class count 148 -> 149.
- Irad_Wiki_Vol1_Core.md: Cinema (Desert Sun's Rebellion lead); Irad etymology (the painting); Culture, Visual arts (painter).
- Irad_Wiki_Vol3_Start_Stub.md: Irad Palace of Art (collection); The 1937 NKVD Clerical Purges (lay victim).
- baselore.md: Desert Sun's Rebellion "starring Almaz Sarybaev" (rename requested by the user).
- newlore.md: appended "Yusup Ayyubov the Painter; Actor Renamed".
- SKILL.md: article count 791 -> 792.

# Change log: the Iradi cross (2026-10-12)
Requested by the user: the bare cross rising from a lotus is the canon Iradi cross.
- Irad_Wiki_Vol2_C_Class.md: new article 4.148 Iradi Cross (C-class count 147 -> 148); Kümöch (parish seals) and Ruins of Old Iyık Janyl (cemetery) link it.
- Irad_Wiki_Vol1_Core.md: Religion in Irad (Folk Christianity) names it and the 1994 adoption.
- Irad_Wiki_Vol3_Start_Stub.md: Maryam Janyl (nun), congregation emblem.
- iradi_cross.svg: new drawing; SKILL.md file table and article count 790 -> 791.
- newlore.md: appended "The Iradi Cross".

# Change log: Iradi Christianity structure and the tribal malka (2026-10-12)
Requested by the user: use Burkhanism + Church of the East as a structural parallel (no in-world Burkhanist movement); the malka survives as a tribal tradition.
- Irad_Wiki_Vol2_C_Class.md: Kümöch Sacramental Bread, Background (malka survival as evidence) and new section "Holy leaven in the tribal regions"; reference 4.
- Irad_Wiki_Vol1_Core.md: Syro-Iradi Catholic Church (kümöch bullet mentions the malka); Religion in Irad (Folk Christianity: white/black symbolism, milk offerings, shamans, Revelation 19:11, bare cross, Janyl and Marian devotion; Interfaith: shared customs and identity-marking refusals).
- newlore.md: appended "Iradi Christianity: Structure, Symbolism and the Malka".

# Change log: former opposition parties Jer-Suu and Labor (2026-10-12)
Requested by the user: opposition parties that existed before the Second Civil War and were dissolved or made powerless.
- Irad_Wiki_Vol2_C_Class.md: new articles 4.146 Jer-Suu Party and 4.147 Labor Party of Irad (C-class count 145 -> 147); Politics "Parties and opposition" and Russos of Nurzhan (Politics) link both.
- Irad_Wiki_Vol1_Core.md: Elections in Irad (territorial-period opponents named; ISEZ section adds the 2008 ban and the 2010 Political Parties Act); Territory of Irad (Parties).
- Irad_Wiki_Vol3_Start_Stub.md: Elena Petrova (Labor list, then civic list).
- newlore.md: appended "Former Opposition Parties: Jer-Suu and Labor".
- SKILL.md: article count 788 -> 790.

# Change log: Gendarmerie name origin (2026-10-12)
Requested by the user: the name "gendarmerie" is a Russian loanword (not French or Turkish).
- Irad_Wiki_Vol2_C_Class.md: Republican Gendarmerie of Irad, new "Name" section and reference 10.
- newlore.md: appended "Name of the Republican Gendarmerie".

# Change log: Mor-Pop groups Karakush and Altyn Muuz (2026-10-12)
Requested by the user: two Mor-Pop groups, one popular with a breakout single that had limited success in Korea and the Korean diaspora (a one-hit wonder outside Irad), one niche and cheesy that never got popular outside Irad.
- Irad_Wiki_Vol3_Start_Stub.md: new Start-Class articles #56 Karakush (Group) and #57 Altyn Muuz (Group) after Mor-Pop; later Start-Class articles renumbered +2; section count 224 -> 226; Culture, Arts & Folklore 42 -> 44; Mor-Pop article links both.
- newlore.md: appended "Mor-Pop Groups: Karakush and Altyn Muuz".
- SKILL.md: article count 786 -> 788.

# Change log: Mor-Pop as "dark K-pop" (2026-10-12)
Requested by the user: Mor-Pop is similar to "dark K-pop" but with Mor-Wave's usual Turkic pagan imagery; K-pop is also popular in Irad.
- newlore.md: appended "Mor-Pop as \"Dark K-Pop\"; K-Pop in Irad" (supersedes the love-and-city-life description of Mor-Pop lyrics).
- Irad_Wiki_Vol3_Start_Stub.md: Mor-Pop article rewritten (idol-group model, K-pop following in Talas and Nurzhan, Koryo-saram promoters, pagan imagery, clergy objections); new reference 3.
- Irad_Wiki_Vol2_C_Class.md: Mor-Wave (Subgenres) and Music of Irad (Mor-Wave and its offshoots) Mor-Pop entries.
- baselore.md left as is ("commercial danceable synth-pop" still fits).

# Change log: lore aligned with the wiki maps (2026-10-11)
Requested by the user: where the maps and the lore disagreed, the maps win.
- Irad_Wiki_Vol1_Core.md: Irad (Transport) and Transport in Irad (Rail transport): railway about 540 -> 580 km. Energy in Irad (Exports): feeder runs northeast across the Chu plain (was northwest across the lower Chu plain). Transport in Irad (Pipelines): Nurzhan Petroleum Pipeline about 118 -> 90 km. Iyık Janyl article and cities table: 18 -> 20 km from Tash-Kömür.
- Irad_Wiki_Vol2_C_Class.md: Northern Export Feeder (Route): runs northeast.
- Irad_Wiki_Vol3_Start_Stub.md: Nurzhan Petroleum Pipeline: about 90 km.
- newlore.md: appended "Map Alignment: Transport and Oil Figures"; Iyık Janyl entry 18 -> 20 km.

# Change log: FreeIrad.org added (2026-10-11)
Requested by the user: add an entry about https://freeirad.org/.
- Irad_Wiki_Vol2_C_Class.md: new article 4.145 FreeIrad.org (Media & Broadcasting); C-class count 144 -> 145.
- newlore.md: appended "FreeIrad.org (October 2026)".
- SKILL.md: article count 785 -> 786.
- The article names real people only as the site's existing subjects (the Bush family) and describes its other claims about real people generically.

# Change log: Iyık Janyl moved to the Fergana foothills (2026-10-11)
Requested by the user: Iyık Janyl now lies in the Fergana foothills, within the Lower Naryn District (the ISEZ's southern salient).
- newlore.md: appended "Iyık Janyl Relocated to the Fergana Foothills" (location, road, climate, setting; supersedes the Talas Alatau placement).
- Irad_Wiki_Vol1_Core.md: Iyık Janyl article (lede, since 1992, Geography, Climate, Demographics minorities, Transport); Siege of Talas refugees; Administrative divisions (cities table, Lower Naryn row and description); Irad article district table; Geography of Irad (location, climate list); Transport in Irad (road list).
- Irad_Wiki_Vol2_C_Class.md: Fergana Gateway (medieval pilgrims), Fergana Mountain Transit Highway (branch road to Iyık Janyl), ISEZ district table, Qara-Chik line southern sector, Archbishopric (territory), Tash-Kömür (salient's largest city is now Iyık Janyl).
- Irad_Wiki_Vol3_Start_Stub.md: Diz-i Safid and Khunuk Creek (Fergana Range foothills), Father Toma Alimbek ("high valleys above").
- Unchanged on purpose: Janyl's cave in the Talas Alatau (legend), Kokand and Fergana Oblast history, the 1967 film shot "in the Talas Alatau and near Iyık Janyl".

# Change log: Tajikistan removal (2026-10-10)
Requested by the user: remove Tajikistan claims and border; footprint = Talas + Jalal-Abad regions (Kyrgyzstan), N/W Fergana Valley (Uzbekistan), parts of Turkistan + Jambyl (Kazakhstan).
- baselore.md: claimants "all four" -> three; added Land Borders line (KZ, UZ, KG; none with TJ/CN/AF; doubly landlocked); pipeline no longer routed through an "Irad-Tajikistan-Afghanistan-Pakistan" adjacency.
- newlore.md: appended "Territorial Footprint & Borders" (supersedes earlier border/claimant text).
- Irad_Wiki_Vol1_Core.md: infobox border sentence; "all four surrounding republics" (x2: lines ~101, ~624) -> three.
- Irad_Wiki_Vol2_C_Class.md: El-Choro frontier list now includes Kyrgyzstan.
- Irad_Wiki_Vol3_Start_Stub.md: "2021 Afghan Border Alert" -> "2021 Regional Security Alert" (Irad has no Afghan frontier).
- Kept: Tajiks as a ~1% minority; Taliban-resurgence pipeline stall.
- SKILL.md / Irad_Wiki_Original.md: original article saved as Markdown and registered in the file table.

# Follow-up (2026-10-10, later)
- Footprint corrected: northern and EASTERN Fergana Valley (not western). Border directions updated: KZ north/northwest, UZ west/south, KG east/southeast.
- Renamed out-of-footprint antimony sites: Sary-Tash -> Sary-Bulak (mine; STAW -> SBAW), Kadamjay -> Chatkal (smelter, mill, tailings, rare-earth facility, extraction zone, "Chatkal-Irad" combine), incl. Cyrillic forms. Wiki already placed them in the southern Chatkal / Talas Alatau foothills.
- Vol2 Sary-Bulak article: antimony concentrate now goes by rail through Kazakhstan to China (Irad has no Chinese frontier).
- newlore.md: added "Real-World Features Within the Footprint" (Toktogul/Naryn, Mailuu-Suu, Arslanbob/Sary-Chelek, Battle of Talas 751, Fergana rim).
- Fergana footprint amended: large Fergana cities (Namangan, Andijan) excluded; rural/foothill rim only (user decision, 2026-10-10).
- Toktogul decision (user approved Inguri-style split): newlore.md "The Toktogul Complex and the Naryn Water and Power Protocol"; baselore.md ceasefire bullet + Hydropower bullet; Vol1 transit-bottleneck bullet now notes electricity leverage.
- New Vol2 articles 4.99 Toktogul Hydroelectric Complex and 4.100 Naryn Water and Power Protocol (neighbor friction: Uzbekistan, Kazakhstan, Kyrgyz objection, 2027 renewal vs. Toktarov's absence). Vol2 count 98 -> 100.
- Updated: Vol2 Qara-Chik (new "Naryn Corridor" section), El-Choro, Trans-Irad Pipeline (route now exits via Kyrgyz territory, not an Irad-China border); Vol3 stub 207; Vol1 Hydropower bullet.
- Removed real UN Security Council resolution number (1762, an unrelated real resolution) from 6 citations/mentions; kept title and date.
