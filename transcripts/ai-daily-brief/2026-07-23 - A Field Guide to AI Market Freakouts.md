# A Field Guide to AI Market Freakouts — Transcript (2026-07-23)

https://aidailybrief.ai/e/2026-07-23 · Listen: https://pod.link/1680633614

<!-- metadata -->
Format: commentary · Level: 1 · Length: ~00:25:00
Host: Nathaniel Whittemore
Categories: open-weights, infrastructure, policy, funding-markets
Featured: OpenAI, Anthropic, distillation, DeepSeek, Google, Kimi
Also mentioned: ChatGPT
<!-- /metadata -->

---

[00:00:00] Today on the AI Daily Brief, a field guide to AI market freakouts. The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI. All right, friends, quick announcements All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors

KPMG, Airtable, Retool, and Blitzy To get an ad-free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts. To learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai. Now, one other quick note. A couple people have asked me recently if there are better ways that they can support the show.

First of all, you listening is all the support I need. I appreciate you being here And diving deep with me in this incredibly fascinating and important AI world. Second, already one of the things that you guys do very frequently, which is incredibly helpful for the show, is just sharing it For those who don't know, I recently updated the aidailybrief.ai website to turn every episode into a set of shareable cards.

Some of them are quotes, some of them are themes, some of them are [00:01:00] statistics, and each of them can be shared directly to various social media platforms or as an image that you can put anywhere you want



the most valuable way the show grows is when you share it with new listeners, so that is always appreciated. Lastly, for whatever reason, Apple and Spotify both very highly reward Ratings and reviews



so if you have not at this point left a five-star rating on those platforms, that is helpful as well Mostly though, like I said, I am just excited to have you here as we explore this insane world the one other note today is that it was one of those days where even all of the headlines fit inside the main theme.

So we just have one extended theme for the entire episode. Tomorrow we will be back with our normal division between headlines and main. But for now, let's talk about the patternicity in AI market freakouts and what they mean for the future of AI Welcome back to the AI Daily Brief. We are in the midst right now of our latest round of AI FUD and concern. Now, this one specifically is about Chinese AI and how it might impact the revenue potential of companies like OpenAI and Anthropic, especially as they position to go public later this year or early [00:02:00] next year.

Having watched this very closely now for the last few years, I think there are some pretty clear patterns in the specific ways in which investors get stressed about AI. And so that's what we're gonna talk about today. However, to get into it, we first need to do an update in this particular round of concern

As the Trump administration levies new allegations against Moonshot

Earlier this week, Treasury Secretary Scott Bessent proposed that Chinese AI companies could face sanctions as a response to distillation attacks And while model distillation has been a hot topic for over a year when it comes to Chinese model performance, this was the first time a member of the executive suggested the government might do something about it it Besant doubled down on his policy view on Wednesday, writing in a post on X, " "We We support open source AI and the innovation it unlocks, but open source is not open season on American IP.

When PRC firms conduct covert industrial-scale distillation attacks that cross the line into IP theft Sanctions and entity list designations will be on the table



now now that post came hours after White House Office of Science and [00:03:00] Technology Policy Director, Michael Kratsios, made specific allegations against Moonshot, the creators of Kimi K-3.

Wrote Kratsios: We have information that Moonshot AI distilled Anthropic's Fable for the development of its K-3 model. To do this, they developed a sophisticated internal platform to conduct large-scale distillation against US models, allowing them to quickly switch between multiple methods of access to avoid detection.

AI has also acquired GB300-equipped servers and has accessed GB300s in Thailand likely to train its AI models. The United States strongly supports the free and fair development of AI, including a thriving competitive ecosystem that spans frontier models, specialized systems, open source frameworks, and open weight models.

Legitimate AI distillation used to create smaller, more efficient models plays a vital role in this open innovation ecosystem. However, large-scale covert industrial distillation aimed at stealing proprietary US technology and undermining American research is unacceptable



Now here once again, while there have long been whispers of Chinese labs getting access to NVIDIA GPUs

through illicit pathways across Southeast Asia, this is the first time a [00:04:00] government official has made specific claims about the practice Anthropic head of public policy and former State Department official Sarah Heck confirmed that Anthropic is working with the administration on this matter

With Heck writing, " Illicit adversarial distillation is IP theft that supports adversary military and intelligence capabilities. It is a national challenge that creates serious national security risks for the United States and democratic allies."

Following the posts, The Information reported that the Commerce Department has an active investigation into Moonshot and other Chinese labs for circumventing export controls to access NVIDIA GPUs

GPUs Signal summed up the feeling of many when they wrote, " Wow, am I understanding this correctly? One, put Chinese models on the entity list. Two, force American companies to buy more expensive AI from American labs. Three, watch the rest of the world use cheaper models with equal or better intelligence.

Four, discover that distillation did not magically stop because Washington published a list. Five, make American businesses less competitive globally while raising prices for ordinary Americans. Six, meanwhile, none of this stops Chinese AI labs from becoming better and better. [00:05:00] Congratulations, you protected domestic AI companies by taxing the competitiveness of the entire country. What a colossal mess!"

Now, Now, for what it's worth, it's not even particularly clear how much support Bessent and Kratsios have within the White House. Wired wrote on Wednesday, " The Trump administration is split over how to respond to the rapid rise of China's leading AI models. the debate is broadly divided between parts of the White House, which has pushed for stricter controls on Chinese AI that may soon rival the powerful US models, and the Commerce Department, which has viewed those restrictions as unworkable



sources said that Commerce Secretary Howard Lutnick would prefer to combat Chinese AI with competition. He has pitched incentives for US labs to open source their models and spoken with multiple labs about the idea in recent weeks

Writes Andrew Curran, the Commerce the Commerce Department is apparently arguing strongly against regulation, which they see as unworkable. They are certain to have David Sacks on their side. American open source may have a surprise ally in Howard Lutnick.

According to the report, he's arguing for direct incentives to US open source software to accelerate development so they can match Chinese OSS. Commerce sees this as a way to avoid regulating anyone. apparently Lutnick [00:06:00] has even met directly with leaders at unnamed American labs to discuss how best to accomplish this.



perhaps a rebirth of OpenAI OSS with federal funding? he should meet with Nus and Prime Intellect among others, in my opinion. Exciting developments

Writes AEI's Ryan Fedasiuk, " "This might This might be the most important week for US AI policy so far in 2026." 

now one group that's watching this whole thing very closely is investors there has been a growing concern, the latest in a long line of AI market concerns 

That if all of a sudden enterprise buyers get all cost-conscious and they look to cheaper alternatives, They're going to find themselves moving towards these open China models, undercutting the revenue coming to the major American labs with big implications across the market



And for people who are watching closely, All of this is part of a broader market narrative story that's been happening now for coming up on four years





since the end of 2022 when ChatGPT was

One of the most important AI questions right now isn't who's using ai, it's who's using it? Well,

KPMG and the University of Texas at Austin. Just to analyzed [00:07:00] 1.4 million real workplace AI interactions and found something surprising. The highest impact users aren't better prompt engineers. They treat AI like a reasoning partner.

They frame problems, guide thinking, iterate, and push for better answers.

Since, since since the end of 2022 when ChatGPT was released



which was right in the midst of the Fed rate hiking cycle. it has been AI versus everything in markets

Indeed, back in the early days of the AI boom at the beginning of twenty twenty-three, there was a lot of confusion on why [00:10:00] markets were ripping while the Fed was still raising interest rates. The Fed didn't stop hiking until July, and it became obvious that rate policy would do nothing to deter AI investment.

At this point, AI has become a structural part of the US economy and arguably the most important part

According to Bloomberg, AI investment now represents 25% of US GDP growth, the largest single contribution of any sector in history

JP Morgan analysts claim that since the release of ChatGPT in late twenty twenty-two, AI drove seventy-five percent of returns in the S&P Five Hundred, eighty percent of earnings growth, and ninety percent of capital spending growth. In a very real way then, the AI industry is now the driving force in the US economy and US markets As a consequence of this, the market is extra terrified of AI going badly or reversing because they feel like so much is riding on it

And in this context, AI bubble talk isn't just a catchy headline, but is a persistent and central piece of market analysis



while acknowledging that this is a bit reductive, at this point, one could be forgiven for looking at the American economy as basically a bet on AI being transformative enough to [00:11:00] drive enough revenue to make the infrastructure build-out justified so the party gets to continue

And by the way, even if you're not typically interested in markets, we're now at a point in the AI boom where everyone needs to pay attention and understand the narrative Given that around 50% of the S&P 500 is now AI or AI exposed stocks, that means that even if you are just a passive indexer or contribute to a 401, 

You, my friend, have significant AI exposure. Now, with this background, let's talk about the stuff that freaks investors out



The one that we are living through right now, of course, is cheap models undercutting Anthropic and OpenAI's ability to charge a premium and continue to grow their revenue This is the freak out du jour

But it's had various versions going all the way back to the DeepSeek moment at the beginning of 2025, when the market believed that a Chinese lab had produced frontier AI for a few million bucks when the US labs were spending billions on training runs

Now there were a ton of things wrong with how DeepSeek had been presented. People learned about the difference between compute for training and compute for inference



Some of DeepSeek's claims started to have big asterisks around them

And finally, markets also ultimately discover that DeepSeek R1 wasn't actually ahead [00:12:00] of the best models trained in the US, it was simply the first and only free reasoning model on the market, with OpenAI's o1 still locked behind subscription we now find ourselves at another DeepSeek moment with the release of Kimi K three, which in many ways was teed up with the amuse-bouche of GLM 5.2 when Fable was offline courtesy of the US government



Now to many investors, theoversimplified understanding of the situation is a hardwired belief that Chinese AI is cheap while US AI is eye-wateringly expensive. And it didn't help that K3 arrived just after we had had a months-long narrative about US companies slashing token budgets

Now we are not out of this DeepSeek moment yet, but among other things that will help drag us out is the recognition that while K3 is, yes, cheaper, it is nowhere near as cheap as some believe K3 is currently being served at around a third of the price of Fable or half the price of Opus. That's still a meaningful savings, but it's not pennies on the dollar like I believe many analysts have in their heads

Still, what is real is that US companies are looking for ways to manage their AI budgets

Especially as more agentic use cases come online

with potential [00:13:00] implications for the market success of the leading companies

Now zooming back into previous versions of the Market Freak Out, another one that related to the durability of revenue was the concern around the circularity of revenue. This concern really picked up between the end of last summer and last fall When you started to see graphics like this one floating around showing maps of all the deals that Nvidia and others were making across the industry

While many of those deals were small-scale investments in startup labs and neo clouds

At that point, there had been recent reports that Nvidia had struck a deal to invest up to a hundred billion in OpenAI

some investors saw this potential investment as likely to flow straight back into Nvidia as chip revenue massively and in their minds artificially boosting the bottom line

Now that deal, by the way, ended up closing at 30 billion in February alongside 50 billion from Amazon and 30 billion from SoftBank

And for some, the circular financing means that this isn't just OpenAI and Anthropic's revenue that's suspect, but also a concern that NVIDIA and the other hyperscalers and everyone all the way down the chip supply chain are built on shaky foundations

Now, since Now, since people love analogy, the other reason that circular financing has been a concern is the [00:14:00] history of circular financing popping bubbles. Some credit the dot-com crash to a type of circular or vendor financing coming unstuck.



hardware providers like Cisco would sell equipment to fledgling startups on finance, so when the startups went belly up, the hardware manufacturers were left holding the bag. That practice was actually made illegal in the early 2000s as a result, and there are a few key differences this time



In this case, Nvidia isn't actually participating in vendor financing OpenAI is paying cash for their GPUs

Even if some of that cash is investment money from NVIDIA. What this means is that if OpenAI runs out of runway, NVIDIA doesn't have a debt default on their hands and a massive hole in their balance sheet, they just have devalued OpenAI stock. the companies this time around are also categorically different.

OpenAI and Anthropic are nothing like pets.com in their scale or legitimacy or the scale of their revenue



of m- the next category ofAI market freak out has a chance to come up renewed every few months



That concern is AI companies not showing revenue growing fast enough to justify spend

And this has been the big story for hyperscaler earnings every quarter since the AI build out began. At the beginning of the year, some hint of AI [00:15:00] ROI tended to be enough for investors.



In In January, Meta reported twenty-four percent revenue growth suggesting that AI was driving a boost in ad revenue and that was enough for investors. The stock soared by ten percent that night

As the year continues, investors are starting to ask a little more from the hyperscalers, But some are still able to deliver as an example, On Wednesday of this week, Google showed just how much it's going to take to appease this particular market. They delivered a huge earnings beat, reporting twenty-four percent overall growth And a fairly massive eighty-two percent growth for their cloud division year over year. They're making money hand over fist serving AI inference

But the stock didn't soar

In fact



the numbers that the investors were focused on were not the growth of their cloud division, but the growth of their CapEx spend. Wrote the Wall Street Journal: " Wall Street's tolerance for artificial intelligence investment might seem to have no limits, but Google parent Alphabet found one on Wednesday: two hundred billion."

At the beginning of the year, Google estimated that they would spend between a hundred and eighty-five billion on CapEx, making this only an eight percent increase that can mostly be chalked up to cost pressure in the supply chain.



[00:16:00] And yet still, that two hundred billion dollar number was the breaking point for some. Brian Mulberry of Sachs Investment Management commented, " "The two The two hundred was the do-not-cross line. You can't be offloading this much cash and not talking about it."

Now, likely this is just the psychological shock of a big round number, but it also demonstrates the point. even at eighty-two percent growth, investors investors aren't sure that revenue growth will continue to justify the escalating CapEx. Google stock was the first to see the result, falling by one point two percent in overnight markets



so obviously the market freak out concern of revenue growth not growing fast enough

has a twin in CapEx growing too fast. The more CapEx grows



the bigger the hill that revenue has to climb to justify it

To some investors, the concern is that they just don't understand where this all ends. Hyperscalers have now raised CapEx guidance every quarter for the past three years. Combined CapEx is now looking like it will exceed a trillion dollars next year and could head even higher

Now, Now, of course, part of the challenge here

is that we are just in totally uncharted waters

Seeing companies go from one billion in revenue to 30 billion in revenue in less than two [00:17:00] years has absolutely no precedent in the history of any markets anywhere at any time in history



Now, of course, part of the reason that the bubble narrative from late 2025 calmed down this year was exactly this sort of hypergrowth from OpenAI and Anthropic

Whereas many investors were, counting the number of total knowledge worker seats available, multiplying that by twenty or thirty, and not finding enough revenue to really justify this big CapEx spend



When agentic use cases came online and we started to see employees spending hundreds or even thousands of dollars a month

it helped jog investors to realize that this is not just a different category of SaaS and represents something fundamentally different. Still, fundamentally different isn't necessarily comfortable for investors who like having clear patterns and history that they can draw from as they're making their allocations



and and even in that new context of massive agentic spend, that in and of itself has created new categories of concern

One of the big recurring AI market freakout themes is any suggestions of limits of AI spend. Last year, of course, we had a version of this in the notorious MIT report that claimed that 95% of gen AI [00:18:00] pilots fail

And while the study was absolute garbage social science That MIT should be embarrassed to have its name anything associated with, all that mattered was the headline, and that headline found its way into every desk on Wall Street

This year's version of that is a little less stupid because at least it's based in reality

Which is of course the idea of token caps as companies begin to limit AI use

Now, once again, the headlines are more dramatic than the actual policies Uber is capping users, for example, at $1,500 per month

And Tesla, another company in a similar boat, is allowing workers to use $200 worth of tokens a week

With the ability to request larger budgets

importantly, we've barely scratched the surface on the ability for most knowledge workers to use anywhere near that sort of token budgets, meaning that even if every company adopted similar policies, there is still an enormous amount of growth to be had



But still, the market understands that everyone will be looking for ways to bring their token budgets under control

Creating a new looming threat of cheaper inference



now one now one last recurring market freak out that is worth mentioning for completeness, even though it hasn't been much of a concern this year

[00:19:00] is the idea of performance plateaus that once again lead to reduced spend

If AI performance hits the wall, that limits what it can do, which limits the amount that companies will spend on it, which limits the total revenue growth, which makes it harder to justify the CapEx 

This was the big fear in the fall of 2024 when the major narrative was the pre-training scaling wall There were rumors at the time that both Anthropic and OpenAI had scuttled flagship pre-training runs over the summer as the minor performance boost they were seeing didn't justify the increased cost.

Now, from Now, from where we are today, that argument looks quaint, ridiculous, insane

Like Gary Marcus and Ed Zitron were actively trying to lose you money A few months later, we got a glimpse of AI reasoning for the first time with o1



That pre-training was not the only vector to getting increased performance out of AI

Now Now subsequent to that we've also just seen pre-training very clearly not having hit a wall

With pretty much no one being willing to argue that Fable V isn't an entirely different beast to, for example, Opus III

IIIthe, so if these are all the common categories of investor freakouts that we've seen in the three and a half year history of AI Let's now turn to some important [00:20:00] caveats

First up First up

It may or may not surprise you to find that there is a pretty consistent seasonality to the FUD. It's almost like investors want a reason to not care as much in August now, summer doldrums are a well-known phenomenon in markets

And the AI boom seems to amplify the effect this is not just a theory. There is a ton of research that momentum breakdowns occur over the summer, particularly when momentum stocks like semiconductors are driving the rally

And And this has been a historic summer breakdown. Last week, Morgan Stanley noted that momentum stocks are down forty percent this month, making it the worst month on record, beating the previous worst of twenty-nine percent in early twenty twenty-one

Now, Now, that's not to dismiss all of this drawdown as a quirk of the market. In a note earlier this week, Goldman Sachs said that hedge funds have sold tech stocks in record numbers



but it is still worth contextualizing the fears that you see

with that summer seasonality

Now here's another really important caveat



As much as I might bemoan the fact that an entire generation watched The Big Short, thought Michael Burry was cool, and spent the next decade calling everything a bubble The fact that the market is so determined to have a bubble logic at [00:21:00] all times is one of the biggest things preventing a runaway bubble Every time this market gets a little over its skis, there is a pressure release to moderate it a little

We're just not seeing the frenetic runaway market we saw in 1999 and 2000 with boom and bust IPOs every other day driving 100X gains and massive losses The reason why the late 2025's bubble talk dissipated?

is that agents changed the dollar logic and we saw the numbers show up in Anthropic Rational concern followed by evidence to the contrary



Now, Now, when it comes to how I think we drag ourselves out of this round of concern



one of my strongest candidates

will be an increasing recognition That things like token caps matter far less

than the realization that we're using a vanishingly small portion of the intelligence that we'll ultimately demand.

The room to run will give us room to run



I I also believe that at the speed at which an infrastructure build-out is even possible, it's almost impossible for capacity to grow faster than demand

In other words, building data centers just takes a really, really long time

And half of data centers that were announced this year have either been canceled or delayed. Bears are calling [00:22:00] this a sign that the demand just isn't there, but there is literally zero evidence of this. And the simpler explanation is simply that it's A, really hard to permit and construct a data center, and B data center builders have done a spectacularly bad job up to this point of actually addressing citizen concerns in their communities, leading to an upswell in anti-data center activity

In other words, there are just these built-in road bumps

that will slow things down and give everyone more time to adjust Now, Now, when it comes to this latest round of FUD with China I think one of the ways that it becomes resolved is people realizing that it doesn't really matter if your model is cheap if you don't have the inference to serve Moonshot was completely tapped out of compute on opening weekend, and I think it is extraordinarily questionable Whether all of the Chinese AI companies put together can serve even a tiny fraction of the users that the US companies do

And And lastly, and really importantly Look at the utter explosion

of companies flooding into this new opportunity driven by alternative model architectures and the hunt for cheaper inference. We are seeing routers announced every day. We're [00:23:00] seeing fine-tuning and post-train model plays actually working, many of which are verticalized to specific industries.

We're seeing a flourishing, in other words

of companies flooding in to solve a market opportunity



and that's even before we see these potential incentives for US open source efforts

if those should happen

Investor Nick Carter wrote, " The US government does not owe either of the large labs a business model. If the economics of selling tokens don't work due to distillation, cheap clones, Chinese AI magic, the American enterprise andwill be A-okay. They will benefit from hyper deflation and the cost of digital cognition just like everyone else.

The hyperscalers will be fine. It's just OpenAI and Anthropic that won't be, in their current forms at least. If they're willing to adapt, they can develop new business models. So what if the token merchants don't do well? The Neoclouds will be fine. The internet companies will be fine. The consumers get cheaper queries, the enterprise will still incorporate AI."

The The AI CapEx super cycle will still produce tokens closed weight or not. American firms will consume these tokens



ge-- look, my general base case is that every frontier token for at least the next five years gets bought at a [00:24:00] premium price, even as cheaper workloads come online. I just think the amount of premium state-of-the-art tokens that we're going to be able to produce

we'll still be ahead of demand even with a lot of non-premium tokens being consumed as well I think the viability of alternative architectures and new model approaches relieves larger macroeconomic pressure on OpenAI and Anthropic to carry the whole market by better distributing the revenue gains of AI.



I think natural enterprise inertia combines with the inherent long horizon of the infrastructure build-out to stretch the adaptive timeline in a way that allows the economy to adapt better than if the only factor was raw model capability. And yet, with all of this, I think there will be a never-ending sequence of new FUD which by the way will frequently coincide with preexisting market seasonality.



but also that at the end of the day, these fairly consistent and patternistic market freak-outs Ultimately reduce the likelihood that a full bubble is able to form. Anyways, friends, that is my take. That's what I believe. And for now, that is gonna do it for today's AI Daily Brief. Appreciate you listening or watching as always, and until next time, peace. 

​ 

[00:25:00]
