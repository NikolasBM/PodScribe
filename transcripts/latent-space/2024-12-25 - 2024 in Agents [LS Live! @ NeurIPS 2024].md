---
podcast: "latent-space"
podcast_title: "Latent Space"
title: "2024 in Agents [LS Live! @ NeurIPS 2024]"
date: 2024-12-25
url: "https://www.latent.space/p/2024-agents"
guid: "substack:153568377"
host: "Swyx"
transcript_source: "publisher"
---

# 2024 in Agents [LS Live! @ NeurIPS 2024]

## [00:00:29] State of LLM Agents in 2024

**Speaker 9** [00:00:00] Our next keynote covers the state of LLM agents. With the triumphant return of Professor Graham Newbig of CMU and OpenDevon, now a startup known as AllHands. The renamed OpenHands has done extremely well this year, as they end the year sitting comfortably at number one on the hardest SWE Benchful leaderboard at 29%.

**Speaker 9** [00:00:00] Though, on the smaller SWE bench verified, they are at 53 percent behind Amazon Q Devlo and OpenAI's self reported O3 results at 71. 7%. Many are saying that 2025 is going to be the year of agents, with OpenAI, DeepMind, and Anthropic setting their sights on consumer and coding agents. Vision based computer using agents and multi agent systems.

**Speaker 9** [00:01:00] There has been so much progress on the practical reliability and applications of agents in all domains, from the huge launch of Cognition AI's Devon this year, to the sleeper hit of Cursor Composer and recent guest Codium's Windsurf Cascade in the IDE arena. To the explosive revenue growth of recent guests StackBlitz's Bolt, Lovable, and Vercel's vZero.

**Speaker 9** [00:01:00] And the unicorn rounds and high profile movements of customer support agents like Sierra, now worth 4 billion, and search agents like Perplexity, now worth 9 billion. We wanted to take a little step back to understand the most notable papers of the year in agents, and Graham indulged with his list of eight perennial problems in building agents.

**Speaker 9** [00:02:00] As always, don't forget to check our show notes for all the selected best papers of 2024, and for the YouTube link to their talk. Graham's slides were especially popular online, and we are honoured to have him. Watch out and take care!

## [00:02:20] Professor Graham Newbig's Insights on Agents

**Speaker** [00:02:00] Okay hi everyone. So I was given the task of talking about agents in 2024, and this is An impossible task because there are so many agents, so many agents in 2024. So this is going to be strongly covered by like my personal experience and what I think is interesting and important, but I think it's an important topic.

**Speaker** [00:02:00] So let's go ahead. So the first thing I'd like to think about is let's say I gave you you know, a highly competent human, some tools. Let's say I gave you a web browser and a terminal or a file system. And the ability to edit text or code. What could you do with that? Everything. Yeah.

**Speaker** [00:03:00] Probably a lot of things. This is like 99 percent of my, you know, daily daily life, I guess. When I'm, when I'm working. So, I think this is a pretty powerful tool set, and I am trying to do, and what I think some other people are trying to do, is come up with agents that are able to, you know, manipulate these things.

**Speaker** [00:03:00] Web browsing, coding, running code in successful ways. So there was a little bit about my profile. I'm a professor at CMU, chief scientist at All Hands AI, building open source coding agents. I'm maintainer of OpenHands, which is an open source coding agent framework. And I'm also a software developer and I, I like doing lots of coding and, and, you know, shipping new features and stuff like this.

**Speaker** [00:03:00] So building agents that help me to do this, you know, is kind of an interesting thing, very close to me.

## [00:03:57] Live Demo: Coding Agents in Action

**Speaker** [00:03:00] So the first thing I'd like to do is I'd like to try some things that I haven't actually tried before. If anybody has, you know, tried to give a live demo, you know, this is, you know very, very scary whenever you do it and it might not work.

**Speaker** [00:04:00] So it might not work this time either. But I want to show you like three things that I typically do with coding agents in my everyday work. I use coding agents maybe five to 10 times a day to help me solve my own problems. And so this is a first one. This is a data science task. Which says I want to create scatter plots that show the increase of the SWE bench score over time.

**Speaker** [00:04:00] And so I, I wrote a kind of concrete prompt about this. Agents work better with like somewhat concrete prompts. And I'm gonna throw this into open hands and let it work. And I'll, I'll go back to that in a second. Another thing that I do is I create new software. And I, I've been using a service a particular service.

**Speaker** [00:05:00] I won't name it for sending emails and I'm not very happy with it. So I want to switch over to this new service called resend. com, which makes it easier to send emails. And so I'm going to ask it to read the docs for the resend. com API and come up with a script that allows me to send emails. The input to the script should be a CSV file and the subject and body should be provided in Jinja2 templates.

**Speaker** [00:05:00] So I'll start another agent and and try to get it to do that for me.

**Speaker** [00:05:00] And let's go with the last one. The last one I do is. This is improving existing software and in order, you know, once you write software, you usually don't throw it away. You go in and, like, actually improve it iteratively. This software that I have is something I created without writing any code.

**Speaker** [00:05:00] It's basically software to monitor how much our our agents are contributing to the OpenHance repository. And on the, let me make that a little bit bigger, on the left side, I have the number of issues where it like sent a pull request. I have the number of issues where it like sent a pull request, whether it was merged in purple, closed in red, or is still open in green. And so these are like, you know, it's helping us monitor, but one thing it doesn't tell me is the total number. And I kind of want that feature added to this software.

**Speaker** [00:06:00] So I'm going to try to add that too. So. I'll take this, I'll take this prompt,

**Speaker** [00:06:00] and here I want to open up specifically that GitHub repo. So I'll open up that repo and paste in the prompt asking it. I asked it to make a pie chart for each of these and give me the total over the entire time period that I'm monitoring. So we'll do that. And so now I have let's see, I have some agents.

**Speaker** [00:07:00] Oh, this one already finished. Let's see. So this one already finished. You can see it finished analyzing the Swebench repository. It wrote a demonstration of, yeah, I'm trying to do that now, actually.

**Speaker** [00:07:00] It wrote a demonstration of how much each of the systems have improved over time. And I asked it to label the top three for each of the data sets. And so it labeled OpenHands as being the best one for SWE Bench Normal. For SWE Bench Verified, it has like the Amazon QAgent and OpenHands. For the SWE Bench Lite, it has three here over three over here.

**Speaker** [00:07:00] So you can see like. That's pretty useful, right? If you're a researcher, you do data analysis all the time. I did it while I was talking to all of you and making a presentation. So that's, that's pretty nice. I, I doubt the other two are finished yet. That would be impressive if the, yeah. So I think they're still working.

**Speaker** [00:08:00] So maybe we'll get back to them at the end of the presentation. But so these are the kinds of the, these are the kinds of things that I do every day with coding agents now. And it's or software development agents. It's pretty impressive.

## [00:08:20] Designing Effective Agents

**Speaker** [00:08:00] The next thing I'd like to talk about a little bit is things I worry about when designing agents.

**Speaker** [00:08:00] So we're designing agents to, you know, do a very difficult task of like navigating websites writing code, other things like this. And within 2024, there's been like a huge improvement in the methodology that we use to do this. But there's a bunch of things we think about. There's a bunch of interesting papers, and I'd like to introduce a few of them.

**Speaker** [00:08:00] So the first thing I worry about is the agent computer interface. Like, how do we get an agent to interact with computers? And, How do we provide agents with the tools to do the job? And within OpenHands we are doing the thing on the right, but there's also a lot of agents that do the thing on the left.

**Speaker** [00:09:00] So the thing on the left is you give like agents kind of granular tools. You give them tools like or let's say your instruction is I want to determine the most cost effective country to purchase the smartphone model, Kodak one the countries to consider are the USA, Japan, Germany, and India. And you have a bunch of available APIs.

**Speaker** [00:09:00] And. So what you do for some agents is you provide them all of these tools APIs as tools that they can call. And so in this particular case in order to solve this problem, you'd have to make about like 30 tool calls, right? You'd have to call lookup rates for Germany, you'd have to look it up for the US, Japan, and India.

**Speaker** [00:09:00] That's four tool goals. And then you go through and do all of these things separately. And the method that we adopt in OpenHands instead is we provide these tools, but we provide them by just giving a coding agent, the ability to call arbitrary Python code. And. In the arbitrary Python code, it can call these tools.

**Speaker** [00:10:00] We expose these tools as APIs that the model can call. And what that allows us to do is instead of writing 20 tool calls, making 20 LLM calls, you write a program that runs all of these all at once, and it gets the result. And of course it can execute that program. It can, you know, make a mistake. It can get errors back and fix things.

**Speaker** [00:10:00] But that makes our job a lot easier. And this has been really like instrumental to our success, I think. Another part of this is what tools does the agent need? And I, I think this depends on your use case, we're kind of extreme and we're only giving the agent five tools or maybe six tools.

**Speaker** [00:10:00] And what, what are they? The first one is program execution. So it can execute bash programs, and it can execute Jupyter notebooks. It can execute cells in Jupyter notebooks. So that, those are two tools. Another one is a file editing tool. And the file editing tool allows you to browse parts of files.

**Speaker** [00:11:00] And kind of read them, overwrite them, other stuff like this. And then we have another global search and replace tool. So it's actually two tools for file editing. And then a final one is web browsing, web browsing. I'm kind of cheating when I call it only one tool. You actually have like scroll and text input and click and other stuff like that.

**Speaker** [00:11:00] But these are basically the only things we allow the agent to do. What, then the question is, like, what if we wanted to allow it to do something else? And the answer is, well, you know, human programmers already have a bunch of things that they use. They have the requests PyPy library, they have the PDF to text PyPy library, they have, like, all these other libraries in the Python ecosystem that they could use.

**Speaker** [00:11:00] And so if we provide a coding agent with all these libraries, it can do things like data visualization and other stuff that I just showed you. So it can also get clone repositories and, and other things like this. The agents are super good at using the GitHub API also. So they can do, you know, things on GitHub, like finding all of the, you know, comments on your issues or checking GitHub actions and stuff.

**Speaker** [00:12:00] The second thing I think about is the human agent interface. So this is like how do we get humans to interact with agents? Bye. I already showed you one variety of our human agent interface. It's basically a chat window where you can browse through the agent's results and things like this. This is very, very difficult.

**Speaker** [00:12:00] I, I don't think anybody has a good answer to this, and I don't think we have a good answer to this, but the, the guiding principles that I'm trying to follow are we want to present enough info to the user. So we want to present them with, you know, what the agent is doing in the form of a kind of.

**Speaker** [00:12:00] English descriptions. So you can see here you can see here every time it takes an action, it says like, I will help you create a script for sending emails. When it runs a bash command. Sorry, that's a little small. When it runs a bash command, it will say ran a bash command. It won't actually show you the whole bash command or the whole Jupyter notebook because it can be really large, but you can open it up and see if you want to, by clicking on this.

**Speaker** [00:13:00] So like if you want to explore more, you can click over to the Jupyter notebook and see what's displayed in the Jupyter notebook. And you get like lots and lots of information. So that's one thing.

**Speaker** [00:13:00] Another thing is go where the user is. So like if the user's already interacting in a particular setting then I'd like to, you know, integrate into that setting, but only to a point. So at OpenHands, we have a chat UI for interaction. We have a GitHub plugin for tagging and resolving issues. So basically what you do is you Do at open hands agent and the open hands agent will like see that comment and be able to go in and fix things.

**Speaker** [00:13:00] So if you say at open hands agent tests are failing on this PR, please fix the tests. It will go in and fix the test for you and stuff like this. Another thing we have is a remote runtime for launching headless jobs. So if you want to launch like a fleet of agents to solve, you know five different problems at once, you can also do that through an API.

**Speaker** [00:14:00] So we have we have these interfaces and this probably depends on the use case. So like, depending if you're a coding agent, you want to do things one way. If you're a like insurance auditing agent, you'll want to do things other ways, obviously.

## [00:14:13] Choosing the Right Language Model for Agents

**Speaker** [00:14:00] Another thing I think about a lot is choosing a language model.

**Speaker** [00:14:00] And for agentic LMs we have to have a bunch of things work really well. The first thing is really, really good instruction following ability. And if you have really good instruction following ability, it opens up like a ton of possible applications for you. Tool use and coding ability. So if you provide tools, it needs to be able to use them well.

**Speaker** [00:14:00] Environment understanding. So it needs, like, if you're building a web agent, it needs to be able to understand web pages either through vision or through text. And error awareness and recovery ability. So, if it makes a mistake, it needs to be able to, you know, figure out why it made a mistake, come up with alternative strategies, and other things like this.

**Speaker** [00:14:00] Under the hood, in all of the demos that I did now Cloud, we're using Cloud. Cloud has all of these abilities very good, not perfect, but very good. Most others don't have these abilities quite as much. So like GPT 4. 0 doesn't have very good error recovery ability. And so because of this, it will go into loops and do the same thing over and over and over again.

**Speaker** [00:15:00] Whereas Claude does not do this. Claude, if you, if you use the agents enough, you get used to their kind of like personality. And Claude says, Hmm, let me try a different approach a lot. So, you know, obviously it's been trained in some way to, you know, elicit this ability. We did an evaluation. This is old.

**Speaker** [00:15:00] And we need to update this basically, but we evaluated CLOD, mini LLAMA 405B, DeepSeq 2. 5 on being a good code agent within our framework. And CLOD was kind of head and shoulders above the rest. GPT 40 was kind of okay. The best open source model was LLAMA 3. 1 405B. This needs to be updated because this is like a few months old by now and, you know, things are moving really, really fast.

**Speaker** [00:16:00] But I still am under the impression that Claude is the best. The other closed models are, you know, not quite as good. And then the open models are a little bit behind that. Grok, I, we haven't tried Grok at all, actually. So, it's a good question. If you want to try it I'd be happy to help.

**Speaker** [00:16:00] Cool.

## [00:16:24] Planning and Workflow for Agents

**Speaker** [00:16:00] Another thing is planning. And so there's a few considerations for planning. The first one is whether you have a curated plan or you have it generated on the fly. And so for solving GitHub issues, you can kind of have an overall plan. Like the plan is first reproduce. If there's an issue, first write tests to reproduce the issue or to demonstrate the issue.

**Speaker** [00:16:00] After that, run the tests and make sure they fail. Then go in and fix the tests. Run the tests again to make sure they pass and then you're done. So that's like a pretty good workflow for like solving coding issues. And you could curate that ahead of time. Another option is to let the language model basically generate its own plan.

**Speaker** [00:17:00] And both of these are perfectly valid. Another one is explicit structure versus implicit structure. So let's say you generate a plan. If you have explicit structure, you could like write a multi agent system, and the multi agent system would have your reproducer agent, and then it would have your your bug your test writer agent, and your bug fixer agent, and lots of different agents, and you would explicitly write this all out in code, and then then use it that way.

**Speaker** [00:17:00] On the other hand, you could just provide a prompt that says, please do all of these things in order. So in OpenHands, we do very light planning. We have a single prompt. We don't have any multi agent systems. But we do provide, like, instructions about, like, what to do first, what to do next, and other things like this.

**Speaker** [00:17:00] I'm not against doing it the other way. But I laid out some kind of justification for this in this blog called Don't Sleep on Single Agent Systems. And the basic idea behind this is if you have a really, really good instruction following agent it will follow the instructions as long as things are working according to your plan.

**Speaker** [00:18:00] But let's say you need to deviate from your plan, you still have the flexibility to do this. And if you do explicit structure through a multi agent system, it becomes a lot harder to do that. Like, you get stuck when things deviate from your plan. There's also some other examples, and I wanted to introduce a few papers.

**Speaker** [00:18:00] So one paper I liked recently is this paper called CoAct where you generate plans and then go in and fix them. And so the basic idea is like, if you need to deviate from your plan, you can You know, figure out that your plan was not working and go back and deviate from it.

**Speaker** [00:18:00] Another thing I think about a lot is specifying common workflows. So we're trying to tackle a software development and I already showed like three use cases where we do software development and when we. We do software development, we do a ton of different things, but we do them over and over and over again.

**Speaker** [00:19:00] So just to give an example we fix GitHub actions when GitHub actions are failing. And we do that over and over and over again. That's not the number one thing that software engineers do, but it's a, you know, high up on the list. So how can we get a list of all of, like, the workflows that people are working on?

**Speaker** [00:19:00] And there's a few research works that people have done in this direction. One example is manual prompting. So there's this nice paper called STEP that got state of the art on the WebArena Web Navigation Benchmark where they came up with a bunch of manual workflows for solving different web navigation tasks.

**Speaker** [00:19:00] And we also have a paper recently called Agent Workflow Memory where the basic idea behind this is we want to create self improving agents that learn from their past successes. And the way it works is is we have a memory that has an example of lots of the previous workflows that people have used. And every time the agent finishes a task and it self judges that it did a good job at that task, you take that task, you break it down into individual workflows included in that, and then you put it back in the prompt for the agent to work next time.

**Speaker** [00:20:00] And this we demonstrated that this leads to a 22. 5 percent increase on WebArena after 40 examples. So that's a pretty, you know, huge increase by kind of self learning and self improvement.

**Speaker** [00:20:00] Another thing is exploration. Oops. And one thing I think about is like, how can agents learn more about their environment before acting? And I work on coding and web agents, and there's, you know, a few good examples of this in, in both areas. Within coding, I view this as like repository understanding, understanding the code base that you're dealing with.

**Speaker** [00:20:00] And there's an example of this, or a couple examples of this, one example being AgentList. Where they basically create a map of the repo and based on the map of the repo, they feed that into the agent so the agent can then navigate the repo and and better know where things are. And for web agents there's an example of a paper called Bagel, and basically what they do is they have the agent just do random tasks on a website, explore the website, better understand the structure of the website, and then after that they they feed that in as part of the product.

**Speaker** [00:21:00] Part seven is search. Right now in open hands, we just let the agent go on a linear search path. So it's just solving the problem once. We're using a good agent that can kind of like recover from errors and try alternative things when things are not working properly, but still we only have a linear search path.

**Speaker** [00:21:00] But there's also some nice work in 2024 that is about exploring multiple paths. So one example of this is there's a paper called Tree Search for Language Agents. And they basically expand multiple paths check whether the paths are going well, and if they aren't going well, you rewind back. And on the web, this is kind of tricky, because, like, how do you rewind when you accidentally ordered something you don't want on Amazon?

**Speaker** [00:22:00] It's kind of, you know, not, not the easiest thing to do. For code, it's a little bit easier, because you can just revert any changes that you made. But I, I think that's an interesting topic, too.

## [00:22:21] Evaluation and Future Predictions for Agents

**Speaker** [00:22:00] And then finally evaluation. So within our development for evaluation, we want to do a number of things. The first one is fast sanity checks.

**Speaker** [00:22:00] And in order to do this, we want things we can run really fast, really really cheaply. So for web, we have something called mini world of bits, which is basically these trivial kind of web navigation things. We have something called the Adder Code Editing Benchmark, where it's just about editing individual files that we use.

**Speaker** [00:22:00] But we also want highly realistic evaluation. So for the web, we have something called WebArena that we created at CMU. This is web navigation on real real open source websites. So it's open source websites that are actually used to serve shops or like bulletin boards or other things like this.

**Speaker** [00:23:00] And for code, we use Swebench, which I think a lot of people may have heard of. It's basically a coding benchmark that comes from real world pull requests on GitHub. So if you can solve those, you can also probably solve other real world pull requests. I would say we still don't have benchmarks for the fur full versatility of agents.

**Speaker** [00:23:00] So, for example We don't have benchmarks that test whether agents can code and do web navigation. But we're working on that and hoping to release something in the next week or two. So if that sounds interesting to you, come talk to me and I, I will tell you more about it.

**Speaker** [00:23:00] Cool. So I don't like making predictions, but I was told that I should be somewhat controversial, I guess, so I will, I will try to do it try to do it anyway, although maybe none of these will be very controversial. Um, the first thing is agent oriented LLMs like large language models for agents.

**Speaker** [00:24:00] My, my prediction is every large LM trainer will be focusing on training models as agents. So every large language model will be a better agent model by mid 2025. Competition will increase, prices will go down, smaller models will become competitive as agents. So right now, actually agents are somewhat expensive to run in some cases, but I expect that that won't last six months.

**Speaker** [00:24:00] I, I bet we'll have much better agent models in six months. Another thing is instruction following ability, specifically in agentic contexts, will increase. And what that means is we'll have to do less manual engineering of agentic workflows and be able to do more by just prompting agents in more complex ways.

**Speaker** [00:24:00] Cloud is already really good at this. It's not perfect, but it's already really, really good. And I expect the other models will catch up to Cloud pretty soon. Error correction ability will increase, less getting stuck in loops. Again, this is something that Cloud's already pretty good at and I expect the others will, will follow.

**Speaker** [00:25:00] Agent benchmarks. Agent benchmarks will start saturating.

**Speaker** [00:25:00] And Swebench I think WebArena is already too easy. It, it is, it's not super easy, but it's already a bit too easy because the tasks we do in there are ones that take like two minutes for a human. So not, not too hard. And kind of historically in 2023 our benchmarks were too easy. So we built harder benchmarks like WebArena and Swebench were both built in 2023.

## [00:25:31] Future of Agent Development

**Speaker** [00:25:00] In 2024, our agents were too bad, so we built agents and now we're building better agents. In 2025, our benchmarks will be too easy, so we'll build better benchmarks, I'm, I'm guessing. So, I would expect to see much more challenging agent benchmarks come out, and we're already seeing some of them.

**Speaker** [00:25:00] In 2026, I don't know. I didn't write AGI, but we'll, we'll, we'll see.

## [00:25:56] Human-Agent Interaction Challenges

**Speaker** [00:25:00] Then the human agent computer interface. I think one thing that we'll want to think about is what do we do at 75 percent success rate at things that we like actually care about? Right now we have 53 percent or 55 percent on Swebench verified, which is real world GitHub PRs.

**Speaker** [00:26:00] My impression is that the actual. Actual ability of models is maybe closer to 30 to 40%. So 30 to 40 percent of the things that I want an agent to solve on my own repos, it just solves without any human intervention. 80 to 90 percent it can solve without me opening an IDE. But I need to give it feedback.

**Speaker** [00:26:00] So how do we, how do we make that interaction smooth so that humans can audit? The work of agents that are really, really good, but not perfect is going to be a big challenge.

## [00:26:48] Expanding Agent Use Beyond Programming

**Speaker** [00:26:00] How can we expose the power of programming agents to other industries? So like as programmers, I think not all of us are using agents every day in our programming, although we probably will be in in months or maybe a year.

**Speaker** [00:27:00] But I, I think it will come very naturally to us as programmers because we know code. We know, you know. Like how to architect software and stuff like that. So I think the question is how do we put this in the hands of like a lawyer or a chemist or somebody else and have them also be able to, you know, interact with it as naturally as we can.

## [00:27:25] Redesigning Systems for Agent Efficiency

**Speaker** [00:27:00] Another interesting thing is how can we redesign our existing systems for agents? So we had a paper on API based web agents, and basically what we showed is If you take a web agent and the agent interacts not with a website, but with APIs, the accuracy goes way up just because APIs are way easier to interact with.

**Speaker** [00:27:00] And in fact, like when I ask the, well, our agent, our agent is able to browse websites, but whenever I want it to interact with GitHub, I tell it do not browse the GitHub website. Use the GitHub API because it's way more successful at doing that. So maybe, you know, every website is going to need to have an API because we're going to be having agents interact with them.

## [00:28:03] Accelerating Progress with Agent Technology

**Speaker** [00:28:00] About progress, I think progress will get faster. It's already fast. A lot of people are already overwhelmed, but I think it will continue. The reason why is agents are building agents. And better agents will build better agents faster. So I expect that you know, if you haven't interacted with a coding agent yet, it's pretty magical, like the stuff that it can do.

**Speaker** [00:28:00] So yeah.

## [00:28:28] Call to Action for Open Source Contributions

**Speaker** [00:28:00] And I have a call to action. I'm honestly, like I've been working on, you know, natural language processing and, and Language models for what, 15 years now. And even for me, it's pretty impressive what like AI agents powered by strong language models can do. On the other hand, I believe that we should really make these powerful tools accessible.

**Speaker** [00:28:00] And what I mean by this is I don't think like, you know, We, we should have these be opaque or limited to only a set, a certain set of people. I feel like they should be affordable. They shouldn't be increasing the, you know, difference in the amount of power that people have. If anything, I'd really like them to kind of make it It's possible for people who weren't able to do things before to be able to do them well.

**Speaker** [00:29:00] Open source is one way to do that. That's why I'm working on open source. There are other ways to do that. You know, make things cheap, make things you know, so you can serve them to people who aren't able to afford them. Easily, like Duolingo is one example where they get all the people in the US to pay them 20 a month so that they can give all the people in South America free, you know, language education, so they can learn English and become, you know like, and become, you know, More attractive on the job market, for instance.

**Speaker** [00:29:00] And so I think we can all think of ways that we can do that sort of thing. And if that resonates with you, please contribute. Of course, I'd be happy if you contribute to OpenHands and use it. But another way you can do that is just use open source solutions, contribute to them, research with them, and train strong open source models.

**Speaker** [00:30:00] So I see, you know, Some people in the room who are already training models. It'd be great if you could train models for coding agents and make them cheap. And yeah yeah, please. I, I was thinking about you among others. So yeah, that's all I have. Thanks.

**Speaker 2** [00:30:00] Slight, slightly controversial. Tick is probably the nicest way to say hot ticks. Any hot ticks questions, actual hot ticks?

**Speaker** [00:30:00] Oh, I can also show the other agents that were working, if anybody's interested, but yeah, sorry, go ahead.

## [00:30:36] Q&A: Agent Performance and Benchmarks

**Speaker 3** [00:30:00] Yeah, I have a couple of questions. So they're kind of paired, maybe. The first thing is that you said that You're estimating that your your agent is successfully resolving like something like 30 to 40 percent of your issues, but that's like below what you saw in Swebench.

**Speaker 3** [00:30:00] So I guess I'm wondering where that discrepancy is coming from. And then I guess my other second question, which is maybe broader in scope is that like, if, if you think of an agent as like a junior developer, and I say, go do something, then I expect maybe tomorrow to get a Slack message being like, Hey, I ran into this issue.

**Speaker 3** [00:31:00] How can I resolve it? And, and, like you said, your agent is, like, successfully solving, like, 90 percent of issues where you give it direct feedback. So, are you thinking about how to get the agent to reach out to, like, for, for planning when it's, when it's stuck or something like that? Or, like, identify when it runs into a hole like that?

**Speaker** [00:31:00] Yeah, so great. These are great questions. Oh,

**Speaker 3** [00:31:00] sorry. The third question, which is a good, so this is the first two. And if so, are you going to add a benchmark for that second question?

**Speaker** [00:31:00] Okay. Great. Yeah. Great questions. Okay. So the first question was why do I think it's resolving less than 50 percent of the issues on Swebench?

**Speaker** [00:31:00] So first Swebench is on popular open source repos, and all of these popular open source repos were included in the training data for all of the language models. And so the language models already know these repos. In some cases, the language models already know the individual issues in Swebench.

**Speaker** [00:32:00] So basically, like, some of the training data has leaked. And so it, it definitely will overestimate with respect to that. I don't think it's like, you know, Horribly, horribly off but I think, you know, it's boosting the accuracy by a little bit. So, maybe that's the biggest reason why. In terms of asking for help, and whether we're benchmarking asking for help yes we are.

**Speaker** [00:32:00] So one one thing we're working on now, which we're hoping to put out soon, is we we basically made SuperVig. Sweep edge issues. Like I'm having a, I'm having a problem with the matrix multiply. Please help. Because these are like, if anybody's run a popular open source, like framework, these are what half your issues are.

**Speaker** [00:32:00] You're like users show up and say like, my screen doesn't work. What, what's wrong or something. And so then you need to ask them questions and how to reproduce. So yeah, we're, we're, we're working on that. I think. It, my impression is that agents are not very good at asking for help, even Claude. So like when, when they ask for help, they'll ask for help when they don't need it.

**Speaker** [00:33:00] And then won't ask for help when they do need it. So this is definitely like an issue, I think.

**Speaker 4** [00:33:00] Thanks for the great talk. I also have two questions.

## [00:33:23] Q&A: Web Agents and Interaction Methods

**Speaker 4** [00:33:00] It's first one can you talk a bit more about how the web agent interacts with So is there a VLM that looks at the web page layout and then you parse the HTML and select which buttons to click on? And if so do you think there's a future where there's like, so I work at Bing Microsoft AI.

**Speaker 4** [00:33:00] Do you think there's a future where the same web index, but there's an agent friendly web index where all the processing is done offline so that you don't need to spend time. Cleaning up, like, cleaning up these TML and figuring out what to click online. And any thoughts on, thoughts on that?

**Speaker** [00:33:00] Yeah, so great question. There's a lot of work on web agents. I didn't go into, like, all of the details, but I think there's There's three main ways that agents interact with websites. The first way is the simplest way and the newest way, but it doesn't work very well, which is you take a screenshot of the website and then you click on a particular pixel value on the website.

**Speaker** [00:34:00] And Like models are not very good at that at the moment. Like they'll misclick. There was this thing about how like clawed computer use started like looking at pictures of Yellowstone national park or something like this. I don't know if you heard about this anecdote, but like people were like, oh, it's so human, it's looking for vacation.

**Speaker** [00:34:00] And it was like, no, it probably just misclicked on the wrong pixels and accidentally clicked on an ad. So like this is the simplest way. The second simplest way. You take the HTML and you basically identify elements in the HTML. You don't use any vision whatsoever. And then you say, okay, I want to click on this element.

**Speaker** [00:34:00] I want to enter text in this element or something like that. But HTML is too huge. So it actually, it usually gets condensed down into something called an accessibility tree, which was made for screen readers for visually impaired people. And So that's another way. And then the third way is kind of a hybrid where you present the screenshot, but you also present like a textual summary of the output.

**Speaker** [00:35:00] And that's the one that I think will probably work best. What we're using is we're just using text at the moment. And that's just an implementation issue that we haven't implemented the. Visual stuff yet, but that's kind of like we're working on it now. Another thing that I should point out is we actually have two modalities for web browsing.

**Speaker** [00:35:00] Very recently we implemented this. And the reason why is because if you want to interact with full websites you will need to click on all of the elements or have the ability to click on all of the elements. But most of our work that we need websites for is just web browsing and like gathering information.

**Speaker** [00:35:00] So we have another modality where we convert all of it to markdown because that's like way more concise and easier for the agent to deal with. And then can we create an index specifically for agents, maybe a markdown index or something like that would be, you know, would make sense. Oh, how would I make a successor to Swebench?

**Speaker** [00:36:00] So I mean, the first thing is there's like live code bench, which live code bench is basically continuously updating to make sure it doesn't leak into language model training data. That's easy to do for Swebench because it comes from real websites and those real websites are getting new issues all the time.

**Speaker** [00:36:00] So you could just do it on the same benchmarks that they have there. There's also like a pretty large number of things covering various coding tasks. So like, for example, Swebunch is mainly fixing issues, but there's also like documentation, there's generating tests that actually test the functionality that you want.

**Speaker** [00:36:00] And there there was a paper by a student at CMU on generating tests and stuff like that. So I feel like. Swebench is one piece of the puzzle, but you could also have like 10 different other tasks and then you could have like a composite benchmark where you test all of these abilities, not just that particular one.

**Speaker** [00:37:00] Well, lots, lots of other things too, but

**Speaker 2** [00:37:00] Question from across. Use your mic, it will help. Um,

**Speaker 5** [00:37:00] Great talk. Thank you.

## [00:37:16] Q&A: Agent Architectures and Improvements

**Speaker 5** [00:37:00] My question is about your experience designing agent architectures. Specifically how much do you have to separate concerns in terms of tasks specific agents versus having one agent to do three or five things with a gigantic prompt with conditional paths and so on.

**Speaker** [00:37:00] Yeah, so that's a great question. So we have a basic coding and browsing agent. And I won't say basic, like it's a good, you know, it's a good agent, but it does coding and browsing. And it has instructions about how to do coding and browsing. That is enough for most things. Especially given a strong language model that has a lot of background knowledge about how to solve different types of tasks and how to use different APIs and stuff like that.

**Speaker** [00:37:00] We do have a mechanism for something called micro agents. And micro agents are basically something that gets added to the prompt when a trigger is triggered. Right now it's very, very rudimentary. It's like if you detect the word GitHub anywhere, you get instructions about how to interact with GitHub, like use the API and don't browse.

**Speaker** [00:38:00] Also another one that I just added is for NPM, the like JavaScript package manager. And NPM, when it runs and it hits a failure, it Like hits in interactive terminals where it says, would you like to quit? Yep. Enter yes. And if that does it, it like stalls our agent for the time out until like two minutes.

**Speaker** [00:38:00] So like I added a new microagent whenever it started using NPM, it would Like get instructions about how to not use interactive terminal and stuff like that. So that's our current solution. Honestly, I like it a lot. It's simple. It's easy to maintain. It works really well and stuff like that. But I think there is a world where you would want something more complex than that.

**Speaker 5** [00:38:00] Got it. Thank you.

**Speaker 6** [00:38:00] I got a question about MCP. I feel like this is the Anthropic Model Context Protocol. It seems like the most successful type of this, like, standardization of interactions between computers and agents. Are you guys adopting it? Is there any other competing standard?

**Speaker 6** [00:39:00] Anything, anything thought about it?

**Speaker** [00:39:00] Yeah, I think the Anth, so the Anthropic MCP is like, a way to It, it's essentially a collection of APIs that you can use to interact with different things on the internet. I, I think it's not a bad idea, but it, it's like, there's a few things that bug me a little bit about it.

**Speaker** [00:39:00] It's like we already have an API for GitHub, so why do we need an MCP for GitHub? Right. You know, like GitHub has an API, the GitHub API is evolving. We can look up the GitHub API documentation. So it seems like kind of duplicated a little bit. And also they have a setting where it's like you have to spin up a server to serve your GitHub stuff.

**Speaker** [00:40:00] And you have to spin up a server to serve your like, you know, other stuff. And so I think it makes, it makes sense if you really care about like separation of concerns and security and like other things like this, but right now we haven't seen, we haven't seen that. To have a lot more value than interacting directly with the tools that are already provided.

**Speaker** [00:40:00] And that kind of goes into my general philosophy, which is we're already developing things for programmers. You know,

**Speaker** [00:40:00] how is an agent different than from a programmer? And it is different, obviously, you know, like agents are different from programmers, but they're not that different at this point. So we can kind of interact with the interfaces we create for, for programmers. Yeah. I might change my mind later though.

**Speaker** [00:40:00] So we'll see.

**Speaker 7** [00:40:00] Yeah. Hi. Thanks. Very interesting talk. You were saying that the agents you have right now solve like maybe 30 percent of your, your issues out of the gate. I'm curious of the things that it doesn't do. Is there like a pattern that you observe? Like, Oh, like these are the sorts of things that it just seems to really struggle with, or is it just seemingly random?

**Speaker** [00:41:00] It's definitely not random. It's like, if you think it's more complex than it's. Like, just intuitively, it's more likely to fail. I've gotten a bit better at prompting also, so like, just to give an example it, it will sometimes fail to fix a GitHub workflow because it will not look at the GitHub workflow and understand what the GitHub workflow is doing before it solves the problem.

**Speaker** [00:41:00] So I, I think actually probably the biggest thing that it fails at is, um, er, that our, our agent plus Claude fails at is insufficient information gathering before trying to solve the task. And so if you provide all, if you provide instructions that it should do information gathering beforehand, it tends to do well.

**Speaker** [00:42:00] If you don't provide sufficient instructions, it will try to solve the task without, like, fully understanding the task first, and then fail, and then you need to go back and give feedback. You know, additional feedback. Another example, like, I, I love this example. While I was developing the the monitor website that I, I showed here, we hit a really tricky bug where it was writing out a cache file to a different directory than it was reading the cache file from.

**Speaker** [00:42:00] And I had no idea what to do. I had no idea what was going on. I, I thought the bug was in a different part of the code, but what I asked it to do was come up with five possible reasons why this could be failing and decreasing order of likelihood and examine all of them. And that worked and it could just go in and like do that.

**Speaker** [00:42:00] So like I think a certain level of like scaffolding about like how it should sufficiently Gather all the information that's necessary in order to solve a task is like, if that's missing, then that's probably the biggest failure point at the moment.

**Speaker 7** [00:43:00] Thanks.

**Speaker 6** [00:43:00] Yeah.

