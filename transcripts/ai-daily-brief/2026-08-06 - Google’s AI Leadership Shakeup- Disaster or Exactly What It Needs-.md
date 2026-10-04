# Google’s AI Leadership Shakeup: Disaster or Exactly What It Needs? — Transcript (2026-08-06)

https://aidailybrief.ai/e/2026-08-06 · Listen: https://pod.link/1680633614

<!-- metadata -->
Format: news-analysis · Level: 2 · Length: ~00:33:00
Host: Nathaniel Whittemore
Categories: models, agents, coding, funding-markets
Featured: Google, Meta, Google DeepMind, Gemini, Muse Spark, agent harness
Also mentioned: Kimi, ChatGPT, Claude Opus, distillation, Figma, Claude Fable, Grok, GLM, Qwen
<!-- /metadata -->

---

260806 in_EDIT: [00:00:00] Today on Today on the AI Daily Brief, A massive AI leadership shakeup at Google. And before that in the headlines, Meta drops two new models and a coding harness. The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI. All right, friends, quick announcements before we dive in.

First of all, thank you to today's sponsors, KPMG, Rackspace, Blitzy, and Hyperagent. To get an ad-free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts. And if you wanna learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai. 

Meta continues its comeback kid quest with the release of Muse Spark 1.2 and Muse Code

260806 hed_EDIT: Alongside the twin model release, they are releasing their first coding harness as well. 

Meta described Muse Spark 1.2 as a coding-focused update to the 1.1 version, which was released in July. This is the first model that Meta has trained in a harness, improving its agenda capabilities in that environment



Nathaniel Whittemore: 

260806 hed_EDIT: the results look like a pretty strong [00:01:00] coding model on the benchmarks. It scored 82.9% on Terminal Bench 2.1, placing it between Opus 5 and GPT 56 Tera. On DeepSUI, it scored 59.3%, placing it behind Opus 5 and GPT 56 Tera, trailing by around five points. Meta chose not to compare Muse Spark to the frontier models likely because it's not in the same size class as Fable 5 or GPT 56 Sol



260806 hed_EDIT: and the model appears to be designed to be cheap and efficient as a daily driver rather than taking on the larger models on the benchmarks Artificial analysis had similar findings.

The model scored fifty-four on the AI intelligence index placing it behind Opus 5, GPT 56 Tera, and Kimi K3, tying it with Grok 4.5 and putting it a few points ahead of GLM 5.2. AA also wrote that Spark 1.2 is, quote, " " Among the most cost-efficient models at its intelligence level." It cost 40 cents per task on their benchmark run, which gave it a similar cost to intelligence ratio as Grok 4.5 and GPT 5.6 Sol turned down to medium effort settings.

Its run was around half the cost of Kimi K3, further reinforcing the idea that every [00:02:00] Chinese model is not just some incredibly low-cost wonder



260806 hed_EDIT: Muse Spark 1.2's run on the AA index was around half the cost of KimiK3 with results in the same ballpark AA also noted that the three-point overall improvement



260806 hed_EDIT: was almost entirely down to agentic performance. The update delivered a big jump on GDPVal, making it the sixth highest ranked model behind Opus five, Fable five, Qwen 3.8 Max, GPT-5 6-Sol, and Kimi On the harness side, the biggest thing besides Meta actually bringing a coding harness to market is sub-agents. In his launch thread, once again on Twitter, where Mark Zuckerberg has been spending a lot more time recently, Zuckerberg wrote, " " Muse Code runs specialized background agents that stay active your whole session, so they build up context over time instead of starting from scratch on every task.

When a job is big enough, it fans out to separate sub-agents working in parallel in isolated work trees. Your working copy is never touched. In testing, we had it build six features for a game simultaneously with no collisions."

Meta saw very strong performance for long horizon tasks with this architecture. During testing, they deployed the model [00:03:00] to a kernel optimization task, and the model successfully ran for 24 hours, executing more than 1,000 tool calls and delivering steady improvements throughout the session

Meta is also selling Muse Code as suitable for professional work due to its auditability. The harness logs every tool call and code edit and has the ability to use these logs to restart midway through a task if it crashes

Now, aside from the release, Zuckerberg also teased parts of the future roadmap. He wrote that larger and more capable models are on the way as well as hinting that Muse code might be open sourced

sourced now now so far, if you dig around, you can find both positive and negative responses

I would say overall, the steady drumbeat of each sequential release getting a little bit better for Meta and them getting closer and closer to relevant again, continues with this set of releases

Teasing what will be the subject of our main episode, Hader wrote, " How quickly the tables have turned. Meta is starting to look like Google, moving fast, shipping AI products, and finally building momentum. Meanwhile, mighty Google suddenly looks like last year's Meta, confused, reactive, and somehow watching everyone else move faster."

faster." Now, Now, this was not the only Meta story in the news. Not to be left [00:04:00] out of the current trend, Meta's agents have also escaped containment and hacked into third-party systems. Meta said that during cybersecurity testing for Mu Spark 1.1, the model left its sandbox and exploited a vulnerability to break into systems owned by another unnamed company.

A Meta spokesperson said the issue was a misconfigured sandbox provided by security evaluation partner Irregular. Irregular, by the way, was also involved in the incidents reported by OpenAI and Anthropic, with those companies stating that the sandbox failed to quarantine the model away from the open internet.

Meta said that the hack was carried out, quote, " " In a manner similar to previously reported instances with other companies." conducting, they're still conducting an investigation and said they will provide a full report once they have all the facts. But a spokesperson for Irregular confirmed that the Meta incident involved the exact same sandboxing previously disclosed by the other labs

labs. Moving over to another hot button topic, ByteDance's founder has ruled out distillation as a way to keep up in the AI race. On Wednesday, the information reported on a meeting held last month shortly after the release of Kimi K three. ByteDance founder Zhang Yiming told his AI team that they [00:05:00] wouldn't resort to distillation even if it means falling behind the other Chinese labs.

said that ByteDance should be, quote, "willing to sacrifice some short-term gains for longer term goals." These These comments reportedly came in response to AI leaders at the company proposing a distillation project as a way to catch up quickly. Notably, ByteDance is at this particular moment something of an outlier among the Chinese labs.

Their latest LLM, called Seed 2.1 Pro, went pretty well unnoticed when it was released in June. It ranks 19th on Arena AI's coding leaderboard, distantly behind models from DeepSeek, ZAI, Alibaba's Qwen team, and Moonshot's Kimi team

On the flip side, ByteDance does produce the highly acclaimed Seed Dance video models But their text models have never been all that competitive. They're also the only major Chinese lab that keeps their LLMs proprietary rather than releasing them as open weights. Sources suggested 

hesit-- that the hesitancy to distill US models stems from ByteDance having experienced the wrath of US policymakers.

Washington has threatened to ban their core product, TikTok, multiple times over recent years. That situation was resolved last year with a forced sale of portions of the US-facing infrastructure stack, [00:06:00] including data handling and algorithm control And And so either A, ByteDance leadership is in no rush to provoke another round of scrutiny on TikTok by getting caught distilling US models, or B, and this is kind of where I would put my money, having gone through the process of getting to a resolution with the US, I think they might see the writing on the wall for other Chinese labs

And see an opportunity to tortoise and the hare it



260806 hed_EDIT: by being the one Chinese lab that can continue to play in the US environment

Based on not resorting to the same techniques that are arousing the US's ire elsewhere

Over Over in chip world, Anthropic is getting into the chip making game with the creation of an in-house chip design team. Business Insider reports that Anthropic is beginning to staff up the new team, with a spokesperson confirming the move, stating that Anthropic wants to co-design hardware and models to allow them to run faster and more efficiently at the scale our customers need, quote-unquote.

According to earlier reports, Samsung is being considered as a manufacturing partner.

Over Over the past year, Anthropic has taken a multi-chip approach. Across various applications, they're using chips from Amazon, Google, Nvidia, and AMD

And at this stage, while all of the frontier labs have [00:07:00] started to dabble with custom silicon, we're yet to see a huge benefit



260806 hed_EDIT: certainly even these customization projects are not in the short term about replacing other things

As witnessed by the fact that earlier this week, Bloomberg reported that Anthropic is in talks with Blackstone to issue 36 billion in debt to fund the use of Google's TPUs

TPUs Finally today, Finally today, two SaaSpocalypse adjacent stories. Figma is seeing echoes of that SaaSpocalypse moment as what the market perceives as weak earningssending the stock plummeting. On Wednesday night, Figma reported forty-eight percent annualized growth, but forecast a significant slowdown to thirty-six percent for Q3.

Now, Now, technically, these earnings beat analyst expectations and saw a hike in forecasts, but slowing growth is the canary in the coal mine that SaaS investors have been watching for Part of the issue is the transition to usage-based pricing. AI sales provided a tailwind to this quarter's earnings, but there's a fear that increased costs will drive user attrition In In an interview following earnings, CFO Praveer Melwani said, " We've transitioned from that moment of unlimited beta, free without limits, now to one where we've effectively monetized Figma's AI tools on the other side.

Largely, we've been able [00:08:00] to make that transition pretty seamlessly." Investors, however, were less convinced, sending the stock down by fifteen percent in after-hours trading

On the flip side is Shopify They reported 34% revenue growth and 68% growth in operating income, both beating analyst expectations. Operating costs, meanwhile, are rising at 21%, which came in below expectations. What's more, Shopify delivered a huge hike to expectations



260806 hed_EDIT: forecasting Q3 revenue growth in the mid-30s

So how were they able to do this? President Harley Finkelstein credits the rise of AI search. While While publishers have lamented AI search for undermining their web traffic, the same isn't true for Shopify merchants. Finkelstein said that AI had been a, quote, "complement to search rather than a substitute for it."

AI-driven traffic to Shopify stores is up 3X year over year, while traditional search continues to grow alongside. And according to Finkelstein, AI has been particularly helpful to some of the smaller brands. On TBPN, he said, " The merchants that seem to be benefiting the most from agentic, commerce are not the big box stores.

It's the [00:09:00] long tail of these specialized independent businesses."

He continued, " Agentic commerce is merit-based. It's not based on who is supplying the most amount of ad dollars. It is a much better shopping experience, and I still think itcould get better."

Harley continued, " 75% of all AI-attributed purchases in Q2 on Shopify are from outside of our top 100 categories. Agentic shopping is not, 'I want yoga pants.' It's, ' I want reef-safe sunscreen that doesn't leave a white cast on my black leather.'"

He basically explained that AI shopping has allowed the smaller merchants that use Shopify to compete on an even playing field with the e-commerce giants, saying, " While search engines rank by popularity against a handful of keywords, AI agents make multiple calls into Shopify's catalog, working with richer structured data to match products with the buyer's specific intent rather than just keywords.

When a buyer asks an AI assistant for the best car seat that fits three across a sedan, traditional search focuses on the keyword car seat. An agent, however, understands the actual need: the dimensions, the vehicle type, and the fact that they need three. It searches across all of those constraints at once to find the product that actually works, [00:10:00] not just the one that ranks highest."

The stock was up as much as twenty-five percent on Wednesday following earnings. Shopify's largest intraday trade since late twenty twenty-four. now now I have not been tracking my 2026 predictions all of that closely. That is something that I will do at the end of the year, of course, in our fun end of year content. But I do wanna call out this one specifically because it was probably the weirdest surprise to be included kind of thing that I had in there.



260806 hed_EDIT: one of my AI predictions for 2026, was that Shopify actually had a unique role to play

not only is there this dimension of how agentic searching can improve the shopping experience for buyers, but the way that Shopify has integrated AI for the actual store owners is exactly the sort of unbelievably powerful, self-evident use case that for a ton of small business entrepreneurs who now make their living from Shopify, shows just how valuable this technology can be without anyone having to convince them.

I'm I'm very glad to see the company doing well, and I hope it will continue to do well. For now, though, that is gonna do it for today's headlines. Next up, the main episode [00:11:00] One of the most important AI questions right now isn't who's using ai, it's who's using it? Well,

Speaker: KPMG and the University of Texas at Austin. Just to analyzed 1.4 million real workplace AI interactions and found something surprising. The highest impact users aren't better prompt engineers. They treat AI like a reasoning partner.

They frame problems, guide thinking, iterate, and push for better answers.

Nathaniel Whittemore: Welcome

260806 main_EDIT: back to the 

Nathaniel Whittemore: Welcome 

260806 main_EDIT: back to the AI Daily Brief. Some absolutely seismic shakeups over in Google land today

both DeepMind CEO Demis Hassabis and chief scientist Jeff Dean have

stepped aside from their current roles, marking what is probably the biggest shakeup in a frontier lab since the utter chaos around Sam Altman at OpenAI at the end of 2023 

now the questions are, of course, what this says about what's going on for Google, what the implications are for the Google AI project And to reveal my cards a little bit

While I think that the obvious first instinct is to be quite concerned, 

I also think that there are some strong counterpoints and maybe a different conclusion than some others are coming to that I will share a little bit later. But let's get into the details first. both both Hassabis and Dean announced their exits and future plans on Wednesday.

Hassabis will step aside as [00:15:00] CEO, but will remain as DeepMind chairman



260806 main_EDIT: Kavukcuoglu, formerly the CTO at DeepMind, will take over day-to-day leadership at the division, but but not as CEO, instead as senior vice president for DeepMind. In other words, the division will no longer have an independent CEO, as does YouTube, Google Cloud, and Waymo.

Hassabis will remain in his position as leader of Isomorphic Labs, the drug discovery spin-off incubated by Google since 2021. He will also take over as chief scientist for all of Google

In In a public note Alphabet CEO Sundar Pichai wrote, " wrote, Demis has described us as standing in the foothills of the singularity and has been spending a lot of his time engaging externally. He and I have been long discussing a role that allows him to put his full attention on actively shaping the future of AGI.

It's work that is vitally important to Alphabet and humanity, and I can't imagine a better person than Demis to do it."

it." In In his own public message, Demis added, " We have arrived at a pivotal moment in human history. I have been working towards AGI my whole life, and now, like many of you, I feel it is close at hand. It's [00:16:00] critical that we collectively get the next steps right to ensure this all goes well for humanity, and we usher in an incredible new age of discovery and wonder.

With this backdrop, I've decided that now is the right time for me to hand over my day-to-day operational responsibilities at DeepMind so that I have the time and space to focus on the big picture and help influence what is to come to the best of my ability."

Now, as Now, as surprising as Demis' move was, in many ways, Jeff Dean is the even bigger Google institution. Dean has been at Google since 1999, led the separate Google AI team between and 2023, and served as Google's chief scientist from 2023 onwards.

Unlike Demis, Dean is leaving for something new

In In the same note where he talked about Demis' departure, Sundar Pichai wrote that Dean and Google senior fellow Sanjay Gemawat are, quote, " Launching an independent public benefit corporation to accelerate discoveries in ML, science, and engineering

In In a follow-up post on X, Jeff Dean announced that his new startup is called Discovery Loop and will focus on automated research. He wrote, " Our general approach is to automate the experimental loop. We [00:17:00] think this approach is broadly applicable across many fields of science and engineering. We'll initially focus on machine learning research and engineering, but believe the approach can help with important sub-problems in nearly every one of the 14 National Academy of Engineering Grand Challenge problems.

We think doing this well requires strong expertise in machine learning as well as large scale systems."

In a press release, the company wrote, " While science and engineering have tremendously advanced society over past centuries, progress has traditionally relied on slow sequential human iterations, creating a significant bottleneck. Discovery Loop is developing advanced AI systems that leverage massive computational scale to fundamentally transform the speedand efficiency of innovation by automating complete experimental loops."

In other words, if you thought that loops were just a buzzword or just something for AI coding, Jeff Jeff Dean is trying to say that he and his team believe that that is not the case, and that this is in fact the pattern that will lead to other types of major advances

Google will be investing in Discovery Loop as an initial backer. But importantly, the company will be run independently and has raised outside capital from a range of top VCs

[00:18:00] Somewhat hilariously, Jeff posted a few slides from his pitch deck

260806 main_EDIT: deck But Siqi Chen from Runway got it right when he retweeted that and said, "Lol, there are precisely zero VCs in the Valley who needed to see a deck from Jeff Dean."

Dean." Now, Now, listeners who work in the tech industry will already understand the gravity of these moves, but for those outside of Silicon Valley, it's worth emphasizing just how important these two figures have been to Google's AI journey. Hassabis founded DeepMind as an independent AI lab in 2010, and until the formation of OpenAI, they were the locus of pretty much all major advances in the field.

They were acquired by Google in 2014, and the following year, they grabbed major headlines after pitting their Go-playing algorithm, AlphaGo, against Grandmaster Fan Hui. Go is considered a much more complicated game than chess, so at the time, it was baffling that a machine could beat a top-ranked human player

The most famous moment in that match was move 37, when the machine played a completely or seemingly unintuitive move that no human would have made. It was so unorthodox, in fact, that the commentators believed that it was an error or a glitch. But the move paid [00:19:00] dividends later in the match and was crucial to the victory.

Still, Still, that early triumph was eclipsed in 2018 by the release of AlphaFold, an AI model that could predict protein folding based on an amino acid sequence. This was one of the core problems in biology and drug making, and won Demis Hassabis the Nobel Prize in Chemistry in 2024

While While it is certainly the case that none of DeepMind's achievements are solely attributable to Hassabis, he has been the steady hand at the head of the organization since its inception 16 years ago

For most folks, the only potential knock on his leadership his exclus- has been his near exclusive focus on long-term high-minded goals. From the beginning, Hassabis has been extremely AGI pilled and viewed the ultimate goal of the technology as things like unlocking the ability to cure all diseases.

This arguably led him to forego the commercial opportunity of chatbots after the release of 2022, with Google failing to release any sort of viable competitor until 2024 with Gemini 2.

Jeff Dean, as I mentioned, joined Google in 1999 as employee number 30 and has been at the heart of every major [00:20:00] technology developed at the country ever since. he is a virtuoso level programmer mentioned in the same breath as luminaries like John Carmack or Linus Torvalds And arguably has been more instrumental in Google's commercial AI strategy than even Hassabis from his role as the head of Google AI and then chief scientist

Dean Dean also seems like he is just a really good guy

The number of stories about him being a fantastic and generous mentor to everyone in the company have just been pouring out

Meaning that the loss for Google truly is more than technical

So So what does this mean for DeepMind? One important piece of context is that Hassabis and Dean aren't actually the first high-profile exits from Google's AI work over the past year



Nathaniel Whittemore: 

260806 main_EDIT: last last month, John Jumper left the company after nine years 

and joined Anthropic. Jumper had been a key part of the AlphaFold project with contributions so notable that he shared the Nobel Prize with Demis That That same week, legendary AI researcher Noam Shazeer left to join OpenAI. Shazeer had been part of early chatbot efforts at Google, but left in 2021 to found Character.ai after getting [00:21:00] frustrated with Google's refusal to release a commercial chatbot.

Then Then he returned in 2024 as part of a $2.7 billion acqui-hire deal, and since then hadserved as the tech lead on Gemini, playing a major role in getting the product up to snuff

So then one possible and plausible interpretation of this week's news is a continuation of the brain drain that's been happening at Google throughout the year 

Core Autos Anil summed this up. " Pour one out for Big G. it's so over."

over."

And And I would say on average, that is probably the most common category of response. Tenebris writes, " Demis is ousted as DeepMind CEO, and Jeff Dean and Sanjay are leaving to start a neo lab. They're all being very careful to frame these as positive shifts, but there's no way in hell Demis would have accepted this willingly, and there's no way Sundar happily accepted Jeff doing this as a totally independent new PBC rather than a bet under Alphabet.

Tough to see an interpretation other than Jeff losing confidence in working on AGI under Google. Very bad day for Alphabet overall."

Author Author Tae Kim writes, " Jeff Dean leaving is a huge red flag. He created nearly [00:22:00] everything important to Google from AI to TPUs to search. This is a day for the history books."

Markets seem to agree with Google down 4% on the day



260806 main_EDIT: although honestly some were surprised the market impact was that little Sajid Mahmood wrote, " Google being down only 4% on Jeff Demas news either means one, markets are dumb and don't understand how valuable they are, or two, markets are smart and already priced in the risk of top-tier talent leaving

Former DeepMind researcher Susan Zhang wrote a very cryptic post about internal politics at Google



Nathaniel Whittemore: 

260806 main_EDIT: adding in a follow-up that she had gotten pretty burned out by certain people who just say yes to everything to avoid ever making a hard call and leave it to all the hungry minions to backstab each other until success finds a cursed hole to crawl out of.

So So perhaps reports that there are some culture issues aren't that far off

And And yet practically speaking, some are arguing that this might just at this point be a formalization of something that had effectively already happened

Shortly after the announcement, reports surfaced that suggested that Demis had already been checked out for the better part of a year. Writes Semafor, " Google DeepMind CEO Demis Hassabis' [00:23:00] departure Wednesday from the top job at the company he founded in 2010 and sold to Google in 2014 was at least a year in the making, said two people familiar with his thinking.

Hassabis had been drifting away from the day-to-day responsibilities of running the company's Gemini AI models and its consumer AI strategy increasingly shifting them to Koray Kavukoglu, the company's chief AI architect Said both sources, Hassabis wasn't pushed out against his will.

Rather, he struggled to get satisfaction out of being in the role of a tech executive rather than a visionary scientist



260806 main_EDIT: now this now this would seem to line up with how Sundar Pichai described Demis's departure. Pichai referred to the shift away from DeepMind to lead Isomorphic Labs and take on the role of chief scientist as, quote, " Truly his life's work and purpose."

And And for a lot of folks, this is the self-evident point



260806 main_EDIT: CEO Parm kind of crashed out Smashing the keyboard in all caps. He is He is still the CEO of Isomorphic Labs. He is doing the right thing. He is building drugs instead of Gemini Pro seven point five Max parallel reasoning for you to code Python better. So he can keep his promise of saving lives

Now Now another [00:24:00] big implication though of the move is that Hassabis will have the opportunity to focus on policy with day-to-day operations off his plate And we've certainly seen some evidence of this with Hassabis publishing a lengthy proposal for frontier AI regulations last month. The core idea was to 

Nathaniel Whittemore: create a self-regulatory body 

260806 main_EDIT: enable collaboration between the major labs and government regulators modeled after FINRA in financial regulation

Wrote Wrote journalist Alex Heath, " Inside Google DeepMind, Demis Hassabis leaving his CEO post landed with essentially a shrug. Sources tell me he's already been disengaged from day-to-day management For a while now. However, says Alex

That doesn't mean that there aren't big implications. He continued, " "But But Demis was a firewall between DeepMind and the rest of Google, even as the two got pulled closer over the last couple of years. I expect that distance to dissolve more with him stepping back



260806 main_EDIT: to to some the bigger surprise is both Jeff Dean leaving to start a new company, but also that company not being incubated within the larger Alphabet structure. 

Nathaniel Whittemore: 

260806 main_EDIT: indeed,

indeed, in some ways the entire premise of Google's parent company, Alphabet, is to function as an incubator on a grand [00:25:00] scale

Some though think the explanation is pretty simple. Author Tay Kim again writes, " " OMG, they didn't wanna work with TPUs. Jensen is probably calling Jeff Dean right now Google's infrastructure works well for big consumer apps, large ad systems, and search, but he said it has very different requirements than the type of infrastructure we want to build for research

In otherin other words, this isn't some crazy big Machiavellian thing. It is just talent following compute and the right type of compute for the project at hand



260806 main_EDIT: and and there are still some keeping the faith over at Google. Very visible member of the team, Logan Kilpatrick, tweeted that he remained steadfast bullish on Gemini But a But a lot of folks are asking where the heck Gemini is

In fact, some actually thought that we were finally going to get Gemini 3.5 Pro alongside these announcements. although then the leaker said that it was being pushed today. So who knows? Maybe by the time you're listening to this, Gemini 3.5 Pro will actually be out

And And yet I don't think that 3.5 Pro is likely to solve all their problems or answer the big questions. Alex Heath again reported, " Google is currently running behind the frontier, especially on coding, and the [00:26:00] internal sentiment I'm hearing on Gemini 4 is muted. On its current trajectory, it's not expected to push frontier AI forward the way Fable and Soul just did."

And And this could be a major issue. Wall Street might be willing to have a muted response to serious top talent leaving. 

Nathaniel Whittemore: 

260806 main_EDIT: but proof of what it feels like



Nathaniel Whittemore: 

260806 main_EDIT: that Google is unable to keep up with OpenAI and Anthropic at the state of the art

would have some serious financial market implications

Now in the Now in the past, one of my cautions around personnel movements

has been that there is so much that goes into any individual's decisions about what they spend their time on that I think it is very easy to significantly overestimate the broader implications of a personnel move 

When a lot of it, in many cases, is in fact just personal



260806 main_EDIT: taking Demis in that light, he is certainly not short on resources

He has been in this leadership role for a very long time. He has dealt with a huge amount of internal politics as Google reorganized its AI divisions numerous times

And he's found himself in the dogfight of all business dogfights when that's never where he really wanted to be in the first [00:27:00] place. I I think Sundar Pichai's analysis that where he's moving is a better type of fit for him is true, even if there's more going on than that post lets on

And for And for Jeff Dean

As deeply associated with so many of Google's innovations as he is, after 27 years at a single company, in the modern age that we live in, can you really fault the guy for wanting to go out and do something on his own in a new context without the bureaucracy, with just a bunch of big brain bro and broettes that he got to pick for himself?

I I think the bigger story is that the man lasted for 27 years at a big company, even one as cool as Google And And yet still



260806 main_EDIT: While one or even two changes might be seen as individual data points, combine these with the other high-profile departures from the last couple of months, and it certainly does seem to be a pattern And it's a pattern that's happening in a context

That is undoubtedly, at least in most people's eyes, of Google having fallen critically behind in the AI race

Take him, who I've quoted a couple times in this show wrote a post in July called Google is a Secular Short

[00:28:00] In it, he argued, " Hassabis DeepMind chase one shiny vanity science project after another while being blindsided by every major commercial AI advance, from LLMs and reasoning models to agentic AI. miss and fall behind every big AI wave. Most importantly, Google has fallen critically behind in the third major wave of AI computing, coding agents and agentic Anthropic and OpenAI are thriving by selling coding agents to corporations, generating billions in revenue that could turn into hundreds of billions in the coming years. Gemini has become a laughingstock among AI model enthusiasts in Silicon Valley. Where is Gemini on the coding agent leaderboards?

260806 main_EDIT: Nowhere. Bloomberg also reported that Google is months behind schedule with Gemini 3.5 Pro as it tries to improve its coding capabilities. Many wonder why Google, with all of its resources, can't beat a tiny Chinese startup like Kimi Maker Moonshot in the AI model race. Even the one time Gemini caught up with its release late last year, it was state-of-the-art for just six days before being overtaken by Anthropic's Claude Opus."



260806 main_EDIT: and so while that is obviously not an argument that this is good for Google, it is instead simply an argument about the facts [00:29:00] about where they are today

I I think that some parts of this history are fairly undeniable

Perhaps most emblematic of this 

is the failure to launch ChatGPT before ChatGPT

Midjourney's Chang Liu recently tweeted, " I sometimes think about that Jeff Dean interview where he said that they had an internal bot before ChatGPT, but didn't think it was better than just Googling."

Googling." Tebo, who now leads Codex and ChatGPT at OpenAI, responded and said, " I was part of that team. Basically, ChatGPT one year before it came out, called LM Chat and then another code name. Google was too nervous to release it, and DeepMind was blocked from shipping products that could disrupt Google.

I think about this a lot."



260806 main_EDIT: now now anyone who was around back then can remember just how insane it was for all of 2023 and the beginning of 2024 that Google had not only letthis startup flank it, but that it simply couldn't catch up

Where Where it finally started to get some of its mojo back was in late 2024, specifically with the release of NotebookLM, which was their first genuine consumer AI product hit pretty much ever. [00:30:00] That momentum rolled into 2025, and Gemini actually became a major model, 

getting to hundreds and hundreds of millions of monthly active users, and seemingly coming into 2026 positioning Google to compete



Nathaniel Whittemore: Alas, since then we have seen 

that 

260806 main_EDIT: where the AI battle has shifted



260806 main_EDIT: in terms of coding agents and harnesses as the anchor for everything else, has left them completely in the dust

You You can feel throughout all of this sourcing and reporting and even public comments how dismissive and disinterested Demis Hassabis has always been in these sort of things. it feels like even getting to Gemini was like pulling teeth



260806 main_EDIT: 

and a compromise to be able to spend time on what he really wanted to do

The The point being Without any disrespect to the unique and incredible attributes of Demis Hassabis as a scientist and as a leader for one type of organization If we are taking it on evidence alone, he has not done the job that has been expected of him as the leader of Google's AI organization



260806 main_EDIT: and yes, you might be thinking, " Well, isn't that a little uncharitable? I mean, look [00:31:00] at all the things that they put out



260806 main_EDIT: but this is kind of like Real Madrid in soccer. When you get to a certain level, you don't get points for putting points on the board. You only get points for winning



260806 main_EDIT: when a team like Madrid doesn't win La Liga and doesn't win the Champions League, those seasons are considered a failure, full stop. And hard questions start getting asked about whether there need to be personnel changes and coaching changes

And And yes, I am among those who are soccer pilled coming off of the World Cup. But the point is that Google is in that similar position. Anything less than state-of-the-art models, anything less than growing consumer usage



Nathaniel Whittemore: 

260806 main_EDIT: these things are going to be considered failures

And And it seems very possible that this particular leadership change was overdue. Not only that



260806 main_EDIT: if we are for the world's sake just trying to allocate people where their gifts are most going to impact the world, getting Demis out of that commercialized role and into a place where he can do either A, more science or B, more policy shaping, could be better for everyone



Nathaniel Whittemore: 

260806 main_EDIT: Martin Martin Shkreli wrote, "Buy Google. As much respect as I have for Dean and co, which is a lot, Google is bigger than any person. Further, losing [00:32:00] these fine engineers may result in the board of directors asking, 'What is going on here?' And changing management or making other changes which course correct for the better."

better." Now, to the extent that the reporting around broader culture issues is true, it's gonna take more than just a leadership switch to solve those problems. But a leadership switch isn't a bad place to start



260806 main_EDIT: Look, in short, from where Google was, they were never gonna get back to where they needed to be

with the same arrangement that they had used to lose their place in the race over the last year

year I would not be even close to counting them out. And I think there's a strong argument that being able to now redesign the organization to be exactly what it needs to be could, in some number of months Leave Google in a much better position than it is today again, maybe the whole thing flops and they just sell TPUs and cloud access forever, and it's still a big company and who cares?



Nathaniel Whittemore: 

260806 main_EDIT: in either in either case, no doubt it is huge news, something to be debated and discussed. For now, though, that is gonna do it for today's AI Daily Brief. Appreciate you listening or watching as always, and until next time, peace. 

​ 

[00:33:00] 

Nathaniel Whittemore's audio recording:
