---
podcast: "how-i-ai"
podcast_title: "How I AI"
title: "How Warp ships 2,000 PRs a month with AI factories | Zach Lloyd (CEO, Warp)"
date: 2026-09-21
url: "https://podcasters.spotify.com/pod/show/pen-name/episodes/How-Warp-ships-2-000-PRs-a-month-with-AI-factories--Zach-Lloyd-CEO--Warp-e3p0f07"
guid: "c41174cf-cb70-49cc-80cc-73942e7dbb44"
host: "Claire Vo"
guests: ["Zach Lloyd"]
format: "interview"
level: 2
length: "00:46:20"
categories: ["coding", "agents", "work", "model-strategy"]
featured: ["Warp", "Slack", "computer use", "MCP"]
mentioned: ["Figma", "Instinct", "Claude Code", "Granola", "OpenAI Codex", "Grok"]
transcript_source: "azure-asr"
transcribed_by: "MAI-Transcribe-2"
---

# How Warp ships 2,000 PRs a month with AI factories | Zach Lloyd (CEO, Warp)

**Claire Vo** [00:00:00] Can I give you a hard time that humans really are the bottleneck? Because if you look at kickoff to PR time, it's 35 minutes, but if you look at PR to first human review, it's 3 and a half hours. And when you're doing, I think it was like over 2,000 PRs in the last month. Like, how do you keep things in the team from going, as I say, like chaos reigns?

**Zach Lloyd** [00:00:20] What is a software factory? For us, at least, it's an actual noun. It's like a product concept where it consists of a bunch of repos, a bunch of like MCP servers, like a bunch of configuration, and then a bunch of agents, essentially. So like a code review agent is on different agents, different automations, and it's all defined in code. Scoring happens across all runs, but then there's a second loop, popular thing on Twitter right now called self-improvement, where you have like an observer agent, and it can then create updates to your factory that will try to prevent the particular failure mode. One of the things that's most helpful is like you could have these factory agents do computer use verification. So in this case, it made a video. I'm just like talking to this thing that is doing this job that I've done for the last 20 years, and it's now it's like doing it kind of better than me.

**Claire Vo** [00:01:11] Spoiler alert, the humans are the problem. Welcome back to How I AI. I'm Claire Vo, product leader and AI obsessive, here on a mission to help you build better with these new tools. Today I have Zach Lloyd, CEO of Warp, and he's going to show us exactly what he means by the software factory. He's going to show us how you can kick off tasks in Slack, what it means to go beyond the software development life cycle, and how a technical CEO uses non-technical tools with AI. Let's get to it.

[00:02:23] Zach, thanks for joining How I AI.

**Zach Lloyd** [00:02:38] Thanks for having me. Excited to be here.

**Claire Vo** [00:02:40] There are a lot of trends on the timeline right now, but one that I think is going to be big for 2026, or seems to be big for 2026, is the factory. The factory, this like fantastical idea that we have that we're going to, you know, input tokens and output enterprise value, something like that. At least we'll output code. So I, you know, I'm excited for you to show us as CEO, as engineer, as builder, you know, what to you is the factory and how it looks inside Warp?

**Zach Lloyd** [00:03:12] The factory is definitely trending. I actually don't love the term factory, but it is the sort of thing everyone is standardized on. It feels a little bit sort of like dehumanizing to me, but, but yeah, the idea is exactly what you said. It's like, how do you, in a world where we have these sort of magical agents, kind of harness their power in a more organized way to have them, you know, basically build software for you from your ideas. And so, yeah, excited to show you how I use factories and like what it means to me.

**Claire Vo** [00:03:48] I was at Lenny's Summit recently, and I think Marty Kagan also said he hated the word factory. I wonder if it's more like Santa's workshop, right? Like, we have magical elves that craft wonderful things that spark joy, and are delivered, gift wrapped for us. So I'm going to say the AI, the AI magical, magical workshop. No, show us, you know, what does, what does this look like for you? Yeah, you did, you did say, you know, you put in

**Zach Lloyd** [00:04:14] Yeah.

**Claire Vo** [00:04:14] your ideas, you output product. Is that real? How, how does that really work?

**Zach Lloyd** [00:04:19] Yeah, so it kind of works like that. Um, the, the way that I think of, of factories is like there's, there's basically 2 types of personas who are using them. So there's, I'll show you like basically how we do this in Warp. There's like the builder persona. So the builder persona is someone who is contributing ideas, wants to build stuff. And from that persona, it doesn't look like, at least the way that we have it set up, it doesn't look that different from like how one of these engineers or designers or product people on our team might build with a local coding agent. The big difference you can see here, so this is like, this is our Slack, is that most work is starting in a public place. And so the way we think of factories is like, you, you basically can say in a public Slack channel, you can tag, we named our factory Wilson, you can tag Wilson and be like, okay, I want you to build something for us. And when you do that, what Wilson will do is like, essentially do not just like the direct build, which is what you might get if you're using like Claude Code or Codex, but we'll also like do a few other steps.

[00:05:33] So what it will do is it'll kind of go through all the steps of like, first it will triage whatever this is. So it'll treat it as like an input to the factory, not just like a direct thing to build, meaning it will, for this one, Harry's saying he wants to change the way this feature looks. He gives like pretty detailed instructions. He, you know, attaches an image. He says use computer use, and this kicks off a flow where the first thing that the factory does is actually kind of open an issue. So you can see over here, it's like we use linear in addition to using Slack so that everything gets tracked. So the factory integrates not just with Slack, it opens an issue, then it does the actual implementation. For this one, it's like it was simple enough and ambiguous enough that we could actually implement it. Then it does, it will create the PR, so it integrates also with like GitHub.

[00:06:36] Then it does the QA, which I think is like really important these days. Like if you want to not spend all your time doing code review, one of the things that's most helpful is, like, you could have these factory agents do, like, computer use verification. So in this case, it, like, made a video of the completed feature. So it's like showing the thing, showing all the keystrokes. And so what you get here is not just like, and then it gets merged, right? Is not just like the single step of build the thing. Like, if you were to do this with like a coding agent in like the pre-factory world, what you would typically do is like pull up your local coding agent, do the change there, test it locally, and then like push it up to GitHub. But you get the whole thing of like the ticket, the code review, PR, the video, all done together. And then the other like really, really, kind of magical thing is that it's all done in public.

[00:07:38] So if you are, you know, someone else wanted to come in and like look at this and see how the task was done or even contribute to it, and so we all have people like multiple people on these Slack threads, you get to a world where as like a builder, you're no longer sort of working in this local silo. Instead, you're working in a public space where everyone can see what you're doing. And so that's like, from the builder's point of view, how they like use the factory. Does that make sense so far?

**Claire Vo** [00:08:04] Yeah, and you know, I think what I'm reflecting for folks who are maybe still trying to grapple with, okay, like what's a coding agent? What's a factory? What's the difference? I think what I'm hearing from you is the factory, quote unquote, is comprehensive, comprehensively designed to reflect your version of what the software development life cycle should be. And so it's not just like idea to code to PR to push. It is, okay, an idea needs to go through several steps. It needs to go down the conveyor belt of product and into like the funnel of issue tracking, and then we need to code it, and then we need to QA it, and then we need to have these very specific verification loops where we can take our sticker and say quality controlled by, you know, number 1, 2, 3. And so to you and the way you're describing it, where it goes beyond a coding agent or a co-pilot is that it is actually designed to take the very specific end-to-end product steps, not just the engineering kind of like input output.

**Zach Lloyd** [00:09:09] That's definitely part of it for sure. It's like it does more of the software life cycle, so it does more of those steps. There's a whole other bigger part of it to me, which is, so I showed you this from like the perspective of the individual builder. If you were to go into our Slack, you would see like this is happening over and over, like all day long, the people in our team are building in this way. And sometimes, by the way, it's not just like the engineers who were kicking off work like this. It could be work that's being kicked off, automatically. So, for instance, we have, I don't know if you know Sentry, but it's like a crash reporting system. And so we have signals when there are crash reports coming from like our terminal app that we try to automatically fix those, and those go into the factory too. So it can either be human initiated, it can be initiated by like an external system, and it can be initiated actually in any of these tools.

[00:10:14] So it's like you can initiate it, like we could have started this whole thing in Linear, we could have started this whole thing in GitHub, and so it's integrated into all the tools. But the bigger piece of the factory approach, in my opinion, is not like, it's not so much how it, the individual builders work, because it's not all that different from individual builders who might be using, like, who might be going into the terminal, for instance, and using a coding agent to do something. It's different, it's in public. But what's really different in the factory approach is that everything is like centralized in the cloud, and there's a whole other aspect to it, which is for not the builders, but for the people who are like the managers who are like trying to scale software development on their team.

**Claire Vo** [00:11:04] Finally, something for the managers.

**Zach Lloyd** [00:11:08] It's what everyone's been wanting, right? Too much attention on the builders. No, but in all seriousness, if you're like, my concern, as someone who's running a company, is like, I want, I want soft, like, it's a super duper competitive market. I want to see how quickly we're moving. I want confidence that, the way that we're building software is actually improving over time. I want to make sure that we're not, like, wasting too much money. And in the world of, like, all of, like, every builder has their own individual local setup, that's very, very hard to get. And so this is like an engineering manager's dream. It's like a CTO's dream. Like, not that this is the coolest thing in the world, but it's like, now I have the ability to sort of centralize and see what everyone's doing. So, for instance, on this screen here, it's like these are, this is actual data from our team in terms of like how we're using the factory.

[00:12:10] It's like there's a sort of sense of like how automated is the factory?

**Claire Vo** [00:12:13] Mhm.

**Zach Lloyd** [00:12:14] What's our velocity? How long does it take us to like ship stuff? And so there's just all these measurements.

**Claire Vo** [00:12:20] Can we pause real quick on your productivity? Because I actually haven't seen this measure before, and we've seen a lot of measures, which is human interactions per PR. Just

**Zach Lloyd** [00:12:31] Yeah.

**Claire Vo** [00:12:31] talk us through why that, because honestly,

**Zach Lloyd** [00:12:33] Like, what is this?

**Claire Vo** [00:12:33] I hadn't heard that one before, and I like it.

**Zach Lloyd** [00:12:36] You know, the sort of instinct underlying this is that, we are gonna be, not to put this the wrong way, but it's like humans are a little bit of the bottleneck in terms of production itself. They're also the creative force, but in general, what companies want, and we're, you know, we're trying to build for companies at Warp largely, is like, how do you automate more? How do you make things that can truly just be done agentically be done in an almost fully automated way? And so, the general instinct is like, the more times you have to prompt, the more times you have to steer or like cajole your agent, that's like, that's going to be a limiter on throughput. So this is where you start to get into like factory world. Like, this is like, imagine you're running like a Tesla plant or something. It's like, how many times do you have to stop the line? Yeah. And so, you know, we're trying to give engineering leaders a view of like, okay, how are you, are you able to sort of make things more efficient over time?

**Claire Vo** [00:13:43] And quick question, are those, just because my mind, I mean, I, you know, as a once one-time CTO, I'm like, yeah, this is exactly

**Zach Lloyd** [00:13:50] Yes.

**Claire Vo** [00:13:50] what I want." Are these interactions- do you think of these interactions as like the prompts, the sort of like upfront steering? Are you thinking about, like, how many comments on PRs, how many loops? Like, how inclusive is this, like, interaction per PR score?

**Zach Lloyd** [00:14:05] It's- it's all of those. So

**Claire Vo** [00:14:07] Okay.

**Zach Lloyd** [00:14:07] because the- and again, I think this can t- definitely be refined

**Claire Vo** [00:14:12] Mhm.

**Zach Lloyd** [00:14:12] over time, and bear in mind we're like trying to figure out, so what is the right set of metrics? But

**Claire Vo** [00:14:18] Yeah.

**Zach Lloyd** [00:14:18] this actual metric, because the factory is like integrated into all of your knowledge work tools, it includes all those things, like how many reprompts in Slack, how many comments on Linear, how many times did you have to correct the thing in code review? And so, it's like a kind of like, yeah, it's a proxy for how much work did you have to do in order to, you know, get the thing to do the job.

**Claire Vo** [00:14:41] Okay, wait, I want to- I want to give you a hard time, one more thing.

**Zach Lloyd** [00:14:44] Yes, do it, please do.

**Claire Vo** [00:14:45] Because we talked, you know, but before we started recording, you said, like, how technical, and I was like, okay, well, we're going to put on the CTO, at least the CTO hat right now. Um,

**Zach Lloyd** [00:14:52] Okay.

**Claire Vo** [00:14:53] Can I give you a hard time that humans really are the bottleneck? Because if you look at kickoff to PR time, it's 35 minutes, but if you look at PR to first human review, it's 3 and a half hours, 3 and a half hours. And so it's like so funny that still cycle time, man, like it's the thing you really have to focus on.

**Zach Lloyd** [00:15:15] It's this.

**Claire Vo** [00:15:16] It's that, it's that number.

**Zach Lloyd** [00:15:18] Yeah. There's still the bottleneck.

**Claire Vo** [00:15:20] Yeah.

**Zach Lloyd** [00:15:20] And we're, I mean, we're still doing human code review.

**Claire Vo** [00:15:25] Do you do all, all your PRs get human code review?

**Zach Lloyd** [00:15:27] Do you do all, all your PRs get human code review.

**Claire Vo** [00:15:32] Wow.

**Zach Lloyd** [00:15:33] And so, now this is like, I think of a team choice, an organizational choice.

**Claire Vo** [00:15:38] Yeah.

**Zach Lloyd** [00:15:39] We have, the one thing that we have changed around this is not, like, we used to require, like, the workflow used to be like person A on our team would build something with an agent, and person B would review the agent's code. We no longer require that, like, the person who prompts the agent can also review its code.

**Claire Vo** [00:15:58] Okay.

**Zach Lloyd** [00:15:58] Yeah.

**Claire Vo** [00:15:59] You're making me feel better.

**Zach Lloyd** [00:16:00] So that- that's a better thing, but it's still like we, you know, we don't have yet complete trust. I think the way this will evolve is like some percentage of- some percentage of stuff will, um- will eventually, we'll feel confident enough that we can skip that.

**Claire Vo** [00:16:18] Yeah, I did an episode recently. I built an Eve agent called Merge Mommy, and this is the flow that I often see in even mature engineering organizations, is what you do is you basically like risk score every PR automatically. So go through, risk score it, and then anything that is low or extra low risk gets a stamped approval from Merge Mommy, and then a human's allowed to just smash the button and merge. Anything that's like medium high or whatever, or has some like outlier on risk requires human review, and that just like lets you get that bottom tranche of the queue out. also just so you have good capacity for high quality human review on the things that really matter.

**Zach Lloyd** [00:17:02] 100%. I think code review becomes an exercise in risk management. I think that's right. I want to show you some other stuff in the factory

**Claire Vo** [00:17:10] Yeah.

**Zach Lloyd** [00:17:10] just to show you, like, how this is different than just standard interactive agents.

**Claire Vo** [00:17:14] Yep.

**Zach Lloyd** [00:17:15] So you get, cost is on everyone's mind right now,

**Claire Vo** [00:17:19] Mm-hmm.

**Zach Lloyd** [00:17:19] and so you get, like, this is agent cost. It doesn't factor in the sort of cost of the people at the moment,

**Claire Vo** [00:17:25] Yeah.

**Zach Lloyd** [00:17:26] but it's like, you know, you can see, like, we were really expensive a few weeks ago. We made some changes to our model configuration, and we've driven this cost down, and we want to continue to drive it down, but just like having the centralized view for this across your whole team, super valuable.

**Claire Vo** [00:17:45] Can I ask you a question on cost? Quick question on cost. So, I mean, this is a pretty, you can see the drop here. I see this a lot when I'm talking to engineering organizations. They often see like a rise in cost of PR as they're per PR as they're adopting AI, which you all already have, and then we see this drop as you're doing optimization. Do you feel like the biggest lever here is model right now? It's like that the, is that the lever?

**Zach Lloyd** [00:18:11] Yeah, it's, it's model. I think model is the biggest. I think like context, like the way

**Claire Vo** [00:18:21] Context management.

**Zach Lloyd** [00:18:23] like context management matters as a secondary thing. I would say model is the biggest.

**Claire Vo** [00:18:30] Yeah.

**Zach Lloyd** [00:18:31] And the way to really figure this out actually is to test, which is something I want to show as well. But basically, I think model is the biggest one. Any other questions on the just like the spend view?

**Claire Vo** [00:18:46] No, that's great.

**Zach Lloyd** [00:18:48] So the other thing, like this is where it really gets kind of factory oriented, is like the way that we're changing development, and this is, I think this is most relevant for folks who are watching, we're trying to manage like these teams and scale coding agents, is like we now, we're like measuring everything. And so this last thing in here, which we call scoring, basically gives you a view, across all your agent runs of like how they're doing on different dimensions. And so we basically, because the factory is like a closed, kind of like closed loop system, like every time an agent does a task in the factory, that task gets recorded. And what that opens is the possibility for you to go and like, go back retroactively and look at how well the task was done. And so you could do this as a person, you could literally just go back and look at tasks, but the other thing that you can do is you can have agents do this, which is what we do.

[00:19:58] And so, for instance, let me see if I can find an interesting one. Like, here's an interesting one, like redundant tests. So if you're working with, you know what I'm talking about here? It's like

**Claire Vo** [00:20:10] Oh, I know what you're talking about. Every PR I push is like, I have run and set up 135 tests.

**Zach Lloyd** [00:20:17] Exactly.

**Claire Vo** [00:20:17] Here.

**Zach Lloyd** [00:20:19] It's, it's the, it's like, it's, it's like, and the reason it does this is because, you know, they're writing tests not to like prevent regressions necessarily, but also just to like test behavior along the way. And so you end up with a bunch of tests that you don't need. And so we, you know, if you take the factory approach, you kind of know this might be a failure mode. And what you can do is you can write essentially a, like a score that uses LLM as a judge to be like, okay, I want to go and look at, you know, all of the agent runs, and I want to see how often we're, you know, an agent thinks, a different agent than the one that did the task thinks that there's redundant tasks. This make sense?

**Claire Vo** [00:21:01] Yeah, totally.

**Zach Lloyd** [00:21:02] And so you basically are like, okay, I want, I'll pick a judge model. This is like a kind of medium smart judge model. You don't want it to be too expensive, otherwise you end up spending a lot of money on scoring. You have it classified in terms of like, for this task, like, how did it look? you pick like a sort of sampling rate on in terms of how you want to do this, and then you get, over time, a set of runs where you can see that, like, sometimes this agent thinks that there were some, like, surplus tests. And so this is what I mean by, like, the real measurement. Then what you can do is, like, you can go and you can actually, you know, as a human, you can go and kind of look at what's happening here, but I'll show you there's also a better way to do this in the factory world where it's like you can actually, use agents to sort of identify what's gone wrong in these runs and try to improve the factory. Does this make sense?

**Claire Vo** [00:21:59] Yeah, I'm curious, do you do this, on a per run basis or on an aggregate basis across a set of PRs?

**Zach Lloyd** [00:22:07] Aggregate, great question.

**Claire Vo** [00:22:08] Okay.

**Zach Lloyd** [00:22:09] So.

**Claire Vo** [00:22:09] Yeah.

**Zach Lloyd** [00:22:10] Yeah, so what we do is like the scoring, and this is what I call like this thing, we call this like the score, the scoring happens across all runs, but then there's a second loop, which is another like popular thing on Twitter right now called self-improvement, where you take an agent and you basically say, okay, for all of the failed runs, and you need like, you need like a real sample, like maybe 20, 25 failed runs. You need some significant sample size, otherwise it starts to overcorrect based on single, based on single things. You have it look, you have like an observer agent look, and it can then create updates to your factory that will try to prevent the particular failure mode. And so, let's see if I can find one that's like, I don't know, this I'm just literally picking a random one here, but this is finding some issue with our skills that are driving the factory.

[00:23:13] It's presenting evidence, and it's saying, okay, we should change the definition of one of our factory agents in a particular way. And if you go under the hood and look at this, it's like it's changing this like step 10 of what our factory agent should do. Does it make sense?

**Claire Vo** [00:23:27] Yep.

**Zach Lloyd** [00:23:28] And so this is, to me, this is really exciting. Like the way, the thing that's like enabling this whole thing to work is that you define the factory in code.

**Claire Vo** [00:23:42] Code, yep.

**Zach Lloyd** [00:23:42] And so, you know, what I mean by that is like if you were to look at the sort of definition, you would say, okay, the factory, what is a software factory? It's like, for us at least, it's an actual noun. It's like a product concept where it consists of a bunch of repos, a bunch of like MCP servers, like a bunch of configuration, and then a bunch of like agents, essentially. So like a code review agent, design, like different agents, different automations, and it's all defined in code, and the value of doing it that way with, like, in Warp Factories is that you get the ability to actually, you can like test different configurations and know, like, you're basically freezing the state of the factory at a given point. So you can be like, okay, if we were to change the factory definition and like run all these tasks again, we could see if things were better.

[00:24:43] it also makes it so that like an agent can actually, because these are all, it's all code, like coding agents can actually update the factory to make it better. Does this make sense?

**Claire Vo** [00:24:54] Yeah.

[00:26:00] Yeah, I just want to like, you know, kind of sum up where we are so far because I think there's so much rich stuff in here, especially for engineering leaders and builders, and then I know we're going to get to some workflows that are not engineering focused, which I'm excited about. But the, you know, a couple trends, themes that I've seen as you talk through this. One, work happens in public. So I'm seeing, you know, this move towards instead of work being assigned in tickets and then tickets being worked on laptops, work is happening in public, whether it's Slack or some other channel, and then executed in the cloud, so sort of anybody can interact with that. The factory does have this software development lifecycle kind of like definition to it, but on top of that, it has this aggregate meta analysis that you're doing across all the behaviors, which is giving, as we said, giving the people, the managers, what they want, which is, are we getting more efficient over time? Is this factory actually effective? How many humans? How many agents? What's the interbalance between the two? Spoiler alert, the humans are the problem right now.

[00:27:03] And then, and then what you're doing is you're also doing these evals against key behaviors in your factory that you want to correct. and this is something that when I talk to engineering organizations, I tell them all the time, which is such a challenge when you're using something locally, like, for example, Claude Code, is I say you need session level telemetry because you need to be able to aggregate up the failures within sessions across your engineering team. And so some teams do this truly by like sucking up every local coding session to S3 and running their evals kind of like on their own, in their own platform. But I do believe that if you do not have session, tool call, MCP call, test failure, computer use level observability into every single coding session, you're missing a lot of opportunity to optimize efficiency, cost, model, just like how your team uses the tools.

[00:28:05] And so I think it's super important that people do this, and then what you've added is this extra layer of, great, then take those insights and make the factory better, however you define better.

**Zach Lloyd** [00:28:17] This is a great summary.

**Claire Vo** [00:28:19] Great, I did it.

**Zach Lloyd** [00:28:21] Great.

**Claire Vo** [00:28:21] Professional podcaster.

**Zach Lloyd** [00:28:22] There's, there's, there's what, just to give a sense of how you can continue to like, you can go even further once you have this data. I think your summary was awesome. The other thing that you can do, and like, I think end orgs are going to do this because this is, this is how, like, there's going to be nothing more important than optimizing the way that you like build and ship software in the future. And so one other thing that is really powerful, if you set up everything you just said, where it's like you have the tracking, you have the evals, there's one further way that you can make it even more powerful, which is adding the ability to basically take your own data and replay those sessions with different configurations to actually measure, like to your question earlier, like, well, how would it have done from a cost perspective or a quality perspective, if you'd done like different models? And so, for instance, again, this is what we have built into Warp Factories, but there's lots of ways you could do this.

[00:29:22] Like, the idea is you can, just like there are these public benchmarks like Sweetbench and TerminalBench that are on like generic data, you can recreate on your own data, like from real past factory tasks, how would things have gone had you used a different model configuration, for instance? So this is like a kind of Pareto chart, which again, these things are on Twitter all the time, but it's like what's cool here is like if you take the factory approach and are like really scientific around, okay, I want to know, like, I want to, let's say you wanted to curate a bunch of front-end tasks and then see, like, can I be using JLM 5.3 on those instead of using, you know, Opus? Yes, definitely. Should I be using Gemini 3.7 Flash? You're going to take a quality hit. and so, like, you get to choose your own sort of trade-offs here, and then you can feed this back into a model routing strategy where you actually have evidence that, okay, on your own tasks for these types of, like, the best model configuration for cost and quality is, like, whatever you find.

**Claire Vo** [00:30:39] Are you comparing that to what actually shipped? Like, how are you evaluating quality? You know, there's like 7 ways to skin a CSS. Like, how do you actually

**Zach Lloyd** [00:30:49] Yeah.

**Claire Vo** [00:30:49] decide, you know, this is better quality or not on front end tasks, for example?

**Zach Lloyd** [00:30:55] Yeah, awesome question. So the way that we do it in Warp Factory is, and you're gonna probably, you can do different things here, is we use the exact same, like, scoring infrastructure that I showed you earlier. So, for instance, you know, we over here, we have all these different scoring dimensions. So you can, if you have confidence in this scoring infrastructure, basically you're replaying past tasks and trying to see if there was like how it affected these scores. So it's primarily LLM as a judge, but you can also, it's like you could do this with human judges, you could do it algorithmically, but the thing that we have built is LLM as a judge.

**Claire Vo** [00:31:33] Got it. Super interesting. Okay, so you've given me so many ideas on how to take the factory idea further. I'm curious, just like take off our builder hat, our CTO hat. Let's put on, you know, I was talking to you again before we came on. I was like, people love to see how non-technical people can do technical things and how technical people can do non-technical things. So show us some of your other like AI use cases that are maybe less about evals and benchmarks and MCPs and more about, you know, being a CEO.

**Zach Lloyd** [00:32:09] Yeah, so we'll get, like, I think, like, zooming out, this is cool with all these charts. I still have a hard time making changes to Figma. and like, I don't know if you're the same way, but when I go to try and change like a Figma thing, I'm like, it's like I have three thumbs or something. Like, I just, I cannot figure out how to use it, but I do know that it's like if you, like, this is how we like do our slide decks, for instance, it's like we are using Figma slides, you can make things that look very nice. So one thing that I do now is like, if I need to change a slide deck, I do it through the Figma MCP and the coding agent. And so like, just to kind of show what that looks like, we have this kind of semi-boring, like, slide here on cloud execution. So I'll show you how I would do this, just so you get a sense. So I'm going to do this, I use this in Warp. I use Warp as a coding agent.

[00:33:10] This would also work in Claude Code or Codex, anything that has Figma MCP. And so I'll just paste this in, and then I'm going to talk to it, which is another thing. I assume people are on the voice train at this point. Are

**Claire Vo** [00:33:22] you on the voice? Yeah, we, we give all credit to Hilary Gridley. She calls it the Yappers API, highest bandwidth way to talk to an LLM.

**Zach Lloyd** [00:33:32] Yeah. So I'm going to say, like, I'd like to make a new version of this slide, use the Figma MCP to get the context, duplicate the existing slide rather than making changes directly to it. Let's have it be so that, the host box contains the runtime box. Let's, let me see what else I got. I gotta switch back here. So we're gonna have host contains, sorry, host should contain sandbox. I'll go back and edit this. Let's make the context system something that's like, kind of like, you know, cloud around these things that feeds into them.

**Claire Vo** [00:34:19] True CEO, put a cloud on the slide.

**Zach Lloyd** [00:34:22] You're going to see some bad design here. Let's make the launchpad have a sort of like rocket type theme. This is my, this is not what my sales team wants, by the way. and let's make tracking. I don't know, why don't you come up with some ideas for how to make tracking better? The overall idea here is to make this slide more visually appealing, than the simple, you know, five boxes and semantically show the relation of the boxes to each other. So I'll do this.

**Claire Vo** [00:34:59] Do you know what word I say to Figma? I say semantically

**Zach Lloyd** [00:35:05] No, what?

**Claire Vo** [00:35:05] to Figma MCP all

**Zach Lloyd** [00:35:07] Really?

**Claire Vo** [00:35:07] the time. Oh my God, all the time. Semantic color, sema- sema- semantic. It is, it is my orthogonal.

**Zach Lloyd** [00:35:16] That's really funny. Yeah, I mean, um, uh, we'll see. So, and I'm using- I'm using Grok a lot recently, um.

**Claire Vo** [00:35:28] Same.

**Zach Lloyd** [00:35:28] I don't know what your model of choice is. I think Grok is pretty good from like the cost and speed and quality, quality trade off. I could show you how I could do some other, you know,

**Claire Vo** [00:35:39] Yeah, why don't, why don't, while that's loading, why don't you show us something else?

**Zach Lloyd** [00:35:43] Yeah, I'll show you another one. So I- I'm a big Granola user as well. And so, again, if I were really trying to improve this sales deck, another thing that I would want to make sure is that the sales deck is speaking to the things that customers are actually talking about. So I'm going to start a second task here using the Granola MCP, where I'm like, can you use the Granola MCP to look back over my last four weeks of sales meetings and try to build up a list of the top 10 frequently most asked questions in these meetings as they pertain to Warp software factories. Don't list any specific customer info in the summary, anonymize it, because I'm doing a podcast. So we'll get this one cooking as well. I can do one more if you want.

**Claire Vo** [00:36:40] Yeah, let's, I mean, let's queue them up again. I love to see a AI-pilled CEO just open tab after tab after tab and kick stuff off.

**Zach Lloyd** [00:36:50] I mean, this is stuff that, this is stuff, these are all, by the way, real things that I am constantly using AI for. So the last one is like, a task that I use AI for is trying to rediscover potentially like cold leads that I might have talked to in the last, like, you know, 6 months or so. You know, our product has changed a crazy amount. I might want to re-approach them. And so the thing that I use for this, or had in the past been using for this, I actually just started using Instinct. Do you use Instinct?

**Claire Vo** [00:37:25] Oh no, I had a bad experience with Instinct.

**Zach Lloyd** [00:37:28] You had a bad experience with Instinct. So the normal way I would do everything is still through my, is still through a coding agent, but I would, let's, I'll do one more prompt here. Can you use the GOG CLI to look for emails and calendar events I've had in the past six months with potential enterprise leads who might be useful for another outreach for Warp factories? You can learn about Warp factories at Warp.dev/factories and make me a Google sheet with the info on them and share the sheet link, but don't print out any specific customer email or name in this thread.

**Claire Vo** [00:38:19] What I like about this at the meta level is like, is this how your brain works, where you're just like, I need to do the slide, kick off the slide. I need to like update some of our sales position, kick that off. I need to like follow up with cold leads. Like, is this three panel, is this a reflection of your CEO brain? Because it's certainly a reflection of my brain.

**Zach Lloyd** [00:38:40] Yeah, I mean, if I were, if I were in like sales mode,

**Claire Vo** [00:38:44] Yeah.

**Zach Lloyd** [00:38:45] go-to-market mode, and like I am in that mode quite a bit now, unfortunately, more so than like straight up builder mode or eng manager mode, although I do all these different things. I'm constantly trying to find like what is the right positioning? Are we communicating in these meetings in a way that lands? And like it's so amazing to have A, this ability like for me who can't design or draw at all or like to have this now superpower, and we can go, let's see how this Figma is doing over here. Has it started to do it yet? Oh,

**Claire Vo** [00:39:21] it's starting.

**Zach Lloyd** [00:39:22] Oh, it's got some work to do, but it will do better. But yeah, if I was in sales mode, like I'm trying to figure out, are we positioning it right? What are people asking about? Yeah, and this is right, like this is from our actual sales calls, and like this is the, what I would say is the number one thing for the factory, like the product category we're in is like buy versus build, and it's backed up by evidence, and it makes sense to me. security comes up a lot. workflow, what's the workflow, what's the measurement, how do we manage costs? It's so cool. And so it's like what I would do is like, you know, I want to then go make sure that our sales deck, our website, all this stuff is speaking to the questions people have. I might turn this into like a literal FAQ. Like, I think we have, you know, probably ability to improve that, or I would just try and work this into our positioning, but I'm constantly doing this and trying to understand if what we're building is the right thing and we're positioning it the right way.

**Claire Vo** [00:40:26] Oh, you got a rocket ship. Sorry, we're back at Figma for those that are not watching. We got a rocket ship. We got a cloud of some sort. It's trying.

**Zach Lloyd** [00:40:36] It's not very good yet.

**Claire Vo** [00:40:37] It's trying its best.

**Zach Lloyd** [00:40:37] It will get better.

**Claire Vo** [00:40:38] The rocket ship's not terrible.

**Zach Lloyd** [00:40:40] No.

**Claire Vo** [00:40:41] It's not bad. Um, Zach, this is so fun. I want to go to quick lightning round questions, and then we'll get you back to

**Zach Lloyd** [00:40:50] Cool.

**Claire Vo** [00:40:50] back on the factory floor. All right, first lightning round question. Everybody wants the factory, everybody wants the go-to-market intern that will happily go through your call transcripts and the design intern that will happily make your ugly cloud slides as a CEO. But when you have the factory humming and when you're doing, I think it was like over 2,000 PRs in the last month, like, how do you keep things in the team from going, as I say, like chaos reigns? Like, how do you keep your arms around all that activity, all that work, all that context, all those tasks, and know at the highest level you're doing the things that matter?

**Zach Lloyd** [00:41:27] It's a great question. like the kind of boring answer is like a lot of the stuff that we've always done as software engineers still applies, which is like, you know, we're dogfooding. So we're just like huge constant users of the thing that we're building and making sure that like the quality of the thing still works well. there's like cool knowledge transfer that's happening, where it's, I don't know if you've seen this too, but like the, this, there's like a kind of power law for like how these tools are used in terms of like we have some people on our team who are super duper power users and other people are like kind of more at the average. And so there's this, when you're working in this, what seems like a very chaotic way in public with everyone slacking these factories all day, you do get a chance to sort of see how like the really expert people are using it, and that kind of up levels other people on the team. And then, like I said earlier, we're still doing, you know, it's not just like chaos, like everyone like, you know, slops stuff into the machine all the time.

[00:42:33] It's like we still have a product development process that, you know, is somewhat traditional in a bunch of ways. So it's like we do a whole bunch of user interviews, we watch people use the product, we do design jams before we start building to not so much like figure out exactly like how the UI should look, but just to make sure that we're tackling the right user stories. Like, because at the end of the day, like, it doesn't matter how fast you build software, it's like it still has to solve some user problem and solve it in a good way. And so we, we're trying to figure out how to like not lose the key parts of like the human input here, but also, you know, use the fact that there's this like magic technology to, that can make you just go much faster.

**Claire Vo** [00:43:19] I love it. I, amen. I could not say it better. okay, last question, and then we will get you out of here. When your AI is not doing what you want, and also I am curious if this question is, if you answer this question differently when you're working with AI privately versus working in with it in Slack. When it's not doing what you want, what's your prompting strategy? Do you yell? I am lately, I will admit this to the audience, I am doing a lot of, like, "Why are- why are you like this? Why? Why?" A lot of questioning.

**Zach Lloyd** [00:43:56] That's funny. Um, I'm, like, a pretty level guy. I'd like- if- I think if you ask the people on my team, I don't- I've never, like, the yelling not my style. Um, I get, like- passive aggressive is kind of what I would say. I- I get, like, eye-rolly, like, "Really? Like, this is what we're doing now? Like, you built this whole thing that no one asked you to build." So I'll get, like, annoyed, like, in, like, subtle undertones, but I- I'm not a- I'm not a yeller, and so, uh, I don't know, and I also try to just keep the perspective that this is just, like, a bonkers thing that I'm just, like, talking to this, uh- talking to this thing that is doing this job that I've done for the last 20 years, and it's now it's like doing it kind of better than me. And so, I don't know, I'm still in like, I'm in like a little bit of like a wonder phase with it. I don't know if you've ever seen that Louis CK skit where he talks about how when internet, like Wi-Fi first got onto airplanes, stop me if you know this, but it's like, he- it's a skit, he's like- he's riding on an airplane, it's like- it's like 20 years ago, and there's Wi-Fi for the first time, and he's just like, "This is incredible.

[00:45:14] Everyone- like, this is, like, amazing, and nobody's happy." And he tells a story about how, like, the guy next to him is, like, trying to watch a YouTube video and, like, throwing his hands up, like, "Screw this, like, I can't get any signal," and- and Louis CK's like, like, "This is bonkers, like, we're on an airplane. This thing is like going up to space, give it a second. And so I think it's so easy to lose perspective of like how wild this technology is. Like, I'm like, I'm generally like pretty, probably like kind of more patient with it than most, I would say.

**Claire Vo** [00:45:45] I love it. That's such a great perspective. Well, Zach, this has been super fun. Where can we find you, and how can we be helpful to you?

**Zach Lloyd** [00:45:52] So you can find me personally, like I'm on Twitter. I have Zach Lloyd Tweets is my Twitter. You should obviously come check out Warp at Warp.dev, if you want to build software factories. You know, I hardly even talked about it, but we have an extremely popular agentic terminal that's open source that you should also come check out and use. It's a great place to work with interactive coding agents. But yeah, this was awesome. I really appreciate you having me on.

**Claire Vo** [00:46:20] Yeah, thanks for joining How I AI. Thanks so much for watching. If you enjoyed the show, please like and subscribe here on YouTube, or even better, leave us a comment with your thoughts. You can also find this podcast on Apple Podcasts, Spotify, or your favorite podcast app. Please consider leaving us a rating and review, which will help others find the show. You can see all our episodes and learn more about the show at howiaipod.com. See you next time.
