# AI Companies Still Haven’t Delivered on Their Biggest Promises — Transcript (2026-08-17)

https://aidailybrief.ai/e/2026-08-17 · Listen: https://pod.link/1680633614

---

260817 cold_EDIT: [00:00:00] In a recent podcast appearance, a prominent investor said that he had heard from multiple sources inside Anthropic that Dario Amodei and other leaders in that company felt that at some point in the future, they might be the only company left.

It would just be them, governments, and the rest of us. Now, these comments on that podcast kicked off quite a firestorm of discourse about Anthropic and their, about Anthropic and their role in AI, and what their beliefs actually meant for the industry.

that, it also generated that rarest of phenomenon, an appearance on social media from Anthropic CEO Dario Amodei himself In his response post, Dario discusses his real views on regulatory capture, what he thinks the real root of AI's trust problems with people are, and what he thinks could actually address those trust problems in the long run.

So did people find it enlightening, convincing? 

Nathaniel Whittemore: Did anyone's 

260817 cold_EDIT: opinions actually change? And what does the whole conversation say about the AI discourse and Anthropic's place in it?

260817 in_EDIT: pod... The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI. [00:01:00] All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, Blitzy, Robots and Pencils, and Hyperagent. To get an ad-free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts.

And to learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai. 

We got ourselves quite a Monday here, so strap in

260817 hed_EDIT: first up comes a new model and one that is sure to kick off a lot of debate. has, Z- ZAI has dropped GLM 5.3. Now, you might remember that when ZAI released GLM five, released 5.2 in June, it helped kick off this new wave of concern that we're still in right now, that Chinese open weight models were closing the gap.

now, part of that was timing. The release came during the period where Fable 5 was locked behind government doors and OpenAI was delaying 5.6 for the same reason

But the feeling of Chinese models nipping on Western heels compounded with the release of Kimi K3 the following month still [00:02:00] as has happened every other time, 

even acknowledging what these models are really good for

there has been a sense that they still are ultimately behind the frontier in pretty meaningful ways So where does that leave us with GLM Well, 5.3 is built on the same base model as 5.2

meaning it's not some massive multi-trillion parameter model. Still, ZAI claims that they've made some big advances purely by scaling reinforcement learning

on coding, GLM 5.3 scores 28.3% on Terminal Bench 3.0. That puts it around five points behind the frontier with Fable 5 and GPT 5.6 Sol, but 11 points ahead of Kimi K3. The results on DeepSWE were less impressive, scoring 66.9%, which puts the model half a point behind Kimi K3, three points behind Fable, and six points behind 5.6 Sol For agentic use

Five three scored state-of-the-art results on automation bench and GDPVal, Just slightly inching out the US frontier



260817 hed_EDIT: overall it looks like that for high-level use cases like running agents andcoding, remains a bit behind the absolute state-of-the-art, but has [00:03:00] squeezed a lot of performance out of a mid-sized model and may in some cases have overtaken Kimi Now, ZAI said improved cyber performance was one of the key focuses for their reinforcement learning run. They noted that during the Hugging Face attack, cyber defenders had been forced to use GLM 5.2 because the guardrails on frontier models had rendered them useless

In a In a WeChat post, ZAI said, " If the powerful attack ability is spreading, the defensive ability cannot be limited to a few closed source model companies."

that makes their performance gains on cybersecurity benchmark Cyber Gym

A bit more interesting, jumping seven points from their predecessor 

to actually overtake Fable 5

Now, just to be super clear, because of course we're already seeing some people freak out about a mythos level cyber model released as open source, that is not what these benchmarks are saying even if you take the benchmarks at face value. There is a difference in being mythos or fable level at finding vulnerabilities

and being mythos or fable level at then doing something about it and or autonomously executing cyber attacks

ZAI is also taking a phased approach to the release, testing the model with trusted partners before publishing the full [00:04:00] weights. Now, at the time of recording, we don't yet have the full benchmark run from artificial analysis. so we don't have either a full barrage of independent tests Nor do we have a great gauge for token-adjusted cost

On a per token basis, GLM 5.3 is less than a 10th of the cost of Fable or Five Six Soul and one fifth the cost of Kimmy K3. In limited testing, some users are finding that GLM 5.3 costs around two thirds of Kimmy K3 or Groq 4.6 for the same task

First testing for real-world performance leads to feedback that is a little mixed

ZAI claims to have detected over a thousand critical and high-risk vulnerabilities in open source repos They also believe they found a potentially serious vulnerability in Cursor, which they privately reported to the team

But some of the other first tests are a little less clear

Developer Aditya tested it for game development tasks and found GLM 5.3 struggling a bit and clearly behind KimeK3 And another big complaint was that the model was painfully slow to the point of being unusable. Now, that could just be issues with excessive demand on release day rather than a fundamental problem

But that remains to be seen 

Nathaniel Whittemore: Overall, it 

260817 hed_EDIT: looks like ZAI delivered a [00:05:00] solid improvement over GLM 5.2 and showed once again that a lot of performance can come simply from scaling reinforcement learning

open model researcher Nathan Lambert used his review to argue that we should stop being surprised by strong performance out of Chinese labs

to risk a broad oversimplification, he wrote, " ZAI seems to have strength in post-training when compared to Qimi, which is more of a pre-training masterpiece." following this release, there have been a lot of discussions wondering how China can keep up so well.

How can such a small model be matching the leading public American models? Are these results real? The simplest explanation, he continued, is that ZAI is very good at what they do

Lambert's point is that we need to stop writing off the Chinese labs as only performing well because of distillation or benchmark maxing

Arguing that when we do so, we underestimate what they're actually capable of

of

Nathaniel Whittemore: Importantly alongside 

260817 hed_EDIT: this type of release

Wall Street analysts and people who aren't necessarily listening to the AI Daily Brief every day are finally beginning to update their priors and recognize that Chinese labs aren't in most cases selling frontier intelligence for pennies on the dollar the way they had previously [00:06:00] assumed

The savings are definitely still there, but the pricing gap has contracted substantially At this stage, cheaper US models like Grok 46, Muse Spark 1.2, or GPT-56 Luna are cost competitive with the best models out of China. Wall Street is also recognizing that even Chinese models still need infrastructure

Now, that probably won't come as a huge surprise to you, but it is worth remembering that following the DeepSeek moment in early 2025, one of the big concerns was that cheaper models would invalidate large-scale GPU investment In a recent note, however, Morningstar analyst Malik Khan wrote



260817 hed_EDIT: if an enterprise were to consolidate its entire AI stack on open weight models, it would still need cloud infrastructure to run those workloads, store data, manage security and access to resources, et cetera. All tailwinds to cloud infrastructure companies. companies.5.3. I will certainly keep an eye on 5.3 aspeople test it further

Nathaniel Whittemore: but another bit of model news, or at least model innuendo and rumor, is that Anthropic has suggested that they won't release their next model, instead keeping it for internal use

260817 hed_EDIT: The second edition of the Anthropic Risk Report included a discussion of unreleased [00:07:00] models that are currently being used internally. As of mid-July, Anthropic had three significant unreleased models. The first two were Opus 5 and a model referred to as Model One, with capabilities broadly in line with Anthropic also disclosed a model known as Model 2, which they described as, quote, "somewhat more capable than Mythos-5." However, Anthropic continued, " Our rough qualitative sense is that this model is a noticeable improvement on Mythos-5 for many tasks relevant to internal use, but does not display a capability jump to the degree observed from Claude Opus4-6 to Mythos Preview."

Anthropic said they have no plans for releasing this model publicly and have not run it through their usual suite of evaluations

Chris GPT pointed out, " Anthropic's new Model 2 doesn't just slightly outperform Mythos-5 as they stated in the report. it scores 62.8% on Anthropic's internal co-benchmark V2 AI R&D benchmark versus 50.3 from Mythos-5 and 54.8 from Mythos Preview."

Also keep in mind the report's date is July 15th, so these reports are already a months-old snapshot of Anthropic's internal capabilities. their [00:08:00] current internal frontier is most likely further ahead

