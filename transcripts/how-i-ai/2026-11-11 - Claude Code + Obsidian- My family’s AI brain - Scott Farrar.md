---
podcast: "how-i-ai"
podcast_title: "How I AI"
title: "Claude Code + Obsidian: My family’s AI brain | Scott Farrar"
date: 2026-11-11
url: "https://podcasters.spotify.com/pod/show/pen-name/episodes/Claude-Code--Obsidian-My-familys-AI-brain--Scott-Farrar-e3s3sgr"
guid: "cd46c212-7b4e-4102-aa94-d5c13bd6b9f1"
host: "Claire Vo"
guests: ["Scott Farrar"]
format: "interview"
level: 1
length: "00:33:46"
categories: ["agents", "consumer"]
featured: ["Claude", "Claude Code"]
mentioned: ["Meta Muse", "ChatGPT", "OpenAI Codex", "Grok Bot", "Instinct"]
transcript_source: "azure-asr"
transcribed_by: "MAI-Transcribe-2"
---

# Claude Code + Obsidian: My family’s AI brain | Scott Farrar

**Claire Vo** [00:00:00] When you're using like the web, ChatGPT or Claude, you're like, what does it really know about me? What does it really remember? What information does it have? Like, that is very opaque to most people.

**Scott Farrar** [00:00:12] I wanted to build a system where I was confident that AI was grounded in my truth. So in Claude Code, I built this system that would read and write markdown files so they would have the memory of what we were talking about. I have all the appliances in my house and all their serial numbers. I might go start a new chat here and say, what's going on with the fridge? And it knows the warranty information because I put that in there at some other time.

**Claire Vo** [00:00:39] I'm going to drop it to Claude. What do I need to be thinking about in this house?

**Scott Farrar** [00:00:44] Let's actually go to Claude here and say like, hey, do I need to plan for earthquakes?

**Claire Vo** [00:00:52] Welcome to How I AI. I'm Claire Vo, product leader and AI obsessive, here on a mission to help you build better with these new tools. We have talked about Claude for work. We have talked about Claude for coding. We have talked about Claude for kids, but we have not talked about Claude for the homeowner. If you are adulting hard, then this is the episode for you. We talked to Scott Farrar, who has a obsidian vault of everything in his house and a set of Claude skills that keeps his dry route under control and his insurance quotes as cheap as they can be. Let's get to it.

[00:01:52] Scott, welcome to How I AI parent, busy parent, busy dad, busy household manager edition.

**Scott Farrar** [00:02:53] Busy, busy adulting.

**Claire Vo** [00:02:55] Busy adulting. We have so much, so many questions. Everybody always asks, like, we need more parents on, we need more people handling their busy lives. And so when I saw some of the stuff that you were doing, I was so excited for you to demo it for us. So walk us through what your busy adulting looks like and what problem you are trying to solve.

**Scott Farrar** [00:03:14] I have kids, I've got a career, and it's, like, hard to juggle everything. And if I come up with a question like, oh, should I- do I have the right car insurance? Do I need to change that? You know, lots, like lots of people, I might come to AI, I might go to the chat and have it help me out. But the problem I was having there is if I start doing a complex problem with chat, it's like, well, do I dump my information in there? Do I give it all the context into this chat here? and as the conversation goes, is it drifting? What is it really remembering about me? And so I wanted to build a system where I was confident that AI was grounded in my truth and knowing what it knows about me, so that I could be confident in what advice it was giving me back. So what I did, instead of just going with the chat interface, switching over to a coding agent, so in Claude Code, I built this system that would read and write files, read and write markdown files, so they would have the memory of what we were talking about, and it would be living on my computer so that if I come back later and start a new chat session, a Claude Code session, it can reference those same files.

[00:04:29] So if I, here's kind of a sample of the car insurance question in progress where I'm like, oh, I've been working on this. Has that third quote come in? Like we were getting quotes from people like, oh, it's summarized, it has some quotes here and here. It's like, oh, well, should I update that car insurance? What gaps do I have in the coverage? So it's read the documents that I put in the file folder. This has been a huge unlock of like both my confidence and what it knows about me, but also just when it can build me like a checklist of what to do, then it keeps me moving forward.

**Claire Vo** [00:05:03] So the problem that you're trying to solve here really is when you're using, like, the web, you know, ChatGPT or Claude, you're like, "What does it really know about me? What does it really remember? What information does it have?" Like, that is very opaque to most people, but once you download these desktop apps, whether it's Claude Code, Claude Cowork, ChatGPT, ChatGPT Codex, whatever you're working with, they can write, it can write to your desktop or to your desktop, to your computer. And what you're saying is, then you just tell it to use Markdown files as kind of like your very transparent source of truth, source of knowledge, that any question about your household can answer. And then you're using that, if you just show us the kind of like Claude session, you're using that to do things like update your insurance, like check, are you up to date on your insurance, what do you need, and get quotes.

[00:06:04] Can you walk us through just that, like, experience of getting car insurance and quotes and what did well with,

**Scott Farrar** [00:06:11] Yeah.

**Claire Vo** [00:06:11] you know, using that through code versus what kind of failed?

**Scott Farrar** [00:06:14] What I started with was, um, just saying, well, should I update this? And in the conversation around updating another insurance, it says, well, one of these people giving you a quote said you need to update the cars, and if you also wanted this other policy, in the previous years, I might have been like, wow, this is a headache, I might come back to this. But I might say, like, well, what should I do next on this project. And because I, it's a very loose question, but because I'm grounded on what I'm working on here, it comes back with a response that says, oh, your next step is email Dana Whitfield. This is a fake person. But that's the blocker and say, like, you should email, ask this question of like, you know, what is it that I really need here? And these are the questions that you need to have answered before you can make an informed decision on car insurance.

**Claire Vo** [00:07:13] And, I mean, how would you have done this before? Because I'll tell you exactly how I would have done it before. I wouldn't have done it.

**Scott Farrar** [00:07:19] Yeah. I think what I would have done is actually it requires maybe a lot more trust in your insurance agent.

**Claire Vo** [00:07:26] Mhm.

**Scott Farrar** [00:07:27] Not that I don't necessarily trust them, but it meant that, like, I wouldn't have read those documents in detail. Um, and so what the power of AI, you can read it via the AIs, and then I wanted to bring in my own home context and have that system mesh with what the insurance agent was giving me. And then I was able to ask way more detailed questions and email back and forth with the insurance agent and know exactly what I was asking and know exactly what they were telling me.

**Claire Vo** [00:07:57] Okay, so you know, for you, the secret sauce is context, and we've seen a couple of these. I see that you have Obsidian. We've seen a bunch of these, like, personal brains. What I loved about your personal brain is you're a lot more comprehensive in the type of household information you put in that personal brain. So, like, what are you putting into your Obsidian? What do you think goes into that context that you think lets you do more stuff within the household, um,

**Scott Farrar** [00:08:28] Yeah.

**Claire Vo** [00:08:28] than other folks?

**Scott Farrar** [00:08:31] Yeah, so actually, let's start just a picture of the insurance project itself.

**Claire Vo** [00:08:35] Mm.

**Scott Farrar** [00:08:35] This is a markdown file. This is like the picture of the memory that Claude was working with. Uh, it go- it's going constantly referencing back what it knows here, and it will update information as it goes, and there's the checklist of like, "Oh yeah, that is the blocking step I needed to email the Dana person. But it also is going to, at a wider view, like what, this is one of the project files in here, but if I go over to Obsidian and see the graph view of all the context that I put into Claude or all the context that Claude can reference, I have kind of all the appliances in my house and all their serial numbers, or like here's a picture, a fake picture of the range, for the serial number of the refrigerator and like, oh, when is the, when is my kid's iPad gonna lose iOS support, software updates? And so I might just put that information in like, they're on OS such and such, or it's this model from 2019 or something.

[00:09:38] So actually, when I set this system up, I said to Claude, like, what information should I gather about my house? I asked it, and I said, you know, perhaps what about, like, the refrigerator? And said, well, actually, you go around and take pictures of every appliance in your house. And so that's actually what all these yellow files are, the pictures. They are summed up on this appliances list, another markdown file, and Claude is kind of enforcing the rules of how it's organized. And while I can inspect the memory here in the markdown file itself, I often am actually just using Claude itself. I might go start a new chat here and say, what's going on with the fridge? And it's going to go read the database, look for exactly what am I talking about with the fridge? And maybe I'll say like, because the ice maker is broken, so.

**Claire Vo** [00:10:33] Wait, hold on. I have to pause because

**Scott Farrar** [00:10:36] Yeah.

**Claire Vo** [00:10:36] are all houses the same? Because do you know what the number one problem in my house right now is? My broken ice machine in my refrigerator. I am, like, not even kidding. We have a Grok bot that is, like, dealing with our refrigerator repair people.

**Scott Farrar** [00:10:56] Yeah.

**Claire Vo** [00:10:56] Young- young people, just g- this episode is not for you. This episode is for people

**Scott Farrar** [00:11:01] Uh-huh. This is-

**Claire Vo** [00:11:02] who need their- not one of those fancy little nugget ice makers that you put on the- on the countertop on TikTok. We're talking a good old stainless steel refrigerator ice maker, always broken.

**Scott Farrar** [00:11:15] Yeah. Yeah, um- ...so, yeah, when you have that problem, you're using Grok, but actually it's- it'll be interesting. We can c- talk about the contrast with- with bots and- and dots and Muse and Instinct and those types of things too. Um, but here what I will do is, like, I'm not- I might go into the appliances and look at that list and that markdown file itself. I could if I wanted to, I see all the memory there, but really I'm going to Claude Code often and just starting a new chat and saying, like, ah, what do I do? It's very loose. And I'm like, make, help me make a plan. And so it might come back and say, ah, well, you know what? Oh, bad news. It's going to cost you, the warranty is going to run out in 2027. It knows the warranty information because I put that in there at some other time. so that's been super powerful. You know, actually, a lot of this is influenced by my dad because in a pre-AI era, my dad and his file cabinet are actually just like AI, 'cause he'll have all the receipts and all the warranty information, and he sells that- I can still ask him, like, "Hey, how did you do this when you were solving this?" And he's like, "Oh yeah, I have this file from 1978.

[00:12:27] let's see, yeah, the fridge then did such and such." So every time I ask Claude this, I'm like, "Ah, this is just- this is just what my dad did, naturally.

**Claire Vo** [00:12:38] I- I have this kind of, like, hypothesis that there are 2 types in the world. There are, like, Notion boys and not Notion boys, and, like, you- you don't even have to use Notion to be a Notion boy, but, like, you have to have that, like, thing in you that's like, "I'm gonna file this stuff, I'm gonna organize it, I'm gonna tag it." I am not. I'm the opposite. I am a type B large language model. You just dump in unstructured context and you're gonna get the next token out. But I do think it's funny when you see people's kind of like mental model of the world go into how they design their AI systems. Everything from like hyper organized obsidian nodes and structure to, like, I don't know, I have a video of my refrigerator somewhere in iPhotos, go find it and then tell me what's going on with it.

**Scott Farrar** [00:13:34] Well, I think that's actually the- what I really like is the loose kind of

**Claire Vo** [00:13:39] Mhm.

**Scott Farrar** [00:13:40] spectrum between the type A, type B here, where

**Claire Vo** [00:13:43] Yeah.

**Scott Farrar** [00:13:44] I was able to dump in a lot of unstructured information and rely on the coding agent to structure it and maintain that structure. Actually, part of the system here is like there's a linting script that goes through and makes sure that, you know, verbose chat agents haven't over, haven't expanded too much, that making my to-do list too verbose or something. But I think actually that was really, I was really inspired by kind of how- These agents can just unlock files that's been on my computer forever, and just I've always known the data's in there, it's somewhere in there. I don't have time to sort through it right now. I would love it to manually go through and sort this, but I never have. But with Claude Code, with Codex, you know, you give it a directory and it can go through there and pull out and organize all the stuff in an amazing way. One of the files actually that I really come back to a lot in a manual way is the to-do list, the massive to-do list.

[00:14:48] So I said, I had it create this. I was like, you know, me and my wife, we had a brainstorming session of like, what is every single to-do item in our brain, big and small? Is it fixing the tub spout in the kid's bathroom that's doesn't spray quite right? is it, oh, there's going to be dry rot. We have a multi-thousand dollar dry rot problem, or do we? Or like, how do we find out if that's true or not? and so like, compile those into things, give me a priority level, give me a cost estimate, give me a priority and reference. So this is the file I come back to a lot, the to-do file.

**Claire Vo** [00:15:30] I love that because we was very similar household. It's like, I have a dry rot problem. Am I getting scammed by my dry rot guy? Did the dry rot guy do his job? And I do think, how do you and your wife collaborate on this? That's my question on- we talk a lot about multiplayer in the enterprise. Tell me about multiplayer in the home.

**Scott Farrar** [00:15:49] Yeah. Yeah, that was one of the earliest things that I talked about as I was setting this up. Um, so setting this up was super easy, uh, because I- I said, "Here are my constraints. I want to collaborate with my wife on this. I want to know things about the household, kinda scope it to the household. I'm not gonna do finances with this, I'm not doing medical information." Um, and- but when it would- when we're talking about sharing and working with me and my wife, I was like- I was imagining that, like, "Okay, I'll have this with my computer, I can talk to Claude, and it will know this stuff,

**Claire Vo** [00:16:23] Mhm.

**Scott Farrar** [00:16:23] but I also want my wife to talk to her Claude

**Claire Vo** [00:16:26] Mhm.

**Scott Farrar** [00:16:26] and have it know the same

**Claire Vo** [00:16:27] Yep.

**Scott Farrar** [00:16:27] things. And so I've been trying out a couple different variations on this, and the first one was just purely Dropbox, where it was a

**Claire Vo** [00:16:34] Yep.

**Scott Farrar** [00:16:34] Dropbox folder that we both had access to, copied on both our laptops, and so we

**Claire Vo** [00:16:39] Yep.

**Scott Farrar** [00:16:39] could do it. And there was a little bit of, like, it warned me that saying, "Well, maybe if you're both in there at the same time, you might have some Dropbox sync

**Claire Vo** [00:16:47] Mhm.

**Scott Farrar** [00:16:47] conflicts." Uh, and I said, "Well, what's the alternative?" And it said, "Well, you could try- you could do, like, GitHub, you could-

**Claire Vo** [00:16:54] Mhm.

**Scott Farrar** [00:16:55] if you're- if you're in that mindset of coding, you could, like, commit Markdown files into a- a GitHub repo and, you know, s- sync with that. And, uh, my wife was like, "I don't know if it's worth all that," um, there's some trade-offs for that still, and where we've landed actually is somewhere in the middle where, um, w- I kind of do like GitHub for some of the stuff. There's a few scripts that- like the linter, uh, and some of the other things that export to a wall display, but a lot of the stuff is handled with Dropbox, and we kind of just know that we're both not really in there at the same time, uh, reading and writing.

**Claire Vo** [00:17:32] Yeah. I mean, I do think this, like, sort of practical product constraint of, like, how real time is your collaboration, and if it's only lightly real time, you can probably deal with some conflicts. And so I also love that some of us, the more technically inclined, are like trying to bring into our households, like, "What if you just did a pull request, honey? Like, what if you just did a pull request? That would be totally fine for us to manage the refrigerator. so I think that's really funny.

[00:18:32] Jira Product Discovery, better product decisions in the AI era. You know, talking about that household board, how are you displaying using this information inside your house?

**Scott Farrar** [00:19:15] Oh, so, you know, here's one view that I look at because I'm a math teacher and I really like graphs.

**Claire Vo** [00:19:21] Yep.

**Scott Farrar** [00:19:22] But it's not like this is, uh, readable to the rest of my household. Um, and so what- what I- what I've been using for a little while is a product called Dakboard, which is kind of just a wall display. You can put information on there, you can put a lot of stuff that you want. Um, and one of the things, though, is you can just put a custom web page in there, and I was toying with the idea of, like, well, what can I extract out of my database and put it on the wall that might be useful so that I can kind of have that reference for me? I can- you know, you walk by it and your- catches your eye that, like, "Uh, I do need to do that. I do need to fix the faucet. I do need to get the new ice machine." That's what I wanted to surface. I wanted to get it out of my laptop and available for everyone. So what I had Claude do is build a little script to scrape kind of the to-do items, scrape upcoming trips, and scrape some other information and build a piece of the wall display that has just like top of mind things.

[00:20:27] You should keep this in your mind, like, what projects are you working on? What are the trips? Uh, a little su- a little, like, kind of, uh, suggestion of something to do today. Hey, it's only 12 dollars if you want to recock the hall bath. Um- And then maybe some longer term stuff that's, like, needs attention, uh, and y- just some t- stuff for my kids. Uh, I- I also put- made a section of recent wins just to say, like, "Good job, you did fix that, or you found out what iPads were out of date with software. You fixed the water heater in one day. Great job, Dad.

**Claire Vo** [00:21:04] I really love this. When I was working at Optimizely, we had this huge wall that we stood in front of every Monday. It was called the Wall of Work, and we, like, actually printed out- this was, like, back in the day where we had to, like, walk uphill both ways for our code, like, printed out every single epic that we were working on, and we would, like, move it on this physical board, and then we had, like, a wall of wins. Um, and I like that you are bringing that very wonderful scrum master energy to- to your household- household management. Um, do you find that this, like, helps you get stuff done? Do you- does it actually change your behavior?

**Scott Farrar** [00:21:42] It does. It does because when it has built a checklist for me-

**Claire Vo** [00:21:48] Mhm.

**Scott Farrar** [00:21:50] like- ...the- on the insurance- ...all these next steps or open items, uh, they are not, like, lost in my memory of, like, "Ah, I should do that," just a, like, a should thought in my head.

**Claire Vo** [00:22:02] Mhm.

**Scott Farrar** [00:22:03] It's recorded somewhere, and it's, like, will come back every time I- I do something in India chat, it might remind me, I was like, "Hey, actually, you're overdue on something." Like, it's going to remind me that you've been waiting since September 24th on this. And so it's really actually has moved me forward on so many projects that I've actually kind of like run out of pending fires, and I was like, "Oh, that's a new experience. I used to have a backlog, and now I'm- now I actually- it's the balls in everyone else's court. Like, I'm always sending the email, and it's, I'm waiting on them, and that's been really nice.

**Claire Vo** [00:22:40] So give me, just give me the list of, you know, somebody's like lives in their house as an adult, give me the list of like, here are household tasks you should just get your AI to think about. So I saw repairs, I saw like comparison shopping. What else? What's on, what's on the list so people can be inspired?

**Scott Farrar** [00:22:58] So here's the, here's what's in this to-do list. there's repairs, there's a little bit of like, yeah, insurance, financial, maybe like future planning, wills, guardianship, trusts, retirement funds, like if you want to consolidate your retirement. Actually, that's a huge headache that's I've been working on, that's been helpful here too. I think also like kind of IT, uh, and device management, um, trip planning, um, actually what I recently, with the earthquake reminder day, yesterday I think it was, I was like, oh, let's actually go to Claude here and say like, hey, do I need to plan for earthquakes? And then, you know, it's a very loose question that you just start with that, and because it's empowered by all the context you have, so it might know that the foundation is such and such, it might know you're in a liquefaction zone, liquefaction zone, and then I'm really confident of like, okay, let's start working here.

[00:24:08] So, oh, you should plan for earthquakes, da da da da, okay, yeah, let's capture this as an idea. I'm going to start a new project. so one of the structures in this is like there are project files, and those are going to be where we collect information and start checklists and check things off. and I really love to like close a project file when I'm done with it. I love to say like, all right, we finished all the, we finished that project, put it in the wins column, put it on the dashboard.

**Claire Vo** [00:24:36] I really love this, and what I'm seeing here, it looks like this is invoking a skill or a plugin to just follow your little process.

**Scott Farrar** [00:24:42] I think, yeah, I think it's picking up some structures from the Claude dot markdown, and saying, yeah, you should start by creating the project file or starting as an idea first. It hasn't been promoted to a full project. I do have, like, the backlog ideas, like earthquake readiness or just anything I think of, of like, just put that in the idea file. Should I re-landscape? Should I, do I need to repaint? Is the paint peeling off? I like taking a picture of the circuit breaker with all the scrawled electrician handwriting, and I have it on my backlog of like, can I go through and actually check which circuits those are and log it here so that I can ask Claude instead of trying to decipher the handwriting every time?

**Claire Vo** [00:25:27] We're burying the lead here. There are some really good workflows. I'm like looking around my house, I'm like, oh my gosh, I should do all of this, and you're giving me another idea, which I'm going to try, and then I'll report to you if it works. I'm just going to do a video walk through my house talking about stuff, and then I'm going to drop it to Claude or to ChatGPT. I'm going to be like, what do I need to be thinking about in this house? You have the video, you have all this stuff. Um, gen- genius, genius. This is gonna be AI for the homeowner is- is gonna be the- the headline here. You know, Scott, I wanna- I wanna zip to lightning round question, although the first question might not be so lightning because you and I have a shared interest, which is AI and kids and learning math. So tell- tell me a little bit about your co- you know, what you think about as somebody who's trying to figure out the intersection of AI and math and kids, and what should we be thinking about as parents?

**Scott Farrar** [00:26:25] I am a big fan of student agency. You know, we talk about agents a lot, right? And it's interesting in the contrast with this kind of project with what Muse or Instinct might do. There's some overlap, but there's not entirely some, not 100% overlap. And I think that's related to math education in a little bit, so give me some rope here. the- it's like if you're asking Muse, I know you've used Muse a little bit, Muse is the one out there maybe doing stuff for you, and in this model, I've kind of kept it back, kept that role for myself a little bit, like I want to know what you're going to suggest and recommend, but I'm going to be the one having some agency still. And I think when especially for students who are learning mathematics, we want to keep them doing the cognitive effort and keep them doing the agency, deciding what they want to know and struggling in a productive struggle to get there. so we got to find a role for AI that supports that instead of kind of short circuits and gives them the answer or is too helpful, or kind of maybe even doesn't appreciate the ideas that the student is giving.

[00:27:41] So I really like some of the products I see out there that are interpreting what the students say and running with that. It's like, oh, good idea, kid. tell me more about that.

**Claire Vo** [00:27:52] So what you're saying is important is, one, you personally like to be human in the loop. I don't like to be human. That's not for me. I like to the agent to be in the loop, so I'm very heavy, like Grok bot go, Muse go, but you're saying, like, I want the AI to put me to work, and that's what works well for my brain and how I like to be in the loop. And from a AI education perspective, you like, you know, solutions where it can support interpretation of what a student is doing but not take away that agency of, like, "I am learning how to solve this problem, I am learning how to- how to do the work." Can you show me an example of what you mean?

**Scott Farrar** [00:28:36] Yeah, I think, like, I've seen some projects, I've kind of noodled on projects, uh, myself where, uh, you kinda flip the relationship of a chatbot tutor where the tutor

**Claire Vo** [00:28:45] Mhm.

**Scott Farrar** [00:28:46] is now- uh, the- the chatbot is not aiming to teach the student,

**Claire Vo** [00:28:50] Mhm.

**Scott Farrar** [00:28:50] but the chatbot is aiming to extract some teachings from the student.

**Claire Vo** [00:28:53] Yes.

**Scott Farrar** [00:28:54] And so the chatbot might say- ...help me understand how to solve a linear equation, and-

**Claire Vo** [00:28:59] Yep.

**Scott Farrar** [00:29:00] and the student might say, like, "Oh, well, I kinda know what you should do is maybe subtract things from both sides," and the chatbot's like, "Ah, but, uh, but why do you- why do you have to do that?" And, you know, if- if- can the chatbot be positioned so that they are not annoying, but they can still add- grab the ideas that the student has. And the students have a lot of great knowledge in their heads, but sometimes they're afraid to share it out with humans and share it out with AI. So I think it's going to be powerful if we can enable kids to share their thoughts.

**Claire Vo** [00:29:32] Today, this is my second episode I've recorded today, and the earlier one was also about a language tutoring episode, so it might already be live, but what we were talking about in that one is AI is this like infinitely patient private tutor you can say all your dumbest stuff to. And so it's like never going to be that's a stupid question, or you should know that already. It can always kind of like help you privately go through your growth mindset, go through the like, what do I call my kids? The zone of frustration, where it's like, if you're frustrated, you're learning, and you can go through that zone of frustration with this sort of, like, private, patient, foil for your learning, and I think that's really powerful. And I tell people this all the time about coding, but it applies to any sort of learning activity.

**Scott Farrar** [00:30:23] Yeah, I think actually, the zone of frustration or zone of proximal development, I think,

**Claire Vo** [00:30:29] Mhm.

**Scott Farrar** [00:30:29] like, you know, can the tutor, um- I- I like you- you also mentioned, uh, infinite patience, and I think that's something that is interesting to- to play with o- in the chatbot realm of, like,

**Claire Vo** [00:30:42] Mhm.

**Scott Farrar** [00:30:42] should it be infinitely patient or should it also kind of, you know, politely but

**Claire Vo** [00:30:48] Mhm.

**Scott Farrar** [00:30:48] also, uh, be a- be a polite demander, a warm demander

**Claire Vo** [00:30:52] Mhm.

**Scott Farrar** [00:30:52] of saying, like, "You actually- I think you do know this, so

**Claire Vo** [00:30:55] Yep.

**Scott Farrar** [00:30:56] I can't quite do all the work for you. I

**Claire Vo** [00:30:58] Yeah,

**Scott Farrar** [00:30:59] need to

**Claire Vo** [00:30:59] yeah.

**Scott Farrar** [00:30:59] let you, uh- yeah.

**Claire Vo** [00:31:01] Need to give you some o- you can do it. Le- why

**Scott Farrar** [00:31:04] Yeah,

**Claire Vo** [00:31:04] do you give it a try?

**Scott Farrar** [00:31:05] I- I- yeah, I can- I can be super encouraging, uh, yeah, and s- and say what I know you already know and- and point you in the way to- to unleash your own knowledge.

**Claire Vo** [00:31:14] I- I love it. What a great- what a great framing. Okay, my last question we ask everybody when AI is not doing what you want, when it's being frustrating, when it cannot close that idea file, how do you prompt it? This is a good question to ask parents and teachers.

**Scott Farrar** [00:31:30] My honest answer is I kind of close that chat and see that. I was like, I just start a new session maybe and say like, ah, we must have gotten somewhere out of sync somehow." Um- Sometimes I- I ask it of like, "Why- why would you think that? Why did- how did you get that idea?" 'Cause I actually, in this context of working with the memory file so directly, I want to be sure that it's not like it hasn't written it somewhere in there. Uh, wa- one example is some- i- in an earlier version of the to-do file, it's just started writing all the updates in the to-do table, and then the to-do was just massively a lot of information, and I was like, "Didn't- didn't I put in the Claude instructions that, uh, it should be short and brief and not have the updates?" And then, you know, it comes back and- in a very positive voice of like, "You did tell me that, I'm sorry.

**Claire Vo** [00:32:31] So you ask a different- you ask a different why, like, why did you do that? I ask, why are you like this? Why? Or I just do a straight up why with 7 whys. Again, I think there is just like personality differences that go that we- how we work with our AI. This has been super fun. Um, AI put a bunch of context in there, put a bunch of loose context in there, figure- let AI figure it out.

**Scott Farrar** [00:32:59] Interesting.

**Claire Vo** [00:32:59] Use AI to keep you on track with managing your household responsibilities. Give yourself a pile of wins, and then, um, you know, when it comes to learning with AI, don't let it just give you the answer, let it push you, but also pull out from you what you already know. I- yeah. Great episode,

**Scott Farrar** [00:33:18] Great.

**Claire Vo** [00:33:18] Scott, I really appreciate this. Where can we find you and how can we be helpful?

**Scott Farrar** [00:33:23] I am, at SFXmath.com. You can see kind of what I work on there. you can find me on LinkedIn at Scott For. and yeah, I'm always eager to talk about math education.

**Claire Vo** [00:33:38] Amazing. Well, I am too. We're gonna stop the recording, and we'll go there. Thank you so much for joining How I AI.

**Scott Farrar** [00:33:45] Thank you.

**Claire Vo** [00:33:46] Thanks so much for watching. If you enjoyed the show, please like and subscribe here on YouTube, or even better, leave us a comment with your thoughts. You can also find this podcast on Apple Podcasts, Spotify, or your favorite podcast app. Please consider leaving us a rating and review, which will help others find the show. You can see all our episodes and learn more about the show at howiaipod.com. See you next time.
