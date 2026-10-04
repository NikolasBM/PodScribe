# What OpenAI and Anthropic Think Happens Next with AI — Transcript (2026-06-05)

https://aidailybrief.ai/e/2026-06-05 · Listen: https://pod.link/1680633614

---

[00:00:00] Today Today on the AI Daily Brief, what OpenAI and Anthropic Think about what happens next in AI. Before that in the headlines, is the US government gonna take a stake in the big AI labs? The AI Daily Brief is a daily podcast and video about the most important news and discussions in [00:00:15] AI.

All right, friends, quick announcements before we dive in. 

First of all, thank you to today's sponsors, KPMG, Section, Zencoder, and OutSystems

To get an ad-free version of the show, go to [00:00:30] patreon.com/aidailybrief, or you can subscribe on Apple Podcasts. To learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai. On aidailybrief.ai, You can also find out about everything else going on in the ecosystem, including a bunch of free education programs 

like the Agent OS [00:00:45] program. or you can check out some of the paid programs that we've been building with Nufar Gaspar leading, including the upcoming four-week AI executive sprint called Executive Catch-Up.

That is registering folks right now, but is going to be closing very soon. So if you want to check that out and get up to speed fast, check [00:01:00] out the link in the show notes 

Welcome back to the AI Welcome back to the AI Daily Brief headlines edition, all the daily AI news you need in around five minutes. And boy, do we have a juicy little end to this week. First up, bombshell reporting claims that the US government is in talks to [00:01:15] acquire equity in major AI companies.

Writes Notice, " Senior US officials have held primary discussions with major artificial intelligence companies about the potential for the federal government to acquire some shares in their firms." The commentary is sourced to three people familiar with the [00:01:30] matter. Notice adds that Sam Altman has discussed this idea periodically with senior administration officials since the beginning of the second Trump term.

In fact, Altman is said to have pitched the idea directly to the president in early twenty twenty-five. Discussions have reportedly continued with senior officials in recent [00:01:45] weeks. Sources said that Altman viewed this as a way to more broadly distribute the economic benefits of AI to the public. And what's more, people familiar with the discussion said that itcurrently centers on the idea of AI labs, quote, "voluntarily ceding shares to the government."

The shares would then [00:02:00] produce returns that could be directed to public purposes, such as cutting an AI dividend check to all American households Now that language of voluntarily ceding makes it a little unclear whether the government would pay for the shares

And sources also state that Anthropic is not involved in discussions about providing [00:02:15] equity at this time Now, for those of you with one eye raised on the sourcing, Notice is a relatively new publication but has extremely strong credibility. Founded by Politico reporter Robert Albatron. Former Washington Post reporter Jeff Stein is the lead journalist on this story, and Stein is generally considered to be one of [00:02:30] the most well-sourced and highly regarded journalists in Washington

Now overall, while some of this is fairly dramatic, it's also not entirely unexpected. This administration has floated the idea of building a sovereign wealth fund and taken steps towards it by acquiring minority stakes in numerous companies, including [00:02:45] Intel

It's also not, as we saw earlier this week, entirely novel thinking in Washington, with Bernie Sanders floating the idea of the government taking a 50% stake in AI companies through a one-time tax earlier this week

The idea has made for some strange political bedfellows, with figures on the [00:03:00] populist right finding themselves aligning pretty closely with Sanders

Responding to the Sanders proposal, Steve Bannon said this week, " You can smell the stench of desperation emanating from the oligarchs as they run heedlessly to a public market takeout. We should not take tip money, but force them to cough up [00:03:15] 50% of the equity to be dispersed to American citizens."

The horseshoe theory of American politics is well and truly intact

Now in terms of the public reaction

a lot of folks just question simply why taxation wasn't the right way to do this Georgetown Law professor Peter Harrell [00:03:30] writes, " The government should tax and regulate them and potentially distribute the taxes as a dividend, but ownership risks giving thegovernment control outside of public view and potentially the wrong incentives."

