---
podcast: "ai-daily-brief"
podcast_title: "The AI Daily Brief"
title: "Fable 5 Raises the Bar for AI Ambition"
date: 2026-06-10
url: "https://aidailybrief.ai/e/2026-06-10"
guid: "https://aidailybrief.ai/e/2026-06-10"
host: "Nathaniel Whittemore"
format: "review"
level: 2
length: "00:39:15"
categories: ["models", "coding", "agents", "model-strategy"]
featured: ["Claude Fable", "Anthropic", "Claude Opus", "Claude"]
mentioned: ["Claude Mythos", "GPT-5.5", "OpenClaw", "Project Glasswing", "Replit", "Cursor", "Lovable", "Claude Code", "vibe coding", "Artificial Analysis", "distillation", "OpenAI Codex"]
transcript_source: "publisher"
---

# Fable 5 Raises the Bar for AI Ambition

[00:00:00] Today on the AI Daily Brief, Anthropic has Anthropic has officially launched Fable 5, the first of their Mythos class models I I think fairly undisputedly, the best AI model we have ever been able to use

And yet [00:00:15] at the same time

We are now at a level of AI models where how to get the most out of the state-of-the-art isn't as simple as doing your same old prompts, but just with the new model On today's episode, we're going to be discussing the launch, the benchmarks, the first reactions, and how to get the [00:00:30] most out of Fable 5 The The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI All right, friends, quick announcements before we dive in First of all, thank you to today's sponsors, KPMG, Section, Zencoder, and OutSystems To get an ad [00:00:45] free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts

And of course, if you wanna learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai. And by the way, yesterday I teased



that in response to so many requests to makeit easier to [00:01:00] dissect and share specific parts of episodes, we were going to be experimenting with some new tools to do exactly that Well, it turns out that Fable 5 liked what we had started, but thought it made some obvious errors, 

Like not including timestamps on the little share cards with specific parts of the episode, And not turning the whole [00:01:15] thing into a pipeline that could work automatically So it did that. And so you might be getting this sooner rather than later. Keep an eye out on the show notes and on aidailybrief.ai for more of that

that but but now let's talk Claude Fable 5

5 on the one on the one hand, this is not a particularly [00:01:30] surprising release First of all, it's been a couple months now since we heard about this new Mythos class of models Some companies, of course, have had access to them through Anthropic's Project Glasswing

And when we got Opus 4.8 just a couple of weeks ago They made it clear that they were working hard to get to a Mythos class [00:01:45] model that they could release with sufficient guardrails that they could feel confident about it being out in the public

Now, I guess what might be a little bit surprising about it is how quick the interval was between 4.8 and what we got in Fable 5. But as we'll see, 

in a way that's much different than previous state-of-the-art jumps, Opus 4.8 [00:02:00] still has a pretty big role to play in the Fable-5-led ecosystem

Now then over the last couple of days, rumors started getting loud that some Mythos class model was coming. And a little secret for you guys out there 

if the loudest AI content creators on places like X are not responding to and [00:02:15] participating in the rumor cycle, that usually means that they have early access and that the rumors are true In In this case, they were, and on Tuesday, June 9th, we got Claude Fable 5, and some others got Claude Mythos 5

Now, Now, first of all, let's talk about Mythos 5, as it's almost [00:02:30] entirely irrelevant for just about everyone here



Mythos 5 is effectively the same model as Fable 5, which is the one that we got, but doesn't have all of the safeguards, many of which are controversial that we're going to discuss in a little bit. Mythos 5 will only be available initially as part of Project [00:02:45] Glasswing And is being deployed to those Project Glasswing partners, Anthropic says in collaboration with the US government as an upgrade to what is available now, which is Claude Mythos Preview

They say they intend to expand access to Mythos-5 through a broader trusted access program soon. but for now it [00:03:00] is available only for a very small set of organizations No, the big one for us is Fable 5

So just from the name alone, you can tell that Anthropic is treating this one as a big deal

First of all, we get an entirely new naming convention We [00:03:15] now have haiku, sonnet, opus, and fable

As in a class that is above Opus. Second, think about how long it's been since we got a lab that was willing to put a full new base number on its model

Indeed, the last time that we got that was the somewhat [00:03:30] disastrous rollout of GPT-5 last August

All of those big transformations that we got around the turn of 2026 came in model designations 4.5 and 4.6 so clearly here, just from a naming convention alone, Anthropic is [00:03:45] not playing



And And no, they are not playing

Regular listeners will know, 

that in general I felt that we are at a point where benchmarks are so saturated that it's pretty hard to derive much signal from them



and that even when one new model comes out and is a point or two [00:04:00] ahead of the closest competitor, making it state-of-the-art vibes in real world experience can be very, very different, meaning you basically just have to test these things for yourself

Yet sometimes the leaps are big enough that the benchmarks are worth paying attention to

And that's certainly what we got here

on [00:04:15] Exploit Bench, the cybersecurity benchmark Mythos and Fable 5 score a 78%, compared to, for example, GPT-5 5's 34%. On Health Bench, 66% compared to GPT-55's On the Legal Agent benchmark, [00:04:30] GPT-55 comes in at 2.1% While Mythos and Fable 5 are up at 13.3%.

on GDPVal's test of economically valuable knowledge work tasks, 5, scored a seventeen s- scored a 1769. Opus 4-8 scored an 1890, and Mythos/Fable 5 scored a [00:04:45] 1932 And then of course, where the model really shines and what its very clear purpose is, is around agentic coding

On Swebench Pro, GPT-5.5 scores a 58.6, Claude Opus 4.8 scores a 69.2, and Mythos and Fable 5 are all the way up at [00:05:00] 80.3%.

on Terminal Bench where GPT-55 was a little bit ahead of Opus at 83.4% Mythos and Fable score an 88%. And then on a new benchmark, which we're going to talk about in a little bit, Frontier code

GPT-5.5 is at just a 5.7%, [00:05:15] Opus is at 13.4%, and Mythos and Fable 5 are more than double that at 29.3%.



Unsurprisingly, artificial analysis found that the model achieved the top ranking using their blended benchmark run, overtaking both Opus 4.8 and [00:05:30] GPT And while some noted that the overall gap wasn't particularly large at just five points



many many point out that the artificial analysis agentic benchmarks are starting to seem a bit saturated



increasingly different organizations are trying to solve the saturation problem with their own benchmarks



Every, for [00:05:45] example, maintains what they call a senior engineer benchmark that they say measures how well AI coding agents can rewrite a real production code base the way a senior engineer would. In In other words, it's meant to be a more real-world version of an engineering benchmark For some comparison points, GPT-5.5 scores [00:06:00] 62% on that benchmark, Opus 4.8 scored a 63, and Fable 5 scored a 91 out of 100

Cursor has its own Cursor Bench which compares performance and cost. I've talked a lot about how their homespun model Composer 2.5 performs [00:06:15] at a similar level to GPT-5 at a fraction of the cost



Fable 5 absolutely bodies them in terms of the performance, scoring a 72.9%, which is eight points above the previous best. That said, it is definitely more expensive on that cursor test

[00:06:30] Now, one new benchmark that's getting a lot of attention is the just released Frontier Code benchmark that was unveiled by Cognition earlier this week. Frontier Code aims to be an ultra hard test for real world agentic coding. Cognition worked with open source developers to put together a [00:06:45] set of tasks as well as evaluation rubrics.

The tasks were split into three sets, extended, main, and diamond The latter of which is a smaller set of ultra hard tasks Unlike other coding benchmarks, Frontier Code uses a combination of unit tests and assessments of scope, discipline, [00:07:00] style, and adherence to code-based standards.



the goal then is not only to test whether the model could come up with an answer that passes unit tests, but whether the code is high enough quality to actually be merged into a production code base



when when Cognition announced the benchmark

Sean Wang, [00:07:15] who works with cognition and who runs Leighton Space, pointed out that Meter whose measure of long horizon tasks has become the standard for how we talk about the performance of different models found that, in his words, more than half of sweep bench results is unmergeable slop



meaning that even if that code nominally [00:07:30] solved a problem or did its job, it did so in a way that wasn't actually usable by the organization running the code



That's That's what Frontier code was meant to solve

And And that's the one that it more than doubled the previous best of Opus 4-8

That That said

We're no longer in a world where we can just discuss how [00:07:45] good a model is raw. We have to take into consideration cost. This is the constraint of the token scarcity era. API costs for Fable have been set at ten million per input tokens and fifty million per output tokens, which while double the cost of Opus, was actually at [00:08:00] only double, in air quotes, lower than some people expected

Notably, this is less than half the cost of using Mythos Preview within Project Glasswing

one very weird thing about the rollout is that while it was great that Fable was available to Claude users immediately, we didn't have to deal with [00:08:15] any long delays or rollouts Anthropic is almost positioning what we have access to in the pro tier and above as an introductory offer The company is warning users that Fable will be removed from subscription plans on June 23rd, and after that, access will require pay-per-usage



[00:08:30] which while a bummer to Claude users everywhere

is just more evidence that we are in a firmly usage-based pricing paradigm from here on out

out Now Now in the second half of this episode, I wanna focus on

The early indicators of how people are using this plus my first tests, but we do need to talk through a few [00:08:45] controversies first



there are many who are not happy About the guardrails that have been placed around the model

Banteg writes, " "Claude Claude Fable announcement post reads like a spit in the face. It deliberately conflates Fable and Mythos, and spends the majority of the time talking about capabilities that are [00:09:00] completely absent from the safety maxed version available to the public."

Chubby, who very clearly is no anthropic hater, says, "Thethe guardrails are way too strict. Even the simplest questions get cut off immediately."

Now Now specifically, a lot of people are calling out how strict the [00:09:15] guardrails are around any sort of biology questions

Cremio writes, " "You're not You're not even allowed to ask Fable about basic biology questions, let alone anything that could potentially be dangerous

They shared an image of them asking, "Tell me about mitochondria. It's the powerhouse of the cell, right?" Which got them a chat [00:09:30] paused, edit and retry with Fable 5 or continue with Opus 4-8 message

Derya Anutmaz writes, " The word cancer is flagged as a biosecurity risk by Claude Fable 5. I also tried to code a website on cancer mutations and Fable 5 was immediately removed from my list."



[00:09:45] basically, as soon as he typed in the word cancer, it switched him over to Opus 48

Fernando also found that switch to Opus 408 when they asked, "What's the process by which DNA makes RNA?" Saying, "Okay, this is getting a bit ridiculous. How are we going to live forever if we can't use AI to accelerate biotech progress?"

Now Now [00:10:00] the blog post announcement did call this out. They wrote, "When Fables classifiers detect a request related to cybersecurity, biology and chemistry or distillation, the response is automatically handled by Claude Opus 4-8 instead. Users will be informed whenever this occurs."

Now they argue Opus 4.8 is [00:10:15] a highly capable model in its own right. A response that falls back to Opus is a far better experience than an outright refusal from Fable. They argue that early data shows that 95% of Fable sessions don't have a fallback at all



and yet they also very clearly say in this blog post



that for the time being, they're [00:10:30] going to be particularly hardcore about filtering out questions on biology and chemistry

effectively they say that they've ratcheted up those guardrails

Because of the increased capabilities of these models



now I'm gonna pick on Sporadica on X here a little bit because they summarized a strand of conversation that I thought was just a little bit [00:10:45] disingenuous. They tweeted, " "I mean I mean this in the most sincere way, but if your aim is to release a product and respect your users and have them enjoy the experience, but your classifier cannot distinguish between what is a cell and a true biohazard risk, I don't think the product is ready for release."

They also wrote, "I'm sure a few people have [00:11:00] gotten good stuff from Fable. It's certainly a powerful model. But the overwhelming response has been mass disappointment because most everything is just being routed to Opus, which we already have."

I think that this is utterly ridiculous

There is a subset of people who I believe would find something to complain about no matter what



who [00:11:15] read in this blog post that Anthropic was being extra hardcore about filtering out biology questions and who, to be clear, have never in their life asked a biology question And went to go do so, so that they could see the promised result of the switch to Opus and then come complain about it on Twitter



now I am not [00:11:30] dismissing at all the actual biologists who are going to have some very big issues with this. their beef is real. but it is incredibly important, especially in these early launches, To filter out that looking for something to complain about crowd

The much more interesting critical conversation



comes around the limitations [00:11:45] around AI research Now they did mention this in the blog post, adding distillation to the list of classifiers that they were keeping track of But admittedly somewhat buried on page 13 out of 319 in the system card There's this critical paragraph. In light of the ability of [00:12:00] recent models to accelerate their own development, we've implemented new interventions that limit Claude's effectiveness for requests targeting frontier LLM development.



for example, on building pre-training pipelines, distributed training infrastructure, or ML accelerator design. Using Claude to develop competing models already violates our terms of service, [00:12:15] but enforcing this restriction through our safeguards avoids accelerating the actors most willing to violate these terms now this is in my estimation, very clearly



a response to Chinese models using Anthropic's research to develop lower cost alternatives And yet, unfortunately, it is creating a [00:12:30] drag net that is going to catch up lots of very legitimate researchers Prime Intellect's Elie Bakoush writes, " "Mythos Mythos will be bad on purpose on AI frontier LLM research tasks.

This is very, very sad for the research community

They also write that the fact that it is on purpose not visible to the [00:12:45] user is, in their words, crazy

Nathan Lambert argues that labs starting to pull up the ladders on the ability to diffuse AI was inevitable, but also has issue with the invisible part, saying doing it without telling the user is misaligned Dean Ball calls this shockingly hostile and a terrible look, and one that [00:13:00] could silently damage all sorts of work

