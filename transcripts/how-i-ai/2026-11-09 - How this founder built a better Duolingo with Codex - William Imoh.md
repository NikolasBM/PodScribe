---
podcast: "how-i-ai"
podcast_title: "How I AI"
title: "How this founder built a better Duolingo with Codex | William Imoh"
date: 2026-11-09
url: "https://podcasters.spotify.com/pod/show/pen-name/episodes/How-this-founder-built-a-better-Duolingo-with-Codex--William-Imoh-e3rokon"
guid: "8e46e458-ab20-4543-a092-320adef5ed8c"
host: "Claire Vo"
guests: ["William Imoh"]
format: "interview"
level: 2
length: "00:38:05"
categories: ["agents", "coding", "work", "marketing"]
featured: ["OpenAI Codex", "Grok Bot", "GPT Live", "ChatGPT", "computer use"]
mentioned: ["GPT-6", "Cursor"]
transcript_source: "azure-asr"
transcribed_by: "MAI-Transcribe-2"
---

# How this founder built a better Duolingo with Codex | William Imoh

**William Imoh** [00:00:00] I tried building this app, but it just wasn't a great experience. Bombed the hackathon. I think I probably came in last with it. The meta skill that you have, which is like a growth mindset, which is I can learn Norwegian. Like, I can learn something. If you just have this confidence that this thing is a solvable problem, learning a language is a solvable problem, building an app is a solvable problem, and if you can just ask the right questions and get the right feedback, you can get there. I wanted to speak Norwegian to someone to something first that wouldn't judge me and something that would correct me. Now, I know it's counterintuitive in some parts and some conversations that you want to be skeptical about what AI has access to. For me, I just let all that fly out the window. The only thing it doesn't have right access to is the bank.

**Claire Vo** [00:00:47] You run a business and like me, like to keep that business lean with agents. So tell me a little bit about how you run your business with agents.

**William Imoh** [00:00:55] I don't get frustrated. I get scared because I'm so dependent on agents now that I fear for myself. What if these agents go to zero tomorrow? What am I supposed to do?

**Claire Vo** [00:01:08] Welcome back to How I AI. I'm Claire Vo, product leader and AI obsessive, here on a mission to help you build better with these new tools. Today I have William Imo, founder of Hack Mamba and creator of Mural Chat, a real-time language learning app that he built for himself to learn how to speak Norwegian, of all things. William's going to show us how he went from knowing nothing about native development to hacking together one of the coolest native apps I've ever seen, plus how he uses an army of Lord of the Rings themed Grok bots to run his business as a solo founder. Let's get to it.

[00:02:08] William, welcome to How I AI. Thanks for joining.

**William Imoh** [00:02:59] Thanks. Thanks, Claire. Thanks for having me.

**Claire Vo** [00:03:01] So I invited you on the podcast because I saw this app that you have up, Mural, I think it's Mural Chat, and I just thought it was such a cool use of AI and something that, a year or two ago would have been sort of like unimaginable for someone to build on their own, like almost impossible. And you've shown that you can build this amazing app with this really interesting use case and do it all by yourself with AI. It's just, it's kind of unbelievable to me. So tell me what brought you to building this app? Like, what problem were you trying to solve? What was driving you?

**William Imoh** [00:03:38] Yeah, I think you're also correct that a year ago it was technically impossible. it was possible to build the app, but with a poor experience, because I tried. I was at a hackathon in San Francisco, and it was, I think it was an all things web hackathon. I tried building this app, but it just wasn't a great experience. Bombed the hackathon. I think I probably came in last with it. and the main motivation behind this is I live in Norway, and I one-upped and moved from Dubai to Norway because I wanted an adventure. I didn't know what to expect. I just hoped everyone spoke English. As soon as I got here, I learned that people actually speak Norwegian, and to make it by, I mean, a lot of people speak English, but you need Norwegian to get by. But then the Norwegians are also very polite in the sense that if you try to speak Norwegian to them, but it's poor, they speak English back, unlike the French.

**Claire Vo** [00:04:38] Mm-hmm.

**William Imoh** [00:04:38] So they speak English back to you. So this meant I couldn't learn Norwegian, right? And then I tried using Duolingo. I had a thousand day streak on Duolingo. I was always like chasing streaks and but I wanted to speak Norwegian to someone to something first that wouldn't judge me and something that would correct me. But also I wanted to experience that felt like being thrown in a Norwegian village where you have no other option but to speak Norwegian. That was just the experience I wanted.

**Claire Vo** [00:05:08] I love this because in our house, we are trying to, we, my husband and my kids are trying to learn Italian, and they're doing it this like very classic language learner way, which is a combination of Duolingo and like listening to Ital- like basically these like tapes, these audio lessons, and so they're in the car and they're like, you know, hearing somebody speak Italian and then they repeat it. But the only way you can really learn a language is immersion, and I love what you call out because it's so counterintuitive, which is you said you can't learn this language because people are so polite, they will respond to you in English, and so you can't actually get that reinforcement loop of like, did I say it right? What am I supposed to hear? And so you built this app to give you that experience. Tell us a little bit about like, are you an iOS developer? Are you like a fancy developer?

**William Imoh** [00:06:07] So first, I have a chemical engineering degree, but then I taught myself to code to do some web development. So I did a lot of web development over the last, five, six years. I can write some front end, I can, and then I can write some back end code to save my life. Building a web, building a mobile app, I can do it with something like React Native, for instance. But I wanted today, or at least when I built Mural, I wanted a native experience. So I wanted like a premium feel to it because I felt like I could build anything, but I wanted to optimize for the best user experience possible, and I wanted to use like all the better iOS features. So I decided to build in Swift. Well, it wasn't going to be me building it. I needed Codex to build it. so I, this is building Swift for iOS and Kotlin for Android. I guess when we have AI agents building stuff, like the language doesn't matter, like the language I know doesn't matter anymore.

[00:07:11] I just choose the best possible language for the tech that I'm building. so that's why I went with Swift and Kotlin, even though I haven't written a line of Swift in my life.

**Claire Vo** [00:07:21] You know, what's really funny about this is, you know, over 10 years ago, I did a like a venture funded startup, a real startup, and we picked the language we built that application in based on who we knew could write that code. So we were like, well, we know a bunch of people that can write Python, and we know a bunch of people that can do this, and so we're just going to build our app in that language to optimize for humans we knew knew how to write that code. And now I love what you said, which is you can just pick the best language for the user experience, the thing that you want to build, and it doesn't matter if you have somebody on staff that knows that language or not, because you have our friend Codex on staff. Speaking of Codex, do you mind pulling it up and just showing us how you, how do you get organized around a Swift? I've actually never, don't tell, sorry, we're doing admission right here. I have not built a native mobile app ever, even in the age of AI, I have not built one.

[00:08:22] So I am learning as we go. How do you, how did you kick this off? How do you, how do you work it?

**William Imoh** [00:08:29] background, because I have some software engineering background, I understand how to architect apps. I understand like what's required if I need to make the front end, the back end, also the experience that I want. I think that's the most important piece here is the experience I wanted for this app. I used to be a product manager as well. I was a product manager for four years. So I've learned to work in epics and user stories, right? Because those are closely tied to user problems. So that's one way I've found, I've had like the best results when building AI apps. So how did you start? I first started with a very long prompt that was very specific, and this prompt opened with literally, I want a very aesthetically pleasing application. Like, this is my equivalent of make no mistakes, but is I want an aesthetically pleasing iOS application, that would, that I can learn Norwegian with. And I described the experience I want, which was basically, I want this application to run on GPT Live 1, because GPT Live 1 was just released, I think, a week after.

[00:09:36] So GPT Live 1 was the technology that I tested that enabled me build this. I don't think I'll be able to build this without GPT Live 1 today. So I specified we need to use GPT Live 1, and then we needed to use GPT 6, Luna for any other AI, any other AI tasks on it. I described also the experience I wanted. So I wanted an orb that was, a pulsating orb that I could talk to that felt like a phone call, like a familiar interface that we would use. And then I went on to describe the style. So I wanted something warm. I literally wrote, I want something that feels like fall, like autumn, use fall colors, and again, it should be really beautiful. Follow design best practices like you are a senior designer at Apple.

[00:10:36] So I'm just giving it, I'm just giving it references of like, because I needed to get the taste that I wanted. because I live in Norway now, I love to adopt like a very minimalist style. So I was like, make it like it should be really minimalist. No element on the screen should exist unless it absolutely has to. And if something isn't necessary, remove it or put a toggle for it. so this was the like the base experience, and then I requested that it reviews the design after it's done. Now, the first design it produced was shit. It was in dark mode. It was in dark mode. I was like, "No, this isn't gonna work.

**Claire Vo** [00:11:20] Maybe that feels like autumn in Norway, right? It starts to get really dark.

**William Imoh** [00:11:26] So, yeah, I had to refine even further. I was like, first, this shouldn't be in dark mode. Not everything belongs in dark mode. it should be light mode. Use light, warm colors, explore gradients, and I'll use liquid glass as much as possible as well.

**Claire Vo** [00:11:45] So I want to pause really quickly because what I think is so interesting about what you just said in that prompt and our conversation so far is, look, you don't need to know Swift. Like, you just don't. It's none of your business. You don't need to know. You need to know that maybe that you should use Swift, although AI could figure that out. But what you do have that I feel like a lot of people haven't invested in their own skilling is design and product language. Like truly the ability to describe what you want with specificity. And when people talk about taste, do they talk about taste all the like, what is taste? We need taste. And really what you need is design language and references in the world that you can point to. You need to know what liquid glass is, you need to know what minimalism is, you need to know what a gradient is, and I think the more rich your reference set is when it comes to design, the better.

[00:12:49] And then on the product side, the more you know how to articulate a user journey in a way that anybody can execute on, an engineer, human engineer, a AI engineer, the better that like workflow will be. And so, when people ask me like, how do you develop taste or how do you get good at work? I'm like, describe websites, like use your words to describe what makes brand A versus brand B special or what makes website A or app A better. And the more you practice that, I think the better you can be at prompting agents to do a great job.

**William Imoh** [00:13:28] Yeah, I agree. I look at, and as soon as I put this out there, I didn't intend to share it with anyone because I wanted to build this for myself to use just by myself. And then I put out a tweet out, hey, I made this thing. I think it's really cool. I'm not going to share because I don't want the burden of having to maintain it and having to like deal with users' expectation. Every- not everything has to be a business. I already have a lot of problems running the business. I don't want another one. so I put it out there and people loved it, and not just people liking the experience, but I also saw a lot of people that had similar applications. And then I looked at the difference between what I built and theirs, and I noticed a lot of it just had to do with the experience, like how it felt when you looked at it, right? A lot of it were was also in dark mode, like I rejected first. It had a lot of features, right? for me, I just wanted speech and a caption.

[00:14:28] A caption would be the only way you would understand what's being said if you're just hearing the language for the first time. That was my opinion, and that was the only thing I wanted.

**Claire Vo** [00:14:38] Can you show it to us real quick? We're gonna put your Norwegian to the test.

**William Imoh** [00:14:44] Ja, kan du høre meg? Ja, jeg hører deg. Hva vil du snakke om? Jeg er på møte. Rettelse, det heter et møte. Hva skjer i møtet? Can you speak English? Jeg holder meg på norsk. Hva skjer i møtet? Yeah, please, please just speak English. Jeg forstår, men jeg snakker norsk. Hva snakker dere om i møtet nå? Ja, ja, vi kan snakke norsk. Fint. Hvem er med i møtet? Ja, jeg er på møte med vennen min. Dette det heter vennen min. Hva snakker dere om? Jeg snakker med vennen min. Dette det heter vennen min. Hva...

**Claire Vo** [00:15:40] I am, one, really impressed. I'm very impressed, um, a-at your Norwe- I mean, I know nothing about Norwegian, but it impressed me. And 2, I totally get it, like, I get why that's the way you need it to learn- like, need to learn. So can you just walk me through what that conversation we just heard kinda, like, was? Like, what were you talking about?

**William Imoh** [00:16:07] Yeah. Basically, I was trying to- first, I was like, hi, and because Mural starts with hi and then figures out your level of language learning or speaking. so it said hi back, and then it said something complex, and I said something mildly complex back, and I said, I'm doing all right. And it's, it, Mural asked me, so what am I doing? I said, I'm in a meeting with a friend, and, Mira said something, but I ignored that, and I said, "Please, can you speak English?" And Mira said, "No, I cannot- I cannot speak English back. I have to speak Norwegian." So I think I can pull up the past conversation.

**Claire Vo** [00:16:52] Yeah, yeah, I wanna

**William Imoh** [00:16:52] Uh-

**Claire Vo** [00:16:52] see.

**William Imoh** [00:16:54] Yeah. so it was like, "Hi, like, what do you want to talk about today?" I was like,

**Claire Vo** [00:17:00] Mhm.

**William Imoh** [00:17:00] "Oh, yeah." I was like, "Are you ready to start or do you want to think a little bit? I was like, hmm. And I said, can you hear me? And Mira said, yes, I hear you. What do you want to talk about? I said, I'm in a meeting. and I said a meeting wrong. I said yarapo en murte, but that's the wrong tense. So it says, it's called et møte, not en møte. So it corrected me as I said that and then asked, what's happening in the meeting? Then I said, can you speak English? and it refused, said, I'm only going to speak Norwegian. What are you doing in the meeting? I said, oh, please just speak English. And then Mira said, I understand, but I'm going to speak Norwegian. What are you talking about in the meeting? And then I gave up.

**Claire Vo** [00:17:54] I'm- okay. Quick- quick-

**William Imoh** [00:17:56] Yeah.

**Claire Vo** [00:17:56] quick question. When did you start learning Norwegian? Like, how-

**William Imoh** [00:18:01] Um-

**Claire Vo** [00:18:01] how long?

**William Imoh** [00:18:03] So I started learning Norwegian, I mean, I had a- a 1,000-day streak on Duolingo.

**Claire Vo** [00:18:07] Yeah. Okay, so you

**William Imoh** [00:18:08] Um,

**Claire Vo** [00:18:08] had a

**William Imoh** [00:18:08] but

**Claire Vo** [00:18:08] little

**William Imoh** [00:18:08] I

**Claire Vo** [00:18:08] bit of a

**William Imoh** [00:18:09] couldn't-

**Claire Vo** [00:18:09] head start.

**William Imoh** [00:18:10] Yes, but I couldn't have this kind of conversation. I wouldn't know what to say. I'm- I'm stuck

**Claire Vo** [00:18:15] Yeah.

**William Imoh** [00:18:15] at I'm a man or this is a phone, you know?

**Claire Vo** [00:18:19] Yeah.

**William Imoh** [00:18:20] Uh, so I would- I wouldn't be able to hold a conversation. Um, and then I took the Norwegian- I took the Norwegian language, um, exams. Um, and I took a course for, like, a week, like a short course for a week, just so I understood, like, grammar. Um,

**Claire Vo** [00:18:37] Yep.

**William Imoh** [00:18:37] I took the exams, I passed. As soon as I came out of, like, the exam hall, I deleted Duolingo because I was like, nah, this is just completely useless. and I tried it, and that was my like, my motivation to build something like Mural started after that. So Mural just helped me get better at practicing my Norwegian in different like settings. And you know, this is, I could talk about like the weekend, I can also see, like, the words that I've learned, and how well I've, you know, I've gone with, like, with each one. I recently introduced flashcards, for instance, in case I want to practice, like, the words.

**Claire Vo** [00:19:21] The words.

**William Imoh** [00:19:23] Yeah, exactly. and I also have themes because at the end of the day, you want to be able to speak these languages, within a particular setting. And I can also pick like a random theme about like maybe AI or something, in the world today. It would search the internet and come up with a conversation about that. But at the end of the day, it all lives on the talk screen. I just go here, I start a conversation with Miro, and I just talk about stuff, whatever. And it just keep nudging me further and correcting me as I go, and it wouldn't stop correcting me until I say it properly.

**Claire Vo** [00:21:03] Okay, so we've had a lot of impressive people on How I AI. There's a lot of impressive things. One, let's put aside that you vibe coded this whole thing, which is awesome. Two, let me just say the meta skill that you have, which is like a growth mindset, which is I can learn Norwegian, like I can learn something, and I feel like this is the skill that really helps people go very far in the age of AI, which is like, if you just have this confidence that this thing is a solvable problem, learning a language is a solvable problem, building an app is a solvable problem, like, these are solvable problems that you have the tools, and if you can just ask the right questions and get the right feedback, you can get there. I think that is just like, that is the skill of the- and also I would say being really low ego, which is like, I'm okay getting it wrong as long as I can be corrected.

[00:22:10] And I think AI is such a great teacher because I tell this to people about learning to code. I say it is an infinitely patient private tutor. Like, it's not gonna make fun of you. It's not gonna say you're stupid. It's not gonna be embarrassing. So, like, the ability to use AI as a tutor for any topic and let it be patient with you and let it let you make mistakes, I just, I think it's the skill that is a real signal that somebody's gonna be very high impact in this next phase of the world. And so that is what I'm observing of you at a higher level. no, thank you. This is so, it's like given me so many ideas. The other thing I just want to pause before we go into a couple other workflows is GPT Live. So for people that don't know what GPT Live is, it's OpenAI's kind of real-time voice model, and it does really good with real-time experiences and like interruptions, which make it great for this kind of language testing.

[00:23:15] The other thing GPT Live is really good at is voice control of apps because it's so fast. So, I think we did an episode, I'll have to dig it out, of voice control through GPT Live in your app. so I think GPT Live is a totally slept on model that people don't appreciate how much you can do with it. The only thing I have to ask you a question, is this expensive to run?

**William Imoh** [00:23:42] so the honest answer, yeah, but I just chug it into like my token budget, right? I made it open source so anyone can run it, and it currently costs around, it costs about five dollars to chat with Miro for, I think, for 30 minutes. Yeah, so for about 30 minutes, it's going to cost $5 in... No, it's going to cost between 3 and 5 dollars for 30 minutes. but then I'm building this for fun, so I'm just, I put $1,000 on my OpenAI budget and just let folks burn it to the ground. I think it's remaining like a hundred dollars now.

**Claire Vo** [00:24:36] Well, what I'll also say is that it's less expensive than a one-on-one tutor, and you can't call your tutor to your house in the middle of the night and say, I'm ready to practice some Norwegian. So it's so cool. Okay, we're gonna do a couple more workflows. We'll get you out of here. So, aside from building cool apps and learning Norwegian, you run a business, and like me, like to keep that business lean with agents. So tell me a little bit about how you run your business with agents.

**William Imoh** [00:25:06] Yeah, so first of all, in sometime in June, when we started planning Q3, I put together a mandate internally, and I called it 100x, and this was a way for us to go 100x our current like revenue goals and the way we're set up as a company without drastically increasing headcount. And this meant that we needed to use AI as much as possible without using AI to generate content or ceding any of our creative work to AI tools. so first of all, I had to figure out everything I currently do. I put together a list on Notion. That was my first step. I listed everything. So as the founder, and I'm a solo founder, so I do a bit of customer success. I handle most of the inbound sales, currently working, I think, about 11 to 15 deals in parallel at the moment.

[00:26:08] I handle the product team as well because I used to be a product manager, and I do a bit of like accounting, HR interviews, like hiring, so just talking to folks, and we're a team of around 25 people internally. so I wanted a way to be able to manage a lot of things. First, I wanted to hire a chief of staff. I tried hiring someone, they didn't start. They quit on like just before they started for some reason. I think that was like a Hail Mary for me. so I decided to adopt AI tools. and I tried different tools, right? I tried Claude first. I got used to use the Claude Cowork, and then for some reason my account got banned. I don't know why. I skipped it. I went back to ChatGPT and installed Work, and I decided to use projects, as I currently have on here. I set up projects for everything, basically, because I just wanted a siloed way to manage individual things I do.

[00:27:14] My company's called Hackmamba, so for every critical piece that I work on directly, I create a project for it. I have a project for Hackmamba operations. This is where I manage things like, invoicing, campaigns, not just, and if anyone sends me a message on Discord, this is where that would likely fall into, and that task will be run from here. I have stuff for growth. So this is like, I also get like an operator brief every Sunday night of the week. So what's something we should start doing? What's something we should stop doing, and stuff we should keep doing. I also ask it for like the three highest impact activities I would conduct this week. So that's a routine. So I use routines a lot as well. we built an internal tool for growth. this is what we use to, we use with our customers. We go from content ideation all the way to distribution in Boki. I also support with the growth for Boki and content creation.

[00:28:17] so I created a project for it. For sales, I did the same thing for our website. This is my podcast, Everything Outside Code. I manage like interview briefs and all that in there, and just every other thing. So I use projects a lot with Codex. now for Codex, I kind of reserve like the complex work. So for instance, Miro, haven't written Swift, so I kind of like wanted Astra to work on Miro. So I wanted frontier model on that stuff. that that's what I do on Codex. But on the flip side, I found Grok bot, and instantly I think it was amazing, like it was a game changer for me because it gave me colleagues, whereas with ChatGPT I got, and like Codex, I got folders, and on Grok bot I got my fellowship, as I like to call them. if you've seen Lord of the Rings, you know what the fellowship of the ring is.

[00:29:18] So I just, I was first asked to create a chief of staff. I just called him Gandalf, straight up, straight up. And then I asked Gandalf to create everyone else. I needed, all the bots for engineering, marketing, project, product management, account sales, and customer success. And kind of the personas are, very close match, like Legolas is, pretty Legolas, he's the marketing dude. Eron the elf runs engineering. I have Gimli, the dwarf with the coins in accounts. Aragon recruits everyone and sells the fellowship. He runs sales, and Sam always plays support. So he's customer success for this one. And yeah, Frodo is in charge of getting the ring. He's basically the product owner in this case. So our further rounds PM.

[00:30:19] And yeah, so this, I set up the fellowship and with my AI workflow, what I do first of all after setting up the fellowship, and not just on Grok bot, but also on Codex, was to give it access to everything. Now, I know it's counterintuitive in some parts and some conversations that you want to be skeptical about what AI has access to and what it doesn't, what, it has read or write access to. for me, I just let all that fly out the window. The only thing it doesn't have write access to is the bank. So I'm like, anything else can go wrong. I mean, I don't have access to customer data, right? So that's safe as well. But the bank and customer data, aside from that, every other thing is up for grabs. So I gave it access to like Google Suite. I gave it access. I just looked at my browser window. I have like 15, 16 tabs open, and I just gave it access to everything that I could, I could see from Linear, Notion, my calendar, Pipedrive, QuickBooks, everything that I had access to, I gave it access.

[00:31:30] And then for ChatGPT, like for Codex, I just enabled computer use and browser use. So if it cannot find it via MCP, just use my computer. That's all right. It's fine. Whatever, I just give it access. It's like allow once. I'm like, no, allow always. That's, just use it. so setting those up, that was like the next thing, and that just instantly changed a lot of things for me, right? So I wasn't giving it information. I would just like, I could even put a typo in the input box. I would just like give it my like a thought, like I've been hiring and talking to like a lot of candidates. I built a tool internally called Three Pipes. So, and the reason I built it is because I have a firm belief that at the end of the day, we're going to be left with systems of record, like a custom database that is designed around a problem. That's what's going to be left, and an AI interface.

[00:32:34] So, I would build these tools internally, and they just become systems of record. Three Pipes is for people and HR. So now I just tell like my Grok bot, and the good thing is I don't need a skill for this. I talk to a candidate and I just say to my Grok bot, hey, I just spoke to this person, get them into three pipes. It goes, scours my email, my calendar, looks at meeting notes, collects all that information, puts it in three pipes, gives me a summary. It's all done, and then scores the candidate as well and says, you've spoken to 15 people. This person ranks number seven on that list, just so you know, like FYI. and I skip down it, then I can switch context to something else, to sales. So that's like the one piece. And then the final piece of how I use AI and how I'm set up currently would be the skills that I have. so there are a couple important skills that I do have, and I call these important because over time, while I've made a lot of skills, the models have gotten a lot better that I don't need these skills anymore.

[00:33:41] so there's just very few that stop. a skill I use for growth marketing, like to create a growth marketing strategy based on what we know at Hackmamba. a skill to create a content strategy, also based on what we know, and then my content de-slop skill. That's the

**Claire Vo** [00:34:02] Critical, critical skill in this stack.

**William Imoh** [00:34:04] Exactly.

**Claire Vo** [00:34:05] I just, I think this is so useful. I mean, for folks that have stuck around this long in the episode, you've gotten like true gold, which is you have Codex for complex tasks, Codex projects to keep everything organized. Grok bot, as you do this very similar to me, where like Grok bot has roles, so it's like your marketing role, your HR role, your sales role. you need an eye of Sauron that looks across everything for things going wrong. That's the last one you need. Eye of Sauron, and then you use just like skills very precisely, like very specific ones. William, this is one of my favorite ep- I'm not, I've done a lot of episodes. This has been one of my favorite, one of my favorite ones. I'm going to ask you our one question we ask every guest, and then I'm going to get you out of here to back to all your awesome work. But when your Grok box, your Codex, your Norwegian agent just is not replying to you, doing what you want, what's your prompting strategy? Are you polite? Do you yell?

[00:35:07] What's the real truth?

**William Imoh** [00:35:10] So first I just restart the agent. Just reboot. I just reboot. I reboot, and I try again. And if it doesn't work, I try to be a bit more specific, right? Because I know how to do it already. I just don't want to do it because it's like low level work. so I get very specific on do this first, test this first, and also review what you've done to be sure this is what I asked for. So just asking it to like go over it again. and more recently, I've had my Grok bot drive my Cursor agent. so while the Cursor agent would do like some random stuff that isn't really accurate, my Grok bot is sort of like that agent that goes and reviews all that again and improves it also. so that that's been like one way, but the agents have just been like really good that if it doesn't get it, I just go on Twitter and I blame Thibault for not fixing.

**Claire Vo** [00:36:19] At Thibault. That's exactly right.

**William Imoh** [00:36:22] Just at Thibault straight, you know, for not fixing Codex. Like, yeah, I tried, or I just switched the agent, use something else and wait and update it. but yeah, that's typically my strategy. I don't get frustrated. The frustration I feel is if it eventually doesn't get it at the quality I want, I get scared

**Claire Vo** [00:36:44] Yeah.

**William Imoh** [00:36:44] because I'm so dependent on agents now that I fear for myself. I'm like, what if all this tanks? What if, like, what if these agents go to zero tomorrow? What am I supposed to do? How am I supposed to manage 15 different, like, sales opportunities in a week in tandem, having all these calls, still doing, like, hiring, doing all these things at once? I- that's the only, like, panic attack I get because I'm like, this goes down, I'm screwed. What am I gonna do?

**Claire Vo** [00:37:17] What- what a perfect end to our episode, William. This has been super, super fun. for our audience, where can we find you and how can we be helpful?

**William Imoh** [00:37:27] Yeah, I'm on LinkedIn, I'm on X at iTrilo, William Imo on, on LinkedIn, just find a dude with, like, put on headphones, like, I fly small planes on off days, so, that's a way to find me. And if anyone's interested in growth, especially if you have a dev tool product and you want to reach your next 5, 10K users, I'm always happy to chat about like how we could do that together, basically.

**Claire Vo** [00:37:58] Amazing. Well, thank you so much for joining How I AI.

**William Imoh** [00:38:02] Yeah, thanks. Thanks for having me.

**Claire Vo** [00:38:05] Thanks so much for watching. If you enjoyed the show, please like and subscribe here on YouTube, or even better, leave us a comment with your thoughts. You can also find this podcast on Apple Podcasts, Spotify, or your favorite podcast app. Please consider leaving us a rating and review, which will help others find the show. You can see all our episodes and learn more about the show at howiaipod.com. See you next time.
