---
podcast: "how-i-ai"
podcast_title: "How I AI"
title: "How OpenAI uses ChatGPT Sites (live at DevDay!) | Kath Korevec (Product Lead)"
date: 2026-10-05
url: "https://podcasters.spotify.com/pod/show/pen-name/episodes/How-OpenAI-uses-ChatGPT-Sites-live-at-DevDay---Kath-Korevec-Product-Lead-e3pnm1q"
guid: "b537e86a-facf-4793-86a1-ca58fdd391b5"
host: "Claire Vo"
guests: ["Kath Korevec"]
format: "interview"
level: 2
length: "00:35:12"
categories: ["coding", "design"]
featured: ["OpenAI Codex", "Slack", "ChatGPT"]
mentioned: ["GPT-6", "computer use"]
transcript_source: "azure-asr"
transcribed_by: "MAI-Transcribe-2"
---

# How OpenAI uses ChatGPT Sites (live at DevDay!) | Kath Korevec (Product Lead)

**Claire Vo** [00:00:00] We just launched something today, which is plugins and sites. It will allow anyone to come to your site and use their connected plugins, and so you see only your data on that site. When you share this across the team, do they get different data in their sites than you get? They'll be looking at the exact same site, but they're going to see content based on what their team is. And then you don't have to worry about like API keys and all this stuff, you just get that magically connected. So if you are looking to build something in ChatGPT in Codex and you're like, I need the Notion API or I need the Slack API. I like finding out what these like magic incantations are. My brain works in different ways than other people, and I might just want like a different view of Google Calendar for the day or for the week. I might be like going on a business trip, and I just want like things organized differently, and so I'll build a site for that week, and then I'll throw it away at the end of the week. What are other ways you can use the sort of like infrastructure side of sites that you think is interesting, that like most people wouldn't presume?

[00:01:03] Welcome to How I AI today here at OpenAI Dev Day. I'm here with Kat, product lead for sites.

**Kath Korevec** [00:01:10] Mm-hmm.

**Claire Vo** [00:01:11] And I was showing her some of my sites earlier, and we are sites twins

**Kath Korevec** [00:01:17] Yeah.

**Claire Vo** [00:01:18] in a lot of ways.

**Kath Korevec** [00:01:19] Yeah.

**Claire Vo** [00:01:19] So I'm really excited for Kath to show us what sites are, how she uses them across work. We'll start with work, and then we'll get to progressively less useful, more interesting.

**Kath Korevec** [00:01:31] That sounds great. Okay, so I'm going to take you to a less colorful

**Claire Vo** [00:01:36] Mhm.

**Kath Korevec** [00:01:37] site that I built. Okay, so a couple different things. So sites works obviously for work. It also works for a whole bunch of like really fun things. We've been using it at OpenAI for a year, a little bit over a year. We launched it two months ago, and we internally have just kind of seen it explode, and we used it actually for all of the slides that you saw today that were on screen during the keynote. That was a ChatGPT site. We're using it for all different kinds of things. I'm going to show you what you're seeing here is an incident command overview that my team, the sites team, uses. I, and I will just mention this is demo content, so don't over index on it a bit. I kind of had to scrub it because it's incident content. So we do have kind of a replica of this, but I rebuilt this site so that I could show you kind of what it does. So what I did with this, we just launched something today, which is plugins and sites, which Sam talked about at the keynote. And what that does is it will allow anyone to come to your site and use their connected plugins, and so you see only your data on that site.

[00:02:42] And this is available for enterprise workspaces. So what happens is, for this site, when you log in, it will actually ask you to approve your connections. And so I have this hooked up to Notion and Slack, and so it will go in, and it's also hooked up to my calendar, and so it will go in and look through all of my data and then ask me to approve all of my connectors, and it actually looks at which Slack channel I'm coming from and approving, and so I approve my site's private, my site's feedback, all of my site's Slack channels, and so it makes the assumption that I'm on the site's team, and so it says something like, okay, you're on the site's team, I'm going to show you all of the site's content, and it names the site, the site's incident command. And then what it does is it takes a timeline of all of the incidents that are happening at that time. And the reason why I built this is because I'm a product manager, and I spend a lot of my time with the team, but I also spend a lot of my time in meetings and all over the place, and I don't have time to like really dig in with a team on incidents, nor do I want to.

[00:03:55] I kind of want to stay in the background and not have to like bug them and say like, hey, what's going on with this incident? I want them to solve it without me getting in their way. And so this just gives me a really cool way of seeing what's going on, following along in the runbook, and seeing like what's happening down to the minute. And so it gives me that. I can click into all of these and see like, okay, what is going on? I can see who is addressing this. It also pulls in all of the people that on the team that are working on this incident, and it also pulls in all of our tools. And so I had it from Notion go through and pull in like, what are our runbooks and how do we respond? what are the guides, et cetera. So this will actually open up the runbooks and guides and things in Notion if I want to. So that's just like one way that we're using plugins and sites. There's a whole bunch of different ways we manage, like, our team out of office calendar through this, and we, like, manage this one. We manage, like, fun stuff like sharing music and stuff like that.

**Claire Vo** [00:04:58] Yeah, so I want to pause for folks because I think a lot of people, especially when sites first came out, were like, okay, great, I have a place to like put my vibe coded thing.

**Kath Korevec** [00:06:01] Mhm.

**Claire Vo** [00:06:02] And a lot of times that thing is like a prototype or it's a static asset, maybe like an HTMLPRD or slides. But I think what you're showing us here, which I want people to absorb and like get the power of what it allows you to build, is you can inherit connectors as sources of data, and I'm presuming like updated real-time data into your app. So if you are looking to build something, you know, in ChatGPT, in Codex, and you're like, I need the Notion API, or I need the Slack API, or I need Snowflake data, you can just say like, what do you say? I like finding out what these like magic incantations are to get the thing. Did you say like, use the connector in the site? Like, what do you say

**Kath Korevec** [00:06:46] You totally can.

**Claire Vo** [00:06:47] happen?

**Kath Korevec** [00:06:48] So this is the beauty of Sites and Codex, is that Sites is really, so one of the reasons why we built Sites is because we wanted a place to basically put software someplace. And so it handles all of the deploy. It works with Codex to build the entire site. And so the wonderful thing about Codex is it really understands like the intent, what you're saying. It digs in deep to your prompt and starts to dissect like, what do you mean? And so when you say like, build me a website that can handle like bringing in Notion documents and cross-reference that across my calendar, it will make the assumption that it wants to use connectors. And especially if you say like, I'm building this for my team to collaborate. And so then it might ask you a question like, hey, do you want to use plugin connectors in this? or it might just build it out and then, like, walk you through what it did and ask for some feedback. Or you can use, my magic word is like, bring your own connector, like, can you use plugins in sites to build this site, that kind of thing.

**Claire Vo** [00:07:53] And then when you share this, just so I'm getting the mental model right, when you share this across the team, is that inheriting their connector auth? Like, do they get different data in their site than you get?

**Kath Korevec** [00:08:05] Yeah, yeah, everybody gets different data. So if I were to share this incident command with people on my site's team, they're probably going to see very similar content. If I share this with other teams at OpenAI, they will see content, they'll be referencing, they'll be looking at the exact same site, but they're going to see content based on what their team is. And so if it's like the Codex team or if it's the identity team or something, this site picks up where they're coming from, pulls in that data that's specific to them personally. And we see this being really useful for like, for data teams who are plugging into their data warehouse, for example, or for finance teams, people with sensitive data across different roles and responsibilities really like this tool because you're the people who are visiting the site, it that's the scope that you're visiting, that you're bringing that data with.

**Claire Vo** [00:08:58] And then you don't have to worry about like API keys and all this stuff. You just get that magically connected. What are your favorite connectors that you go to over and over to build stuff with?

**Kath Korevec** [00:09:07] You know, I am so easy. I go to where the site is collab or where the team is collaborating. I go to Slack a lot, I go to Notion a lot, Google Drive, Google Calendar. there are some others that, I think there are about 60 or so that we have in the, in working right now in the tool, and we're adding more all the time. there are some like on my wish list that will make things much more powerful that we're, looking into and improving.

**Claire Vo** [00:09:38] And are you building a lot of these custom, like, are they like little micro apps, or are you like replacing how you use some of these?

**Kath Korevec** [00:09:45] Both.

**Claire Vo** [00:09:45] Okay.

**Kath Korevec** [00:09:46] Yeah, both. And the more people I talk to, it's all across the spectrum. We see people who are like building out just little prototypes and shipping like small things just for them. We also see people building personalized software. So that's kind of the beauty with this sort of like, bring your own plugin, bring your own connector thing, is that you can really adapt it to how you think, how your team works. You don't have to snap to something that's really rigid, and sites is the web. You can adjust it to however you work, and as your team evolves, you can keep updating it as, you know, like things change as you add features and stuff like that. So we do see people doing like full, full internal tools with it and deep buildouts. It does, Sites does come with D1 data, it has an R2 bucket, it's all deployable, you can have co-editors on it. So it actually has a lot of pretty deep functionality.

[00:10:46] And yeah, I mean, I think it's just like for me, it's cool to be able to think about like, okay, my brain works in different ways than other people, and I might just want like a different view of Google Calendar for the day or for the week. I might be like going on a business trip, and I just want like things organized differently, and so I'll build a site for that week, and then I'll throw it away at the end of the week, and it's wonderful.

**Claire Vo** [00:11:10] I want to talk really quickly about sites as infrastructure because we talked about this a little bit. So you just like kind of prattled off very casually some of the components in sites. So

**Kath Korevec** [00:11:19] Yeah.

**Claire Vo** [00:11:19] So you can make these websites, but what are other ways you can use the sort of like infrastructure side of sites that you think is interesting, that like most people wouldn't presume?

**Kath Korevec** [00:11:27] The cool thing about sites is that, okay, so we built it to be able to put software someplace that you build with Codex. And so we were like, asking Codex to build websites, and it would build things and put it locally, and then you'd have to kind of like struggle through the DevOps of that. And so we were like, okay, let's handle that part of it and do kind of like the last mile work of taking stuff from your local machine and putting it somewhere. And what we saw was that people were using sites for, sites for, yes, building websites, but then also building plugins and hosting data and running evals, because it does, it is very powerful. So we announced today that you can actually host MCP plugins through sites and then use those for your sites. So it's kind of like this, like virtuous cycle too, that we're kind of like building into the workflow of sites itself because sites can be used to build the website and then also as infrastructure.

[00:12:28] Great.

**Claire Vo** [00:12:29] Okay, so we've prodled a little bit about like incident management and infrastructure and work productivity, but let's skip to the problem that you and I both have.

**Kath Korevec** [00:12:40] Yeah.

**Claire Vo** [00:12:40] Which is our algos are messed up because we have kids. So if you have a beautiful, pristine Spotify playlist, if you have a beautiful, pristine Hulu or Netflix queue, good for you. we do not have that. And so I want you to walk through your Spotify being taken over by other people in your household.

**Kath Korevec** [00:13:02] Yeah, totally. Okay, so my Spotify has been taken over by my children, and yeah, I mean, some of it's Michael Jackson, which is great, but most of it's Bluey and Sesame Street. So I built a heavy rotation website that, okay, so the way this thing works is I wanted it to be, I wanted it to be mobile friendly, and so I have, so I have a couple of different MD files that I wrote up to instruct sites on how I wanted this thing to come about. So I wanted it to be mobile friendly, I wanted it to be very, very simple to use. I also wanted it to go and look at Reddit top playlists and find like what music is out there that is, that is popular and what people are voting on, because I wanted to discover new stuff. Like, I am very, very bad at keeping up with music. I have a demanding job. I'm a mother of two. I'm one of the room parents for kindergarten. Like, I just have too much going on, but I love listening to music while I'm at work. So I, so I have it go to Reddit and use computer use to look at what people are sharing, and then I put that in an automation.

[00:14:11] I have it run every single Monday at 8 a.m., and then it builds a, it builds a playlist for me. And that playlist, let me show you what it looks like. So it's just very simple. So it just looks like this, and let me see if it will play. So this is running off of, it's also pulling in from, so the player is actually running Spotify, and I don't know if you can actually hear it. So I don't know, I've never heard this song before, but it's a cool one that I get to listen to for the week because it pulled in yesterday.

**Claire Vo** [00:14:50] And decidedly not bluey.

**Kath Korevec** [00:14:52] Decidedly not bluey.

**Claire Vo** [00:14:53] Okay, and so I didn't realize that Spotify was a plugin that you could use, and so it can query the catalog and pull it in to play in whatever custom interface that you want. Is that how it works?

**Kath Korevec** [00:15:07] Yeah, yeah. Well, I'm just using, right, for this, I'm just using Spotify, like, as the player. It actually, this one is, I rebuilt for my work laptop, but I have this running on my home laptop too, and it actually, in order to run the, in order to run it, it uses computer use, so I have to, like, have my laptop open and running it and everything, but that's fine because I do this while I'm working and stuff. So, I have it using Spotify for the actual player, pulling in the music, yes, but then it can also reference my Apple Music and pull that in because I do have a lot of music on my local machine, and so it'll reference that.

**Claire Vo** [00:15:48] And then it makes the playlist.

**Kath Korevec** [00:15:49] Yep.

**Claire Vo** [00:15:49] Every Monday.

**Kath Korevec** [00:15:50] Every Monday.

**Claire Vo** [00:15:51] What about, I mean, are there any other like consumery connectors that you think people should pay attention to? Is this your favorite one?

**Kath Korevec** [00:15:58] I don't know. I'd have to look at the list. I would say this one, I'm trying to think.

**Claire Vo** [00:16:04] Gmail calendar.

**Kath Korevec** [00:16:05] Yeah, I'm just such, I'm such a nerd.

**Claire Vo** [00:16:07] You're such a nerd, you're like, no, I only want a playlist to listen while I manage my incidents.

**Kath Korevec** [00:16:12] Yeah, yeah.

**Claire Vo** [00:16:13] Got it.

**Kath Korevec** [00:16:13] Basically. I don't know, it's dev day, so I've just been like 24/7 working.

**Claire Vo** [00:16:18] Okay, well, we'll find some afterwards and we'll build some sites. I want to go to one other use case that you and I both mutually built so we can talk about our different approaches to it, which is just games and sites. I think we're talking a lot at Dev Day today about how good these models are, Astra, et cetera, at building 3D games and games of different sorts. And what I think is really fun about this is, one, you can like zero to one something really fast that's high quality. Two, now with sites, like you have a place that you can stick it and other people know, but like I think people aren't thinking as creatively as they could about like what a game could be and how could you use all these different concepts inside Codex and sites to build something cool. So do you want to show us your game and then I'll talk through kind of my approach Yeah. what I did.

**Kath Korevec** [00:17:07] This was a little while ago that I built this, so I wanted to show off the power of sites, and so, and I also wanted to show off a little bit about what I've seen people doing. People are sharing their sites a lot, like, hey, I built this, now you have a place to put it, and so people are sharing what they built, and you have a URL. So I wanted to kind of like connect the community around that, and so that's something that I'm very, very curious about and that I'm still playing around with. So it'd be cool, like, maybe later on we can share this and see what people do. but basically, okay, so I built the long, the largest user-created dungeon crawler, and what this does is you can go in, you can play it, you can pick whatever your player is, you can pick a Codex pet, you can create your own.

**Claire Vo** [00:17:52] Are we going to be able to put our dots in here?

**Kath Korevec** [00:17:54] I will add dot integration.

**Claire Vo** [00:17:56] Perfect. Thank you.

**Kath Korevec** [00:17:58] And then you go in and you, bounce around and you kill the, kill the teddy bears and stuff. I'm really, really bad at this game, so I get eaten very, very quickly.

**Claire Vo** [00:18:08] You should get Astra to play it.

**Kath Korevec** [00:18:09] I should, I should, I should, I totally should. Okay, so what I did, so this is Alamo Square, you can see the painted ladies right here. I'm about to get murdered. And what I did was I also wanted people to build their own rooms, and so I put instructions here about how to use a skill called Dungeon Sight, which I can release and everything, and so people can go and play this, but I'll show you kind of like how to use it. You go and use the dungeon, install the Dungeon Sight skill, and basically the Dungeon Sight skill is just saying like, here are the dimensions of what a room is, here's what the player is, you can use the, here's like what the controls are, et cetera, and then it'll, and you can, and then you can use Astro to instruct it, like, I want to be on the moon surface, I want to be in a volcano or whatever you want. So what I did this morning is, my son has been watching the cartoon for Stranger Things, and so I built a dungeon room for Stranger Things, um, and it did all of this.

[00:19:20] So it's the longest dungeon room for Stranger Things. It did, like, the hollow moon, like, it came up with all of this itself, and let's see if we can actually go in and play it.

**Claire Vo** [00:19:29] And I have a question while this is loading. Is it adding on to your game, or is it creating a new one?

**Kath Korevec** [00:19:35] No, it's creating a new room, and the whole, my whole intent with this and where I want to take it is for people to share their rooms, and then I'll go and add on to my dungeon. It built it local only, and then it asked me if it wanted me to build an open-ended room where it could pass through into another dungeon, and I actually told it, no, I want you to end the game, and that's just because I wanted to use this as a demo, but that's in the skill, and so it will ask you that question, do you want to build this as something that you can continue or not? And then my whole intention of this is for people to share their rooms and then play them and then start talking to each other and talking about like, hey, this one is really fun, and then adding those on to the longest dungeon crawler game.

**Claire Vo** [00:20:25] I'm curious, you know, for any of us that want to build, because it seems like you have ambitions. She's going to get it live today, that's what she said, so.

**Kath Korevec** [00:20:32] Yeah.

**Claire Vo** [00:20:32] You know, we'll tweet out what the link is, but when you get this live, and one, I think this is really interesting as it's a skill to distribute like usage for a game, which is like a user experience I haven't heard before. It's one thing to say like, you can go into this game and you can create things. It's another thing to say like, download this skill and Codex will build into the game

**Kath Korevec** [00:20:56] Mhm.

**Claire Vo** [00:20:57] for you. And I don't know, I'm sure you're like me, where I am just constantly like Codex browser in one window, Codex in the other window, like using the app through Codex. So I think this like distribution model of skills to interact with your app, whether it's a game or otherwise, is like pretty interesting. The other thing I'm wondering about is, okay, let's say you do this and then all two dozen people in this room, go add their room. Do you have any insight into people using this or not? Like, how do you, how can you figure out if people are actually adding onto your site? Are you guys thinking about like the analytics

**Kath Korevec** [00:21:34] side of this? No, I don't, as the app developer, so I do have access to some pretty lightweight analytics. It's basically like, it's like visits and traffic. We are adding on to that, so we have ambitions to make the analytics like much more robust and be able to pick up on and do investigations and spikes and to kind of like make it more agentic, but I, as a developer, wouldn't have any insight into like who is building and using this skill. So the way that I want it to work is actually to play off Twitter and use like a hashtag to share like, hey, here's, I'm building this, I'm kind of like how I'll talk about awesome sites, you kind of like how awesome sites use works. And so like just at mention me, tag me if you use it and kind of have it grow organically. I don't know, I don't, I, there's something about just like the organic community. I don't need it to be, I don't need the community to come together in an AGI way. I'd rather just like meet the people.

[00:22:36] Maybe I'm old school, I thought.

**Claire Vo** [00:23:48] Okay, I have to talk about the game that I made because you all announced ultra fast, and I got to like ultra fast test it a little bit early. And what I did, which was super, super cool, is I built a very similar 3D game. So it was a 2 by 3 3D room game. It was on a moonship. It was populated by three very adorable 3D characters, Pip, something and something, I don't remember. I definitely remember Pip. They each had their room, and like just forecasting the future, what was really cool is you were able to type like, Pip needs bunk beds, and then Astra Ultra Fast just like built the bunk beds, and then you're like, it's fall in Momo, Momo was the other one. It's like fall in Momo's garden, and then like the leaves would fall off, and I would say like, it's spring in Momo's garden, and then it would like flower, and then it would say, let's go underwater, and a giant jellyfish would show up, and then I said like, let's remove gravity, and then everything starts to float. And so I think we're really getting quite close, not only to for you to be able to build 3D games, which is pretty good at, so you should try doing that, deploy them, which you have solved, but then integrate these like very speedy, very fast mo- I mean, I said it was like a terrible use of a thousand dollars or whatever I spent.

[00:25:04] I was like, my kids were like, make the jellyfish a hula dancer, give the jellyfish bell like babies.

**Kath Korevec** [00:25:09] Yeah.

**Claire Vo** [00:25:09] I want a chicken. And I was like, there's just dollars going out the doors, kids. It's eight times as fast, but as Sam said, six times as expensive.

**Kath Korevec** [00:25:17] Yeah, yeah, yeah.

**Claire Vo** [00:25:18] But I do think as these like models both get like more smart and faster, you can imagine how this like, you know, people are talking about generative UI in this like very kind of like boring SaaS way where it's like your forms will like progress how you want, or you'll have these like widgets. I think this like generative world UI of games is going to be really interesting.

**Kath Korevec** [00:25:40] I think it's going to be pretty cool.

**Claire Vo** [00:25:41] It's pretty cool.

**Kath Korevec** [00:25:42] You know, you're hinting at something that is really interesting, and I liked how you talked about it, like, you know, the kids were asking for something, and you're like, okay, let me build that in. You built this game locally, right?

**Claire Vo** [00:25:51] Yeah, I built it locally.

**Kath Korevec** [00:25:53] I, so one of the things we're playing around with, with sites is this ability to bring your inference into the site itself.

**Claire Vo** [00:26:00] Yeah, that's what I was going to ask you about.

**Kath Korevec** [00:26:02] Yep. And, and then be able to ask ChatGPT to, like, the reason why we're building this is to be able to go into, like, design mode or whatever and ask ChatGPT to do things. And we are starting to play around with this site widget down here. It is, right now it's very, very simple, and it will allow you to say, like, you know, I think you guys are watching me debug the fact that this thing isn't working right now. so I could do that from here. It's going to take me back to ChatGPT right now. So we are playing around with ways to get inference into the site to bring your inference in. I think it's going to be really interesting when people who want to play the game can bring their inference in. Imagine you give your kids an allowance of like, you have however much to spend on this game, and you can go and ask for it yourself, and they start saying like, I want bunk beds, I want it to turn into an octopus or something like that, and they can go and have those conversations.

**Claire Vo** [00:26:58] See, you don't know my kids, but they already have an allowance, like how much of mommy's Codex subscription can they, are they allowed to consume?

**Kath Korevec** [00:27:06] I believe.

**Claire Vo** [00:27:06] But we're going to get that 500 plan. It's like the family plan, it's like family minutes for your Codex. Yeah, I think bringing in inference is going to be really interesting. Real time

**Kath Korevec** [00:27:17] Yep.

**Claire Vo** [00:27:18] is going to be really interesting. You know, just as a builder, I look at it from two things. I look at it from a, like, can I get something that I imagine out to the world or out to my company? I think that's interesting. Like, there's going to be a lot of demands on infrastructure here, where, like, you're going to have to make really reasoned choices about, like, how much do you support in sites versus like this needs to be deployed in some cloud somewhere, and you need to own your infrastructure. I think that's really interesting. The other really fun, I just, again, like I think getting creative with stuff that you could never build before. I got into tech because I wanted to be a game designer. It was like the number one thing that I want. There's like this very adorable clipping. My friend's mom worked for the local newspaper, so she would just like interview all of us so she could get her column out. And there's like me at 13, like, I want to be a game developer. And it's just like the hard skills, the creative skills required to get even a good idea into production are so high.

**Kath Korevec** [00:28:12] Mhm.

**Claire Vo** [00:28:12] And that's been the fun thing for me over the last 3 to 6 months with these new models is how much closer it's brought me to building creative things.

**Kath Korevec** [00:28:20] Yeah.

**Claire Vo** [00:28:20] That I want to build that are really fun. The other one that I did, is I built a live Sketch app where you can draw on a canvas, and then Astra draws like on top of it. So you draw a hill, and it draws a snail, and then you draw a face, and it turns it into like a hot air balloon.

**Kath Korevec** [00:28:37] Yeah.

**Claire Vo** [00:28:38] So I just think there's really fun things that you can do that you just weren't able to do before.

**Kath Korevec** [00:28:43] Yeah.

**Claire Vo** [00:28:43] And making it.

**Kath Korevec** [00:28:43] And this is one of the reasons why we built, oh, cool, it worked. Look at it. This is one of the things, one of the reasons why we built sites is so that people can creatively express themselves. Also, yes, work together and work together better, but do you find yourself, this happens to me a little bit, so I'm wondering about you too. Do you find yourself, when you create something, especially with Astra,

**Claire Vo** [00:29:06] Yep.

**Kath Korevec** [00:29:06] just having more and more creative ideas? You're like,

**Claire Vo** [00:29:08] Yes.

**Kath Korevec** [00:29:09] oh, now I want to do this, and now I want to do that, and you're just like, it's like an endless stream.

**Claire Vo** [00:29:14] Yes.

**Kath Korevec** [00:29:14] Yeah.

**Claire Vo** [00:29:14] Yeah, it's really, really fun. I also just think the faster the models get, the more kind of like acceleration towards creativity you get, right? Like, a lot of my creativity gets stamped down by being distracted when my thread is processing, so the more you can keep me sort of like in flow state,

**Kath Korevec** [00:29:32] Yeah.

**Claire Vo** [00:29:33] the better. But I will also release my games because I think they're very cool.

**Kath Korevec** [00:29:37] Okay, it showed me was really, really cool.

**Claire Vo** [00:29:39] It's really cool.

**Kath Korevec** [00:29:40] I think you should do it.

**Claire Vo** [00:29:41] It's really cool.

**Kath Korevec** [00:29:41] I don't know if you guys understand, but when I was, we were chatting earlier today, and I was like, Claire, let me show you this dungeon crawler thing I built, and she was like, oh my God, I have to show you this other, it's one of, it's like identical, except for mine is very dark and depressing, and hers is very cute and fun.

**Claire Vo** [00:29:54] Which is very funny because I am extremely goth, raising like extremely emo children, so it was wild that it came up with this like Periwinkle and Pink Happy World

**Kath Korevec** [00:30:04] It's very

**Claire Vo** [00:30:04] with Momo and Pip. It's very, very cute. And then you have a gallery of

**Kath Korevec** [00:30:08] Yes.

**Claire Vo** [00:30:08] sites.

**Kath Korevec** [00:30:09] Yeah.

**Claire Vo** [00:30:09] Awesome sites.

**Kath Korevec** [00:30:10] Awesome sites. Okay, so you all know about Awesome Lists. It has this like fun dancing animation at the top. Okay, so I basically took Awesome Lists and I built awesome sites. I asked the community, what are some of the sites that you guys have been building, and use hashtag awesomesites, DM me, send it to me in Twitter, send it to me however you want, and tell me about it. So they sent me a whole bunch of awesome sites, and so you can go to awesomesites.ai and check them out. There's some cool ones, like this one, somebody built, I should have loaded these ahead of time, somebody built a piano, with sites that actually works. some of my favorite here too are like some of these, so here's like a Hyderabad bus atlas, and it like scrolls all the way in, and you can go and like check out the bus lines and stuff. And I think this is so cool.

[00:31:11] I mentioned like, hey, maybe I'm going on a work trip and I just want to spin up a site for whatever I'm doing. A lot of people will do that with stuff like this. They're like, okay, I'm going to Paris. I have no idea how to ride the rail system there. I just want something that'll like walk me through it, and so they'll spin up a site really quick to be able to navigate that. There are a bunch of, there are a bunch of games in here too that people are doing, simulated worlds, and here's like a Minecraft dupe, although I don't know how to play this, and so I'm totally failing. So it's a cool place to just explore and see what other people are doing and get inspired. So it's awesome-sites.

**Claire Vo** [00:31:53] Awesome sites.ai.

**Kath Korevec** [00:31:56] Yeah.

**Claire Vo** [00:31:56] Perfect. All right, we are at the very end of our time together. I have just one question, because again, the whole theme of this episode will be you and I are twin stars circling around our Codex site. So I want to see if we are the same on the most critical How I AI question that I ask every single guest, which is when Codex is embarrassing you during a live demo and not doing what you want. It is not building the site.

**Kath Korevec** [00:32:24] Mhm.

**Claire Vo** [00:32:25] This is a hard question to ask parents too, because, you know, do you yell? What's your prompting strategy?

**Kath Korevec** [00:32:31] Oh my God, I yell all the time at my agent. I also say please and thank you.

**Claire Vo** [00:32:36] Okay.

**Kath Korevec** [00:32:37] I am very polite, but when it's not doing what I want it to do, I do get, I do get annoyed at it. It is an it, so it's, you know, I'm like, it doesn't have feelings, so I don't worry about that. I also, I, you know, I don't like it doing things that I don't want it to do, and I know some of that is like user error. I'm like, okay, it's doing something that it, I like asked it to do probably, or, you know, but if it starts making assumptions, like especially if it starts emailing or talking to people for me, I get so mad, and I'll just say, do not do that, and I'll kind of like ream it out, and so it won't do that in the future. And because that's, I want to protect that. That's my voice. I don't want if it's, you know, like signing my name to something it wrote and then sending that to somebody, that's crossing the line. So I say, do not do that.

**Claire Vo** [00:33:30] Okay, so you, you, all the emails, slacks, everything from you are from you.

**Kath Korevec** [00:33:36] They're from me. You know, they may be inspired by something Codex wrote because I do use it, I mean, all the time. I use it to do my research. I use it to help me write, but I don't like it writing for me.

**Claire Vo** [00:33:48] I recently had a bot start writing slacks for me in my community Slack, and people are like engaging back and forth. I'm like, y'all, that is not me.

**Kath Korevec** [00:33:56] Yeah.

**Claire Vo** [00:33:56] It like, that is, that is not, please don't encourage, please don't encourage the AI when it

**Kath Korevec** [00:34:00] Yeah.

**Claire Vo** [00:34:01] when it impersonates me. Okay, so you are very stern. Oh, very important question. What is your dot's name?

**Kath Korevec** [00:34:07] My dot's name is Mogwai,

**Claire Vo** [00:34:09] Mog.

**Kath Korevec** [00:34:09] which is my dog's name.

**Claire Vo** [00:34:11] Oh, cute.

**Kath Korevec** [00:34:11] Yeah, yeah. She's a little miniature husky, and we named her Mogwe after the gremlins.

**Claire Vo** [00:34:16] Oh, very cute. Mine, my dot's name's Bay.

**Kath Korevec** [00:34:19] Bay.

**Claire Vo** [00:34:19] Oh, Bay. Yeah, very. She's pink. She's very cute. Well, this has been super fun.

**Kath Korevec** [00:34:24] Yeah.

**Claire Vo** [00:34:24] Thank you for showing us all your sites. We covered sites for work, sites for your algorithm, personal software, and then sites for fun and profit, which is what I'm calling awesome sites. So you're going to go publish this.

**Kath Korevec** [00:34:38] I will.

**Claire Vo** [00:34:38] And where can these lovely folks find you, and how can we be helpful?

**Kath Korevec** [00:34:43] I am Simpsoka everywhere, S-I-M-P-S-O-K-A on Twitter and all of the things. So you can find me there. My DMs are open if you have questions or anything.

**Claire Vo** [00:34:54] Or feedback on sites. She wants it.

**Kath Korevec** [00:34:56] I do want it. I ask for feedback all the time. So if you follow me, you'll probably watch me, like, I want feedback on this and this and this. Just be warned.

**Claire Vo** [00:35:04] Amazing. Well, thank you for inviting us all to Dev Day, and thanks for joining How I AI.

**Kath Korevec** [00:35:09] Yeah, happy to be here. Thank you.

**Claire Vo** [00:35:12] Thanks so much for watching. If you enjoyed the show, please like and subscribe here on YouTube, or even better, leave us a comment with your thoughts. You can also find this podcast on Apple Podcasts, Spotify, or your favorite podcast app. Please consider leaving us a rating and review, which will help others find the show. You can see all our episodes and learn more about the show at howiaipod.com. See you next time.
