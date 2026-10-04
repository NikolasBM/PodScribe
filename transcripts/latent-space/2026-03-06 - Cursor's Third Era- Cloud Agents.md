---
podcast: "latent-space"
podcast_title: "Latent Space"
title: "Cursor's Third Era: Cloud Agents"
date: 2026-03-06
url: "https://www.latent.space/p/cursor-third-era"
guid: "substack:190063769"
host: "Swyx"
guests: ["Samantha", "Jonas", "swyx"]
format: "interview"
level: 2
length: "01:06:00"
categories: ["agents", "coding", "work", "model-strategy"]
featured: ["Cursor", "Slack", "agent harness", "computer use"]
mentioned: ["MCP", "OpenAI Codex", "vibe coding"]
transcript_source: "publisher"
---

# Cursor's Third Era: Cloud Agents

## Agentic Code Experiments

**Samantha** [00:00:00] This is another experiment that we ran last year and didn’t decide to ship at that time, but may come back to LM Judge, but one that was also agentic and could write code. So it wasn’t just picking but also taking the learnings from two models or and models that it was looking at and writing a new diff.

[00:00:00] And what we found was that there were strengths to using models from different model providers as the base level of this process. Basically you could get almost like a synergistic output that was better than having a very unified like bottom model tier.

**Jonas** [00:00:00] We think that over the coming months, the big unlock is not going to be one person with a model getting more done, like the water flowing faster and we’ll be making the pipe much wider and so paralyzing more, whether that’s swarms of agents or parallel agents, both of those are things that contribute to getting much more done in the same amount of time.

## Why Cloud Agents Matter

**swyx** [00:00:00] This week, one of the biggest launches that Cursor’s ever done is cloud agents. I think you, you had cloud agents before, but this was like, you give cursor a computer, right? Yeah. So it’s just basically they bought auto tab and then they repackaged it. Is that what’s going on, or,

**Jonas** [00:01:00] that’s a big part of it.

[00:01:00] Yeah. Cloud agents already ran in their own computers, but they were sort of site reading code. Yeah. And those computers were not, they were like blank VMs typically that were not set up for the Devrel X for whatever repo the agents working on. One of the things that we talk about is if you put yourself in the model shoes and you were seeing tokens stream by and all you could do was cite read code and spit out tokens and hope that you had done the right thing,

**swyx** [00:01:00] no chance

**Jonas** [00:01:00] I’d be so bad.

[00:01:00] Like you obviously you need to run the code. And so that I think also is probably not that contrarian of a take, but no one has done that yet. And so giving the model the tools to onboard itself and then use full computer use end-to-end pixels in coordinates out and have the cloud computer with different apps in it is the big unlock that we’ve seen internally in terms of use usage of this going from, oh, we use it for little copy changes to no.

[00:02:00] We’re really like driving new features with this kind of new type of entech workflow. Alright, let’s see it. Cool.

## Live Demo Tour

**Jonas** [00:02:00] So this is what it looks like in cursor.com/agents. So this is one I kicked off a while ago. So on the left hand side is the chat. Very classic sort of agentic thing. The big new thing here is that the agent will test its changes.

[00:02:00] So you can see here it worked for half an hour. That is because it not only took time to write the tokens of code, it also took time to test them end to end. So it started Devrel servers iterate when needed. And so that’s one part of it is like model works for longer and doesn’t come back with a, I tried some things pr, but a I tested at pr that’s ready for your review.

[00:02:00] One of the other intuition pumps we use there is if a human gave you a PR asked you to review it and you hadn’t, they hadn’t tested it, you’d also be annoyed because you’d be like, only ask me for a review once it’s actually ready. So that’s what we’ve done with

## Testing Defaults and Controls

**swyx** [00:02:00] simple question I wanted to gather out front.

[00:02:00] Some prs are way smaller, like just copy change. Does it always do the video or is it sometimes,

**Jonas** [00:03:00] Sometimes.

**swyx** [00:03:00] Okay. So what’s the judgment?

**Jonas** [00:03:00] The model does it? So we we do some default prompting with sort. What types of changes to test? There’s a slash command that people can do called slash no test, where if you do that, the model will not test,

**swyx** [00:03:00] but the default is test.

**Jonas** [00:03:00] The default is to be calibrated. So we tell it don’t test, very simple copy changes, but test like more complex things. And then users can also write their agents.md and specify like this type of, if you’re editing this subpart of my mono repo, never tested ‘cause that won’t work or whatever.

## Videos and Remote Control

**Jonas** [00:03:00] So pillar one is the model actually testing Pillar two is the model coming back with a video of what it did.

[00:03:00] We have found that in this new world where agents can end-to-end, write much more code, reviewing the code is one of these new bottlenecks that crop up. And so reviewing a video is not a substitute for reviewing code, but it is an entry point that is much, much easier to start with than glancing at some giant diff.

[00:04:00] And so typically you kick one off you, it’s done you come back and the first thing that you would do is watch this video. So this is a, video of it. In this case I wanted a tool tip over this button. And so it went and showed me what that looks like in, in this video that I think here, it actually used a gallery.

[00:04:00] So sometimes it will build storybook type galleries where you can see like that component in action. And so that’s pillar two is like these demo videos of what it built. And then pillar number three is I have full remote control access to this vm. So I can go heat in here. I can hover things, I can type, I have full control.

[00:04:00] And same thing for the terminal. I have full access. And so that is also really useful because sometimes the video is like all you need to see. And oftentimes by the way, the video’s not perfect, the video will show you, is this worth either merging immediately or oftentimes is this worth iterating with to get it to that final stage where I am ready to merge in.

[00:04:00] So I can go through some other examples where the first video wasn’t perfect, but it gave me confidence that we were on the right track and two or three follow-ups later, it was good to go. And then I also have full access here where some things you just wanna play around with. You wanna get a feel for what is this and there’s no substitute to a live preview.

[00:05:00] And the VNC kind of VM remote access gives you that.

**swyx** [00:05:00] Amazing What, sorry? What is VN. And

**Jonas** [00:05:00] just the remote desktop. Remote desktop. Yeah.

**swyx** [00:05:00] Sam, any other details that you always wanna call out?

**Samantha** [00:05:00] Yeah, for me the videos have been super helpful. I would say, especially in cases where a common problem for me with agents and cloud agents beforehand was almost like under specification in my requests where our plan mode and going really back and forth and getting detailed implementation spec is a way to reduce the risk of under specification, but then similar to how human communication breaks down over time, I feel like you have this risk where it’s okay, when I pull down, go to the triple of pulling down and like running this branch locally, I’m gonna see that, like I said, this should be a toggle and you have a checkbox and like, why didn’t you get that detail?

[00:05:00] And having the video up front just has that makes that alignment like you’re talking about a shared artifact with the agent. Very clear, which has been just super helpful for me.

**Jonas** [00:06:00] I can quickly run through some other Yes. Examples.

## Meta Agents and More Demos

**Jonas** [00:06:00] So this is a very front end heavy one. So one question I was

**swyx** [00:06:00] gonna say, is this only for front

**Jonas** [00:06:00] end?

[00:06:00] Exactly. One question you might have is this only for front end? So this is another example where the thing I wanted it to implement was a better error message for saving secrets. So the cloud agents support adding secrets, that’s part of what it needs to access certain systems. Part of onboarding that is giving access.

[00:06:00] This is cloud is working on

**swyx** [00:06:00] cloud agents. Yes.

**Jonas** [00:06:00] So this is a fun thing is

**Samantha** [00:06:00] it can get super meta. It

**Jonas** [00:06:00] can get super meta, it can start its own cloud agents, it can talk to its own cloud agents. Sometimes it’s hard to wrap your mind around that. We have disabled, it’s cloud agents starting more cloud agents. So we currently disallow that.

[00:06:00] Someday you might. Someday we might. Someday we might. So this actually was mostly a backend change in terms of the error handling here, where if the secret is far too large, it would oh, this is actually really cool. Wow. That’s the Devrel tools. That’s the Devrel tools. So if the secret is far too large, we.

[00:07:00] Allow secrets above a certain size. We have a size limit on them. And the error message there was really bad. It was just some generic failed to save message. So I was like, Hey, we wanted an error message. So first cool thing it did here, zero prompting on how to test this. Instead of typing out the, like a character 5,000 times to hit the limit, it opens Devrel tools, writes js, or to paste into the input 5,000 characters of the letter A and then hit save, closes the Devrel tools, hit save and gets this new gets the new error message.

[00:07:00] So that looks like the video actually cut off, but here you can see the, here you can see the screenshot of the of the error message. What, so that is like frontend backend end-to-end feature to, to get that,

**swyx** [00:07:00] yeah.

**Jonas** [00:07:00] And

**swyx** [00:07:00] And you just need a full vm, full computer run everything.

[00:07:00] Okay. Yeah.

**Jonas** [00:07:00] Yeah. So we’ve had versions of this. This is one of the auto tab lessons where we started that in 2022. No, in 2023. And at the time it was like browser use, DOM, like all these different things. And I think we ended up very sort of a GI pilled in the sense that just give the model pixels, give it a box, a brain in a box is what you want and you want to remove limitations around context and capabilities such that the bottleneck should be the intelligence.

[00:08:00] And given how smart models are today, that’s a very far out bottleneck. And so giving it its full VM and having it be onboarded with Devrel X set up like a human would is just been for us internally a really big step change in capability.

**swyx** [00:08:00] Yeah I would say, let’s call it a year ago the models weren’t even good enough to do any of this stuff.

[00:08:00] So

**Samantha** [00:08:00] even six months ago. Yeah.

**swyx** [00:08:00] So yeah what people have told me is like round about Sonder four fire is when this started being good enough to just automate fully by pixel.

**Jonas** [00:08:00] Yeah, I think it’s always a question of when is good enough. I think we found in particular with Opus 4 5, 4, 6, and Codex five three, that those were additional step changes in the autonomy grade capabilities of the model to just.

[00:09:00] Go off and figure out the details and come back when it’s done.

**swyx** [00:09:00] I wanna appreciate a couple details. One 10 Stack Router. I see it. Yeah. I’m a big fan. Do you know any, I have to name the 10 Stack.

**Jonas** [00:09:00] No.

**swyx** [00:09:00] This just a random lore. Some buddy Sue Tanner. My and then the other thing if you switch back to the video.

**Jonas** [00:09:00] Yeah.

**swyx** [00:09:00] I wanna shout out this thing. Probably Sam did it. I don’t know

**Jonas** [00:09:00] the chapters.

**swyx** [00:09:00] What is this called? Yeah, this is called Chapters. Yeah. It’s like a Vimeo thing. I don’t know. But it’s so nice the design details, like the, and obviously a company called Cursor has to have a beautiful cursor

**Samantha** [00:09:00] and it is

**swyx** [00:09:00] the cursor.

**Samantha** [00:09:00] Cursor.

**swyx** [00:09:00] You see it branded? It’s the cursor. Cursor, yeah. Okay, cool. And then I was like, I complained to Evan. I was like, okay, but you guys branded everything but the wallpaper. And he was like, no, that’s a cursor wallpaper. I was like, what?

**Samantha** [00:09:00] Yeah. Rio picked the wallpaper, I think. Yeah. The video.

[00:09:00] That’s probably Alexi and yeah, a few others on the team with the chapters on the video. Matthew Frederico. There’s been a lot of teamwork on this. It’s a huge effort.

**swyx** [00:09:00] I just, I like design details.

**Samantha** [00:09:00] Yeah.

**swyx** [00:09:00] And and then when you download it adds like a little cursor. Kind of TikTok clip. Yes. Yes.

[00:10:00] So it’s to make it really obvious is from Cursor,

**Jonas** [00:10:00] we did the TikTok branding at the end. This was actually in our launch video. Alexi demoed the cloud agent that built that feature. Which was funny because that was an instance where one of the things that’s been a consequence of having these videos is we use best of event where you run head to head different models on the same prompt.

[00:10:00] We use that a lot more because one of the complications with doing that before was you’d run four models and they would come back with some giant diff, like 700 lines of code times four. It’s what are you gonna do? You’re gonna review all that’s horrible. But if you come back with four 22nd videos, yeah, I’ll watch four 22nd videos.

[00:10:00] And then even if none of them is perfect, you can figure out like, which one of those do you want to iterate with, to get it over the line. Yeah. And so that’s really been really fun.

## Bug Repro Workflow

**Jonas** [00:10:00] Here’s another example. That’s we found really cool, which is we’ve actually turned since into a slash command as well slash repro, where for bugs in particular, the model of having full access to the to its own vm, it can first reproduce the bug, make a video of the bug reproducing, fix the bug, make a video of the bug being fixed, like doing the same pattern workflow with obviously the bug not reproducing.

[00:11:00] And that has been the single category that has gone from like these types of bugs, really hard to reproduce and pick two tons of time locally, even if you try a cloud agent on it. Are you confident it actually fixed it to when this happens? You’ll merge it in 90 seconds or something like that.

[00:11:00] So this is an example where, let me see if this is the broken one or the, okay, this is the fixed one. Okay. So we had a bug on cursor.com/agents where if you would attach images where remove them. Then still submit your prompt. They would actually still get attached to the prompt. Okay. And so here you can see Cursor is using, its full desktop by the way.

[00:11:00] This is one of the cases where if you just do, browse use type stuff, you’ll have a bad time. ‘cause now it needs to upload files. Like it just uses its native file viewer to do that. And so you can see here it’s uploading files. It’s going to submit a prompt and then it will go and open up. So this is the meta, this is cursor agent, prompting cursor agent inside its own environment.

[00:12:00] And so you can see here bug, there’s five images attached, whereas when it’s submitted, it only had one image.

**swyx** [00:12:00] I see. Yeah. But you gotta enable that if you’re gonna use cur agent inside cur.

**Jonas** [00:12:00] Exactly. And so here, this is then the after video where it went, it does the same thing. It attaches images, removes, some of them hit send.

[00:12:00] And you can see here, once this agent is up, only one of the images is left in the attachments. Yeah.

**swyx** [00:12:00] Beautiful.

**Jonas** [00:12:00] Okay. So easy merge.

**swyx** [00:12:00] So yeah. When does it choose to do this? Because this is an extra step.

**Jonas** [00:12:00] Yes. I think I’ve not done a great job yet of calibrating the model on when to reproduce these things.

[00:12:00] Yeah. Sometimes it will do it of its own accord. Yeah. We’ve been conservative where we try to have it only do it when it’s quite sure because it does add some amount of time to how long it takes it to work on it. But we also have added things like the slash repro command where you can just do, fix this bug slash repro and then it will know that it should first make you a video of it actually finding and making sure it can reproduce the bug.

**swyx** [00:13:00] Yeah. Yeah. One sort of ML topic this ties into is reward hacking, where while you write test that you update only pass. So first write test, it shows me it fails, then make you test pass, which is a classic like red green.

**Jonas** [00:13:00] Yep.

**swyx** [00:13:00] Like

**Jonas** [00:13:00] A-T-D-D-T-D-D

**swyx** [00:13:00] thing.

[00:13:00] No, very cool. Was that the last demo? Is there

**Jonas** [00:13:00] Yeah.

[00:13:00] Anything I missed on the demos or points that you think? I think that

**Samantha** [00:13:00] covers it well. Yeah.

**swyx** [00:13:00] Cool. Before we stop the screen share, can you gimme like a, just a tour of the slash commands ‘cause I so God ready. Huh, what? What are the good ones?

**Samantha** [00:13:00] Yeah, we wanna increase discoverability around this too.

[00:13:00] I think that’ll be like a future thing we work on. Yeah. But there’s definitely a lot of good stuff now

**Jonas** [00:13:00] we have a lot of internal ones that I think will not be that interesting. Here’s an internal one that I’ve made. I don’t know if anyone else at Cursor uses this one. Fix bb.

**Samantha** [00:13:00] I’ve never heard of it.

**Jonas** [00:13:00] Yeah.

[00:14:00] Fix Bug Bot. So this is a thing that we want to integrate more tightly on. So you made it for

**swyx** [00:14:00] yourself.

**Jonas** [00:14:00] I made this for myself. It’s actually available to everyone in the team, but yeah, no one knows about it. But yeah, there will be Bug bot comments and so Bug Bot has a lot of cool things. We actually just launched Bug Bot Auto Fix, where you can click a button and or change a setting and it will automatically fix its own things, and that works great in a bunch of cases.

[00:14:00] There are some cases where having the context of the original agent that created the PR is really helpful for fixing the bugs, because it might be like, oh, the bug here is that this, is a regression and actually you meant to do something more like that. And so having the original prompt and all of the context of the agent that worked on it, and so here I could just do, fix or we used to be able to do fixed PB and it would do that.

[00:14:00] No test is another one that we’ve had. Slash repro is in here. We mentioned that one.

**Samantha** [00:14:00] One of my favorites is cloud agent diagnosis. This is one that makes heavy use of the Datadog MCP. Okay. And I think Nick and David on our team wrote, and basically if there is a problem with a cloud agent we’ll spin up a bunch of subs.

[00:15:00] Like a single

**swyx** [00:15:00] instance.

**Samantha** [00:15:00] Yeah. We’ll take the ideas and argument and spin up a bunch of subagents using the Datadog MCP to explore the logs and find like all of the problems that could have happened with that. It takes the debugging time, like from potentially you can do quick stuff quickly with the Datadog ui, but it takes it down to, again, like a single agent call as opposed to trolling through logs yourself.

**Jonas** [00:15:00] You should also talk about the stuff we’ve done with transcripts.

**Samantha** [00:15:00] Yes. Also so basically we’ve also done some things internally. There’ll be some versions of this as we ship publicly soon, where you can spit up an agent and give it access to another agent’s transcript to either basically debug something that happened.

[00:15:00] So act as an external debugger. I see. Or continue the conversation. Almost like forking it.

**swyx** [00:15:00] A transcript includes all the chain of thought for the 11 minutes here. 45 minutes there.

**Samantha** [00:15:00] Yeah. That way. Exactly. So basically acting as a like secondary agent that debugs the first, so we’ve started to push more and

**swyx** [00:15:00] they’re all the same code.

[00:16:00] It is just the different prompts, but the sa the same.

**Samantha** [00:16:00] Yeah. So basically same cloud agent infrastructure and then same harness. And then like when we do things like include, there’s some extra infrastructure that goes into piping in like an external transcript if we include it as an attachment.

[00:16:00] But for things like the cloud agent diagnosis, that’s mostly just using the Datadog MCP. ‘Cause we also launched CPS along with along with this cloud agent launch, launch support for cloud agent cps.

**swyx** [00:16:00] Oh, that was drawn out.

**Jonas** [00:16:00] We won’t, we’ll be doing a bigger marketing moment for it next week, but, and you can now use CPS and

**swyx** [00:16:00] People will listen to it as well.

[00:16:00] Yeah,

**Jonas** [00:16:00] they’ll

**Samantha** [00:16:00] be ahead of the third. They’ll be ahead. And I would I actually don’t know if the Datadog CP is like publicly available yet. I realize this not sure beta testing it, but it’s been one of my favorites to use. So

**swyx** [00:16:00] I think that one’s interesting for Datadog. ‘cause Datadog wants to own that site.

[00:16:00] Interesting with Bits. I don’t know if you’ve tried bits.

**Samantha** [00:16:00] I haven’t tried bits.

**swyx** [00:16:00] Yeah.

**Jonas** [00:16:00] That’s their cloud agent

**swyx** [00:16:00] product. Yeah. Yeah. They want to be like we own your logs and give us our, some part of the, self-healing software that everyone wants. Yeah. But obviously Cursor has a strong opinion on coding agents and you, you like taking away from the which like obviously you’re going to do, and not every company’s like Cursor, but it’s interesting if you’re a Datadog, like what do you do here?

[00:17:00] Do you expose your logs to FDP and let other people do it? Or do you try to own that it because it’s extra business for you? Yeah. It’s like an interesting one.

**Samantha** [00:17:00] It’s a good question. All I know is that I love the Datadog MCP,

**Jonas** [00:17:00] And yeah, it is gonna be no, no surprise that people like will demand it, right?

**Samantha** [00:17:00] Yeah.

**swyx** [00:17:00] It’s, it’s like any

[00:17:00] system

**swyx** [00:17:00] of record company like this, it’s like how much do you give away? Cool. I think that’s that for the sort of cloud agents tour. Cool. And we just talk about like cloud agents have been when did Kirsten loves cloud agents? Do you know, in June

**Jonas** [00:17:00] last year.

**swyx** [00:17:00] June last year. So it’s been slowly develop the thing you did, like a bunch of, like Michael did a post where himself, where he like showed this chart of like ages overtaking tap. And I’m like, wow, this is like the biggest transition in code.

**Jonas** [00:17:00] Yeah.

**swyx** [00:17:00] Like in, in like the last,

**Jonas** [00:18:00] yeah. I think that kind of got turned out.

[00:18:00] Yeah. I think it’s a very interest,

**swyx** [00:18:00] not at all. I think it’s been highlighted by our friend Andre Kati today.

**Jonas** [00:18:00] Okay.

**swyx** [00:18:00] Talk more about it. What does it mean? Yeah. Is I just got given like the cursor tab key.

**Jonas** [00:18:00] Yes. Yes.

**swyx** [00:18:00] That’s that’s

**Samantha** [00:18:00] cool.

**swyx** [00:18:00] I know, but it’s gonna be like put in a museum.

**Jonas** [00:18:00] It is.

**Samantha** [00:18:00] I have to say I haven’t used tab a little bit myself.

**Jonas** [00:18:00] Yeah. I think that what it looks like to code with AI code generally creates software, even if you want to go higher level. Is changing very rapidly. No, not a hot take, but I think from our vendor’s point at Cursor, I think one of the things that is probably underappreciated from the outside is that we are extremely self-aware about that fact and Kerscher, got its start in phase one, era one of like tab and auto complete.

[00:18:00] And that was really useful in its time. But a lot of people start looking at text files and editing code, like we call it hand coding. Now when you like type out the actual letters, it’s

**swyx** [00:18:00] oh that’s cute.

**Jonas** [00:18:00] Yeah.

**swyx** [00:18:00] Oh that’s cute.

**Jonas** [00:18:00] You’re so boomer. So boomer. And so that I think has been a slowly accelerating and now in the last few months, rapidly accelerating shift.

[00:19:00] And we think that’s going to happen again with the next thing where the, I think some of the pains around tab of it’s great, but I actually just want to give more to the agent and I don’t want to do one tab at a time. I want to just give it a task and it goes off and does a larger unit of work and I can.

[00:19:00] Lean back a little bit more and operate at that higher level of abstraction that’s going to happen again, where it goes from agents handing you back diffs and you’re like in the weeds and giving it, 32nd to three minute tasks, to, you’re giving it, three minute to 30 minute to three hour tasks and you’re getting back videos and trying out previews rather than immediately looking at diffs every single time.

**swyx** [00:19:00] Yeah. Anything to add?

**Samantha** [00:19:00] One other shift that I’ve noticed as our cloud agents have really taken off internally has been a shift from primarily individually driven development to almost this collaborative nature of development for us, slack is actually almost like a development on Id basically.

[00:20:00] So I

**swyx** [00:20:00] like maybe don’t even build a custom ui, like maybe that’s like a debugging thing, but actually it’s that.

**Samantha** [00:20:00] I feel like, yeah, there’s still so much to left to explore there, but basically for us, like Slack is where a lot of development happens. Like we will have these issue channels or just like this product discussion channels where people are always at cursing and that kicks off a cloud agent.

[00:20:00] And for us at least, we have team follow-ups enabled. So if Jonas kicks off at Cursor in a thread, I can follow up with it and add more context. And so it turns into almost like a discussion service where people can like collaborate on ui. Oftentimes I will kick off an investigation and then sometimes I even ask it to get blame and then tag people who should be brought in. ‘cause it can tag people in Slack and then other people will come

**swyx** [00:20:00] in, can tag other people who are not involved in conversation. Yes. Can just do at Jonas if say, was talking to,

**Samantha** [00:20:00] yeah.

**swyx** [00:20:00] That’s cool. You should, you guys should make a big good deal outta that.

**Samantha** [00:20:00] I know. It’s a lot to, I feel like there’s a lot more to do with our slack surface area to show people externally. But yeah, basically like it can bring other people in and then other people can also contribute to that thread and you can end up with a PR again, with the artifacts visible and then people can be like, okay, cool, we can merge this.

[00:21:00] So for us it’s like the ID is almost like moving into Slack in some ways as well.

**swyx** [00:21:00] I have the same experience with, but it’s not developers, it’s me. Designer salespeople.

**Samantha** [00:21:00] Yeah.

**swyx** [00:21:00] So me on like technical marketing, vision, designer on design and then salespeople on here’s the legal source of what we agreed on.

[00:21:00] And then they all just collaborate and correct. The agents,

**Jonas** [00:21:00] I think that we found when these threads is. The work that is left, that the humans are discussing in these threads is the nugget of what is actually interesting and relevant. It’s not the boring details of where does this if statement go?

[00:21:00] It’s do we wanna ship this? Is this the right ux? Is this the right form factor? Yeah. How do we make this more obvious to the user? It’s like those really interesting kind of higher order questions that are so easy to collaborate with and leave the implementation to the cloud agent.

**Samantha** [00:21:00] Totally. And no more discussion of am I gonna do this? Are you gonna do this cursor’s doing it? You just have to decide. You like it.

**swyx** [00:22:00] Sometimes the, I don’t know if there’s a, this probably, you guys probably figured this out already, but since I, you need like a mute button. So like cursor, like we’re going to take this offline, but still online.

[00:22:00] But like we need to talk among the humans first. Before you like could stop responding to everything.

**Jonas** [00:22:00] Yeah. This is a design decision where currently cursor won’t chime in unless you explicitly add Mention it. Yeah. Yeah.

**Samantha** [00:22:00] So it’s not always listening.

[00:22:00] Yeah.

**Jonas** [00:22:00] I can see all the intermediate messages.

**swyx** [00:22:00] Have you done the recursive, can cursor add another cursor or spawn another cursor?

**Samantha** [00:22:00] Oh,

**Jonas** [00:22:00] we’ve done some versions of this.

**swyx** [00:22:00] Because, ‘cause it can add humans.

**Jonas** [00:22:00] Yes. One of the other things we’ve been working on that’s like an implication of generating the code is so easy is getting it to production is still harder than it should be.

[00:22:00] And broadly, you solve one bottleneck and three new ones pop up. Yeah. And so one of the new bottlenecks is getting into production and we have a like joke internally where you’ll be talking about some feature and someone says, I have a PR for that. Which is it’s so easy to get to, I a PR for that, but it’s hard still relatively to get from I a PR for that to, I’m confident and ready to merge this.

[00:23:00] And so I think that over the coming weeks and months, that’s a thing that we think a lot about is how do we scale up compute to that pipeline of getting things from a first draft An agent did.

**swyx** [00:23:00] Isn’t that what Merge isn’t know what graphite’s for, like

**Jonas** [00:23:00] graphite is a big part of that. The cloud agent testing

**swyx** [00:23:00] Is it fully integrated or still different companies

**Jonas** [00:23:00] working on I think we’ll have more to share there in the future, but the goal is to have great end-to-end experience where Cursor doesn’t just help you generate code tokens, it helps you create software end-to-end.

[00:23:00] And so review is a big part of that, that I think especially as models have gotten much better at writing code, generating code, we’ve felt that relatively crop up more,

**swyx** [00:23:00] sorry this is completely unplanned, but like there I have people arguing one to you need ai. To review ai and then there is another approach, thought school of thought where it’s no, reviews are dead.

