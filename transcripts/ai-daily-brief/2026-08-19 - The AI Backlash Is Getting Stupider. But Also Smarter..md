---
podcast: "ai-daily-brief"
podcast_title: "The AI Daily Brief"
title: "The AI Backlash Is Getting Stupider. But Also Smarter."
date: 2026-08-19
url: "https://aidailybrief.ai/e/2026-08-19"
guid: "https://aidailybrief.ai/e/2026-08-19"
host: "Nathaniel Whittemore"
format: "news-analysis"
level: 1
length: "00:29:00"
categories: ["policy", "safety-security", "funding-markets", "infrastructure"]
featured: ["OpenAI", "Anthropic"]
mentioned: ["OpenRouter", "GPT-6", "Gemini", "Hugging Face incident"]
transcript_source: "publisher"
---

# The AI Backlash Is Getting Stupider. But Also Smarter.

Nathaniel Whittemore: [00:00:00] The anti-AI conversation is somehow getting dumber and more productive at the same time. ~This week, a governor who-- This week, a, this week, a centrist governor who formerly touted the, uh... This week, a centrist governor who... This week, a centrist governor who formerly... ~ This week, a centrist governor who just a year ago was touting AI investment in the state reversed course entirely to sign an extremely strong executive order that makes it much harder for data centers to get built in his state

~We also saw a, we also saw, we also saw a commercial go viral. ~We also saw a commercial go viral that features a former NFL star turned podcaster sending his urine to a data center

~But as much as, but as much as the, but as much as these~

~There is no doubt, ~there is no doubt that American animosity towards data centers is at a high and politicians are recognizing it and yet as OpenAI voluntarily pauses their training

And that governor that we were just mentioning before chose an executive order with specific criteria that data center builders could meet instead of a blanket moratorium. I actually think that there's way more positive progress on the horizon than it might seem right now

Nathaniel Whittemore-1: The AI Daily Brief The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI

All right, friends, quick announcements All right, [00:01:00] friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, Rackspace, Blitzy, and Hyperagent

To get an ad-free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts

~To learn more about, and ~ and to learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai

Now, one thing that I wanted to flag coming up next week, if you have listened to any of my recent episodes on graph engineering or loops, ~we have got, we have got a practical, ~we have got a practical webinar and workshop for you

The premise is that your AI can do a lot more than it's probably doing. ~If you set it up, if, if you set it up, if you set it up corre- if you set it up to, ~if you set it up for success, it can work until the job is done

~In this session, we're gonna take-- ~In this session, we're going to take the sort of agentic loops ~that developer, ~that developers and software engineers are already using and make them applicable for knowledge workers of all stripes

The first 60 minutes will be a live session led by Nufar Gaspar

that explains loops, shows a real loop live in action, explains graph engineering, and has time for Q&A. mi- and then in the next 30 minutes

We'll have a hands-on lab where you can design a loop for your own work

This is completely free and [00:02:00] happening next Wednesday, August 26th at 2:00 PM Eastern. And if you register and can't make it, we will send you the recording as well. ~All the information will be on AI... ~ All the information will be on aidailybrief.ai

And I'll see you next Wednesday 

Nathaniel Whittemore: Welcome back to the We kick off today with a story

~that really got my goat yesterday. ~ That really got my goat yesterday, but is relevant even if I disagree with the tone of the reporting, because of how it's being received on Wall Street. The TLDR is that the two major AI labs, OpenAI and Anthropic, of course, are facing increased scrutiny ~after their-- after reports of revenue this week~

After reports around their revenue this week

OpenAI recently told investors ~that they'd surpassed 40 billion in annualized revenue-- That they'd surpassed a $40 billion-- That they'd surpassed a 40 bill-- ~That they'd surpassed a $40 billion annualized revenue run rate, while Anthropic told investors they had reached 65 billion

Both numbers seemed pretty positive at first Showing that revenue was still growing quite strongly despite a summer slowdown

However, capturing the zeitgeist of the pre-IPO period, whereas many folks are looking for reasons to not be enthusiastic ~as they are to, as they are to, as they are to, as they are to, ~ as they are to pump the numbers

The skeptics think that they've found some weaknesses underneath. On the OpenAI side, ~The Wall Street Journal reports ~ The Wall Street Journal dropped a piece called "OpenAI's second~ quarter sales sh- second~ [00:03:00] quarter sales show tepid growth compared with Anthropic."

OpenAI had told investors they saw 18% revenue growth across the entire second quarter to reach six point seven billion in revenue. However, citing sources familiar with the matter, the Journal wrote, " Its operating margins ~sank further, ~sank further into the red, pushing the company farther away from profitability ahead of a much-anticipated initial public offering."

~So, ~ so that is factually accurate. So where's my beef?

~Well, you might n-- well, you being the smart, ~ well, you being a smart individual who decided to turn on this show today ~might notice that it i- might notice that it is, might notice that it is, might notice that it is we- might notice that it is, ~ might notice that we're ~pretty deep in Au- that we're~ pretty deep into August right now, ~ and that the second quarter ended in,~ in, and that the second quarter ended at the end of June

If we are trying to understand a momentum story Is it perhaps worth asking what has happened in the subsequent seven weeks since the quarter ended? ~Especially in the conte- ~especially in the context of an industry which moves as fast as AI does

~What the Journal says, what the Journal says about, ~what the Journal says about that is the one line, " OpenAI has told investors that its growth rate has picked up since the launch of a set of new models in July, the people said."

~But that kind of makes it, but that kind of makes it... But not only does that, but not, ~ but but not only does that minimize ~that this entire period has been, that this entire period has been after, ~ that this entire new period has been subsequent to the release of a frontier model But it also suggests that our only [00:04:00] sources for this information are the same anonymous sources that they had for the rest of it.

it. But that's not true

~OpenAI executives, ~ OpenAI executives have been sharing precise numbers

~CFO Sarah Friar has been run-- ~ CFO Sarah Friar has been running around giving precise details. ~And Greg Brockman, and, and Greg Brockman on Squ-~

~And Greg Brockman on CNBC told~

And And Greg Brockman on CNBC told Andrew Sorkin That July revenue had grown 20% month over month

Not including those very out in the open details

~only serves to reinforce a nar- ~ only serves to reinforce a narrative

~ If you ever wonder why people are get ~it, if you ever wonder why people have trust issues when it comes to mainstream media, it's crap like this

~ But even if, b- ~ but however you feel about my beef with that, ~it is telling that the, it is telling that the Wall Street... ~ It is telling that the Wall Street Journal is finding resonance with increased scrutiny around these companies' reported numbers. ~ That is an im- that is an important signal, uh, ~ that is an important signal in terms of understanding where the market is heading into this pre-IPO period

Anthropic, however, in this case has not been spared scrutiny either. ~Semi Analysis CEO Dylan, ~ Semi Analysis CEO Dylan Patel took a pretty big swipe at Anthropic's preferred accounting methods, posting, " Wow, have y'all seen Anthropic ARR? As measured by the last one hour at two PM [00:05:00] times eight thousand seven hundred and sixty."

The joke is, of course, that Anthropic doesn't~ measure it doesn't~ measure revenue in a way that would pass muster in public markets

They take the past four weeks of API revenue and extrapolate that out to a full year

And whether you agree or not, that leads to an inflated figure. At the very least, it's not recurring revenue by the nature of~ of being sold on demand, by the nature~ being sold on demand through the API. Now, Now, the deeper take came from the main Semi Analysis account, which posted, " Anthropic crossed 40% of ARR from indirect channels like Bedrock, Foundry, and Gemini~ and Gemini Enter- ~Agent Enterprise in the second quarter of '26, with API and B2B making up the vast majority of net new ARR dollars at the labs.

~The mix, ~ the mix shift matters because indirect revenue isn't monetized the same way direct is." ~SemiAnalysis, ~ SemiAnalysis went on to explain that hyperscalers take a cut, but Anthropic counts their revenue ~before removing their cut, ~before removing that cut, which can make their numbers look a lot better than their competitors Again, hold aside the details.

The takeaway is that scrutiny is ramping up on two of the largest and strongest companies that Wall Street has ever seen

No one has experience pricing companies that are growing revenue at [00:06:00] twenty percent a month after ramping from single-digit billions to tens of billions in a year's time As the IPO comes nearer, expect the noise to increase as analysts figure out how ~to think about these, how to, how~ to even wrap their heads around these businesses

You You can also expect a lot more novel business model-based approaches to competition. For example, OpenAI is discounting tokens to win a bigger share of the developer market. On Monday, OpenAI announced that GPT 5.6 sole tokens would be half price on OpenRouter and Vercel's Gateway. OpenAI had already applied the same discount to the smaller Luna and Terra variants in recent weeks.

The discount increases OpenAI's ability to compete with cheaper Chinese models and also positions their models ~as a better cost efficiency choice ag- ~as a better cost efficiency choice against models from Anthropic This is particularly important on Open Router and Vercel Gateway as a lot of users simply allow the router to make that choice automatically.

~The discounting already is-- ~ The The discounting is already paying dividends ~with use of~

~With use of With use of L- ~ with use of Luna skyrocketing over the past month

It's now the top used closed model on the platform, seeing 40% more use than Opus 5 and Sonnet 5 combined

And sixth overall [00:07:00] even ~including, and sixth overall ~including the open models

~Now, AI bears will-- now, ~ now AI bears might warn that this discounting is the beginning of a price war that obviously leads to the AI bubble popping. But OpenRouter isn't necessarily a great place to look for evidence that a price war is actually breaking out. Despite its rise in its big sale to Stripe, OpenRouter is a vanishingly small portion of overall token usage, meaning that OpenAI can discount pretty heavily on OpenRouter without materially impacting the business

In fact, SemiAnalysis once again believes that this is actually a canny marketing ploy due to how the media reports Open Router metrics. They wrote, ~"Despite being, ~ despite despite being a very small portion of OpenAI's total token volumes, Open Router and Vercel are disproportionately impactful ~because they are, ~because they are two of the main data sources everyone uses to estimate AI lab and model market share."

If the 50% price cut ~is able to move-- is able to, ~is able to more than two X token volumes for Five Six Soul over the next month, many investors will likely naively view it as a big win for OpenAI versus Anthropic

~Now staying on the theme, now staying on the theme of, now staying on the theme of chain, now staying on the theme of chain, ~ now now staying on the theme of the pre-IPO period, The Information reports that Anthropic ~is preparing a, ~is preparing a [00:08:00] governance overhaul to give Dario Amodei greater control over the company ahead of the IPO

The TLDR is that Anthropic is preparing to grant super voting shares to Amodei and the other co-founders

~Amodai currently owns around 2% of the company, with other co-founders holding similar stakes. Now, this stat alone was pretty... ~ Now~ Now this, now this,~ now this stat alone had a lot of people's gobs smacked

And I thought Pom summed it up pretty well when he wrote, " I don't know what is crazier, Dario only owning 2% of Anthropic or 2% of Anthropic being worth about $20 billion."

Coming back to the substance at hand, ~despite their-- ~despite the founders' roughly 15% ownership as a collective, the super voting shares would allow them ~to veto shareholder votes, ~to veto shareholder votes and control appointments to the board

Now, to be clear, using special classes of shares to allow founders to keep control of their company has become relatively common in the tech industry

Google co-founders Larry Page and Sergey Brin are credited with pioneering the approach in Silicon Valley ahead of Google's 2004 IPO. Mark Zuckerberg then followed prior to Facebook's in 2012, and more recently, we saw Elon Musk take this approach with SpaceX

~There are also a number of other governance measures within-- There are also a number of other governance measures within which Anthropic is putting into place to again create some checks and balances~

~Actually, let's kill that line~

~However, even if, ~ however, even if these sort of founder shares have become increasingly common, ~it's not hard to under-- ~ it's not hard to understand why some people are having [00:09:00] a different reaction to Anthropic taking that approach than to these other companies

This is a company which, using their own framing, is attempting to build AI systems so powerful they could have a major impact on the trajectory of society

So powerful, in fact, ~where reports say that Amud-- ~where reports say that their founder believes That they could be the only private company left in the world after out-competing everyone else

~That's a scenario where, that's a scenario, that's a scenario where, that's a n- ~n- that's a scenario where me thinks ~people are gonna want, ~ people are gonna want shareholders and the public at large to have more rather than less control ~over what happens, over what, over what happens in the, ~over the decisions that they make

Lastly today, an interesting~ little, an interesting little one that tell-- an interesting~ little story that tells us a bit about how ~companies are prioritizing, about how~ companies are valuing unique data. Google has won a bidding war against AI data labeling service Mercor ~for the corporate data, ~for the corporate data from Spirit Airlines.

The data went under the hammer last week in a bankruptcy auction, ~and Google submitted the winning, ~and Google submitted the winning bid at~ at 10 billion, ~at $10 million, beating Mercor ~at seven, ~at 7.5 million What we're seeing is the third big data push of the AI era. First, we saw the AI labs scraping every page of the internet and uploading every available book to train their models on writing and general knowledge.

Then the rise of coding agents saw AI labs buying out the code bases of failed startups to build. ~Now the AI, ~now [00:10:00] the AI labs are paying up for corporate data to help train their agents to do white collar work. In this case, Google isn't buying customer information or payment records to build a better AI travel product, as that data is excluded from the sale.

They're purely interested in mundane internal communications data like email, Slack messages, and meeting transcripts. The goal is to use this data to help agents understand how corporations function.

Commenting on the bidding war, Murkor said, ~"Companies are sitting on decades of records that show how real work gets done."~

Companies are sitting on decades of records that show how real work gets done

There's There's a surprising amount of interest in this deal, ~in particular for the possibilities, in the particular, ~ in particular for the possibilities of other data sources that it opens up. Although there's also a lot of skepticism that it's going to actually be valuable

~Maybe the most, maybe, maybe the most common take comes from Sheekadelic who wrote it, comes from-- Maybe the most common type of take came Maybe the most common take was, maybe the most common take, ~ maybe maybe the most common take was exemplified by SheikahDelic who wrote, " Really? We wanna train models to be like Spirit?"

For now, however, that is gonna do it for today's headlines. Next up, the main episode ~ ~

Nathaniel Whittemore: One of the more interesting shifts in enterprise AI right now is how quickly the conversation is moving towards infrastructure and operations. As AI moves into core workflows, regulated data environments, and agentic systems, ~enterprises need g- ~ enterprises need governed infrastructure and inference that can operate reliably day to day with clear operational accountability built in from the start.

As those systems scale, the operating model increasingly becomes part of the AI strategy itself

Nathaniel Whittemore: Welcome back to the AI Daily Brief. Welcome back to the AI Daily Brief.

Today we are talking about an [00:14:00] interesting paradox In short, the anti-AI backlash as embodied specifically in the anti-data center backlash is fairly undeniably getting dumber. ~Or at least, ~ or or at least more meme-driven and more performative But at the same time

~Some of the latest, some of the latest moves ~ Some of the latest shifts do suggest That going forward, there may be a bit more room for understanding and collaboration than there has been up till now. So how can these two things be true at the same time?

~ Let's Let's first look at... Well, let's, ~ well, to understand, we have to start by looking at the performative and meme side of things

~Yesterday, this new TV... Yesterday, this new commercial. Yesterday, this new Liquid Death commercial. ~ Yesterday, this new Liquid Death commercial featuring Jason Kelce, a former NFL star and one half of the New Heights podcast ~with, ~with his brother, Mr. Taylor Swift

~Released with the theme, with the, ~released with the theme of mailing urine to data centers

Liquid Death is of course known for their provocative ad campaigns

~And so something like this isn't all that surprising. ~ And so something like this isn't all that surprising from them

~What's notable, what's notable, what's notable is that, what's notable is that, what's notable is that, ~ what's notable is that the advertisers

read the sentiment in the room

~And came to the conclusion that, ~and came to the conclusion that an ad about literally mailing urine to data centers would be [00:15:00] popular

Wired's Max Eff summed it up perfectly. " Unfortunately for the tech industry, hating data centers is now so popular that companies think it will help them sell beer and water."

Perhaps they were inspired by comedian Charlie Berens who called opposition to data centers the most bipartisan issue since beer

~Now, of course, it is not just, ~just, now of course it is not just internet memes where this opposition to data centers and AI and tech more broadly is showing up

Georgia Senator Jon Ossoff, who is currently running for re-election and who is increasingly being discussed in Democratic circles as an Obama-esque uniter candidate for the 2028 presidency ~has made opposition, has made opposition, has made opposition, ~has made opposition to tech one of his central platforms

In a recent ad, he said, " "When When you step back and consider it, the situation is absurd. Tech titans dig bunkers and warn us the new intelligence they're training could lead to mass joblessness or human extinction, while our Congress debates ballrooms and youth sports."

But yes, Dario

~Your constant badgering about, ~ your constant badgering about the number of jobs that could be lost by AI ~definitely wasn't, ~definitely isn't impacting the narrative at all

~And lest you think, ~ think, and lest you think this is just a [00:16:00] left-right easy partisan divide issue

In the race for Wisconsin governor, Republican candidate Tom Tiffany has dropped an ad labeling his,~ his, his~ opponent David Crowley as Data Center David Crowley

~As though this were, ~ as though it were swearing on national TV or something

He posted on X a video clip of David Crowley saying, " " There's an opportunity for us ~to be--~ to really become AI and a data hub, not only for the entire country, but for the entire globe."

But that's not the big news that captured everyone's attention yesterday

~Pennsylvania Governor, ~ Pennsylvania Governor Josh Shapiro

~is another one, is another, ~ is another person who's frequently mentioned in Democratic circles as a contender for the 2028 candidacy

~relative to the emerging wave of democr-~

~Relative to the emerging wave of democratic socialists for~

Relative to the emerging wave of Democratic socialists of America, ~Shapiro is Shapiro, ~ Shapiro is moderate and a centrist

~Just 14 months ago, ~just 14 months ago, Shapiro was proudly announcing plans for Amazon to invest 20 billion into Pennsylvania as part of a large AI infrastructure build-out

And so people took notice when yesterday

He not only signed an executive order around AI data centers, but took an extraordinarily aggressive tone in publicizing that order He tweeted, " Effective [00:17:00] immediately, I'm putting AI data center developers on notice. If they want to even think about doing business in Pennsylvania, they must adhere to the strictest standards in the nation and get approval from the local community.

Pennsylvanians deserve the right to say no to unwanted AI data center projects and block developers who are trying to bully their way into our neighborhoods without addressing neighbors' concerns."

Journalist Scott McFarlane wrote, " Governor Josh Shapiro used the following words to describe data center developers today: predators, bullies, secretive."

In another tweet, he said, " I will not allow Pennsylvanians to be bullied by greedy developers and bulldozed by the lawyers working for these big tech companies."

I'm putting these developers on notice and letting them know that they will not bully Pennsylvanians, disregard our constitutional right to clean air and pure water, and drive up our utility bills. I'm using the full weight of my executive authority to block the objectionable, unwarranted projects and put the nation's strictest set of protections in place

~Now among the tech forward members of-- ~ now among the tech forward community of a place like X, ~there were plenty of people to point out, there were plenty of people to point out, there were plenty of people to point out~

~ ~ There were plenty of people lamenting this turn~ from,~ from Governor Shapiro

RSI Innovation Policy Analyst Adam Terier writes, " [00:18:00] What is this nonsense on data centers from Governor Josh Shapiro about being bullied by greedy developers? Nobody is being bullied into building data centers in their states or communities. They decide willingly if they are going to bring those investments and economic and job opportunities into their states and communities."

In fact, just last August, while proudly announcing major new AI-related investments in the state, ~including twenty billion from Amazon for major data center... including twenty billion for A- from Amazon for major data center pro- ~ including twenty billion from Amazon for major data center projects, Governor Shapiro boasted of how his administration was, quote, " Creating thousands of good-paying jobs, generating new revenue for our local communities, and making it easier for companies to build and grow in Pennsylvania."

He said it was about, quote, "Ensuring the future of AI and innovation runs through the Commonwealth." So was the governor being bullied by greedy developers then? Or instead just wisely welcoming much needed investments into the future of his state?

Sad to see the otherwise level-headed Governor Shapiro adopt such outlandish rhetoric. I thought he was the clear leader of the abundance Democrats, ~but this is just more of the old business bash-- ~but this is just more of the old business-bashing Dem playbook

playbook Investor Shio Mona points out

~That Shapiro, ~ that Shapiro is getting pressure on the left and the right on this policy. He said, " [00:19:00] said, He has a Republican opponent for governor who is anti-data center. She suggested a total pause in Pennsylvania

And voters are pretty anti data center right now, both on the right and left

~Adding something that we'll come back to in a moment, ~ adding something we'll come back to in a moment, ~Sheil als- ~Sheil also said, " From what I can tell, his words are stronger than what the actual text of the executive order says, so he is playing to the polling."

~And while there were some moderate and centrist, and while there were some moderate and centrist, and while there were some moderates and cent, ~ and while there were some moderate liberal and centrist groups lamenting this~ lamenting this shift, lamenting~ shift

This is absolutely an indicator of where~ the political winds are, of where the political winds are, of where~ the political winds are blowing

Just a few hours before recording, Axios released a piece called GOP Issues Stark Warning to AI Companies

~In a memo, ~ in a memo that was obtained by Axios, the National Republican Senatorial Committee

~warned that the, ~warned that toxic voter views of US data centers ~are threatening the, ~ are threatening Republicans' chances of ~ a seat, of holding~ holding one of their seats in Ohio Currently held by Senator John Husted

The memo says, " If he loses and data centers get the blame, politicians across the country will take notice, and they will not go near the next one. This has become a sleeper issue for the entire election cycle."

~ Making that point and making that-- and putting a fine point, and putting a-- ~ and making that point pretty crisply, if shockingly, is the fact that recent polls have [00:20:00] consistently showed ~ community-- ~ individual voters having more opposition ~to having, to having a, to having an AI data center, to having an AI data center, ~to having an AI data center in their community than to having a nuclear power plant

~And making the po - ~ and and making the point that this is indeed at least partially about AI

~That poll actually, that poll actually asked, that poll actually, that poll actually, that poll actually, ~ that that poll that I was mentioning actually asked about data centers twice

When asked if they would support a data center to power digital services like online search and video streaming 35% said that they would support As opposed to 53% who said that they would oppose. ~Whereas when the data cen- ~ whereas when the question was a data center to power artificial intelligence, just 27% said that they would support and 62% ~said that they would suppo- ~said that they would oppose

That's compared to, by the way, ~thirty-four percent of-- thirty-four, ~thirty-four percent support and fifty-seven percent opposition for a nuclear power plant

Historian Aaron Astor writes, " I've been trying to say this for months now. The argument about data centers is only partly about the environmental, ~ec-~ energy, or economic effect of data centers. It's also about AI and whether people embrace it or not. A lot of people don't see AI as progress at all."

~So certainly a lot to be concerned, ~so certainly a lot to be concerned about

But how then, outside of the need [00:21:00] for an interesting and contrarian title

~Could I also suggest that there, ~could I also suggest that things are simultaneously getting better?

~Well, first let's, ~ well, first let's think about the critique of AI companies ~that they're behaving, ~ that they're behaving irresponsibly

~With that background, with that background, many were interested to~

With that background, OpenAI yesterday announced ~that they were actually pausing, ~ that they were actually pausing certain types of training Voluntarily. Sam Altman tweeted, " We've paused some frontier RL training to ensure that we can meet the appropriate alignment, security, and monitoring standards for the new levels of capabilities in front of us.

Model progress is now extremely rapid, and we always said we would take action if we felt that model capabilities were outstripping the pace of safety and alignment. We care very deeply about AI safety. We believe the entire field will have to coordinate on shared safety standards, but we'll act unilaterally in the meantime."

We expect confidence in safety to increasingly set the pace of AI progress. We're optimistic about the alignment work we are doing, and we remain committed to making frontier capabilities widely available

OpenAI's lead scientist, Jakub Pachocki, added, " We temporarily slowed some frontier training to strengthen security and monitoring. Our [00:22:00] largest planned frontier RL run remains on hold ~while smaller scare train-- ~while smaller scale training and evaluations help us test safeguards and gather more evidence of alignment."

I expect confidence and safety to increasingly set the pace of AI development. We urgently need tools for labs and countries to coordinate on this, which is why I signed Pacing the Frontier. In the meantime, we're taking practical steps ourselves, and we'll continue to share what we learn as our approach evolves

evolves Now Now as to specifics, OpenAI points to two developments that led them to this decision. ~The first is, of course, O- ~ the first is, of course, the OpenAI Hugging Face incident

where an unreleased model escaped containment and actually hacked into Hugging Face, going undetected for some amount of time

And also they write, "Preliminary evidence that one of our upcoming models, Astra, ~may meet the critical cybersecurity, ~ may meet the critical cybersecurity capability threshold under their preparedness framework."

~So this, so the pause, so the RL, so the, so the reinforcement, so the pause in RL, ~ Now, during this two-week pause period, one of the things that they're talking about doing ~is expanding, ~is expanding their ability to monitor AI

They They are significantly expanding how they are~ are monitoring, how they are monitoring, how they~ monitoring the training and testing process

~Saying that they're actually spending about 20-- saying that they're a- saying that they're going to a- ~ saying that they anticipate spending about 20% of inference compute ~on this sort of monitor, ~on this sort of monitoring

~Now some jumped in to suggest, ~ now some jumped in to [00:23:00] cynically suggest

~That this was just an ex- that this was just an excuse, ~ that that this was just an excuse as the company~ runs into compute, as the company~ runs into compute shortages

~But all the, ~ but all the indications that I can see suggest that this is indeed about an understanding ~that something has, ~ that something has shifted, not only in terms of capability, but in terms of public awareness

Wyatt Walls wrote, " I've been doing a lot of AI governance work for enterprise lately. Hugging Face incident has broken through to normies. Many non-technical people like execs, directors, and lawyers ~don't understand why, ~don't don't understand why some agents are much riskier ~ to,~ than others."

If your model is known for hacking, that means more agentic AI projects in the enterprise get held up ~over risks and-- ~over risk concerns, and more likely people will choose a different, quote-unquote, "safer model," which is bad for your enterprise business. Your AI escaping its sandbox is not a selling point with CIOs and IT security

~Now, in terms of how this will impact-- ~ now, in terms now, in terms of how this will impact all of us

~Sam Altman clarifi- Sam Altman clarified~ that the company, quote, "Still expects to ship great new models soon," ~and that this change, ~ and that this change, quote, "Impacts further out releases."

Prinz added, " OpenAI has been testing an internal model that has never~ been publicly released since-- that has never~ been publicly released since at least early May. In contrast, Astra's potential designation [00:24:00] as critical for cyber was announced less than two weeks ago, which implies that Astra has been subject to testing accounting for the two-week pause in July and August.

This would seem to suggest that these two models are different models."

In line with this theory, Sam Altman's post below promises that great new models will be shipped soon. This is in contrast to Astro, which would be a further out release. Fingers crossed

~For the sake of our conversation about, for the sake of our conversation about, about the potential for a better, for about, for a... In the, now ~ now in the context of our conversation ~about, ~about the potential for a ~better AI dialogue For a better discourse about AI-- for a~ better discourse about AI's risks

I think Arena's Peter Gosta makes a good point when he writes, " This is why the original pause AI for six months never made sense. ~Just arbit- ~ just pausing arbitrarily when 20 people will have 20 opinions on what the problems are is completely pointless

Now everyone is clear what the issue is. Pause and solve it. Much more productive

Fascinatingly

Nathaniel Whittemore: One of the arch-accelerationist figures of the accelerationist movement, Beth Jasos

Retweeted Greg Brockman's announcement about this pause and said, " said, I've got mixed feelings about this. I do agree all cyber systems need to be hardened given the recent jump in capabilities. ~I don't like this pausing p- I don't like this pa- I don't like the posit- ~ I don't like this pausing precedent this sets.

At the same [00:25:00] time, companies will find the right balance of risk and reward as long as competition is healthy Now to give you a sense of just how nuanced that is coming from Beth specifically Another tweet from around the same time period ~was him re-sharing, ~ was him re-sharing Governor Josh Shapiro's announcement Adding the note, " D-cells are traitors serving the interests of China."

China."~ But let's come back to, ~to, but let's come back to Shapiro's actual announcement

~Former Obama and Biden appointee Dave Borland tweeted, former Obama and, ~ former Obama and Biden appointee posted, " This is one where it is worth reading beyond the headline. While it restricts data center development, the restrictions themselves make a lot of sense. This is way better than the non-solution of a moratorium."

~So among the req-- so~

~So among the requirements, ~ so The Philadelphia Inquirer ~shared some of the, the Philadelphia Inquirer share, the Philadelphia Inquirer shared some of the, shared some of the, shared some of the con, ~shared some of the details of the executive order, including requiring data center projects to sign legally binding agreements to certain transparency and environmental requirements in grid, such water conservation standards and early and transparent public notification of proposed projects ahead of key local approvals.

Prohibiting any state agency from signing a non-disclosure agreement related to a data center project. Instructing the Department of Environmental Protection to publish a [00:26:00] publicly accessible map of current permitting information for all proposed data center projects. Mandating that the projects bring their own electricity generation and pay all costs associated with increased energy usage, and requiring a community benefit agreement that includes promises to hire and train local employees and developer investments in schools or infrastructure

Now, I don't wanna be dismissive of the devil in the details. Even these~ provis- these~ provisions could absolutely have been written in a way ~that is a, that it is an effective ban, that is an, ~ that it is an effective ban even if it pretends not to be. However, just from a principle standpoint, ~ anyone who's heard me rant about data centers, ~ anyone who's heard me rant about what I think data center builders should be providing to the community, will have heard some version of basically all of these things coming from my mouth at various points.

Mandating that the projects bring their own electricity generation and pay all costs associated with increased energy usage, ~that's just the Trump data center-- That's just the Trump, ~ that's just the Trump pledge that he had everyone agree to earlier this year. ~ Certainly nothing... Shouldn't, ~ shouldn't really be anything controversial about that

The community benefit agreement, including promises to hire and train local employees, as well as investments in schools and infrastructure ~This is what some are finally getting needs... ~ This This is what you're starting to see from companies like Meta who are going hard on this point

When it comes to [00:27:00] environmental standards and transparency around them

~One of the, one of the problematic me-- one of the, one of the problematic memes for data centers, ~ one of the problematic memes for data centers

~is factually inaccurate assessment, ~ is factually inaccurate arguments about their environmental impact

So while this is the area where I believe ~has the most room to write effecti- has the most room to, ~ has the most room to turn into effective bans depending on how the rules are written

~Nothing could be, nothing, in principle, ~nothing could be better for combating those memes than actually meeting strict requirements imposed

by local government. ~And lastly, we get to, and lastly we get to what I think is going to be-- ~And lastly we get to what I think is one of the most important pieces of this, the prohibition against NDAs

In Jasmine Sun's recent reporting about data centers, ~the thing that came out most strongly-- ~ One One of the things that came out most strongly

~was not just a, ~ was not just blanket opposition to AI

But a feeling that people didn't have agency~ in their in their own lives as,~ in their own lives as the world changed around them ~NDAs become a l- ~ NDAs become a totem and living embodiment of that lack of agency and control

They are a tool for denying people access to the information they need to make up their minds about something that is ~going to im- ~going to affect them

~I don't care if it makes, ~ I don't care if it makes it harder to do business now

The only way to start building trust back

~is to have these conversations, ~ is to have all of these conversations and dealings happen out in the [00:28:00] open with full transparency

~So am I happy, ~so am I happy that Governor Shapiro

~Is using these trope, is using these trope words, is using these, ~is using these populist trope words like bully and greedy. No, I am not. Not only because of a disappointment in Shapiro, who I don't really have feelings about one way or another, ~but more because he's just, but more because it just reflects, but more just bec- but more because he's a good politician and it, but more because he's a pol- but more because he's a good politician, ~ but more because he's good at being a politician and it reflects the signals that he's getting

~But do I think there is more... But do I think there i- But do I think that there is more r- ~ But do I think that there is more room for positive progress In the context of even a very strict EO like this one, as opposed to a blanket moratorium, absolutely without question. ~ I will take any set of rules, ~ I will take any set of rules that can be debated and interacted with a hundred times out of a hundred out of a blanket ban

My personal opinion is that moratoriums ~are an increasingly popul- ~are an increasingly popular political tool ~ Because they are a blunt instrument~

~ Because people feel that, because,~ because of how blunt an instrument they are. ~If people are ultimately, if people are ultimately scared of change ~ If people's fears come back to, in some way or another, a fear of change or a feeling of a lack of control of change

There is no more direct action

Then saying that change isn't allowed to happen, which is what a moratorium does

But as emotionally satisfying as that might be for people who~ who are feeling, who are feeling the sting,~ are feeling the challenge of change, that [00:29:00] does not make it a good policy

I don't wanna be overly optimistic here

~And unfortunately, I think the Jason Kelce ad has... ~ And unfortunately, I think the Jason Kelce ad says more about where the average person is ~ than the nu-~ than the nuance between a moratorium and what Josh Shapiro gave us

But practically speaking In Shapiro's non-moratorium executive order

~I see this, ~ I see the thin thread of an opportunity, and you better believe I'm gonna grab it. For now, that's gonna do it for today's AI Daily Brief. Appreciate you listening or watching as always, and until next time, peace 

​ 

Nathaniel Whittemore's audio recording: ~Quick note before we get into today. A ~
