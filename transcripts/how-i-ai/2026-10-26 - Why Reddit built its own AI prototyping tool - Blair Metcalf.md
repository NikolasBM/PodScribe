---
podcast: "how-i-ai"
podcast_title: "How I AI"
title: "Why Reddit built its own AI prototyping tool | Blair Metcalf"
date: 2026-10-26
url: "https://podcasters.spotify.com/pod/show/pen-name/episodes/Why-Reddit-built-its-own-AI-prototyping-tool--Blair-Metcalf-e3qtst2"
guid: "f0c0c734-92f3-4b9b-b2b1-b107d50a63a0"
host: "Claire Vo"
guests: ["Blair Metcalf"]
format: "interview"
level: 2
length: "00:29:14"
categories: ["coding", "design", "agents"]
featured: ["Figma", "MCP", "agent harness", "Cursor"]
mentioned: ["Slack", "Gemini"]
transcript_source: "azure-asr"
transcribed_by: "MAI-Transcribe-2"
---

# Why Reddit built its own AI prototyping tool | Blair Metcalf

**Blair Metcalf** [00:00:00] The distance between design and product is wide, and if we made everyone a builder, they could vibe code new features and products easily. And so we made a harness that uses our design system and all of our components, UX patterns, and it keeps all the designers and product managers on rails. And so this way that you can make a million ideas, they can be reviewed, and then you can pick one, and then that's where we spend our time, and that's what goes into prod.

**Claire Vo** [00:00:25] I have not heard anybody say, okay, go ahead and let you off into your production data and render that.

**Blair Metcalf** [00:00:31] And the reason why that we do this is because Reddit has personalized data, but if designers are mocking everything in Figma, and then they show that to leadership, leadership's going to look at that and be like, this isn't relevant to me, and you don't have to take 9 months to get that into prod, see if that works. It saves so much time, and everybody can work on other things. So if you make one of these real world prototypes with real data, they'll put it through the paces of like some new feature. Search is like a, is a great example to like How I AI, and it knew podcast, like it's pulling that real data, it sends it to an LLM, ranks it, and then you can test out that design.

**Claire Vo** [00:01:08] Are designers prototyping the most? Are product managers prototyping the most? Like who is prototyping the most? Welcome back to How I AI. I'm Claire Vo, product leader and AI obsessive, here on a mission to help you build better with these new tools. Today I have Blair Metcalf, principal UX engineer at Reddit, and he's going to show us Reddit Proto, their custom harness for product managers, designers, and anyone else to get their ideas into a production-like prototype they can share with anybody in the company. This is an awesome one for anybody interested in design systems, prototyping, and how to make high quality things without exposing GitHub. Let's get to it.

[00:02:18] Blair, welcome to How I AI. Thanks for joining.

**Blair Metcalf** [00:02:35] Thanks. I'm glad to be here.

**Claire Vo** [00:02:36] Well, one of the reasons why I was so excited to have you on the show is I feel like the best teams, their answer to what are we, how are we going to use prototyping in our product design engineering flow is eventually they decide, you know, we're just going to build our own, our own rig here. We're going to build our own prototyping harness, and it's going to give us exactly what we need for exactly how our team operates. And the folks that do that, and it is not impossible to do, unlock some magic in the team. So walk me through what this is and why you built it.

**Blair Metcalf** [00:03:07] We wanted to innovate, go faster, and get new features into users' hands. And so we made a harness that uses our design system and all of our components, UX patterns, and it keeps all the designers and product managers on rails. And so this way that you can make a million ideas, they can be reviewed, and then you can pick one, and then that's where we spend our time, and that's what goes into prod.

**Claire Vo** [00:03:31] So what I'm looking at right now is a little render of the mobile app or the mobile site for Reddit. So tell me how would somebody come to this inside your team and actually design something? What do you think is unique? I mean, it has the design system, but what else, why did you build this, and what is super unique about how you approached the harness that you built?

**Blair Metcalf** [00:03:52] When we started working with designers, we wanted to start obfuscating all of Git, what the file structure is. And so we actually made an app on your desktop that just gets you right into a new project. And you would load the boilerplate and name it, and then you would end up here in a vibe coded environment. You can work in any IDE you like, and it sets up like what the app, a starting point. And we think of that app as like, this is the whole world, and as people add new features, it's kind of like a mountain, and we absorb that mountain, and it's everyone's starting point.

**Claire Vo** [00:04:29] So, one, if I'm a designer or product manager, I don't have to think about like, am I cloning the repo? Am I on a branch? Am I running locally? You've created a little custom app that says just start a project, happy, happy. you name that project, and then you all do the hard work of like a baseline scaffold. And then does that scaffold put the app in a specific state? Like, what are the kind of convenience things that you get when you land with this scaffold as a designer or product manager?

**Blair Metcalf** [00:04:59] That's right. Yeah. So I just showed like how you create a new project. It's cloning the Git. You don't need to know any of that. We'll go back to that screen, and you'll just start coding. And the things that you get right out of the bat are examples of, like, features. And this is what every product development team does. They're going to add new features to the product in their explorations. There's other doodads under here of, like, navigation. you can change the navigation, you can prevent navigation because some stakeholders click too much, and you don't want them to click. We have

**Claire Vo** [00:05:36] I love this.

**Blair Metcalf** [00:05:36] like- yeah, and then so everything is controllable. You can change the device, the theme, and so you can switch to dark, and you can test out every state that you can get in, even like who is a moderator. And so Reddit has complex user ecosystem, and then the nice, the nicest doodad here is that you can then use signed in data, and so you'll know if your design works. And this helps with all kinds of real-time data feeds. So like if you wanted to do search, you can actually do search right here. And before we started this, I was just playing around, and I was wondering, could I add search with these annotations? And surprisingly, I was able to. I commented here, make relevant type-aheads, trending recent communities, et cetera. And then down here, I said, overall direction, using the signed-in Reddit data and real type-aheads as user types in the search box.

[00:06:38] And then I sent that to Cursor, and it vibe coded it on the spot. And this was just playing around. I was stunned, it worked.

**Claire Vo** [00:06:46] Okay, so I just want to kind of like walk this through for folks that are listening or maybe missed some of this. So first of all, you have like features as configuration, basically like the ability to toggle on or off features inside this constrained prototype.

**Blair Metcalf** [00:07:01] Mm-hmm.

**Claire Vo** [00:07:02] You have the ability to configure the prototype itself in terms of like turning off the interactivity of features like navigation. I love this because if it is a fully like featured sort of prototype, you can kind of go anywhere with it.

**Blair Metcalf** [00:07:14] Mhm.

**Claire Vo** [00:07:14] But this is letting a product manager designer sort of constrain and say like, this is the piece that I want you to pay attention to. you can obviously switch between devices, but you can also switch between persona views, which I thought was very interesting. And then I want to make sure people did not miss that this. One of the things that it looks like you do, and correct me if I'm wrong, is you scaffold it with mocked data, but then you can log in with your account and render production data in the prototype as well. And so this is not a tactic that I've heard people use before, which I think is really, really clever. I've heard a lot about mocked data. We have a great episode about using JSON as the backing for your prototypes and updating the JSON instead of updating kind of like hard-coded data in your prototype, but I have not heard anybody say, okay, go ahead and let you auth into your production data and render that, which gives you a much more flexible set of data to work with when you're testing new features.

**Blair Metcalf** [00:08:17] Right, yeah, it's a clever trick. Our team is like a bunch of magicians.

**Claire Vo** [00:08:22] Mhm.

**Blair Metcalf** [00:08:22] And the reason why that we do this is because, Reddit has personalized data, but if designers are mocking everything in Figma, and then they show that to leadership, leadership's going to look at that and be like, why? This isn't relevant to me.

**Claire Vo** [00:08:34] Mhm.

**Blair Metcalf** [00:08:35] So if you make one of these real world prototypes with real data, they'll put it through the paces of like some new feature. Search is like a, is a great example because they're going to want the search results. I think I already did it. I said like, how I AI, and it knew podcast, like, it's pulling that real data, it sends it to an LLM, ranks it, and then you can test out that design. This design, I didn't spend any time on it, but a designer could then populate the landing, the type-aheads, and the results, and you don't have to take 9 months to get that into prod, see if that works. It saves so much time, and everybody can work on other things.

**Claire Vo** [00:09:15] And then to make modifications to it, just because I'm kind of inferring based on what you showed us, you have sort of like a prompt-based thing, but that's ultimately just kicking prompts over to Cursor, is that right?

**Blair Metcalf** [00:09:28] That's right, yeah. So the way that this kicked off was, it's a surprising workflow, but once I showed these annotate, once I wrote the annotations, I just said send a Cursor, and it writes a file, and then I just tell Cursor, apply annotations, and it takes the location in the code, the annotation, and the overall to kick it off. And you can, with that specificity, you can target any surface, any composite, any component, and add real data to it with very little training.

**Claire Vo** [00:10:01] Got it. So if I click something in this prototype and write an annotation on it, the prototype has already been enriched with this is like roughly where the code is, this is roughly what this component is, this is what the request is from the user, and so it's like a very targeted edit request in this repo. Is this the real repo, or is this like an approximate repo that's just for prototypes?

**Blair Metcalf** [00:10:27] So, yeah, everything that you asked, I can go into the annotations, I can clear these, and I can say, make this Italics. And so you can target very specific things. It'll use all of our design system tokens, components, et cetera. And then this is the real thing, that launchpad that I showed earlier, it deploys it on our infra. And so it basic- it uses Kubernetes. It's basically like an internal Vercel. And so then you don't have to worry about any deployment, and you can share it. You can share it internally, it'll copy the URL, or you can share it externally, and you can like scan that. You go through some security, and then now it's on your phone, and so then that is a PWA, and these are apps that I've already installed, and you can click around them as if you were on desktop, and you can check.

**Claire Vo** [00:11:19] Got it. So that's the way that you, I was curious, so how do you share these prototypes internally? Are you just able to give links to people or QR codes, and then they can pull up and play with your prototype? Is that how it works?

**Blair Metcalf** [00:11:30] This is a piece that we're working on right now, and it's going into great places. Internally, you can share this URL quickly, like on Slack. And we have a dashboard that just keeps everyone's prototypes. Right now, there's about 700. The problem with this is it doesn't scale. That list doesn't scale. So what we're working on now is a very searchable console. So you can find people's prototypes, what areas they work in, people, tags, if that feature was like labeled, search or growth. And then you can go into prototype types. We're going to go into iOS, Android, and then you can also go through your prototypes, and so what teams you work on. This would be the way that everybody can discover quickly who's working on what, like gives visibility to leadership.

**Claire Vo** [00:12:20] And are all of these prototypes public? Are prototypes public by default or private by default? I'm just curious.

**Blair Metcalf** [00:12:25] Right, yeah, so internally they're all public, but then like-

**Claire Vo** [00:12:28] That's amazing.

**Blair Metcalf** [00:12:29] Yeah. We need to add that. We should add some so you can work under the skunkworks.

**Claire Vo** [00:12:34] Yeah, under the radar. I don't know, I kind of like this idea of like everything's public, you can kind of see what people are messing around with. I'm curious, who is prototyping the most? Like, are designers prototyping the most? Are product managers prototyping the most? Like, who is prototyping the most?

**Blair Metcalf** [00:12:52] Yeah, so it's a mix of designers and product. We have 100% adoption in UX and product, but there are like some surprising folks that show up, like a visual designer turned out to be one of our best prototypers. An animator turned out to be one of our best prototypers. And what it seems like is these people are like great directors, they have huge context, they can describe all of the things, they are vulnerable, and they try things without like worry of failing. but yeah, it's a mix. It's almost a perfect mix over design and product, over 150 people.

**Claire Vo** [00:13:30] I can imagine how this changes how ideas are generated, and I see a lot of teams moving to this more like prototype style requirements for designs. What I'm curious is, how has this changed how designs are reviewed? Like, how do you give feedback?

[00:14:31] How do people make iterations? How do they collaborate?

**Blair Metcalf** [00:14:34] Right, yeah, and so this is a part that we're working on also, but long story short, these go into like leadership reviews. Leadership uses them, clicks through them, and you're getting feedback live, you're getting feedback in Slack, but we want to add, you can comment live on the prototype, and so you have those annotations. Those annotations can be kicked off, they could be comments, they could kick off another build.

**Claire Vo** [00:14:58] Mm-hmm.

**Blair Metcalf** [00:14:59] If a leader just wants to say, like, make this change, it could be live momentarily. but then, you know, like that console, it also has a place for commenting. These are all things that are coming.

**Claire Vo** [00:15:12] Got it. And so do you feel like this has cha- what has this changed in terms of, you know, is it velocity, is it quality, like craft? Where do you feel like the impact to how you build products has been felt the most?

**Blair Metcalf** [00:15:27] It's instant alignment. And so if you use systems with high craft, all the velocity, like, comes because you have, alignment with leadership using real data, reviewing real design system components that nobody's hanging up on, like, a gotcha, and they don't rat hole on a detail, and they can quickly approve it. That goes out to everyone. Nobody, everybody knows, like, the North Star that they're heading towards, but it's instant alignment.

**Claire Vo** [00:15:53] And then how does this get handed off to engineering?

**Blair Metcalf** [00:15:57] Right, yeah, this is the big puzzle piece here, which is that, can you take this code and send it to prod? So here I've sketched out a fake feature. It's just like saving posts to folders. And so would there be a way that we could select a component and then copy the example prompt and take this into prod? So under this launchpad, we can also start a new project where we make a feature capsule. So what you do is you copy the location in Figma, you go over to Figma MCP, you create from Figma, and it's going to make this thing that we call a feature capsule. And what it does is it takes a lot of things. It uses Figma MCP, it goes through all of the design system, maps it to what we know is in prod.

[00:16:59] It has also incorporated, you know, CI review feedback and engineer feedback into this MCP. And then now it's analyzing all of those Figma frames, components, and it'll spit out a PRD. And so I'm going to say, yes, this is what you're looking at, and I'll continue, and then it'll generate this PRD. These can get really large. This, we just selected a specific frame, but you could do many surfaces. We've tried the kitchen sink, but we kind of back, we're going back to just like high fidelity UI. And so here you've got your generated PRD, and it'll say like, this is what the user goal is, this is the acceptance criteria. It'll get into details here, links to the Figma, and then once it's done, I'll accept and continue, and you save this file locally, and then we'll send that to Cursor.

**Claire Vo** [00:17:53] Can you explain, go a little deeper. If somebody wanted to build this themselves, is this a lot of this you built yourself, or like, how did you get here? Because this is really interesting. It's going from a Figma link, um, and frame link all the way through PRD, and then something that your Cursor can execute. So just like, walk us through how it got built.

**Blair Metcalf** [00:18:12] Right. So we started with the Reddit proto design system.

**Claire Vo** [00:18:18] Mm-hmm.

**Blair Metcalf** [00:18:19] And so we have all of the colors and typography baked into our design system, and then we read prod and we mapped the two. so here you have all of the button sizes, and so we use Code Connect, and we know that those are everything is connected. This is kind of the whiz bang moment where like you're like, what am I looking at?

**Claire Vo** [00:18:42] Yeah, exactly.

**Blair Metcalf** [00:18:43] This right here is every single token, component, surface, journey that we know of across RPL, Reddit Product Language. And so here, this one token is mapped into Figma, into iOS in the GitHub, and into the prototyping GitHub. And here it has picked out that there may be a difference in the actual literal values and the token on some platforms. And so what we then take that and we map it to prod code. We submit PRs that do and don't get through CI reviews, and like we take all of the engineer feedback, and that iterates back. So basically, you start with a map, and then you try, fail, iterate, and you refine the MCP through feedback.

**Claire Vo** [00:19:36] Got it. And this is an MCP that you've built?

**Blair Metcalf** [00:19:39] Mhm. Well, the team, working with the team.

**Claire Vo** [00:19:42] Okay. I meant you, the collective, the collective you. And what are some of the tools in that MCP? Is it like, where's the component? What's the design token?

**Blair Metcalf** [00:19:51] That's right. Yeah, so right here we got it hooked up, this Proto MCP Ultra, and it's basically like looking for what are you feeding it, and then it's finding tokens, components, and examples to write that prod-shaped code. This is what the code ends up looking like. I can't show the code, but like,

**Claire Vo** [00:20:13] Yeah, of course.

**Blair Metcalf** [00:20:13] Just proof in the pudding, like it goes through all the Git reviews,

**Claire Vo** [00:20:18] Yeah.

**Blair Metcalf** [00:20:19] and makes a build for you to test out on your device.

**Claire Vo** [00:20:24] Okay, so I want to make sure that people don't miss this process, which is you all have built an MCP basically to translate any input, and in this instance, that input might be like a Figma frame, into discovering the correct tokens, design system components, code snippets, whatever, based in production, so that when you're generating prototype style code, it is as close to production as you can reasonably get because it's done this traversal kind of like through this MCP.

**Blair Metcalf** [00:20:57] Yeah, that's right. Yeah. So in this example, we're going from Figma to prod. We have tried out going from prototypes to prod, but we think that this is like a very like accurate way of getting like high fidelity Figma, high fidelity architecture. but yeah, it's doing that through a map.

**Claire Vo** [00:21:14] You know I'm a PRD girl. Do you feel like the PRD makes a difference?

**Blair Metcalf** [00:21:18] Yeah, it's, it actually carries a lot of weight. And so when we started talking, the reason why we added this is because that was the handoff

**Claire Vo** [00:21:24] Mhm.

**Blair Metcalf** [00:21:24] with engineering. And so then you clearly define your scope, all of the user goals and, you know, workflows. Yeah, it's, it is, it is the perfect handoff. It has all the context.

**Claire Vo** [00:21:35] I mean, you heard it here, folks. The PRD is the perfect handoff. Keep making them. I really, I really love this. I mean, I think what folks should take away from this is not just can you build your own prototyping system and can you make it form fit to how your team likes to build things. You can hide away some of the complexity of vibe coding and prototyping from your less technical friends, while still running it in something like Cursor in the background. And then the idea of building sort of convenience method, design system based MCPs is a really clever one, because a lot of times you're just leaving these LLMs to kind of flail about in the code and find what they think they can find.

**Blair Metcalf** [00:22:20] Yeah, that that's exactly it. Like, you know, folks say that bots hallucinate. They hallucinate writing code. And our opinion has always been like, well, what what's your goal? What's the context? And you look at the design system, you look at the end state shape, and then we refine from there. But, yeah, this is the MCP using that feature capsule and asking me where it should write the code.

**Claire Vo** [00:22:49] Mhm. Amazing. And it could write that code basically in the app or in a prototype or whatever you might want.

**Blair Metcalf** [00:22:56] It's right now, it's writing it in a sibling repo, to keep prod clean, and then it'll iterate, and then it'll send off a draft PR, and then, yeah, and then that'll get reviewed and may or may not go through.

**Claire Vo** [00:23:10] May or may not. And then can you go back to the Rosetta Stone, because I don't want people to miss this amazing thing that you had, which is you have this like nice visualization of what's going on in our design system.

**Blair Metcalf** [00:23:21] Right.

**Claire Vo** [00:23:21] Basically, why did you all decide to build this?

**Blair Metcalf** [00:23:27] Well, so the theory was, how do we get the design system into a harness, and then the harness goes into an MCP? And we had made several attempts, and the number one thing was, well, I don't know if what's in there. And so I was like, well, this is a visual verification, and if I can hunt down and see that I know that a avatar has these colors and is used in these surfaces and is a part of these workflows, I can visually verify, ah, well, I know that the harness and therefore the MCP has all of the parts.

**Claire Vo** [00:24:06] So it's just like kind of, and is this how your brain works? Because you're like, oh, I can easily visualize. And I'm like, you can visualize what, man? It's like a bunch of fuzzy auras over here. So tell me, like, is this just, is this what is inside Blair's brain?

**Blair Metcalf** [00:24:20] This is, well, yeah, collectively, this was what it was in the team's brain, but this was like, you know, I was trying to explain this to people,

**Claire Vo** [00:24:27] Mm.

**Blair Metcalf** [00:24:27] like, you need a single source of truth that's upstream from everything.

**Claire Vo** [00:24:31] Mm.

**Blair Metcalf** [00:24:32] you know, and then when I would show this, people were like, I know it's in there. It was a visual verification for the team. Yeah.

**Claire Vo** [00:24:39] I love it, and it's very beautiful. It's very soothing. It needs a little, it needs a little music, though.

**Blair Metcalf** [00:24:46] What would you play?

**Claire Vo** [00:24:47] I don't know, some sound bathy kind of stuff.

**Blair Metcalf** [00:24:51] Oh, there you go. Yeah, some Brian Eno.

**Claire Vo** [00:24:53] Exactly, exactly. I love this. I just want to recap for everybody. Okay, so we saw Reddit Proto, purpose-built prototyping tool for product managers, designers, public by default, anybody can open these deployed sort of in your cloud, some controls via config, connection to Cursor, and then a really thoughtful, audited, and contextualized design system that's accessible to this whole harness via a custom MCP.

**Blair Metcalf** [00:25:26] Nailed it. Yeah, that is what we do.

**Claire Vo** [00:25:27] No big deal. No big deal. Easy peasy. Um, this is really- I just- my head is spinning. I'm gonna swirl on, like, how much of this I think I can build because I think it would really change how I think about some of my, um, design system problems. As I noodle on this, let's go to some lightning round questions,

**Blair Metcalf** [00:25:49] Mhm.

**Claire Vo** [00:25:49] um, if you're ready. One is just what are some non-work, non-prototyping, yeah, maybe not non-work, but like what are some non-prototyping use cases that you're really loving AI for these days?

**Blair Metcalf** [00:26:02] Before this podcast, I was working on, I was working on making playing cards for the whole team. And so this is like, this is, this is the person who helped start the whole Reddit proto project. And so we're making a play, like a players, all the players on the team, and then you have like all their stats on the back. And what's nice about this is like you have to like direct this and get it into like brand and yeah, and then everybody will have it in their hand.

**Claire Vo** [00:26:36] I know, it's so fun to be able to make like creative physical goods that are high quality. I mean, again, and these are like very high quality, super cute, in consistent. What did you use to generate these? Like, how did, what was the process?

**Blair Metcalf** [00:26:51] Yeah, so I bounced around a bunch of places, but with my bots, I described everyone, and I kind of just like ad-libbed. This is their like, you know, this is their persona. And then I actually took that to, I took that to Gemini. Gemini could have performed better, but like ChatGPT ended up making the illustration that was perfect. I took that into Cursor and generated on a high model, and then that used like a markdown file to use the prompt that kept them all in the same aesthetic. Yeah, it was quite a workflow.

**Claire Vo** [00:27:25] Oh, I love it. Super, super genius. I mean, a hidden How I AI at the very, very end of this episode. Okay, my last question to ask everybody this. When your MCP is not replying, when Claude is being obstinate, well, you know, whoever it is, when AI is not listening, what is your prompting strategy? How do you get it back on track?

**Blair Metcalf** [00:27:47] So I don't yell at them. I know some folks do, but what I do is I take a day and then I get more vague, and we all have like bots with like projects and context, and I pop out of a project and I describe the thing large,

**Claire Vo** [00:28:02] Yeah.

**Blair Metcalf** [00:28:02] like a movie director. And so here are all the facts, and then here's all the intents. And then I pull that back into the project, and then it knows enough to apply it to what our goals are. But essentially, I become a better director that is more vague, not specific.

**Claire Vo** [00:28:20] I like that. I do tell a lot of people just like under-prompt your AI. It's a lot more effective than over-prompting. that's a good one. That's one we haven't heard yet. Well, Blair, this has been really interesting, very, very dense, and I think a lot of great ideas for teams out there looking to think about how they can improve their own prototyping harness, why they might build their own, and even just designers and product managers out there that want to get better at using design systems to build production-like code.

**Blair Metcalf** [00:28:49] Awesome. Yeah, thanks for having me. We're really excited to get these features into users' hands.

**Claire Vo** [00:28:55] Awesome. Well, where can we find you and how can we be helpful to you?

**Blair Metcalf** [00:28:58] I'm on LinkedIn, and when I'm not on LinkedIn, I'm touching grass. If you want to work at Reddit, feel free to reach out to me on LinkedIn if you got any puzzles like this. I'm also really friendly. I love helping folks.

**Claire Vo** [00:29:10] Amazing. Well, thanks for joining How I AI.

**Blair Metcalf** [00:29:13] Thanks.

**Claire Vo** [00:29:14] Thanks so much for watching. If you enjoyed the show, please like and subscribe here on YouTube, or even better, leave us a comment with your thoughts. You can also find this podcast on Apple Podcasts, Spotify, or your favorite podcast app. Please consider leaving us a rating and review, which will help others find the show. You can see all our episodes and learn more about the show at howiaipod.com. See you next time.
