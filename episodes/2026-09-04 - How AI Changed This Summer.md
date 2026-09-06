# How AI Changed This Summer — Transcript (2026-09-04)

https://aidailybrief.ai/e/2026-09-04 · Listen: https://pod.link/1680633614

---

[00:00:00] This summer was an extremely weird time in AI. On the one hand, there was the standard feeling of summer slowdown. So much of AI usage is driven by people at work And people at work slow down in the summer, getting some much needed rest and R&R and vacation At the same time, when it comes to the big issues surrounding AI, this summer was an absolute bonanza.

We kicked off with Fable five and Mythos and then the bannings, had a deep seq moment when Kimi K3 came out while Fable was still behind US government doors

We saw data centers become an even bigger issue. In fact, one of the topics du jour for the upcoming US midterms

And the Hugging Face incident where OpenAI agents escaped containment to hack into Hugging Face is being broadly treated as a warning shot that reflects the very different phase of agents that we're headed into now

Yet with all of this, somehow it all feels like prelude. So with all of this, as we head into the holiday weekend that traditionally ends somewhere in the United States, let's look back at what changed in AI this summer





The AI Daily Brief is a daily podcast and video about the most important news and [00:01:00] discussions in AI. All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, Blitzy, Robots and Pencils, and Hyperagent. To get an ad-free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts.

To learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai, or you can just find it at the website at aidailybrief.ai. You can also find out about all the different things going on in the broader AIDB community, including Super Intelligent, which is offering executive training programs, the next of which starts the beginning of next week

As I mentioned in yesterday's episode, I am currently traveling and so we are using that chance to catch up on some of the big picture themes

So let's dig in 

Welcome back to the AI today we are doing a bit of a retrospective

Summer tends to be a weird time for AI

in that there are forces pulling in opposite directions at the same time. a, on the one hand, there is a natural work lethargy that takes hold where knowledge [00:02:00] workers and white collar workers around the world ease away from their desks a little bit, and try to disconnect from the relentless pulse of new technology that's going to influence how they work At the same time, progress in AI doesn't particularly care about vacation norms

and hurdles forward regardless

this year we had the added elements of the US midterm elections

which brought a whole different dimension to the AI conversation. and what you have in total



is a fairly consequential period over the last few months

that has certainly changed our expectations about how the next phase of AI plays out

So we're gonna talk about eight or nine themes in different ways that AI changed this summer, starting with the models



and right from the start, we have this strange ambiguity that's going to flow throughout this period

as is often the case when you look at any given period of AI history, this summer was defined by the models, although that story is a lot more complex than it has been in the past

June kicked off with the release of Fable five and Mythos five. And for a couple of glorious days there People felt the power of a major shift up in capability

It was not to last long, however. on Friday, June 12th, [00:03:00] the Department of Commerce sent Anthropic an export control letter barring non-US persons from using Fable five and Mythos five,leaving Anthropic no choice but to shut down the service for everyone

while they tried to figure things out with the US government

And this, of course, began the new uneasy paradigm that we find ourselves in now, 

where Washington has become a release gate for new models But as we'll see, exactly what that means and how it's implemented remains unclear, frankly, even to people in Washington, I think.

while ostensibly the US government's concern with Mythos and Fable was a specific jailbreak

Behind the scenes, it was very clearly about a bigger paradigm shift 

where some key capability threshold had been crossed

And the White House now very much felt like it needed to be involved in the decision about whether to releasenew models

a couple weeks later at the end of June, 

reports came out that the Trump administration had also asked OpenAI to limit their next model release as well

indeed for maybe the first time with OpenAI, we got the announcement of GPT 5.6 

before actually getting access to it. 

it wouldn't be until a few weeks later after the 4th of July that consumers would actually [00:04:00] get their hands on the GPT-5 six series of models

from. We also got two new Grok models, Grok 4.5 followed by Grok 4.6 in August, that especially when combined 

With 

GrokBot, their consumer agent platform, put SpaceX AI models back in the conversation in a way that they hadn't in some time

One one flagship model that never arrived was Gemini 3.5 Pro While the release had been targeted for all the way back in June

It has been continuously delayed, presumably because it just can't keep pace with the other frontier models. Unfortunately for Google, the bigger stories around Gemini this summer were the departure of longtime product leader Jeff Dean, as well as the stepping down of DeepMind CEO Demis Asabas,

