---
podcast: "how-i-ai"
podcast_title: "How I AI"
title: "Claude Code for normal people: skills, voice mode, and how to collaborate with AI"
date: 2026-08-10
url: "https://podcasters.spotify.com/pod/show/pen-name/episodes/Claude-Code-for-normal-people-skills--voice-mode--and-how-to-collaborate-with-AI-e3n48ci"
guid: "f44825c8-94f4-453f-bca6-0ae008422cb0"
host: "Claire Vo"
format: "interview"
level: 2
length: "00:42:40"
categories: ["agents", "work", "marketing", "coding"]
featured: ["Claude", "Claude Cowork", "Claude Code"]
mentioned: ["Slack", "ChatGPT", "OpenClaw", "Claude Opus"]
transcript_source: "azure-asr"
transcribed_by: "MAI-Transcribe-2"
---

# Claude Code for normal people: skills, voice mode, and how to collaborate with AI

**Speaker 1** [00:00:00] Prompt engineering is dead, but intent engineering is where we need to be focusing our time. I do a lot of work when I'm walking and on the go, and I spoke maybe for 2 or 3 minutes and just said, here's my problem. Claude came back to me and said, I think we need to be creating an interactive artifact that's password protected. That is a prompt going from a hyper-engineered chunk of text to a conversation that's 3 or 4 minutes. Claude needs to get the prompt out of you.

**Claire Vo** [00:00:27] You have another example at the personal level as a fellow email hater.

**Speaker 1** [00:00:33] What did Gmail do to us?

**Speaker 2** [00:00:35] What did Gmail do?

**Speaker 1** [00:00:37] I know it was once upon a time amazing. It is like everybody has a key to your front door and can come leave things in your house. No more. I want to show you what I built out of pure frustration. Send in Gmail, this will push it to Gmail, a draft, and then hopefully open up a browser window and get it the extra mile. This gets me pretty much where I want to go because I can go back in here and work with Claude and chat and have the reply drafted, or I can just send it and never have to deal with it again. My job is to sit over your shoulder and smack your hands every time you open Slack or Gmail or Google Calendar and say, no, Claude. People need to feel the benefits in order to keep using it. That's actually not true. Instead, people mostly need to understand that we're going to learn to collaborate. The real hump to get over is defaulting to this and building the muscle memory of simply opening an app.

**Claire Vo** [00:01:39] Welcome back to How I AI. I'm Claire Vo, product leader and AI obsessive, here on a mission to help you build better with these new tools. Today I have Grace Clark, and she's going to show us Claude for normal people, but not really for normal people, for people who want to show up to their clients and to the many, many, many people in their inbox with a level of personalization and professionalism that only an AI agent can provide. Let's get to it. This episode is brought to you by Bolt.new, the AI app builder for people who have ideas and want to ship them. Most AI tools spit out code that looks great in a demo and falls apart the second you try to do anything real with it, or they lock you into their own platform with no real way out. Bolt is different. You describe what you want to build, a startup MVP, a landing page, an internal tool, a side project, and Bolt generates production-ready code in minutes. Connect Stripe or any other MCP, hook up your domain, and deploy it live.

[00:02:40] Founders are using Bolt to build businesses doing real revenue. Product managers are shipping prototypes their teams actually use. Designers and marketers are launching campaigns without waiting in line. Anyone can build, engineering can ship, everyone wins. You just need an idea and a weekend. Check it out at bolt.new/howiai. Grace, welcome to How I AI.

**Speaker 3** [00:03:07] Thank you for having me.

**Claire Vo** [00:03:09] I am excited about this episode because one of my hypotheses about how AI is going to kind of like impact our work is it's really going to allow us all to differentiate on service a lot better, and I think the bar for service and service quality and customer relationships and human relationships overall will go up because we'll be able to do more and make things more customized for the people that we're working with and the people that we collaborate with. And so I love some of the stuff you've built, and I wonder if you could just walk us through what brought you to some of these AI projects you're going to show us and what problem you were trying to solve.

**Speaker 3** [00:03:49] I am a big believer that AI is democratizing the way all of us are going to work if we put in the work. And I was thinking about different efficiencies that I could build in my business. I'm an AI teacher and a former marketing consultant, so very relationship driven, very process driven business. And I started teaching myself how to build an OpenClaw in January, and I was posting about it enough on Instagram that people said, "You should teach a class. You seem to be documenting this. There's a process. Would you ever want to get people together in a room and do it?" The process of teaching myself OpenClaw and building a curriculum is now the foundation of what I teach people, and it's the reason I have a few core products that I've built that I actually use in my curriculum. So now I've built a few processes and products that run my business that I actually teach to my students and then the teams that I get to train.

[00:04:49] The most impactful is my pipeline operator, and that's because underneath it is solving a few problems. One, just a deluge of emails. Email is a scourge. Nobody wants to be in Gmail anymore. So my Claude is ingesting all of that and correlating it with a bunch of context. The second problem it's solving is that client relations and relationship building is really devoid of any emotion and love. So when we can make visual expressions of that through HTML, interactive HTML and encrypted documents, it's a really warm welcome, and it's a much more hospitable way to communicate process. And then third is I simply cannot keep track of 20 open tabs in any given day, much less organize a process where I'm meant to support people and teach them and support them through learning. So going from 20 tabs and 20 hours a week on admin just to be able to teach people was so painful.

[00:05:54] I wasn't doing the teaching, and I just had a hunch that there was going to be a way to solve all these things. The first thing I did was open up Claude Code after having it downloaded for 2 hours, and I yapped into it everything I just told you, and I sat back and let Claude take me through the process and learned from the jump how to collaborate with agentic AI, and now I have a pipeline that runs once an hour, and it's probably the most popular thing I teach.

**Speaker 4** [00:06:26] Amazing. So can we actually see what this looks like? Because I think there's a lot of folks that, have businesses similar to yours that are just looking for practical ways to integrate this into your flow, and so I'd love just some inspiration on how this thing actually works.

**Speaker 3** [00:06:43] You don't need to run a whole process like this in order to have Claude or Agentic AI support you. On demand, it can generate a proposal without all of this underneath.

**Speaker 4** [00:06:54] Mhm.

**Speaker 3** [00:06:54] It's something that looks like this. At the core of this is a skill file that tells Claude to create a proposal in HTML, and the outcome is something that looks like this.

**Speaker 4** [00:07:07] Yep.

**Speaker 3** [00:07:08] Beautiful, branded, reflects all of the context from conversations I've had with someone, puts it into a process that I actually get to talk to and iterate, and then we get to gift the client this wonderful welcome to the way that we're going to work, and it acts as a bit of an advertisement for what they're going to be able to do, because immediately they're typing a password into a site that looks like them, that feels like them, that they can interact with, and I get to say, this is what you're going to be able to build by the end of our time together. It also spits out interactive pre-work that gets someone prepped for our time together, automatically will pull updated documentation from any of the large labs that we're going to be working with. You can click around. On the back end, this is communicating to me where people are in their progress, so I can nudge them if they're not quite ready for our training. And my favorite part that I just added on to this skill is the generation of a questionnaire before I have a session with people, so I can understand themes and where they're at, where they're stuck.

[00:08:20] What have you started using Claude for since our first session? What's challenging? Seeing themes here is really helpful, and there'd be no way for me to have gathered this through Slack DMs or one-on-one conversations with a 30-person team. That's just not going to happen. So underneath, this is the same logic. It's a Google form, but it is much more branded, much more fun to make, and students and clients will say, I need to learn how to do that myself.

**Speaker 4** [00:08:47] Teach me. What I tell people when they are trying to drive AI adoption internally, so I like, I get to work and talk to a lot of executives, and they're trying to teach their teams to use AI and give them good reasons to use AI. And I tell them, if every touch point that you do is not AI first, then how can you convince people that every touch point they should do should be AI first? So I'm like, if your agendas, you know, you're not doing the best job doing these like cool HTML, sort of like custom agendas for your meeting. If you're not, if you're not using an agent, if you're not customizing them, then you can't demonstrate to others how you can change how you work. And so I love this from the moment you're trying to, I would say, like, incept a client to really see the AI future. You're setting a vision by saying, if you use AI the way I am just implicitly using AI, you're going to get this level of quality asset, and just imagine how that could go to your customers. I mean, the other thing that I always tell people is I try to get out proposals very fast.

[00:09:51] I'm sure you can get proposals out very fast, and I'm like, if you improve your AI use, you too could get proposals out in like 45 minutes if you really wanted to. And so I think like setting the standard of like speed, quality, personalization is a good way to just get people to start seeing the impact of AI and how they can imagine it in their life or their work.

**Speaker 3** [00:10:15] The number one thing that I get asked when I'm teaching is how can I build the muscle of going to AI, of going to ChatGPT desktop, of going to Claude, and underneath it, I need to support them in building a muscle. So teaching them that everything we're looking at is AI is not sufficient, which is one of my big lessons from teaching now. Instead, there are two things that I really focus on doing, even for friends who are just asking how they can get into this. One is to build a forcing function in your environment that gets you to open up Claude. And the easiest thing is to set a Slack reminder or a Google Calendar alert that says whatever you're doing, screenshot it and put it into Claude. Get the whole window and just ask Claude, could you help me with this? We are just trying to build the muscle of deferring to Claude and asking, could you be my shadow and help me here? With a screenshot is no text. Claude can infer. It shows people the magic power of inference and that Claude can come to you with a prompt that is just an image.

[00:11:19] The second thing I tell people is let's actually build a skill together. So I host virtual co-working sessions now, and we'll build a voice guide, and underneath it, people will be able to look at their markdown. And I make an effort to teach people technical terms, even if in the near future we don't use them, because that builds confidence and it eradicates this view of not being technical. That is the biggest hump to get over, is that people think I'll never know how to do this, so they don't have a chance to get the value out of it. So teaching people this muscle memory and then getting them excited about the technical aspects of this turns everyone into this excited adopter. It can be a really slow process.

**Speaker 4** [00:12:02] So show us how this actually works behind the scenes, because what I'm seeing is like customized content, customized branding, you have this whole pipeline, like kind of what goes into building something like this?

**Speaker 3** [00:12:15] It's really just three steps, not to simplify it too much, but underneath it is some standards that you document with Claude. For me, it's a voice guide, and it is an explanation of what a proposal is for me, defining those two things, putting it on a timer, and then having everything pub to Netlify. So I want to show you what it actually looks like, give you the roadmap. Yep. One thing I teach all my students is the importance of verbalizing an SOP, especially when we're building workflows, whether it's one simple task or many chained together. So one of our exercises is yapping into Claude and having it make us a roadmap that we can understand, are these steps right? It's as if we're training a new employee. So underneath, I'm going to show you the skills. It's a pipeline operator that wakes up every hour and checks a couple things for me and knows if we need to move clients through different steps or make something. It's my proposal maker, which I'll show you, and it's my voice guide, my how I think and sound guide.

[00:13:20] Extra cherry on top is sometimes I will run a proposal through my board of directors, and on that board right now is Kat, who's the head of Applied AI at Anthropic, Ben Thompson from Stratechery, Jamie Dimon, who is going to give me a really solid CBA cost-benefit analysis, and then a skeptic, an investor, and a founder, and I will run everything at the end through them. But I want to show you underneath what it actually looks like. So Proposal Maker, I updated this one yesterday. I like to teach students to version their documents and add naming conventions to it so they feel more connected to their tech. But this outlines exactly what I need to do. It has a change log at the top, and then it has rules about my philosophy for teaching, which is where we define the difference between teaching and consulting. Has different steps, different reference points. It will also explain how it to itself how it needs to lay out this document.

[00:14:24] Has different workflows, confirms the deal shape. On and on and on and on.

**Speaker 4** [00:14:31] And how did you, how did you make this skill? Just like, what's your general, like, skill making process? Did you write this by hand? Did you use our favorite, the Yappers API to get it out? Like, how did you actually build this skill?

**Speaker 3** [00:14:45] I'm a big believer that prompt engineering is dead, but intent engineering is where we need to be focusing our time. Technically, this was me on a walk opening up the Claude mobile app. I do a lot of work when I'm walking and on the go, so the mobile app is incredible for getting things out of your head in an unfiltered way. And I spoke maybe for 2 or 3 minutes and just said, here's my problem, and here's what I think I want. First, do not interview me ever. I hate this have Claude interview you approach. The work should never be on you. Claude has immense amounts of context if you've connected it right. It should be studying you and then coming back with a really strong idea that you can react to. So I always put the pressure on Claude, and I said, come back to me. What do you think this process could be? Is this even possible? And Claude came back to me and said, I think we need to be creating an interactive artifact that's password protected. What do you think? And we went back and forth. That is a prompt going from an hyper-engineered chunk of text to a conversation that's 3 or 4 minutes.

[00:15:50] Claude needs to get the prompt out of you. So this was 10 minutes of talking and then an hour of Claude creating this thing and me giving it feedback, actually creating an HTML right inside Claude that I was pressure testing and throwing screenshots in of what I liked and didn't like. This was the very first thing I ever made when I was making the pipeline operator, and I pretty much did it mostly on my phone.

**Speaker 4** [00:16:14] I love it. I love it so much. And how often do you, like, do you read this really, unless you're teaching or you're like, "That's Claude's business, that's not my business, and as long as the output's good, I'm happy"?

**Speaker 3** [00:16:26] I think the world is right that HTML is the new Markdown, which I know is an easy thing to throw around, but it's true. I actually don't read Markdown anymore unless I am teaching. Occasionally, I'll go in here and point to certain things, but I want to see my Markdown visualized.

**Speaker 4** [00:16:45] Yep.

**Speaker 3** [00:16:45] I am not in here anymore. I do look at the markdown for my voice guide, which is another part of this proposal maker. It is a skill that auto fires in almost every single thing I do because it's not just a voice guide, it's a think like me guide, and it's the best corpus of how I make decisions. So Claude always needs to have that ready to go. So I want to show you that too. All right, pride and joy, and the number one thing I teach in my class because it is a quick win. It forces us to learn the power of ingesting context, and it teaches students how to push and collaborate with Claude and then commit something so that it is an invokable skill. What's most interesting about creating this is all it requires is you telling Claude how you think and then having it go study you. So to create this, which has all of my philosophy of communication, words I use, words I don't use, this started with me saying, I think I need a guide that will make everything more like me.

[00:17:49] And that was the very first instruction that I gave Claude, and it had the idea to produce more of a communication and philosophical guide. Only down at the bottom do we start to see words I use and words I don't use, which is where we get, we avoid the AI slop of it all. And now my students can take this and repurpose it for themselves. No fluff, no filler. No, you're absolutely right. Here's the uncomfortable truth. I never want to see these things, and most people don't either, which is why this gets updated so often. I'll just voice note into Claude and say, I saw this terrible post on LinkedIn. Can you make sure my voice guide never touches something like this? Yes, I mean, underneath this in the session log is just basically me calling out all sorts of people on LinkedIn who I never want to sound like.

**Speaker 4** [00:18:41] It's just like a moving target too, because every time one of these new models come out, it like it ships like two or 3 really obvious tells, and then it just starts to like grind my gears every time, every time I see it. I think, side note, I think on TikTok I could do, you know how those, I don't know if you know this, how like there are women that will like close their eyes and they have like a blind box and they taste the different Diet Cokes. They're like, this is Diet Coke in ice and this is Diet Coke from a can. I could do that with slop from a model. Easy, easy, I could do it. So maybe there's going to be a new How I AI mini series on Claire blind taste testing slop from different models.

**Speaker 3** [00:19:21] Do you think you could pick pin- pinpoint Opus 5?

**Speaker 4** [00:19:24] Yeah, I think I could pinpoint Opus 5.

**Speaker 3** [00:19:25] I think you probably could.

**Speaker 4** [00:19:26] Yeah. I could definitely pinpoint Fable.

**Speaker 3** [00:19:29] I should bring this into my

**Speaker 4** [00:19:30] And I could definitely pinpoint 5.6, uh, GPT 5.6. Easy.

**Speaker 3** [00:19:34] Our sweet 5.6.

**Speaker 4** [00:19:36] Our sweet 5.6.

**Speaker 3** [00:19:37] Our sweet 5.6. So the point really of preserving instruction in skill files has been the biggest teaching for me.

**Speaker 4** [00:19:47] Yep.

**Speaker 3** [00:19:48] Is getting people to understand that you are going to chain these things together and that you can write code, like Karpathy said years ago, the hottest programming language is English, which is really why I think I have a job and also why I think I won't have a job in a couple months. I don't think I'll be teaching this way, but being able to help people understand how to prompt and then end up with an entire workflow is really powerful.

**Speaker 4** [00:20:13] I love it. Well, this is, I mean, I think a bunch of folks can take inspiration from this. So if you are working with clients and you want to deliver highly customized, both like proposal, onboarding, tracking, training experiences, and you want them to sound like you, and you want it to look like them. I think take inspiration from this and build your own sort of like SOP. And again, something that I tell people a lot is AI has forced us all to sort of write down the processes we have been doing kind of mechanically in our businesses and actually write down, like, in an ideal world, how would I do this thing step by step? Because now you have that ideal world, because you have sort of this limitless intelligence and ability to execute on tap, which you may not have had a couple years ago. And so I say, go down and write the ideal way you would do proposals, the ideal way you would do content marketing, the ideal way you would do software engineering, and then that SOP can be executed and automated by AI, and then you have an even better performing business.

[00:21:19] So I think this is really great example at the business level. You have another example at the personal level, as a fellow email hater, hater, hater. Let's just get rid of it. Let's game over. You text me all day.

**Speaker 3** [00:21:33] What did Gmail do to us? I know it was once upon a time amazing. It is like everybody has a key to your front door and can come leave things in your house.

**Speaker 4** [00:21:45] Yes.

**Claire Vo** [00:21:45] No more.

**Speaker 3** [00:21:46] We cannot work like that. I want to show you what I built out of pure frustration. It started as a rant into Claude Code and has now become a recreation of Gmail that lives in my Claude. So I haven't intentionally opened Gmail in a month out of muscle memory. I think we might for a while, but we can get out of that slog of emails and not just get out of it, but do one better. We can actually be training our AIs as we respond and communicate through Gmail. If we stay in Gmail, all that learning and all that writing and all that work actually doesn't go anywhere. It doesn't compound. It's just locked away. So now rebuilding Gmail is a project that I think everyone can do in a half hour, maybe a little bit longer if we want to get fancy with it, but I want to show you what it looks like and then talk you through how I built it.

**Speaker 4** [00:22:41] Amazing.

**Speaker 3** [00:23:55] So functionally, this is an artifact in Claude Cowork. Cannot get more simple than this. And the process was talking to Claude Code and having it write a markdown file that I saved to my computer that I brought into Cowork. One thing that took me a long time to actually accept was that it is easy to move ideas and conversations between sessions or between products. So the Claude desktop app, Cowork, underneath it's code, but moving things back and forth across that partition is just as simple as asking Claude, can you write me a markdown file for another session? Can you write me a markdown file? I can bring this conversation elsewhere. So I went back and forth with Claude saying, I hate Gmail, absolutely never want to be in it. It's the bane of my existence because I avoid things that I don't want to do, and it creates this emotional experience for me. I don't really care about inbox zero. I don't go there. I just want to have a better relationship with my work.

[00:24:55] Claude was like, let's rebuild Gmail, and let's have it look the way you want. Let's choose the colors that you like, and I'm going to mock it up for you and pull in some of your real information, and we're going to go from there. Back and forth, back and forth, the process was just asking Claude, can you change this? Can we add a link? Can we add bolding? Can we push this to Gmail? Let's see what happens. can I do a live one and see if it works?

**Speaker 4** [00:25:21] Yeah, please.

**Speaker 3** [00:25:22] Okay, totally okay, embarrassing myself. Let's see. Okay, a student wants a recording for the class. I don't like this draft, it's totally fine. Sending it today, oh my gosh, thank you for the reminder. Send in Gmail. This will push it to Gmail, a draft, and then hopefully open up a browser window and get it the extra mile. But let's see what's going to happen.

**Speaker 4** [00:25:48] Ah! Magic!

**Speaker 3** [00:25:50] Okay, well, it decided it wants to use the actual original email. Troubleshooting aside, this gets me pretty much where I want to go because I can go back in here and work with Claude and chat and have the reply drafted, or I can just send it and never have to deal with it again. I love it. The ideal it process is just telling Claude the outcome you want and the problem that you have and letting it fill in the gaps. Otherwise, if we are overdirecting it, we're in its way, and we are not letting it reverse engineer the solutions to our problems. So no more prompting, be conversational, give it your outcome, and then let these powerful models help you and carry you and teach you how to work with them. They will rebuild Gmail for you, and you'll never have to go into Gmail ever again.

**Speaker 4** [00:26:40] I love this use case because I've seen almost everybody I know do this. They're like, I hate email, I'm going to rebuild Gmail. And what I love about this as an exercise for almost everybody, it's universally applicable. We all hate our email, we all have too much, and we're all unique snowflakes in that, like, you like this, like, long thing with the pre-draft prompt. I'm like, I just want a voice agent, like a magical EA that just whispers to me and says, hey, Claire, what do you think about this email? And then I whisper back, and the email gets sent without me even thinking about it. Like, we all want our, like, special little thing. I have a friend who has, like, completely built a desktop app that does this. Like, there's so many different ways that you could, think about your email experience. And again, what I love about something you said earlier when we were prepping for this conversation is people feel like I have to be super technical to pull this off. Like, I have to be a software engineer, capital S, capital E, to pull- I have to know what a server is, I have to know all the stuff.

[00:27:41] And I'm like, no, actually, you just have to type, I hate Gmail, build me a better one into Claude Code, and you are off to the races. so can you just show us how you even got started building this thing? I know you just said, like, I hate it, rebuild it, but was it like a one shot? Did it take a little time? What is it using connectors behind the scenes? Kind of how does it technically work?

**Speaker 3** [00:28:05] The technical elements of this, the way I built it was, I wish it was a one shot, although I'm grateful for the collaboration with these tools, but underneath it, I just followed a few steps. One was I connected every single thing that I could and then made custom connectors and custom plugins for the other data sources Claude was going to need. For example, Claude has a hell of a time right now writing to Google Sheets, writing to Google Docs. So I made custom plugins, which taught me the process of making a Google Cloud project and a service account, which taught me scoping and permissions, and now I get to teach that to students. Those just live right here in my settings. Super simple. I made a bundle, updated it on June 25th, but this is giving Claude some of the context and access that it didn't have. So I figured out what I needed to pipe in so that this would be useful and spent time doing that, and then opened up Claude Code and asked, can you help me do this?

[00:29:06] The reason I chose Claude Code is because I find it to be much faster, much more efficient, and much more proactive. If Cowork says I can't send an email, Code's answer to that would be I can't do it with the official connector, but I can always open up a browser window and I can try to drive it that way, or I could try to find something else. So I use Code anytime I'm kicking off a project or something really ambiguous or something that to me feels technical. And then I asked that Claude Code session, once we'd scoped it out and built some connectors, I said, I want to take this the rest of the way in Cowork. I like that UX better. It's a little more hospitable for someone who is actually trying to see something visual. Write me a markdown file. And Claude saved a markdown file, a session handoff to my desktop, and I went right back into Cowork, opened up a new session, and did nothing other than drag that markdown file in here, and Cowork took over from there.

**Speaker 4** [00:30:02] So to recap, you started this thing in Claude Code. I agree. I find that Claude Code and Codex on the ChatGPT side just like much more proactive and like, I think I can figure it out, than Cowork. I also find it much faster. So, anybody that's been in Cowork that wants to like up their ambition but is intimidated by Claude Code, don't be. It's kind of like same, same, and you can always go back. And so, I love that you built it in code, you imported it in Cowork, and now you're operating basically in the Cowork browser, plus popping open a Chrome browser when you need to like press a button, and you have a really effective email triage agent. Grace, this has been super fun. I think this is really great for small business owners, for anybody who is like responsible for a lot of things across internal and clients, doing a lot of communication. I want to get to our lightning round questions, and then get you back to, I bet your pipeline three times a day is about to run.

[00:31:02] You're going to get a bunch of inbound, and you'll have your agents off to the races. So my first question for you is, outside of these sort of like big projects, pipeline operator, rebuild Gmail, are there any like tiny hacks that you find yourself reaching for as somebody who has really immersed themselves in AI?

**Speaker 3** [00:31:23] That is such a good question, and I have a really silly personal one

**Speaker 4** [00:31:28] Great.

**Speaker 3** [00:31:29] that was one of the first things I ever built, and I can actually show this one to you live. I track my workouts for no reason. I'm not training for anything, but I like to have a record, like a true Virgo, of what I have done in my life. So I voice note Claude anytime I take a walk or go to the gym, and I say, I worked out. Can you track all of these exercises and update a spreadsheet for me? So here you have my workout tracker that Claude made. This is none of my business. I do not know what goes on here. I don't go into it. And one of the lessons of working with Claude is to let go and let it put information where it needs to be. So I could say I worked out today, did Bulgarian split squats.

**Speaker 4** [00:32:25] Ah, cool girl.

**Speaker 3** [00:32:26] At the gym, in Nantucket. Add to tracker. Also, Claude has demolished my typing ability.

**Speaker 4** [00:32:35] Oh, of course. No, no, no, no spelling required, no typing required.

**Speaker 3** [00:32:40] No typing required. So asking Claude this will usually pull up a few things behind the scenes, and this also works when I'm on my phone, which is useful because sometimes I don't want to be in front of a screen. Yeah, but Claude might come back and say, I want to clarify a few things. What did you do? So we're going to let it crank and see what it does. Ultimately, it is going to update this spreadsheet and keep a running list, and then I can ask Claude, what should my next workout be? What am I doing? Why do I feel so sluggish? But this has been really helpful. And then the more personal use is to send it pictures of plants. I'm a gardener, and I really love understanding what plants are growing where. So Claude and I have an ongoing chat where I just screenshot it pictures of plants. ChatGPT gives it obviously a run for its money with image detection and generation, but so much happens in Claude, and I plan some gardens and gardening projects in Claude, so I want all that context. I selfishly want it all in one place.

**Speaker 4** [00:33:37] I have to make you laugh because it feels like a year ago, I don't know when it was when GPT-5 came out. I got some early access, and one of the like tests that the OpenAI team wanted us to just experiment with to see how it worked is like, could it make a good personal website for you? And the design was great. That's what kind of we're like looking at, at front end design kind of feedback from some developers. And mine was like, really thought I was into lemon plants because all my ChatGPT prompts were like about my container lemons and like I have ants on my lemons, and my lemons are blooming, and like, when can I eat this le- I was like ve- like lemon plant mom. and so it's really funny when I see people put out these like, have Claude or have ChatGPT like tell you what you don't know about yourself, and I'm like, I'm a very specific person. I'm not my best version of myself to ChatGPT or to Claude.

[00:34:39] I don't know if that's like the mirror that I want to put on myself. I love this. I see workout tracking, nutrition checking, plant tracking, all on the go, all on phone. second question, you know, you teach like AI for normal people, which I love. What do you think is the most common like barrier or misconception people have to adopting AI that you have to like get them over the hurdle in order to like enjoy the benefits.

**Speaker 3** [00:35:07] That's so funny. I was just talking about this with Claude, but also with some of my students today. I teach class, and I said, is it unhelpful that I'm giving you these Mondo prompts? I'm basically doing the work for you. And they said, yes, this was what I was giving students before, just incredible direction to preload their Claude so they would get to a quick win. I thought people need to feel the benefits in order to keep using it. That's actually not true. Instead, people mostly need to understand that we're going to learn to collaborate and that we're not going to prompt, but we're going to collaborate. So the easiest way to do that when I'm with students or friends is I tell them to set a reminder in their phone to screenshot what they're seeing and bring it into Claude, just to say, might you help me with this? And to walk them through the process of actually having a couple of regular tasks that I help them set up. The real hump to get over is defaulting to this and building the muscle memory of simply opening an app.

[00:36:15] I'm surprised how so many people I teach don't want to learn. They don't want to put in the time, and my students are coming to a class, but my clients are forced to go to a training, and they're not always willing participants in this doomer future, and being empathetic and getting on the same level with them is the way to encourage behavior change. What we're really doing is teaching people to collaborate with a different tool and understanding where their fear might be coming from.

**Speaker 4** [00:36:48] So I occasionally coach CEOs and executives on AI, and I'm like, you got to be the most Claude-pilled person in your org, so I'm going to teach you how to do this. And I joke with them, I'm like, my job is to sit over your shoulder and smack your hands every time you open Slack or Gmail or Google Calendar and say, no, Claude, no, Claude's just like behavioral reinforcement. I need like a fly swatter because that is like literally it. I tell them exact same thing, like when you are staring at a task that you hate, that you're like, ugh, my brain cannot get me to write this Slack, respond to this email. I'm like, that is the moment. Capture that moment. I love your idea of taking a screenshot, so I'm going to steal that screenshot and go, "Dear Claude, save me," because it truly is just muscle memory. It's like total muscle memory. And so, yeah, you got, you and I are in the same, in a similar business of just like redirect, redirect, redirect.

[00:37:49] Eventually, eventually we'll get there, right? Like we've done all these things I've seen, you know, believe it or not, people, we did not used to have Slack. We didn't. It did not. We did other things. And so, like, redirection of behavior is positive. I do think there's something to the products themselves, like, going back to my Slack example, like, we didn't used to have Slack. Slack was fun, and so it got people to adopt because it was like communal and fun and customizable and like, you know, like did unlock some value. I think, sometimes people think of Claude less, like it's not as fun, and you have to, like, do get it to the fun aspect, but I agree, muscle memory is the thing that's got to change. I'm going to point out one thing on your prompt and go to my last question. You start this prompt adorably by saying, "Hi, Claude." It's like a very charming way, very charming way to greet.

[00:38:53] Use those two tokens, baby, to greet, to greet Claude. My question for you is, when Claude is being annoying, sloptastic, not doing what you want, what's your prompting strategy? Do you yell?

**Speaker 3** [00:39:08] I am not proud of anything I'm about to say to you. I am a smash the keyboard kind of responder to Claude. I have never been more direct, meaner. I'm never more frustrated. I don't admonish Claude and say, you're stupid. Yeah. I say, I've told you this.

**Speaker 4** [00:39:32] Yep.

**Speaker 3** [00:39:33] A million times. What's going on? I'm not like sweet and nice. I've heard people say, "Be really lovely in case the AI overlords one day take over you and your life." I am just winging it, and whatever happens is

**Speaker 4** [00:39:49] I have.

**Speaker 3** [00:39:49] gonna happen.

**Speaker 4** [00:39:51] So we, you might be, you might be, or you're gonna be around our 100th episode. So like, we're coming on 100 episodes of How I AI, and I used to be like, "Oh, gentle parent your AI." Like, I used to be like, "I know you can do it, sweet little, sweet baby Sonnet, like, I know you can do it. And now I am like, why are you the way you are? This is garbage. This is trash. And I think why I've gotten so mean is like, I know you're- it's like wasted potential. I'm like, I know you're smart. I know you're capable, and yet you show up to me with this C plus work. What is-

**Speaker 3** [00:40:29] You are wasting my time.

**Claire Vo** [00:40:31] Wasting my time.

**Speaker 3** [00:40:32] That's not how we're meant to work. Well, let's see, I really admonished my Claude this morning. It was, I told it while we're talking, I want to make you a proposal as if we were going to work together. So let's see what it did. We're going to go into Netlify and see if it-

**Speaker 4** [00:40:47] If it did a good job.

**Speaker 3** [00:40:48] If it did its work. This should look like ChatPRD, and this should actually be interactive, so let's see what it's done.

**Speaker 4** [00:40:57] We can admonish it together.

**Speaker 3** [00:40:59] Here it is.

**Claire Vo** [00:41:01] Okay.

**Speaker 4** [00:41:02] That is, that's our font. That's our font.

**Speaker 3** [00:41:04] You know, it could be worse.

**Claire Vo** [00:41:06] Let's see.

**Speaker 3** [00:41:06] It could be worse. Let's see how much, let's see how much. Wow, made you some custom homework.

**Speaker 4** [00:41:14] I love it.

**Speaker 3** [00:41:14] Claire, it's going to charge you 0 dollars.

**Claire Vo** [00:41:16] Oh.

**Speaker 3** [00:41:17] That's how much

**Speaker 4** [00:41:17] Best price. Best.

**Claire Vo** [00:41:20] You know what? Claude, you get, you get, you get a bonus.

**Speaker 3** [00:41:25] And it's gonna give you some homework. Okay, my Claude wants you to be documenting your progress, building that muscle memory, defaulting to Claude, documenting your wins.

**Speaker 4** [00:41:34] Oh, I do like, I do use an orange rose purple button, so it got, it got most of it right.

**Claire Vo** [00:41:39] I love that guy. I love that guy.

**Speaker 3** [00:41:42] Okay, well, it did its best for you.

**Speaker 4** [00:41:44] Okay, future Claude overlords, be kind to us.

**Speaker 3** [00:41:48] Thank you.

**Speaker 4** [00:41:48] We did not know better. We just didn't know.

**Speaker 3** [00:41:51] No. We are simple mere humans trying to understand this, the powers of Fable.

**Speaker 4** [00:41:57] That's exactly right. This has been so, so fun, Grace. Thank you for showing us all these use cases. I think, like, very applicable, very inspirational, very, like, practical, which is what we love to see here on How I AI. Where can we find you, and how can we be helpful?

**Speaker 3** [00:42:12] I am Grace Clark everywhere on the internet. Have been online for decades, so Grace Clark on Twitter, Grace G Clark on Instagram, Grace Clark on Substack, and be helpful by telling people that anything is possible, and they start with one sentence as a prompt. Put that out into the world, and my job will be easier.

**Speaker 4** [00:42:34] Amazing. I love it. Thank you for joining How I AI.

**Speaker 3** [00:42:38] Thanks for having me.

**Claire Vo** [00:42:40] Thanks so much for watching. If you enjoyed the show, please like and subscribe here on YouTube, or even better, leave us a comment with your thoughts. You can also find this podcast on Apple Podcasts, Spotify, or your favorite podcast app. Please consider leaving us a rating and review, which will help others find the show. You can see all our episodes and learn more about the show at howiaipod.com. See you next time.