**Speaker 6** [00:43:00] I'm just, I'm just using this as a chance to ask you all my questions.

## [00:43:09] Q&A: Self-Improving Agents and Authentication

**Speaker 6** [00:43:00] You had a, you had a slide on here about like self improving agents or something like that with memory. It's like a really throwaway slide for like a super powerful idea. It got me thinking about how I would do it. I have no idea how.

**Speaker 6** [00:43:00] So I just wanted you to chain a thought more on this.

**Speaker** [00:43:00] Yeah, self, self improving. So I think the biggest reason, like the simplest possible way to create a self improving agent. The problem with that is to have a really, really strong language model that with infinite context, and it can just go back and look at like all of its past experiences and, you know, learn from them.

**Speaker** [00:43:00] You might also want to remove the bad stuff just so it doesn't over index on it's like failed past experiences. But the problem is a really powerful language model is large. Infinite context is expensive. We don't have a good way to index into it because like rag, Okay. At least in my experience, RAG from language to code doesn't work super well.

**Speaker** [00:44:00] So I think in the end, it's like, that's the way I would like to solve this problem. I'd like to have an infinite context and somehow be able to index into it appropriately. And I think that would mostly solve it. Another thing you can do is fine tuning. So I think like RAG is one way to get information into your model.

**Speaker** [00:44:00] Fine tuning is another way to get information into your model. So. That might be another way of continuously improving. Like you identify when you did a good job and then just add all of the good examples into your model.

**Speaker 6** [00:44:00] Yeah. So, you know, how like Voyager tries to write code into a skill library and then you reuse as a skill library, right?

**Speaker 6** [00:44:00] So that it improves in the sense that it just builds up the skill library over time.

**Speaker** [00:44:00] Yep.

**Speaker 6** [00:44:00] One thing I was like thinking about and there's this idea of, from, from Devin, your, your arch nemesis of playbooks. I don't know if you've seen them.

**Speaker** [00:44:00] Yeah, I mean, we're calling them workflows, but they're simpler.

**Speaker 6** [00:44:00] Yeah, so like, basically, like, you should, like, once a workflow works, you can kind of, like, persist them as a skill library. Yeah. Right? Like I, I feel like that there's a, that's like some in between, like you said, you know, it's hard to do rag between language and code, but I feel like that is ragged for, like, I've done this before, last time I did it, this, this worked.

**Speaker 6** [00:45:00] So I'm just going to shortcut. All the stuff that failed before.

**Speaker** [00:45:00] Yeah, I totally, I think it's possible. It's just, you know, not, not trivial at the same time. I'll explain the two curves. So basically, the base, the baseline is just an agent that does it from scratch every time. And this curve up here is agent workflow memory where it's like adding the successful experiences back into the prompt.

**Speaker** [00:45:00] Why is this improving? The reason why is because just it failed on the first few examples and for the average to catch up it, it took a little bit of time. So it's not like this is actually improving it. You could just basically view the this one is constant and then this one is like improving.

**Speaker** [00:45:00] Like this, basically you can see it's continuing to go up.

**Speaker 8** [00:46:00] How do you think we're going to solve the authentication problem for agents right now?

**Speaker** [00:46:00] When you say authentication, you mean like credentials, like, yeah.

**Speaker 8** [00:46:00] Yeah. Cause I've seen a few like startup solutions today, but it seems like it's limited to the amount of like websites or actual like authentication methods that it's capable of performing today.

**Speaker** [00:46:00] Yeah. Great questions. So. My preferred solution to this at the moment is GitHub like fine grained authentication tokens and GitHub fine grained authentication tokens allow you to specify like very free. On a very granular basis on this repo, you have permission to do this, on this repo, you have permission to do this.

**Speaker** [00:46:00] You also can prevent people from pushing to the main branch unless they get approved. You can do all of these other things. And I think these were all developed for human developers. Or like, the branch protection rules were developed for human developers. The fine grained authentication tokens were developed for GitHub apps.

**Speaker** [00:46:00] I think for GitHub, maybe just pushing this like a little bit more is the way to do this. For other things, they're totally not prepared to give that sort of fine grained control. Like most APIs don't have something like a fine grained authentication token. And that goes into my like comment that we're going to need to prepare the world for agents, I think.

**Speaker** [00:47:00] But I think like the GitHub authentication tokens are like a good template for how you could start doing that maybe, but yeah, I don't, I don't, I don't have an answer.

**Speaker 8** [00:47:00] I'll let you know if I find one.

**Speaker** [00:47:00] Okay. Yeah.

## [00:47:31] Live Demonstration and Closing Remarks

**Speaker** [00:47:00] I'm going to finish up. Let, let me just see.

**Speaker** [00:47:00] Okay. So this one this one did write a script. I'm not going to actually read it for you. And then the other one, let's see.

**Speaker** [00:47:00] Yeah. So it sent a PR, sorry. What is, what is the PR URL?

**Speaker** [00:48:00] So I don't, I don't know if this sorry, that's taking way longer than it should. Okay, cool. Yeah. So this one sent a PR. I'll, I'll tell you later if this actually like successfully Oh, no, it's deployed on Vercel, so I can actually show you, but let's, let me try this real quick. Sorry. I know I don't have time.

**Speaker** [00:48:00] Yeah, there you go. I have pie charts now. So it's so fun. It's so fun to play with these things. Cause you could just do that while I'm giving a, you know, talk and things like that. So, yeah, thanks.
