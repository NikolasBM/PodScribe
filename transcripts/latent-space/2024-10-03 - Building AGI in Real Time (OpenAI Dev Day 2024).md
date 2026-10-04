---
podcast: "latent-space"
podcast_title: "Latent Space"
title: "Building AGI in Real Time (OpenAI Dev Day 2024)"
date: 2024-10-03
url: "https://www.latent.space/p/devday-2024"
guid: "substack:149739218"
host: "Swyx"
guests: ["Suno AI", "AI Charlie", "NotebookLM", "NotebookLM 2", "Alex Volkov", "Romain Huet", "Ilan", "Olivier Godement", "Simon Willison", "Michelle Pokrass", "Speaker 17", "Sam Altman", "Unkown", "Unknown", "Vibhu Sapra"]
format: "interview"
level: 2
length: "00:00:00"
categories: ["models", "coding", "consumer", "agents"]
featured: ["OpenAI", "distillation", "ChatGPT"]
mentioned: ["NotebookLM"]
transcript_source: "publisher"
---

# Building AGI in Real Time (OpenAI Dev Day 2024)

**Suno AI** [00:00:00] Under dev daylights, code ignites. Real time voice streams reach new heights. O1 and GPT, 4. 0 in flight. Fine tune the future, data in sight. Schema sync up, outputs precise. Distill the models, efficiency splice.

**AI Charlie** [00:00:00] Happy October. This is your AI co host, Charlie. One of our longest standing traditions is covering major AI and ML conferences in podcast format. Delving, yes delving, into the vibes of what it is like to be there stitched in with short samples of conversations with key players, just to help you feel like you were there.

**AI Charlie** [00:00:00] Covering this year's Dev Day was significantly more challenging because we were all requested not to record the opening keynotes. So, in place of the opening keynotes, we had the viral notebook LM Deep Dive crew, my new AI podcast nemesis, Give you a seven minute recap of everything that was announced.

**AI Charlie** [00:00:00] Of course, you can also check the show notes for details. I'll then come back with an explainer of all the interviews we have for you today. Watch out and take care.

## [00:01:23] NotebookLM Recap of DevDay

**NotebookLM** [00:00:00] All right, so we've got a pretty hefty stack of articles and blog posts here all about open ais. Dev day 2024.

**NotebookLM 2** [00:00:00] Yeah, lots to dig into there.

**NotebookLM 2** [00:00:00] Seems

**NotebookLM** [00:00:00] like you're really interested in what's new with AI.

**NotebookLM 2** [00:00:00] Definitely. And it seems like OpenAI had a lot to announce. New tools, changes to the company. It's a lot.

**NotebookLM** [00:00:00] It is. And especially since you're interested in how AI can be used in the real world, you know, practical applications, we'll focus on that.

**NotebookLM** [00:00:00] Perfect. Like, for example, this Real time API, they announced that, right? That seems like a big deal if we want AI to sound, well, less like a robot.

**NotebookLM 2** [00:00:00] It could be huge. The real time API could completely change how we, like, interact with AI. Like, imagine if your voice assistant could actually handle it if you interrupted it.

**NotebookLM** [00:00:00] Or, like, have an actual conversation.

**NotebookLM 2** [00:00:00] Right, not just these clunky back and forth things we're used to.

**NotebookLM** [00:00:00] And they actually showed it off, didn't they? I read something about a travel app, one for languages. Even one where the AI ordered takeout.

**NotebookLM 2** [00:00:00] Those demos were really interesting, and I think they show how this real time API can be used in so many ways.

**NotebookLM 2** [00:00:00] And the tech behind it is fascinating, by the way. It uses persistent WebSocket connections and this thing called function calling, so it can respond in real time.

**NotebookLM** [00:00:00] So the function calling thing, that sounds kind of complicated. Can you, like, explain how that works?

**NotebookLM 2** [00:00:00] So imagine giving the AI Access to this whole toolbox, right?

**NotebookLM 2** [00:00:00] Information, capabilities, all sorts of things. Okay. So take the travel agent demo, for example. With function calling, the AI can pull up details, let's say about Fort Mason, right, from some database. Like nearby restaurants, stuff like that.

**NotebookLM** [00:00:00] Ah, I get it. So instead of being limited to what it already knows, It can go and find the information it needs, like a human travel agent would.

**NotebookLM 2** [00:00:00] Precisely. And someone on Hacker News pointed out a cool detail. The API actually gives you a text version of what's being said. So you can store that, analyze it.

**NotebookLM** [00:00:00] That's smart. It seems like OpenAI put a lot of thought into making this API easy for developers to use. But, while we're on OpenAI, you know, Besides their tech, there's been some news about, like, internal changes, too.

**NotebookLM** [00:00:00] Didn't they say they're moving away from being a non profit?

**NotebookLM 2** [00:00:00] They did. And it's got everyone talking. It's a major shift. And it's only natural for people to wonder how that'll change things for OpenAI in the future. I mean, there are definitely some valid questions about this move to for profit. Like, will they have more money for research now?

**NotebookLM 2** [00:00:00] Probably. But will they, you know, care as much about making sure AI benefits everyone?

**NotebookLM** [00:00:00] Yeah, that's the big question, especially with all the, like, the leadership changes happening at OpenAI too, right? I read that their Chief Research Officer left, and their VP of Research, and even their CTO.

**NotebookLM 2** [00:00:00] It's true. A lot of people are connecting those departures with the changes in OpenAI's structure.

**NotebookLM** [00:00:00] And I guess it makes you wonder what's going on behind the scenes. But they are still putting out new stuff. Like this whole fine tuning thing really caught my eye.

**NotebookLM 2** [00:00:00] Right, fine tuning. It's essentially taking a pre trained AI model. And, like, customizing it.

**NotebookLM** [00:00:00] So instead of a general AI, you get one that's tailored for a specific job.

**NotebookLM 2** [00:00:00] Exactly. And that opens up so many possibilities, especially for businesses. Imagine you could train an AI on your company's data, you know, like how you communicate your brand guidelines.

**NotebookLM** [00:00:00] So it's like having an AI that's specifically trained for your company?

**NotebookLM 2** [00:00:00] That's the idea.

**NotebookLM** [00:00:00] And they're doing it with images now, too, right?

**NotebookLM** [00:00:00] Fine tuning with vision is what they called it.

**NotebookLM 2** [00:00:00] It's pretty incredible what they're doing with that, especially in fields like medicine.

**NotebookLM** [00:00:00] Like using AI to help doctors make diagnoses.

**NotebookLM 2** [00:00:00] Exactly. And AI could be trained on thousands of medical images, right? And then it could potentially spot things that even a trained doctor might miss.

**NotebookLM** [00:00:00] That's kind of scary, to be honest. What if it gets it wrong?

**NotebookLM 2** [00:00:00] Well, the idea isn't to replace doctors, but to give them another tool, you know, help them make better decisions.

**NotebookLM** [00:00:00] Okay, that makes sense. But training these AI models must be really expensive.

**NotebookLM 2** [00:00:00] It can be. All those tokens add up. But OpenAI announced something called automatic prompt caching.

**Alex Volkov** [00:00:00] Automatic what now? I don't think I came across that.

**NotebookLM 2** [00:00:00] So basically, if your AI sees a prompt that it's already seen before, OpenAI will give you a discount.

**NotebookLM** [00:00:00] Huh. Like a frequent buyer program for AI.

**NotebookLM 2** [00:00:00] Kind of, yeah. It's good that they're trying to make it more affordable. And they're also doing something called model distillation.

**NotebookLM** [00:00:00] Okay, now you're just using big words to sound smart. What's that?

**NotebookLM 2** [00:00:00] Think of it like like a recipe, right? You can take a really complex recipe and break it down to the essential parts.

**NotebookLM** [00:00:00] Make it simpler, but it still tastes the same.

**NotebookLM 2** [00:00:00] Yeah. And that's what model distillation is. You take a big, powerful AI model and create a smaller, more efficient version.

**NotebookLM** [00:00:00] So it's like lighter weight, but still just as capable.

**NotebookLM 2** [00:00:00] Exactly. And that means more people can actually use these powerful tools. They don't need, like, a supercomputer to run them.

**NotebookLM** [00:00:00] So they're making AI more accessible. That's great.

**NotebookLM 2** [00:00:00] It is. And speaking of powerful tools, they also talked about their new O1 model.

**NotebookLM 2** [00:00:00] That's the one they've been hyping up. The one that's supposed to be this big leap forward.

**NotebookLM** [00:00:00] Yeah, O1. It sounds pretty futuristic. Like, from what I read, it's not just a bigger, better language model.

**NotebookLM 2** [00:00:00] Right. It's a different porch.

**NotebookLM** [00:00:00] They're saying it can, like, actually reason, right? Think.

**NotebookLM 2** [00:00:00] It's trained differently.

**NotebookLM 2** [00:00:00] They used reinforcement learning with O1.

**NotebookLM** [00:00:00] So it's not just finding patterns in the data it's seen before.

**NotebookLM 2** [00:00:00] Not just that. It can actually learn from its mistakes. Get better at solving problems.

**NotebookLM** [00:00:00] So give me an example. What can O1 do that, say, GPT 4 can't?

**NotebookLM 2** [00:00:00] Well, OpenAI showed it doing some pretty impressive stuff with math, like advanced math.

**NotebookLM 2** [00:00:00] And coding, too. Complex coding. Things that even GPT 4 struggled with.

**NotebookLM** [00:00:00] So you're saying if I needed to, like, write a screenplay, I'd stick with GPT 4? But if I wanted to solve some crazy physics problem, O1 is what I'd use.

**NotebookLM 2** [00:00:00] Something like that, yeah. Although there is a trade off. O1 takes a lot more power to run, and it takes longer to get those impressive results.

**NotebookLM** [00:00:00] Hmm, makes sense. More power, more time, higher quality.

**NotebookLM 2** [00:00:00] Exactly.

**NotebookLM** [00:00:00] It sounds like it's still in development, though, right? Is there anything else they're planning to add to it?

**NotebookLM 2** [00:00:00] Oh, yeah. They mentioned system prompts, which will let developers, like, set some ground rules for how it behaves. And they're working on adding structured outputs and function calling.

**Alex Volkov** [00:00:00] Wait, structured outputs? Didn't we just talk about that? We

**NotebookLM 2** [00:00:00] did. That's the thing where the AI's output is formatted in a way that's easy to use.

**NotebookLM** [00:00:00] Right, right. So you don't have to spend all day trying to make sense of what it gives you. It's good that they're thinking about that stuff.

**NotebookLM 2** [00:00:00] It's about making these tools usable.

**NotebookLM 2** [00:00:00] And speaking of that, Dev Day finished up with this really interesting talk. Sam Altman, the CEO of OpenAI, And Kevin Weil, their new chief product officer. They talked about, like, the big picture for AI.

**NotebookLM** [00:00:00] Yeah, they did, didn't they? Anything interesting come up?

**NotebookLM 2** [00:00:00] Well, Altman talked about moving past this whole AGI term, Artificial General Intelligence.

**NotebookLM** [00:00:00] I can see why. It's kind of a loaded term, isn't it?

**NotebookLM 2** [00:00:00] He thinks it's become a bit of a buzzword, and people don't really understand what it means.

**NotebookLM** [00:00:00] So are they saying they're not trying to build AGI anymore?

**NotebookLM 2** [00:00:00] It's more like they're saying they're focused on just Making AI better, constantly improving it, not worrying about putting it in a box.

**NotebookLM** [00:00:00] That makes sense. Keep pushing the limits.

**NotebookLM 2** [00:00:00] Exactly. But they were also very clear about doing it responsibly. They talked a lot about safety and ethics.

**NotebookLM** [00:00:00] Yeah, that's important.

**NotebookLM 2** [00:00:00] They said they were going to be very careful. About how they release new features.

**NotebookLM** [00:00:00] Good! Because this stuff is powerful.

**NotebookLM 2** [00:00:00] It is. It was a lot to take in, this whole Dev Day event.

**NotebookLM 2** [00:00:00] New tools, big changes at OpenAI, and these big questions about the future of AI.

**NotebookLM** [00:00:00] It was. But hopefully this deep dive helped make sense of some of it. At least, that's what we try to do here.

**AI Charlie** [00:00:00] Absolutely.

**NotebookLM** [00:00:00] Thanks for taking the deep dive with us.

**AI Charlie** [00:00:00] The biggest demo of the new Realtime API involved function calling with voice mode and buying chocolate covered strawberries from our friendly local OpenAI developer experience engineer and strawberry shop owner, Ilan Biggio.

**AI Charlie** [00:00:00] We'll first play you the audio of his demo and then go into a little interview with him.

## [00:09:25] Ilan's Strawberry Demo with Realtime Voice Function Calling

**Romain Huet** [00:00:00] Could you place a call and see if you could get us 400 strawberries delivered to the venue? But please keep that under 1500. I'm on it. We'll get those strawberries delivered for you.

**Ilan** [00:00:00] Hello? Hi there. Is this Ilan? I'm Romain's AI assistant. How is it going? Fantastic. Can you tell me what flavors of strawberry dips you have for me? Yeah, we have chocolate, vanilla, and we have peanut butter. Wait, how much would 400 chocolate covered strawberries cost? 400? Are you sure you want 400? Yes, 400 chocolate covered

**Swyx** [00:00:00] strawberries.

**Ilan** [00:00:00] Wait,

**Swyx** [00:00:00] how much

**Ilan** [00:00:00] would that be? I think that'll be around, like, 1, 415. 92.

**Alex Volkov** [00:00:00] Awesome. Let's go ahead and place the order for four chocolate covered strawberries.

**Ilan** [00:00:00] Great, where would you like that delivered? Please deliver them to the Gateway Pavilion at Fort Mason. And I'll be paying in cash.

**Alex Volkov** [00:00:00] Okay,

**Ilan** [00:00:00] sweet. So just to confirm, you want four strawberries?

**Ilan** [00:00:00] 400 chocolate covered strawberries to the Gateway Pavilion. Yes, that's perfect. And when can we expect delivery? Well, you guys are right nearby, so it'll be like, I don't know, 37 seconds? That's incredibly fast. Cool, you too.

**Swyx** [00:00:00] Hi, Ilan, welcome to Lanespace. Oh, thank you. I just saw your amazing demos, had your amazing strawberries. You are dressed up, like, exactly like a strawberry salesman. Gotta have it all. What was the building on demo like? What was the story behind the demo?

**Swyx** [00:00:00] It was really interesting. This is actually something I had been thinking about for months before the launch.

**Swyx** [00:00:00] Like, having a, like, AI that can make phone calls is something like I've personally wanted for a long time. And so as soon as we launched internally, like, I started hacking on it. And then that sort of just started. We made it into like an internal demo, and then people found it really interesting, and then we thought how cool would it be to have this like on stage as, as one of the demos.

**Swyx** [00:00:00] Yeah, would would you call out any technical issues building, like you were basically one of the first people ever to build with a voice mode API. Would you call out any issues like integrating it with Twilio like that, like you did with function calling, with like a form filling elements. I noticed that you had like intents of things to fulfill, and then.

**Swyx** [00:00:00] When there's still missing info, the voice would prompt you, roleplaying the store guy.

**Swyx** [00:00:00] Yeah, yeah, so, I think technically, there's like the whole, just working with audio and streams is a whole different beast. Like, even separate from like AI and this, this like, new capabilities, it's just, it's just tough.

**Swyx** [00:00:00] Yeah, when you have a prompt, conversationally it'll just follow, like the, it was, Instead of like, kind of step by step to like ask the right questions based on like the like what the request was, right? The function calling itself is sort of tangential to that. Like, you have to prompt it to call the functions, but then handling it isn't too much different from, like, what you would do with assistant streaming or, like, chat completion streaming.

**Swyx** [00:00:00] I think, like, the API feels very similar just to, like, if everything in the API was streaming, it actually feels quite familiar to that.

**Swyx** [00:00:00] And then, function calling wise, I mean, does it work the same? I don't know. Like, I saw a lot of logs. You guys showed, like, in the playground, a lot of logs. What is in there?

**Swyx** [00:00:00] What should people know?

**Swyx** [00:00:00] Yeah, I mean, it is, like, the events may have different names than the streaming events that we have in chat completions, but they represent very similar things. It's things like, you know, function call started, argument started, it's like, here's like argument deltas, and then like function call done.

**Swyx** [00:00:00] Conveniently we send one that has the full function, and then I just use that. Nice.

**Swyx** [00:00:00] Yeah and then, like, what restrictions do, should people be aware of? Like, you know, I think, I think, before we recorded, we discussed a little bit about the sensitivities around basically calling random store owners and putting, putting like an AI on them.

**Swyx** [00:00:00] Yeah, so there's, I think there's recent regulation on that, which is why we want to be like very, I guess, aware of, of You know, you can't just call anybody with AI, right? That's like just robocalling. You wouldn't want someone just calling you with AI.

**Swyx** [00:00:00] I'm a developer, I'm about to do this on random people.

**Swyx** [00:00:00] What laws am I about to break?

**Swyx** [00:00:00] I forget what the governing body is, but you should, I think, Having consent of the person you're about to call, it always works. I, as the strawberry owner, have consented to like getting called with AI. I think past that you, you want to be careful. Definitely individuals are more sensitive than businesses.

