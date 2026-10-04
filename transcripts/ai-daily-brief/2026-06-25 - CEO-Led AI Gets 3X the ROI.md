# CEO-Led AI Gets 3X the ROI — Transcript (2026-06-25)

https://aidailybrief.ai/e/2026-06-25 · Listen: https://pod.link/1680633614

---

[00:00:00] Today Today on the AI Daily Brief, why companies where CEO owns the AI strategy are seeing three times as much ROI. Before that in the headlines, so much is going on, including OpenAI announcing their first custom-designed chip. The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI

All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, Superintelligent, Mission Cloud, and OutSystems. To get an ad free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts. And if you wanna learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai. 

Lastly, check out our new enterprise upgraded training programs at training.besuper.ai. The new executive agent leadership program Kicks off next week and is registering now Man, some days there is one dominant story that just absolutely kicks into dust all the small things that are happening around it. And then [00:01:00] there are other days where there's no one singular story that everyone is talking about, but about a million smaller stories

that if we're looking for them correctly, tell us all sorts about what's actually happening in the world of AI

and almost serve as tea leaves for what might happen next. today is one of those days, so these headlines might be a little bit longer than five minutes. First First up, OpenAI has unveiled their first in-house chip. The chip is codenamed Jalapeño and was produced in collaboration with Broadcom.

OpenAI referred to Jalapeño as an integrated processor and described it as the, first AI accelerator in a multi-generation compute platform."

In a statement, OpenAI President Greg Brockman said The The world is moving to a compute-powered economy. Jalapeno is part of our long-term full stack infrastructure strategy to make compute more abundant, resulting in AI which is faster, more reliable, more affordable for people and businesses, and can be used to solve more important problems.

By designing more of the stack ourselves, we can serve more intelligence with greater efficiency and keep pushing advanced AI towards broader access. The chip is The chip [00:02:00] is an ASIC similar to Google's TPUs, which means it's designed for the specific task of serving inference for LLMs. By contrast, NVIDIA's GPUs are much more general in their application. OpenAI said that they believe this to be the fastest development cycle ever for a high-performance ASIC, going from initial design to manufacturing tape-out in nine months

In an interview with CNBC, Brockman credited the speed to AI-enhanced design, commenting, " The degree to which our models have been able to accelerate it was very surprising to us." Now, while Now, while OpenAI will begin deploying the chips as soon as they're ready, This almost certainly does not mean they'll cut down on NVIDIA orders. Brockman reaffirmed that OpenAI, quote, "Cannot get compute fast enough."

Appearing alongside Brockman, Broadcom CEO Hock Tan agreed, stating that compute demand from all of their customers is, quote, "simply insatiable." Tan Tan added, " "It's It's just much more than we can address, and this is not just '26, not '27. We're seeing that same and even elevated demand in '28 as well."

Now in a little bit Now in a little bit when we talk about Micron, we will come back to why

The long duration [00:03:00] nature of that demand is one of its most significant aspects.



one one additional small update from OpenAI. Atat this point, any model update that isn't at the edge of the frontier is likely to fall on fairly deaf ears. But OpenAI has handed free users another upgrade with a new version of their GPT-5.5 Instant

For the portion of people who are on the free plan, which is the vast majority of ChatGPT users, These sort of updates to instant can make a big difference. OpenAI OpenAI claim the model is much more fun to talk to, saying, " "Our Our most used model is now better at understanding the intent behind a question and adapting its response accordingly.

It also handles complex constraints more reliably and makes shopping and local recommendations more useful and cohesive."



now for those trying to understand where general consumers and free users fit alongside the clear increase in importance of enterprise customers. OpenAI has now released upgrades to their instant model every month or two since February

Whether that's because they really care about free users as a category or because they see them as top of funnel for their bigger enterprise use, Doesn't really matter in practice, the models that the free users have access to continue to [00:04:00] improve as well

wellNow Now on the question of the model that we are really waiting for We continue to experience rumor whiplash as prediction markets went from very dreary about Fable 5 to all of a sudden a massive increase in the chance that we get Fable 5 back soon.

Around Around 2:00 PM on Wednesday



the odds of a fable return by July 1st skyrocketed from 15% all the way up to 63%.



assuming that there was some sort of insider knowledge going on, Greg Eisenberg posted, " Someone knows something." Now, there Now, there have been at least a few signs that things are moving



earlier in the day, SynthWave posted a code snippet from a Claude code update, which they believed, quote, "Hints at preparations for a Fable 5 return, with it being permanently included in subscriptions with weekly usage." the code snippet adds a warning for using up weekly Fable 5 limits and removes a reference to separately purchasing access to the model.

A little later, they noted that Fable is also reappearing on Amazon Bedrock. Ever hopeful, Chubby posted, " This Fable five update sounds almost too good to be true. Including Fable in subscriptions would be fantastic, and I hope it's true insofar as Anthropic generates good PR with [00:05:00] it." Still, a couple of hours later, the headline that likely drove the shift in the market came out with Wired reporting that the Trump administration is, on the one hand, sick of Dario Amodei, but on the other, seemingly more than happy to deal with co-founder and chief compute officer Tom Brown.

According to one White House source With characteristic parhesia, they said, " "Tom Tom Brown is not being a weirdo like Dario and can actually engage." Now, Brown traveled to Washington last Monday to participate in negotiations, and reports state that Dario has now been sidelined from the discussion as talks continue by phone

TR Taxes commented, " "One of the One of the two must stay in the locker, either Fable or Dario. Dario is a weirdo, so Fable gets to walk." Now, aside from that, the reporting was pretty vague on how much progress is being made. It reported that there's still no timeline for reinstating Fable, but said talks are ongoing with leadership and technical teams at the White House.

Sources said a big part of the conversation has shifted to establishing what level of proof Anthropic could provide to alleviate the administration's concerns about the jailbreak I I don't know, man. I guess it's better than bad news But I'm kind of with Rand [00:06:00] Longevity when he writes, " I'm gonna believe Fable is imminently coming back, and I'm ready to get hurt again."



now staying on Anthropic news, in a follow-up to our discussion yesterday of Claude Tag, the release is proving to be a little bit more controversial than I would've guessed



and I think it has to do with a couple of things. First, the response, at least among the highly enfranchised AI community, shows that Anthropic's reputation in the community right now is kind of at a low ebb. Secondly, I think people responded fairly negatively to how much folks from Anthropic were trying to say that this thing is much more than the Slack bot it seems at the surface

Specifically, Andrej Karpathy caught a lotta guff for calling it a new paradigm



in a in a discussion on another post, he said, " I think a number of people on the timeline didn't read past the title and made inferences and comparisons that are just wrong, and then use it as an opportunity to take cheap shots. This is not a, quote-unquote, 'feature' like some crappy Slackbot, and it's certainly not a claw, though it has aspects of it.

It is an org-level harness. The difference will become clearer over time



Now, if Now, if you listened to [00:07:00] yesterday's episode, you will have heard the argument for why this is indeed potentially more than just a Slack bot

But there was another strand of critique which I think is a little bit more interesting, especially in the context of everything else happening in the AI industry

Gopinath of Sentra suggested that Claude Tag will start off as a handy feature, but quickly transform into vendor lock-in. 

now in some ways, this is just a natural byproduct of anything that gets more deeply integrated into organizational context. you might remember when people were concerned about memory as a lock-in when it came to individual accounts.



but those concerns petered away a little bit at least when Labs started to introduce one-click migrations

but what people are recognizing is that it's going to be a lot more difficult to migrate away from something like CloudTag once it's fully embedded in the organization

Summing up this point of view, Mark Agin stat wrote, " "CloudTag CloudTag is turning your company's context into vendor lock-in, and it looks like convenience until you try to cancel

Herbie Herbie Bradley had a lengthy take on the pros and cons that essentially boiled down to a combination of pricing anxiety and a lack of user control



his post [00:08:00] expressed the reality that we don't know a great deal about how expensive it will be to deploy Claude in this way across the organization, but that people's assumption is that it's unlikely to be cheap

Now, I Now, I don't think that these conversations are unreasonable and I think that for anyone who's been starting to flirt with the idea of different model architectures or even using local models, this might be another example of why that could be valuable.

At the same time, I do think a little bit of the concerns that people are sharing are sort of just the inevitable outcome of AI getting more deeply integrated, whether it was Claude or ChatGPT or something else. It is, yes, definitively the case that when you take all sorts of time to give organizational agentic systems access to lots of important context and permissions, it creates a very high barrier to switching But But that's not Anthropic specific and it's not Claude Tag specific.



it is just an unavoidable consequence of AI doing what we hope it will, which is making the organization work better

Capturing the nature of the challenge, Ethan Mollick writes, " Decisions about how to use AI in your organization are increasingly organizational design and strategy decisions, [00:09:00] not IT choices. how do you integrate agents into your firm? What intelligence will you outsource? What are the boundaries of the firm?

What is the role of people?

people? Now, Now, one other interesting story from Anthropic. The company has accused Alibaba of illicitly accessing their models in order to distill Claude's capabilities. In a letter to the Senate Banking Committee, Anthropic has accused Alibaba of, quote, "brazenly and illicitly" carrying out what they describe as the largest distillation attack ever detected.

Anthropic says that Alibaba accessed their models almost twenty-nine million times through a network of twenty-five thousand fraudulent accounts. they say the attack ran from mid-April through to early June before it was shut down. The letter states, " These distillation attacks are carried out illicitly, systematically, and at an industrial scale to harvest US AI capabilities across frontier labs and repackage them as their own without incurring the training and R&D costs required to train US frontier models."

Anthropic warned the senators that models created via distillation often lack safety guardrails, posing broader security risks. The letter also noted previous attacks from the Chinese AI sector, including a major campaign from DeepSeek, which [00:10:00] they publicly disclosed in February.

Anthropic claimed these distillation attacks pose a threat to the US military and broader competition with China, commenting, " "Distillation Distillation attacks turn hundreds of billions of dollars in American investment and R&D into a massive subsidy for our geopolitical competitors." Now, a couple interesting things about this letter.

First of all, Anthropic is clearly ratcheting up the rhetoric when it comes to Chinese model distillation. The attacks that they're discussing are ultimately nothing more than using Claude, recording the outputs, and repurposing them as training data. in other words, they don't degrade Anthropic's product in any way

Distillation does allow the Chinese labs to catch up quickly, but calling them attacks is a deliberate choice in how Anthropic communicates with Washington

Second, Anthropic describes the attacks as illicit, largely because it's unclear that anything actually illegal is going on

In other words, this is a breach of Anthropic's terms of service, but not necessarily the law, although that could change soon. Senators Haggerty and Kim have proposed a bipartisan bill addressing distillation to be included in this year's Defense Authorization Act. If passed, the bill would blacklist or sanction any Chinese lab found to be distilling US [00:11:00] AI models For now, Anthropic seems to be agitating for more action.



now, none of now, none of this is to say that Chinese distillation isn't a big problem. A A post on Hacker News this week discussed a thriving underground economy reselling Anthropic tokens. Formally, both Anthropic and OpenAI block access in China, but informally, there is a huge market for discounted AI tokens farmed from Mac subscriptions.

Commenting on the post, Chubby wrote, " "There may There may be an entire gray market economy around Claude access in China. Resellers allegedly pool Claude Max accounts, operate bot networks, and sell access far below official API prices. The more interesting claim, user logs and reasoning traces may be resold as training data.

If true, this is not just API abuse, but model access arbitrage turning frontier AI usage into a shadow data pipeline."

/

Meanwhile, separately, Alibaba has sued the Department of Defense over a decision to designate them an affiliate of the Chinese military. Earlier this month, the Pentagon updated their list of firms with ties to the Chinese military, adding more than a dozen firms. This includes every Chinese cloud giant alongside [00:12:00] multiple electric vehicle companies, robotics labs, and chip makers.

The designation blocks these firms from doing business with the Pentagon and restricts lobbying activities. Many analysts also view the designation as a precursor to these firms being blocked for civilian use, as occurred with Huawei. in the lawsuit filed on Tuesday, Alibaba claimed they had no affiliation with the Chinese military and that the Pentagon had acted unlawfully in applying the designation.

The lawsuit stated, " The designation thus does not merely impose commercial costs. It strips Alibaba of its ability petition the government through its chosen representatives." Alibaba claimed its relationship with the Chinese government is purely regulatory and no different to any other firm operating in China.

The Chinese government has also spoken out against the expanded list of designated firms In comments earlier this month, the Chinese Ministry of Commerce said the US had, quote, "Disregarded the consensus reached during the recent trade summit."

summit." One One more quick bit of lab news and then a little market news, and then we're out of here



Google continues to bleed talent as two additional senior researchers head for the exits. Last week, DeepMind was rocked by the departure of AI luminary Noam Shazeer and Nobel laureate John Jumper, who joined [00:13:00] OpenAI and Anthropic respectively. On On Wednesday, Bloomberg reported that Jonas Adler and Alexander Pritzel were also leaving to join Anthropic.

The report described Adler and Pritzel as senior researchers who were viewed as key contributors to Gemini. After After scraping social media, Chris GPT found two more Googlers parting ways this week

He argued, Typically, this is Typically, this is a sign when a company is about to release a subpar model. This happened with OpenAI, xAI, and is now happening with Google." While we don't know whether Gemini 3.5 Pro will actually be subpar, we now do have confirmation that it's been delayed.



After speaking with sources, Business Insider reported that the model will not be released this month as planned. Instead, DeepMind is now indeed targeting a July launch, with their sources suggesting that they're using the additional time to tweak the model based on feedback from early testers.

In particular, testers are being asked to stress test the model in real-world coding use cases using anti-gravity.

Now, Now, interestingly, meta researcher Lukas Bayer suggested this might not be just about Google falling behind. He commented, " "One thing One thing I noticed with the big departures lately is that most of them [00:14:00] are longtime Londoners leaving Google DeepMind. This would be consistent with laments I've heard about the center of gravity for pre-training slowly but surely shifting to Mountain View."

Mountain View is, of course, Google's main campus south of San Francisco.

But since DeepMind was founded in London, that's historically been a big locus for them

them perhaps notably, Anthropic opened a major office in London in April with space for eight hundred employees, conveniently just a few miles away from the DeepMind office



Finally, over in markets, it is bubble on, bubble off as blowout earnings from Micron send the markets in the opposite direction. Throughout this week, concerns had been steadily growing that the bull market for AI stocks was coming to a close. The narrative began with SpaceX falling 16% on Monday and accelerated as Cerebras fell below its IPO price for the first time on Wednesday

Even Even well-established hardware stocks were taking a hit as the drawdowns spread. Micron, and Arm all fell more than ten percent on Tuesday and bled lower on Wednesday, dragging the Nasdaq down three point eight percent so far this week Now there are, of course, plenty of external catalysts to explain the plunge, including the on-again, off-again peace deal with Iran and [00:15:00] growing expectations of rate hikes from the Federal Reserve.

But for the AI-centric narrative, analysts seem to believe it's just time for the semi-annual bubble jitters to set in. " Gravity strikes," proclaimed J.P. Morgan analysts in a Tuesday note

Dan Ives of Wedbush wrote, " "With With Micron set to report earnings this Wednesday, there is some added nervousness on the important memory chip trade. In this market, we will continue to go through a number of gut check moments in the tech trade as the AI revolution remains in the third inning. This morning is another one of those moments."

moments." Now, Now, with the stakes established, analysts held their breath on Wednesday night to see if Micron could come through, and the results were much stronger than anyone expected. Micron delivered a beat on top-line revenue and profits, reporting four hundred and forty-five percent year-over-year revenue growth and a seventy-four percent jump from last quarter.

More importantly, Micron hiked forecasts, guiding another twenty-two percent jump in revenue for next quarter. They also disclosed four long-term contracts with what they described as very large customers that lock in current memory prices, which are historically high and deliver fifty-six percent gross margins.

Micron executives said that they expect the memory market to be [00:16:00] undersupplied for at least the next year, forecasting that gross margins will expand to eighty-six percent in Q4. The The market was quick to pivot in overnight trading, 

Setting the stock up 14% in overnight trading, recovering the entire drawdown from this week. Now, for months, the bearish case for memory and storage companies has been their boom and bust track record. Any sign of weakness led to an aggressive sell-off based on the belief that a bust is inevitable The Wall Street Journal noted that even though several semiconductor firms are up 10X over the past year, they're, quote, "Still cheap, trading below 10 times projected earnings over the next 12 months because investors are skeptical that the good times will keep rolling."

This is the narrative that Micron disrupted on Wednesday night. It is now clear that their massive growth surge in Q1 wasn't a one-off. It appears the AI industry is instead driving a structural shift in memory demand, and the suppliers are struggling to keep up

Goldman Sachs seems to have the correct read on the market, warning that consensus forecasts are underestimating the size of the AI buildup by as much as 50%. In a note earlier this month, they wrote, " "The The investment boom is likely to extend, and near-term expectations of its scope may 

still need to rise. But with a lot of value already built in, [00:17:00] markets are more vulnerable to news that challenges an optimistic view.



we'll see what the summer has in store for markets, but for now, that is gonna do it for the headlines. Phew. Like I said, extended headlines today. Next up, the main episode 

One of the most important AI questions right now isn't who's using ai, it's who's using it? Well,

KPMG and the University of Texas at Austin. Just to analyzed 1.4 million real workplace AI interactions and found something surprising. The highest impact users aren't better prompt engineers. They treat AI like a reasoning partner.

They frame problems, guide thinking, iterate, and push for better answers.

The average enterprise is spending eleven and a half million dollars on AI [00:19:00] this year, and most of them can't prove a single dollar came back.

Welcome back to the AI Daily Brief. In In today's episode, we are looking at the latest KPMG Quarterly Pulse Survey. Now, one of the things that's been challenging this year about enterprise data is that there was such a massive shift that happened at the beginning of this year for early adopters kind of between November and January, and then for everyone else starting from January on, that a lot of the surveys that companies have done just really don't reflect the reality anymore.

Now, overly simplifying, it's the shift [00:21:00] from non-agentic to true agentic AI



but everything from the use cases to the patterns of how we interact with it changes so dramatically that I haven't found a lot of studies that I think provide a lot of signal. What's What's useful then about the KPMG study is first, that it is a quarterly repeated survey, so you get a more longitudinal view.

And two, that these survey results

were actually collected in that agentic period. it wasn't back in the before times



and there are some pretty interesting findings in this, so let's dig in

The story is very much of AI on the rise

You see confidence in AI rising You also see where it sits in organizational strategy, increasing who's in charge of it, shifting even higher in the organization

And for the first time, we're starting to see some of the trends that we've been discussing on this show recently, including cost considerations at the frontier start to actually find their way into AI strategy discussions

Let's start on the confidence department



One of the most encouraging things is that the percentage of these senior leader respondents who say that AI is currently [00:22:00] driving meaningful business value at the organization level has jumped 12 points from 64 Now importantly, as we will see, this does not mean that they have perfectly precise ROI metrics

But it is still a powerful indicator Of the reported sensibility among executives about how AI is working at an organizational level



perhaps unsurprisingly then

We also saw a couple of interesting shifts in where on the maturity spectrum organizations self-report

The spectrum that KPMG uses from early stage to mature stage is research and development, experimentation, strategic planning, scaling the technology, driving adoption, and established ROI Now, of Now, of course, one challenge with this is that there is so much variety across different parts of the organization.

And also with AI, there's usually overlapping waves based on the type of technology. So for example, certain types of use cases from the pre-agentic era might be an established ROI, while some of the more advanced agentic uses might now be in experimentation

That's the limits of the self-assessment, but I still [00:23:00] think it's overall an interesting way to see where organizations see themselves. Both research and development and experimentation are down because organizations are moving farther.

The percentage that are in the strategic planning stage has stayed the same. And actually, the number who are in the scaling the technology stage has also gone down a little bit, from twenty-six to twenty-two percent. But that's because by far the biggest jump was seen in the fourth of five stages driving adoption, i.e.

embedding AI across the organization

That jumped nine percentage points from 13% of respondents to 22% of respondents



and and in one of the clearest indications I've seen yet outside, of course, of the AIDB usage pulse surveys which have shown this throughout the year

is that opportunity AI, in other words, strategic opportunity generating use cases for AI is on the rise, while efficiency AI

is proportionally on the decline. so in terms of where organizations' priorities are when it comes to AI, faster, better decisions declined from forty-one to thirty-six percent between Q1 and Q2. Productivity gains declined from [00:24:00] forty-two to thirty-five percent, and cost reduction declined from thirty-one to twenty-nine percent.



Now remember, I don't think any of those things like productivity or cost reduction are meaningless or not important. I just think that they are the amuse-bouche of what you can really get out of AI.

And on the priorities rising side, you have human AI collaboration and fluency going up from twenty-eight to thirty percent. Responsible AI and governance going up from twenty-six to twenty-eight percent. Adaptability and resilience going up to twenty from eighteen percent.

And ecosystem and partnerships going up from twelve to sixteen percent

KPMG sums this up as AI priorities becoming more strategic

Now Now what about the big concerns?

data security privacy, that has remained pretty consistent for a long time as the top concern among these enterprises

But interestingly, you are very, very much starting to see the AI subsidy era ending showing up in the numbers



in terms of organizations that have these different concerns, pressure to demonstrate value jumped from nineteen to twenty-four percent. Limitations on hiring and upskilling jumped from eighteen to twenty-two percent. access to lower cost [00:25:00] LLMs had a big jump from fifteen to twenty-two percent

And I would anticipate, of course, that we're going to see that do nothing but increase in the immediate term. But it's interesting to see that even in this period before we had the most dramatic shifts to usage-based models That cost and that interest in lower cost LLMs is already on the rise

Now, when it comes to leadership of AI, a couple really interesting things. First of all, the percentage who say their CEO actively owns AI asa strategic priority is very high, all the way at 75%.



to me this is a very strong indicator of just how significant of organizations getting the idea that this is not a tool selection problem, but an organizational design challenge. Now what's interesting is that although three-quarters say that their CEO actively owns AI as a priority the actual accountability is somewhat diffuse and distributed, which makes sense given how different AI is going to interact with different parts of the organization.



KPMG found very few organizations that have a single point of accountability for AI-informed decisions. It's usually spread between a CEO or [00:26:00] executive committee, some named C-suite executive

Or other groups like the business unit leader or a centralized AI governance group. However, whatever combination of accountability there is, organizations that had clear accountability were three X more likely to report ROI from their AI. So if you are an enterprise and you are looking for quick wins after you listen to this, making sure that everyone knows who is accountable for what decisions when it comes to AI seems to be a clear indicator of a stronger AI organization

and man

When a CEO is accountable for key parts of AI It massively changes the outcomes. I talked about the established ROI, where the CEO is accountable. 14% of respondents reported seeing established ROI. But when the CEO is less or not accountable, that number dips all the way down to four percent.

When asked whether AI is currently delivering meaningful business value, only twenty-one percent of organizations who had the CEO who wasn't accountable said yes, versus fifty-seven percent where the CEO was accountable. Same with confidence in their organization's ability to future-proof its AI strategy.



[00:27:00] where the CEO wasn't or was less involved, it was only twenty-two percent, whereas when the CEO was accountable, it was sixty percent. So quick win number two. Sorry, CEOs, if you are listening, it is your job, or else your organization is going to have a much tougher time.



We'reWe're also seeing a growing maturity in AI deployments. One example of this is that just about half of the responding organizations had rephased AI deployments when they discovered that costs had outweighed expected value

this to me doesn't threaten the overall trajectory of AI as all these other numbers show. It just shows that organizations aren't just buying hype and dreams, they're actually figuring out what works for them It should be a reminder though, to organizations that even if you feel behind, that does not mean that every AI implementation you're going to do is going to work, and you do need to be comfortable cutting your losses and saying, "Let'srepurpose those funds and time for something else."

Yet there are still some big challenges. Only about one-third of organizations report having full visibility into their AI operating costs and actively monitoring them, which I think is going to be hugely challenging when it comes to this new token efficiency era I would not put this in the [00:28:00] category of quick wins, but if you are looking for strategic ideas coming out of this, if you are in the two-thirds of organizations that don't have that full visibility, I would suggest even before you shift any strategy, creating systems to actually have active monitoring around costs is going to pay dividends in the long run

Right now, about 54% of organizations have a cost review as part of AI approval processes. Fifty-three percent have AI cost monitoring dashboards, and about forty percent have usage or token budgets

Even as someone who is completely convinced that AI is going to change everything, with enough time, all of those numbers will be at one hundred percent



now now one interesting last note

is around the human side of AI scaling

And frankly, this is one area where I really think that these executive surveys can only tell half of the story. One very common thing that we've seen across so many different surveys is that bosses tend to radically overestimate the excitement around AI relative to their employees.

So 71% of these executives report making good progress towards becoming a fully integrated AI human workforce Which [00:29:00] is great, but I'd like to see that number from individual contributors inside those organizations



and while globally significant employee adoption of AI agents rose from 25 to 28% and resistance a little bit to 14%, in the United States there was a big difference, where resistance to agents increased from five to 20%. Now, by next quarter, we'll be able to find out whether that is noise in the data or whether that represents something more significant, but it is certainly something to keep an eye on Ultimately, I think there is a lot to be excited about in this survey.



a lot that reflects what we're seeing more broadly in the trends And a lot that indicates that organizations are starting to think about things in a smarter, more long-term sort of way We will of course report on Q3 when it comes out, but for now, that is gonna do it for today's AI Daily Brief.

Appreciate you listening or watching as always, and until next time, peace 

​ 

[00:30:00]