[00:24:00] Like just show me the video. It’s it like,

**Samantha** [00:24:00] yeah. I feel again, for me, the video is often like alignment and then I often still wanna go through a code review process.

**swyx** [00:24:00] Like still look at the files and

**Samantha** [00:24:00] everything. Yeah. There’s a spectrum of course. Like the video, if it’s really well done and it does like fully like test everything, you can feel pretty competent, but it’s still helpful to, to look at the code.

[00:24:00] I make hep pay a lot of attention to bug bot. I feel like Bug Bot has been a great really highly adopted internally. We often like, won’t we tell people like, don’t leave bug bot comments unaddressed. ‘cause we have such high confidence in it. So people always address their bug bot comments.

**Jonas** [00:24:00] Once you’ve had two cases where you merged something and then you went back later, there was a bug in it, you merged, you went back later and you were like, ah, bug Bot had found that I should have listened to Bug Bot.

[00:24:00] Once that happens two or three times, you learn to wait for bug bot.

**Samantha** [00:24:00] Yeah. So I think for us there’s like that code level review where like it’s looking at the actual code and then there’s like the like feature level review where you’re looking at the features. There’s like a whole number of different like areas.

[00:24:00] There’ll probably eventually be things like performance level review, security review, things like that where it’s like more more different aspects of how this feature might affect your code base that you want to potentially leverage an agent to help with.

**Jonas** [00:25:00] And some of those like bug bot will be synchronous and you’ll typically want to wait on before you merge.

[00:25:00] But I think another thing that we’re starting to see is. As with cloud agents, you scale up this parallelism and how much code you generate. 10 person startups become, need the Devrel X and pipelines that a 10,000 person company used to need. And that looks like a lot of the things I think that 10,000 person companies invented in order to get that volume of software to production safely.

[00:25:00] So that’s things like, release frequently or release slowly, have different stages where you release, have checkpoints, automated ways of detecting regressions. And so I think we’re gonna need stacks merg stack diffs merge queues. Exactly. A lot of those things are going to be important

**swyx** [00:25:00] forward with.

[00:25:00] I think the majority of people still don’t know what stack stacks are. And I like, I have many friends in Facebook and like I, I’m pretty friendly with graphite. I’ve just, I’ve never needed it ‘cause I don’t work on that larger team and it’s just like democratization of no, only here’s what we’ve already worked out at very large scale and here’s how you can, it benefits you too.

[00:26:00] Like I think to me, one of the beautiful things about GitHub is that. It’s actually useful to me as an individual solo developer, even though it’s like actually collaboration software.

**Jonas** [00:26:00] Yep.

**swyx** [00:26:00] And I don’t think a lot of Devrel tools have figured that out yet. That transition from like large down to small.

**Jonas** [00:26:00] Yeah. Kers is probably an inverse story.

**swyx** [00:26:00] This is small down to

**Jonas** [00:26:00] Yeah. Where historically Kers share, part of why we grew so quickly was anyone on the team could pick it up and in fact people would pick it up, on the weekend for their side project and then bring it into work. ‘cause they loved using it so much.

**swyx** [00:26:00] Yeah.

**Jonas** [00:26:00] And I think a thing that we’ve started working on a lot more, not us specifically, but as a company and other folks at Cursor, is making it really great for teams and making it the, the 10th person that starts using Cursor in a team. Is immediately set up with things like, we launched Marketplace recently so other people can configure what CPS and skills like plugins.

[00:27:00] So skills and cps, other people can configure that. So that my cursor is ready to go and set up. Sam loves the Datadog, MCP and Slack, MCP you’ve also been using a lot but

**Samantha** [00:27:00] also pre-launch, but I feel like it’s so good.

**Jonas** [00:27:00] Yeah, my cursor should be configured if Sam feels strongly that’s just amazing and required.

**swyx** [00:27:00] Is it automatically shared or you have to go and.

**Jonas** [00:27:00] It depends on the MCP. So some are obviously off per user. Yeah. And so Sam can’t off my cursor with my Slack MCP, but some are team off and those can be set up by admins.

**swyx** [00:27:00] Yeah. Yeah. That’s cool. Yeah, I think, we had a man on the pod when cursor was five people, and like everyone was like, okay, what’s the thing?

[00:27:00] And then it’s usually something teams and org and enterprise, but it’s actually working. But like usually at that stage when you’re five, when you’re just a vs. Code fork it’s like how do you get there? Yeah. Will people pay for this? People do pay for it.

**Jonas** [00:27:00] Yeah. And I think for cloud agents, we expect.

[00:28:00] To have similar kind of PLG things where I think off the bat we’ve seen a lot of adoption with kind of smaller teams where the code bases are not quite as complex to set up. Yes. If you need some insane docker layer caching thing for builds not to take two hours, that’s going to take a little bit longer for us to be able to support that kind of infrastructure.

[00:28:00] Whereas if you have front end backend, like one click agents can install everything that they need themselves.

**swyx** [00:28:00] This is a good chance for me to just ask some technical sort of check the box questions. Can I choose the size of the vm?

**Jonas** [00:28:00] Not yet. We are planning on adding that. We

**swyx** [00:28:00] have, this is obviously you want like LXXL, whatever, right?

[00:28:00] Like it’s like the Amazon like sort menu.

**Jonas** [00:28:00] Yes, exactly. We’ll add that.

**swyx** [00:28:00] Yeah. In some ways you have to basically become like a EC2, almost like you rent a box.

**Jonas** [00:28:00] You rent a box. Yes. We talk a lot about brain in a box. Yeah. So cursor, we want to be a brain in a box,

**swyx** [00:28:00] but is the mental model different? Is it more serverless?

[00:28:00] Is it more persistent? Is. Something else.

**Samantha** [00:28:00] We want it to be a bit persistent. The desktop should be something you can return to af even after some days. Like maybe you go back, they’re like still thinking about a feature for some period of time. So the

**swyx** [00:29:00] full like sus like suspend the memory and bring it back and then keep going.

**Samantha** [00:29:00] Exactly.

**swyx** [00:29:00] That’s an interesting one because what I actually do want, like from a manna and open crawl, whatever, is like I want to be able to log in with my credentials to the thing, but not actually store it in any like secret store, whatever. ‘cause it’s like this is the, my most sensitive stuff.

[00:29:00] Yeah. This is like my email, whatever. And just have it like, persist to the image. I don’t know how it was hood, but like to rehydrate and then just keep going from there. But I don’t think a lot of infra works that way. A lot of it’s stateless where like you save it to a docker image and then it’s only whatever you can describe in a Docker file and that’s it.

[00:29:00] That’s the only thing you can cl multiple times in parallel.

**Jonas** [00:29:00] Yeah. We have a bunch of different ways of setting them up. So there’s a dockerfile based approach. The main default way is actually snapshotting

**swyx** [00:29:00] like a Linux vm

**Jonas** [00:29:00] like vm, right? You run a bunch of install commands and then you snapshot more or less the file system.

[00:29:00] And so that gets you set up for everything that you would want to bring a new VM up from that template basically.

**swyx** [00:30:00] Yeah.

**Jonas** [00:30:00] And that’s a bit distinct from what Sam was talking about with the hibernating and re rehydrating where that is a full memory snapshot as well. So there, if I had like the browser open to a specific page and we bring that back, that page will still be there.

**swyx** [00:30:00] Was there any discussion internally and just building this stuff about every time you shoot a video it’s actually you show a little bit of the desktop and the browser and it’s not necessary if you just show the browser. If, if you know you’re just demoing a front end application.

[00:30:00] Why not just show the browser, right? Like it Yeah,

**Samantha** [00:30:00] we do have some panning and zooming. Yeah. Like it can decide that when it’s actually recording and cutting the video to highlight different things. I think we’ve played around with different ways of segmenting it and yeah. There’s been some different revs on it for sure.

**Jonas** [00:30:00] Yeah. I think one of the interesting things is the version that you see now in cursor.com actually is like half of what we had at peak where we decided to unshift or unshipped quite a few things. So two of the interesting things to talk about, one is directly an answer to your question where we had native browser that you would have locally, it was basically an iframe that via port forwarding could load the URL could talk to local host in the vm.

[00:31:00] So that gets you basically, so in

**swyx** [00:31:00] your machine’s browser,

[00:31:00] like

**Jonas** [00:31:00] in your local browser? Yeah. You would go to local host 4,000 and that would get forwarded to local host 4,000 in the VM via port forward. We unshift that like at

**swyx** [00:31:00] Eng Rock.

**Jonas** [00:31:00] Like an Eng Rock. Exactly. We unshift that because we felt that the remote desktop was sufficiently low latency and more general purpose.

[00:31:00] So we build Cursor web, but we also build Cursor desktop. And so it’s really useful to be able to have the full spectrum of things. And even for Cursor Web, as you saw in one of the examples, the agent was uploading files and like I couldn’t upload files and open the file viewer if I only had access to the browser.

[00:31:00] And we’ve thought a lot about, this might seem funny coming from Cursor where we started as this, vs. Code Fork and I think inherited a lot of amazing things, but also a lot of legacy UI from VS Code.

## Minimal Web UI Surfaces

**Jonas** [00:32:00] And so with the web UI we wanted to be very intentional about keeping that very minimal and exposing the right sum of set of primitive sort of app surfaces we call them, that are shared features of that cloud.

[00:32:00] Environment that you and the agent both use. So agent uses desktop and controls it. I can use desktop and controlled agent runs terminal commands. I can run terminal commands. So that’s how our philosophy around it. The other thing that is maybe interesting to talk about that we unshipped is and we may, both of these things we may reship and decide at some point in the future that we’ve changed our minds on the trade offs or gotten it to a point where, put

**swyx** [00:32:00] it out there.

[00:32:00] Let users tell you they want it. Exactly. Alright, fine.

## Why No File Editor

**Jonas** [00:32:00] So one of the other things is actually a files app. And so we used to have the ability at one point during the process of testing this internally to see next to, I had GID desktop and terminal on the right hand side of the tab there earlier to also have a files app where you could see and edit files.

[00:32:00] And we actually felt that in some ways, by restricting and limiting what you could do there, people would naturally leave more to the agent and fall into this new pattern of delegating, which we thought was really valuable. And there’s currently no way in Cursor web to edit these files.

**swyx** [00:33:00] Yeah. Except you like open up the PR and go into GitHub and do the thing.

**Jonas** [00:33:00] Yeah.

**swyx** [00:33:00] Which is annoying.

**Jonas** [00:33:00] Just tell the agent,

**swyx** [00:33:00] I have criticized open AI for this. Because Open AI is Codex app doesn’t have a file editor, like it has file viewer, but isn’t a file editor.

**Jonas** [00:33:00] Do you use the file viewer a lot?

**swyx** [00:33:00] No. I understand, but like sometimes I want it, the one way to do it is like freaking going to no, they have a open in cursor button or open an antigravity or, opening whatever and people pointed that.

[00:33:00] So I was, I was part of the early testers group people pointed that and they were like, this is like a design smell. It’s like you actually want a VS. Code fork that has all these things, but also a file editor. And they were like, no, just trust us.

**Jonas** [00:33:00] Yeah. I think we as Cursor will want to, as a product, offer the whole spectrum and so you want to be able to.

[00:34:00] Work at really high levels of abstraction and double click and see the lowest level. That’s important. But I also think that like you won’t be doing that in Slack. And so there are surfaces and ways of interacting where in some cases limiting the UX capabilities makes for a cleaner experience that’s more simple and drives people into these new patterns where even locally we kicked off joking about this.

[00:34:00] People like don’t really edit files, hand code anymore. And so we want to build for where that’s going and not where it’s been

**swyx** [00:34:00] a lot of cool stuff. And Okay. I have a couple more.

## Full Stack Hosting Debate

**swyx** [00:34:00] So observations about the design elements about these things. One of the things that I’m always thinking about is cursor and other peers of cursor start from like the Devrel tools and work their way towards cloud agents.

[00:34:00] Other people, like the lovable and bolts of the world start with here’s like the vibe code. Full cloud thing. They were already cloud edges before anyone else cloud edges and we will give you the full deploy platform. So we own the whole loop. We own all the infrastructure, we own, we, we have the logs, we have the the live site, whatever.

[00:35:00] And you can do that cycle cursor doesn’t own that cycle even today. You don’t have the versal, you don’t have the, you whatever deploy infrastructure that, that you’re gonna have, which gives you powers because anyone can use it. And any enterprise who, whatever you infra, I don’t care. But then also gives you limitations as to how much you can actually fully debug end to end.

[00:35:00] I guess I’m just putting out there that like is there a future where there’s like full stack cursor where like cursor apps.com where like I host my cursor site this, which is basically a verse clone, right? I don’t know.

**Jonas** [00:35:00] I think that’s a interesting question to be asking, and I think like the logic that you laid out for how you would get there is logic that I largely agree with.

**swyx** [00:35:00] Yeah. Yeah.

**Jonas** [00:35:00] I think right now we’re really focused on what we see as the next big bottleneck and because things like the Datadog MCP exist, yeah. I don’t think that the best way we can help our customers ship more software. Is by building a hosting solution right now,

**swyx** [00:35:00] by the way, these are things I’ve actually discussed with some of the companies I just named.

**Jonas** [00:35:00] Yeah, for sure. Right now, just this big bottleneck is getting the code out there and also unlike a lovable in the bolt, we focus much more on existing software. And the zero to one greenfield is just a very different problem. Imagine going to a Shopify and convincing them to deploy on your deployment solution.

[00:36:00] That’s very different and I think will take much longer to see how that works. May never happen relative to, oh, it’s like a zero to one app.

**swyx** [00:36:00] I’ll say. It’s tempting because look like 50% of your apps are versal, superb base tailwind react it’s the stack. It’s what everyone does.

[00:36:00] So I it’s kinda interesting.

**Jonas** [00:36:00] Yeah.

## Model Choice and Auto Routing

**swyx** [00:36:00] The other thing is the model select dying. Right now in cloud agents, it’s stuck down, bottom left. Sure it’s Codex High today, but do I care if it’s suddenly switched to Opus? Probably not.

**Samantha** [00:36:00] We definitely wanna give people a choice across models because I feel like it, the meta change is very frequently.

[00:36:00] I was a big like Opus 4.5 Maximalist, and when codex 5.3 came out, I hard, hard switch. So that’s all I use now.

**swyx** [00:36:00] Yeah. Agreed. I don’t know if, but basically like when I use it in Slack, right? Cursor does a very good job of exposing yeah. Cursors. If people go use it, here’s the model we’re using.

[00:37:00] Yeah. Here’s how you switch if you want. But otherwise it’s like extracted away, which is like beautiful because then you actually, you should decide.

**Jonas** [00:37:00] Yeah, I think we want to be doing more with defaults.

**swyx** [00:37:00] Yeah.

**Jonas** [00:37:00] Where we can suggest things to people. A thing that we have in the editor, the desktop app is auto, which will route your request and do things there.

[00:37:00] So I think we will want to do something like that for cloud agents as well. We haven’t done it yet. And so I think. We have both people like Sam, who are very savvy and want know exactly what model they want, and we also have people that want us to pick the best model for them because we have amazing people like Sam and we, we are the experts.

[00:37:00] Yeah. We have both the traffic and the internal taste and experience to know what we think is best.

**swyx** [00:37:00] Yeah. I have this ongoing pieces of agent lab versus model lab. And to me, cursor and other companies are example of an agent lab that is, building a new playbook that is different from a model lab where it’s like very GP heavy Olo.

[00:37:00] So obviously has a research team. And my thesis is like you just, every agent lab is going to have a router because you’re going to be asked like, what’s what. I don’t keep up to every day. I’m not a Sam, I don’t keep up every day for using you as sample the arm arbitrator of taste. Put me on CRI Auto.

[00:38:00] Is it free? It’s not free.

**Jonas** [00:38:00] Auto’s not free, but there’s different pricing tiers. Yeah.

**swyx** [00:38:00] Put me on Chris. You decide from me based on all the other people you know better than me. And I think every agent lab should basically end up doing this because that actually gives you extra power because you like people stop carrying or having loyalty with one lab.

**Jonas** [00:38:00] Yeah.

## Best Of N and Model Councils

**Jonas** [00:38:00] Two other maybe interesting things that I don’t know how much they’re on your radar are one the best event thing we mentioned where running different models head to head is actually quite interesting because

**swyx** [00:38:00] which exists in cursor.

**Jonas** [00:38:00] That exists in cur ID and web. So the problem is where do you run them?

**swyx** [00:38:00] Okay.

**Jonas** [00:38:00] And so I, I can share my screen if that’s interesting. Yeahinteresting.

**swyx** [00:38:00] Yeah. Yeah. Obviously parallel agents, very popal.

**Jonas** [00:38:00] Yes, exactly. Parallel agents

**swyx** [00:38:00] in you mind. Are they the same thing? Best event and parallel agents? I don’t want to put words in your mouth.

**Jonas** [00:39:00] Best event is a subset of parallel agents where they’re running on the same prompt.

[00:39:00] That would be my answer. So this is what that looks like. And so here in this dropdown picker, I can just select multiple models.

**swyx** [00:39:00] Yeah.

**Jonas** [00:39:00] And now if I do a prompt, I’m going to do something silly. I am running these five models.

**swyx** [00:39:00] Okay. This is this fake clone, of course. The 2.0 yeah.

**Jonas** [00:39:00] Yes, exactly. But they’re running so the cursor 2.0, you can do desktop or cloud.

[00:39:00] So this is cloud specifically where the benefit over work trees is that they have their own VMs and can run commands and won’t try to kill ports that the other one is running. Which are some of the pains. These are all

**swyx** [00:39:00] called work trees?

**Jonas** [00:39:00] No, these are all cloud agents with their own VMs.

**swyx** [00:39:00] Okay. But

**Jonas** [00:39:00] When you do it locally, sometimes people do work trees and that’s been the main way that people have set out parallel so far.

[00:39:00] I’ve gotta say.

**swyx** [00:39:00] That’s so confusing for folks.

**Jonas** [00:39:00] Yeah.

**swyx** [00:39:00] No one knows what work trees are.

**Jonas** [00:39:00] Exactly. I think we’re phasing out work trees.

**swyx** [00:39:00] Really.

**Jonas** [00:39:00] Yeah.

**swyx** [00:39:00] Okay.

**Samantha** [00:39:00] But yeah. And one other thing I would say though on the multimodel choice, so this is another experiment that we ran last year and the decide to ship at that time but may come back to, and there was an interesting learning that’s relevant for, these different model providers. It was something that would run a bunch of best of ends but then synthesize and basically run like a synthesizer layer of models. And that was other agents that would take LM Judge, but one that was also agentic and could write code. So it wasn’t just picking but also taking the learnings from two models or, and models that it was looking at and writing a new diff.

[00:40:00] And what we found was that at the time at least, there were strengths to using models from different model providers as the base level of this process. Like basically you could get almost like a synergistic output that was better than having a very unified, like bottom model tier. So it was really interesting ‘cause it’s like potentially, even though even in the future when you have like maybe one model as ahead of the other for a little bit, there could be some benefit from having like multiple top tier models involved in like a model swarm or whatever agent Swarm that you’re doing, that they each have strengths and weaknesses.

[00:41:00] Yeah.

**Jonas** [00:41:00] Andre called this the council, right?

**Samantha** [00:41:00] Yeah, exactly. We actually, oh, that’s another internal command we have that Ian wrote slash council. Oh, and they some, yeah.

**swyx** [00:41:00] Yes. This idea is in various forms everywhere. And I think for me, like for me, the productization of it, you guys have done yeah, like this is very flexible, but.

[00:41:00] If I were to add another Yeah, what your thing is on here it would be too much. I what, let’s say,

**Samantha** [00:41:00] Ideally it’s all, it’s something that the user can just choose and it all happens under the hood in a way where like you just get the benefit of that process at the end and better output basically, but don’t have to get too lost in the complexity of judging along the way.

**Jonas** [00:41:00] Okay.

## Subagents for Context

**Jonas** [00:41:00] Another thing on the many agents, on different parallel agents that’s interesting is an idea that’s been around for a while as well that has started working recently is subagents. And so this is one other way to get agents of the different prompts and different goals and different models, different vintages to work together.

[00:42:00] Collaborate and delegate.

**swyx** [00:42:00] Yeah. I’m very like I like one of my, I always looking for this is the year of the blah, right? Yeah. I think one of the things on the blahs is subs. I think this is of but I haven’t used them in cursor. Are they fully formed or how do I honestly like an intro because do I form them from new every time?

[00:42:00] Do I have fixed subagents? How are they different for slash commands? There’s all these like really basic questions that no one stops to answer for people because everyone’s just like too busy launching. We have to

**Samantha** [00:42:00] honestly, you could, you can see them in cursor now if you just say spin up like 50 subagents to, so cursor defines

**swyx** [00:42:00] what Subagents.

[00:42:00] Yeah.

**Samantha** [00:42:00] Yeah. So basically I think I shouldn’t speak for the whole subagents team. This is like a different team that’s been working on this, but our thesis or thing that we saw internally is that like they’re great for context management for kind of long running threads, or if you’re trying to just throw more compute at something.

[00:42:00] We have strongly used, almost like a generic task interface where then the main agent can define like what goes into the subagent. So if I say explore my code base, it might decide to spin up an explore subagent and or might decide to spin up five explore subagent.

**swyx** [00:43:00] But I don’t get to set what those subagent are, right?

[00:43:00] It’s all defined by a model.

**Samantha** [00:43:00] I think. I actually would have to refresh myself on the sub agent interface.

**Jonas** [00:43:00] There are some built-in ones like the explore subagent is free pre-built. But you can also instruct the model to use other subagents and then it will. And one other example of a built-in subagent is I actually just kicked one off in cursor and I can show you what that looks like.

**swyx** [00:43:00] Yes. Because I tried to do this in pure prompt space.

**Jonas** [00:43:00] So this is the desktop app? Yeah. Yeah. And that’s

**swyx** [00:43:00] all you need to do, right? Yeah.

**Jonas** [00:43:00] That’s all you need to do. So I said use a sub agent to explore and I think, yeah, so I can even click in and see what the subagent is working on here. It ran some fine command and this is a composer under the hood.

[00:43:00] Even though my main model is Opus, it does smart routing to take, like in this instance the explorer sort of requires reading a ton of things. And so a faster model is really useful to get an answer quickly, but that this is what subagent look like. And I think we wanted to do a lot more to expose hooks and ways for people to configure these.

[00:44:00] Another example of a cus sort of builtin subagent is the computer use subagent in the cloud agents, where we found that those trajectories can be long and involve a lot of images obviously, and execution of some testing verification task. We wanted to use that models that are particularly good at that.

[00:44:00] So that’s one reason to use subagents. And then the other reason to use subagents is we want contexts to be summarized reduced down at a subagent level. That’s a really neat boundary at which to compress that rollout and testing into a final message that agent writes that then gets passed into the parent rather than having to do some global compaction or something like that.

**swyx** [00:44:00] Awesome. Cool. While we’re in the subagents conversation, I can’t do a cursor conversation and not talk about listen stuff. What is that? What is what? He built a browser. He built an os. Yes. And he experimented with a lot of different architectures and basically ended up reinventing the software engineer org chart.

[00:45:00] This is all cool, but what’s your take? What’s, is there any hole behind the side? The scenes stories about that kind of, that whole adventure.

**Samantha** [00:45:00] Some of those experiments have found their way into a feature that’s available in cloud agents now, the long running agent mode internally, we call it grind mode.

[00:45:00] And I think there’s like some hint of grind mode accessible in the picker today. ‘cause you can do choose grind until done. And so that was really the result of experiments that Wilson started in this vein where he I think the Ralph Wigga loop was like floating around at the time, but it was something he also independently found and he was experimenting with.

[00:45:00] And that was what led to this product surface.

**swyx** [00:45:00] And it is just simple idea of have criteria for completion and do not. Until you complete,

**Samantha** [00:45:00] there’s a bit more complexity as well in, in our implementation. Like there’s a specific, you have to start out by aligning and there’s like a planning stage where it will work with you and it will not get like start grind execution mode until it’s decided that the plan is amenable to both of you.

[00:46:00] Basically,

**swyx** [00:46:00] I refuse to work until you make me happy.

**Jonas** [00:46:00] We found that it’s really important where people would give like very underspecified prompt and then expect it to come back with magic. And if it’s gonna go off and work for three minutes, that’s one thing. When it’s gonna go off and work for three days, probably should spend like a few hours upfront making sure that you have communicated what you actually want.

**swyx** [00:46:00] Yeah. And just to like really drive from the point. We really mean three days that No, no

**Jonas** [00:46:00] human. Oh yeah. We’ve had three day months innovation whatsoever.

**Samantha** [00:46:00] I don’t know what the record is, but there’s been a long time with the grants

**Jonas** [00:46:00] and so the thing that is available in cursor. The long running agent is if you wanna think about it, very abstractly that is like one worker node.

[00:46:00] Whereas what built the browser is a society of workers and planners and different agents collaborating. Because we started building the browser with one worker node at the time, that was just the agent. And it became one worker node when we realized that the throughput of the system was not where it needed to be to get something as large of a scale as the browser done.

**swyx** [00:47:00] Yeah.

**Jonas** [00:47:00] And so this has also become a really big mental model for us with cloud, cloud agents is there’s the classic engineering latency throughput trade-offs. And so you know, the code is water flowing through a pipe. The, we think that over the coming months, the big unlock is not going to be one person with a model getting more done, like the water flowing faster and we’ll be making the pipe much wider and so ing more, whether that’s swarms of agents or parallel agents, both of those are things that contribute to getting.

[00:47:00] Much more done in the same amount of time, but any one of those tasks doesn’t necessarily need to get done that quickly. And throughput is this really big thing where if you see the system of a hundred concurrent agents outputting thousands of tokens a second, you can’t go back like that.

[00:47:00] Just you see a glimpse of the future where obviously there are many caveats. Like no one is using this browser. IRL. There’s like a bunch of things not quite right yet, but we are going to get to systems that produce real production code at the scale much sooner than people think. And it forces you to think what even happens to production systems. Like we’ve broken our GitHub actions recently because we have so many agents like producing and pushing code that like CICD is just overloaded. ‘cause suddenly it’s like effectively weg grew, cursor’s growing very quickly anyway, but you grow head count, 10 x when people run 10 x as many agents.

[00:48:00] And so a lot of these systems, exactly, a lot of these systems will need to adapt.

**swyx** [00:48:00] It also reminds me, we, we all, the three of us live in the app layer, but if you talk to the researchers who are doing RL infrastructure, it’s the same thing. It’s like all these parallel rollouts and scheduling them and making sure as much throughput as possible goes through them.

[00:48:00] Yeah, it’s the same thing.

**Jonas** [00:48:00] We were talking briefly before we started recording. You were mentioning memory chips and some of the shortages there. The other thing that I think is just like hard to wrap your head around the scale of the system that was building the browser, the concurrency there.

[00:48:00] If Sam and I both have a system like that running for us, shipping our software. The amount of inference that we’re going to need per developer is just really mind-boggling. And that makes, sometimes when I think about that, I think that even with, the most optimistic projections for what we’re going to need in terms of buildout, our underestimating, the extent to which these swarm systems can like churn at scale to produce code that is valuable to the economy.

[00:49:00] And,

**swyx** [00:49:00] yeah, you can cut this if it’s sensitive, but I was just Do you have estimates of how much your token consumption is?

**Jonas** [00:49:00] Like per developer?

**swyx** [00:49:00] Yeah. Or yourself. I don’t need like comfy average. I just curious. I

