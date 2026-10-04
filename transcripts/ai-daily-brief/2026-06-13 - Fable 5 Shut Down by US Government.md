# Fable 5 Shut Down by US Government — Transcript (2026-06-13)

https://aidailybrief.ai/e/2026-06-13 · Listen: https://pod.link/1680633614

---

[00:00:00] In

this In this emergency episode, we are discussing the US government shutting down Anthropic's Fable 5 The AI Daily Brief is a daily podcast and video about the most important news and discussions in 

AI. 

All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, Robots and Pencils, Scrunch, Blitzy, and OutSystems. To get an ad-free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts If you wanna learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai. And while you're there, check out the new site if there is any specific part of a specific episode that you wanna share with someone Whether it's a number or some stat or quote, There's a good chance that it is now there cut up and shareable for you, so go check it out aidailybrief.ai. 

Hello, friends.

Welcome

Hello, friends. 

Welcome back to the AI Daily Brief. For the first time in the three-year history of this show, News has broken on a Friday afternoon that is too significant to wait [00:01:00] until Monday to explore

Last night, just before nine Eastern Time in the US, Anthropic tweeted, " The US government, citing national security authorities, has issued an export control directive to suspend all access to Fable 5 and Mythos 5 by any foreign national, whether inside or outside the United States, including foreign national Anthropic employees.

The net effect of this order is that we must abruptly disable Fable 5 and Mythos 5 for all our customers to ensure compliance. Access to all other Claude models is not affected. We apologize for this disruption to our customers. We believe this is a misunderstanding and are workingto restore access as soon as possible."

After this absolutely stunning news

journalists and internet sleuths flew into a tizzy to try to figure out 

what the heck had actually just happened

The Wall Street Journal added some color 

reporting that Commerce Secretary Howard Lutnick

had sent a letter to Anthropic CEO Dario Amodei announcing that the new models Fable 5 and Mythos 5 were now subject to export restrictions, meaning usage by customers outside [00:02:00] the US as well as foreign nationals within the US would be prohibited

So where did this seemingly capricious policy come from?

It was apparently a report from another company 

about a jailbreak it had discovered

Anthropic gave more details in their blog post writing, " We received the directive from the government today at five twenty-one PM. The letter did not provide specific details of its national security concern. Our understanding is that the government believes that it has become aware of a method of bypassing or jailbreaking Fable 5.

we reviewed a demonstration of this specific technique being used to identify a small number of previously known minor vulnerabilities. These vulnerabilities all appear relatively simple, and we have found that other publicly available methods are able to discover them as well without requiring a bypass."

And basically from there went on to say

That they just don't buy the US's logic

They point out that in the weeks leading up to the release of Fable, they worked with the US government and many others to red team Fable safeguards for a significant amount of time. They pointed out that, quote, "No testers have yet been able to find a universal jailbreak, a jailbreak method that can very broadly bypass the model [00:03:00] safeguards."

Indeed, they write, "We suspect that perfect jailbreak resistance is not currently possible for any model provider. Every safeguard used in the industry is vulnerable to non-universal jailbreaks, which can elicit some cyber information in specific circumstances, and it is likely that universal jailbreaks will eventually be found in the future."

They said, "Given that perfect jailbreak resistance does not appear to be possible today, Anthropic adopted a defense in depth strategy with Fable 5. We aimed to make jailbreaks either narrow or very expensive to produce, and to combine this with thorough monitoring to quickly detect and shut down any successful attacks."



hearkening back to the controversy of this week, they continue, " This is also why Anthropic has required 30-day retention of customer data with Fable, a policy change that carries real costs for us with customers, but that allows us to research and mitigate jailbreaks."

Importantly, they conclude, we have notreceived a disclosure of a concerning non-universal potential jailbreak that led to a harmful result. The potential jailbreaks that have been disclosed to us are either entirely benign responses or are minor findings that provide no mythospecific uplift.

To date, they [00:04:00] write, the government has only given us verbal evidence of a potential narrow, non-universal jailbreak, which essentially consists of asking the model to read a specific code base and fix any software flaws. Our understanding is that one potential jailbreak was shared with the government.

we have reviewed a report that we believe is the basis of the government's directive and validated that the level of capability displayed there is widely available from other models, including OpenAI's GPT and is used every day by the defenders who keep systems safe

Given that then they write, " We are complying with the government's legal directive and are removing access to Fable-5 and Mythos-5 for all users. However, we disagree that the finding of a narrow potential jailbreak should be cause for recalling a commercial model deployed to hundreds of millions of people.

If this standard was applied across the industry, we believe it would essentially halt all new model deployments for all frontier model providers."

Now, the Wall Street Journal later added, " The jailbreak research in question was done by researchers at Amazon, who used a series of prompts to get Anthropic's models to provide them with information about a handful of security vulnerabilities."

Now Now one note, as people will [00:05:00] clarify, is that although The Wall Street Journal reported 

that the research was done by Amazon

The Journal did not report that it was Amazon who shared the findings with the US government Nick on X writes, "Project Glasswing's whole purpose is to literally do security tests to find vulnerabilities and share findings. Amazon is a Glasswing partner and Anthropic investor. So why would they file a federal complaint?"



togeth-- Now Prinz on X put together a bunch of different posts to try to put together something of a timeline of what happened

They argued that Contra to Anthropic's argument That every safeguard used in the industry is vulnerable to non-universal jailbreaks, and they stated that clearly when they released Fable 5. Quote, "My best guess is that the US government did not fully realize this at the time when the release of Fable 5 was approved."

Now, Prinz added that per Axios, the government contacted Anthropic to ask to pause 

releasing the models, but was unsuccessful. 

as, 

or as they put it, Anthropic told the government to pound sand

Now, it's hard to wrap our heads around just how consequential this is



Risha Sharma was one of many to point out that a huge number of Anthropic's technical [00:06:00] staff, Andrej Karpathy, are not US citizens, but instead here on things like EB-1 visas

Meaning that even internally they are not allowed interact with these models now

So where we sit, at least at 7:32 AM Eastern Time on Saturday morning



is that Fable and Mythos are not available to anyone right now. And you gotta think that there is a flurry of behind-the-scenes activity trying to resolve this as fast as humanly possible

So So what does the chattering class think?



Dan Robust- Dan Robustus on X teed up pretty much the entire conversation when he wrote, " Am I mad at Anthropic or the US government? Both? Probably both. Yeah, it's both."

So let's talk first about the US government side, or specifically the what the hell are you doing US government side

many pointed out

that the specific pretext for this banning is incredibly loose. AI entrepreneur Bindu Reddy wrote, " This is really stupid. The US banned Fable just because it responded with information that is already freely available on the internet.

Every other model can easily be made to respond to some silly questions about common security vulnerabilities or how to make drugs or [00:07:00] whatever. The cluelessness of the government is astounding."

In the Wall Street Journal the CEO of 

cybersecurity firm Letta Security, Moussouris wrote, " Who at the White House evaluated this and thought it was a threat? It's a complete overreaction because this is exactly the kind of prompting that defenders would do

AI policy expert Dean Ball wrote, " I can't tell if this is lawfare against Anthropic in particular or extreme national security hawkery. Regardless, it's simply cartoonish."

Council on Foreign Relations Senior Fellow Chris Maguire wrote, " If the Trump administration is so concerned about access to advanced AI models, Why is it not enforcing the export controls currently on the books on advanced AI models or the export controls that would require a license to buy large numbers of AI chips to make these models?"

Now to be clear about Chris's position, he later tweeted, "I actually think targeted export controls on model access are prudent, but across the board controls on all countries on a single model without any warning is highly questionable."

Export controls are a critical tool and an extremely powerful one. Used correctly, they have the potential to massively extend the US lead in AI. used [00:08:00] incorrectly, they will stifle AI development. The Department of Commerce's export control strategy has been completely incoherent and sabotaging.

It is sending powerful AI chips to China, not enforcing controls that would prevent Chinese smuggling, creating massive loopholes that allow AI chips to be sent to China, and preventing US AI companies from releasing their own models. This has to stop.

We urgently need a smart export control strategy that applies robust export controls to deny our adversaries access to advanced technology while advantaging US companies. Commerce and BIS are consistently doing the opposite. If BIS doesn't understand how to use its authorities or what the implications are of its actions, then it needs to find some new personnel who can actually execute a competent export control strategy.

The current one is incoherent and self-defeating

Many pointed out that it was also hypocritical

Emerson Brooking from the Atlantic Council

reshared a post from the White House Office of Science and Technology Policy from just a couple of weeks ago when they bit back at The New York Times after the NYT reported that President Trump had signed an executive order asking tech companies to give the government oversight of new AI models before releasing [00:09:00] them to the public.

At the time, the White House account wrote, " Lazy and inaccurate reporting on this policy. The EO creates a process for frontier labs to voluntarily share cutting-edge cyber models in order to secure critical infrastructure and strengthen the government's own cyber defenses. We are not conducting oversight of all new models."

and here's the money quote, " As that level of government overreach would have chilling effects on free speech and innovation."

Indeed, the policy seems so baffling

For example, as Dean Baligan put it, " An administration whose posture is that we should export advanced AI chips to China, which also wants to ban Britain and every other non-American on Earth from using our best models. I have no words." Yes, to many the policy is so baffling 

that it feels distinctly personal

Presaging the next point we'll get into, Josh Pigford wrote, Anthropic has not done themselves any favors 

with their hyperbole over the past six to 12 months, but I also guarantee this has zero to do with national security

Now adding evidence to that is when the Department of War CIO Kirsten Davies tweeted, " We fully support POTUS and the [00:10:00] Secretary of War in prioritizing national security and the security of our war fighters, DIB partners, critical infrastructure, international partners, and allies. Some things are simply more important than revenue cycles, clickbait, and pre-IPO val- valuation."

Now, I don't know who approved that tweet

And it could just be Davey's opinion, but that level of animosity 

specifically targeted to Anthropic makes it seem like this has pretty much nothing to do with Fable 5 and everything to do with the relationship between Anthropic and the government

uh, well-known tech journalist, Ashley Vance writes, " This strikes me as so petty and dumb on the government's part. they want Anthropic to do their bidding and are willing to hold the whole country back as a result

Georgetown Law's Peter Harrell is pissed. " I find it ridiculous," he writes, "and un-American for the government to tell me as an American I cannot use an advanced AI model because of a vague and non-public alleged security threat. We should regulate AI, but based on transparent and impartial rules, and not 5:00 PM on a

Friday, dick tots



Joey Politano writes, " All of the worst impulses of the Trump presidency on full display. [00:11:00] No plan or strategy, everything reactive, arbitrary, and maximally invasive."

Anthropic is just repeatedly being singled out because they have insufficiently bent the knee

Putting it even more dramatically, Lasana Next writes, " Trump really wants to kill both OpenAI and Anthropic, nationalize their tech, and then become the emperor of mankind

Now, as much animosity as there is towards the US government

Frankly, most of the industry scorn right now is being levied on Anthropic itself

AI builder Sarah Hooker writes, " You have to be humble even when pursuing excellence. I think the arrogance with which Anthropic has pursued the latest release has universally landed poorly. It is presumed everyone else should just be grateful to touch the technology even if it is intentionally hobbled, and no one else should be given permission to develop the technology because it is too dangerous

Jeremy Howard, who's no hyperbolic ex-poster hater, wrote, "I disagree with this decision and I don't like it, but also how did Anthropic not see this coming? It is the obvious response to 'This is too dangerous for anyone except us to use,' since that relies on a premise, 'We are uniquely good,' [00:12:00] that almost no one agrees with."

Dario Anutmaz, who has spent the last few days not being able to use Fable 5 because it knows that he is a biomedical researcher, wrote, " Happy now, Dario Amodei? You got your wish for government regulation after constant fear-mongering to slow AI progress. Anthropic has done tremendous damage to AI advancement.



they succeeded in realizing this nightmare scenario. It is a sad and grave day for America and humanity

Now, summing up the sentiment behind this was a three-panel cartoon that went viral. In the first panel, a concerned-looking Dario Amodei says, " This is the most dangerous AI yet.

It could kill us all. It will destroy all global infrastructure. This can't be allowed to fall into the wrong hands." In the middle panel, Donald Trump says, "Okay, it's banned." And in the third and final panel, an apoplectic Dario says, "You can't do this!"

investor, entrepreneur, and writer Will Manidis was one of about a bajillion people to point back to an old quote from a recent Anthropic blog post that said, " The government should have the power to block or deter deployment of the model if it is determined in light of third-party assessment to present unacceptable risks."

Will points out, Dario, 48 hours ago, US government should be able [00:13:00] to block model deployment. US government export controls models. Dario says, "Not like that."

Now Now some trying to point out That Anthropic did actually try to address this in their blog post saying, " As we have stated publicly, we believe the government should have the ability to block unsafe deployments as part of a statutory process that is transparent, fair, clear, and grounded in technical facts.



This action does not adhere to those principles

still even with that caveat, a whole lot of people felt like this was an F around, find out kind of moment for Anthropic investor Nick Carter wrote, "I can't believe Anthropic comparing their product to nuclear weapons 800 times backfired on them.

I am shocked

Author Tae Kim writes, "So livid right now. Anthropic overhyped mythos scared the living daylights out of the clueless global politicians like Treasury Secretary Bessent and ECB President Christine Lagarde, and stoked a regulatory panic that may set back the entire AI industry."

Expressing the same sentiment but with a slightly more dispassionate voice, entrepreneur John Ennis wrote, " My opinion is that Mythos is the current best model, but not actually some world-changing dangerous model, and [00:14:00] that Anthropic did their usual song and dance about safety, largely because they didn't have enough compute to serve it at scale.

So then they launched Fable because they still have to think about the IPO, but they are still somewhat compute limited, so they put all sorts of restrictions on it. Around the same time, because they are trying to get regulatory capture and not because things are actually dangerous, Dario did more scaremongering and published his honestly confusing white paper that offered no real solutions.

So finally they succeeded. They managed to freak out the government, their cynical plan backfired, And now it's a giant pain in the butt

Or as Banteg simply put it, " They named it Fable 

and then acted surprised when it came with a moral."

One thing I keep seeing in enterprise AI, companies hedging across every cloud, every model, every framework, or paying a GSI for a pilot that never ends. The teams actually shipping, they've picked a lane and they move fast.

Now, [00:18:00] one Now, one thing that I will note

Is that to their credit, the safetyists are not dancing around excitedly. Eliezer Yudkowsky

who I disagree with pretty vehemently most of the time wrote, " I can't tell today whether this ends up good or bad. International treaties to stop all further AI escalation would be a definite good. Things short of that, complicated.

This has some bad aspects like selectivity and likely overrule, and good aspects like pushing against the psychology of 'but no government would ever dare tell AI companies to do anything, so give up,' or raising doubts that impede venture funding for ever biggermodels So please stop tweeting about how I must be celebrating this.

I'm not one of the kids who immediately goes 

into overacted victory paroxysms about any hit on a perceived enemy. I care about the effect on where things end up a year later, and that's a little harder to know the first day, 

you know?

And in fact, trying to figure out where this leads days, weeks, months, or years from now was where a lot of the conversation resolved

Aaron Levy stating almost the obvious bluntly writes, " This is a big turning point for AI regulation. The government is starting to deem some models too powerful for certain uses, which creates a precedent for a [00:19:00] range of possible controls in the future." I'm in the camp that this is unnecessary, and we should be primarily regulating the use of AI as opposed to the underlying models.

But equally, there are plenty of people who actually prefer this outcome. Either way, it's unlikely that we're going back to a world where the government doesn't have far more meaningful involvement in the rate of AI progress

Andrew Friedman wrote, " This is a moment we'll look back on as a major turning point in AI. For years, people in this community have warned that AI policy would get weird, that these systems would grow powerful enough to put them on a collision course with our institutions, our economy, our governments. I don't know what caused this moment.

I don't know what it means for future models. I can't tell if this is targeted specific to Anthropic, but I can't think of a more overt act of government intervention in our capitalist society in my lifetime. AI policy just got weird

coining a new and I think important term, Sterling Crispin wrote, " The worst thing about this Fable situation is that it just created precedence for capability thought crimes and drew a clear line in the sand going forward. Are the next round of models going to need DOW clearance before release?

New open source models? This is not good for progress [00:20:00] Daniel Jeffries wrote, we're seeing a speed run of a hideous future play out Nobody can build a business on this quicksand and uncertainty. If we continue with this wild gibbering fear-mongering and the fear-based gated access, and if we create the regulatory capturing policies this insane and idiotic and incoherent fear pushes the clueless towards, we will absolutely Guarantee that the future of intelligence gets built outside America

Brian Zhao writes, " If this sticks, this means Americans will need proof of citizenship to gain access to models on the level of Mythos. That means potential ID verification, not just on Claude, but everywhere Fable is served downstream. Cursor, Devon, 

OpenRouter, et cetera.

A law firm that uses Harvey serving Fable 5 will get impacted just the same." Brian also writes, "How is Anthropic supposed to serve Fable through API billing? They will somehow have to figure out a way to verify citizenship of the end user. API access will need to be drastically changed before access, even to American companies and citizens, can be restored.

And of course, researchers at Frontier Labs themselves will no longer be able to use their own models 

Brian points out also that OpenAI and Google DeepMind no longer have incentives to ship anything Mythos caliber until this [00:21:00] is resolved.

If they release it, any company that can jailbreak the model can get export controls imposed on the model, and then they now have to deal with the same headaches Plus any non-US partners with Mythos access through Project Glasswing get cut off. Now that the US has exercised its kill switch once, expect other countries to operate with the assumption that Frontier access Can and will be revoked unilaterally Honestly, one of the moments that I'm reminded of in AI history was when Sam Altman was first removed and then reinstated as 

OpenAI CEO. That was the beginning of the end of their relationship with Microsoft. Now, nominally, Microsoft stuck with them, with Satya Nadella playing a behind-the-scenes role trying to get everything sorted out.

But from a sheer fiduciary responsibility standpoint, from that moment on, 

he had to start putting up walls with OpenAI and building resilience at Microsoft that was outside of OpenAI's models. the company had simply proven itself to be too capricious for Microsoft to trust it and the entire history of how Microsoft has developed AI since has been shaped by that one moment

Connor Brown was one of many to point out the comparisons to the 1990s. He [00:22:00] wrote, "Welcome to the AI wars. We are now staring down the barrel of KYC and anti-compute laundering laws for frontier models. And this is just for Mythos. What happens when we get further capability jumps? Will the public have access to frontier intelligence ever again?

We fought this battle in the '90s for free and open access to cryptography, but it was not easy. The fight this time around will be much harder, and the stakes will be much higher."

Now, one thing we haven't discussed yet, which I think is hugely important, is the impact in markets 

Machine 

Street Talk wrote, " This will become a textbook example of how a company snatched defeat from the claws of victory. Their BS game spectacularly backfired. You reap what you sow."

Daniel Wu writes, " How does something like this not torpedo the AI intelligence explosion bull case? US government establishing precedent that access to anything as smart as Fable 5, which is not RSI and nowhere near AGI will be banned. Even if Anthropic could make the model accessible to US nationals, How will any customer ensure compliance seeing as not all employees of US enterprises are US nationals?

So we have a situation where the labs need to [00:23:00] spend increasing amounts of CapEx to build more powerful models, but are restricted from monetizing them. I do not think the intelligence levels of Opus 4.8 and GPT-5.5 are enough to justify anywhere close to the amount of AI CapEx being spent, let alone projected to be spent."

And And in that scary reality, one person who potentially has a target on their head is Anthropic CEO Dario Amodei himself

Tech commentator Robert Scoble writes, " I can't see how Dario survives another week. Investors in Anthropic are pissed at his leadership

Lasan on X again writes, "The realistic take on the Anthropic situation, investing in AI companies has just become permanently more risky as the US government could pull the plug at any moment

GDP on X writes, " Anthropic IPO has been kneecapped. If Anthropic cannot offer the powerful models to the rest of the world, this reduces their global market share by 25%. Is it then still a $1 trillion USD market cap company?" Open source is already near Opus and Sonnet and will cross that tier soon.

While I duly respect safety concerns, this is very broad and is akin to throwing the baby out with the bathwater. The world is [00:24:00] going to be split by model access

Lasun sharing the Wikipedia post for 1987's Black Monday event on Wall Street wrote, " Trump popping the AI bubble wasn't on my bingo card."

Now, I don't like to speculate on market reactions, and I hope that investors can be a little bit dispassionate. But I more or less am of the belief that at this point, the entire American economy kind of rests on the relationship 

between Anthropic and OpenAI's revenue continuing to go up 



and investors being willing to continue to fund the AI build out

I think the sheer tonnage of damage that this move from the US government does, not just to Anthropic but to the entire US economy, is hard to overstate

Certainly everyone around the world who is not American

has to be feeling very different about things than they were just a day ago

Hemant Mahapatra writes, "

the sovereign AI is real moment is here. Nation states will soon start needing citizenship and or security clearances to work on their next state-of-the-art models the way they do for defense, space, and nuclear tech. It's only a matter of time.

Talent wars here will be crazy Alex Metropolis writes, " This should [00:25:00] be a warning shot for all middle powers. Your access to frontier AI systems is not guaranteed. You need to build and pool your leverage to secure access. A failure to do so is a threat to your R&D, economic, and defensive competitiveness."

Gale Weiner writes, " Up until now, the US position against China has been we are the rule of law, predictable, trustworthy provider. They are arbitrary and politically directed. The asymmetry of the narrative just evaporated."

Any procurement officer in Brussels, Tokyo, or São Paulo who watched this happen Now has a defensible argument for sovereign AI hedging, EU model preference, or cautious experimentation with Chinese open weight alternatives. The DeepSeek and Qwen quality gap is small enough that this matters



British politician TomTugendhat wrote, " Disabling Fable 5 and other models for foreigners is not a misunderstanding or a mistake. It's the inevitable result of technology shaping warfare so that sovereignty is more about code than cannons. With high energy costs and the emphasis on safety not opportunity, Britain's response has been to build the break cutting ourselves off from the future and tied ourselves to the past.

We cannot continue [00:26:00] like this and remain sovereign."

The Europeans account on Twitter writes, " The US government has ordered the suspension of access to Anthropic's frontier AI models, Fable-5 and Mythos-5 for all foreign nationals worldwide, citing national security concerns. Now imagine a European company, hospital, ministry, or public administration that has built critical processes around a frontier AI model.

From one day to the next, access disappears. Workflows stop, services are disrupted, teams scramble to migrate, millions are spent on energy replacements. This is what technological dependence looks like. When access to critical technologies depends on decisions taken by foreign governments, Europe no longer fully controls its ability to act, compete, or innovate."

Writes Harvard's Ben Murphy, " This is another step on the balkanization of technology."

Mal on X writes, " The scariest part of this whole story is the dystopia looming on the horizon. It is the way the US government is literally creating 

a caste, 

system based on access to intelligence. This is even no longer a divide between rich and poor. It's a divide between those who are allowed to think at the frontier level, accelerate science and medicine, create breakthrough technologies, and [00:27:00] those who simply happen to be citizens of another country This is a new kind of Iron Curtain, digital, intellectual, and if they are testing this on Anthropic, who knows who they will come for tomorrow?

Now, Now, I have no idea what happens next. one has to think that the base case is that this gets reversed in some way

But make no mistake, this is an incredibly dramatic step

bring you... I will of course continue to bring updates as they happen, but for now, that's gonna do it for this emergency episode of the AI Daily Brief 

Tomorrow I'll be moving things around a little bit and releasing the short weekly recap episode that I've been experimenting with

And then pushing what was originally going to be the Long Read Sunday episode for some time in the next week or so. Big thanks for listening or watching as always, and until next time, peace 

​
