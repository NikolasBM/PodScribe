# The Right Way to Deal With AI Data Centers — Transcript (2026-06-23)

https://aidailybrief.ai/e/2026-06-23 · Listen: https://pod.link/1680633614

<!-- metadata -->
Format: news-analysis · Level: 1 · Length: ~00:25:00
Host: Nathaniel Whittemore
Categories: infrastructure, models, safety-security, policy
Featured: Google, Claude Mythos, OpenAI, Amazon, GPT-5.5
Also mentioned: Project Glasswing, Cursor
<!-- /metadata -->

---

[00:00:00] Today on the Today on the AI Daily Brief, the right way to deal with AI data centers. Before that in the headlines

Updates on Mythos, SpaceX's Neocloud, and much, much more. The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI. All right, friends, quick announcements before we dive in. First of all, thank you to All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, Robots and Pencils, Mission Cloud, and OutSystems

To get an ad free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts And to learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai

Last note, I've been sharing the new training.besuper.ai. This is the updated home of some of the programs that we've been experimenting with this year, including the Executive Catch-Up program, as well as the inheritor to Enterprise Claw, which is the enterprise-grade version Executive Agent Leadership Program.

That is a six-week sprint that will have you not only [00:01:00] building agents, but also building the organizational infrastructure, policies, et cetera, around them that you need to actually use agents. The next cohort for that launches on June 29th. Sign up now. Again, you can find all the links that are relevant at training.besuper.ai We kick We kick off today with an update in a story that we were covering yesterday, which is around the NSA dimension of the Mythos Fable ban



Now the TLDR, now the TLDR of what I was discussing in that initial coverage was that there seemed to me to be a mismatch between what was actually said and the way that it was being interpreted. In In short, People sitting around waiting for Fable to return were looking for a reason that made a little bit more sense than there just being this jailbreak that Amazon had reported.

And when they went back and found a story that seemed to indicate that the NSA had been hacked by Mythos It seemed to some to make more sense

Now, commentators with an understanding of NSA operations

pointed out that what the director was telling Senator Mark Warner



was likely a discussion of a controlled red team exercise rather than some live cyberattack. Joshi, the [00:02:00] Economist reporter whose article went viral, has now provided an update writing, " A US official tells me that Senator Warner misunderstood the NSA director General Rudd in this case.

Rudd did use the hours, not weeks wording, but the use of Mythos in this context was, as widely assumed, part of a red teaming effort, i.e., testing the security of internal networks. The official also told me that the agency's red teams no longer have access to Mythos because their authority for accessing it was under Project Glasswing

Yoshi pointed to commentary from a cybersecurity account called Iris C2, suggesting that they had the correct read on what had actually happened. That That account noted that, quote, " "In the In the case of almost every exercise, the red team begins with some kind of initial access to the air-gapped classified network." essentially, classified NSA systems aren't generally accessible from the outside, and gaining that initial access is one of the most difficult parts of any attack. Iris C2 commented that Mythos doesn't suddenly mean that any random person can suddenly hack the NSA.

However, However, they did note that if an attacker manages to gain [00:03:00] access, Mythos makes the design and execution of an exploit much faster, reducing the available time to detect and contain an intruder.

So the point if we're looking for takeaways



is not that Mythos has broken into the NSA, but that it does raise the stakes for cybersecurity by making attackers far more efficient



Now Now the bigger detail for many

was the throwaway line about the NSA not having access to Mythos anymore



yet another reason to want this situation to be resolved as soon as humanly possible

Now staying on the cybersecurity train, OpenAI has updated their cybersecurity model alongside a big new cyber initiative. on Monday, OpenAI announced a significant update to their Daybreak security initiative. Daybreak was first launched in May as an answer to Anthropic's Project Glasswing.

As part of the initial rollout, OpenAI made a preview version of GPT 5.5 Cyber available to trusted partners. As a As a point of differentiation to Glasswing, OpenAI invited smaller organizations to apply for access. OpenAI wrote, " Frontier defensive capabilities should not be concentrated in the hands of a few.



as AI changes the pace of [00:04:00] vulnerability discovery, defenders everywhere need democratized access to these models to find, fix, and protect their infrastructure before attackers can identify and abuse these flaws."

With the With the expansion, OpenAI has now launched the full version of GPT 5.5 Cyber, their first model that's been fine-tuned for cybersecurity work. like Mythos, the model has reduced guardrails to ensure professionals can use it freely in their work

And OpenAI has updated the Codex security plugin to make their harness more performant for cybersecurity tasks

OpenAI is claiming that with the new updates, their new cyber model has overtaken Mythos on the relevant benchmark, CyberGym

In addition, OpenAI is launching a new initiative called Patch the Planet in partnership with security research firm Trail of Bits. Reporting on their initial testing of GPT 5.5 Cyber, Trail of Bits wrote that they'd found hundreds of bugs in open source libraries. They've deployed 37 patches so far and have many more in the pipeline.

Over 30 open source projects have already joined Patch the Planet with the goal of securing the critical software that underpins the digital world. Trail of Bits noted that the introduction of strong AI security models has fundamentally changed the nature of the work.

[00:05:00] They wrote

wrote If If it wasn't already clear from the last several months of security news, this week makes one thing clear. The expensive part of security work has moved. The advantage is no longer in finding bugs but everything after. Confirming a finding, getting its severity right, writing a patch a maintainer will accept, and coordinating a disclosure.



that is the work that floods of AI-generated reports threaten to bury

The release comes as the Five Eyes intelligence agencies



which is an intelligence alliance between Australia, Canada, New Zealand, the UK, and the United States

issued a rare public alert for AI-driven cyber risk In a bulletin published on Monday, the UK National Cybersecurity Centre wrote, " The evolving landscape of AI is rapidly transforming cyber risk, and we must act swiftly to remain ahead." The bulletin called on the business community to assess the changing risk, prioritize cybersecurity practices, and, quote, "Stay actively engaged as threats and guidance evolve."

The agencies warned that the rapid pace of frontier AI development means cyber risk assumptions can become outdated in months, not years. They also heavily encourage the integration of AI tools into cybersecurity operations and [00:06:00] warn that, quote, " Cyber risk can no longer be treated as a purely technical issue.

This is a core business risk and leadership responsibility."



now nothing in the bulletin will be surprising to anyone who has been paying attention. but it's pretty clear that the intention of the bulletin was to light a fire under the enterprises who perhaps are not spending as much time listening to the AI Daily Brief as they should



now now staying in the regulatory space, a story that isn't exactly related to AI, but which is being kind of lumped in as frontier tech writ large.

President Trump has called for the construction of a powerful quantum computer in a pair of new executive orders. One order instructs federal agencies, including the Energy Department, to collaborate with private industry to deploy a quantum computer for scientific research purposes Michael Kratsios, director of the White House Office of Science and Technology Policy, said he believes a functional computer can be done by 2028.

In In addition, the first order instructs the government to migrate to quantum secure cryptography by 2031. The second order deals with protection of intellectual property within quantum companies and hardening the supply chain for components for quantum computing.

[00:07:00] this order emphasizes the need for international cooperation to prevent the technology from falling into the hands of adversaries

Now, for anyone who's been paying attention to the quantum story, it is honestly a little hard to tell exactly where the state of the technology is

Nor is it particularly easy with this administration to know at any given time what the motivations behind an executive order are So for this one I'm going to have to just leave it at the news and make of it what you will

Now, on the market side of the house, SpaceX has signed another multi-billion dollar data center deal as Elon Musk extends his compute empire. Open Open source AI startup Reflection AI agreed to pay a hundred and fifty dollars a month to rent capacity from the Colossus II data center.

That agreement begins next month and runs through to twenty twenty-nine, putting the total deal value at six point three billion. As with the other SpaceX deals, either party can walk away on three months' notice. This is also significantly smaller than the Anthropic and Google deals, each running at around a billion dollars a month

Still, with SpaceX coming down from its IPO sugar rush, anything that helps people understand the long-term of the business is probably helpful

[00:08:00] Reflection AI, meanwhile, used the deal as a way to promote themselves as a domestic open source alternative. In a press statement, the startup said, " "Recent Recent events highlight how important open source is to the AI ecosystem, with more nations and enterprises recognizing the risks and costs associated with exclusively depending on closed models."



They said that the deal signals their strategic importance in the frontier AI ecosystem, and that more compute would give them more runway to develop leading open models. Now, Reflection is yet to release their first frontier model, but has been working with government partners, including the Pentagon and the Department of Energy's Genesis Mission

Swigs from Now Swigs from Layton Space



the potency of SpaceX's new moves. He tweeted, " "I don't I don't think anyone is correctly doing the math around how SpaceX, the Neo Cloud plus Neo Lab, is currently going to market. SpaceX has already recouped about half its investment in Cursor in compute deals.

The other half is paid for if Composer 3 does well. No No other company is simultaneously a leading model lab and Neo cloud, at least where GPUs is concerned. It's a crazy effective combo if you've adequately planned out GPU [00:09:00] supply if in-house training, one, goes very well or two, doesn't go very well."



Which is Which is certainly not to say that SpaceX did well yesterday, actually experiencing a sixteen percent drop. but it wasn't the only AI company running into some trouble Google stock fell sharply as the market reacted to the loss of two key AI researchers.

On Monday's show, I covered the departure of Nobel laureate John Jumper, who left DeepMind for Anthropic just a couple of days after Noam Shazeer packed his bags to join OpenAI. The sort of standard reading of the situation is things going sideways at DeepMind, and there were plenty of anonymous quotes to be had to suggest morale was plummeting as Google lags behind in the AI race

Now, while my personal take was that we have a tendency to overreact to personnel changes, evidently the market disagrees. Google stock was down as much as 7.2% on Monday, its largest intraday move since February that means that if you can attribute this directly to those two employees departing Those departures cost the company over two hundred billion in market cap

Now, it might Now, it might be reasonable to chalk this up to the market over-indexing on AI headlines [00:10:00] once again, as they did during the DeepSeek moment. But there is also a more fundamental narrative shift happening around Google

Up until very Up until very recently, Google had been the top performer in big tech and even briefly became the largest company in the world



and yet the more that the perception is that Google's models aren't keeping pace OpenAI, particularly on enterprise essential agentic use cases, skepticism has started to creep in

With With that as background, Jumper and Shazeer moving to rival labs



seems to confirm that point of view rather than simply representing some new trend. Gil Luria, the head of technology research at D.A. Davidson summedup that viewpoint saying, " "Google Google is losing the war for talent at the frontier of AI.

Google had the state-of-the-art model for a few weeks last year which helped it get credit as an AI winner but has fallen off since, and these departures may mean it is falling behind."

Now I will say I'm sticking to my guns Around reading too much around any personnel moves



and I think Prime Intellect's Florian brand is directionally correct when they write, " "We are We are in peak Google is done for and will never catch up," which which is always followed by them [00:11:00] releasing a new model and people going, "The others are done for. No one has the TPUs and data that Google has."



that... For now, it is for markets to debate which side of that equation is more accurate. But for us, that is gonna do it for the headlines. next up, the main episode 

One of the most important AI questions right now isn't who's using ai, it's who's using it? Well,

KPMG and the University of Texas at Austin. Just to analyzed 1.4 million real workplace AI interactions and found something surprising. The highest impact users aren't better prompt engineers. They treat AI like a reasoning partner.

They frame problems, guide thinking, iterate, and push for better answers.

Welcome back Welcome back to the AI Daily Brief.

Today we're gonna take advantage of a slightly slower news cycle in which everyone is somewhere between sitting on their hands waiting for Fable 5 to return going full open source tinkerer building out local infrastructure in their basements. To try to discuss calmly one of the most contentious issues surrounding AI, which is the impact of data centers



Now on any given day, I could find a reason to discuss this topic. Especially with midterm elections coming up, it is becoming more and more of a hot button, and it's also rising in cultural significance

On On his popular This Past Weekend podcast

Theo Vaughn recently went on a data center rant

He said, " [00:15:00] "Nobody Nobody wants a data center, dude. And the people that want them, to me, they seem kind of evil. One of these companies is gonna own all this information. There's gonna become this social or emotional credit score, and then AI is going to try to become our new God Which by the way, has to be a contender for the most misperceptions or concerns, depending on your perspective about AI shoved into a single paragraph



And yet Theo Von here is, I think, more reflectiveof an emerging mainstream point of view than he is even a leading indicator



AI researcher Andy Masley recently posted a New Yorker cartoon



of a little robot coming into its parents' bedroom with the mom reaching over to the dad and whispering, " "It's It's AI again. He wants another thousand glasses of water."

As Andy, who has done more to debunk some of these myths than just about anyone captioned, " This idea will never die."



l- and on those lines, you might have recently noticed

that famed activist Erin Brockovich has started a major campaign against data centers And on the other side of the political aisle Former Tea Party conservatives are now planning a nationwide protest against AI data centers



The New The New York Times quoted comedian Charlie Berens calling opposition to data [00:16:00] centers the most bipartisan issue since beer



now when you hear critiques

despite Theo grabbing some concerns that we've previously heard around things like central bank digital currencies, i.e., the worry about a social credit score. For most people, the two big issues come down to water use

and energy prices

Take, for example, this Take, for example, this recent tweet from Indiana resident Valerie Ann Smith. 

she wrote, " Amazon is dropping an $11 billion AI data center right in Indiana. This this monster will guzzle electricity for one million homes and 300 million gallons of water every single year. Just one facility."

Our grid is already crumbling, bills will explode, water shortages incoming, blackouts while they power their AI overlords. And these same tech giants lecture us regular people about climate change?

Nicole Dividar, who so far as I can tell from just their Twitter profile seems to be pretty much as opposite politically as she can be From Valerie Anne Smith reposted that

and reiterated that key point. Amazon's monster data center projected to consume three hundred million to three hundred and thirty million gallons of water every year. [00:17:00] Insane. The way we're going will be the downfall of humanity and every living being. The madness must end.

The thinking that nature is here to exploit must end

Now these numbers do seem at first glance huge. 300 million gallons of water a year seems like just an enormous amount, right?

Overall, Amazon recently released full water use statistics for their data centers

And according to their figures, their global data center operations consumed 2.5 billion gallons of water in 2025

Now Now that report did note that water use at its sites had actually fallen 2% from 2024, even though it expanded its data center footprint meaningfully, but still 2.5 billion gallons of water, right?



The The problem is that relative to many of our other uses of water these numbers actually aren't particularly large

So to use some comparisons



the 16,000 golf courses in the United States consume over 500 billion gallons of water a year. that means that means that a full year of operations for Amazon's data centers is slightly more than a single day of US golf course maintenance



another [00:18:00] frequent point of comparison is almonds. California almonds use between one point two and one point eight trillion gallons of water each year

which is somewhere between five and eight times the total amount of water used by all data centers

in America.

One recent study

found that the US lost 3.29 trillion gallons of water per year to leaky pipes



About 15 ti- about 15 times as much as data centers use



oneand one of the key sources for the myth of water consumption



author Karen Hao in her book Empire of AI

had to apologize for her most dramatic claim being a factor of 1,000 wrong Basically, she claimed that a Google data center in Chile consumed a thousand times more water than the surrounding population

But she was off by a factor of 1,000 due to a unit mix-up

Howe Howe eventually acknowledged the error and issued the correction

But the book is still out there saying the same thing



In Indiana

where the citizens were concerned about Amazon's data center using 

300 million gallons of water per year

The state delivers a little under five hundred million gallons of water per day for domestic use, or or around a hundred and eighty-two billion gallons per year

That That means the Amazon [00:19:00] data center represents 0.2% of water use for the state without including industrial use



and this gets and this gets to one of the biggest problems with the data center conversation when it comes to water

Which is that if you don't like the thing that the water is being used for, even one gallon is too many. And that's really what And that's really what a lot of this critique comes back to. Big numbers are politically potent, ' cause most people don't have any idea of how much water we actually consume And these numbers all just sound so astronomically large that it's very easy to grab attention



and get people to think that the water being used is just too much



Now what's more, for those who think that even this is too much water

The companies in the data center space are working to reduce it even more



NVIDIA recently touted what they called one of the biggest efficiency leaps in data center history



saying that their new approach to liquid cooling could cut water use to near zero

Now, Now, as I mentioned



the second big issue that comes up around data centers

is the idea that they drive up electricity prices

And And once again, digging into the numbers, it's a lot less clear [00:20:00] than the data center opposition would make it seem



the Institute for Energy Research recently concluded: There is no statistically significant correlation between the number of data centers in a state and its current electricity prices. In fact, prices in the top ten datacenter states are virtually identical to the average across other states.

Furthermore, there is no statistically significant relationship between data center concentration and faster increases in electricity rates

Now, where I think that this does get more complicated

is that ultimately most electricity price pressure is due in some way not just to new data centers coming online but to costs associated with upgrading an aging grid. a problem that we have to face even without the new data center build-out

The Daily Economy explored this research and asked why so many Americans are convinced that data centers do increase their electricity prices. They concluded, " "In the In the short run at the local level, the story is more complicated. A Bloomberg analysis of wholesale electricity prices across twenty-five thousand grid nodes found that prices have risen as much as two hundred and seventy-six percent since 2020 in areas near major [00:21:00] data center clusters.

More than seventy percent of nodes recording price increases were located within fifty miles of significant data center activity. In these regions, data centers create a surge in demand on local grids. When transmission capacity is constrained and the new generation has not yet come online, prices spike.

Those higher wholesale costs can then filter into retail bills, at least in the short run, and local customers bear the brunt of this regional electricity demand."

Now continuing later, they write, " Concentrated price spikes are not evidence that data centers are inherently incompatible with affordable electricity. They are evidence that grid infrastructure and cost allocation rules haven't kept up."

They then point to some of the examples of how policy is racing to catch up with this and make things more fair in the short run as well. They point to, for example, Oregon's Power Act which requires the biggest electricity users, i.e. the data centers, to bear the cost of infrastructure that is built specifically for them

This is also the same principle behind the White House's Ratepayer Protection Pledge

where companies agreed to quote, "Protect American consumers from price hikes due to data center energy and infrastructure requirements, and [00:22:00] lower electricity costs for consumers in the long term."



the the five commitments in the pledge included specifically building, bringing, or buying new power supply, paying for new power delivery infrastructure upgrades, paying whether they use the power or not, investing in local job creation and workforce development, and contributing to electric and community resilience

Now, Now, my personal belief and why I think this is worth talking about is that as with much in the AI debate

The conversation on both sides gets wildly reductive and extreme

It tends to be snarky reactions like Marc Andreessen reposting Theo Vaughn's post saying, "I have bad news about your podcast, dude." pointing out the inherently hypocritical position of critiquing data centers when they are the thing that allows his podcast to reach all the people that it reaches

Or you have Or you have commentary, as Alex Finn said, that just calls this insane drivel Now, Alex is someone who's incredibly excited about AI, and I think rightly points out that there is a huge excitement gap between, for example, America and China when it comes to AI

He writes, "If a large majority of Americans believe the most powerful, prosperous, important technology of our [00:23:00] lifetimes is somehow evil, we simply won't be able to keep up with a country that believes it's good."

And while I think that that's right, we're not gonna convert people by not taking their concerns seriously



Now, Now, I think that in all of this, maybe the most important actor for finding space in the middle are the labor unions Labor unions represent multiple constituencies On the On the one hand, they are of the communities that have these concerns

And I think take them seriously. I think they are sympathetic to concerns that AI and any big tech

is another way to disproportionately benefit the already rich. At At the same time, unions representing key skilled blue-collar work

are also at the forefront of seeing



how valuable the data center build out can be



as the demand for more skilled work from their members just goes up and up and up



The Information's Anne Davis Vaughn recently wrote a piece called "Debunking the Myths that AI Dataset Critics Believe." and I actually think that the title undersells the value of the piece



I I think that her lead paragraph nails it when she writes, " I've been visiting large AI data center projects [00:24:00] in rural and industrial communities in the Midwest, Southeast, and West, and I have found that two things can be true at the same time. AI data centers have drawbacks but are better for communities than their residents think, and those communities can win a lot more financial concessions and benefits from the tech firms than they realize."

I think right now Communities are being taught to felt like their choices are roll over and let big tech and the data centers do whatever they want with the natural resources surrounding their homes. Or on the other end of the spectrum

get your signs and pitchforks and stop it from happening entirely



I think communities should. Absolutely

get to advocate for what they think is right for their communities, whatever it may be relative to data centers. But I think that they're missing that there is a massive middle path

Or they can be negotiating for the data center builders to effectively give them the world



and Anne's article starts to make this a little bit real She writes, in rural in rural Richland Parish, Louisiana, for instance, hundreds of teachers are set to receive unprecedented fifty thousand dollar [00:25:00] bonuses this year, funded by a surge in tax receipts tied to Meta platforms, which is building a large AI campus there.

An existing ordinance mandates that teachers get a slice of sales taxes, and teacher bonuses quintupled due to their activities related to campus construction."

Not to be too crass about this, but I think that with the amount of money involved and the stakes of what's being built



We're not just talking about data center builders and owners making sure that people's electricity prices don't go up. We're talking about major intentional economic benefits to the communities if negotiated well

I hope that we can move past The knee-jerk binary phase of this conversation

into the how everyone wins phase sooner rather than later

For now, that's gonna do it for today's AI Daily Brief Appreciate you listening or watching as always, and until next time, peace 

​
