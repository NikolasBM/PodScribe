---
podcast: "ai-daily-brief"
podcast_title: "The AI Daily Brief"
title: "How to Get the Most Out of Fable 5 and GPT-5.6 Sol"
date: 2026-07-20
url: "https://aidailybrief.ai/e/2026-07-20"
guid: "https://aidailybrief.ai/e/2026-07-20"
host: "Nathaniel Whittemore"
format: "tutorial"
level: 1
length: "00:26:00"
categories: ["agents", "coding", "models"]
featured: ["Claude", "GPT-5.6", "ChatGPT", "Claude Fable", "agent harness"]
mentioned: ["OpenAI Codex"]
transcript_source: "publisher"
---

# How to Get the Most Out of Fable 5 and GPT-5.6 Sol

[00:00:00] Today on the AI Daily Brief, how to get the most out of frontier models. The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI. All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, Blitzy, Retool, and Airtable.

260720 in_EDIT: To get an ad-free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts. To learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai. And a quick note about today's episode, this was recorded in advance. In fact, I am recording it on Thursday afternoon as everyone freaks out about Kimi So in the meantime, you know, if Dario and Sam have lost their minds and released new versions of Fable and GPT in response to the threat that's tearing value off the Nasdaq, you'll know why I am not talking about it right now.

Just a quick little bit of travel on Monday. I will be back on Tuesday with a normal episode But still, regardless of what is going on in the wide world of models out there, today's episode is all about how to get the most [00:01:00] out of the most advanced and newest models.

So without any further ado, let's dive in. It has now been a couple of weeks with this new class of models in Fable 5 and GPT Now, weirdly These models have actually been around a little longer than a couple of weeks. there was a particularly long early access period for GPT 5.6 and Fable 5 was here for a couple days before going away But at this point now, pretty much everyone has now had these models for some time.

260720 ep_EDIT: In fact, our access to them 

keeps getting extended and reset. And along with that, people have started to publish their tips and tricks for getting the most out of them. Now, it is always the case that new models demand new ways of interacting with those models to get the most out of them.

But this is exactly the sort of information that can't really be captured in anything like benchmarks and just has to go be experienced through trial and error

As 

you will see, there are a number of common threads that cut across both 5.6 Sol and Fable 5

That suggests, I think, not just some new ways to get the most out of these models, but for some new [00:02:00] patterns of interaction that are going to become increasingly common from here on out And we're gonna start with some official sources and commentary

Codex team member Eric Provencher wrote, " With 5.6 Sol, a lot of people are still prompting the model exactly as they did 5.5. It's important to note that 5.6 Sol is a lot more tenacious and thorough than previous models."

Eric Eric published a prompting guide on the official learn.chatgpt.com site

And while in this case it is not presented as a way to get more out of five-six as opposed to five-five, there there are a few things that are specifically worth noting

one piece of guidance that comes from that tenacity is around setting boundaries

Boundaries, writes the guide, are the few instructions ChatGPT needs to avoid creating extra work or taking an action you didn't intend

Add one when changing the wrong detail would make the result unusable, or when you wanna review something before it affects other people Examples. 

keep the approved dates and budget figures unchanged. Used only the supplied sources. Flag missing information instead of guessing. Keep recommendations [00:03:00] within the stated budget.

Prepare the message as a draft, don't send it. You can see how in each of these cases, a more tenacious model, to use Eric's word, might assert a little bit more agency than the user would be comfortable with and actually go off and do something that ended up not being optimal 

for whatever the prompter was trying to achieve

One One example of these boundaries wasbeing explicit about where you wanted it to stop and actions you didn't want it to take, i.e., don't send the message, just prepare it as a draft



another example around the approved dates and budget figures 

was to limit and focus where the tenacious model was applying its attention

When it comes to the injunction to use only the supplied sources, a tenacious model that has access 

to the entire internet could go off and get lost in some serious rabbit holes if not told not to do that. Now, obviously, setting boundaries is nothing new But the point here is that the more powerful the model, the more significant those boundaries become, and the more real-world consequences there can be if those boundaries aren't set.

On the lower end of the spectrum of consequence, there's just burning through way more [00:04:00] tokens than you actually needed to, which in an increasingly cost-conscious era isn't nothing. But then, of course, there's much bigger consequences like sending a message that hasn't been approved yet to a critical customer, partner, or colleague

tip,

another prompting tip from Eric, which again isn't different, but certainly comports with the idea of 5.6 Sol being a model where you actually want to interact with it as opposed to just give it a task and let it go off and do its thing, is to iterate with the model to improve the result with follow-up messages



260720 ep_EDIT: Once you see the first version, you can follow up with things like keep the opening more direct, keep the evidence, move this or that part around

And interestingly, increasingly iteration isn't going to happen in a completely turn-based way where you have to stop and wait for an output before you can steer where the model goes next. As ChatGPT and Codex come together, some of the sort of steering behaviors that are normal in Codex can come to that main app experience as well The guide writes, "When Codex is already working, you can send another message without waiting for the current run to finish.

Steer adds the message to the current run. Use it to change direction, add a missing detail, or share new [00:05:00] information. Queue saves the message for the next run. Use it as a follow-up that should wait until the current work finishes."

this sort of behavior reduces the latency of collaborating with AI in ways that become important the more powerful the models get



260720 ep_EDIT: Now one of the things that follows from the recent integration of Codex and ChatGPT and the split of ChatGPT into chat and work 

is different prompting tips for different types of experiences.

In this post, Eric and the team at ChatGPT explicitly separate prompting best practices and examples for chat as opposed to for work

A lot of the tips around work have this element of cost and efficiency consciousness embedded within them One section is called Use Work Efficiently and says, work is useful for time-consuming or recurring tasks or for finished files you can reuse. A task that uses more credits can still be worthwhile if it saves time, improves quality, or helps you make an important decision."

and a lot of their recommendations are again about managing that tenacity that Eric was talking about. They suggest starting with only one result that you can review

And doing things like narrowing or stopping the [00:06:00] task if it starts doing work you no longer need

Now there is of course a lot more in here, but the last one that I wanted to note specifically 

was the suggestion, which you'll hear a lot if you stick around these parts, to use voice dictation. One thing that's great about ChatGPT is that even if you don't have something like Whisperflow set up on your computer, 

ChatGPT's dictation is absolutely best in class, and so you can use the native dictation tool that's embedded right within the app 

as I've said before, one of the reasons that voice dictation is so valuable in the context of AI 

is, 

well, 

context. 

In a world where AI needs more information to do its job well, 

the

the rambler shall inherit the earth.

And talking at your computer for a bunch of minutes, even if it's a totally unstructured stream of consciousness, is often going to be more effective in giving the AI what it needs to do well than a hyper-precise and clearly articulated set of typed notes that don't necessarily include all of that context

out. Now, this is not the only new model guide that came out around 5.6. 



over on the OpenAI developer site, they also have a set of best practices for GPT 5.6

Nathaniel Whittemore: 5.6 

260720 ep_EDIT: And what's cool is you can actually [00:07:00] click back and see best practices for previous models as well, going all the way back to GPT-4.1content, AI content creator Ollie Lehmann 

found the really valuable and summed up some of the best tricks he found.

One, he writes, "Delete instructions from your old prompts." OpenAI's rule is to state each instruction exactly once. They found that removing repeated instructions raised scores by 10 to 15%, while cutting tokens by up to 66%. The giant rule lists you wrote for older models now make GPT-5.6's answers worse 



and cost you more Two, match the compute to the job.

There are two separate dials now, which model size, i.e. Sol for the hardest problems, Terra for everyday business work, and Luna for cheap, fast tasks, and how hard it thinks. Six effort levels from none to max. OpenAI's advice on the thinking dial, start at whatever setting you used on the last model, then test one level lower.

The new generation usually needs less. Save max for your genuinely hardest problems this is one of those pieces of advice that sounds incredibly simple, 

but is [00:08:00] almost emotionally hard to do

For so many of us, the temptation for just about every problem is to dial up the settings all the way to max because all things held equal, wouldn't you want the most intelligence on every single problem?

even outside of costs, it is increasingly clear 

that 

that is not necessarily the optimal behavior

And so that's why Open-- And so that's why OpenAI is trying to give some discrete guidance around what you should do instead

tip,

another tip in the area 

of undoing previous instructions 

is to check older rules you gave about brevity

Ollie writes, "GPT 5.6 defaults to shorter answers than 5.5, so brevity rules you added for older models can now cut too much. When you do want something short, tell it which information to keep and which detail it can drop instead of a blanket keep it brief."

On tone, concrete instructions beat abstract instructions. 

for example, OpenAI suggests that terms like friendly and empathetic are going to be too abstract, and instead, Oli writes, "Spell out the actual writing behavior you want, how direct to be, what to open with, what to skip."

Something like, " Name the customer's problem in your first line, give the fix as numbered steps, skip the apology [00:09:00] paragraph," gets you the same tone every single time

And yet, if these tips are all very clear and practical, and stuff that you can go use right away there is another theme that I'm starting to see 

across a lot of the discourse, which is about the level of ambition we're bringing to these most advanced models



Christine Xu, an AI UX PM at Intuit, wrote a post called You're Not Ambitious Enough with Claude

Christine writes, " The biggest productivity and capacity unlock in my daily work happened when I went beyond automating busywork to asking Claude to do more high-leverage work. For months," she wrote, " I was using Claude to clear the dopamine backlog, the queue of little tasks that I respond to too eagerly because completing gave a dopamine hit, an illusion of progress.

These automations freed up a lot of my time. With that newfound time and fable, I started pushing it for higher leverage work, hard tasks I didn't trust Claude with before. This made the biggest leap in my productivity, capacity, and sense of flow



Christine calls upon a concept from Stripe product leader Shreyas Doshi, who wrote, "There are three levels to product work [00:10:00] One, the execution level. Two, the impact level. And three, the optics level

Christine notes that, quote, "Many of us use Claude to automate busy work in optics and execution and leave the impact work to ourselves. We tell ourselves the story that judgment is the defensible human thing. But when given the right context, Claude can do the hard work better and faster than you.

lowering the activation energy of starting is a major unlock in itself

in fact, Christine suggests using Fable 5 in different ways for each of these three categories of work. Optics work, for example, she says, is about making your team's progress visible to the right people in the right forums For this She suggests using Claude with Fable as autopilot to replace production

The example she gives, " I have a scheduled task on CoWork that runs twice a week. It pulls context from key sources and writes the latest updates for each work stream into a Google Sheet template. this G Sheet status board is visible for the teams to get their questions answered without asking me.

I also have a skill that packages these updates at different levels for the right audience and forums." " Optics work," she [00:11:00] continues, "is the layer to automate ruthlessly because it takes care of the dopamine backlog so you can stay in flow." In fact, she suggests, "I wouldn't be surprised if these flows are productized soon in Claude itself."

At the next level for execution work Instead of Claude as Automator, she suggests Claude as Copilot

" Every Monday," Christine continues, "I run the context dump skill, which reads my past week across Slack, calendar notes, and repo activity, gives me an analysis of my efficiency and patterns to watch, recommends what I should prioritize, and offers specific work to help me get started on.

It reads less like a summary and more like a coach who notices my personal patterns and actually makes helpful observations and recommendations."

I also run a planning skill that checks Jira status and the roadmap and shows me how the team is tracking and what to line up next For staying close to the customer, I run a scheduled task monthly that analyzes our customer support channel to give me the top themes, the trends, and recommends the top requests or problems I can prioritize.

Overall, she says, "Get more ambitious with the asks. don't treat Claude as just for distilling a summary. Ask for judgment."

Lastly, for impact work, she suggests [00:12:00] using Claude as sparring partner to get the hardest work started

This level, she says, is the high leverage work that is the hardest to start, e.g., thinking through a new product bet, preparing narrative for a high-stakes presentation, testing strategy against business unit strategies, etc.

Now around this, she suggests it's worthwhile to, quote-unquote, "onboard Claude and set it up with the right context."

This is something we've talked about a lot. Creating a personal context portfolio that includes all the information that any

given AI or model needs to be able to actually be a useful collaborator

And overall, the biggest thing

Is that it feels to me like Christine is

really feeling like Fable unlocks this sort of impact work for her for the first time She writes, "Fable is 

noticeably better than previous models for impact work. I especially enjoy its calmness. It sounds more concise. It feels more like a conversation with a smart colleague than reading walls of text with unnecessary dispositions.

This makes a big difference in keeping a train of thought going."

One of the most important AI questions right now isn't who's using ai, it's who's [00:13:00] using it? Well,

Speaker: KPMG and the University of Texas at Austin. Just to analyzed 1.4 million real workplace AI interactions and found something surprising. The highest impact users aren't better prompt engineers. They treat AI like a reasoning partner.

They frame problems, guide thinking, iterate, and push for better answers.

Nathaniel Whittemore: Now, along the idea of moving Fable into more high impact and higher order types of work, Tariq from the Cloud Code team recently wrote a [00:16:00] post called A Field Guide to Fable: Finding Your Unknowns

260720 ep_EDIT: Tariq writes, " Working with Claude Fable 5 keeps reteaching me an old lesson. The map is not the territory. The map, a representation of the work to be done, is my prompts and skills and context. It's what I give Claude. The territory is where the work needs to happen, the code base, the real world, its actual constraints.

The difference between the map and the territory is what I call unknowns. When Claude runs into an unknown, it needs to make a decision based on its best guess of what I want. The more work being done, the more unknowns Claude might run into. Fable is the first model where I find the quality of the work is bottlenecked by my ability to clarify its unknowns."

And the rest of the thrust of Tariq's post is to point out that, in his words, planning ahead isn't enough 

And instead that, 

in his words, working with Fable is an iterative process of discovering my unknowns before, during, and after implementation

So what are examples of this? Tariq says that when he starts engaging with Fable, he breaks it down in [00:17:00] four ways. The four categories are known knowns, or essentially what is in his prompt, i.e. what do I tell the agent that I want?

the known unknowns are what he hasn't figured out yet, but is aware that he hasn't. The unknown knowns are what are so obvious he'd never write it down, but would recognize it if he saw it. And the unknown unknowns are what hasn't he considered at all

Tariq argues that reducing and planning for unknowns is the skill of agentic coding

And suggest that there are ways to improve upon it

and key to that is helping Claude help you. Tariq writes, "Instructing Claude is a delicate balance. If you're too specific, Claude will follow your instructions even when a pivot may be more appropriate. If you're too vague, Claude will often make choices and assumptions based on industry best practices that may not be a fit for your task."

Importantly, when you don't account for your unknowns, you fail both ways. You don't know when the path will be filled with obstacles, 

and you don't know when the path will be clear, but you still want Claude to veer. Claude can help you discover your unknowns faster

The most important part, he says, is to give Claude context about your [00:18:00] starting point. For example, tell it where you are in your thought process, disclose your experience with the problem, and let it work with you like a thought partner



260720 ep_EDIT: a couple specific ideas are things like a blind spot pass

An example he gives, "I don't know what color grading is, but I need to grade this video. Can you teach me to understand my unknown unknowns about color grading that I can prompt better?"

Another suggestion is to brainstorm and prototype. Tariq writes, "When I'm working in an area with a lot of unknown knowns involving criteria I only know to define when I see it, I like to ask Claude to brainstorm and prototype with me."

" It's extremely valuable," he continues, "to identify and verbalize unknown knowns early during prototyping, because finding them out during implementation can be relatively expensive. Small changes in a feature or spec can cause drastically different implementations in code and can be more difficult for your agent to revert previous changes."

Now this is something I think a lot of you guys are probably doing intuitively. An example prompt he gives is, " I want a dashboard for this data, but I have no visual taste and I don't know what's possible. Make me an HTML page with four wildly different design [00:19:00] directions so I can react to them."

Now, Tariq gives a bunch of other ideas about how to work with unknowns

And a lot of it ultimately comes to a meta process where you invite Fable in as a co-creator of the process to get the most out of what it can do

Now, Daniel Meisler thinks that even beyond a single model like Fable 5

that there are a set of prompts to rerun every time a new state-of-the-art model drops that can help you reorient your experience to take most advantage of that new model. He calls these tactical meta prompts worth rerunning every time there's a significant jump in intelligence

The first category category is around harness optimization and are all related to improving

your AI harness, i.e. the set of resources and information 

around your model to getthe most out of the newest version

One example he provides

is the self model audit. Read everything my harness believes about me, identity, goals, voice and preferences, and find where it's modeling a version of me that's stale, aspirational, or just wrong. compare what my files say I am against what my recent behavior and work [00:20:00] actually reveal.

Flag every place the system is optimizing for who I said I was instead of who I am now, and propose the specific edits that close the gap. Now, to some extent, this is just context hygiene. And what Daniel is really doing here 

is using the moment of a new model release to engage in that sort of context hygiene and make sure 

all of the information that you've surrounded your model with, things likeyour agents.md file, 

are actually reflective of the person and projects that you're bringing 

to that new model

Daniel's also a fan of testing new models by going really, really big. He has a whole category of prompts that he calls overall life and work optimization, i.e. massive scope prompts that basically help you sort out your priorities, your projects, and come up with a plan for maximizing the next crucial few years One he calls Big Picture is a prompt like, "Take a look at all my various projects in writing online, all the activities we've been doing in the harness, and everything you know about me from web search, and analyze it deeply.

Then look at what's going on in my field, in AI, and in society, and in the future in general, And tell me what solves the Japanese concept of ikigai for [00:21:00] me. What should I be working on that gives me fulfillment but is also lucrative? Doing it for myself, with collaborators, 

or working for a corporation?

Make concrete recommendations if you have them, and feel free to interview me for more context before creating the output. Now, I don't think that this is necessarily going to be everyone's cup of tea, but I do think that this sort of prompt is a great way, even if it's just for the sake of 

taking the vibe temperature of a model 

to understand how it engages with these sorts of questions

sugge- another suggestion from Daniel, which is starting to come up more and more frequently, is to once again think in terms of loops

Matt Schumer actually included this in his Fable five tips as well

with the recommendation he called loop it until it hits the bar, especially for creative tasks

Now for this, you have to go back to Matt's 

previous recommendation to give Fable a real bar for done. Matt writes, "If you tell Fable to make something high quality, it stops at its own idea of good enough, which is usually lower than yours. So I don't use adjectives. I give it a bar it can check itself against, then I make that bar hard.

Sometimes I write the test myself, something concrete like a stranger can't tell our render from the [00:22:00] real photo. Other times, I don't even know how to measure the thing I want, so I hand that problem to Fable too."

Now Matt continues, "Once there's a bar, I put Fable on a loop against it and let it go. It builds, checks itself, finds the biggest gap, closes it, and goes again."

Nat says that he uses the /

loop command for this constantly, especially on creative work, where there's always something concrete to keep measuring against until it's actually there

Importantly, Matt writes, "The whole point of the loop is that Fable never gets to decide it's finished. There's always a next gap. It stops when I say it's done or when it genuinely can't find anything left to fix, which is rare if you've set this up right."

Now, at some point, we'll do a show entirely about some of these loop strategies. but I did wanna share just a couple notes from a Claude Devs post recently about getting started with loops

260720 ep_EDIT: Where they break loops apart into a set of different categories 

that I think are useful in helping understand the concept at core

loops. Turn-based loops are the first type. They are triggered by a user prompt, and they stop when Claude judges that it hascompleted the task or needs additional context. Turn-based loops are best for shorter [00:23:00] tasks that are not part of a regular process or schedule

every prompt you send they write starts a manual loop with you directing each turn. Claude gathers context, takes actions, checks its work, repeats if needed, and responds. For example, they say, ask Claude to create a like button. It reads your code, makes the edit, runs the tests, and hands back something it believes works.

You then manually check the work and write the next prompt You can improve the verification step by encoding your manual steps as a skill.md so Claude can check more of its own work end to end

Contrast that with a goal-based loop which is triggered by a manual prompt in real time, where the stop criteria is the goal being achieved or the maximum number of turns being reached. This, they say, is best used for tasks that have verifiable exit criteria

And is useful when a single turn is not enough. Agents do better, they write, when they can iterate

And when you define the success criteria, they say, Claude doesn't have to make a determination on what is good enough and end the loop early Each time Claude tries to stop, an evaluator model checks your condition and sends it back to work until the goal is met or a number of turns you define is reached

[00:24:00] A time-based loop is triggered by a specific time interval that can be stopped when the user cancels it or when the work completes. And this is going to be useful for things like recurring work. Proactive loops, on the other hand, are those that are triggered by an event or schedule and don't require a human in real time to set them going

The stop criteria is once again when a specific goal is met, with the routine running itself until you turn it off

Now, a lot of what we'll be exploring over the next few months is how to bring this sort of loop-based interaction outside of the realm of coding and into 

into more creative and knowledge work

Even though we're not getting deeper than that when it comes to loops, the reason it's worth mentioning them at the end of this particular episode

is that the big theme and takeaway of all of these recommendations

is two-part. At a simplest level, they are all reminders that every time we get a new model, especially when those new models represent a big jump in intelligence we need to do the hard, sometimes time-consuming work of going through and trying everything and figuring out where the ways that we prompted and interacted with the old models

either no longer get the most out of the new models or actively harm them

But [00:25:00] secondly, and perhaps in the long run even more importantly We need to figure out the new techniques which actually unlock the differentiated capabilities of that jump in intelligence

And many times those things aren't just going to be prompting tips

But totally new interaction patterns like these loops represent

If there is one takeaway from all of these pieces, it is to ratchet up one's ambition

And almost to assume no limits on what the newest model can do

so that by trying the biggest, most challenging things you can think of, you can actually figure out what 

those limits are once they inevitably reveal themselves

uh, the first the first layer of this work is always going to happen on an individual level

But I think that there is an analogy for organizations here as well

It is so easy, especially in a business or work context, 

to default to using AI for the things that we're already using AI for, the places where we've already found value, the type of work that we already do And the view AI is just a way to do it 

faster or cheaper or maybe a little bit better, but ultimately to do that same work The unlock, of course, is a new relationship [00:26:00] with work and even unlocking new categories of work that weren't possible before.

Figuring out how to do that is a lot less simple, but it's also really exciting. the, hopefully some of the tips you've heard today give you tools you can use across that full spectrum of work

And hopefully they're still useful about five minutes from now when we get the next model leap. For now, that's gonna do it for today's AI Daily Brief. Appreciate you listening or watching as always, and until next time, peace 

​ 

Nathaniel Whittemore's audio recording:
