---
podcast: "ai-daily-brief"
podcast_title: "The AI Daily Brief"
title: "6 Questions Every Enterprise Has to Answer About AI"
date: 2026-07-30
url: "https://aidailybrief.ai/e/2026-07-30"
guid: "https://aidailybrief.ai/e/2026-07-30"
host: "Nathaniel Whittemore"
format: "news-analysis"
level: 1
length: "00:28:00"
categories: ["agents", "work", "enterprise", "model-strategy"]
featured: ["OpenAI", "agent harness", "Microsoft Copilot"]
mentioned: ["OpenClaw", "Hugging Face incident", "open-weight models", "Claude Code"]
transcript_source: "publisher"
---

# 6 Questions Every Enterprise Has to Answer About AI

[00:00:00] Today Today on the AI Daily Brief, sixsix questions shaping enterprise AI. Before that in the headlines, Sam Altman goes to Washington, and the conversation has gotten a lot more complicated over the last week. The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI.

All right, friends, quick announcements before we dive in. First of all, All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, Blitzy, Retool, and To get an ad free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts To learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai

and to bone up on your AI skills with the last month or so of summer, go check out our latest free self-directed education program, this one being a choose your own summer adventure. You can find it at summeradventure.ai 





Well, Sam Altman has arrived in Washington to meet with lawmakers and White House officials, and when the trip was set at the beginning of last week, the agenda [00:01:00] was pretty simple. Altman would brief Washington on the capabilities of OpenAI's new model and discuss a protocol for release, hopefully avoiding a repeat of the Fable and GPT 56 rollout.



then, since then however, we've had the OpenAI hugging face hack, a public debate about open weights models, and an attention-getting petition for the government to step in and build the capability to slow down the pace of frontier AI. In other words, conversations have become a lot more complicated for Altman in just a couple of weeks.

According to reports, Altman met with Senate Commerce Chair Ted Cruz and several Democrat senators on Wednesday, but we got very little information on what was actually discussed. Speaking to reporters, Altman declined to state when or even whether the model being previewed would be released, commenting, " Not sure.

That's the part we're here to talk about." Altman also declined to discuss the new capabilities of the model that give cause for concern.

Now, of course, the hugging face incident looms large over this visit, but it increasingly appears like the model at the center of that controversy will not see release

In a Tuesday update to their postmortem blog, OpenAI said that the model was an [00:02:00] internal-only research prototype never intended for public release

In Washington, Altman told the press that the model has now been permanently deactivated and is inaccessible even for internal research. Meaning presumably it's not the model being previewed to lawmakers this week said, now Sam said that he and Ted Cruz had not specific legislation, but that, quote, " We talked about our new model and what it's going to take for America to remain competitive with Altman also said that he didn't support mandatory safety testing, particularly because it could introduce an unnecessary burden on open weights model developers, but added, " For frontier models at new levels of capabilities, we think it's really important that the federal government has great testing capacity and capabilities."

Altman said he plans to meet with a range other officials to end the week, including White House Chief of Staff Suzy Wiles, who for whatever reason, has wound up as one of the key decision-makers on AI policy. That meeting will likely include a discussion of the voluntary AI safety testing framework, which has a deadline of August 1st.

Reports state that this framework has been circulated to OpenAI, Anthropic, and Google for comment. But Altman declined to comment on the draft

In a hallway interview on [00:03:00] Capitol Hill, Altman was asked whether he would talk to the White House about the need to decelerate AI development. Representing the views of his staff from the recent open letter, Altman responded, " I wouldn't use the word deceleration, but we talk about the need to pace it as the models get more capable, which I think is in everyone's interests



Now, one other story that I'm going to get into in more depth tomorrow is the significant increase in revenue numbers on both the OpenAI and Anthropic front. But I do not wanna bury that in the headlines, so that will be a major topic for tomorrow.

Come back for that. Suffice it to say, CF- the CFO of OpenAI, Sarah Friar, recently told employees that annualized revenue in July topped all of the previous quarter



one more bit of OpenAI intrigue. President Greg Brockman says that the company is working on an entire range of devices to give a physical presence to their chatbots. in a new interview with former Wall Street Journal reporter Joanna Stern, Brockman confirmed that OpenAI's hardware plans are still on track, stating that the company is building a family of devices.

He wouldn't confirm the recently rumored smart speaker or any other form factors that have seen speculation this year, [00:04:00] nor would he give a timeline beyond commenting, "You can expect them soon." Still, this is the clearest confirmation we've had so far that a full hardware range is still on the roadmap, surviving the end of SideQuest and an IP lawsuit from Apple Brockman was understandably brief when talking about that lawsuit, stating, " We are focused on our own development and technology."

One interesting bit of competitive news which I think sounds good for consumers, particularly those of you who are in the enterprise without a ton of choice on which models and platforms you're going to use. Microsoft appears to be gearing up to compete more directly with OpenAI and Anthropic with the development of a Copilot super app.

During Wednesday night's earnings call, Satya Satya Nadella confirmed the app is coming later this year with the goal of unifying the Copilot experience for both consumer and enterprise customers. He said Copilot is rapidly evolving from chat to co-work to autopilots. This quarter, we are bringing these Copilot experiences together, including code in one super app.

This is a major step forward, and I look forward to sharing more soon Microsoft is beginning to see OpenAI and Anthropic as direct rivals



thanks to the capabilities of their [00:05:00] new MAI models. Nadella told analysts that the combination of cost and data privacy concerns gives Microsoft an opportunity to sell customers on their own cheaper models When asked about the rolling debate about open versus closed, Nadella suggested the framing is too simplified

He said, "The goal is to have the firm be in control of their own destiny. We are very, very clear about the architectural design of the platform, which is you get to keep your harness separate from the model. That means any model at any given time is swappable."



you-- Now, I'm sure some of you will think

That that's kind of a corporate-y answer. But I actually think that his assessment of how most enterprises feel is correct

in that I don't think that most enterprises actually care ultimately about whether a model is open or closed. They care what they can do with it, what control they have and what sacrifices around control they're making to someone else to have access to the systems they're using.

Anyway, Overall, Microsoft is increasingly positioning themselves not as a reseller of OpenAI or Anthropic products, but rather as a model agnostic platform offering a full range of options

Said Nadella, "Every customer wants the right model for each task based on latency, quality, cost, and compliance. [00:06:00] We offer the broadest model catalog in the cloud with over 11,000 models, including the leads from OpenAI, Anthropic, Mistral, xAI, as well as our own MAI family

Now, along the swirl of all these big discussions and jockeying for position in AI, Mark Zuckerberg has made the case for AI acceleration in a new op-ed in The Wall Street Journal. In an essay titled "The AI Future Is for Everyone," Zuckerberg argued that the defining question of the AI age won't be whether superintelligence will exist, but who will have access to it.



In other words, whether we end up in a world where superintelligence is closely held by a handful of institutions or broadly distributed to normal people

Zuckerberg wrote, "It is surprising that the discourse from many of those who are developing artificial intelligence is so filled with doom. I don't understand why anyone who believes that AI will eliminate most jobs and much of humanity's relevance would rush to build that future."

This This is, for what it's worth, exactly the point that I was trying to make yesterday when I was discussing what I think the normie response to the Pacing the Frontier letter would be that the only acceptable answer to why are you building AI is not, "Well, if we don't, someone [00:07:00] else will," but instead, "Because we think AI will be awesome and dramatically better than all the risks that it comes with."



Zuckerberg continued, " The notion that AI is so dangerous that the only safe path is an extreme concentration of power seems dangerous. Historically, hoping that an absolute power will benevolently provide for humanity if sufficiently enlightened hasn't led to safe or positive outcomes."

Zuckerberg's view is that much like previous technologies, like the internet, the best result will come from diffusing the technology freely across society

He wrote, "Rather than centralizing this power, we believe that delivering personal super intelligence to everyone is the way to answer this question. This has the potential to begin a new era of personal empowerment in which individuals have greater freedom to pursue their interests and reach their full potential."

Now, the op-ed came as part of a press tour that linked up with Meta's new AI optimism campaign. In a separate interview with the Journal, Zuckerberg called for the US government to accelerate AI development rather than restrict it. He argued that the benefits of broadly distributing AI outweigh the risks by quite a margin, adding, " I get that it's always hard to debate [00:08:00] about the future because it hasn't happened yet.

But I do think we have a lot of data points at this point, and that should point us to be much more optimistic than I believe the current discourse reflects."

Specifically, he warned against thinking a 30 or 60-day government review window is harmless, commenting, " The field is moving so quickly that actually is quite a meaningful amount of time." Now notably, Meta is the only frontier AI lab that hasn't agreed to the government's voluntary testing framework Zuckerberg also said that the US government shouldn't ban Chinese AI in a separate interview with the Financial Times.

Not only does he think a ban won't be effective, but he believes it would open the risk of regulatory capture and could stymie the release of open models more generally Now, Now Meta's AI CEO, Alexander Wang, recently said that the company will begin launching open source models again, suggesting that this isn't just hollow sentiment Still, overall, the core message is simply that more AI optimism is needed

Speaking with The New York Times, Zuckerberg said, " So much of the discourse from a lot of the other labs that are developing this is overwhelmingly filled with doom. There needs to be a voice or several voices that are bringing realism to this debate."

Now, I think unfortunately Mark Zuckerberg's [00:09:00] power to be the leading face of of AI optimism is limited by history and people's fairly negative view of the overall impact of social media on society



still to start to have loud, sustained discourse that other people can pick up and run with is immensely important, and you better believe I will be here amplifying that message. For now, however, that's gonna do it for today's headlines. Next up, the main episode 

One of the most important AI questions right now isn't who's using ai, it's who's using it? Well,

KPMG and the University of Texas at Austin. Just to analyzed 1.4 million real workplace AI interactions and found something surprising. The highest impact users aren't better prompt engineers. They treat AI like a reasoning partner.

They frame problems, guide thinking, iterate, and push for better answers.

back to the AI Daily Brief. This week, I Welcome back to the AI Daily Brief. This This week, I had the chance to be out in Utah with KPMG for their annual Tech and Innovation Symposium

Now, Now, this is the second year that I've been at the event, and in each case, I've had a chance to do a similar type of presentation

This time around Both my focus and the focus of the conversation after was about trying to sum up, broadly speaking, the big questions that are currently shaping how enterprises have to think about AI

is how much the conversation has changed since last year at this time



Now I'm gonna go through a version of the presentation I gave but before that, I actually wanna zoom back to last year

[00:13:00] 

last year I did Where AI Is: 15 Slides in 15 Minutes, which was actually, as you can see, 23 slides

Now looking back, it's almost quaint what we found interesting or fascinating and what we were discussing at that event. The first theme was acceleration

And we talked about how AI wasn't just moving faster, but was actually getting faster in the speed it was being adopted



I discussed the more than 100% growth in the total monthly tokens that Google was processing between May and July, where they reached nearly a quadrillion tokens



now as many of you know, a quadrillion tokens at this point is about what a single OpenClaw left unattended will do in a month

But it was a big deal back then to see this massive inflection point



And indeed, And indeed, some of the themes from that presentation were effectively setups to where we are now

The compute shortage has done nothing but get worse as we've moved to a new era

And of course, even back then, the big conversation was agents. Now, what was Now, what was interesting is that at least in the way that we use agents today

AI was still firmly in the domain of the future



this was the Claude 4 Sonnet o3 type time horizon

and we were just wrapping our [00:14:00] heads around the meter time horizon task graph that showed that AI capability was doubling every few months



theme, now speaking of themes that would continue to be important

Even back then, it was clear that agentic coding was the breakout agentic use case.

Then again, to give a sense of just how long ago this was

We were all gobsmacked because we had hit a billion-dollar revenue run rate in just about a single year



to put a fine point on how much this has changed. right before this, I read a post from Dwarkesh that suggested that Anthropic Could get to 100 or $150 billion revenue run rate this year

Now, I won't go through all of these different slides, but what stands out to me reflecting back then

was that the questions of AI and agents were really still for some if questions. One slide that I didn't have in this particular chart, but I know I had in a longer presentation that was being given around the same time, was this chart from McKinsey that showed the growth in the number of organizations that had implemented at least one or two or three different AI use cases.

Yes, the big deal in mid twenty twenty-five was still that something like forty percent of enterprises were up to two or three [00:15:00] use cases

A year on, the conversation has changed immensely

and the historian in me thinks it's worth reflecting how we got here



the the big capability jump as we now know came towards the end of the year, the November-December time period where we got Opus For For whatever set of reasons, those were the model updates

where agents and agentic workflows actually came online in a major way. Now, Now, what was fascinating is that it actually took a couple of months for people to really grok that something had shifted. Everyone went home for the holiday, had a little bit of time to decompress



and when they fired up their instance of Claude Code or whatever tool they were using, they found that the stuff that they could do was significantly different than what it had been before

I still remember vividly the absolute tidal wave of tweets in that week between Christmas and New Year's of entrepreneur after entrepreneur and developer after developer coming back gobsmacked about what they could now build that they simply couldn't before

Now Now what's interesting is that this almost immediately translated into organizational practice as well. Part of this was because software [00:16:00] organizations had been adapting to greater and greater capabilities throughout the year and even before

By the turn of 2026, we were long past software engineering organizations a ph- viewing AI coding as just an autocomplete solution and they became some of the first groups in the enterprise to actually shift from viewing their job as writing code to managing the agents that wrote the code for them

That said, maybe because the enterprise folks had been paying attention for over two years at that point, it wasn't like there was some major lag from the AI early adopters to enterprises thinking about what this new agentic capacity was going to mean for their work.



and coming back into 2026, it was absolutely not just software engineering organizations that were racing to put into practice these new ways of working

You saw Vanguard builders and early adopters across domains from marketing to legal to finance starting to figure out, how to bring these new capabilities into their work as well

Alongside the model jump, folks also recognized that part of the new capability set was actually about the harness that you situated the models in

Now, Claude Code had been growing in adoption throughout 2025

but became a real focal [00:17:00] point in the new year, which was perhaps augmented by OpenAI going all in on their Codex product as well

Still, I think Still, I think in many ways, where this whole idea of harnesses, and frankly, a much deepened understanding ofwhat we actually mean when we say agents and what it means to build and manage an agent, came when OpenClaw became popular

Hundreds Hundreds of thousands of people perhaps millions of you include the people who are standing in line in China to get access to an OpenClaw really got their hands dirty figuring out the guts of how these agents work And while you don't necessarily see everyone running their Mac Mini setups anymore, the explosive learning of that early period of OpenClau, I think will be seen as a key inflection point moment for the history of agentic AI

Now, Now, of course, all of this wasn't just happening to individual builders And the evidence that something fundamental shifted started showing up particularly on the revenue side of the ledger for the big labs



for the first few months of this year, it seemed like every time we turned around, Anthropic in particular had released some new jaw-dropping number about how much their revenue run rate had grown Eventually eclipsing OpenAI, although [00:18:00] it's not like they've been particularly slow in their revenue growth either



Now, the interesting thing is that the enterprise experiences the inverse side of that revenue chart as a cost chart

And on the And on the one hand, this was always inevitable. For years, For years, we've been talking about the idea that AI in the enterprise is not just another category of software spend, but represented something fundamentally different, something more akin perhaps to labor

The explosion of intelligence consumption reflected in that growing revenue and the growing cost for enterprises were simply a manifestation of that fact coming to bear

Now, Now, as an aside, the recognition that we were not talking about seats but instead talking about tokens did a whole lot to collapse the AI bubble narratives on Wall Street from Q4 of last year as well pretty pretty soon we were getting stories of enterprises absolutely torching their annual budgets in just a few short months.

Uber was the most notable of this And although these stories were presented as surprising, if you actually think about it, It's really not that surprising at all.

How are we gonna expect organizations toeffectively budget for the agentic token era of AI when no one knew that that was right around the corner when [00:19:00] those budgets were being made?

Subsequently, and regular listeners of this show will know that these are the themes that have dominated for the past several months. We have seen adaptation to this new agentic paradigm run in all sorts of different directions. In some corners, we're seeing token caps where companies are going with limits per user per month.



we're seeing companies have to experiment with and try to figure out measurement and monitoring and observability systems



As As costs spiral, it puts a whole new emphasis something that was already coming up in the harness conversation around the fact that we were no longer just talking about AI as a choice of which models, but as an architectures and systems design question



The router, of course, the product du jour is one response to this. but when it comes to enterprise buyers and planners and strategists I don't think anyone, and certainly my conversations this week the KPMG event have confirmed this, is looking to OpenRouter or any other solution as some silver bullet that's going to solve all these problems

And there And there are new problems. Specifically, the capability gap is growing on both an individual and an organizational level. the capability gap, of course, is [00:20:00] the space between what AI can do and the value that we're getting out of it



Now, the good news is that it's grown largely because the upper bound of what AI can do It is rocketing upwards at an incredible rate And yet still there are real consequences to that gap widening

One of my bully pulpit issues is that I believe that the upskilling bill is coming due in a huge way

When AI learning was just about whether you could prompt well, maybe you could get away with not investing a ton in training your workforce. Now, on the other hand, we are talking about a fundamentally new work primitive. The way The way that people work is changing in a core way in many disciplines and functions from I do my work to I manage agents that do my work for me.

the the need that that creates for training is radically heightened from the previous era of AI



and indeed one of the things that a lot of folks are talking about here at this event

is how to deal with apportioning these incredibly powerful tools that are inherently technical tools to folks that aren't engineers and aren't technical by background

[00:21:00] 

There are a lot of stories floating around this event of people accidentally unleashing agents on critical systems. not because even necessarily they were doing anything wrong, but because there weren't the right guardrails or access provisioning, and these incredibly capable models with their new tenacity just didn't stay in their boxes Now, this is not Now, this is not an upskilling question alone

again, the watchword of the moment is systems and architectures



but without that training, organizations are almost doomed to face this sort of issue in increasing fashion. Or on the other hand, restrict the opportunity for people who could really be doing incredibly valuable work with these tools to do so because they're not trusted to do so



and and this gets us to the questions that were explored not only in the panel discussion that followed this presentation, but honestly in the side conversations all over the event as well

The first question is how are enterprises redesigning for the agentic era?

And And the key word here is redesigning



the biggest caution that folks like Steve Chase from KPMG on the panel had was the warning of the problems with and ill effects of trying to simply [00:22:00] bolt on an AI strategy to existing processes and systems Now that has always been problematic and at least under maximizing for the potential of AI, even when we were firmly in the assisted AI and efficiency AI era.



but in this time of new agent capability, that gets even worse

Relatedly, the second question is about the nature of that redesign

and why organizations need to be thinking in terms of architectures, systems, not just models.



if previously an organization's response to some new challenge brought by technology was to figure out which vendor was best suited to solving that problem, that is simply insufficient for the moment that we find ourselves in now



thinking about architectures means thinking about complex model systems that allow different levels of intelligence for different types of tasks. it means thinking about, yes, the routing systems, whether they are products off the shelf or bespoke or something else that allow that routing to happen.

But it's also about that harness design, about which functions and people have access to what types of context and data and systems integration, and what the guardrails that surround it need to be

And And as we get into the third question, how are you provisioning costs across [00:23:00] different groups? The big thing that underlies that is another systems design need, which is systems for monitoring and measuring AI usage



seen, you have not seen the word token used more at an event since the height of the crypto era, man

And obviously the tokens we're talking about at this event are very different

But there is a very broad recognition here

that without better visibility into

the cost of AI and its relationship with outputs, it gets very hard to figure out which individuals, which groups, which functions, which projects should be getting access to which types of models 

and at what magnitude? 

see, given given that bully pulpit I mentioned before, I've certainly been gratified to see how big a concern enablement in education really is among these organizations. If I had to characterize the average discourse I've seen around that, there is a lot of throwing up of the hands and saying, "Screw it, we're just gonna have to do this ourselves," and experimentation with bespoke customized solutions for this that work for the organization and the population that it has.

In other words, there's a recognition that this is not gonna [00:24:00] be a bunch of cute video courses of the pattern of corporate trainings yore, but instead is going to involve real messy work of getting people to use these tools in new ways to do new things

And then figure out how to transmit knowledge between parts of the organization that are figuring it out well versus parts that are not figuring it out so well. Indeed, one of the big patterns that I am seeing over and over and over again is various forms of collaboration between Both, AI redesigned software engineering organizations and business units, but also AI early adopters and AI champions and other types of business units

I think the sophistication in the conversation is that no one is talking about the marketing folks replacing the engineers, but they are now talking about the 10% or 20% of the types of skills and even more than that, mindsets that engineers or product managers have that can become a part of the essential toolkit for those people in other functions, be it marketing or sales or back office or what have you, and how to best do that new sort of transmission

Now, I would say that a lot of the discourse at this event

has been focused on internal transformation. [00:25:00] 2026 is very clearly the year thatfor this representative sample of enterprises, as not a technology problem, but a transformation problem has really come home to roost as the reality and yet there is also the entire dimension of agentic transformation that has to do with what happens externally as well.

In other words, how are agentic opportunities, reshaping business cases?

some of the examples of that that people are discussing here include shifts to the business model. People experimenting with outcomes-based pricing of input-based pricing like hourly billing. there is some discussion of new types of products and new types of services that become available in this new context.

And there's also a lot of reevaluation of what the core state of the old product actually means. What is, for example, an audit if agents can be doing a lot of that work and if they can be doing it not just on a one-off basis but on a persistent basis? 

it feels to me as though that while that type of conversation is happening, most organizations are viewing themselves as patient zero, let's call it, for for whatever their external AI strategy is, and are focusing on shoring up how they work first before [00:26:00] necessarily making radical changes to what they sell externally.

Although certainly for certain types of organizations, that change is being forced upon them Now, of course, when it comes to business model disruption, it's made all the more difficult by the fact that no one gets to just shut things down for six months to figure this all out. They gotta do it in real time, even as they're servicing legacy customers on legacy products with legacy methods of delivery

And on top of all of this, the the last question that we explored and that was floating around here is if and as we are successful in designing new systems, how can we build dynamism into that, that has almost planned obsolescence and an appreciation of ephemerality built into it

the harnesses around them are going to change

Interaction patterns are going to change

Customer expectations are going to change. Market expectations are going to change. Policy is going to change

and so whatever new that gets built has to assume And design for the fact that a few months down the line from whenever it is ready, will likely require it to change all over again

If If all of this sounds head-spinning, it is. But I think that there is something [00:27:00] immensely positive. Last year, Last year, even at this event, which is about as AI-pilled as an enterprise event can be There There were still, as I said, so many if questions.

How do I convince others in my organization that this is real and that we should be doing it? How do I show ROI to prove that what we're doing is worth the time and money that we're spending on it?



now it's not that ROI questions and things of the like are gone. But by and large, the questions that people are asking now are, it feels like to me, the foundational questions for redesigning for a new era that we are going to be answering for the next, call it half decade



Companies asking about designing and allocating token budgets



are now exploring this new category of spend that is just going to become an essential part of their organization. When companies are talking about building observability systems around the new intelligence they're using

While the models and harnesses may change it is very likely that whatever gets updated is still going to need that sort of observability

I guess the I guess the point is that the paradigm shift has happened. for years, basically since the ChatGPT moment, enterprises have been [00:28:00] anticipating The shift from assisted AI to agentic AI, the opportunity for AI not just to help us do work, but to actually do the work itself. Now that that is here, all of the questions

are about how we solve all the new problems that that new way of working brings and how we best seize the opportunities that it opens up.

Almost none Almost none of the questions have answers right now

but it should feel good, I think, that the questions being asked are the right ones. Anyways, thanks to KPMG for having me out. It was a great event, and I look forward to coming back next year Where honestly, I can't even imagine how different it's gonna be by then. For now, that's gonna do it for today's AI Daily Brief.

Appreciate you listening or watching as always, and until next time, peace.
