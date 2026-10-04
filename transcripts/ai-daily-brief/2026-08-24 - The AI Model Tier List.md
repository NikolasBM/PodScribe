# The AI Model Tier List — Transcript (2026-08-24)

https://aidailybrief.ai/e/2026-08-24 · Listen: https://pod.link/1680633614

<!-- metadata -->
Format: news-analysis · Level: 1 · Length: ~00:29:00
Host: Nathaniel Whittemore
Categories: funding-markets, model-strategy, models, infrastructure
Featured: Nvidia, Claude Fable, open-weight models, Nvidia Nemotron, GPT-5.6, Claude Opus, Vercel AI Gateway
Also mentioned: DeepSeek, OpenRouter, Perplexity, Kimi, Grok, Muse Spark, Claude Sonnet, Cursor, Gemini
<!-- /metadata -->

---

[00:00:00] It used to be that when it came to advanced AI models, all that anyone cared about was who was in the lead. Was the model from Anthropic or OpenAI or Google the best one out there? and was it better enough that it meant that I needed to switch right away?

These days, things are getting a lot more sophisticated

Not only have all of these models reached a certain critical threshold where they can just do a lot more than any of those models used to be able to do

the sheer volume at which we are using AI on both individual, small team, and enterprise levels has created a new moment where people and companies are thinking not only about capabilities, but also model efficiency and how they put together complete model architectures or model stacks that can allow for the right tasks to find the right models. Today we're looking at a few ways in which that new moment is showing up in the numbers, as well as analyzing a popular AI YouTuber's AI model tier list

The AI 

The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI

[00:01:00] 

All 

All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, Rackspace, Blitzy, and Hyperagent. To get an ad-free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts

If 

If you wanna learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai. While you're at aidailybrief.ai, you can find out what else is going on in the community Superintelligence next round of agent training programs for executives is kicking off at the beginning of September, and there's a link to register for those.

And this week on Wednesday

We have a free webinar and hands-on lab, Agentic Loops for Knowledge Workers 

will 

which will try to take a thing that has been very buzzy and hypey in developer circles and make it relevant for all of you non-developers

Again, 

Again, you can find all of that at aidailybrief.ai. 



The subtheme subtheme that's gonna run through both the headlines and the main episode today

is about the growing place of open models in the overall model stack. And that is certainly the subtext of our first story



which is Hugging Face apparently courting acquisition [00:02:00] partners

Business Insider reports that Hugging Face is seeking a thirteen billion dollar exit. Sources say they've engaged an investment bank to field offers, but no deal has been reached as of yet the company's last round came all the way back in 2023 at a valuation of 4.5 billion.



that round saw participation from Google, Amazon, Nvidia, Intel, and Salesforce. Since then, the platform has, of course, only grown in prominence.

It started off as a place for developers and researchers and enthusiasts to explore open models that while of course they were interesting and important in a variety of different ways, weren't really in the consideration set for professional or business type of users.

Over the past year, of course, the gap between open models and Frontier has closed

with open models crossing critical thresholds that allow them to be integrated 

into serious business workflows

In and around that change, Hugging Face has become a critical piece of infrastructure, 

hosting the latest model drops that can dramatically change how AI work gets done.

AI commentator Rohan Paul wrote

Hugging Face now hosts more than two million models, one point five million datasets, and one point five million AI apps. A [00:03:00] buyer would be acquiring the distribution layer around those assets, plus the workflow that helps developers find an artifact, judge whether it is safe, and put it into production.

As open models multiply, that coordination layer becomes harder to replace Both Stripe's purchase of OpenRouter and this new interest in Hugging Face look like a bet on persistent model fragmentation as the future.

AI Testing Catalog writes, "To be honest, for NVIDIA it would make a lot of sense." And Jun Song expands, "If NVIDIA acquires Hugging Face and actually taps into that data, they could easily drop an open weight model that beats China before the end of the year."

Certainly Certainly it is the case that one of the underfollowed NVIDIA products is their Nemotron series of models. But if you are paying attention, you certainly get the sense that NVIDIA is getting more and more serious 

about open models as a major piece of the competitive stack, whichcould make this type of deal pretty interesting

Adding some further heft to that idea, on Thursday, independent tech journalist Eric Newcomer reported that poolside

had accepted what amounted to a partial acquisition deal from NVIDIA. NVIDIA will pay six billion dollars for a non-exclusive licensing deal to access Poolside's [00:04:00] 

technology, 

alongside a billion dollar equity investment at a twelve billion dollar valuation.

Poolside was founded in 2023 by a former GitHub CTO to train open source foundation models geared towards software development. As part of the deal, NVIDIA will hire over 100 Poolside engineers away from the company to work on future iterations of their yep, exactly, Nemotron models.

Sources said that this is the bulk of Poolside's engineering team, but according to the letter sent to Poolside investors, quote, "This is not an acquisition and it is not an acqui-hire." A key distinction is that unlike other huge acqui-hire deals in recent years, the founders and key leaders will remain at Poolside and will continue operating the startup with a focus on unspecified research projects Sources said the plan was to staff up the Nemotron team for an attempt to build the world's most powerful open models to rival Chinese labs like DeepSeek and Moonshot specifically.

In that same letter to shareholders, Poolside's founders wrote that the deal was intended to create a future where AGI, quote, " Would not be a closed technology controlled by a few, but one [00:05:00] built by many out in the open." Ellie Bakasha of Prime Intellect wrote, "Wow, this is 

kind of 

a shock.

From what I understand, Nvidia bought the model factory part of Poolside and a lot of employees, researchers, got offers from 

Nvidia."

Founders staying at Poolside is unusual. wondering if they will just become a Neo cloud/compute provider since I don't see any mention of PIC, Poolside Infrastructure Company here

The Wall Street Journal reports that the deal came together in a hurry over recent weeks as a result of a busted fundraising round. Poolside founders wrote to shareholders, " At the end of last year, we had a six-week window in which to raise two billion dollars 

to pay for a forty thousand GB300 cluster coming online in January.

We didn't close it in time, and we lost the cluster." 

They said they dusted themselves off and got back to work but quickly realized that they would run out of compute and capital as soon as next year. In their view, NVIDIA was the perfect partner to carry on the work of building a frontier open coding model

Now, just to add further heft to the idea that NVIDIA isgoing deeper on model training, last week The Information reported that the company is taking part in the latest fundraising round for data labeling startup Mercore And [00:06:00] notably, NVIDIA used MerCore for reinforcement learning on their last two Nemotron models

On Sunday night, The Information added reporting that NVIDIA is also participating in a new fundraising round for Perplexity. The round would value Perplexity at thirty billion dollars, a fifty percent markup from their last fundraising round almost a year ago. Sources said that NVIDIA was initially interested in a licensing deal that would allow them to hire some staff, but are settling for a normal equity investment Now, I think the chattering classes in the AI world are gonna have a lot to say about this one, so I would expect we'll hear more about it.

But the point is that it's very clear that across all of these deals, NVIDIA is putting serious consideration into research, talent, training data, and the app layer 

as they look at the growing importance of the open source frontier

Now back to NVIDIA's core business The Information again reports that NVIDIA has begun notifying customers that the price for top-end Grace Black and Vera Rubinchips will increase by as much as seventeen percent. The change applies to chips already ordered and set to be delivered next year.

The price for a full seventy-two chip rack of Vera Rubens

is expected to reach eight million dollars, adding five [00:07:00] billion to the cost of building a gigawatt of compute. Writes The Information, "It isn't clear whether cloud providers that buy Nvidia chips will eat some of the price hikes or pass the cost to customers that rent the chips.

One person with knowledge of the price hike said cloud providers will almost certainly need to pass on the increases to their customers." Bloomberg suggests the price increase stems from the spiraling costs of memory. Nvidia already trimmed the amount of memory to be included on some Vera Rubin systems, but that hasn't made them immune to cost pressures.

Overall, it seems like further confirmation that companies are positioning for a memory shortage that will stretch deep into next year or even longer

longer. now speaking of positioning to deal with Alibaba has raised ten billion dollars in a record-breaking share sale. the secondary share sale was executed on Friday at the market close, completing the largest offering of its kind in the Hong Kong market.

Shares were down as much as ten percent on Monday morning, their largest intraday drop since April of last year. The sale suggests that China is ramping up their AI build-out and starting to pull capital from every available source. Vaser Ling, the managing director at Union Bancaire noted this is a [00:08:00] departure from Alibaba's tight management of share supply, asking, " Why not bonds?

It tells me that they may need more funds than we expect for AI investments and also that they may be rushing to be ahead of other companies."

Big shorter Michael Burry was outspoken on Alibaba following the US tech giants into the AI CapEx wars. In a Substack post, he wrote, Alibaba is making serious inroads in the commodity low-cost LLM bloodbath in the US.



it is impressive as a disruptive force, and I believe this will continue. But I cannot bless share issuances. This is a new paradigm again for Alibaba, and its return on invested capital will continue to fall."

Elsewhere in the Chinese markets, a massive IPO marked the beginning 

of the humanoid robot hype cycle. Unitree Robotics went public on Wednesday on the Shanghai Stock Exchange, raising nine hundred million dollars and debuting with a market cap of nine billion It appears that the offering was severely underpriced, with the stock surging more than four hundred and sixty percent on the first day of trading.

Bloomberg intelligence analyst Ian Ma said

Unitree's debut surge signals strong appetite for China's embodied AI [00:09:00] sector. 

IPO proceeds should accelerate AI development and commercialization. Now, the information does note that a huge day one pop isn't all that unusual for Chinese IPOs. In fact, this is now the fourth IPO this year that rose by more than 400% on day one.

A range of regulatory guardrails help boost day one performance mechanically by limiting selling

But the Chinese market also features smaller companies going public with much larger returns, which is a little bit different than the scenario here in the US

US

Lastly today, a 

bit of a narrative violation. Dr. Dre, at least, isn't worried about AI taking over the music industry. In a profile in The New York Times, the rap legend and his longtime producer, Jimmy Iovine, said thatthey believe that AI is good for music

Said Iovine, " I'm very pro-AI in music creation. I don't see the downside at all. There will be some crappy music. There's crappy music now. In the studio, when gifted people have AI, they're going to make better records

At the same time, Iveen acknowledged the AI companies have the worst public relations in the history of the world. I don't know the history of the world, but let's just put it this way, they have terrible communication [00:10:00] skills. That's why everybody is all up in arms



Dre agreed completely adding, "

I don't see it as a threat. I think the only people that see it as a threat are the people who have trouble creating. I had a discussion with a few people a few days ago. they were against AI, and I'm like, 'Okay, you sound like the person who would've been against the drum machine when it came out or synthesizers, right?

It's a new tool for creativity.' Some people are afraid of learning new things. I'm embracing it. I can't wait to see what's going to happen with this

Dre said that he is extensively using AI in his work, particularly to see how the model might do it differently, kind of the musical equivalent of brainstorming. Iovine noted thatTimbaland is also making use of the tools, commenting, " There's a lot of closet AI producers out there."

Dre added, "That's a good way to put it. They're using it. They just don't want to admit it."

interview. I think it's a super interesting interview

particularly because music to me has always provided some of the best reason to not be concerned about AI infringing on creativity

that, if you're interested in that discussion, 

Go dig up the interview I did with Rick Rubin from last year

Where we get into why he as well views AI simply as a tool in the next generation of things that great musicians are going to use to create great music

[00:11:00] For now though, that's gonna do it for today's headlines. Next up, the main episode 

Welcome back to the AI Daily Brief. One very common kind of content that you see on social media these days is the tier list

list 

Even back since before social media became a thing, People have always loved listsIt's why there's a billboard

and a Forbes list and so many other examples

but on the internet, especially in the short-form video era, we really, really love putting things into tier lists. in other words, ranking them on a sort of grading A, B, C, D type of scale, with the very top being S tier, which depending on who you ask, stands for either supreme or superior or just nothing and just S tier, and you just know what S tier means

Over the weekend

AI entrepreneur and content creator, Theo 

put 

together an AI model tier list. And as they do, it generated a ton of discussion

at the top of the list, he had Fable 5 in S tier. GPT 5 Six Soul was in A Kimi K3, DeepSeek V4 Flash, and [00:15:00] GPT 5.6 Luna were in B. 



Grok 4.6 and MuSpark 1.2 were in C. Then below, yes, MuSpark Down in D tier were Opus 5, Sonnet 5, 

5.6 

56 Terra,

and 

Cursor/SpaceX AI's Composer 2.5

DeepSeek V4 Pro was in F tier.and down in their own sad tier below F, called the Google tier, was Gemini 3.7 Flash and Gemini 3.1 Pro

Now we're gonna explore this idea of a model tier list today, 

Not just because it's fun to debate, although it is, but because one of the main things that's happening right now is a diversification of our model stacks. This is certainly happening on an individual level, and increasingly it is happening on a business level, where organizations aren't simply picking one model or another, but building an infrastructure that can move between models based on different needs and different tasks

there's even a category of businesses that are made to do exactly this, the router companies

the best known of which, OpenRouter, was just acquired by Stripe for $7 billion

And even mainstream media is [00:16:00] picking up on the idea

that the AI model war is no longer just about the pure state of the art. Although of course they're doing it in a very incomplete kind of way

You You might have seen this chart from the Financial Times flying around social media this weekend

The header of the chart is Anthropic's best model, Fable 5, has drawn limited sales

And it shows that across business spend on Anthropic, remains by far the most dominant model.

In the last few weeks, as Opus 5 has come online, it has also outpaced Fable 5

in fact, at the moment, Sonnet 46 and Fable 5 are at pretty common levels

Now, for some folks, this was very surprising. Investor Dan Robinson wrote: " This is pretty surprising to me and makes me rethink some assumptions. Are so many enterprise use cases really saturated by Opus? I can't really imagine not wanting for simpler tasks."

now his comment section reflects a lot of the discourse about this chart that's flown around X and other places which is to say that it's confidently sure that businesses in general are making a very conscious decision not to buy Fable because it's too expensive

without either A, understanding the [00:17:00] context of where this data comes from, or B having any real experience with what AI in the enterprise actually involves

from, this data comes from the Ramp AI Index

And was shared by Ramp's lead economist, Eric Karazian abouttwo weeks ago

Now the RAM team is great

and the work they do putting out economic analysis of AI is really good and incredibly valuable to the industry

but with this one, it was pretty clear to me that they had missed the analysis. when Era introduced the chart, he added the summary statement, "A model so powerful it was briefly banned, 

And yet businesses don't think it's worth the price. Except I don't think that businesses making a conscious decision that Fable 5 isn't worth the price has very much to do with this at all. It certainly might be a part of it. But one thing that was completely missed in the diagnosis 

was the fact that Fable 5 has a 30-day data retention policy. it was part of the provisional safeguards that came with it when the model came back online after being shut down by the government

that all on its own is enough for a huge number of enterprises to say absolutely not

There's just no way that causing all sorts of [00:18:00] serious infosec and data concerns justifies upgrading to the next model when the models that don't have that data retention policy are still quite powerful

fact-- And if you need evidence that this is in fact a big part of this, just look at how aggressively in the past week OpenAI have been pushing their zero data retention policies for frontier models

Now to Aaron Ram's credit, he actually came back later and said, " A lot of replies from employees who say they aren't allowed to use Fable because Anthropic is required to retain prompts for 30 days for US government safety checks."

and that's not the only thing here

As Simon Smith points out This data not only comes from Ramp, which is an extremely tech-forward company that only other pretty extremely tech-forward companies are interacting with

but comes specifically from a token and spend management product that users are using to try to minimize costs

Simon writes, "Ramp data overall suffers from selection bias, and this data suffers from it even more so. This is from their token and spend management product, so users are predisposed to focus on cost control. Fable simply isn't [00:19:00] cost-effective for most tasks."

there is also the startup world blind spot showing through here, where the idea that it's shocking that enterprises in general haven't adopted a model that's just a few months old kind of misses the glacial pace at which most enterprises move.

that, shocking though it may be, I hear from people every single day who are still using GPT 5.2 And other models from nine months ago because that's what their companies give them access to

which which is not to say that the leading indicators don't suggest that enterprises are in fact getting more model fluent and building more complete model stacks

This week, for example, The Information profiled AT&T and reported on their attempt to use open source models to cut down on their AI bills. AT&T's plan, according to Vice President of Data Science Mark Austin, is to hold spending with OpenAI and Anthropic flat over coming years and slowly supplant that use with open models.

The company has around 100,000 staff and has embedded AI into workflows across every department, ranging from coding and financial analysis to HR and customer [00:20:00] support.

The vast majority of AT&T's AI use is internal

And the company claims that they are already using open models to service forty percent of employees' AI queries. They plan to ratchet that percentage up to between sixty and seventy percent over the coming years

Austin said that he's found that open models are just as good or better than previous generation models from Anthropic or OpenAI, which were already up to the task. AT&T still uses frontier models for advanced tasks like generating code, but for simpler use cases like summarizing a PR, AT&T is now using an open model.

Austin said, "We expect that to just keep getting better going forward."

By the way, it's worthnoting that the models that AT&T is using include NVIDIA's Nemotron, as well as open models from Meta and Google AT&T is also making extensive use of model routers drive further savings.

For AI coding, Austin said that the use of a router has decreased cost by as much as fifty-six percent, while quality only fell two percent

Now when it comes to competition with China, although at the moment they're not using any Chinese models, they are analyzing the risks of including them in the mix. and one thing which could change how they view that equation is that [00:21:00] Austin noted that switching to open models allowed them to host part of the service in their own data center stocked with NVIDIA and AMD chips, which was often cheaper than renting compute from cloud providers

The point being that thinking about what different models are good for compared to one another is in fact more than a vanity exercise and will be something that enterprises do more of

even if the Financial Times is just grabbing a chart that they can use to reinforce their preexisting narratives. Now Now back to Theo's list

Theo didn't only publish the list, he put a companion video with it

And to give a few of the highlights from that before we get into the takes

let's talk first about GPT 5六 Soul at A tier and Fable 5 at S tier

On 56 Soul, he says, " It's capable of things I never

thought AI would ever be able to do. It's unbelievable what you could do. It's my default model I use for most things most of the time, but it's not the most intelligent model I use. It's still not my favorite for writing important code I actually hope to merge."

Now on Fable, he writes, " Fable knows more than any model I've interacted with. unbelievably thoughtful." He notes that it still trips over things [00:22:00] and touches things that it shouldn't sometimes, that it takes unnecessary shortcuts and occasionally loses track of what it's doing

He calls Fable 5 a genius that needs to be tamed, whereas Five Six Soul is a slightly dumber robot that does exactly what you tell it Interestingly, even though he rated Fable five as the only S tier above GPT 5.6 Sol's A tier, he said, " If I had to pick, I would pick Sol. It's the model I default to.

I would miss Sol more than Fable. But Fable is the best model. It's the model that writes code I want to merge. It's the model I trust to double-check work from other things. It's the model I talk to about hard, deep things with...things I want to build or areas I want to explore.

Fable five is the next generation. 5.6 Sol is an unbelievable model that feels next generation while still being built on the last generation of tech." Fable is that genius at the company that no one wants to work with, but no one wants to fire because they're the smartest person there. If you learn how to work with them, it's incredible

Now what's super interesting about this Is that this is pretty similar to my experience right now

On any on any given day, at any given moment, I am jockeying between [00:23:00] these two. and for many tasks

I initiate the task in both of them, and after a little bit of back and forth, decide which one I wanna hone in on, which tends to be but is not always Fable

To To some extent though, what's way more interesting than the A and S tier is how he ranks the other models. because the other models aren't trying to compete with Five Six Soul and Fable 5. They are meant to do different things

A really great example of this is that Luna which is presented as the least capable of the three GPT 5.6 models. he has ranked a couple tiers ahead

of the theoretically balanced middle Terra model

Of Luna at the B tier, he says

it's not there because of coding, but because it is, in his words, " Smart, fast, and good at a bunch of random stuff." Luna, he says, "Is probably my most used models by sheer calls to it, not because I'm doing code with it, but I'm doing a bunch of other stuff with my code."

The things that he's referring to are things like categorizing code, pulling from GitHub, reading content. Basically, he doesn't trust it with things that aren't reversible



Now meanwhile, of Terra, he writes, " Fits in such a weird place. A lot of these numbers can [00:24:00] be gotten for much cheaper with Luna. I'd rather use Sol on high because it's going to be much faster because it generates fewer tokens. I have never chosen Terra for anything, and I would be surprised if many people do.

It makes sense on a pricing chart, but doesn't make sense in reality for me."

and I think what's interesting and what this reflects is that because we are just now coming into this

model stack and complex model architecture type of moment where companies are realistically thinking about

Different models for different tasks

We're starting to get more conscientious trade-offs in model design with companies actually competing not just at the state-of-the-art but for various types of performance efficiencies based on what they hope people will do with their model And as that transition happens, it's likely to me that you see a lot of models fall in kind of an uncanny middle, 

where they are neither frontier state-of-the-art models worth the premium that they cost, but are also not the most efficient or fast models for other types of use cases

For example, although Theo likes Kimi K3, he reminded people in his video that it's not as cheap as people seem to think. That just because it's open weight doesn't mean it's cheaper, and that in fact, it [00:25:00] costs slightly more than Sol on extra high, given that Sol does more with fewer tokens

Now in terms of other people's responses

You get the impression that a lot of folks are just shilling for their personal favorite. and given that a lot of this analysis comes from X, as you might imagine, 

one of the most common commentaries was that Grok 46 needed to be higher

And yet one other strand of analysis came from Noah, who said, " I have zero understanding of how people develop opinions about ModelNow ever since Sonnet 4.5, to be honest. They're all fantastic, bro."

Feddy's intern writes

One of the reasons I hope we reach AGI is that I'mtired of these modelconnoisseurs opining nonstop about subtle pseudo differences between the models. This is starting to look like arguing about your favorite color or your favorite Pokémon.

In a few years, we will laugh about all this. Even Theo in his video says, " Whether you're using expensive best-in-class stuff like Fable or surprisingly cheap and effective stuff like DeepSeek V4 Flash, it's kind of hard to go wrong. I don't think a tier list is the best way to compare models right now because there's so many axes to compare on: task capability, cost, token efficiency, speed, et cetera."

And in [00:26:00] many ways, what becomes more interesting than the tier list

Is the combined composition

an, and an interesting source of data for what that composition might look like and how it's changing comes from Vercel

Vercel CEO Guillermo Rauch

recently showed how the balance of open weight models versus closed weight models had shifted on their AI gateway product

In terms of the share of tokens used On June 24th, a couple of months ago, closed model tokens represented around 72%, while open model tokens represented around 28%. that, two months later that ratio has largely flipped With closed at 38% and open up to 62%.

Now, if anything, the Vercel Gateway data is going to be even more heavily biased towards developers as it is specifically positioned as an AI routing tool for developers

And yet to some, it still shows where the winds might be blowing. Investor Gavin Baker shared the chart and said, " More data that open source AI is taking share from OpenAI and Anthropic."

Super impressive given that the sum of OpenAI and Anthropic accelerated in July. So net token and [00:27:00] AI infra demand accelerated even more than the acceleration we saw at the frontier

In Gavin's estimation, open source AI taking share is positive for AI infrastructure demand as it lowers margins at the model layer and an open source token costs justas much compute to produce as a frontier token. Nothing about open source AI inference is free. Gavin predicts, "Most likely end state in my opinion is that closed frontier tokens are60 to 90% of economic value, but only 15 to 25% of tokens."

Doubling down on the conclusion, investor Daniel Newman adds Two very important points here from Gavin. One, open source models will be the highest utilization and consumption over closed source. Two, Frontier will still realize most of the economics because premium intelligence commands an economic premium

MIT's Christian Catalini thinks that it will actually split in three different ways

the first spend category is cheap generalist, which is the commodity open weight models. on the other end of the spectrum is the state-of-the-art generalist, i.e. the tokens from the closed labs. And then in the middle, in the category he's adding, is what he calls the state-of-the-art specialists

[00:28:00] Those that combine open weights with enterprise proprietary context. Now while obviously Microsoft's models are not open weights, this is the type of thesis that Microsoft seems to be pursuing with their Microsoft Foundry product, which allows companies to use their own data to post-train and build on the base of their MAI models

Although I think there's a lot of reasonable debate to be had around just how common that will be across all enterprises

don't li- what's clear is that we don't live in a world anymore where the only thing that matters is what's the best model. Increasingly, it will be important to understand where different models fit for different reasons, and even enterprises

that yes, move more slowly and stay a little bit more connected to a single ecosystem Are probably going to want to set up environments where small groups of users can test various approaches 

to 

look for these new types of efficiencies

but does this mean that the days of getting excited about the latest state-of-the-art model release are gone?

We'll have to see. A lot of chatter that Fable 5.1 is coming shortly, although it appears that OpenAI's Astra has been delayed until September chance, so we'll have a chance to find out soon

For now, that's gonna [00:29:00] do it for today's AI Daily Brief. Appreciate you listening or watching as always, and until next time, peace. 

​
