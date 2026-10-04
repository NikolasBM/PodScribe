---
podcast: "ai-daily-brief"
podcast_title: "The AI Daily Brief"
title: "How the 4 New AI Models Change How You Work"
date: 2026-07-09
url: "https://aidailybrief.ai/e/2026-07-09"
guid: "https://aidailybrief.ai/e/2026-07-09"
host: "Nathaniel Whittemore"
format: "news-analysis"
level: 2
length: "00:34:00"
categories: ["models", "coding", "agents", "model-strategy"]
featured: ["GPT Live", "Grok", "OpenAI", "GPT-5.6", "ChatGPT", "Claude Fable", "computer use"]
mentioned: ["Cursor", "Kimi", "Claude Opus", "GPT-6", "GPT-5.5", "GLM", "Claude Tag", "Claude", "Slack", "OpenAI Codex", "Artificial Analysis", "Claude Code", "open-weight models", "Cognition Devin", "Claude Mythos"]
transcript_source: "publisher"
---

# How the 4 New AI Models Change How You Work

[00:00:00] Today Today on the AI Daily Brief, how the how the count 'em four new models we got access to this week will change how you work. The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI. All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, AI. All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, Robots and Pencils, Blitzy, and Airtable.

To get an ad-free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts. And if you wanna learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai. Welcome back to the AI Daily Brief

Among the Among the many changes that AI is bringing to the professional world



one of them is an almost total obliteration



of the previously agreed upon idea that you could actually slow down a little bit over the warm summer months

While not While not every white-collar professional would agree that July and August are a time, for resting and [00:01:00] vacations and catching up

It's pretty undeniable that it's a season where things quiet down a bit. Except Except in AI land, where almost especially now that the previous cadence was thrown off by the government's interference We are in for what I believe will just be an absolute cavalcade of models, many of which, as you'll see, I think have fairly significant implications for how we work



The month of models got off to a big start with the return of Fable, which while yes, of course, technically was released in June, for all intents and purposes, for most of us, 

It actually feels like an early July release. And yet this week, we added a whole new slate of models to the roster



including OpenAI's first answer to Fable, 5.6 Sol



a new entrant from Groq, their first since they hooked up with Cursor called Groq A new A new model from Cognition, which continues a trend that we saw with Cursor and Composer And finally, And finally, the model that we're going to start with today

GPT Live



now you now you might have seen this announcement floating around social media

It's It's a set of cute and charismatic [00:02:00] grannies talking to ChatGPT's new live model in a way that's meant to represent just how much more natural and conversational the new model feels



now now this is not at all the main point of the show, but it is worth noting as a side story



That I think and many think that this content was some of the more effective we've seen from OpenAI. Not Boring's Packy McCormick wrote: " " The OpenAI just be normal strategy is working beautifully. Bonus points for making the ladies look very smart and sophisticated and clearly putting them in control of the conversation/interrupting/even being kinda rude with chat



Now that particular choice I also think reflects one of the big underlying points of this announcement which is an evolution in how they imagine consumers interacting with AI. We'll We'll come to that in just a minute, though. Let's talk about the actual model that was released first.

The model is called GPT Live, and it comes in two flavors GPT Live 1

and GPT Live Mini

It It is built on what they call a full duplex architecture, meaning OpenAI says that it can listen and speak at the same time



and a and a big part of the emphasis here is in how the interaction model has changed. the earliest versions of ChatGPT Voice were built on something called [00:03:00] a cascaded voice system

Basically 

that model was actually three models chained together. The user would speak, and then a speech-to-text model would transcribe that speech. An LLM in the background would produce a response and then a text-to-speech model would convert it back into speech



this approach OpenAI wrote, "Enabled us to talk to frontier AI models for the first time, but the complexity came at a cost. Information could be lost across models, and responses were slow and stilted."

Now the next version

which was built into ChatGPT advanced voice mode, was was a turn-based model system. It It generated audio within a single model, As in it didn't have to go through that speech-to-text and text-to-speech translation which made a big difference in terms of latency, but it still operated in a discrete turn-based way.

I.e., the model had to wait for the user to stop speaking before it started, which created all sorts of challenges because when turn detection was based on silence, something like a brief pause in thought or background noise could be mistaken for the end of the user talking Which could lead to the model interrupting in weird ways, keeping things feeling stilted and not all that natural

The [00:04:00] The new model makes two big architectural changes. The first is that full duplex architecture, which means that GPT Live, they say, is built for continuous interactions. " "Instead Instead of processing a sequence of separate messages," they write, "GPT Live continuously processes input while generating output."

The model they say can therefore make interaction decisions many times per second, whether to speak, continue listening, pause, interrupt, or invoke a tool



And And as you can hear from all of the different tests and videos they shared, this makes for a conversational experience that's a lot closer to what you get when you're interacting in a normal human-to-human conversation

The The second architectural decision

is that they separated GPT Live as a model which has its focus on continuous interaction from deeper types of work, including reasoning, agentic capabilities or search

So basically as the GPT Live model is doing that interaction It can summon another model like GPT 5.5 or now going forward 5.6 to go take care of a task like searching or reasoning, even as it keeps the conversation going



now you now you might remember a couple months ago when Thinking Machines Labs introduced their interaction model

[00:05:00] 

that took a pretty similar approach here

Riley Brown, in fact, wrote, " this graphic this graphic from Thinking Machine seems relevant to the GPT voice release. They are, from my understanding, very similar. Real-time voice models have an interaction model that can run background models that use tools. You You don't need to wait for the voice model to finish doing something while talking to it.

It can just do things in the background."

Developer Daniel Vella wrote, wrote, I built I built a project with this architecture. Instead of a secondary background LLM, my project is a voice-first mini agent that delegates tasks to other agents like Hermes or OpenCode ACP. You can continuously talk with the agent while heavy task occurs in background.

Much more pleasant experience than the usual voice agents."



so in some ways what you're seeing here is a voice equivalent version of an increasingly common architectural pattern in general with advanced AI systems



that involve multiple models at the same time, and the ability for an orchestrator model

to initiate agents or sub-agents to go do some specific set of tasks that work in the background before organizing it all into a coherent single response

So So there are a couple interesting things that come up right away from the [00:06:00] demos. one of the first places that people went was just how powerful this was going to be for anything involving multiple language interactions

Live turn-less operation means, for example, that the model can translate each phrase as it's spoken Not having to wait for a break in the conversation This means the model can function much more like a human translator and less like a wooden computer. Think about when you'veThink about when you've seen a translator for a speech where the translation happens just a few seconds after the person being translated starts speaking, rather than waiting for that speaker to stop and pause at any given point



Now people also grokked very quickly, no pun intended that this seemed like a really excellent tool for language learning



Click Health Simon Smith Says that yes, indeed, for learning, this does rock. He wrote, " prac-I tried practicing Spanish with it. It can give me words in English to translate and properly critique my pronunciation. He also, though, saw that this was probably valuable for more than just language learning Noting that if there was a generic flashcard tool, we could use this for all sorts of learning

He writes, flashcards, quizzes, blackboard-like sketchpad, and so forth would just be incredible here. This thing could be an exceptional teacher."

[00:07:00] Now, one thing Now, one thing that is worth noting is that although there is not a flashcard feature specifically

The new model in ChatGPT does now have, the ability to show visual cards For things like weather, stocks, sports schedules, and more

this this suggests that the jump to something like flashcards wouldn't be all that difficult



and yet the flashcards I think are another part of the story that started with the grannies, which that is, to me, this is very clearly



the set of use cases that this is really focused on are what we might call the Siri use cases This is the basic personal assistant stuff that they assume a lot of regular people who aren't using for work, using ChatGPT for



at the, when you look at the grandma's ad again, 

