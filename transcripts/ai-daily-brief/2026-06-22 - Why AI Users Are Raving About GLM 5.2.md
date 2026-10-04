---
podcast: "ai-daily-brief"
podcast_title: "The AI Daily Brief"
title: "Why AI Users Are Raving About GLM 5.2"
date: 2026-06-22
url: "https://aidailybrief.ai/e/2026-06-22"
guid: "https://aidailybrief.ai/e/2026-06-22"
host: "Nathaniel Whittemore"
format: "news-analysis"
level: 2
length: "00:29:00"
categories: ["models", "open-weights", "policy", "coding"]
featured: ["GLM", "Claude Fable", "Claude Mythos", "Anthropic", "DeepSeek", "Gemini", "open-weight models"]
mentioned: ["Claude Sonnet", "GPT-5.6", "OpenAI Codex", "OpenClaw", "ChatGPT", "OpenRouter"]
transcript_source: "publisher"
---

# Why AI Users Are Raving About GLM 5.2

260622 in_EDIT: [00:00:00] Today on Today on the AI Daily Brief, why AI power users are raving about GLM 5.2. Before that, in the headlines, Trump talks anthropic, and Fable five return rumors swirl. The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI. All right, friends, quick announcements before we dive in.

First of all, thank you to today's sponsors, KPMG, Scrunch, Mission Cloud, and Outsystems. To get an ad free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts

And if you wanna learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai. For those of you who are looking for deeper training programs, we announced last week that we have upgraded Enterprise Claw and the Executive Catch-Up program to be more enterprise grade in collaboration with Superintelligent.

You can learn all about that at training.besuper.ai

And specifically the new Executive Agent [00:01:00] Leadership Program, formerly known as Enterprise Claw, is registering its next cohort, which will begin next week. So if you are interested in that, again, go check it out at training.training.besuper.ai

Last Last note today, we're in this kind of weird period where there's so much headline news that I don't just wanna be doing the Fable five update story every day for the main episode, but the consequence of that is that the normally five-minute headlines is extending to more like 10 or even 12 or 13 minutes.

That won't be the case forever, but for now, we got a little bit of a weird balance. And so with that, let's dive into the slightly extended headlines 

260622 hed_EDIT: The theme of this headlines episode Is separating out fact from innuendo

In the attempt to understand where things actually are in this very confusing moment with AI

we're gonna start with some comments that seem to some to shed light on the whole Fable 5 mythos situation

and by the end of the headlines see where it leaves us relative to whether we might be getting Fable V back this week

Now over the weekend, many folks thought that they figured out some new old information that seemed to make the Fable [00:02:00] ban make a little bit more sense

Specifically, they dug up reporting from The Economist from June 14th, in which The Economist wrote

On June 11th, Mark Warner, the vice chair of the Senate Intelligence Committee, said that General Joshua Rudd, who leads the National Security Agency and the Pentagon Cyber Command, had told him that Mythos, quote, " broke into almost all of our classified systems not in weeks, but in hours."

Now, June 11th was the same Thursday that Amazon CEO Andy Jassy informed the administration of the jailbreak that became the center of the story Once the quote resurfaced, X commentators were quick to jump on it commented Chubby summing up the feelings of many, " Wow, that changes the whole Fable 5 story completely."

University professor Pedro Domingos, who is typically not a fan of the current administration, commented, " Mythos broke into almost all of the NSA's classified systems in hours, per its director. It would have been irresponsible to not impose export controls on it, and on Fable with its pathetically inadequate guardrails."

Now, on the one hand, part of why this is resonant is that it has a feel of [00:03:00] truthiness to it, in that it would make way more sense If the White House was already keyed up about Mythos/Fable being too powerful from some other evidence that they'd seen, with this weird jailbreak report just providing enough pretext for them to do what they had wanted to do in the first place, which is to disallow the model at this time

running, and yet for those who are reading this line from Mark Warner

as some literal breach of the NSA which demanded some response

the reporter behind the story, Shashank Joshi, added some additional context. While he said that the quote attributed to Mark Warner was accurate, he added It would be a mistake to read the quote literally, I think. It surely depends on using mythos alongside other tools under very particular conditions.

I quoted it to give a sense of mythos potency, but it was a mistake not to have added caveats. In other words, this was not the director of the NSA reporting some terrifying breach. It was them reporting

how powerful they had found Mythos in their specific controlled tests

AI policy commentator Peter Wil- AI com- AI policy commentator Peter [00:04:00] Wildeford

gave an example of what he thinks is a more plausible scenario for what happened. He wrote, " Senator Warner claimed that he was told by the head of the NSA and Cyber Command thatMythos was breaking into classified systems in hours. This is an important claim to understand better.

I thought Mythos was very good at cybersecurity, but break into classified systems in hours good? NSA classified networks are physically disconnected from the internet entirely, with specialized hardware controlling what data can even cross between them. more plausible readings of what actually happened then, one, this was a simulated exercise against replica systems, not the real NSA network.

Two, Mythos was given the relevant code and architecture docs up front rather than breaking in blind. Three, it tore through poorly secured internal IT that got described as classified systems. Four, Mythos was operated with significant additional tooling and human expertise."

course, he, of course, Peter concludes, "None of this means that Mythos' underlying cyber capability isn't alarming. An AI that compresses weeks of expert security research into hours is a genuine threat to systems that are connected to networks, as we've seen." Peter's [00:05:00] point then was not to say that his scenarios were exactly what happened, But that they were all, in his estimation, more plausible explanations than what people assumed was some massive mythos breach of the NSA

The The cybersec guru added even more context in a blog post breaking down the story. They noted additional reporting thatconfirmed this breach occurred during a red team exercise run by the NSA

i.e. this was not some outside attack or breach. It was in a specific controlled environment where they were trying to run adversarial tests

Now, CyberSec Guru, also cast at least a little bit of skepticism on the source Pointing out that NSA Director Rudd was appointed in a heavily contested vote this March, with those who opposed his confirmation citing Rudd's background as a special operations officer with no relevant experience in signals intelligence or cyber warfare

writes CyberSec guru. that doesn't make his claim false, but it's relevant context for a statement about a cyber incident made by the agency's own director. He's a relatively new appointee in a technical domain that wasn't his original specialty, testifying about his own agency's capabilities

And And yet, [00:06:00] even with all of this, I think it is fair to say

That the Fable ban wasn't solely or cleanly about the Amazon jailbreak

And clearly wasn't just about personality differences between Anthropic and the White House Interestingly, in an interview withthe Axios Show on Saturday, President Trump spoke about the issue at length. He said, "We have a situation with Anthropic. We didn't like what they're doing.

So far, I think they've responded very responsibly to our request." 

Nathaniel Whittemore: When 

260622 hed_EDIT: asked if he regards Anthropic and Dario Amodei personally as a national security threat, Trump responded, " Not now, but a week ago, maybe." Referring to the G7 summit, Trump added, "I was with him yesterday. He made a speech. I made a little speech.

Seems like a nice guy, smart guy. He responded to us very quickly because, you know, it's tremendous liability. People get put in prison immediately for that. You can't play games with that. He responded very responsibly, I thought, so far." Asked about the possibility of shutting down Anthropic, Trump commented, " I don't wanna do that.

You know, we're beating China. I was with President Xi. We talked about it. We're beating China by a lot." Trump also explicitly ruled out the Defense Production Act to [00:07:00] control AI, stating, " I don't think we have to do that. So far, it's been very responsible." Summing up, Trump commented, "I think the good far outweighs the bad.

we are going to find the bad, and we're going to stop it

I think the biggest takeaway is that right now everything is heightened

People are completely geared up. Everyone is looking for any tea leaf that they can read to understand when Fable might be coming back, what the new relationship between the White House and AI companies is going to be



260622 hed_EDIT: all of which is to say it's a good time to be extremely careful about the sourcing of reporting and to try to separate what we know from what we think

Now Now, one other story from the weekend that was real and does also seem to have some big implications for the AI race was another high-profile departure at DeepMind as Nobel laureate John Jumper left for Anthropic. Jumper announced the move in an X post on Friday

thanking Demis Hassabis for taking a chance on him nine years ago and hiring him to lead the AlphaFold team shortly after he completed his PhD. That work, of course, resulted in an AI model that predicts the 3D structure of proteins based on their amino acid sequence, [00:08:00] massively accelerating the field of biochemistry and drug discovery.

For that work, Jumper shared the Nobel Prize in chemistry with Hassabis in twenty twenty-four.

Honoring his colleague, Kasabov thanked Jumper for his collaboration, commenting, " What we achieved with AlphaFold changed the world and showing the field what was possible with AI for science and medicine, lighting the way for how AI can benefit humanity."

Now from the outside, lots of folks were left to wonder what the heck is going on at DeepMind to trigger an exodus of elite talent Lasan on X wrote, "Google is in free fall. This is the second VP of engineering that left Google DeepMind this week. First, Noam Shazeer, transformer and mixture of experts pioneer.

Today, Nobel laureate John Jumper, who basically built AlphaFold 1 through 1 through 3, and most recently also worked on AI coding at DeepMind."

Now speaking of that, some suspected that being assigned to lead AI coding efforts rather than continue his work on AI for science may have contributed to Jumper's exit

But still, to have two very, very high-profile leaders of DeepMind head one to Anthropic and one to OpenAI in a single week doesn't look [00:09:00] great from the outside. A few minutes after Jumper made his announcement, Leo at Synthwaved added some background about plummeting morale in DeepMind

They wrote, "After the release of Fable 5 and with 5.6 looming, the mood behind the scenes at Google DeepMind is increasingly one of frustration and broad discontent over the lab's perceived fall into a distant third or even fourth place."

deep-- a well-connected DeepMind employee told me, "I can't blame Noam for walking. He won't be the last big name to go either." Leo added that staff were demoralized by ZAI's GLM 5.2 overtaking Gemini 3.1 Pro on the Artificial Analysis Intelligence Index

In addition, the release of Gemini 3.5 Flash and Gemini Omni earlier this year was received with little fanfare, and DeepMind has now gone four months without a flagship model release. Another source at DeepMind told Leo that Gemini 3.5 Pro is, quote, "Not the step change we need to be truly competitive in the race to AGI

Nathaniel Whittemore: That model is reportedly slated to be released next Tuesday, June 30th

260622 hed_EDIT: Leo added, "The consensus seems to be that leadership at Google has all but conceded the race to Anthropic and OpenAI, and [00:10:00] that only a big shakeup will propel them back to the heights of mid to late 2025." Another DeepMind source commented, " We no longer have a frontier model in text, image, video, voice, or even vision.

If we can't release a real frontier model after over four months of work with all these resources, what are we doing?"

Google's, Now Googler Logan Kilpatrick did offer some pushback, responding, " Everyone I know is hopeful and locked in. Lots of things in the pipeline that will hopefully pay off short and long term."

And once again, I will caution

This is all behind-the-scenes sources and reporting

Meaning you have to take it with at least a little bit of a grain of salt

I think in general

that we tend to make too much of any individual career move

For example, there was another story this weekend That Barrett Zolf was out at OpenAI just five months after rejoining And this is a guy that has now absolutely ping-ponged between OpenAI and Thinking Machines Labs and then back to OpenAI

And while of course any high-profile departure could be an indication of something going on in a lab

Humans are complex creatures with lots and lots of reasons and motivations behind their decisions that we on the outside aren't [00:11:00] going to be privy to. What What is true, however, and what is worth noting about the Google story is first that two very high-profile leaders does start to make a pattern, and that two

The drop off in where Google fits relative to at least the coding and enterprise side of the AI race

is in 2026

Absolutely notable

Now we haven't seen 3.5 Pro yet

and Google has many strengths outside just where they sit at the state-of-the-artBut you do have to think that the stakes for Google DeepMind with every new model release have raised significantly

Nathaniel Whittemore: Now 

260622 hed_EDIT: really as we head into this week, the biggest rumors that people care about is when we're going to be getting Fable V back

as, and as much hay As the press made, about Trump saying a week ago that Dario and Anthropic were national security threats

others actually saw the interview as the first step to a resolution Dan McAdieux wrote, " If you listen to Trump, he's quite conciliatory. He doesn't want to kill the goose that lays the golden egg. Trump knows AI is the foundation of America's future. Claude fable back next week. [00:12:00] Bet on it

Now beyond that, we did get even more substantial rumors about what comes next. Andrew Curran, who's one of the best follows for actual AI news and tends to have good sources when he reports something that hasn't been reported yet, wrote, " A new, more capable version of Mythos has emerged from training.

I don't know whether it will be called Mythos 5.1 or Mythos or if Anthropic will keep it internal to accelerate further development, but it has arrived." Then Andrew points out something important that we haven't discussed enough. he continues, " Stopping models like Fable-5 or Mythos-5 from being served to the public does nothing to slow down development.

In fact, it probably speeds it up slightly by freeing up resources. There are also no rules preventing the labs from continuing to advance capabilities while any current model is under embargo, or from keeping progress quiet until they choose to release it. None of them can afford to pause or slow down.

We need only look at how capable GLM 5.2 is as proof of this. To protect their business models, the frontier labs must continually train increasingly capable systems to stay ahead of open source and each other. The [00:13:00] current continues to rage beneath the ice, and we continue to race towards our destination."

Now, in addition, to a potential Mythos 5.1 or 6 emerging in the labs, Some found evidence that Sonnet 5 might be nearing release. Leo at SynthWave again wrote, " The slug Claude Sonnet 5 has appeared on an Anthropic partner provider.

Gonna be a busy week."

Chubby responded, "So we get Claude Sonnet 5 instead of Fable 5 soon. Looks like a busy week, probably GPT 5.6 and Sonnet 5. But hey, keep 'em coming." Leo responded, "I suspect it'll actually be Fable 5 plus Sonnet 5 plus 5.6, but let's see."

Now regarding GPT 5.6, some are reporting that they're already seeing the model show up in Codex, implying that we're getting pretty close A French X user called MiroChill posted a playable demo of a Pokemon game supposedly one-shotted by GPT 5.6

Meanwhile, within OpenAI, Codex lead Thibault has begun the vague posting. He wrote, "We built the Codex app with models that were okay-ish at front end. Wait to see what we can do when we finally improve front-end capability significantly in our models. [00:14:00] That day will be something."

Scientist Derya Nutmaz, who typically gets early access to models, joined in the vague posting, writing, " People were flabbergasted by Fable-5, rightly so. But those who think this will remain the best AI for a long time will soon be proven wrong." When some thought he was just stating the obvious, Nutmaz urged them to read between the lines, adding, "Read the words long time versus soon.

I didn't say eventually."

Now I think

Andrew Curran's visual metaphor of the current raging under the ice is a good one. And what's important to note with all these rumors is that even if we are in line for a big week right now, there is so much that could happen that could change that path Still, if you want to let yourself get excited about anything

my fellow builders out there, I have no doubt will be very excited to see that the way that the OpenAI team seems to be teasing the next models is them being better at front end. We should be so lucky.

For now, though, that's going to do it for this extended headlines. next up, the main episode [00:15:00] One of the most important AI questions right now isn't who's using ai, it's who's using it? Well,

Speaker: KPMG and the University of Texas at Austin. Just to analyzed 1.4 million real workplace AI interactions and found something surprising. The highest impact users aren't better prompt engineers. They treat AI like a reasoning partner.

They frame problems, guide thinking, iterate, and push for better answers.

260622 min_EDIT: Nathaniel Whittemore: Welcome back to the AI Welcome back to the AI Daily Brief

Last week, in the wake of Fable five going offline, one of the major topics of conversation on this show was the new models and new model approaches that were rushing in to fill the gap

not only 

trying to win people's usage,

but also 

having a side effect of making people think differently about how to construct their AI stack.f- now, part of what has made this Fable five moment so resonant and important among businesses

is that already,

the changes in the cost paradigm based 

on the shift to agentic AI



and magnified by the broader compute shortage, we're already causing companies to look 

around and ask whether there would be different approaches 

than just firing up the most state-of-the-art model 

for every single AI use case ep- 

now in those conversations last week, we mentioned the first impressions of [00:19:00] GLM 5.2

And they were good. 

but we have now had a weekend pass where people actually got their hands on the thing And the stature of the model



and people's belief about its implications has done nothing but grow so today we're going to talk a little bit about those second impressions of GLM 5.2

and explore whether it's something that you should actively consider

Now, the analogy that everyone is plumbing for is the DeepSeek R1 moment Yuchen Jin writes, " Looking at my timeline, it feels like GLM 5.2 is having its DeepSeek R1 moment. I never thought an open source model could break into the top three coding models this soon Zhen Xu writes, " 5.2 feels like a turning point that's as significant as DeepSeek R1.

The Fable Saga and GLM 5.2 release happening at the same time just changed the adoption calculations, and things will only accelerate from here, with DeepSeek's massive funding, Kimi, Minimax, Tencent, Qwen all lining up releases in the coming months."

Berkoff writes, "The GLM 5.2 moment is the new DeepSeek-R1 moment. The last remaining moat is gone unlessthe US labs pull something unseen before from the [00:20:00] sleeve."

So what are we referring to when we talk about the DeepSeek moment? many of you might remember that there was this crazy thing that happened in January of twenty twenty-fivewhere all of a sudden, there was this new model and this new application called DeepSeek that had raced to the top of the Apple App Store

and that for many casual users felt distinctly better than whatever they were getting with ChatGPT Now what had happened

was that DeepSeek, a Chinese lab 

spun out from or connected to a hedge fund, believe it or not, 

reas- had plopped a reasoning model inside a free app

This was not the first reasoning model that was available. OpenAI's o1 had been announced back in the previous September 

and had started to be rolled out more broadly in December of '24, but it was behind a paywall.



260622 min_EDIT: whereas DeepSeek was putting its R1 reasoning model 

right there for free use now anyone who remembers the shift 

from non-reasoning models to reasoning models will remember just what a huge difference it was, and so all of a sudden all these people were having that experience in real time.

Pair that with some reports from [00:21:00] DeepSeek themselves, which ended up being a little misleading about how little they had spent to train that model, 



and the market absolutely freaked out Nvidia had the single biggest 

daily loss in terms of pure numbers

with DeepSeek peeling off $589 billion from its market cap in a single day

Now, of course, this ended up being the market getting way ahead of itself. 

the DeepSeek phenomenon eventually receded, but it did force American labs to think differently about how fast they got reasoning models into the free versions of their applications

And yet DeepSeek has kind of a weird legacy. Every time a new Chinese open weight model comes out

It scores super high on benchmarks. everyone talks about how it's closed the gap with the Western labs

Nathaniel Whittemore: And then a couple weeks later, no one's using it

260622 min_EDIT: and honestly, a couple weeks later is being generous What usually happens is that these models don't really survive first contact with the real world of usage and fade almost instantly

Now, GLM 5.2 had some of these hallmarks. which is not to say that Chinese models have been irrelevant. In fact, over the course of the last year, they have been increasingly [00:22:00] integrated into the stack, especially for startups and younger and smaller companies that don't necessarily have as many big constraints in which models they can use

And on top of that, as the overall state-of-the-art increases, being just a few months behind the state-of-the-art

Nathaniel Whittemore: still lots of use cases that are viable 

260622 min_EDIT: In other words, what it means to be three or six months behind the state-of-the-art now has a lot more viable use cases than what it meant to be three or six months behind the state-of-the-art a year ago

Now coming back to GLM 5.2

at first blush, it did the same thing 

that these Chinese open weight models always do. Impressive benchmarks Lots of excitement

but the vibes have been very clearly different turns out it's not just random Twitter hypebeasts that are talking about GLM 5.2, but some very respected figures in the industry.

Vercel Rauch writes, "Genuinely impressed, almost shocked at how good GLM 5.2 is at coding. This changes things."

Itamar Golan writes, "GLM 5.2 is not just another open model. I played with it for a few hours, and for the first time, an open or public model felt meaningfully close to Frontier Lab quality across real tasks. Not perfect, not fully [00:23:00] benchmarked, but very different

In another post he wrote, "This is not another AI slot model. Don't ignore it. It feels like a ChatGPT moment for public open models." However, Intermardoes have a caveat about cost, which we'll come back to in a moment

about. Now, even more than just random people talking about GLM 5.2

I think a lot of folks started paying attention after Design Arena wrote a long post on X about how GLM 5.2 beat Fable 5 at website design

Now this is one of those benchmarks that one might have been tempted to be skeptical of when it was first announced. 

how could GLM 5.2 possibly be ahead of Fable V on design?

And how could it do so for a significantly lower price point?

Now importantly, they do caveat that GLM 5.2 doesn't surpass Fable 5 in everything. It's behind Fable 5 on game development, data visualization, and 3D design, and it's down all the way at fourth place on UI component. But when it comes to websites themselves, that's where it ranks first

Now Design Arena pointed to

Three different model behaviors 

that they suggested made the difference

The first they wrote is that the outputs seem to [00:24:00] indicate a beautiful set of starting templates

and while they point out that all of the models use a starting point of web design templates GLM 5.2's

seem to avoid some of the most infamous anti-patterns like the purple gradients that were all over early AI web design

Now what they found is that when you compare the outputs in GLM 5.2 to something like Fable 5, they're much, much more concentrated That concentration means that on average, they might be better, although they are going to be less diverse

The second model behavior is that GLM 5.2 avoids common error cases

Specifically, it seems to be really good at using certain dependencies such as Chart.js and Three.js

Design Arena writes, "While other models often fail to effectively use these libraries, GLM 5.2 calls and uses them naturally."

It also uses Tailwind CSS in 91% of sessions, as compared to Opus four eight, which only uses Tailwind 57% of sessions

The third model behavior is more intricate, detailed outputs

Now they do point out though 

that this complexity comes with a cost

that cost [00:25:00] being longer generation times as the model outputs more tokens. In fact, GLM 5.2 websites produced 25% more characters and lines of code in their testing and had an average generation time that was about double Claude Fable 5

Now, one thing that is worth pointing out that you start to see here with GLM is that I think that in general, people's assumption

are that these Chinese open weight models are going to be much, much less expensive to run

and in this case it's not as clear cut

YouTuber and AI entrepreneur Theo writes, "I see a lot of people hyped about GLM 5.2, rightfully so. Having an open weight model surpass GPT 5.4 and every

Gemini model is dope. That said, it's not cheap. Both Opus 4-8 and GPT 5.5 set to medium are cheaper and smarter than GLM 5.2. It also uses way more output tokens.

The tokens are cheaper, but the volume of them means you spend more time waiting for results. Still dope, just trying to make sure people set their expectations properly."

Now it's fascinating especially for those of you who listened to the

episode this weekend about local models with Nouf Ar, is that a lot of people are [00:26:00] acting like the only way to use GLM 5.2 is running it locally yourself Going back to Itamar Golan, he writes, " The catch of GPT 5.2 is that running it properly is still expensive.

You probably need something like eight NVIDIA H200 GPUs, which means roughly 400K to buy or around 20K a month to rent."

Oran- Shutterstock founder John Oranger also did this sort of math talking about how many Blackwells you need to run this under what settings

But of course, in reality

Most people are just going to use this model via one of the routing tools like OpenRouter or in one of the open source harnesses that they can maintain for themselves

Nathaniel Whittemore: OpenCode, for example, tweeted, "GLM is a hit. Been out for three days and it's already sixth on our leaderboard."

260622 min_EDIT: and I would strongly suggest for those of you who wannatry this, that rather than trying to hack at some 

very complex physical infrastructure, at least to start, you go try it via some service like OpenRouter

Still, you can absolutely feel the Overton window shifting 

on how fast people think we'll get a fable class model from China got, Elon Musk actually got into a bit of a debate with X user TR Taxes about [00:27:00] this after TR suggested That we'd see a full Chinese mythos by November or December of this year.

Elon Musk argued that it would actually be Q1



260622 min_EDIT: When the founder of ZAI responded that it won't take that long

Elon Musk responded again, " On benchmarks, yes, but as measured by true usefulness, even Q1 would be very impressive. Anthropic is rightly focused on maximizing useful intelligence, which does not show up in benchmarks, but definitely shows up in revenue."



and yet as Box's Aaron Levy points out, " The fact that open-weight models are being discussed credibly at this level of capability should be a huge update for many." to-- the implications of open models getting to frontier performance ensures that you can always have sovereign AI, have the ability to post-train for your specific workflows, cost optimize for various workloads, and actually afford to do much more with AI, which opens up meaningfully different applications.

Huge win for the applied AI layer. So for those of you who are running businesses and are trying to figure out what to do with this my recommendation is not that you race out and try to buy expensive hardware Now, if you do wanna start experimenting with local AI, you can absolutely go check out the episode I did with [00:28:00] Nufar.

But I think that the bigger thing here is that even assuming we get Fable back this week

I think the idea that AI was fully down to a two-horse race between OpenAI and Anthropic, with a little asterisk for Google if they can get their mojo back has been broken over the course of the past six weeks or so

The combination of workloads getting so much more intense, meaning so much more costly

Plus the double-edged sword of models getting powerful enough that they're subject to government review and restriction While also meaning that models just behind them are probably gonna be viable for a lot of use cases means just this incredible potential flowering 

of new diverse model architectures and setups inside companies that can optimize for different priorities, whether it's speed, cost, performance, or something else

think that, I don't think that on average most companies need to be trying to race and shift off of their,

core subscriptions, whatever they may be. But I do think that having some part of the organization have some license and sandbox to experiment with some of these alternative [00:29:00] model architectures 

is probably time and money well spent right now

Certainly as we see more evidence and case studies of how companies areputting this together, I will bring them to you. For now, though, that's gonna do it for today's AI Daily Brief. Appreciate you listening or watching as always, and until next time, peace. 

​ 

Nathaniel Whittemore's audio recording:
