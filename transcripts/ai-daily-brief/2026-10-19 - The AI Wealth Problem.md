---
podcast: "ai-daily-brief"
podcast_title: "The AI Daily Brief"
title: "The AI Wealth Problem"
date: 2026-10-19
url: "https://aidailybrief.ai/e/2026-10-19"
guid: "https://aidailybrief.ai/e/2026-10-19"
host: "Nathaniel Whittemore"
format: "news-analysis"
level: 1
length: "00:32:00"
categories: ["safety-security", "funding-markets", "policy", "infrastructure"]
featured: ["Anthropic", "agent harness"]
mentioned: ["distillation", "Claude"]
transcript_source: "publisher"
---

# The AI Wealth Problem

[00:00:00] 

Anthropic is proposing to give away hundreds of billions of dollars in public benefit funding So everyone's pretty excited about this, right?

In fact, it's bringing up a lot of interesting, important, and sometimes difficult questions about not only the opportunities but also the challenges of AI wealth, as well as the relationship between highlyconcentrated AI wealth and power and the public sector and democracy at large

These are poised to be some of the biggest questions we face as a society in the coming years

The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI. All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, Robots and Pencils, CData, and Blitzy. To get an ad-free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts.

And if you wanna learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai. 

[00:01:00] Welcome back to the We start off today with a story that many are paying attention to because of what it potentially reveals about the world we now live in

OpenCode suffered a major cyber attack that could undermine support for open source alternatives to the big labs.

On Friday night, users saw linked API accounts running up massive bills in the hundreds or even thousands of dollars in some cases. 

By Saturday afternoon, OpenCode acknowledged the attack, writing, " We had a security breach last night related to a large-scale distillation attack that impacted 1.4% of OpenCode console users." They said that the attack was still ongoing at that point, and they were working with OpenAI, Anthropic, and Google on remediations.

If you are not familiar with their service, OpenCode offers an open source coding harness akin to Codex or Claude Code. Users typically bring their own models, storing API keys with OpenCode. This was the attack vector with the full database of user API keys seemingly exposed Even OpenCode founder Dax Rad was vulnerable.

On Saturday afternoon, he posted, " My personal accounts are being attacked now too. [00:02:00] Whole new world with AI-powered hacking."



OpenCode warned 

users that they need to rotate their API keys, not just revoke access Anthropic said that they were mitigating the damage on their end and were revoking any compromised keys that they could detect And as the weekend continued, we got some additional details about what the attack involved.

On Sunday morning, Dax posted, " They've been nonstop trying to attack our systems for the past 48 hours. A side effect is everything is getting hardened, but damn, we basically need agents going 24/7 because that's what they have."

This sounds similar to the Hugging Face incident where a swarm of agents pounded the servers for several days. The Hugging Face agents rapidly spun up infrastructure to avoid shutdown, moving much faster than human defenders could

Like Hugging Face, Dax said he ran into the issue of Frontier Model Labs blocking cyber tasks, leaving him reliant on open source models He wrote, " That was a bit frustrating mid-incident when trying to investigate. They did quite a bit, and then they started refusing. We got access to Daybreak Blue now, so it's better."

Daybreak Blue is OpenAI's vetted cyber defender program, [00:03:00] and Dax said he is now running continuous defensive agents using the service Overnight on Sunday, Tebow from OpenAI confirmed that damage mitigation had concluded on their end with API keys reset and refunds issued to impacted customers 

The 

The story is still evolving and presumably we'll have a lot more information later in the week. But at first glance, 

There's reason to think that this incident could have a very significant impact. It appears to be the first instance of an agentic swarm carrying out a large-scale malicious attack Now, OpenCode said thatthe hack was related to a distillation attack, which is causing a little confusion on X.

It seems that user API credentials for OpenAI, Anthropic, and Google were used to generate a ton of tokens very quickly for later use as synthetic training data

That doesn't necessarily imply a Chinese lab was behind the attack With API access potentially being sold through black market resellers.

However, it does imply the hackers were able to directly monetize the attack by stealing valuable digital services rather than just digital information.

The attack could also have big implications for how AI companies deal with security. Services that store API keys are now looking a lot more like financial [00:04:00] services and will need to beef up their security, likely with always-on defensive agents

Former AI czar David Sacks used this moment to advocate for widely distributed cyber-capable models. 

he wrote, " This illustrates the point I've been making about the limits of centralized approaches to SI safety and cyber." And yes, I apologize for some time We're going to continue to have to deal with White House allies using the term SI while everyone else continues to use AI.

But in either case, Sachs continues, " The only durable response is decentralized. d-- make powerful models available so defenders can build and run their own cyber defenses. The only solution to SI-powered cyber attacks is SI-powered cyber defense."

Dean Ball of OpenAI called the lack of access to Daybreak a, quote, " Fairly modest hindrance that was quickly resolved by being granted access to a trusted access program, so seems reasonably fine versus the cost of enabling sustained autonomous cyber attacks? Question mark."

And this is a pretty good proxy of the debate right now. Is the right approach

specialized access granted by the labs who can whitelist someone as part of a program? Or is it just having the models more generally [00:05:00] available? Now, another big potential implication is the swinging pendulum of open versus closed models. OpenCode is the leading open coding harness and could be suitable for enterprises looking to go multi-model One user on the OpenCode Reddit said that they were pitching the service to their company, but the compliance department will

likely now shut it down

Like I said, 



there will presumably be lots more to come For now, we are officially in it

Welcome to the new era of cyber

Meanwhile, over in markets, Wall Street is on edge as analysts call an AI bubble burst The past few weeks have been full of extremely bad news for the Neo clouds

First, the failed Firmus IPO leading into a massive drop in CoreWeave bonds. Charles Gasparino of Fox Business has seen enough, writing in the New York Post, " The AI bubble is about to burst and a big market correction is coming."

The article was a list of comparisons to the end of the dot-com bubble, with Gasparino concluding

But Common sense and history teach us it won't last. The correction is coming to AI and all the companies tapping into its technology through big spending, much of it using debt, the main ingredient of [00:06:00] any crash. If history is any guide, it's time to take your profits and not get greedy. or pray that whichever AI you're betting on will be a survivor of the crash that's coming

Now, I will leave it to you

to decide what it means 

that 

that op-ed is being presented in the New York Post. But the signs of pain are more widespread than just the neo clouds, who have taken an absolute beating over the past couple of weeks.

Semiconductors are in the middle of their longest correction since two thousand and six, with the Philadelphia Semiconductor Index down eight days in a row for a total loss of twelve percent. This is all weighing on the major Nasdaq index, which lost more than five percent last week

Of course, there are still pockets of optimism in the middle of the drawdown. Nvidia CEO Jensen Huang told Bloomberg on Friday, " All of this is going to pass, and the reason for that is very simple. It's going to be transformative. It's going to impact in a very positive way every single industry and every single country.

There's no question it will continue, and we're at the beginning of that."

Elon Musk used an AI-generated video to highlight that compute supply is still insanely tight. He claimed that SpaceX can't find spare capacity at AWS, Google, or [00:07:00] anywhere else at the moment Ark CEO Cathie Wood, who knows a thing or two about investing in tech hype cycles, isn't concerned with what she's seeing so far.

Wood said, "The fear out there actually is good. I'm talking about fear that AI, we're in a hype cycle. We do not believe we are, but the fact that people are afraid means we are not in a bubble." She added, " While some people might say we're in the first inning, we would say we're still in the parking lot before we enter the baseball game.

We're very optimistic about semiconductors generally, about cloud computing, neo cloud computing, because we've barely begun in AI."

whatever innings we're in

Inevitably, comparisons to the dot-com are gonna be left wanting. Opinions differ on the true state of demand, but we're certainly not hearing about massive overbuilds and canceled spending. Mostly, we're just seeing investors demand a little more to finance risky data center projects through the bond market.

That's crimping valuations for NeoClouds

But that's very different to the dynamics that burst the dot-com bubble

Some more evidence of that comes from spot GPU rental prices, which are up seventeen days in a row now

The question to ponder is what it means if neo [00:08:00] cloud debt funding dries up

And at this point, for those of you who wanna go deeper in markets analysis, what I would recommend is to shy away from anyone whotries to use big overarching terms

or weighty if inaccurate historical comparisons, and instead look for the people who are trying to get into the actual specifics 

