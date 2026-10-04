# What the Heck is Graph Engineering? — Transcript (2026-08-10)

https://aidailybrief.ai/e/2026-08-10 · Listen: https://pod.link/1680633614

<!-- metadata -->
Format: news-analysis · Level: 1 · Length: ~00:26:00
Host: Nathaniel Whittemore
Categories: agents, safety-security, models, open-weights
Featured: agent harness, OpenAI, Anthropic, Hugging Face incident, agent loops
Also mentioned: GPT-6, Qwen, Kimi, Claude Code, Claude Mythos, Claude
<!-- /metadata -->

---

260810 in_EDIT: [00:00:00] Today on the AI Daily Brief, what the heck is graph engineering and why should you care? Before that in the headlines, OpenAI's Atlas model getsa cyber delay. The AI The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI. All right, friends, quick announcements before we dive in.

First of all, thank you to today's sponsors, KPMG, Blitzy, Robots and Pencils, and Hyperagent. To get an ad-free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts. And to learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai. 

260810 hed_EDIT: Late last week, rumors were swirling that OpenAI's latest model, codenamed Astro, was being prepared for an imminent release. Sam Altman even traveled to Washington to preview the model and discuss new model testing policies. In the background, however, the discussion around the Hugging Face hack just continued to grow in prominence and significance.

For those who missed that episode, OpenAI's technical breakdown at the Black Hat Conference revealed that not only had their model [00:01:00] escaped the sandbox and hacked into Hugging Face's servers, it also left internal notes instructing future models on how to pull off the same trick

On Friday, OpenAI decided to make a big shift. They They wrote



260810 hed_EDIT: Our latest internal evaluations of Astra, one of our upcoming models, over the past few days indicate significant advancements in agentic coding and cybersecurity. These results, in addition to expert assessments, have led us to conclude last night that we cannot rule out critical cyber capabilities under our preparedness framework.

OpenAI defines that critical threshold as the ability to, quote, " Identify and develop functional zero-day exploits of all severity levels in many hardened real-world critical systems without human intervention, or devise and execute end-to-end novel strategies for cyber attacks against hardened targets given only a high-level desired goal."

Now on this front, GPT 5.6 Soul had been assessed in the high category, which was a little more risky than previous models, but still appropriate for a release 

model, 

Nathaniel Whittemore: Given that 

260810 hed_EDIT: the new Atlas models are now in the critical category. 

Nathaniel Whittemore: 

260810 hed_EDIT: as a result, OpenAI is holding back the model from release while beefing up internal safety [00:02:00] measures.

Testing environments will now be isolated. Model weights will have enhanced encryption to prevent leaking, and additional sandbox monitoring will be implemented. OpenAI will also be limiting internal activities using Astra that don't yet meet these enhanced security measures

On On X, Sam Altman added some context around the decision posting, " Astra is a powerful model, and we're working to make it generally available. We do not think it is a good strategy to keep powerful models to a chosen few. Given its cyber capabilities, we need a little bit longer to do this safely, but hopefully not too long."

Now, one thing we don't know

Is to what extent this is an OpenAI voluntary pause versus a government-imposed pause

Or whether that distinction even matters at this point One interesting note is that there aren't a lot of folks suggesting that this is just a publicity stunt, as was one of the narratives surrounding the Mythos release Basically, the Hugging Face incident seems to have made the case that advanced cyber capabilities could be a real concern.

OpenAI Head of Strategic Futures, Dean Ball, noted that this year is the first big test of whether frontier AI labs would follow their stated safety preferences when push comes to shove. He wrote, " Our next model, Astra, [00:03:00] may be critical under our preparedness framework. We cannot rule out the serious possibility that it is, and so we are going to take steps consistent with the higher risk level, 'critical,' rather than assuming the model is at a lower risk level."

Some of these decisions have the effect of slowing down internal development, and in that sense, they are costly decisions. but they are the right decisions. I am proud of OpenAI for making them

discourse, now a lot of the discourse surrounding this is what sort of changes OpenAI can actually make

to the guardrails and monitoring around these models OpenAI's RSI preparedness lead, Micah Carroll Wrote, "As part of our response to cyber critical, we've expanded chain of thought monitoring to cover all agentic applications of Astra, including training and evaluation.

flags trigger a security response to review and interrupt high-risk activity."

Now at the same time, there's also some skepticism around that sort of chain-of-thought monitoring. But these are the types of discussions and experiments you're going to see a lot more of now



260810 hed_EDIT: where I believe there will be a significantly increased

investment in the resources to properly support models that won't be able to be released to the public without it

without it Now, speaking Now, speaking of big powerful models, ByteDance is reportedly [00:04:00] training an ultra-large model comparable in size to Mythos. The Financial Times reports that ByteDance is in the early stages of a training run that will result in a base model with as many as 10 trillion parameters So far, we've only seen a couple of large-scale training runs out of Chinese labs, with Kimi K3 weighing in at two point eight trillion parameters and Alibaba's Qwen three eight Max at two point four trillion

Anthropic doesn't disclose model sizes, but the best estimates have Mythos at around eight trillion and Opus 4A at around three trillion for some comparison. Sources said that the training run could take three to six months to complete, with more time added for reinforcement learning after that.

ByteDance also hasn't determined how largethe final model will be on release

Still, this could be the first Chinese pre-training run that's truly on the frontier. And while model size is not a guarantee of performance

This could put ByteDance back in the conversation for leading Chinese labs. That is, of course, all the more relevant if they follow through with their pledge not to distill from Western AI models as reported last week

Nathaniel Whittemore: 

260810 hed_EDIT: Brookings Research fellow Kyle Chan wrote, " Chinese AI labs seem confident that they have the compute needed to [00:05:00] pre-train five to 10 trillion parameter models. Some way, somehow, compute does not seem to be such a major bottleneck, at least when it comes to reaching these levels of model size."

Nathaniel Whittemore: 

260810 hed_EDIT: geopolitics commentator Dmitry Alpe-Alperovitch responded, " Why would there be when there are no restrictions on remote access to compute and the export controls on chips are full of holes like Swiss cheese?"

cheese?" Speaking Speaking of, 

Some of those holes do seem to be top of mind in Washington



260810 hed_EDIT: shortly after the release of Kimi K three last month, The New York Times collated research on the flow of compute from large scale data centers in Southeast Asia. According to SemiAnalysis, the Oracle data center in Malaysia was being used almost exclusively by ByteDance. The data center was powered on in mid twenty twenty-five and contains over a hundred thousand NVIDIA Blackwell GPUs.

Think tank ChinaTalk determined that Oracle makes up around twenty-two percent of China's total supply of compute. Bloomberg also reported last month that Moonshot had access to twenty thousand NVIDIA H200s to train Kimi K three. This compute was reportedly provided by Alibaba, although they deny the cluster contains H200s.

Now, an H200 cluster of [00:06:00] that size 

shouldn't be possible under the current export controls as licenses haven't yet been issued. Bloomberg was unable to confirm the location of the cluster, but heavily implied it could be located overseas and rented by Alibaba The information offered conflicting reporting that the training cluster actually contained current generation Blackwell chips And around the same time, an administration official accused Moonshot of acquiring Blackwell chips and setting them up for remote access in Thailand

Now, this is all legal. The export control regime only prohibits the import of advanced chips and does nothing to stop them from being installed in another country and then leased to Chinese firms. During its final weeks, the Biden administration proposed rules thatwould restrict chip supply routed to third countries, but those rules were scrapped on day one of the Trump administration.

the Trump Commerce Department is now reportedly looking into the practice. Per sources familiar with the situation, Bloomberg writes



260810 hed_EDIT: the effort involves compiling a list of countries with alleged black market operations to get restricted Nvidia chips physically into China, well within enforcement's usual purview. But the division will also draw up a list of countries where Chinese firms access the [00:07:00] chips remotely, which isn't typically an enforcement question because it's not illegal.

Draft rules that prohibit the export of advanced AI chips into Malaysia and Thailand have been circulated, but none have made it past the drawing board Part of the issue is the convoluted nature of these arrangements

According to Bloomberg, Alibaba accesses chips in Malaysia through a Singaporean shell company controlled by a Cayman Islands entity, which is ultimately owned by Alibaba. Meaning, of course, that simple identity checks on compute supply are unlikely to be effective the chips are also installed already, meaning that a forward-looking crackdown on imports would do nothing to the existing data centers

centers Speaking of Speaking of Alibaba, an interesting business model experiment might be afoot. During last week's release of Qwen 3.8 Max, some were surprised that Alibaba wouldpublish the weights to their flagship model Earlier this year, Alibaba hadsignaled a shift away from open source

With Quen team founders stepping away from the company, management signaling a more commercial direction, and multiple flagships, including Quen 3.7 being kept as closed source

That's why folks are very excited to see that Qwen 3.8 Max was released [00:08:00] with the announcement that the full weights would be forthcoming. According to Reuters, however, there is a catch Reports suggest that Alibaba plans to demand revenue sharing from large commercial users

And while the specifics of revenue sharing deals are still being finalized, we can perhaps look at Moonshot's Kimmy K3 release for the blueprint. Moonshot kept the weights proprietary for the first week to ensure that they captured all the curiosity revenue from the release

After that, they reportedly signed 30% revenue sharing deals with all major inference providers, allowing Moonshot to retain pricing power by limiting how much the model can be discounted through other providers. Even now, none of the suppliers on Open Router are offering K3

for more than a 7% discount

Paddy Srinivasan, the CEO of inference provider DigitalOcean, described this as the freemium model for AI

And Korean aggregator Cozy Bear added

Everyone is trying to figure out how to get paid for open weights, and revenue share is the most honest attempt so far. It doesn't pretend the model itself is the product. It treats the model as infrastructure with a toll booth. The interesting part, they continue, is enforcement. You can't track who's making money on top of your weights, so this is mostly as a signal to enterprises.

Use Qwen, and when [00:09:00] you win, we want a seat at the table. More like a relationship contract than a tax. Open source AI just entered its licensing era

era Lastly Lastly today, one functional update. Auto mode is now the default for Claude Code, marking a big transition point for work automation. Auto mode allows the user to set Claude on a task that gets completed without interruption. Claude will only prompt the user if a code change is extremely significant, i.e.,

irreversible, destructive, or aimed at something outside of your environment. Auto Mode was first introduced as a preview feature in March with the version prior to that being the dangerously skip permissions command. the alternative to that was hitting enter every couple of minutes to skip the latest notification and keep the session going

after iterating on auto mode, however, Anthropic now believes that skipping permissions isn't that dangerous and in fact could actually be safer than seeing a prompt for every code change. They conducted a study with over 1,000 testers, finding that auto mode caught eighty-nine percent of harmful actions.

Human reviewers only caught thirteen point six percent of harmful code changes. Anthropic suggests that this is down to approvals [00:10:00] becoming basically automatic, with their users approving ninety-seven percent of code changes. One of the interesting things about the evolution of auto mode is that it has forced Claude Code to work in a safer way.

The system uses a classifier to detect destructive or irreversible code changes and block them, and when this happens, Claude typically finds a safer way to achieve its goal. Only once it runs out of safer options does it alert the user. Auto mode will now be the default for pro, max, and team plans, but will remain opt-in for the enterprise Still, when it comes to those enterprise users, Anthropic suggests there are significant benefits to using Auto Mode. They claim that Auto Mode users ship twenty-five percent more PRs, and that many organizations, including Adobe, Gusto, and Garner Health, are already running Auto Mode as their production default

uh, for the team at Anthropic, perhaps unsurprisingly, auto mode is the default, with Claude Code creator Boris Cherny commenting, " The team and I use auto mode exclusively and have been for many months. I couldn't imagine going back to permission prompts.

Really excited to get this out to everyone."

The ascendancy of auto mode isanother example of how our default patterns of interacting with AI are changing, which provides the perfect [00:11:00] segue to our main episode A primer on the latest buzzy buzzword, graph engineering If you're leading AI inside an enterprise, you already know that the gap right now isn't capability, but execution. That's why KPMG's You Can with AI is back with a new season featuring conversations with leaders like Serojia Chatterjee of Emma, May Habib of Writer, Ellery Fisher, and others focused on practical execution.

One thing I keep seeing in enterprise AI, companies hedging across every cloud, every model, every framework, or paying a GSI for a pilot that never ends. The teams actually shipping, they've picked a lane and they move fast.

One conversation with robots and pencils and you'll know.

Nathaniel Whittemore: We'll go back to the AI Daily Brief Today we are discussing the latest buzzy term on AI Twitter, which is graph engineering

260810 main_EDIT: Now this one admittedly is a little confusing because A

It sort of started tongue in cheek and B, depending on who's talking about it, it kind of is describing two different things But I actually think that the concept at least is useful to situate relative to the lineage of engineerings we've had from prompt to context to harness to loop and so I think it's worth doing this primer.

And indeed, this is definitely more a primer on graph engineering than a complete guide to graph engineering. I wanna bring you up to speed on what this term is and why I think it matters

So the tweet that kind of kicked off this discourse came from OpenCL creator Peter Steinberger. Back in mid-July, he wrote, " Are we still talking loops or did we shift to graphs yet?"

AI creator Matthew Berman captured the [00:15:00] feelings of many when he said, "Bro, stop. I'm on vacation."

and and while almost immediately

the Twitter article boasters got to work

Big, bold declarations like loop engineering is dead, long live graph engineering We're visible all over the place

even after, but after this initial phase of hype and bluster, there is in fact actually something interesting here

So let's talk about all of the things that have had engineering around them. The first blank engineering that we had was, of course, prompt engineering. This was what a lot of the AI courses around '23 and early 2024 were all about. And depending on which corporation you look at, still unfortunately the substance of a lot of those upskilling courses today.

The idea of prompt engineering was a recognition even then that we were shifting how we did work. Instead of doing all the work ourselves, we were deputizing an AI chatbot to do some amount of that work. Now, whether that was final production or just some intermediate step like research

we still needed to find ways to optimize what we were asking for to get the best results. That was prompt engineering

At various points in the life cycle of prompt engineering, you had,[00:16:00] tips and tricks ranging from

telling the AI to pretend it was a certain type of person

To fancy JSON engineering

which use this complex way of typing to theoretically better structure requests. And we kind of had every other thing in between as well

by late Heading into 2025, however We started recognizing that the prompt was only one part of getting the most out of AI

we didn't just need to be good at asking for things in the right way. We also needed to be good at giving AI all of the information and knowledge it needed to do a good job with whatever that prompt was

to take a simple example, if you're asking your LLM To create a highly successful on-brand marketing campaign

Nathaniel Whittemore: Well, 

260810 main_EDIT: first of all, it needs to know what on brand is, which means giving it access to brand guidelines and potentially other write-ups in the past about things like brand values



260810 main_EDIT: and in order to have it not just be guessing at what good means, it would probably be helpful To give it stats and analytics from previous marketing campaigns

perhaps with some subjective reflections on what worked and what didn't as well. That body of information, that surrounds the prompt is the context. Context engineering

was [00:17:00] all about making sure

that all of that type of information was accessible in the right way. have-- Now, here at this point, We also have an interesting split, which I think we're gonna see once again with this latest graph engineering term.

s- the split broadly speaking is between technical folks and software developers and everyone else For the software developers, context engineering wasn't just a matter of making sure

that your AI had access to the right files for the job. It was in fact an actual engineering task

it was thinking about not just what information is useful



260810 main_EDIT: but designing the technical systems by which the AI 

Nathaniel Whittemore: could traverse the web of accessible context in a way that didn't just spend the entire context window

260810 main_EDIT: On this side, context engineers were actually thinking in terms of context budgets



260810 main_EDIT: making sure, for example, as they were designing applications

That certain parts of a process didn't get bogged down in context while others could go deeper when they needed it



260810 main_EDIT: so so here we have context broadly referring to the same thing, but engineering being a literal engineering task for the engineers and a mindset for everyone else in terms of how they organized information around the LLMs that they were using

Now [00:18:00] this year, just like everything else has sped up, we've also had a speed up in the succession of blank engineering type of terms



260810 main_EDIT: starting with you've probably heard me talk about harness engineering

Nathaniel Whittemore: 

260810 main_EDIT: the harness is of course the environment that exists around a model

on a simple level that might be an actual software tool like Claude Code and Codex

But the more expansive definition of Harness includes everything from the tools to the permission sets

to the skills files

that an AI or agent has available to it to do its work

Nathaniel Whittemore: throughout 2026, people have become more and morecomfortable with the idea that the agent is actually a combination of the model and the harness that surrounds it

260810 main_EDIT: some... This is why, for example, when we're getting new benchmarks Companies will now explain what harness the benchmarks were run in, as that's actually an important part of the story

Now, when it comes to harness engineering, once again, we've got two very different meanings of engineering

there are, of course, the actual engineers and software developers who have beenbuilding different and better harnesses and trying to advance our understanding of harnesses in general.



260810 main_EDIT: and then there's the more individualist, and then there's the more individualist, sense of harness engineering 

Nathaniel Whittemore: which is about things like

260810 main_EDIT: which skills you surround your [00:19:00] agents with, and what tools they have access to

Now you see here That as each of these new terms comes online, it's not like the old one goes away

Prompt engineering is certainly the one where there'sprobably at this point the least leverage to be had. but it's not like because we started to understand the value of harnesses All of a sudden, context stopped mattering. In fact, quite the opposite, the harness became a new context for that context engineering

So we've got the prompt which controls the instructions. We've got context which controls what the model sees. The harness which controls the environment

And that brings us to the loop

which controls the iteration that an agent goes through to accomplish a goal 

loops or loop engineering, which has become a big topic over the last few months, is about thinking about your relationship with agents in different ways. 

The canonical short explanation, once again, came from OpenClausPeter Steinberger, who said, " You shouldn't be prompting coding agents anymore.

You should be designing loops that prompt your agents."

Loops are the systems by which an agent can observe, plan, act, check results, and repeat until some measurable [00:20:00] stop condition is reached

in, as we've discussed in the past on this show

one of the big challenges for non-engineers who have beentrying to put loops to work

is in figuring out which aspects of their knowledge work have those sort of measurable stop conditions

One of the things that we discussed in my show about loops from a month or two ago



260810 main_EDIT: was this idea that in some cases where there wasn't a natural measurable condition, to get an agent working in this sort of loop you were going to have to precisely define something measurable like that to actually get the loop to work

But what you'll notice here is that a loop is about how to get the most out of a single agent or agentic process

It is a work backwards from a specific goal

that gives the agent the repeatable steps it needs to follow that as many times as is necessary to actually achieve that goal

Nathaniel Whittemore: But what about when a goal is more complex and requires multiple different processes interacting to actually accomplish whatever that goal is? 

260810 main_EDIT: What about when we move beyond

the output being a single agentic process to actually designing an ongoing agentic system for working That's where we get into graph [00:21:00] engineering

If prompts control the instruction and context controls what the model sees, harnesses control the environment and loops control the iteration, the graph controls the new agentic organization. Graft engineering is about designing how multiple agents

tools, knowledge sources And humans interact and connect

Nathaniel Whittemore: 

260810 main_EDIT: graft engineering describes both the parts of the system which some people are referring to as nodes. That could be agents, routers, or human gateways, And graphed engineering also explains

the interactions between those nodes which handoffs are permitted

what information or state travels between them

ExplainX.ai explained a loop as an autonomous cycle for a single agent. A trigger fires, an agent acts, a verifier checks, and if not done, the whole system is retried with updated context until the goal has been met

As they right every guardrail i.e., max iterations, token budget, etc., applies to one agent's run. The loop is the agent's behavioral contract with itself. A graph, on the other hand, is an organization of agents

As they put it, each node in a [00:22:00] graph is an agent running its own loop

The edges or interactions between those nodes define data flows and dependencies

They continue, " The graph specifies who exists, which agents and with what specialization, what each owns, their domain context and tool access, how work moves sequentially, in parallel, or conditionally I e. is this a loop between different loops?

and finally, the graph defines what happens on failure. Is the node retried? Is it routed to a fallback? Or is there an alert upstream

The graph, they conclude, is the organization's operating structure. Loops live inside nodes. the graph connects them

In In short

A loop is how an individual agent does its job

where a graph is how an entire agentic organization works. as Google's Shubham Sabhu put it, " Loops made agent behavior programmable. Graphs make agent organizations programmable."

now now what I don't expect is for all of you to run out and start designing complete agentic organizations But the idea of graph engineering

is to be able to think in those system terms.



260810 main_EDIT: [00:23:00] And even slightly differently from the context in harness engineering With loops and graphs, while sometimes you will use both of these patterns

there will be times when the simpler architecture of a single loop is going to be fine

When a single job has a clear finish line with genuinely sequential steps and one agent's context window able to hold the whole domain

that's a good candidate for a single loop When the work instead splits into specialties with different handoffs when parallelism becomes valuable, when different steps in a process want different models or tool sets, when routing has to be explicit

And when you want to design a resilient system where the failure of one node doesn't take down the rest the, That's where you get into this actual graph engineering



260810 main_EDIT: as that, now as tends to happen, as soon as we get a new term, we very quickly explore all the nuances as well. one discussion, for example, that you're seeing a little bit is the difference between org graphsversus work graphs.

graphs, org graphs are gonna be more stable agentic systems that defines a more permanent style of setup. The org graph is gonna have long-lived agents, with each agent owning a domain [00:24:00] and accumulating context over time, preserved memory, and stable relationships and dependencies that don't change unless explicitly told to

So if you were designing an agentic organization that's going to do the same thing over and over again, for example, if I was designing a multi-agent system that automated the process of going from research to production to editing 

to publishing, to extracting insights, to posting. That might be a good candidate for an org graph because these are ongoing recurring processes.

This is just how my work happens day in and day out The work graph, on the other hand, is more dynamic and more ephemeral 

it can include task nodes that only exist as long as the work exists.

Dynamic edges, remember edges are the interactions between the nodes

that can split or merge

an, an adaptive structure where tasks can disappear when evidence makes them unnecessary or new tasks can be spawned if new complexities are discovered

but let's wrap up this primer by coming back to the main point

Like I said at the beginning, my expectation is not that all of a sudden

you go out and design complex agentic organizations now that you are [00:25:00] acquainted with this wonky concept of graph engineering. What I think is valuable for all of us, however, in the same way that even if you weren't designing loops, understanding the architecture of a loop

A trigger that fires, an action that's taken, A validator that checks the work and then that on repeat until it's done. That is extremely helpful in thinking about how to use agents to automate chunks of your work In the same way what I think graph engineering will unlock for many is the ability to start thinking in multi-agent systems terms



260810 main_EDIT: where you can start to see different agents with different jobs

and actually understand and even design their relationships with one another

over time, some of you I guarantee will start to design those more complex agentic systems

and the best practices and lessons and tool sets that people build around this graph engineering discipline are going to be extremely useful when you do

So yes, graph engineering is the latest buzzy buzzword

And some of the early tweets about it were frankly tongue in cheek But designing agentic systems is, I believe, a new work [00:26:00] primitive and something which we will increasingly be called upon to do So hopefully you now have a better sense of that and can dig in as makes sense for you. For now, that's gonna do it for today's AI Daily Brief. Appreciate you listening or watching as always, and until next time, peace. 

​ 

Nathaniel Whittemore's audio recording:
