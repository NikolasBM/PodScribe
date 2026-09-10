# Why GPT-6 Astra Is So Significant and So Confounding — Transcript (2026-09-08)

https://aidailybrief.ai/e/2026-09-08 · Listen: https://pod.link/1680633614

---

[00:00:00] 

GPT-6 Astra is here, and if you feel like people's first impressions are a little strange, you're not alone

this is supposed to be this crazy advanced model from OpenAI. It's a totally new pre-training base. It was so powerful they had to keep it under wraps for a little while. It's supposed to answer Anthropic's Fable and Mythos And certainly some of the stuff that's showing up on social, these incredible one-shot games and 3D models and things like that, are really impressive, at least visually

but then in some other more basic areas, people aren't necessarily finding it all that much better. So what is the story of Astra?



The challenge is that GPT-6 Astra is not an efficiency AI model. In other words, it is not about doing what you currently do better. It is through and through an opportunity AI model that is going to challenge you to think differently about what you can do

And not only is it bringing a new capability set With its computer use capabilities, it's also bringing along a new default interaction pattern, where increasingly we will not be sitting there clicking around and typing to our [00:01:00] computer But instead, we'll be ambiently talking to it as it does all the things that we used to do



in short, the changes that it represents are immense

But not easy to package up in a weekend of testing



so let's try to figure out together the right way to look at Astra and maybe help you figure out where to begin



D- the AI Daily Brief is a daily podcast and video about the most important news and discussions in AI

All right, friends,All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, Blitzy, Robots and Pencils, and Hyperagent

To get an ad free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts. And to learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai. Two other quick things before we get into this very big episode



First is a last call for our new cohorts of our executive agent leadership program and our executive catch-up program. Both of those are kicking off this week. Although you are not too late to join right now.



you can find the information to that [00:02:00] linked off the top of aidailybrief.ai. and of course, you can also find linked at the top the new multiplayer AI sprint for teams This is the latest AIDB free program following AIDB New Years and Claw Camp, Agent OS, and the Summer Adventure

And this one is the first one that's designed specifically not just for individuals, but for teams to come together to use agents together. which I believe this shift from single player to multiplayer AI is going to be one of the biggest trends defining the best, most successful AI-using companies this fall

you can find this print, which is again, completely free linked from the main website or at multiplayerai.ai 

Welcome back to the AI Daily Brief. Today, we are talking about one of the most significant and confounding model releases for a very long time, certainly for all of 2026



Now inevitably, as soon as I planned a trip for Labor Day weekend and my birthday, you just knew that we were going to get a bunch of important model releases



right as I was on my way wheels up and [00:03:00] OpenAI did not disappoint

Now, Astra is one we have been waiting for for some time



It is intended much more than the GPT-5 six class ever was to be an answer to Anthropic's Mythos class models

Unlike the jump between something like 5.5 and 5.6 Astra started as a fundamentally different training run



And while the model has nominally been ready for some time now, Astra is of the new generation of models which now operate in the paradigm of having to be delayed somewhat before their release



Based on safety and security considerations

Indeed in his announcement, Sam Altman said, " "It It took us some extra time to ensure that we could meet the safety and alignment standards required for this capability level, but we think you will find it worth the wait."

Now, the rollout was a little bit messy. The model was announced on Thursday, but availability was limited to partners enrolled in the cybersecurity-focused Daybreak program

And a lot of people, myself included, were very antsy to get our hands on the thing

that had been so long anticipated

Tibo from OpenAI promised that [00:04:00] for everyday paid subscribers didn't have access to Astra, they would give them one banked reset



and Altman promised to begin the broad rollout to their API and ChatGPT subscribers as soon as possible



And by Friday night, the new models were in everyone's hands

The announcement video for Astra went absolutely mega viral on X

at the time of recording on Tuesday morning, it has been viewed more than a hundred and thirty-two million times and saved more than a hundred thousand times



The video is three minutes of people

sitting in or pacing around a room with a big projection of a screen on the wall talking to an open laptop and watching Astra do things for them. The use cases are split between business, personal productivity, and recreation One person is listing an item on eBay, one person is doing a contract review, one person is building a presentation, one person is making a game



They also show those same people



untethered from old pesky things like browser windows and mouses, doing multiple things at once.



While in the foreground, they are working on their main productivity task. In the background, they're working on some administrative or simple task like [00:05:00] ordering food or booking a tennis court