I think that is just important context to keep in mind

as we discuss things like how far behind Chinese models are relative to the state of the art

especially in this new emerging paradigm ofgovernment involvement in US state-of-the-art model releases, the gap between what we're using and what the labs have internally

is somewhat wider than it's been in the past

meanwhile, not wanting to be left out of the game people are noticing that OpenAI staffers have started vague posting about Astra

suggesting that that model, whatever it ends up being called officially, will be in our hands soon



260817 hed_EDIT: IPO up. lastly today, we're staying on the big labs, but moving over to their IPO plans. Anthropic has begun meeting with investors and investment banks, and reports have come in Relaying some details that Anthropic has shared, as well as a few points they stayed away from Anthropic told investors that revenue was up14x compared to a year ago, reaching 11.5 billion in Q2.

That annualizes out to 46 billion for the year

But no updated run rate was leaked to the press The other big number is two trillion, which is the valuation that Anthropic [00:09:00] investors said that they expect from the IPO Anthropic themselves reportedly hasn't discussed valuation, so thisis purely what investors have told the Financial Times. make-- Still, if they achieve that, it would make Anthropic's debut valuation even larger than the one point seven billion attached to SpaceX earlier this year.

It would also mean more than a doubling in valuation from where they were when they raised funds in May. Investors said that they expect Anthropic to reach between a hundred and a hundred and twenty billion in revenue by the end of this year, so around two and a half times where they are currently

Anthropic themselves are a little more modest with their forecasts

And while some investors are extrapolating out this type of growth rate indefinitely, Anthropic themselves are perhaps a little more modest with their forecasts, with Reuters reporting that they see revenue hitting between a hundred and ninety and two hundred billion by 2028. Now the financial press is starting to poke holes in the valuation with, for example, Fortune noting that public stocks typically trade on an earnings multiple, not a revenue multiple

And assuming an average earnings multiple, they write, a $2 trillion Anthropic would need to post annual profits in the neighborhood of 59 to 79 billion to keep pace. [00:10:00] Then again, Anthropic is not being valued as an average company

And we are really working without precedent. I think you can expect to see a lot more of this type of debate in the lead-up to this IPO, because in the absence of clear precedent, all we have is opinion to be argued.

Now, speaking of opinions and just how unique Anthropic is

reported discussions of how singular Anthropic believes they are was actually what started the topic that I will address in the main episode.

So for now, let's end the headlines and move on over into main. Hello everyone

Nathaniel Whittemore: One big change around AI is we've shifted our thinking from how we rank our pages to how do we become the source that AI trusts enough to answer with?

KPMG Aug_EDIT: At KPMG, they're seeing this firsthand. AI-generated results now surface answers directly, often without a single click. that's why they are increasingly focused on generative engine optimization or GEO, structuring content so AI systems can retrieve it, understand it, and cite it as trusted authority this is not just an SEO evolution, but a visibility [00:11:00] mandate. And indeed, the GEO mandate from KPMG is simple: If AI is shaping decisions, your expertise needs to show up inside the answer.

Read all about it at slash us/geo. Again, that is kpmg.com/us/geo



Every AI coding tool on the market does the same thing first. It starts writing code. Blitzy does the opposite. Before writing a single line, Blitzy spends days reverse engineering your entire code base

blitzy July_EDIT: Thousands of agents ingest millions of lines, mapping every dependency, every undocumented constraint, every architectural decision made over the last decade. 

the result is a dynamic knowledge graph that understands your software the way a principal engineer would after 30 years in the building

Other tools guess at context with grep searches and markdown files. Blitzy never guesses. it builds true understanding first, then delivers over 80% of entire software epics autonomously

validated end-to-end tested production grade pull requests. That's why Fortune 500 engineering teams trust Blitzy with the code bases that matter most

See for yourself at blitzy.com. That's [00:12:00] B-L-I-T-Z-Y.com



I cover the capability gap between AI potential and AI reality every day on this show most companies are still figuring out how to start. Robots and Pencils is already launching and scaling. Agentic generative AI in production at large enterprises in weeks. AWS Advanced Tier pattern partner more than doubled in a year

Speaker 11: And they're hiring

50 open roles. If you're someone who knows this moment is different, who wants to be inside it, not watching it, this is worth a look. At Robots and Pencils, the best ideas win, and the team is purposefully kept super high quality

This is the kind of place you look back on as the best decision you ever made. Take a look at robotsandpencils.com/careers 



Nathaniel Whittemore: This episode of the AI Daily Brief is brought to you by Hyperagent where you run fleets of agents your team can manage together New users get 1000 in inference Forget local agents and chat workflows waiting on your laptop to be prompted Hyperagent deploys alwayson agents in the cloud doing real work across the tools your team already uses Marketing's agent [00:13:00] turns competitor moves into landing pages sales agent enriches leads drafts emails and updates the CRM ops agent chases the paperwork and tracks the budget Every agent has access to shared context and follows your rules about scope and approvals It's time you add agents that feel like teammates Hire yours at Hyperagent built by the team at Airtable Claim your 1000 in inference at hyperagent.com/aidailybrief. 

Welcome back to the AI Daily Brief

260817 main_EDIT: one of the things that I try to do on this show is bring you a wide-ranging and representative set of commentary around whatever the big events happening are.

I think this is one of the best ways to understand the news on a deeper level Given that when it comes to how news impacts our world, It's not just the news itself, but how that interacts with how people perceive it

Today, however, this goes a step farther, where the discourse is actually the news itself. As Anthropic's Dario Amodei has waded into the muck of X.com

for a rare public engagement around some concerns about Anthropic

the responses and interaction around [00:14:00] this are more than just insider baseball psychodrama

Given the stakes of this particular conversation

and the outsized role specifically Anthropic are playing in global economic discourse

The comments themselves in this case actually count as news

it started when investor Gavin Baker, CIO of Eutrades Capital, appeared on the All In podcast this weekend

In that interview, he said

Internally, Anthropic is very confident. I have been told by multiple people I trust that Dario has said that Anthropic might be the only private company in the world at some point. Think about that. In this vision, an Anthropic maximalist vision, there's Anthropic, and then there are governments, and that's it.

So there's a lot of confidence. I'm sure they have more advanced checkpoints than Fable up their sleeve. They've executed really, really well. 



I would probably take the under on them being the only private company in the world. I think it's gonna be a long time before they land a rocket

AI,

when former AI Czar David Sacks said, "I might interpret that as a negative signal because it's so hubristic. This is getting into SBF land a little bit." Gavin followed [00:15:00] up, "I would certainly discourage Dario from saying that ever again to anyone

And those comments might have just stayed on "All In"

Had Anthropic's Sholto Douglas not decided to wade in in

He reshared that post on X and said, "Completely false. I like Gavin's takes, but whoever he heard this from is lying so that it fits the narrative some people so desperately want you to believe. The same people will try to convince you Anthropic has no moat, and a sentence later that it might become so powerful it could be the only company left.

In fact, one of the things we are most worried about is economic concentration of power. There is no world where the government should let any company have that much influence. We need competition and capitalism. The AI market is literally the most competitive market in the world right now. Every single one of the largest companies on Earth is singularly focused on getting you smarter, cheaper models.

If it all works out, we'll succeed in reducing the cost of everything to the cost of energy. This is awesome, but it threatens a lot of people's old moats. They're frightened."

For sure with AGI, capitalism gets super weird and what a company even is might look different

[00:16:00] Gavin picked it up from there. " Sholto, thank you for setting the record straight. Larger issue is that multiple very serious people in Silicon Valley have heard some variation of this and believe it to be true, and the reason it is believable to so many is that it is consistent with Dario's public messaging and what he outlined in the essay you shared.

This technology might be dangerous for humans in multiple ways, could lead to extreme concentration of economic power, and therefore needs to be regulated thoughtfully. I agree with the potential risks, and I believe Dario makes all of these arguments in good faith. As discussed on the pod, if one agrees that AI might be dangerous, there are two ways to address this potential risk, either concentrated in the hands of a chosen few companies and politicians via regulation or distribute it widely.

Essentially boils down to whether one believes AI is too dangerous to concentrate or too dangerous to distribute. There are reasonable arguments on both sides, but I profoundly agree with Zuckerberg's statement that, quote, ' The notion that AI is so dangerous that the only safe path is an extreme concentration of power seems inherently problematic.

Historically, hoping that an absolute power 

[00:17:00] will benevolently provide for humanity if sufficiently enlightened has not led to safer positive outcomes.'

Continuing, Gavin writes, "And as Dario says in the aforementioned essay, quote, Some may object that we can simply keep AIs in check with a balance of power between many AI systems as we do with humans.'" Continuing his own thoughts, Gavin says, " I believe this is the best path forward.

I want as many AIs as possible to maximize the odds that one shares my own particular values."

And as Dario notes, no human has ever been able to take over the world. At this point, I think safe to say that Dario has lost the argument. His messaging has failed to result in his preferred regulatory path. The fact that the only solution to the recent incident where an unreleased advanced OpenAI model hacked Hugging Face was an open source model likely ended any chance of strict near-term regulation.

Essentially, every major company other than Anthropic has signed Jensen's letter. However, Dario's messaging has been massively helpful to efforts to ban data centers here in America. I suspect we will see anti-data center advocacy groups running ads using clips of Dario warning about how dangerous AI could be for humans.

His good [00:18:00] faith efforts in favor of regulation are now increasing the odds that AI will not be beneficial for Americans and humans everywhere. I believe there is a reasonable chance AI might help us cure most forms of disease, such that we 

Nathaniel Whittemore: have extended lifespans and can enjoy these long lives in an abundant Star Trek-like future.

260817 main_EDIT: That is the future I want, and I think Dario is decreasing the odds of that future at this point. He is about to be the CEO of one of the most important public companies in the world, and given that the pro-regulatory effort has failed, at least for now, I respectfully think he should make an effort to be a more positive advocate for his own industry.

And if I am wrong, and we do need to regulate this technology, he will be a more effective advocate for this in the future, having been open-minded to the alternative.

For the sake of clarity, I think Anthropic has deep competitive advantages and is an amazing company. Ironically, the main risk I saw to Anthropic a few months ago was nationalization as a result of Dario's own rhetoric and behavior

Now, Sholto and Gavin go on from there. but this is the point where Dario comes into the conversation

Now just for some context, Dario is very rarely on social media. He has been very clear that he hates it. in fact, [00:19:00] he has blamed it for a lot of people misinterpreting him. He currently follows zero people on X

And the last time he posted was June 10th 

to share his essay policy on the AI exponential

Before that, it was April 7th to announce Project Glasswing, and before that, January 26th to promote another essay of his, The Adolescence of Technology

Coming back to his response to Gavin, he says, " Thanks, Gavin, for an es- thoughtful exchange. I don't usually spend much time on social media, but I wanted to engage here because it really brings out the heart of an important conversation. First, on regulation, I think that either concentrated in the hands of a chosen few companies and politicians via regulation or distributed widely is a false choice

I know that there is a sort of Silicon Valley shorthand where regulation equals regulatory capture equals concentration of power. But I've always found this to be an overly simplified picture of the world. Many people outside this bubble think of regulation as something that constrains corporate power and benefits ordinary people. I don't necessarily agree with that perspective either. Rather, I think it's complicated and really depends on what the regulation consists of. But in particular, I think that [00:20:00] those in the regulation equals regulatory capture equals concentration of power frame often underrate the decentralizing power of objective and fair institutional processes.

A crude analogy is that the formal court system can sometimes feel stuffy and elitist, but it does a much better job of defending the rights of vulnerable individuals than the alternative, mob justice. At their best, institutions can vest power in ideas rather than people and thereby decentralize that power That is why Anthropic has always made its policy proposals very carefully.

We try very hard to make proposals that disadvantage or slow down frontier AI companies while advantaging smaller competitors. California's SB53, which we supported, and even the much-maligned SB 1047, which we were ambivalent on, 

completely exempt any company below a certain amount of revenue or model training costs from being covered at all.

More recently, the testing process we've advocated for at CAISI and the White House involves more rigorous testing of frontier models than off-frontier models, something that differentially advantages challengers. Similarly, the Pacing the Frontier letter envisions, or at least Anthropic's preferred implementation of it envisions, modulating the pace of the very best models while [00:21:00] not constraining those who are catching up.

This hurts the business interests of the frontier labs and helps challengers, including open weights. Overall, my view is that AI is structurally a technology that tends to concentrate power for reasons that have nothing to do with regulation. more to do with the extreme implications of the scaling laws.

Open weights do help some with this but are nowhere near a sufficient solution because they simply shift the concentration somewhat to those with the most compute and chips which are roughly the frontier labs plus maybe hardware providers.

By contrast, I think the right rules of the road can simultaneously, A, address AI cyber/bio/alignment risks, B, institutionally constrain the power of the frontier AI companies, and C, leave room for open weights models while also addressing the specific risks that they bring By the way, I do not think that the events of the last months haveregula-- have, quote, "failed to result in my preferred regulatory path."

The approach that the Trump administration is reported to be taking, pre-deployment testing for frontier models and also testing of open weights models when they get closer to the frontier, is one that I am very supportive of, though of course I have to see the details to be sure. I am also supportive of [00:22:00] Demis Hassabis' ideas around a FINRA-like entity This contrasts with six months ago when most of the industry was still pushing for preemption of all state regulation and no apparent federal approach either.

next, in his next post, he continues, " Second, on the messaging around AI, I do not agree that my messaging has been disproportionately negative. In fact, it has been equally balanced between risks and benefits. I've written one major essay about each, and even in interviews where I discuss the risks, I make sure to frequently mention the incredible benefits as well as proposing possible solutions to the risks.

Short clips from my interviews that end up on social media tend to be disproportionately negative, as that gets clicks. In fact, I wrote 'Machines of Loving Grace' because I didn't feel the AI industry was painting an inspiring enough picture of how the technology could radically transform the world for the better.

the bulk of the essay is devoted torefuting skepticism of AI's potential in health and biology and showing why I think it will actually be possible to cure most human diseases in around five to 10 years, as crazy as it may sound to ordinary people, and frankly, to biologists as well.

And if you read my most recent essay, 'Policy on the AI Exponential,' I discuss concrete proposals for how to streamline the [00:23:00] FDA process to make sure the deluge of AI-accelerated drugs isn't slowed down by the regulatory process. I feel the urgency here. I lost my father to hepatitis C only a few years before the development of directly direct-acting antivirals, which cures 95% of patients and probably would have cured him."

I do agree that the public has a negative view of AI and that this is a big problem, but I don't think it is primarily caused by me or any other AI leader warning about AI's risks. I think it is fundamentally a crisis of trust. I think that ordinary people don't trust companies, governments, or the tech industry, and always suspect that we are cooking up some new ways to screw them over.

The causes of this go back decades, and AI is just the latest iteration of it. I don't think that a glitzy marketing campaign with a positive spin, which some have advocated that Anthropic do, is the way to win back that trust. At this point, saying that AI will cure cancer is more of a cliché than it is inspiring, and most people think it is deceptive.

The thing that will work is actually curing cancer. I think by far the most accurate criticism of AI companies, including Anthropic, is that we haven't yet delivered on our big promises to benefit the world. That is totally on us, and I [00:24:00] think it's the criticism you should be making instead of all this stuff about messaging and marketing.

We are, however, doing our best to fix this. Anthropic is ramping up efforts very quickly in biology and medicine, and we hope to have incredible results in the coming years and some early glimmers in the coming months. When we've actually accomplished something real, the whole world will hear about it as loudly as possible.

You have my word on that. But until then, I don't wanna make empty promises, and in the meantime, I feel compelled to speak honestly about the very real risks of AI and how to address them. Honesty is the right thing on the merits, And in terms of public credibility and trust, it is no worse than and may in fact be better than an approach that ignores or distracts from risks which people instinctively understand are real

All right, All right, so very long, but I didn't wanna summarize here given that

the posts are the actual story

So one of the first types of reactions was basically more of this, please Gavin himself responded, " Most of all, I think it is great that you are engaging here in such a constructive, thoughtful way. Open dialogue is a great way to build trust with the public, and these are difficult, weighty issues that I deserve to be debated in the proverbial town square."

Former OpenAI staffer Will [00:25:00] DePue says, "I really think Dario should be writing a lot more in public. This was well done." Jessica Lessin, the founder of The Information, writes, "With just two tweets, Dario Amodei did what he has struggled to do all year. He changed the narrative about himself and gave the chattering classes of tech a far more accessible message to quote regardi-his views."

And his trust comment is, I believe, exactly the point

Now, others weren't so sure that he actually changed the narrative, though

Capturing the feeling of many. 

Austin Allred, 

screenshot of Dario's second post with a highlight on the section, "I do not agree that my messaging has been disproportionately negative

Adding the comment, "Lol. LMFAO."

Onl, Terminally Online Engineer highlighted that same line and said, "Are you kidding me?"

AI commentator Hater wrote

oh, Dario, as usual, you blame everyone else for misunderstanding you or hyping your own words. It's almost like you say something reckless, then later try to gaslight people into thinking they misunderstood you

Former AI researcher Susan Zhang writes

A wall of text and an army of sycophants to thoughtfully not deny the original accusation ofDario says Anthropic might be the only [00:26:00] private company in the world at some point. Oh, and by the way, Dario is totally not spreading p-doom or massive human disempowerment fears.

No, no, 

no, you all hallucinated that and misread it all in bad faith. Shame on you, dear readers and users, for all of your own skill issues

Nathaniel Whittemore: PR expert Lulu Cheng Meservey actually 

260817 main_EDIT: discussed this section of Dario's post in more clinical terms. She writes, "The argument in part two is an interesting insight into how Dario assesses his own messaging. When accused of negative messaging, qualitative, he rebuts that it's roughly balanced in large part because he's written one essay about benefits and one about risks, quantitative.

Implication? He's taking an analytical approach to measuring positivity, but many others are simply going off vibes. So this won't be the last time he and his critics talk past each other."

that it- For my part, I don't think that it's just two parties talking past each other. I think this is an area where Dario is just wrong

or perhaps being willfully unwilling to understand the reality of the world we live in

in my view, you can't on the one hand claim to know And understand that social media is always going to clip the most negative parts

and then go and do an endless string of [00:27:00] interviews with a seeming never-ending torrent of easily sound bitable negative statistics

In the real world of public discourse

Public perception is not shaped by a word counter of how many words in your positive essay versus how many words in your negative essay

And to argue such shows just a radical lack of understanding 

of the actual media environment in which you are going to have to operate

as the leader of an extremely significant company

even-- Now, if you have listened to even a handful of AI Daily Brief episodes where I certainly agree

isn't that I believe that there absolutely is a fundamental trust gap 

the broader world and the labs that is not just a question of messaging and that messaging cannot fix alone But you still do have to understand how messaging plays into this

Nathaniel Whittemore: Others Others picked up on the idea

260817 main_EDIT: that Dario didn't dispute Gavin's original claim. That he had said that Anthropic might be the only private company in the world at some point

Zephyr Z9 made that point, as did David Saxalthough I think that this is more tactical than anything else. Lulu again points out, "Going direct with a personal post 

was the escalation after a senior colleague, i.e. [00:28:00] Sholto, already did the fact-checking and elevated the debate to the level of principles.

So Dario was able to come in and focus on his beliefs rather than having to first debate the details of who said what when."

Still, the bigger critique for many was around Dario's discussion on regulation

Sacks called Dario's characterization of Silicon Valley thinking that all regulation equals regulatory capture a straw man. " Of course," he writes, "treating all regulation as capture would be overly simplified, but almost no one holds that view



meanwhile replits on John Massad

takes issue with Dario's argument that AI structurally centralizes power. He says, " The argument that AI structurally centralizes power because it'scurrently compute hungry ignores 125 years of super exponential growth in compute price performance.

Improvements in algorithms and continued hardware efficiency gains mean there is no reason to assume AGI level capabilities will always require a data center to run. Scaling laws are not laws of physics. They're simply empirical relationships observed for particular architectures, objectives, data sets, et cetera.

Change any one of those factors and you get a different scaling curve."

Meanwhile, for others, the whole thing remains a little too abstract

[00:29:00] writes Silicon Data's head of research, Steve Howe, " Ultimately, the whole discussion can feel self-indulgent to anyone not already deeply inside the industry or AGI-pilled. A relatively small group in Silicon Valley is fully convinced of the accelerating or imminent arrival of systems capable of superintelligence, large-scale displacement, and maximal harm.

To most others, this still looks like a large stretch."

Which is in fact why some agree with Dario That for AI to actually solve its trust issues, it's gonna have to be a show, not a tell

Peter Yang writes, "I 100% agree with Dario that using AI to cure diseases and speeding up the regulatory approval of AI breakthroughs in healthcare could bring 10X the benefit to humanity as everything else combined."

Still, OpenAI's Angel Brodin writes, " My personal opinion, it's an oversimplification to assume that any AI lab can solve the trust problem by doing something spectacular, like curing cancer or achieving some major medical breakthrough. Pharma has delivered some of the greatest improvements in human health and is still one of the least trusted industries.

My friends who are ethically against AI don't feel that way because they don't think it has the potential to do great things. the concern is whether [00:30:00] the company building the technology has their best interests at heart."

Dario is correct that a glossy marketing campaign cannot and will not make people trust AI companies, but people also won't judge AI companies solely by their breakthroughs. They'll judge them by pricing, access, lobbying, opacity, how the economic gains are distributed, who gets to participate in its benefits, and who ultimately holds the power

Dario argues that the public distrusts AI companies because society has spent decades losing trust in powerful institutions. But if that's true, the answer can't simply be asking people to place even more trust in a small number of powerful institutions to responsibly steward this technology

In an ideal future, AI should help distribute power, not just access to technology, but the agency and economic benefits that come with it

That means democratization, individual agency, broad access, affordability, and making increasingly capable intelligence available to more people at lower cost

Now if this, now if at this point your head is spinning around and you're asking, "Yeah, but does anything actually get resolved here?" The answer is, of course, no

But I do think that there are some important takeaways. First, people getting to debate things that were actually said

Rather than [00:31:00] just suppositions that they're making or reports that they're getting, makes for better discourse

Second, as much as he hates social media

these posts themselves show that there is sometimes value in participating in it

And one doesn't have to become Elon posting 50 times a day for that to be the case Third, for Dario specifically

I would suggest that this length of communication might be a better fit for him than he realizes

It's very clear that he's frustrated that people don't read his full posts, but they're like 13,000 words long, man People just don't have that sort of attention span anymore, and so of course they're just gonna grab the statistics. 

same unfortunately with long interviews, even if long is 10 or 15 minutes

This medium of a few hundred words on X is actually much harder for people to take out of context than some other mediums are. Anyone can quickly and easily go check it out for themselves, and many people will

I don't expect nor do I think that Dario should all of a sudden become an inveterate tweeter, but this should absolutely be a tool in their communications toolkit

Fourth and finally, part of why this conversation feels

useful and value accretive is that by having it in public, [00:32:00] other people 

at least get to participate through responses and reposts in a way that they don't with other mediums. Given that the stakes of AI are for everyone, and given that so much of the frustration

Is with a lack of agency around a future that is happening to us The value of this sort of public conversation is pretty disproportionate

Obviously, I encourage you to go check it out for yourselves. Even if you're just making a LurkerX account and never plan on posting it, it is worth it to keep track of this sort of discussion. For now, however, that's gonna do it for today's AI Daily Brief. Appreciate you listening or watching as always, and until next time, peace. 

​ 

Nathaniel Whittemore's audio recording:
