#!/usr/bin/env python3
"""Builds freeforum/CHARACTERS.md: every FREEFORUM sample member with voice notes and stats from the imported history."""
import json, collections

import os
ROOT = os.path.dirname(os.path.abspath(__file__)) + '/'
V = [json.load(open(ROOT + 'history_v1.json')), json.load(open(ROOT + 'history_v2.json'))]

# Seed sample threads (forum/inc/seed.php), not in the history files
SEED_POSTS = [('FREEIRAD', '2019-05-02 20:00', 'Announcements', 'FORUM RULES - READ BEFORE POSTING')] + \
    [(u, d, 'The Erasure', 'POST YOUR EMPTY MAP (screenshot thread)') for u, d in [
        ('Kobozev_Kid', '2019-04-14 21:37'), ('UncleTemir_Chicago', '2019-04-15 06:02'), ('mor_wave_forever', '2021-06-09 01:44'),
        ('Kobozev_Kid', '2021-06-09 08:15'), ('NotADPIagent', '2022-03-03 14:20'), ('Kenkol_Rider', '2025-02-19 19:51'),
        ('zhayloo_girl', '2026-10-13 18:02')]] + \
    [(u, d, 'Leaks & Rumours', 'Tulparcoin megathread: DO NOT GIVE THEM YOUR NUMBER') for u, d in [
        ('Kobozev_Kid', '2026-09-22 23:48'), ('UncleTemir_Chicago', '2026-09-23 04:10'), ('NotADPIagent', '2026-09-23 09:31'),
        ('Kenkol_Rider', '2026-09-23 12:06'), ('mor_wave_forever', '2026-09-30 22:40'), ('FREEIRAD', '2026-10-08 20:15'),
        ('zhayloo_girl', '2026-10-12 21:09')]]

NOTES = {
 # core cast
 'FREEIRAD': ('admin', 'The site operators. Terse, official ALL-CAPS announcements, dry humour. Answers Temir\'s feedback forms with "STILL NO." Refuses to rule on song vs songs, forever.'),
 'Kobozev_Kid': ('mod', 'Nurzhan refinery worker (shift B), Russo, moderator since 2016. Dry and fair. "My grandmother was born in a city that does not exist." Answers NotADPIagent with "No."'),
 'UncleTemir_Chicago': ('core', 'Diaspora uncle, Alatau Heights 1997-2007, now Chicago. Iradi American Association picnic organiser, long earnest posts, feedback forms for everything. Owns the 1994 VHS ("it was the song"), screens it yearly in the Mission hall. Turned 70 on 17 Jan 2023. Ak_Shumkar\'s nemesis 2012-2016, gracious after the ban.'),
 'zhayloo_girl': ('core', 'TSU student, lowercase, protest generation ("october 2023. we were there."). Second-year in Oct 2023; defended her thesis 18 Jun 2026 (supervisor made her write "gathering" instead of "protest" 41 times).'),
 'Kenkol_Rider': ('core', 'Chatkal horse trader. Short dry sentences and horse metaphors: "horses do not lie". His mare carried his father down Kenkol Pass in a 2005 storm.'),
 'NotADPIagent': ('core', 'Suspiciously polite pro-government poster ("Have a nice day. Remember to vote."). Asks who is online and from which city; everyone suspects him. Probation Mar 2022. Beige jacket.'),
 'mor_wave_forever': ('core', 'Bishkek music nerd, lowercase, "lol", tüntolk superfan ("Jolchu on repeat since 1999").'),
 'Ak_Shumkar': ('legend', 'Member no. 3, first night (Irad Day 2011). Talas Old City truther, CAPS, signs "WAKE UP IRAD". Funny and warm early on, increasingly aggressive; feud with UncleTemir 2012-16; probation 2015; BANNED 2016-08-27 after the "better than the song(s)" meltdown. Delivered bread on the Alatau Heights route 2002-06. Remembered fondly; "Ak would have had a field day."'),
 'Ak_Shumkar_Returns': ('legend', 'Obvious alt, joined 2018-04-01, banned the next day after posting about the song in caps.'),
 'JANYL_watch': ('core', 'First moderator (2011-Apr 2019), churchgoer from Iyık Janyl, calm, "Read the rules." Gender never stated: refer to JANYL neutrally. Returns occasionally.'),
 'Erbol8645': ('core', 'Webmaster of the Irad Internet Portal / IRAD WEBRING on attelkom.net. Enthusiastic, bad at tech, "sorry if broken". Price table and barter table always "coming soon". Birthday 9 Aug (34 in 2014). His FREECHAT button is a running-horse gif he can\'t change.'),
 'kino_talasfilm': ('core', 'Film buff, Talasfilm westerns, Nurlan Sadikov; "Desert Sun\'s Rebellion is the greatest film ever made". Dubbing/lip-sync expert ("It is not a conspiracy. It is a mouth.").'),
 'olddog_1992': ('legend', 'Survivor of the 1992 siege of Talas. Short, wise posts typed slowly; everyone respected him. "Ask the old man" thread. Died peacefully Feb 2021; grandson told the forum 4 Mar 2021. No posts after 2021-02-10.'),
 'Koryoin_Lena': ('core', 'Koryo-saram from Talas, food, sharp tongue, calms fights. "laghman is not noodles, it is a philosophy" (won that argument). Her aunt\'s laghman stall at Bazar-i Kalan (free tea for couriers every 12 Oct, half price for TSU students).'),
 'Ruslan_not_that_one': ('core', 'Russo from Nurzhan, Neftchi Nurzhan fan, was at the 2014 NurGaz Stadium riot (lost his left shoe on a tram wire). "No, not THAT Ruslan."'),
 'semiz_taco': ('core', 'Mexican-Iradi from Semiz, cheerful, Spanish-Iradi mix, "taco de Talas". Has never been to Mexico.'),
 'Gulya_Toronto': ('core', 'Toronto diaspora, family from Kara-Buura, practical, backs Temir. Daughter 11 in Feb 2025; mother became Canadian in 2026. Saturday Iradi class in a Ukrainian parish hall.'),
 'seminarian_x': ('core', 'Left St. Ephrem seminary, kept the faith. Church lore; laughs at Grail theories. "No, we do not have the Grail."'),
 'Bishkek_Rail': ('core', 'Polite Kyrgyz neighbour who reads the forum; dragged into partition arguments.'),
 'Chatkal_Shepherd': ('core', 'Posts rarely from the summer pasture on slow internet; long thoughtful posts; clan perspective; distrusts Talas politicians since 2007. Rode with the Popular Front into Talas in 2007.'),
 'olddog_grandson': ('minor', 'olddog_1992\'s grandson; posted once, 4 Mar 2021, to tell the forum.'),
 # batch 1 extras
 'kymyz_and_coffee': ('regular', 'Talas office worker ("office plankton"), passes on tabloid gossip with labels.'),
 'TashKomur_Teacher': ('minor', 'Iradi language teacher (female), 22 years teaching in 2016. "A comma is not a conspiracy." Ruled on the dub: the actress swallows "-lar".'),
 'Dastgoh_Dima': ('minor', 'Neftchi ultra (Vyshka group), joined the night of the 2014 riot.'),
 'Lisa_was_right': ('minor', 'Lurker who registered during the 2016 meltdown; posts very rarely, as a running joke.'),
 'statute_nerd': ('regular', 'Pedantic Talas lawyer ("Section 4(2) enjoyer"). Keeps a running score of cousins_wife_says\' rumours (2.5/11 by Aug 2022). Points out the DPI in the Herald is the press office, not the party.'),
 'liberty_lad_88': ('minor', 'Jason Ilyasov fanboy; probation Sep 2026 for shilling Tulparcoin.'),
 'fergana_walnut': ('minor', 'Muslim from Arslanbob; his 2020 Horses post led to the board\'s "no barbarian / Muslim food" rule.'),
 'frame_by_frame': ('minor', 'Amateur video analyst (joined 2024), always cites the tech monitors on the Governor\'s recordings; never claims certainty.'),
 'surgut_shift': ('minor', 'Nurzhan shift worker in Surgut, Russia.'),
 'white_headscarf': ('minor', 'Ak Jooluk campaign volunteer from Kara-Buura.'),
 'podmoskovye_nurzhan': ('minor', 'Nurzhan Russo builder near Moscow on a Kyrgyz passport.'),
 'golden_doran': ('regular', 'Akyel fan ("Akyel or nothing"), Hippodrome results; names a mare he only sees at the track Altyn Tang.'),
 'kymyz_kid': ('regular', 'Teen from Kyzyl-Adyr when he joined (2014, aged 12), ulak fan, runs the counting game. Finished school Jun 2019, vet training, works at a clinic near the Hippodrome from Feb 2024, shared flat in Talas Mar 2026.'),
 'talas_tapes': ('regular', 'Cassette collector; rewinds the White Stallion tapes every 16 November.'),
 'Nurzhan_Nights': ('regular', 'Veteran of the original Mor-Wave boiler-room scene in Nurzhan (Dastgoh).'),
 'TD_fan_Ohio': ('regular', 'American who found the forum via "Dream of Living" (True Detective S4, 2024); learning Iradi words; visited Talas Oct 2025; went to Chicago events in 2024-25.'),
 # batch 2: leaks
 'depo_Nurzhan': ('regular', 'Old Russo railwayman, Labor Party member 1993-2011, says "comrades" ironically, keeps his party card in a drawer.'),
 'KaraOi_cousin': ('regular', 'Every rumour comes from "my cousin" (caterer at Kara-Oi, print shop, deputy\'s driver). "Yes, the cousin is real."'),
 'Chu_trucker': ('regular', 'Night lorry driver on the Chu road. "Cement doesn\'t lie." Counted the Boz-Korgon trucks.'),
 'source_please': ('regular', 'Talas sceptic who wants the opposition to get its facts right ("citation needed"); Ak_Shumkar\'s main sparring partner after Temir.'),
 'KaraBulak_neighbor': ('minor', 'Lives under the air base flight path, sells kymyz to contractors\' drivers. "I\'ve seen a lot of maize."'),
 'OneDebate_bingo': ('minor', 'Makes the weekly OneDebate bingo cards (Thursdays 21:00).'),
 'cousins_wife_says': ('regular', 'Cheerful tabloid source ("my cousin\'s wife works in the Mejlis canteen"), usually wrong; statute_nerd keeps her score.'),
 'basewatcher_KB': ('minor', 'Kara-Bulak resident who counts tankers on the base road ("I only count"); FREEIRAD: "PLEASE DO NOT POST THE NOTEBOOK".'),
 'western_wells': ('minor', 'Terse herder on the western frontier, posts from a truck stop. "Numbers make revenge."'),
 'Kokjal_nephew': ('minor', 'Young man from the Toktogul basin, lowercase, first followed politics during the 2022 Long Kurultai.'),
 'chu_dacha_pensioner': ('regular', 'Russo pensioner, 71, dacha on the Chu road; counts lorries and helicopters. "I only report what drives past my tomatoes."'),
 'pixel_steppe': ('minor', 'Almaty hobbyist reading public satellite images; careful to a fault. "A roof is a roof."'),
 'precinct_insomniac': ('minor', 'Western Talas teacher who sat on a 2023 precinct commission; plans her mother\'s "illness" for 2027.'),
 'foggy_bottom_iradi': ('minor', 'Second-generation paralegal in Arlington VA who reads US lobbying registrations; "no filing yet"; never starts rumours.'),
 'terminal_tally': ('minor', 'Freight clerk in the Kara-Buura corridor. "Paperwork is destiny."'),
 # erasure
 'transit_almaty': ('minor', 'Engineer on rotations abroad; dry stories about flying home on Kyrgyz bookings via Almaty.'),
 'dotted_line_ok': ('regular', 'Calm map-data sceptic: "it\'s just non-recognition". By 2025 admits non-recognition isn\'t boring any more.'),
 'toponym_patrol': ('regular', 'Adds Iradi place names to map services and tallies what survives. Signature "Added: 312. Survived: 9."'),
 'geog_student_tsu': ('minor', 'Student in the TSU geographer\'s department; defends the "never entered" quote ("read the whole quote").'),
 'chalk_and_paste': ('minor', 'Young lowercase activist who joined after the Feb 2025 marches; chalk, wheatpaste, stickers.'),
 # cities
 'Route_31_Driver': ('regular', 'Drives marshrutka 31 (Old City to Alatau Heights). Gruff and deadpan: "There are ten drivers on the 31. They are all my cousins." "seats are a theory".'),
 'TSU_dorm5': ('minor', 'Lowercase TSU sociology student from 2012; failed history over the siege date; graduated 2016 into a call centre.'),
 'cul_de_sac_kid': ('regular', 'Grew up in Alatau Heights (Amerikanka), Talas American School 2013; American slang, defensive and sincere; dad is a mechanic at the base.'),
 'sim_card_seller': ('minor', 'Runs the Attelkom kiosk at Bazar-i Kalan, row 3; knows every tariff. "I am only the kiosk."'),
 'toi_tamada': ('minor', 'Wedding MC, posts at 3am, tracks what weddings cost. "I am the statistics office."'),
 'pilgrim_guesthouse': ('minor', 'Older woman with a three-room guesthouse in Iyık Janyl; knows JANYL_watch.'),
 'orange_black_67': ('regular', 'Old Neftchi fan from Navbahor; still says "Neftyanik"; west stand by the old clock. "I report only."'),
 'navbahor_mama': ('regular', 'Nurzhan mother of three, Russian-flavoured English; keeps the heating thread going every year.'),
 'taxi_bek_talas': ('regular', 'Talas night taxi driver; short reports of what passengers say; signs off "Cash also accepted."'),
 'tunduk_barista': ('minor', 'Owns the Tündük café near TSU; takes "som, cash, card, napkin"; the 2023 napkin IOUs (140 written, 131 repaid).'),
 'dorm_seven': ('minor', 'First-year applied maths student (2024), lowercase, dorm 7\'s ice-or-lava shower; zhayloo_girl showed his group the forum.'),
 # valleys
 'kamaz_on_kenkol': ('regular', 'Half-Russo truck driver on the Kenkol run; "bratan", "nu"; runs the winter road thread. "I carry flour."'),
 'besh_tash_vet': ('regular', 'Rural vet working both sides of the line, family up the Besh-Tash; explains the valleys to city people. "You do not hand the second government the same pen."'),
 'altyn_say_panner': ('minor', 'Evasive, joking placer-gold panner who supports the mercury ban. "Zero grams, officer."'),
 'shyrdak_needle': ('minor', 'Woman in an Ak Kiyiz felt workshop, posts on her niece\'s phone; slow, proud, talks prices.'),
 'boztorgoy_cattle': ('minor', 'Blunt steppe herder from the "cattle clan"; cattle as a bank; teases mountain clans as poets.'),
 # diaspora
 'istanbul_simit': ('regular', 'Wry Istanbul translator; keeps the "Rumours N, Orozbekov 0" score; never confirms a sighting.'),
 'almaty_kassa': ('minor', 'Works a money-transfer window in Almaty; numbered practical advice ("never give the code").'),
 'semiz_en_culiacan': ('minor', 'Semiz-born agronomy student in Culiacán: "el ruso" there, "the Mexican" at home.'),
 'kitchen_iradi': ('minor', 'Chicago-born son of a Talas nurse, "kitchen-level" Iradi, relearning it with his grandmother.'),
 'night_nurse_houston': ('minor', 'Talas Regional nurse now in Houston; tired, posts from the break room.'),
 # horses
 'Marat4086': ('regular', 'Built the Akyel Syndicate website in 1998 (webring), left 2001. "I only made the buttons." The catalogue is coming "In 1999."'),
 'bluegrass_doran': ('minor', 'Polite American in Kentucky with an Akyel mare, Sunny (colt born 2017).'),
 'tote_window_7': ('regular', 'Cynical punter at the Hippodrome\'s Window 7 since 1986. "The favourite always coughs."'),
 'beef_or_lamb': ('minor', 'Blunt kazy maker on the Bazar-i Kalan meat row; says Homer costs him a week of trade every August.'),
 'berkutchi_uulu': ('minor', 'Terse eagle hunter from the Talas Alatau foothills; released Kara-Kanat in 2024, new bird Boz.'),
 'microdistrict_rider': ('minor', 'Lowercase city girl taking riding lessons, asks the dumb questions; lesson horse Toyota (retired by 2026).'),
 # music
 'lyric_footnotes': ('regular', 'Careful Talas translator who numbers his footnotes.'),
 'hamburg_nachtwelle': ('minor', 'German club DJ who found tüntolk; slightly German English, deadpan.'),
 'ride_for_karaoke': ('minor', 'Sings "Ride for Talas" at karaoke every Friday!!!'),
 'alto_from_IJ': ('minor', 'Church choir alto from Iyık Janyl who loves Mor-Wave; gentle, torn. "Both are true."'),
 'Kanykei5093': ('minor', 'Owner of the 2000 tüntolk fan page on the webring, grown up; lowercase, terse, mysterious ("on purpose.").'),
 # off-topic
 'pentium_266': ('regular', 'Dry, precise Talas programmer ("Pascal since 1997"), fixes things for Erbol; implied (never named) author of the TSU Computer Club page. "FrontPage is for lamers."'),
 'sumolok_spoon': ('minor', 'Warm Muslim poster from Bazar-Korgon, Uzbek at home; runs the yearly Nooruz thread; his aunt controls the spoon.'),
 'night_nurse_Talas': ('minor', 'Tired, kind nurse who only posts 2-5am. "drink water. go to sleep."'),
 'tyotya_Valya': ('regular', 'Bossy Russo pensioner from Navbahor, "detka", "nu", "koroche"; feeds everyone.'),
 'pixel_tulpar': ('regular', 'Talas teen gamer (2016), lowercase, bumps old threads ("lvl 14 lurker").'),
 'periodic_babushka': ('minor', 'Retired Nurzhan chemistry teacher (account made by her grandson, 2020); full sentences, corrects cooking, signs off "Kisses."'),
 'kuble_memes': ('minor', 'TSU student meme-maker; describes memes as "[image: ...]", deadpan.'),
}

def main():
    users = {}
    for v in V:
        for u in v['users']:
            if u['username'] not in users or not u.get('existing'):
                users.setdefault(u['username'], {}).update({k: x for k, x in u.items() if x not in (None, '')})
    posts = collections.defaultdict(list)
    threads_by = collections.defaultdict(collections.Counter)
    started = collections.defaultdict(list)
    for v in V:
        for t in v['threads']:
            started[t['posts'][0]['user']].append(t['title'])
            for p in t['posts']:
                posts[p['user']].append((p['at'], t['board']))
                threads_by[p['user']][t['title']] += 1
        for a in v['append']:
            for p in a['posts']:
                posts[p['user']].append((p['at'], None))
                threads_by[p['user']][a['thread']] += 1
    for u, d, b, t in SEED_POSTS:
        posts[u].append((d, b)); threads_by[u][t] += 1

    order = {'admin': 0, 'mod': 1, 'legend': 2, 'core': 3, 'regular': 4, 'minor': 5}
    names = sorted(users, key=lambda n: (order.get(NOTES.get(n, ('minor',))[0], 9), users[n]['joined']))
    missing = [n for n in names if n not in NOTES]
    out = ['# FREEFORUM characters', '',
           'Every sample member of the freeirad.org forum (FREEFORUM, called FREECHAT until 13 Oct 2026), with voice notes',
           'and stats from the imported history. Use this before writing more posts: keep each voice, respect join dates,',
           'bans and deaths, and continue the running jokes. Rebuild with characters.py in this folder',
           '(it reads history_v*.json here).', '',
           'Sample members cannot log in (no usable password). The live admin and real sign-ups are not listed here.', '',
           '## Hard timeline facts', '',
           '- Forum opened 11 Mar 2011 (Irad Day). Ak_Shumkar was member no. 3, the first after the admins.',
           '- JANYL_watch: moderator 2011 to Apr 2019 (retired). Kobozev_Kid: moderator from 2016.',
           '- Ak_Shumkar: probation Nov 2015, BANNED 27 Aug 2016 (the song/songs meltdown). Ak_Shumkar_Returns banned 2 Apr 2018. No posts by either after their bans.',
           '- olddog_1992 died peacefully Feb 2021 (no posts after 10 Feb 2021); grandson posted 4 Mar 2021; "Ask the old man" locked as a memorial 8 Mar 2021.',
           '- NotADPIagent: probation Mar 2022. liberty_lad_88: probation Sep 2026 (coin shilling, under the 24 Sep 2026 no-coin rule).',
           '- Leaks & Rumours titles must start [RUMOUR], [HEARD] or [SEEN] from 30 Aug 2024.',
           '- Nov 2012: first Attelkom block of the site (9 days), hosting moved offshore. Jul 2014: second outage. "Blocked again" 2017.',
           '- The front-page shoutbox (with its "ü bug") closed on 13 Oct 2026, when FREECHAT was relaunched as FREEFORUM.',
           '- Running jokes: Temir\'s feedback forms ("STILL NO."); "it was the song" vs "songs" (FREEIRAD never rules);',
           '  Kobozev_Kid answering NotADPIagent "No."; Erbol\'s "coming soon" tables and broken webring; laghman is not noodles;',
           '  Ruslan\'s shoe on the tram wire; statute_nerd\'s score of cousins_wife_says; "Rumours N, Orozbekov 0";',
           '  bread prices (Talas 1.20 som in 2012, about 2.00-2.50 by 2022-26).', '']
    cur = None
    heads = {'admin': 'Staff', 'mod': 'Staff', 'legend': 'Legends (banned or gone)', 'core': 'Core regulars',
             'regular': 'Regulars', 'minor': 'Occasional posters'}
    for n in names:
        tier = NOTES.get(n, ('minor', ''))[0]
        h = heads[tier]
        if h != cur:
            out += ['', '## ' + h, '']; cur = h
        u = users[n]; ps = sorted(posts.get(n, []), key=lambda x: x[0])
        boards = collections.Counter(b for _, b in ps if b)
        top = ', '.join(f'{b} ({c})' for b, c in boards.most_common(3))
        th = ', '.join(f'"{t}"' for t, _ in threads_by[n].most_common(3))
        flags = []
        if u.get('banned') or n in ('Ak_Shumkar', 'Ak_Shumkar_Returns'): flags.append('BANNED')
        meta = [f'joined {u["joined"][:10]}']
        if u.get('title'): meta.append(f'title "{u["title"]}"')
        if u.get('location'): meta.append(f'location {u["location"]}')
        out.append(f'### {n}' + (' (' + ', '.join(flags) + ')' if flags else ''))
        out.append('- ' + '; '.join(meta))
        if u.get('signature'): out.append(f'- signature: "{u["signature"]}"')
        out.append('- voice: ' + NOTES.get(n, ('', 'TODO'))[1])
        if ps:
            out.append(f'- in the forum: {len(ps)} posts ({ps[0][0][:10]} to {ps[-1][0][:10]}); profile post count {u.get("post_count", "?")}; mostly {top}')
            out.append(f'- most active in: {th}')
        out.append('')
    open(ROOT + 'CHARACTERS.md', 'w').write('\n'.join(out) + '\n')
    print(len(names), 'members written;', 'missing notes:', missing)

main()