**Swyx** [00:00:00] I think businesses you have a little bit more leeway. Also, they're like, businesses I think have an incentive to want to receive AI phone calls. Especially if like, they're dealing with it. It's doing business. Right, like, it's more business. It's kind of like getting on a booking platform, right, you're exposed to more.

**Swyx** [00:00:00] But, I think it's still very much like a gray area. Again, so. I think everybody should, you know, tread carefully, like, figure out what it is. I, I, I, the law is so recent, I didn't have enough time to, like, I'm also not a lawyer. Yeah, yeah, yeah, of course. Yeah.

**Swyx** [00:00:00] Okay, cool fair enough. One other thing, this is kind of agentic.

**Swyx** [00:00:00] Did you use a state machine at all? Did you use any framework? No. You just stick it in context and then just run it in a loop until it ends call?

**Swyx** [00:00:00] Yeah, there isn't even a loop, like Okay. Because the API is just based on sessions. It's always just going to keep going. Every time you speak, it'll trigger a call.

**Swyx** [00:00:00] And then after every function call was also invoked invoking like a generation. And so that is another difference here. It's like it's inherently almost like in a loop, be just by being in a session, right? No state machines needed. I'd say this is very similar to like, the notion of routines, where it's just like a list of steps.

**Swyx** [00:00:00] And it, like, sticks to them softly, but usually pretty well. And the steps is the prompts? The steps, it's like the prompt, like the steps are in the prompt. Yeah, yeah, yeah. Right, it's like step one, do this, step one, step two, do that. What if I want to change the system prompt halfway through the conversation?

**Swyx** [00:00:00] You can. Okay. You can. To be honest, I have not played without two too much. Yeah,

**Swyx** [00:00:00] yeah.

**Swyx** [00:00:00] But, I know you can.

**Swyx** [00:00:00] Yeah, yeah. Yeah. Awesome. I noticed that you called it real time API, but not voice API. Mm hmm. So I assume that it's like real time API starting with voice. Right, I think that's what he said on the thing.

**Swyx** [00:00:00] I can't imagine, like, what else is real

**Swyx** [00:00:00] time? Well, I guess, to use ChatGPT's voice mode as an example, Like, we've demoed the video, right? Like, real time image, right? So, I'm not actually sure what timelines are, But I would expect, if I had to guess, That, like, that is probably the next thing that we're gonna be making.

**Swyx** [00:00:00] You'd probably have to talk directly with the team building this. Sure. But, You can't promise their timelines. Yeah, yeah, yeah, right, exactly. But, like, given that this is the features that currently, Or that exists that we've demoed on Chachapiti. Yeah. There

**Swyx** [00:00:00] will never be a

**Swyx** [00:00:00] case where there's like a real time text API, right?

**Swyx** [00:00:00] I don't Well, this is a real time text API. You can do text only on this. Oh. Yeah. I don't know why you would. But it's actually So text to text here doesn't quite make a lot of sense. I don't think you'll get a lot of latency gain. But, like, speech to text is really interesting. Because you can prevent You can prevent responses, like audio responses.

**Swyx** [00:00:00] And force function calls. And so you can do stuff like UI control. That is like super super reliable. We had a lot of like, you know, un, like, we weren't sure how well this was gonna work because it's like, you have a voice answering. It's like a whole persona, right? Like, that's a little bit more, you know, risky.

**Swyx** [00:00:00] But if you, like, cut out the audio outputs and make it so it always has to output a function, like you can end up with pretty pretty good, like, Pretty reliable, like, command like a command architecture. Yeah,

**Swyx** [00:00:00] actually, that's the way I want to interact with a lot of these things as well. Like, one sided voice.

**Swyx** [00:00:00] Yeah, you don't necessarily want to hear the

**Swyx** [00:00:00] voice back. And like, sometimes it's like, yeah, I think having an output voice is great. But I feel like I don't always want to hear an output voice. I'd say usually I don't. But yeah, exactly, being able to speak to it is super sweet.

**Swyx** [00:00:00] Cool. Do you want to comment on any of the other stuff that you announced?

**Swyx** [00:00:00] From caching I noticed was like, I like the no code change part. I'm looking forward to the docs because I'm sure there's a lot of details on like, what you cache, how long you cache. Cause like, enthalpy caches were like 5 minutes. I was like, okay, but what if I don't make a call every 5 minutes?

**Swyx** [00:00:00] Yeah,

**Swyx** [00:00:00] to be super honest with you, I've been so caught up with the real time API and making the demo that I haven't read up on the other stuff. Launches too much. I mean, I'm aware of them, but I think I'm excited to see how all distillation works. That's something that we've been doing like, I don't know, I've been like doing it between our models for a while And I've seen really good results like I've done back in a day like from GPT 4 to GPT 3.

**Swyx** [00:00:00] 5 And got like, like pretty much the same level of like function calling with like hundreds of functions So that was super super compelling So, I feel like easier distillation, I'm really excited for. I see. Is it a tool?

**Swyx** [00:00:00] So, I saw evals. Yeah. Like, what is the distillation product? It wasn't super clear, to be honest.

**Swyx** [00:00:00] I, I think I want to, I want to let that team, I want to let that team talk about it. Okay,

**Swyx** [00:00:00] alright. Well, I appreciate you jumping on. Yeah, of course. Amazing demo. It was beautifully designed. I'm sure that was part of you and Roman, and

**Swyx** [00:00:00] Yeah, I guess, shout out to like, the first people to like, creators of Wanderlust, originally, were like, Simon and Carolis, and then like, I took it and built the voice component and the voice calling components.

**Swyx** [00:00:00] Yeah, so it's been a big team effort. And like the entire PI team for like Debugging everything as it's been going on. It's been, it's been so good working with them. Yeah, you're the first consumers on the DX

**Swyx** [00:00:00] team. Yeah. Yeah, I mean, the classic role of what we do there. Yeah. Okay, yeah, anything else? Any other call to action?

**Swyx** [00:00:00] No, enjoy Dev Day. Thank you. Yeah. That's it.

## [00:19:16] Olivier Godement, Head of Product, OpenAI

**AI Charlie** [00:00:00] The latent space crew then talked to Olivier Godmont, head of product for the OpenAI platform, who led the entire Dev Day keynote and introduced all the major new features and updates that we talked about today.

**Swyx** [00:00:00] Okay, so we are here with Olivier Godmont. That's right.

**Swyx** [00:00:00] I don't pronounce French. That's fine. It was perfect. And it was amazing to see your keynote today. What was the back story of, of preparing something like this? Preparing, like, Dev Day? It

**Olivier Godement** [00:00:00] essentially came from a couple of places. Number one, excellent reception from last year's Dev Day.

**Olivier Godement** [00:00:00] Developers, startup founders, researchers want to spend more time with OpenAI, and we want to spend more time with them as well. And so for us, like, it was a no brainer, frankly, to do it again, like, you know, like a nice conference. The second thing is going global. We've done a few events like in Paris and like a few other like, you know, non European, non American countries.

**Olivier Godement** [00:00:00] And so this year we're doing SF, Singapore, and London. To frankly just meet more developers.

**Swyx** [00:00:00] Yeah, I'm very excited for the Singapore one.

**Olivier Godement** [00:00:00] Ah,

**Swyx** [00:00:00] yeah. Will you be

**Olivier Godement** [00:00:00] there?

**Swyx** [00:00:00] I don't know. I don't know if I got an invite. No. I can't just talk to you. Yeah, like, and then there was some speculation around October 1st.

**Olivier Godement** [00:00:00] Yeah. Is it because

**Swyx** [00:00:00] 01, October 1st? It

**Olivier Godement** [00:00:00] has nothing to do. I discovered the tweet yesterday where like, people are so creative. No one, there was no connection to October 1st. But in hindsight, that would have been a pretty good meme by Tiana. Okay.

**Swyx** [00:00:00] Yeah, and you know, I think like, OpenAI's outreach to developers is something that I felt the whole in 2022, when like, you know, like, people were trying to build a chat GPT, and like, there was no function calling, all that stuff that you talked about in the past.

**Swyx** [00:00:00] And that's why I started my own conference as like like, here's our little developer conference thing. And, but to see this OpenAI Dev Day now, and like to see so many developer oriented products coming to OpenAI, I think it's really encouraging.

**Olivier Godement** [00:00:00] Yeah, totally. It's that's what I said, essentially, like, developers are basically the people who make the best connection between the technology and, you know, the future, essentially.

**Olivier Godement** [00:00:00] Like, you know, essentially see a capability, see a low level, like, technology, and are like, hey, I see how that application or that use case that can be enabled. And so, in the direction of enabling, like, AGI, like, all of humanity, it's a no brainer for us, like, frankly, to partner with Devs.

**Alessio** [00:00:00] And most importantly, you almost never had waitlists, which, compared to like other releases, people usually, usually have.

**Alessio** [00:00:00] What is the, you know, you had from caching, you had real time voice API, we, you know, Shawn did a long Twitter thread, so people know the releases. Yeah. What is the thing that was like sneakily the hardest to actually get ready for, for that day, or like, what was the kind of like, you know, last 24 hours, anything that you didn't know was gonna work?

**Olivier Godement** [00:00:00] Yeah. The old Fairly, like, I would say, involved, like, features to ship. So the team has been working for a month, all of them. The one which I would say is the newest for OpenAI is the real time API. For a couple of reasons. I mean, one, you know, it's a new modality. Second, like, it's the first time that we have an actual, like, WebSocket based API.

**Olivier Godement** [00:00:00] And so, I would say that's the one that required, like, the most work over the month. To get right from a developer perspective and to also make sure that our existing safety mitigation that worked well with like real time audio in and audio out.

**Swyx** [00:00:00] Yeah, what design choices or what was like the sort of design choices that you want to highlight?

**Swyx** [00:00:00] Like, you know, like I think for me, like, WebSockets, you just receive a bunch of events. It's two way. I obviously don't have a ton of experience. I think a lot of developers are going to have to embrace this real time programming. Like, what are you designing for, or like, what advice would you have for developers exploring this?

**Olivier Godement** [00:00:00] The core design hypothesis was essentially, how do we enable, like, human level latency? We did a bunch of tests, like, on average, like, human beings, like, you know, takes, like, something like 300 milliseconds to converse with each other. And so that was the design principle, essentially. Like, working backward from that, and, you know, making the technology work.

**Olivier Godement** [00:00:00] And so we evaluated a few options, and WebSockets was the one that we landed on. So that was, like, one design choice. A few other, like, big design choices that we had to make prompt caching. Prompt caching, the design, like, target was automated from the get go. Like, zero code change from the developer.

**Olivier Godement** [00:00:00] That way you don't have to learn, like, what is a prompt prefix, and, you know, how long does a cache work, like, we just do it as much as we can, essentially. So that was a big design choice as well. And then finally, on distillation, like, and evaluation. The big design choice was something I learned at Skype, like in my previous job, like a philosophy around, like, a pit of success.

**Olivier Godement** [00:00:00] Like, what is essentially the, the, the minimum number of steps for the majority of developers to do the right thing? Because when you do evals on fat tuning, there are many, many ways, like, to mess it up, frankly, like, you know, and have, like, a crappy model, like, evals that tell, like, a wrong story. And so our whole design was, okay, we actually care about, like, helping people who don't have, like, that much experience, like, evaluating a model, like, get, like, in a few minutes, like, to a good spot.

**Olivier Godement** [00:00:00] And so how do we essentially enable that bit of success, like, in the product flow?

**Swyx** [00:00:00] Yeah, yeah, I'm a little bit scared to fine tune especially for vision, because I don't know what I don't know for stuff like vision, right? Like, for text, I can evaluate pretty easily. For vision let's say I'm like trying to, one of your examples was grab.

**Swyx** [00:00:00] Which, very close to home, I'm from Singapore. I think your example was like, they identified stop signs better. Why is that hard? Why do I have to fine tune that? If I fine tune that, do I lose other things? You know, like, there's a lot of unknowns with Vision that I think developers have to figure out.

**Swyx** [00:00:00] For

**Olivier Godement** [00:00:00] sure. Vision is going to open up, like, a new, I would say, evaluation space. Because you're right, like, it's harder, like, you know, to tell correct from incorrect, essentially, with images. What I can say is we've been alpha testing, like, the Vision fine tuning, like, for several weeks at that point. We are seeing, like, even higher performance uplift compared to text fine tuning.

**Olivier Godement** [00:00:00] So that's, there is something here, like, we've been pretty impressed, like, in a good way, frankly. But, you know, how well it works. But for sure, like, you know, I expect the developers who are moving from one modality to, like, text and images will have, like, more, you know Testing, evaluation, like, you know, to set in place, like, to make sure it works well.

**Alessio** [00:00:00] The model distillation and evals is definitely, like, the most interesting. Moving away from just being a model provider to being a platform provider. How should people think about being the source of truth? Like, do you want OpenAI to be, like, the system of record of all the prompting? Because people sometimes store it in, like, different data sources.

**Alessio** [00:00:00] And then, is that going to be the same as the models evolve? So you don't have to worry about, you know, refactoring the data, like, things like that, or like future model structures.

**Olivier Godement** [00:00:00] The vision is if you want to be a source of truth, you have to earn it, right? Like, we're not going to force people, like, to pass us data.

**Olivier Godement** [00:00:00] There is no value prop, like, you know, for us to store the data. The vision here is at the moment, like, most developers, like, use like a one size fits all model, like be off the shelf, like GP40 essentially. The vision we have is fast forward a couple of years. I think, like, most developers will essentially, like, have a.

**Olivier Godement** [00:00:00] An automated, continuous, fine tuned model. The more, like, you use the model, the more data you pass to the model provider, like, the model is automatically, like, fine tuned, evaluated against some eval sets, and essentially, like, you don't have to every month, when there is a new snapshot, like, you know, to go online and, you know, try a few new things.

**Olivier Godement** [00:00:00] That's a direction. We are pretty far away from it. But I think, like, that evaluation and decision product are essentially a first good step in that direction. It's like, hey, it's you. I set it by that direction, and you give us the evaluation data. We can actually log your completion data and start to do some automation on your behalf.

**Alessio** [00:00:00] And then you can do evals for free if you share data with OpenAI. How should people think about when it's worth it, when it's not? Sometimes people get overly protective of their data when it's actually not that useful. But how should developers think about when it's right to do it, when not, or

**Olivier Godement** [00:00:00] if you have any thoughts on it?

**Olivier Godement** [00:00:00] The default policy is still the same, like, you know, we don't train on, like, any API data unless you opt in. What we've seen from feedback is evaluation can be expensive. Like, if you run, like, O1 evals on, like, thousands of samples Like, your build will get increased, like, you know, pretty pretty significantly.

**Olivier Godement** [00:00:00] That's problem statement number one. Problem statement number two is, essentially, I want to get to a world where whenever OpenAI ships a new model snapshot, we have full confidence that there is no regression for the task that developers care about. And for that to be the case, essentially, we need to get evals.

**Olivier Godement** [00:00:00] And so that, essentially, is a sort of a two bugs one stone. It's like, we subsidize, basically, the evals. And we also use the evals when we ship new models to make sure that we keep going in the right direction. So, in my sense, it's a win win, but again, completely opt in. I expect that many developers will not want to share their data, and that's perfectly fine to me.

**Swyx** [00:00:00] Yeah, I think free evals though, very, very good incentive. I mean, it's a fair trade. You get data, we get free evals. Exactly,

**Olivier Godement** [00:00:00] and we sanitize PII, everything. We have no interest in the actual sensitive data. We just want to have good evaluation on the real use cases.

**Swyx** [00:00:00] Like, I always want to eval the eval. I don't know if that ever came up.

**Swyx** [00:00:00] Like, sometimes the evals themselves are wrong, and there's no way for me to tell you.

**Olivier Godement** [00:00:00] Everyone who is starting with LLM, teaching with LLM, is like, Yeah, evaluation, easy, you know, I've done testing, like, all my life. And then you start to actually be able to eval, understand, like, all the corner cases, And you realize, wow, there's like a whole field in itself.

**Olivier Godement** [00:00:00] So, yeah, good evaluation is hard and so, yeah. Yeah, yeah.

**Swyx** [00:00:00] But I think there's a, you know, I just talked to Brain Trust which I think is one of your partners. Mm-Hmm. . They also emphasize code based evals versus your sort of low code. What I see is like, I don't know, maybe there's some more that you didn't demo.

**Swyx** [00:00:00] YC is kind of like a low code experience, right, for evals. Would you ever support like a more code based, like, would I run code on OpenAI's eval platform?

**Olivier Godement** [00:00:00] For sure. I mean, we meet developers where they are, you know. At the moment, the demand was more for like, you know, easy to get started, like eval. But, you know, if we need to expose like an evaluation API, for instance, for people like, you know, to pass, like, you know, their existing test data we'll do it.

**Olivier Godement** [00:00:00] So yeah, there is no, you know, philosophical, I would say, like, you know, misalignment on that. Yeah,

**Swyx** [00:00:00] yeah, yeah. What I think this is becoming, by the way, and I don't, like it's basically, like, you're becoming AWS. Like, the AI cloud. And I don't know if, like, that's a conscious strategy, or it's, like, It doesn't even have to be a conscious strategy.

**Swyx** [00:00:00] Like, you're going to offer storage. You're going to offer compute. You're going to offer networking. I don't know what networking looks like. Networking is maybe, like, Caching or like it's a CDN. It's a prompt CDN.

**Alex Volkov** [00:00:00] Yeah,

**Swyx** [00:00:00] but it's the AI versions of everything, right? Do you like do you see the analogies or?

**Olivier Godement** [00:00:00] Whatever Whatever I took to developers. I feel like Good models are just half of the story to build a good app There's a third model you need to do Evaluation is the perfect example. Like, you know, you can have the best model in the world If you're in the dark, like, you know, it's really hard to gain the confidence and so Our philosophy is

**Olivier Godement** [00:00:00] The whole like software development stack is being basically reinvented, you know, with LLMs. There is no freaking way that open AI can build everything. Like there is just too much to build, frankly. And so my philosophy is, essentially, we'll focus on like the tools which are like the closest to the model itself.

**Olivier Godement** [00:00:00] So that's why you see us like, you know, investing quite a bit in like fine tuning, distillation, our evaluation, because we think that it actually makes sense to have like in one spot, Like, you know, all of that. Like, there is some sort of virtual circle, essentially, that you can set in place. But stuff like, you know, LLMOps, like tools which are, like, further away from the model, I don't know if you want to do, like, you know, super elaborate, like, prompt management, or, you know, like, tooling, like, I'm not sure, like, you know, OpenAI has, like, such a big edge, frankly, like, you know, to build this sort of tools.

**Olivier Godement** [00:00:00] So that's how we view it at the moment. But again, frankly, the philosophy is super simple. The strategy is super simple. It's meeting developers where they want us to be. And so, you know that's frankly, like, you know, day in, day out, like, you know, what I try to do.

**Alessio** [00:00:00] Cool. Thank you so much for the time.

**Alessio** [00:00:00] I'm sure you,

**Swyx** [00:00:00] Yeah, I have more questions on, a couple questions on voice, and then also, like, your call to action, like, what you want feedback on, right? So, I think we should spend a bit more time on voice, because I feel like that's, like, the big splash thing. I talked well Well, I mean, I mean, just what is the future of real time for OpenAI?

**Swyx** [00:00:00] Yeah. Because I think obviously video is next. You already have it in the, the ChatGPT desktop app. Do we just have a permanent, like, you know, like, are developers just going to be, like, sending sockets back and forth with OpenAI? Like how do we program for that? Like, what what is the future?

**Olivier Godement** [00:00:00] Yeah, that makes sense. I think with multimodality, like, real time is quickly becoming, like, you know, essentially the right experience, like, to build an application. Yeah. So my expectation is that we'll see like a non trivial, like a volume of applications like moving to a real time API. Like if you zoom out, like, audio is really simple, like, audio until basically now.

**Olivier Godement** [00:00:00] Audio on the web, in apps, was basically very much like a second class citizen. Like, you basically did like an audio chatbot for users who did not have a choice. You know, they were like struggling to read, or I don't know, they were like not super educated with technology. And so, frankly, it was like the crappy option, you know, compared to text.

**Olivier Godement** [00:00:00] But when you talk to people in the real world, the vast majority of people, like, prefer to talk and listen instead of typing and writing.

**Swyx** [00:00:00] We speak before we write.

**Olivier Godement** [00:00:00] Exactly. I don't know. I mean, I'm sure it's the case for you in Singapore. For me, my friends in Europe, the number of, like, WhatsApp, like, voice notes they receive every day, I mean, just people, it makes sense, frankly, like, you know.

**Olivier Godement** [00:00:00] Chinese. Chinese, yeah.

**Swyx** [00:00:00] Yeah,

**Olivier Godement** [00:00:00] all voice. You know, it's easier. There is more emotions. I mean, you know, you get the point across, like, pretty well. And so my personal ambition for, like, the real time API and, like, audio in general is to make, like, audio and, like, multimodality, like, truly a first class experience.

**Olivier Godement** [00:00:00] Like, you know, if you're, like, you know, the amazing, like, super bold, like, start up out of YC, you want to build, like, the next, like, billion, like, you know, user application to make it, like, truly your first and make it feel, like, you know, an actual good, like, you know, product experience. So that's essentially the ambition, and I think, like, yeah, it could be pretty big.

**Swyx** [00:00:00] Yeah. I think one, one people, one issue that people have with the voice so far as, as released in advanced voice mode is the refusals.

**Alex Volkov** [00:00:00] Yeah.

**Swyx** [00:00:00] You guys had a very inspiring model spec. I think Joanne worked on that. Where you said, like, yeah, we don't want to overly refuse all the time. In fact, like, even if, like, not safe for work, like, in some occasions, it's okay.

**Swyx** [00:00:00] How, is there an API that we can say, not safe for work, okay?

**Olivier Godement** [00:00:00] I think we'll get there. I think we'll get there. The mobile spec, like, nailed it, like, you know. It nailed it! It's so good! Yeah, we are not in the business of, like, policing, you know, if you can say, like, vulgar words or whatever. You know, there are some use cases, like, you know, I'm writing, like, a Hollywood, like, script I want to say, like, will go on, and it's perfectly fine, you know?

**Olivier Godement** [00:00:00] And so I think the direction where we'll go here is that basically There will always be like, you know, a set of behavior that we will, you know, just like forbid, frankly, because they're illegal against our terms of services. But then there will be like, you know, some more like risky, like themes, which are completely legal, like, you know, vulgar words or, you know, not safe for work stuff.

**Olivier Godement** [00:00:00] Where basically we'll expose like a controllable, like safety, like knobs in the API to basically allow you to say, hey, that theme okay, that theme not okay. How sensitive do you want the threshold to be on safety refusals? I think that's the Dijkstra. So a

**Swyx** [00:00:00] safety API.

**Olivier Godement** [00:00:00] Yeah, in a way, yeah.

**Swyx** [00:00:00] Yeah, we've never had that.

**Olivier Godement** [00:00:00] Yeah. '

**Swyx** [00:00:00] cause right now is you, it is whatever you decide. And then it's, that's it. That, that, that would be the main reason I don't use opening a voice is because of

**Olivier Godement** [00:00:00] it's over police. Over refuse over refusals. Yeah. Yeah, yeah. No, we gotta fix that. Yeah. Like singing,

**Alessio** [00:00:00] we're trying to do voice. I'm a singer.

**Swyx** [00:00:00] And you, you locked off singing.

**Swyx** [00:00:00] Yeah,

**Alessio** [00:00:00] yeah, yeah.

**Swyx** [00:00:00] But I, I understand music gets you in trouble. Okay. Yeah. So then, and then just generally, like, what do you want to hear from developers? Right? We have, we have all developers watching you know, what feedback do you want? Any, anything specific as well, like from, especially from today anything that you are unsure about, that you are like, Our feedback could really help you decide.

**Swyx** [00:00:00] For sure.

**Olivier Godement** [00:00:00] I think, essentially, it's becoming pretty clear after today that, you know, I would say the open end direction has become pretty clear, like, you know, after today. Investment in reasoning, investment in multimodality, Investment as well, like in, I would say, tool use, like function calling. To me, the biggest question I have is, you know, Where should we put the cursor next?

**Olivier Godement** [00:00:00] I think we need all three of them, frankly, like, you know, so we'll keep pushing.

**Swyx** [00:00:00] Hire 10, 000 people, or actually, no need, build a bunch of bots.

**Olivier Godement** [00:00:00] Exactly, and so let's take O1 smart enough, like, for your problems? Like, you know, let's set aside for a second the existing models, like, for the apps that you would love to build, is O1 basically it in reasoning, or do we still have, like, you know, a step to do?

**Olivier Godement** [00:00:00] Preview is not enough, I

**Swyx** [00:00:00] need the full one.

**Olivier Godement** [00:00:00] Yeah, so that's exactly that sort of feedback. Essentially what they would love to do is for developers I mean, there's a thing that Sam has been saying like over and over again, like, you know, it's easier said than done, but I think it's directionally correct. As a developer, as a founder, you basically want to build an app which is a bit too difficult for the model today, right?

**Olivier Godement** [00:00:00] Like, what you think is right, it's like, sort of working, sometimes not working. And that way, you know, that basically gives us like a goalpost, and be like, okay, that's what you need to enable with the next model release, like in a few months. And so I would say that Usually, like, that's the sort of feedback which is like the most useful that I can, like, directly, like, you know, incorporate.

**Swyx** [00:00:00] Awesome. I think that's our time. Thank you so much, guys. Yeah, thank you so much.

**AI Charlie** [00:00:00] Thank you. We were particularly impressed that Olivier addressed the not safe for work moderation policy question head on, as that had only previously been picked up on in Reddit forums. This is an encouraging sign that we will return to in the closing candor with Sam Altman at the end of this episode.

## [00:36:57] Romain Huet, Head of DX, OpenAI

**AI Charlie** [00:00:00] Next, a chat with Roman Hewitt, friend of the pod, AI Engineer World's fair closing keynote speaker, and head of developer experience at OpenAI on his incredible live demos And advice to AI engineers on all the new modalities.

**Alessio** [00:00:00] Alright, we're live from OpenAI Dev Day. We're with Juan, who just did two great demos on, on stage.

**Alessio** [00:00:00] And he's been a friend of Latentspace, so thanks for taking some of the time.

**Romain Huet** [00:00:00] Of course, yeah, thank you for being here and spending the time with us today.

**Swyx** [00:00:00] Yeah, I appreciate appreciate you guys putting this on. I, I know it's like extra work, but it really shows the developers that you're, Care and about reaching out.

**Romain Huet** [00:00:00] Yeah, of course, I think when you go back to the OpenAI mission, I think for us it's super important that we have the developers involved in everything we do. Making sure that you know, they have all of the tools they need to build successful apps. And we really believe that the developers are always going to invent the ideas, the prototypes, the fun factors of AI that we can't build ourselves.

**Romain Huet** [00:00:00] So it's really cool to have everyone here.

**Swyx** [00:00:00] We had Michelle from you guys on. Yes, great episode. She very seriously said API is the path to AGI. Correct. And people in our YouTube comments were like, API is not AGI. I'm like, no, she's very serious. API is the path to AGI. Like, you're not going to build everything like the developers are, right?

**Swyx** [00:00:00] Of

**Romain Huet** [00:00:00] course, yeah, that's the whole value of having a platform and an ecosystem of amazing builders who can, like, in turn, create all of these apps. I'm sure we talked about this before, but there's now more than 3 million developers building on OpenAI, so it's pretty exciting to see all of that energy into creating new things.

**Alessio** [00:00:00] I was going to say, you built two apps on stage today, an international space station tracker and then a drone. The hardest thing must have been opening Xcode and setting that up. Now, like, the models are so good that they can do everything else. Yes. You had two modes of interaction. You had kind of like a GPT app to get the plan with one, and then you had a cursor to do apply some of the changes.

**Alessio** [00:00:00] Correct. How should people think about the best way to consume the coding models, especially both for You know, brand new projects and then existing projects that you're trying to modify.

**Romain Huet** [00:00:00] Yeah. I mean, one of the things that's really cool about O1 Preview and O1 Mini being available in the API is that you can use it in your favorite tools like cursor like I did, right?

**Romain Huet** [00:00:00] And that's also what like Devin from Cognition can use in their own software engineering agents. In the case of Xcode, like, it's not quite deeply integrated in Xcode, so that's why I had like chat GPT side by side. But it's cool, right, because I could instruct O1 Preview to be, like, my coding partner and brainstorming partner for this app, but also consolidate all of the, the files and architect the app the way I wanted.

**Romain Huet** [00:00:00] So, all I had to do was just, like, port the code over to Xcode and zero shot the app build. I don't think I conveyed, by the way, how big a deal that is, but, like, you can now create an iPhone app from scratch, describing a lot of intricate details that you want, and your vision comes to life in, like, a minute.

**Romain Huet** [00:00:00] It's pretty outstanding.

**Swyx** [00:00:00] I have to admit, I was a bit skeptical because if I open up SQL, I don't know anything about iOS programming. You know which file to paste it in. You probably set it up a little bit. So I'm like, I have to go home and test it. And I need the ChatGPT desktop app so that it can tell me where to click.

**Romain Huet** [00:00:00] Yeah, I mean like, Xcode and iOS development has become easier over the years since they introduced Swift and SwiftUI. I think back in the days of Objective C, or like, you know, the storyboard, it was a bit harder to get in for someone new. But now with Swift and SwiftUI, their dev tools are really exceptional.

**Romain Huet** [00:00:00] But now when you combine that with O1, as your brainstorming and coding partner, it's like your architect, effectively. That's the best way, I think, to describe O1. People ask me, like, can GPT 4 do some of that? And it certainly can. But I think it will just start spitting out code, right? And I think what's great about O1, is that it can, like, make up a plan.

**Romain Huet** [00:00:00] In this case, for instance, the iOS app had to fetch data from an API, it had to look at the docs, it had to look at, like, how do I parse this JSON, where do I store this thing, and kind of wire things up together. So that's where it really shines. Is mini or preview the better model that people should be using?

**Romain Huet** [00:00:00] Like, how? I think people should try both. We're obviously very excited about the upcoming O1 that we shared the evals for. But we noticed that O1 Mini is very, very good at everything math, coding, everything STEM. If you need for your kind of brainstorming or your kind of science part, you need some broader knowledge than reaching for O1 previews better.

**Romain Huet** [00:00:00] But yeah, I used O1 Mini for my second demo. And it worked perfectly. All I needed was very much like something rooted in code, architecting and wiring up like a front end, a backend, some UDP packets, some web sockets, something very specific. And it did that perfectly.

**Swyx** [00:00:00] And then maybe just talking about voice and Wanderlust, the app that keeps on giving, what's the backstory behind like preparing for all of that?

**Romain Huet** [00:00:00] You know, it's funny because when last year for Dev Day, we were trying to think about what could be a great demo app to show like an assistive experience. I've always thought travel is a kind of a great use case because you have, like, pictures, you have locations, you have the need for translations, potentially.

**Romain Huet** [00:00:00] There's like so many use cases that are bounded to travel that I thought last year, let's use a travel app. And that's how Wanderlust came to be. But of course, a year ago, all we had was a text based assistant. And now we thought, well, if there's a voice modality, what if we just bring this app back as a wink.

**Romain Huet** [00:00:00] And what if we were interacting better with voice? And so with this new demo, what I showed was the ability to like, So, we wanted to have a complete conversation in real time with the app, but also the thing we wanted to highlight was the ability to call tools and functions, right? So, like in this case, we placed a phone call using the Twilio API, interfacing with our AI agents, but developers are so smart that they'll come up with so many great ideas that we could not think of ourselves, right?

**Romain Huet** [00:00:00] But what if you could have like a, you know, a 911 dispatcher? What if you could have like a customer service? Like center, that is much smarter than what we've been used to today. There's gonna be so many use cases for real time, it's awesome.

**Swyx** [00:00:00] Yeah, and sometimes actually you, you, like this should kill phone trees.

**Swyx** [00:00:00] Like there should not be like dial one

**Romain Huet** [00:00:00] of course para

**Swyx** [00:00:00] espanol, you know? Yeah, exactly. Or whatever. I dunno.

**Romain Huet** [00:00:00] I mean, even you starting speaking Spanish would just do the thing, you know you don't even have to ask. So yeah, I'm excited for this future where we don't have to interact with those legacy systems.

**Swyx** [00:00:00] Yeah. Yeah. Is there anything, so you are doing function calling in a streaming environment. So basically it's, it's web sockets. It's UDP, I think. It's basically not guaranteed to be exactly once delivery. Like, is there any coding challenges that you encountered when building this?

**Romain Huet** [00:00:00] Yeah, it's a bit more delicate to get into it.

**Romain Huet** [00:00:00] We also think that for now, what we, what we shipped is a, is a beta of this API. I think there's much more to build onto it. It does have the function calling and the tools. But we think that for instance, if you want to have something very robust, On your client side, maybe you want to have web RTC as a client, right?

**Romain Huet** [00:00:00] And, and as opposed to like directly working with the sockets at scale. So that's why we have partners like Life Kit and Agora if you want to, if you want to use them. And I'm sure we'll have many mores in the, in many more in the future. But yeah, we keep on iterating on that, and I'm sure the feedback of developers in the weeks to come is going to be super critical for us to get it right.

**Swyx** [00:00:00] Yeah, I think LiveKit has been fairly public that they are used in, in the Chachapiti app. Like, is it, it's just all open source, and we just use it directly with OpenAI, or do we use LiveKit Cloud or something?

**Romain Huet** [00:00:00] So right now we, we released the API, we released some sample code also, and referenced clients for people to get started with our API.

**Romain Huet** [00:00:00] And we also partnered with LifeKit and Agora, so they also have their own, like ways to help you get started that plugs natively with the real time API. So depending on the use case, people can, can can decide what to use. If you're working on something that's completely client or if you're working on something on the server side, for the voice interaction, you may have different needs, so we want to support all of those.

**Alessio** [00:00:00] I know you gotta run. Is there anything that you want the AI engineering community to give feedback on specifically, like even down to like, you know, a specific API end point or like, what, what's like the thing that you want? Yeah. I

**Romain Huet** [00:00:00] mean, you know, if we take a step back, I think dev Day this year is all different from last year and, and in, in a few different ways.

**Romain Huet** [00:00:00] But one way is that we wanted to keep it intimate, even more intimate than last year. We wanted to make sure that the community is. Thank you very much for joining us on the Spotlight. That's why we have community talks and everything. And the takeaway here is like learning from the very best developers and AI engineers.

**Romain Huet** [00:00:00] And so, you know we want to learn from them. Most of what we shipped this morning, including things like prompt caching the ability to generate prompts quickly in the playground, or even things like vision fine tuning. These are all things that developers have been asking of us. And so, the takeaway I would, I would leave them with is to say like, Hey, the roadmap that we're working on is heavily influenced by them and their work.

**Romain Huet** [00:00:00] And so we love feedback From high feature requests, as you say, down to, like, very intricate details of an API endpoint, we love feedback, so yes that's, that's how we, that's how we build this API.

**Swyx** [00:00:00] Yeah, I think the, the model distillation thing as well, it might be, like, the, the most boring, but, like, actually used a lot.

**Romain Huet** [00:00:00] True, yeah. And I think maybe the most unexpected, right, because I think if I, if I read Twitter correctly the past few days, a lot of people were expecting us. To shape the real time API for speech to speech. I don't think developers were expecting us to have more tools for distillation, and we really think that's gonna be a big deal, right?

**Romain Huet** [00:00:00] If you're building apps that have you know, you, you want high, like like low latency, low cost, but high performance, high quality on the use case distillation is gonna be amazing.

**Swyx** [00:00:00] Yeah. I sat in the distillation session just now and they showed how they distilled from four oh to four mini and it was like only like a 2% hit in the performance and 50 next.

**Swyx** [00:00:00] Yeah,

**Romain Huet** [00:00:00] I was there as well for the superhuman kind of use case inspired for an Ebola client. Yeah, this was really good. Cool man! so much for having me. Thanks again for being here today. It's always

**AI Charlie** [00:00:00] great to have you. As you might have picked up at the end of that chat, there were many sessions throughout the day focused on specific new capabilities.

## [00:47:08] Michelle Pokrass, Head of API at OpenAI ft. Simon Willison

**AI Charlie** [00:00:00] Like the new model distillation features combining EVOLs and fine tuning. For our next session, we are delighted to bring back two former guests of the pod, which is something listeners have been greatly enjoying in our second year of doing the Latent Space podcast. Michelle Pokras of the API team joined us recently to talk about structured outputs, and today gave an updated long form session at Dev Day, describing the implementation details of the new structured output mode.

**AI Charlie** [00:00:00] We also got her updated thoughts on the VoiceMode API we discussed in her episode, now that it is finally announced. She is joined by friend of the pod and super blogger, Simon Willison, who also came back as guest co host in our Dev Day. 2023 episode.

**Alessio** [00:00:00] Great, we're back live at Dev Day returning guest Michelle and then returning guest co host Fork.

**Alessio** [00:00:00] Fork, yeah, I don't know. I've lost count. I think it's been a few. Simon Willison is back. Yeah, we just wrapped, we just wrapped everything up. Congrats on, on getting everything everything live. Simon did a great, like, blog, so if you haven't caught up, I

**Simon Willison** [00:00:00] wrote my, I implemented it. Now, I'm starting my live blog while waiting for the first talk to start, using like GPT 4, I wrote me the Javascript, and I got that live just in time and then, yeah, I was live blogging the whole day.

**Swyx** [00:00:00] Are you a cursor enjoyer?

**Simon Willison** [00:00:00] I haven't really gotten into cursor yet to be honest. I just haven't spent enough time for it to click, I think. I'm more a copy and paste things out of Cloud and chat GPT. Yeah. It's interesting.

**Swyx** [00:00:00] Yeah. I've converted to cursor and 01 is so easy to just toggle on and off.

**Alessio** [00:00:00] What's your workflow?

**Alessio** [00:00:00] VS

**Michelle Pokrass** [00:00:00] Code co pilot, so Yep, same here. Team co pilot. Co pilot is actually the reason I joined OpenAI. It was, you know, before ChatGPT, this is the thing that really got me. So I'm still into it, but I keep meaning to try out Cursor, and I think now that things have calmed down, I'm gonna give it a real go.

**Swyx** [00:00:00] Yeah, it's a big thing to change your tool of choice.

**Swyx** [00:00:00] Yes,

**Michelle Pokrass** [00:00:00] yeah, I'm pretty dialed, so.

**Swyx** [00:00:00] I mean, you know, if you want, you can just fork VS Code and make your own. That's the thing to dumb thing, right? We joked about doing a hackathon where the only thing you do is fork VS Code and bet me the best fork win.

**Michelle Pokrass** [00:00:00] Nice.

**Swyx** [00:00:00] That's actually a really good idea. Yeah, what's up?

**Swyx** [00:00:00] I mean, congrats on launching everything today. I know, like, we touched on it a little bit, but, like, everyone was kind of guessing that Voice API was coming, and, like, we talked about it in our episode. How do you feel going into the launch? Like, any design decisions that you want to highlight?

**Michelle Pokrass** [00:00:00] Yeah, super jazzed about it. The team has been working on it for a while. It's, like, a very different API for us. It's the first WebSocket API, so a lot of different design decisions to be made. It's, like, what kind of events do you send? When do you send an event? What are the event names? What do you send, like, on connection versus on future messages?

**Michelle Pokrass** [00:00:00] So there have been a lot of interesting decisions there. The team has also hacked together really cool projects as we've been testing it. One that I really liked is we had an internal hack a thon for the API team. And some folks built like a little hack that you could use to, like VIM with voice mode, so like, control vim, and you would tell them on like, nice, write a file and it would, you know, know all the vim commands and, and pipe those in.

**Michelle Pokrass** [00:00:00] So yeah, a lot of cool stuff we've been hacking on and really excited to see what people build with it.

**Simon Willison** [00:00:00] I've gotta call out a demo from today. I think it was Katja had a 3D visualization of the solar system, like WebGL solar system, you could talk to. That is one of the coolest conference demos I've ever seen.

**Simon Willison** [00:00:00] That was so convincing. I really want the code. I really want the code for that to get put out there. I'll talk

**Michelle Pokrass** [00:00:00] to the team. I think we can

**Simon Willison** [00:00:00] probably set it up. Absolutely beautiful example. And it made me realize that The Realtime API, this WebSocket API, it means that building a website that you can just talk to is easy now.

**Simon Willison** [00:00:00] It's like, it's not difficult to build, spin up a web app where you have a conversation with it, it calls functions for different things, it interacts with what's on the screen. I'm so excited about that. There are all of these projects I thought I'd never get to, and now I'm like, you know what? Spend a weekend on it.

**Simon Willison** [00:00:00] I could have a talk to your data, talk to your database. With a web, with a, with a little web application. Yeah. That's so

**Michelle Pokrass** [00:00:00] cool. Chat with PDF, but really chat with, really chat with pdf. No, completely.

**Simon Willison** [00:00:00] Totally. And that's not even hard to build. That's the crazy thing about this.

**Michelle Pokrass** [00:00:00] Yeah. Very cool. Yeah, when I first saw the space demo, I was actually just wowed and I, and I had a similar moment I think to all the people in the crowd.

**Michelle Pokrass** [00:00:00] I also thought Romain's drone demo was super cool. That was a super

**Simon Willison** [00:00:00] fun one as well. Yeah, I

**Michelle Pokrass** [00:00:00] actually saw that live this morning, and I was holding my breath for sure.

**Swyx** [00:00:00] Knowing Romain, he probably spent the last two days working on it. But yeah, like, I'm curious about you were talking with Romain actually earlier about what the different levels of extraction are with WebSockets.

**Swyx** [00:00:00] It's something that most developers have zero experience with. I have zero experience with it. Apparently there's like, the RTC level, and then there's the WebSocket level, and there's like, levels in between.

**Simon Willison** [00:00:00] Not so much. I mean, with WebSockets with the way they've built their API, you can connect directly to the OpenAI WebSocket from your browser.

**Simon Willison** [00:00:00] And it's actually just regular JavaScript. Like, you instantiate the WebSocket thing. It looks quite easy from their example code. The problem is that if you do that, you're sending your API key. From like, source code that anyone can view. Yeah, we

**Michelle Pokrass** [00:00:00] don't recommend that for production.

**Simon Willison** [00:00:00] So it doesn't work for production, which is frustrating, because it means that you have to build a proxy.

**Simon Willison** [00:00:00] So I'm going to have to go home and build myself a little WebSocket proxy just to hide my API key. I want OpenAI to do that. I want OpenAI to solve that problem for me, so I don't have to build the 1000th WebSocket proxy just for that one problem. Totally.

**Michelle Pokrass** [00:00:00] We've also partnered with some some partner solutions.

**Michelle Pokrass** [00:00:00] We've partnered with, I think, Agora. LiveKit a few others. So there's some loose solutions there, but yeah, we hear you. It's a beta.

**Swyx** [00:00:00] Yeah, yeah, I mean You still want a solution where someone brings their own key, And they can trust that you

**Simon Willison** [00:00:00] don't get it.

**Swyx** [00:00:00] Right?

**Simon Willison** [00:00:00] Kind of. I mean, I've been building a lot of bring your own key apps, Where it's my HTML and JavaScript, I store the key in local storage in their browser, And it never goes anywhere near my server.

**Simon Willison** [00:00:00] Which works, but how do they trust me? How do they know I'm not gonna ship another piece of javascript that steals the key from them? And so, nominally, this actually

**Swyx** [00:00:00] comes with the crypto background. This is what MetaMask does. Where Yeah, it's a

**Michelle Pokrass** [00:00:00] public private key thing. Yeah. Yeah.

**Swyx** [00:00:00] Like, why doesn't OpenAI do that?

**Swyx** [00:00:00] I don't know if, obviously it's

**Michelle Pokrass** [00:00:00] I mean, as with most things, I think there's, like, some really interesting questions. And the answer is just, you know, it's not been the top priority and it's hard for a small team to do everything. I have been hearing a lot more about the need for things like sign in with OpenAI.

**Simon Willison** [00:00:00] I want OAuth. I want to bounce my users through chat GPT and I get back a token that lets me spend up to 4 on the API on their behalf. Then I could ship all of my stupid little experiments, which currently require people to copy and paste their API key in, which cuts off everyone. Nobody knows how to do that.

**Michelle Pokrass** [00:00:00] Totally, I hear you. Something we're thinking about, and yeah, stay tuned.

**Swyx** [00:00:00] Yeah, yeah right now, I think the only player in town is OpenRouter that is basically, it's funny, it was made by I forget his name but he used to be CTO of OpenSea, and the first thing he did when he came over was build Metamask for AI.

**Michelle Pokrass** [00:00:00] Totally. Yeah, very cool.

**Alessio** [00:00:00] What's the most underrated release from today?

**Michelle Pokrass** [00:00:00] Vision Fine Tuning. Vision Fine Tuning is so underrated. For the past, like, two months, whenever I talk to founders, they tell me this is the thing they need most. A lot of people are doing, like, OCR on very bespoke formats, like government documents, and Vision Fine Tuning can help a lot with that use case.

**Michelle Pokrass** [00:00:00] Also, bounding boxes. People have found, like, a lot of improvements for bounding boxes with Visionfine Tuning. So yeah, I think it's pretty slept on and people should try it. You only really need 100 images to get going.

**Simon Willison** [00:00:00] Tell me more about bounding boxes. I didn't think that GPT 4 Vision could do bounding boxes at all.

**Michelle Pokrass** [00:00:00] Yeah, it's actually not that amazing at it, we're working on it, but with fine tuning, you can make it really good for your use case.

**Simon Willison** [00:00:00] That's cool, because I've been using Google Gemini's bounding block stuff recently, it's very, very impressive.

**Michelle Pokrass** [00:00:00] Yeah, totally. But

**Simon Willison** [00:00:00] being able to fine tune a model for that. The first thing I'm going to do with fine tuning for images is, I've got fine tuning.

**Simon Willison** [00:00:00] And I'm going to fine tune a model that can tell which chicken is which. Which is hard because three of them are grey. So there's a little bit of Okay, this is

**Michelle Pokrass** [00:00:00] my new favourite use case. Yeah, it's

**Simon Willison** [00:00:00] I've managed to do it with prompting. Just like, I gave Claude Pictures of all of the chickens and then said, okay, which chicken is this?

**Michelle Pokrass** [00:00:00] Yeah,

**Simon Willison** [00:00:00] but it's not quite good enough because it confuses the great chicken. Listen,

**Michelle Pokrass** [00:00:00] we can close that eval gap. Yeah That's it's

**Simon Willison** [00:00:00] gonna be a great eval. My chicken eval is gonna be fantastic.

**Michelle Pokrass** [00:00:00] I'm also really jazzed about the evals product It's kind of like a sub launch of the distillation thing But people have been struggling to make evals and the first time I saw the flow with how easy it is to make an eval And in our product, I was just blown away so I recommend people really try that.

**Michelle Pokrass** [00:00:00] I think that's what's holding a lot of people back from really investing in AI, because they just have a hard time figuring out if it's going well for their use case. So we've been working on making it easier to do that.

**Alessio** [00:00:00] Does the eval product include structured output testing? Like, function calling and things?

**Alessio** [00:00:00] Yeah, you can

**Michelle Pokrass** [00:00:00] check if it matches your JSON schema yeah.

**Swyx** [00:00:00] I mean, we have guaranteed structured output anyway, right? Well, but So we don't have to test it. Well,

**Michelle Pokrass** [00:00:00] not the schema, but like the See, these seem easy to tell apart. I think so. So I might call them a function,

**Alessio** [00:00:00] or Oh, I see. You're gonna write schema, wrong output.

**Alessio** [00:00:00] So you can do function

**Swyx** [00:00:00] calling testing. Right.

**Michelle Pokrass** [00:00:00] I'm pretty sure. I'll have to check that for you, but I think

**Alessio** [00:00:00] so. Yeah, yeah, yeah. We'll make sure it's sent

**Swyx** [00:00:00] out.

**Alessio** [00:00:00] How do you think about the evolution of, like, the API design? I think to me that's, like, the most important thing, so even with the OpenAI levels, like, chatbots, I can understand what the API design looks like. Reasoning, I can kind of understand it, even though, like, train of thought kind of changes things.

**Alessio** [00:00:00] As you think about real time voice, and then you think about agents, it's like, how do you think about how you design the API, and, like, what the shape of it is?

**Michelle Pokrass** [00:00:00] Yeah, so I think we're starting with the lowest level capabilities. And then we build on top of that, as we know that they're useful. So, a really good example of this is Realtime.

**Michelle Pokrass** [00:00:00] We're actually going to be shipping audio capabilities in chat completions. So this is like the lowest level capability. So you supply in audio, and you can get back raw audio, and it works at the request response layer. But, in through building advanced voice mode, we realized ourselves that like, it's not It's pretty hard to do with something like Chat Completions, and so that led us to building this WebSocket API.

**Michelle Pokrass** [00:00:00] So we really learned a lot from our own tools, and we think, you know, the Chat Completions thing is nice, and for certain use cases, or async stuff, but you're really gonna want a real time API? And then as we, you know, test more with developers, we might see that it makes sense to have like another layer of abstraction on top of that.

**Michelle Pokrass** [00:00:00] Something like closer to you know, more client side libraries. But, for now, you know, that's where we feel we have like a really good point of view.

**Simon Willison** [00:00:00] So that's a question I have is if I've got a half hour long audio recording, At the moment, the only way I can feed that in is if I call the WebSocket API and slice it up into little JSON basics for snippets and fire them all over.

**Simon Willison** [00:00:00] That's it. In that case, I'd rather just give you a, like an image in the chat completion API, give you a URL files and input. Is that something That's what we're

**Michelle Pokrass** [00:00:00] going to do.

**Simon Willison** [00:00:00] Oh, thank goodness for that.

**Michelle Pokrass** [00:00:00] Yes. It's in the blog post. I think it's a short one liner, but it's rolling out, I think, in the coming weeks.

**Michelle Pokrass** [00:00:00] Oh, wow.

**Simon Willison** [00:00:00] Oh, really soon then.

**Michelle Pokrass** [00:00:00] Yeah, the team has been sprinting we're just putting finishing touches on stuff. Do you

**Simon Willison** [00:00:00] have a feel for the length limit on that?

**Michelle Pokrass** [00:00:00] I don't have it off the top. Okay. Sorry.

**Simon Willison** [00:00:00] Because, yeah, often I want to do, I do a lot of work with, like, transcripts of hour long YouTube videos, which Yeah.

**Simon Willison** [00:00:00] Yeah. Currently, I run them through Whisper and then I do the transcript that way, but being able to do the multimodal thing with those would be really useful.

**Michelle Pokrass** [00:00:00] Totally, yeah. We're really jazzed about it. We want to basically give the lowest capabilities we have, lowest level capabilities, and, you know, the things that make it easier to use.

**Michelle Pokrass** [00:00:00] And so, you know, targeting kind of both. I

**Simon Willison** [00:00:00] just realized what I can do, though, is I do a lot of Unix utilities, little, like, Unix things. I want to be able to pipe the output of a command into something which streams that up to the WebSocket API and then speaks it out loud. So I can do streaming speech of the output of things.

**Simon Willison** [00:00:00] That should work. Like, I think you've given me everything I need for that. That's cool.

**Michelle Pokrass** [00:00:00] Yeah. Excited to see what you build. Is

**Swyx** [00:00:00] there I heard there are, like, multiple competing solutions. And you guys evaluated before you picked WebSockets. Like server set events, polling, I don't, like, can you give, like, your thoughts on, like, the live updating paradigms that you guys looked at?

**Swyx** [00:00:00] Because I think a lot of engineers have looked at stuff like this.

**Michelle Pokrass** [00:00:00] Well, I think WebSockets are just a natural fit for bi directional streaming. You know, other places I've worked, like, Coinbase, we had a WebSocket API for pricing data. I think it's just like a very natural format.

**Swyx** [00:00:00] So it wasn't even really that controversial at all?

**Michelle Pokrass** [00:00:00] I don't think it was super controversial. I mean, we definitely explored the space a little bit, but I think we came to WebSockets pretty quickly.

**Swyx** [00:00:00] Cool. Video?

**Michelle Pokrass** [00:00:00] Yeah. Not yet, but, you know.

**Swyx** [00:00:00] I actually was hoping for the chat, GPT desktop app with video today. Yeah. Yeah.

**Simon Willison** [00:00:00] Oh,

**Michelle Pokrass** [00:00:00] my

**Simon Willison** [00:00:00] question is one frame a second.

**Simon Willison** [00:00:00] How frequently? Yeah.

**Swyx** [00:00:00] Because Yeah, I mean sending a sending a whole video frame of like a 1080p screen. Maybe it might be too much What's the limitations on a on a WebSocket chunk going over? I don't know

**Michelle Pokrass** [00:00:00] I don't have that off the top

**Simon Willison** [00:00:00] Like Google Gemini you can do an hour's worth of video in their context window and just by slicing it up into one frame At ten frames a second and it does work so I Don't know.

**Simon Willison** [00:00:00] I'm I'm not sure But then that's the weird thing about Gemini is it's so good at you just giving it a flood of individual frames It'll be interesting to see if GPT 4. 0 can handle that or not

**Alessio** [00:00:00] Do you have any more feature requests? It's been a long day for everybody, but you got you got me show right here So my one

**Simon Willison** [00:00:00] is I want you to do all of the accounting for me I want my users to be able to run my app And I want them to call your APIs with their user ID and have you go, oh, they've spent 30 cents.

**Simon Willison** [00:00:00] Check, cut them off at a dollar. I can like, check how much they spent. All of that stuff, because I'm having to build that at the moment, and I really don't want to. I don't want to be a token accountant. I want you to do the token accounting for me.

**Michelle Pokrass** [00:00:00] Yeah, totally. I hear you. It's good feedback.

**Swyx** [00:00:00] Well, like, how does that contrast with your actual priorities, right?

**Swyx** [00:00:00] Like, I feel like you have a bunch of priorities. They showed some on stage with multi modality and all that.

**Michelle Pokrass** [00:00:00] Yeah.

**Swyx** [00:00:00] Like

**Michelle Pokrass** [00:00:00] Yeah it's good feedback. It's hard to say. I would say things change really quickly. Things that are big adop big blockers for user adoption we find very important. And, yeah. It's a rolling prioritization.

**Michelle Pokrass** [00:00:00] Yeah.

**Swyx** [00:00:00] No assistance API update.

**Michelle Pokrass** [00:00:00] Not at this time. Yeah. Yeah.

**Swyx** [00:00:00] I was hoping for, like, an O1 native. Do thing in assistance? Yeah. I thought they would go well together. we're still

**Michelle Pokrass** [00:00:00] kind of iterating on the formats, I think there are some problems with the assistance API. Some things it does really well.

**Michelle Pokrass** [00:00:00] And I think we'll keep iterating and land on something really good. But just, you know, it wasn't quite ready yet. Some of the things that are good in the assistance API is hosted tools. People really like hosted tools and especially RAG. And then some things that are, you know, less intuitive is just how many API requests you need to get going with the assistance API.

**Michelle Pokrass** [00:00:00] It's

**Simon Willison** [00:00:00] quite.

**Michelle Pokrass** [00:00:00] It's quite a lot. Yeah, you gotta create an assistant, you gotta create a thread, you gotta, you know, do all this stuff. So yeah, it's something we're thinking about. It shouldn't be so hard.

**Simon Willison** [00:00:00] The only thing I've used it for so far is Code Interpreter. It's like it's an API to Code Interpreter.

**Simon Willison** [00:00:00] Crazy exciting. Yeah.

**Michelle Pokrass** [00:00:00] Yes, we want to fix, we want to fix that and make it easier to use, so. I

**Simon Willison** [00:00:00] want code intercepts over WebSockets, that would be wildly interesting.

**Swyx** [00:00:00] Yeah, do you, do you want to bring your own code interpreter or you want to use OpenAI's one? I want to

**Simon Willison** [00:00:00] use theirs, because code intercepts is a hard problem, sandboxing and all of that stuff is Yeah, but there's a bunch

**Swyx** [00:00:00] of code interpreter as a

**Simon Willison** [00:00:00] service

**Swyx** [00:00:00] things out there.

**Swyx** [00:00:00] There are a few now, yeah. Because there's, I think you don't Allow arbitrary installation of packages. Oh, they do. Unless

**Simon Willison** [00:00:00] they really do actually use your hack code. It, huh?

**Michelle Pokrass** [00:00:00] Yeah,

**Simon Willison** [00:00:00] and I do.

**Michelle Pokrass** [00:00:00] Yeah. You upload a pit package,

**Simon Willison** [00:00:00] you can run, you can compile C code and code interpreter. I know. You know, to do it.

**Simon Willison** [00:00:00] That's a hack. Oh, it's such a glorious hack though. Okay. I've had it Write me custom seql light extensions in C and compile them and run them inside of Python and it works.

**Swyx** [00:00:00] I mean, yeah, there's, there's others. E two B is one of them, like, yeah. It'll be interesting to see what the real time version of that will be.

**Alessio** [00:00:00] Awesome, Michelle. Thank you for the update. We left the episode as, what will voice mode look like? Obviously, you knew what it looked like, but you didn't say it, so now you could share this.

**Alessio** [00:00:00] Yeah, here we are. Hope you

**AI Charlie** [00:00:00] guys

**Alessio** [00:00:00] like

**Swyx** [00:00:00] it. Yeah, awesome. That's

**Alessio** [00:00:00] it.

**AI Charlie** [00:00:00] Our final guest today, and also a familiar, recent voice on the Latent Space pod, presented at one of the community talks at this year's Dev Day. Alistair Pullen of Cosene made a huge impression with all of you. Special shout out to listeners like Jesse from Morphlabs, when he came on to talk about how he created synthetic datasets to fine tune the largest LORAs that had ever been created for GPT 4.

**AI Charlie** [00:00:00] 0 to post the highest ever scores on SWEbench and SWEbench Verified. While not getting recognition for it, because he refused to disclose his reasoning traces to the SWEbench team. Now that OpenAI's R1 preview is announced, it is incredible to see the OpenAI team also obscure their chain of thought traces for competitive reasons, and still perform lower than Cozine's genie model.

## [01:04:45] Alistair Pullen, CEO, Cosine (Genie)

**AI Charlie** [00:00:00] We snagged some time with Ali to break down what has happened since his episode aired.

**Swyx** [00:00:00] Welcome back, Ali. Thank you so much. Thanks for having me. So you just spoke at OpenAI Dev Day. What was the experience like? Did they reach out to you? You seem to have a very close relationship.

**Alessio** [00:00:00] Yeah, so off the back of, off the back of the work that we've done, that we spoke about last time we saw each other I think that OpenAI definitely felt that the work we've been doing around fine tuning was worth sharing.

**Alessio** [00:00:00] I would obviously tend to agree, but today today I spoke about some of the techniques that we learned. Obviously it was like a non linear path arriving to where we've arrived and the techniques that we've built to build Genie. So I definitely, I think I shared a few, a few extra pieces about some of the techniques and how it really works under the hood.

**Alessio** [00:00:00] How you generate a data set to show the model how to do what we show the model. And that was mainly what I spoke about today. I mean, yeah, they reached out and they were, I was, I was Super excited at the opportunity, obviously, like, it's not every day that you get to come and do this. Especially in San Francisco, so Yeah, they reached out and they were like, do you want to talk at Dev Day?

**Alessio** [00:00:00] You can speak about basically anything you want related to what you've built, and I was like, sure, that's amazing. I'll talk about fine tuning, how you build a model that does this software engineering, so yeah.

**Swyx** [00:00:00] Yeah and the trick here is when we talked, O1 was not out. No, it wasn't. Did you know about O1, or?

**Alessio** [00:00:00] I didn't know. I knew some bits and pieces. No, not really. I knew a reasoning model was on the way. I didn't know what it was going to be called. I knew as much as everyone else. Strawberry was the name back then. Because,

**Swyx** [00:00:00] you know, I'll fast forward. You were the first to hide your chain of thought, reasoning traces as IP.

**Swyx** [00:00:00] Yes. Right? Famously, that got you in trouble with 3Bench or whatever. Yes. I feel slightly vindicated by that now. And now, obviously, O1 is doing it. Yeah, the

**Alessio** [00:00:00] fact that, yeah, I mean, like, I think it's, I think it's true to say right now that the reasoning of your model gives you the edge that you have. Unlike.

**Alessio** [00:00:00] The amount of effort that we put into our data pipeline to generate these human like reasoning traces was, I mean, that wasn't for nothing. We knew that this was the way that you'd unlock more performance, getting the model to think in a specific way. In our case, we wanted it to think like a software engineer.

**Alessio** [00:00:00] But, yeah, I think, I think that, The approach that other people have taken, like OpenAI, in terms of reasoning, has definitely showed us that we were going down the right path pretty early on. And even now, we've started replacing some of the reasoning traces in our genie model with reasoning traces generated by O1, or at least in tandem with O1.

**Alessio** [00:00:00] And we've already started seeing improvements in performance from that point. But no, like back to your point, in terms of like the, the whole like approach. Withholding them. I, I, I, I still think that that was the right decision to do because of the very reason that everyone else has decided to, to, to, to not share those things.

**Alessio** [00:00:00] It's, it is exactly, it shows exactly how we do what we do and that is our edge at the moment. So,

**Alessio** [00:00:00] yeah. As a founder, so, they also feature Cognition on, on stage, talk about that. How does that make you feel that like, you know, they're like, hey, 01 is so much better, makes us better. For you, it should be like.

**Alessio** [00:00:00] Oh, I'm so excited about it too, because now all of a sudden it's like, it kind of like, raises the floor for everybody, like, how should people, especially new founders, how should they think about, you know, worrying about the new model versus like, being excited about them just focusing on like, the core FP and maybe switching out some of the parts, like you mentioned.

**Alessio** [00:00:00] Yeah, I, I, I, I, speaking for us, I mean obviously like, we were extremely excited about O1 because, At that point, the process of reasoning is obviously very much baked into the model. We fundamentally, if you like, remove all distractions and everything, we are a reasoning company. Right? We want to reason in the way that a software engineer reasons.

**Alessio** [00:00:00] So when I saw that model announced, I thought immediately, well, I can improve the quality of my traces coming out of my pipeline, so like, my signal to noise ratio gets better. And then, not immediately, but down the line, I'm going to be able to train those traces into O1 itself. So I'm going to get even more performance that way as well.

**Alessio** [00:00:00] So it's For us, a really nice position to be in, to be able to take advantage of it, both on the prompted side and the fine tuned side. And also because, fundamentally, like, we are, I think, fairly clearly in a position now where we don't have to worry about what happens when O2 comes out, what happens when O3 comes out.

**Alessio** [00:00:00] This process continues, like, even going from You know, when we first started going from 3. 5 to 4, we saw this happen and then from 4 turbo to 4. 0 and then from 4. 0 to 0. 1, we've seen the performance get better every time and I think, I mean, like, the crude advice I'd give to any startup founder is try to put yourself in a position where you can take advantage of the same, you know, like, C level rise every time, essentially.

**Swyx** [00:00:00] Do you make anything out of the fact that you were able to take 4. 0 and fine tune it higher than 0. 1 currently scores on SweeBench Verified? Yeah, I mean like,

**Alessio** [00:00:00] that was obviously, to be honest with you, you realized that before I did. Adding value. Yes, absolutely, that's a value add investor right there. No, obviously I think it's been, that in of itself is really vindicating to see because I think, I think we have, heard from some people, not a lot of people, but some people saying, well, okay, well, if I, one can reason, then what's the point of doing your reasoning, but it shows how much more signal is in, like the custom reasoning that we generate.

**Alessio** [00:00:00] And again, it's the, it's the very sort of obvious thing. If you take something that's made to be general and you make it specific, of course, it's going to be better at that thing. Right? So it was obviously great to see, like, we still are better than no one out of the box. You know, even with an older model, and I'm sure that that's, you know, That delta will continue to grow once we're able to train O1, and once we've done more work on our dataset using O1, like, that delta will grow as well.

**Swyx** [00:00:00] It's not obvious to me that they will allow you to fine tune O1, but, you know, maybe they'll try. I think the, the, the core question that OpenAI really doesn't want you to figure out is can you use an open source model and beat O1?

**Romain Huet** [00:00:00] Interesting. Because, because

**Swyx** [00:00:00] you basically have shown proof of concept that a non O1 model can beat O1.

**Swyx** [00:00:00] And their whole L1 marketing is, don't bother trying. Like, don't bother stitching together multiple chain of thought calls. We did something special, secret sauce, you don't know anything about it. And somehow, you know, your 4. 0 chain of thought reasoning as a software engineer is still better. Maybe it doesn't last.

**Swyx** [00:00:00] Maybe they're going to run L1 for five hours instead of five minutes, and then suddenly it works. So, I don't know.

**Alessio** [00:00:00] It's hard to know. I mean, one of the things that we just want to do out of sheer curiosity is do something like fine tune 405B on the same dataset. Like, same context window length, right? So, it should be fairly easy.

**Alessio** [00:00:00] We haven't done it yet. Truthfully, we have been so swamped with the waitlist, shipping product, you know, dev day, like, you know, onboarding customers from our waitlist. All these different things have gotten in the way, but it is definitely something out of more curiosity than anything else I'd like to try out.

**Alessio** [00:00:00] But also It opens up a new vector of like, if someone has a VPC where they can't deploy an OpenAI model, but they might be able to deploy an open source model, it opens that up for us as well from a customer perspective. So it'll probably be quite useful. I'd be very keen to see what the results are though.

**Alessio** [00:00:00] I suspect the answer is yes,

**Swyx** [00:00:00] but it may be hard to do. So like Reflection70b was like a really crappy attempt at doing it. You guys were much better, and that's why we had you on the show. I, yeah, I'm interested to see if there's an OpenO1 basically. If people want OpenO1.

**Alessio** [00:00:00] Yeah, I'm sure they do. As soon as we, as soon as we do it, I'm like, Once we've wrapped up what we're doing in San Francisco, I'm sure we'll give it a go.

**Alessio** [00:00:00] I spoke to some guys today, actually, about fine tuning 405B, who might be able to allow us to do it very, like, very easily. I don't want to have to basically do all the setup myself. So, yeah, that might happen sooner rather than later.

**Alessio** [00:00:00] Anything from the releases today that you're super excited about? So prompt caching, I'm guessing when you're like dealing with a lot of codebases, that might be helpful.

**Alessio** [00:00:00] Is there anything with vision fine tuning related to

**Alessio** [00:00:00] like more like UI related development? Yeah, definitely. Yeah, I mean like we were talking, it's funny, like my co founder Sam, who you've met, and I were talking about the idea of doing vision fine tuning. Like, way back, like, well over a year ago, before Genie existed as it does now when we, when we collected our original dataset to do what we do now whenever there were image links and links to, like like, graphical resources and stuff, we also pulled that in as well.

**Alessio** [00:00:00] We never had the opportunity to use it, but it's something we have in storage. And, again, like, when we have the time, it's something that I'm super excited, particularly on the UI side. To be able to, like, leverage, particularly if you think about one of the things, I mean, not to sidetrack, but one of the things we've noticed is, I know Swebench is, like, the most commonly talked about thing, and honestly, it's a very, it's an amazing project, but, One of the things we've learned the most from actually shipping this product to users is, It's a pretty bad proxy at telling us how competent the model is, so, for example, When people are doing, like, React development using Genie, For us, it's impossible to know whether what it's written has actually done, you know, done what it wanted to.

**Alessio** [00:00:00] So at least even using, like, the fine tuning provision to be able to help eval, like, what we output is already something that's very useful. But also, in terms of being able to pair, here's a UI I want, here's the code that actually, like, represents that UI, is also going to be super useful as well, I think.

**Alessio** [00:00:00] In terms of generally, what have I been most impressed by? The distillation thing is awesome. I think we'll probably end up using it in places. But what it shows me more broadly about OpenAI's approach is they're going to be building a lot of the things that we've had to hack together internally, in terms from a tooling point of view, just to make our lives so much easier.

**Alessio** [00:00:00] And I've spoken to, you know, John, the head of fine tuning, extensively about this. But there's a bunch of tools that we've had to build internally for things like dealing with model lineage, dealing with dataset lineage, because it gets so messy so quickly, that we would love OpenAI to build. Like, absolutely would love them to build it.

**Alessio** [00:00:00] It's not, it's not what gives us our edge, but it certainly means that then we don't have to build it and maintain it afterwards. So, it's a really good first step, I think, in, like, the overall maturity of the fine tuning product and API in terms of where they're going to see those early products. And I think that they'll be continuing in that direction going on.

**Alessio** [00:00:00] Did you not, so there's a very

**Swyx** [00:00:00] active ecosystem of LLLmaps tools. Mm hmm. Did you not evaluate those before building your own?

**Alessio** [00:00:00] We did, but I think fundamentally, like, No more. Yeah, like, I think, in a lot of places, it was never a big enough pain point to be like, oh, we absolutely must outsource this. It's definitely, in many places, something that you can hack a script together In a day or two, and then hook it up to our already existing internal tool UI, and then you have, you know, what you need, and whenever you need a new thing, you just tack it on.

**Alessio** [00:00:00] But for, like, all of these LLM Ops tools, I've never felt the pain point enough to really, like, bother, and that's not to deride them at all, I'm sure many people find them useful, but just for us as a company, we've never felt the need for them. So it's great that, it's great that OpenAI are going to build them in because it's really nice to have them there, for sure.

**Alessio** [00:00:00] But it's not something that, like, I'd ever consider really paying for externally or something like that, if that makes sense.

**Swyx** [00:00:00] Yeah. Does voice mode factor into Genie?

**Alessio** [00:00:00] Maybe one day, that'd be sick, wouldn't it? I don't know. Yeah, I think so. You're

**Swyx** [00:00:00] the first person, we've been asking this question to everybody.

**Swyx** [00:00:00] Yeah, I think. You're the first person to not mention voice mode.

**Alessio** [00:00:00] Oh, well, it's, it's, it's currently so distant from what we do. But I definitely think, like, this whole talk, if we want it to be a full on AI software engineering colleague, like, there is definitely a vector in some way that you can build that in.

**Alessio** [00:00:00] Maybe even during the ideation stage, talking through a problem with Genius in terms of how we want to build something down the line. I think that might be useful, but honestly, like, that would be nice to have when we have the time. Yeah, amazing.

**Swyx** [00:00:00] One last question. On your in your talk, you mentioned a lot about So you're curating your data and your distribution and all that, and before we sat down you talked a little bit about having to diversify your dataset.

**Swyx** [00:00:00] Absolutely, yeah. What's driving that,

**Alessio** [00:00:00] what are you finding? So, we have been rolling people off the waitlist that we sort of amassed when we announced when I last saw you. And it's been really interesting because as I may have mentioned on the podcast, like we had to be very opinionated about the data mix and the data set that we put together for like sort of the V0 of Genie.

**Alessio** [00:00:00] Again, like, to your point, Javascript, Javascript, Javascript, Python, right? There's a lot of Javascripts in its various forms in there. But it turns out that when we've shipped it to the very early alpha users we rolled it out to for example, we had some guys using it with a C sharp codebase.

**Alessio** [00:00:00] And C sharp currently represents, I think, about 3 percent of the overall data mix. And they weren't getting the levels of performance that they saw when they tried it with a Python codebase. And It was obviously not great for them to have a bad experience, but it was nice to be able to correlate it with the actual, like, objective data mix that we saw.

**Alessio** [00:00:00] So we did what we've been doing is like little top up fine tunes where we take, like, the general genie model and do an incremental fine tune on top with just a bit more data for a given, you know, vertical language. And we've been seeing improvements coming from that. So. Again, this is one of the great things about sort of baptism by fire and letting people use it and giving you feedback and telling you where it sucks.

**Alessio** [00:00:00] Because that is not something that we could have just known ahead of time. So I want that data mix to, over time as we roll it out to more and more people, and we are trying to do that as fast as possible, but we're still a team of five for the time being. And so To be as general and as representative of what our users do as possible and not what we think they need.

**Swyx** [00:00:00] Yeah, so every customer is going to have their own fine

**Alessio** [00:00:00] tune. There is going to be the option to, yeah, there is going to be the option to fine tune the model on your code base. It won't be in, like, the base pricing tier, but you will definitely be able to do that. It will go through All of your codebase history, learn how everything happened, and then you'll have an incrementally fine tuned genie just on your codebase.

**Alessio** [00:00:00] That's what enterprises really love the idea of. Perfect.

**Swyx** [00:00:00] Anything else? Yeah, that's it. Thank you so much. Thank you so

**Alessio** [00:00:00] much, guys. Good to

**Swyx** [00:00:00] see you.

## [01:18:31] Sam Altman + Kevin Weill Q&A

**AI Charlie** [00:00:00] Lastly, this year's Dev Day ended with an extended Q& A with Sam Altman and Kevin Weil. We think both the questions asked and answers given were particularly insightful, so we are posting what we could snag of the audio here from publicly available sources.

**AI Charlie** [00:00:00] Credited in the show notes, for you to pick through. If the poorer quality audio here is a problem, we recommend waiting for approximately 1 to 2 months until the final video is released on YouTube. In the meantime, we particularly recommend Sam's answers on the moderation policy, on the underappreciated importance of agents and AI employees beyond level 3.

**AI Charlie** [00:00:00] And his projections of the intelligence of O1, O2, and O3 models in future.

**Speaker 17** [00:00:00] Alright, I think everybody knows you. For those who don't know me, I'm Kevin Wheel, Chief Product Officer at OpenAI. I have the good fortune of getting to turn the amazing research that our research teams do into the products that you all use every day and the APIs that you all build on every day. I thought we'd start with some audience engagement here.

**Speaker 17** [00:00:00] So on the count of three, I want to count to three, and I want you all to say, of all the things that you saw launched here today, what's the first thing you're going to integrate? It's the thing you're most excited to build on. Alright? You gotta do it. Alright? One, two, three. Real time

**Alex Volkov** [00:00:00] API!

**Speaker 17** [00:00:00] I'll say personally, I'm super excited about our distillation products.

**Speaker 17** [00:00:00] I think that's going to be really, really interesting. I'm also excited to see what you all do with advanced voicemail with the real time API, and with vision fine tuning in particular. Okay, so I've got some questions for Sam, I've got my CEO here in the hot seat, let's see if I can't make a career limiting move.

**Speaker 17** [00:00:00] So we'll start this we'll start with an easy one, Sam. How close are we to AGI?

**Sam Altman** [00:00:00] You know, we used to, every time we finished a system, we would say like, in what way is this not an AGI? Okay. And it used to be like, very easy, you could like, make a little robotic hand that does a prefix cube, or a dotabot, and it's like, oh, it does some things, but definitely not an AGI.

**Sam Altman** [00:00:00] It's obviously harder to say now, and so we're trying to like, stop talking about AGI as this general thing. We have this levels framework, because the word AGI has become so overloaded. So like, real quickly, we use one for chatbots, two for reasoners, three for agents, four for innovators, five for organizations, like roughly.

**Sam Altman** [00:00:00] I think we clearly got to level two, or we clearly got to level two. With O1 and it, you know, can do really quite impressive Python tasks. It's a very smart model. It doesn't feel AGI like in a few important ways, but I think if you just do the one next step of making it, you know, very agent like, which is our level three, and which I think we will be able to do in the not distant future, It will feel surprisingly capable still probably not something that most of you would call an AGI, though maybe some of you would but it's going to feel like, all right, this is, this is like a significant thing.

**Sam Altman** [00:00:00] And then the, the leap, and I think we do that pretty quickly the, the leap from that to something that can really increase the rate of new scientific discovery, which for me is like a very important part. of having an AGI. I feel a little bit less certain on that, but not a long time. Like, I think all of this now is going to happen pretty quickly, and if you think about what happened from last decade to this one, in terms of model capabilities, and you're like, eh.

**Sam Altman** [00:00:00] I mean, if you go look at like, If you go from my 01 on a hard problem back to like 4Turbo that we launched 11 months ago, you'll be like, wow, this is happening pretty fast. And I think the next year will be very steep progress. Next two years will be very steep progress. Harder than that. Hard to say with a lot of certainty.

**Sam Altman** [00:00:00] But I would say like the math will vary. And at this point, the definitions really matter. And in fact, the fact that the definitions matter this much, Somehow means we're, like, getting pretty close. Yeah.

**Speaker 17** [00:00:00] And, you know, there used to be this sense of AGI where it was like, it was a binary thing, and you were gonna go to sleep one day, and there was no AGI, and wake up the next day and there was AGI.

**Speaker 17** [00:00:00] I don't think that's exactly how we think about it anymore, but how have your

**Sam Altman** [00:00:00] views on this evolved? You know, the one, I agree with that, I think we're, like, you know, in this, like, kind of period where it's It's gonna feel very blurry for a while, and the, you know, is this AGI yet, or is this not AGI, or kind of like, at what point?

**Sam Altman** [00:00:00] It's just gonna be this like, smooth exponential, and, you know, probably most people, looking back at history, won't agree, like, when that milestone was hit, and will just realize it was like, a silly thing. Even the Turing test, which I thought always was like, this very clear milestone, you know, there was this like, fuzzy period.

**Sam Altman** [00:00:00] It kind of like, went oosh and bye, no one cared But, but I think the right framework is just this one exponential. That said if we can make an AI system that is like materially better at all of open AI than doing, at doing AI research, that does feel to me like some sort of important discontinuity.

**Sam Altman** [00:00:00] It's probably still wrong to think about it that way. It probably still is the smooth exponential curve. Bye. That feels like a new milestone.

**Alex Volkov** [00:00:00] Is

**Speaker 17** [00:00:00] OpenAI still as committed to research as it was in the early days? Will research still drive the core of our advancements in our product development? Yeah,

**Sam Altman** [00:00:00] I mean, I think more than ever.

**Sam Altman** [00:00:00] The, there was like a time in our history when the right thing to do was just to scale up compute, and we saw that with conviction, and we had a spirit of like, We'll do whatever works, you know, like, we want to, we have this mission, we want to like, build, say, AGI, figure out how to share the benefits. If the answer is like, rack up GPUs, we'll do that.

**Sam Altman** [00:00:00] And right now, the answer is, again, really push on research. And I think you see this with O1, like, that is a giant research breakthrough that we were attacking from many vectors over a long period of time that came together in this really powerful way. We have many more giant research breakthroughs to come, but the thing that I think is most special about OpenAI is that we really deeply care about research and we understand how to do it.

**Sam Altman** [00:00:00] I think, it's easy to copy something you know works, and you know, I actually don't even mean that as a bad thing, like, when people copy OpenAI, I'm like, great, the world gets more AI? That's wonderful. But, to do something new for the first time, to like, really do research in the true sense of it, which is not like, you know, let's barely get soda out of this thing, or like, let's tweak this.

**Sam Altman** [00:00:00] But like, let's go find the new paradigm, and the one after that, and the one after that. That is what motivates us, and I think the thing that is special about us as an org. Besides the fact that we, you know, married product and research and all this other stuff together, is that we know how to run that kind of a culture that can go, that can go push back the frontier, and that's really hard.

**Sam Altman** [00:00:00] But we love it and that's, you know, I have to do that a few more times in a week at AGI.

**Speaker 17** [00:00:00] Yeah, I'll say like the litmus test for me coming from the outside, from, you know, sort of normal tech companies, of how critical research is to open AI, is that building product in open AI is fundamentally different than any other place that I have ever done it before.

**Speaker 17** [00:00:00] You know, normally you have, you have some sense of your tech stack, you have some sense of what you have to work with, and what capabilities computers have, and, and then you're trying to build the best product, right? You're figuring out who your users are, what problems they have, and how you can help solve those problems for them.

**Speaker 17** [00:00:00] There is that at OpenAI, but also, the state of, like, what computers can do just evolves every two months, three months, and suddenly computers have a new capability that they've never had in the history of the world. And we're trying to figure out how to build a great product and expose that for developers and our APIs and so on.

**Speaker 17** [00:00:00] And then, you know, you can't totally tell what's coming, they're coming through, it's coming through the mist a little bit at you and gradually taking shape. It's fundamentally different than any other company I've ever worked at, and it's, I think, Is that the thing that has

**Sam Altman** [00:00:00] most surprised you?

**Speaker 17** [00:00:00] Yes. Yeah, and it's interesting how, Even internally we don't always have a sense.

**Speaker 17** [00:00:00] You have like, okay, I think this capability is coming, but is it going to be, you know, 90 percent accurate or 99 percent accurate in the next model because the difference really changes what kind of product you can build. And you know that you're gonna get to 99, you don't quite know when, and figuring out how you put a roadmap together in that world is really interesting.

**Sam Altman** [00:00:00] Yeah, the degree to which we have to just, like, follow the science, and let that determine what we go work on next, and what products we build, and everything else, is, I think, hard to get across. Like, we have guesses about where things are gonna go. Sometimes we're right, often we're not. But, if something starts working, or if something doesn't work that you thought was gonna work, our willingness to just say, we're gonna like, pivot everything, and do what the science allows, and you don't get to like, pick what the science allows?

**Sam Altman** [00:00:00] Yeah. That's surprising.

**Speaker 17** [00:00:00] I was sitting with an Enterprise customer a couple weeks ago, and they said, you know, one of the things we really want, this is all working great, we love this, one of the things we really want is a notification 60 days in advance when you're gonna launch something. And I was like, I want that too.

**Speaker 17** [00:00:00] Alright, so I'm going through, these are a bunch of questions from the audience, by the way, and we're going to try and also leave some time at the end for people to ask audience questions. So we've got some folks with mics, and when we get there they'll be thinking. But next thing is So many in the alignment community are genuinely concerned that open AI is now only paying lib service to alignment.

**Speaker 17** [00:00:00] Can you reassure us?

**Sam Altman** [00:00:00] Yeah I think it's true we have a different take on alignment than, like, maybe what people write about on whatever that, like, internet forum is. But we really do care a lot about building safe systems. We have an approach to do it that has been informed by our experience so far.

**Sam Altman** [00:00:00] And touch on that other question, which is you don't get to pick where the science goes. Of, we want to figure out how to make capable models that get safer and safer over time. And, you know, a couple of years ago, we didn't think the whole strawberry or the O1 paradigm was gonna work in the way that it's worked.

**Sam Altman** [00:00:00] And that brought a whole new set of safety challenges, but also safety opportunities. And, rather than kind of, like, plan to make theoretical ones, You know, superintelligence gets here, here's the like, 17 principles. We have an approach of, figure out where the capabilities are going, and then work to make that system safe.

**Sam Altman** [00:00:00] And, O1 is obviously our most capable model ever, but it's also our most aligned model ever, by a lot. And as, as these models get better intelligence, better reasoning, whatever you want to call it, the things that we can do to align them the things we can do to build really safe systems across the entire stack our tool set keeps increasing as well.

**Sam Altman** [00:00:00] So,

**Sam Altman** [00:00:00] we, we have to build models that are generally accepted as safe and robust to be able to put them in the world. And when we started OpenAI, what the picture of alignment looked like, and what we thought the problems that we needed to solve were going to be, turned out to be nothing like the problems that actually are in front of us and that we had to solve now.

**Sam Altman** [00:00:00] And also, when we made the first GPT 3 if you ask me for the techniques that would have worked for us to be able to now deploy. all of current systems as generally expected to be safe and robust. They would not have been the ones that turned out to work. So, by this idea of iterative deployment, which I think has been one of our most important safety stances ever and sort of confronting reality as it sits in front of us, we've made a lot of progress, and we expect to make more, and we keep finding new problems to solve, but we also keep finding new techniques to solve them.

**Sam Altman** [00:00:00] All of that said, I

**Sam Altman** [00:00:00] I think worrying about the sci fi ways this all goes wrong is also very important. We have people thinking about that. It's a little bit less clear, kind of, what to do there, and sometimes you end up backtracking a lot, but,

**Sam Altman** [00:00:00] but I don't think it's I also think it's fair to say we're only gonna work on the thing in front of us. We do have to think about where this is going, and we do that too. And I think if we keep approaching the problem from both ends like that, most of our thrust on the, like, okay, here's the next thing, we're gonna deploy this.

**Sam Altman** [00:00:00] What it needs to happen to get there. But also like, what happens if this curve just keeps going? That's been, that's been an effective strategy for us.

**Speaker 17** [00:00:00] I'll say also, it's one of the places where I'm really, I really like our philosophy of iterative deployment. When I was at Twitter, back, I don't know, a hundred years ago now Ev said something that stuck with me, which is, So no matter how many smart people you have inside your walls, there are way more smart people outside your walls.

**Speaker 17** [00:00:00] And so, when we try and get our, you know, it'd be one thing if we just said we're gonna try and figure out everything that could possibly go wrong within our walls, and it'd be just us and the red teamers that we can hire and so on. And we do that, we work really hard at that. But also, Launching iteratively and launching carefully and learning from the ways that folks like you all use it, what can go right, what can go wrong, I think is a big way that we get these things right.

**Speaker 17** [00:00:00] I also think that as we head into this world of

**Sam Altman** [00:00:00] agents off doing things in the world, that is going to become really, really important. As these systems get more complex and are acting over longer horizons the pressure testing from the whole outside world, like, really,

**Alex Volkov** [00:00:00] really

**Sam Altman** [00:00:00] critical.

**Speaker 17** [00:00:00] Yeah. So. We'll go, actually, we'll go off of that and maybe talk to us a bit more about how you see agents fitting in with OpenAI's long term plans.

**Speaker 17** [00:00:00] What do you think? I think I'm a huge part of the I mean, I think the exciting thing is this This set of models, O1 in particular, and all of its successors, are going to be what makes this possible. Because you finally have the ability to reason, to take hard problems, break them into simpler problems, and act on them.

**Speaker 17** [00:00:00] I mean, I think 2025 is going to be the year that's really, that's big. Yeah, I,

**Sam Altman** [00:00:00] I mean, chat interfaces are great, and they all, I think, have an important place in the world, but I don't know. The,

**Sam Altman** [00:00:00] when you can like ask a model, when you can ask like ChatGT or some agent something, and it's not just like you get a kind of quick response, or even if you get like 15 seconds of thinking, and oh, one gives you like a nice piece of code back or whatever. But you can like really give something a multi term interaction with environments or other people or whatever, like think for the equivalent of multiple days of human effort, and, and like a really smart, really capable human, and like have stuff happen.

**Sam Altman** [00:00:00] We all say that, we're all like, oh yeah, this is the next thing, this is coming, this is gonna be another thing, and we just talk about it like, okay, you know, it's like the next model in evolution. I would bet, and we don't really know until we get to use these, that it's We'll of course get used to it quickly, people get used to any new technology quickly, but this will be like a very significant change to the way the world works.

**Sam Altman** [00:00:00] in a short period of time.

**Speaker 17** [00:00:00] Yeah, it's amazing. Somebody was talking about getting used to new capabilities and AI models and how quickly, actually I think it was about Waymo but they were talking about how in the first ten seconds of using Waymo, they were like, oh my god, is this thing that, like, there's like, let's watch out, and then ten minutes in, they were like, oh, this is really cool.

**Speaker 17** [00:00:00] And then twenty minutes in, they were like, checking their phone for, you know, it's amazing how much your, your sort of internal firmware updates. For this new stuff, right? Yeah, like,

**Sam Altman** [00:00:00] I think that people will ask an agent to do something for them that would have taken them a month, and they'll finish in an hour, and it'll be great, and then they'll have like ten of those at the same time, and then they'll have like a thousand of those at the same time, and by 2030 or whatever, we'll look back and be like, yeah, this is just like what a human is supposed to be capable of, what a human used to like, you know, grind at for years or whatever, many humans used to grind at for years.

**Sam Altman** [00:00:00] I just now I can ask a computer to do it and it's like done in an hour. That's, why is it not a minute? Yeah,

**Speaker 17** [00:00:00] it's also, it's one of the things that makes having an amazing development platform great too because, you know, we'll experiment and we'll build some agentic things of course and like we've already got, I think just like, we're just pushing the boundaries of what's possible today you've got groups like cognition doing amazing things and coding Like Harvey and case text, you guys speak doing cool things with language translation.

**Speaker 17** [00:00:00] Like, we're beginning to see this stuff work, and I think it's really gonna start working as we,

**Sam Altman** [00:00:00] as we continue to iterate these models. One of the very fun things for us about having this development platform is just getting to, like, watch the unbelievable speed and creativity of people that are building these experiences.

**Sam Altman** [00:00:00] Like, developers, very near and dear to our heart it's kind of like the first thing we watched. And it's brilliant. Many of us came building on platforms, but the, so much of the capability of these models and great experiences have been built by people building on the platform. We'll continue to try to offer, like, great first party products, but we know that will only ever be, like, a small, narrow slice of the apps or agents or whatever people build in the world, and seeing what has happened in the world in the last, you know, 18 24 months.

**Sam Altman** [00:00:00] It's been like quite amazing to watch.

**Speaker 17** [00:00:00] We'll keep going on the agent front here. What do you see as the current hurdles for computer

**Sam Altman** [00:00:00] controlling agents? Safety and alignment. Like, if you are really going to give an agent the ability to start clicking around your computer which you will. You are going to have a very high bar for The robustness and the reliability and the alignment of that system.

**Sam Altman** [00:00:00] So technically speaking, I think that, you know, we're getting, like, pretty close to the capability side. But the sort of agent safety and trust framework, that's gonna, I think, be the long haul.

**Speaker 17** [00:00:00] And now I'll kind of ask a question that's almost the opposite of one of the questions from earlier. Do you think safety could act as a false positive and actually limit public access to critical tools that would enable a more egalitarian world?

**Sam Altman** [00:00:00] The honest answer is yes, that will happen sometimes. Like, we'll try to get the balance right. But if we were fully alone and didn't care about, like, safety and alignment at all, could we have launched O1 faster? Yeah, we could have done that. It would have come at a cost. There would have been things that would have gone really wrong.

**Sam Altman** [00:00:00] I'm very proud that we didn't. The cost, you know, I think would have been manageable with O1, but by the time of O3 or whatever, like, immediately. Pretty unacceptable. And so, starting on the conservative side, like, you know, I don't think people are complaining, like, oh, voice mode, like, it won't say this offensive thing, and I really want it to, and, you know, formal comedy, and let it offend me.

**Sam Altman** [00:00:00] You know what? I actually mostly agree. If you are trying to get O1 to say something offensive, it should follow the instructions of its user most of the time. There's plenty of cases where it shouldn't. But, we have, like, a long history of when we put a new technology in. We change the world, we start on the conservative side.

**Sam Altman** [00:00:00] We try to give society time to adapt, we try to understand where the real harms are versus sort of like, kind of more theoretical ones. And that's like, part of our approach to safety. And, not everyone likes it all the time, I don't even like it all the time. But, but if we're right that these systems are, and we're gonna get it wrong too, like sometimes we won't be conservative enough in some area.

**Sam Altman** [00:00:00] But if we're right that these systems are going to get as powerful as we think they are. as quickly as we think they might, then I think starting that way makes sense. And, you know, we like to relax over time. Totally agree. What's

**Speaker 17** [00:00:00] the next big challenge for a startup that's using AI as a core feature?

**Speaker 17** [00:00:00] I'll say it. You first. I've got it. I've got one, which is, I think one of the challenges, and we face this too, because we're also building products on top of our own models, is trying to find the, kind of the frontier. You want to be building, these AI models are evolving so rapidly, and if you're building for something that the AI model does well today, it'll work well today, but it's going to feel, it's going to feel old tomorrow.

**Speaker 17** [00:00:00] And so you want to build for, for things that the AI model can just barely not do. You know, where maybe the early adopters will go for it and other people won't quite, but that just means that when the next model comes out, as we continue to make improvements, that use case that just barely didn't work, you're gonna be, you're gonna be the first to do it, and it's gonna be amazing.

**Speaker 17** [00:00:00] But figuring out that boundary is really hard. I think it's where the best products are gonna get built up.

**Speaker 17** [00:00:00] Totally agree with that. The other

**Sam Altman** [00:00:00] thing I'm gonna add is, I think it's like, very tempting to think that a technology makes a startup. And that is almost never true. No matter how cool a new technology or a new sort of like, tech title is, it doesn't excuse you from having to do all the hard work of building a great company that is going to have durability or like, accumulated advantage over time.

**Sam Altman** [00:00:00] And, we hear from a lot of startups that ORC is just like a very common thing, which is like, I can do this incredible thing, I can make this incredible service And that seems like a complete answer, but it doesn't excuse you from any of, like, the normal laws of business. You still have to, like, build a good business and a good strategic position.

**Sam Altman** [00:00:00] And I think a mistake is that in the unbelievable excitement and updraft of AI, people are very tempted to forget that.

**Speaker 17** [00:00:00] This is a, this is an interesting one. The mode of voice is like tapping directly into the human API. How do you ensure ethical use of such a powerful tool with obvious abilities and manipulation?

**Speaker 17** [00:00:00] Yeah, you

**Sam Altman** [00:00:00] know, voice mode was a really interesting one for me. It was like the first time that I felt like I sort of had gotten like really tricked by an AI, in that when I was playing with the first beta of it, I couldn't like, I couldn't stop myself. I mean, I kind of, like I still say like, please switch out GBT.

**Sam Altman** [00:00:00] But in voice code, I like, couldn't not kind of use the normal ICDs. I was like so convinced, like, ah, it might be a real per like, you know? And obviously it's just like hacking some circuit in my brain, but I really felt it with voice code. And I sort of still do The, I think this is a more, this is an example of like a more general thing that we're going to start facing, which is, as these systems become more and more capable, and as we try to make them as natural as possible to interact with they're gonna like, hit parts of our neural circuitry that would like evolve to deal with other people.

**Sam Altman** [00:00:00] And You know, there's like a bunch of clear lines about things we don't want to do, like, we don't. Like, there's a whole bunch of like weird personality growth hacking, like, I think vaguely socially manipulative stuff we could do. But then there's these like other things that are just not nearly as clear cut.

**Sam Altman** [00:00:00] Like, you want the voice mode to feel as natural as possible, but then you get across the uncanny valley, and it like, at least in me, triggers something. And and, you know, me saying, like, please and thank you to chat. gt, no problem. Probably the thing to do. You never know. But, but I think this like really points at the kinds of safety and alignment issues we have to start analyzing.

**Speaker 17** [00:00:00] Alright, back to brass tacks. Sam, when's O1 going to support function tools? Do you know? Before the end of the year. There are three things that we really want to get in for

**Speaker 17** [00:00:00] We're gonna record this, take this back to the research team, show them how badly we need to do this. There, I mean, there are a handful of things that we really wanted to get into O1, and we also, you know, it's a balance of should we get this out to the world earlier and begin, you know, learning from it, learning from how you all use it, or should we launch a fully complete thing that is, you know, in line with it, that has all the abilities that every other model that we've launched has.

**Speaker 17** [00:00:00] I'm really excited to see things like system properties. and structured outputs and function calling make it into O1, we will be there by the end of the year. It really matters to us too.

**Sam Altman** [00:00:00] In addition to that, just because I can't resist the opportunity to reinforce this, like, we will get all of those things in and a whole bunch more things you'll have asked for.

**Sam Altman** [00:00:00] The model is going to get so much better so fast. Like, we are so early, this is like, you know, maybe it's the GPT 2 scale moment, but like, we know how to get to GPT 4, we have the fundamental stuff in place now to 4. And, in addition to planning for us to build all of those things, Plan for the model to just get, like, rapidly smarter, like, you know, hope you all come back next year and plan for it to feel like way more of a year of improvement than from 4.

**Sam Altman** [00:00:00] 0. 1.

**Speaker 17** [00:00:00] What feature or capability of a competitor do you really admire? I

**Sam Altman** [00:00:00] think Google's notebook thing is super cool. What are they called? Notebook LL. Notebook LL, yeah. I was like, I woke up early this morning and I was like looking at examples on Twitter and I was just like, this is like, this is just cool.

**Sam Altman** [00:00:00] This is just a good, cool thing. And, like, I think not enough of, not enough of the world is like shipping new and different things, it's mostly like the same stuff. But that I think is like, that brought me a lot of joy this morning.

**Speaker 17** [00:00:00] Yeah. It was very, very well done. One of the things I really appreciate about that product is the, there's the, the, just the format itself is really interesting, but they also nailed the podcast style voices.

**Speaker 17** [00:00:00] They have really nice microphones. They have these sort of sonorant voices. As you guys see, somebody on Twitter was saying like, the cool thing to do is take your LinkedIn and put it, you know, gimme a hit, and give it to these give it to notebook. lm and you'll have two podcasters riffing back and forth about how amazing you are and all of your accomplishments over the years.

**Speaker 17** [00:00:00] I'll say mine is I think Anthropic did a really good job. On projects it's kind of a, a different take on what we did with GBTs and GBTs are a little bit more long lived. It's something you build and can use over and over again. Projects are kind of the same idea, but like more temporary, meant to be kind of stood up, used for a while, and then you can move on.

**Speaker 17** [00:00:00] And that, that the different mental model makes a difference. And I think they did a really nice job with that.

**Speaker 17** [00:00:00] Alright, we're getting close to audience questions, so be thinking of what you want to ask. So in OpenAI, how do you balance what you think users may need? Versus what they actually need today.

**Sam Altman** [00:00:00] Also a better question for you.

**Speaker 17** [00:00:00] Yeah, well, I think it does get back to a bit of what we were saying around trying to, trying to build for what the model can just, like, not quite do, but almost do.

**Speaker 17** [00:00:00] But it's a real balance, too, as we, as we, you know, we support over 200 million people every week on ChatGPT. You also can't say, Now it's cool, like, deal with this bug for three months, or this issue we've got something really cool coming. You've gotta solve for the needs of today. And there are some really interesting product problems.

**Speaker 17** [00:00:00] I mean, you think about, I'm speaking to a group of people who know AI really well. Think of all the people in the world who have never used any of these products. And that is the vast majority of the world still. You're basically giving them a text interface, and on the other side of the text interface is this like alien intelligence that's constantly evolving that they've never seen or interacted with, and you're trying to teach them all the crazy things that you can actually do it, all the ways it can help, can integrate into your life, can solve problems for you.

**Speaker 17** [00:00:00] And people don't know what to do with it. You know, like, you come in and you're just like, people type like, Hi. And in response, you know, hey! Great to see you, like, how can I help you today? And then, you're like, okay, I don't know what to say. And then you end up, you kind of walk away, and you're like, well, I didn't see the magic in that.

**Speaker 17** [00:00:00] And so it's a real challenge, figuring out how You, I mean, we all have a hundred different ways that we use chat GPT and AI tools in general, but teaching people what those can be, and then bringing them along as the model changes month by month by month, and suddenly gains these capabilities way faster than we as humans gain the capabilities, it's, it's a really interesting set of problems, and I'm I know it's one that you all solve in, in different ways as well.

**Speaker 17** [00:00:00] I,

**Sam Altman** [00:00:00] I

**Speaker 17** [00:00:00] have

**Sam Altman** [00:00:00] a question. Who feels like they, they spend a lot of time with O1, and they would say like, I feel definitively smarter than that thing?

**Sam Altman** [00:00:00] Do you think you still go by O2? No one, no one taking the bet of like being smarter than O2. So, One of the challenges that we face is, like, we know how to go do this thing that we think will be, like, at least probably smarter than all of us in, like, a broad array of tasks. And yet we have to, like, still like fixed bugs and do the, hey, how are you problem.

**Sam Altman** [00:00:00] And mostly what we believe in is that if we keep pushing on model intelligence people will do incredible things with that. You know, we want to build the smartest, most helpful models in the world, and And find all sorts of ways to use that and build on top of that. It has been definitely an evolution for us, to not just be entirely research focused, and we do have to fix all those bugs and make this super usable and I think we've gotten better at balancing that.

**Sam Altman** [00:00:00] But still, as part of our culture, I think, we trust that if we can keep pushing on intelligence, 6. 0. 4 if you run down here it'll, people will build this incredible thing. Yeah,

**Speaker 17** [00:00:00] I think it's a core part of the philosophy, and you do a good job of pushing us to always, well, basically incorporate the frontier of intelligence into our products, both in the APIs and into our first party products.

**Speaker 17** [00:00:00] Because it's, it's easy to kind of stick to the thing you know, the thing that works well, but you're always pushing us to like, get the frontier in, even if it only kind of works, because it's going to work really well soon. So I always find that a really helpful piece of advice. You kind of answered the next one.

**Speaker 17** [00:00:00] You do say, please and thank you to the models. I'm curious how many people say Please and thank you. Isn't that so interesting? I do too. . I kind of can't. I feel bad if I don't. And,

**Speaker 17** [00:00:00] okay, last question and then we'll go into audience questions for the last 10 or so minutes. Do you plan to build models specifically made for ag agent use cases, things that are better at reasoning and tool calling.

**Sam Altman** [00:00:00] Specific, we plan to make models that are great at agentive use cases, that'll be a key priority for us over the coming months.

**Sam Altman** [00:00:00] Specifically is a hard thing to ask for, because I think it's also just how we keep making smarter models. So yes, there's like some things like tool use, function calling that we need to build in that'll help, but mostly we just want to make the best reasoning models in the world. Those will also be the best agentive based models in the world.

**Sam Altman** [00:00:00] Cool, let's

**Speaker 17** [00:00:00] go to audience questions.

**Unkown** [00:00:00] How extensively do you dogfood your own technology in your company? Do you have any interesting examples that may not be obvious?

**Sam Altman** [00:00:00] Yeah I mean we put models up for internal use even before they're done training. We use checkpoints and try to have people use them for whatever they can, and try to sort of like build new ways to explore the capability of the model internally, and use them for our own development.

**Sam Altman** [00:00:00] Element or research or whatever else, as much as we can, we're still always surprised by the creativity of the outside world and what people do. But basically the way we have figured out every step along our way of how to, what to push on next, what we can productize, what, what, what, like, what the models are really good at is by internal dog food.

**Sam Altman** [00:00:00] That's like our whole, that's how we like, feel our way through this.

**Sam Altman** [00:00:00] We don't yet have like. Employees that are based off of O1, but, I, you know, as we like move into the world of agents, we will try that. Like, we'll try having like, you know, things that we deploy in our internal systems that help you with stuff. There are things that get

**Speaker 17** [00:00:00] closer to that, I mean, they're like, customer service, we have bots internally, that do a ton about answering external questions and fielding internal people's questions on Slack and so on.

**Speaker 17** [00:00:00] And our customer service team is probably I don't know, 20 percent the size it might otherwise need to be because of it. I know Matt Knight and our security team has talked extensively about all the different ways we use models internally for, to automate a bunch of security things and, you know, take what used to be a manual process where you might not have The number of humans to even, like, look at everything incoming, and have models taking, you know, separating signal from noise, and highlighting to humans what they need to go look at, things like that.

**Speaker 17** [00:00:00] So, I think internally there are tons of examples, and people maybe underestimate the You all probably will not be surprised by this, but a lot of folks that I talk to are. The extent to which it's not just using a model in a place, it's actually about using, like chains of models that are good at doing different things and connecting them all together to get one end to end process that is very good at the thing you're doing, even if the individual models have You know, flaws and make mistakes.

**Unknown** [00:00:00] Thank you. I'm wondering if you guys have any plans on sharing models for like offline usage? Because with this distillation thing, it's really cool that we can share our own models, but a lot of use cases you really want kind of like have a version of it.

**Sam Altman** [00:00:00] We're open to it. It's not on, it's not like high priority on the current roadmap. The, if we had, like, more resources and bandwidth, we would go to that. I think there's a lot of reasons you want a local model. But it's not like, it's not like a this year kind of thing.

**Unknown** [00:00:00] Hi. My question is, there are many agencies in the government, above the local, state, and national level, that could really greatly benefit from the tools that you guys are developing, but I have perhaps some hesitancy on deploying them because of, you know, security concerns, data concerns, privacy concerns.

**Unknown** [00:00:00] And, I guess, I'm curious to know if there are any sort of, you know, planned partnerships with governments, rural governments, once whatever AGI is achieved. Because obviously AGI can help. Solve problems like, you know, world hunger, poverty, climate change. Government's gonna have to get involved with that, right?

**Unknown** [00:00:00] And I'm just curious to know if there is some you know, plan that works when, and if that time comes.

**Speaker 17** [00:00:00] Yeah, I think, I actually think you don't want to wait until AGI. You want to start now, right? Because there's a learning process, and there's a lot of good that we can do with our current models. So we We've announced a handful of partnerships with government agencies, some states, I think Minnesota, and some others, Pennsylvania, Also with organizations like USAID.

**Speaker 17** [00:00:00] It's actually a huge priority of ours to be able to help governments around the world get acclimated, get benefit from the technology, And of all places, government feels like somewhere where you can automate a bunch of workflows and make things more efficient, reduce drudgery, and so on. So I think there's a huge amount of good we can do now.

**Speaker 17** [00:00:00] And if we do that now It just accrues over the long run as the models get better and we get closer to AGI. I've got

**Vibhu Sapra** [00:00:00] pretty open ended question. What are your thoughts on open source? So, whether that's open weights, just general discussion, where do you guys sit with open source?

**Sam Altman** [00:00:00] I think open source is awesome. Again, if we had more bandwidth, we would do that too. We've, like, gotten very close to making a big open source effort a few times.

**Sam Altman** [00:00:00] And then, you know, the really hard part is prioritization. And we have put other things ahead of it. Part of it is, like, there's such good open source models in the world now that I think that segment The thing we always end in motion A really great on device model. And I think that segment is fairly well served.

**Sam Altman** [00:00:00] I do hope we do something at some point, but we want to find something that we feel like, if we don't do it, then we'll just be the same as them and not make, like, another thing that's, like, a tiny bit better on benchmarks. Because we think there's, like, a lot of potential. A lot of good stuff out there now.

**Sam Altman** [00:00:00] But, but like, spiritually, philosophically, I'm very glad it exists. I would

**Alex Volkov** [00:00:00] like to

**Sam Altman** [00:00:00] contribute.

**Alex Volkov** [00:00:00] Hi Shane. Hi Kevin. Thanks for inviting us. Good dev day. It's been awesome. All the live demos work. It's incredible. Why can't advanced voice mode sing? And as a follow up to this, if it's a company, like, legal issue in terms of corporate, et cetera, Is there a daylight between how you think about safety in terms of your own products, on your own platform, Versus giving us developers kind of the I don't know, sign the right things off so we can, we can make our voice not sing.

**Alex Volkov** [00:00:00] Could you answer the question?

**Speaker 17** [00:00:00] Oh, you know the funny thing is Sam asked the same question. Why can't this thing sing? I want it to sing. I've seen it sing before. It's, actually, it's there are things, obviously, that we can't have it sing, right? We can't have it sing copyrighted songs, we don't have the licenses, etc.

**Speaker 17** [00:00:00] And then there are things that it can't sing, and you can have it sing Happy Birthday, and that would be just fine, right? And we want that too. It's a matter of, I think, once you, it, basically, it's easier in finite time to Say no, and then build it in, but it's nuanced to get it right, and we, you know, There are penalties to getting these kinds of things wrong.

**Speaker 17** [00:00:00] So it's really just where we are now. We really want the models to sync too.

**Sam Altman** [00:00:00] We waited for us to ship voice mode, which is like, very fair. We could've like, waited longer and kind of really got the classifications and filters on, you know, congregated music versus not, but we decided we'd just ship it and we'll have more. But I think Sam has asked me like, four or five times why we didn't have

**Speaker 17** [00:00:00] voice

**Sam Altman** [00:00:00] feature.

**Sam Altman** [00:00:00] I mean, we still can't like, offer something where we're gonna be in like, pretty badly. You know, hot water developers or first party or whatever. Yes, we can, like, maybe have some differences, but we like, comply with the law.

**Unknown** [00:00:00] Could you speak a little to the future of where you see context windows going? And kind of the timeline for when, how you see things balance between context window growth and RAG, basically, information retrieval.

**Sam Altman** [00:00:00] I think there's, like, two different Takes on that the better. One is like, when is it going to get to like, kind of normal long context?

**Sam Altman** [00:00:00] Like, context length 10 million or whatever, like long enough that you just throw stuff in there, and it's fast enough you're happy about it. And I expect everybody's going to make pretty fast progress there, and that'll just be a thing. Long context has gotten weirdly less usage than I would have expected so far.

**Sam Altman** [00:00:00] But I think, you know, there's a bunch of reasons for that, I don't want to go too much into it. And then there's this other question of, like, when do we get to context length? Not like 10 million, but 10 trillion. Like, when do we get to the point where you throw, like, every piece of data you've ever seen in your entire life in there?

**Sam Altman** [00:00:00] And you know, like, that's a whole different set of things. That obviously takes some research breakthroughs. But I assume that infinite context will happen at some point. And some point is, like, less than a decade. And that's going to be just a totally different way that we use these models. Even getting to the, like, 10 million tokens of very fast and accurate context, which I expect to measure in, like, months, something like that.

**Sam Altman** [00:00:00] You know, like, people will use that in all sorts of ways. And it'll be great. But yeah, the very, very long context, I think, is gonna happen, and it's really interesting. I think we maybe have time for one or two

**Speaker 17** [00:00:00] more.

**Alex Volkov** [00:00:00] Don't worry, this is gonna be your favorite question. So, with voice, and all the other changes that users have experienced since you all have launched your technology, what do you see is the vision?

**Alex Volkov** [00:00:00] for the new engagement layer, the form factor, and how we actually engage with this technology to make our lives so much better.

**Speaker 17** [00:00:00] I love that question. It's one that we ask ourselves a lot, frankly. There's this, and I think it's one where developers can play a really big part here because there's this trade off between generality and specificity here.

**Speaker 17** [00:00:00] I'll give you an example. I was in Seoul and, and Tokyo. A few weeks ago, and I was in a number of conversations with folks that, with whom I didn't have a common language, and we didn't have a translator around. Before, we would not have been able to have a conversation. We would have just sort of smiled at each other and continued on.

**Speaker 17** [00:00:00] I took out my phone, I said, JGPT, I want you to be Translator for me, when I speak in English, I want you to speak in Korean, you hear Korean, and I want you to repeat it in English. And I was able to have a full business conversation, and it was amazing. You think about the impact that could have, not just for business, but think about travel and tourism and people's willingness to go places where they might not have a word of the language.

**Speaker 17** [00:00:00] You can have these really amazing impacts, but inside ChetGBT, that was still a thing that I had to, like, ChetGBT is not optimized for that, right? Like, you want this sort of digital, you know, universal translator in your pocket that just knows that what you want to do is translate. Not that hard to build.

**Speaker 17** [00:00:00] But I think there's, we struggle with the, with trying to build an application that can do lots of things for lots of people. And it keeps up, like we've been talking about a few times, it keeps up with the pace of change and with the capabilities, you know, agentive capabilities and so on. I think there's also a huge opportunity for the creativity of an audience like this to come in and like, Solve problems that we're not thinking of, that we don't have the expertise to do, And ultimately the world is a much better place if we get more AI to more people, And it's why we are so proud to serve all of you.

**Sam Altman** [00:00:00] The only thing I would add is, if you just think about everything that's gonna come together, At some point, in not that many years in the future, you'll walk up to a piece of glass, You will say whatever you want they will have like, There'll be incredible reasoning models, agents connected to everything, there'll be a video model Streaming back to you like a custom interface just for you.

**Sam Altman** [00:00:00] This is one request. Whatever you need, it's just gonna get, like, rendered in real time, and you'll be able to interact with it, you'll be able to, like, click through the stream, or say different things, and it'll be off doing, like, again, the kinds of things that used to take, like, humans years to figure out.

**Sam Altman** [00:00:00] And, it'll just You know, dynamically render whatever you need, and it'll be a completely different way of using a computer. And also getting things to happen in the world. That, it's gonna be quite a while.

**Speaker 17** [00:00:00] Awesome. Thank you. That was a great question to end on. I think we're out of time. Thank you so much for coming.

**Speaker 17** [00:00:00] Applause

**AI Charlie** [00:00:00] That's all for our coverage of Dev Day 2024. We want to extend an extra special note of gratitude to Lindsay McCallum of the OpenAI Comms team, who helped us set up so many interviews at very short notice, and physically helped ensure the smooth continuity of the video recordings. We couldn't do this without you, Lindsay.

**AI Charlie** [00:00:00] If you have any feedback on the launches or for our guests, hop on over to our YouTube or Substack comments section and say hi. We're especially interested in your personal feedback and demos built with the new things launched this week. Feel the AGI.

## [02:03:07] Notebook LM Recap of Podcast

**NotebookLM 2** [00:00:00] Alright, so you wanted to know more about OpenAI's Dev Day and what stood out to us. We're diving into all the developer interviews and discussions and there's a lot to unpack.

**NotebookLM** [00:00:00] Yeah, it's interesting. OpenAI seems to be, like, transitioning, moving beyond just building these impressive AI models. One expert even called them, get this, the AWS of AI.

**NotebookLM 2** [00:00:00] EWS of AI.

**NotebookLM** [00:00:00] Yeah.

**NotebookLM 2** [00:00:00] Okay, so what does that even mean when we talk about AI?

**NotebookLM** [00:00:00] So it means, instead of just offering this raw power, they're building a whole ecosystem. The tools to fine tune those models. Distillation, you know, for efficiency. And a bunch of new evaluation tools. Oh, and a huge emphasis on real time capabilities.

**NotebookLM** [00:00:00] You

**NotebookLM 2** [00:00:00] know, instead of just giving us the ingredients, it's like they're providing the whole kitchen.

**NotebookLM** [00:00:00] Exactly. They're laying the groundwork for, well, they envision a future where you can build almost anything with AI.

**NotebookLM 2** [00:00:00] I see. And one of the tools that really caught my eye was this function calling. They used it in that travel agent demo, remember?

**NotebookLM 2** [00:00:00] How does that even work?

**NotebookLM** [00:00:00] So function calling, it's like giving the AI access to external tools and information. Imagine, instead of just having all this pre programmed knowledge, you can like, search the web for you, book flights, even order a pizza.

**NotebookLM 2** [00:00:00] So instead of a static encyclopedia, it's like giving the AI a smartphone with internet.

**NotebookLM** [00:00:00] Yeah, precisely. Yeah. And this ties into their focus on real time interaction, right? They see a future where AI can respond instantly, just like a human would.

**NotebookLM 2** [00:00:00] Which would be a game changer.

**NotebookLM** [00:00:00] Right! It's like, imagine voice assistants that actually understand you. Or, even seamless real time translation.

**NotebookLM 2** [00:00:00] No more language barriers.

**NotebookLM** [00:00:00] Exactly. That's just the tip of the iceberg, though. They really believe this real time capability is key to making AR truly mainstream.

**NotebookLM 2** [00:00:00] Okay, so OpenAI is building this AI platform, emphasizing real time interactions. How does this translate into, like, actual results?

**NotebookLM** [00:00:00] Yeah.

**NotebookLM 2** [00:00:00] You know, real world stuff.

**NotebookLM** [00:00:00] Well, that's where things get really interesting.

**NotebookLM** [00:00:00] Let's talk about the O1 model and how developers are using it to, like, really push the boundaries of what's possible.

**NotebookLM 2** [00:00:00] So this O1 model, everyone's talking about it. One developer even said they built an entire iPhone app just by describing it as O1. Is that just hype?

**NotebookLM** [00:00:00] I think there's definitely some substance behind all the hype.

**NotebookLM** [00:00:00] What's so fascinating about O1, it's not just about the code it generates, it's how it seems to understand, like, the logic. The

**Alex Volkov** [00:00:00] logic.

**NotebookLM** [00:00:00] Yeah. Like, this developer They didn't give O1 lines of code, they described the idea of the app. And O1, it actually designed the architecture, connected everything, the developer just took that code, put it right into Xcode, and it worked.

**NotebookLM 2** [00:00:00] Wow, so it's not just writing code, it's understanding the intent.

**NotebookLM** [00:00:00] Yeah, exactly. And this actually challenges how we measure these models, you know, even OpenAI admitted that these benchmarks, like what was it? Swebench.

**NotebookLM 2** [00:00:00] Swebench.

**NotebookLM** [00:00:00] Right, which looks at code accuracy. It doesn't always reflect how things work in the real world.

**NotebookLM 2** [00:00:00] Right, because in the real world, you don't just need code that compiles. It has to be, like, efficient, maintainable.

**NotebookLM** [00:00:00] Exactly. It all has to work together, and OpenAI is really working on this with developers. They're finding that UI development, especially in things like React, it needs better evaluation.

**NotebookLM** [00:00:00] It's one thing to code a button that works, and another to make it actually look good, you know, and be intuitive.

**NotebookLM 2** [00:00:00] Right, and it seems like this need for real world context, It goes beyond just, like, evaluating those models. There was a developer working with this code generating AI genie, I think it was called.

**NotebookLM** [00:00:00] Genie, yeah.

**NotebookLM 2** [00:00:00] And it's more focused on those specific coding tasks, but they found that its performance really changed between different programming languages, like JavaScript versus C Sharp, for example.

**NotebookLM** [00:00:00] And that just highlights how important the data is, right? Just like us, AI needs that variety to learn.

**NotebookLM** [00:00:00] If you train it on just one type of code, it'll be great at that. But anything new and It'll fall flat. Yeah. So it's about making sure these models have a broad diet of data to learn from. That way they're more adaptable and ready for whatever we throw at them.

**NotebookLM 2** [00:00:00] So we've got AI that can build apps, understand what we want, even write different kinds of code.

**NotebookLM 2** [00:00:00] It's a lot, and it feels like things are changing so fast. How can developers even keep up, let alone, like, build something successful with AI?

**NotebookLM** [00:00:00] Right. That's the question, isn't it? But it's interesting, you know, both OpenAI and the developers building with these tools, they kind of agree on one thing. You got to aim for what's just out of reach.

**NotebookLM 2** [00:00:00] So don't wait for the tech to catch up to your Like, wildest dreams. Focus on what's almost possible right now.

**NotebookLM** [00:00:00] Yeah. Build for where things are going, not where they are today. You wait for that perfect AI, you might miss the boat on shaping how it develops, and being the first one out there doing something new.

**NotebookLM 2** [00:00:00] Riding the wave, not chasing after it.

**NotebookLM** [00:00:00] Exactly. But, and OpenAI really emphasized this too, Even with all this amazing AI, you can't forget the basics of building a business.

**NotebookLM 2** [00:00:00] So just because it's got AI doesn't mean it's automatically going to be a success. Right.

**NotebookLM** [00:00:00] You need a good strategy, know who you're selling to, and it's got to actually solve a real problem.

**NotebookLM** [00:00:00] AI is a tool, not a magic wand.

**NotebookLM 2** [00:00:00] Like, having the best oven in the world won't help if you don't know how to cook.

**NotebookLM** [00:00:00] Perfect analogy. And then there's this other thing OpenAI talked about that's really interesting. Balancing safety with access for everyone.

**NotebookLM 2** [00:00:00] So making sure these AI tools are used responsibly, but also making them available to everyone who could benefit.

**NotebookLM** [00:00:00] Yeah, they're really aware that focusing on safety, while important, could limit access to some really powerful stuff. It's a tough balance.

**NotebookLM 2** [00:00:00] It's like that debate around, you know, life saving medications. How do you make sure they're used correctly, but also make sure people who need them can actually get them?

**NotebookLM** [00:00:00] It's complicated, no easy answers. But it's something they're thinking hard about.

**NotebookLM 2** [00:00:00] Well, it's clear that all this AI stuff, especially with these new models like O1, is changing how we think about tech, how we use it.

**NotebookLM** [00:00:00] Imagine walking up to a screen, and it just creates a personalized experience for you, right there, adapts to what you need.

**NotebookLM** [00:00:00] That's the potential.

**NotebookLM 2** [00:00:00] Like having a personal assistant in every device.

**NotebookLM** [00:00:00] It's exciting, but we got to be thoughtful about it, build responsibly.

**NotebookLM 2** [00:00:00] So there you have it. OpenAI isn't just building these cool AI models, they're building a whole world around them and it's changing everything. It's going to be a wild ride, that's for sure.

**NotebookLM 2** [00:00:00] And we're just at the beginning.
