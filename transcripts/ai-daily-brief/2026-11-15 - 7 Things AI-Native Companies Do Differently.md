---
podcast: "ai-daily-brief"
podcast_title: "The AI Daily Brief"
title: "7 Things AI-Native Companies Do Differently"
date: 2026-11-15
url: "https://aidailybrief.ai/e/2026-11-15"
guid: "https://aidailybrief.ai/e/2026-11-15"
host: "Nathaniel Whittemore"
format: "commentary"
level: 1
length: "00:22:00"
categories: ["agents", "work", "coding"]
featured: []
mentioned: ["Slack", "OpenClaw", "Warp", "Claude Code", "OpenAI Codex"]
transcript_source: "publisher"
---

# 7 Things AI-Native Companies Do Differently

[00:00:00] People have been excited about the idea of agents as teammates for a lot of 2026, going all the way back to the OpenClaw explosion. I myself had an entire team of OpenClaws, some researchers, some writers, a bunch of different coordinators for projects, and a chief of staff that sat above them all.

Increasingly, though, I am getting more and more convinced that agents as teammate is in fact the wrong mental model

Or at least it doesn't at all reflect how the most sophisticated users are using agents in practice. Today, we're going to get into that, but also look at more broadly seven things that AI-native organizations are really doing And why so many of them come back to how they manage context



The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI. All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, Robots and Pencils, Cdata, and Blitzy. To get an ad-free version of the show, go to [00:01:00] patreon.com/aidailybrief, or you can subscribe on Apple Podcasts.

And if you wanna learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai.

one more last call to register for the AI Champions Bootcamp. It's the first time that we're running this program. It is six live sessions with Nufar. It kicks off tomorrow and will transform you not only into an agent user, but into someone who can help agents propagate across your entire organization.

You can find info about that at besuper.ai. 

Welcome back to the AI Daily At this point

we have all been drowning in China spy and chip export control scandals for way more time than I think anybody wants and so for this week's Long Read Sunday/Big Think episode, I really wanted to do something that was once again much more practical

And as you might imagine, one of the things that I am constantly watching for

Is companies reporting how they're actually using AI? I think one of the great things that we all struggle with is that there's so little information relative to the speed at which things changes about how these new capabilities are actually finding their [00:02:00] way into existing systems

You hear a lot of companies aspire to be AI native, but what does that actually mean? 

Well, 

luckily, over the past few months At least a handful of the most aggressive AI adopters have started publishing exactly how they run agents in production. These are companies like Stripe, Shopify, Uber, Ramp, Cloudflare, as well as smaller AI native companies and startups as well.

Individual operators, of course, are posting their setups on X on a much more frequent basis

Now you read enough of these things

And a picture starts to become clear of what, at least at the moment, the closest to AI-native organizations have in common look, today we're going to look at seven of those practices

practices which theoretically you could put in place as soon as you're done listening to this

and then we're gonna spend time on one thing that I might imagine many of you to expect to be on the list, but it isn't, which is the concept of agents as teammates. I've been getting increasingly convinced that the agent as teammate mental model is an incorrect one.



and I'm starting to see some evidence 

for other people finding something similar as well Now, [00:03:00] one important caveat up front is that, as you might guess, a lot of the examples that we'll discuss today come from the world of software engineering

That's not only because code got there first, it's because of why code got there first It has tests, verifiability. Done has a clear definition. And in some cases, applying these things to other areas outside of coding and software engineering won't be as clear Still, I've always said that one of the best ways to actually see into the future of your own organization or your own AI practices is to go watch what the engineers are doing today to give you a sense of what you might be doing in three to six months

So let's get into these seven practices

and then talk about why agent organization seems increasingly less like a team of coworkers and more like hiring consulting firms on demand.

So let's start with these seven practices for getting useful work out of agents. And if you had to give it a TLDR, the idea is that the company becomes a system

The first practice, which will come as a surprise to exactly zero of you, is about context. Context which has lurked around as the important unspoken issue for basically the entire [00:04:00] history of AI As we all know so well, especially for significant meaningful knowledge work, the limit tends not to be the model, and it hasn't been for some time.

It's the context and information and systems that the model has access to

So the first practice of the most advanced AI-native organizations is to give agents the whole picture, to give them everything an employee can see, or in some cases, even more than a single employee because agents are working so cross-functionally

One example, which by the way was one of the inspirations for this piece as a whole

came from the blog post by Francis Davidson after OpenAI acquired his company, Odessa

This is a company that was less than a year old And people were really excited to see Francis spell out a ton of his different practices. Now, when it comes to this idea of giving agents everything an employee can see, Davidson called the approach content maxing

And what it means is that agents get MCP or CLI access to Every meeting recording, Slack, email, Drive, and every tool the company uses. Now, one thing that I thought was really [00:05:00] notable 

it is another stealable idea that many of us might not be doing is that Odessa also wrote clean shared documents for every decision

Agents keep that knowledge base up to date, but it provides a track record 

of not just the decisions, but what went into them and how they were decided

has,

Ramp has something similar. A daily pipeline pulls Slack, Notion, Linear, and Calendar into persistent memory, so agent sessions never have to start cold.

Uber built a context graph for more than 30 internal systems.

call, And at Shopify, agents work inside a monorepo effectively. They have one repository that holds the code plus skills, conventions, runbooks, and instruction files that are written for agents

now one of the key catches in giving agents this amount of rich context, holding aside, of course, any security concerns, 

which I am blissfully breezing over right here, 

is that this context layer is in and of itself something that has to be managed Ramp's analyst agent, for example, they found gets absolutely worse when its context layer gets out of date or is neglected

One additional fascinating challenge

that George Sevalca of Hebia found was that this [00:06:00] actually has some political issues to it as well

Basically, employees who are unsure about their future are starting to hoard context as job security

If you know what your value is, why would you hand it to the agent? Now, that is, of course, a cultural problem much more than a technical one, and one that I think leaders are gonna have to deal with head-on

Practice number two: put agents in every function, not just engineering

Being AI native Does not mean having an engineering team who is AI native. It means being AI native across the organization

Odyssey again put agents across strategy, partnerships, product design, marketing, support, legal and finance

and the different groups share back in the way that they use agents To understand how that might differ from other groups as well

Over in Anthropic, their growth marketing team 

is or at least has been in the past, a single person

They've built a robust set of workflows 

that leverage agents to do things like 

reading CSVs of hundreds of ads that are running, flagging the underperformers

sub-agents for writing headlines and descriptions. And the net result is that they can write hundreds of new ads in minutes

OpenAI's Enterprise Signals research found examples [00:07:00] like Basis running customer onboarding with agents

Clay running account management with a workspace and sub-agent for every account And next, is using agents to run developer ecosystem growth

I recently did my episode about how I use agentic video pipelines 

which is another example of agents outside engineering

engineeringpractice number,

with practice number three, the description gets a little more abstract, but I think what it is will become clear. The idea is that a signal, not a prompt, starts the work In other words, in non-AI native companies, AI isn't doing something unless someone explicitly tells them to do it.

In the more AI native companies The work starts without anyone telling it to do it because it's based on some trigger that when it happens doesn't require a human transfer that trigger to a prompt the types of signals or triggers include things like a customer message, an invoice, a renewal, some sort of operational alert

At RunLayer, they find that work comes in from customer calls, custom Slack channels, builds failing, Slack mentions, and pins people drop right in the live product

In Uber, most of their agent sessions are now [00:08:00] started by other agents around things like code review, self-healing CI, and on-call triage

And if you want to think about this outside of engineering

Just try to think about which events in your business should start work on their own. A churn signal, a renewal coming due, an invoice arriving

The question changes here from what should I ask the AI to do

to which things happen that should start work automatically

Number practice number four starts to get into some of what we'll talk about 

in the, team member section

But the point of this one is that increasingly

Teams are not interacting

With a whole bunch of standing agents there is one main or orchestrator agent that can figure out what's needed

And can spin up or call in other sub-agents as whatever challenge it's dealing with requires

Anthropic's research system is one of the clearest public examples. A lead agent plans the work and then spins up sub-agents in parallel. Each one gets its own task, its own context, and its own output format, and doesn't even know the others exist. The number scales to the job. One agent for a simple fact check, 10 or more for a hard problem This approach to [00:09:00] agents beat a single agent by about 90% on Anthropic's internal research evaluations.

Warp has an orchestrator whose only job is to route work but not do the work itself. For each job, it picks which agent or agents, which models, and which slice of context the agents get

Ramp has a coding agent that they call Inspect that's a good example of how this is coming into the shared or team agent domain

for this, and one of the key reasons for this again comesback to context windows sing-- rather than having to maintain comprehensive context 

across a large number of different agents, the orchestrator keeps the summaries and the key context, and each worker gets a narrow instruction and a

clean slate, and theoretically just what they need

theoretically just what they need Practice number five: having agents check each other's work and show proof At this point, I think it's pretty clear 

that the bottleneck across pretty much all types of knowledge work has moved from producing the work to verifying it and/or just making sure it doesn't suck

AI-native organizations 

are not only viewing verification as its own important job, but are also designing specific systems for that step and that layer. They [00:10:00] don't view the agent's job as being done when it produces whatever it was supposed to produce

So a couple examples that have been published Shopify has a security system that treats every finding as a claim that has to be proven. If it can't write a test that actually exploits the bug, the finding is rejected or downgraded. And the model that checks the finding is different from the model that found it

At run layer, an agent fixes any problems and opens a pull request with before and after screenshots or a recorded walkthrough. A second agent then reviews that adversarially. And then even after it ships, a QA agent tries to break it in production

So to sum up, we've got one, check the work, and two use a different agent that produced the work to be the one who checks the work

Practice Practice number six

Scaling human review to the level of risk involved and keeping someone, a person, accountable The point is that AI-native companies neither review everything nor do they review nothing. They try to decide ahead of time what types of things are going to need a human

And they always know which human owns the result

Whenever there's an agent-to-agent handoff at Uber, they retain a chain of responsibility that traces back to a specific person Every time one agent calls another, the call carries a record of the whole chain, so even a long agent-to-agent handoff traces back to that responsible person.



at Stripe, while agents are writing the code, it's humans who merge it. every merge has a human reviewer. At RunLayer, they do it a little bit differently. small, [00:14:00] low-risk changes merge on their own, and humans step in when asked

is,

Ramp is actually selling something similar for finance, offering finance agents that approve low-risk expenses on their own or recommend a decision with their reasoning.

Each customer gets to decide how much those agents can do alone and where they have to stop

Interestingly, Snap says they put more than half of their agent investment into guardrails rather than the agents themselves

The seventh The seventh practice is about the consistency of the system across the organization Most companies, even who are working very hard to use AI well, still tend to have wild variations in how different people use AI. Basically, everyone is using AI in their own way, 

or maybe at least different departments are using AI in their own way.

The more AI-native the organization, the more there tends to be a single system that's dynamic enough to adapt and allow everyone to improve it while still working within the same system

couple, and there are a couple hallmarks of this Ramp and Uber, for example, both have shared skills libraries

that make workflows reusable across the whole organization. Ramp has [00:15:00] 350 shared workflows in one library with a tool that recommends skills based on your role. Uber's library, meanwhile, has 3,600 skills that runs over 30,000 times a day

way to,

another way to build this sort of shared system comes from Shopify Its coding agent only works in public Slack channels, never through DMs, which means that every session is a transcript that anyone can search and learn from

these AI native companies are also figuring out novel and

interesting ways to help the systems improve themselves. For example, at Warp, scoring agents grade finished runs, and another agent proposes improvements to the system as pull requests the team reviews.

Basically, they're using some of their agentic power 

to examine the agentic system in an ongoing way

or ch- one caveat or caution within this is to make sure to measure the right thing. Shopify, for example, does not count lines of AI code or pull requests.

It focuses instead on things like how often changes get reverted

reverted so these

so these are seven practices that tend to be hallmarks of AI-native organizations. and again, as I said at the beginning, the one that isn't in here, at least not in [00:16:00] the way that we were talking about it a few months ago was Agent Teammates.

Now, I don't wanna be overly pedantic or semantic about this

But I do think that exploring why the way we work with agents has evolved a little bit differently than many of us thought is useful, even if it risks either A, overstating the case, or B, trying to ascribe a single reality when lots of different individuals and lots of different companies are going to have different experiences

I do think it's fair to say that many folks thought that agents as teammates would be the defining feature of AI-native companies, that every person would have their digital representation, or that there would be specific agents that have specific roles that are maintained and persistent, 

and that you anthropomorphize through names and things like that

Now what this did get right is that it helped us shift our thinking from AI as a chat window

that we could ask for help for work that we do, to something that could go out and do work on its own

AI as teammates was a useful mental model to help people make the transition from assisted AI to agentic [00:17:00] AI

But there are a few different reasons why it didn't exactly play out that way One is that a teammate model tends to assume some fixed roster. When we're just using the analogy 

of agent as digital version of the people that work for you, that means a set number of agents, each with a role they own and an identity that lasts

Instead, what we've seen

is a move towards dynamically sized fleets of agents that can scale up or scale down

based on the work at hand

So what that means is instead of a fixed roster, you have capacity that follows the job. Instead of a persistent identity, you get fresh context for every task. Instead of a single enduring role, models and workers can change

And instead of personal memory, the most important thing is actually company-wide knowledge, company context. In fact, interestingly, Anthropic's guidance on multi-agent systems has found that splitting agents by job function, like planner, coder, tester, reviewer, tends to backfire.

Each handoff becomes a game of telephone. In one experiment, agents split by [00:18:00] role spent more effort coordinating with each other than actually doing the work I think a little bit of this is a version of the bitter lesson It's very natural for humans to assume that the right way to organize agents is to approximate the things that we've learned about managing people, when in fact what's better is to just let them figure out how to organize themselves

because those structures might look very different than what works best for us. 

game-- I think that these games of telephone and ever coordinating are the chief example of that

another example of,

another example of this shift came from Every who did a bunch of experimentation towards the beginning of the year with each person having their own proxy agent and then realized that didn't make sense at all. It made much more sense just have a smaller number of agents that lived at the intersection and could expand themselves through sub-agents as was required

and every week that goes on, you see 

more examples of this shift popping up as well I've certainly experienced it. at the beginning of the year when I was messing around with OpenClaw, I had a research agent

Actually multiple different research agents based on different projects

I also had a coordinator agent. 

I also had agents Who were responsible for keeping track of different projects, and then a chief of staff [00:19:00] agent that sat on top of them

Now my behavior is pretty much not like that at all Within Claude Code and Codex I have projects that are basically organized around their shared context in the form of repositories And then agents get spun up to do specific things with them

which in a session of Codex or Claude Code is actually more akin to spinning up 

a new orchestration agent 

given how many sub-agents they might spin up to do whatever work you've given them

There's not a persistent named anthropomorphized agent. There's a persistent bundle of context that I can drop any set of agents into at any given time

ways, although it's not perfect I think in some ways, A better analogy than teammates is something like on-demand consulting firms

Think about how an engagement works. You bring a goal, that's a prompt or a signal. The engagement lead or coordinator staffs it, that's an orchestrator. You never manage the staff, and you may never even meet them. The deliverable comes back with evidence. You sign off and you own the result internally.

And when the engagement ends, the agents and people who did the work are gone, but the work and the [00:20:00] records of the work stay. And theoretically, if you've done that well, the firm's methodology can get better every time

So not totally perfect, But I think directionally closer if we are plumbing for analogies that help people wrap their heads around how to use these new systems

Interestingly, a study published in the Harvard Business Review in May found some actual downsides to treating agents as teammates as well The study looked at researchers working with BCG. Managers reviewed the same documents with errors planted in them. The only difference was the label on who wrote them.

An AI tool, a human colleague named Alex, or an AI team member named Alex 3. When the work came from an AI teammate Alex three, managers checked it less carefully

And the clearest effect was that companies that said they already treat AI as employees, where scrutiny dropped about 16%. One manager describing an agent named Kevin

pointed out that a problem was when Kevin, AKA the AI team member, makes a mistake, Kevin literally can't be accountable

overstate, it's always important to not overstate this. it was one study. It happened [00:21:00] very early on in the adoption of agents. And to be clear, if you are finding success in your company 

using the teammate analogy, far be it from me to suggest that you shouldn't be doing so

One last note you might be wondering if it is true that the agent teammate paradigm, the named agent paradigm isn't really how things are playing out, how does that interact With the personal agent paradigm where Meta and ChatGPT are having you name your muse or dot, doesn't that somehow sit in contrast to that?

Especially 'cause those products are doing well I don't necessarily think it does For the simple reason that comes back to the idea 

that focusing your interactions on the orchestrator is where you need to focus. Effectively, these personal agents are like the ur-orchestrators. They have theoretically all of the context about everything in our lives, and so are going to be in the best position to orchestrate whatever agents and sub-agents we need to do anything

While leaving us to still only interact with one point of contact

Now, I think it's still too early to know if these two trend [00:22:00] lines will fully merge or if they just represent different parts of the AI experience. But I don't think that they're as mutually exclusive as they might seem at first. Anyways, guys, based on a close reading of lots and lots of recent shares, that is seven things AI-native companies do And that is gonna do it for today's AI Daily Brief.

Appreciate you listening or watching, as always. And until next time, peace 

​
