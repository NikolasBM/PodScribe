# Agentic Loops for Knowledge Workers — Transcript (2026-09-03)

https://aidailybrief.ai/e/2026-09-03 · Listen: https://pod.link/1680633614

<!-- metadata -->
Format: tutorial · Level: 3 · Length: ~00:57:00
Host: Nathaniel Whittemore
Categories: agents, work
Featured: Claude, agent harness, agent loops, Claude Code
Also mentioned: Claude Cowork, ChatGPT, Cursor
<!-- /metadata -->

---

[00:00:00] 

Throughout the summer, one of the hot topics among advanced AI users has been the idea of loops or loop engineering simply put, the concept is to think about the way that we interact with AI, not as prompting it and telling it what to do, but to setting up the circumstances where the AI or agent can loop over and over again, working to complete a specific task with a measurable output that it can check itself against, running until that task is complete based on that measurable goal

The first place loops took hold was, of course, in software engineering

where the nature of the tasks is fairly definable and success is pretty clear. Moving loops into knowledge work domains where sometimes success is less definable is more of a challenge, but it's not impossible

if you have the right tools to design your knowledge work tasks for this type of agentic work.

Today's episode is a webinar with Nufar Gaspar where we do exactly that

And that is coming up right now

The AI Daily Brief is a daily podcast and video about the most important news and discussions in [00:01:00] AI. All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, Blitzy, Harbor, and Hyperagent.

To get an ad-free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts. To learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai. And if you like Nufar's presentation on this and you wanna go deeper into the world of building agents, allow me to recommend our super intelligent executive agent leadership program.

The next cohort is kicking off next week. It is led by Nufar, and you can find out all about it at training.besuper.ai Lastly, a note, I am traveling currently for Labor Day and my birthday. So if something absolutely crazy has happened and you're wondering why the heck you are getting this agentic loops presentation, that is why

Although obviously if there is something big enough, I will pop back in

For now, let's dive into agentic loops for knowledge workers today we will cover I believe, some very important topics around loops and graphs and in general how to utilize the [00:02:00] most advanced techniques for getting agents to work autonomously and as a group. and I wanna hand it over to Nathaniel to set the table stakes as to why 

we are 

here today. Awesome. 

So, one of the, the really interesting dynamics right now is we're pretty well past the point where people hear you say you're vibe coding or doing something, with Claude code, and assume that you're now all of a sudden, as a knowledge worker, trying to become a software engineer.

It's very clear that we're 

kind of 

in the phase of actually figuring out how code and software engineering style processes and these set of tools can make their way into other aspects of work and influence how that work gets done. And y- this... Just a couple of weeks ago, OpenAI dropped these recent usage statistics which show just how dramatically consumption and, and use of AI has shifted from the assisted to the agentic.

So the chart that's on your screen is from that. You can see around April, May, we flipped from, majority AI usage in [00:03:00] terms of total tokens consumed being in that kind of ChatGPT-assisted paradigm to the agentic paradigm. And the notable thing about this is that alongside this more advanced type of usage, you also see the firms and individuals who are using AI in these new agentic ways are pulling away.

their,



the space between them and others, at least in terms of tokens consumed, you know, which is obviously a, pretty rough metric. But at least by that metric, they are getting farther apart from the average. What's really difficult, and I'm sure a lot of you have felt, is that knowing how to translate these concepts that originate in software engineering to other types of knowledge work can be a difficult process.

It can be abstract. It can involve layers of abstraction. and so we wanted to put together this, webinar because, this idea of using agents in loops and 

sort of 

no longer prompting, but designing loops and things like that, has been 

kind of 

part of the buzzy zeitgeist uh, of AI early adopters for a few months now.

But I think it's still been remained [00:04:00] abstract what it actually means for knowledge workers. So that's the goal of this, is to 

kind of 

bring everyone into new ways of interacting with AI, and I'm excited to see where we go with it. All right. 

So, podcast.

Um, A loop is basically a job, and a graph is an organization. 

that's a quote actually from you from the Keep that in mind, and we'll walk you through that. But if I need to give you like a TLDR of what we're doing in three sentences. So the first thing is that AI tools, the ones that most of you are using, the agentic tools, already use loops to do the work behind the scenes, and once you learn to give them a concrete verifiable end goal, they will keep working until the job is actually done without you nudging them or without you being frustrated by the mediocre result potentially.

That's the big promise, okay? And when one loop and one agent stops being enough, you can always compose loops into teams of agents, and that's the whole idea behind the graph engineering noise and the, chatter in social. There is substance [00:05:00] around that, and this is very important. All of these ideas were born in software engineering, so if you are coming from this background or have computer scientists working for you in your company and so on the graphs are not news to any of them.

And AI engineers have been building with these concepts for a couple of years and over the last few months with a lot of focus on specifically on agents. But almost all the, practice, as Nathaniel said, is very focused on coding, and we will try to show you the, pros and cons, the pitfalls, and how best to leverage that to other types of work, namely knowledge work.

One last thing to say upfront, because most of the work that you do regularly probably requires just, let's call it regular agent execution and only in some cases you might need loops. The graph and the more sophisticated things should be for special occasions, meaning I want you to keep things simple and go into loops and graphs and multiple agent orchestrations only when, uh, needed.