Bobak McGuffin writes, " What if they set up some system where the [00:03:45] company sent a certain percentage of their profits to the federal government every year in quarterly installments? Maybe the states could also choose to tax the companies if they operate in that state

Joel Griffith was more blunt, writing, "More, quote-unquote, capitalism but with Chinese Communist [00:04:00] Party characteristics. Brought to you not by AOC and Bernie Sanders, but by the current United States president."

editor, even Axios business editor Dan Primack wrote, " This is basically the Bernie proposal. really never expected that electing Trump would push the US government so far towards actual socialism. [00:04:15] Not even a judgment call, just surprise."

Now, Now, heading on over to a completely different type of topic, OpenAI hasshipped a huge update for their memory system, which they're calling Dreaming Now, some version of memory has been available in ChatGPT for a little over two years and has [00:04:30] already come a long way. Early versions of memory were very manual and pretty clunky, relying on a list of saved memories.

Users often needed to tell the chatbot to remember specific things and actively cull useless information from the list

Indeed, one of the big challenges of memory

is when it remembers [00:04:45] details that are no longer relevant. last April, OpenAI integrated the first elements of the system that would become Dreaming. It allowed ChatGPT to actively curate memories in the background, slowly building a more accurate picture of the user's preferences.

This upgrade made the process feel more natural and continuous, [00:05:00] eliminating many of the early pain points. 

With this release, OpenAI said that they have made the memory system much more capable and compute efficient. Individual saved memories are gone. Instead, the dreaming system will maintain a summary that provides richer context about the user.

The summary is fully accessible to the user and can [00:05:15] be edited directly to make corrections or add more information. OpenAI provided a simple example of where memory is useful in the context of asking ChatGPT aboutbuying peripherals photography setup.

Without memory, ChatGPT provides generic information and makes standard recommendations. With memory, the [00:05:30] chatbot can tailor its suggestions to the gear the user already owns

Now, OpenAI devised a new benchmark to test their system based on asking questions that required the model to recall relevant facts. With the 2024 version of Memory, which again was just the saved list of facts, the model succeeded on [00:05:45] 41.5% of tasks. The 2025 version, which added the early version of Dreaming, kicked that success up to 67.9%.

With the version of Dreaming announced this week, OpenAI found the model could succeed at 82.8% of tasks that required the recollection of relevant facts

[00:06:00] now if you have done either our ClawCamp or Agent OS program, You might be thinking to yourself, " This system looksa lot like building the memory.md file for an agent, or even something like the personal context project we ran the AIDB operators community

And indeed, one could be forgiven for thinking that [00:06:15] Memories is just about creating and maintaining a markdown file that stores crucial information about the user. The key difference is that ChatGPT is now running this process automatically through the back end, requiring far less of the average user to take full advantage

OpenAI also noted that the huge efficiency gains from [00:06:30] their new setup will allow them to provide dreaming to free users for the first time

Last summer, when paid subscribers gained access to Dreaming style memory, free users had only access to basic saved memories. OpenAI says that they've been able to cut down the compute requirements for Dreaming by 5X, meaning [00:06:45] it's now practical to serve at scale

Mark Mark Kretschmann argues that this is a bigger deal than it sounds, writing, " The more ChatGPT becomes an actual work partner, the less sense it makes to restart from zero every time. Projects, preferences, constraints, tools, writing styles, code-based details, all of this [00:07:00] should carry forward.

Sounds small, but it changes the product. A chatbot with real memory becomes much closer to a persistent agent."

I also I also think it's interesting in our context of how companies are adapting to the token scarcity era. you remember Arvind Jain, the CEO of Glean, wrote a piece about the token [00:07:15] economy that he called Your Token Spend is an AI Architecture Problem



And in it he discussed a lot of similar themes around token efficiency In short, all the time that you spend getting a model to remember all the relevant context each and every time are wasted turns and wasted tokens that could be fixed [00:07:30] theoretically through better memory systems

so again, in some ways a small update, but one with potentially bigger implications



now speaking of dealing with the token scarcity era, TSMC has warned that there's only so much they can do to alleviate the chip shortage that is expected to last all of this [00:07:45] decade. In candid commentary at their annual shareholders meeting on Thursday, CEO CC Wei said, Customer demand is so high and we can only support so much. We are already working very hard. We're doing our best to ensure TSMC does not become a bottleneck

Now TSMC has already [00:08:00] committed to building multiple new fabs in the US as well as more capacity in Taiwan, but construction takes time. Wei discussed a series of roadblocks that have caused the US plans to fall behind schedule, including environmental permitting and a shortage of construction workers TSMC has expanded plans for six new [00:08:15] fabs in Arizona, adding another four facilities to their construction plan.

Still, Wei commented that construction and operational progress in Arizona is proceeding better than originally expected. While Wei didn't forecast how long he expects the overall shortage to last, he did comment, " It will be a long [00:08:30] time before we can meet customer demand." When a shareholder asked Wei if he plans to raise prices given the shortage, he said he would like to do that, but wants to avoid the abrupt price hikes that have been seen in memory chips

TSMC is famously a relationship-based company, with NVIDIA CEO [00:08:45] Jensen Huang commenting that he's never signed a contract despite becoming TSMC's largest customer. Still referencing the memory chip suppliers, Wei said, " I envy their 80% gross margins, but I would never do that."

that." one one interesting little one. CEO Brian Chesky is planning [00:09:00] to launch a new AI lab. Bloomberg said the lab would be focused on user interactionand design, it's not entirely clear what that means. It doesn't sound like the pitch for a new foundation model lab, so there's speculation it will be some kind of agent lab.

Now, Chesky, despite a very prominent role in [00:09:15] Silicon Valley, has so far been mostly in the periphery in the AI boom. He was considered for a role on the OpenAI board and was a key power broker in negotiating Sam Altman's return as CEO afterhis brief ouster back in 2023.

Sources said that Chesky wouldn't be going founder mode for [00:09:30] this venture. Instead, he plans to remain as CEO of Airbnb and hire a new leader to helm the lab

Bloomberg said that the unnamed startup is in the early stages of fundraising, and honestly, for most people, the jokes write themselves. Taylor writes, "Soon you can rent your Airbnb as a data center

But others are [00:09:45] interested to see what comes out of this. Saxum writes, " Instead of the nth lab to focus on coding benchmarks, we might get a model that is actually great at coming up with new UI/UX Huge alpha in just having a model that makes great UI/UX experiences."

Lastly Lastly today, as we head into [00:10:00] the weekend, X is abuzz with rumors of new models coming soon. While some expected GPT 5.6 to arrive this week, it's looking like we'll have to wait a little while longer.

The OpenAI account dropped a new promotional video with thetagline, "Time to fly."

And the OpenAI developers account posted a still [00:10:15] from the video with the caption, "Look closely. There's more in the showcase."

refer-- many thought this was referring to a solid diamond symbol next to the model selector

Perhaps indicating a new ultra-fast speed mode 

Still, 

the OpenAI release that everyone is holding their breath for is of course GPT 5.6 5.6 

On [00:10:30] the Anthropic side of the house, it's all about Mythos. Leo at Synthwaved posted, " Anthropic is gearing up for the public launch of a new version of Mythos, better than Mythos preview. A checkpoint of the model codenamed Oceanus was made available to red teamers yesterday.



I'm told these programs typically begin seven [00:10:45] days after the wider launch.



Lasan on Twitter, meanwhile, dug up another API endpoint serving the model, noting the sky-high pricing of 16 per million input tokens and $80 per million output tokens. That would price the model at around three times the cost of Opus but slightly below the reported [00:11:00] pricing of Mythos Preview, which was 25 per million input and 125 per million output

Whatever the details, it is clear that Mythos is coming soon, with Andrew Curran writing, public release is almost here. I predicted this for the 16th, and I'm feeling pretty good about it."



now usually model coming rumors aren't all that [00:11:15] interesting, but in this case, I think they actually have an interesting story to tell about how the labs see competition. Specifically, we know that some version of Mythos is coming, and that theoretically it's much more powerful than Opus 4.8

and so what's interesting to me is when OpenAI decides to [00:11:30] release their next version of GPT

Right now they're not under a ton of pressure to do so. The release of Opus 4.8 didn't all of a sudden catapult Anthropic the agreed upon leader position once again. Many people still think Phi-5 is better, and it hasn't really shifted the pro [00:11:45] coder momentum around Phi-5 at all.

What that means is that if they release 5.6 right now, it is not a response to 4.8, but a preemption to Mythos Preview

Meaning that they think that 5.6 or whatever the version is called probably won't be able to hang with Mythos when it [00:12:00] comes. because you have to think that if 5.6 is as good as or better than Mythos in the estimation of OpenAI, they would wait until right after Mythos came out to try to clip off the new momentum that Mythos will inevitably give Anthropic So in this case, more than normal, the timing will [00:12:15] tell us a lot about how companies see where the state of the art is relative to one another.



In any case, lots of fun coming up in the early summer of 2026. But that is going to do it for today's slightly extended headlines.

Next up, the main episode [00:12:30] One of the most important AI questions right now isn't who's using ai, it's who's using it? Well,

KPMG and the University of Texas at Austin. Just to analyzed 1.4 million real workplace AI interactions and found [00:12:45] something surprising. The highest impact users aren't better prompt engineers. They treat AI like a reasoning partner.

They frame problems, guide thinking, iterate, and push for better answers. and the good news, these behaviors are teachable at scale.

If you're trying to move from AI [00:13:00] access to real capability, KPMG's research on sophisticated AI collaboration is worth your time. Learn more at kpmg.com/us/slash sophisticated. That's kpmg.com/us/sophisticated. [00:13:15] Here's a harsh truth. Your company is probably spending thousands or millions of dollars on AI tools that are being massively underutilized. Half of companies have AI tools, but only 12% use them for business value. Most employees arestill using ai. To summarize meeting notes, if you're the one [00:13:30] responsible for AI adoption at your company, you need section.

Section is a platform that helps you manage AI transformation across your entire organization.

It coaches, employees on real use cases

tracks who's using AI for business impact and shows you exactly where AI is and isn't creating [00:13:45] value.

The result, You go from rolling out tools to driving measurable AI value. Your employees move from meeting summaries to solving actual business problems, and you can prove the ROI. Stop guessing if your AI investment is working. Check out section@sectionai.com.

That's [00:14:00] S-E-C-T-I-O-N ai com. 

Coding agents are basically solved at this point. They're incredible at writing code. But here's the thing nobody talks about. Coding is maybe a quarter of an engineer's actual day. The rest is [00:14:15] standups. Stakeholder updates, meeting prep, chasing context across six different tools, and it's not just engineers.

Sales spends more time assembling proposals than selling finances, manually chasing subscription requests. Marketing finds out what shipped two weeks after it merged. Zen Coder just launched [00:14:30] Zen Flow work. It takes their orchestration engine, the same one already powering coding agents connects it to your daily tools.

Jira Gmail, Google Docs, linear calendar notion. It runs goal-driven workflows that actually finish

your standup brief is written before you sit down, review cycle. [00:14:45] Coming up, it pulls six months of tickets and writes the Prep Doc.

Now you might be thinking, didn't open Claw try to do this?

It did, but it has come with a whole host of security and functional issues. which can take a huge amount of time to resolve. Zen Coder took a different approach. SOC two. Type two certified. Curated [00:15:00] integrations titer. Security perimeter. Enterprise grade from day one.



Model agnostic and works from Slack or Telegram. Try it at Zen. Flow free. 

This episode of the AI Daily Brief is brought to you by OutSystems, a leading agentic systems platform built for [00:15:15] the enterprise. Organizations all over the world are building, orchestrating, and governing agentic systems on the OutSystems platform and with good reason.

OutSystems' open and unified platform allows teams to architect, deliver, and scale governed agentic systems with [00:15:30] agility. Teams of any size and technical depth can use OutSystems to build, deploy, and manage AI apps and agents quickly and cost effectively without compromising reliability and security.

Without systems, you can rapidly launch ideas from concept to completion. It's the leading agentic systems platform that is [00:15:45] unified, agile, and enterprise-proven, allowing you to accelerate growth, reduce operational friction, and deliver real enterprise impact with AI OutSystems.

Build your agentic future 

[00:16:00] Welcome 

back to the AI Daily Brief

at the close of the headlines today 

I mentioned that the particular release sequence 



of the next upcoming models from Anthropic and would go a long way to telling us what those labs think about where thestate of the art is and implicitly 

where their

[00:16:15] competition with one another lies

And that theme

Of the big labs revealing more about the state of the world as they see it is the subject of our main episode as well This episode is going to be anchored aroundtwo pieces of writing that came out one each from Anthropic and OpenAI The [00:16:30] first from Anthropic is called When AI Builds Itself It is a bit of a meditation I guess you would say around the state of AI development and what comes next The OpenAI document is a little bit more pointed it is a policy document called Democratic Governance of Frontier AI A [00:16:45] Blueprint for a Federal Framework

but actually starts from a similar place of giving us a picture of where OpenAI thinks we are when it comes specifically to AI development

Now to do a little bit of upfront contextualization here's how Ethan Mollick framed the Anthropic piece When AI [00:17:00] Builds Itself He said I think it is really worth reading this piece on RSI at Anthropic

There's a bit of navelgazing some marketing and a lot of very sincere beliefs about what Anthropic thinks is likely in the near future of AI that you probably want to be aware of

The big [00:17:15] theme of the piece is RSI or recursive selfimprovement

And what Anthropic is pointing to at core Is an inflection point moment coming very quickly around how the next best AI gets built

Anthropic writes For most of AI's history humans [00:17:30] drove every step in its development cycle But at Anthropic we are delegating a growing share of AI development to AI systems themselves which is speeding up our work Taken far enough and given enough compute that trend points to an AI system capable of fully autonomously designing and developing its [00:17:45] own successor This is called recursive selfimprovement We're not there yet and recursive selfimprovement is not inevitable but it could come sooner than most institutions are prepared for

Now a lot Now a lot of what you're gonna see on social media from this 

is big surprising numbers

[00:18:00] For example they write Anthropic engineers on average ship eight X as much code per quarter as they did from twenty twenty-one to twenty twenty-five." Another big number is 80 That is the percentage 

of Claude's production code that is authored by Claude itself

They [00:18:15] also note that as they put it the code that Claude writes is good and improving

Good code they say means two things It works and is written in a manner that allowsanother engineer to understand it and build upon it On the first criterion they say the evidence is clear The rate at which Anthropic staff [00:18:30] correct redirect or take over midtask from Claude has been falling steadily for a year including on the most complex and openended tasks this means problems with no clear specification where the engineer isn't sure what the answer looks like

As evidence they point to a chart 



of Claude Code session success rate where [00:18:45] across trivial tasks routine tasks substantial tasks and openended problems

the success rate of all of those has climbed well above 60 

and for the trivial routine and substantial tasks well above 80

From a much lower place less than a year ago

They also note that the [00:19:00] mode of how Claude interacts with the code base is changing Claude they write is getting better at proposing its own experiments



to 

they point to research that was published in April of this year

That was exploring whether a weaker AI 

could manage a stronger AI

The evidence suggests that the human role [00:19:15] is narrowing at each step in the AI development process Once human and AIauthored code quality reach parity humans will stop writing code entirely and shift to only reviewing it But if they can't review code as quickly as Claude can generate it human review will become the bottleneck to AI development Similarly once Claude can [00:19:30] run experiments the question shifts towards which of those experiments is worth running Put simply the doing writing the code running the experiment producing the result now costs almost nothing in human time even if it still has costs in compute An area of human comparative advantage for [00:19:45] now is research taste and judgment including choosing which problems matter which results to trust and when an approach is a dead end

Indeed they continue

The work that is still in human hands choosing which problems to work on is what matters most Without that judgment Claude is a capable assistant but [00:20:00] not as a system that could drive AI progress on its own

They write It's genuinely unclear whether today's training methods and architectures could unlock that capacity But even if we suppose that Claude achieves good research taste a conservative reading of our evidence still implies compounding [00:20:15] acceleration

Now the meat of the piece and the part that's generating the most discussion is the last section on three possible futures po the first possible future which they say they include for completeness but don't believe it's likely is one in which the trend stalls but today's AI capabilities are widely [00:20:30] diffused They write This article features many exponential trajectories but these trajectories may actually turn out to be Scurves We may be approaching the bend in the curve where returns to scale diminish and the line straightens then flattens The judgment that separates a competent researcher from a great one might be a capability [00:20:45] that cannot come from scaling up training inputs like compute and data If so getting past this bottleneck would require a new idea like an architectural approach that supplants the transformer architecture that all current frontier models use Alternatively And this is my editorialization but I 

think we're seeing lots of evidence of [00:21:00] right now The binding constraint to AI progress could be in the supply chain not the model Advancing and diffusing the frontier may require more energy and compute than presently exists

The pace of chip fabrication grid expansion or interconnect bandwidth may be the constraint rather than the intelligence itself

[00:21:15] Now still they say even if model capabilities were frozen at today's level we would expect major changes to occur in the world They point to the example of Mythos Preview finding more than 10,000 high and critical severity software vulnerabilities across many of the world's most important systems

Still like I said [00:21:30] they don't believe that this scenario 

is 

particularly likely Every capability we can measure they write has so far followed the same curve We've not yet seen that curve bend of the three futures we consider this one would give governments and societies the most time to adapt we are more worried they [00:21:45] continue about the next two which would move faster and leave far less room for preparation

Scenario two then is the AI labs continuing to see compounding efficiency gains

In this scenario they say AI development becomes substantially automated but humans continue to set research directions and judge results

[00:22:00] In this scenario one hundredperson companies could do the work of ten thousand or one hundred thousand person organizations

They say this would revolutionize knowledge work and government services but could also be termedTo harmful ends from authoritarian surveillance of whole populations

To influence operations that tailor manipulation to each [00:22:15] individual and run at a scale no human team could match

now interestingly and this is where I wish there was a bit more of a discussion they write that while this is the scenario that is most likely based on the evidence that they've seen they also note speeding up one part of a process often just shifts the bottleneck elsewhere [00:22:30] Overall pace is capped by the parts that haven't sped up

In computing they write this is known as Amdahl's law and the same logic can apply to organization Anthropic has already encountered one signature of Amdahl's law As we've begun to push more code around the organization human code review has become a new bottleneck We've [00:22:45] also encountered this friction outside engineering There has been an explosion of new ideas initiatives tools and simulations as a result of Anthropic employees working with highly capable models far more than we have the capacity to pursue The rate at which organizations can spot and fix these bottlenecks may be [00:23:00] a skill that improves over time and it may become the most important skill for any organization

This 

into a lot of the ideas that I've explored around the infinite backlog 

And why all of a sudden I don't think we're not gonna have jobs

Aaron Levie from Box commented on this part saying that it points to the key [00:23:15] element of the optimistic scenario for 

AI

AI 

AI, he 

writes lowers the barrier dramatically to allowing us to do more As a result of that we have far more ideas than we can pursue and the ones that we want to pursue we're ultimately limited by our ability to go take on the surrounding work to execute those ideas

There's almost no [00:23:30] amount of AI progress that can happen where that goes away AI is going to let us build much more software launch more marketing campaigns research more drugs and so on All of this work even when augmented by agents still ultimately requires people to manage

Now back to Anthropic The third scenario they [00:23:45] point to is the full recursive selfimprovement scenario where AI systems start to build their own successors

Now this scenario is where you see the most hand waviness from Anthropic with them just not really knowing how to guess at all the implications of this

The final section

is the one that has been [00:24:00] jumped all over especially by AI safety advocates They write If it were possible to effectively slow the development of this technology to give ourselves more time to deal with its immense implications we think that would likely be a good thing We believe it would be good for the world to have the option to slow ortemporarily [00:24:15] pause frontier AI development to enable societal structures and alignment research to keep up with the advance of the technology But they write in the same breath If a slowdown simply lets the least cautious actors to catch up technologically it could leave everyone less safe Without a global [00:24:30] coordination mechanism companies and governments will have to make difficult decisions about safety while under competitive and geopolitical pressures

They go through and talk about all that would be required for a slowdown or pause noting that while none of it would be necessarily impossible in principle

pointing to for example the [00:24:45] IntermediateRange Nuclear Forces Treaty

Quote Those regimes took decades to build both the infrastructure and the trust

We don't have that long they write A unilateral pause by one lab by contrast is achievable immediately but accomplishes much less It would change who the frontrunner is but would not create the [00:25:00] wider deliberative process that is currently missing In the coming months we will organize conversations where policymakers researchers civil society and other AI companies can help answer some of the questions this piece raises especially around full recursive selfimprovement and how to create better options for coordination and [00:25:15] deliberation The window to investigate the questions together is here and people outside AI companies should be involved in this deliberation Now the responses to this fully run the gamut



some in the AI safety community are thrilled The AI Safety Memes account sums up

holy blank let's [00:25:30] blanking go

yet others like If Anyone Builds It Everyone Dies coauthor Nate Soares writes

One big quibble is that they aren't thinking big enough

The tone reads like RSI could happen but don't fret too much it'll probably be fine rather than OMFG we're possibly on the brink of AIsthat make smarter [00:25:45] AIs Society needs to act

fi-- others though find that the whole thing 

kind of 

leaves a bad taste in their mouth Sean Ralston writes No way that Anthropic slows or temporarily pauses frontier AI development What an insincere and silly sentiment if they really feel [00:26:00] that way then let them act that way

Corey Quinn writes Asking your competitors to pause development right after you file your S1 is the single most effective moatbuilding exercise I've seen pitched as ethics Do they not realize the quiet period is for them not homework they assign their [00:26:15] competitors

Now there's an even broader critique of Anthropic that recently came out on the AllIn podcast from legendary investor Bill Gurley

who spent 30 days reading everything that Anthropic had ever written

Coming to the conclusion I don't think they're writing software I think they're midwifing a deity here

[00:26:30] I don't know which one I'm more afraid of the regulatory capture or this Dr Frankenstein theory

Jason Calacanis chimed in These are delusions of grandeur Let's call it what it is They believe they're so powerful they can create God Then the God you create is going to be so benevolent and perfect that will give you your [00:26:45] little pellet of resources

ex- now even if you don't think 

that 

that's exactly what's happening 

the fact that that idea is coming up in mainstream conversation will give you some idea 

why the public discourse gets so frustrated with these companies

who talk about the huge implications of their work and yet proceed on with it at an [00:27:00] everincreasing pace

former AI czar David Sacks wrote Signs you might be trying to get your frontier AI lab nationalized You compare it to nukes threaten half of white collar jobs warn recursive selfimprovement could end humanity then race ahead anyway In other words [00:27:15] you want the government to save us from you

Now like I said at the beginning if Anthropic's document is more meditation on thestate of the world OpenAI's policy document about democratic governance is a little bit more precise

And yet [00:27:30] still one part that people noted is that it also mentions RSI as a starting frame of reference In the first paragraph OpenAI writes We also see signs of recursive selfimprovement in today's systems where AI development is itself accelerated by AI We expect this to [00:27:45] increase competitive pressures among developers and nations and create governance challenges that existing institutions are not equipped to address Writes Chubby The vibe has changed Something is happening

Now the,

now the main thrust of OpenAI's paper is that democracies specifically have [00:28:00] a key role to play in solving these very complex and difficult problems

of advanced AI in larger society





they propose three broad policy directions The first they call building a national framework through reverse federalism

Basically arguing that [00:28:15] instead

of the national system preempting state rules

Congress should in fact adopt and scale up the best pieces of state regulations

now the second policy priority is one that actually runs a little bit counter to the executive order. the recent executive order put the locus of the [00:28:30] voluntary testing regime in the NSA whereas OpenAI is arguing that we need to be investing in civilian institutions 

specifically groups

like the CAISI

The Center for AI Standards and Innovation

they also argue contra the EO that at least eventually there should be [00:28:45] a mandatory evaluation process not just a voluntary one

Their last policy priority is quote mobilizing a whole of government resilience strategy

Writing that frontier AI should be treated as a nationalpriority requiring coordination across national security public health cybersecurity [00:29:00] scientific diplomatic and economic agencies as well as with international partners

A pol- AI policy expert Dean Ball writes This seems reasonable Having CASI a civilian agency conduct this testing in primarily nonclassified ways is the way to ensure it does not become a licensing regime The Trump's [00:29:15] EO classification of the process raises the risk that testing morphs into a de facto mandatory permitting and licensing system



now in addition to this document 

which is being treated in some ways as a response 

to the recent executive order even though it feels fairly likely that it was being worked on before that EO [00:29:30] was finalized

Congress is also starting to get a little bit more active on what they think AI regulation should look like On Thursday Republican J Overnolte and Democrat Lori Trahan unveiled their bipartisan AI bill in the House The comprehensive two hundred and sixty-nine-page bill [00:29:45] aims to set up a federal regulatory framework That would override the growing number of state AI laws The bill would require leading AI labs to create and implement plans to deal with catastrophic risks posed by their models Thirdparty auditors would be required to ensure compliance

Now while this seems in line [00:30:00] with the AI law recently passed in Illinois Much of the controversy right now around any AI regulation is about a federal bill preempting state authority Representative Trahan has received pushback from fellow Democrats for supporting this bill particularly in the Northeast New York has already [00:30:15] passed their own laws and her home state of Massachusetts is quickly moving to do the same

With Brad Carson the president of Americans for Responsible Innovation and Former Arizona Democrat arguing that cutting state legislators out of the process would be a quote Generational mistake

Still I would say that ifyou were reading the tea leaves [00:30:30] on average This bill is a little bit less dead on arrival than most at least in terms of the substance the problem is the current timeline Politico reporter Meridith Lee Hill writes Lots of skepticism in House GOP leadership about the Obernolte AI framework and also [00:30:45] getting any AI bill to the floor before midterms Speaker Johnson when asked if he was committed to putting an AI bill on the floor before November said 

Well 

we're going to do it as soon as we're able to build consensus around a package So I mean I would consider it a high priority but I don't know yet on the timing

[00:31:00] In other words I wouldn't hold my breath Anyways friends there is a lot going on

in both the technology and policy of AI but for now that is gonna do it for today's AI Daily Brief Appreciate you listening or watching as always and until next time peace. ​ 

[00:31:15]
