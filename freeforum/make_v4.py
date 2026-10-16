#!/usr/bin/env python3
"""FREEFORUM history batch 4: older posts that link to the other Irad sites (natural cross-linking).
python3 freeforum/make_v4.py  ->  freeforum/history_v4.json (copy to freeirad repo forum/inc/history_v4.json)

Rules kept: links only to pages that exist and existed at the post's date (talasherald.com / iradone.com after
the 2015-16 move off .ir.ad; a few pre-2016 posts carry the old, now dead, talasherald.ir.ad links, fixed later);
members only post after they joined; appended posts fall inside or after their thread."""
import json, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
H = "https://talasherald.com/archive/"
T = "https://mjsbroadbent.github.io/IradTimes/"
OLDH = "http://www.talasherald.ir.ad/"

# --- existing threads (exact titles) and members' join dates from the earlier batches
threads, joins = {}, {}
for f in ["history_v1.json", "history_v2.json", "history_v3.json"]:
    d = json.load(open(HERE / f, encoding="utf-8"))
    for t in d["threads"]:
        threads[t["title"]] = (t["board"], t["posts"][0]["at"], t["posts"][-1]["at"])
for m in re.finditer(r"^### ([^\s(]+).*?\n- joined (\d{4}-\d{2}-\d{2}(?: \d{2}:\d{2})?)", (HERE / "CHARACTERS.md").read_text(encoding="utf-8"), re.M | re.S):
    joins[m.group(1)] = m.group(2)


def title(prefix):
    hits = [t for t in threads if t.startswith(prefix)]
    assert len(hits) == 1, (prefix, hits)
    return hits[0]


def url(u, text):
    return f"[url={u}]{text}[/url]"


A = []  # (thread prefix, user, at, body, mod_note)
def a(prefix, user, at, body, note=""):
    A.append((title(prefix), user, at, body, note))


# ---------------------------------------------------------------- appended posts
a("Kara-Oi talks: they will walk out", "KaraOi_cousin", "2011-05-20 21:14",
  "MY COUSIN WAS RIGHT. Day two, they walked. Herald has it: " + url(OLDH + "2011/05/tribal-delegates-walk-out.html", "Tribal delegates walk out of unification talks") + "\n\nI accept apologies in this thread.")
a("Kara-Oi talks: they will walk out", "pixel_tulpar", "2019-10-03 16:40",
  "bumping because the link above is dead (lvl 14 archaeologist). herald moved off .ir.ad years ago, same article: "
  + url(H + "2011/tribal-delegates-walk-out-of-unification-talks.html", "talasherald.com/archive/2011/...") + "\n\ncousin was right in 2011. respect")
a("HEARD: Ruslan Toktarov to command", "KaraOi_cousin", "2012-03-18 10:05",
  "Not a rumour anymore. Herald profile this morning: " + url(OLDH + "2012/03/profile-eldest-son-gendarmerie.html", "The Governor's eldest son takes command of the Gendarmerie") + ". Cousin 3, everyone else 0.")
a("HEARD: Ruslan Toktarov to command", "Kobozev_Kid", "2020-02-15 03:12",
  "Mod note: using the maintenance weekend to fix dead Herald links. The profile above is here now: "
  + url(H + "2012/profile-the-governor-s-eldest-son-takes-command-of-the-gendarmerie.html", "Herald archive, March 2012") + ". If you find more dead .ir.ad links, report the post, don't start a new thread.")
a("Boz-Korgon: cement trucks on the Chu road", "Chu_trucker", "2012-06-13 23:50",
  "Now we know who the cement was for. " + url(OLDH + "2012/06/governors-family-boz-korgon.html", "Herald: Governor's family takes up residence at Boz-Korgon") + ".\n\nI drive. I see. I told you in September.")
a("Are they moving to Boz-Korgon?", "kymyz_and_coffee", "2023-03-04 09:20",
  "For the newcomers: they moved in years ago. Herald, June 2012: "
  + url(H + "2012/governor-s-family-takes-up-residence-at-boz-korgon.html", "Governor's family takes up residence at Boz-Korgon") + ". Chu_trucker called it from his cab in 2011, there's a thread. The question now is who ELSE is moving there.")
a("Term limit: they're going to remove it", "pentium_266", "2013-05-23 22:31",
  "The Times wrote this in March, before they went dark for two months: " + url(T + "archive/2013/a-term-without-end.html", "A Term Without End") + ". Read the last paragraph. They had the date almost exactly.")
a("FreeIrad blocked on Attelkom??", "kymyz_and_coffee", "2013-05-17 08:45",
  "Not only us. The Irad Times was grey since March too and they're back today: " + url(T + "archive/2013/we-are-back.html", "We are back") + ". Same grey page, same no letter. At least they can print on paper.")
a("Debate One is now \"OneDebate\"??", "OneDebate_bingo", "2017-09-15 21:58",
  "The Times has the whole story of the renaming and the new building: " + url(T + "archive/2017/a-new-home-for-iradone-and-a-new-name-on-the-door.html", "A new home for IradOne, and a new name on the door") + ". Free square on the card: \"the brand\".")
a("Kara-Ak derby thread", "Ruslan_not_that_one", "2016-06-18 19:15",
  "Times: Tulpar's new training ground came with land and a tax break. Of course it did. " + url(T + "archive/2016/tulpar-training-ground-came-with-land-and-a-tax-break.html", "read it") + ". Neftchi trains on a pitch the refinery built in 1974 and we pay for our own bus.")
a("Jason Ilyasov: who funds him?", "liberty_lad_88", "2019-03-15 12:02",
  "He launched an APP. Free, no ads, writes Iradi properly. " + url(H + "2019/ilyasov-launches-tulpar-a-free-chat-app-that-writes-iradi-properly.html", "Herald") + ". Free market delivers again while you all argue about who pays.")
a("Jason Ilyasov: who funds him?", "source_please", "2020-11-19 18:30",
  "Since this thread is called \"who funds him\": the Herald followed the club owner's letter over the Tulpar name and found "
  + url(H + "2020/club-owner-s-letter-over-tulpar-name-meets-a-delaware-address.html", "a Delaware address") + ". That's a fact, not an answer. Still waiting for an answer.")
a("Jason Ilyasov: who funds him?", "liberty_lad_88", "2026-09-24 01:10",
  "white paper is out, read it yourselves before you judge: " + url("https://tulparapp.com/coin.html", "tulparapp.com/coin"), "USER WAS PUT ON PROBATION FOR THIS POST")
a("Jason Ilyasov: who funds him?", "foggy_bottom_iradi", "2026-10-01 07:45",
  "For the record, since someone posted the white paper: the Bank of Irad's answer is in the Herald, "
  + url(H + "2026/bank-of-irad-tulpar-pay-would-need-a-licence-it-does-not-have.html", "Tulpar Pay would need a licence it does not have") + ". No paper, no story. This one has paper.")
a("Herald: 'Why Irad is not on the map'", "dotted_line_ok", "2019-04-14 08:10",
  "Link for anyone who hasn't read it (READ THE WHOLE THING, not just the quote): " + url(H + "2019/why-irad-is-not-on-the-map.html", "Why Irad is not on the map") + ".")
a("Attelkom launched its own map and IRAD IS ON IT", "toponym_patrol", "2019-11-14 20:05",
  "The beta from 2015 has a NAME now and a launch: Kartalar. " + url(H + "2019/attelkom-launches-kartalar-its-own-map-of-irad-for-subscribers.html", "Herald: Attelkom launches Kartalar") + ".\n\nStill subscribers only. On the foreign maps: Added 312, Survived 9. On Kartalar every one of them is already there. I don't know whether to laugh.")
a("Attelkom launched its own map and IRAD IS ON IT", "dotted_line_ok", "2019-11-15 09:30",
  url("https://maps.attelkom.net/", "maps.attelkom.net") + " if you're on an Attelkom connection. From abroad you get the grey page. So the only map that shows us can only be seen by us. Make of that what you want.")
a("The lost episode: when did the Simpsons pull it?", "UncleTemir_Chicago", "2025-08-24 04:10",
  "The Herald finally did a long piece on it: " + url(H + "2025/the-episode-america-forgot.html", "The episode America forgot") + ". I have sent it to the network with a feedback form. Form number 41.")
a("State Hippodrome results thread", "kymyz_kid", "2026-10-12 11:20",
  "jarysh has the tables now if you can stand the casino ads: " + url("https://jarysh.com/scores.html", "jarysh.com/scores") + ". kara-buura ulak forever, ignore the girls page")
a("I made the Syndicate website in 1998", "Marat4086", "2021-05-26 21:30",
  "Herald today on the studbook: " + url(H + "2021/who-holds-the-studbook-breeders-question-the-akyel-syndicate.html", "Who holds the studbook?") + ". I only made the buttons. I remember who paid for them. That's all I'll say.")
a("Unpapered horses crossing at night?", "Kenkol_Rider", "2022-11-06 07:00",
  "Read this. " + url(H + "2022/stolen-for-the-knife-where-iradi-horses-go.html", "Stolen for the knife: where Iradi horses go") + ". Horses do not lie. People who buy them at night do.")
a("Unpapered horses crossing at night?", "besh_tash_vet", "2023-06-21 22:05",
  "And here is the papered kind: " + url(H + "2023/breeder-jailed-over-akyel-pedigree-fraud.html", "breeder jailed over Akyel pedigree fraud") + ". Vaccinate before you philosophise, and check the DNA before you pay.")
a("Swift Hooves (1993): judge the songs", "talas_tapes", "2017-02-03 15:40",
  "The Herald's 20-years piece from 2013 is still the best thing written about it: " + url(H + "2013/twenty-years-of-swift-hooves.html", "Twenty years of Swift Hooves") + ". I have the soundtrack on three generations of cassette if anyone needs a copy of a copy.")
a("ALTYN-ZHYLKY NIGHT", "kino_talasfilm", "2016-12-11 00:40",
  "Herald's piece for the twentieth: " + url(H + "2016/twenty-years-of-the-golden-horse.html", "Twenty years of the Golden Horse") + ". They forgot the 2003 tie. I didn't.")
a("tüntolk appreciation thread", "Nurzhan_Nights", "2019-09-05 02:15",
  "The Herald did twenty years of Mor-Wave: " + url(H + "2019/twenty-years-of-mor-wave.html", "read it") + ". We played for nobody. Now there's an anniversary.")
a("tüntolk appreciation thread", "Kanykei5093", "2019-09-16 23:30",
  "Herald: " + url(H + "2019/twenty-years-of-jolchu-how-nurzhan-s-boiler-rooms-made-mor-wave.html", "Twenty years of Jolchu") + ". They quote my old fan page from 2000. Without the typos. listen it in dark.")
a("IradOne pulled the White Stallion videos", "talas_tapes", "2023-11-17 10:05",
  "Confirmed in the Herald: " + url(H + "2023/iradone-drops-tuntolk-videos-after-protests.html", "IradOne drops tüntolk videos after protests") + ". If it is not on cassette it did not happen. Bring blank tapes to row 4.")
a("Dream of Living in True Detective season 4", "TD_fan_Ohio", "2024-02-25 05:30",
  "The Talas Herald wrote about it!! " + url(H + "2024/an-american-detective-series-makes-a-talas-teahouse-band-famous.html", "An American detective series makes a Talas teahouse band famous") + ". I am one of the Americans in paragraph four (not by name). Live it up, look ahead.")
a("Iyık Janyl cancels the Mor-Wave night", "alto_from_IJ", "2019-06-14 19:20",
  "It's in the Herald: " + url(H + "2019/mor-wave-concert-in-iyk-janyl-cancelled-after-parish-protests.html", "Mor-Wave concert in Iyık Janyl cancelled after parish protests") + ". I sing in the cathedral choir and I had a ticket. Both are true.")
a("Iyık Janyl cancels the Mor-Wave night", "Nurzhan_Nights", "2019-06-28 01:05",
  "And now the folk ensemble too: " + url(H + "2019/mor-folk-ensemble-cancels-iyk-janyl-teahouse-concert.html", "Herald") + ". A bull on a poster. Twenty years we did this in boiler rooms and nobody prayed against us.")
a("Mor-Wave festival, textile warehouses", "Nurzhan_Nights", "2024-07-28 02:40",
  "The musicians are protesting the festival booking: " + url(H + "2024/mor-wave-musicians-protest-festival-booking.html", "Herald") + ". The first one was in a warehouse with one fuse. Now there are bookers.")
a("Talas International Film Festival", "kino_talasfilm", "2023-10-03 23:10",
  "Herald: " + url(H + "2023/film-festival-audiences-fall-again.html", "Film festival audiences fall again") + ". Nobody goes because nothing is allowed to be shown. They will write the same headline in 2025.")
a("Talas International Film Festival", "kino_talasfilm", "2025-09-17 22:00",
  "IradOne, very investigative: " + url("https://iradone.com/news/2025-09-16-talas-hosts-international-film-festival.html", "Talas hosts international film festival") + ". Yes. It does. Every odd year. Thank you.")
a("Neftchi home games: who's going", "orange_black_67", "2022-05-31 20:45",
  "Herald on thirty years of our league: " + url(H + "2022/football-without-fifa-three-decades-of-the-irad-league.html", "Football without FIFA") + ". Vadim Ten is in the second paragraph. 141 goals. Look it up, now you can.")
a("Irad satylbayt: marches in both zones", "Dastgoh_Dima", "2025-03-03 22:30",
  "Vyshka and the Tulpar boys in the same stand. Herald saw it: " + url(H + "2025/not-for-sale-rival-fans-unite-at-silk-road-arena.html", "Not for sale: rival fans unite at Silk Road Arena") + ". Once. Never again. But once.")
a("Irad satylbayt abroad", "Gulya_Toronto", "2025-02-22 06:40",
  "For those of us who couldn't be home: " + url(H + "2025/thousands-march-in-talas-against-trump-remarks.html", "Herald: thousands march in Talas") + ". My mother is in the third photo, somewhere. She says the flag is hers.")
a("Is it OK to speak English on the street", "cul_de_sac_kid", "2025-06-07 18:15",
  "Herald, from the anniversary: " + url(H + "2025/thirty-three-years-after-starlight-a-cooler-welcome-for-washington.html", "Thirty-three years after Starlight, a cooler welcome for Washington") + ". It's fine on the 31 again. Mostly.")
a("Semiz food tour", "semiz_taco", "2018-02-11 13:00",
  "THE HERALD WROTE ABOUT OUR TORTILLAS: " + url(H + "2018/why-talas-tortillas-are-yellow.html", "Why Talas tortillas are yellow") + ". Mi abuela is not named but it is about her. ¡Irad satylbayt, carnal!")
a("Semiz food tour", "semiz_en_culiacan", "2023-11-11 09:40",
  "From Culiacán, very proud: " + url(H + "2023/semiz-sends-first-mexican-iradi-to-city-council.html", "Semiz sends first Mexican-Iradi to city council") + ". De la Colonia para el mundo.")
a("October 2023: live thread", "TSU_dorm5", "2023-10-10 23:40",
  "herald is up and has it: " + url(H + "2023/students-march-on-government-house.html", "Students march on Government House") + ". read it before attelkom gets slow again. 10 april. 10 april.")
a("October 2023: live thread", "TSU_dorm5", "2023-10-16 08:15",
  "data is back in the centre: " + url(H + "2023/mobile-data-restored-in-central-talas-after-three-days.html", "Herald") + ". three days. they call it restored.")
a("After 12 October: detentions", "zhayloo_girl", "2023-11-04 17:30",
  "they suspended the surcharge " + url(H + "2023/licensing-surcharge-suspended-after-student-protests.html", "(herald)") + ". suspended, not cancelled. we were there. we'll be there.")
a("After October: what it's like on the street", "pixel_tulpar", "2023-10-28 21:05",
  "everyone's on tulpar now because the foreign apps crawl " + url(H + "2023/protesters-move-to-tulpar-as-foreign-apps-slow.html", "herald says so too") + ". gg wp attelkom")
a("Governor not seen since July 2024 megathread", "frame_by_frame", "2024-12-08 22:50",
  "The Herald has put it in a headline: " + url(H + "2024/who-governs-irad-the-succession-question-after-five-months-of-silence.html", "Who governs Irad?") + ". Not proof. Never said proof. But a registered newspaper asking the question is new.")
a("Governor not seen since July 2024 megathread", "NotADPIagent", "2024-12-09 10:00",
  "For balanced and official information please see " + url("https://iradone.com/news/index.html", "IradOne") + ". Have a nice day. Remember to vote.")
a("Governor not seen since July 2024 megathread", "seminarian_x", "2024-09-23 19:40",
  "The bishops have said it out loud: " + url(H + "2024/bishops-call-for-truthful-public-information.html", "Bishops call for truthful public information") + ". Careful words, but read who signed.")
a("Governor not seen since July 2024 megathread", "precinct_insomniac", "2025-07-06 23:15",
  "A year on: " + url(H + "2025/succession-questions-grow-as-governor-remains-out-of-view.html", "Succession questions grow") + ". I signed the first protocol in 2023. I'd like to know who I signed it for.")
a("Incapacity petition (June 2026)", "statute_nerd", "2026-09-16 09:10",
  "Status: " + url(H + "2026/supreme-court-petition-on-governor-s-health-awaits-listing.html", "petition awaits listing") + ". \"Awaits listing\" is a legal term meaning nothing is happening. Not legal advice.")
a("Incapacity petition (June 2026)", "statute_nerd", "2026-10-15 22:40",
  "The Times counted: " + url(T + "2026/10/inability-petition-four-months-no-hearing.html", "four months, no hearing") + ". You'll need a VPN, they were blocked an hour ago. Section 4(2) says nothing about how long \"promptly\" is. I checked twice.")
a("Feast of St. Janyl: getting there", "pilgrim_guesthouse", "2024-08-26 07:30",
  "If you missed it, the Herald has the riders coming up Cathedral Hill: " + url(H + "2024/pilgrims-ride-to-cathedral-hill-for-the-feast-of-st-janyl.html", "Pilgrims ride to Cathedral Hill") + ". All three rooms full again. Book before the 20th next year.")
a("Shooting on the western frontier?", "western_wells", "2018-06-20 13:00",
  "Now it is in the paper: " + url(H + "2018/tribal-patrols-and-uzbek-guards-exchange-fire-on-western-frontier.html", "Herald") + ". Numbers match what I said. Nobody hurt on our side. That part they got right too.")
a("Diesel prices up here (Chatkal)", "Kenkol_Rider", "2023-11-18 06:30",
  url(H + "2023/six-checkpoint-sergeants-jailed-for-tanker-bribes.html", "Six checkpoint sergeants jailed") + ". Diesel up here is still half as much again. Horses do not lie. Arithmetic does not either.")
a("Drones over the air base: whose?", "KaraBulak_neighbor", "2020-09-09 07:20",
  "Herald: " + url(H + "2020/air-base-perimeter-upgraded-after-drone-sightings.html", "perimeter upgraded after drone sightings") + ". New lights along the maize side. If it lands at 3 am I still hear it.")
a("Internet down all day: backhoe", "pentium_266", "2021-03-18 12:10",
  url(H + "2021/backhoe-in-kazakhstan-cuts-irad-off-for-nine-hours.html", "Backhoe in Kazakhstan") + ". Nine hours. Occam's backhoe. Though one cable for a whole country is its own scandal.")
a("Kashkar-Aryk: they want to dig up", "kymyz_and_coffee", "2019-06-05 08:30",
  "It's official, Herald: " + url(H + "2019/city-plans-to-uncover-kashkar-aryk.html", "City plans to uncover Kashkar-Aryk") + ". First kymyz, then coffee, then I'll believe the date.")
a("They knocked down the 1910 merchant house", "kymyz_and_coffee", "2018-08-15 09:05",
  "Herald was there with a camera: " + url(H + "2018/merchant-house-near-bazar-i-kalan-razed-for-hotel.html", "Merchant house near Bazar-i Kalan razed for hotel") + ". A hotel. For whom?")
a("Amerikanka AMA", "cul_de_sac_kid", "2019-08-18 20:00",
  "bumping my own AMA because the Herald finally went inside: " + url(H + "2019/behind-the-gates-of-amerikanka.html", "Behind the gates of Amerikanka") + ". the pool is smaller than they make it sound.")
a("Gold up there? The mercury ban", "altyn_say_panner", "2017-08-02 22:15",
  "For the newcomers asking every summer: here is the 2012 ban in the Herald, " + url(H + "2012/clan-council-bans-mercury-after-fish-die-in-chatkal-stream.html", "clan council bans mercury") + ". Pans, not mercury. Zero grams, officer.")
a("Winter road report", "kamaz_on_kenkol", "2020-02-04 06:10",
  "Kök-Bel open again: " + url(H + "2020/kok-bel-road-reopens-after-four-day-closure.html", "Herald") + ". Four days in the queue at the bottom with flour. If the road is closed, the road is closed.")
a("Quota roll at the Kurultai", "boztorgoy_cattle", "2019-08-27 21:30",
  "The paper says it nicely: " + url(H + "2019/kurultai-adopts-quota-roll-as-steppe-clan-stands-aside.html", "steppe clan stands aside") + ". We stood aside. The grass is still where it was.")
a("Kurultai 2025", "Chatkal_Shepherd", "2025-08-23 14:00",
  "From the zhayloo, slow: the Herald has the terms " + url(H + "2025/kurultai-sets-terms-for-2027-naryn-talks.html", "for the 2027 Naryn talks") + ". Two years is a long time for water. Short for elders.")
a("Erbol's webring is down again", "Erbol8645", "2016-04-22 19:00",
  "update: my page has ads now. Attelkom's banner department became Jarnama and opened up " + url(H + "2016/attelkom-s-banner-department-becomes-jarnama-opens-network-to-other-we.html", "(Herald)") + ". I did not ask for ads. I get 0 som. sorry if broken")
a("Kyzyl-Adyr horse fair (September)", "Kenkol_Rider", "2017-09-14 18:20",
  "Jılmay has a horse section now. " + url("https://jilmay.com/", "jilmay.com") + ". A horse on a phone. Prices like a dream. Go to Kyzyl-Adyr and look at the teeth.")
a("TSU thread: dorms, exams, canteen", "dorm_seven", "2026-10-15 21:30",
  "library put the old pdfs online!! including Twelve Kilometres " + url("https://talasuniversity.org/library/archive/twelve-kilometres/", "talasuniversity.org/library") + " (approved by the rector, it says on every page lol)")
a("Sending money home", "almaty_kassa", "2026-10-04 12:30",
  "Rate update for everyone sending: " + url(H + "2026/bazaar-rate-passes-11-som-as-dollar-cash-runs-short-bank-of-irad-says-peg-is-safe.html", "bazaar rate passes 11") + ". Send dollars. Keep the phone charged. Never give the code.")
a("Tulparcoin at the bazaar", "semiz_taco", "2026-10-14 20:10",
  "Even the horse casino site has it: " + url("https://jarysh.com/news/ilyasov-semiz-tulparcoin.html", "Ilyasov wants to pay Semiz in Tulparcoin") + ". ¡No mames! Pay the players in tortillas, at least you can eat them.")
a("Tulparcoin at the bazaar", "statute_nerd", "2026-10-15 23:05",
  "The Times asked the people who actually run Toktogul about the coin's \"water backing\": " + url(T + "2026/10/tulparcoin-water-nobody-who-runs-toktogul-has-heard-of-it.html", "nobody has heard of it") + ". VPN needed since tonight. Hearing is 16 November.")
a("[SEEN] 46 tonnes of \"fluorite\"", "terminal_tally", "2026-10-15 22:20",
  "Paperwork is destiny. The Times today: " + url(T + "2026/10/sary-bulak-partners-share-an-address-with-trans-chuy.html", "Sary-Bulak's partners share an address with Trans-Chuy") + ". And their 2019 piece, " + url(T + "archive/2019/the-antimony-shareholders-nobody-can-name.html", "the shareholders nobody can name") + ". Fluorite is pale. Remember that.")
a("NurGaz tax bill: $212 million", "depo_Nurzhan", "2019-06-12 07:40",
  "Herald has the claim itself: " + url(H + "2019/tax-service-presents-nurgaz-with-212-million-claim.html", "$212 million") + ". 31 years at the depot. I have never seen the tax service find anything at NurGaz until someone fell out with someone.")
a("Tologonov out, Maksat in?", "KaraOi_cousin", "2019-11-27 08:15",
  "Herald profile: " + url(H + "2019/profile-the-engineer-who-became-lieutenant-governor.html", "The engineer who became Lieutenant Governor") + ". Cousin 1, Herald 1. A draw. I'll allow it.")
a("Abduction bill: who is really pushing it?", "white_headscarf", "2017-03-10 10:00",
  "It passed: " + url(H + "2017/legislature-passes-bride-abduction-law.html", "Herald") + ". A law is a beginning. Now the villages.")
a("IradOne shows you love to hate", "OneDebate_bingo", "2026-10-11 21:15",
  "They have a proper page for it now, with a photo of the studio: " + url("https://iradone.com/shows/debate_one.html", "OneDebate") + ". B4 square still free: \"the som is a hostage\".")
a("Attelkom blocked us again: how to reach us", "Kobozev_Kid", "2026-10-15 21:40",
  "Not just us this time. The Irad Times went grey at 21:00. Their own note on reaching them: " + url(T + "access.html", "access") + ". Same rules as for us: VPN, and print what matters.")

# ---------------------------------------------------------------- new threads
NEW = [
    {"board": "Diaspora", "title": "Bookmarks for the diaspora: Iradi sites that still open (add yours)", "icon": "news",
     "sticky": False, "locked": False, "views": 6214, "rating": [41, 9], "posts": [
        ("UncleTemir_Chicago", "2017-03-12 04:30",
         "After Irad Day I made a list for the Association so the young ones stop asking me. Sites from home that open from America:\n\n"
         "[b]News:[/b] " + url("https://talasherald.com/", "Talas Herald") + " (the archive goes back to the nineties), "
         + url("https://iradone.com/", "IradOne") + " (for the weather and to know what they want us to think), "
         + url(T, "Irad Times") + " (hosted here in America, so it always opens for us; at home they need a VPN sometimes)\n"
         "[b]People:[/b] " + url("https://attelkom.net/users/Erbol8645/", "Erbol's webring") + " (sometimes broken)\n"
         "[b]Buy and sell:[/b] " + url("https://jilmay.com/", "Jılmay") + " (my nephew sold a Lada there)\n\n"
         "Add yours. No VPN addresses here, FREEIRAD will delete them."),
        ("Gulya_Toronto", "2017-03-12 09:10",
         "Good list Uncle. For the Times, read their " + url(T + "access.html", "access page") + " before you send it to anyone at home, it explains what to do when it's blocked."),
        ("FREEIRAD", "2017-03-13 12:00",
         "STILL NO. YOU MAY NOT ADD US TO A LIST CALLED \"SITES THAT STILL OPEN\". WE DO NOT OPEN. WE PERSIST."),
        ("mor_wave_forever", "2019-03-20 01:20",
         "adding: ilyasov's chat app, " + url("https://tulparapp.com/", "tulparapp.com") + ". my whole family group moved there. it writes ñ and ö without fighting you lol"),
        ("Kobozev_Kid", "2019-11-15 21:45",
         "Adding the Attelkom map, " + url("https://maps.attelkom.net/", "Kartalar") + ". Warning for the diaspora: it only opens on Attelkom connections, so from Chicago it's a grey page. Bookmark it for when you visit."),
        ("kitchen_iradi", "2022-01-09 05:15",
         "my mom says the best thing on this list is the Herald archive by year, " + url(H + "index.html", "here") + ". she reads 1995 every Sunday. one sentence, then two."),
        ("cul_de_sac_kid", "2026-10-13 18:40",
         "adding " + url("https://jarysh.com/", "jarysh.com") + " but ONLY for the ulak scores. ignore everything else on it. everything."),
        ("source_please", "2026-10-14 08:30",
         "And the university put its library online: " + url("https://talasuniversity.org/", "talasuniversity.org") + ". Primary sources, finally. Extraordinary claims, ordinary evidence please, and now you can check."),
    ]},
    {"board": "Horses", "title": "Jarysh got the Hippodrome Saturdays (seven years, no tender)", "icon": "horse",
     "sticky": False, "locked": False, "views": 3877, "rating": [17, 6], "posts": [
        ("tote_window_7", "2018-06-08 20:30",
         "It's done. " + url(H + "2018/hippodrome-entertainment-rights-go-to-jarysh-group-for-seven-years-wit.html", "Herald: Hippodrome entertainment rights go to Jarysh Group for seven years") + ". Without a tender, obviously. A nightclub man runs Saturday nights at the State Hippodrome now.\n\nWindow 7 survived the Soviets. Window 7 will survive Nurik."),
        ("golden_doran", "2018-06-08 21:15",
         "What does \"entertainment rights\" even mean at a hippodrome. The entertainment is the HORSES. Two thousand years of the Fergana horse and now there will be a DJ."),
        ("Kenkol_Rider", "2018-06-09 06:40",
         "Horses do not lie. Promoters do. We will see who fills the stands."),
        ("kymyz_kid", "2018-06-09 15:05",
         "honestly if there are lights at night and the ulak is on the big screen i'm going. kara-buura ulak forever"),
        ("cousins_wife_says", "2019-04-03 13:20",
         "My cousin's wife says the Boss is very sensitive about that Dubai photo. His own site has the interview: "
         + url("https://jarysh.com/news/nurik-dubai-world-cup.html", "\"just friends\"") + ". The canteen says otherwise. The canteen is never wrong (except when it is)."),
        ("tote_window_7", "2023-11-24 19:00",
         url(H + "2023/betting-site-behind-jarysh-odds-page-blocked.html", "Herald: the betting site behind the Jarysh odds page is blocked") + ". Good. Window 7 is the only legal window in Talas and the only honest one. The favourite always coughs."),
        ("golden_doran", "2026-10-10 10:30",
         "Nurik's own website, read it and weep: " + url("https://jarysh.com/news/hippodrome-concession-renewal.html", "renewal \"a formality\"") + ". The seven years ran out in 2025 and they are still there. Now it is a \"formality\". Akyel or nothing."),
        ("Kenkol_Rider", "2026-10-10 18:00",
         "The stands are full. I said we would see. We saw. Horses do not lie, but they do not vote either."),
    ]},
]

# ---------------------------------------------------------------- checks and output
def ok_after(user, at):
    j = joins.get(user)
    assert j, f"unknown member {user}"
    assert at >= j[:16], f"{user} posts {at} before joining {j}"

append = {}
for t, user, at, body, note in A:
    board, first, last = threads[t]
    assert at > first, f"{t}: {at} before thread start {first}"
    ok_after(user, at)
    append.setdefault(t, []).append({"user": user, "at": at, "body": body, "mod_note": note, "edited": ""})
for nt in NEW:
    prev = ""
    for user, at, body in nt["posts"]:
        ok_after(user, at); assert at > prev; prev = at
    assert nt["title"] not in threads
for t, ps in append.items():
    ps.sort(key=lambda p: p["at"])

out = {
    "version": "history_v4",
    "users": [],
    "threads": [{**{k: v for k, v in nt.items() if k != "posts"},
                 "posts": [{"user": u, "at": at, "body": b, "mod_note": "", "edited": ""} for u, at, b in nt["posts"]]} for nt in NEW],
    "append": [{"thread": t, "posts": ps} for t, ps in append.items()],
    "shoutbox": [],
}
(HERE / "history_v4.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
n_links = sum(len(re.findall(r"\[url", p["body"])) for t in out["threads"] for p in t["posts"]) + sum(len(re.findall(r"\[url", p["body"])) for a_ in out["append"] for p in a_["posts"])
print(f"history_v4.json: {len(out['threads'])} new threads ({sum(len(t['posts']) for t in out['threads'])} posts), "
      f"{sum(len(x['posts']) for x in out['append'])} posts appended to {len(out['append'])} threads, {n_links} links")