[00:06:00] Um, So I want you to keep it simple while being mindful of the full breadth of how far you can take the modern technology. Very quickly, what happened on social for those who are not sitting in the echo chamber of Twitter X all the time. In uh, July, six words by uh, the founder of uh, OpenClaw. What he was basically saying is that we're no longer talking about loops, we're talking about graphs very quickly, millions of views.

He was half joking but very quickly an obituary for the loop engineering. That is primarily a naming event. But I think the joke stuck because it pointed into something that was

more

real, and to be very concrete of what's 

kind of 

happening or the naming ladder that does have some substance around it.

This is how we got here. And this is, I think, what tells the story of the evolution of agents and AI over the last

Month or even one or two years. So we were very obsessed at the beginning about what you say to the model. That was prompt engineering, [00:07:00] and we all uh, learned how to speak effectively to the models.

Then we got obsessed about what the model knows. That's the context engineering that we talked about extensively. Then we started talking about where it runs and what tools it can touch, and that became the conversation around harness engineering. And this year, we started talking more and more about how long the models

and

the agents can run on their own.

That's the loop engineering. And lastly



we started asking how many of them work together in order to get the job done, and that's the essence of what is now referred to as graph engineering. If you notice kind of

the

direction of the travel, each evolution is about giving the AI more independence at a bigger scale. That's where we're headed.

And some people even claim that this is just a rebranding of a very natural evolution alongside the technology's abilities. And because the field and the practitioner is adding new terms and new skills, evolution roughly every, every couple of month,

and

chasing them can be [00:08:00] exhaustive. I think it's-- the more important thing is the essence is knowing how to get the agents to work effectively and how to orchestrate them.

That's the skill that probably survives the 

e-every 

renaming and every buzz on social. at the end of the day, we just want to get the job done and to be ambitious about the type of jobs that we can do. All right, so that's the background. One last data point that I think proves that loops are important.

Just f- three weeks ago when Jeff Dean one of the most renowned engineers, I think, in the history of modern technology, has left Google. He basically went to establish a company literally called Discovery Loop. And this company is gonna be around using loops for discoveries, so there is merit about being able to run AI in loops in order to get progressively better results.

Okay, so that was the background. Now I want to make sure that we are all on the same page with regards to what is a loop and where can you find one. and the one thing that uh, you need to understand that [00:09:00] every agentic tool that you use, whether it's CoWork ChatGPT Work Codex, Cursor, any, any agentic tool for that matter what is being implemented under the hood is already a loop.

That's what the harness is doing and in various degrees of effectiveness. Basically, it runs through an iterative process of planning how to get the job done, acting, typically using tools, checking whether the results that were received from the tools uh, are or good enough, and then adjusting.

The thing is that the loop that was implemented by the companies behind the agentic tools are as good as what they implemented, and in general, they are quite generic. And that's why even though these tools are amazing and we are g- able to get very good results out of them uh, many cases we are observing the fact that we need to 

kind of 

nudge them, or we need to be very proactive in our prompting if we want them to work extra hard or run multiple iterations on something before it stops.

That's not something that the native loop that were already implemented by the companies [00:10:00] will not do that for you. But the one thing to understand is that under the hood, there is always,

a loop. And then the question, what is all this buzzword or what is the loop, the advanced loop that we're talking about?

So today, what we're talking is about a loop that basically you control what is the end goal. Um, So we're looking for a loop that happens when you extend the native cycle, the cycle that is already run by the tool. And the way to extend it is by leveraging the specific commands. In most tools, it's called a /goal command.

In Cursor, it's called literally loop command. And the entire purpose of this is to give the tool a concrete end goal. And make sure that this end goal is highly verifiable, And making sure that there is a way for the tool to progressively test itself versus is it done or not, okay?

So that's the entire thing that we're talking about today. And if you want to master [00:11:00] two things that really matter here is, first of all, you need to understand when you need to create this special loop, the one that you control the end goal and the one that you encourage the tool to run in multiple cycles until result is done.

And the second thing that you need to know is to define the correct finish line. That's the most important skill for a knowledge worker that wants to leverage that for their day-to-day. Two additional notes here. One is that a loop is not a synonyms for a schedule. A schedule answer the question of when something should run by when it can be based on the clock.

It can be when something happens, for example, when there is an email that is being sent. That's a- an automation or, or a schedule. A loop answer the question of until, and it stops when the work meets the bar however long that takes or the other constraints that you will give it. I'll show those constraints in a minute.

So those are profoundly different promises, okay? So don't confuse loops with automations. Those have different purposes. [00:12:00] And also the other caveat as,

I

mentioned before, because loops were born in coding they are not as optimized for knowledge work as such because coders invented them for coders and for coding.

And coding has a very clear superpower that not all of our work as knowledge worker has. It has verification as a very abundant thing that they can execute. The code either compiles or it's not compiled. The test pass or they fail. It's very relatively easy. If, If there are coders here on the line, I don't want to say that your work is easy.

But in order to verify coding, we have built-in mechanisms which makes the ability to run until a certain condition is being met much more doable, okay? 

So, 

when we're talking about knowledge work in many cases, we don't have a built-in referee. Is this report good enough to present to management?

Is this analysis deep enough? Nobody's [00:13:00] compiler answer these questions for you. So when someone tells you, "Just put it on a loop," they're forgetting that they as coders had free

v-verification,

and we or you don't have. So the good news,

a-and

that's the, the central move of what we're doing here today, is that verification for knowledge work can be designed by you.

It's slightly more difficult than for but you can manufacture the referee, the one that decides whether the job was done. that's what you need to be able to do 

well. 

And if you are unable to design a finish line that is very clear and verifiable, the answer is don't loop it. Okay?

So, 

let me give you concrete criteria as to whether the task at hand deserves and can be looped for you. So, 

in order for a task to be loop-worthy or loop relevant it needs to be long-running, meaning that it's not something that you can achieve with one prompt and get good enough results.

With modern models, often that's more than enough. [00:14:00] I urge you use one shot and getting the results if you can. The second thing, and those have to come together, you have to be able to check whether the results are good enough or the progress is headed in the right direction. That's the most important pair.

The second thing is that you look for things that you probably and potentially want to send overnight, meaning that you want to be able to run autonomously maybe over lunch, you don't have to run overnight, a-and come back to a finished result instead of a draft. That's part of something that might indicate that a loop is in order.

Also, we want something that should keep running until a specific bar is met or keep running indefinitely, watching for something. Those might also be a good indication for a loop. We also want something that, comes, by the way, from hard experience is want something that you tried with the outputs, with the fable, with the GPT solo whatever smartest model that you have out there, and it was just not good enough.

It didn't meet the bar with the one-shot [00:15:00] execution. Also, it's relevant for cases where you want to push the model to work harder than one polite pass, which is often will will be the default. Think about uh, when you send the model to do the research, and that's gonna be the example that we will show in a minute.

Often it will uh, a decent web search, synthesize the results, and that's gonna be that. Uh, Unless you prompt it very rigorously, in many cases, it will not run multiple iterations of trying to improve the quality and the abundance of results unless you ask for it very nicely or not so nicely.

And lastly we want something that has a natural retry and improve shape. Okay? Something that can be a draft, but then it gets better with multiple iterations. That's by the way, part of why I s- I think Jeff Dean is going to do that for research and science because this is a place where with more and more and more experiments, typically you eventually get to the right direction.

On the flip side, and that's also very important, if the task is short and one pass does it, if your judgment is the actual work and you cannot offload the, the judgment [00:16:00] to a referee a normal conversation with your agent is the right call, and choosing that is the smart move, not the cop-out.

Okay? Last thing to say, loops are the most-- among the most token-hungry executions that you can have with your agentic tools. So be mindful that you're using your tokens for the things that matter, and that you don't loop for everything. we wanna loop for the things that, the value is there.

Um, 

All right. 

So, 

here are some concrete use cases of type of knowledge work that people do in order to leverage loops. I'll start with the-- my first attempt of using a loop. I ironically decided to use a loop in order to do a very extensive research on token efficiency best practices.

That's also something that I will demo in a minute. I know that the-- there is a little bit of irony to use the most token wasteful method to look for token efficiency. But that's a very good use case that you can pursue. Uh, Research where you want the agent to go deep and wide and synthesize and make [00:17:00] sure that you get the results that you're after.

Another very powerful example that many people have been uh, leveraging loops for, to do the ad and campaign optimization. V-- highly verifiable use case because you can always test with very concrete data, whether the click-through rate and other analytics that you're using on digital campaigns are actually improving.

And thereby by iteratively trying multiple things and getting the agents to work on a loop, or sometimes indefinitely, sometimes with some kind of a uh, cap on how many times it's trying, you can overly improve the results. And you can see some other results there. Competitive analysis or scans some audit around content verifying some results doing a compliance and so on and so forth.

The places where we're not doing loops is anything that requires human judgment and cannot be fully automated. So if the executive communication requires your judgment, it's not a loop. [00:18:00] Similarly with these other folks, hiring and strategy. Because autonomy, at the end of the day, does not have a taste on its own.

You probably need to be there to be the final say of that Okay, so that's a bunch of examples for what people are actually looping. And if I need to kind of give you the bottom line of the three requirements in order to build a loop. 

So, 

one, checkable finish line. Knowledge work only succeeds on loop exactly when you invent a very boring, very checkable finish line.

And a ch-- boring here, by the way, is a compliment. So for example, saying, "I want two hundred verified data points," is very boring, but very concrete and very machine checkable for you. Every competitor covered, every claim cited, summary under one hundred and fifty words. Very boring, very checkable, and you can think about the equivalent in your domain, and you will actually be encouraged to do that in the lab part.

Something like make it insightful is not checkable, okay? There is no way for the agent to converge on make it [00:19:00] insightful, okay? We're looking for things that the agent can measure itself. The second thing that we want to do is to, as much as possible, have a bounded sandbox. It's a, a space where the loop mistakes are cheap.

So for example, going back maybe to the ad um, campaigns or to the digital campaigns optimization don't do that on the highest

table

stakes and let the agent uh, go wild unless you're okay with the results. But for example, doing a research in a sandbox or running a specific experiment in a sandbox where if there are mistakes they are not very costly because we're staying in draft mode or in, in a bounded place, that's a, a better place for you to run the loop.

And lastly we want a task that can converge. So we want use cases where we have different paths and go through different potentially gates. We are in de facto getting closer to be done. Research is a task that can converge more sources, fewer gaps make it better going back to that.

Uh, Forever doesn't converge, and the, the agent can get into [00:20:00] the loop indefinitely. It can always ask itself, "Is it good enough? I don't know. Let me try again. Is it good enough? I don't know. Let me try again." Okay? So if a task is not well-defined and cannot converge we're not gonna loop it.

Okay. So how do you define, that's

li-like

the, the bottom line. How do you define the goal for the loop? Conceptually, you should think about it designing a goal card, and these are the things that you should configure as part of the goal cards. also will be the things that you will append after the the execution of the actual loop command.

So it starts with a concrete and clear objective, okay? The objective should be very clear very machine readable. For example, in the

research that

I'm gonna trigger in a minute I want to create the definitive token efficiency playbook as of today, as of 

August 2026. 

Uh, You should define what is the output of the loop.

In our case, it's gonna be a file, but maybe for you it's gonna be something different. And this is [00:21:00] what makes or breaks everything here. Because this is how you define the judging and the stopping criteria the, the initial ones. in this case, it's gonna be I want more than

two hundred unique

data points.

I want each with URL and date and type. I want a specific mix, at least

forty

vendor

docs, forty pr-practitioners,

twenty benchmarks, and I want zero duplications. So that's me trying to give the machine a very concrete criteria about what the purpose of the loop. And once all of these conditions are met, the agent will stop doing the work.

So your skill is knowing to configure exactly that. And if you struggle with defining what's the done when meaning that you're unable to find something that will be, very clear, ver-very nonambigu-ambiguous. You're gonna struggle, and you might have a loop running either too short or too long.

And that's not the right place to go. You can it's optional, but you can configure stages, like specifically what gates or what type of actions you [00:22:00] want the agent to take. it's not mandatory. Sometimes you want to manage that. Sometimes you actually don't want to do that because you want to leave the agent sufficient amount of judgment to decide how to go about achieving this objective with these stopping criteria.

And in all of the tools, you also have the ability to add an additional, let's call them uh, fail-safe or fallbacks things to avoid the loops running indefinitely. So for example here, in order to make sure that may-maybe there aren't 200 unique data points in the internet, and the agent will try to run it forever and ever and ever for me unless I give it another stopping criteria.

So I can tell it try up to 30 turns and sandbox only, meaning don't go and do stuff outside the world. You can also cap it with time and pair the specific tool that you're using. Sometimes there are additional things that you can constrain in order to make sure that in case this is something that ends up not being convergent you have a different mechanism to convergent.

That's [00:23:00] actually very important to have this fail-safe mechanism. So that's the proper goal. Let's very quickly try to demo that So again, going back to my use case, I wanna do token efficiency research. I'm within as you can see, Claude Code.

In Claude Code, the loop is called /goal.

And

And 

take a look at my card here. Research is done when all of the following are true. The artifact I want the file listed here. I want executive summary, the data, and so on. I'm giving it the concrete criteria. I'm giving it a q- a quota.

It contains at least two hundred unique data points about token efficiency and agentic AI work. No two points sta- stating the same fact. The receipt, every data point yada, yada, yada. It creates a URL. This is the mix that I'm asking for as, as noted, and I'm asking for a log. I'm asking for a log in order to show you how the loop work, but I actually think that's a very good practice for you when you're running a loop to ask the model to be a little bit verbose [00:24:00] and saying out loud what it's doing and what's the cycle number, so you can see the progression.

If you want to monitor, especially as you are new to, uh, using loops, it's gonna be a great practice for you. I'm not gonna use Fable. I'm gonna use Opus, and I'm gonna move to the auto mode to make sure that it's actually running. Now, obviously we're not gonna sit here and wait for the, I don't know, good twenty, thirty minutes or more that it will take it to run.

But as you can see goal set. Okay. And then it's reflecting the interpretation. It will start reflecting the cycles. In order to not have you waiting, I already ran this exact command earlier, and that's what you can see as the results. So let's see how it went.

Exact same command, and as you can see here. So cycle one, checked workspace space. Doesn't matter. Cycle two, it got fifty-six out of two hundred. it checked various sources. In cycle three, it got to ninety out of two hundred, and so on. [00:25:00] Interestingly it went above the two hundred.

In some other executions, it went even all the way to three hundred, so it's not always as disciplined. But fortunately for us, we do have the cap of thirty cycles, so it will not go above that. And that's the, 

like, the, 

the finish line, and it created an artifact But

And it's also giving me some things to pull in front of you guys if you're interested. So that's how you run a loop here. And the other one is running in the background. We can check it out later on. But that's the entire purpose here. 

So those were loops. Now I want to make sure that you understand that loops can fail and can fail very miserably.

The first one is runway spend. It just keeps going. That's why we have the hard cap, and that's why I said it, it's very critical. I've seen people running loops indefinitely or much longer than what they expected the loop to run for. We also have a loop that can stuck. It cycles without progress.

it's sometimes just because it cannot converge or something about the conditions are not there. If [00:26:00] that's something that happens, we need to either stop the execution manually there are also dedicated commands in different tools or we can ask it to stop and report if we know that this is a type of loop because you tried it, that sometimes gets stuck.



Sometimes the loop is done, but it's very mediocre. That's very sneaky because it might have met the letter of your finish line, but the results are still very bland. So what you need to do here is acknowledge, first of all, that it's not the loop failure, that's probably the failure of your definition of the goals.

If it met verbatim the goals that you defined, but you are not happy with the result, that means that you need to better define what is the finish line or what are the uh, referee guidelines. in many cases, it's gonna be around quality and taste and things that are gonna be harder to configure, but that's something to note.

And lastly sometimes we just started running something on a loop that was not something that was meant to be a loop. So, 

if that's the case the, the turn cap is your best 

bet. 

Okay.

so we're done with the loop part of the webinar. Just to summarize we talked about the fact that loops are already a cycle that is being executed by any agentic harness that you're using.

But the loop command or the slash goal command, the entire purpose of it is to make sure that you can get the tool to work harder for a longer time using a verifiable goal. We also distinguished between a schedule and a loop. It was born in coding, so you, and we and all of us need to work harder in order to create a finish line that makes sense in knowledge work or not use a loop if we can.

The main skill here both of these things. Identify the use case and configure the goal card. And always add the caps and the safe sandbox in order to make it work. Now uh, I want to move from loops to org chart because everything so far was basically one worker. It, was one agent working alone until done in loops. And the progression of this whole field is here. Okay?

We all started on the left, or [00:31:00] if 

you're-- n-- 

you haven't started building agents yet, you should be there already. Then we talked now about uh, looping things relevant and when doing so well. The next station is when the work itself splits. Basically, we have several agents.

Each is doing one piece passing work between them, passing information between them. That's gonna be a

work

graph, and it bu-it's built for one job. Okay? And the last station is when those agents stop being disposable and become your standing team or what is sometimes referred to as an org graph. So one agent working one time, agent working on a loop we de-decompose the work into multiple agents only when it makes sense and when there is a tool need for that. More on this to come. And lastly, if we realize that type of work that we want to get done is much more than the one thing, we can build an entire organization of agents as an org graph to get it to work.

So 

maybe 

one thing to say, it's not [00:32:00] like that you have to get to number four, okay? You don't graduate there. There are uh, many tasks that 

are more than 

good 

for number one and so on. But there are some cases where the, 

like, 

the quality of the results and the scale will only be unlocked if you go all the way to building entire teams of agents and orchestrating them e-efficiently.

So we only move when there is a justification, but in some cases, there is huge value to be gained here. Okay. So to keep it very simple and concrete, I want to explain what a graph is. And a graph is basically dots and arrows. That's that. Okay? The dots are called nodes. For us, a node is an agent or a task that needs to be done.

The arrows are called edges and the edges include work or information that is flowing. And when an arrow has a direction for example, research flows into the writing a-agent, we say that the graph is directed. And one detail that is very fun and also for the [00:33:00] computer science curious or passionate folks on the line look at at the bottom line, 

right?

If we have one node with an arrow pointing back to itself, that is the textbook definition of a loop. So a loop and a graph are not different things. The, the loop is probably the simplest form of a graph or the smallest form of a graph out there. Okay? So the real question is and always was how many nodes does your work deserve?

Computer science has drawn work this way for fifty years, so it's not new. But what is new for our day and age is that AI made the drawing operational. Today, you can draw it, and it actually can run for you. Okay? So that's the big thing here, right? It's not just something theoretical that you learn in computers 101.

It's something that you can actually execute. 

Another deconfusion because the same week this trended, half of LinkedIn was also and X, of course, was also talking about knowledge graph, and I've watched very smart people blend three unrelated things into one word. 

[00:34:00] So, 

we have knowledge graph.

Those are graph that stores facts what we know and how it connects. It's a very beautiful technology, completely different jobs, not very related to what we're talking here. We also have LangGraph which you may have heard engineers mention. This is a developer framework. This is a tool for building agent systems in code, and it is leveraging the power of graph and a very powerful and good technology.

And today, we're focusing on the work graph. It's-- This is about the execution of the work specifically for knowledge work we're focusing here, who does what uh, in what order, and what flows between them. Okay? So these are the concepts. Don't confuse them as much as possible. I'm leaving the computer science engineering alone, and I'm talking about graphs and work before everything.

So, 

let's talk about what we had before AI and before agents. The main graph that we actually had and have in each and every one organizations we're concerned about the org chart. And the org chart, the main problem with it is that it basically pretends that work flows in one [00:35:00] directions top to bottom, right?

The manager says something, the CEO, and then it goes to the rest of the organization, and that's how we pretend that work gets done. Not at all. We all know that work branches, it loops back, it ends up sideways. It ends off sideways. It skips levels and occasionally flows straight up at 11:00 PM, 

so, 



especially before board meetings.

So that's not how work gets done. the org chart is the diagram of the authority. It's not

and never was a diagram of how work gets done. A graph, however, dots and arrows going wherever the work actually goes, is the more relevant picture and the picture that we need to paint to our agents in order for them to follow the work.



it... As mentioned, two flavors, the org graph that is more persistent and the work graph that is per request or per uh, task. Okay. 

So, 

let's talk about what changed, okay? Because the skeptics will tell you one thing. Engineers have been wiring agents into graphs for years.

we talked about LangGraph a minute [00:36:00] ago So why are we all so excited about graphs again beyond the, the chatter on social? The thing that changes the node because the node used to be one fragile LLM

LLM 

call, AI call, and in many cases it was not that great, and to orchestrate an entire graph like that was not very feasible for a complex task or you have... to work very hard in order to get something to work. Today a node is a whole agent, a, a worker that you hand the job to, and a worker has two gears. It can be a quick one-pass task like we normally or typically do, or it can be a full uh, 

uh, 

loop running until done. So either one can be a node, and loops are just your heavy duty nodes if you want to 

kind of 

understand how everything falls together.

And what's totally new here is that agents got reliable enough to be building blocks within these graphs and that's a big unlock. So nothing was invented that is new this summer. It's just that something was more democratized and the technology has gone far enough to be able to actually draw this graph on a whiteboard and [00:37:00] get it to work effectively.

And one last very important thing we only go into the 

orchestration 

or composing these graphs of multiple agents and multiple nodes when the one worker, the one agent that you built is no longer doing the job. You're unhappy with the results that you're getting. Okay. So how do you know that a specific task cannot be executed well with a single agent and requires multiple agents and graphs in order to orchestrate?

In some cases, both are valid options. If I'm going back to my example of research in many cases, a good research agent with or without a loop is more than enough. You've seen that after it took about eight cycles, right? We got a very interesting report out. So in some cases that's good enough.

If I want to be more comprehensive or I'm discovering that for my intents and purposes it's gonna be better to separate the work, I can do the same research as a graph, meaning as multiple agents that needs to be orchestrated. [00:38:00] For example, I can send multiple parallel agents to research different angles that I'm interested.

So one can research vendor, one can research what practitioners are saying, and one can research benchmarks. And because these are tasks that are independent, I can run them very easily by multiple agents in parallel. Then I can offload the results into a synthesizer move it to a citation verifier that hopefully is not encumbered by everything that was done prior such that it's a, a objective verifier and either the human can verify or maybe I would want to run another verifier by an agent before I, publish.

And I can also maybe add, and I will do that, an agent that designs the output in a way that I like. So when each is better, first of all, as, as I said at the beginning, I want you to keep it simple, and if one agent works well, that's good. Uh, I want you to move into that in several uh, scenarios.

First of all scenario, which I call a rubber stamp your agent or your loop [00:39:00] says, "Done," everything checks out and you keep finding issues that it should have caught. In many cases, self-review is not the way to go, especially with things that are critical. 

There, 

there is also a lot of work showing that models tend to agree with themselves.

If you use the same model to verify the results of, the same... like a GPT verifying GPT, odds are it will say that it's correct versus Claude verifying GPT. 

So, 

in many cases, we want to fan out to a graph of multiple workers when we realize that the verification is not very reliable.

Another scenario will be that we identify context overflow. Like one agent is wearing too many hats, and it starts confusing them. Like you are both the objective researcher but also the very creative designer. So the researcher might start uh, bringing creative uh, uh, results because it's trying to be creative too early on.

So when you identify that's the scenario it's probably better to fan out to multiple uh, nodes or multiple agents. Another [00:40:00] thing is where you don't want to sit down and wait for the work to be done serially when it can be spawned out to multiple agents doing the work parallelly.

I know that we are all very patient in uh, this day and age, and we're willing to wait for many minutes, if not hours, to get the results. But if we can parallelize the work, often we should. And another signal will be when the finish line keeps changing mid-run. So you keep rewriting basically the goal card while it works because it's really two jobs wearing one card.

So if you realize that basically it's either an if/else or a if/then 

kind of 

a goal that under the hood hides two different goals and two different jobs to be done, this is where you probably want to separate. And lastly when despite your best effort, no matter how much you tried, the quality flatlined too soon maybe it's because the context is missing or maybe because it's just not the right architecture you probably want to bring a second perspective or span out at least one [00:41:00] more agent.

Okay? If none of this is correct, stay in the loop or stay in the agent and don't overcomplicate things. Okay. 

So, 

up until now, it sounds very promising. Like,

We 

will build multiple agents, they will work in a graph, we will describe everything that we have in mind and it will work.

But the bottom line is, how do you actually build a graph? What do you need to do? And I think that it sometimes sounds overcomplicated if you talk to the practitioners, but in fact, there is a progressive level of complexity, and they will all work. It's just a matter of different competencies and different needs that, uh, defines how, to do it.

So the very first thing that you should always do, I think, but can be a good start, is to just draw it, like a paper, a whiteboard. You just sketch the text. This is very critical because you need to be clear about how to get the job done, and painting that on a whiteboard gets you to confront all of things that [00:42:00] are not well defined.

And in many organizations, many things are not well defined, and until you can agree upon a work graph for something uh, you cannot uh, automate that. So that's the very first thing that you can do. And if you can draw it, that means that you can even just take a picture of this drawing, show it to any agentic tool, and it can build it for you.

So that's why I'm treating that as not only a, a gateway, but as a concrete modality. Another thing that you already do without knowing or maybe you are paying attention to that, but the agentic tools improvise little work graphs every time that you give it uh, a task, especially complex task because that's how the harnesses, the modern harnesses work.

You've probably seen some tool, maybe it's a, 

cursor or something else saying, "I'm gonna spawn several sub-agents to do different types of work," or, " Let me divide and conquer the work," and stuff like that. So this is under the hood, the tool creating a work graph for you based on the prompt.

So you're not in control of that, but that's another way that the job is doing that, and also the co-work and the Ch- ChatGPT [00:43:00] work, they do that as well. 

another way

for you to do that is to prompt the graph. Basically, tell the tool- Research these five competitors in parallel with separate sub-agents, then have a fresh context reviewer check the merged results against this rubric.

That's just one sentence, but under the hood, what you're describing is a graph that fans out five sub-agents to do different research and one to verify that. You just built, in words, seven-node graph. Congratulations. Another thing that you can do is you can create persistent workers. You can create basically either sub-agents uh, files, or you can create what I refer to as folder agents.

I'm not gonna go deep to all of that 'cause there is a ton of that, but I'll show some examples. You can basically create these agents as persistent workers that you can summon to the conversation as needed. On top of that, you can create a skill if you want to have that as a reusable thing that you do, or you can just ad hoc have the tool refer to the specific sub-agents that you created.

We also have the option to create [00:44:00] canvases using the tools like N810 and other automation tools that lets you basically create a visual graph. And lastly, we can always create those in code. So there are multiple tools and multiple packages that lets you create these graphs and this orchestration via code. code. So this is the five tiers. Again, it's not a competition as to who can get to the highest tier. It's just a enumeration of all the ways that you can build these, uh, work graphs using multiple agents doing the work for you. For most of the knowledge work that we need to do you will probably live in these tiers, and it's more than enough to get the job done.

Let's show you some concrete examples. So first of all, let's go back to the execution that we had before. One thing that I did once the result came in is I said to Claude the following: "Hand the playbook to the citation verifier subagent." I'll show you in a minute. Make sure it's fresh context.

It knows nothing about how the document was produced. then the document will be [00:45:00] that. It checks everything there. Sample ten random data points and verify each agent against its real URL. The the then count the totals and the source mix, and I'm giving it, 

like, 

a bar. So that's me basically taking the result of the loop and getting Claude to add another node, and that is the node of citation verification manually just by prompting it.

And you can see Claude is being very compliant. It's handing it off code. The verifier gets the file path and the bar. Nothing about how documents was built to avoid contamination, and the verifier verdict is ship uh, with one required fix and now applied, and it gives me the sample verification and the total.

So you can see how my research went into another node. And then I added one more node I want to make it into something visually attractive. So I, had it hand it to the report visualizer subagent. Build a beautiful self-contained HTML page from [00:46:00] output, yada, yada, yada. Its visual language and attribution rules live in its role file, save as a output and so on.

And then it was done. So that's one way for you to add additional workers into an existing loop or an existing thing. Maybe the-- one of the simplest ways to do that. I can also paint a picture on a whiteboard, the research sweep. That's how I would imagine such a research to happen from here on after.

And as I said, I can just give this picture to Claude, and Claude will be able to implement that quite well. But the fact that I am able to paint this picture means that I can automate that using multiple agents, so that's a very important thing that I can do. Another thing that I can do, I can build,

a

persistent workers. Okay? 

So, 

what I'm showing you now are subagents that I created specifically for research. I have a benchmark collector that's an agent that brings specific research around benchmark. I have ci- citation verifier- citation verifier is an agent that the entire [00:47:00] purpose is to verify the citation.

That's was the one that you've seen in Claude. And I have the report visualizer that describes exactly how I want to get things visualized um 

that describes exactly how I want to get, things visualized, 

and so on. As you've seen, I can summon them to the conversation ad hoc, or I can create a skill. And the skill here basically describes the graph. Take a look. In case I want to run the research time and again the same way that's a skill research with the work graph as a file, and I'm showing it how to do the flow, and I'm giving it phases.

And I'm telling it in each phase of the skill which workers to summon into the conversation. And by the way, as part of the-- I don't know if you've seen that, but as part of the agents, I can also configure which model to use. So that's a way that anyone here on the line that knows how to work with Claude, knows how to build sub-agents cards like you've seen and knows how to build a skill can orchestrate multiple agents very effectively with a lot of controls, and it's working with any uh, agentic tool. So that's [00:48:00] level three, basically. Two more things that I wanted to show you. Specifically, I chose n8n, but just to make it very visually clear that's another way for you to if you want to create a work graph. Okay? So in this workflow in triggering that on a schedule.

I have collector agents for different stuff. I have synthesizer agent. Note that ideally I would probably want to use the synthesizer as a strong model, whereas the collectors might not have to be a very strong model. I have a citation verifier, which definitely, as much as possible, needs to be a different model.

I can put all of that in a loop until a certain quality is met. In this case, I added a human verifier. 

verifier, 

And lastly, I have a report visualizer and an image. So if you are versed in a tool that is more canvas-like tool, or that's the way you want to work the nice thing about this is that it's very visual, and you can very easily see how work flows across the graph, and you can verify that.

[00:49:00] So an overkill for most of us, but also an option. And by the way, if you wanna see the output, that's the report that we got from the research. That's the one I will share with you. So it's giving you both an executive summary and a ton of data points on how to use your tokens uh, better. Yeah.

Ah, sorry. Last thing, LangGraph. LangGraph is basically a code, if you want to create work graph with-- in LangGraph, that's basically a code that's how it looks. But another thing that is nice about LangGraph, you can have a visualization built in done by LangGraph.

So even for those of you who are using code, LangGraph has a built-in way to visualize the code that was created. So even the, the top tier is not that scary in reality. 

Right. 



A few more things before we maybe take a couple of questions The six habits that separate an effective agent orchestration or graph from a very expensive one.

Some of those were mentioned there implicitly. You want to match the node-- the model to the node. Part of the decision here is which model to use for which work or [00:50:00] which type of work. And of course, we want to be cheap and fast for more mechanical steps and yes/no verdicts, and much more stronger models where judgment is needed.



Each node ideally should get the relevant context only. what's being passed between different nodes is the contract. So you need to be very careful and intentional about what passes between nodes. Maybe a, a draft and a rubric or finding in a format. We-- you never need to pass the entire conversation.

That's not the right way to flow uh, work for most cases. the next thing I want you to spend where verification pays, meaning that if you want to fan out to multiple agents, there is a token cost to that. If you need to summarize between nodes, that can help. If you can cap turns per node, that can also help.

But be very deliberate about that because

a,

a beautiful graph like that can easily become a huge token cons-consumer if you, for example, will use the built-in deep research by some of the tools. Those can easily take millions of tokens without [00:51:00] batting an eye. 

So, 

be careful about that. I want you to verify early, so add these nodes of verification and add clear boundaries, whether it's because you ran a loop or just as part of the work graph that you did because the...

especially the more complex your graph is, the more compounding of mistakes become e-expensive. And at least as of now, humans are needed and for the most part superior than the beast. So have human at the right gate. Maybe it's at the end, maybe it's early on to approve the plan, but humans should be intentionally brought into the graph.

right. one last thing that I want to cautious you again. Many people when they come to design a work graph, they think about exactly the way the work is being done by humans today. And the way work is being done by human today is often highly bounded by human limitations: attention span time, bandwidth, ability to be proficient in multiple things.

Many of these limitations are not the relevant limitations [00:52:00] for your agents and for your tools. So I don't want you to just take the exact way that work is being offloaded between humans today and move it to a machine. That's not the way to go. You need to understand, either by testing or by understanding the limitations of the tools, how to better configure the work, given that in many cases these tools are much less prone to get confused or get tired than humans are.

Uh, And in many cases, that requires a little bit of a radical thinking about what's the bottom line, what's the job to be done, not what's the current processes of how humans do the work in order to design the best possible graphs out there. I, I'm sharing with that that with you later on, but these are the concrete commands for the different tools that people are using.

So, the co- concrete commands for loops using sub-agents. Because things are moving so quickly, always do a web search or consult with the tool at hand as to what's the best way, 'cause sometimes they deprecate commands between you will [00:53:00] wake m- one morning and the command is no longer there, as well as different modalities.

For example, the in the Claude code, the sub-task

is only

accessible in the CLI and not in the desktop. 

So, 

don't just assume that because there is a command that it's gonna be operational in the, surface specifically that you're using. I think that if you're looking at loops versus graph then loops are more uh, forgiving because the graph is a bit of a, a confession of how your work really flows, who really owns what, and where quality really gets decided.

And by the way, this is why you will probably be better in that than most engineers, because you've spent your career learning how the specific work that youfocus on move through the organization, and that's the knowledge that became the technical skill, knowing how to inject your subject matter expertise into designing the, these right the correct systems.

if I, I need to like, summarize the hour on one slide and it's only relevant as of August 2026 because the thing will continue to [00:54:00] grow probably by wintertime, e-either with a new buzzword or with new uh, skills as we get there. But the best practitioners in knowledge work, they have mastered all of these four.

They understand agents, and they understand the underlying loop that is being implemented on, in the harness. They know how to define concrete agentic workflows. They know how to configure loops to get the tools to run autonomously well, and they know how to configure teams of agents that work effectively, either as one task or in general to implement an entire organization.

That's the skill set for you to master as of August 2026. Before I go to Q&A, I will just do a quick plug. If you want to go much deeper, depending on where you are, we do have two training programs. One is the executive catch-up for people who are a little bit let's call it behind or needs to make sure that they become best in class in AI usage and not just best effort.

And the executive agent leadership, that's a much more advanced course for building teams of agents [00:55:00] and configuring the strategy for your organization, and so on. Um, NLW, before do you wanna add a few words? 

I mean, 

what, uh, what more words are there? I, I think that the, the... Part of what makes this moment important 

is 

we've shifted from AI skills being useful new tools to actually being fundamental work primitive shifts. And what I mean by that is that, like, when we started Superintelligent a million years ago, the very first iteration of the platform was, like, how to use Midjourney and how to prompt And, and these things were valuable.

They were, like, nice skills to have. They could get you leverage. But the way that we did work hadn't fundamentally changed yet. We are now increasingly finding that big chunks of what we used to do, instead our job is to now manage agents to do them, and that is a transitional process. It's not all at once.

It's not gonna be all of the tasks that we do, but all kind of [00:56:00] involved now in the discovery, to some extent, of what it means to manage agents. And so I think that that's the, the lens through which I look at these things is, we're all 

kind of 

like 

piece by piece giving ourselves an MBA in agent management.

And it's gonna keep iterating and evolving. But I think that a lot of these things, the reasons that we 

cling 

on to 

loops and graph engineering and some of these ideas, is that they start to feel more like core primitives as opposed to just, another fly-by-night skill or something like that.

So, in the same way that you wouldn't expect yourself to know or to be perfect at advanced management techniques in a single session or experiment or a couple of days, it's gonna be the same with this. It's just gonna take hands-on work and experimentation and, there are no experts at this, as, as I've said in the past. There are just people who have done it more. 

So, 

even by virtue of being here, I think you're probably ahead. 

​ 

[00:57:00]
