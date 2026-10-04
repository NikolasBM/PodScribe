---
podcast: "latent-space"
podcast_title: "Latent Space"
title: "Extreme Harness Engineering for Token Billionaires: 1M LOC, 1B toks/day, 0% human code, 0% human review — Ryan Lopopolo, OpenAI Frontier & Symphony"
date: 2026-04-07
url: "https://www.latent.space/p/harness-eng"
guid: "substack:193478192"
host: "Swyx"
guests: ["Ryan Lopopolo", "swyx"]
format: "interview"
level: 2
length: "01:12:00"
categories: ["agents", "coding", "work", "models"]
featured: ["OpenAI Codex", "agent harness", "OpenAI"]
mentioned: ["Slack", "OpenClaw"]
transcript_source: "publisher"
---

# Extreme Harness Engineering for Token Billionaires: 1M LOC, 1B toks/day, 0% human code, 0% human review — Ryan Lopopolo, OpenAI Frontier & Symphony

**Ryan Lopopolo** [00:00:00] I do think that there is an interesting space to explore here with Codex, the harness, as part of building AI products, right? There’s a ton of momentum around getting the models to be good at coding. We’ve seen big leaps in like the task complexity with each incremental model release where if you can figure out how to collapse a product that you’re trying to.

[00:00:00] Build a user journey that you’re trying to solve into code. It’s pretty natural to use the Codex Harness to solve that problem for you. It’s done all the wiring and lets you just communicate in prompts. To let the model cook, you have to step back, right? Like you need to take a systems thinking mindset to things and constantly be asking, where is the Asian making mistakes?

[00:00:00] Where am I spending my time? How can I not spend that time going forward? And then build confidence in the automation that I’m putting in place. So I have solved this part of the SDLC.

**swyx** [00:00:00] All right.

## [00:01:03] Meet Ryan

**swyx** [00:01:00] We’re in the studio with Ryan from OpenAI. Welcome.

**Ryan Lopopolo** [00:01:00] Hi,

**swyx** [00:01:00] Thanks for visiting San Francisco and thanks for spending some time with us.

**Ryan Lopopolo** [00:01:00] Yeah, thank you. I’m super excited to be here.

**swyx** [00:01:00] You wrote a blockbuster article on harness engineering. It’s probably going to be the defining piece of this emerging discipline, huh?

**Ryan Lopopolo** [00:01:00] Thank you. It is it’s been fun to feel like we’ve defined the discourse in some sense.

**swyx** [00:01:00] Let’s contextualize a little bit, this first podcast you’ve ever done. Yes. And thank you for spending with us. What is, where is this coming from? What team are you in all that jazz?

**Ryan Lopopolo** [00:01:00] Sure, sure.

**Ryan Lopopolo** [00:01:00] I work on Frontier Product Exploration, new product development in the space of OpenAI Frontier, which is our enterprise platform for deploying agents safely at scale, with good governance in any business. And. The role of VMI team has been to figure out novel ways to deploy our models into package and products that we can sell as solutions to enterprises.

**swyx** [00:01:00] And you have a background, I’ll just squeeze it in there. Snowflake, brick, stripe, citadel.

**Ryan Lopopolo** [00:02:00] Yes. Yes. Same. Any kind of customer

**swyx** [00:02:00] entire life. Yes. The exact kind of customer that you want to,

**Vibhu** [00:02:00] so I’ll say, I was actually, I didn’t expect the background when I looked at your Twitter, I’m seeing the opposite.

[00:02:00] Stuff like this. So you’ve got the mindset of like full send AI, coding stuff about slop, like buckling in your laptop on your Waymo’s. Yes. And then I look at your profile, I’m like, oh, you’re just like, you’re in the other end too. Oh, perfect. Makes perfect.

**Ryan Lopopolo** [00:02:00] I it’s quite fun to be AI maximalist if you’re gonna live that persona.

[00:02:00] Open eye is the place to do it. And it’s

**swyx** [00:02:00] token is what you say.

**Ryan Lopopolo** [00:02:00] Yeah. Certainly helps that we have no rate limits internally. And I can go, like you said, full send at this stay.

**swyx** [00:02:00] Yeah. Yeah. So the Frontier, and you’re a special team within O Frontier.

**Ryan Lopopolo** [00:02:00] We had been given some space to cook, which has been super, super exciting.

## [00:02:47] Zero Code Experiment

**Ryan Lopopolo** [00:02:00] And this is why I started with kind of a out there constraint to not write any of the code myself. I was figuring if we’re trying to make agents that can be deployed into end to enterprises, they should be able to do all the things that I do. And having worked with these coding models, these coding harnesses over 6, 7, 8 months, I do feel like the models are there enough, the harnesses are there enough where they’re isomorphic to me in capability and the ability to do the job.

[00:03:00] So starting with this constraint of I can’t write the code meant that the only way I could do my job was to get the agent to do my job.

**Vibhu** [00:03:00] And like a, just a bit of background before that. This is basically the article. So what you guys did is five months of working on an internal tool, zero lines of code over a mi, a million lines of code in the total code base.

[00:03:00] You say it was cenex, more like it was cenex faster than you would’ve. If you had done it by end. So

**Ryan Lopopolo** [00:03:00] yeah, that

**Vibhu** [00:03:00] was the mindset going into this, right?

**Ryan Lopopolo** [00:03:00] That’s right.

## [00:03:46] Model Upgrades Lessons

**Ryan Lopopolo** [00:03:00] Started with some of the very first versions of Codex CLI, with the Codex Mini model, which was obviously much less capable than the ones we have today.

[00:03:00] Which was also a very good constraint, right? Quite a visceral feeling to ask the model to build you a product feature. And it just not being able to assemble the pieces together.

[00:04:00] Which kind of defined one of the mindsets we had for going into this, which is whenever the model just cannot, you always pop open at the task, double click into it, and build smaller building blocks that then you can reassemble into the broader objective.

[00:04:00] And it was quite painful to do this. Honestly, the first month and a half was. 10 times slower than I would be. But because we paid that cost, we ended up getting to something much more productive than any one engineer could be because we built the tools, the assembly station for the agent to do the whole thing.

## [00:04:43] Model Generations, Build Systems & Background Shells

**Ryan Lopopolo** [00:04:00] But yeah, so onward to G BT 5, 5, 1, 5, 2, 5, 3, 5 4. To go through all these model generations and see their kind of corks and different working styles also meant we had to adapt the code base to change things up when the model was revved. One interesting thing here is five two, the Codex harness at the time did not have background shells in it, which means we were able to rely on blocking scripts to perform long horizon work.

[00:05:00] But with five, three and background shells, it became less patient, less willing to block. So we had to retool the entire build system to complete in under a minute and. This is not a thing I would expect to be able to do in a code base where people have opinions. But because the only goal was to make the Asian productive over the course of a week, we went from a bespoke make file build to Basil, to turbo to nx and just left it there because builds were fast at that point.

**swyx** [00:05:00] Interesting. Talk more about Turbo TenX. That’s interesting ‘cause that’s the other direction that other people have been doing.

**Ryan Lopopolo** [00:05:00] Ultimately I have. Not a lot of experience with actual frontend repo architecture.

**swyx** [00:05:00] You’re talking that Jessica built the sky. So I’m like, I know the NX team. I know Turbo from Jared Palmer.

[00:06:00] And I’m like, yeah, that’s an interesting comparison.

## [00:06:02] One Minute Build Loop

**Ryan Lopopolo** [00:06:00] The hill we were climbing right, was make it fast.

**swyx** [00:06:00] Is there a micro front end involved? Is it how how complex react

**Ryan Lopopolo** [00:06:00] electron base single app sort of thing

**swyx** [00:06:00] And must be under a minute. That’s an interesting limitation. I’m actually not super familiar with the background shelf stuff.

[00:06:00] Probably was talked about in the fight three release.

**Ryan Lopopolo** [00:06:00] BA basically means that codex is able to spawn commands in the background and then go continue to work while it waits for them to finish. So it can spawn an expensive build and then continue reviewing the code, for example.

**swyx** [00:06:00] Yeah.

**Ryan Lopopolo** [00:06:00] And this helps it be more time efficient for the user invoking the harness.

**swyx** [00:06:00] And I guess and just to really nail this, like what does one minute matter? Like why not five, okay, good. We want no. We

**Ryan Lopopolo** [00:06:00] want the inner loop to be as fast as possible. Okay. One minute was just a nice round number and we were able to hit it.

**swyx** [00:06:00] And if it doesn’t complete, it kills it or some something,

**Ryan Lopopolo** [00:06:00] No.

[00:06:00] We just take that as a signal that we need to stop what we’re doing, double click, decompose a build graph a bit to get us to high back under so that we can able the agent continue to operate.

**swyx** [00:07:00] It’s almost like you’re, it’s like a ratchet. It’s like you’re forcing build time discipline, because if you don’t, it’ll just grow and grow.

[00:07:00] That’s right. And you mentioned that my current, like the software I work on currently is at 12 minutes. It sucks.

**Ryan Lopopolo** [00:07:00] This has been my experience with platform teams in the past, where you have an envelope of acceptable build times and you let it go up to breach and then you spend two, three weeks to bring it back down to the lower end of the average low bed stop.

[00:07:00] But because tokens are so cheap Yeah. And we’re so insanely parallel with the model, we can just constantly be gardening this thing to make sure that we maintain these in variants, which means. There’s way less dispersion in the code and the SDLC, which means we can simplify in a way and rely on a lot more in variance as we write the software.

## [00:07:45] Observability, Traces & Local Dev Stack

**Vibhu** [00:07:00] Lovely.

## [00:07:46] Humans Are Bottleneck

**Vibhu** [00:07:00] You mentioned in your article, like humans became the bottleneck, right? You kicked off as a team of three people. You’re putting out a million line of code, like 1500 prs, basically. What’s the mindset there? So as much as code is disposable, you’re doing a lot of review. A lot of the article talks about how you wanna rephrase everything is prompting everything, is what the agent can’t see.

[00:08:00] It’s kind of garbage, right? You shouldn’t have it in there. So what’s like the high level of how you went about building it, and then how you address okay, humans are just PR review. Like how is human in the loop for this?

**Ryan Lopopolo** [00:08:00] We’ve moved beyond even the humans reviewing the code as well.

## [00:08:19] Human Review, PR Automation & Agent Code Review

**Ryan Lopopolo** [00:08:00] Most of the human review is post merge at this point.

[00:08:00] But post, post merge, that’s not even reviewed. That’s just

**swyx** [00:08:00] Oh, let’s just make ourselves happy by You

**Ryan Lopopolo** [00:08:00] haven’t used fundamentally. The model is trivially paralyzable, right? As many GPUs and tokens as I am willing to spend, I can have capacity to work with my hood base.

[00:08:00] The only fundamentally scarce thing is the synchronous human attention of my team. There’s only so many hours in the day we have to eat lunch. I would like to sleep, although it’s quite difficult to, stop poking the machine because it makes me want to feed it. You have to step back, right?

[00:08:00] Like you need to take a systems thinking mindset to things and constantly be asking where is the agent making mistakes? Where am I spending my time? How can I not spend that time going forward? And then build confidence in the automation that I’m putting in place. So I have solved this part of the SDLC, and usually what that has looked like is like we started needing to pay very close attention to the code because the agent did not have the right building blocks to produce.

[00:09:00] Modular software that decomposed appropriately that was reliable and observable and actually accrued a working front end in these things, right?

## [00:09:35] Observability First Setup

**Ryan Lopopolo** [00:09:00] So in order to not spend all of our time sitting in front of a terminal at most, doing one or two things at a time, invested in giving the model that observability, which is that that graph in the post here.

**swyx** [00:09:00] Yeah. Let’s walk through this traces and which existed first

**Ryan Lopopolo** [00:09:00] we started with just the app and the whole rest of it. From vector through to all these login metrics, APIs was, I dunno, half an afternoon of my time. We have intentionally chosen very high level fast developer tools. There’s a ton of great stuff out there now.

[00:10:00] We use me a bunch, which makes it trivial to pull down all these go written Victoria Stack binaries in our local development. Tiny little bit of python glue to spin all these up. And off you go. One neat thing here is we have tried to invert things as much as possible, which is instead of setting up an environment to spawn the coding agent into, instead we spawn the coding agent, like that’s the entry point.

[00:10:00] It’s just Codex. And then we give Codex via skills and scripts the ability to boot the stack if it chooses to, and then tell it how to set some end variables. So the app and local Devrel points at this stack that it has chosen to spin up. And this I think is like the fundamental difference between reasoning models and the four ones and four ohs of the past, where these models could not think so you had to put them in boxes with a predefined set of state transitions.

[00:11:00] Whereas here we have the model, the harness be the whole box. And give it a bunch of options for how to proceed with enough context for it to make intelligent choices. So

**Vibhu** [00:11:00] sales, so like a lot of that is around scaffolding, right? Yes. Previous agents, you would define a scaffold. It would operate in that.

[00:11:00] Lube, try again. That’s pivoted off from when we’ve had reasoning models. They’re seeming to perform better when you don’t have a scaffold, right? That’s right.

## [00:11:28] Docs Skills Guardrails

**Vibhu** [00:11:00] And you go into like niches here too, like your SPEC MD and like having a very short agent MG Agent md.

**swyx** [00:11:00] Yes. Yes.

**Vibhu** [00:11:00] Yeah. So you even lay out what it is here, but I like

**swyx** [00:11:00] the table contents.

**Vibhu** [00:11:00] Yeah.

**swyx** [00:11:00] Like stuff like this, it really helps guide people because everyone’s trying to do this.

**Ryan Lopopolo** [00:11:00] This structure also makes it super cheap to put new content into the repository to steer both the humans and the agents.

**swyx** [00:11:00] You, you reinvented skills, right?

**Vibhu** [00:11:00] One big agents and

**swyx** [00:11:00] skills from first princip holds

**Ryan Lopopolo** [00:11:00] all skills did not exist when we started doing this.

**Vibhu** [00:11:00] You have a short one 100 line overall table of contents and then you have little skills, right? Core beliefs, MD tech tracker. Yeah. Yeah. The scale is over

**Ryan Lopopolo** [00:12:00] The tech jet tracker and the quality score are pretty interesting because this is basically a tiny little scaffold, like a markdown table, which is a hook for Codex to review all the business logic that we have defined in the app, assess how it matches all these documented guardrails and propose follow up work for itself.

[00:12:00] Before beads and all these ticketing systems, we were just tracking follow up work as notes in a markdown file, which, we could spa an agent on Aron to burn down. There’s this really neat thing that like the models fundamentally crave text. So a lot of what we have done here is figure out ways to inject text

**swyx** [00:12:00] into

**Ryan Lopopolo** [00:12:00] the system right when we get a page, because we’re missing a timeout, for example.

[00:12:00] I can just add Codex in Slack on that page and say, I’m gonna fix this by adding a timeout. Please update our reliability documentation. To require that all network calls have timeouts. So I have not only made a point in time fix, but also like durably encoded this process knowledge around what good looks like.

**swyx** [00:13:00] Yeah.

**Ryan Lopopolo** [00:13:00] And we give that to the root coding agent as it goes and does the thing. But you can also use that to distill tests out of, or a code review agent, which is pointed at the same things to narrow the acceptable universe of the code that’s produced.

**swyx** [00:13:00] I think one of the concerns I have with that kind of stuff is you think you’re making the right call by making, it’s persisted for all time across everything.

[00:13:00] Yes. But then you didn’t think about the exceptions that you need to make, right? And that you have to roll it back.

**Vibhu** [00:13:00] Part of it is

**swyx** [00:13:00] also sometimes it can follow your s instructions too.

**Vibhu** [00:13:00] It’s somewhat a skill, right? So it determines when it uses the tools, right? Like it’s not like it’ll run outta every call.

[00:13:00] It’ll determine when it wants to check quality score, right?

**Ryan Lopopolo** [00:13:00] Yeah. And we do in the prompts we give these agents, allow them to push back,

## [00:13:51] Agent Code Review Rules

**Ryan Lopopolo** [00:13:00] When we first started adding code review agents to the pr, it would be Codex, CLI. Locally writes the change, pushes up a PR on those PR synchronizations of review agent fires.

[00:14:00] It posts a comment. We instruct Codex that it has to at least acknowledge and respond to that feedback. And initially the Codex driving the code author was willing to be bullied by the PR reviewer, which meant you could end up in a situation where things were not converging. So yeah, we had to,

**swyx** [00:14:00] he’s just a thrash.

**Ryan Lopopolo** [00:14:00] We had to add more optionality to the prompts on both of these things, right? The reviewer agents were instructed to bias toward merging the thing to not surface anything greater than a P two in priority. We didn’t really define P two, but we gave it, you

**swyx** [00:14:00] did define P two.

**Ryan Lopopolo** [00:14:00] We gave it a framework within which to score its output

**swyx** [00:14:00] and then greater than P zero is worse, right?

[00:14:00] Yes. P two is very good.

**Ryan Lopopolo** [00:14:00] P zero is you will mute the code place if

**swyx** [00:14:00] you merch this

**Ryan Lopopolo** [00:14:00] thing, right?

**swyx** [00:14:00] Yeah.

**Ryan Lopopolo** [00:14:00] But also on the code authoring agent side, we also gave it the flexibility to either defer or push back against review feedback, right? This happens all the time, right? Like I happen to notice something and leave a code review, which.

[00:15:00] Could blow up the scope by a factor of two. I usually don’t mean for that to be addressed Exactly. In the moment. It’s more of an FYI file it to the backlog, pick it up in the next fix it week sort of thing. And without the context that this is permissible, the coding agents are gonna bias toward what they do, which is following instructions.

**swyx** [00:15:00] Yeah.

## [00:15:19] Autonomous Merging Flow

**swyx** [00:15:00] I do wanted to check in on a couple things, right? Sure. All the coding review agent, it can merge autonomously. I think that’s something that a lot of people aren’t comfortable with. And you have a list here of how much agents do they do Product code and tests, CI configuration and release tooling, internal Devrel tools, documentation eval, harness review, comments, scripts that manage the repository itself, production dashboard definition files, like everything.

[00:15:00] Yes. And so they’re just all churning at the same time, is there like a record that, that any human on the team pulls to stop everything

**Ryan Lopopolo** [00:15:00] Because we are building a native application here. We’re not doing continuous deploy. So there’s still a human in the loop for cutting the release branch.

[00:15:00] I see. We require a blessed human approved smoke test of the app before we promote it to distribution, these sort of things.

**swyx** [00:16:00] So you’re working on the app, you’re not building like infrastructure where you have like nines of reliability, that kinda stuff?

**Ryan Lopopolo** [00:16:00] That’s correct. That’s correct. Okay. And also like full recognition here that all of this activity took in a completely greenfield repository.

[00:16:00] There’s. Should be no script that this applies generally to

**swyx** [00:16:00] this is a production thing, you’re gonna ship

**Ryan Lopopolo** [00:16:00] to

**swyx** [00:16:00] customers. Of course. Yeah, of course. So this is real

**Vibhu** [00:16:00] And like one of the things there is, you mentioned you started this as a repo from scratch. The onboarding first month or so was pretty, it was like working backwards, right?

[00:16:00] Yeah. And then you had to work with the system and now you’re at that point where you know, you’re very autonomous. I’m curious like, okay, so what, how human in the loop is it? So what are the bottlenecks that you wish you could still automate? And part of that is also like, where do you see the model trajectory improving and offloading more human in the loop?

[00:16:00] We just got 5.4. It’s a really good,

**Ryan Lopopolo** [00:16:00] fantastic model, by the way.

**Vibhu** [00:16:00] Yeah. Yeah. It’s the first one that’s merged. Top tier coding. So it’s codex level coding and reasoning. So general reasoning both in one model. So

**Ryan Lopopolo** [00:16:00] and

**Vibhu** [00:16:00] computer use vision.

**Ryan Lopopolo** [00:17:00] Now we now with five four, I can just have Codex write the blog post, whereas for this one I had to balance between chat.

**swyx** [00:17:00] Oh, I need to, I might be out of a job. Oh my God.

**Ryan Lopopolo** [00:17:00] Oh,

**swyx** [00:17:00] I know. You just gave me an idea for a completely AI newsletter that five four could do. Yeah, I get it Now.

**Ryan Lopopolo** [00:17:00] This sort of thing is just one example of closing the loop, right? Like the dashboard thing you mentioned. We have Codex authoring the Js ON, for the Grafana dashboards and publishing them and also responding to the pages, which means when it gets the page, it knows exactly which dashboards are defined and what alerts.

[00:17:00] What alert was triggered by which exact log in the code base. ‘cause all of this stuff is collated together.

**swyx** [00:17:00] It has to own everything.

[00:17:00] Yes. Yeah. Yeah.

**Ryan Lopopolo** [00:17:00] And it means that if we have an outage that did not result in a page. It has the existing set of dashboards available to it. It has the existing set of metrics and logs and can figure out where the gaps in the dashboard are or in the underlying metrics and fix them in one go.

[00:18:00] In the same way, you would have a full stack engineer be able to drive a feature from the backend all the way to the front end.

**Vibhu** [00:18:00] So it, it seems like a lot of the work you guys had to do was you as a small team are fully working for a way that the model wants the software to be written. It’s like less human legible for better. Code legibility, agent legibility. How do you think that affects broader teams? So one at OpenAI, do liaison, like this is how software should be written. Like I can imagine, say you join a new team with this methodology, this mindset there’s ways that, teams do code review, teams write code, like teams are structured and a lot of it is for human legibility.

[00:18:00] So should we all swap? Like how does this play back one broader into OpenAI and then like broader into the software engineering, right? Is it like teams that pick this up will it’s pretty drastic, right? You have to make a pretty big switch. Should they just full send Yeah.

**Ryan Lopopolo** [00:18:00] The mindset is very much that I’m removed from the process, right? I can’t really have deep code level opinions about things. It’s as if I’m. Group tech leading a 500 person organization.

**Vibhu** [00:19:00] Yeah.

**Ryan Lopopolo** [00:19:00] Like it’s not appropriate for me to be in the weeds on every pr. This is why that post merge code review thing is like a good analog here, right?

[00:19:00] Like I have some representative sample of the code as it is written, and I have to use that to infer what the teams are struggling with, where they could use help, where they’re already moving quickly and I can pivot my focus elsewhere.

**Vibhu** [00:19:00] Yeah.

**Ryan Lopopolo** [00:19:00] So I don’t really have too many opinions around the code as it is written.

[00:19:00] I do, however, have a command based class, which is used to have repeatable chunks of business logic that comes with tracing and metrics and observability for free. And the thing to focus on is not how that business logic is structured, but that it uses this primitive ‘cause I know that’s gonna give leverage by default.

**Vibhu** [00:19:00] Yeah.

**Ryan Lopopolo** [00:19:00] Yeah, back to that sort of systems stinking,

**Vibhu** [00:19:00] and you have part of that in your blog post, enforcing architecture and ta taste how you set boundaries for what’s used. There’s also a section on redefining engineering and stuff, but yeah, it’s just, it’s interesting to hear,

**Ryan Lopopolo** [00:20:00] and as the models have gotten better, they have gotten better at proposing these abstractions to unblock themselves, which again, lets me move higher and higher up the stack to look deeper into the future on what ultimately blocked the team from shipping.

**swyx** [00:20:00] Yeah. You mentioned so you, this is primarily a, it is like a 1 million line of code base electron app. But it manages its own services as well, so it’s like a backend for front end type thing.

**Ryan Lopopolo** [00:20:00] We do have a backend in there, but that’s hosted in the cloud.

[00:20:00] Yeah. This sort of structure is actually within the separate main and render processes

[00:20:00] Within the

**swyx** [00:20:00] electric.

[00:20:00] That’s just how electronic works.

**Ryan Lopopolo** [00:20:00] Yeah, of course. So have also treated like. MVC style decomposition with the same level of rigor, which has been very fun.

**swyx** [00:20:00] I have a fun pun. This is a tangent, NVC is model view controller. Any sort of full stack web Devrel knows that.

[00:20:00] But my AI native version of this is Model view Claw, the clause the harness.

**Ryan Lopopolo** [00:20:00] That’s right. That’s right. I do think that there is an interesting space to explore here with Codex, the harness as part of building AI products, right? There’s a ton of momentum around getting the models to be good at coding.

[00:21:00] We’ve seen big leaps in like the task complexity with each incremental model release where if you can figure out how to collapse a product that you’re trying to build, a user journey that you’re trying to solve into code, it’s pretty natural to use the Codex Harness to solve that problem for you. It’s done all the wiring and lets you just communicate and prompts to let the model cook.

[00:21:00] Yeah. It’s been very fun. And there’s also a very engineering legible way of increasing capabil. It’s fantastic, right? Yeah. Just give you, just give the model scripts, the same scripts you would already build for yourself.

**swyx** [00:21:00] Yeah.

[00:21:00] Yeah. So for listeners, this is Ryan saying that software engineering or coding against will eat knowledge work like the non-coding parts that you would normally think.

[00:21:00] Oh, you have to build a separate agent for it. No, start a coding agent and go out from there. Which open Claw has like it’s pie Underhood.

**Ryan Lopopolo** [00:21:00] Yes.

**Vibhu** [00:22:00] Basically define your task in code. Everything is a coding

**swyx** [00:22:00] agent by the way. Since I brought it up, it’s probably the only place we bring it up. Is any open claw usage from you?

[00:22:00] Any?

**Ryan Lopopolo** [00:22:00] No. No. Not for me. I don’t have any spare Mac Minis rattling around my house.

**swyx** [00:22:00] You can afford it? No. I just, I’m curious if it’s changed anything in opening eye yet, but it’s probably early days. And then the other, the other thing I, I wanna pull on here is like you mentioned ticketing systems and you mentioned prs and I’m wondering if both those things have to go away or be reinvented for this kind of coding.

[00:22:00] So the git itself and is like very hostile to multi-agent.

**Ryan Lopopolo** [00:22:00] Yeah. We make very heavy use of work trees.

**swyx** [00:22:00] But like even then, like I just did a, dropped a podcast yesterday with Cursors saying, and they said they’re getting rid of work trees ‘cause it still has too many merge conflicts.

[00:22:00] It’s still un too un unintuitive. But go ahead.

**Ryan Lopopolo** [00:22:00] The models are really great at resolving merge conflicts. Yeah. And to get to a state where I’m not synchronously in the loop in my terminal, I almost don’t care that there are merge

**swyx** [00:22:00] with disposable.

[00:22:00] Yeah.

**Ryan Lopopolo** [00:23:00] We invoke a dollar land skill and that coaches codex to push the PR Wait for human and agent reviewers Wait for CI to be green.

[00:23:00] Fix the flakes if there are any merged upstream. If the PR comes into conflict, wait for everything to pass. Put it in the merge queue. Deal with flakes until it’s in Maine. End. This is what it means to delegate fully, right? This is in a, very large model re probably a significant tax on humans to get PRS merged, but the agent is more than capable of doing this and I really don’t have to think about it other than keep my laptop open.

**swyx** [00:23:00] Yeah. I used to be much more of a control freak, but now I’m like, yeah, actually you could do a better job of this than me. Yeah. With the right context. Yes.

## [00:23:47] Encoding Requirements

**swyx** [00:23:00] Anything else in harness in general? Just this piece, I just wanna make sure we,

**Ryan Lopopolo** [00:23:00] I think one thing that I maybe didn’t make super clear in the article that I heard on Twitter as an interesting, that’s respond

**swyx** [00:24:00] to them.

[00:24:00] What’s the chatter and then what’s your response?

**Ryan Lopopolo** [00:24:00] Ultimately, all the things that we have encoded in docs and tests and review agents and all these things are ways to put all the non-functional requirements of building high scale, high quality, reliable software into a space that prompt injects the agent.

[00:24:00] We either write it down as docs, we add links where the error messages tell how to do the right thing. So the whole meta of the thing is to basically tease out of the heads of all the engineers on my team, what they think good looks like, what they would do by default, or what they would coach a new hire on the team to do to get things to merch.

[00:24:00] And that’s why we pay attention to all the mistakes, mistakes that the agent makes, right? This is code being written that is misaligned with some as yet not written down, non-functional requirement.

**swyx** [00:24:00] Sorry, what? Did the online people misunderstand or

**Ryan Lopopolo** [00:24:00] No,

**swyx** [00:24:00] what

[00:24:00] you

**Ryan Lopopolo** [00:24:00] responded to? Somebody just literally said that.

[00:24:00] I was like, oh yeah,

**swyx** [00:24:00] okay,

**Ryan Lopopolo** [00:24:00] This is the thing. This is what I’ve been doing. Oh, you

**swyx** [00:25:00] agree? Yeah. I see. Interesting.

**Ryan Lopopolo** [00:25:00] One other neat thing, which I did totally did not expect is folks were just. Taking the link to the article and giving it to pi or Codex and say, make my repo this,

**Vibhu** [00:25:00] you achi a whole recursion.

**Ryan Lopopolo** [00:25:00] And it was wildly effective. Really? It was wildly effective. No

**Vibhu** [00:25:00] way. It just actually is something I tried with five, four yesterday. I didn’t have time. Last time I was like out speaking of something, and this is one of my things, I was like, okay, I have this article. Can we just scaffold out what it would be like to run this?

[00:25:00] And I, I did it first as that and then I was like, okay, let me take another little side repo and say okay, if I was to fully automate this like this because I haven’t written a line of code, it’s

**Ryan Lopopolo** [00:25:00] like over full, set

**Vibhu** [00:25:00] it right. The side thing I’m doing of voice. TTS I’m just like, slobbing out, whatever.

[00:25:00] It’s nothing production. I’m like, how would I make this like this? And it’s actually like a really good way. It’s like a good way to learn what could be changed, what could be like, it’s just a good analyzing, right? You give it all the codes, you give it all the context, you give it the article and it walks you through it very well.

[00:25:00] That’s right. That’s right.

## [00:25:57] Inlining Dependencies

## [00:25:57] Dependencies Going Away & Brett Taylor’s Response

**swyx** [00:25:00] I guess one more thing before we go to Symphony is I wanted to cover Brett Taylor’s response. We had him on the show. He is your chairman, which is wild. Yeah. That he’s reading your articles as well and like getting engaged in it. He says software dependencies are going away.

[00:26:00] Basically they can just be like vendored. Yes. Response.

**Ryan Lopopolo** [00:26:00] A

**swyx** [00:26:00] hundred percent. A hundred percent agree. You still pro qr, you still pay Datadog. You still pay Temporal. Thank you.

**Ryan Lopopolo** [00:26:00] Yep. The level of complexity of the dependencies that we can internalize is, I would say low, medium right now. Just based on model capability.

[00:26:00] What does the,

**swyx** [00:26:00] what is medium?

**Ryan Lopopolo** [00:26:00] I would say like a. A couple thousand line dependency is a thing that we could in-house No problem. Call in an afternoon of time. One neat thing about it is like probably most of that code you don’t even need. Like by in-house and abstraction, you can strip away all the generic parts of it and only focus on what you need to enable the specific thing.

[00:26:00] Yes. You’re building,

**swyx** [00:26:00] I’ve been calling this the end of bullshit plugins.

**Ryan Lopopolo** [00:26:00] Yeah.

**swyx** [00:26:00] Because there’s so much when I published an open source thing, I want to accept everything, be liberal. I want to accept, this is post’s law, but that means there’s so much bloat. Yes. There’s so much overhead.

**Ryan Lopopolo** [00:26:00] One other neat thing about this too is when we deploy Codex Security on the repo, it is able to deeply review and change. The internalized dependencies in a much lower friction way than it would be to like, push patches upstream, wait for them to be released, pull them down, make sure that’s compatible with all the transitive I have in my repo and things like that.

[00:27:00] So it’s also much lower friction to internalize some of these things if code is free. ‘cause the tokens are cheap sort of thing.

**swyx** [00:27:00] Yeah. Yeah. I think like the only argument I have against this is basically scale testing, which obviously the larger pieces of software like Linux, MySQL, he calls up even the Datadog and Temporals and then maybe security testing where Yes.

[00:27:00] Classically, I think, is it linis tos, it said security open source is the best disinfectant.

**Ryan Lopopolo** [00:27:00] Many eyes.

**swyx** [00:27:00] Many eyes. And if inline your dependencies and code them up, you’re gonna have to relearn mistakes from other people that Yep.

**Ryan Lopopolo** [00:27:00] Yep. And to internalize that dependency, you’re back to zero and you have to start.

[00:27:00] Reassembling all those bits and pieces to Yeah. Have high confidence in the code as it is written. Yeah.

**Vibhu** [00:28:00] Even part of the first intro of this, you basically mentioned like everything was written by codex, including internal tooling, right? So internal tooling, like when you’re visualizing what’s going on it’s writing it for itself.

**swyx** [00:28:00] Yeah. I’m built internal tools way I now, and like I just show them off and they’re like, how long did you spend? And I didn’t spend any time. I just prompted it,

**Ryan Lopopolo** [00:28:00] very funny story here.

**swyx** [00:28:00] Yeah, go ahead.

**Ryan Lopopolo** [00:28:00] We had deployed our app to the first dozen users internally had some performance issues, so we asked them to export a trace for us get a tar ball, gave it to our on-call engineer, and he did a fantastic job of working with Codex to build this beautiful local Devrel tool, next JS app, the drag and drop the tar ball in, and it visualizes the entire trace.

[00:28:00] It’s fantastic. Took an afternoon, but none of this was necessary. Because you could just spin up codex and give it the tar ball and ask the same thing and get the response immediately. So in a way, optimizing for human legibility of that debugging process was wrong. It kept him in the loop unnecessarily when instead he could have just like Codex cooked for five minutes and gotten this same.

**swyx** [00:29:00] Yeah, you verify your instincts here of this is how we used to do it. Or this is how I would have used to solve it.

**Ryan Lopopolo** [00:29:00] Yeah. In this local observability stack. Like sure, you can de deploy Yeager to visualize the traces, but I wouldn’t expect to be looking at the traces in the first place because I’m not gonna write the code to fix them.

**swyx** [00:29:00] Yeah. So basically there needs to be like this kind of house stack and owning the whole loop. I think that is very well established. And it sounds like you might be like sharing more about that in the future, right?

**Ryan Lopopolo** [00:29:00] Yeah. I think we’re excited to do

## [00:29:36] Ghost Libraries Specs

## [00:29:36] Ghost Libraries & Distributing Software as Specs

**Ryan Lopopolo** [00:29:00] We’re gonna talk about Symphony in a little bit, but like the way we distribute it as a spec, which I think folks are calling Ghost Libraries on Twitter.

[00:29:00] This is like a such a cool name. It does mean it becomes much cheaper to share software with the world, right? You define a spec, how you could build your own specifying as much as is required for a coding agent to reassemble it locally. The flow here is very cool. Like we have taken. All the scaffolding that has existed in our proprietary repo spun up a new one.

[00:30:00] Ask Codex with our repo as a reference. Write the spec. We tell it. Spin up a team ox spawn a disconnected codex to implement the spec. Wait for it to be done. Spawn another codex and another team ox to review the spec com or review the implementation compared to upstream and update the spec so it diverges less.

[00:30:00] And then you just loop over and over Ralph style until you get a spec that is with high fidelity able to reproduce the system as it is. It’s fantastic.

**Vibhu** [00:30:00] And you’re basically, you’re not really adding any of your human bias in there, right? That’s correct. A lot of times people write a spec and be like, okay, I think it should be done this way, and you’ll riff on something.

[00:30:00] And it’s no, the agent could have just handled it like you’re still scaffolding in a sense, right? I want it done this way. It can determine its spec better.

**swyx** [00:30:00] That’s right. That’s right. Part of me it, I’m, I’ve been working a lot on evals recently, and part of me is wondering if an agent can produce a spec that it cannot solve.

[00:31:00] Is it always capable of things that he can imagine or can you imagine things that it is impossible to do?

**Ryan Lopopolo** [00:31:00] I think with Symphony, we, there’s like this there’s this axis where you have things that are easier, hard, or established or new, right? And I think things that are hard and new is still something that the models need humans.

[00:31:00] Yeah. Drive.

**swyx** [00:31:00] Yeah. Yeah.

**Ryan Lopopolo** [00:31:00] But I think those other quadrants are largely salt. Given the right scaffold and the right thing that’s gonna drive the agent to completion,

**swyx** [00:31:00] it’s crazy that it solved,

**Ryan Lopopolo** [00:31:00] but it means that the humans, the ones with limited time and attention get to work on the hardest stuff, like the problems where it’s pure white space out in front. Or like the deepest refactorings where you don’t know what the proper shape of the interfaces are. And this is where I wanna spend my time. ‘cause it lets me set up for the next level of scale.

**swyx** [00:31:00] Yeah. Yeah. Amazing. Let’s introduce Symphony.

[00:31:00] I think we’ve been mentioning it every now and then. Elixir. Interesting option.

**Ryan Lopopolo** [00:31:00] Yeah.

**swyx** [00:31:00] Yeah. I’m not,

**Ryan Lopopolo** [00:31:00] again, like the elixir manifestation here is just a derivative. Is it a model

**swyx** [00:32:00] chosen? Yeah.

**Ryan Lopopolo** [00:32:00] Yeah. Yeah. And it chose that because the process supervision and the gen servers are super amenable to the type of process orchestration that we’re doing here.

[00:32:00] You are essentially spinning up little Damons for every task that is in execution and driving it to completion, which. Means the mall gets a ton of stuff for free by using Elixir and the Beam.

**swyx** [00:32:00] I had to go do a crash course in Beam and Elixir, and I think most people are not operating at that scale of concurrency where you need that.

[00:32:00] But it is a good mental model for Resum ability and all those things. And these are things I care about. But tell me the story, the origin story of Symphony. What do you use it for? Is this, how did it form maybe any abandoned paths that you didn’t take?

## [00:32:46] Terminal Free Orchestration

## [00:32:46] Symphony: Removing Humans from the Loop

**Ryan Lopopolo** [00:32:00] At the end of December we were at about three and a half PRS per engineer per day.

[00:32:00] This was before five two came out in the beginning of January. Everyone gets back from holiday with five two and no other work on the repository. We were up in the five to 10 PRS per day per engineer. And I don’t know about y’all, but like it’s very taxing to constantly be switching like that. Like I was pretty tapped out at the end of the day, again, where are the humans spending their time? They’re spending their time context switching between all these active tmox pains to drive the agent forward.

**swyx** [00:33:00] Yeah. No way. Yeah.

**Ryan Lopopolo** [00:33:00] So let’s again, build something to remove ourselves from the loop. And this is what frantic sprinted adapt here to find a way to remove the need for the human to sit in front of their terminal.

[00:33:00] So a lot of experimentation with Devrel boxes and, automatically spinning up agents, like it seems like a fantastic end state here, where my life is beach. I open live twice a day and say yes no to these things. Yeah. And this is again, a super, super interesting framing for how the work is done.

[00:33:00] Because I become more latency and sensitive. I have way less attachment to the code as it is written. Like I’ve had close to zero investment in the actual authorship experience. So if it’s garbage. I can just throw it away and not care too much about it. In Symphony, there’s this like rework state where once the PR is proposed and it’s escalated to the human for review, it should be a cheap review.

[00:34:00] It is either mergeable or it is not. And if it’s not, you move it to rework. The elixir service will completely trash the entire work tree NPR and start it again from scratch. Okay. And this is that opportunity again to say, why was it trash right? What did the agent do that was

**swyx** [00:34:00] bad. Yeah.

**Ryan Lopopolo** [00:34:00] Fix that before moving the ticket to

**swyx** [00:34:00] end

**Ryan Lopopolo** [00:34:00] of progress again.

**swyx** [00:34:00] Yeah. Why is this not in codex app? I guess this, you guys are ahead of Codex app,

**Ryan Lopopolo** [00:34:00] yeah, so the way the team has been working is basically to be as AI pilled as possible and spread ahead. And a lot of the things we have worked on have fallen out into a lot of the products that we have.

[00:35:00] Like we were in deep consultation with the Codex team to. Have the Codex app be a thing that exists, right? To have skills be a thing that Codex is able to use. So we didn’t have to roll our own to put automations into the product. So all of our automatic refactoring agents didn’t have to be these hand rolled control loops.

[00:35:00] It has been really fantastic to be, in a way, un anchored to the product development of Frontier and Codex and just very quickly try to figure out what works and then later find the scalable thing that can be deployed widely. It’s been a very fun way to operate. It’s certainly chaotic. I have lost track very often of what the actual state of the code looks like.

[00:35:00] ‘cause I’m not in the loop. There was. One point where we had wired playwright directly up to the Electron app. With MCPM CCPs, I’m pretty bearish on because the harness forcibly injects all those tokens in the context, and I don’t really get a say over it. They mess with auto compaction. The agent can forget how to use the tool.

[00:36:00] There’s probably only what three calls in playwright that I actually ever want to use. So I pay the cost for a ton of things. Somebody vibed a local Damon that boots playwright and exposes a tiny little shim CLI to drive it. And I had zero idea that this had occurred because to me, I run Codex and it’s able to, it’s oh, it’s better.

[00:36:00] Yeah. Like no knowledge of this at all. Uhhuh.

## [00:36:30] Multi Human Chaos

**Ryan Lopopolo** [00:36:00] So we have had like in human space to spend a lot of time doing synchronous knowledge sharing. We have a daily standup that’s 45 minutes long because we almost have to. Fan out the understanding of the current state.

**swyx** [00:36:00] Yeah, I was gonna say this is good for a single human multi-agent, but multi human, multi-agent is a whole like po like explosion of stuff.

**Ryan Lopopolo** [00:36:00] Yeah. And that this is fundamentally why we have such a rigid, like 10,000 engineer level architecture in the app because we have to find ways to carve up the space so people are not trampling on each other.

**swyx** [00:37:00] Sorry, I don’t get the 10,000 thing. Did I miss that?

**Ryan Lopopolo** [00:37:00] The structure of the repository is like 500 NPM packages.

[00:37:00] It’s like architecture to the excess for what you would consider, I think normal for a seven person team. But if every person is actually like 10 to 50. Then the like numbers on being super, super deep into decomposition and sharding and like proper interface boundaries make a lot more sense.

**swyx** [00:37:00] Yeah. To me, that’s why I talked about Microfund ends and I, an anex is from that world, but Cool. It is just coming back to, to, to this I dunno if you have other, thoughts on. Orchestrating so much work coin going through this. Is this enough? Is this like any aha moments?

**Vibhu** [00:37:00] It’ll be interesting to see like where, okay, so right now you pick linear as your issue tracker, right?

**swyx** [00:37:00] Or it’s like a is it actually linear? This is actually linear.

## [00:37:55] Linear vs Slack Workflow

**Vibhu** [00:37:00] Oh, that’s linear. It’s linear.

**swyx** [00:37:00] Oh I never looked at

**Vibhu** [00:37:00] video. The demo video I had to download to run.

**swyx** [00:38:00] So I, because I’m a Slack maxie, but Yeah, linear. Linear is also really good. Yes,

**Ryan Lopopolo** [00:38:00] we do make a good use of Slack. We we fire off codex to do all these lotion, elasticity, fix ups, the things that like sync that knowledge into the repository.

[00:38:00] It’s super cheap. Yeah.

**swyx** [00:38:00] Yeah.

**Ryan Lopopolo** [00:38:00] Just do it in Codex.

**swyx** [00:38:00] My biggest plug is OpenAI needs to build Slack. You need to own Slack. Build yours. Turn this into Slack.

**Ryan Lopopolo** [00:38:00] I did read about it. You

**swyx** [00:38:00] did?

**Ryan Lopopolo** [00:38:00] Yeah.

## [00:38:25] Collaboration Tools for Agents

**Ryan Lopopolo** [00:38:00] I would say that if we think that we want these agents to do economically valuable work, which is like this is the mission, right?

[00:38:00] We want AI to be deployed widely, to do economically valuable work, then we need to find ways for them to naturally collaborate with humans, which means collaboration tooling, I think, is an interesting space to explore.

**swyx** [00:38:00] Yeah, totally. Yeah. GitHub, slack, linear.

**Vibhu** [00:38:00] Yeah, that was my thing. Okay, where do we see right now Codex has started Codex Model, then CLI, now there’s an app, app can let me shoot off multiple Codex is in parallel, but there’s no great team collaboration for Codex.

[00:38:00] And it seems like your team had some say into what comes out, right? So you talked to ‘em, codex kind of was a thing. From there, if you guys are on the bound, what stuff that like, you might not focus on, but what do you expect other people to be building, right? So people that are like five x 50 Xing.

[00:39:00] Should you build stuff that’s like very niche for your workflow, for your team? Should it be more general so other people can adopt? Is there a niche there? ‘Cause part of it is just okay, is everything just internal tooling? Do we have everything our own way? Like the way our team operates has our own ways that we like to communicate or is there a broader way to do it?

[00:39:00] Is it something like a issue tracker? Just thoughts if you wanna riff on that.

## [00:39:35] Standardizing Skills and Code

**Ryan Lopopolo** [00:39:00] I think TBD we have not figured this out in a general way. I do think that there is leverage to be had in making the code and the processes as much the same as possible. If you think that code is context, code is prompts, it’s better from the agent behavior perspective to be able to look in a package in directory X, Y, Z, and it not to have to page so deeply into directory if you C, because they have the same structure, use the same language, they have the same patterns internally.

[00:40:00] And that same like leverage comes from aligning on a single set of skills that you’re pouring every engineer’s taste into to make sure that the agent is effective. So like in our code base, we have, I think, six skills. That’s it. And if some part of the software development loop is not being covered, our first attempt is to encode it in one of the existing setup skills, which means that we can change the agent behavior.

[00:40:00] Yeah. More cheaply than changing the human driver behavior.

**swyx** [00:40:00] Yeah.

## [00:40:39] Self Improvement via Logs

**swyx** [00:40:00] Have you ever, have you experimented with agents changing their own behavior?

**Ryan Lopopolo** [00:40:00] We do.

**swyx** [00:40:00] Yeah. Or parent agent changing a subagents, behavior or something like that.

**Ryan Lopopolo** [00:40:00] We have some bits for skill distillation. So for example, there’s one neat thing you can do with Codex, which is just point it at its own session logs to ask it to tell you how you can use the tool pedal better.

**swyx** [00:41:00] It’s like introspection

**Ryan Lopopolo** [00:41:00] or ask it to do things. I use

**Vibhu** [00:41:00] this session better. What skills should I

**swyx** [00:41:00] high? I like the modification of, you can do, just do things to you can just ask agent to do things.

**Ryan Lopopolo** [00:41:00] Yeah. You can just codex things. This is like a, this is like a silly emoji that we have, right? You can just codex things, you can just prompt things.

[00:41:00] It’s really glorious future we live in, but okay, you can do that one-on-one. But we’re actually slurping these up for the entire team into blob storage and. Running agent loops over them every day to figure out where as a team can we do better and how do we reflect that back into the repositories?

[00:41:00] Yes, though everybody benefits from everybody else’s behavior for free. Same for like PR comments, right? These are all feedback. That means the code as written, deviated from what was good, a PR comment, a failed build. These are all signals that mean at some point the agent was missing context. We gotta figure out how to

**swyx** [00:41:00] Yeah.

**Ryan Lopopolo** [00:41:00] Slurp it up and put it back in the reboot.

**swyx** [00:41:00] By the way, I do this exactly right. I used to, when I use cloud code for knowledge work, cloud cowork is like a nice product, right? Yes. In I think you would agree. I always have it tell me what do I do better next time? And that’s the meta programming reflection thing.

[00:42:00] So I almost think like you have six reflection extraction levels in symphony and almost like the zero of layer. So the six levels are PO policy, configuration, coordination, execution, integration, observability. We’ve talked about a couple of these, but the zero layer is like the, okay, are we working well?

[00:42:00] Can we improve how we work? Yes. Can I modify my own workflow without MD or something? I don’t know.

**Ryan Lopopolo** [00:42:00] Yeah, of course. Yeah, of course you can. Like this thing is also able to cut its own tickets ‘cause we give it full access.

[00:42:00] Yeah. Make it a ticket to have it cut. Tickets you can.

[00:42:00] Put in the ticket that you expect it to file as on follow up work,

**swyx** [00:42:00] like Yeah. Self-modifying. Yeah.

**Ryan Lopopolo** [00:42:00] Yeah.

## [00:42:44] Tool Access and CLI First

**Ryan Lopopolo** [00:42:00] Put, don’t put the agent in a box. Give the agent full accessibility over it. Domain.

**swyx** [00:42:00] I had a mental reaction when you said don’t put the agent in a box. So I think you should put it in a box. Like it’s just that you’re giving the box everything it needs.

**Ryan Lopopolo** [00:42:00] Yeah. Context and tools.

**swyx** [00:42:00] But we’re like, as developers, we’re used to calling out to different systems, but here you use the open source things like the Prometheus, whatever, and you run it locally so that you can have the full loop. I assume.

**Ryan Lopopolo** [00:43:00] Yep.

**Vibhu** [00:43:00] I think like

**Ryan Lopopolo** [00:43:00] another, you wanna minimize cloud, cloud dependencies.

**Vibhu** [00:43:00] You also want to make sure that you think about what the agent has access to. What does it see? Does it go back into the loop, like from the most basic sense of you let it see its own like calls, traces it can determine where it went wrong. But are you feeding that back in? So you know, just the most basic level of you wanna see exactly what’s input output, like does the agent have access to.

[00:43:00] What is being outputted, right? It can self-improve a lot of these things. It’s all

**Ryan Lopopolo** [00:43:00] text, right? My job is to figure out ways to funnel text from one agent to the other.

**swyx** [00:43:00] It’s so strange like way back at the start of this whole AI wave Andre was like, English is the hottest day programming language.

[00:43:00] It’s here, it’s just Yeah. The feature as well.

**Vibhu** [00:43:00] A lot of, okay. Like a lot of software, a lot of stuff. There’s a gui, it’s made for the human. We’re seeing the evolution of CLI for everything, right? All tools have CLIs. Your agents can use them well, do we get good vision? Do we get good little sandboxes?

[00:44:00] Like right now? It’s a really effective way, right? Models love to use tools. They love the best. They love to read through text. So slap a CLI let it go loose. That works for everything.

**Ryan Lopopolo** [00:44:00] It does. Yeah. Yeah.

## [00:44:14] UI Perception and Rasterizing

**Ryan Lopopolo** [00:44:00] We’ve also been adapting nont, textual things to that shape in order to improve model behavior in some ways, right?

[00:44:00] We want the agent to be able to see the UI agents do not perceive visually in the same way that we do. They don’t see a red box, they see red box button, right? They see these things in latent space. So if we want, Hey, yeah, I do. We have

**swyx** [00:44:00] a ding if that goes off every time. Alien space

**Ryan Lopopolo** [00:44:00] ding.

[00:44:00] Anyway if we wanna actually make it see the layout, it’s almost easier to rasterize that image to ask EOR and feed it in to the agent. Ha. And there’s no reason you can’t do both, right? To like further refine how the model perceives the object it’s manipulating.

**swyx** [00:45:00] Cool. Could we, you wanna talk about a couple more of these layers that might bear more introspection or that you have personal passion for?

## [00:45:07] Coordination Layer with Elixir

**Ryan Lopopolo** [00:45:00] I will say that the coordination layer here was a really tricky piece to get right.

**swyx** [00:45:00] Let’s do it. Yep. I’m all about that. And this is Temporal core.

**Ryan Lopopolo** [00:45:00] This is where when we turn the spec into Elixir, where like the model takes a shortcut, right? Like it’s oh, I have all these primitives that I can make use of in this lovely runtime that has native process supervision.

[00:45:00] Which is I think, a neat way to have taken the spec and made it more choices achievable by making choices that naturally map

**swyx** [00:45:00] Yeah.

**Ryan Lopopolo** [00:45:00] To the domain, right? In the same way that like you would prefer to have a TypeScript model repo if you are doing full stack web development, right? Because the ability to share types across the front end and backend reduces a lot of complexity.

[00:45:00] And because

**swyx** [00:45:00] that’s what graph kill used to be.

**Ryan Lopopolo** [00:45:00] That’s right. And

**swyx** [00:45:00] I don’t know if it’s still alive, but

**Ryan Lopopolo** [00:45:00] no humans in the loop here. So like my own personal ability to write or not write elixir. Doesn’t really have to bias us away from using the right tool for the job. It is just wild.

**swyx** [00:46:00] Love it. I love it.

[00:46:00] Yeah. I wonder if any languages struggle more than others because of this? I feel like everyone has their own abstractions. That would make sense. But maybe it might be slower, it might be more faulty where like you’d have to just kick the server every now and then. I, I don’t know. I think observability layer is really well understood.

[00:46:00] Integration layer, CP is dead. I think all these just like a really interesting hierarchy to travel up and down. It’s common language for people working on the system to understand

**Ryan Lopopolo** [00:46:00] The policy stuff is really cool, right? Yeah. You don’t really have to build a bunch of code to make sure the system wait for the, to pass

**swyx** [00:46:00] it’s institutional knowledge.

**Ryan Lopopolo** [00:46:00] Yeah. You just give it the G-H-C-L-I with some text that say CI has to pass. It makes the maintenance of these systems a lot easier.

## [00:46:57] Agent Friendly CLI Output

**swyx** [00:46:00] Do you think that CLI maintainers need to be do anything special for agents or just as is? It’s good because like I don’t think when people made the G GitHub, CLI, they anticipated this happening.

**Ryan Lopopolo** [00:47:00] That’s correct. The GH CLI is fantastic. It’s great super industry.

**swyx** [00:47:00] Everyone go try GH repo create GH pull and then pull request number, right? GH HPR, like 1 53, whatever. And then it like pulls

**Ryan Lopopolo** [00:47:00] basically my only interaction with the GitHub web UI at this point is GH PR view dash web.

[00:47:00] Exactly. Glance

**swyx** [00:47:00] at the diff

**Ryan Lopopolo** [00:47:00] and be like Sure thing. Send it. Yeah. But the CLI are nice ‘cause they’re super token efficient and they can be made more token efficient really easily. Like I’m sure you all have seen like I go to build Kite or Jenkins and I could just get this massive wall of build output.

[00:47:00] And in order to unblock the humans, your developer productivity team is almost certainly gonna write some code that parses the actual exception out of the build logs and sticks it in a sticky note at the top of the page. And you basically want CLI to be structured in a similar way, right? You’re gonna want to patch dash silent to prettier because the agent doesn’t care that every file was already formatted.

[00:48:00] Just wants to know it’s either formatted or not. So it can then go run a right command. Similarly, like in our PNPM distributed script runner, when we had one, when you do dash recursive, like it produces a absolute mountain of text. But all of that is for passing. Test suites. So we ended up wrapping all of this in another script

**swyx** [00:48:00] to suppress the,

**Ryan Lopopolo** [00:48:00] which you can vibe the channel only output the failing parts of the tests.

**swyx** [00:48:00] You make a pipe errors versus the standard, standard out. I don’t know. Okay. Whatever. Too much thinking have to do that. The CII used to maintain SCLI for my company and yeah, this is like core, very core to my heart. But you’re vibing my job.

**Ryan Lopopolo** [00:48:00] That’s right.

**swyx** [00:48:00] Cool. Any other things?

[00:48:00] This is a long spec. I appreciate that. It’s got a lot of strong opinions in here. Any other things that we should highlight? I think obviously you can spend the whole day going through some of these, but I do think that some of these have a lot of care or some of this you might wanna tell people, Hey, take this, but, make it your own.

## [00:49:15] Blueprint Spec and Guardrails

**Ryan Lopopolo** [00:49:00] Fundamentally, software is made more flexible when it’s able to adapt to the environment in which it is deployed, which means that things like linear or GitHub even are specified within the spec, but not required pieces of it. There’s like a more platonic ideal of the thing that you could swap in like Jira or Bitbucket, for example.

[00:49:00] But being able to tightly specify things like the ID formats or how the Ralph Loop works for the individual agents. Basically means you can get up and running with a fully specified system quickly that you then evolve later on. I think we never intended for this to be a static spec that you can never change.

[00:50:00] It’s more like a blueprint to get something worth a starting point up and running.

**swyx** [00:50:00] Yeah.

**Ryan Lopopolo** [00:50:00] For you then to vibe later to your heart’s content,

**swyx** [00:50:00] you have like code and scripts in here where it’s oh, I think this is a really good prompt. It’s just a very long prompt.

**Ryan Lopopolo** [00:50:00] Fundamentally, the agents are good at following instructions, so give them instructions.

[00:50:00] And it will, improve the reliability of the result. We, much like the way we use Symphony, we don’t want folks to have to monitor the agent as it is vibing the system into existence. So being very opinionated

[00:50:00] Very strict around what these success criteria are means that our deployment success rate goes up. Yeah. It means we don’t have to get tickets on this thing.

**Vibhu** [00:50:00] Think it all goes back to that like code to disposable, right? Like early on when you had CLI or you’d kick off a Codex run, it would take two hours. You would wanna monitor okay, I’m in the workflow of just using one.

[00:50:00] I don’t want it to go down the wrong path. I’ll cut it off and, just shoot off four, like that was my favorite thing of the Codex app, right? Yeah. Just Forex it like, it’s okay. One of them will probably be right, one of them might be better. Stop overthinking it. Like my first example was probably like deep research.

[00:51:00] When you put out deep research and I’d ask it something like, I asked it something about LLM, it thought it was legal something and spent an hour, came back with a report completely off the rails. And I was like, okay, I gotta monitor this thing a bit. No don’t monitor it. Just you want to build it so it’s that it, it goes the right way.

[00:51:00] And you don’t wanna, you don’t wanna sit there and babysit, right? You don’t want to babysit your agents

**Ryan Lopopolo** [00:51:00] with that deep research query that you made. Looking at the bad result, you probably figured out you needed to tweak your prompt Yeah. A bit, right? That’s that guardrail that you fed back into the code base for the task, your prompt to further align the agent’s execution.

[00:51:00] Same sort of concept supply there too.

**swyx** [00:51:00] When you talk, how are the customers feeling

**Ryan Lopopolo** [00:51:00] for Symphony? I think we have none, right? This is a thing we have put out into the

**swyx** [00:51:00] world. Symphony’s internal, right? As long as you are happy, you are the customer. That’s right. Just, what’s the external view?

## [00:51:53] Trust Building with PR Videos

**Ryan Lopopolo** [00:51:00] I’d say folks are very excited about this way of distributing software and ideas in cheap ways. For us as users, it has again, pushed the productivity five x, which means I think there’s something here that’s like a durable pattern around removing the human from the loop and figuring out ways to trust the output.

[00:52:00] The video that is shared here

**swyx** [00:52:00] Yeah.

**Ryan Lopopolo** [00:52:00] Is the same sort of video we would expect the coding agent to attach to the pr.

**swyx** [00:52:00] Yeah.

**Ryan Lopopolo** [00:52:00] That is created. Yeah. That’s part of building trust in this system and that’s, to me, like fundamentally what has been cool about building this is it more closely pushes that persona of the agent working with you to be like a teammate.

[00:52:00] I don’t shoulder surf you like for the tickets that you work on during the week. I would never think that I would want to do that.

**swyx** [00:52:00] Yeah.

**Ryan Lopopolo** [00:52:00] I wouldn’t want a screen recording of your entire session in Cursor or Claude code. I would expect you to do what you think you need to do to convince me that the code is good and mergeable

**swyx** [00:53:00] Yeah.

**Ryan Lopopolo** [00:53:00] And compress that full trajectory in a way that is legible to me. The reviewer.

**swyx** [00:53:00] Yeah.

**Ryan Lopopolo** [00:53:00] It’s Stu. And you can just do that because Codex will absolutely sling some f you can just around. It’s great.

**swyx** [00:53:00] Oh, F FM P is the og like God, CLI.

**Ryan Lopopolo** [00:53:00] Yeah.

**swyx** [00:53:00] Swiss Army Chainsaw. I used to say. There’s a SaaS, micro SaaS that’s called it in every flag in FFM Peg.

**Ryan Lopopolo** [00:53:00] Oh, for sure.

**swyx** [00:53:00] You know what I mean? For sure. Just host it as a service, put a UI on it. People who don’t know FM Peg will pay for it.

**Ryan Lopopolo** [00:53:00] When we were first experimenting with this, it was a wild feeling to be at the computer with just like windows just popping up all over the place and getting captured and files appearing on my desktop, like very much felt like the future to have a thing controlling my computer for like actual productive use.

[00:53:00] Like I’m just there

**swyx** [00:53:00] keeping it. Like awake, jiggling the mouse every once in a while. That’s what some office workers do. So they buy a mouse jiggler. That’s right.

## [00:53:59] Spark vs Reasoning Models

**Vibhu** [00:53:00] One thing I wanted to ask, so okay, as stuff is so CO is disposable is saying shoot off a budget of agents. One question is okay, are you always like a extra high thinking guy?

[00:54:00] And where do you see Spark? So 5.3 Spark, there’s a lot of me wanting to make quick changes. I’m not gonna open up a id, I’m not gonna do anything. But I will say, okay, fix this little thing, change a line, change a color. Spark is great for that, but am I still a bottleneck? Like, why don’t I just let that go back?

[00:54:00] I’m like, just riff on that. Is there,

**Ryan Lopopolo** [00:54:00] spark is such a different model compared to the. The extra high level reasoning that you get in these, five Yeah. To clear for people.

**swyx** [00:54:00] It is a different model, different architecture, different, like it doesn’t support

**Ryan Lopopolo** [00:54:00] it, it just, it’s incredibly fast smaller model.

[00:54:00] I have not quite figured out how to use it yet. To be honest, I use faster. I was adapting it to the same sorts of tasks I would use X high reasoning for. Yeah. I, and it would blow through three compactions before writing a line of code.

**Vibhu** [00:54:00] And that’s another big thing with 5.4 right.

[00:54:00] Million co context.

**Ryan Lopopolo** [00:54:00] Yes, it’s

**Vibhu** [00:54:00] fantastic. Which is huge ingenix, right? Like you can just run for longer before you have to compact. The more tokens you can spend on a task before compacting, like the better you’ll do.

**Ryan Lopopolo** [00:55:00] That’s right. That’s right. I’m not sure how to deploy spark. I think your intuition is right, that it’s very great for spiking out prototypes, exploring ideas quickly, doing those documentation updates.

[00:55:00] It is fantastic for us in taking that feedback and transforming it into a lint. Where we already have good infrastructure for ES links in the code base these sorts of things it’s great at and it allows us to unblock quickly doing those like anti-fragile healing tasks in the code base.

**swyx** [00:55:00] Yeah, that makes sense.

## [00:55:38] What Models Can’t Do Yet

**swyx** [00:55:00] So you are push, you guys are pushing models to the freaking limit.

## [00:55:41] Current Model Limitations

**swyx** [00:55:00] What can current models not do well yet?

**Ryan Lopopolo** [00:55:00] They’re definitely not there on being able to go from new product idea to prototype single

**swyx** [00:55:00] one shot.

**Ryan Lopopolo** [00:55:00] This is where I find I spend a lot of time steering is translating end state of a mock for a net new thing, right?

[00:56:00] Think no existing screens into product that is playable with. Similarly, while this has gotten better with each model release, like the gnarliest refactorings are the ones that I spend my most time with, right? The ones where I’m interrupting the most, the ones where I am. Now double clicking to build tooling to help decompose monoliths and things like that.

[00:56:00] This is a thing I only expect to get better, right? Over the course of a month, we went from the low complexity tasks to like low complexity and big tasks in both these directions. So this is what it means to not bet against the model, right? You should expect that it is going to push itself out into these higher and higher complexity spaces.

[00:56:00] Yeah. So the things we do are robust to that. It just basically means I’ll be able to spend my time elsewhere and figure out what the next bottleneck is.

**Vibhu** [00:56:00] I do think it’s also a bit of a different type of task, right? Codex is really good at codebase understanding, working with code bases. But companies like Lovable bolt, repli, they solve a very different problem.

[00:57:00] Scaffold of zero to one, right? Idea of a product. And it’s there, there are people working on that and models are also pushing like step function changes there. It’s just different than the software engineering agents today, right?

**Ryan Lopopolo** [00:57:00] Like I said, the model is isomorphic to myself.

[00:57:00] The only thing that’s different is figuring out how to get what’s in here into context for the model and for these white space sort of projects. I, myself, I’m just not good at it. Which means that often over the agent trajectory, I realize the bits that we’re missing, which is why I find I need to have this synchronous interaction.

[00:57:00] And I expect with the right harness, with the right scaffold, that’s able to tease that outta me or refine the possible space, right? To be super opinionated around the frameworks that are deployed or to put a template in place, right? These are ways to give the model. All those non-functional requirements, that extra context to acre on and avoid that wide dispersion of possible outcomes.

**swyx** [00:57:00] Thank you for that.

## [00:58:00] Frontier Enterprise Platform

**swyx** [00:58:00] I wanted to talk a little bit about Frontier.

**Ryan Lopopolo** [00:58:00] Yeah, sure.

**swyx** [00:58:00] Overall you guys announced it maybe like a month ago. And there’s a few charts in here and it’s basic like your enterprise offering is what I view it. Is there one product or is there many,

**Ryan Lopopolo** [00:58:00] I can’t speak to the full product roadmap here, but what I can say is that Frontier is the platform by which we want to do AI transformation of every enterprise and from big to small.

[00:58:00] And the way we want to do that is by making it easy to deploy highly observable, safe, controlled, identifiable agents into the workplace. We want it to work with your company native. I am stack. We want it to plug into the security tooling that you have. Oh, we want it to be able to plug into the workspace tools that you used,

**swyx** [00:58:00] so you’re just gonna be stripping specs, right?

**Ryan Lopopolo** [00:58:00] We expect that there will be some harness things there. Agents, SDK is a core part of this to enable both startup builders as well as enterprise builders to have a works by default harness that is able to use all the best features of our models from the Shell tool down to the Codex Harness with file attachments and containers and all these other things that we know go into building highly reliable, complex agents.

[00:59:00] We wanna make that great and we wanna make it easy to compose these things together in ways that are safe, for example, right? Like the G-P-T-O-S-S safeguard model. For example. One thing that’s really cool about it is it ships. The ability to interface with a safety spec. Safety specs are things that are bespoke to enterprises.

[00:59:00] We owe it to these folks to figure out ways for them to instrument the agents in their enterprise to avoid exfiltration in the ways they specifically care about, to know about their internal company, code names, these sorts of things. So providing the right hooks to make the platform customizable, but also, mostly working by default for folks is the space we are trying to explore here.

**swyx** [01:00:00] Yeah. And this is the snowflakes of the world just need this, right? Yes. Your Brexit of the world stripes. Yeah, it makes sense.

## [01:00:11] Dashboards and Data Agents

**swyx** [01:00:00] I was gonna go back to your, I think the demo videos that you guys had was pretty illustrative. It’s like also to me an example of very large scale agent management.

[01:00:00] Yes. Like you give people a control dashboard that if you play, if you like, play any one of these like multiple agent things, you can di dig down to the individual instant and see what’s going on.

**Ryan Lopopolo** [01:00:00] Yes, of course.

**swyx** [01:00:00] But who’s the user Is it let’s it like the CEO, the CTO, ccio, something like that.

**Ryan Lopopolo** [01:00:00] At least with my personal opinion here, the buyer that we’re trying to build product for here is one and employees who are making productive use of these agents, right?

[01:00:00] That’s gonna be whatever surfaces they appear in the connectors they have access to, things like that. Something like this dashboard is for it. Your GRC and governments folks, your AI innovation office, your security team, right? The stakeholders in your company that are responsible for successfully deploying into.

[01:01:00] The spaces where your employees work, as well as doing so in a safe way that is consistent with all the regulatory requirements that you have and customer attestations and things like that. So it is a iceberg beneath the actual end. It’s,

**swyx** [01:01:00] yeah you jump every, I guess layer in the UI is like going down the layer of extraction in terms of the agent, right?

[01:01:00] Yep. Yeah. Yeah. I think it’s good.

**Ryan Lopopolo** [01:01:00] Yeah. The ability to dive deep into the individual agent trajectory level is gonna be super powerful.

[01:01:00] Not only for from like a security perspective, but also from like someone who is accountable for developing skills. One thing that was interesting that we also blogged about shipping was an internal data agent, which uses a lot of the frontier technology in order to make our data ontology accessible to the agent and things like that to understand.

[01:01:00] What’s actually in the data warehouse?

**swyx** [01:02:00] Yeah. Seman layer Yes. Type things. Yes. I was briefly part of the, that, that world is it salt? I don’t know. It’s actually really hard for humans to agree on what revenue is. Yes.

**Ryan Lopopolo** [01:02:00] Yes.

**swyx** [01:02:00] What is an active user?

**Ryan Lopopolo** [01:02:00] There’s what, five data scientists in the company that have defined this Golden.

**swyx** [01:02:00] They, yeah. And no. And there’s also internal politics. Yes. As to attribution of I’m marketing, I’m responsible for this much, and sales is responsible for this much, and they all add up to more than a hundred. And I’m like you guys have different definitions.

**Vibhu** [01:02:00] Yeah. And if you’re a startup, everything is a RR,

**swyx** [01:02:00] So I think that’s cool.

[01:02:00] Oh, you guys blog about this. Okay. I didn’t see this. Yeah. Is this the same thing? I don’t know. This is what you’re referring to? Yes. Okay. We’ll send people to read this. This is our data.

**Vibhu** [01:02:00] Him this one.

**swyx** [01:02:00] Yeah. I don’t know if you’re you have any highlights? I

**Vibhu** [01:02:00] No. In general from the playlist.

[01:02:00] Yeah. A lot of good things to read.

**swyx** [01:02:00] Yeah. Yeah. Lot, lots of homework for people. No, but like data as the feedback layer, you need to solve this first in order to have the products feedback loop closed. That’s right. So for the agents to understand and this is not something that humans have not solved.

[01:02:00] This like, and

**Ryan Lopopolo** [01:02:00] this is how you build artists that do more than coding, right? Yeah.

**swyx** [01:03:00] Yeah.

**Ryan Lopopolo** [01:03:00] To actually understand how you operate the business.

**swyx** [01:03:00] Yeah.

**Ryan Lopopolo** [01:03:00] You have to understand what revenue is, what your customer segments are. Yeah. What your product lines are.

## [01:03:13] Company Context and Memes

**Ryan Lopopolo** [01:03:00] Like one thing that’s in looping back to the code base that we described here for harnessing, one thing that’s in core beliefs.md is who’s on the team, what product we’re building, who our end customers are.

[01:03:00] Who our pilot customers are, what the full vision of what we want to achieve over the next 12 months is these are all bits of context that inform how we would go about building the software. Oh my God. So we have to give it to the agent too.

**Vibhu** [01:03:00] I’m guessing that stuff is like pretty dynamic and it changes over time too, right?

[01:03:00] Like part of it was, it’s not just a big spec. You have it as one of the things and it will iterate.

**Ryan Lopopolo** [01:03:00] One, one thing that I think is gonna break your mind even more is we have skills for how to properly generate deep fried memes and have Ji culture and Slack. Because with the Slack Chachi PT app that you’re able to use in Codex, like I can get the agent to shit post on my behalf.

[01:04:00] Just, it’s part of humor.

**swyx** [01:04:00] Theme humor. Humor is part of EGI. Is it funny? It is pretty good, yeah. Okay. Yeah,

**Ryan Lopopolo** [01:04:00] it’s pretty good at making

**swyx** [01:04:00] Deep, it’s a lot of I think humor is like a really hard intelligence test, right? It’s like you have to get a lot of context into like very few words.

[01:04:00] This is why make references

**Ryan Lopopolo** [01:04:00] is why five four is such a big uplift for our it’s the me. Yeah, for sure. Yeah. Yeah.

**swyx** [01:04:00] It’s very cool.

**Vibhu** [01:04:00] So five, four can two post. So that’s what we take over here.

**Ryan Lopopolo** [01:04:00] Yeah. Maybe maybe when y’all are done here today, ask Codex to go over your coding agent sessions and to roast you.

**swyx** [01:04:00] Love it. I’ll give it a shot. Give a shot. Coming back to the final point I wanted to make is, yeah I think that there, there are multiple other, like you guys are working on this, but this is a pattern that every other company out there should adopt. Yes. Regardless of whether or not they work with you.

[01:04:00] To me, this is I saw this, I was like, fuck, every company needs this. This

[01:05:00] is

**swyx** [01:05:00] multiple billions.

**Ryan Lopopolo** [01:05:00] This is what it takes to get

**swyx** [01:05:00] Yeah.

**Ryan Lopopolo** [01:05:00] People to Yes. Yeah. Actually realize the benefits. Yes. And distribute.

**swyx** [01:05:00] And it’s, it, I think it sounds boring to people like, oh, it’s for safeguards and whatever, but I think you to handle agents at scale like you are envisioning here I don’t know if it’s like a real screenshot, like a demo, but this is what you need.

[01:05:00] This is, or my original sort of view of what Temporal was supposed to be that you, you built this dashboard and you basically have every long running process in the company Yes. In one dashboard and that’s it. That’s right.

**Vibhu** [01:05:00] Yeah. I think it’s pretty customized towards every enterprise, right?

[01:05:00] Like you care about different things.

**swyx** [01:05:00] There’s a lot of customization, but there’ll be multiple unicorns just doing this as a service. I don’t know. I’m like very frontier field, if you can tell. Amazing. But it, it only clicked ‘cause obviously this came out first, then Harness eng, then symphony and only clicked for me that like, this is actually the thing you shipped to do that.

**Ryan Lopopolo** [01:05:00] Yeah. Yeah. There’s a set of building blocks here that we assembled into these agents and the building blocks themselves are part of the product, right? Yeah. The ability to steer revoke authorization if a model becomes misaligned, like all of this is accessible through Frontier. And there’s gonna be a bunch of stakeholders in the company that have the things they need to see in the platform Yeah.

[01:06:00] To get to. Yes. So we’ll build all of those in the frontier so that we can actually do the widespread the planet. Yeah. That’s the fun part.

**swyx** [01:06:00] Yeah. I’m also calling back to there’s this like levels of EGI I don’t know if Opening Eye is still talking about this, but they used to talk about five levels of EGI and one of it was like, oh, it’s like an intern coding software patient.

[01:06:00] At some point it was AI organization and this is it. That’s right. This is level four or five. I can’t remember which, which level, but it’s somewhere along that path. Was this.

**Ryan Lopopolo** [01:06:00] You know how I mentioned that my team is having fun sprinting ahead here. And we do this thing where we’re collecting all the agent trajectories from Codex to slurp them up and distill them.

[01:06:00] This is what it means to build our team level knowledge base, happen to reflect it back into the code base. But it doesn’t have to be that way. And it doesn’t have to be bound to just codex. I want Chacha BT to also learn our meaning culture and also the product we are building and how so that when I go ask it, it also has the full context of the way I do my work and I’m super excited for Frontier to enable this.

**swyx** [01:07:00] Yeah. Amazing.

## [01:07:21] Harness vs Training Tension

**swyx** [01:07:00] What are the model people say when they see you do this? Like you have a lot of feedback, obviously you have a lot of usage, you have a lot of trajectories and don’t, I don’t imagine a lot of it’s useful to them, but some of it is,

**Vibhu** [01:07:00] you have this too, you deploy a billion tokens of intelligence a day and this was, this was at the beginning of 2096.

[01:07:00] You’re Yeah. Cooking.

**Ryan Lopopolo** [01:07:00] Yeah, there’s this fundamental tension, which I think you have talked about between whether or not we invest deeper into the harness or we invest deeper into the training process to get the model to do more of this by default. Yeah, and I think success for the way we are operating here means the model gets better taste because we can point the way there and none of the things we have built actively degrade Asian performance.

[01:08:00] ‘cause really all they’re doing is running tests and like running tests is a good part of what it means to write reliable software. If we were building an entire separate rust scaffold around Codex to restrict its output, that I think would be like additional harness that would be prone to being scrapped.

[01:08:00] But yeah. Yeah. If instead we can build all the guardrails in a way that’s just native to the output that Codex is already producing, which is code, I think. No friction with how the model continues to advance, but also like just good engineering and that’s the whole point.

**swyx** [01:08:00] Yeah. So I’ve had similar discussions with research scientists where the RL equivalent is on policy versus off policy.

[01:08:00] Yeah. And you’re basically saying that you should build an on policy harness, which is already within distribution and you modify from there. But if you build it off policy, it’s not that useful.

**Ryan Lopopolo** [01:09:00] That’s right.

**swyx** [01:09:00] Super cool. Any, anybody thoughts, any things that we haven’t covered that we should get it, get out there?

## [01:09:08] Closing Thoughts & OpenAI Hiring

**Ryan Lopopolo** [01:09:00] Just I’ve been super excited to benefit from all the cooking that the Codex team has been doing. Yes. They absolutely ship relentlessly. This is one of our core engineering values, ship relentlessly, and they, the team there embodies it. To extreme degree, yeah, I have five three and then Spark and five four come out within what feels like a month is just a phenomenally fast.

**swyx** [01:09:00] It’s exactly a month ago it’s five three and yesterday was five four. Yeah. I mean it’s, do we have every month now is five five next? Exactly.

**Ryan Lopopolo** [01:09:00] I can’t say that the poll markets would be very upset.

**swyx** [01:09:00] I think it’s interesting that it’s also correlated with the growth. They announced that it’s 2 million users, but like almost don’t care about Codex anymore.

[01:09:00] This is it, this is the gay man. It’s like coding cool, soft like knowledge work.

**Ryan Lopopolo** [01:09:00] That’s right. That’s right. This is the thing to chase after. Yeah. And this is one of things that my team is excited to support,

**swyx** [01:09:00] get the whole like self-hosted harness thing working, which you have done and like the rest of us are trying to figure out how to catch up, but then do things.

[01:10:00] You That’s right. With you

**Vibhu** [01:10:00] do things.

**swyx** [01:10:00] That’s right. You can just do things. That’s the line for the episode.

**Vibhu** [01:10:00] That’s it. Any other call to actions. You’re based in Seattle, your team, I’m guessing. New Bellevue office.

**Ryan Lopopolo** [01:10:00] New Bellevue office. We just had the grand opening yesterday as of the recording date which was fantastic.

[01:10:00] Beautiful buildings. Super excitedly part of the Bellevue Community building the future in Washington. And I would say that there is lots of work to be done in order to successfully serve enterprise customers here in Frontier. We are certainly hiring and if you haven’t tried the Codex app yet, please give it a download.

[01:10:00] We just passed 2 million weekly active users growing at a phenomenally fast rate, 25% week over week. Come join us.

**swyx** [01:10:00] Yes. And I think that’s an interesting no. My, my final observation opening is a very San Francisco centric company. I know people who have been. Who turned down the job or didn’t get the job ‘cause they didn’t want to move to sf and now they just don’t have a choice.

[01:11:00] You have to open the London, you have to open the Seattle. And I wonder if that’s gonna be a shift in the culture, obviously you can’t say, but

**Ryan Lopopolo** [01:11:00] I was one of the first engineering hires out of our Seattle office, so Yeah.

**swyx** [01:11:00] See I was very natural.

**Ryan Lopopolo** [01:11:00] Its success has been part of what I have been building toward and it is, it has grown quite well, right?

[01:11:00] Yeah. We have durable products in the lines of business that are built outta there a ton of zero to one work happening as well, which is the core essence of the way we do applied AI work at the company to sprint after it new to figure out where we can actually successfully deploy the model.

[01:11:00] Yeah. Yes. A hundred percent. We also have a New York office too that has a ton of engineering presence.

**swyx** [01:11:00] Yeah. Exact. Exactly. That’s these are my road roadmaps for a e wherever people hiring engineers, I will go. That’s right. Ra it’s

**Vibhu** [01:11:00] a cool office to New York is a old REI building, I believe the REI office.

**swyx** [01:11:00] It’s just No, you’ll never be as big. New York is you can’t get the size of office that they need.

**Ryan Lopopolo** [01:12:00] The New York office, Seattle user has a very office Mad Men vibe. It’s beautiful. The Bellevue one is very green, gold fixtures, very Pacific Northwest is very cool place to the vibe.

[01:12:00] Be local

**Vibhu** [01:12:00] little, yeah. A lot of people are like there for people like New York. They wanna be in New York, right?

**Ryan Lopopolo** [01:12:00] Yeah. Yeah. We have a fantastic workplace team that has been building out these offices. It really is a privilege to work here. Yeah. Excellent. Okay. Thank you for your time. You’ve been very

**swyx** [01:12:00] generous and you’re, you’ve been cooking, so I’m gonna let you get back to cooking.

[01:12:00] It’s been amazing to be with you folks. Happy Friday. Happy Friday.