Meanwhile, Microsoft has pulled the plug on a multi-billion dollar UK data center deal over energy delays. According to The Telegraph, Microsoft has canceled their contract to build a large-scale data center in Essex. The site has faced multiple delays, with local utilities most recently saying they don't expect to connect the facility to the grid until the twenty-thirties.

It was originally intended to come online next year. This is a huge blow to Endscale, who position themselves as the UK's sovereign data center provider. Microsoft represents forty percent 

of their one hundred andthree billion in contracted revenue, although this site is believed to be a small portion of that amount Still, Endscale has been attempting to go public in an IPO deal that would make them one of the most valuable AI companies in the UK.

They had been seeking a valuation of thirty billion, but according to Bloomberg, a group of investors have been pushing management to [00:09:00] settle for a valuation that's in the sixteen to nineteen billion dollar range. That would represent not a huge jump over their last funding round, which reportedly valued the company at fifteen billion in September.

The contract being canceled is also a pretty big blow to market confidence. This is one of the first high-profile projects to get mothballed and another high profile in the OCloud generating some terrible headlines

To take the optimistic read, this cancellation isn't, again, about a lack of demand or other structural issues with the AI industry. Per the reporting, it seems to be a narrow case of a data center without aclear path to electricity supply. That could say something about the scarcity of capital, essentially that Microsoft can't afford to have theirbudget allocated to a facility that won't come online for several years

more broadly, it could indicate that we're past the frothy part of the data center build-out when hyperscalers were signing 

contracts with brand new companies with zero track record

record For the sake of the full breadth of takes we have on the one end of the spectrum from Ben Bridgeman

Microsoft still has substantial contracts with Enscale. The recent issue in the UK is about power availability, not a lack of demand for Enscale's capacity. Are we really surprised that building enormous [00:10:00] data centers in the Arctic Circle presents logistical challenges? And then on the other end of the spectrum 

from nobody special on X, " N scale IPO not looking good here.

How long until they start using the word contagion to describe what's happening to Neo clouds?"

clouds?" Lastly Lastly today, one from the Anthropic IPO files. New York City Comptroller Mark Levine has urged Anthropic to pause their IPO for safety reasons. In a letter sent to Anthropic last week, Levine wrote, " Anthropic and five other companies recently signed a quote-unquote morally binding accord with the White House, which is insufficient to meet the moment."

Before going public, the company should prioritize addressing the myriad safety concerns surrounding AI threats and establish a governance regime that matches the seriousness of the concerns being raised by you as well as industry researchers, policymakers, and the public The demands of preparing for a public offering diverts resources and attention from this very necessary work

Now, if you're wondering why on earth should we care if the Office of the Comptroller of New York City 

is upset with Anthropic, That is a very reasonable question The Office of the Comptroller is incharge of a range of different [00:11:00] financial auditing and oversight functions for city government.

But in this instance, the office wrote in its capacity as the investment advisor and custodian of the three hundred and twenty-five billion dollar New YorkCity pension fund. In other words, this could be a representative opinion from a deep-pocketed investor It might reflect the type of thing that others are thinking about as well. Levine noted that Anthropic's IPO filings contained eighty pages of risk disclosures, more than twice the length of the section describing the business. The letter stated, "These disclosures are not routine and indicate risks that are without precedent, let alone at a public offering of this scale."

The Comptroller is calling for a similar level of detail on Anthropic's plans for auditing and controls to deal with this risk The letter also called attention to

reported attempts to grant super voting shares to the founding group, giving them contracted control of the company.

Levine argued, "A gap between control and accountability is especially concerning for investors given the unprecedented risks the company has already acknowledged." The letter was sent before Anthropic's Thursday blog, which discussed the appointment of Meter as the first external auditor with employee-like access to the company.

However, the comptroller seemed to be asking [00:12:00] for a far more detailed plan and a specific timeline

Anthop-- given the gravity of Anthropic's own concerns, Levine called on Anthropic to pause their IPO so the company can fully address safety issues Levine appeared on Bloomberg TV to discuss the Anthropic IPO, noting the company had opened discussions with his office following his letter

He wasn't able to characterize the discussion, but said, "It does appear they are under pressure from multiple sides right now. If they go public and then there is a catastrophic safety incident far beyond what we've seen right now, that would be terrible for their stock. Much better to take a little time right now and get this done."

Levine is assuming the indexes will rush Anthropic in as the Nasdaq 100 did with SpaceX earlier in the year Some of the city's pension funds are invested in the major indices, so they would have forced exposure over a relatively short timeframe. Levine noted there's risk for the markets either way, commenting, " Some people are making the opposite point, that if they delay their IPO, then that in itself could be a problem for the market."

However, he continued, "I worry about going public and then having an incident."

in-it's beyond the scope of the headlines to get into 

but why I think this is an interesting moment is that it [00:13:00] dramatizes a lot of the issues that are gonna come up

As I've said before, I have a very hard time thinking that people are going to be comfortable

with Anthropic's plan for super voting shares. And I think you're gonna see a lot more resistance to that

But more broadly than that, there's an interesting question

of the risk of an incident happening after Anthropic or OpenAI is public and that dragging the market down

versus the increased visibility and transparency we get with a public company

I think there's a fairly strong argument that you in fact want these companies public as soon as possible

if we want more of a hand and an influence in determining their direction. In any case, that is gonna do it 

for today's headlines

welcome back to the AI welcome back to the AI Daily Brief. 

Today we 

are talking about how AI is going to change the world, but in this case, it's a very different aspect of that conversation

Anthropic has just announced what amounts to a significant philanthropic arm

Over the weekend, they wrote, " We're committing a portion of Anthropic shares to the Anthropic Public Benefit Fund, a new wholly owned entity dedicated entirely to the public benefit. It will start off with five percent of our shares. For every fifty percent increase in the company's value over a set baseline, we can contribute an extra two percent subject to our board's discretion.

In total, this means that roughly twenty percent of Anthropic shares are committed to the public good. Our co-founders have already pledged to donate eighty percent of their equity, and around half of our employees are donating a portion of their equity as part of a donation matching program we've run since our founding."

In the companion blog post, they go a [00:17:00] little bit deeper into some of their theory of change and how it relates to the beneficial mission of the company as a whole. They write, "As a public benefit corporation, most of our work in pursuit of our mission takes place inside the company.

Research relevant to AI safety and interpretability, applied biomedical research, discounts on Claude for nonprofits and scientific institutions. These activities have both a public benefit component and for-profit value, so we house them directly in the company The Anthropic Public Benefit Fund will have increased flexibility and scale, enabling us to pursue our mission in new ways.

For example, we might explore large donations to traditional nonprofits or direct distributions to specific populations

The example they give is labor market impacts, where they say not only might they use this money 

to study these issues But they imply heavily that they might just give money to people as well

As they put it, given the pace of AI progress, bolder approaches may be needed



they do note that this is not going to be a 501[c][3], the

traditional structure for US nonprofits

Instead, it will be a wholly owned LLC which [00:18:00] they say is to, quote, "Give adjustability between different forms of giving."

They do pledge

that none of the equity held by the LLC will be used for lobbying or political giving 

although many of the skeptics are specifically skeptical about that



a number of Anthropic employees took the chance to say that this was part of what made them passionate about their company. 

Engineer Jason Clinton, said that he had pledged half of his equity and added, " This was the principal reason that I left Google for Anthropic.

The existence of this kind of program was a costly signal that Anthropic wasn't just talk at a time when Anthropic didn't even have a released model. Fund a bright future

Now what's interesting is that although we are starting to get details

The philanthropic world has been looking over at AI wealth for a while

and starting to prepare for a very different paradigm

this,

earlier this year, Nan Ransohoff, a Stripe executive focused on public good, wrote a blog post called The Third Wave of American Philanthropy

Between the OpenAI Foundation holding26% of OpenAI and Anthropic seven co-founders pledging to give away 80% of their wealth

Nan wrote, " I was doing some simple napkin [00:19:00] math to wrap my head around the scale of what's coming and radicalized myself in the process. I had dramatically underappreciated thescale of the philanthropic capital that's about to become available and the corresponding gap in talent and organizations that will be needed to make the most of it."

NAN estimates that over the medium term, AI will likely add between thirty-seven and a hundred billion dollars per year

in intended philanthropic spend

now that's estimating the OpenAI Foundation's 26% at the company's valuation at the time of $850 billion and Anthropic employees and co-founders' commitments at their then current nine hundred billion dollar valuation. obviously those numbers are all smaller than what we're dealing with today and what we anticipate at the IPO to, added up, Nan estimates $370 billion in total philanthropic assets

The 37 billion she gets to

by guessing at everyone wanting to spend around 10% per year

The 10% she gets to

by taking the in-between on foundations that pay out an average of five to nine percent of their assets per year versus donor-advised funds that pay out an average of 20 to 25%.

She points out that that thirty seven billion per year could go up quite [00:20:00] quickly

If A, the valuations double She writes, "In a handful of years," although that's basically already where we are 

and if, as she puts it, maybe these donors want to increase their target annual spend from 10 to 15% because they're especially worried about the AI transition

That's what gets her to $100 billion a year in target annual spend on the top side

Compare that to current US charitable giving, which is around $600 billion per year This would represent somewhere between a six and 17% increase in annual spend.

Now, it's a little bit beyond the scope of today's show, although if this is something that's interesting to you, I will absolutely get into it given that a lot of my early background is in the philanthropic and social entrepreneurship space but the rest of Nan's post gets into why it's actually going to be quite difficult

to positively spend all that new money

She points out that, in her words, "We're short thousands of philanthropic startups and the talent to run them, that we need elite capital allocators who can deploy $50 billion a year well

And that neither of these things is super easy to fix

Like I said, there is a lot of thinking that's going into this right now. So if this is a subject that's of interest to you, I'm happy to go deeper. [00:21:00] Coming back, however, to the Anthropic Public Benefit Fund

There were, as you might imagine, a lot of responses

on the negative side, a lot of the folks that view Anthropic

as the chief purveyors of the doom and gloom narrative are concerned about all the funding going to that

Writes Accelerationist spiritual leader Beth Jasos, "this is going to be doomer NGO bonanza forever

Given Anthropic's tussles with the administration this year there are also plenty of right or right-leaning commentators

that reject the idea that this money won't be political. summing up that strand of discourse

is Polymath from X who writes, "This is going to be an NGO slush fund. This is a bribe to left-wing politicians to get them on board with AI so that they will follow Anthropic's lead on any policy or regulation."

open, perhaps the more if not nuanced critique, then at least open question around this was summed up by former AI czar David Sacks, who said, " You've put 20% of your equity in an LLC. Whether it serves the public good remains to be seen

And there are plenty of folks Who are asking, in this context, what does public good or public benefit actually mean?

[00:22:00] of, pointing to the part of Claude's constitution where Anthropic discusses principles encouraging consideration of non-Western perspectives, Anduril CEO Palmer Luckey writes, " The problem is that their definition of public good is helping everyone else, not the American public.

If they would commit to helping America and Americans, that would be one thing, but this reeks of USAID 2.0, just another way to funnel billions out of our own economy

Bloomberg's Joe Weisenthal, on the other hand, thinks it's fairly rich for arch-capitalist entrepreneurs and VCs to be telling Anthropic what to do with their funds

He posts, "Lots of people telling another company how they should spend their money

But in some ways, this is just speed running and accelerating difficult conversations that have always been had around philanthropy

Jeremy Flores on X posts

The public good is something determined by the public itself, and the public has a say in its administration via democratic controls over a democratic state. This instead is your company stealing everyone's work, dismantling the state, and then deciding who gets resources Now hold aside the very clear position that Jeremy is coming from, 

given that he's [00:23:00] accusing Anthropic of stealing everyone's work

The first part of his post actually gets to a question of philanthropy that has been around since the Gilded Age

Ma-- social reformer Jane Addams

wrote a piece for The Atlantic in 1899 called The Subtle Problems of Charity

This was, of course, another moment in American history where people were very uncomfortable with the recent power acquisition of private enterprise relative to other institutions like democratic institutions.

And the essay's a meditation

on how far philanthropy can go and where democratic process has to begin

Adams wrote, " Probably there is no relation in life which our democracy is changing more rapidly than the charitable relation, that relation which obtains between benefactor and beneficiary. At the same time, there is no point of contact in our modern experience which reveals more clearly the lack of that equality which democracy implies."

we find in ourselves the longing for a wider union than that of family or class. And we say that we have come to include all men in our hopes, but we fail to realize that all men are hoping and are part of the same movement of which we are a part. [00:24:00] many of the difficulties in philanthropy come from an unconscious division of the world into the philanthropists and those to be helped

It is an assumption of two classes, and against this class assumption are democratic training revolts as soon as we begin to act upon it

And so bringing it back to the Anthropic Public Benefit Fund

What would it even look like to give the beneficiaries more control in how the resources are used?

lawyer Gabriel Shapiro wrote, "Notice how they always have to stay in control. God forbid you just airdrop 5% on the public. No, they have to be able to monetize their own stock while determining how to spend it on things deemed by them as benefits."

perhaps a more impactful version of that comes from Elon Musk, who said, "I recommend giving the shares directly to the public."

This is what I will be doing

Andrew Curran pointed out that this actually reminded him of another company's policy He wrote, " Elon says that instead of putting shares into a public benefit fund, he will be giving shares directly to the public." Back in April, 

OpenAI also proposed a public wealth fund that would distribute returns directly to US citizens through a dividend

Now as to the mechanism of [00:25:00] this

Mach33 founder Aaron Burnett wrote, If Elon means by donating via Invest America, i.e. Trump accounts, then I think this is a very good idea. The single most optimistic future is one where the entire next generation owns a piece of SpaceX. Ownership is amongst the most American ideals.

Owning a piece of a spacefaring future is next level American optimism." Elon simply responded to that, "Yes."

for some, for some, the interesting question

wasn't about the specifics of the redistribution, but about what was going on inside Anthropic 

that made it feel like this was important to discuss now Token Gremlin wrote, " In short, Fable55 is the best model in the world, and we're so confident it'll print money that we're planning how to redistribute the wealth of a model that doesn't even exist publicly yet Lumen avenge simply writes, "What on earth do Anthropic have internally to be doing this?"

on sim, commenting on a similar post

four Lex four referenced 

another recent anthropic research paper saying they've seen 17% GDP growth in 2030

Now the report that had that 17% number also had a detail, 

About Anthropic, reducing and then ultimately ceasing to hire junior technical [00:26:00] talent in fairly short order Joel Stein wrote, Pretty wild that we're seeing this about the Public Benefit Fund at the same time we're learning that Anthropic is on track to cease hiring junior technical talent by mid-2027."

And indeed to some, this is basically Anthropic announcing privatized UBI

AI aggregator Andrew Curran again writes, "The most significant line for me is direct distributions to specific populations. It sounds to me like they are planning their own form of self-directed global universal basic income."

Now getting at why a private UBI is quite different than a government program

Prinz on X writes, "You can't have UBI that is also only to specific populations."

Now, one group who was interestingly absent from the discourse were the AI safety folks

And looking around, it seems like they were too busy being angry at Anthropic about their new proposed AI safety bill to comment on the public benefit fund Politico reports that Anthropic is pitching their own AI safety bill to lawmakers right now. A confidential draft has been quietly circulating around Washington and was provided to Politico last week through an anonymous source.

[00:27:00] An Anthropic spokesperson confirmed the existence of the bill and commented, " This bill represents the proposals outlined in Anthropic's advanced AI framework, which we have been advocating for with federal and state lawmakers since June. These are sensible policies we believe Congress should act on."

The bill would allow the government to block the release of a model if it poses a foreseeable imminent risk of causing more than a billion dollars in damages or killing more than fifty people 

the risk must arise from the creation of a bioweapon, an AI model evading the developer's control, or a cyber attack.

This is similar to the way safety thresholds are defined in state AI bills in California and New York. In addition, the bill would require independent evaluators to assess safety protocols at frontier labs. These evaluators would be required to register with the Commerce Department but would be independent of the government.

the evaluators are tasked with reporting, quote, "imminent enumerated risk" to the Commerce Department, establishing the basis to block a model. Blocking a model's release or use 

is adjudicated through the federal court rather than as an administrative matter within the Commerce Department.

And notably, the language of the bill expressly prohibits 

[00:28:00] any other, quote, "department, agency, or officer from suspending a model's development, deployment, or internal use

that seems to be targeted at similar incidents to the Pentagon's use of the supply chain risk designation to disrupt anthropic models from being used by military contractors

Finally, the bill includes various safety requirements from the state legislation, such as mandating the creation of safety protocols and reporting of major safety incidents

As I said, the AI safety folks are not happy about this If Anyone Builds It, Everyone Kills It co-author Nate Soares writes, " Anthropic's proposed law would make it even harder than it already is for a court to block or restrict the development of an AI that threatens all humanity."

Others were mad at things like federal preemption from state rules. Geoffrey Lidish writes, " This seems insanely dangerous coming from Anthropic. Dario has called on the government to slow things down, and this bill would remove the ability for states to do exactly that while making it very difficult for the federal government to actually stop dangerous training runs."

Now others pointed out the inherent problem with definitions in these types of bills

David Sachs pointed to the problems of the definition of frontier

He wrote, " A new anthropic written safety bill is circulating on Capitol [00:29:00] Hill. Some of its ideas could be reasonable if limited to true frontier companies. As written, however, it will eventually sweep in most of Silicon Valley, damaging the startup ecosystem. The bill defines the frontier as any model trained on ten to the twenty-fifth flops.

The EU standard from 2023. Biden's executive order, California's SB53, and New York's RAISE Act use ten to the twenty-sixth, ten times more. Ten to the twenty-seventh is where the frontier actually is today."

Astra was reportedly trained on one hundred thousand Grace Blackwell GPUs. a ten to the twenty-fifth model can be trained on as few as several hundred GB300 chips in three months. That is not Frontier in twenty twenty-six The frontier keeps moving. any definition meant to track risks should move with it

Now on the totally opposite end of the political spectrum New York politician Alex Boris, who was targeted very intensely 

by pro-AI PACs earlier this year, wrote, " Anthropic is pitching a bill that closely matches its framework from June.

How can you watch Hugging Face, Coxon, and rogue AI swarms and conclude that the bill you cooked up in June is sufficient? close, this comes nowhere close to the speed of [00:30:00] developments nor the speed we need to keep people safe."

What I think is interesting is that both Boras and Sachs are, from very different perspectives, saying that this bill is basically outdated

although in very different ways

folk, for many folks, 

the subtextual reading of this

Is Anthropic actually trying to limit the powers of the executive when it comes to AI risk?

Adam Connor wrote, " This bill could most charitably be described as the best way for Anthropic to defend itself from abuse from the federal executive branch by limiting their power to take action and taking away everyone's ability to do 

so."

journalist Kelsey Piper expanded. She wrote, " One unfortunate conclusion I'm reaching from this is that Anthropic, while acknowledging they're doing something extremely dangerous, is more importantly with regard to policy terrified of the executive branch having the ability to flexibly make them stop at the drop of a hat.

This isn't shocking given that they've been on the receiving end of the executive branch doing that in an unprincipled and stupid way. Anyone who has dealt with the bureaucracy becomes a libertarian, and the administration's treatment of Anthropic was genuinely outrageous. But it means that they're interested in giving themselves more [00:31:00] process-based protections when everyone else is interested in giving us more process-based protections against them

Here's Here's where this nets out for now

What's coming up in the episode today are two massive issues related to AI



that appear independent but become linked very quickly

one is the AI wealth problem

The immense success of these companies is concentrating an extraordinary amount of wealth in a relatively small number of hands

And the public benefit fund in some ways 

amounts to a recognition that some amount of that wealth is going to have to be redistributed some way It's either gonna be redistributed voluntarily Or it's gonna be redistributed by someone doing the redistribution. 

and anthropic clearly and perhaps understandably wants to be doing that redistributing themselves.

And yet this is running headlong into another problem, which is concentration of power



and a growing concern

That owning these models and the wealth that comes with them involves too much power for one private institution

the-- all the all the discourse and debate around the fund and around the safety bill

are really all proxies in some ways

for the larger question of how AI wealth and power is [00:32:00] going to interact with democracy

Those are not easy questions, but they are certainly ones we should all be involved in. it is a subject that I anticipate 

growing in people's focus and recognition. 

but for now, we're gonna leave it there for today



appreciate you listening or watching as always, and until next time, peace 

​
