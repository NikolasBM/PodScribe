# ChatGPT Just Became a Work Agent — Transcript (2026-07-10)

https://aidailybrief.ai/e/2026-07-10 · Listen: https://pod.link/1680633614

<!-- metadata -->
Format: news-analysis · Level: 2 · Length: ~00:25:00
Host: Nathaniel Whittemore
Categories: models, agents, coding, infrastructure
Featured: Meta, OpenAI, ChatGPT, GPT-5.6, agent harness, OpenAI Codex, Muse Spark, Claude Fable, Meta Muse
Also mentioned: GPT-5.5, Claude Opus, Cursor, Artificial Analysis, Claude Cowork, Grok, open-weight models, MCP
<!-- /metadata -->

---

260710 in_EDIT: [00:00:00] Today on the Today on the AI Daily Brief, more new models plus a big harness update from OpenAI

And before that in the headlines, Cursor also appears to be developing a harness to go after the larger knowledge work sector. The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI.

Nathaniel Whittemore: back to the AI Daily Brief headlines edition, all the daily AI news you need in around five minutes Quite 

260710 hed_EDIT: appropriately, given that our main episode is about a big harness update, we kick off our headlines with news that Cursor is planning a general purpose agent to compete with Claude Cowork. The Information reports that work began on the project in April, shortly after Cursor signed their deal with SpaceX.

The agent is expected to use Grok 4.5 and will be Cursor's first project aimed at anyone other than professional coders. Called Sand, it's designed to function as a personal assistant performing standard office tasks like dealing with email or working with spreadsheets

It sounds like it could also eventually become a unified platform with the information's reporting suggesting that the agent will also be [00:01:00] functional at AI coding. Sources said the platform was rolled out internally in June. However, it's still unclear whether it will get the green light for a public release or when that would happen

Certainly the product suggests that Cursor, now a part of SpaceX AI, is looking to grow beyond their traditional user base of software engineers

This makes sense, as we'll see a huge theme of all of the announcements today with OpenAI are all about taking what has been working in coding and bringing it to a broader set of knowledge work

Now Now speaking of what's working with coding and what's not workingOpenAI has captured the zeitgeist and declared that the leading coding benchmark is bunk. In a new report, OpenAI audited Suitebench Pro and found the benchmark to be sorely lacking. In their testing, they found that 30% of the tasks on the benchmark were broken and are now formally retracting their support of the benchmark.

Many of the issues stem from some of the tasks being public, which can distort results. by having those specific problems be included in training data. Others had hidden requirements, contradictory instructions, overly strict tests, or incomplete grading criteria.

Their conclusion was that SWE-bench Pro, quote, no longer reliably [00:02:00] measures frontier coding capability

and to be clear, the shift away from Swebench was already well underway. Cursor has been using their own proprietary benchmark for months, while Cognition and Databricks also launched their own benchmarks this week

I think I think we're officially at the point Where there's gonna be lots of introduction of new benchmarks. companies are going to present all of them, including I guarantee they will still present SuiteBench Pro

and mostly just wait for people to have the vibes that confirm whether the benchmarks are bunk or not

notfor... Now Now staying on OpenAI for a minute, but going to a very different area, the company has published a new statement that explains their approach to government and military partnerships.

Announcing their new national security principles

OpenAI writes, "We believe democratic societies should be able to use AI to protect people, defend critical infrastructure, deliver public services, and respond to emerging threats. But increasingly capable AI systems must be deployed in ways that reinforce democratic accountability, meaningful human judgment, and the rule of law, and strengthen democratic institutions rather than concentrate power."

Distilling the principles into a few key points OpenAI explicitly stated that they will not support the use of their technology for [00:03:00] mass domestic surveillance, high-stakes decisions, including decisions over the use of force without appropriate human judgment and accountability, or uses that evade legal obligations, oversight, and accountability.

Now, these you might recognize are essentially the same as Anthropic's red lines

And given that that created such chaos with the government, it's not clear what the goal of this document is supposed to be

But I guess at least we have a clear articulation of what they stand for

and something to build from in their conversations with the government.

government. speaking speaking of the overlap between the government and AI, Anthropic has appointed former Fed Chair Ben Bernanke to the board of their long-term benefit trust

Bernanke, of course, was appointed Fed chair by the W. Bush administration in 2006 and served until 2014, presiding over the events that led up to and followed the global financial crisis

he is one of the more controversial Fed chairs in recent history, with views on him differing depending on whether you think the bank bailouts in 2008 saved the world from a depression or you view them as the original sin that accelerated the wealth divide in the United States

when Claude was asked to provide an objective viewpoint on Bernanke, it responded that he's generally well-regarded but has critics on both [00:04:00] the left and the right who view him as, quote, " Emblematic of an unaccountable technocracy protecting elite interests."

So what then is Anthropic's long-term benefit trust? In their own words, they write, "Anthropic is a public benefit corporation, meaning the company was created to balance commercial success with generating social and public good. The benefit trust exists to help the company responsibly maintain that balance over the long term, providing a check on how Anthropic develops and deploys Essentially, this is an independent oversight and advisory board that sits on top of Anthropic's normal board of directors. Importantly, the benefit trust has the power to elect or remove one member of the corporate board, which escalates to two and then three according to time and funding-based milestones By next year, they will have majority control over the corporate board, albeit with a shareholder override that requires a supermajority vote against the actions of the trust.

Unlike normal corporate boards, no one on the board of the trust is allowed to be a shareholder

there is a lot of discourse on this one, especially from folks on FinTwit. but I think Tom Bruni got at the key question that many of us are asking: Will he bring token prices to [00:05:00] zero like he did with rates?

rates? moving over Moving over to the chips world, Meta is heading north for their next big data center project with a $10 billion facility planned in Canada. Meta announced the groundbreaking for the Alberta site on Wednesday, with plans to build a total of one gigawatt of capacity over the coming years

Interestingly, community pledges were front and center in the announcement, with Meta planning to contribute sixty million in Canadian dollars to local infrastructure upgrades including roads and water On electricity, Meta pledged to pay full infrastructure costs and officials expect local rates to actually decrease as a result of the project.

They will also provide direct funding to local nonprofits. In addition, they plan to hire three thousand construction workers at the peak of the build and support three hundred ongoing operational jobs

to,now as I continue to scream from my bully pulpit, these sort of community contributions can be on the one hand incredibly valuable to those communities and are a rounding error in these data center budgets, making it one of the easiest potential alignments between hyperscalers and the communities they operate in than they could possibly imagine if they only take the time to actually do it.

So it's great to see [00:06:00] Meta actually going down that path. Now, the other big implication here is, of course, that Meta's big AI build-out is not slowing down. When news broke last month that Meta was planning to sell extra capacity, many drew the implication that they'd wind back on CapEx. Adding another gigawatt suggests Meta's plans are still ticking along at a rapid pace, and I think when you get to the main episode, you'll kind of start to understand a bit more why, 

Meanwhile, Meta's in-house chip program is back from the dead and set to enter production in the coming months. According to an internal memo cited by Reuters, Meta is on track to begin producing the first chips in September. The report states that at least one chip design sailed through the testing phase in just six weeks.

Meta is working with Broadcom on design and will contract with TSMC for processors and Samsung for memory

Most semiconductor analysts assume this generation of chips would be shelved just like all the others. Meta has been working on their own advanced AI chip since at least twenty twenty-two, but each iteration hit roadblocks and was never put into full-scale production. This generation had a similar vibe up until now.

It was first announced in March, just one month after Meta had canceled the previous generation With [00:07:00] that announcement describing four configurations across the chip family tuned for different inference and training workloads. Then last month, it was reported that Meta had asked Samsung to temporarily pause development on their custom chipset, and many assumed that was the beginning of the end To the contrary, it now seems that Meta has a finalized design and just needs to wait for some foundry time with their chip-making partners.

The chips are expected to be installed in Meta's data centers and allow them to cut down on their spending with NVIDIA and AMD. Meta also plans to design a new chip every six months beginning next year, which would be significantly faster than the standard industry cadence

the memo viewed by Reuters also reaffirms Meta's plan to scale compute. The company said that they plan to deploy seven gigawatts of capacity this year and double that pace in 2027

So yeah, it doesn't seem like we're getting a cutback from Meta anytime soon But again, for why, I think we need to end the headlines and move on to the main episode 

