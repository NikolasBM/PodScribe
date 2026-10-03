# The AI Engineering Skills Map for Knowledge Workers — Transcript (2026-08-18)

https://aidailybrief.ai/e/2026-08-18 · Listen: https://pod.link/1680633614

---

Nathaniel Whittemore: ~ Nothing ha- nothing will change, ~[00:00:00] Knowledge work is being totally transformed by agents right now after years of promise, agents are actually here, and they are changing the way that knowledge work gets done broadly speaking, we are increasingly moving from doing our work to managing agents that do our work. But in that transition, what are the key skills that matter?

~Five that stand out to me,~ five that stand out to me are one, AI capability mapping Two, context and harness management. Three, problem and product prototyping. Four, new opportunity identification And five, rapid new skill acquisition

When you combine these with a foundation of domain judgment, you get a type of knowledge worker that is more capable and more powerful than ever before

Nathaniel Whittemore-1: The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI. right, friends, quick announcements before we All right, friends, quick announcements before we dive in

First of all, thank you to today's sponsors, KPMG, Section, Blitzy, and Hyperagent

To get an ad-free version of the [00:01:00] show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts

And to learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai 

Nathaniel Whittemore: In the world of

In the world of AI, ~nothing, ~ nothing is safe as everything gets rebuilt

~The latest reminder of this~

~The latest reminder of this, the latest reminder of this comes fr- the latest reminder of this comes from Cursor~

~The latest reminder of this is-- ~ the latest reminder of this comes from Cursor, who are taking on GitHub with their new repo hosting platform, Origin. The pitch is pretty straightforward. ~Take Git hosting~

Take Git hosting and add better integrations for the coding agents you're already using. Origin allows developers and their agents to access the code base from the same surface they're already working in. That makes it easier to run natural language queries across the code base ~or u- ~or use agents to handle comments and commits without context switching or using connectors ~Still, maybe their biggest, still maybe their big, ~ still still maybe their biggest pitch is around platform stability

GitHub's service has been widely perceived to be degrading over the past year, with ~frequent, uh, with frequent issue-- with~ frequent outages and issues As if on cue, ~right around the time that Or- ~right around the time that Origin was announced, GitHub experienced a six-hour service degradation

Matt Matt Palmer, a dev experience staffer at SpaceX AI, nodded to the issue, commenting, " "We were [00:02:00] We were going to ship this earlier, but GitHub was down."

Vercel CEO Guillermo Vercel CEO Guillermo Rauch piled on,~ on, Vercel CEO Guillermo Rauch piled on saying, piled~ saying, " "You You can now host your repos in Cursor Origin and deploy to Vercel via Cursor Origin, ~which itself is-- ~which is itself hosted on Vercel. And unlike GitHub, it's online

Now Now at this point complaining about GitHub, ~complaining about GitHub~

~is basically just, is basic, ~ is basically just part of the experience of being a developer ~even Or~ Or increasingly, being a not developer who works with code thanks to coding agents. Still, as we've seen so many times in the past

~Major switches like this are extremely costly and extreme... Major switches like this can be ex- ~ major switches like this ask a huge amount of users ~And it's not clear, and it's not clear whether a promise, ~ and and it's not clear whether a promise of better platform stability And AI integration is enough to drive users to switch

GitHub has incredibly strong lock-in given how painful migrating code-based infrastructure is And while there were plenty of people ready to immediately crown ~Origin as a Cur- ~Origin as a GitHub killer Many question the premise

Scott Dolinsky, a content creator focused on dev tools, wrote, " I'm gonna be real. GitHub's outages are super annoying. I just don't see myself moving all my stuff [00:03:00] to Origin. Maybe some of y'all moving your stuff there will take the pressure off GitHub servers for me though

Kush, a software developer at Cursor, used the opportunity to highlight one of the key design decisions with Origin, commenting, " We get it. Moving your code is extremely hard. That's why Origin supports mirroring. Leave your code where it is and let us sync it ~so you can always access, ~so you can always access it performantly through Cursor, agents, pull requests, local, et cetera.

And if you end up liking Origin, you can make the decision to detach from GitHub later on."

This means, in other words, that GitHub ~can remain, ~can remain the developer's system of record theoretically minimizing the risk of breaking production workflows ~Others weren't sure, ~ others others weren't sure that Cursor was really in a position to actually promise better long-term platform stability. Veteran developer Michael Cove wrote, " "I I don't trust them.

Not that Cursor is a bad company. They are not, but that they don't have a proven track record of security ~ in- and infra- and ~and infra opsec because obviously it's a new offering. ~I like Cur- ~ I like Cursor as a coding harness. ~I think they have truly inno- ~I think they have a truly innovative product, and I do trust that my code is not going to be used in training.

But a code repository store? That's a bit of a different concern."

[00:04:00] ~Ultimately where he, ultimately where Cove landed is, ~ ultimately where Cove landed was to say that he would be happy trying out Origin for personal projects, but that he's going to need to see a ~larger, ~longer track record before moving customer projects over

The launch itself is happening as an early preview to existing customers

And some were disappointed about that decision

~Still, most felt that early teething issue-- ~ still most felt that the inevitable early teething issues made that call completely understandable

Still, the promise for this kind of product is obvious as software organizations integrate agents deeper ~into, into, into, into ~into how they work. One developer noted that Origin makes it easier to connect automations to your code base. For example, triggering an agent on a code change or running scheduled tasks from a single platform

~ And this idea of agent native... And this idea of, ~ and this idea of a GitHub that is built from the ground up

Assuming agents are pushing most of the code is what has people interested

~I think if nothing else, the response show... ~ I think if nothing else, the response shows ~that there is d- ~that there is demand for a new agent-first approach to code-based management

~But that does not make, but that does not make Origin's path, ~ but but that does not make Origin's path any easier, as there is also a very high bar for ripping out and replacing core infrastructure like GitHub

~One has to be pretty impressed with the absolute velocity of Cursor shipping ~ One has to be pretty impressed though with the absolute velocity of Cursor shipping, ~especially given that this is now, especially given that this is now hap--~ especially given that this is [00:05:00] happening in the context

of the SpaceX acquisition being complete

~Now it's early days. ~ Now it's early days, but stereotypically

Acquisitions ~tend to significantly slow down, ~tend to significantly slow down the rate of innovation ~from most ~from the acquired companies SpaceX AI seems determined for that not to be the case

And in their announcement blog, ~and in an announcement, and then in their announcement blog~

~Confirming, confirming that, confirming that the acquisition is complete, ~confirming that the acquisition is complete Cursor said that Grok 4.6 was an early look at what the two companies plan to build together

~Perhaps framing what we can expect of the relationship division of labor-- perhaps, ~ perhaps perhaps framing what we can expect from the division of labor within SpaceX AI, Cursor wrote, " SpaceX is building the computing capacity needed to scale intelligence far beyond what exists today. Cursor will be one place where that intelligence becomes useful."

Now, speaking of companies pushing at an incredible rate More details have emerged about Anthropic's exact financial situation ~as a revenue figure of sixty-five billion-- as an official revenue figure of sixty-five-- as an official, as a f- ~as an official run rate figure of sixty-five billion is leaked

~According to sour-- ~ according according to sources who have seen the information, Anthropic ~hit sixty-five-- hit a sixty-five billion-- hit sixty-five billion in revenue run rate by the-- ~hit sixty-five billion in revenue run rate at the end of July. The figures were reportedly shared with investors as part of a regular update.

This represents a sevenfold increase since the beginning of the year ~and a roughly forty percent jump, ~ and a roughly forty percent jump since Anthropic disclosed a [00:06:00] figure of forty-seven billion in May

~Now obviously what makes their growth rate more important-- ~ Now Now obviously what makes their growth rate so important right now ~Are, is the ast- are the astronomical compa- ~ are the astronomical numbers the company is seeking as a valuation for their IPO

Reports from last week suggested that some investors expect the valuation to come in at two trillion, and some quoted an eight hundred percent growth rate as justifying an even larger number

These figures would put the annualized growth rate at five hundred and fifty percent

Still incredibly strong, but slowing compared to the first half of the year

~In fact, when people dig into... In fact, when people~

~In fact, when people marked... In In fact, when people...~~ In fact, when people looked at the trailing four-week growth~

~ It's clear that a huge percent of that-- It's clear that a huge perc- It's clear that~

~It's clear that the biggest spike happened in February-- It's clear that the biggest spike happened in February and March And has meaningfully lev- and has meaningfully leveled off since then. And has meaningfully leveled off since then. And has meaningfully leveled off since then~

~ as an interesting data point, as an interesting data point, this is pretty similar, this is pretty similar to how the-- This is pretty similar to how the-- This is pretty similar to how audience growth for this podcast has grown~

~ Which tends to be ti- which tends to be, which tends to be tied as much to, which tends to be tied as much to, which tends to be tied as much ~~to~

~Uh, let's just kill all that part~

Now believe it or not

~Because these numbers weren't as stratospheric as they-- because these, because the, ~ because the sheer growth rate behind these numbers wasn't as stratospheric as it was earlier in the year, ~there were actually some investors, ~ there were actually some investors who were a little bummed out by this

Author Tae Kim wrote, " Come on people. You can't extrapolate month-over-month growth acceleration to infinity. This is still insane growth

And what's more, ~when you combine this, when you combine this, ~ when you combine this with the 40 billion in annualized revenue run rate that OpenAI CFO Sarah Friar has been reporting

~That means you're talking about-- that, that means you're talking about-- ~ that means that between these two companies, you're talking about $100 billion in revenue run rate

~Up from ~ Up from low single digit billions at this time last year

~Lastly today, lastly today, lastly lastly today we've got-- lastly today~

Lastly today, we got official information about the Stripe Open [00:07:00] Router deal The deal appears to be complete, and Stripe will acquire Open Router for seven billion. That price tag is of course less than the rumored ten billion, but still a huge markup for OpenRouter, who last raised funds at one point three billion in May

~ In fact, some are suggesting that Stripe overpaid~

Indeed, one of the big strands of conversation is the idea that Stripe overpaid. After the news broke, there were infinite variations on this post from Vercel's Max Lader, who wrote, " Big congrats to the OpenRouter folks, but can someone explain how an AI gateway justifies seven billion dollars? Surely Stripe can make their own gateway, and it's not like switching costs for users are particularly high."

~ Fintech engineer Sam, fintech engineer Samir, ~ fintech engineer Samir disagreed. He wrote: ~The reported Stripe Open Rider-- the reported Stripe slash Open-- ~ the reported Stripe Open Router price is inexpensive. Everyone calling it that is anchoring on the wrong number. Seven billion only looks crazy if you judge it against what Open Router is worth on its own, and that's not the number that matters.

What matters is what the deal does to the acquirer's value. ~ Look at what WhatsApp...~ WhatsApp... Look at what Facebook did with WhatsApp or SpaceX with Cursor. Big acquirers pay up, and they pay up relative to their own market cap, not the target. So here's the real test. Ask [00:08:00] yourself if you actually think buying Open Router ~for around s- ~for seven billion improves Stripe's own valuation prospects by more than five percent.

If you believe it does, the price makes total sense. It pays for itself Then it's a competitive tension question. What do you pay to make sure nobody else gets the deal? You get a little more generous than the hurdle. That's how five billion becomes seven billion

And that's why 7 billion makes sense to me

me~ To be honest, I think everyone might be overthinking a little bit. ~ To be To be honest, I think everyone might be overthinking this a little bit

Stripe is and views itself as the ~core plumbing, as the ~core financial plumbing for the internet economy

~Tokens are a, ~a, tokens are a new essential currency in that economy

Recently, people have realized that not all tokens are created equal, ~and they needed to be-- and they need to be able to move-- ~ and they need to be able to easily move between different categories of tokens for different types of use cases, and OpenRouter is the leading company doing that

To get all those customers, all that infrastructure, the brand

And to have it come online and into your system right away rather than later down the line after you've introduced your own version and asked people to switch over

~especially in the c- ~ especially in the context of the speed at which AI is moving

Basically, you just pay the price that it takes to get the deal done, and it turns out that was seven billion

A great outcome for the [00:09:00] OpenRouter team, of course, but my guess is that this pays off for Stripe in big ways as well. For now, though, that's gonna do it for the AI Daily Brief headlines edition. Next up, the main episode ~ ~

KPMG Aug_EDIT: ~We've moved from ranking pages~

Nathaniel Whittemore: A new study from KPMG and the University of Texas A new study from KPMG and the University of Texas at Austin found that when people work with AI, similar skills don't guarantee similar outcomes. Researchers studied more than five hundred early career professionals and found that the best performers consistently amplified the value of AI by guiding, evaluating, and refining its outputs.

These top performers, called AI amplifiers, weren't defined by what they knew alone, but by how they worked with AI. Learn more about what separates AI amplifiers from everyone else at kpmg.com/us/aiamplifiers. 

Here's a harsh truth. Your company is probably spending thousands or millions of dollars on AI tools that are being massively underutilized. Half of companies have AI tools, ~but only 12% of them use, ~but only 12% use them for business value. Most [00:10:00] employees are~ are still using ai, ~still using ai. To summarize meeting notes, if you're the one responsible for AI adoption at your company, you need section.

Nathaniel Whittemore: Section is a platform that helps you manage AI transformation across your entire organization.

It coaches, employees on real use cases

tracks who's using AI for business impact and shows you exactly where AI is and isn't creating value.

The result, ~you go from rolling out tools to driving measurable. ~You go from rolling out tools to driving measurable AI value. Your employees move from meeting summaries to solving actual business problems, and you can prove the ROI. Stop guessing if your AI investment is working. Check out section@sectionai.com.

That's S-E-C-T-I-O-N ai com. 

Blitzy deeply understands your code base before it writes code. Here's the first place that pays off: security in the age of AI

blitzy July_EDIT: Vulnerabilities don't live in isolation. They live buried inside millions of lines of interconnected code, where patching one thing quietly breaks three others. That's why surface-level scans fail Blitzy starts from its knowledge graph of your entire application, identifies and surfaces CVEs across the full estate, proactively [00:11:00] recommends patches, and can execute the PR Each fix is grounded in how your systems connect and validate so nothing new breaks.

And the knowledge graph dynamically updates, keeping you ahead of an ever-accelerating threat landscape

One Blitzy customer resolved 21 active CVEs across six core microservices in four days. Zero compile errors, every validation scan clean, months of planned work fixed in less than a week

Security remediation grounded in real architectural context at the speed of compute. Harden your code base at blitzy.com. That's B-L-I-T-Z-Y.com



Nathaniel Whittemore: This episode of the AI Daily Brief is brought to you by Hyperagent where you run fleets of agents your team can manage together New users get 1000 in inference Forget local agents and chat workflows waiting on your laptop to be prompted Hyperagent deploys alwayson agents in the cloud doing real work across the tools your team already uses Marketing's agent turns competitor moves into landing pages ~Sales agent enriches ~sales agent enriches leads drafts emails and updates the CRM ops agent chases the paperwork and tracks the budget Every agent has access to shared context and follows your [00:12:00] rules about scope and approvals ~It's time you add agents that felt ~ It's time you add agents that feel like teammates Hire yours at Hyperagent built by the team at Airtable Claim your 1000 in inference at hyperagent.com/aidailybrief. 

Welcome back to the AI Daily Brief. Welcome back to the AI Daily Brief. Today I've got a fun one for you It's very clear that the skills of knowledge work are changing and changing fast. Not that everything's upended. ~There-- Not that everything's upended, as you'll s- not that everything's upended. But all of a sudden, ~but all of a sudden, knowledge workers have ~this totally, have these totally new ~these totally new capabilities ~brought on by new, ~brought on by new tools and new ways of working And of course, alongside that comes with the challenge of figuring out how to harness all that power

~Today we're going to go through-- Today, ~ today we're going to go through my AI engineering skills map for knowledge workers

~It's a five ski-- ~It's It's a list of five skills ~that I think, that I think broadly, ~ that I think broadly are now relevant ~for, ~for knowledge workers of all stripes who want to work in this new paradigm. And And the inspiration for this came from Coursera founder Andrew Ng's ~AI engineering, ~ AI engineering skills map, ~a post that he dropped, a post that he dropped on X, a post that he dropped on X, ~ a post that he dropped on X last week

~Now, ~ now in his post, he is talking about AI [00:13:00] engineering very specifically in the context of software engineering

Andrew writes, " " AI allows us to build software very differently today than in 2022, and everyone with the skills to take advantage of this shift has numerous exciting project and job opportunities. But with the noisy, hype-filled information environment around AI, what are the most valuable skills for you to learn?

I have been working with my team to synthesize a map of AI engineering skills in order to help developers prioritize what to learn ~and employers hire skilled-- and help d- ~and help employers hire skilled developers."

For Andrew, the four most important AI engineering skills are one, building and deploying AI applications. Two, software engineering fundamentals. Three, using coding agents. ~And four, shaking the build. ~And And four, shaping the build

~I don't wanna spend too much time on these. ~ I don't~ I don't wanna spend too much time on these 'cause we are going... ~I don't wanna spend too much time on these

Before getting to our interpolation But to give you a quick flavor

On something like software engineering fundamentals He's basically saying that even if you are using coding agents, as is the third skill You need to deeply understand how software works, i.e., understanding trade-offs between cost, scalability,~ reliably, ~reliability, speed, and more

more~ Even if you are not writing the code, ~ even if you are [00:14:00] not writing the code directly This is going to lead, as he puts it, to better decisions in choosing your software stack, designing systems architecture, designing your data store, testing, and so on

So foundations and fundamentals still matter. However, there are obviously new skills as well. ~As Andrew put-- as Andrew points out, as Andrew points out, as Andrew points out, honestly, as Andrew points out~

~ ~ As Andrew points out fairly uncontroversially at this point, ~using, ~ using agentic coding effectively is now a key skill for every developer

And And it is indeed a skill. It involves understanding limitations, how how to steer them, how much to intervene, how much to leave them alone

Et cetera cetera~ So these are the types of, ~so these are the types of new skills for AI engineering. But what's interesting is that AI engineering is infiltrating the rest of knowledge work as well

And here admittedly, we're using AI engineering in sort of two ways

~ We're using it in the sense-- We're using, we're using it in the m- ~we're using it in the metaphorical sense ~ of engineering AI and using AI--~ of engineering AI to use AI well, but also the literal sense ~of engineering-style skills and dis- of engineering-style skills, of engi- ~ of engineering-style skills coming to ~non-en-~ non-software engineering fields

As you'll see

As many of you have experienced

Even without pretending that somehow knowledge workers outside of software engineering are all of a sudden going to be software engineers, [00:15:00] ~the capability~

The capability that knowledge workers have now to build and use code to solve problems and create opportunities is creating a dramatic shift in how we all work

~Um, if you could use this view while I was just saying that line, uh, because this line reinforces it~

~Still, while I'm going to get into the five s- ~ still, while I'm going to get into these five new skills of AI engineering for knowledge workers, ~I do, ~ I do also wanna suggest that a foundation is and remains domain judgment

~And the analogy here is certainly, ~and the analogy here is certainly the software fundamentals from Andrew's post It's things like the ability to define quality, recognize trade-offs, understand consequences, take responsibility for decisions

It is the judgment that comes with experience in that field ~You wouldn't expect someone who's never done any mark just because-- In other words, just because ChatGPT can make... In other words, just because ChatGPT can make an Instagram ad ~ In other In other words, just because ChatGPT can write all the copy and make all the ad assets, ~you wouldn't expect someone with no experience in mar-- you wouldn't expect someone with no experience in-- ~ you wouldn't expect someone with no experience in marketing ~To be able to really plan and, to be able to really plan and execute a, ~ to be able to plan and execute a marketing campaign really well because they lack that domain judgment

~And I think it's important to-- And I think it's also important-- ~ And I think it's important to note in the context of your specific work that domain judgment is not just general. It's~ It's not for exa-- It's not to continue that analogy. It's not to continue that partic- ~ It's not to continue that example marketing in general that matters.

It is marketing in the context of your [00:16:00] organization

In every field ~There are going to be, ~ there are going to be things

~that don't or ha- that haven't, that haven't or, ~that haven't or even can't get encoded into AI training data And that ~shape the difference between something that's okay and shape the difference between work that is okay and ~shape the difference between work that is passable, good, or great

Now, Now, one of the interesting challenges that the continued need for domain judgment

Creates

is the apprenticeship question of how young workers can develop that domain judgment

if more experienced workers with the domain judgment are simply using the tools to do ~what the younger workers, ~ what the younger workers might previously have done

~At the end of the ep- at the end of the episode, ~ at the at the end of the episode, I'll get into a new organizational structure, which I think might be an interesting answer to that. But I do also wanna point out that domain judgment ~isn't just, isn't exclusively, isn't exclusively~

~Isn't exclusively, ~doesn't exclusively come from 10 or 20 years of working in a particular firm or field

There are lots of different types of judgment that matter. Personal judgment, standards, pattern recognition, and trade-off awareness that you've already internalized. Borrowed judgment, expertise supplied through collaboration, review, explanation, and shared decision-making, ~i.e., younger, ~i.e., younger workers can work with older workers.

~And it-- ~and of course, there's embedded judgment, which is expertise that's captured in [00:17:00] examples, rubrics, policies, evaluations, the sort of context that you feed AI

~But wherever the judgment, ~ but but wherever the domain judgment comes from, it is the foundation for the rest of it, it,~ and does not sudden, ~and does not suddenly leave when you introduce AI

~But let's talk about-- But let's, but let's move on to the five-- But let's talk-- ~ But let's move on to these~ five, to these~ five skills

~These are not, these are not, these are not somehow completely dis- these are not s- ~these are not somehow completely disconnected from one another. Indeed each~ c- in fact, each~ capability strengthens the next

And I would argue that it starts with AI capability mapping One term that you'll frequently hear popularized by people ~like, popularized by people like, ~like Professor Ethan Mollick, is the idea of AI having a jagged frontier. What he and others mean by that

~Is that while someti-- ~ is that while AI can absolutely blow you away in one minute, ~it can do something, ~ it can make a mistake the next minute that you wouldn't expect the least capable intern in the organization to make

~Capability mapping is in part understanding that, that is a-- capability mapping is in part, ~ capability mapping is in part ~understanding that. Understand, understand, ~ understanding that jaggedness

~It's about being able to understand-- It's about, ~it's about being able to know ~what AI is, ~ what AI is natively good at and what it isn't, ~where you, where, ~ where in the context of where it isn't great yet, how you can help it. It's It's the ability to match different tasks with different approaches to AI

~In other words, understanding un-- ~un-- in other words, understanding the difference between ~an as- ~ an assisted approach, a workflow [00:18:00] automation, ~or a truly agent, ~ or a truly agentic solution. Increasingly, capability mapping is also about understanding ~which different models and efforts level-- ~ which different models and effort levels ~are sufficient for different, ~ are sufficient for different types of tasks

And capability mapping is about understanding how much human oversight is going to be needed.

And And unfortunately, and this will be a recurring theme throughout this, ~this is not something, this is not something that, this is not something exactly, ~ this is not something that in general someone can just hand you to learn. ~You kinda have to go, ~ you kinda have to learn this by doing it yourself through trial and error.

~Which isn't to say, which isn't to say that, ~ which isn't to say that standards and norms and conventional wisdom can't be helpful guides on this process But different people's experience with AI is going to be different. ~One person may find that on out-- ~ one person may find that on every different type of writing task they've had, Fable is by far the better writer.

But for a particular type of technical writing, that is the writing that matters for you, ~Five, Six Soul is the only... ~ Five, Six Soul blows it out of the water. Capability mapping is a combination then ~of what, ~ of broadly what we all know and specifically ~what matters for your particular, ~ what matters for your particular function or role

The The next skill after capability mapping is is context and harness management. Basically how you set the AI up for success

We've [00:19:00] talked a lot over the last calendar year about ~both, about~ context engineering ~and harnet- and harnet- and increasing- ~and more recently harness engineering

Context engineering or context management ~ is all about making sure the AI has access to the information it's going to nee-- ~ is all about making sure the AI has access to the information it needs Going back to that marketing example, there is likely to be a wild difference in how the AI performs for you

If you provide it with past campaign performance, analytics, subjective reviews, customer feedback, as opposed to just giving it a prompt ~and hoping that, ~and hoping that it comes up with something great

~Harness management builds on con- ~harness harness management builds on context

To give us more ways to help the AI succeed. ~If you think about the harness, if you think about the harness~

~ ~You can think about the harness as everything~ that surrounds, as everything~ that surrounds the model ~that isn't just, ~ that isn't just the context, meaning instructions documents, tool access, permissions

memory and more Now Now in both of these cases, ~some amount of this is going to be, ~some amount of this is going to be governed by your organization

But But a lot of it is going to be customized by each individual worker

~And how well they've set up their envi- ~ and how well they've set up ~their particular, ~their ~particular instance, their~ particular instance of a model to be successful or not

~Here we get to, here we, here we also see another as- ~ Here Here we also start to understand that these skills are extremely dynamic Best practices in context and [00:20:00] harness management today ~will almost inevitably change, ~ will almost inevitably have changed six months from now. ~There might still be, there might still be strong, ~ there there might still be strong core ideas

But different models, different harness software are going to change the best practices for what you have to do

to maximize the AI's environment

The next The next skill I'm calling problem and product prototyping

~And this is my, ~ and and this is my sort of catch-all For the new capability that knowledge workers have ~to use, to use building, ~ to use building software and pushing code

~to do parts of their job that didn't, that to do parts of their job~

that used to work very differently

And And I wanna be clear here, and this is why I use the term prototyping, although it's not perfectly accurate, that what I am not talking about here is all of a sudden marketers being the software engineers

But it turns out that when everyone can use code

in a much more robust way, ~a lot of work can be done, a lot of work, a lot of previous work, ~ a lot of previous work can be done much more effectively Maybe the most obvious example that is going to resonate across ~a broad s- a broad cross- ~a broad cross-section of you listeners is anything having to do with analytics or data

~ Continuing our anal-~ continuing our analogy of the marketer, ~let's assume that there's some regular reporting-- ~ Let's assume that there's some regular reporting interval for figuring out how well a campaign is doing

Previously

[00:21:00] Getting all that information ready was probably a ton of work ~going to each of the different, ~going to each of the different platforms' analytics suites, downloading what you had access to, taking it ~and moving it into another system like taking ~and moving it into another system like Google Sheets or Excel, running analysis on it, taking that analysis from one channel and trying to combine it with other channels And then once you actually came to some conclusions Turning that all into presentations that could help share it with other parts of the organization

That changes fairly dramatically in a world where marketers can push code All of a sudden They can build not only an internal dashboard, but the engine underneath it that is automatically ingesting and processing that information

in a totally different way. Instead of having to manually go and get all that data, ~ they can in many-- they can, they can connect that and ~they can connect that marketing analytics engine ~the APIs, to~ to the APIs of those services and ingest that automatically

The first layer of analysis can come not from them ~crunching, ~crunching through Excel, ~but by the AI surfacing, ~ but but by the AI surfacing interesting insights

Of course, where domain judgment comes in ~ is that there is on top of--~ is that there is an additional translation layer that's still required ~ To turn that into real insight,~ to turn that [00:22:00] into real actionable insight ~But all of a sudden, ~ but all of a sudden, a huge amount of time is freed up

~to ask those sorts of, to ask tho- to,~ to ask those sort of judgment style questions and do that sort of judgment style work

I I truly do believe, ~I truly do believe That even though, ~that even though knowledge workers are not and should not think of themselves as ~turning into pure, ~turning into full product managers and software engineers

Being able to build things, to solve problems and do parts of our jobs is perhaps the most significant shift in how knowledge work will happen that we've ever experienced

for those of you who have been on the fence, it is worth taking the time ~to go messily clunk your way, to go messily clunk your way through, ~to go messily clunk your way through Codex and Claude Code

~To start figuring out how, to start figuring out~

Which parts of your work could be transformed if you were building things that did the work instead of doing it yourself?

~Skill four ~ four Skill four is sort of the matched pair and advanced level of skill three three If If skill three is all about using the new capability to build software to solve problems of the existing way you work, skill four is about identifying the new opportunities

that building software and pushing code open up in what your job actually consists [00:23:00] of

Instead of asking how can AI help with different parts of my job, it's about asking what can we do now that was previously impossible or uneconomic?

~In other places I've refer-- ~refer-- In other places I've referred to the idea of the infinite backlog. The idea that every knowledge worker has this endless list of things that they would do ~if time and resources were no limit. ~ If time and resources were no limit Agents bring forward that infinite backlog and make~ a huge porti- and make~ a much bigger portion of it ~actually, ~actually viable

~And while the, and while I don't think that there's any, ~ and and while I don't think that there's any super general shorthand for how to identify the new opportunities ~of, of, of things that were or thought, of things that you, of things that were previously impossible or unecon- or things that, of things that were previously un- ~of things that were previously impossible that you should be doing now

~One small sh- one small t- one small twi- ~ one small tip that I have seen help

~is imagine, ~is to imagine

~that your organization gave you access to, ~ that your organization gave you access to a team of software engineers ~and said, "You can do whatever you want with these guy," ~ and said, "You can do whatever you want with these folks."

What would you do then?

Maybe the first layer would be things like we saw in number three, where you take a lot of the work that used to be manual and turn it into actual automated or agentic systems

~But likely before long you come up, but, but before long you might start to see other ideas ~ But before long, you might start to run into totally net new ideas

~I think we're gonna start to see some-- ~some-- I think we're gonna start to see some weird and very cool things ~like marketing teams, ~like marketing teams from small [00:24:00] companies ~building and releasing games, building and releasing games as part of their... Building and releasing games or ~building and releasing games as part of their top of funnel

~And honestly, if you've heard me-- ~ And And honestly, if you've spent any time around this show, you'll know that I think this skill ~is where some of the most exciting, is where some of the most exciting, ~ is where some of the most exciting outcomes of AI are~ going to, are~ going to come from Skill five is a meta skill that cuts across all of these things, which is the ability to rapidly acquire new skills

The speed at which AI changes the opportunity set

~is incredibly, ~ is incredibly quick ~And while, and while there is organizational and institutional level, ~ and and while there is organizational and institutional inertia that will limit

~How many new s-, ~ how fast new systems and processes can be integrated into the way that the organization works as a whole

There is far less inertia ~in how, in how quickly you are able to, ~ in in how quickly you are able to integrate new ways in how you accomplish what you do. And in fact, your ability and your team's ability to integrate those new skills and new capabilities more rapidly probably has net positive impacts on how fast your organization can move as well

New skill acquisition is a combination of being able to recognize ~what, uh,~ what new or adjacent skills and capabilities have suddenly become valuable. ~It's the ability to, it's the ability, ~ it's it's the ability to create the right type of space to actually go experiment and [00:25:00] learn by doing and applying it ~to real, to the, to re- ~to real world environments

~And it's about the ability to as- and it's about the ability to assess, ~ and and it's about the ability to assess the output ~and understand whether it's actually worth integrating into, and whether it's act- ~ and understand whether it's actually worth integrating into how you work

~ It It is both mindset and practice. ~It is both mindset and discipline

~Skill acquisition become, skill acquisition becomes, skill ac- skill acquisition becomes a cont- ~ skill skill acquisition becomes not the work of semi-regular ~upskilling wor- ~upskilling seminars

~but a continuous process that happens, ~ but a but a continuous process that happens in an ongoing way

~So those are, so those are my fi- so those are my five AI engineering skills. So that is my AI-- ~AI-- So those are my five AI engineering skills for knowledge workers. ~Again, AI, ~ again, again, to recap, it's AI capability mapping, context and harness management, problem and product prototyping, new opportunity identification, ~and new skill, and new skill, ~ and rapid new skill acquisition

I'm I'm super interested to release this show and see which~ of these~

~Which~ of these resonate the most with you? Which ones~ you're struggling, and which ones ~you're struggling with? Obviously, I'm thinking a lot these days about how to support all of this So your commentary and ideas are very welcome. Lastly, one flag for something that I'm thinking about ~for a future expl- ~for a future podcast exploration ~I think this idea I think this idea, I think this idea of what happens to the next generation~

I think this question of what happens to the next generation of domain judgment if young workers ~aren't being the, ~aren't being given the chance to develop that judgment

because more experienced workers are simply using AI to do what those younger workers might [00:26:00] have previously done, is a really fascinating one

~And one of the answers, and one of the answers that I think, and one of the answers that I think, ~ and and one of the answers that I think is interesting to explore ~is a shift in thinking about AI, ~is a shift in thinking about AI as single player to AI as multiplayer, ~ with the core unit of AI being,~ with the core unit of AI

Moving outside the individual and to the small team

~I think that that, ~ I I think that that could create some really interesting new opportunities, ~but that is, ~ but but that is a subject for a future show ~For now, that's gonna do it for today's AI-- ~ For For now, that's gonna do it for today's AI Daily Brief. Appreciate you listening or watching, as always. And until next time, peace 

​ 

Nathaniel Whittemore's audio recording: ~Quick note before we get into today. A ~
