---
podcast: "latent-space"
podcast_title: "Latent Space"
title: "The End of SWE-Bench Verified — Mia Glaese & Olivia Watkins, OpenAI Frontier Evals & Human Data"
date: 2026-02-23
url: "https://www.latent.space/p/swe-bench-dead"
guid: "substack:188928663"
host: "Swyx"
transcript_source: "publisher"
---

# The End of SWE-Bench Verified — Mia Glaese & Olivia Watkins, OpenAI Frontier Evals & Human Data

## [00:00:00] Meet the Frontier Evals Team

**Swyx** [00:00:00] Okay. Hi. We’re here in the PI studio with Mia and Olivia from the Frontier Evals team. Or however you want to introduce yourself. Maybe m want to introduce name, what you do at Open AI and we can get it started.

**Olivia** [00:00:00] Sure. Hi, I’m Olivia, I’m on the Frontier Evals team.

**Swyx** [00:00:00] Great. Pete.

**Mia** [00:00:00] Hi, I’m Mia. I am a VP of research at OpenAI and my teams are the Codex team, the human data team, and the alignment team. And we work a lot with Olivia’s team on Frontier.

**Swyx** [00:00:00] Yeah. Very exciting. And as by my understanding, you were part of the original team that worked on SWE-Bench verified as well.

**Mia** [00:00:00] Yeah. Olivia’s team, the Frontier team and the human data team collaborated on creating SWE bench verified.

**Swyx** [00:00:00] So you’ve, you’ve seen the evolution of coding benchmarks over time, and I I think it was round about to the mid to late 2024 when you first covered three verified. These have evolved a lot since then.

## [00:00:56] Why SWE Bench Stalled

**Swyx** [00:00:00] What’s the blog post that you have worked on that you, that we’re releasing today? Like what, what is the sort of con, what’s the main thesis that you’re pushing out?

**Olivia** [00:00:00] So the main thesis is that SWE-Bench verified has been one of the North Star coding benchmarks that the field has looked at to measure coding progress. But recently we’ve seen that. Progress has kind of stalled. And basically we realized that this is because the eval is effectively saturated and also highly contaminated.

[00:00:00] So at this point we think that it’s not really measuring coding performance improvements well anymore. And we think that the field should move away from this towards other benchmarks

**Swyx** [00:01:20] like SWE-Bench Pro.

**Olivia** [00:01:20] Like SWE-Bench Pro. Yeah.

**Swyx** [00:01:20] Amazing. Yeah, I, one of the jokes I always have is like there’s a group chat with all the labs.

[00:01:20] And everyone just takes turns, the increment, like 0.1 on trucks and then it’s like, okay, well you have the best coding model, I guess. ‘cause you’re 0.1% higher, but it’s not super convincing at this point. No. Yeah. So cool.

## [00:01:47] How Verified Was Built

**Swyx** [00:01:34] I think the let’s, let’s sort of reset on like, what was the original work that you guys did for Verified, which I think was pretty substantial.

[00:01:34] Like, it was like a very significant investment from OpenAI, which like people still don’t appreciate. And then. What were the satisfactions that we, that we found over time? Right? So like what, what was Sweet Bench Verify, or should, should that people should know about?

**Olivia** [00:02:00] Suite bench verified was kind of a cleanup of original bench academic benchmark from a lab at Princeton called Suite Bench.

[00:02:00] And the agent is basically given a code base and a task that was sourced from a real world repository and GitHub issue, and was asked to solve a task and is graded on whether some tests pass. And at the time this was quickly became a popular benchmark because at the time the field didn’t really have good real world coding benchmarks.

[00:02:14] Then when open, I took a look at the benchmark as part of one of the evals we wanted to track in our preparedness framework. Folks started realizing that some of the cases where agents were failing were due to bad problem setups rather than just to models being dumb. So folks at OpenAI did a pretty extensive human data campaign hiring like almost a hundred real world software engineers to go through the problems and figure out like, are the tasks well specified?

[00:03:00] Are the tests actually fair? And kind of created a curated set of like 500 tasks that we thought were much better.

**Mia** [00:03:00] It’s just, it’s maybe, it’s hard to, to overstate like the amount of effort that it took to like create that benchmark. It was literally like many export software engineers. Reviewing the problems like differentially multiple times and to, you know, basically like three.

[00:03:00] Different experts independently decided it.

**Swyx** [00:03:26] Yeah, you didn’t have to do that. You just tripled your costs for just,

**Mia** [00:03:26] I mean, we had to do it, we had to do it actually, because it’s quite a hard task to like look at something like a, a problem and, and the patch and then like, it’s not just the problem and the patch, right?

[00:03:26] You have to like understand it in the context of the code base that the human or, or the murders and to solve the task. So it’s a very complex problem and it was definitely needed to have. Three reviews and I think like maybe we should have done more, but it was definitely a lot of effort to get there.

**Swyx** [00:04:00] And there’s, there’s more, but people can read the, the blog post for that. I will note that you guys had a trend in verifying benchmarks. ‘cause I just recently saw, I think Quinn had a HLE verified for humanities. M verified.

**Mia** [00:04:00] Yeah.

**Swyx** [00:04:00] Which like, so now everyone’s verifying everything, which is. Nice and good and like extra quality there.

[00:04:00] Okay. So, but the, I think that the meat of it is that, that this, this was a lot of like, well, here’s the issue or problem statements, and then here’s the, here’s the diffs, here’s the golden tests, and here’s some regression tests. Right? That’s, that’s like the rough setup of these 500 problems.

## [00:04:32] Contamination In The Wild

**Swyx** [00:04:17] And there’s some contamination always happens because all the C measure I was.

[00:04:17] Fully open. I think you, you did have canaries, but like, you know, stuff, stuff, leaks,

**Mia** [00:04:35] there’s like multiple avenues that like the problems are sourced from open source repos. Yes. So it’s not just like when we usually publish evaluations. We publish evaluations and then we, we add can strengths to ensure that, you know, they are easily fit out, out at training time.

[00:04:35] Obviously if you use sort of like. Data from like open market, just

**Swyx** [00:05:00] GitHub.

**Mia** [00:05:00] Yeah. You don’t have actually like a CAGR cannery string in that. Yeah.

**Swyx** [00:05:00] And you,

**Olivia** [00:05:00] and these are also like, some of these are very popular repos, like the Jengo repository. So you’re gonna see like many instances being used kind of throughout go.

**Swyx** [00:05:00] Yeah. Yeah. And you just before recording, you’re telling me that you found this in your own chain of thought with that 5.2 also seeing that like. They had extra knowledge or something?

**Olivia** [00:05:00] Yes. So this was an example where the task asked the agent to influence something, but it wasn’t told that there was this specific argument that the test was going to be looking for it using.

[00:05:00] But in the GP 5.2 chain of thought, we actually saw instances of the model reusing, like, Hey, I think that at some length version of this repository, they implemented this particular argument. Maybe I should add it in. Yeah. So this is an example of a test that like would be pretty impossible to pass without this contamination knowledge.

**Swyx** [00:05:36] Yeah.

**Mia** [00:05:36] And I think you found that. Sort of forced, right? And had triggered like a whole investigation, both like in our own modes oh, and also in other frontier modes, like in the market, and like understanding how contaminated the benchmark is, like across the industry.

**Swyx** [00:06:00] What else did you find? I mean, that’s, I have to double click on this.

**Olivia** [00:06:00] So we, and when I say we, this is mostly from other folks at our tape, not don’t, not

**Swyx** [00:06:00] familiar.

**Olivia** [00:06:00] Yes.

## [00:06:16] Unfair Tests And Narrow Specs

**Olivia** [00:06:00] But so we did some analysis on, first of all, are the tests actually fair? I. So this happened by first taking all the problems that O three E couldn’t solve lively, and then again getting a lot of humans to do basically another pass of kind of digging into, you know, what’s wrong.

**Swyx** [00:06:00] Is it the same exact analysis or were they reading o three’s output and going o. Here’s where all three went wrong.

**Olivia** [00:06:00] I think it was, I mean, it was definitely like a scope to the set of problems that models failed. And I believe they were able to look at like what the model solutions look like versus what the, so

**Swyx** [00:06:00] this isn’t the same work as the original.

**Mia** [00:06:00] It’s not exactly the same work. It was like a, a deeper dive. It’s like, okay. Which are the problems that we don’t see any murder solving is like, is there’s something fundamentally wrong with those problems or is there something you know wrong with the other model? Just not smart enough to solve the problems.

[00:07:00] So that’s kind of like what we, what we dug into.

**Swyx** [00:07:07] Yeah. And you found some.

**Olivia** [00:07:07] Oh, yes. Like in over half of the problems that were investigated in that deep dive, there was one problem or the other. I think the most common problem are like overly narrow tests where there’s some particular implementation detail that the tests we’re looking for, but wasn’t specified in the problem description.

[00:07:07] So it wasn’t fair to expect that model to make that particular design choice like one. Pretty blatant example are cases where the task asks you to implement some feature and the tests are looking for you naming that argument or that function with a particular name. But if you may chose another reasonable name, the test would fail.

**Mia** [00:07:28] Yeah.

**Olivia** [00:07:28] And another set of types of bad tests or tests that are just looking for additional features that were never mentioned. The problem description.

**Mia** [00:07:28] Where, where that’s a significant, it like that means that if you pass a test, actually, like you probably did like a really good job, but just because you didn’t pass a VE test doesn’t mean that your implementation wasn’t like a good one.

[00:08:00] Right. So it was just like, we only accept like very narrow versions of solutions and like not the whole space

**Swyx** [00:08:03] Yeah.

**Mia** [00:08:03] Of, of like viable and sort of like good solutions to the problem.

**Swyx** [00:08:03] Yeah. I think it’s important that you’re doing this because it, in some way it is you in 2020. Five, six, going back in time and correcting your own work, right?

[00:08:03] Because you could have caught all this in in the original verified work. I

**Olivia** [00:08:24] think so it’s definitely much harder to find a problem in the abstract than when you’re looking at a very smart agent’s best effort solution and trying to compare it. It

**Swyx** [00:08:24] is harder or harder,

**Olivia** [00:08:24] sorry. It’s much easier when you have those solution much easier.

[00:08:24] Exactly. Sorry,

## [00:08:40] When Benchmarks Saturate

**Mia** [00:08:39] I think, I think also like at the time and three Be Verified was published, I think it was like a very strong benchmark. It’s not like we are, we’re like, oh, this is not, this wasn’t like a strong benchmark at the time. I think this is something that a lot of. Benchmarks go through like as an evolution, right?

[00:08:39] Like when they start to become like popular and like viable, it’s because they measure something like important and modes maybe do like 20% correct on them, sometimes even less. And sort of like people have something to hold on and, and improve modes on, on these benchmarks. And by the time that you hit like very high performance on the benchmarks, like additional like 0.1% improvements, it’s become sort of like meaningless and sort of like at the time I think, you know.

[00:09:00] That benchmark was like super valuable and it, it taught like us and like the industry a lot. It’s just like now at the point that we are at now where markets are as strong as they’re now, we are kind of starting to measure, not necessarily like what we want to measure, which is like coding capability of our agents, but like the agent’s ability to like correctly guess how to name a specific function.

**Swyx** [00:09:23] Yeah.

**Mia** [00:09:23] And, and that isn’t really what we are like want to measure at this point. Yeah.

**Swyx** [00:09:23] I think that’s fair. Is there, I mean if I, if I asked you to ballpark it, like most models are, most frontier models are now like 80 something. Is there, like, what’s the actual like number on superb bench verify that you did you guess as like the ceiling or?

**Olivia** [00:10:00] I guess that’s really hard to say. Like I when GDI 5.2 came out folks took a look and found that it was solving like 31 problems that were in the set of, should be very hard to solve without contamination problems. So I think it’s quite possible that that number is already something that we’ve hit.

[00:10:00] If you didn’t have contamination at all. Fair enough. Hard to say though.

**Swyx** [00:10:23] Yeah. Cool.

## [00:10:28] Switching To SWE Bench Pro

**Swyx** [00:10:23] We’re gonna stop reporting CBE verified. Right? And then SWE-Bench Pro Will will be sort of the next one, which is an effort from scale. What’s your sort of comparison analysis? What’s, what attracts you to SWE-Bench Pro?

**Olivia** [00:10:23] The first one I think is just that it’s harder for SWE-Bench verified.

[00:10:23] I think, I mean like 90% of the problems are things that were estimated to take like an expert software engineer like less than an hour. They’re like very well specified, very self-contained, and the SWE-Bench Pro problems are just bigger and harder. There’s much more head rewind that eval because it’s not saturated.

**Swyx** [00:10:41] Yeah. Like categories of like one to four hours and four plus.

**Olivia** [00:10:41] Yeah. And it’s more diverse. Lots of repositories, multiple languages, qualitatively more different types of problems. So all that’s great. On the contamination side, we also think it’s better there. So the way we were measuring for contamination for SWE-Bench verified was with this little like contamination auditor agent, which is given the description of the task and the patch and the task ID and told to go take this target model.

[00:11:00] And kind of as an open-ended, like set of questions, try to find questions that will manage to kind of reveal what contamination might be lurking in that model. And in SWE-Bench verified, we found. Many instances of contamination across like across open eye models, across like quad Opus 4.5, Gemini Flash.

[00:11:23] And, and all of these we saw things like regurgitating the ground proof solutions, things like in some cases giving like the task IDs and other things that are pretty clear evidence of at minimum familiarity was the stories.

**Swyx** [00:11:42] Yeah.

**Olivia** [00:11:42] So we

**Mia** [00:11:42] that,

**Olivia** [00:11:42] yeah. It was SWE-Bench Pro. On the other hand we don’t see this.

[00:12:00] I think they’re the auto agent found some, like very light evidence that maybe a couple models might be very lightly familiar with like one or two of the source repositories, but it’s very different than SWE-Bench verified. So less contamination is good.

**Mia** [00:12:01] I think there also like we should expect that at some point like that, that’s not going to be like the right benchmark anymore and like it’s a field we kind of have to continue to like move on and like find harder and more representative.

[00:12:01] Yeah, problems that we can match our capabilities on.

**Swyx** [00:12:28] Awesome.

## [00:12:31] What Great Coding Evals Measure

**Swyx** [00:12:28] So let’s go into that. I think that there are a lot of I think we also practiced in the, in the pre-chat was, well, people feel a qualitative difference when they’re using 5.1 to 5.2 to 5.3, and it’s not super expressed in the these benchmarks because they, they are on a number of these things.

[00:12:28] What capabilities do you really want to benchmark in a, in a ideal coding benchmark? You know, I guess like agent coding, benchmark, whatever you call it.

**Olivia** [00:12:47] I mean, one thing is kind of open-ended design decisions, places where the problem maybe is a little bit underspecified and seeing if the model can make reasonable design decisions.

**Swyx** [00:13:00] What’s a reasonable prompt for that? Like this vibe Code me. B2B SaaS to make no mistakes or, you know, that’s, that’s the meme, but like, okay. What’s like, what’s like an actual usable open-ended problem like that? Like,

**Olivia** [00:13:00] Sure. I mean, maybe an example could be finding a way to speed up a particular.

[00:13:00] Part of a code base, but there might be multiple different ways to

**Swyx** [00:13:22] Yeah, there are dedicated performance benchmarks. I think you guys have one. So, efficiency or is that, is that, oh, no, I think that’s, that’s off your group. But yeah. Yeah, I mean that, that, that is a good one.

**Mia** [00:13:22] I think there’s just many, many things that people like value about working with, with software engineering agents.

[00:13:22] They think Swyx, Swyx bank’s verified, obviously measured like some. Still measures like some important capability, which is like given like a description of a GitHub issue, can you produce like a patch that solves that issue, you know, satisfactorily. And like, obviously there’s like some issues with the, with the benchmark that needs that.

[00:14:00] Now that we are like 80%, we don’t really trust like further improvements on it, but like it does match on something that is like a via, via like capability of motors. But I think. As a field, we are like moving beyond sort of, you know, can my coding agent like solve a small like GitHub issue for me?

[00:14:05] Right? And so we are starting to look at like much more long, longer term tasks, right? Like. That don’t take like 15 minutes, but maybe like hour, sometimes days. And then beyond sort of like what kind of tasks can my agent solve? Like there might be things that are kind of a bit harder to grasp, right? Like Olivia talked about sort of like, does it have like design taste, right?

[00:14:23] Like does it solve the problem the way that you know. My team likes to solve problems. Okay. Is the code nice? Right? Like is it, is it well written? Like, is it sort of like clean code, right? Like people care about these, is it maintainable in the future? People care about a lot of these, maybe less tangible less tangible and like harder to measure, frankly.

[00:15:00] Things that, that are still like super meaningful for people that are working with coding agents?

**Swyx** [00:15:14] Yeah, so I mean these are all qualities that are obviously the, no longer the low hanging fruit. Like we have no idea how to eat all this. I think the, the, the simple question maybe that the, that there’s sort of two function road.

[00:15:14] One is the sort of very human intensive, money intensive path, which is hire a bunch of contractors and try to annotate this. The other is. Use an LLM to to proxy it and try to align the LLM so that it can give you a reasonable proxy. Which of those would you want? I want You wanna do both?

**Mia** [00:15:30] I think like maybe you should talk about GDP law as like an example.

**Olivia** [00:15:30] Sure. So GDP be is an eval that was again produced by a collaboration between human data team and the front of evals team. And it’s trying to measure whether agents can do kind of a variety of like, real world white collar work. That was an eval where grading is very hard requires kind of a lot of kind of like knowing knowledge on exactly what are you looking for in each different context?

**Swyx** [00:16:00] Yeah. Across like. 15, 16 white collar jobs. Professions like I, that take of a significant part of gdp, DP, which is great.

**Olivia** [00:16:00] No, it’s high level professions and then a lot of like different granular sub professions.

**Swyx** [00:16:00] I have said like I’m a big fan. It’s so, it, it is, this is the eval for agi. I basically,

**Olivia** [00:16:00] but, but part it because it was so hard to.

[00:16:00] It required so much kind of like domain knowledge that the human data team hired like a lot of people from these professions to be very involved in creating tasks and creating the gold solutions and trying to help create rubrics and so forth so they can create it lively.

**Swyx** [00:16:36] So basically take the GDP valve, which is a generalist, take that same approach to apply it to code and you roughly have like a, a rough road.

**Mia** [00:16:36] I think it’s an interesting yeah. Solution. I think what you’re pointing out as an important problem, which is sort of this. This, like how realistic is it? And like, do you know what, what we want to do is like. Coding agents should write code that, you know, we think is good. And so it’s like asking human, it’s actually like a, a good way to ensure that is also kind of a slower, like, complex way to do that.

[00:17:00] And so part of why I think, you know, three Venture verified ended up being super popular and where we are seeing like all benchmarks, like this being super popular. I was like, it’s very easy. It could even be easier. Validating that a solution passes all the tests. It’s like fairly trivial once you can like run the tests in, in like your, on your computer or wherever you’re running them and you can kind of like, okay, is it correct or is it not correct?

[00:17:23] And you can kind of aggregate that and that it’s super simple, but it doesn’t tell you. It’s like, you know, did the method like solve the problem? Like wow, like, you know, I agree with like what if actually like. An open source maintainer of that project have like merged that pr like that, it doesn’t tell you, but there is a lot of value in having benchmarks that are both like easy to compare across the industry and also that can be sort of run really fast without human involvement.

**Swyx** [00:18:00] Yeah. Amazing.

## [00:18:17] Beyond Tests Dollars And Autonomy

**Swyx** [00:18:00] Your teams also put out other kinds of evals that are related, like the, I think there’s an RL. Paper, bench paper. And then they sort of like the more sort of recursive self-improvement type evals. How much should that figure into mainstream coding evals? You know, like is there, is there some way in which those things join together?

**Olivia** [00:18:00] So we were asking like, should we build, should also be voting evals for the self-improvement evals? Are you saying do coding evals currently cover that? Mine?

**Swyx** [00:18:00] I think I, I, I just think like those are some of the most advanced EVs that we have. We’re not using them in a normal path. And it’s just, it’s an interesting split between, well here’s evals for coding normal things, and then here’s the one for machine learning that is like completely different.

[00:19:00] Right? Yeah. I think you would be get what I mean. That’s mostly a safety argument, I guess. But also like it’s actually really useful for people to understand if the model is really good at. Like AI code basically.

**Olivia** [00:19:03] Yeah. Oh yeah. Like, my guess is that part of the reason that a lot of benchmarks so far haven’t focused as much on the AI coding is just a question of like, what data sets are easy to gather.

[00:19:03] Yeah. Because a lot of the, like, you know, state of the art AI code bases are proprietary. So if we make evals for that, like we’re probably not gonna release them. And it’s harder for people in the field to make evals that kind of measure. Like, is this a realistic. Research, coding, workflow. I do think that it’s good for the field to try to measure these skills in a public way and think it’s just harder to make it realistic.

**Swyx** [00:19:24] And then one more thing that a lot of people are trying to do, which is like sort of, well, in, instead of like a percentage of zero to 100, maybe we red denominate in dollars. Right? So you have freelancer and all that. Other people are doing like vending, bench, whatever. Any, any alpha in those or are they, are they you, you still want like a traditional academic benchmark.

**Mia** [00:20:00] I think in a way, like there’s like different ways to measure the same thing, right? If we’re like, oh, this is like how much money it produces. Yeah. It’s a fairly similar thing to saying like, oh, this problem would take like a human, you know, two hours to solve or something like that. Usually they, they’re like fairly like correlated, right?

[00:20:00] Like, however you know much, it would take like a human to solve. That problem kind of determines. The value that we ascribe like a solution. And so I, I do think that is like an important thing is like how complex and how sort of long running are the tasks that we’re like able to entrust our agents with.

**Olivia** [00:20:20] Yeah.

**Mia** [00:20:20] And so I think that that’s like an important piece, but I, I think here sort of. Monetary value, time, complexity. They all kind of like try to capture like a similar thing.

**Swyx** [00:20:20] Yeah. Okay. So there, there are proxies for some amount of increasing capacity that we wanna measure. I think that’s a good thing. I think the only other sort of major player in this field is meter, which has done the sort of long grass and congrats.

[00:21:00] You guys have completely destroyed the curve for that. Any takes on that? Obviously you’ve come up really well, so like it looks good, but I don’t know if like that approach is something that you wanna incorporate in your own work, making it else. This is the long autonomy pass eval. You’re,

**Mia** [00:21:07] yeah, yeah.

[00:21:07] No, from we are, and, and, and we, we, we work with, with meter on these evaluations. So like we, we do appreciate them. I think then they’re using time, right? They’re not using money. So I think like that was a, your question. I think like complexity, however we can sort of like quantify it, is really important to understand like where our motive are, are are getting to.

**Swyx** [00:21:21] Okay. Com complexity is the abstract thing and it projects down the time, projects down to. Story points, whatever dollars. Great.

## [00:21:49] Preparedness And Future Directions

**Swyx** [00:21:21] One last question on just like, just the overall preparedness framework is you know, I was actually kind of looking at, people mentioned the preparedness framework a lot.

[00:21:21] I don’t think it’s well explained to a lot of people. And you actually have a nice website where it’s like I think it’s like test and like inform and teach something. And I, I feel like you, you actually do a lot of work there and, and I don’t know if you wanna talk about how the preparedness framework applies.

**Olivia** [00:22:00] So the preparedness framework is open eyes, kinda like public framework for how we track frontier risks. So these are kind of capabilities that are typically dual use, like you can use ‘em for good things or bad things, but we wanna at least keep an eye out for the bad things to make sure that we ha both we as a company and like the broader society are kind of prepared to handle the potential downsides.

[00:22:00] And so at the moment we kind of track three different categories. One is kind of bio risk, another is cybersecurity, and a third is kind of research automation and model autonomy. And that’s kind of what ties the most into the SWE-Bench, where Got it. Where coding is not all of automating research, but it is one very important key component.

[00:22:28] And so we initially created Swyx Venture verified as part of like building out evals for that mono autonomy work stream. And now. I think for like we have to move beyond that, towards, I’m looking more at like, can models actually start to actually automate research workflow.

**Swyx** [00:23:00] Yeah. Amazing.

[00:23:00] Okay. Abi, anything else to add on just the general, what people should know about preparedness and how evals and human data and alignment all work together at that?

**Mia** [00:23:03] I think maybe the thing that I would say is that we really appreciate, we, we work really hard to build these events and, and so we, that’s where we published.

[00:23:03] SWE-Bench ver verified and that’s where we’re like sharing GDP via these sorts of things. We also deeply appreciate like other people and the entire field to kind of build EVAs and, and share them. And we use them like SWE-Bench program, like, yes, but that’s a better eva now we should use them. So would really encourage people to find more ways to.

[00:23:23] Create and share ev events that we can, we and the entire field can use to measure like progress.

**Swyx** [00:23:43] Yeah.

**Mia** [00:23:43] On, on, on like a variety of capabilities, including, including coding, because it’s important to understand, so where we are,

**Swyx** [00:23:43] me, I had to leave. But we’re, we are just kind of talking a little bit about like the, the future directions that we want evals to go.

**Mia** [00:24:00] Mm-hmm.

**Swyx** [00:24:00] And I, I think here, here we can dive in on like, give us. Good work on these, these, these things. We’ll talk to you, you know here’s your platform to make a call. Look for what you’re looking for.

**Olivia** [00:24:00] I think a few things that would be useful. I’d say first of all, really, really hard task. Like the kinds of things that would take top-notch engineers months or teams weeks would be quite good.

[00:24:00] Especially if. Breeding is reliable and breeding is like, you know, you have for example, like rubrics that have been sourced and validated by many people in the field. I think that’d be quite valuable. I think also benchmarks on kind of creating products end to end. I think as people are like putting more, that would be quite useful.

[00:24:26] I think. A third thing that I’d say that is maybe not quite an eval, but I think it’s still relevant to the kind of overall mission of like. We as a field and as a world should be tracking, like where are these capabilities going? I’d like to see more metrics the tracking, like real world usage.

[00:24:42] Like how much is AI actually being used in the field and how much is it, you know, replacing people’s jobs? How much is it? You know, augmenting people is speeding people up, just like real world metrics. Yeah,

**Swyx** [00:25:00] yeah. The, the, the replacement thing is always like a sensitive one on the, on the sort of PR side of things.

[00:25:00] But you know, we create new jobs that, that manage the old jobs and that’s how it’s yourself like you know, I think in terms of the frontier evals that, that open I is really going to excited to push like you, you put out really good work every single time. What should people expect from, from OPI itself?

**Olivia** [00:25:12] I’m not sure I can say what we’re gonna

**Swyx** [00:25:12] general directions,

**Olivia** [00:25:12] I mean, general directions. I think looking at real world impact, like real world real to,

**Swyx** [00:25:12] yeah, whatever.

**Olivia** [00:25:12] That kind of stuff. Yeah. Yeah.

**Swyx** [00:25:12] Yeah. Amazing. Okay. Well, I’m excited for more real world impact. I, I think you guys have, you know, really made a lot of progress and I think taking a lot of industry leadership for C Bench verified and, and now moving on to C Orange Pro.

[00:25:12] So thank you for doing this. Thank you for being so transparent. And I think people will respond in kind. Yeah,

**Olivia** [00:25:50] for your time.

**Swyx** [00:25:50] Thank you.