A lot of the things that they ask the new model to do are the things that you've seen for the last several years people screeching about on social media because it seems like stuff that Siri should be able to do but can't

They're basically actively stress testing it along archetypal failure modes that cause user frustration, and it appears to keep functioning properly

And I think in some ways, that this sort of interaction mode, voice first, might be closer to the future of how people interact with [00:08:00] AI than the current paradigm of typing. Sam Sam Altman basically said as much, writing, " GPT Live launches today in ChatGPT.

It feels magical and real. I have always preferred typing to talking to an AI. Now I think that's going to shift." What's interesting though

is that while I think this makes a ton of sense for consumers, it's a more interesting question to ask how this might change the interaction pattern for work-based users as well

Now, Now, regular listeners will know

that one of my most common tips to getting more out of AI is to switch to a voice paradigm. Not to switch to these voice models, but to use something like Whisperflow to be able to ramble speak your inputs rather than typing them. The reason for this is pretty simple.

AI tends to live or die on the basis of the context you give it. And no matter how fast you type you almost certainly talk faster. typing also forces you into structure in a way that while it can be useful, it might not always actually be helpful to what you're trying to achieve with AI



in short, when you speak, i.e. ramble, you can provide the AI a lot more context. And at [00:09:00] this point, the vast, vast majority of my interactions with AI, even when I'm sitting at my desktop computer, are done via voice. but it's not this sort of back and forth voice mode It's just about voice as my input.



not only do I not care about having the AI speak back to me, in many applications, including the one that we built with Superintelligent that interviews people, I've I've sometimes found

that waiting for the AI to speak back can be incredibly annoying and slow Basically, Basically, your brain's ability to read a sentence and absorb it is a lot faster than having to listen to the AI talk at some mediated pace. so an interesting question I have about this new model is how it might start to interact, if at all

with people's work behaviors



And while it's early, there is some interesting feedback on that front

Early tester Daria Early tester Daria Anutmaz wrote: since the original release of voice in ChatGPT, I rarely used it." But this new version completely changed that. It has made me a frequent user. The voice is so much more natural, smooth, intelligent, and really so enjoyable to talk with. I I also tried it in my mother tongue, Turkish, including a few local [00:10:00] dialects, and it does a phenomenal job.

The simultaneous translation is impressive, but what is even more remarkable is that it captures the subtleties, rhythm, and local feeling of the language

Okay, Okay, so we have a skeptic who's starting to be converted, which was also Riley Brown's experience. He wrote, "This one was unexpected. I was not excited for voice models until I tried this one. It's very realistic, almost spooky. The coolest part, the model can search the internet fast. And if you've spent any time with GPT real-time too, you know these voice models are getting very good at using tools.

Soon, I'm guessing, you'll be able to do your email, check on business data, schedule meetings, and basically anything just by chatting with this voice model. The tech The tech is basically already there for Jarvis. The only thing left is a generative UI layer Okay, so we have here Riley

not only being a skeptic converted, but starting to see how it might start to become



Something that changes how he works,even if it's not there yet

Simon Smith again wrote, This felt like the closest I've ever seen an AI come to being a capable human-like digital assistant, Jarvis, her what have you. On the heels of my experience the past [00:11:00] two weeks with Claude Tag, it feels like we're in a transition period where AIs become more like colleagues and less like tools."

Ethan Mollick made a similar point GPT Voice is really good and much closer to the science fiction experience of talking to AI, in part because it is much smarter. That plus Claude Tag suggests emerging new modes of working with AI. Now, Claude Now, Claude Tag, you'll remember, isthe version of Claude that sits inside your Slack and has shared context across user channels, i.e.,

isn't just limited to a single user's instance of Claude

Max Weinbach wrote, " "Imagine Imagine GPT live in Codex with the thread management tools. You just chat with it, and it can delegate, read, and manage all the work going on in projects and chats. I imagine this will be a thing, and downstream of that is just controlling your entire computer with voice

Prinz had a great analogy writing, " AI is a toy. 2026, AI is a genie that lives in a bottle. If you know where to find the bottle and how to phrase your wish, then your wish shall be fulfilled. 2027, the genie has escaped the bottle and lives alongside you. It infers your wishes from context and fulfills them before you ask.

The most important skill is [00:12:00] real-time genie steering." So is So is everything different? Did everything change? not not so fast, says Gail Wiener, who wrote, " I just tried GPT Live Voice, and the voice itself is gorgeous. The pacing, the warmth, the naturalness is genuinely impressive. It sounds like someone you'd enjoy thinking with.

But the voice isn't the product. The thinking is. A beautiful voice wrapped around shallow reasoning is just a pretty face with no depth. It's pleasant to look at, but doesn't help you build. If you're looking for quick answers to questions, it's lovely. If you wanna brainstorm and work, it's not great at all."



Reinforcing that point is this video from Husk



who showed that while the voice model may have gotten smarter, it still isn't necessarily state-of-the-art when it comes to raw intelligence



So ChatGPT just had a big voice update, and this is supposed to be way smarter now and way more natural. So let's put that to the test. I have it set to the highest smart setting

Um, hey, can you tell me how many E's are in the number seventeen? Two E's, one in seven and one in teen. [00:13:00] And you're really smart, right?

Yeah, two E's and 17 And you're sure about that? 

Absolutely. S-E-V-E-N-T-E-E-N. 

That is two. I-- That's right. 

Exactly 

Now, this is obviously meant to be a bit of a meme, and the OpenAI folks took it in stride with Adi Oelatti saying, "Bro, you didn't even give us a day. JK, we love your videos." But I think that the important thing here to note is that when you look at the difference between GPT Realtime 2, the API, and GPT Live 1, and the GPT-5 class reasoning models, 

These are not just model tiers, they're interaction tiers. Realtime 2 is the smarter real-time voice model for developers. GPT Live 1 is the ChatGPT voice experience

It's a more natural, interruptible, always flowing interface that can call on GPT 5.5 behind the scenes. But if you are looking to do something like it sounds like Gail was, and something that's one of my main use cases, which is extended strategic debate, the benchmark is still going to be the underlying frontier reasoning model, not the voice [00:14:00] layer itself.



Voice models, in other words, are making a trade-off. They have to listen, decide when to interrupt, respond naturally, avoid awkward silence, and keep latency low. That's a very different optimization target from sit with the problem the user is suggesting and reason deeply

And yet still, this is one more indication that overall, even if it's not this model exactly, the interaction pattern is starting to shift

Site Bringer wrote, " GPT Live points at the moment AI stops feeling like software and starts feeling like a live cognitive presence

Text keeps AI at a distance, voice collapses that distance. Once the model can interrupt naturally, respond emotionally, follow rhythm, catch hesitation, hear uncertainty, and keep pace with human thought, the interaction starts moving from tool use into relationship use. 

now obviously there are implications here for the sort of companionship dimension of AI, which we'll probably discuss at some point in the future. but I think it would be a mistake to solely view this as a consumer shift.



Instead, I think it is part and parcel of a larger shift



whereas we delegate more and more, and more of our work becomes coordination and management Voice might be an [00:15:00] increasingly important way that we do that coordination



One of the most important AI questions right now isn't who's using ai, it's who's using it? Well,

KPMG and the University of Texas at Austin. Just to analyzed 1.4 million real workplace AI interactions and found something surprising. The highest impact users aren't better prompt engineers. They treat AI like a reasoning partner.

They frame problems, guide thinking, iterate, and push for better answers.

the the the next new model I wanna discuss is Groq 4.5. And candidly, up until very recently, specifically the announcement of the Cursor acquisition There have been a fair number of people who have thought that we might be seeing Elon moving away from owning the model layer to owning the compute layer.



certainly at some point he started to think differently about his competitive advantage by giving both Anthropic and Google and even some other companies access to Colossus and Colossus 2

Elon was clearly deciding that he was willing to play at that compute czar type of level as well And yet, one of the outcomes of SpaceX AI going public and seeing such a big pop and having success in the public markets is that they have a lot more capital to play with, and that capital becomes leverage



The completion of the Cursor acquisition was a great case in point. And Grok 4.5

is the first output of the new collaboration between SpaceX AI and Cursor

SpaceX AI called this their [00:19:00] first model trained specifically for coding in agents



and really emphasizes those engineering type of use cases Grok 4.5, they wrote, was built for real-world engineering. It excels in large code bases and handles long-running tasks that span multiple repositories, hundreds of skills, and a variety of tools

Cursor, for their part, tweeted, "It's our most powerful model yet, and the first we've built for more than software engineering."

Now for those worried that Cursor is now headed in a different direction

the main Twitter account made sure to point out that Grok 4.5 and Composer are two different model weight classes, and that not only will Composer 2.5 continue to be remain offered, but they will be releasing new models of that size going forward Cursor 2.5, you'll remember, is their model that was built on a Kimi base

And post-trained using their unique data to get high performance at a lower cost

When it comes to the benchmarks, Grok 4.5 is more or lech- is 4.8 and GPT-55 across Terminal Bench 2.1, SWE Bench Pro, and Deep SWE 1.0

On the artificial analysis index, 4.5 places fourth overall behind Fable 5, Opus 48, and GPT [00:20:00] 55. it has particularly strong performance in agentic knowledge work and coding, And also ranks fourth in GDP Val Importantly though, We continue to see that these models are no longer simply competing on the question of raw intelligence, but also on questions of efficiency

on Artificial Analysis' tests, 4.5 was by far the most cost-efficient run of the near frontier models

It cost 31 cents per task across the overall index benchmark

As compared to 180 for Opus 48 and 275 for Fable 5

for some comparisons, it was slightly cheaper than GLM 5.2 and Kimi K 2.6, and slightly more expensive than Haiku 4.5 and Nemotron 3 Ultra. Its cost per task was about a third of GPT-5 five, a fifth of Opus 4-8, and one ninth of the cost of Fable 5



effectively based on the benchmarks alone, it is very realistic to say that the model delivers near Opus performance for Haiku-level costs

Meanwhile, Groq Build seems like a big deal as well. The combination of Build and Groq 4.5 was the third best harness and model pairing on [00:21:00] AI's coding agent index, ahead of Opus 4-8 and Claude Code, and just behind GPT 5-5 in Codex and Fable 5 in Claude Code

Grok Grok 4.5 is also fully state-of-the-art on Automation Bench, which is AI's proprietary benchmark that tests a model's ability to use tools to complete a range of real-world SaaS workflows in simulated app environments like Excel, Gmail, and Slack

Essentially, Essentially, it's an agentic computer use style benchmark based in real world examples



and not only did it get the top score at 51.4% compared to, for example, Fable 5's 48.6%, it did that at 34 cents per task compared to $1.35 for Fable

It used less than half the tokens of Opus 48's run and fewer turns while using tool calls than other frontier models



But as But as we know, benchmarks can be deceiving



back back in April, YouTuber and AI entrepreneur Theo wrote, " I legitimately believe xAI might have a crazy comeback." And after testing Grok he retweeted himself and said, "Called it."



Elon Musk would actually later on retweet the video that Theo ended up producing about Grok 4.5

Where he had a lot of positive things [00:22:00] to say about the model

After After asking it to do multiple code base changes and PRs at the same time, Theo said, " "This is the This is the kind of back and forth and complex multi-target tasks that you could make most models do if you try to break them up really carefully and not try to bloat the context. I had no ergonomic issues with 4.5 at all.

It was actually really pleasant to work with. Did it find everything Fable found? No. Was its code as thorough as GPT 5.6? No. Was it able to go back and forth with me on really big, heavy tasks and be pleasant to use while also being very fast and cheap? Yeah

In In a lot of ways, I see this model, Theo concludes, as a good alternative to something like Opus and it kind of outclasses GLM 5.2. I have no interest in that model anymore, aside from it being open weights. But Grok 4.5 is a weirdly good default code model

And I think in some ways what you can view Grok 4.5 as, as the first model that self-consciously understands its relationship to the state of the art in the era of more complex model architectures. Elon Musk, who is not one for underselling, even tweeted at one point, in fairness, Fable is definitely better than Grok [00:23:00] 4.5, but most tasks don't require Fable-level capability."

And indeed, if you look across the early adopters, what they're excited about is not 4.5 replacing the top OpenAI or Anthropic model



but using it as the model for one of the implementation agents when you have Fable or GPT 5.6 acting as the orchestrator

Now this comes at an extremely important moment. Remember, yesterday's entire episode was about what happens and the unique market opportunities that arise if China decides to back off allowing their companies to continue to push state-of-the-art open weight models



for some playing around with 4.5, that question ceases to matter as they're just going to default to that instead of one of those GLM 5.2 or Kimmy K models anyway

Stonk Daddy wrote, " "Not Not sure people fully grasp what the launch of Grok 4.5 means. Enterprises are already clamping down on token spend. Chinese open source models offer strong price and performance and have gained traction, but many orgs still avoid them over data sovereignty, compliance, security, and geopolitical risks.

4.5 delivers better [00:24:00] than Chinese open source performance at near Chinese open source cost without the stigma of being Chinese open source, Western built and enterprise friendly. they are about to suck the oxygen out of the room."

And as Stong points out, " Oh, and surprise, Cursor is already in Enterprises. That Trojan horse already got Croc through the door."



now now because we are back to being absolutely spoiled with new models, we also this week got Cognition SWE 1.7



now this is closer to Cursor's composer model



Like Composer, it's built on a Kimi base, in this case, Kimi K 2.7

They point out that it's slightly better than GLM 5.2 and Composer 2.5 on the standard benchmarks, and almost as good as frontier models, but costs only around half to a third as much as those frontier models for the same tasks

Now, not as many people have had a chance to play around with SWE 1.7 yet, so it's hard to get too many first impressions of its actual performance in the real world



there were two things that I thought were interesting though about the way that the cognition folks were talking about it. first is the implications for the state of research Cognition founder Silas Alberti [00:25:00] wrote, recently the industry chatter moved from reinforcement learning to pre-training and mid-training.



RL is supposed to get diminishing returns because it hits a ceiling That depends on the quality of your pre-train. while that is certainly true, it's an open question how high the ceiling actually is. We wanted to push this to the limit. For KimiKae 2.7, which has already been heavily post-trained multiple times, it initially seemed like there wasn't much to squeeze We dealt with fast entropy collapse and many other issues.

However, we used this as a challenge to tune our algorithm and data. at some point, it suddenly started working, and the model, SWE-1.7, magically improved by much more than we expected. It also seems like the ceiling isn't obviously hit yet, so we're excited to see how much further we can push it

Cognition's Jeff Wang wrote, " "We've made We've made some awesome breakthroughs in research, such as multi-region training, self-compaction, and efficiency, as well as changing the overall behavior compared to Kimi K 2.7, the base model."

And And Ben Dickson points out that this is a broader pattern. " Application layer companies," he writes, "are using their unique access to UX data to fine-tune specialized models that perform specific tasks on [00:26:00] par with closed frontier AI models at a higher speed and at a fraction of the price." Cognition SWE 1.7 is the second application layer model that is showing promising results. Cursor's Composer series follow the same pattern. Closed frontier AI models are good for exploration. Open LLMs are the engine for scale and production

Now this is a pattern we're seeing more and more and and that we've been paying attention closely to

Now the one other thing Now the one other thing that I wanted to flag around SWUI 1.7

Is it speed?

JP Xenaware Xenaware writes, " "Just Just tried Suite 1.7 Lightning andholy crap it's fast. My eyes can't keep up up Now Now what makes this more than just a novelty is that this actually has implications once again for the interaction patterns. Last year, Sean Wang, AKA had a great graph, 

of one of the challenges for AI-enabled coding

where things worked great if you were either A

dealing with tasks that needed enough interaction that you were there and engaged, or B, on the other end of the spectrum, dealing with tasks that were complex enough that you could just delegate them entirely and go away for a while. But that in the middle There were real challenges because there was too much latency to be actually [00:27:00] real time, but not enough to go away for long, making it really uncomfortable 1.7 seems to be playing in that space

But almost challenging the problems based on its speed Cognition's Nader Dabit wrote, " "Building Building this way is a new category of DX. A task that used to justify walking away finishes before you've mentally moved on. There's a weird middle mode now. It's technically async, but fast enough that you just watch 

This is something that I think is going to be super interesting to watch, and actually gets at one part of the conversation of the final model that we're going to discuss today, which is GPT 5.6

The early reviews of GPT 5.6 continue to come in



and we're starting to get more details than just it was good or not. Specifically, we're starting to get a lot more about where it excels and how it compares to Fable 5 and how we're likely to use it as part of our new, more complex model architectures



how IAI's Claire Vo writes, " Things GPT 5.6 Sol is significantly better at than other models: browser use, writing like a human, communicating to a human, [00:28:00] shipping usable product, not just code, video editing, the dark horse use case, front-end design, though it loves forest green, and productive loops."

Dan Shipper from Every who are some of the most conscientious writing testers in AI, also agrees that GPT 5.6 is, in his words, a much better writer than Fable Dan continues, " It consistently one-shots marketing emails that every previous model would fail at. Fable Fable is too verbose and liable to fall into using sentences in its own private language."

Lawyer Prinz found that 5.6 was very good at work that related to his job as a lawyer. He wrote, " It can replace an associate of any level in the specific task of legal research, provided that the entirety of relevant legal authorities are publicly available online.

This is a very narrow claim, but this kind of legal research is a very important part of my work as a lawyer."

Now, part of why Prince prefers OpenAI models to Anthropic models for this type of legal work is that one of his key tests is around search He tests a model's needle in the haystack search capabilities

which are obviously very important when you're dealing with the legal field, which needs extremely [00:29:00] precise information

Now, in terms of overall comparisons, people were really plumbing for analogies. Dan Dan Shipper again writes, " GPT 5.6 is like a Porsche. Fable is like a warp drive. He said that after testing 5.6 internally for about a month, that the team at Every decided that it was the best combination of power, speed, and performance for your day-to-day knowledge work and coding

" " Fable is a different beast," Dan writes. " If you need to get across the galaxy, use Fable. If you need to get around town using the best available tool for the job, use 5.6."

In fact, Dan wrote, when they lost access to 5.6 as part of the US government's Fable delay He said he felt like he was back in the Stone Age

Another member of his team, Austin Tedesco said that going back to 5.5 after having access to 5.6 felt like, quote, " Trying to shoot a basketball that's twice as heavy as the one I'm used to using."

Going into some more details, there were a few things that Every found which I think are things that you should look out for as you start to test 5.6 The first they said is that speed changes the model

" Sol," they wrote, "is the fastest model we trust as a daily driver. A revision costs minutes, [00:30:00] which makes it easier to discard a weak draft, try a different direction, and keep moving while the problem is still in your head." So So here we have a very different example than the coding use case that Nader was describing with SWE-1.7, but still an area where the increase in speed actually changes the way that people think about the work.



second, they found that Sol finds the context it needs. Give Sol an outcome and access to the project. It reads the relevant files, follows standing instructions, asks useful questions, and keeps those choices through long runs

However, this does come with a challenge. If there are stale instructions, rules written around older models can make it worse

Their final note was that it works best when you plan to steer. " Sol," they write, "gets better when the surrounding system supplies sources, examples, style guidance, and a clear outcome. Review its choices and redirect it as the work changes." Ultimately, they said, "We use Fable for the loosest, longest assignments and Opus for when we want to see the work more clearly.

Sol is what we want beside us for the work that fills the day."

This gets to what has been the most popular review so far, which came from Arena AI's Peter Gustev, who wrote Fable 5 and GPT 5.6 [00:31:00] Soul are not easy models to compare. My overall feel is that Fable is a wise owl who is very thoughtful and very well-spoken. GPT 5.6 Soul is like a Rottweiler who will grab the problem by the throat and not let it go until it's done.

In other words, Fable is a fundamentally smarter model. Even at low reasoning, it can be very insightful and writes in a clear, compelling way. GPT 5.6 Soul, on the other hand, is extremely diligent. I can give it a list of eight things to do, and you will be sure that they will be done.



he then goes through a bunch of examples around how the different models work for video editing, computer use research, writing, UI and app building

but concludes



So is GPT-5 six Sol better than Fable? On pure intelligence, no. But man, I missed it when I wanted to get things done. it is an insanely capable workhorse that you can give any task to and just expect it to be done. No lectures or you are absolutely right isms.

Nothing is beneath it. If it takes two days to do some dirty work, it will do it. He concludes, " It feels like the first time in a while when we have quite different types of frontier intelligences that benchmark sort of similarly, but feel very different. If you can, you would [00:32:00] probably be better off using both and iteratively finding what you'd use Fable or GPT-5 six Sol for."

And And indeed, this is Dean Ball's takeaway as well He writes, " "I can't I can't remember a time when the leading models were A, so decidedly ahead of everything else, and B, so distinct from one another."



Ethan Mollick reinforces that first point, writing, " My big takeaway is that both Soul and Fable represent jumps over previous models and have opened a large gap with the next best AIs. People will have preferences for one or the other, but if you're doing any work where better intelligence matters, those two models are your only choices."

And yet, rumors suggest that this might not be the case for long



Leo on Twitter, @synthwave, who has become one of the leading rumor leakers

writes that GPT-6 is slated to launch in about a month, which is earlier than expected, and possibly even later in July.

GPT-5.6, he says, will be based on a new, significantly larger pretrain versus the four trillion 5.5 and 5.6 Spud base. Leo says, quote, " There is lots of excitementat OpenAI over this new base, which they believe will be much better able to [00:33:00] compete with both Fable-5 and upcoming which is targeting a similar release window."

OpenAI initially intended to continue with Spud through GPT-6 but decided against it. On the topic of Fable 5.1, Leo continues, " It is in the late stages of the pipeline at Anthropic and a release is expected in the coming weeks."

Andrew Curran, who has the benefit of not being an anonymous leaker, writes, " I have also heard some of this independently, and I believe the following to be true. GPT-6 is the next release from OpenAI. It's their true answer to Mythos, and it will arrive much sooner than people expect. Model release cadence has been speeding up for a while now.

It's possible that GPT-6 even arrives within the next four weeks. When I say arrive, however, it may not mean a general release because if the last couple months are any indication, GPT-6 will almost certainly be held back by the government, at least initially. It's a new, much larger pre-train, as Leo says.

Mythos changed everything. Everyone is going big, including Elon, who has a 10 trillion Grok in training. Both OpenAI and Anthropic see capabilities increasing rapidly, with advancement continuing on a new trajectory over the rest of this year and [00:34:00] beyond. Both labs are very confident in what they have internally and see nothing above us but air.

No ceiling."

So friends, even though we So friends, even though we had a lot of models to talk about today, buckle in because I don't think that we're done. For now, that is gonna do it for today's AI Daily Brief. Appreciate you listening or watching as always, and until next time, peace ​