And just from that video alone

You could tell that there was kind of going to be something different



about this Astra model



the the first takes quickly started rolling in

And some parts were kind of expected

Dan Shipper from Every summed up, "It's a big upgrade from Five Six Soul with some frustrating habits that keep it from matching Fable at the top end

Dan said that it was the best writing model he'd tried, being very easy to steer and producing very little slop

He found that it was incredibly good at computer use. clearly a major priority for this model launch

with Dan saying that Astro can quote go for hours at a time using complicated apps to get work done. Harkening to something that would be all over X all weekend, and which by the way is a good reason to potentially switch to the video version of this if you're just listening.

Dan also pointed out that Astro was incredibly good at making 3D games and visualizations

But he said

Astra also had a tendency to overcomplicate things for example, when he asked for a simple interface, he got extra labels, extra buttons, and features all over the place. He suggested that it, quote, [00:06:00] "Doesn't quite match Fable's ability to intuitively understand your prompt and do something delightful without overcomplicating."

Now on the one hand



It's not all that surprising that a new release from OpenAI, even one that is meant to catapult them ahead of Anthropic and Fable



Had aspects where people who were dedicated users preferred Fable more

At the same time, reading the Every Vibe Check after seeing a lot of other people's first experiments with it, Felt very muchlike trying to judge a new thing with old criteria that didn't quite fit

There was something almost discordant

about the capability set and the tools and tests people were using to evaluate it



exa-- certainly an even more dramatic example of this came when the artificial analysis intelligence index scores came out

Initially, Astra scored a 61 on the intelligence index. That gave it the same score as GPT-5 six Soul

And left it a full five points behind Fable 5.1. It also meant that Meta Mu Spark, which was also released at the end of last week and which we haven't had a chance to dig into here yet, but we will, was [00:07:00] one point ahead of GPT-6 Astra

And for some, this was evidence of exactly the idea that I just mentioned

that the tests that we're using to judge old models don't really reflect what their impact is likely to be.

Now, when Now, when it comes to artificial analysis specifically



the index is fairly skewed towards benchmarks that reward, for example, memorization of facts they have fewer tests that require advanced coding and even fewer still 

that are about advanced computer use





And lest one think that this is just a problem for the people who don't get a great score on the intelligence index the AA team actually rushed out their update to the index over the weekend, announcing their new index version 4.2



The update includes more emphasis on agentic tasks With their AA briefcase test, plus a different structure and weighting

on many of the existing tests. in that new version 4.2 iteration, GPT-6 Astra was still behind Fable 5.1, but was ahead of everything else



Hello everyone

One big change [00:08:00] around AI is we've shifted our thinking from how we rank our pages to how do we become the source that AI trusts enough to answer with?

At KPMG, they're seeing this firsthand. AI-generated results now surface answers directly, often without a single click. that's why they are increasingly focused on generative engine optimization or GEO, structuring content so AI systems can retrieve it, understand it, and cite it as trusted authority this is not just an SEO evolution, but a visibility mandate. And indeed, the GEO mandate from KPMG is simple: If AI is shaping decisions, your expertise needs to show up inside the answer.

Read all about it at slash us/geo. Again, that is kpmg.com/us/geo



Blitzy deeply understands your code base before it writes code. Here's the first place that pays off: security in the age of AI

Vulnerabilities don't live in isolation. They live buried inside millions of lines of interconnected code, where patching one thing quietly breaks three others. That's why surface-level scans fail [00:09:00] Blitzy starts from its knowledge graph of your entire application, identifies and surfaces CVEs across the full estate, proactively recommends patches, and can execute the PR Each fix is grounded in how your systems connect and validate so nothing new breaks.

And the knowledge graph dynamically updates, keeping you ahead of an ever-accelerating threat landscape

One Blitzy customer resolved 21 active CVEs across six core microservices in four days. Zero compile errors, every validation scan clean, months of planned work fixed in less than a week

Security remediation grounded in real architectural context at the speed of compute. Harden your code base at blitzy.com. That's B-L-I-T-Z-Y.com





The The best teams don't have a single star carrying everyone else. They know their own strengths and each other's weaknesses and play to both. That's the team Robots and Pencils has built on purpose. Nobody there is grinding through busy work to pad a headcount number.

People come for the hard problems, and they stay because everyone around them is leveling up at the same time. In a market full of companies that are just trying to hire fast, that's worth a look. check out [00:10:00] robotsandpencils.com/careers 

the AI... This episode This episode of the AI Daily Brief is brought to you by Hyperagent, where you run fleets of agents your team can manage together.

Forget local agents and chat workflows waiting on your laptop to be prompted. deploys always-on agents in the cloud doing real work across the tools your team already uses

marketing agents turn competitor moves into landing pages. Sales agents enrich leads, draft emails, and updates the CRM. Ops agent chases the paperwork and tracks the budget. Every agent has access to shared context and follows your rules about scope and approvals

It's time you had agents that feel like teammates Hire yours at Hyperagent. Get $100 in credits at hyperagent.com/aidailybrief 

So what is going on

So what is going on here? Well, in just a minute, we're gonna look at the benchmarks that OpenAI chose to highlight and some of the unique and different things that people share that they were doing with Astra over the weekend.

But to not bury the lead, GPT-6 is not an efficiency AI model. this is an opportunity [00:11:00] AI model. In other words, GPT-6 Astra is not about doing what you currently do better It's about expanding what you can do



p- that makes Astra extremely interesting, potentially extremely valuable, but also challenging

And part of what we're gonna do in today's episode is look at some comparable past examples of this type of opportunity AI model release to see if and how we figured out what made those models different, and how long it took



But first, let's go back to some other benchmarks, specifically to OpenAI and what they chose to highlight 

even if one takes lab benchmarks with a grain of salt, where they choose to put their focus can still tell us something about, how the OpenAI team sees the unique and differentiated value of Astra relative to other models

As has become the norm OpenAI now shows benchmarks not just as a list of comparative performance numbers, but on charts that can map performance versus cost, building efficiency right there into the core analysis

On coding benchmark TerminalBench 4.0, the model scored fifty-seven point six percent, which beat Fable [00:12:00] 5.1 at fifty-five point eight percent and represented a large jump from GPT-5 six Sol at thirty-seven point three percent

On DeepSui, Astra scored 74.1%, which was slightly higher than Fable 5.1 at 73.7%. Now interestingly, for both of those benchmarks, Astra achieved its best score on high or extra settings and actually declined a little bit with effort set to max. This suggests that higher effort could mean overthinking and getting sidetracked



And importantly, OpenAI chose to highlight



that not only did Astra score higher, but they did it a lot more cheaply than, for example, Fable 5.1

Now on Automation Bench, which measures computer use, the scores were off the chart

Astra scored 41.1%.

Which was much higher than Fable 5.1 at 31.4%. And GPT-5 six sole at18.1%.



And honestly, if you had to pick just one thing that OpenAI really wanted you to know about Astra It is how transformatively different at using computers it is in the announcement post, they call it explicitly the world's [00:13:00] best computer use model Claiming that Astra marks a new frontier in the speed, accuracy, and safety of computer use



OpenAI also emphasized a big increase in capabilities for science and math. On Terminal Bench science, Astra scored 64.6%, beating Fable 5.1 at 52.6% and absolutely demolishing GPT-5 six Solo's score of 22.4%. And on Frontier Math Tier 4, Astra achieved a near-perfect score of 97.6%

Another jump from Fable 5.1 score of90.2%. In cybersecurity, advanced computer use seems to have led to a big breakthrough in capabilities as well Astra scored 100% on Exploit Bench across all effort levels, suggesting it can build and execute exploits with little difficulty



Using an internal benchmark of recently disclosed vulnerabilities, Astra scored thirty-nine percent compared to just five point five percent for GPT 5.6 Sol.



Now, in addition to benchmarks, GPT-6 Astra announcement post also highlighted some use cases, and it's very clear that OpenAI is not just pitching [00:14:00] this as a better way to write documents and do research

They point to game development, circuit board printing, 

Car transmission design

And again, many other things that are very much outside

The classic set of use cases that these sort of model announcement posts focus on

And this was reflected in the types of experiments



that were going on viral on X over the weekend OpenAI's Thomas Ricard wrote, " Astra is very good at 3D modeling." Andand then showed a walkthrough of how he built a demo house walkthrough for their blog post



Arita's Peter Gosteve used Astra in Blender



to recreate a famous Apple announcement video

of Craig Federighi doing some weird parkour moves



now Blender, which is a 3D creation program, was all over Astro related posts



Alex Oliver showed its capability and persistence by building a photorealistic bat in Blender, saying, "It just kept going until I ran out of tokens."



Yunfan Yi modeled the house tour use case that had been on the OpenAI blog post writing, " Give it a Zillow listing. It can 3D model the house based on the listing [00:15:00] photos and create a cool promotional video." This video was created in one shot, and there are still some wrong details, but I'm sure it would be much better if I asked it to polish further.



DuncanDuncan Trussell built a creepy VHS-looking version of Backrooms

Sharing something that looks like an old VHS, but actually was an AI-generated video, just was all built in Blender

As As Duncan went on, " I wonder how it is at rigging 3D characters and animating them. I'll try that next." He followed up, "Yeah, we're cooked. It did it, no problem. Rigged a 3D character, put it in the backrooms, and made it walk around." If you've never messed with Blender, this might not seem like a big deal, but rigging sucks.

I've tried this with other versions of GPT, and it never really works. This did it perfectly in one prompt

Ash Bytes writes GPT-6 Astra to create a 3D website that pulls apart a Tesla Model X into three hundred and thirty-four modeled pieces



Google Applied AI PM Barron Roth wrote, " Astra helped me win an argument I had with my fiancée on whether glasses dry faster right side up or upside down after dishwashing by simulating the physics of the water molecules and nearby [00:16:00] air humidity."



Now, many wonder whether this is an advisable use case or not with Michael Briggs responding, " One small step for science, one giant leap towards sleeping on the couch."



As you As you might expect from what you've heard so far

lots of people also tested Astra by building games

Ethan Mollick wrote, I I asked GPT-6 Astra to turn Zork, the classic 1977 text adventure, into a full 3D action adventure game. It kept the original plot and puzzles, added fight scenes, and built all of the characters and environment directly in Three.js

Derya Unutmaz wrote, " One of the games I absolutely loved playing in the mid-'90s was Doom. Now, more than 30 years later, I've created my own Doom-inspired game in just a few hours with Astra, and I keep adding new features, enemies, and levels that are so enjoyable to play and have almost no bugs I can notice, even in first versions

Building it brought back so many great memories from those early days of gaming and was so much fun. It's beyond remarkable to think that something that once required a legendary team and extraordinary engineering can now be recreated, experimented with, and expanded in hours by someone like me, who has no software engineering expertise

[00:17:00] Theo built a game called Fish Slop, writing, " GPT-6 Astra is world-class at Blender and three-dimensional reasoning. This was a one-shot game it created all running in browser."

Now, when people assume that this must be just absolutely eating through tokens

Theo responded, " Fish slop would've been under $30 to generate. Wouldn't have even noticed the dent on the $200 sub."



entrepreneur Anshu found something similar, sharing a game that they created And adding, " Dude, GPT-6 Astra is some kind of turbo AGI machine god for 3D games. It one-shot this in 45 minutes for hardly a couple percentage of my quota



The AI battle account built Sonic and found that on max settings, Astra was able to build it in 53 minutes using 4% of weekly usage on a Pro X5 account, while Astra on medium took 25 minutes and used1% of the weekly usage

Even Sam Altman weighed in on this use case saying, " It is obviously trivial relative to everything else, but the fact that Astra can make me whatever fun little game I can imagine and I can be playing it a few minutes later is so cool



ca- others took this 3D capability in a learning direction. Anne Draganin wrote, " [00:18:00] Yesterday I built a cell model. Today it showed me how Ozempic works. I asked it to explain the mechanism, 

And one hour later, this



the video that Andrew shares is an interactive 3D model that shows exactly what Ozempic does

Higgsfield Head of Product combined Astra and Higgsfield

To build an overlay for watching soccer that tracks players, maps passes, and follows possession all in real time



and and Emmanuel from Scenario said that GPT-6 Astra helped him build something that he wished he'd had as a kid He writes, " "Input Input just an image or an idea in a few words and get a fully buildable Lego set 100% customized to your prompter image using official Lego parts you can order online."

Emmanuel AOF writes, " I asked GPT-6 Astra to help me understand my own ankle pain. It gave me a full interactive 3D atlas, bones, ligaments, tendons, real motion axes, sliders for plantar flexion and inversion, and a live readout of what each ligament is doing.

One session

Ethan Mollick writes, " I don't think this was the goal, but the fact that Astra is incredibly good at visually pleasing 3D work like Blender gives it a [00:19:00] perception edge over Fable in the war for social media attention. It's harder to judge other kinds of outputs, but the visual stuff comes through."



and of course Ethan is right. this stuff is really cool. But how much does it matter to the average person?



if you knew that this sort of 3D design was what Astro was really good at, would you even have something that you could think of to use it for?



And indeed, when people were sharing some of their more generic use cases

It wasn't all sunshine and rainbows. A16Z's Martin Casado wrote, " The new models are amazing, but it seems coding has saturated?" There's clearly a meaningful step in computer use, but I don't notice a meaningful step in coding for the work I'm doing. Maybe a skill issue



found, but others report something similar. Ronacher wrote, " "I don't I don't know where Astra learned Python programming, but when it's one step removed from normal code, it writes weird Python slop. The unit tests it writes are absolutely horrific

Stripes Chris Puckett wrote, " Astro Thoughts absolutely blew me away with taking some shader animation work to an incredible level. Absolutely crap the [00:20:00] bed, the sloppiest slop to ever slop on front-end design

Dan Driss wrote, " "GPT-6 Astra has one pretty big problem, front end and UI design. Astra is absurdly good at spatial reasoning, 3D, computer use, math, agents, coding. But ask it to make a beautiful website, and Claude can still look noticeably better. This might genuinely be the biggest reason I'd still use Claude."

Which is not to say that's been everyone's experience. Claire Vo from the How I AI podcast

described in her long review how she had been trying to build an architecturally complex product intelligence app that aggregates and analyzes data across platforms. she said Fable did insane things with the architecture. Five/Six just got stuck on quality of insights. Astra one-shotted it " This," she says, "has been my experience this entire model.

It's been so hard to do these very specific tasks. I've tried them over and over again for six months. Then Astra one-shotted it."

And yet And yet still

What comes through in the much more full reviews, like the one from Claire

Or like Ali K. Miller's review 

[00:21:00] is that in addition to these 3D capabilities The really transformative thing around Astra

Seems to be in the realm of computer use

Claire, describing herself as a computer use maxer, said that Astra has taken her computer use to the next level

She described things like managing complex web UI or automating lead routing workflow in CRM and said, "This kind of thing, just typing and thinking takes forever. Before Astra, I didn't feel like computer use could navigate these nodes as well."



Now, however," she said, "I'm just hands-off my computer all the time now

And pointed out how different a mental paradigm this type of interacting with computers really represents

Ali Miller agreed, writing, " Computer use and browser use are just incredible. I'm confident that pretty much any stable workflow done on a computer can be at least partially done by AI. It's just so, so good

Imagine you were a creepy boss and recorded your screen for seven straight days. What would you have AI do that you've been doing? Can you challenge yourself to go mouse-free for a day?

Now there's way more to get into, and we are just [00:22:00] barely beginning to pull back the curtain on this model



but I wanna close out on this idea



of why I'm describing Astra as both significant and confounding all at the same time



when you think about capabilities of advanced AI



LLMs like GPT 3.5 and then 4 hit pretty directly down the line of an extremely core set of things

that lots and lots of people do Looking up answers to questions, researching, writing things these sort of tasks and queries make up a big part of our daily experience, especially in the work world.

And what's more, The interaction pattern of effectively just sending text messages to a bot was something that most people were at that point really comfortable with



but even as those core writing and research type use cases of LLMs

have attracted legions of users, we've had a few major jumps outside of what people normally do as well



The The first was image generation Now, this is a little bit borderline because obviously even before things like Midjourney and Stable Diffusion and later NanoBanana and GPT Image People were [00:23:00] interacting with images But still, before it was really easy to generate them

interacting with images or at least creating images remained a more specialized domain.



if if you look at the big generative AI releases from November 2022 as a proxy, it's not surprising that ChatGPT

was so quickly so much more ubiquitous than Midjourney's version four, which also came out that month.



there are there are simply more people and more established use cases for the things that ChatGPT could do than at that time, at least for the things that Midjourney 4 could do

Over time though, as the AI capability set has changed, the way that people use generative images has increased and expanded and made it a major mainstream use of this technology as well

The second time I think we had a major jump outside of what the average person, call it knowledge worker does

was with the introduction of advanced AI coding

Now what makes this interesting is that obviously for some people, a significant number and class of AI early adopters, coding was in fact the major substance of what they do in a day-to-day way

But for the [00:24:00] rest of us who would quickly become vibe coders, it was a little bit different cap- we hadn't had the ability to interact with code as a way to build things and solve our own problems and accomplish our work up until a set of models and tools Made it viable to do so without having to know the underlying coding languages

In many ways, you can chart the long history of 2026 backto the end of November 2025. When we got Claude Opus 4.5

which wasfollowed quickly after by GPT 5.2, and which together people realized over the next month or so represented a total step change in their ability



to do significant quality work with AI coding



at this point now 10 months on from that

Many of us previously non-coders have integrated AI coding into our work streams in various ways, but that's still a work in progress. it hasn't yet translated all the way across the entire span of knowledge work, even though for those of us who have fully embraced it, it feels like some version of that is inevitable



all of this 3D modeling and design stuff

feels like a third example of that pattern in other words, a set of capabilities [00:25:00] unlocked by some new advance in AI That gives people who previously had no way to interact with that capability set the opportunity to now do so

The question will be

What, if any, use cases

will become normalized for that for people whose work at this moment doesn't normally include 3D modeling or design Will these use cases remain entirely novelty?



or will some make the jump, like AI and agentic coding has made the jump, to just a thing that now a much broader set of knowledge workers actually use in a regular way?

The other pattern of change that I see with Astra comes in the interaction patterns that it models

What I mean by that is that sometimes the big shift isn't just in capabilities, but in how we interact to leverage those capabilities



when when NanoBanana, AKA Gemini 2.5 Flash Image, was originally released back in August of 2025

It wasn't notable specifically because it was massively better at making photorealistic images or images in particular styles What made it so powerful was that instead of having to regenerate an entire image [00:26:00] from scratch to change one detail, you could instead prompt it to fix just one specific part.

And it turns out that that one small change in the interaction pattern unlocks a tremendous number of use cases



Throughout Throughout 2026, coding has also been witness to a set of rapid shifts in the interaction pattern as well. Now, Now, some of this obviously 

has been capability changes as well, but what has been the big watchword for AI and agentic coding this summer? It's It's been all about loops

And shifting from thinking of prompting a coding agent to do a thing, to instead setting up a loop structure

in which it can manage itself and continuously progress towards a goal in a way that it can evaluate its own progress and continue on until it actually achieves that goal

That is a totally different type of interaction pattern that will change what we can do with and how much we can get out of AI, and that we are in the middle of trying to expand outside of just the initial domain of coding to other areas of knowledge work as well



And it feels to me like even [00:27:00] if



3D modeling and design stays more niche than either image generation or coding as a default part of all knowledge work



OpenAI at least is making a very strong argument

that computer use capabilities are changing and will change



how we think about interacting with computers



I don't think it's an accident at all that the entire three-minute launch video that has been seen 130 million times is people completely hands-free Sitting in a chair, pacing around



Verbalizing and externally processing their way through a variety of different types of work

All with their voice as the AI manages the interface

Now this sort of interaction pattern



has long been a part of sci-fi

There's a reason that everyone references Tony Stark's Jarvis

And we've had baby steps towards this With developments in voice mode



anyone who's done pretty much any of the free training programs that I've released this year has heard me squawk endlessly about anchoring the way that you interact by using voice mode

But it's pretty clear that we're still early days

And I think the upshot of all of this is that [00:28:00] Astra is not a modelthat I think we should expect to fully understand Or take anywhere near full advantage of in the immediate term

While there's gonna be lots of debates around whether this is now AGI

as for example, OpenAI's Greg Brockman says that he believes GPT-6 Astra represents The real work of the next few months is going to be to figure out

not where Astra replaces GPT-5, 6, Sol, or Fable 5. For the everyday sort of things we do

But in a much bigger and more core way what new opportunities it unlocks for us



one place to keep an eye on that Is what's coming out from OpenAI staffers themselves



Tibo, who leads product over there, said, for example, " Astro was probably our biggest competitive advantage while it wasn't generally available. Since we've had it, our productivity jumped so much that we shifted some of our plans six months ahead, and we'll ship them at Dev Day instead of mid-next year."



Was it just better agentic coding, or was it something else entirely?

That is the question that faces us, and we're gonna have to take a lot more time to figure it out. for now, though, that is gonna do it [00:29:00] for today's AI Daily Brief

One where even though we've gone wildly long, I feel like we are just barely scratching the surface. Appreciate you listening or watching as always, and until next time, peace 

​