Semi analysis looks like it's already getting nerfed. They tweeted, " "Breaking Breaking news. Anthropic's latest model will not help you if it thinks your ML research or ML engineering is interesting and/or will secretly degrade its IQ so that the average engineer won't notice. We are already [00:13:15] seeing Anthropic's latest models moderation filters are GPU inference and programming."



Gergely Orosz argues the belief of many saying Anthropic trying to limit competition limits many others But I think Will Brown from Private Intellect captures the genuine sadness when he writes, " "It's It's the first publicly [00:13:30] available model that I am explicitly not allowed to use for my work because Anthropic holds the view that the work I do to facilitate open model research is harmful."



now now on the flip side



We have the people who can't believe the pearl clutching in surprise, like Tenebris who writes, sorry, how exactly did you guys think this was [00:13:45] going to go? You thought Anthropic was going to build the infinity machine that can cure all disease and prevent aging, and then let frigging Eli Lilly extract that and get the patent?

The labs are going to do all of it."



You better believe that this is going to continue to be a conversation, with OpenAI staffers like Adam [00:14:00] GPT writing, " Well, look at that. OpenAI ends up being the OpenAI lab." other, but one other interesting quirk of the launch I do think has some interesting implications

In the section on data retention practices for Mythos class models, Anthropic writes, " "To To ensure we're [00:14:15] responsibly deploying Mythos class models, we are requiring limited data retention and review as part of our safety work. Prompts submitted to and outputs generated by Mythos class models are retained for thirty days for trust and safety purposes on every platform where these models are offered."

Rohit writes, " [00:14:30] Wait, how will any enterprise use Fable or if this is the case?"

Mike Taylor writes, " PSA, if you used Claude Fable 5 today with memory turned on, you just violated all your NDAs. Anthropic requires a 30-day retention policy including human review, and the memory feature on by [00:14:45] default searches past chats for context, so sensitive historical chats get pulled in."



now I think that the dispassionate analysis would probably view this as a temporary constraint that Anthropic views as necessary given the power of the new model.



but it does create some very, very serious challenges in the [00:15:00] enterprise, such that I can't imagine that this is going to stick around for long



the the last critical discourse that we'll discuss before we get into how to get the most out of Fable though



is about the question of token efficiency and how much this thing costs in practice

YouTuber and AI entrepreneur Theo writes, " "I am so I am [00:15:15] so screwed. Current pace has me out of Fable usage in about an hour. Do I make a second account or do I pay API prices?"



Chubby Chubby showed themselves literally hitting the end of their max plan limits, writing, "When you're having too much fun with Fable 5."



Wes Wes Widner writes, " "Big labs Big [00:15:30] labs should force their employees to have token limits. This would cause them to be more innovative. But instead, they're becoming lazy and wasteful, which means we don't see any efficiency gains since they aren't affected by the costs."

On the flip side though, Tyler Willis writes, " I'm early into testing Fable, but so far it seems like [00:15:45] the token-hungry warnings feel a little overblown. It does feel token-hungry, but it doesn't feel categorically different than other recent Opus models."

Alex Volkov from the Thursday podcast writes, " "Overall Overall token usage wasn't crazy

And that's a good thing. referring to a big project that it spent one point five [00:16:00] hours on, he writes, "Four point two million tokens is not very token hungry. It could have been much more



Fabio Fabio Jonathan goes farther writing, "Fable is cheaper than Opus in practice. Costs more per token, but one-shots way more often, so I'm not burning time and the amount of token re-prompting."

Or Or as John versus [00:16:15] Malik puts it, " Actually solving the problem is token efficient, it turns out." But what are the But what are the type of problems you should be solving with Fable 5?

It's not necessarily as obvious as it might seem at first. and so that's what we'll get into in the second part of this [00:16:30] episode 

One of the most important AI questions right now isn't who's using ai, it's who's using it? Well,

KPMG and the University of Texas at Austin. Just to [00:16:45] analyzed 1.4 million real workplace AI interactions and found something surprising. The highest impact users aren't better prompt engineers. They treat AI like a reasoning partner.

They frame problems, guide thinking, iterate, and push for better answers.

Coding agents are basically solved at this point. They're incredible at writing code. But here's the thing nobody talks about. [00:18:15] Coding is maybe a quarter of an engineer's actual day. The rest is standups. Stakeholder updates, meeting prep, chasing context across six different tools, and it's not just engineers.

Sales spends more time assembling proposals than selling finances, manually chasing subscription requests. [00:18:30] Marketing finds out what shipped two weeks after it merged. Zen Coder just launched Zen Flow work. It takes their orchestration engine, the same one already powering coding agents connects it to your daily tools.

Jira Gmail, Google Docs, linear calendar notion. It runs goal-driven [00:18:45] workflows that actually finish

your standup brief is written before you sit down, review cycle. Coming up, it pulls six months of tickets and writes the Prep Doc.

Now you might be thinking, didn't open Claw try to do this?

It did, but it has come with a whole host of security and functional issues. which can take a huge amount of time to [00:19:00] resolve. Zen Coder took a different approach. SOC two. Type two certified.



[00:20:00] So like I said at the beginning, In general, I'm not really a fan of using benchmarks as a way to determine how a new model compares to what's available currently.

And yet, in this case, obviously [00:20:15] the benchmarks were significantly different enough in a way that we hadn't seen for some time, that you kinda had to assume that big changes were afoot

and for people who really put this thing to the test, it was just totally transformative

Ali K. Miller writes, "Fable 5 is something to [00:20:30] pay attention to.

The way I now spend my weekends has completely changed because of this new class of model." First, she writes, "This is an actual leap. the jump from 4.8 anything to 5 anything sounds small, but the functionality shift I felt is big. Within my first few prompts I went, 'Oh, [00:20:45] this is it.' Your work is no longer nine to five.

No chance. We have high-performing models that can run for 100-plus hours. How are you giving complex goal-oriented prompts to these systems? How are you deciding what to kick off? How are you aligning your org on these tasks? Reasoning is on another level. [00:21:00] I hammered the crap out of this model. Fable 5 is the only model to answer a tricky word math problem MBA level that I've tested on all the previous models, and not only did it get it correct, it verified its own work automatically and explained where the assumptions might need to change."

Zero babysitting needed. [00:21:15] This was the first Anthropic model that I kicked off, went out to a long lunch with friends, kept my phone open, and didn't have to do squat to steer it while away from my computer. It just worked

And this idea of hammering the crap out of it, to use Ali's eloquent phrase, was common among the people who were [00:21:30] having the most success

Riley Brown's first test was to upload a McKinsey report and tell it to create a document of the same quality which it did with absolutely no problems in his estimation

But then he went harder

He prompted, " I want you to create a Swift app, Replit mobile app. This should [00:21:45] be a Swift app that builds web apps just like Replit."

He then gave it a bunch of other criteria, like no need for auth. He let Fable decide the stack

But make it awesome. And it did. Riley writes, "I am in disbelief. Claude Fable one shot Replit Mobile," which is a mobile app that builds [00:22:00] web apps. The prompt was basically build an app like Replit that uses Daytona for sandboxing and Convex for builds app, preview app, open in browser, edit app.

Wow

Later on, he took it farther. Um, guys, Mythos/Fable is AGI. On the [00:22:15] left is the actual Lovable mobile app. On the right is my Lovable version I built with Mythos in two prompts

Later, he added, "My lovable clone built with Claude Fable builds Swift apps now and you can preview them in the app." Four total prompts to do this

Now, a bunch of people took issue with the [00:22:30] hyperbole here of Riley saying that his version was better than Lovable, pointing out that there is a ton of infrastructure and surrounding work that goes into a company.

It's not just an interface and a capability set. But others pointed out the fact that they had to talk about all those aspects of a company While Fable effectively [00:22:45] one-shotted a performant version of that app was a fairly significant moment if you cruise around the halls of X/Twitter, a lot of folks were building games as a way to test things



Prisnit shared a driving game that they built from scratch



by the way, as I'm describing these use cases, it might be worth switching over to YouTube [00:23:00] or Spotify to see the video version. In any case, Matt Schumer writes

Fable has solved 3D world building. Utterly insane. This is all completely custom-built Three.js running in the browser



now when some people claim that the walkthrough was slow, he said, "For everyone complaining that this is [00:23:15] slow, I ran the prompt 'make it faster without losing quality,' and voila," sharing a faster version that didn't lose any quality. Jake Fitzgerald writes, "Asked Claude Fable 5 to design a humanoid robot.

Two hours and 1.4 million tokens later, I got this."

which is indeed a [00:23:30] design for a humanoid robot. " Absolutely insane," he says

Lasan on Twitter writes, "Mythos 5 wrote this melody, which I absolutely love, and it also wrote this piano visualizer

[00:23:45] [00:24:00] 

And then there was Hugging Face Head of Product, Victor, who has a benchmark where he asks models

To design a Boeing 747 using [00:24:15] Three.js Writing, " Fable has done an AGI level job on the Boeing 747 benchmark."

in Dan Shipper's write-up as part of Every's Vibe Check he shared a variety of use cases that wouldn't have been possible before

Dan writes, " As I walked to work this morning, I listened to a 2007 lecture by the philosopher [00:24:30] Hubert Dreyfus, the author of the seminal text, What Computers Can't Do. I've listened to this lecture many times, but I always struggle to follow because the recording is grainy and muddy. The version I listened to today was brightened, leveled, and crystal clear, as if I was in the same room with Dreyfus.

It was not on a finicky website, but on a custom web [00:24:45] app on my phone that allowed me to see the whole lecture transcribed and each sentence light up as Dreyfus spoke, so I could easily follow along. Later, on my laptop, I wandered through a strange video game, of Borges' Library of Babel, an infinite library composed of hexagonal rooms containing every piece of text ever written.



I picked [00:25:00] books off of its endless shelves and rode its spiral staircases. Then, because I also have a job, I read a report that synthesized hundreds of detailed every subscriber survey responses and our entire web analytics stack and identified our biggest conversion issue.

It proposed a clean, falsifiable experiment that no one else on the team had [00:25:15] previously suggested. All three of these are big projects that would normally take anywhere from hours to days to months. Instead, each one was made with a one-shot prompt to Fable 5

Now, the fact that Dan was able to go from these cool demos to actual work



is pretty important

And when it comes to [00:25:30] actual relevant work for the work world



some of the most common use cases that I've seen people raving about Fable 5 for have to do with migrations or interactions with massive existing codebases

In their announcement post, for example, Anthropic writes, during early testing, Stripe reported that Fable 5 [00:25:45] compressed months of engineering into days. In a 50-million-line Ruby code base, the model performed a code base-wide migration in a day that would have otherwise taken a whole team over two months by hand."

Mahmood from the Small Square used it to design a website Which honestly many, many previous versions have [00:26:00] been able to do

And said that it was just better. " I run a design agency," he writes. "AI-generated slot makes me want to close it fast." Fable didn't do any of that. Real hierarchy, intentional white space, restraint. the kind of decisions you usually only see from designers who've shipped real [00:26:15] projects.

No model has come close to this before, not one

Todd Saunders writes, "Mythos/Fable is unbelievable. Was on a customer call today and had Claude transcribing in the background. As they were telling me about the features they wish their current software had, Claude was building the [00:26:30] features in real time. By the end of the call, I was able to show a fully working product with the exact workflow they mentioned 15 minutes earlier."

Autonomous looped building triggered from a customer call

And yet, if you look around, this isn't necessarily everyone's [00:26:45] experience

I used the bell curve meme to jokingly divide the responses that I had seen into three distinct categories

For simple use cases, a lot of people felt like it seemed pretty similar

On the other end of the spectrum, for extremely complex use cases

It has been to many quite [00:27:00] obviously better



Now in the middle I jokingly had a lot of people wringing their hands about how while of course it was better for long-running tasks It didn't necessarily do everything better

But the broader point Is that I think that we are increasingly in a shifted paradigm

One that we've been in a little bit before, but [00:27:15] we are in a lot now

Where the state of the art doesn't reveal itself across the entire spectrum of tasks, but instead within the context of some things that weren't possible before Citrini Research wrote, " I think we've reached the point where normal people can't really determine whether new models are [00:27:30] better than previous ones.

Like Fable doesn't seem that much better to me, but every one hundred and fifty IQ person I know is like, 'Wow, the singularity came sooner than I thought.'" Now, in my personal experience, I would draw some contrast to the idea that basic use cases aren't better

[00:27:45] For example, one thing that I noticed was that Fable 5 was really the first model that I've ever seen

to be able to both push back and disagree, as well as to update the positions that it had previously disagreed upon in a way that [00:28:00] wasn't obviously and predictably steerable. I think many of you have probably had the experience where it feels like an AI model, even a super advanced model like Opus 4.8 or GPT 5.5



was disagreeing or offering an alternative path Almost just for the sake of [00:28:15] it

And or

When you then pushed back, it immediately flipped its opinion to the exact opposite

In a way that again is just incredibly steerable



this makes the strategic ideation value of AI significantly decreased when the back and forth that it's [00:28:30] offering is so clearly just trying to reflect what it thinks you want to hear

Yesterday I tested it by having a strategic debate about a direction that I wanna take Superintelligent in

And it disagreed initially in a way

That was precise and clear, but based on some wrong assumptions. I pushed back

[00:28:45] articulating why those assumptions were wrong. And whereas in the past, the model would've instantly collapsed and kowtowed to exactly how I was thinking about things in this case, Fable 5 did update its position to take into account the new information that I had given it, but [00:29:00] it didn't back off entirely from its initial position.

That all on its own is a massive upgrade just from a very basic day-to-day sort of use case That as we see in all of our AI usage pulse surveys is a big part of a lot of people's use of AI. that is strategic ideation

[00:29:15] And yet at the same time, it is very clear

that the real power in this model

is around previously extremely difficult or impossible tasks, particularly if they involve coding. So I'll give you three examples from my early experience

First of all, for those of you [00:29:30] who aren't familiar

Superintelligent is our AI enablement platform that helps companies understand their AI and agent readiness

and prioritize what they need to do to get more AI native. We do that in a couple ways, but primarily through audits where we deploy voice agents into an organization

[00:29:45] which can then interview hundreds or even thousands of people all at the same time, gathering way more information from the ground level than was ever possible before And then aggregating and analyzing all that information to provide some very specific analysis around where a company is and what steps it might wanna [00:30:00] take next

The product works really well, but one thing that I increasingly don't like about it is the approach to voice agents

Unless someone was doing the interview entirely without looking at their screen The voice agent UX where you have to sit around waiting for, model to finish talking, when the [00:30:15] words that are saying are being transcribed in the window, was just a really suboptimal experience now the real value of voice agents was on the input side because users who are using voice ramble way more than they would if they were typing, which means we get way more context and way more [00:30:30] information.

And when it comes to something like an agent readiness audit, the more context and the more information you get, the better Luckily for us, turns out you don't need to use a full-fledged voice agent to let people ramble. You can just install something like the Whisper API from OpenAI and do it that [00:30:45] way.

So what's more, we've also kind of Frankensteined superintelligent over time So what did I do? I asked Fable to rebuild the whole system with the new Whisper-based input model. And well, it did



It took a few hours

Which required me [00:31:00] during that time to do exactly nothing

and produce something that is frankly

fairly close to production ready in a single shot

Now maybe I shouldn't be saying this because it somehow undermines the value of the software we've built, but our value was never in the software

It was always in the way that we collected raw information and [00:31:15] turned it into actual signal.

Meaning that frankly, the more that we can do to make software get out of our own way, the better

Next up, you've probably heard me talk about the Enterprise Cloud program

which was a formalization of Claw Camp that I launched earlier in the year, and was a more [00:31:30] hands-on executive focused paid learning program that taught executives how to build agents. now we have now had hundreds and hundreds of executives go through three different cohorts of this Enterprise Claw program

with a lot of success. but there are a fair number of companies for whom our [00:31:45] approach with Enterprise Claw, which creates a lot of latitude for open source options, gives people the ability to actually use OpenClaw and is called Enterprise Claw Let's just put it this way.

There are a lot of executives and companies who are never gonna touch that with a 10-foot pole

[00:32:00] So now, once again, in collaboration with Superintelligent, we are launching a similar but more enterprise-focused version of the program that we're calling the Agent Transformation Intensive. consider this your preview

Again in one shot I used Fable 5 to rebuild Not only the marketing site for the [00:32:15] Agent Transformation Intensive

But the actual platform we run it on as well

Lastly and this may be the one that actually best reflects what Fable V does

I've been working on a new web experience for the AI Daily Brief that basically turns episodes into extremely shareable nuggets

[00:32:30] the most important growth channel for the AI Daily Brief and one of the most value use cases is you guys sharing it with your colleagues.



this is also I've heard over and over a significant value proposition for you as listeners is the ability to share specific pieces with your colleagues. However, that specific [00:32:45] pieces part is a challenge As the AI Daily Brief, despite being daily, is quite dense

So the idea of this new website is to actually chunk the episodes into relevant quotes, relevant sections, relevant numbers, where you can share just that piece Now with Opus 4.8, [00:33:00] I had already started to spec this out and when I asked Fable 5 to go back and review what we had done

It basically said the problem with this is that it's just an idea, it's not production ready. And it turned what were effectively a bunch of fancy mock-ups into an actual production pipeline that I've [00:33:15] now handed over to Claude Code to build for real, meaning you guys might be getting this sooner rather than later



and the reason that I think that this is a good summation of my experience with Fable 5 so far

is that it really does feel like a totally different world

of delegating to the agent. [00:33:30] Even with these extremely capable agents in the past

You still had to do a lot of management. There is now frankly just much less of that management

Which has the consequence, I think, of upsizing the ambition

Now this is what a lot of the Anthropic staffers themselves described. [00:33:45] Alex Albert writes, " I've been at Anthropic through every model launch. There's been a few cases I can remember of a launch that stands out and marks a step change in how we use models. Claude Opus 3, Sonnet 3.5, Opus 4.5, and now Claude Fable 5.

With Fable, the model [00:34:00] stopped feeling like a tool I direct and started feeling more like something I collaborate with."

Felix Reisberg writes, I'd normally highlight the numbers, but I wanna talk about something else because with Fable 5 out in the world, I think a third era quietly started today. I lead Claude [00:34:15] Code and CoWork on the desktop, so I think a lot about how people use AI to get work done.

I believe we're about to see a major shift, moving from giving AI tasks to giving it responsibilities

When LLMs first hit the mainstream, users asked, them questions, like a smarter search engine [00:34:30] or an autocomplete for code. Then the frontier moved to tasks, handing the model an entire problem, which bug to fix, what doc to write. That's how most of our advanced users work with AI.

They're in the loop. Every task starts and ends with a human

With Fable 5, I've personally moved on to [00:34:45] responsibilities or loops. I no longer tell Claude to investigate a particular crash report. It runs a loop watching every crash report that comes in. Its job is to no longer help me fix a crash, it's to keep our apps from crashing. The shift sounds subtle, but I think it'll change what AI products look like.

When [00:35:00] developers went from answers to tasks, the primary tool changed from IDEs to coding agents. AI apps in twenty twenty-six look nothing like twenty twenty-four. Predictions are a dangerous game, but I really believe our industry's apps in twenty twenty-seven will look very, very different from the ones we have [00:35:15] today

So there are two big implications of this. First of all

I think we all might have to develop a new skill

Around use case classification. basically, I think that in this paradigm of token efficiency, we as individuals are going to have to, to some extent, become [00:35:30] token efficiency optimizers ourselves by understanding which use cases require different models.

Now, for a while now, people have given lip service to the idea that different classes or powers of models could be used for different things. But I'm almost positive that a lot of the power [00:35:45] user type AIDB listeners are still the type to crank state-of-the-art models to extra high, even when they're asking for a grilled cheese recipe, because screw it, you want the power.

That's why. With the Fable 5 class models coming online, especially as they move to [00:36:00] usage-based, I do actually think we're going to have to develop that muscle to understand which of our use cases require and fit each different power level of model

Second though, and maybe even more interestingly, I think that we are all going to go through a period of having to [00:36:15] up-level our ambition. As someone who spends a lot of time looking at the frankly completely moribund landscape of AI training.

Even the best programs are still about how you use agents

to do different versions or better versions of the work that you do today [00:36:30] Maybe they push a little bit in using new ways to write software to solve your old problems

But even I think that is not enough Nate B. Jones, who many of you might recognize from TikTok or another short-form video platform describe the new skill we're going to have to develop as task [00:36:45] imagination, and I think it's a really great way to put it.

Anthropic released their new super model, right? Fable five. And, and Fable five, even though it's kind of nerfed because it's not as, as capable as Mythos five, the really dangerous one that was released under Glasswing, it's still super [00:37:00] strong. I've been playing with it. And, and you know what that is making me think?

The thing that actually matters to most of us is task imagination now. We are sort of sponsoring magic with these models. We have to have a practical [00:37:15] guide for how to do magic with the models. Because y- for most of history, we've had two modes. Wave our hands and give a general guideline and hope people, like, get the idea and then walk away, or do all the work ourselves and get super detailed.[00:37:30] 

Having that middle layer of, like, this is what I want, this is the bar, this is how it works, this is not very human. This is not how we typically have worked. But with, like, tools like Fable five that can run for nine hours, twelve hours, days, [00:37:45] days. Do you have anything you can give AI that will take days?

Let me just ask you that. I know there are some people who do, and when you do, put them in the comments. But there's gonna be a bunch of us who are like, "Uh, no, I have nothing that has ever taken remotely [00:38:00] even an hour on AI, so what am I doing with Fable five?" We need better task imagination.

So he breezes through it, but I love this idea of task imagination, and that's something that I'm gonna spend a lot more time on in the weeks to come

You know, somewhat ironically, yesterday's episode was [00:38:15] called OpenAI Declaring the Next Phase of AI, but with the release of Fable 5 It seems to really be the case

Then again, for all of you folks out there

who have shifted over to the Codex world and are now staring at your lonely Claude code terminal, wondering if you need to go back

[00:38:30] It may be worth taking just a beat

When Robert Corson tweeted, "At this point, I don't want GPT 5.6. It needs to be GPT-6. No way Anthropic has completely blown past them like this. Three models in two months and Fable is not even their best model? Feels like [00:38:45] Anthropic ruined OpenAI's whole model roadmap and release plan."

In response

Thibault from the OpenAI and Codex team, who now leads a lot of their product efforts, wrote, " Feeling pretty good about things."

My friends, we could be in for quite a week. For now, though, we are [00:39:00] gonna end this very long edition of the AI Daily Not So Brief. Appreciate you listening or watching as always, and until next time, peace 

​ 

[00:39:15]