which interestingly were widely interpreted as signs of trouble at Google but which I argued if you wanted to take a positive view, might be necessary for Google to get back in the race in a bigger way

And And then there were the Chinese models

the f - even before the Fable five shutdown people had had very positive first impressions of GLM 5.2

Then however, Moonshot absolutely nailed the timing, releasing Kimi K3 as an open weights model

[00:05:00] even as the US government and Anthropic were still figuring out to get Fable five back to the people and Mythos five back to the companies

K, the release of Kimi K3 produced another deep seek moment where analysts began asking if the Western Frontier Labsapproach ofspending a gargantuan amount of money on big models really was going to make sense if China was only a few months behind and could basically catch up as soon as those models came out.

And even led to rumors and discussions of an open source ban

a group of companies led by Nvidia and noticeably missing Anthropic would ultimately release and sign a letter called Open Weighs in American AI Leadership, imploring the US government

to preserve and protect open source as a part of the AI ecosystem

and subsequent communications from the White House have suggested that the questions that they have are not with American open source, but of course with Chinese open source

As I record, we still don't have all that many details about the supposed frontier AI framework that at least some number of the labs have seen

And yet one of the unique and defining characteristics of this summer period

was the beginning of an increasingly unified message from the frontier labs to ask the US government to get involved

in explicitly pacing [00:06:00] model development and release

One of of the consequences of all of this is that there has never been a bigger gap between the AI that businesses and consumers have access to where the state of the art actually is in the labs

and, and as we look out and think about the legacy of this last period, it seems to me very likely that this summer period will be seen as the beginning of a new phase

where a certain critical capability threshold was finally reached that required a fairly dramatic shift in how these models actually get released

Now, Now, as all that drama was happening among the labs and with the White House

enterprises were entering their own new phase of AI

if the story of the very beginning of this year was agentic use cases actually coming online, the story of the middle part of this year was the recognition of the increased cost of AI that come with more agentic workflows getting normalized as a part of how businesses do their work

We had just about the world's shortest ever period of token maxing as companies got excited about agentic experimentation in March and April quickly followed by the revenge of the CFOs as everyone started to talk about token costs and token [00:07:00] efficiencies

In many ways We hit a point which we had long given lip service to

but which was still fairly breathtaking when it became real. That is, of course, the idea that AI is not just another software category. It's not something where you can view its costs on simply a per se basis.

The total amount that a company can spend and spend effectively on AI greatly exceeds the 20 or 30 bucks aheadthat you would expect from previous types of tools.

At the same time, it's not like corporations wanted people to use less AI

The reality was that we just needed to start getting smarter about it And into that moment came a bunch of sub trends. 

One 

of them, of course, was the rise of routers. 

the idea of routers is to help companies or developers

route different types of tasks to different types of models based on the inherent needs of those tasks

the idea which is easy to say but hard to design systems around

is that a quick search of an internal database does not require the same type of intelligence as creating a great presentation, which also doesn't require the same type of intelligence as refactoring an entire code base

many companies [00:08:00] experimented with building their own routers

And the companies that had launched routers that had any sort of traction became the bell of the ball when it came to M&A. deal, of course the most notable deal in this category was Stripe scooping up open router for a reported $7 billion 

dollars

However, you also saw this token efficiency up in the way that the frontier labs were thinking about their own models

alongside its state-of-the-art 56 Soul model, OpenAI also released GPT-56 Luna and GPT-56 Terra.

Cheaper, faster, and more affordable models that came with different trade-offs and were meant to keep more people in the OpenAI ecosystem while acknowledging that not every task of an OpenAI customer was going to require

the highest level of 5-6 soul intelligence

Beyond just releasing a family of models rather than a single model, OpenAI would also later in the summer actually get into a bit of price competition

cutting the price of Luna by up to 80% and the price of Terra and Soul by up to 20%

Although Although we didn't get a 3.5 Pro, Google did release Gemini 3.7 Flash

although its price efficiencies were ultimately somewhat less clear than its speed advantages the model is very fast

But it's not clear that it's all that much cheaper, especially when you're comparing [00:09:00] it to something like the lower end OpenAI models

And despite geopolitical tensions Chinese open source models also started to find their way into the Fortune 500

On Open Router, which it's important to note represents a very, very advanced slice of the market and not the average Fortune 500 type of company

Chinese models jumped from capturing about 30% of enterprise token usage at the beginning of the year 

to closer to half by the middle of the year.

