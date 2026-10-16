---
podcast: "ai-daily-brief"
podcast_title: "The AI Daily Brief"
title: "What Gemini 4 Argon Is Actually Good For"
date: 2026-10-14
url: "https://aidailybrief.ai/e/2026-10-14"
guid: "https://aidailybrief.ai/e/2026-10-14"
host: "Nathaniel Whittemore"
format: "news-analysis"
level: 2
length: "00:30:00"
categories: ["models", "coding", "agents", "design"]
featured: ["Gemini", "Google", "agent harness", "Google Antigravity", "computer use"]
mentioned: ["GPT-6", "Meta Muse", "Claude Opus", "vibe coding", "Claude Code", "Instinct", "ChatGPT", "Claude Fable", "OpenAI Codex", "Claude"]
transcript_source: "publisher"
---

# What Gemini 4 Argon Is Actually Good For

[00:00:00] Two weeks after being announced, Google's new Gemini 4 Argon model is here, available for testing

And the questions abound. Will it live up to its high benchmarks? Can Google finally compete when it comes to agentic coding? If not agentic coding, are there other use cases where Google might now be in the lead?

Today we're looking at the newest frontier model we have access to, Gemini 4 Argon, and where it fits 

The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI. All right, friends, quick announcements before we dive in. All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, Section, Robots and Pencils, and Blitzy

To get an ad-free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts

To learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai. And to find out about everything happening in the broader AIDB ecosystem, go check out the website. You can find access to our past episodes

[00:01:00] Each of which is divided into a million small sharing nuggets to make it easy for you to share with friends and colleagues you can also get access to our free training programs. Or if you wanna go deeper, you can check out the paid training programs that are offered via Superintelligent, like the new AI Champions program that we just announced

Last note today, it's not completely essential, but there are some benefits to consuming this one as a video, given that a lot of the demos of Gemini 4 Argon are video



the episode will be in video on both YouTube and Spotify

NVIDIA will be coming to Apple soon as well 

Welcome back to the AIwe kick off today with some palace intrigue. On Tuesday afternoon, the OpenAI newsroom account posted, " We discovered a sophisticated recording device that was hidden inside one of our offices.

We used our models to understand the device and where it had come from, identifying that a specific employee had planted it a few days earlier. We referred the matter to the FBI and were grateful to the agents and prosecutors who moved quickly to make an arrest."

TLDR, an OpenAI employee has been arrested and charged after a listening device was discovered in an executive conference room. [00:02:00] According to a DOJ complaint, around two weeks ago, OpenAI discovered an audio recording device disguised in toilet paper and plugged into the back of a TV in a conference room at their San Francisco offices As you might imagine, meetings in that room routinely involved discussion of highly confidential technical, commercial, and strategic information

As would come out later, security footage showed employee Abdulrahman Alfozan near the conference room on multiple occasions prior to the discovery of the device

Abdulrahman had no authority to access the room or participate in the meetings held there. Alfazan had been employed by OpenAI for around a year as an engineering lead working on agentic products. He had previously worked for Meta for five years. According to the complaint, Alfazan used a productivity tool to make inquiries about OpenAI's meeting room layout, executive locations, and details of meetings with external partners.

a chatbot owned by Alfazan's spouse was also used for queries related to building a continuous audio recorder, customizing Wi-Fi connectivity, improving audio and live listening, and encrypting the SD card, among other things." The account was also used for queries about the specific device that was found, [00:03:00] identified by its customer header and unique MAC address.

These queries all took place in the week prior to the device being found. Finally, Finally, on October 5th, Alfazan entered the conference room and checked behind the TV, a moment that was captured on camera. The same day, upon searching an unattended bag, OpenAI security personnel found Alfazan's wallet and ID, as well as a second recording device of a similar make.

Alfazan has been charged with attempting to use an electronic device to intercept oral communications, and the FBI is conducting further investigations

If this were just corporate espionage



There would be plenty to keep all of us in the peanut gallery interested. What takes this case to the next level, however, is Al-Fasan status as a Saudi national The suspicion being that this is not only corporate espionage, but straight up international espionage

The DOJ announcement was overt in calling this a potential national security incident. FBI Director Kash Patel said, " According to the complaint unsealed today, Alfadan allegedly concealed a covert recording device inside his employer's executive conference room to secretly capture sensitive communications about the company's super [00:04:00] intelligence technology.

Protecting American SI innovation is essential to safeguarding our nation's economic strength and national security, and the FBI views that mission as one of our highest counterintelligence priorities."

Patel noted that National Intelligence Director Jay Clayton has been working closely on the case. Clayton, of course, also being the newly appointed head of the administration's AI task force

US Attorney Craig H. Missakian added, " The Bay Area and Silicon Valley lead the world in developing tomorrow's technology, and our office will continue to stand at the forefront of protecting that American innovation. For us, it is a matter of national security."

The Bay Area The Bay Area in general and the AI industry in specific 

Have long been a target of international espionage. What makes this somewhat different is Saudi Arabia, nominally a US ally, being implicated Journalists on X got to work unpacking the backstory Scott Stedman from Newsground said that according to his sources 

Alfazan was the only Saudi employee at OpenAI

Adding another piece of red string to the corkboard, Steadman noted that Alphazon is also a venture partner at RAED Ventures, where he works alongside Prince Khalid bin Bader Al Saud Steadman [00:05:00] identified Prince Khalid's father as a member of Saudi intelligence, but officially he's currently the ambassador to the UK

Holding aside the specifics, essentially the point here is that Al-Fasan has ample ties to the House of Saud and the Saudi government to ground suspicion

As far as implications go, OpenAI claims their operations are secure. They wrote that, " "At At this time, we have no indications of this individual inappropriately accessing or exfiltrating model weights, source code, or customer data."

Still, Chris Maguire from the Council on Foreign Relations believes this is an extremely bad look for Saudi Arabia, and if the Saudi government is indeed involved, this should have significant implications for the US-Saudi AI relationship McGuire presented a lengthy analysis that's actually worth reading in full if you are interested.

But to hit the high points, McGuire believes that AI labs will need to harden their security and presume they are already the target of less ham-handed, his words, espionage attempts

For Saudi-US relations, he believes this is a very bad sign. The investigation is being handled by the DOJ's Counterintelligence Division, not the Criminal Division who would handle regular commercial espionage cases McGuire wrote, " If Alfazan was acting in coordination with the Saudi [00:06:00] government, I do not see how any company could possibly host a Frontier AI model in Saudi Arabia after this incident."



Sadly, it is way beyond the scope of this particular show, but there is a lot going on right now in the US-Saudi relationship. And while there are plenty of explanations for this that don't implicate the Saudi government

It is an incident that could have some fairly significant implications for global AI politics



moving over to the much more banal reality of our new agentic era, JPMorgan plans to block third-party agents from accessing customer accounts. During Tuesday's earnings call, agentic risk was top of mind for JPMorgan executives.

CEO Jamie Dimon said, We're not going to allow just any outside agent to come inside the company Because it's just too risky for clients and for JPMorgan. You don't want rogue agents, and it could be thousands of them."

While Dimon seemed to be conflating the scary headlines around Hugging Face, with consumer agents like Muse and Instinct, the bank is still changing its policy

CFO Jeremy Barnum said, " To the extent that we're able to block those, we are blocking them to protect customers and to protect ourselves."

After the call, a spokesperson told CNBC, [00:07:00] protecting our customers is our top priority. Because it is not safe, we do not permit third parties to access accounts by obtaining customers' banking credentials and logging in on their behalf. We support secure customer-authorized data sharing through open banking providers and are committed to enabling agenda connections securely."



this means that agents will likely at some point be able to access account information for basic read-only tasks like making a budget or finding old subscriptions to cancel. But JPMorgan customers are unlikely to be able to get their agents to pay bills or settle invoices

Dimon said frankly that customers don't understand the risks they're running, commenting, " If people are using them, they should understand the risk. They should understand that there's a liability transfer." Essentially, the bank won't indemnify faulty agents in the same way they do for fraud

Now, agentic banking has been a touchy subject since the introduction of Muse brought personal agents to the mainstream. Late last month, Apollo chief economist Torsten Slok warned that agents seeking a higher yield on savings account for their users could trigger a bank run If one puts much credence in that scenario, JPMorgan would be ground zero with an average savings account rate [00:08:00] of zero point zero one percent.

JPMorgan doesn't seem concerned about that particular outcome, but rather the potential liability of personal agent spending without proper authorization Basically, with this policy change, they've made it clear that they won't be refunding customers if Muse goes on a spending spree



AI for Finance founder Bob Su thinks that while this was completely inevitable It's also not the right approach to a real problem. Bob wrote, " Banks blocking AI agents is the most predictable move of 2026.

They're right about the risk, wrong about the fix. Users don't need agents locked out. They need agents locked down. Scoped permissions, hard limits, a kill switch

Meanwhile, on the other end of the spectrum, Shopify has thrown open their doors to agents of all stripes. Last month, Shopify partnered with Muse to allow agents to browse and shop across their platform and the key technical detail was that Shopify would provide API access directly to their backend.

This was a mutually beneficial arrangement. It allowed Muse to produce better results, while allowing API access meant Shopify wasn't paying web hosting costs associated with agents scraping their front end Now, [00:09:00] Shopify has extended this arrangement to agents from any provider. Users can now connect their agent via the Shopify app for a fully supported agentic shopping interface, regardless of whether they're using Muse, Town, Hermes, Instinct, Dots, or any of the other dozens of personal agents on offer The move is part of a broader trend that's seeing two diverging approaches to servicing agents.

Some, like Amazon and eBay and JP Morgan, as we just heard, are locking their platforms down and forcing customers to use their proprietary agents. That approach maintains control of the customer relationship and associated data, but it risks driving agentic customers to other platforms. The other option is to facilitate agentic interactions directly by offering a headless interface for agents, as Shopify has done

The same strategic divergence is playing out in SaaS, where platforms like Salesforce have leaned into headless product by opening their APIs to third-party agents. SAP, on the other hand, has tightened controls on APIs, securing their moat at the cost of customer choice This schism between open and closed platforms is one of the key battlegrounds as agent adoption grows And it's still very unclear which strategy will win out

[00:10:00] Lastly today, Character AI has filed for bankruptcy, marking the end of the road for a once popular consumer AI product. Back in twenty twenty-four, the olden days, Character AI was the first breakout hit beyond ChatGPT, ranking at third place in a16z's list of top consumer AI apps. It allowed customers to create their own character-based role play using chatbots



many assumed that when Google acquired most of the company's top talent in a multi-billion dollar acqui-hire deal that character would be living on borrowed time, but for a while, the company maintained a dedicated following

The bankruptcy tells two stories First, there's the incredible legal liability from playing fast and loose with technology and business decisions. Beyond lawsuits over customer self-harm and chatbots mimicking doctors, Character AI ran afoul of Disney in twenty twenty-five after adding support for unlicensed characters.

The bankruptcy filing states that Character AI has between fifty and a hundred million in liabilities that they're seeking to discharge. Disney has emerged as the stalking horse bidder to salvage assets from the bankruptcy. They've agreed to pay twenty million dollars for certain intellectual property [00:11:00] and recently hired Character AI's CEO to facilitate the technology transfer

Beyond that, there's a broader question about whether a consumer-focused business model can function in 2026 404 Media, who it should be known is pretty wildly antagonistic to AI and tech in general, made the bold claim that the economics of AI don't work based on the bankruptcy filings

According to an affidavit from CEO Colin Adams, Character AI was spending $10 million per month on compute with peak monthly subscription revenue of 2.8 million. Other months saw less revenue, even dipping below a million dollars a month at times

While 404 presented this as a condemnation of the AI business model as a whole



I think the more interesting questions, which don't need to apply to absolutely everything to be interesting

are about what consumers are going to be willing to pay for and how much they're going to be willing to pay, and how that does or doesn't line up with products on offer



discovering that people aren't willing to pay enough for a specific implementation of role-play chatbots



doesn't mean that there's no business model in consumer AI. It means that people didn't wanna spend enough to justify that particular set of role-playing chatbots

Pleometrics summed it [00:12:00] up. " A strange company. They got addicted to free user analytics numbers, dragged their feet on moderation for adult content, and got stuck in this will they, won't they loop. Half measures all around. They missed the boat one too many times."

Wrote computer scientist John Kentman, This is the pets.com of AI. People genuinely do not understand the AI industry. I can't believe people genuinely think that character AI filing for bankruptcy means Anthropic is next."



still an interesting moment as the early phases of AI cede to something different. for now, however, that is gonna do it for today's headlines. Next up, the main episode If you're leading AI inside an enterprise, you already know that the gap right now isn't capability, but execution. That's why KPMG's You Can with AI is back with a new season featuring conversations with leaders like Serojia Chatterjee of Emma, May Habib of Writer, Ellery Fisher, and others focused on practical execution.

What's working, what's not, and what it actually takes to move from pilots to real scaled impact across strategy, data readiness, governance, [00:13:00] workforce, and value. And of course, it's co-hosted by me, Nathaniel Whittemore. Go listen and subscribe at www.kpmg.us/aipodcasts. That's www.kpmg.us/aipodcasts. 

Here's a harsh truth. Your company is probably spending thousands or millions of dollars on AI tools that are being massively underutilized. Half of companies have AI tools, but only 12% use them for business value.

Welcome back to the AI Daily Brief. Today, for the second day in a row, we are looking at a big new model release and what's interesting is that just like yesterday This is a model release from a company that has, for at least the last phase of AI, been considered a little bit behind the eight ball

I'm talking, of course, about Google's new Gemini 4 Argon

And while the perception of Google has been nowhere near as bad as it was for, for example, Meta earlier this year



It's been a bit of a rollercoaster where Google was far behind, only to then launch themselves right back into contention, spending most of 2025 right on par more or less with OpenAI and Anthropic [00:16:00] Only to almost completely miss the 2026 wave ofagents and agentic coding

Gemini 4 Argon was announced a couple of weeks ago at the end of September



but it wasn't available yet, which many took as not such a good sign



still for the very many of us who were quite willing to give Google the benefit of the doubt and not at all comfortable with writing them off, it was really always just a waiting game to see what the model could actually do when we could get our hands on it



as we dig in

It's important to note that I believe that the right question about any new frontier model has shifted

Whereas it might have been before, how good is it?

With the implication being, should I switch? The question is now much more, where does it fit?

In other words, what things does this particular model do well or different That should make me consider integrating it into my overall model stack



ex- so that's what we're going to explore today



to recap the basics from a couple of weeks ago, this is a brand-new model built on a brand-new pre-train after Google scuttled the Gemini 3.5 Pro release earlier this year. It's unclear exactly how large the model is, but Google is presenting [00:17:00] it as an ultra-large model in the same class as Astra and Fable



that, to recap the benchmarks that we got a preview of



at least by the benchmarks, Argon appears to be broadly a match for frontier models from the rival labs. For knowledge work, Argon is state-of-the-art on the VALS index, automation bench, VALS finance agent, and Harvey's legal agent benchmark



and other than the Core VALS Index, each of these benchmarks have a wide gap above competitors. On Harvey's legal benchmark, for example, Argon is 13 points ahead of its closest competitor, Fable 5.1

On coding, the results are more mixed. Argon is state-of-the-art on DeepSui, scoring a few points above Opus 5.5, but on FrontierSui, Argon is behind the three major rivals and about 10 points off of the leader Astra Score Similarly, on TerminalBench 4.0, Argon is nine points behind Opus 5.5, who has the leading score

Although to be fair, that presentation is probably a little misleading

The spread of coding scores has widened with recent updates to the benchmark and although they are behind, Argon is firmly in the frontier range, just not at the head of the pack. Google highlighted a variety of [00:18:00] other benchmarks across agentic science, cybersecurity, and multimodal, with Argon state-of-the-art across each category based on the benchmark selected by Google

One other benchmark worth highlighting, given that a lot of the questions are going to be about agents, is Argon's score on OSWorld, which is the standard computer use benchmark. Argon scored 69.2%, which was just shy of Astra's 72.6%, which when announced was considered a paradigm shift in AI computer use

Independent benchmarking from artificial analysis similarly placed Argon squarely at the frontier. it scored 53 overall, putting it tied for fourth place with Fable 5.1 and GPT-6 Astra. Muse Wonder Full and Sonnet 5.5 are tied for second with 56 points, while Opus 5.5 is in the lead with 58 points realistically, and so we don't get too hung up on the exact numbers, there is now a group of between six and eight models across four US labs with a legitimate claim to being competitive at the frontier Depending, of course, how you feel about GPT-6-1 Soul and Grok 4.7

But of course, we no longer live in just a world of performance, we live in the world of efficient [00:19:00] performance. And cost is a little more difficult to dissect due to the way that Google has rolled this model out. On the On the API, Argon is available with a 50% cost reduction until November 30th.



that allowed the model to complete the AA benchmark run at $199 per task, very similar to the cost of GLM 5.3 and significantly cheaper than all frontier rivals other than 6-1 Sol. Once the subsidy goes away, Argon will be more expensive than Astra, but still around two-thirds the price of the Anthropic models

Trying to sum it up, going purely from the numbers, Argon looks like a frontier AI at a discount, which presumably would put Google back in the game

And And yet, for many, the biggest question to be answered by the release of Argon is, can it code? Coding has been Google's Achilles heel over the past year, and there's been speculation that poor coding performance led Gemini 3.5 Pro to be shelved over the summer

Pavel Hurrin ran Argon through his bug hunting test and found it to be inadequate. It performed about as well as MuSpark 1.3 and significantly behind Astra, Fable, and Opus. Hurrin still gave Google credit for making [00:20:00] progress, writing, " A way better model than Gemini 3.8 Flash. Looks like Google is back."

Noah Dunigan from Railway was less impressed, posting

This model is useless when it comes to real-world code. I'm not mad, just disappointed This, however, actually kind of makes sense for Google. I think they have given up the programming model race and are instead aiming for knowledge workers

Others found similarly not so great results



developer, content creator, and entrepreneur Theo wrote, Just ran Argon on my codebase analysis bench. Not looking good. Only model with a greater than 50% false claim rate."

Dan Shipper from Every writes, " Gemini 4 Argon really struggles on our senior engineer benchmark test. Comes in at 21%, far below Sol 6 and even Muse

Analyst Max Weinbach did respond to Dan saying, " It really depends on the harness you're using. I didn't love it in anti-gravity, but found it was really good in Claude Code and Open Code



However, as some pointed out using the model in other harnesses is technically a violation of the terms of service



summing it up, developer Rishi [00:21:00] writes A A few billion tokens later on data, code, and analysis, here's what I can say. Gemini 4 roughly equals Opus 4.8

Now, going back to Anti-Gravity, one of the quirks of this release that could be causing the difference in experience is that Google decided to differentiate between Pro and Ultra subscribers on coding. Pro subscribers only have access to Argon in the Gemini harness.

You still have access to the Gemini CLI, but that's not the same as Google's Anti-Gravity coding harness, which is their equivalent of Codex or Claude Code. To use Argon in Anti-Gravity, users need to upgrade to the Ultra tier. Pavel Pavel Hurin again noted a huge difference in performance between the two setups.

Running his bug hunt test again, he wrote, Testing Gemini four Argon on real work with Anti-Gravity CLI, not Gemini CLI, changed the score dramatically. Argon went from good to a frontier model, landing very close to Opus five five max. I ran the benchmark three times to confirm the results.

It hadn't worked for me before, and I didn't expect the harness to matter so much."

Marcelo P. Lima summed up the frustration: " "Why Why does [00:22:00] Google make it so hard to try out their new model? I have a Workspace account. I can't pay $100 to get AI Ultra add-on because that's only available to individuals. In order to get AI Ultra access, I have to talk to sales?

This is crazy. Make it frictionless for people to try your product. Your models have all this intelligence. Certainly, you can ask Argon to vibe code a sales page that'll let me buy this add-on

Now, Now, regular listeners of this show will not be surprised that there is a big difference depending on the harness and frankly for Google it would be great news



if model performance was a setup issue, not underlying model capability, given how important that agentic coding use case remains



still still one area that Google's models have always shined is on the multimodal. And given how much every model now has to compete in the arena of social media where videos and 3D renders capture all the attention, you would think this would be an area for strength for Google

Certainly the company released some breathtakingly impressive examples alongside the model. Demis Hassabis showcased a modern version of Battle Chess as an example, with the results looking like triple A game graphics and way beyond in many cases what we've seen from rivals

Chetaslwa was blown away by one of the demos from Google, which depicted [00:23:00] a massive pagoda and temple complex from multiple angles, including a full walkthrough

Others noted that this wasn't a one-shot, but a massive multi-agent run that would've been quite expensive. but still the output is impressive



Professor Ethan Mollick was able to produce a version of his imminence game that he's been using to test different models with similarly impressive visual results

But But others have found much more lackluster results

Max Techno writes

Guys, I'm genuinely confused about Gemini 4 Argon. Just ran Argon High through my old Vibe Check prompt, and I really don't know how to evaluate it. Now, Max's test

is a 3D render of a vehicle that you can look at from different angles. Max continued, " It did a really good job with the car shape. looks much more like the reference than Opus 5.5's, but the colors look completely washed out, the textures are literally floating, the garage scene is still way too basic, and the UI is still stuck in twenty twenty-four.

It was fast, but be real. Would you actually choose this an Opus output with all of these cons?"

Max actually even later wondered whether they trained the model on hyped public tests He said, "It's not close to Opus 5.5 or Astra, and honestly [00:24:00] Solon Sonnet sometimes look way better. It's good at rockets, pelicans, and voxel hype tests, but the second it needs to do anything actually creative It serves junk

So what are we supposed to make of all this?

One of the things that I said about Astra when it came out is that it felt like a model that was really asking you to push yourself farther

Not to simply do the same stuff a little bit better, but to really try and do totally different things



And given some of the multimodal and 3D capabilities of Argon, maybe that's a similar way that we should be looking at this model

Certainly the people who were most impressed tended to be exploring these types of dynamic multimodal advanced or scientific use cases Fah for AI writes, " Argon has this amazing natural understanding of the world. It can do so many things from first principles

Beonx shared a futuristic 3D battle helicopter made purely in Three.js, saying, " Everything you see was procedurally generated from scratch. This is a result of a multi-round self-iteration loop of Argon and Nano Banana

Venture investor Justine Moore wrote, " wrote, Asked Gemini for [00:25:00] Argonne for an interactive museum of Apple computers and didn't provide any images or data. It scraped archival Mac photos, wrote a tool to clean the images, pulled fifty years of specs, and built a three-D cover flow with UI that morphs to match the decade you're in."



in in other words, it is a wildly impressive execution of what she was looking for



Websim Suria

argued that this is really what the model is about, writing, " Gemini 4 Argon is the first model where it felt like an image, video, and language model all at once."



And if that's the case It's not surprising that some of the early tests feel like they're just scratching the surface



The bugged dev wrote, " I feel like we haven't seen enough of what Gemini 4 Argon can actually do. I gave it one image of a Gothic Victorian carriage and asked it to build this whole thing as an interactive 3D experience. Just one image and this is what you get. A one hundred and seventy-four thousand face model from scratch, complete with opening doors, hinged windows, working wheel physics, suspension, flickering lanterns, and and even custom-sculpted skulls.

All of this generated through code, no blender

What's clear is that whatever it's for, Gemini 4 is different

[00:26:00] Ethan Mollick writes, " Using Gemini 4 makes you realize how many other models must be distilling Claude or GPT or using a similar training pipeline. It feels quite different than other models."

Theo agrees that it's different, but doesn't necessarily love that, writing, " It's a huge jump for Gemini and pretty good value for the price, but it's still a Gemini model though. Does weird stuff regularly, and I don't feel like I can trust it at all."

Kavish Krishnakumar tested it extensively with agentic coding and wrote

I've been coding with Gemini 4 Argon today, and I actually completely forgot about the character traits Gemini models have when coding They just love to structure code in a certain way and add comments. Not too long either. Mostly neat one-liner comments, which is a good thing if anything. I kind of like it.

I'm not even certain if the code works yet, which is the classic Gemini trait, but it's just nice to look at code if that makes sense. When you compare it to the other models, their habits are wildly different. It's kind of refreshing to talk to a model that feels to its own model lineage

Expanding out, Google DeepMind's director of AGI economics, Alex Emas wrote, " One thing that's been [00:27:00] under-emphasized is the importance of having true diversity of output at the frontier. Using a single model, there are unmistakable signatures of each in everything from writing to taste in code And this is most obvious in design, i.e.

g, the color palette chosen as background. I've been using Gemini Four for some time now, and I can say it is completely unique. This is obvious from the visualizations everyone is sharing now, but also in the way that it writes and communicates back and forth For an economist, the benefits of diversity and independence are baked into nearly all of our models.

Correlated signals, information, and priors is how you get fragility, learning traps, and AI slop. So I'm very glad to see our big boy out there for people to use

And bringing it all together, Dan Shipper from Every even found at least one place where it doesn't take some wild imagination to consider switching to Gemini for a core use case

wrote, " " Gemini 4 is out and it's surprisingly good? I admit I was ready to trash this model when I saw the benchmarks. But six of us at Every spent the past week testing it across coding, writing, design, and knowledge work, and were [00:28:00] pleasantly surprised. It's a breakthrough if your company lives in Google's ecosystem and a strong option for frontier hoppers as a secondary model for certain tasks."

Some of the things that Dan found was that Gemini 4 was, in his words, "Shaky at refactors, but fast on Greenfields, apps."

Basically that it could build new stuff pretty quickly and efficiently and well, but that it, in his words, cut corners on self-verification in existing code bases. he also noted the problems with the harness, calling it a 2026 model trapped in a 2025 harness.

And I think it's worth noting 

that in addition to missing

eight months of coding model development, Google has also more or less missed eight months of harness UX iteration

Dan put it bluntly saying, " Antigravity, Google's desktop agent app feels six months to a year behind Claude Code and Codex, lacking cloud environments, SSH, a built-in browser, and smart permission checks, leaving you clicking constant pop-ups or using unrestricted turbo mode."

But then it comes to writing, where Dan called it his new favorite writing partner

He wrote, " DeepMind hired professional writers with red pens to stamp out AI [00:29:00] slop, and it worked. I use it to untangle structure and sharpen metaphors. It's got a natural feel for structure and detailed explanations that Astra and Opus lack

The net result, he said, " I keep ChatGPT and Claude open day-to-day and switch to Gemini for when I need an editorial partner to structure a tough essay, sharpen a metaphor, or close read a book. Reach for it for live writing collaboration, fast, low-effort prototypes, or steerable UI and dashboard design, ideally via cursor or the API to skip anti-gravity.

When a model is good enough to force you to use a bad harness, it tells you something."



Given how bad all the other models continue to be on writing

If Dan's results really stick, That alone would be enough for me to spend some time with this model



so when we come back to the question of where Argon fits, the answer seems to be so far

We're not quite sure yet



that writing use case is enough to give it a test. but it does feel like as that one X poster said, that we may be just scratching the surface of this. And once again, we might wanna push ourselves to think about harder, stranger, more unexpected things that we can do with it to really see its full [00:30:00] potential Or alternatively, wait till others do that so I can talk about them on this show and you

can just do the stuff that actually works. Either Either way, I'm excited that we are sitting here on Wednesday in the middle of October with both Google and Meta meaningfully back in the model race. But for now, that's gonna do it for today's AI Daily Brief. Appreciate you listening or watching as always, and until next time, peace. 

​
