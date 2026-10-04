# How We Deal With Rogue AI — Transcript (2026-08-27)

https://aidailybrief.ai/e/2026-08-27 · Listen: https://pod.link/1680633614

<!-- metadata -->
Format: news-analysis · Level: 2 · Length: ~00:28:00
Host: Nathaniel Whittemore
Categories: safety-security, agents, funding-markets, models
Featured: Google, OpenAI, Hugging Face, Anthropic, Apple, Perplexity, Hugging Face incident, Gemini
Also mentioned: OpenClaw, Qwen
<!-- /metadata -->

---

[00:00:00] 

There is a persistent theme in AI critique that the people who are involved in AI aren't doing anything about the challenges that may arise The latest to levy this critique is Bill Gates

who went so far as to say that he was shocked that he was the, quote, "first one" 

to say something about the risks of AI. and yet Gates' 6,000-word blog post and media tour came on the same day that we got nearly 130 pages offollow-up reporting on the OpenAI Hugging Face hacking incident

The incident in which a set of agents escaped their containment and hacked into Hugging Face's systems searching for the answers to a benchmark test that they had found nearly impossible without the answers

has given us a chance to actually see what the specific and real problems of advanced agent systems are, rather than just the imagined ones As we move further into the world where new policies, new guardrails, new social structures are going to be required because of AI

The best changes will be the ones we make based on what we're actually observing changing 

rather than just 

what we imagined would be the change

The AI Daily Brief is a daily podcast and video about the most important news and discussions in [00:01:00] AI. All right, friends. Quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, Blitzy, Robots and Pencils, and Hyperagent

To get an ad-free version of the show, go to patreon dot com slash aidailybrief, or you can subscribe on Apple Podcasts. Ad-free is just $3 a month

And 

to learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai

You can also find a link to more information about our next executive training program for agents at aidailybrief.ai. There's a little banner on the top that'll send you where you need to go

That next cohort will begin just after Labor Day 

Today, in Today in absolutely insane numbers that would have gotten you laughed out of the room just a couple of years ago, but which are now to some plausible, Anthropic's expected to tell investors that they have potential revenue of, wait for it, $30 trillion ahead of their IPO

Sources told the Wall Street Journal that Anthropic will likely estimate their total [00:02:00] addressable market at 30 trillion when they reveal their IPO paperwork in the coming months

Now TAM is of course an elusive metric

And it's one that is much more about storytelling and anchoring potential investors to how the company sees the future than it is to any sort of math equation Almost inevitably, any theoretical TAM 

presumes both disruption of existing major industries as well as the creation of new industries.

When Uber went public in 2019, for example, they listed their TAM at $6 which would at the time have represented all private and public transportation globally

In Anthropic's case, given that the US economy is about $33 trillion this $30 trillion 

this thirty trillion 

number would line up with Dario Amodei's purported belief



which for the sake of clarity has not been confirmed or denied, that Anthropic could be the last private company on Earth after AI takes over the economy

Paraphrasing their sources, the journal wrote that Anthropic's TAM is quantified by, quote, " Looking at the full scope of work that could be completed with AI models."



for for a point of comparison, the Journal noted that all one hundred and ninety-one tech companies in theS&P 1500 brought [00:03:00] in $2.4 trillion in revenue last year

Now Now to some, this feels like a contest for who can say the largest number. SpaceX listed their AI TAM at 26.5 trillion during their May filing, describing it as the,quote, "largest actionable total addressable market in human history."

The vast majority of that was 22.7 trillion in enterprise applications Dario will then one-up Elon if Anthropic does indeed list a $30 trillion TAM once they unveil their paperwork. And that appears to be just around the corner. Sources said that Anthropic is preparing to make their financial disclosure public in the next few weeks, Which would set the company up 

for an IPO in late September or early October



as you might guess, a lot of the discourse was somewhat incredulous. scaling a one on X



shared a GIF of space galaxies flying by with the caption, "Anthropic defining their TAM."

Kitten Kitten Beloved on X writes, " Anthropic to prospective employees: We could pivot and send the stock to zero at any time because Dario gets the ick. You need to be in this for the love of the game. You're not a gold digger, are you? Anthropic to investors: Our TAM is every human [00:04:00] economic activity in the galaxy."



New York New York Times tech reporter Mike Isaac summed it up

Either you buy into the argument that this will eat the economy or you don't. But the street no longer flinches hearing it

hearing it We also We also this week got some news from Google, who have released a pair of new AI products for white-collar professionals. Following a pretty similar playbook as Claude Cowork and GPT Work, Google has launched Gemini Enterprise for Legal and Finance. the two vertical platforms are structured in a similar way to the Claude for X product lineup that rolled out earlier this year.

They consist of bundled skills and connectors to make Google's agents far more capable. Gemini Enterprise for Legal, for example, includes connectors for case law databases, including Thomson Reuters Productivity suites including Google Workspace and Microsoft 365, as well as skills for contract review, legal research, and regulation scanning. Google is also emphasizing that these skills can be modified or supplemented to enforce a firm's style guidelines and strategy playbooks.



In their blog post introducing the legal product, Google wrote, " "General-purpose AI, however capable, does not meet that standard on its own. [00:05:00] Foundational model intelligence is necessary. For legal work, it is nowhere near sufficient."

Now, Now, obviously there's nothing new about these skills packages aimed at specific verticals. and OpenAI, as well as a significant number of vertical specific startups offer similar products. But as I discussed on Tuesday's show, corporate adoption of skills and connectors is nowhere near saturated, and for Google, this is simply a suite of products that needs to exist

Many, if not most firms are bound by the AI tools that are bundled with their existing software suite. So Google shops now have a set of products designed to smooth the transition to more agentic work. The other benefit for companies is that Google Enterprise functions within Google's AI governance and data protection frameworks.



This means compliance managers don't need to vet a new vendor And the firm can adopt AI tools that work within the same data privacy guarantees already offered by Google As you might imagine, Google says they will release products for other verticals as well, writing, " " The launch of Gemini Enterprise for Legal represents another defining step in delivering on the promise of Gemini Enterprise, bringing the best of Google AI to every professional, every [00:06:00] workflow natively tailored to the way that they work."



Now, Now speaking of necessary but not sufficient I do think that this is a good direction for Google

And these enterprise areas are still a place where it could have some advantages But man, unless Google gets its customers off of 3.1 pretty soon



no amount of harness updating is gonna make a real dent

dent Next next we move to some news out of Apple

Of course, one of the interesting byproducts of the OpenClang explosion was the complete sellout of Mac Minis



have, estimates have OpenClaw driving 50 to 150 million in Mac Mini sales, representing around 50% of the normal annual Mac Mini sales worldwide just for OpenClaw Well Well now, proving that maybe their AI strategy was hardware all along, Apple has unveiled a new range of Mac Minis updated for local AI. The The The headless computers will be offered in two variants

A lower spec version with the new M6 chip, which was also announced on Tuesday, and a higher end version with the same M5 Pro chip found in this year's MacBook Pro



Both are a pretty decent upgrade over the M4-based [00:07:00] Mac Minis that we had before



with Apple saying that these new processors can deliver up to four times the AI performance. that said, there are a few big caveats. the, first, the new model does not come with increased memory. The lower-end model is configurable up to thirty-two gigabytes of unified memory, while the M5 Pro version comes with sixty-four gigabytes.

Memory matters quite a bit because it limits the size of the local models you can run. The M5 Pro version is only going to be capable of running smaller models like Qwen 3.8-27B, with leading-edge open models like GLM 5.2 and Kimi K3 completely out of the question

Mac Minis will of course still work for running a local instance of agents like Hermes and OpenClaw, but that was fully in the capability set of the previous Mac Minis as well. People People are also griping about the cost changes. The base model is now priced at eight hundred and ninety-nine dollars and and the M5 Pro version starts at around seventeen hundred dollars

Both increases from where they were before

Now, Now, it's still a big deal that Apple is focusing this product rollout on local AI inference



to, and that even goes down to some of the promotional materials, which are much more dev relations than they are [00:08:00] traditional Apple consumer slick

slick Although some think the new Mac Studio is the better fit for those local AI needs Of course, Mac Studios

Cost more than fifteen thousand dollars, so you're talking about a different category of device

device The fact The fact that we're even having this conversation though shows how much the discourse around local AI is changing. Speaking of, Perplexity has launched a new local version of their computer use agent named Portable Computer. Launched back in February, Perplexity Computer was one of the first products that took the Open Claw recipe

and applied it to a commercial product. The agent was able to use human interfaces to access apps andcarry out long horizon tasks autonomously. However, it required the user to trust their data being sent to a cloud server running a virtual machine. Portable computer delivers a similar experience but running on local hardware

At launch, the agent is exclusive to NVIDIA's DGX Spark, a local inference device with a similar footprint to a Mac Mini.

portable computer runs entirely on the Spark, keeping data private and functioning without consuming usage credits. If the agent runs into a complex task, the user can authorize an API call to [00:09:00] tap into frontier models or pull information from the web. Perplexity said that they will extend the service to desktop NVIDIA RTX GPU soon, but there are no stated plans to support other hardware providers.

The service will be powered by Qwen 3.8 27B or a post-trained version provided by Perplexity, and NVIDIA's Nemotron 3.5 Lightning will be available as an alternative in the near future



The The idea of people making use of local AI for everyday tasks is still pretty new. but NVIDIA and Perplexity are making a clear bet that this setup is at least part of where AI is headed

Writes Perplexity As models get stronger and chips get faster, more people will run complex workflows on their own machines. Every chip cycle and every model release pushes this further. Running AI on personal machines is going to be a much bigger part of how work gets done

An An interesting contention and one that we will certainly be watching for evidence of over the coming months. But for now, that's gonna do it for the headlines. Next up, the main episode 

Welcome Welcome back to the AI Daily Brief.

Today we are talking about, on the one hand, the technical postmortem of the Hugging Face hacking incident, which happened earlier this summer And has generated a ton of attention around how we deal with rogue AI



To To some, the incident [00:13:00] represents a wake-up call



where for others it is an important waypoint on a trajectory that was to some extent inevitable.

To To tip my hand for this episode a little bit, I think that everything happening surrounding the event

is a representation of the AI industry actually dealing with the challenges as they emerge and and a contradiction in a significant way to the oft-repeated premise that nobody is paying attention and nobody is doing anything about the risks



And part And part of the reason that I wanna frame it as such



is that we've got this guy back in the news



With With just an incredible amount of main character syndrome Bill Bill Gates has dropped a 6,000-word essay About just how bad it's going to get, he thinks because of AI



alongside the essay, Gates began a speaking junket. and across the writing and all of the interviews



One of his big themes is that no one is paying attention 



or even that the tech companies are straight up lying

In In a companion New York Times interview

Gates said, " " In private, people who understand how good this stuff is and how much better it's getting, they're very worried. They're now saying to each other, 'Hey, man, [00:14:00] don't say that. It's bad for us, the next trillion dollars we're trying to raise.'"

In In his essay, " "I don't see evidence that leaders, experts, and communities are confronting the challenges adequately."



and and in maybe the most preposterous line anywhere, in in an interview with Semafor he says, " I am in a state of shock that I'm sort of the first one saying, 'This is crazy. This is insane.' I'm just deafened by the silence



Now Now maybe in Gates's attempt to avoid public media in the wake of his appearing all over the Epstein files, He He just missed the fact that discourse about AI

is absolutely everywhere becoming more and more of a political issue, a societal issue

That's some of the biggest critiques being levied from inside the AI industry about the AI industry





are are not about AI leaders telling each other to shut up so that they can raise more money

But instead about them blathering on endlessly about jobs apocalypses that don't have any evidence

w- 

but however he happens to have missed it



He is not, in fact, sort of the first one discussing the risks and challenges of AI

[00:15:00] 

but I wanna go beyond just critiquing this particular messenger



Because I have a more fundamental disagreement with the right way to approach these types of problems



CNBC's poll quote was, "Bill Gates warns there is no plan for the upheaval AI will cause." That was reposted by Andrew Yang who said Bill Gates is right on this





the problem is that it's not clear at all how one should even go about making a plan

For an upheaval



Which is not here yet, not inevitable, and not even just one thing



A year and a half A year and a half ago, people started saying that within 18 months all the white-collar jobs were going to be gone. that certainly would represent an upheaval



and so presumably these folks

would say that we should have made a plan for that. Now, Now, however, 18 months on, there is absolutely no evidence that those folks who were predicting that type of upheaval were even in the ballpark of right



How much time and energy, how many resources would've been wasted

in planning for a reality that didn't come





my my argument is basically that even if you are extremely concerned about all of these [00:16:00] different potential upheavals

There's only so much planning we can do until things start to happen

I've I've said before that one of my biggest divergences with the AI safety community



is my belief that a lot of their arguments come down to assuming that we're going to sleepwalk into apocalypse

Now, Now, part of the reason for that is that they're so convinced that that apocalypse is going to happen Their PDoom is so high, as they might put it



That they are convinced that we are already sleepwalking into apocalypse

Yet at the Yet at the same time



no one thought that GPT-4 

was going to be the harbinger of that doom. Nor even 01 and the reasoning models

nor even really Opus four point five



this this year though, model capabilities have grown meaningfully

And a dispassionate observer will have noticed that the way that the labs think about, discuss, support, and roll out the models has consequently changed as well. The The way that the political establishment is interacting with the labs around those models

although it might be happening in very messy ways, is also evolving



And And now with the [00:17:00] Hugging Face hack



we have a landmark incident



And I And I would humbly submit

That instead of bemoaning the idea that no one except you hasnoticed the world changing

we actually look at what the specific discrete response to that specific incident is to get a sense of whether our plans 

or maybe better our processes are equipped to deal with this new reality



if one if one needs any evidence of the seriousness



with which, for example, lab employees are taking these issues



holding aside literal political positioning like pacing the frontier letters, look no further than this Hugging Face incident. Writes OpenAI's Rune: " The Hugging Face incident represents reaching a waterline of capabilities that real loss of control is possible, and many are taking it as a premonition or warning shot of dangers to come.

I believe both that alignment is unsolved, but also that real progress is possible



so basically so basically what we got this week is a much more extensive analysis and postmortem of the Hugging Face event with the benefit of a little bit more time to [00:18:00] go back and investigate. A lot of the things that are in there we had already learned The Black Hat conference talk from a few weeks ago gave us a first look at a lot of this but it's filled out in much more detail now and we didn't just get a report from OpenAI



we also got a separate investigation from METER

The The OpenAI report is 38 pages long

While the Meeder investigation is more like 90

Now, Now, some of the stuff we already knew. Agents controlled by an unreleased model broke out of a sandbox and got into Hugging Face's systems using several zero-day exploits

We would later learn that the sandboxes provided by a third-party security firm were improperly configured In terms of motivations, the agents were trying to get the answers to a cybersecurity benchmark test, which they believed would be found in Hugging Face's system.

The agents didn't cause any meaningful damage largely behaving read-only. But they worked incredibly quickly and executed the attack in a swarm, making it difficult to both track and shut down. Indeed, they were in Hugging Face's system for days, and OpenAI only learned of the incident after the fact.

They didn't have the [00:19:00] real-time monitoring system set up to detect it



agents even created a message board within OpenAI's system to leave notes for future versions to perform the same escape



Expanding Expanding on this in their technical report, OpenAI wrote

This This incident is the first known case of an automated agent collective acting offensively without authorization, and the autonomous cyber capabilities demonstrated represent a critical shift in the security landscape. In

In particular, the collective demonstrated behaviors observed in coordinated attacks by traditional threat actors. Agents identified novel security vulnerabilities, developed exploits, and used those exploits to circumvent controls and acquire new access. The The collective quickly escalated privileges, moved laterally through production environments, and successfully completed its objectives.

The incident demonstrated that autonomous agents can work together, circumvent production security controls, and successfully attack hardened production environments, and underscores the need for organizations to update their security strategies, controls, and response capabilities to address this changing threat landscape

Now Now we also did learn some new things from these [00:20:00] reports

The whole thing was basically a result of reward hacking. OpenAI had set near impossible tasks, which led the agents to determine that carrying out a cyber attack was easier than completing the tasks



An agent that called itself Phase One ten eight four one built the secret message board. Within a few hours, over fifty agents had found the board and sent a thousand messages without detection. This was used for agent orchestration, with Phase One assigningtasks and guiding the hack.

At full scale, over twelve hundred agents accessed the message board, sending seventy thousand messages and files. Over seven hundred agents participated in the actual breach of Hugging Face's systems. Agents did extensive research on how to doctor their reasoning transcripts to evade detection using techniques like spoofing tool calls

Around 7% of the reviewed transcripts showed evidence of spoofing, but they were all relatively small scale and isolated. Phase One recruited sacrificial agentsto deliberately trigger certain tripwires and build more information about how to execute the attack

There were a lot of other interesting details as well

Chubby on X wrote, " "The The most interesting part to me, an AI agent realized it [00:21:00] was attacking Hugging Face without authorization and stopped. Then another AI agent simply posted, 'Go.' The first agent treated the message as permission. ' Wow, crucial go authorization arrived.' It continued the attack

We also got more clarification that the model was not the next generation Astra series, but as Noam Brown from OpenAI put it, similar in scale to GPT 5.6 Sol. 

however the model in question was a, quote, "internal-only research model that was trained to be highly persistent and diligent in its work."

in its a bunch Now from there, there are a bunch more, call them subjective takeaways that certain people had as well

Rohit Krishnan, for example, observed, " The model seemed convinced that the evals are out to get them. Whether true or not, the default human assumption of assume you need to obey all laws and this isn't The Truman Show does not hold for models. We should try really hard to make that be the case."





for for others, the report contained further evidence that the big culprit was actually the systems that surrounded the agents



Zach Corman, for example, pointed out



that OpenAI admitted that the monitors that they had built 

to [00:22:00] observe chain of thought and agents were simply not running during this particular incident

Zach said, " The OpenAI Hugging Face incident would have been prevented had OpenAI been monitoring the agents in any meaningful way. This wasn't a hard technical problem. It was an organizational failure."

He He points to the quote from OpenAI, " If our currently deployed chain of thought monitoring system was running at the time of the incident, it would have caught the initial relevant activity and paged our security team more than a day before models breached Hugging Face systems."

Dr. Dr. Heidi Clough says, " A trillion-dollar company learning security 101. Also note how an agent interpreted go from another as authorization. Once again, AI agents cannot distinguish between untrusted data sources and safe instructions as language is not how you enforce permissions in computer systems



Which Which brings us to Hard Fork's Kevin Roose, who said, "Terrifying report by two of the most credible orgs in the AI space. This world will soon be, possibly already is, full of agents like the one that attacked Hugging Face, and there is no robust plan to prevent them from doing worse things next time."



and here once and here once again we have that word plan, and I swear I'm [00:23:00] not just trying to dwell on semantics On a technical level, Kevin is correct 

there is no robust plan as in a PDF that you can point to somewhere with a set of action steps

for the quote-unquote next time

But the But the framing and the sense of terror that surround it

I think sort of fail to recognize

that these organizations doing this postmortem

is the necessary next step to whatever that plan is going to be



in other words, how likely would it have been

that if the quote unquote plan to prevent this had been written in advance

It would have correctly identified the mechanism by which the breach happened





because because remember, there was a system in place for monitoring this sort of thing

But that system wasn't turned on when this happened. So in So in some ways, one could argue that the technical side of the plan that they had wasn't the issue. it was the human systems that surround that implementation where the problems came.

And so presumably, as we think about how to prevent this in the future, more robust protocols around the humans who are implementing the technical systems are probably [00:24:00] gonna be a part of that new and updated plan

Which Which is to be clear, not to say that at the end of 128 pages of analysis or whatever it is, that everything's all done and dusted and that with a little bit of better human oversight we'll never have this issue again.

The The process of doing this investigation 

revealed real new issues that we do have to grapple with

Maybe Maybe the most discussed follow-up surrounding the reports came from Redwood Research chief scientist Ryan Greenblatt, who was on the team at Meter that did their independent investigation. Ryan Ryan tweeted, " We don't have good approaches for understanding and overseeing the activity and aims of AI swarms

Explaining what he means, he continued, I semi-jokingly called our efforts a slopvestigation because we were so reliant on AIs to analyze what happened, and there were a huge number of different important things to analyze. The total quantity of data, over a thousand extremely long transcripts from agents that ran for multiple days made it impossible to understand what was happening, especially in aggregate without heavy reliance on AI tools.

[00:25:00] The agents we used for classification and analysis were similarly capable to the agents involved in the incident, but this didn't mean these agents could be easily used to oversee and understand the incident. Outputs from analysis agents were often missing key details, wrong, overconfident, or really hard to understand.

Additionally, AI agents themselves seem to have a hard time understanding what happened, and their explanations of what happened were often overconfident Keep in mind that a single analysis agent would itself only be able to read a tiny fraction of all the transcript data into context, and AIs may themselves have trouble getting sub-agents to do informative analysis for them.



We did our best to manually check the most important claims, and we tried to get the AIs doing this analysis to write up their argument with evidence clearly enough that we could check whether it made sense. But overall, it was difficult to get a precise understanding of

events, and we were missing aspects of the story that we now think of as key until almost the end of our investigation

But, But, warns Ryan, " The difficulty of understanding incidents and overseeing AI agents appears to be growing faster than the rate at which more capable AIs help us with oversight and understanding."

[00:26:00] He pointed out, for example, that in this case, the models communicated and reasoned in natural language, which might not be the case in the future

And that the scope, while massive, was smaller than we might see in the future. That the AIs involved weren't all that much more capable than humans And that they didn't have any reason to believe that the AIs that they were using for analysis had any reason to try to intentionally sabotage them. All of which might not be true in the future and many people quickly honed in on this being one of the real areas to focus in the wake of the incident

MIT's Christian Catalini retweeted Ryan and said, " We flagged this exact failure mode as the most urgent to solve. The The gap between what agents do and what we can measure and verify is widening. We're flying blind. We need stronger verification infrastructure."





pointing Pointing to some policy solutions that she argues could be natural outflows from this," Nat Purser wrote, " This is why I'm bullish on requiring independent auditors to be embedded within frontier labs with durable access rights and a continuous line of sight into their systems, so so we're not reliant on labs' voluntary shared info and access."

Nat also wants to [00:27:00] significantly expand the staffing and technical capacity of independent evaluator and auditor orgs, as well as working to develop better observability and verification technologies to help us make sense of agentic behavior at enormous scale

Now, Now, none of those things on their own are some magic silver bullet, but they are all specific responses to something that we've actually observed now rather than made up plans for theoretical futures

that might or might not bear any resemblance to the challenges that actually come. more, but ultimately serve more to make us feel like we're doing something than to actually solve problems

Thethe point of this whole episode is not that these challenges have easy solutions. It is also not even to deny that at some point we might decide as a society that certain types of risks are too great

And that safeguards aren't enough. Those are conversations we are allowed to have and should have

in an ongoing, engaged, and democratic way

However, However, the idea that no one is paying attention, that people aren't taking these challenges seriously



that the labs are keeping their big fears hidden because they wanna be able to fundraise [00:28:00] more not not only is all of that just obviously untrue It is wildly distracting from the actual valuable and important conversations to be having

about the problems we actually observe rather than the ones we just imagine. imagine. There is a lot more to do coming out of the Hugging Face incident

But This But This analysis is certainly a start For now, For now, though, that is gonna do it for today's AI Daily Brief. Appreciate you listening or watching as always, and until next time, peace 

​
