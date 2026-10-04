# How Big Is the AI Economy? — Transcript (2026-06-30)

https://aidailybrief.ai/e/2026-06-30 · Listen: https://pod.link/1680633614

<!-- metadata -->
Format: news-analysis · Level: 1 · Length: ~00:27:00
Host: Nathaniel Whittemore
Categories: infrastructure, enterprise, policy, model-strategy
Featured: Anthropic, Claude, Claude Code, Claude Mythos
Also mentioned: distillation, OpenAI Codex, Gemini
<!-- /metadata -->

---

[00:00:00] Today on the AI Daily Today on the AI Daily Brief, just how big is the AI economy? Before that in the headlines, are we are we about to have to KYC to use the newest AI models?



the AI Daily Brief is a daily pod... The d- the AI Daily Brief is a daily podcast and video about the most important news and discussions in AI. All right, friends, quick announcements before we dive in. All right, friends, quick announcements before we dive in. First of all, thank First of all, thank you to today's sponsors, KPMG, Scrunch, Mission Cloud, and Outsystems. To get an ad-free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts And if you wanna learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai.

By the way, if you haven't checked out the new improved aidailybrief.ai, you should check it out

Each episode is not only summarized, but chunked into the key numbers and a set of between 15 and 20 shareable chunks that are the key points, key quotes from the show, organized by topic. If you've been looking for a way to share just some specific part of [00:01:00] the show, Go check it out at aidailybrief.ai. Although lots going on, so this might be a slightly extended headlines. as per usual, we are starting with our Mythos/Fable watch, where we are getting more signs of a Fable relaunch, but with some strict new controls

AI leaker M1 Astra posted some new code strings to the Claude app, giving some hints on how the Fable relaunch might be handled. Firstly, it seems that Fable usage will be credit-based rather than part of subscriptions. It's unclear whether Anthropic will still honor the trial period

But the code strings indicate clearly that Fable usage will be billed separately ultimately. In addition, it appears model access will require users to submit identification documents to Anthropic. One code string states, "Your credits will be added once your identity is verified."

And And And folks are not so happy about this

Hader wrote, "No sensible person is going to give their identity verification to Anthropic just to use a heavily guardrailed model."

While I understand where Hader is coming from, Having spent a lot of years closely watching people's relationship with privacy when it comes to [00:02:00] technology, I am quite sure that basically everyone is going to give their identity verification to Anthropic Even if the model is heavily guardrailed

indeed some believe that this was inevitable as soon as the government intervened. Max Weinberg commented, " I called this within 40 minutes of Fable and Mythos getting banned. Seems like the only path forward, similar to getting a gun license."

Given how the government seems to view these models, I think that's a fair comparison By the way, that is a comparison that Dario Amodei made himself When he said about Mythos, companies we gave to it said, 'This is a super weapon. you should have to own a gun license to use it.'"

So, you know, just A+ communications all around

Now, of course, at this stage, this is just rumors based on code snippets, so we don't have anything official



especially as we get closer to what people anticipate might be the return of Fable. People are going to be looking for any information in the tea leaves

Now, as we discussed yesterday, even when we get Fable back, the impact of this whole saga is going to be widespread, not least of which in Washington, DC. In DC, Senator Mark Warner is preparing to unveil a [00:03:00] sweeping new regulation apparatus for AI agents.

So what is in this bill? Well, first of all, the bill protects access for third-party agents. For example, it ensures users can send their own open clot to shop on Amazon rather than being locked into the built-in agent.

Amazon and other platforms have started experimenting with various methods of blocking or restricting third-party agents, although these largely deal with data scraping rather than agentic shopping The bill also enshrines a concept of a duty of loyalty that ensures agents are acting on behalf of their users rather than the companies that create them.

A legislative aide used the example of a travel booking agent preferring to book with Hilton due to an undisclosed partnership with the hotel chain. This kind of behavior would be barred under the regulations

Senator Warner said in a statement

As agentic AI transforms how Americans interact with technology, consumers deserve a real choice in the marketplace, and AI agents must be accountable to the people they serve. This discussion draft is a major step towards building a clear federal framework that promotes innovation, protects consumers, and ensures the United States continues to lead the world in emerging technology

[00:04:00] Now, it's worth noting that the bill is exclusively concerned with consumer-facing agents, meaning it won't deal with internal workflow agents for enterprises

And at the moment, the bill is just a discussion draft and is relatively brief at twenty-five pages It largely instructs government agencies to develop regulations according to certain principles. And there's also an understanding that the bill isn't likely to move forward this year. A staffer acknowledged that the bill likely needs a Republican co-sponsor and a companion bill in the House before it can be put through committee

but Senator Warner is one of the most powerful Democrats in Washington And the fact that we are now at the stage where we're getting into the nitty-gritty of agent behavior gives you an indication of where things are headed

Now it's too early to get too deep into the substance of this bill But I'm basically of two minds when it comes to this. On the one hand, it's going to be very important to keep an eye on how much liability these sort of regulations impose on agent providers.



as many times we've seen well-meaning proposed regulations effectively amount to a backdoor ban At the same time, these sort of agent neutrality principles that Warner is articulating

are probably gonna be welcome to lots of folks. [00:05:00] And so it's worth not dismissing out of hand



staying in, now staying in the government's relationship with AI, but moving to a very different part of that, California has cut a deal for half-price Claude. Governor Gavin Newsom announced a new agreement with Anthropic to expand the deployment of Claude across the state government.

All state departments and local governments will now have access to Claude in the first statewide rollout of an AI tool. Anthropic has also agreed to provide free workforce training and technical support, all at 50% off. California's CIO and Department of Technology director, Chris Given, said, " A lot of departments are going to switch their usage to this contract, and that's very much our intent.

When we see that folks are going to be using a tool more, we want to make sure that we, as the state, have negotiated the best possible price."

Also, despite Anthropic's ongoing schism with the federal government, Newsom's office said the new contract was not intended as a response to Washington. Newsom was also cautious of negative AI sentiment, especially in government services, commenting, " AI should not replace the human work of government. It should help our workers move faster, solve problems more effectively, and deliver better results for Californians."

Next up, another [00:06:00] deal with Anthropic. and this time it's Amazon. The Information reports that Anthropic has renegotiated the sweetheart deal that Amazon locked in as part of their $13 billion investment. Until now, Amazon's Claude bill was based on raw computing hours, effectively a wholesale rate. In a new pricing agreement set to begin next year, Amazon will have to pay token-based, similar to every other large Anthropic customer.

The pricing adjustment doesn't just apply to internal use of Claude, but also to Amazon products powered by Anthropic's models, such as Alexa for Shopping. Sources said that Amazon is now looking into potential cost savings from switching to OpenAI or even their own in-house Nova models.

Amazon's recent $50 billion investment in OpenAI allows them to use OpenAI models in their products for the first time, but there's been no reporting on how that arrangement will be priced. The reporting also dug into simmering acrimony between the two companies. Anthropic was reportedly frustrated late last year when new features weren't added to Bedrock fast enough for their liking.

On Amazon's side, the information writes, " Fears that Anthropic's models might eventually become more expensive [00:07:00] have prompted some engineers to distill them proactively The source added that Anthropic does still have some limited rights to use Anthropic models to build their own small models for internal use. An Amazon spokesperson denied the reporting, commenting, " Amazon and Anthropic share a multifaceted partnership grounded in technical collaboration, and we continue to foster that relationship and deepen our work together.



It's incorrect that changes from our expanded collaboration will increase our costs."

Anthropic also claimed that their services are in fact getting cheaper, with a spokesperson for them stating, " The cost of getting important work done with Claude falls every generation. In November 2025, we significantly reduced Opus pricing, And that price has held since while the models keep getting more capable, so the same budget buys materially more each cycle."



Look, all of those are the things that Amazon and Anthropic are supposed to say, but it's still pretty clear that the end of the AI subsidy era is dramatically changing the economics for AI services



Meta, meanwhile, has placed limits on Codex and Claude Code, but not because of issues of cost. According to internal guidelines reviewed by the information, Meta is placing strict controls on how software [00:08:00] engineers in their Applied AI division use the leading coding agents.

Applied AI is Meta's recently established data labeling initiative, which seeks to collate training data for their frontier AI efforts. One memo told teams to discontinue the use of Codex and Claude Code on certain tasks for fear that model outputs could contaminate training data.



The document warned that this could lead to, quote, "serious escalations with partner companies." Now, Meta has been one of Anthropic's largest customers this year, pushing Claude Code in every corner of their operations. However, the Applied AI team is now required to solve coding problems without the use of AI to avoid contaminating the training data.

The restrictions are fairly widespread in training workflows. Workers have been prohibited from using AI to create programming challenges for use in training data, and they also aren't allowed to use AI to look for bugs in source code or generate ideas for problems based on code analysis. The memo stated that these workflows, quote, " fall firmly in the category of the engineering being out of the driver's seat, and 

and we do not want tasks that originated from models." Sources said that these guidelines were introduced in May but remain in place, and they suggest that Meta is worried about inadvertently [00:09:00] distilling models from OpenAI and Anthropic as they build their own frontier coding model.

Distillation violates the terms of service for both frontier labs, and the new policy suggests Meta is concerned about legal exposure. Anthropic has, of course, been particularly active in documenting distillation efforts from the Chinese labs. Back in February, they released a report detailing distillation attacks, and earlier this month, they wrote to Congress complaining that Alibaba had engaged in this practice at a massive scale

Chubby summed it up. Meta is now facing the exact problem every AI company will soon face. It wants to replace expensive external coding tools like Claude Code and Codex with its own internal system, MetaCode. But to build a better coding model, Meta has to make sure it's not accidentally training or evaluating on outputs from rival models.

That is the distillation trap. The more companies rely on frontier models to build internal AI infrastructure, the harder it becomes to prove where the intelligence actually came from



Now, according to the Financial Times, that is not Meta's only recent challenge. as the FT reports that Google capped Meta's use of Gemini earlier in the year as a way to deal with the compute crunch

Back [00:10:00] according to reports, Google imposed usage limits on Meta and other large customers in March. sources said that the restrictions, which remain in place, were part of the reason Meta stopped token maxing and encouraged staff to be more token efficient. Several other clients were reportedly effective, but none to the extent of Meta due to their exceptionally high token demand.

Aside from burning tokens to top the leaderboards, the FT reports that Meta Gemini to automate some of their safety processes

As well as driving some customer service and advertising help chatbots. Sources said that Meta used Gemini and Claude because they were more performant than their in-house Llama models. But more recently, the focus has shifted to prioritize the use of Muse Spark, which was the model that Meta released in April

On the topic of the compute crunch, the FT wrote, " Despite spending tens of billions of dollars on chips, data centers, and power, even the largest tech companies are struggling to secure enough computing power to support surging demand for advanced models and AI services."

On that topic, AWS has hiked prices on GPU rentals. AWS announced that they would be raising the price for EC2 capacity blocks by twenty percent, which impacts workloads [00:11:00] scheduled to run on NVIDIA The price hike won't affect capacity blocks using Amazon's Trainium chips Capacity blocks were introduced by AWS in 2023 to replace on-demand GPU rentals which were no longer viable in a supply-constrained environment.

They function in a similar way, but require reservations in advance

Now, the pricing adjustment is another data point in the hotly debated AI inference market earlier earlier in the month, you might remember there was that widely misinterpreted token expenditure index crashing for multiple weeks in a row. As I discussed at the time, the index shows average token costs from token routers not overall expenditure

and was also sourced from data from the companies whose job was to help their customers find cheaper alternatives. But it did give some indication that the market was starting to turn to cheaper open source tokens



more recently, spot rental prices for H-100 fell significantly and are now down 40% from their peak in May

The AWS price hike, however, suggests that this could also be a slightly misleading signal



Semianalysis noted that their own data showed that although spot GPU rentals [00:12:00] were falling, contract prices still going up They wrote, Spot and on-demand markets are where buyers run proof of concepts, one-off evaluations, burst workloads, and capacity overflow.

They can be useful when taken as part of a data set, but are not reflective of where production economics are set. Contract pricing is where sustained workloads show up with the intention of planned, recurring, revenue-bearing inference or training demand. Falling spot prices alongside rising contract prices are therefore not evidence of weaker demand.

It is more likely a shift of opportunistic capacity usage towards committed production deployment." In other words, they conclude, " Serious buyers are locking in term capacity, and that is pushing contract pricing higher."



Lastly today, spiking memory prices from AI demand are driving a search for a scapegoat for the Ramageddon. Last week saw Apple raise prices on multiple products by as much as 15% due to increased memory costs. Microsoft quickly followed suit, announcing a significant price hike for Xbox consoles.



At a conference last week, Lenovo declared that pricing will never return to where it was last year and presented their five-step [00:13:00] Ramageddon survival guide

Now, some are using the price spike as another reason to hit on the AI industry, viewing high memory costs as a tax on all electronics. Bloomberg's Joe Weisenthal pondered the implications in a recent newsletter, suggesting that winning the AI race may require diverting real resources from the non-AI economy

What he called a worrying but plausible path others are looking to the memory producers themselves, accusing them of excessive profiteering. Writes The Wall Street Journal, " "We We are witnessing an enormous transfer of cash from the providers of AI, and perhaps one day AI users, to the memory chip makers.

Profit shifts of this scale are rare events, and investors should be paying attention to where the money's coming from, where it's being spent, and how long it will keep flowing."



now to give an example, Micron has increased their prices by more than 60% over the past three months and quadrupled them over the past year, and recently reported that they're running at gross margins and targeting 84% margin by the end of the year That puts them on track to have the third highest profit margin among US companies behind only Google and Nvidia

And it's in this [00:14:00] context that the Financial Times reported that Apple has petitioned the Trump administration for clearance to buy memory from Chinese supplier CXMT, a company that is currently on the Pentagon's blacklist due to alleged ties from the Chinese military

Separately, a class action lawsuit was filed in California this week alleging that Samsung, SK Hynix, and Micron conspired to run a memory cartel to inflate consumer memory prices

which is beyond the scope of this show to go deep into, at least for now

But it's a good indicator of just how severe the memory shortage is becoming

Now there is even more we could get into today with the headlines, but we are already way over time, so let's close it there and head into the main episode where we are going to talk about the true size of the AI economy 

One of the most important AI questions right now isn't who's using ai, it's who's using it? Well,

KPMG and the University of Texas at Austin. Just to analyzed 1.4 million real workplace AI interactions and found something surprising. The highest impact users aren't better prompt engineers. They treat AI like a reasoning [00:15:00] partner.

They frame problems, guide thinking, iterate, and push for better answers.

Welcome back to the AI Daily Brief. Today we are talking about one of the, one of the most interesting and [00:18:00] consequential questions Welcome back to the AI Daily Brief. Today we are talking about one of the most interesting and consequential questions around AI, which is just how big is the AI economy? now this question is much more than a vanity question. ever since the ChatGPT moment in late 2022 And the corresponding explosion of economic activity surrounding AI, There have been questions about whether we were actually in some sort of bubble that inevitably would pop. Now, relative to other technologies, frankly, AI has done a pretty good job of outrunning the bubble question, at least when it comes to its utility. In other words, as much as a handful of skeptics have tried, by and large folks accept that AI is extremely useful.



but as many market historians will point out, a technology can be extremely useful and still produce a financial bubble. these two things don't necessarily have anything to do with one another. 

This is, of course, why questions about a bubble got much louder throughout the course of 2025 as companies, significantly increased the size of their AI infrastructure [00:19:00] build-outs now at first the hyperscalers were just using their free cash flow to finance data centers and other infrastructure but as that free cash flow has been used up they've turned to other sources, including debt and credit

Now, right now we're on a little bit of a low ebb when it comes to the bubble talk, but that never lasts for that long

And in that vacuum, it's a really good time to actually try to somewhat dispassionately understand just how big the AI economy is right now Or putting it differently how much economic activity around is justified not only by the future potential, but by the numbers today Enter the team at Exponential View, who have just released a great report called The State of the AI Economy

they went through reports surrounding over 1,000 AI companies

They gave a confidence score to different sources



meaning that actually audited accounts count for more than public comments by executives. and they made sure to deduplicate so that AI spend was only counted once



in other words, $100 in app spend that sends $60 to a model provider, and $30 on inference hosting is counted as $100, not [00:20:00] $190

So let's talk about the big numbers and then let's get into the details. The top line they say is that AI demand is more clearly validated by realized revenue than previous platform shifts

Or as they put it, demand is real, big, and fast. Indeed, the sector they say is growing three times faster than any IT wave before it



the big headline number



is that AI companies have banked 110 billion over the past 12 months

And are at an annualized run rate of 175 billion 

compare that to year three revenue

And the revenue is growing fast They point out that back in 2023, the AI industry needed 180 days to add a billion dollars in cumulative revenue

It has now gotten 90 times faster at that, needing less than two days to add each new additional billion dollars of revenue

And And what's more, as regular listeners of this show will know

Demand for the core product has also launched economic value beyond the core product



what the exponential view dubs a compute super cycle

2026 projections have the global semiconductor market reaching one point five trillion in revenue this year, Basically [00:21:00] doubling from last year's seven hundred and ninety-two billion

And that demand for compute also has secondary effects

As AI demands reignites, what they call a moribund US power sector

Between 1950 and 2008

US electricity net generation grew at six terawatt hours per month on average. between 2008 and 2024 however, post-global financial crisis We have effectively been flat with no new net US electricity generation.

Between 2024 and today, We're now seeing annual growth at 150% the historical average, reaching nine terawatt-hours per month in annual growth



more, but let's talk more about the relationship between all this CapEx spend and current revenue. The way that they sum it up is that the largest build-out in tech history is paying back for now



CapEx will reach eight hundred and forty-eight billion this year and two trillion cumulatively since twenty twenty



And while the majority is still coming from balance sheet cash



external funding sources like debt are definitely on the rise



now in terms of the revenue picture today, [00:22:00] the report argues that revenues are covering the ongoing expense but not yet the cumulative bill starting in Q4 of last year, quarterly revenues started to exceed CapEx depreciation

And what's more

rental yields suggest that a lot of infrastructure is outperforming its long-term depreciation expectations



this has at times been one of the key questions around the bubble With people arguing that if all these GPUs that companies are buying are out of date almost immediately That doesn't give a lot of time for them to make a return on their investment.



however, what the data suggests is that older GPUs are earning yields long beyond their six-year depreciation life

Seeing meaningful gains all the way into year seven, year eight, and even year nine



this obviously creates a much healthier economic scenario in which, to pay back all that CapEx

Now, as the report points out, we're still really early. despite all this infrastructure cost

AI revenue still has a ton of room to grow

For one comparison The IT sector represents around 9.4% of US GDP. AI revenue, meanwhile, is equivalent to [00:23:00] 0.42% of US GDP



these numbers are growing quickly, however. AI revenue relative to GDP has written 3x versus Q1 of 2025 and 10x versus Q1 of 2024



And even though so much of our discussion right now is around token efficiency and token caps and things like that, the report points out that AI spending is still relatively small relative to what it might be

The example they gave is Uber's 1.5K per engineer



which as they point out barely dents that company's P&L

only, and not only does AI consumption have room to grow, it very clearly is



that, the report points out that the transition from chat to agents is multiplying token use

Pointing out that an agentic coding task can have around 1,200 times the tokens of a chat task

Global token volumes are now above thirty quadrillion per month and are growing fourteen X year over year

Now what's interesting is that even though overall AI spend is going up because of that growth of token consumption the cost of tokens on a unit basis is going down



between mid '24 and mid '26

despite the epic capabilities [00:24:00] index of AI going from 112 to 158, IE meaning AI can do a lot more now The blended price per million tokens went from $17 to $2, And the tokens processed per output token a measure of the intensity of the average request jumped from twelve to thirty-six.

As they point out, price declines encourage more use and make previously uneconomical applications viable

And And bringing it back to CapEx, this new efficiency is increasing electricity monetization even though revenue per token is falling

Energy monetization per gigawatt is increasing

Energy monetization has basically doubled since mid-2024 in terms of the amount of revenue generated per each gigawatt of capacity



and as much as it requires a broad adjustment

The report argues that token-based pricing is key to the next step of the AI economy



comparing it to the moment in digital advertising when we went from untracked banner ads to attributable ad spend with pay-per-click



which grew annual digital ad revenue to way over $100 billion by 2024

Now, in terms of where value is [00:25:00] accruing, revenue remains concentrated around chips, but the mix is starting to shift the portion of overall AI revenue that is, from hosting is going up. obviously foundation models revenue is going up.

And for the first time, app revenue such as from companies called Cursor is showing up as well

Indeed, the report argues that value is moving up the stack towards apps and models



the percentage of AI revenue that comes from the app and model layer was up almost 3x over the last year

and the value stack mix is still very unresolved. one of the things the report points out, which will be familiar to all of you guys

is that even as there's pricing pressure around token costs, labs are increasingly pushing both down the stack into infrastructure and up the stack into apps. And I would expect these sort of shifts and experiments to continue for some time to come

Now, in terms of justifying all this spend from a business perspective, public companies are reporting increased impact of Gen AI

The percentage of companies making claims of AI impact on earnings calls has jumped from around 10% back in early 2023 to a third at 33% today, with now a full 20% of companies quantified claims on their earnings calls

[00:26:00] 

of the, and while most of those claims right now, seven in 10, focus on either cost savings or efficiency



the most dramatic indicator of the comparative success of high AI adopters comes in the comparison of revenue growth between companies with no AI spend and companies with high AI spend

Companies with no AI spend have grown revenue over the last three years pretty close in line with US nominal GDP

Between 15 and 20%. Companies with high AI intensity, i.e., those who are in the top 25% of AI spenders by share of revenue



have seen their revenue grow in that same period by more than 100%. In other words, there is a 92% revenue growth differential between high AI spenders

and no AI spenders

The conclusion they write AI demand is more revenue validated than any prior platform shift Ultimately, they say the investment case comes down to whether falling prices can move enough token volume to earn a return on CapEx. But as you just heard, a lot of the indicators of that are much more positive than the average discourse suggests

So [00:27:00] friends, that's how big the AI economy is, it's on 175 billion annual run rate. It's growing three times faster than previous platform shifts

It's causing massive secondary growth in the compute super cycle and in the energy build-out

Many of the raw resources of that infrastructure build-out, i.e. the chips, are seeing economic value past their expected time horizon

None of this is to say that the market can't get over-exuberant But I continue to think that the most insightful tweet ever about an AI bubble came from OpenAI's Rune back in October of last year when he tweeted, " Not enough people are emotionally prepared for if it's not a bubble."

That's gonna do it for today's AI Daily Brief. Great work to the team at Exponential View Check our show notes for a link to the original report. And thanks for listening or watching, as always. Until next time, peace 

​
