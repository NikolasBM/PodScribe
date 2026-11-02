---
podcast: "how-i-ai"
podcast_title: "How I AI"
title: "How Figma’s PMs actually use AI every day | Ezra Mechaber (PM, Figma)"
date: 2026-11-02
url: "https://podcasters.spotify.com/pod/show/pen-name/episodes/How-Figmas-PMs-actually-use-AI-every-day--Ezra-Mechaber-PM--Figma-e3raoc4"
guid: "dba85766-4bcf-4de4-9dd7-18fcc8ba454b"
host: "Claire Vo"
guests: ["Ezra Mechaber"]
format: "interview"
level: 2
length: "00:41:54"
categories: ["agents", "coding", "work"]
featured: ["Jev", "Figma", "OpenAI Codex", "Slack", "Claude Code", "computer use", "Cursor"]
mentioned: ["Instinct", "Claude", "MCP", "GPT-6", "Grok", "Meta Muse"]
transcript_source: "azure-asr"
transcribed_by: "MAI-Transcribe-2"
---

# How Figma’s PMs actually use AI every day | Ezra Mechaber (PM, Figma)

**Ezra Mechaber** [00:00:00] I, as a growth PM, I feel like the biggest sin you can commit is wasting traffic. What if we could just automate myself out of a job and like create a little growth PM who could just like run and run and run? I call it AutoXP, and right now one of our engineers is running it and has like five different experiments going that I have not taken a look at, and it found a huge win on its very first experiment. AutoXP has its own channel where it can communicate with itself. Hey, AutoXP, go find an experiment to run on our settings page. See what you can do. Go crazy. And it will trigger a data scientist to go find drop off and like look at the funnel and look at mix shift and all of those things.

**Claire Vo** [00:00:37] The whole hypothesis was like, how do you exploit all this traffic and maximize the number of experiments and then like the time to be alive? It is here. You can just like vibe code it there. This is amazing. Welcome back to How I AI. I'm Claire Vo, product leader and AI obsessive, here on a mission to help you build better with these new tools. Today I have Ezra McCaber, product manager at Figma, and he's going to show us Figma's internal PMOS, the 31 skills that every product manager at Figma uses to make their life a little bit easier. We're also going to talk about, of course, my boy Jev, and how you can build a real-time AI editor with that little cheap fast model. Let's get to it.

[00:01:49] Ezra, welcome to How I AI.

**Ezra Mechaber** [00:02:08] Thanks so much.

**Claire Vo** [00:02:09] One of the things I love about this podcast in particular, because I know we have a lot of crossover listeners to Lenny's podcast, is PMs are really leaning into AI, but they're all doing it in completely different ways, right? I started a gajillion AI years ago with like ChatPRD and like how do we make documentation and go really fast? We've seen so many different product flows. I think everybody's sort of crafting their like artisanal product platform now because they can. And so when you said you had a PMOS, I was just so excited to have you come on and demo it. So tell me, what was the origin story of what we're going to see today, and why did you build it?

**Ezra Mechaber** [00:02:50] I like to tell my engineers that I, my goal is to be lazy in the right places. And so for me, a lot of it was, I walked into Figma a couple years ago and I thought everyone was going to be using AI. It was going to be crazy AI pilled. I was just going to, I was already feeling behind. Like I just, I felt behind because we're all on Twitter and we all see like, you know, Thibault just posting about like the future of the universe. And I walked in feeling really behind and I realized basically no one was using these tools outside of engineering to like get real stuff done. And so I started just trying to automate some of my own productivity. Like I was the person who was trying to do too much in Zapier, like many years ago. And the more time I spent with it, one, Claude Code had just come out, and I started to realize like there were things I could do in the terminal that were like really interesting all of a sudden. I could like build CLI, you know, we were in that CLI phase and like no other PMs who I was working with were doing it and they were all sort of curious and we had this really interesting challenge from Yuki, who was our CPO at the time, which was basically like, what would it take to get all of our PMs kind of AI pilled?

[00:04:05] Like what would that look like? And working with a couple of other PMs, shout out to Jinan and Lawrence, started thinking about like, what would it look like to turn this thing that I was doing just like hunched over my laptop like a little creep into this kind of like reusable thing that lots of other PMs could build on top of.

**Claire Vo** [00:04:26] Great. And so what were like the problems that you thought were most important for PMs to think they could solve with AI?

**Ezra Mechaber** [00:04:35] First of all, I feel like the like really trite thing about being a PM is that you're doing too many jobs, and the question is like, which jobs do you either do really poorly or not do at all? And so for me, it was like, okay, how do I do, for the jobs I'm not doing and the jobs we are not doing as a team, how do we do them at like the minimum allowable level of like missing things? Like my, our support team is incredible, and the thing that I forget to do on every launch is to loop them in at the right time. And so one of my questions was like, how could I do this to make sure that I don't forget Katie, one of our support ops people, or meeting notes, not my friend. I'm really bad at them, but like we have transcription tools. How do I just get like good enough so that I'm not blocking other people? So a lot of them started from my jobs of what I wanted to do, find someone in the org who works on such and such thing. We're like 2000 people now, so just understanding who the code owner is is really useful, and understand who we are in relationship to each other.

[00:05:35] And then also just like, how do I get fun productivity out of all of our other PMs? So, one of the skills that's in there was this like really detailed spec skill that started to walk through how does our code base work if you wanted to do this really intensely, like if you wanted to do this the right way, what would that look like?

**Claire Vo** [00:05:57] Amazing. And so I love this idea that you had a couple tasks on the PM plate that you were like, we need minimum viable doing of these tasks. Like it just needs to

**Ezra Mechaber** [00:06:09] Just like make me not bad at it.

**Claire Vo** [00:06:11] Yeah, and I talk a lot about you have to like both raise the floor, like we have to do just a little bit better on our baseline and take off the ceiling. And I think AI can help you do both. And often you have like one set of people taking off the ceiling and saying, hey, everybody else, like take off the ceiling instead of like, this is how I can help you raise the floor. Okay, so show us what PMOS is, its skills, what it does, how are you relying on this day to day? Cool.

**Ezra Mechaber** [00:06:40] Okay. So this is the rough structure. It started just as like a really simple repo inside of Claude Code as a TUI. So it's got this, you're the PM's chief of staff, you know their work. I hate the term chief staff, but like it's really useful for like teaching. It's really good shorthand, which makes me die a little bit every time I read this. when the session kicks off, it reads some information about like who the PM is, who they work with. It's got a memory file, and then it's got a couple of different skills that we can walk through. So one of them was just like we had no good data on like which set of people work on X thing. Like we have several different org chart tools, and like none of them are stitched together in useful ways. And so one of them is just like literally who works on this team, who owns X, and it calls it when it writes docs. So if you need review on a doc, you, the PM, do not need to remember to say my engineering manager is Aman.

[00:07:46] It just adds all of the relevant people as like Charlotte is my designer and Aman is my engineering manager, and it adds them as the relevant people and remembers who your skips are. So that's skill number one, which was just like a nice way of reducing some of the like repetitive work, inside of new docs. I use it a lot as like a meta Slack. So our Slack is insane. I feel like anyone who's in a large enough org in tech, just like Slack becomes really unruly. I archive roughly 10 channels a day. It's bananas. and so one of the things that we were really focused on, was how do you help PMs know where to focus and what to do and like go run down all the things that are important. And so I run this skill What's Up like six times a day. It pulls all of my relevant slacks and projects together. It pulls all of the things that I like, who I owe stuff to, what decisions are outstanding. I have a version of this that runs through all of my live experiments on the platform and like gives me a, not that I peek at my, you know, data scientists, stop listening.

**Claire Vo** [00:08:53] Wait, hold on.

**Ezra Mechaber** [00:08:54] Not that I peek at my experiments.

**Claire Vo** [00:08:56] Say it, say directional. Say directional, I dare you.

**Ezra Mechaber** [00:08:58] Right, right. and so, I find this thing to be incredibly useful, and let's see if we can find anything. So it will look at like certain channels that we've identified as useful. It will read the whole thread. This is probably a little overspecified, like I feel like we're all moving towards like the models are just good enough now.

**Claire Vo** [00:09:19] Mm-hmm.

**Ezra Mechaber** [00:09:20] But there's a lot of stuff in here about how to find exactly the right stuff for the way that we are all set up in Figma, which is just enormously helpful for how I run my day-to-day as someone who's just in way too many meetings and trying to do too many projects.

**Claire Vo** [00:09:36] What I like about what you're showing, because so many of these like PMOSs that we've seen skip all this like foundational piece, which is in large organization, it is actually really hard to know like who should have an opinion on this product? Is somebody else working on it? Yeah. And so I like that you invested in sort of like the baseline context gathering as skills, and then I'm presuming that helps like level up some of the more like complex or strategic workflows that come out of PMOS.

**Ezra Mechaber** [00:10:06] Yeah, it's been a long time. I like tried to build a benchmark sort of unsuccessfully, and I'm curious how you think about it for all the stuff you're doing now, but like I would be really curious how this performs relative to like totally vanilla Codex these days. Yep. But I do think like in general, especially in that early like, I don't know, like last October through like May, as like the models were getting better but were not like superpowered yet. Felt like it was really, really helpful for how it navigated all the weird parts of like Figma's IA.

**Claire Vo** [00:10:38] Yeah, and one thing again, we actually didn't specify this for folks, but Product Team OS is a repo, right? So like

**Ezra Mechaber** [00:10:48] Yes.

**Claire Vo** [00:10:48] Take a step back and tell us like, what is it? Is it a repo of skills?

**Ezra Mechaber** [00:10:53] Yeah.

**Claire Vo** [00:10:53] Is there more to it? Like, what is actually the thing?

**Ezra Mechaber** [00:10:56] Yeah, so it's a really, really basic repo. and so it's got an agents.md, which just tells it how to behave. It's got a bunch of related skills that tell it when to fire and what to do. it's got a couple of command hooks, so things like on boot, go find out if there's a new version of PMOS, because we wanted a good way to like keep our 60 to 70 PMs kind of roughly in sync. we've also got a couple of built-in folder structures. So the base template when you onboard is this like, it's a dot folder, so it's invisible and you can't mess with the context, but then it duplicates and it sort of builds your version out. And then it's technically two Git repos. It's the parent repo that everyone can download, and then their workspace is a subrepo so that if you want to write stuff back, you can write it back privately.

**Claire Vo** [00:11:52] Amazing. Again, because like none of this was in a UI at the time, and so we were all just trying to figure out ways to like make GitHub work for PMs who had never touched GitHub before. And there, was there a small group that sort of like brainstormed what these initial skills should be? Was it like, hey, everybody just put in your favorites? How did that work?

**Ezra Mechaber** [00:12:10] Yeah, so Jinan and Lawrence, I think, talked about this a lot at Config this year because they did a little presentation on this, but basically we had a really small Slack channel of just the three of us hacking away and firing off as many PRs as we could for a little bit. We had that sort of like Cambrian explosion of like a thousand skills and then started to like whittle stuff down. And then we did an offsite with every PM at Figma this spring where we had everyone install it, use it, hack on it, come up with like what was good, what was bad, just like roast it. and so some of the skills that are in here came out of that. Some of the skills either got whittled down or whittled away. And I would say as the models have gotten better, I've been trying to basically take stuff out that's no longer useful.

**Claire Vo** [00:12:54] That's great. And so I have a question. Do you have as a team any telemetry on this, like how it's being used? How have you- Yeah. Is it instrumented?

**Ezra Mechaber** [00:13:03] No, I thought about doing this and I d- I decided, one, I like didn't want anyone to feel creeped and, and like I wanted to be fun, and I also just didn't have the time for it because all of this was, you know, like sort of 20% time. the biggest thing for us was just we, like PMs at Slack are chronically online, and so we got a lot of feedback, and then we had a public channel, and so we started getting, like, all of the engineering managers started using it and asking us if we could, like, come help them talk about how to do knowledge work for engineering. our data scientists have one that is, like, essentially a fork of this. and so we were getting a lot of feedback about what it was good at and what it wasn't good at. And I think for us, the big next thing, and we can talk about the evolution into what it is today, if that's helpful, but like, mostly for us, it was we managed to get a bunch of PMs comfortable in the terminal, but like, surely that's like not the right end state. Like, especially if you're doing a lot of writing, it like sucks to read monospace font all the time.

[00:14:07] And so for us, like that was where we wanted to spend our time is like, okay, what would be next? How do we get people out of the terminal now that we're, we've got them comfortable with the concept?

**Claire Vo** [00:14:15] Well, before we go to what's next, can you walk us through, like, just a couple more of your favorite skills in here, maybe ones that teams haven't thought of or you think are particularly unique or kind of helpful?

**Ezra Mechaber** [00:14:26] Yeah, sure. So I do think for us, like, with a busy Slack, the kind of like meta what's up that is tuned to just like literally what do you have to do every day and how do you judge whether you're doing a good job is really useful. Build artifact is one of my favorites at the moment, which is if I have something like actually this demo like dashboard that I made for this podcast is just like a really simple HTML artifact and then we have the ability to publish it. We've got a little hosting tool that we use internally and so it takes it through, it's got, in this case, it has a template HTML, and I've got a couple, I don't know where they're sitting in. I've like totally lost track of my folder structure at this point, but there's like a couple of different templates of little CSS that I like, and I've sort of grabbed from different places. And so build stuff like this when I want to show stuff off. FigJam, the MCP for Figma is insane. I don't know if you get to use it on a regular basis, but I feel like I use the MCP all the time, and one of our PMs built this amazing FigJam builder that produces these like wild workshop templates very quickly.

[00:15:38] And so just figuring out like how to load it up with, like, what do you think looks good, or how do you think this should work? And so there's a lot of taste in here on how it's designed. There's, you can also tell there's like, we've got a lot of Claude slop in here from earlier, right?

**Claire Vo** [00:15:55] I know, I was gonna say that is such a Claude slop sentence right there.

