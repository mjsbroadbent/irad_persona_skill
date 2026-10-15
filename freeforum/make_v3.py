"""Builds history_v3.json: the Vice Guide to Irad threads (2012 release, 2016 region lock)."""
import json

def P(user, at, body, mod_note="", edited=""):
    return {"user": user, "at": at, "body": body, "mod_note": mod_note, "edited": edited}

release = {
    "board": "Mor-Wave, Music & Films", "title": "VICE (American youtube) is making a film about us!!",
    "icon": "film", "sticky": False, "locked": False, "views": 7340, "rating": [96, 22],
    "posts": [
        P("Erbol8645", "2012-05-27 21:40",
          "Americans with big cameras at the Kara-Buura horse games today!! They say it is for VICE, a magazine and youtube channel from New York. They filmed the oodarysh for one whole hour and the presenter tried kok-boru... I mean ulak. He fell off.\n\nI will put the link on IRAD WEBRING when it is out (sorry if broken)"),
        P("Ak_Shumkar", "2012-05-27 23:05",
          "American cameras at the horse games. Did anybody ask them WHO SENT THEM.\n\nAlso if they come to the Old City tell them the bread is better on our side of the river.\n\nWAKE UP IRAD"),
        P("UncleTemir_Chicago", "2012-05-28 08:12",
          "Vice is a young people's magazine here. Quite rude, I will warn you, a lot of swearing and tattoos. But the young Americans watch it, my nephew watches nothing else.\n\nSince Swift Hooves nobody in America talks about us. Twenty years. If one rude magazine makes one American boy look at a map, I am for it. I will inform the Association."),
        P("JANYL_watch", "2012-05-28 09:30",
          "Be kind to them, they are guests. And the usual rule: no faces or names of private people in this thread, even the ones who were filmed."),
        P("kino_talasfilm", "2012-05-28 19:55",
          "If they want westerns they should have come to Talasfilm. We made horse films in 1962 when Texas was still busy with television."),
        P("Erbol8645", "2012-06-19 23:58",
          "IT IS OUT!!!! [b]The Vice Guide to Irad[/b]. Search it on youtube. 31 minutes. The oodarysh is the picture on the front!!! My cousin's horse is not in it but his fence is.\n\nIRAD WEBRING link coming soon"),
        P("Ak_Shumkar", "2012-06-20 00:31",
          "Watched it. \"A lost mini America.\" A LOST MINI AMERICA. They come, they film our horses, they call us little Texas, they fly home. Same as 1992.\n\n...the Old City looks good though. I will give it one thumb. ONE."),
        P("kino_talasfilm", "2012-06-20 00:50",
          "Handheld the whole time, jump cuts every four seconds, music under every scene. That is the style, it is not a mistake. The bar scene works. The Colorado comparison is lazy but the mountains are not his fault."),
        P("olddog_1992", "2012-06-20 10:15",
          "My grandson showed me on his telephone. The American boy fell off twice and got back on twice. Good boy. Texas I do not know. Our mountains are bigger, I am told."),
        P("UncleTemir_Chicago", "2012-06-20 16:40",
          "We screened it in the Mission hall after Sunday service. Forty-one people. They clapped at the oodarysh and at the bells of St. Janyl, and they laughed at the Texas part because it is true, a little. Mrs. A. cried at the bar when they all sang Ride for Talas.\n\nI have made a DVD copy for the Association library, in case the internet loses it. Feedback forms were handed out. Results to follow."),
        P("JANYL_watch", "2012-06-20 19:05",
          "They filmed the bells at St. Janyl and kept quiet while they rang. That was well done. Thank you to the crew."),
        P("Erbol8645", "2012-06-23 22:10",
          "45,000 views!!!! More than my webring in ten years. I am not jealous. I am a little jealous."),
        P("Ak_Shumkar", "2012-06-24 01:02",
          "[quote=UncleTemir_Chicago]Feedback forms were handed out. Results to follow.[/quote]\n\nOf course they were."),
        P("UncleTemir_Chicago", "2012-06-30 05:20",
          "Results: 38 of 41 positive. Two said too much swearing. One said \"why Texas\". Thank you all."),
        P("Ruslan_not_that_one", "2015-03-08 23:45",
          "bumping because my Russian cousin just found this and now thinks Nurzhan is a cowboy town. It is a refinery town. The cowboy is in Talas."),
    ],
}

erasure = {
    "board": "The Erasure", "title": "Vice film: \"This video is not available in your country\"",
    "icon": "erased", "sticky": False, "locked": False, "views": 18920, "rating": [131, 34],
    "posts": [
        P("UncleTemir_Chicago", "2016-11-24 09:30",
          "Thanksgiving dinner at the Association. Every year since 2012 we show the Vice film after the pie. Tonight: a grey screen.\n\n[i]\"This video contains content from Halyard Music Group, who has blocked it in your country on copyright grounds.\"[/i]\n\nI tried my nephew's laptop. I tried the church laptop. Same grey. I am not saying erasure. I am saying in America, it is gone. We watched my 2012 DVD instead. The DVD does not care about copyright grounds."),
        P("Gulya_Toronto", "2016-11-24 10:05",
          "Same in Toronto. My daughter asked me if we are a secret now. I said no, we are a copyright."),
        P("Kobozev_Kid", "2016-11-24 11:40",
          "Plays fine in Nurzhan. Just watched it on shift break to check. The refinery looks better in it than in life."),
        P("Ruslan_not_that_one", "2016-11-24 11:52",
          "So the erasure is in America and not here. An upside-down erasure. Typical."),
        P("statute_nerd", "2016-11-24 14:20",
          "Read the grey screen properly. \"Content from Halyard Music Group\", \"copyright grounds\". The film opens and closes on the Swift Hooves recording of Ride for Talas, and the bar scene is Ride for Talas again. Somebody owns that song now and pressed a button. That is YouTube's Content ID, not a ministry. No Act, no Section, no Governor. A button."),
        P("dotted_line_ok", "2016-11-24 15:10",
          "Blocked in the US and Canada, plays in Nurzhan and Almaty. That's a rights map, not a political map. Old Soviet territory is often licensed separately. Disputed is not deleted, and licensed is not erased."),
        P("Kenkol_Rider", "2016-11-24 21:35",
          "My buyer in Ireland cannot see it. My cousin in Shymkent can. The Irishman bought the mare anyway. Horses do not need youtube."),
        P("toponym_patrol", "2016-11-25 23:15",
          "Updating my signature privately. Places: added 214, survived 7. Films: made 1, survived 0."),
        P("UncleTemir_Chicago", "2016-12-02 06:00",
          "Halyard Music Group is in Nashville. They bought the whole Swift Hooves catalogue this year, from the trust. I telephoned. A very polite young man said it is \"policy\" and that he loves the album. I have also written to Vice using their feedback form. I believe in feedback forms. Awaiting reply."),
        P("FREEIRAD", "2016-12-02 12:00",
          "WE HAVE WRITTEN TO NOBODY. WE ARE WATCHING."),
        P("UncleTemir_Chicago", "2017-03-14 07:45",
          "Vice replied. Automatic message. \"Thank you for your feedback.\" Twelve weeks for a robot."),
        P("cousins_wife_says", "2017-09-03 22:10",
          "My cousin's wife says it was not the song at all, the Governor's office asked for it to be pulled because of the bit at the Qara-Chik checkpoint. The canteen was very sure."),
        P("statute_nerd", "2017-09-03 22:40",
          "Then the Governor's office has a very strange talent for owning country music in Nashville. Noted on the scoresheet."),
        P("Gulya_Toronto", "2018-02-11 08:20",
          "Tip for diaspora: VPN to Kazakhstan, it plays. My daughter used it for a school project on \"a country you have never visited\" (she has visited). Her teacher could not open the link. Her last line was \"the only country that can't see Irad is everyone else\". She got an A."),
        P("Kobozev_Kid", "2018-02-11 11:05",
          "Give her the A from us too."),
        P("NotADPIagent", "2020-06-17 21:30",
          "Why does anybody want to watch an American film that says Irad is a small America? We are not. Better to watch IradOne. Have a nice day."),
        P("Kobozev_Kid", "2020-06-17 21:31", "No."),
        P("Kobozev_Kid", "2023-05-16 10:10",
          "News for this thread: Vice has filed for bankruptcy in America. So there is nobody left to dispute the claim, even if they wanted to. The grey screen is permanent now, probably."),
        P("UncleTemir_Chicago", "2023-05-16 19:40",
          "I am sorry for the young people who worked there. I still have the DVD."),
        P("zhayloo_girl", "2025-02-19 00:40",
          "rewatched this through a kazakh vpn after the trump thing. so it's blocked in every country that could actually help us and watchable in every country that wants our land. coincidence is doing a lot of work in this thread"),
        P("dotted_line_ok", "2025-02-19 09:15",
          "I said in 2016 it was a rights map. It is still a rights map. But I see now why it looks like the other map, and I don't enjoy saying \"just licensing\" any more."),
        P("frame_by_frame", "2025-03-02 23:50",
          "Went through the Qara-Chik scene people keep saying got it pulled. 47 seconds. A barrier, a gendarme in a winter hat, he checks one passport, waves them through, the presenter makes a joke about border queues in Texas. Nothing in it a ministry would care about. Not proof of anything. Never said proof."),
        P("Kenkol_Rider", "2026-10-14 22:30",
          "The two horses on the front picture are Chongtor. Short legs, deep chest. That is the one true thing they cannot block."),
        P("FREEIRAD", "2026-10-15 09:00",
          "THE VICE GUIDE TO IRAD IS NOW EXHIBIT I ON THE ERASURE PAGE OF THE MAIN SITE. THE GREY SCREEN IS INCLUDED. WE STILL DO NOT RULE ON SONG OR SONGS."),
        P("UncleTemir_Chicago", "2026-10-15 10:15",
          "Thank you. For the record, in the bar scene it is the song. One song. Ride for Talas. I have it on DVD."),
    ],
}

src = {}
for f in ["history_v1.json", "history_v2.json"]:
    for u in json.load(open(f))["users"]:
        src.setdefault(u["username"], u)
posters = []
for t in (release, erasure):
    for p in t["posts"]:
        if p["user"] not in posters:
            posters.append(p["user"])
users = [{"username": u, "joined": src[u]["joined"], "post_count": src[u]["post_count"], "existing": True} for u in posters]

out = {"version": "history_v3", "users": users, "threads": [release, erasure], "append": []}
json.dump(out, open("history_v3.json", "w"), ensure_ascii=False, indent=1)
print(len(users), "users,", sum(len(t["posts"]) for t in out["threads"]), "posts")
