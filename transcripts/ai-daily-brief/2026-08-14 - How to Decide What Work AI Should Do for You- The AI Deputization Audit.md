# How to Decide What Work AI Should Do for You: The AI Deputization Audit — Transcript (2026-08-14)

https://aidailybrief.ai/e/2026-08-14 · Listen: https://pod.link/1680633614

<!-- metadata -->
Format: news-analysis · Level: 2 · Length: ~00:29:00
Host: Nathaniel Whittemore
Categories: models, agents, model-strategy, work
Featured: Grok Bot, OpenAI, Gemini, Google, ChatGPT, GPT-5.6, SpaceX AI
Also mentioned: OpenClaw, GLM, Kimi, Artificial Analysis, Nvidia Nemotron, Claude Sonnet, Gemma, Claude Opus, Slack, Cursor
<!-- /metadata -->

---

260814 cold_EDIT: [00:00:00] What if I told you that figuring out what parts of your work you should be getting AI to automate was a simple math equation? This week, two new products came online that make getting AI to do work for you much simpler

GrokBot gives users the ability to teach it a task by manually recording them doing something, While ChatGPT's computer history watches how you work and learns over time. Together, these represent the shift of the biggest challenge in AI moving from capability to context But as these new features come online, you still have to figure out which part of your work you want AI to automate

The work best suited for AI deputization is frequent, time-consuming, teachable, easily verifiable, and doesn't require you to have been the one to do it to be successful



260814 in_EDIT: the AI Daily Brief is a daily podcast and video about the most important news and discussions in AI. All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, Blitzy, Harbor, and Hyperagent

To get To [00:01:00] get an ad-free version of the show, go to patreon.comcom/aidailybrief, or you can subscribe on Apple Podcasts. To learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai.

And one more thing before we get into the headlines, including a new model from Gemini

A lot of the shows this week, including today's show, 

have to do with the newly launched Grok bot 

And for those of you who are doing our AI Summer Adventure choose your own adventure learning program, we've just posted a new pop-up destination, i.e.

project, all about testing out GrokBot. You can sign up for free at summeradventure.ai And walk through how to use this always-on teammate

that I think is the simplest, cleanest version of Open Claw we've ever had. Again, you can find that at summeradventure.ai. But now, let's get into the headlines It's almost like Google heard us yesterday talking

260814 hed_EDIT: about how many people were talking about SpaceX AI as though it had completely usurped Google in the pantheon of serious frontier model companies

On Thursday, Google released Gemini 3.7 Flash



260814 hed_EDIT: and while it is neither the much-delayed Gemini 3.5 Pro

nor the now [00:02:00] increasingly anticipated Gemini four It does play in a different category of efficiency

That's becoming a higher and higher consideration, especially for serious and advanced users

So let's start with what's good about this model. It appears to be very, very fast. During testing from artificial analysis, the model ran at three hundred and forty tokens per second, Which is an entirely different category than anything else.

It's more than twice as fast as GPT-56 and even a bit faster than NVIDIA's new Nemotron 3.5 Lightning

g- On the benchmarks, Google made some solid gains over3.6 Flash. Most notably improving their score on coding benchmark DeepSwee from 48.6 

Nathaniel Whittemore: And 

260814 hed_EDIT: with this model, Google is also slashing prices by half, making it a little more cost-effective than its predecessor Unfortunately, just like 3.6 Flash, by optimizing for speed, the model kind of ends up in a strange no man's land

Even with the cost reduction

The model still costs 40 cents per task on the artificial analysis benchmark run. That makes it the [00:03:00] same price as MuSpark slightly more expensive than models like Nemotron 3 Ultra or GLM 5.2, and around eight times more expensive than the ultra-cheap models like GPT 56-Luna At the same time It feels like the model just isn't strong enough on the benchmarks to justify the cost difference Cognition pointed out that 3.7 Flash has Sonnet 5 coding performance for less than half the cost but to put it mildly, Sonnet Five has not been a hit 

most users are either paying a little more for a Frontier model or looking for a much cheaper model

Google-- none of which is to say that Gemini three point seven Flash is bad. It just sits in an uncomfortable middle ground right now on the cost per intelligence trade-off

And yet, I think it would be a mistake to assume yet that we really understand how on aggregate these behaviors are going to shape out

In practice, some users are reporting increased utility, particularly with the boost in coding Brandon Galang of Vercel wrote, " Ignore the FUD on Gemini 3.7 Flash. It actually sits on the Pareto frontier."

[00:04:00] It still technically gets edged out by 5.6 Luna, but that's extremely deceptive. 5.6 Luna is a much smaller model, and while my team has cut over a lot of production workflows to it, I personally would not turn to it for coding tasks. Gemini models have always had strong pros in multimodal understanding.

I'm actually feeling somewhat iffy on Grok 4.6 from a model behavior standpoint. So for now, I'm giving Gemini 3.7 Flash a try as my daily driver and execution model.

Nathaniel Whittemore: 

260814 hed_EDIT: analyst Max Weinbach agreed saying, "I'm really enjoying Gemini 3.7 Flash in Anti-Gravity. It's really fast, seems to be really good, and the usage limits are insanely high."

Now it's worth pointing out that for partially synchronous coding tasks ,i.e. coding tasks that aren't long horizon where you just go off and let the agent work, but where you are actually sitting there interacting with what the agent is producing, be, that speed boost could make a really big difference and actually justify a slightly increased price tag even at a decreased performance from the frontier

The other big use case is improving Gemini Spark, which is Google's personal agent. the massive speed boost, the [00:05:00] implied increase in compute efficiency, and solid improvements on coding and white-collar work benchmarks make it a big upgrade for Spark

take a- if you're trying to take away anything from this, it's another reminder that the model race, quote-unquote, is branching out into multiple races. There's certainly still the race for the frontier But there's also a race for distribution. There's a race around harnesses, a race for revenue.

And within the context of models alone

Google seems to be betting that speed is a dimension that people will pay attention to as well

Now Now, speaking of how we understand the model race We just got a really interesting new study that confirms something that we discuss on this show a lot which is that switching to a cheaper model, particularly a Chinese model, won't necessarily deliver savings to the bottom line

A new study from Alpha Sense looked at how a range of different US and Chinese models perform in real world tasks. It tested GPT 5.6 Sol from OpenAI, as well as Opus Four Eight, Opus Five, Sonnet Five, and Haiku 4.5 from Anthropic. From China, Alpha Sense tested Kimi K3 and GLM 5.2. The study also [00:06:00] included two US open weight models, Inkling from Thinking Machines Lab, and Gemma Four from Google.

The models were tasked with running through a series of several hundred financialanalysis questions that required them to sift through a large volume of data, including earnings call transcripts, SEC filings, news articles. The outputs were scored for quality, which included things like factual accuracy

and including multiple analyst perspectives

The The results showed that both GPT 5.6 Sol and Opus 4.8 were able to deliver a much higher quality result for cheaper than either of the Chinese models. GPT 5.6 Sol, for example, completed the task for around 13% cheaper than Kimi K3 with a quality score around 20% higher.

Both Gemma 4 and Inkling were able to do a decent job around the same quality as GLM 5.2 for less than one-fifth the cost. 5 was an interesting outlier, delivering lower quality responses than Opus 4.8 while also costing more than five times as much

Now, clearly part of the purpose of the study was to test the theory that Kimi K3 and had reached frontier performance at a fraction of the [00:07:00] cost In practice, what the study found was that at least for this use case, they were both around the same level as Sonnet 5 and much more expensive than GPT 5 six Sol. Said Alpha Sense CEO Jack Coco, " Some of the more expensive models, the ones that look more expensive based on just their price per token, actually ended up being less costly because they were more efficient in using tokens."

especially for you enterprise buyers and planners out there, the faster that we shift our conventional wisdom around this and actually figure out the models that are most efficient for our particular tasks, the better off your budget is going to be

be OpenAI OpenAI has introduced ultra fast mode for GPT-56 Sol, which they claim delivers frontier intelligence at fourteen times the speed. The new mode allows Sol to run at seven hundred and fifty tokens per second, which is more than twice the pace of Gemini 3.7 Flash.

For now, ultra fast mode will only be available through the API to select customers. The feature leverages the optimizations OpenAI has made to run models on Cerebras hardware, so available infrastructure will be the limiting factor



260814 hed_EDIT: OpenAI has positioned [00:08:00] this as only really suitable for specific workflows where latency is a major factor, writing, " Ultra Fast is designed for businesses where faster frontier intelligence creates a measurable advantage, including real-time voice and customer support, commerce, coding and design, financial research, and security response."

The company did not mention how large the premium would be for ultra-fast mode, but presumably it's not ultra cheap

Nathaniel Whittemore: especially in the context of what we were just saying about Gemini 3.7 Flash, very interesting to see them push into this area as well

260814 hed_EDIT: One other story from OpenAI, although this time on the personnel side. 

On Thursday, the company's chief revenue officer, Denise Dresser, announced that she would be leaving OpenAI in the coming weeks to pursue other opportunities. Denise joined the company just nine months ago in December and was brought on on a time when OpenAI's growth was being questioned in the press Meaning that her significant pedigree as a veteran tech executive went a long way to easing investors' concerns. prior to joining OpenAI, she had spent more than a decade at Salesforce, including spending her last two years as CEO of Slack.

Alongside OpenAI CFO [00:09:00] Sarah Friar, Dresser was viewed as a part of the new business-focused executive team designed to get the company in shape ahead of the IPO

time, at the same time as they announced Denise is leaving, the company also announced her replacement

This time with another industry veteran, Dolly Rajak, the former president and COO of Wiz

Now in general, I don't spend nearly as much time on these sort of personnel moves as some other media properties do I think that nine times out of 10, the Occam's razor explanation for personnel moves 

is in fact personal

I also think that there is such a desire right now among outside observers to read any sort of shifts as tea leaves for major problems inside

that trying to do a lot of analysis from outside is pretty fraught

however, holding aside whatever I think, the market is certainly noticing this move. Part of that is that it follows by just a couple of days Brad Lightcap's leaving

and part of that is that those two departures

form what looks like a bit of a pattern running for the exits over the past couple of months

after former CEO of apps and then AGI deployment, Fiji Simo leftin July due to [00:10:00] health concerns. Sources speaking to Axios 

suggest that President Greg Brockman has been building up his own team of leaders and this move may be part of that 

Nathaniel Whittemore: Whatever the case, executive

260814 hed_EDIT: whatever the case, executive turnover is being flagged as a problem prior to the IPO But then again, with that now delayed until next year, OpenAI has a lot of time to build another narrative before their Wall Street debut

how, for now we will leave that there. And that's gonna do it for today's headlines. 

next up, the main episode If you're leading AI inside an enterprise, you already know that the gap right now isn't capability, but execution. That's why KPMG's You Can with AI is back with a new season featuring conversations with leaders like Serojia Chatterjee of Emma, May Habib of Writer, Ellery Fisher, and others focused on practical execution.

Every episode, we cover the competition between OpenAI, Anthropic, SpaceX AI, Google, and Meta. Chances are you've already formed an opinion about [00:12:00] who's leading.

Investing involves risk, including possible loss of principal.

Nathaniel Whittemore: Welcome back to the Welcome back to the AI Daily Brief. be-- Today we're doing a type of episode that I'm going to be trying out a lot more, which is effectively combining a news story with a small activity that hopefully makes this practical for you.

260814 main_EDIT: The activity today iscalled the AI deputization audit. and it's a short process for helping you figure out what you can and what you should hand over to AI

now now the news stories that inspired this are actually two-part. this week we got two new features released that reflect the fact that the bottleneck in AI has moved from model capability to access [00:14:00] to context.

I.e., Just because a model can do something doesn't mean it has the information and context it needs to do it well relative to you personally. this... Now, this has been a problem for a very long time, and we'veexplored a bunch of different experiments to improve that

for example, you can still go to contextportfolio.ai and do an interview with an AI that I set up a few months ago to build a transportable personal context file

might, that however might seem incredibly slow given what has launched this week

that, the first feature in this area that launched this week was one of the new capabilities of GrokBot. for those who missed that episode, 

Nathaniel Whittemore: GrokBot 

260814 main_EDIT: is Cursor and SpaceX AI's new simplified version of Open Claw, but for everyone else

And one of the biggest and most interesting features is the feature by which you can teach Grok Bot a task. You simply hit a little plus button in the chat and record yourself doing something in the browser. The bot watches, and then theoretically it can do again and while the team at Cursor say that many things Grokbot can already do by itself If you ever find your bot struggling

Teaching it a task is a way to solve that in one fell swoop

[00:15:00] Now that feature was interesting all on its own, but it was made more so by the fact that we got another feature in the same family, this time from OpenAI. That other feature is for ChatGPT and is called Computer History

OpenAI's Ari Weinstein writes, " Computer history lets ChatGPT learn from everything you do on a computer, so it can better understand how you work, finish tasks that you're in the middle of, and suggest skills and automations based on how you use your computer."



260814 main_EDIT: the goal is exactly the same as teaching GrokBot a task. It's to show ChatGPT how you work so that it can do more of that work. Now, some of you careful listeners might be thinking to yourselves, " Wait a second, didn't we hear about some feature like this not so long ago that caused a bunch of controversy?"

and sure enough, X users like Shove said, " I'm old enough to remember when Microsoft tried to do the same thing with Windows Recall and everyone lost their minds."

to, what Shove is referring to was a feature that was announced around the time that Microsoft introduced its Copilot+ PCs back in early 2024

Time explained the feature like this [00:16:00] Recall allows the device to take snapshots of a person's screen every few seconds. These snapshots are encrypted and then stored locally on the individual's device. Microsoft said that this feature was designed to, quote, "Solve one of the most frustrating problems we encounter daily, finding something we know we have seen before on our PC

But people did not like this



260814 main_EDIT: Dr. Chris Srisack told the BBC, This could be a privacy nightmare. The mere fact that screenshots will be taken during use of the device could have a chilling effect on people

now ultimately Microsoft recalled Recall and did later release a version

making a bunch of changes, including making it opt-in and giving users a lot more fine-grained control

So what has changed? Is it just a matter of time?

Javier Lacort writes, " "2022: I don't trust Google. I'm going to get used to using incognito mode on my phone. I switched to Firefox, VP- VPN always on. 2026: Take my history, my medical analytics, my bank statements, access to my Gmail. Analyze this WhatsApp conversation from 2018."

AI entrepreneur and content creator Theo writes, " I'm so deep in my AI psychosis that I think this sounds great. I'm not gonna lie, I wanted this since Windows Recall or Rewind [00:17:00] or whatever was announced. It got panned so hard that I kept my mouth shut.

Enough time has passed that I'm gonna say screw it and try this

say, and I will say that I do think part of it is simply shifting attitudes on privacy. If I recall correctly, my comments on Recall at the time were that it sounded to me exactly like the type of feature that people now would think was completely insane and that people in the future couldn't believe we previously didn't have

at the same time though, there is very clearly a difference in the value proposition Think about that sentence I said. With Microsoft pitching this as solving the problem of finding something we know we've seen before on the PC, is that really that big a problem? Is it a big enough problem to be willing to risk all the privacy considerations?

I don't think for many people it is. AI, but getting an AI agent to actually do your work for you is a much different value proposition

And what's clear is we now live in a world where there's a lot more choice on how those agents get the information they need to do the work

Simon Smith, for example, points out that Computer History overcomes a limitation of previous attempts because instead of taking [00:18:00] screenshots constantly, it's recording interaction events, not screen or audio

Broadly Broadly speaking, ChatGPT's computer history andbots teach a task reflect two different ways that AI can learn how you work

One, embodied by computer history we might call ambient observation. This is where the AI watchesacross apps, builds ongoing context and can learn about what you do as you do it without any particularly strong consideration on your part The Grokbot teach a task paradigm we might call deliberate demonstration. This is where you intentionally press a button where you are deciding and telling it, "I am going to now teach you a skill."

pre you press teach a task, show it the workflow, it saves the steps as a routine, and it can repeat that process later

paradigms, both of these paradigms have things to recommend them

On the computer history side, for a lot of folks, the fact that this is just happening in the background as they work will be the killer feature. The fact that they don't have to do anything intentional and yet it's still learning how to be more useful is a big part of the value.

on the other hand, I can see for a lot of folks the [00:19:00] deliberate demonstration approach of Grokbot being much preferable

For some, and I would probably put myself in this category, it is likely to be a much more natural and preferred pattern to be intentional about which things you want to actually show the agent how you do so that it can presumably do them for you

260814 main2_EDIT: But then of course, the question becomes which parts of your work should you be deputizing to AI?

to, inevitably, different people are going to come up with different answers to this question



260814 main2_EDIT: but to help you think through which parts of your work catalog mightbe well-suited to these new capabilities let me introduce the deputization audit You'll notice that I am not using the word automation, and I'm doing that very intentionally

for me at least personally, the concept of deputizing AI to go do something in my stead feels a little bit more like the relationship that I want to have with AI

Then automating away and never thinking about some task again

Nathaniel Whittemore-1: So

260814 main2_EDIT: I will publish this deputization audit as an extension of the show. So if you go to aidailybrief.ai and click on today's episode, you will find a link to it there Step one is to take an inventory of your recurring processes [00:20:00] So that we can run them through the rest of this system

I'm focused here on recurring because in general, those are the types of workflows that this sort of automation or deputization is gonna be well-suited for.

and in general I've found that no matter how much we try for our work to be novel and dynamic and different, a lot of it is just this stuff that we have to do day in, day out or week in, week out.

So think about things like email triage, weekly status reports, meeting prep research briefs, CRM or pipeline hygiene, content repurposing, scheduling and travel, vendor portal chores, inbound lead qualification, metrics and analyst polls.

All of these are things that even the most dynamic person might find themselves slogging through a recurring process for

now step two is that for each of those different processes, we're going to give it a score

And the score is going to be across five different dimensions 

Overall then, these are the five dimensions that I'm proposing make a task well-suited to automation or deputization

The first is whether the task is even worth it to automate. The second is whether the task is teachable. The third is [00:21:00] whether the task or process is checkable. the fourth is what the stakes of the task are, especially if something goes wrong

and the fifth criteria is how much you personally are the key factor in the quality of the output. In other words, could someone else be doing this and it would be just as useful or just as valuable or 

Nathaniel Whittemore-1: So criteria one, 

260814 main2_EDIT: is whether a process is even worth it to AI to do. And that basically comes down to how often you do this thing and how much time does it take A score of zero means that it doesn't happen very often and that it doesn't take very long to do when it does happen.

Think a few times a year and a few minutes at a time. A score of one is that it happens moderately frequently and takes some time, but not a ton of time. So for example, some process that happens most weeks and is done in under an hour. A score of two is a process that happens very frequently and takes a lot of time

for example, weekly or more and extending into the hours

can see, obviously you can see here that the higher the score, the more well-suited to at least explore AI deputization that task might be. Second criteria is [00:22:00] teachability. could you show this task in a 10-minute screen share?

a score of zero is basically absolutely not. It would take months to teach or is just impossible to teach in this way. A score of one is that you could demo it, but there would be a lot of caveats. A score of two means one demo could easily cover it and teach the AI that skill

The third criteria is about the output results, the checkability

How long does it take to verify the output compared to how long it would take to produce that output? Obviously, if checking takes as long as doing it yourself, then automation or AI deputization is not gonna be saving you time. So in this case, a score of zero reflects the idea that to check it means redoing it.

A score of one means that it is checkable, but you're gonna have to give it a careful read. A score of two means that a quick glance can tell you all you need to know. Criteria four, we have the stakes, i.e. how bad is it if the AI gets it wrong and nobody catches it? A score of zero, which again means that it's lesslikely to be well-suited for automation

is effectively that the stakes are high, that the problems would be serious or irreversible if AI got it wrong. a [00:23:00] score of one means that doing something bad would be embarrassing but fixable, and a score of two means that it's pretty low stakes, and if something goes wrong, it's easy to redo

Nathaniel Whittemore-1: 

260814 main2_EDIT: last criteria is how integral to the process you are. A score of zero means it has to be you again making that particular process pretty ill-suited for AI deputization. A score of one means that your involvement helps but isn't essential, and a score of two means that literally no one would notice if you did it 

or if a squirrel from outside did it as long as the work got done Now Now from there you have a combined score

Across the 10 total points 

I propose breaking it 

into three tiers A score of eight to 10 means that it's very worth considering deputizing AI to do that task

A score of eight to 10 means the stakes are fairly low, the task happens a lot, it's highly teachable, and the output doesn't really matter whether it's you or someone else. Those are the types of things that you're gonna wanna hand over, spot check the output, and see how it does.

and if and when you are experimenting with something like computer history or GrokBot's teach a task, processes that fall in this bucket are probably where you wanna look first. Now, on the other end of the [00:24:00] spectrum, when the score is between zero and three, instead of a suggestion of deputizing, we'll call that a defend, 

i.e., that you should keep that work to yourself. Maybe this is because a mistake would be expensive. Maybe it's because the person on the other end of the line expects this to be you

It's highly likely that even without a score, you will understand which tasks you need to defend. but at least this puts some consistency around it The challenge will of course be that a lot of stuff is gonna fall right in the middle. A score of four to seven I'm calling a duet where you're gonna have AI do part of the task

But you're still gonna be highly involved. Frankly, most knowledge work today is going to sit in this category. 

and the question will be over time

whether AI and the process by which it learns what you do gets better enough that more of those duet tasks can move and become deputized tasks instead

Which brings us to step four, which is naming the blocker. What would specifically prevent you from handing this off? For those tasks or processes that,land in something like the Duet or Defend category

so some common blockers might be things like the work happens across websites or legacy [00:25:00] software. think vendor portals that have no API

Nathaniel Whittemore-1: 

260814 main2_EDIT: another blocker might be that the process is hard to explain in a single prompt, i.e., you know how to do it but would struggle to write it down. These are two categories of blockers. The reason that identifying the specific blocker matters is that new updates to the tools that we have 

might change the equation around certain blockers.

For example, for the two that I just mentioned, these new systems, Computer History and GrokBot, both potentially change and solve those blockers

For systems with no API, computer use agents that click the same screens you do means that that might no longer be a problem. And for processes that are easy to show but hard to explain, well, you can just show rather than tell

some other blockers might be solved by these new tools but aren't quite as clear. for example, the AI lacking necessary context, i.e., not knowing your accounts, your history, or your formats.

Something like computer history might solve that, where ongoing observation over time could build that up. but a ten-minute teach a task with GrokBot probably won't. Now, some other blockers are not going to be solved by these new [00:26:00] tools. For example, the work requiring taste or judgment, mistakes being costly or irreversible, or the work depending on human relationships None of those things are inherently solved by these new sort of teach task capabilities

worth r-- and it is also worth observing that as with anything, new capabilities do sometimes create new challenges. if the blocker to AI deputization is that privacy or security makes it inappropriate for the AI to do that, these new tools could actually in fact add a blocker as recording your screen creates a new thing to secure



260814 main2_EDIT: Still step four is that after you have identified the blockers to your tasks in Duet and Defend, is to see whether any of those blockers are now solved by these new tools

And with that, you now have a deputization list

so, and hopefully some new ideas for how you can take advantage of these new tools now when it now when it comes to day two and day three sort of responses to GrokBot, which I spoke about very glowingly on the episode before

more people experiencing it does mean in some cases that people are coming up against its limits 

for example, super trainer, and I mean that both in that she is super and that she [00:27:00] works with super intelligent Nufar Gaspar, found that while she felt like GrokBot would be good for a lot of folks who hadn't built complete agent systems yet For more advanced users, there were lots of challenges

she c- she didn't like that she couldn't be more specific about which folder holds the relevant context, and didn't have control on things like model choice

So especially for some of you more advanced users, the type of folks who have gone through Claw Camp, not ultimately be a perfect fit

And we're starting to hear some of the use cases that people are getting value from

John O'Neill, who owns a plumbing company

went from zero to automated dispatch and office chores in 24 hours despite not having any engineers on the payroll

sta- Lots of people are using the chief of staff capabilities, where they spin up individual bots for individual tasks, but then only interact through their main chief of staff who coordinates all the other bots

indeed, that pattern of topic per bot seems to be one of the early emerging best practices



260814 main2_EDIT: finally, one use case that I'm seeing a lot that might be a good one to experiment with

Nathaniel Whittemore-1: is the inbox Slack tracker and morning brief

260814 main2_EDIT: Matt Van Horne calls this the universal starter job, same as it was for every agent before it, except now it takes about a minute [00:28:00] to set up

Regardless of what you test, if you have access to Grok Bot or Computer History, I do think it's worth spending some conscientious time experimenting with what these new sort of AI deputization tools can do for you. One of the biggest challenges, even for people who are highly AI is carving out the time

to learn to do something differently. in fact, especially high efficiency and high productivity workers often have the way that we do things so dialed in 

that taking a little while to totally change that feels like a waste of time in the short term, even ifit would save us a lot of time in the long term

Still, I think the experiments are worth it

And so for those of you who wanna try, keep an eye on the cost coming down on GrokBot as they expand access, and tell me what you find. For now, that's gonna do it for today's AI Daily Brief. Appreciate you listening or watching, as always. And until next time, peace. 

​ 

Nathaniel Whittemore's audio recording: [00:29:00]
