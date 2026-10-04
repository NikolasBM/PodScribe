---
podcast: "ai-daily-brief"
podcast_title: "The AI Daily Brief"
title: "Why AI Washing Won’t Work Much Longer"
date: 2026-08-04
url: "https://aidailybrief.ai/e/2026-08-04"
guid: "https://aidailybrief.ai/e/2026-08-04"
host: "Nathaniel Whittemore"
format: "news-analysis"
level: 2
length: "00:24:00"
categories: ["models", "open-weights", "enterprise", "coding"]
featured: ["Qwen", "open-weight models", "Kimi"]
mentioned: ["Grok", "recursive self-improvement", "Claude", "Claude Cowork", "Claude Fable", "Artificial Analysis", "GPT-5.6", "Microsoft MAI"]
transcript_source: "publisher"
---

# Why AI Washing Won’t Work Much Longer

[00:00:00] Today on the AI Daily Brief what a new Chinese open weight model release has to do with big shifts in enterprise AI thinking. And before that in the headlines, Palantir and the march to AI sovereignty.

260804 in_EDIT: The The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI

All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG

260804 in_EDIT: Airtable, Section, and Blitzy. to get an ad free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts. And to learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai. 

This week, tech earnings continue with Palantir registering another monster quarter quarterly revenue came in 

260804 hed_EDIT: at 1.94 billion, up 93% from this time last 

year and beating expectations. 

Commercial 

sales were up 149% year over year, up from 133% growth rate in Q1, demonstrating that enterprise AI demand is 

still [00:01:00] booming despite 

flashy headlines of token budget cuts 

indeed, indeed, it turns out that caps, which by the way, most organizations haven't even gotten close to that level yet, are are not the same as cuts. Palantir also managed to expand profit margins with net income reaching a billion dollars for the quarter and growing at a two hundred and twenty-five percent annual pace

CEO CEO Alex Karp described the quarter as otherworldly and use the earnings as a chance to proclaim the message that he has been getting increasingly loud about on his bully pulpit

He basically painted Palantir's results as an expression of the demand for AI sovereignty

He He said, " Palantir is the only company that has demonstrated it can transform tokens into actual economic value. Our customers trust us to provide them with maximal control over their operations, data, and decisions." Palantir Palantir hiked annual forecasts, sending the stock surging by 10% in after-hours trading

With maximal control over their operations, data, and decisions



260804 hed_EDIT: this this was the message that he echoed in his shareholder letter as well

Karp Karp wrote, " " Every organization in the world is awakening to the risks of handing the creators of language models the keys to their institutions, of letting these models loose [00:02:00] within their homes

The demand from our partners is clear. It is for control over data, the prompts that the models ingest, and more fundamentally, the organizational and business intelligence, their alpha, that the language labs are not only ready and willing, but structurally designed to capture from their customers

Later in the letter, he continued, " " We do not get paid for clicks or tokens or chats. The gamification of the most significant development in modern economic history seems to us misplaced. The usage of a platform may hint at its value, but isby no means dispositive, and many are now finding out that consumption and usage alone have little or nothing to do with the production of results

Just Just to add a little fire to all of it, he then says, there are Marxist overtones and undertones to our business. Others, Others, including many of those building large language models, intend, knowingly or otherwise, to capture the means of production of their purported partners. The The limitations and faults of the token industrial complex, which has threatened to overtake and dominate the world economy, have increasingly been exposed.

We We have always declined and will continue to decline entering into a parasitic relationship with our partners."

In In a follow-up interview with CNBC

Karp made it clear exactly [00:03:00] who he takes issue with with He said, " " We have people trying to drug addict us to a future they believe they control. Now, I've spent a lot of time with Dario and the effective altruism crew. They wanna They wanna tell you we have to march into a future where we own nothing, where your businesses aren't profitable, where none of us have jobs, and where our adversaries win."

Now, now of course these are not the type of comments that everyone is going to take at face value, and they generated a wide range of opinions

Summing up the most optimistic version of the take, Amit is investing writes, " " The age of AI is not about valuations, but about empowering workers, enabling agency, and growing GDP."



260804 hed_EDIT: 

now speaking now speaking of companies that are taking issue with the Frontier Labs, Apple right now is of course embroiled in a lawsuit with OpenAI



260804 hed_EDIT: claiming that via an employee who left Apple to join OpenAI 



the LLM Lab stole Apple trade secrets

OpenAI is biting back In a new letter, they wrote, "Apple is getting this wrong." " Apple," they write, "is one of the greatest companies of all time and built a reputation for obsessing over the smallest details. This careless, aggressive, and oddly personal lawsuit sadly doesn't live up to that reputation."



260804 hed_EDIT: now [00:04:00] the now the big jaw-drop line was this one. Apple had claimed that they contacted OpenAI in February and that we didn't respond. They now admit that their outside lawyers emailed the wrong person after confusing two Asian last names only after we brought this to their attention



260804 hed_EDIT: 



which honestly, if true

brought up some big questions with the lawsuit 



for many folks watching this from the outside



260804 hed_EDIT: Now Now at this stage, this is a little bit more psychodrama than we normally get into on this show. it'll be worth paying attention to if it actually shifts the plans that OpenAI can make with hardware. for now, that is just such a wild mistake to make that I had to capture the zeitgeist of the AIX community by sharing it with you here

Moving on Moving on to some other comments that are getting attention, Google DeepMind's chief strategy officer has reframed sky-high CapEx as a down payment on recursive self-improvement. During During a panel at UC Berkeley, Jasjeet Sekhon said that RSI was a key part of the investment thesis 

Now, 

now if you've been listening closely, this earning season has been all about how the ROI of AI lines up with endlessly ramping CapEx.

Google in particular was punished for their AI income [00:05:00] failing to live up with AI spending on the short term as free cash flow flipped negative

This particular Google executive acknowledged that current AI revenues, quote, "Don't sustain the capital expenditures we're making so far."

Creating a, quote, "danger we could hit an AI air pocket such that the expenditures happen but the revenues don't show up." However, he argues that the CapEx build-out is not about near-term revenue, but instead the, quote, "biggest scientific bet civilization has ever made."

made."

Nathaniel Whittemore: Next Next up, an interesting good news story in cybersecurity as Claude helps researchers uncover a decades-old vulnerability in DNA evidence databases used in criminal prosecution. At At labs across the country, forensic scientists keep DNA samples as digital files to create a searchable database.

260804 hed_EDIT: A group of researchers have found that they could alter the files using code written by Claude in a process that takes around forty-five minutes. The The core issue is that this database software was created in 1995 and includes none of the tamper-evident protections of modern software.

One of the researchers, forensic scientist and New Haven University professor Laura Gadosh-Combs said

said Effectively what we have are data files that are legitimately referred to as the gold [00:06:00] standard of forensic science that lack the same level of tamper-evident markings that we require for a paper bag

Now the Now, the ramifications are concerning. A bad actor with rudimentary knowledge of how DNA testing works and access to the database could corrupt files or even modify evidence to frame an innocent person. None None of the labs around the nation have reported any kind of this evidence tampering, but they also haven't been able to figure out a way to detect if tampering has occurred As As part of their disclosure, researchers noted that some of the encryption still being used relies on an encryption key that's been available on the internet for years.

The creator of the database software said that they have been working closely with the US Cybersecurity and Infrastructure Agency on mitigations and have pushed a software update to implement digital signatures

Sarah Chu, the director of policy and reform at the Perlmutter Center for Legal Justice, said that the research highlights how badly behind the forensic sector is

She said, " " Lessons learned from other industries haven't been imported into forensic science in a serious way. We've been behind the ball for so long. That kind of all rolls downhill into this incident." Now, for Now, for the AI folks, this highlights what many have been saying about how critical it is to be very [00:07:00] conscientious about guardrails on frontier models.

This is an example where defense-focused researchers were able to find serious vulnerabilities in ancient systems still being used in a very high-stakes field

It is absolutely the case that there are hundreds or even thousands of outdated systems like this running critical infrastructure across society. Cost is a huge part, perhaps the biggest part of why these systems haven't been overhauled or even properly tested for vulnerabilities. While it's obviously not perfect, the ability to do even rudimentary testing using AI on a modest budget could be an absolute game changer for this sort of software TLDR, while yes, it is scary that cyber criminals have a new suite of powerful tools, AI is and remains a massive upgrade for cyber defenders as well

well Lastly Lastly today, one that we will pick up on I'm sure tomorrow, the White House is hosting a set of AI companies to discuss the administration's voluntary review framework for frontier models

I am very interested to see what comes out of that. But let's wait until we have some more solid reporting. For now, that's gonna do it for today's headlines. Next up, the main episode [00:08:00] One of the most important AI questions right now isn't who's using ai, it's who's using it? Well,

Speaker: KPMG and the University of Texas at Austin. Just to analyzed 1.4 million real workplace AI interactions and found something surprising. The highest impact users aren't better prompt engineers. They treat AI like a reasoning partner.

They frame problems, guide thinking, iterate, and push for better answers. and the good news, these behaviors are teachable at scale.

If you're trying to move from AI access to real capability, KPMG's research on sophisticated AI collaboration is worth your time. Learn more at kpmg.com/us/slash sophisticated. That's kpmg.com/us/sophisticated. 

Nathaniel Whittemore: Here's a harsh truth. Your company is probably spending thousands or millions of dollars on AI tools that are being massively underutilized. Half of companies have AI tools, but only 12% use them for business value. Most employees arestill using ai.

Nathaniel Whittemore: Welcome back to the AI Daily Brief. today we are talking about the latest model release, which is Qwen 3.8 Max But the context we're putting it in is a little bit different than normal

260804 main_EDIT: As you know, I am just back from KPMG's Tech and Innovation Symposium last week

And my biggest takeaway was about just how radically the conversation had shifted over the last year. When I was there, for their twenty twenty-five edition We were still genuinely talking about things like the percentage of organizations that had one, two, or three AI use cases This year we were talking about how organizations are handling the complex governance issues that arise from everyone having powerful coding tools, and how people are dealing with cost provisioning issues and different models across different parts of their organization.

And whether they should be looking into fine-tuning open-weights models and have an open-weights models policy



260804 main_EDIT: point being that the level of sophistication around [00:12:00] AI and more importantly, the quality of the questions that enterprises are asking has increased dramatically

Meaning that my guess is for the first time, some meaningful number of enterprise buyers, not just early adopter developer types, 

but actual enterprise IT type folks are actively paying attention when things like the new Qwen 3.8 Max model comes out

out So So first, let's talk about the model

the-- like Kimi K3, it is a large model, this one coming in at 2.4 trillion parameters. 

indeed light, indeed latent space writes the model would've been the top open model in the world, but for the recent Kimi K3 release

The The official Alibaba Qwen account calls it a new bar for coding and co-work, and points to examples of its work on autonomous coding. Ten-plus days of self-evolving development from empty folder to production without hand-holding. 

Nathaniel Whittemore: 

260804 main_EDIT: sharing a complete project trace on their GitHub they also laud production quality deliverables across hundreds of professions, systems-level autonomous planning with closed-loop adaptive learning and native multimodal intelligence.

Vision, they write, isn't just input, it's a continuous feedback loop for planning, execution, and self-correction

[00:13:00] Now, Now, at least on the self-reported benchmarks, there are some pretty impressive numbers

Alibaba reports a terminal bench score that puts them between Fable 5 and GPT-6-Soul. A co-work bench score



260804 main_EDIT: between Soul and Fable 5



260804 main_EDIT: visual reasoning and research reproduction that are totally state-of-the-art, and so on and so forth

They also report state-of-the-art on OS World Verified, which is agentic computer use, which if that result is accurate, is one of the more significant when it comes to its applicability as an agentic work tool

Now interestingly, a lot of the discourse online was not about the model itself, but about the video ad that they released it with

The ad

which is an incredibly simple concept very well executed

is a laptop in the foreground doing all sorts of different types of work. There's coding work, science work different types of knowledge work. And in the background, you see the humans presumably paired with that laptop off doing more of the things that make them, well, enjoy their lives

There's a guy fishing at one point

another man playing tennis, a woman rock climbing, and another woman reading



260804 main_EDIT: in [00:14:00] other words, without using basically any words

Quen is saying that the value to your life as an individual of these incredibly powerful and advanced models is to give you more time to do the things that you actually wanna do



260804 main_EDIT: Calacanis, Jason Calacanis from All In tweeted, " Not only is China making increasingly competitive models, they're also making world positive AI marketing. The computers are going to do our jobs for us, and we're all going to the beach."

Nansen's Alex Svanevik writes, " "What is What is this marketing? No graveyards? No entry-level jobs disappearing?"



260804 main_EDIT: Vittorio also points out that it seems like perhaps They are trolling us a little bit with using one of the examples being verifying protein sources given these strict guardrails on Fable



260804 main_EDIT: and and yet one of the big deals about this announcement is that it represents a return for Alibaba and the Qwen series back to open weights models Last

Last year, there was a lot of personnel shifting around Quen



260804 main_EDIT: and for their largest Max series models, they moved from open to closed in fact, it brought up the question more broadly of whether this was something that was just going to be more commonplace for Chinese models as they got more advanced and got closer to the [00:15:00] frontier

Well, Well, now they are back

And as Yuchen Jin points out, this marks the first time Qwen will open source the weights of a Qwen Max class model. The full weights will be released next week

Strawberry Labs' Chirag AsarpotraAsarpotra writes, " This is so huge for open models. Chinese labs are clearly taking advantage of Anthropic's recent PR mess and are going all in on open weights. The message is loud. They want Chinese open models to dominate globally."

Yet Yet maybe the even bigger deal is the price. One of the things that I've talked about on this show a lot recently is that many folks, particularly around the policy sector, still have this ideathat every Chinese model is cents on the dollar relative to their state-of-the-art American competitors That hasn't been the case for a while



260804 main_EDIT: in fact, to give you one example

while Kimi K3 is cheaper than Opus, it's only cheaper by about 40%. $15 per million output tokens versus $25 per million output tokens

Quen, however, takes it down significantly



260804 main_EDIT: Quen is being priced at $2 per million input and $6 per million output tokens, 

Making it a little more than a third of the price of Kimi and a fifth of the price of Opus. [00:16:00] Now, that's Now, that's still not the pennies on the dollar that some people assume, but it is a much more significant decrease than, for example, Kimi K3

Now, Now, given all of this, it's not surprising that a lot of the first impressions were excited. Alex Volkov from the Thursday AI Podcast writes, " Alibaba is back? 3.8 Max is about to get open weighted with 2.4 trillion parameters. This model comes very close to K3 running projects for 16 days



260804 main_EDIT: but but it is worth being at least a little cautious at this early stage. When it comes to independent benchmarks, artificial analysis did publish Quen 3.8 Max's score Of 53, which puts them four points behind Kimi K3 and even a point behind Grok 4.5 

Nathaniel Whittemore: Now 

260804 main_EDIT: adding some intrigue to the whole thing, Artificial Analysis quickly took down those scores without any explanation.



260804 main_EDIT: So we'll have to see what was going on with that



260804 main_EDIT: on some of Ethan Mollick's tests, he writes, " Basic impression after a bunch of experiments is that it is a solid model, but not Kimi K3 level in my experience so far."



Nathaniel Whittemore: 

260804 main_EDIT: Datam writes, "Quen38 Max is unusable

Saying that they tested it across coding, design, planning, agent orchestration, and multiple harnesses, [00:17:00] and running it against Kimi k3, Grok 4.5, GLM 5.2, GPT Luna, and Opus 5, with Qwen coming in last every time.

He says it's extremely slow, unstable, and burns through usage like crazy. It often fails on the first attempt, then the second, and sometimes the third

Pavel Hurin also tested it

On his Bug Bench test, which has two real repos with 105 hidden bugs



260804 main_EDIT: and found that it found 19 out of 105 bugs



260804 main_EDIT: 5 were both ahead fixing 21. GPT 56 Soul led at 42

And while he noted that Qwen did fix one bug that none of the other10 models he tested found

that quote, " Just getting it to run took five attempts. One coding agent used up the five-hour subscription quota in half an hour. The pay-as-you-go key exhausted its free tier, then refused to bill until I opened a different console."

All in all, the cost was about $31, leading Pavel to conclude, " Let me save you some money and time." GPT 5.6 Luna ran the same benchmark for a buck 80 in fixed 33. Grok 4.5 judged 16 in 25 minutes



260804 main_EDIT: so first evidence suggests some good reason to be skeptical about the published benchmark numbers. But ultimately

[00:18:00] why it's still an exciting release to people is the fact that it's coming in open weights, which means they're going to be able to get their hands on it in a totally different type of way. Which gets us to my contention from the beginning of the show, that despite this being the type of model release that in the past w- would only be something that was really paid attention to by developers and early adopters.

Increasingly, there are going to be folks inside big mainstream corporations and enterprises who are paying attention to this as well Now also yesterday, The New York Times published an opinion piece from theformer chief information officer for Lululemon, Julie Averill



260804 main_EDIT: the piece which remember is titled not by the author of the piece, but by the headline writers at The New York Times was I helped run Lululemon. Companies need to stop kidding themselves about AI

Now to 

Now to some extent



260804 main_EDIT: this is the platonic archetype right now of the average essay about enterprise AI



260804 main_EDIT: The first part is all about how common it is for corporations 

Nathaniel Whittemore: 

260804 main_EDIT: to want to use AI for PR value rather than

Nathaniel Whittemore: actually integrating it deeply into strategy



260804 main_EDIT: Julie Julie coins a term AI wishing, which she defines as the belief by company leaders that AI is magic, that you can wave its wand towards a hard problem and skip the work [00:19:00] of solving it



260804 main_EDIT: but don't mistake this as a critique of AI. It is not. it's a critique instead of the very real human processes that impact how AI gets integrated.

She She writes, " "Don't Don't mistake any of this for doubt about AI's potential. It's the most powerful technology I've seen, and entire industries are already being remade by it

it Pharmaceutical companies are rebuilding drug discovery around it. Banks run fraud and risk detection on it. Governments are treating the chips behind it as a matter of national security. and then inAnd then in the most important line, she concludes, " This kind of work doesn't happen in a quarter, and believing that it can is the trap."

Now And so in this context, not only did we get AI wishing, we got AI washing

As she puts it, the insidious cousin of AI wishing, that is when a company under pressure to immediately show results claims to be doing more with AI than it actually is



260804 main_EDIT: now the most now the most negative and problematic version of thisis the AI layoff

Quote, " A company proclaims it needs fewer people

Because AI made its operations more efficient, often the efficiency doesn't exist yet. The cut is really about freeing up cash, sometimes to spend more on AI. in in May, she [00:20:00] continues, US employers announced ninety-seven thousand job cuts, and according to one research firm, companies blamed forty percent of them on AI.

A separate survey found that around one-third of hiring managers who had cut a role because of AI had already rehired for the same or a similar one. Of course they did. They eliminated positions before redesigning the work, so the work shifted onto the people who remained. Then companies quietly hired back some of the capability they claimed AI had replaced.

That That cycle burns money and loses the talent and experience that was pushed out of the door, not to mention the trust of the people asked to stay

stay now I think at this point my perspective on this is very well-trodden territory I think the organizations that view AI strictly as an efficiency technology rather than as an opportunity technology

might be able to eke out a few headline wins in the short term, but are ultimately going to be absolutely pummeled by the companies who understand that this is a redesign moment that opens up massive new opportunities Not a chance to make shareholders excited about cost cuts for Q3

In In short, AI is going to take work to do well. It is going to involve organizational [00:21:00] redesign, job role redesign, process redesign



260804 main_EDIT: and shortcuts are bound to fail

And so And so how do these two stories intersect? Qwen 3.8 Max on the one hand, and this cautionary tale about AI wishing and washing the enterprise on the other



Nathaniel Whittemore: 

260804 main_EDIT: well, what

well, what it comes down to is that the change in the conversation that I was mentioning as exemplified by the KPMG event, and the sophistication that it implicates shows that more and more enterprise AI leaders are asking the right type of questions

For For example, there is increasingly a discourse about whether open weights models can be part of a complete AI system that involves different types of models for different types of tasks

despite headlines which suggest

only blunt tools like cost caps. The reality in practice



260804 main_EDIT: is that basically every enterprise AI leader that I interact with



260804 main_EDIT: is digging deep to actually understand what their approach to, on the one hand, wanting more AI consumption and on the other, needing to manage costs should actually be

one part of that is discourse about open weight models. [00:22:00] A year ago, almost no company had any sort of actually expressed policy when it came to these models 

other than Lowell, of course we're not gonna use Chinese models Now that conversation has really changed



260804 main_EDIT: just yesterday I saw a Forbes guest op-ed about why leaders should learn about open weight models. and and of course regular listeners will know that it's not just op-eds Increasingly, we have companies that are offering access not only to cheaper models, but to the ability to customize and fine-tune them based on your organization's unique needs and data



260804 main_EDIT: 

Thinking Machines

Thinking Machines Lab, the spinoff from former OpenAI CTO Mira Murati, introduced a product, Tinker, to do that late last year.

And Microsoft, while obviously not using open models, is building a frontier tuning service on top of their lower cost MAI models that is explicitly trying to solve for this era of increasing AI complexity then of then of course, there are the router companies.



260804 main_EDIT: every day it seems we have some new company introducing their latest router or news that indicates how valuable these companies have come, like reports that Stripe is about to buy OpenRouter for $10 billion



260804 main_EDIT: and while and while you might think that routers are justreplacing the last thing as the buzzy [00:23:00] corporate word, in my experience, that is just absolutely not the case

leader, those same enterprise AI leaders that I was talking about before



Nathaniel Whittemore: 

260804 main_EDIT: are yes, exploring routing solutions but not in a way where they're just hoping to buy whatever Gartner says is the best vendor and call it a day 

as a recent post on digitalapply.com put it, " AI cost optimization is now a discipline, not a hack."



Nathaniel Whittemore: 

260804 main_EDIT: companies

companies are exploring what combination of third-party and internal solutions is going to be the right way to handle and whether or not a router is even the right solution. But again, the fact that those are the types of questions they're asking, I think is worthy of a lot of optimism



Nathaniel Whittemore: know, 

260804 main_EDIT: now I know many listeners who are the AI leaders in their organizations will be shaking their heads



Nathaniel Whittemore: 

260804 main_EDIT: wishing that the situation I describe among enterprise AI leaders were the situation that they were dealing with inside their company



260804 main_EDIT: and I certainly don't wanna minimize how steep the hills to climb are for many opportunity AI advocates who are trying to get their organizations to handle this the right way

But But for basically the first time since ChatGPT launched My My observation is that the enterprise conventional wisdom around [00:24:00] AI



260804 main_EDIT: is getting more directionally correct



260804 main_EDIT: I think I think our attitudes around the types of things that go into AI wishing and washing are changing radically. and the PR value or board plotlets that people got before are going to stop, 

Nathaniel Whittemore: 

260804 main_EDIT: which helpfully will cut off the incentive loop to do AI the wrong way If I am right, what we'll be left with

is a situation where we can actually begin



260804 main_EDIT: the the exciting work of really redesigning around the capabilities of AI

With all of the implications for both our personal and our professional lives. For now, though, that's gonna do it for today's AI Daily Brief. Appreciate you listening or watching as always, and until next time, peace. 

​ 

Nathaniel Whittemore's audio recording:
