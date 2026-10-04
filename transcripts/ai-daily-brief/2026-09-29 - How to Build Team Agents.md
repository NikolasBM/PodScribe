# How to Build Team Agents — Transcript (2026-09-29)

https://aidailybrief.ai/e/2026-09-29 · Listen: https://pod.link/1680633614

---

[00:00:00] 

2026 has been the year of agents. From OpenClot at the beginning of the year to now platforms like Muse and GrokBot and Instinct that are getting people to actually take advantage of these incredibly powerful autonomous tools that are getting increasingly large portions of their work done for them

We really have gone from agents being the next big thing to just being here. The problem is our work isn't just done alone. We tend to work in teams with other people. And yet up till now, most agents have been solo affairs, only covering the portion of our work that we do on our own I think that is shifting now.

a trend which I've talked about as multiplayer AI or shared or team agents But what does it mean to even build a team agent? what are the types of considerations that go into it? And how different is it really than just building an agent for yourself?

those are the questions that I get into with Nufar Gaspar on this operator's cut edition of the AI Daily Brief

The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI. All right, friends, quick announcements [00:01:00] before we dive in. First of all, thank you to today's sponsors, KPMG, Blitzy, Harbor, and Hyperagent. To get an ad-free version of the show, go to Pa...

To get an All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, Blitzy, Harbor, and Hyperagent. To get an ad-free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts. And to learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai.

just a couple other notes before we get in. Obviously, this is a pre-recorded episode There are a bunch of things cooking today. We will have a lot to talk about, So we will be back with our normal format tomorrow.

I also wanted to share a couple of upcoming opportunities

First of all, this Thursday, October 1st, We have a free live webinar all about building your personal AI benchmark. The whole idea is that when you get a new model like Opus 5.5 or Sonnet 5.5 or Gemini 4 or whatever model comes next This will help you put together your own standard benchmark to [00:02:00] better understand where that model is going to fit into your own process That is completely free, and if you register, you will get all the materials after, even if you can't attend.

again, that is coming up this Thursday, October 1st

Now speaking of training, if you wanna go a little bit deeper, The next cohort of our super intelligent executive AI and agent training programs is coming up

the Executive Agent Leadership Program is where you learn

how to build AI agents for real business needs, as well as building a playbook to scale them safely across your organization

And if you feel you need a little bit more background before you get into that, you can also do the executive catch-up program

The next Agent Leadership Cohort starts on October 5th, while the next Executive Catch-Up Program starts a week later on October 12th

All right, with all that out of the way, let's talk about how to build team agents 

All right, Nufar, welcome back to the show. We got a, an operator's cut today

Yes. Happy to be here again.

this one has its genesis in some conversations we were having as we were coming up into the fall [00:03:00] around, what we wanted to do with the, you know, this fall's edition of a free self-directed training program. And, we were talking a lot about this idea of multiplayer AI and a shifting pattern, from people just building solo agents that they were using themselves to a prediction that we're gonna start to see, and I guess we're starting to see early evidence of, more agents that live in between people's shared workspace.

And this kind of just follows the natural way that people work. A lot of your work is done individually, but then lots and lots is also done at the intersection, with other people, and that's where team agents can live. And, as we were building out that course that's available right now at multiplayer AI and just thinking about this concept more broadly, one of the things that we kept coming back to was that this is nascent enough that what it means to actually build a team agent won't necessarily be super obvious.

And so the goal of today's Operator's Cut is to help actually think through how to build team agents, to understand what team agents look [00:04:00] like, to understand in what ways they are different from or, I think probably what we'll argue here, similar to the types of agents that people might have already built, and where they can go from here.

So super excited to have you back and, and excited to dive in here.

amazing. So I'm gonna bro-broaden your,definition, and I'm gonna call them team agents, and the concept is teams that your entire team can work with, whether it's because work happened between them or just because they are, something that can be shared across, team members. And kind of the short version is that some agents should stay yours and private, while others should become the teams level agents.

and the ones that do become the teams need a few decisions made on purpose. some of them, as you said, overlap with any, good agent configuration, and some of them are more unique or at least more intentional, and that's what, we'll walk through. And I wanted to start as a means of, motivation to, give you, like, two stories that you will probably recognize for your...

from your company or your ecosystem. so the first is about a person that everybody that I [00:05:00] work with, every company that I work with has at least one like that. And this person, they really know how their pricing exception work or what the data ac- is all about, or how our biggest customer setup was configured three years ago.

And when they're, swamped, then work has to wait for them because, they're the only one who knows. And when they're on vacation, someone still calls them, and when they leave, a piece of the company leaves with them. So in one of the companies that I work with, they had, I think, a person like that for each and every domain, so no one gets to take vacation without getting a call from their peers, and obviously, that's not a desired state.

The second scenario is, work that nobody fully owns. So a customer can move from sales to marketing to customer success, and then sales made them a promise during the deal conversation, and marketing is running a campaign with slightly different messaging, and then customer success finds out these promises were made to them a few weeks before the renewal.

And each team has their own piece, and nobody has the whole [00:06:00] picture because the work sits between them, so to your point. And even if they are using AI in each step of the process, these agents don't talk to each other and only worsen the problem in many cases. So an agent that is built for the whole team can help with both of these problems, and they are, of course, quite different, problems. So there is another reason, I think, why this matters right now and why you should pay attention now, even if you feel a little bit like this is above your head. And that's the pattern that I think what we're starting to see across the most AI forward companies, and it goes in basically three steps.

The step one is that everybody builds their own agents, and they're happy with their productivity boost only with enough of those running around,we kind of get into, an agent sprawl. Lots of agent doing overlapping work, each maintained by one person, each with slightly different picture of the company, and each one stops being useful, the day that the owner, loses interest or leaves the company.

And then what you see in the most AI forward [00:07:00] company, they started to, merge some of those, agents into team level agents. Those will typically be much fewer agents, much broader in their scope, and each, with a named owner and used by many people and, ideally refined over time as the team learns what they should and shouldn't do.

and this, is happening very publicly. There are many companies already talking about it. I think you mentioned Every's, experience. they started by giving every employee an agent early in the year, and then by May they have moved to shared team agents. Sierra merged many of their, agent specialists into one.

Shopify's internal agent. So we see a lot of these in very public, speaking companies all over the place. And most teams that I see, are probably either in step one or two. but I think that it's very important for all of us to look at these AI forward companies and understand how to get to number three and how to do it properly, and that's the entire purpose of today.

so to make sure that we, are talking about the same thing, Because there are multiple names to basically [00:08:00] the same, thing. Some people, including yourself, call it multiplayer AI. you probably also heard shared agents. Some people refer to them as AI teammates, and even company brain is, sometimes, thrown into the mix or inter-interchangeably used to mean agents being used, with shared knowledge across the company.

I'm gonna refer to them throughout the episode as team agents, and what I mean by that is we have one agent that many people talk to with, shared knowledge, shared memory, and one configuration. The instructions, the skills, the access, and the owner, they are all shared. And you might be thinking when you hear me saying that we already share skills, right?

M-most companies have an amazing, skill library or working on a skill library, and that's awesome, and that's great standardization, of how you do the work in the company. but a skill is ba- is a playbook for a specific task, where a team agent is something that your whole team works with on diverse set of tasks, ad hoc as well as repeated stuff, and it does carry the team knowledge, remembers what it [00:09:00] learns, and,using the team level skills if you have them.

those of course can also tap into, skills marketplaces and so on. so a skill library perhaps is one of the ingredients, but they are not one and the same. and I want you to today, think about, how and when to start building your next, team agent. And one more note on scope because there's a lot of excitement right now about all of the personal agents.

I'm talking about Muse and, Instinct and some of the other in this category. those are for, like, a h-home or private, life. today, the focus is gonna be on work. so that's one thing to ma-make sure that it's clear about the scope. We're talking about agents that you build for your job.

All right.

I want to make sure that we understand, like who I build the episode for, and I think it's built for, everybody and not just the frontier professionals that are building the, the absolute cutting edge. if you're about to build one, of course, pay attention, [00:13:00] because it will provide you or verify the full playbook.

it's also aimed at people who are not quite there yet, because the decisions, as you rightfully said, do apply, to any agent that you build or use. and a team agent just makes some of them even more critical. And even if you are working solo and you have, a team of agents or you're contemplating building a team of agents, you have the same decisions.

The other player in the-- your ecosystems are probably not your peers because you work alone, but perhaps you're building it for your customers, or you're building it for a future you to make sure that it's robust enough and representative enough of diverse set of work. So that's, the motivation or who should pay attention.

And, one thing that I wanted to, make sure that it's, very clear is that not every agent should be shared. there is, a dial here or a spectrum with, three settings. We have a private agent that's yours, for your work with your taste and your access. for example, my own social media agent stays private.

I'm probably not gonna be able to share it with anybody 'cause I'm the only [00:14:00] one that wants to share or write in social in a specific way. so nobody should ever sound like me. and then we have shared knowledge. those can be shared knowledge and skills, but still private agents, meaning the team maintains one body of knowledge, for example, what we sell, how we work, what our words mean, often with a shared skill library, and everybody points their own agents at that.

But this is where the skill library, lives, by the way, and it's often the right answer, and it's the easiest place to start. another concrete example, say every salesperson has a prospecting agent tuned to their own, style and their own, preferences. keep those agents as they are because every salesperson wants to have their own, voice, but give them all the same well-maintained picture of the ideal customer and the messaging for the company.

So that's a hybrid mode that, some companies or some, use cases should remain. And lastly, we do have the team agents, where we have one agent that many people work with, that has its own job and its own owner. [00:15:00] And agents can move, along the dial, and if you have a scenario where your colleagues keep asking to borrow your private agent, that's probably a sign that you, need to make it a, a team agent or to consider sharing it with others.

So the next question that I want to answer is, are all team agents from the same archetype, or, do they all follow the same type of use cases? And the answer, is not. Like across the teams that I work with, I can roughly categorize the existing or future-built team agents into four kinds. and knowing which your kind, is, the, it helps you not only identify use cases but also refine the use cases, and also it can tell you, what to pay attention to in order to get it right.

So the first type of team agent, I'm calling it the expert agent. It's the one person's know-how, or one small team's know-how. It's available to everyone who depends on it. you'll recogn-recognize it by the person who can't take the vacation, you remember from the beginning. if you want another example, it can be the data [00:16:00] agent that can answer any data question across multiple department in the company, or a pricing and deal desk agent that serves, a lot of go-to-market organizations, compliance agent, and so on.



in order to get it right, the knowledge has to come from the experts, that holds it in the company. they need to be interviewed, and they need to... you need to collect the answers they already gave in multiple forums, whether those are, direct messaging or emails in other places. And they have to be-- they, the experts have to be involved from day one, because for them, this is what finally makes the vacation possible, but also, a lot of job insecurity.

So tread carefully when working in this domain The second type is what I refer to the common work agent. that's the scenario where many people are doing similar recurring work with one shared way to do it. the way to recognize a use case that falls into this category is when three people have each built their own version of the same agent.



you can think about a team [00:17:00] research and meeting prep agent, that's a very classical one, or marketing team's, content agent, and I'm, I'm sure that you can think of others. In order to get this archetype right, you have to agree on, how work i-is done. And it's easier to say than to actually execute, because you're merging the best of three versions, and that's really a conversation about,what you agree in terms of the standards for the company.

So an interesting conversat-conversation at the very least once you start contemplating, unifying an agent like that. And then we have the bridge agent. That's the work that flows between roles where nobody can do it alone. you'll recognize it when the handoffs break, and every stage, has to explain the context or the agents have to somehow work together between different departments.



example can be a customer agent that spans, sales solution, customer success, and delivery. That's a very classical, one. And to get it right, we have to have each function their own piece of knowledge, that is being fed into this agent. And people with different [00:18:00] access, will be eventually using that, so we have to also pay attention very, very carefully to permissions and you'll have to, work, hard through that.

And lastly, we have the chief of staff. that's the agent that, own, the team operating, like, o-operationalizing of the day-to-day work. It can be the decision, the commitment, the status, onboarding, and you will recognize this one when the team keeps repeating itself, and new joiners take weeks to find their footing.



and in order to get this one right, what you need to do uh, you need to clearly define what it is allowed to learn, how can it learn the processes and the ongoing, and how does it do so automatically, which is not very trivial. and then there are also, of course, many questions around permissions and so on.



so while you're thinking about these archetypes, and which one of them might fit some use cases that you are pondering, or that you should be thinking about, and before I give you the playbook on how to actually build, these team agents, a quick detour, because I do want to, give a quick reality, check.

There are some signs that a team agent is the wrong [00:19:00] move or at least not the right move for you at this moment. so one indication where you shouldn't, build a team agent, at least yet, is when taste beats standards. If different people truly need different answers or are not willing to agree on a standard, and their own judgment or their own voice is the point, those need to remain private agents so people can, remain authentic, and not have to fight about the ground truth.

And the second indication not to build is nobody can own the knowledge. if the team cannot agree on how the work is done, or nobody is willing to own and maintain, the shared knowledge over time, the agent will drift within weeks, sometimes within days. so sort out the ownership before you go and build the team agent because, that's gonna be a no-go.

And lastly, whenever you're realizing that trying to build a shared agent, a team agent only complicates more than it simplifies because you have conflicting needs or tangled, permissions, endless coordination. if you realize that the result is more work [00:20:00] than, what the agent can, provide for you, that's the answer.

don't build it, at least not until you are able to untangle some of the complexities. And of course, notice what's missing from the list, sensitive data and high stakes. Those are design questions, and they shape how you build it, which is how, where we're going next. So I don't think that when data is overly sensitive is a, reason against.

It's just something that needs extra careful attention in order to, build the candidate use case that hopefully you've, gone through the decision, checklist that I shared before, it comes down to five core design decisions for your agent. it goes to, what it does, where it lives, what it knows, what it can touch, and how can you run it.

The- these are the core questions. in order to make it more concrete, I'll use one example the whole way throughout. So it's gonna be a customer, agent, and it's gonna be the bridge kind, meaning one that holds everything the company knows about each customer and everything we've promised them, and it's probably gonna be used by sales and solution [00:21:00] engineering and customer success, delivery, and so on.



they will be using that, example agent to do various customer-related activities. So let's break down some of these decisions to make it a- actionable. So first, the decision that you have to make is what it does. a quick caveat here, there is a lot of scoping that is very similar for any serious agent at work.



it needs to have a clear job and a definition of done and a list of what it doesn't do. I'm gonna stick here to what changes when it's built for a team versus, an agent that you build just for yourself. So the first decision is who it serves, by role. for example, sales asks it different, things than delivery does.

So write down each role and what they'll come to, the agent for to make sure that you're covering all the scope. And of course, you can aim for one broad area of work, because I think the team agent should be, quite capable agents, otherwise, it's harder to justify their existence. In our example, I would expect that the customer agent will be able to prepare a meeting, answers, where [00:22:00] do we stand with this customer, will be able to flag promises that commit, other teams, and draft every handoff.



for example, of a, a quite a broad scope. And what keeps it, focused is the area of work, and that is primarily, in our case, customers. I want you also to pay attention to, the team don'ts, list. This is the part people often, tend to skip. For example, it never, makes commitment on someone's behalf, or it never settles disagreement between people.

Those g- go to its owner. you can think of a- another such examples in your,case. also make sure that the don't list includes, permissions and, data handling stuff. So for example, it never carries information from one private space into a shared one, so it never discuss one customer in another customer space, and it doesn't speak for one person to another.



And of course, like with any agent, ideally start with, narrower scope, reading and drafting. Only when it, earns sufficient trust and was validated enough, then you can, increase [00:23:00] the scope as you gain more and more confidence. so that's the first decision, and we can move to the next one.



the second question will be where the agent lives. and this is the question that gets asked most, so let's be a little bit concrete. basically, if I'm trying to make it as, simple as possible, there are roughly three ways to share an agent, from the simplest to the most involved. The simplest method will just to create a shared folder, with your own tools, like the tools that your company already owns.



and then, each person just point their own tool to the shared, agent, and, the folder will include instructions and potentially how to, store new information as part of the way the agent, overall behaves. That's a very naive and basic way, but as a, a stepping stone to building shared agents and team-level agents, that can be, very good start, especially if all of your team members are already using, similar agentic tools or agentic tools that can point to folders as sources for their information.

So that's the first and simplest method. [00:24:00] The second, way that we can do that is using a vendor ready-made agent, and we're increasingly seeing more and more, and we believe that we will continuously see more and more in the coming weeks and month, of the year. We'll talk more about it later. but the way this work is that the vendor host it, and you configure it.

And in this category, we have many very, recently famous, tools, including, Claude Tag, OpenAI has their Ch-ChatGPT Workspace Agent, Copilot has their own offering, that can be used like that. Notion and, and many others, are already offering shared spaces, with agents that you can work together on, and it's just a matter of you configuring, their specifics.



and lastly, and that's of course, the most sophisticated, is an agent that you host, meaning that's something that you run. It can be, for example, an open source, agent like, OpenClou or Hermes, on your own servers, or, or on a, a leased cloud. Or, you-- some companies are even building their own custom harnesses specifically for these needs.



so that's the most sophisticated, but [00:25:00] obviously, has, the most, tech- like technically demanding requirements as well as the most freedom to build around that. so that's, the three, broad strokes options of where these, team agents can live. on top of the decisions of, how to build or the tools, there are two additional, questions that come with them.



The first question is who can see each person's conversation with the agent? maybe it's only the people who are conversing with the agent, maybe it's the entire channel or everyone in the session. over here, there is a lot of differences between the different tools. In some tools, everybody can read, every chat.



for example, in Claude in, Slack, everyone in the channel sees, what the agent does and w- and what the agent converses with others and can also steer it. with many other agents, your chat is private, so that's, sometimes a design decision by the vendor. Sometimes it's something that you can configure.



and the second question is what it learns stored, and who can read it? So an ideal, agent is [00:26:00] not one that is, obviously frozen, but one that has a lot of, memory and learning, on the go. And then the question, where is this learning, being stored and how does it happen? Is it something that happens per person, and then the, the agent ev- evolves just, from its interaction with you, or is it per channel or team, or maybe the, entire workspace has a shared learning and memory, and the agent evolves with everybody, in public.



and of course, one thing, never across customers. so do, check and choose and tell the team before the first real task, what's, the status with the, team agent that you built 'cause this is where, a lot of trust can be gained or lost. And my rule is to pick the simplest option that two people will actually use this week.



and for our customer agent, that's probably a channel agent or a, simple, like a tool agent because four functions need it, and if I will, make it overly, complicated, and people will need to understand how to connect to that versus just going into a Slack or a Teams channel, it's not [00:27:00] gonna work.

So in, in our case, that's probably gonna be the right, uh, solution. this decision. I wanna move arguably to the most important decision, and that's, what it knows. And I think if you've built any agent, the recipe will sound very familiar. What's different for a team is that this is the moment the team agrees on the ground truth, how the work actually gets done, which definitions we use, which versions of the pricing policy is the real one.

And I think that that conversation is worth having even if you never ship the agent, because in most teams, even just, agreeing on the knowledge is a big deal. And it's also where team agents get harder because the moment knowledge is shared, then you have more contributors and more contradictions and more places for something important to fall through.

So the process around the knowledge matters even more than, It ever did in your private agent, so you need to pay careful attention here. And ideally, you should go through these four stages. I want you to start by collecting, the agent, by interviewing the people who hold the knowledge and [00:28:00] harvest what's already written in all the channels and all the places where information already resides.

And I want, AI do a lot of the heavy lifting in terms of aggregating and collecting the data. so for our customer agents, for... what I would do is I'll make sure that sales and solutions and success and delivery, they all will contribute their own piece. and then I want you to refine. I want you to merge the information coming from different sources, surface the contradictions.

I'm sure that you will find, five versions of the truth, and then date everything, and keep out what should never be shared. Of course, that includes, passwords, notes about people, one customer's details in another customer's space, and so on. and then we have to approve it. each piece should be signed off by, whoever owns it, and the agent's owner puts it all together.

And lastly, this can go stale very quickly, so you have to maintain. You need to decide what, the agent may add to its own memory based on its,working, experience and what person has to [00:29:00] review first, when it goes into to the knowledge and the memory. And, we wanna make sure that one person's definition of what's last year, quietly becomes everyone's without any agreement.



and of course, put the upkeep on a schedule, because you want the agent, to, propose updates regularly, and a person needs to review and approve the updates. And this is really the place to be very, very diligent and disciplined because it can totally make or break your team agent if you haven't done, a good enough and self-sustaining, process around acquiring and maintaining and verifying the knowledge that the agent taps into because it no longer serves y- you where you can very quickly,fix anything that, goes wrong.



it can create a lot of havoc in your company if your team agent is, not well educated enough on what matters. The fourth decision is what it can touch, and this is where team agents differ from, the private ones because your own agent acts as you, and a team agent acts for many people. So [00:30:00] of course, there are many security 101 that you need to apply here, those that apply to any agent.

and you should definitely stick for the four rules that are specific to... Like, I'm gonna just stick to the rules that apply to team agents. the first thing that you have to decide is whose access it uses, and you have three options. You can, use the access or to act as whoever is asking, so it only sees what the person that was asking the question can see, and that's probably the safest choice, but sometimes the most complicated to execute the vendor already did it for you, and probably the right one when people, on the team have different access levels.

The other options that you have is to, have its own, account, set up with exactly the access the job needs, and that's right when the whole team works on the same shared material. And lastly, it can use one person's, login. only ever do that for read-only and non-sensitive material because everyone who talks to the agent gets that [00:31:00] person's access, so I would not recommend to go down that path.

And what I would probably do for our customer agent is to act as the person asking because sales success and delivery see different things in the CRM and in other systems, so I don't want to, have the agents, re-responding to them with information that they shouldn't be able to see. so that was, the first rule on what the agent can see.



the second rule is to decide who can ask it. And when the agent has its own account, everyone who can talk to it can use the account. And if you put an agent with access to the pricing sheet in a channel of 40 people, a few contractors among them, then all of a sudden all 40 can now get the pricing by asking.

The agent knows more than some of the people who can reach it, so decide who can talk to it with the same care you give to what it can see. Okay? So that's something that happens very regularly when people don't pay attention. I also want you to decide where the answer lands. this one runs the other way.

The agent uses the asker's own access, [00:32:00] and the asker has every right to ask the question. The problem is that the answer shows up in a shared space in front of people who don't. So this is, something that is happening right now. If you will look at,the commentation of Claude in Slack, it can use the asker's own connections inside the team channel.

And after the, person approves, and the Anthropic documentation, currently notes that, it doesn't consider who else is in the channel. So if I approve to use my connectors and fetch all the information that I am permitted to see, and now the information is thrown at the channel where others can see that, that's, the reality, currently with the existing, Claude implementation.

So if it's sensitive, the answer has to go to the, person who is asking privately and not in a shared channel. And lastly, keep record of who asked for what. And that's an important logging because when an agent works under its own account, the logs say the agent did it, right? And you want to know which person asked so you can backtrack and make sure that there are no, unexpected behaviors.

And everything [00:33:00] else, like starting with the least access and having a person approve anything that can't be undone, is the same for any agent. So I'm, I'm not, giving you security 101. Okay. Lastly, last decision and the one that wi-will make your team agent live beyond its first week or the first month, that's the full, like, operating manual, here.



of course, the multiplayer sprint has much more comprehensive, way of thinking about it, but these four points are what makes or break, the agents in practice. so the first thing is one owner. anyone on the team can hand, the work, but I want to have one person or a very small group of, of people who owns the priorities, maintain the agent, and decide, when two people ask for opposite, things, how to evolve the agent knowledge or, or feature set.



they also, decide on standing instructions and so on. so that's, one thing. The second thing that I want to mention is the clear rules of el- engagement. I want you to tell people how to work with it, what it does and doesn't do, and what it can see, who can see their [00:34:00] conversation with it, and everything that we discussed, so far.



we also, we want to have clear, indications of how to correct, the agent when it's, uh, wrong. and I think that people trust the agents, that they're using and the team agents, the more they know, the learn... what it's learning and what's the learning process. the next thing I want you to do is to put decisions where it can see them.

So a team agent only knows what's written down in a place that it can reach. And if your team decides things in private messages and hallway conversations, the agent will never hear about them, and part of running it smoothly is to, have it be able to tap into what's happening in real time in, in the team, and to make sure that the team decisions and the team, ongoing day to days, are being, learned by the agent itself.



and lastly, I want you to keep watching because you will s- probably start with a small, ideally, you should start with a small pilot group and keep a few, test questions that you can rerun whenever something changes. but I also want you to just monitor because, we know that things cha-change very [00:35:00] frequently, so it's not just a, about having a, a proper process for whenever you want to introduce a new model or a new tool or a new knowledge or, or, new changes in instructions, but also just to monitor that everything is working, properly.



and of course, in some cases, we would want to retire the team agent if it's not, behaving properly as we expected. we covered, a lot of ground, and if I need to pull it together before we close, first of all, I hope that I've convinced you that team agents matter for everyone, even if you're...

it will take you a while until you will actually be building one, and that building them properly is what makes the difference. of course, not every agent should be shared. a private agent, or a shared knowledge and skills with private agents or a team agents, these are all valid options and should be used, where appropriate we talked about the team agents that are coming in four kinds, the experts, the common, work agent, the bridge, and the chief of staff, and knowing which one, your use case, fits into tells you a lot about how to get it right.



and we also talked about three signs on when [00:36:00] to wait, whether it's because tastes, b-beats the standards, whether because nobody can owns the knowledge or when it doesn't simplifies, the work. and once you're building, we went over the five decisions in order of what it does, where it lives, what it knows, what it can touch, and how do you run it.

And if you take those with you, you have what you need in order to get the team agent, properly. if you want to concretely do that, a quick, way to do that, so first of all, the, we have the multiplayer, AI sprint, which is, free, and we'll walk you through a team activity of in four weeks configuring everything that we, discussed, some of them in greater detail.



if you want to learn how to, properly, build seriously team agents and a-agent rosters and how to do that in the best possible way, we have another cohort of the executive agent leadership that starts on October fifth, and we'll be happy to see you with all of our builders. However, if you feel that you need a little bit of a catch-up before you go and build agents [00:37:00] for, teams and, and rosters of agents and so on, we also have the executive catch-up that helps you become, best-in-class AI user before you go and build those agents.



and lastly, everything is changing. odds are that, every week we will get a relevant release, and by the time you hear this, maybe, already something was released. but I do think that everything that we covered today holds no matter what ships next because when an, an agent,is built properly and the decisions are made right, it's orthogonal to any specific tool or feature.

It's the business decision and the, team, standardization that matters much more than the tools that will help make it, better by design the more releases we will have. and if I need to make some predictions for the rest of the year, so I think that, we will see more and more formalization of what we just covered, and more tools and features that will help us get it, even better and easier, around identity, permissions, ownership, and so on.



as well as, like, we can always trust the practitioners to [00:38:00] share many of their learnings, in the public eye, so we can learn from, many of the, other, AI, like, frontier individuals and companies, and see how it's working for them. That's it.

Awesome. great stuff, Nufar. Um, I have a, few things that I wanna lob out there, discussion style just as we close out. First of all, I guess the question, you know, you gave four archetypes of different types of agents that you've seen. Do you see any of them more common starting places than others for teams that you've observed?

I think that in theory, your definition of an agent that lives between individuals or between teams sounds the most attractive, but it's the hardest to execute. So I think that's actually the ones that will, from what I'm seeing, are not the first to go for. And I've seen various very successful versions of the first one, of the expert agents, that help, create more redundancy in a team, redundancy in the good sense, and relieve some of the burden on the, those bottlenecks within the company.

So those I've seen a ton of [00:39:00] implementations already, and I think the more the tools make it more accessible, the easier those will be to build. So those are probably the lowest hanging fruits.

That's funny 'cause that's exactly where my head goes. I'm, I'm super attracted to the ones that I think are, are most difficult to build. I, I've also seen a, a lot of, you know, very simple implementation of that expert one, which, you know, we talked about for a long time without even identifying it as this sort of team agent, is just basically the agentified, team internal knowledge hub.

You know, policies around whatever, like early dismissal, who knows? Like what-- You know, that just the company database of information that you can access through the chatbot instead. That's been something that companies have had a ton of success with as just an early, easy, fast use case, right from the beginning.



another question that I have for you is how... You know, I'm sure that a lot of folks are, are sitting there wondering how much they should invest in building these sorts of things [00:40:00] before Grok Bot or Microsoft Copilot or one of these sort of core tools that they might be using, OpenAI, Anthropic, just drop the sort of native version of this.

And there's clearly some indications that they're thinking in this way, I think Claude Tag being the best example so far. But, you know, is this one where the value of digging in at this stage is gonna be so you understand the theory and the ways to customize when better tools come around in the future?

Or h-how do you think about that trade-off?



I think the heavy lifting is always gonna be the configuration and the knowledge, curation. so I would select the one tool that is adjacent the most to your existing tool ecosystem and, and figure out how to implement all the rest. And, and if n- like new, better improved tools come to play, we'll be ready because you'll all already agree on the ground truth on the, do's and don'ts of these agents, on the use cases.

So even if you at first implement them very naively, that's gonna have your future ready. [00:41:00] As for going and building these own, like competing products or your own like team level harnesses and so on, if you have the chops and you can do that easily and you have the justification, you can. But I'm not sure that I would have, spent my energy now on going and building, the own-- like, my own version of Claude Tag or similar when we were...

I think both of us agree that, all of these are coming and will probably be made very accessible and very smart, and your, moat is probably in everything that these companies cannot tap into.

Awesome. Well, thanks as always for another great Operator's Cut and, excited to have you back soon

Thank you. Bye 

​