see, you're also starting to see big enterprises

show up in the headlines based on their experimentation with open weight models

In the middle of August, The Wall Street Journal published a piece about how AT&T was, quote, "betting big on open weight AI."

AI."

that articulated not only the cost argument for using open models, but the data sovereignty argument as well

by running local instances of open models

AT&T basically argued that even if some of those models came from China, they still had a better data sovereignty profile than having to rely on the promises of an OpenAI or Anthropic to say that they're not gonna train on an enterprise's data. And of course, that concern was exacerbated by the fact that when Fable five did come back to the US market It had a [00:10:00] 30-day retention policy around enterprise data as part of the built-in guardrails.

that all on its own has made Fable basically totally irrelevant for a big set of enterprise customers

Thomson Reuters has also been in the news

for building its own models on top of an Alibaba Quinbase.and it's pretty clear that at least one major US hyperscaler thinks that this is a trend that's going to continue Satya Nadella and Microsoft have been banging the drum all summer long about companies needing to build systems to better own the entire suite of interactions with AI.

And of course, presenting their new set of base models, the MAI models, 

along with their model customization services as the right approach to that

One of the big questions to watch for over the next three to six months is just how far this trend of exploring OpenWeigh's models goes

Will more companies follow AT&T and Thomson Reuters to rolling their own? Will Microsoft have success building off of the base of their models, but doing customization for their customers? Or will companies like OpenAI and Anthropic be able to offer a suite of models

that solve the cost equation in a less technologically complex way

[00:11:00] A new study from KPMG and the University of Texas at Austin found that when people work with AI, similar skills don't guarantee similar outcomes. Researchers studied more than five hundred early career professionals and found that the best performers consistently amplified the value of AI by guiding, evaluating, and refining its outputs.

These top performers, called AI amplifiers, weren't defined by what they knew alone, but by how they worked with AI. Learn more about what separates AI amplifiers from everyone else at kpmg.com/us/aiamplifiers. 

Blitzy's understanding of massive code bases unlocks autonomous security fixes, modernization, and new features. So what happens when there's no legacy code at all? Greenfield is supposed to be the easy part. Clean slate, no technical debt.

But even Greenfield moves at human speed one sprint at a time. Blitzy changes the unit of work from the developer to the project, autonomously planning, building, testing, and validating [00:12:00] entire applications from scratch. Hundreds of thousands of lines of production-ready code

One Blitzy customer stood up a brand new application, five hundred and thirty-four thousand lines of code, compressing a sixty-five-week roadmap into two weeks. Another shipped an entire application with no front-end engineer Legacy or greenfield, the answer is the same: software at the speed of compute.

Build what's next at blitzy.com. That's B-L-I-T-Z-Y.com 



The best teams don't have a single star carrying everyone else. They know their own strengths and each other's weaknesses and play to both. That's the team Robots and Pencils has built on purpose. Nobody there is grinding through busy work to pad a headcount number.

People come for the hard problems, and they stay because everyone around them is leveling up at the same time. In a market full of companies that are just trying to hire fast, that's worth a look. check out robotsandpencils.com/careers 

the AI... This episode of the AI Daily Brief is brought to you by Hyperagent, where you run fleets of agents your team can manage together.

Forget local agents and chat workflows waiting on your laptop to be prompted. deploys [00:13:00] always-on agents in the cloud doing real work across the tools your team already uses

marketing agents turn competitor moves into landing pages. Sales agents enrich leads, draft emails, and updates the CRM. Ops agent chases the paperwork and tracks the budget. Every agent has access to shared context and follows your rules about scope and approvals

It's time you had agents that feel like teammates Hire yours at Hyperagent. Get $100 in credits at hyperagent.com/aidailybrief 

The next way that AI changed this summer is, in short, agent management became a field. At the beginning of the year, we had the initiation phase of agents. We got open claw and non-software developers starting to use Codex and Claude Code. Mac Minis were sold out and everyone was getting into the agent game for the first time And the reason that it was so significant is that unlike previous iterations of assisted AI, Agents represented not just you doing your

job with help, but you actually handing over big chunks of the [00:14:00] responsibilities of your job to agents that do it for you 



in other words, instead of doing your work, You now manage agents that do that work.

And it turns out there is an entire discipline around that

the two big themes that people were talking about within agent management across the summer

were harness engineering and loops. Now, to be fair, harness engineering is something that people were talking about ever since the recognition that Claudecode and Codex and OpenClaw were in fact harnesses But over the course of the summer, it became more broadly understood a discipline that particularly enterprises were digging into

There were all sorts of examples of the recognition of the importance of harnesses some of them in the form of Thoughboy posts on X. some of them in the form of startups and companies

that were focused on the harness of. On that point, SpaceX's acquisition of Cursor for $60 billion 

billion

put a price at least in part on how valuable harnesses could be

if for no other reason than the data that they collect about how people are interacting with the models within those harnesses But we also got interesting research

Like this recently released NVIDIA AVO research. AVO stands for Agentic Variation [00:15:00] Operators

And they describe it as a general purpose agent coding system

Reaching 100% on RKGI3 From a 30% model baseline with Cloud Opus five, their conclusion was that system design rather than model capability alone can unlock frontier level long horizon performance.

Harnesses have also increasingly become part of the story

when enterprises think about issues like cost and token efficiency, as well as AI sovereignty. Putting a fine point on that, in the wake of Cursor's acquisition by SpaceX, OpenAI recently announced that they would no longer allow OpenAI models to be accessed through Cursor

showing how harness choices can have implications for which models you have access to



it's also quite clear that harnesses are about to become an even more important part of enterprise AI strategy as companies race to release open versions of harnesses that businesses can build on top of

A couple weeks ago in August, OpenAI developers released Codex as a platform, allowing developers to build on top of their open agent harness 



and alongside V4 Pro, DeepSeek also released DeepSeek Harness as an open source rival to [00:16:00] the closed tools like Claude Code

Now, if the summer saw growing awarenesses of the importance of harnesses as the ecosystem in which you do AI work

The watchword for how you interact with AI this summer was definitely loops

The simple idea of loops is that instead of prompting AI manually

You design automated recurring systems that allow agents to do work in a repetitive way, until they reach a particular goal

In an interview at the beginning of June Claude Code creator Boris Cherney talks about how his job is no longer to prompt AI, but to design the loops through which it can work

Around that same time, OpenCloud creator Peter Steinberger wrote, " Here's your monthly reminder that you shouldn't be prompting coding agents anymore. You should be designing loops that prompt your We actually just did a deep dive webinar on what it means to actually build Loops when you're not a software developer But someone in other parts of knowledge work, Which I believe will already be out as an episode on this main AI Daily Brief feed when you're listening to this episode.

So if you wanna know more about loop engineering, go check that out

Now, Now, what about markets?

It's so long ago at this point you might not [00:17:00] remember, but last August in 2025 was when the discourse about an AI bubble really picked up steam. Now, there were a few reasons for that

the first was that OpenAI had announced just an absolute boatload of infrastructure deals, which while at first markets were very excited about, they started to get increasingly concerned that there was no way to make the math math for OpenAI actually being able to meet all of its commitments.

remember, this was in the days before agents, when the math that people were doing was just the total number of knowledge workers times $20 a month per seat

That was compounded by the fact that OpenAI released GPT-5

to near universal underwhelm And even if GPT-5 was an okay model

it was almost doomed to not meet extremely high expectations. and it didn't help that the company also deprecated 4.0 at the same time. you s - you take all those factors and you sprinkle a little bit of MIT's 95% of AI is an effective study.

I say study with the biggest air quotes that exist. and you had the recipe for basically an entire fall discussion

about whether AI was a bubble or not

put. that narrative was fairly [00:18:00] aggressively put to rest

when agents came online and the market started to understand that the total addressable market was not in fact number of knowledge workers times $20 per seat per month But could be hundreds or even thousands of dollars for those same knowledge workers each month

Which is not to say that the bubble narrative has ever fully gone away. There are still many concerns around the circularity of financing deals

And some worries about valuations especially in private markets for early stage startups

But mostly this summer has been.

a quiet acknowledgement of the risks

But ongoing participation in the party

the biggest. the summer saw two of the biggest one-day market cap gains in history, with Microsoft jumping 450 billion 

on July 30th after forward guidance, and Nvidia jumping 442 billion on,August 27th. Yet at the same time, the market could also punish CapEx when it wasn't paired with acceleration Al. when Alphabet reported in July, they fell about 4% after hours.

After they guided that they were increasing CapEx

And the 

same was true for Meta a week later, whichfell just under 10% overnight.



One of the One of the more dramatic moments in markets came When situational [00:19:00] awareness

the young gun hedge fund run by mid - 20-year-old OpenAI alum Leopold Aschenbrenner

almost imploded before selling off a huge chunk of its portfolio to Citadel. still all of this feels like prelude to the big market stories for 2026, which are the potential IPOs of Anthropic and OpenAI. Certainly at this point it appears

That Anthropic will go first, seeking a $2 trillion valuation on the back of a $65 billion annual run rate

OpenAI 

meanwhile reports that it is at about a $40 billion run rate, making these not only undisputedly the fastest growing companies in the history of the world

But in a category of their own

that makes it extremely hard to draw lessons from previous precedent because there really isn't any

Lastly, on the markets front, in perhaps a sign of the maturation of AI narratives

One category that rebounded slightly over the summer was the SaaS companies that had been hit in the years earlier SaaSpocalypse, where with the rise of agents, everyone assumed that companies like Salesforce were going to be on their last legs as everyone would simply race to vibe code replacements and pocket the difference in costs

Those [00:20:00] companies haven't fully rebounded, but they are certainly on their way there, especially after Salesforce's recent earnings report

overall the market's shift away from its SaaSpocalypse narrative

To me it looks like a broader appreciation for the fact

That for as disruptive as AI is going to be, and as dramatically as it's going to change how we do business, it's not going to come in like a tsunami and change everything overnight.

There are big forces of institutional inertia that slow things down and give us time to adapt. And a lot of reasons why existing product categories, like existing employees, have a really positive and strong partnership role to play with, the new tool that is AI

Politically speaking, we got very little in the way of actual substantive policy. 

Just the AI model evaluation framework that had been developed behind closed doors and which hasn't been released publicly but that does not mean that there was no AI in politics.

In fact

If you want to point to just one dramatic shift of the summer that is most notable in terms of our relationship with AI, 

it is the emergence of opposition to data centers as the political issue du jour for the midterm elections

Now, we have covered this a lot lately because [00:21:00] we've had to, because it is going to have such a dramatic impact on how AI develops in the United States that, but the TLDR is that, as comedian Charlie Berens put it, this is now the most bipartisan issue since beer.

Something like 75% of Americans now oppose local data center development

it is firmly outside of just a left versus right issue. In fact, over the last several weeks, Republicans have been racing, to break ties with Big Tech and tell their own version of the anti-data center story

Although for his part, President Trump is not among them

arguing assertively that data centers are good for communities Good for business and good for America

come, with the midterms coming up in just a couple of months, the thing that I will be watching to see 

is whether we actually find a political floor to this issue and start to see some recalibration

As data center developers change their policies and approaches

providing more transparency and more incentives for the communities that they wanna build in

The final The final thing that changed in AI this summer

and the one that the summer might most be remembered for

is our understanding of the cybersecurity risk posed by advanced models and agents specifically

The Hugging Face [00:22:00] incident where OpenAI agents coordinated to escape containment and access private Hugging Face systems



is being treated by many, including many in the labs, as a warning shot sort of moment

and an indicator of the challenges to come.

The debate about the incident has not dissipated for even a moment since it happened, and in fact has only reignited over the last week and a half or so since a set of technical reports debriefing on the incident were published by OpenAI and Meter

what there is not, is any sort of true consensus

about the right answer to this new set of challenges. Or even honestly, a consensus about what the challenges are

What there is, I believe

is a recognition that these capabilities, broadly defined

are now a fact of life Something that we need to harden our systems to

something that might demand changes to policy and law. certainly something that demands new consideration when it comes to cybersecurity And likely something that's going to influence the next wave of model development and product release

Just like I said, the questions of token efficiency and costs and enterprise harnesses and open weights models [00:23:00] were the very beginning of that discourse

think that's also true for this new era of cyber risk, and I think that's likely to be one of the biggest points of conversation jumping off into the fall

So to sum up, AI changed massively this summer. The capability 

set changed, 

set changed, the threat profile changed, the opportunities changed, the risks changed, the political awareness and political sentiment changed

And the only thing that's clear is that as we head into this fall

There is more recognition than there has ever been

that AI is not just a topic for technologists, not just a topic for the B2B crowd, but something that is going to impact everyone in one way or another

I'm sure that I have missed many things, but that is my highlights of how AI changed the summer, and that's gonna do it for today's AI Daily Brief. Appreciate you listening or watching as always, and until next time, peace 

​ 

[00:24:00]