**Samantha** [00:49:00] feel like I, for a while I wasn’t an admin on the usage dashboard, so I like wasn’t able to actually see, but it was a,

**swyx** [00:49:00] mine has gone up.

**Samantha** [00:49:00] Oh yeah.

**swyx** [00:49:00] But I think

**Samantha** [00:49:00] it’s in terms of how much work I’m doing, it’s more like I have no worries about developers losing their jobs, at least in the near term. ‘cause I feel like that’s a more broad discussion.

**swyx** [00:49:00] Yeah. Yeah. You went there. I didn’t go, I wasn’t going there.

[00:49:00] I was just like how much more are you using?

**Samantha** [00:49:00] There’s so much stuff to be built. And so I feel like I’m basically just trying to constantly I have more ambitions than I did before. Yes. Personally. Yes. So can’t speak to the broader thing. But for me it’s like I’m busier than ever before.

[00:50:00] I’m using more tokens and I am also doing more things.

**Jonas** [00:50:00] Yeah. Yeah. I don’t have the stats for myself, but I think broadly a thing that we’ve seen, that we expect to continue is J’S paradox. Where

**swyx** [00:50:00] you can’t do it in our podcast without seeing

**Jonas** [00:50:00] it. Exactly. We’ve done it. Now we can wrap. We’ve done, we said the words.

[00:50:00] Phase one tab auto complete people paid like 20 bucks a month. And that was great. Phase two where you were iterating with these local models. Today people pay like hundreds of dollars a month. I think as we think about these highly parallel kind of agents running off for a long times in their own VM system, we are already at that point where people will be spending thousands of dollars a month per human, and I think potentially tens of thousands and beyond, where it’s not like we are greedy for like capturing more money, but what happens is just individuals get that much more leverage.

[00:50:00] And if one person can do as much as 10 people, yeah. That tool that allows ‘em to do that is going to be tremendously valuable and worth investing in and taking the best thing that exists.

**swyx** [00:51:00] One more question on just the cursor in general and then open-ended for you guys to plug whatever you wanna put.

[00:51:00] How is Cursor hiring these days?

**Samantha** [00:51:00] What do you mean by how?

**swyx** [00:51:00] So obviously lead code is dead. Oh,

**Samantha** [00:51:00] okay.

**swyx** [00:51:00] Everyone says work trial. Different people have different levels of adoption of agents. Some people can really adopt can be much more productive. But other people, you just need to give them a little bit of time.

[00:51:00] And sometimes they’ve never lived in a token rich place like cursor.

[00:51:00] And once you live in a token rich place, you’re you just work differently. But you need to have done that. And a lot of people anyway, it was just open-ended. Like how has agentic engineering, agentic coding changed your opinions on hiring?

[00:51:00] Is there any like broad like insights? Yeah.

**Jonas** [00:51:00] Basically I’m asking this for other people, right? Yeah, totally. Totally. To hear Sam’s opinion, we haven’t talked about this the two of us. I think that we don’t see necessarily being great at the latest thing with AI coding as a prerequisite.

[00:51:00] I do think that’s a sign that people are keeping up and curious and willing to upscale themselves in what’s happening because. As we were talking about the last three months, the game has completely changed. It’s like what I do all day is very different.

**swyx** [00:52:00] Like it’s my job and I can’t,

**Jonas** [00:52:00] Yeah, totally.

[00:52:00] I do think that still as Sam was saying, the fundamentals remain important in the current age and being able to go and double click down. And models today do still have weaknesses where if you let them run for too long without cleaning up and refactoring, the coke will get sloppy and there’ll be bad abstractions.

[00:52:00] And so you still do need humans that like have built systems before, no good patterns when they see them and know where to steer things.

**Samantha** [00:52:00] I would agree with that. I would say again, cursor also operates very quickly and leveraging ag agentic engineering is probably one reason why that’s possible in this current moment.

[00:52:00] I think in the past it was just like people coding quickly and now there’s like people who use agents to move faster as well. So it’s part of our process will always look for we’ll select for kind of that ability to make good decisions quickly and move well in this environment.

[00:52:00] And so I think being able to figure out how to use agents to help you do that is an important part of it too.

**swyx** [00:53:00] Yeah. Okay. The fork in the road, either predictions for the end of the year, if you have any, or PUDs.

**Jonas** [00:53:00] Evictions are not going to go well.

**Samantha** [00:53:00] I know it’s hard.

**swyx** [00:53:00] They’re so hard. Get it wrong.

[00:53:00] It’s okay. Just, yeah.

**Jonas** [00:53:00] One other plug that may be interesting that I feel like we touched on but haven’t talked a ton about is a thing that the kind of these new interfaces and this parallelism enables is the ability to hop back and forth between threads really quickly. And so a thing that we have,

**swyx** [00:53:00] you wanna show something or,

**Jonas** [00:53:00] yeah, I can show something.

[00:53:00] A thing that we have felt with local agents is this pain around contact switching. And you have one agent that went off and did some work and another agent that, that did something else. And so here by having, I just have three tabs open, let’s say, but I can very quickly, hop in here.

[00:53:00] This is an example I showed earlier, but the actual workflow here I think is really different in a way that may not be obvious, where, I start the morning, I kick off 10 agents or something, the first one of them finishes, come in, watch the video either as close. And so I might send a follow up.

[00:54:00] I might say, Hey, make it red, or I might hop into the desktop and try it out. And within, 90, 120 seconds, I’ve kicked this one back off. And either started the merge process like CI is running now and I’ll come back to it later or it’s off with some additional follow up information. And then I can hop into the next one.

[00:54:00] And then the next one I hop in and I’m like, okay, this looks interesting. Actually try it out for real in the app. I want to see it in action, not just in the gallery. So I can kick that off and the agent will go and work on that because maybe I wanted to try it out, like what the button looks like in the actual thing.

[00:54:00] And then here I might hop in as well and, check the video here or do something. And so you’re really parallelizing much more and follow up here, check in there. It’s much more this higher level of abstraction and having the different desktops where you can hop back and forth and you’re not like, oh, I checked out this branch.

[00:55:00] Oh, where was that work tree again? Yeah. It’s really like solving for that which we’ve ourselves have struggled with in cursor and these local agents to be like, where was that diff again? It’s lost in some work tree. Never gonna find it. Oh, my local thing is rebuilding. Oh, just make another one.

[00:55:00] That, that’s what you end up with and then you wait for five more minutes for it to run. And so this is really like a new way of just paralleling that we found to be really fun, honestly. Yeah. Where you’re just hopping in and injecting taste and you’re like that doesn’t quite feel right.

[00:55:00] Oh, actually this is not architected quite right, but you’re just focusing on those like taste interesting questions.

**Samantha** [00:55:00] For me, the cloud ecosystem too also enabled this to be like, something that is like adding productivity to my dead time, like commuting or like overnight or something like that.

[00:55:00] The fact that I don’t have to leave my computer open,

**swyx** [00:55:00] there’s no cursor, there is a cursor mobile app.

**Samantha** [00:55:00] If there is, I’m not sure. It’s like the current thing. We, I use it on my phone all the time, just on the web. So pretty good experience there for checking in. Yeah. And un unlocking. I think, yeah. You can see the videos and stuff in the web app, which is awesome.

[00:56:00] Yeah.

**Jonas** [00:56:00] Yeah.

**swyx** [00:56:00] I think this is one that the a DD one inherited the earth, like the, if you’re like, your attention span is cooked, but you still can manage, like actually this is good for you. Yeah. But also I think this is where the coding tools start coming into conflict with the productivity tools where like the linear the canman boards, because what you have there is cool, but you know what, you actually need a cabin board. Which people have vibe, vibe, cam, van is out there. Open source. I’m sure you guys have talked about it, but we’ll start to conflict because actually the code doesn’t matter anymore.

[00:56:00] It’s the process of the human interacting and checking in. And seeing, like getting the world of warcrafts sound package to go like work or whatever. It’s like job done or, I don’t know. It’s like an interesting like future productivity thing.

**Samantha** [00:56:00] Yeah.

**swyx** [00:56:00] I also think like another big theme like last year li is called like the, your coding agents.

[00:56:00] This year another like coding agents spill over to the real world into cloud cowork and all the other stuff. Yeah. I’m sure cursor’s gonna focus on software, but let’s call it like open claw is like extremely mind expanding in terms of I did not know that could happen.

**Jonas** [00:57:00] Yeah.

**swyx** [00:57:00] And it’s all based on a coding agent based totally.

**Jonas** [00:57:00] And I think one of the things that like talking to, friends and family that are not in the software world that’s interesting is I do. Speeding up predictions. I do think that we are going to start seeing other industries go through what software development has started going through.

[00:57:00] I think by virtue of how good models are at writing software and how early adopter the people building the new technology are and trying it out and applying it to themselves, that’s certain kinds of shifts will happen too to other industries. And there’s a lot to be learned from how that’s gone down and is continuing to go down in software.

[00:57:00] In terms of, all the interesting questions about to what point do people get more leverage, when do you start changing the role to become much more generalist? Like, all of these questions that we’ve seen some data on, but we’ll see a lot more in the coming months. That will happen everywhere.

**swyx** [00:57:00] Sammy party thoughts? Any flus of your own?

**Samantha** [00:57:00] Not really. It’s fine. I feel we covered so much good draft. We covered it. We covered a lot. Coming up with a prediction. I just think agents are gonna keep getting better. Gonna stop doing as much manual coding, probably zero lines of code written in the whole month of December this year by myself.

[00:58:00] A hundred percent agents as a personal prediction, but

**swyx** [00:58:00] oh, you’re not as zero today.

[00:58:00] What in what cases?

**Samantha** [00:58:00] I think honestly, it’s 1% if I like, just am like, get frustrated and I’m like, I don’t wanna go have it tell an agent to change this one thing. But

**Jonas** [00:58:00] prompting sometimes I feel like working on prompts sometimes.

[00:58:00] Yeah. I still go in and manually edit because it’s so like bare intent transfer that like telling the agent what I want. It’s like writing an essay where I don’t use agents to write essays yet because the process of writing it is the thinking.

**Samantha** [00:58:00] I still can’t stand AI generated writing. So yeah, I can also can’t have the agent write prompts.

**swyx** [00:58:00] So no D Spy, no jpa, nothing like that here.

**Jonas** [00:58:00] We have some internal tooling around some of the prompt optimization things, but there’s a fair amount of just what concepts do I need to communicate to the agent or the model.

**swyx** [00:58:00] I also noticed another thing I’m also looking for is voice.

[00:59:00] I noticed that you didn’t use your voice to code even open ai. When we do podcasts with them, they don’t use their voice. Yeah. And I’m like at some point this gets good. You can stop typing.

**Samantha** [00:59:00] We have some people who like that a lot internally, and I think we’ll be experimenting in that space too, for sure.

**Jonas** [00:59:00] Do you use voice log?

**swyx** [00:59:00] Not a lot. Sometimes that’s bound to my caps log, so I can press it. I just,

**Jonas** [00:59:00] and when you use it, do you want it to talk back or you just want

**swyx** [00:59:00] Yeah,

**Jonas** [00:59:00] just dump in. Yeah. Yeah.

**swyx** [00:59:00] But like the brain dump is good. Yeah. Because you can interrupt yourself. You can go on a tangent, whatever.

[00:59:00] It just captures everything. Yeah. And lop it into all m, it’s fine.

**Jonas** [00:59:00] Yeah. The way that we did this with Auto Tab was people would record full screen recordings with audio to teach the model, like how to do a task. And one of the funny things that we learned was people would use their Siri voice, where they would start talking in like short, stilted sentences and enunciate really clearly because they were used to, they last used AI two years ago where you had to

**swyx** [00:59:00] apple has damaged like an entire generation of people’s expectations.

**Jonas** [00:59:00] Exactly. And we had to be like, no you’re very native, so you do this, but just dump everything in. You can say you can repeat yourself. You can contradict yourself. The models are smart enough to figure it out,

**swyx** [01:00:00] but it’s still very bad. So voice coding was always, I considered like the hardest part because you have to say like technical things that pel like spelling matters, capitalization matters and like it’s all not in voice.

[01:00:00] So we’ll see. So far it’s been more sort of emotional companionship, that kind of stuff, but at some point it’s gonna hit voice coding.

**Jonas** [01:00:00] Yeah. I have a prediction for you. I predict that by the end of the year, the volume on, I think it will take longer than people think and longer than we think for cloud and agents working in their own boxes to surpass local agents.

[01:00:00] But I think that crossover will happen before the end of the year and probably by the end of the year, agents running in the cloud will be a multi, like more than two x the volume of local agents.

**swyx** [01:00:00] Okay. You’re leaving me an opening. What’s not good today?

**Jonas** [01:00:00] Yeah, there’s a bunch of hard things. So one of them is just getting those sandboxes to be really good and a thing that was part of this launch that we spend in inordinate amount of time on is cursor.com/onboard where you pick a repo, add secrets, give it access to things, and the agent just goes off and installs things.

**swyx** [01:01:00] Yes, I think all the whole thing. That was my favorite.

**Jonas** [01:01:00] Yeah, we worked a lot on that. Sam and I in particular spent a lot of late nights making that good, but there’s still a lot to do there, right? Set up 1, 2, 2 things. Maybe it’s too slow. It’s too slow. Working on it set up is not like a unitary thing where everything is set up or not, right?

[01:01:00] Like things will break over time. You have new dependencies, you need access to new systems, like you change where your database lives. So that’s one part of it. And then the other part of it is, having these agents run in the cloud and be more autonomous. We’ve really started to see the lack of memory.

[01:01:00] And Sam, as someone who’s thought a lot about this once you start getting the model kind of doing, operating the code base, there’s more particularities that are not it’s not just a read file tool. It needs to know how do I start up the backend, how do I check the status of the backend?

[01:02:00] That’s very particular to your code base. And even if it’s great at NPM Run watch or whatever the default things are, there’s always quirks. Everyone has quirks. And getting the model good at those things will require more work. And we’re working on that. But we think that will be one of the big unlocks, is having them be onboarded not only in terms of their environment, but also in terms of their understanding of design trade-offs, how the code base works, how to be a good developer in any one code base.

**swyx** [01:02:00] It’s lot crier rules. It’s gonna be something else. Is it gonna be a file? Is it. We just call in either markdown file a different name, and

**Samantha** [01:02:00] I don’t know. One thing that we learned at, could we be in cursor of the company this year? There, there’s a really great blog post that the Judi and the other people in the agent quality team put out about dynamic file context.

**swyx** [01:02:00] Is that your team is the different team?

**Samantha** [01:02:00] Different team, yeah. And they were working on basically doing a lot everything, file system, everything is file system. And so a lot of my thinking personally on memory this past year has changed to be more aligned with that, where it’s like giving the agent pointers to things, annotations to things.

[01:03:00] The second thing I think that I’ve started to think differently about memory is a subset of agent self-audit ability and self-awareness. Basically like the agent might wanna propose annotations or links or memory like files to itself when it finds that there’s like some gap in its functionality in its own harness that might need to be filled by like some piece of information on a semi-permanent basis.

[01:03:00] But there’s a whole bunch of other things that are a side effect of self auditability that are really interesting, like potentially finding like conflicting instructions or like skills and rules that like might be like, eh, these are bugging each other. And also things like fixing like Devrel X problems that it runs into.

[01:03:00] I think that basically the dynamic file system stuff is probably very promising from memory. And there’s also this notion of needing to have the agent be a little bit more self-aware in terms of being able to identify gaps in its own functionality and decide how to fill them.

**Jonas** [01:03:00] That’s such a good point.

[01:03:00] Like self-awareness broadly has been a really big thing that I think Sam has pushed us to do more and more of where the agent should understand how its environment works, it should understand how secrets work. Like it needs to be self-aware about its own harness and its environment. And then, and you

**swyx** [01:04:00] think this is not inherent in the model you have to do.

**Jonas** [01:04:00] It’s specifics, right? If it’s running in cursor versus some other sandbox that’s a bit different. And then the other part of it that starts to get really interesting is when the model starts editing its own system. Prompt.

**swyx** [01:04:00] Yeah.

**Jonas** [01:04:00] What does that even mean? How do you do that safely and then way over

**swyx** [01:04:00] do that?

[01:04:00] This is just research, right? This isn’t, this is

**Jonas** [01:04:00] I think it will do that. Yeah. It will manage its own context. And so system prompt is part of the context, and you can argue about

**Samantha** [01:04:00] Yeah, like other things that it might decide to turn off or on depending, and all those, self-awareness to us in this context is not like the model itself, having a notion of consciousness, but more like knowing like what system it’s operating in and the constraints of that system and potentially being able to have agency in optimizing itself to operate best in the, in that system.

[01:04:00] This was like one of the first things I learned at DOT when we launched was that I we had made the model or made the agent or. Whatever we would call it. At that time, it was far less, agentic made the product work very well at a certain number of things, but didn’t have complete self-awareness of like its own boundaries.

[01:05:00] So people would be like, Hey, can you do this thing? And the thing was there and could be done and the and the product would be like, oh no. And I’d be like, but you can. And so like basically like that was one of the earliest things I found is

**swyx** [01:05:00] believe in yourself.

**Samantha** [01:05:00] I know as a product developer, like it needs to both be able to do the thing and it needs to have complete knowledge of its ability to do the thing.

[01:05:00] Those are not always obviously the same like part of the prompt at all.

[01:05:00] Yeah.

**swyx** [01:05:00] Yeah.

**Samantha** [01:05:00] It’s something that I think has continued to be a theme in the ecosystem that users will often attribute increased intelligence to a system that is more highly self-aware and is more able to like, manipulate itself to do well in a system.

[01:05:00] If that makes sense.

**swyx** [01:05:00] Yeah. This is more abstract than I ever thought would get at Thisor discussion. Cool. That isn’t the kind of conversation that you have

**Samantha** [01:06:00] in, we talk about this stuff all the time to

**swyx** [01:06:00] improving

**Samantha** [01:06:00] Yeah.

**swyx** [01:06:00] Agents in general.

**Jonas** [01:06:00] Yeah. I think to your point right about the agent layer and thinking a lot about models and the harness and the product and the affordances like that.

[01:06:00] Yeah. Falls from the

**swyx** [01:06:00] No, I mean you guys are like my sort of needing example what an agent lab looks like and can be successful and I think people always hungry for insights into how you guys operate, so thank you for taking the time to share.

**Samantha** [01:06:00] Yeah. Thanks for coming.

[01:06:00] Yeah. Thank you.