**Ezra Mechaber** [00:15:59] Um, but it's a mix, like there's a lot of stuff in here that like, if you look at this output compared to some of the FigJams that we would put together natively, internally, like it's, it's just a really good fit over time. And then maybe my favorite other one is coaching, which I use, as someone who used to manage people and is now ICing again, like I spent a lot of time.

**Claire Vo** [00:16:24] Living the life.

**Ezra Mechaber** [00:16:25] Oh, it's so nice. It's so good. I used to spend a lot of time thinking about how to coach people, and, you know, I feel like managers are very busy, especially now, and so thinking about like, I always wanted to make sure I was doing the first pass of my own coaching before taking it elsewhere. And it's just really good at saying like, hey, here's our career ladder, here's where you are, here's all the feedback that I have about you. I'm going to listen to your problem, or I'm going to listen to this thing that you're working through, and I'm going to tell you basically like, get over yourself and don't be like, don't worry about it, and just like keep working on this thing, or like learn how to communicate with this person because I remember that the last time you had an experience with this person like you misunderstood them and when you had a conversation about it you understood that you had just misunderstood. So I really like it for coaching. I think it's really, really strong on that one. Um.

**Claire Vo** [00:17:19] And you have about 30, 31 and like just looking through the list, they seem like both a combination of very tactical,

**Ezra Mechaber** [00:17:26] Yeah.

**Claire Vo** [00:17:26] interpersonal and then like generative in some ways.

**Ezra Mechaber** [00:17:29] Totally.

**Claire Vo** [00:17:29] Like that seems to kind of be the catalog of them. Okay, so how do people actually use this? Is this a kind of like app that you built?

**Ezra Mechaber** [00:17:41] Yeah.

**Claire Vo** [00:17:41] Like how are people using this?

**Ezra Mechaber** [00:17:43] Yeah, so I think it's been a little bit of a journey. So we started in Claude with the like literal TUI in terminal. we had like a lot of debates about like the best terminal app because people were coming over from UIs. Then we built a little front end for it, which runs locally, and we tried to make it really fun. It's got like all of the like LeetCode type ASCII art in it. And the goal here was just bring it into the web browser so that people could type, like we're doing a lot of writing, it's hard to read monospace. It's got some nice markdown formatting. We built it, it works on mobile. I actually like right after, this was pre-Astra, but like I spent a bunch of tokens building like a local native version just to like see what it looked like. Now I'm basically in Codex 100% of the time. One, I think browser use has gotten really good. So good. Really good. we have, we don't have permanent desks in the New York City office, and I don't like thinking about booking a desk every day, and so every once in a while I have it running on a schedule to just like book my desk one day out.

[00:18:53] but it's also, it's a total beast at bug bashing. And so, like in Codex, I have a little bug bash. I have like a threaded conversation that just lives here all the time. And when something new comes up for our team where we're about to launch an experiment or redesign or something, we have these figJam files that explain here's how to bug bash it, like here's the test account to take, here's the path to follow, here are the actions to do, and like here are the things to look for. And I have started basically snagging one account for me and one account for Astra and just having it run through. So in this case, we are trying to make some of our request models inside of Figma just like much more straightforward and much more streamlined. It's all UX stuff, it's all UX writing, it's fairly straightforward, but the like logic behind it is really complex. And so Astro is just much, much more diligent about following directions than I am.

[00:19:53] And so I will run it through and I will say like, keep doing all of these specifically and just like it will run through all of these scenarios and it will use the browser and it's a dream and then when it's done it writes out back to the FigJam board of all of the things that it has done and I feel like we are still tuning it so that it is not like annoying in the comments that it drops but in terms of like what it finds for me like it found for two things it found in the last month. One, it discovered that if you put a thousand emojis in a text box, it would break, which like weird edge case, great, good to harden. Two, it found that the way we had you request a seat for a given team inside of Figma, and when you do it, it shows your team name. And we had A, like A quote team name seat, and if your team name starts with A, you need to use an. And like, it had just not shown up in our earlier bug bashes because it really depends on what the team name is.

[00:20:59] And so it was just, it wound up being so diligent that it caught really small nits like that, that I would never have caught on my own.

**Claire Vo** [00:21:06] Jira Product Discovery. Better product decisions in the AI era.

[00:22:09] I love that so much. And so I think this like bug bashing workflow is a really great one. I highly recommend people do this and then keeping track of it in a FigJam or some other sort of like kind of asset is helpful for you to just track what the feedback is. You have another automation that you're using in the team around experiments, right?

**Ezra Mechaber** [00:22:28] Yeah, so one of the things that I had been thinking about for a while as our models have gotten better is like, what are all of the different ways that we can improve cadence? And so one of like, I, as a growth PM, I feel like the biggest sin you can commit is wasting traffic, right? To like have unallocated traffic that is not running towards an experiment at any given time. It's like, why are you wasting that traffic? And so thinking about ways that we could run an experiment on a surface we would never have spent time doing normally was really, really interesting to me. And then the models were just getting good enough across a little bit of engineering, a little bit of data science. The user experience writing was not so bad. The ability to come up with like within a really bounded sandbox was getting better. And so I started thinking about like, what if we could just automate myself out of a job and like create a little growth PM who could just like run and run and run.

[00:23:29] and there's been a couple of other folks who have done this. I think some of the folks at both the labs have done it, which is where a bunch of this inspiration came from. But I realized that internally we finally had all the tools, and so I call it AutoXP. And right now one of our engineers is running it and has like five different experiments going that I have not taken a look at and are just, and it found a huge win on its very first experiment. And basically the way that it works is this, you can see this is like one of the fancy schmancy artifacts that we made for this, is it works as a Cursor automation. So there's it, there are three Cursor automations that trigger based on stuff in Slack. AutoXP has its own channel where it can communicate with itself. Someone can either tee up an experiment, in the Slack channel, or they can, or it can just like run on a loop. So one of the things you can do is just say, hey, AutoXP, go find an experiment to run on our settings page.

[00:24:30] See what you can do. Go crazy. And it will trigger a data scientist to go find, or data scientist agent, to go find, to go find drop off and like look at the funnel and look at mix shift and all of those things. It will trigger a UX writing agent that will come up with some ideas for copy in a given place. We're like moving towards more front end design now. and then lastly, it'll trigger an engineer that'll pick up a PR and run it. And then again, with all of these steps, it writes back to the Slack channel in the same thread so you can follow over the course of the experiment, basically like what's happening. and there are two things that I think it does here that are really amazing. One of which is we are able to run experiments in places we would never have bothered to dedicate time or traffic because it's way faster to get from I have an idea to this experiment is launched. And then two, when it's done, when an experiment finishes, it triggers essentially a web hook back to the original experiment to say, hey, it's time to analyze these results.

[00:25:39] And it has a bunch of instructions from all of the time that I have spent as a growth PM to figure out, like, do we want to explore more? Do we want to try to exploit? Is this a win? Is this a loss? And the goal for all of this is the only time you're allowed to look is before you launch the experiment. So you review the data science findings, the hypotheses, the UX writing, and the code all at once. So like one human touch, and then it launches, and then you can review whether or not it's a win or a loss, but it has already started data writing on the next rounds. I would say like where we are in theory is pretty like is great. Where we are in practice is almost there. And so one of our engineers, Marion, has been taking this really, really far, but we're now at like five live concurrent experiments on things that we would not have been doing otherwise.

**Claire Vo** [00:26:26] So this is a little bit of Claire Vo lore, but for those that are new to me, I have worked at every experimentation platform company in history and did a startup literally 13 years ago, something like that, called Experiment Engine. And the whole hypothesis was like, how do you get, how do you exploit all this traffic and maximize the number of experiments? And then like, what a time to be alive. It is here. You can just like vibe code, vibe code it there. This is amazing. Okay, I want to show one last thing, which is my boy Jev. And we have been doing a lot of Jev episodes.

**Ezra Mechaber** [00:27:06] Poor one out for Jev.

**Claire Vo** [00:27:08] Poor, I would, I don't know, I think Jev's got a real shot at some longevity here,

**Ezra Mechaber** [00:27:12] Jev has the juice.

**Claire Vo** [00:27:13] But you have the juice, but you built something really cool with Jev that I want you to show, because it's a use case I haven't seen.

**Ezra Mechaber** [00:27:20] Yeah, yeah, totally. So, right, so for people who don't know, though, how could you not know, I feel like if you're listening to How I AI right now, Jev is this model where you can ask it really weird, complex questions in text, and you get like essentially a number back, right? So like, how good is this on a scale of 1 to 10? Or is this true or false? Or like, what is the meaning of life? Is it A, B, or C? And it's really fast and it's really cheap. And so I started thinking about all of the different places we could shove this that would really change the way that people work, right? So if you've used Figma has an agent on the design canvas, I adore it. It's really, really good, but it is still subject to all of the latency that you get with all of these top tier models, which is like, it's slow in places where you want to have a coworker and it doesn't feel like a coworker. And so as we work on that, Jev feels like really, really interesting for some of those possibilities. And one of the first things I was thinking about was this idea of like, what if it could run questions about things you were writing as you were doing it?

[00:28:28] Like, what if it could know that you needed to, if you've ever written a blog post and had a section where you aren't sure what's going to go there, maybe you write TK or you leave some brackets. And sure, you could do that like totally programmatically of just like look for and identify, but also maybe you have a claim that you're not sure like you have data for or you need to go look up in your notes later. And so I basically, I built this prototype. I'm going to forget the name of it, but there's, I think it's called Marker, which is this beautiful looking writing app from this guy John Steinbeck, which is an incredible name for a guy who runs a writing company. They have some of these ideas around it. And so as I was just playing with like what could be possible with Jev, that was kind of one of the inspirations here. And I wanted to have Jev basically make a call to Jev anytime I stopped typing. And so the thing that it does is when you stop typing, it will look for places where you've left blanks or claims worth supporting, and it will use stuff in your library to go ahead and actually like substantiate those claims.

[00:29:40] So in this case, like I said, most people find it easier to keep writing than to stop and look something up. And it's making a call here as soon as I stopped writing it into the library where it has all of these interviews about like what these people actually did. Like if I go hunting for a number, the sen- it will, I forget the sentence I was trying to write. We recently put the API behind our own internal firewall, so let me see if I can actually run it live or if it's going to get mad. Uh, okay.

**Claire Vo** [00:30:13] Oh!

**Ezra Mechaber** [00:30:13] And then-

**Claire Vo** [00:30:14] Hot dog.

**Ezra Mechaber** [00:30:14] Oh no, hold on. But it doesn't actually want to, is it blocking it? Oh, it is blocking it.

**Claire Vo** [00:30:21] I don't know.

**Ezra Mechaber** [00:30:21] It wants to run

**Claire Vo** [00:30:22] It im- it impressed me. It did something fast

**Ezra Mechaber** [00:30:24] Right.

**Claire Vo** [00:30:24] in my

**Ezra Mechaber** [00:30:25] Right.

**Claire Vo** [00:30:26] Okay, so I just want to, like, reiterate this for people because

**Ezra Mechaber** [00:30:29] Yeah.

**Claire Vo** [00:30:29] it is mind blowing, which is as you write, as soon as you stop for a minute, it runs a quick Jev check, which is very, very fast, and says, like, does something need to be filled in? Does something need to be supported? Like, what questions do I have about what you're writing? And then, like, hooks up to data sources and actually helps you improve your writing as you add Jev.

**Ezra Mechaber** [00:30:50] Right. Okay, so this is how it works. So you've got, here you've got your title. So this is my title. And as soon as I stop, it's going to start checking things. So maybe I've got, I was thinking about how we serve writers, and I thought TK. Great. And it's like you had a thought that you didn't finish. But then you'll see, like, it also ran a check and it said, I have no idea what you were thinking because it's not in this library. But then I could say something like, we spoke with X writers and they said, and it both knows that I need to finish this, and it went and pulled from the library, like, literal interview quotes from, like, writers we allegedly spoke to for this. A

**Claire Vo** [00:31:35] thousand out of ten.

**Ezra Mechaber** [00:31:35] So this one blew my mind.

**Claire Vo** [00:31:38] I will like this. You rarely get one of these at How I AI, a full Claire hands up, Jev.

**Ezra Mechaber** [00:31:45] It's so cool.

**Claire Vo** [00:31:47] It's so cool.

**Ezra Mechaber** [00:31:48] I just all, for literally for like two weeks after Jev dropped, I was just like running around going like, okay, but like, can we talk about Jev? Like, it was every meeting I was in. My engineers, some of them were very excited about this, some were maybe like a little eye rolly about it, but it's just, it's such a cool idea because I think you can imagine all of the different ways that if you could run checks on things at any given time, like what you would do with it. And I, the thing that sort of blew my mind was that they had built it for RAG or for essentially for like search and document retrieval as well. And so the ability not just to say like, this looks like a pattern, I am confident that this, you left something, but also I took this block of text and it relates to this section over here, and I did it in real time, is just like, it's kind of incredible.

**Claire Vo** [00:32:38] It's unbelievable. this podcast is now How I Jev, just

**Ezra Mechaber** [00:32:43] It did.

**Claire Vo** [00:32:44] We're rebranding.

**Ezra Mechaber** [00:32:44] I did have this really bleak thought, which is it made me wonder if, like, you could imagine you're interviewing for a PM job and you like yap your entire career into something, and then you have a voice to text that is just like searching against like what your examples are. And I did have this fear because I run a lot of Product Sense interviews that I was going to start running into people who were like Jeving their own little helpers, which I don't know, maybe I should hire them if they do, that's great.

**Claire Vo** [00:33:10] Yeah, hire them. I was like, great, sign me up. Ezra, this has been so good. Okay, we're going to get to lightning round. I just, to reiterate for folks, what do we see? PMOS with 31 skills, including what's up, what do I have going on today, find me people in the org, write specs, coach me, the whole thing. You basically are now using that through Codex entirely, also because Codex is magical for browser use. And then you built a real-time Jev editor, author, writing tool, that you're afraid is going to cause you trouble in future PM interviews or impress you in future PM interviews. So many good workflows in this. so the folks that have stuck with us this long, you have gotten some good stuff. quick lightning round questions, and then I will get you out of here. One, you told me a couple weeks ago you were using Instinct. Are we still on Instinct? What are we doing with our personal agent?

**Ezra Mechaber** [00:34:11] Okay, so I still get texts from Instinct and I don't respond. It's kind of the way it works. So, for people who don't know, Instinct is this really sort of beautiful idea, like I'm really into it, which is this idea that what if you had a proactive agent, but instead of like needing a website to visit or an app to use, it just like texts you in iMessage. And I will say I still use it every once in a while. It was this kind of magical thing at the beginning where it was proactive in the right ways and this like concept of memory that was like useful in this kind of mind-blowing way. And I suspect there's a bunch of people who have been running OpenClaw for months who are like, what's the big deal? But it just, it productized this really nice experience in a way that was really great. And for the first few weeks, you could buy things on Amazon with it, which, while not like a killer use case, was really nice because I would just walk around the house and I would say, hey, Siri, tell Instinct that I need to buy paper towels. Or like my current use case is I bike my kids around Brooklyn and I will run into potholes all the time.

[00:35:17] And now you can like, you can 311, like a fix my pothole.

**Claire Vo** [00:35:23] Mm-hmm.

**Ezra Mechaber** [00:35:23] And I never remember to do it on time because, like, you have to look at the address of where it is, and you have to report it, and the website is kind of trash. And so I have started, like, hey Siri, text Instinct, there's a pothole at, like, 269 Atlantic, and it just remembers, like, what it's supposed to go do and submits it. So I do use it for that, and it's amazing for that, but I mostly switched over to Dots now that I'm, like, fully Codex billed.

**Claire Vo** [00:35:49] I- I, I, so I, um, am trying to make Dots ha- I'm

**Ezra Mechaber** [00:35:55] You're like, you're like Grok and Muse, is that right?

**Claire Vo** [00:35:57] I-

**Ezra Mechaber** [00:35:58] That's your

**Claire Vo** [00:35:58] So I'm like max- Codex maxing. I love Codex. You could rip Codex out of my cold dead fingers, but for work, I'm all Grok.

**Ezra Mechaber** [00:36:07] Yep.

**Claire Vo** [00:36:07] But, and then for pers- you should check out Muse. It's a real, it's a real delight. Um,

**Ezra Mechaber** [00:36:12] I can't, I can't bring myself to do it.

**Claire Vo** [00:36:15] I know, but they've been stealing our data for 2 decades, you know?

**Ezra Mechaber** [00:36:18] I know.

**Claire Vo** [00:36:19] That's

**Ezra Mechaber** [00:36:19] I know.

**Claire Vo** [00:36:20] That's my- I- I- as I say to people, the devil I know. This is really

**Ezra Mechaber** [00:36:25] Totally.

**Claire Vo** [00:36:25] where I'm at

**Ezra Mechaber** [00:36:25] Yeah.

**Claire Vo** [00:36:25] with my personal

**Ezra Mechaber** [00:36:26] They already

**Claire Vo** [00:36:26] agent.

**Ezra Mechaber** [00:36:26] have the data. So fair.

**Claire Vo** [00:36:27] They already ha- I said- my joke is my Instagram ads will get better. I'll- I'll end up spending more money.

**Ezra Mechaber** [00:36:32] This is- I think this is like a real value prop. Um.

**Claire Vo** [00:36:35] Okay, and then my last question for you, when your dot is

**Ezra Mechaber** [00:36:40] Yeah.

**Claire Vo** [00:36:40] being obstinate, your AI is not giving you what you want, are you a yeller?

**Ezra Mechaber** [00:36:45] Yeah. No, no, I'm not. I think we should all be nice to our AI. I treat my AIs like a friend that you love who's really like messing it up. You know, you're like, buddy, like, get your life together, like, you're too old for it. That is how I treat, so hold on, I will show you because I yelled at my dot twice today, but I did it very friendly. Okay, so I ordered some shoes. They were too big. I need a half size down, and I tried to like find it, the cheapest version, and it was like, email search is temporary rate limited. Can you go search your email? And I was like, I don't know, man, that's what I needed you for. and then it gave me some like really expensive stuff, and I thought maybe it was being lazy, and so I just said like, yike, assume you aren't going to check this. And I was trying to figure out why I don't yell, and I think partially, like you can ask my wife, I am like mostly not a yeller, but I also think someone posted this on Twitter recently, and it really expresses how I feel, which is not that I have some, for people who don't know, there's like this idea of like Bas- what is it, basilisks?

[00:38:00] The like, this idea that if you're mean to AI, but then it turns out they're alive, like, wouldn't it have just been easier to be nice? Like, isn't that cheaper than like getting turned into a paperclip? And I don't, I don't think they're conscious. I don't think they're approaching conscious, but I do think it's really bad for the soul to just be mean to things all the time. Like, in the same way that you like, like, there's just no reason. Like, it's just, I feel like I get worse when I, like, yell at things that can't help it, even though I don't think it's conscious.

**Claire Vo** [00:38:28] You know, I, like, used to be a very hardcore not yeller, and I'm not, like, I'm not mean. I wouldn't say- I'm not saying anything

**Ezra Mechaber** [00:38:35] Yeah.

**Claire Vo** [00:38:36] nasty, but I am a very- I'm a- I'm like a all caps, like, why? Like, why? Why are you like this?

**Ezra Mechaber** [00:38:43] Why would you do this to me?

**Claire Vo** [00:38:44] And here's- and here's why I'll say this. I'm spending thousands and thousands, if not tens of thousands of dollars on LLMs.

**Ezra Mechaber** [00:38:52] Yes.

**Claire Vo** [00:38:52] Like, a why are you like this after, like, 2,000 dollars of wasted tokens?

**Ezra Mechaber** [00:38:57] Yeah.

**Claire Vo** [00:38:58] That's like, that's like a cheap-

**Ezra Mechaber** [00:39:00] But that doesn't strike me as that mean.

**Claire Vo** [00:39:01] Yeah.

**Ezra Mechaber** [00:39:02] You know, like, I have, you know, there's like, there's some real, like,

**Claire Vo** [00:39:05] Like

**Ezra Mechaber** [00:39:05] road rage

**Claire Vo** [00:39:05] nasty kind of stuff.

**Ezra Mechaber** [00:39:07] Yeah.

**Claire Vo** [00:39:08] No, I'm just expressive.

**Ezra Mechaber** [00:39:11] Yeah. I think that I will say my take is that normally when I want to yell at AI, it's because I have given it poor instruction. This is how you know I have kids, is like, there's so much of that, which is like when you get a bad result, the odds that you have like poisoned the context and asked a bad question is like pretty high. And so I will occasionally find myself in loops. Like Codex has this, Codex, if you're listening, OpenAI team, if you're listening, has this really bad bug right now where if you start a local session and you kick it to a remote session, even if you have YOLO mode enabled on your remote session, it inherits the sandbox with ask permission every time. And so I wind up in like clicking approval hell, and I get so mad, and I go around in loops for a little while where I'm like, we already fixed it, like you have permission. I'm looking at the file. I pulled up the file. We're looking at the config.toml together. Like, what are we doing? And usually the answer is like, the context is poison in that conversation.

[00:40:14] It's unrecoverable, and yelling at it is not going to help, so start a new conversation and just move on with your life.

**Claire Vo** [00:40:18] Well, let me-

**Ezra Mechaber** [00:40:19] Which is not satisfying, but it is how I feel.

**Claire Vo** [00:40:21] Let me give you a TikTok parenting tip if you want to, like,

**Ezra Mechaber** [00:40:25] Yes.

**Claire Vo** [00:40:25] really devastate your AI by being a kind parent, which is, I know that you're capable, but you're not

**Ezra Mechaber** [00:40:34] Oh, yeah.

**Claire Vo** [00:40:35] you're not- you're not showing me how capable you are right now, and that's just signaling to me I need to be a better parent.

**Ezra Mechaber** [00:40:43] My- okay, that- I love that. that one, stealing the parenting tip, two, stealing it for AI. I feel like I really love to give my AIs like big expectations, and I feel like you saw it in the math proof, but like I have been doing a version of this, which is like, buddy, like I know you can cook, like you would not believe the things that I've seen out there that you are capable of. Like if you try a little bit harder, I am sure that we can vibe code this prototype that I can show my engineers so that we can build it. Like, I know this is in your capabilities.

**Claire Vo** [00:41:17] I know you can vibe code Salesforce just a little bit more. Okay, Ezra, this has been so fun, so many good use cases, so many good thoughts. Where can we find you and how can we be helpful?

**Ezra Mechaber** [00:41:31] Yeah, mostly on Twitter. I post too much, Ezra McAber. and then in terms of being helpful, we're hiring PMs. We're hiring a lot of PMs, and we're hiring a lot of different kind, if you're an engineer or a designer, we are hiring. Come work at Figma. It is the most fun I've ever had in a job. we're just, we're building really cool things, and the people are great.

**Claire Vo** [00:41:54] Amazing. Cannot, cannot end it better than that. Ezra, thanks for joining How I AI. Thanks, Claire. Bye. Thanks so much for watching. If you enjoyed the show, please like and subscribe here on YouTube, or even better, leave us a comment with your thoughts. You can also find this podcast on Apple Podcasts, Spotify, or your favorite podcast app. Please consider leaving us a rating and review, which will help others find the show. You can see all our episodes and learn more about the show at howiaipod.com. See you next time.
