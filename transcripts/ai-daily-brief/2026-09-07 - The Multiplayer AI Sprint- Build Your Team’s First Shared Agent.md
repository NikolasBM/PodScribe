# The Multiplayer AI Sprint: Build Your Team’s First Shared Agent — Transcript (2026-09-07)

https://aidailybrief.ai/e/2026-09-07 · Listen: https://pod.link/1680633614

<!-- metadata -->
Format: commentary · Level: 1 · Length: ~00:25:00
Host: Nathaniel Whittemore
Categories: agents, work
Featured: multiplayer agents, Claude, OpenClaw, Claude Tag, Anthropic
Also mentioned: Slack
<!-- /metadata -->

---

[00:00:00] 2026 is undisputedly the year of agents

For years, we were talking about these things, but now they are actually here, and they are changing how we do work, at least on an individual level. The thing is, not all of our work happens on an individual level. Most of us, in fact, split our work pretty comfortably between work that we do on our own and work that we do in teams.

so far, agents have really only been able to impact about half of that equation. I believe strongly that that is about to change and that the best, most dynamic AI using teams are going to shift from single player AI to multiplayer AI 

The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI. All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, Blitzy, Harbor, and Hyperagent To get an ad-free version of the show, go to [00:01:00] patreon.com slash aidailybrief Or you can subscribe on Apple Podcasts.

And to learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai. Finally, last call and blissfully for those of you who are not signing up, the last time that I will be yapping at you for a while about our super intelligent agent executive programs The next cohort starts this week. So one last time, you can check them out at training.besuper.ai 

Welcome back to the AI Daily Brief

The day that this episode comes out is Labor Day in the US, the traditional end of summer and the beginning of back to school and back to work

This is one of those inflection moments where a lot of folks

come back to the office, whether it's virtual or real, reinvigorated and ready to crush out a couple great months before the holidays descend

In fact, I think in many ways outside of New Year's, this is the time where I see the most excitement around new ways of working on an individual and a team level Now this year, Labor Day also happens to fall on my birthday

And I thought that I would give all of you guys a present

released... so far this year we have released four free [00:02:00] self-directed learning programs. 

We kicked off the year with the New Year's AI Resolution, a 10-week 10 project adventure, which was really meant to provide a very broad basis of basic core AI skills 

that were notably in general pretty pre-agentic

little, agents would come a little bit later. In February, we released ClawCamp

Which was a zero to agent team program that was not simple at all

which gave people a guide

to diving into this new crazy agentic world that had been enabled by OpenCloud

Agent OS came just a little bit later and was the more mature, grown-up version of ClawCamp that was not only platform and tool agnostic 

but helped people build not just a single agent or even an agent team, but an entire agentic operating system capable of taking on increasingly complex work.

AI s, finally the AI Summer Adventure

It was a choose your own adventure style program that provided a bunch of fun skills at a variety of different levels 

to people who wanted to stay sharp over the summer. common. Now, there are a few things that all these experiences have in common

They were all free, self-directed, project-based learning experiences. The whole goal [00:03:00] of which was to provide a framework for you to actually go do this work. The pedagogy behind them is pretty simple. it's that to learn how to use AI, you just have to use AI 

AI 

they're all kind of anchored in the truth that at this point there are still no AI experts, there are just people who have practiced with it more

But the other thing that they all are, ultimately and at core, is individual

Year, now with AIDB New Year's, you could form a team, but it was a team only in the sense of mutual support. people going through an individual experience in parallel

pattern-- all the other programs follow the pattern that pretty much all agentic work has so far, which is people building and leveraging individual agents for their individual work The thing is

Not all of our work happens individually. In fact, for most of us, some major and meaningful portion of our work happens as part of a team

a, a recent survey of around 16,500 office workers found that something like 39% of the workday is spent working alone, while 42% of time is spent working with [00:04:00] others

Another survey found that 57% of time is spent communicating i.e., meetings, email, chat, et cetera, versus 43% creating individually And yet another survey found that about 60% of time goes to work about work. Communication, search, coordination, and process

In other words, a significant portion of knowledge work

happens on a team, and the majority of knowledge work runs through team context

Collaboration, meetings, email, chat, coordination, search Those are the substance of a huge amount of work

and yet so far, the vast majority of agentic efforts have been entirely personal Think about all of the early experiments that you've heard about

It's all people building their agent teams, their researchers, their writer agents, their coding agents, their personal chief of staff agent

Advanced users are, yes, experimenting with agent teams, but it's agent teams that serve only the individual

Now to be clear, I don't think that's going away. I think the fact that all [00:05:00] of us now gets to be a manager of a big extensive team of agents that themselves can spawn sub-agents to do lots of different work is now just part and parcel of being an effective knowledge worker.

However, what I don't think that has changed is the fact that much of the meaningful work that we do will not be in our own individual silos, but at the intersection of where we work with other people

ins-- And my strong, strong belief is that the next frontier of agent design

is going to move agents from the individual silos in which they have operated so far

to the shared spaces that teams inhabit together

That means team-owned context Not repeated context where everyone's individual folders have the same documents in them, but one single repository that is shared across the team. It means shared sessions, observable work, and live steering and handoffs where the agent is working, again, not in the solo of someone's individual computer, but in some sort of shared environment where multiple people can have input

All at [00:06:00] the same time and in the same session. 

this is the move from single player AI to multiplayer AI. From individual AI to team AI. AI, the move from single player to multiplayer AI is a move from private outputs, where teammates can only see the final answer, to visible work, where everyone can see what the agent is doing

It's the move from feedback prompts where teammates can only interact

after some output has already happened, to live participation where teammates can redirect, annotate, and join while the work is happening The shift from single player AI to multiplayer AI is a shift from personal memory to shared context, where the durable context belongs to the team, to the channel, or to the project

And ultimately the shift from single player to multiplayer AI represents a shift from agents being about only individual leverage to becoming team capability Not just personal efficiency tools, but agents as reusable organizational infrastructure

Now, as some evidence that this is in fact a trend and not just something that lives in my [00:07:00] head

I think that there are a few examples from the last 90 days or so that have made this pattern pretty clear One, which I don't know, it might actually have been longer than 90 days ago because they're pretty ahead of the curve. At the beginning of the year with the claw camp moment

The team at Every started their agentic experimentation by having everyone have an individual agent that was the mirror of the person who owned that agent. Before long, they realized that that wasn't really how work got done, And they started to shift to a model that had more agents in their shared spaces

doing work that intersected the teams

A big product moment for this, and this might be the clearest product expression of multiplayer AI so far, was when Anthropic introduced Claude Tag

Claude Tag lives inside Slack

But it's different than the previous implementation of Claude and Slack that existed before

The original Claude integration in Slack was one where an individual could tag in their personal Claude, bringing them into a conversation, and then sending them off to do things and managing their personal Claude [00:08:00] from that work interface. Claude Tag was something different

Claude tags are instances of Claude that are shared across an entire team as expressed by specific channels that can each have their own context, tool access, data access

or other types of access that allow that shared Claude to do the work. In other words, when you tag in Claude now in your coding channel, it is not your personal Claude that you're tagging in, but the shared Claude agent that works across your team

The team at Anthropic wrote Tagging Claude comes with a few new advantages. Claude is multiplayer. Within a given Slack channel, there's one Claude that interacts with everyone. That means that anyone can see what it's working on and can pick up the conversation from where the last person left off.

This makes tagging Claude very different from working within a single chat or for a single task. It's much more like interacting collaboratively with a teammate

Because Claude is multiplayer, it can also learn over time. It follows along with the channel that it operates in, building more context about the [00:09:00] work. Because it is operating in that shared team multiplayer space

Each individual user that comes in and needs something doesn't have to explain things over and over again from scratch.

The multiplayer team shared Claude also has the ability to take initiative Teams can enable a setting that allows ambient behavior

that proactively interacts with the information from the channel that might be relevant for its type of work

Now at this point, Claude Tag is only just starting to dissipate across teams, but certainly for Anthropic themselves, it has fundamentally changed the way that they work. In fact, in that same announcement post, they wrote that 65% of their product team's code was now created by their internal version of Claude Tag, i.e.,

not a bunch of individual developers using their own Claude agents to contribute PRs, but a shared space

with that shared agent working between them that's pushing nearly two-thirds of their code

Another re- another recent example of this pattern comes from the OpenClaw 2.0 launch

After pushing relentlessly for the first part [00:10:00] of the year delivering an update every couple of days. 

the OpenClaw maintainers went quiet for about seven weeks to coordinate around a much bigger and more extensive rebuild

initially they tried to collaborate by having all of their different individual agents work together in Discord

But what they found is that that still wasn't collaborative enough

One of the company's maintainers, Colin, wrote, " What we wanted was a way for both developers to see the work itself. If an agent paused because it needed clarification, either of us should be able to jump in. If something needed a second set of eyes, we should be able to open the same session and look at the same context.

No screenshots, no copied transcripts, no here's what the agent has done so far data dump. Just open the work and continue."

And 

they ended up building a new multiplayer web UI for OpenClaw that allowed for exactly that

Colin continued later, " The feature that made the difference wasn't simply seeing another avatar online. it was being able to share a session while work was happening. When something needed another opinion, we could both open the same thread. When the agent needed information one of us had, [00:11:00] that person could add it directly.

There was no need to copy the conversation into Discord, explain what happened, and then carry the answer back. We were working inside the same context. That sounds like a small interface improvement, but it changes the way you collaborate with an agent. The session stops being a private conversation between one developer and a model.

It becomes a shared piece of work another trusted developer can inspect, steer, or take over."

So now you have the very advanced users of the Every team, the Open Claw team, and the Anthropic team all shifting from this individual agentic behavior to this shared team multiplayer agentic behavior

And I don't believe that this is just going to be constrained to coding. What it is to me is clearly agents evolving along a natural pattern to speak to the other half of work that we do that they don't touch yet, which is the work that is shared with other people

One more piece of evidence that this is going to be a thing Each quarter, Y Combinator partners share a request for startups, and it's a great way to see where a very advanced group of investors think the world is headed by them asking for companies that are addressing particular issues.

One of their themes for [00:15:00] fall 2026 is, you guessed it, multiplayer AI. Y Combinator partner Aaron Epstein wrote, " The best work tools of the last two decades won by going multiplayer. Google Docs replaced Microsoft Word. Figma beat Photoshop, and they turned solo tools into places where teams do their best work together.

But AI hasn't had its multiplayer moment yet. AI agents are the mostpowerful new tool a team has

But it's the one thing people still use by themselves. That's because right now, working with AI is largely single player. You open a chat, type a prompt, and get an answer in a box only you can see. When you want to collaborate with your teammates and agents, the best you can do is send a link to a read-only transcript they can't touch.

That's about to change. Agents are starting to run tasks that take hours, days, even weeks. Work at that scale was never meant to be done alone and pulls in many people across a company. Anyone on a team should be able to drop into the same live agent session to watch it work, redirect it, and hand it off the way they'd work with any other human team member.

This turns the work a [00:16:00] team does with agents into a shared living thing instead of a thousand private threads. We think there's a version of this for every kind of work: shared agents for engineers coding together in real time, for sales teams working a deal together, for support teams resolving a ticket, for lawyers drafting a contract, analysts building a model, and marketers shipping a campaign.

Anywhere a team already crowds around one problem, there should be multiplayer agents they all share

Now we here at the AI Daily Brief

are not addressing the startup and build side of that question, i.e., we're not releasing multiplayer agents for some specific use case But what I think that we can do is help your team build the foundations for using multiplayer agents and AI well.

enter this fall's free self-directed education program, The multiplayer AI sprint for teams

You can find this linked from either the aidailybrief.ai website or the extremely clever direct URL, multiplayerai.ai

The idea of the program is to build a shared four-week sprint for your team 

to get yourselves [00:17:00] ready to use multiplayer agents and then to actually try one in practice

Now, at the time I'm recording

we're still finalize- we're still finalizing some pieces of this platform. So what you see on your screen now might change slightly by thetime you're actually signing in. but what I wanted to do was go through the four weeks at a high level to give you a sense of what the sprint involves

Week one or session one of four, you certainly don't haveto do it in just one week. You can do it all in one fell swoop if you want. But in any case, the first session is an inventory to find out what your team is actually running

The goal of this is to take stock of how people on your team are currently using AI and agents 

Is 

everyone still just prompting ChatGPT or Claude? Has anyone actually built or managed some agent that does recurring work for them? Does anyone have context files? or has even broached into using skills with an agent? 

agent?

almost inevitably on any team, there is going to be a wide range of what people are doing currently. But figuring out where everyone is, is a really important first step in making the leap from single [00:18:00] player AI and agents to this multiplayer team type of usage

with,

as with each of the weeks, there will be two parts of this experience. A part that people do on their own, and then a meeting where they come together and share. The part that you do on your own is to actually build the portfolio that helps you explain what you've done to your team.

Now, certainly you can do that on your own

But you can also use the builder that we have natively on the multiplayer AI site to take a short interview with our AI to help you build that shareable portfolio automatically

if you do choose to use our tool, it can contribute to a shared space that is just for you and the rest of the members of your team, where you can see all of the answers to how people are using AI all together in one single spot 

kind of 

creating a living artifact of the type of thing that you would discuss in that shared meeting Now for each of these different weeks or different sessions, we wanted to give people a lot of different options.



you can, as I said, do everything inside of our platform but if you have security considerations that you don't wanna deal with, You can also just download the worksheets and do them in your own spaces without ever touching or leaving anything about your

team on our site

You are also welcome, of [00:19:00] course, to simply take inspiration from this and do your own version of it I don't care at all about you doing the work in our space. All I care about is you getting ahead of everyone else understanding that multiplayer AI is coming and getting there first.

Now, some of you might be thinking to yourselves, "What if our team is still really nascent and actually doesn't have a lot of AI or agents running yet?" Does that mean we shouldn't do this inventory week?

The short answer is no. And I think that there are two valuable things that you could do with it. The first is the other type of inventory that you could take would be to explore what your barriers have been to see if those are things that your team as a group can address to make this multiplayer AI a little bit easier than the single player AI that hasn't happened yet.

The other approach, however, that I really like is to go find someone or some set of people in your company who are advanced, even if they're not on your team, and ask them to present to your team how they're using AI and agents, presumably within the same guardrails and constraints and governance protocols that your team will face as well That can be a great way to see what [00:20:00] power users inside your own company are doing, even if that's not exactly what your team's experience is so far



sprint week two or sprint two is all about context

Remember, one of the key things that we're going to be doing as we move from single player AI to multiplayer AI 

is moving from individual memory to shared context

But to do that, the members of your team 

kind of have to figure out what that shared context repository needs to know

So in the second sprint

We have a tool that can help you extract context about yourself

that can be shared with the team, or again, you can download the worksheet and do that in some other shared space



Again, there's an individual and a sharing component of this 

you write down your context on your own with the assistance of our AI or some other AI, and then you bring it together with your team to put together that shared repository

week three, we move from figuring out what context we share to mapping out the areas where our work actually overlaps

Now a note here. The multiplayer AI sprint is assuming nothing about how sophisticated a team's understanding of itself [00:21:00] is. It is absolutely possible that some teams will, right out of the gate, even as you are listening to this, know exactly what shared work you wanna focus agents on. And so to the extent that that's the case, you certainly don't have to go through this process.

All of this is just designed as an asset so you can go from zero to multiplayer agents inside the context of this sprint. but the idea of this sprint or week three of discovering the shared work is once again to use AI to do a short interview that walks you through your common work and maps your work streams.

For each recurring work stream, the interview is gonna ask what it is, who else touches it, what context it needs and how often it's run

when you have work that overlaps with others, that becomes a candidate for where a shared agent could live

And from there, we're gonna give you a framework for how to score a candidate



I suggest looking at it across four different dimensions. The first is shared need. How many people need the same context for this? Obviously, more is a better candidate for a multiplayer agent The second is a staleness [00:22:00] cost. How much does it hurt when each person's version drifts?

The third category is permission sensitivity. How much restricted data does it touch? And the fourth is checkability. Can you tell quickly whether an agent got it right?

A simple way to figure out where you wanna start experimenting would be to score each of those axes on a one to five scale

And then squint at the ones with the highest scores as your potential candidates

Now, the fourth and final part of the sprint is actually one that you can repeat over and over again. The idea is to ship and start to use one shared agent

On whatever tools you already have access to Loaded with your team context, used by at least two of you on real work.



now certainly if you have access to Claude Tag, that's a really easy way to test this. but we'll have some ideas for other ways that you can set up a shared agent as well inside the system

The goal then is to test one shared agent, give it some amount of time to see if and how it changes the work, and then ask if it actually improved things

It may be that some use cases, despite there being a lot of shared overlap between you and [00:23:00] others

just aren't the right shape for an agent to get a lot of value currently. That's okay. That means you move on to the next shared use case to see if an agent can help there

And again, theoretically after,a single rotation of this, you can be done if you'd like. But you can also run this basically repeatedly 

working through each potential space that you uncovered that could be a good fit for a shared multiplayer agent

So that's the idea As with all of our programs, this is just meant to provide a loose framework that allows you to dive in and figure something new out through experimentation

When you sign up, you'll get an invite code you can share with other members of your team to make sure that you're all working in the same shared space together. and if you choose to share your artifacts can all resolve to the same spot

Now, if you'll permit me, I would also be remiss at this point to not note that if you are sitting here feeling a bit overwhelmed and like you don't exactly have the foundations even on single player AI to really be effective with this

I would recommend either A, going back through some of our free programs like the AIDB Agent OS program, or if you want even more support than that, [00:24:00] checking out some of our paid executive programs, specifically the Executive Catch-Up Program and the Executive Agent Leadership Program.

In particular, the Agent Leadership Program

is going to leave you in the top 1% of people who actually understand how to build and interact with agents, which obviously gives you a huge advantage as you shift from thinking about single player agents to multiplayer agents And the next iteration of that program is actually starting this week, just following Labor Day

Day.

there's a link of course to that in the show notes

Overall, the important thing to me here

is that it seems fairly obvious to me when I squint at it, that this is the direction that things are headed. Again, it's not that you won't use individual agents. You absolutely will 

and not just one or two, but you will probably have entire fleets and teams that you manage

What I'm convinced of, though, is that that only represents one part of the work that we do. And so it is only natural that we start to figure out agents for the other part of work, which is the work that lives between us. I think that if you and your team work your way through this sprint, you will be in a significantly better [00:25:00] position to use these new multiplayer AI tools as they come online

and be a leader in this exciting new world of team and multiplayer AI

Again, you can find all these links at aidailybrief.ai or go direct to multiplayerai.ai. Yes, that is two AIs in a row

and I'm excited to join this experiment with all of you

We'll also set up a community for this on the AIDB operator circle, so look for a link for that in the show notes as well

All right, guys, for now, that is gonna do it for today's AI Daily Brief. Appreciate you listening or watching as always, and until next time, peace 

​