260710 main_EDIT: Welcome back to Welcome back to the AI Daily Brief This week, obviously, the entire story has been new models. I mean, it has just been a barrage. We've got [00:08:00] GPT 5.6, the entire family

which are finally officially out, available for everyone

with all the related public release information. but then also the fairly unexpected Grok at least unexpected in terms of its apparent performance, as well as a new one, Muse Spark 1.1 out of left field that actually has people talking about Meta again And yet, in a year where people have come to understand just how significant not only the model is, but the harness in which it operates, It is so appropriate that we are also closing out the week With in some ways the biggest news being big changes to the OpenAI harness through which you are going to use the model

OpenAI has released ChatGPT Work. And we are gonna talk about what that means in first impressions. But first, let's finally catch up on the now fully released GPT-5.6 model family

Now, this is the first time that OpenAI has split their model family into a set of classes. in addition to the flagship model Sol, GPT-5.6 also has a mid-size version in Terra and a small cost-efficient version in [00:09:00] Luna

Now we have started to talk about these models throughout the week

As OpenAI gave clearance to people to start talking about their early adopter impressions of it start-- But we just now, with the official announcements yesterday, got the benchmarks

and interestingly, the benchmark story as it's presented is very different than the way that OpenAI has done this in the past

Sam Altman tweeted, "Obviously the best model we've ever produced, but also one of the best blog posts we've ever produced." And part of that is that instead of just a simple, easy table of a bunch of numbers for their benchmarks

OpenAI is now highly focused on charts that show performance per cost For example, on the agent's last exam test

which is long horizon agentic workflows across a number of professional domains The chart is actually presented in three ways, the score on the Y-axis and some other variable on the X-axis, with the premier chart being the API cost

They show the comparison not only to GPT 5.5 Claude Opus 48 and Claude Fable 5

In terms of the score, but also in terms of the cost. With the strong emphasis being that not only do the [00:10:00] GPT-5 six series of models perform better, but they do so at a much reduced cost. Now, you can also vary that chart to be organized by latency or by output tokens used, which is, of course, another measure of efficiency

the-- You see a similar chart presented this way for the artificial analysis coding agent index. Again, cost, latency, and output tokens

And this is pretty much now the standard for how they present the benchmarks

Sam Altman Sam Altman reinforced this focus with one of his announcement tweets where he said, " We have heard enterprises on their concerns about AI costs, and 5.6 SOL is a huge step forward for dollars per task, as are Terra and Luna

Now, rather than trying to explain all of these different charts on a podcast that many if not most of you still consume via audio, the big overview is basically that 5.6 Sol on max settings benchmarks ahead of Opus 4-8, near or above Fable 5, and most importantly, at a significantly lower cost to each

For the artificial analysis index run, GPT-5.6 was a close second to Fable 5, falling [00:11:00] short by a single point, but it completed the run at a third of the cost of Fable and was even 40% cheaper than Opus 4.8

Meanwhile, on the coding agent index, GPT 5.6 is the new state-of-the-art, beating Fable 5 by three points. In fact, at least on that artificial analysis benchmark, the mid-size Terra variant performed at the same level as Fable and would, of course, be significantly cheaper as a daily driver coding model If those benchmark results translate to real-world experience

now bringing it back to the model thathad so much attention in the Fable 5 shutout period, Simon Smith pointed out that 5.6 Luna actually matches GLM 5.2 on the artificial analysis intelligence index, and comes in at 43% cheaper

Getting at the idea that we were talking about in our episode a couple of days ago

of the new market opportunity for more efficient Western models. Simon continued, " I'm glad open-weights models exist because they push frontier labs to innovate and release, but I don't think enterprises shift to open-weight models strictly for cost reasons. I think frontier labs will optimize for both [00:12:00] intelligence and efficiency, offer models at multiple performance and price points, and train their best models to know how and when to use their cheaper models to maximize impact for cost.

And that will make for a compelling value proposition that negates the need to shift to open-weight models strictly to save money."

Now, as I mentioned, since early testers were allowed to break their silence from the beginning of the week, we've been able to cover a number of first impressions over the last couple of shows. and to recap, the big takeaway is that we now have two frontier models that perform very differently.

Broadly speaking, the early consensus is that Fable 5 is the big model for massive long-running tasks, especially ones where there can be a lot of autonomy

While GPT 5.6 Sol is a huge upgrade not only as a daily driver, but for large tasks where you wanna be more involved in the intermediate decisions

reinforcing some of the early takes, every CEO Dan Shipper wrote, " 5.6 is powerful, fast, half the price of Fable, and my default for almost everything." He noted that 5.6 is not as good as Fable for coding, But also pointed out that Every's [00:13:00] benchmark for coding is a massive long-running code refactoring task, which Fable is naturally more suited to than 5.6

Fascinatingly, on writing, he said that 5.6 is the model that Every has liked more than anything else, arguing that it's clearer and more concise than Anthropic models And throughout his review, Schipper continuously comments on the speed Fable is a big, slow, incredibly powerful model, while GPT 5.6 is very fast, making it more of an active collaborator Rather than a model you leave running and come back to

in one of the biggest green flags for a lot of you listening, shipper said that the real leap is around knowledge work. " Sol," he wrote, "is the first model I've trusted to run whole loops of knowledge work, not just help with individual tasks.

It has shifted my job from doing the work to tending the system that does it." Now, probably many of you have spent the last couple of months listening to all of these new conventions like slash goals and discussions of loops. not exactly sure how they relate when you move outside of the coding domain and into knowledge work.



260710 main_EDIT: And so the fact that Dan and others are starting to experience some of that with Five Six Soul is pretty notable

Summing up, he wrote, " If I really [00:14:00] had to put my finger on it, I'd say Fable has way more big model smell."

But that means it's a skill in itself to get value out of it, and 99% of people are still not there yet. GPT 5.6 is almost as powerful, but it's easy to use, fast, and relatively cheap. It should give you an early sense of where model work is going

Theo presented his review in the form of a portfolio posting. " Over the last month, I burned over $200,000 in tokens with GPT-5, 6, Sol. I built a lot."

And if you listen to the way that Theo describes his building process, it once again reinforces the idea that whereas Fable is a model that you let it go off on its own to do things, Five/Six is one you interact with

Now overall, the sentiment towards Five Six Soul is extremely positive

And it feels to me like to some extent, it's also being the beneficiary of the fact that heading into the Fable five ban, OpenAI kind of had all the momentum when it came to the most enfranchised AI users

Codex had increasingly become the default harness that people were looking for

And before Fable at least, a lot of folks had shifted over from Opus to [00:15:00] GPT-5.5 Now, given that we've been so excited to have Fable 5 back, we haven't talked for a while about some of the constraints that were placed on the model when it was announced But certainly for some buyers, those concerns haven't gone away.

Gergely Orosz tweeted, "Interesting take on Fable versus GPT 5.6 Sol from a dev at a large and AI bullish company spending lots of money on AI. They told me Anthropic has not changed their data retention policy on Fable, meaning they would store our data, so we cannot use it. we're going hard on GPT 5.6 Sol as a result."

But as I said at the top of this, the story of 2026 is not just a model story. in fact, in many ways it is equally, if not more, a harness story. As we move into the agentic era, the systems that we put around our models to allow them to access tools, interact with other models, spin up sub-agents

access context, et cetera, are every bit as important as the underlying model themselves

It's pretty clear that part of the reason that OpenAI started to let people talk about GPT 5.6 early is that they wanted the [00:16:00] emphasis on the official announcement day to be on the harness updates that we got in a new user interface that they call ChatGPT Work OpenAI wrote, " ChatGPT Work is an agent that can take action across your apps and files, stay with a project for hours if needed, and turn a goal into finished work."

Now at a surface level

This is OpenAI's answer to Claude CoWork. but it's also clearly the next step of their super app strategy. This is a new agentic harness that takes the functionality of Codex and extends that approach out to all knowledge work

OpenAI wrote, "The best way to learn how to use ChatGPT work is to give it tasks you already know well. Analyze a month-end budget variance, turn source materials into a marketing campaign brief, or prepare for a sales meeting. You can follow its progress, answer questions, change direction, and improve important actions."

Now the interface supports everything you would expect. It has connectors for all of the typical tools, including Notion, Google Drive, and Microsoft 365, allowing easy access to full work context. it also supports scheduled tasks and functions on a cloud instance, so your agents [00:17:00] can work even when your laptop is closed.

It's configurable for enterprise-grade security and access controls, as companies are coming to expect from leading-edge AI tools

The early testimonials sound pretty compelling. Angela Ferrante, the head of enterprise at Zapier, wrote: " Used ChatGPT work to build a repeatable system for reviewing thousands of leads each month. It traced customer touchpoints across Zapier's CRM, email, and other tools, found where follow-ups broke down, and generated a weekly executive dashboard that highlighted missed pipeline and revealed seven figures in potential sales."

And really across the entire set of announcement materials

The biggest part of the pitch is about taking work patterns in Codex and applying them more generally Rather than micromanaging small components of tasks, OpenAI is encouraging knowledge workers to define a goal, load context, and use ChatGPT work to complete large multi-step tasks.

What's more, they said that their teams have already adapted to this new approach

all of their teams are now using ChatGPT, work in Codex with OpenAI writing In sales, ChatGPT Work turned a discovery conversation into a tailored proof of concept for a mission-critical problem within [00:18:00] twenty-four hours, a process that normally takes weeks. ChatGPT structured the notes, routed the request to a solutions architect, and collaborated with the technical team, freeing the lead to focus on the customer and serve as a high-value consultative partner In finance, ChatGPT work reduced month-end close and forecasting from days to hours by helping teams find source data, move it into Excel or Sheets, reconcile it, create slides, and verify the results

This lets the finance team spend more time understanding what's changed in the forecast, explaining why it changed, and advising leaders on what the company should do next

Now, when it came to consumer response

It was a little bit more muted than I think OpenAI might have hoped



260710 main_EDIT: Peter Yang summed up one set of feelings, I think, when he wrote: " I think the ChatGPT work versus Codex thing is confusing. It raises questions like, ' so developers aren't working? And what if I'm using it to plan my vacation?

Is that work?' I think the whole thing should just be called ChatGPT Codex or ChatGPT Codex, and there should be no tabs or toggles. In my opinion, Codex is not that complicated for a normie to understand and use. You're still chatting, except now it can do stuff. The sooner this is all unified, the better."

[00:19:00] Ethan Mollick wrote, " This is confusing. Claude Cowork was a purposefully more secure and slightly weaker alternative to Code designed so non-coders couldn't cause too much trouble. I got that, but I don't understand what ChatGPT Work is or what I am gaining or giving up using it versus Codex on Work."

Now, some were even actively worried about the blending of the apps. Dan Shipper again wrote, "I was extremely worried about this because I love the Codex app. OpenAI was caught in an interesting position. How to make an agent orchestration app for regular ChatGPT consumers, coders, and businesses all in one app.

They now split the interface between ChatGPT Work and ChatGPT Codex. They're basically the same except Work hides code, and Chat has been demoted to second-tier status for quick questions in either one. It's not a big leap, but it's not a huge setback either, and it remains my favorite of the desktop agent orchestration apps."

Still, when you're coming with a big new announcement, having the response be the merged app is fine, which is what Dan's headline was, is not necessarily exactly what you want. I think that there are confusions in the naming conventions, [00:20:00] and to get a real feel for this, it's just gonna take some time for people to actuallyexperience it and figure out what the benefits or the particular challenges are

Now one additional feature, that came alongside ChatGPT work

was their updated sites feature. this basically allows you to turn any knowledge work into a website or web app that you can share with other users inside your company, even if they're not using ChatGPT, which I already did a whole show about how many different knowledge work use cases I think you should be building websites for instead of the traditional artifacts.

And so I think that making that easier and integrating better hosting is gonna actually be a pretty significant change in how people output work with ChatGPT

ultimately all of this is still first impressions. What's clear is that the OpenAI team is really excited about all of these things and seemingly fairly confident that as users get more reps on with both 5.6 and with the work harness Our second and third impressions are going to be even better than our first, but for that we will just have to wait and see

Now we knew that the official release of 5.6 was coming and at least 24 hours before OpenAI started teasing that a new harness was coming as well. [00:21:00] What I don't think anyone expected was for Mark Zuckerberg from Meta to tweet for the first time in three years announcing that Meta was also releasing a new model today, this time called Muse Spark 1.1

Now, the first edition of Muse Spark landed in April without much fanfare, but this updated version seems like an entirely different beast

on the benchmarks, the model looks competitive with Opus 4-8 and GPT-55. It beat both by a significant margin on Humanity's Last Exam, which tests web search, tool execution, and knowledge. On coding, it's in the ballpark, a couple of points behind Opus and 5.5 on Terminal Bench 2.1, and between the two rival models on Suitebench Pro.

On DeepSUI, which is increasingly important as a standard, MuSpark 1.1 was a little further behind with a score of 53.3%, compared to 59 for Opus and 67 for GPT-55. Still, for Meta, who have struggled to produce a viable LLM since Llama 3, this is a big improvement.

And where the model shows signs of actually leading the pack is on personal agentic tasks

[00:22:00] Muse Spark beats both Opus 4.8 and GPT 5.5 on Job Bench, which tests the ability complete real-life professional work

It's state-of-the-art on MCP Atlas, which is a toolathon-style benchmark that tests the ability to gather information through MCP servers

And on DeepSearch QA, which is an agentic search benchmark, it's slightly behind GPT 55 and slightly ahead of Opus 48



260710 main_EDIT: Basically, this is a model that has glimmers of frontier performance, especially in the context of Meta focusing on more consumer-friendly personal assistant style AI

Now we haven't seen a ton of interaction with the model yet But it also doesn't fully appear to be one that just released with no one ever having had a chance to build with it

Nathaniel Whittemore: it 

260710 main_EDIT: The team from Julius, for example, used Muse Spark to build a Minecraft clone inside Julius, which it was able to do in about five minutes for seventy-three cents in tokens

On the VALS AI public LLM evaluation

Muse Spark 1.1 landed at number four Ahead of both GPT-55 and and as Vals AI pointed out, running three times faster than the top three models

Rayyan from VALS wrote, " [00:23:00] Wow, this model is fast. Across our benchmarks, we found it to be one-fourth the latency of Opus 4-8 and one-half the latency of GPT 5-5. I would expect Meta to have incredible web infra, but really don't know what witchcraft they're pulling to host the model for such fast inference at high rate limits."

biggest thing, still the biggest thing that Rayon talked about, and that was really key to this announcement, was the cost

Chubby writes, "Meta Muse Spark 1.1 is a very good agentic model, but above all, it is incredibly affordable and cost efficient."

For example, on Vibe Code Bench 1.1

it came in fifth overall, but the cost to test it was 92 cents compared to, for example, $5.09 for Opus 48 and $12.51 for Fable 5

Rayyan again from Vows wrote, " The model is so cheap I almost don't believe it. In practice, we see it's one-tenth the cost of both Fable and GPT-55."

If you thought open source models would compete away margins, just wait till you see this. it's somehow cheaper to use Muse Mark 1.1 than host your own OS model

Leo really summed up the feeling of many when he wrote, " For my second LMAO [00:24:00] WTF moment of this week, Meta just announced Muse Spark 1.1, and it's also a frontier-level model competing with Opus 48 and GPT-55. Zuck and Elon are back." And I think as we zoom out to broader implications

Every single model this week, Grok 4.5, Swee 1.7 from Cognition, MuSpark 1.1, and even GPT 5.6, had an incredibly strong emphasis on cost and efficiency in its announcement. Even 5.6, which is also competing for the state-of-the-art

So much of the emphasis was aboutits performance in practice and the difference that that was going to make to overall token budgets

What this all means is not only that the AI race has shuffled, which it clearly has, but we are now officially at the point where the labs themselves realize that they are competing on an entirely different vector than just frontier performance alone At the beginning of this week, xAI, now SpaceX AI, and Meta were not functionally in the conversation at all when it came to model selection especially for enterprises And they are now ending the [00:25:00] week back in that conversation.

In fact, 

SemiAnalysis even wrote, " At the simplest level, there are three things you need to build a true frontier model: data, talent, and compute. We believe Meta is the only hyperscaler/neo-lab on track to be world-class at all three, and therefore has the best chance at catching up with Anthropic and OpenAI."

The AI tectonic plates have shifted once again

And in this case, we are all the beneficiaries. I am excited to dig more into these models over the weekend and in the coming weeks. For now, though, that is gonna do it for today's AI Daily Brief. Appreciate you listening or watching, as always, and until next time, peace 

​ 

Nathaniel Whittemore's audio recording:
