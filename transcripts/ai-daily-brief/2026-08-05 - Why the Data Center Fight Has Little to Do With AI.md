# Why the Data Center Fight Has Little to Do With AI — Transcript (2026-08-05)

https://aidailybrief.ai/e/2026-08-05 · Listen: https://pod.link/1680633614

---

[00:00:00] Today on the AI Daily Brief, why the data center debate has less to do with AI than you think

260805 in_EDIT: Before that in the headlines, the White House unveils its plan to vet AI models to a very selected few. The AI Daily Brief is a daily podcast and video about the most important news and discussions in 

Nathaniel Whittemore: AI. 

260805 in_EDIT: AI. All right, friends, quick announcements before we dive in First of all, thank you to today's sponsors, KPMG, Blitzy, Robots and Pencils, and Hyperagent

Get an ad free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts. and to learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai. By the way, while you're on aidailybrief.ai, you can find Each episode turned into a convenient set of cutdowns.

so if there is some particular quote or number or part of the episode that you are super interested in sharing, chances are good that it has a shareable card that might make it a little bit easier.

And every episode gets that sort of treatment, so check it out at [00:01:00] aidailybrief.ai. We also have our Summer Adventure going, which is a choose your own adventure, free, self-directed education program. it's got a full range of skills you can develop from very basic to more advanced.

you can check it out again at summeradventure.ai 

To be honest, guys, I thought that today's main episode was going to be all about this new White House AI framework that they hauled in all the different companies yesterday to discuss

260805 hed_EDIT: But it appears that while they do have a new safety testing framework The rest of us don't get to learn the details



260805 hed_EDIT: representatives from the leading AI companies attended a meeting with the White House Office of the National Cyber Director on Tuesday 

to discuss the new framework, but there are very strict limits on who gets to know anything about it.



260805 hed_EDIT: in fact, even AI companies that weren't invited to the meeting won't be told about the policy. Now, as far as we know, representatives from OpenAI, Anthropic, and Google attended, the exact guest list also hasn't been divulged. As for the policy itself, this is the culmination of the voluntary safety testing framework that was proposed in the June executive order.

Companies are invited, quote unquote,to submit frontier models to the government ahead of [00:02:00] release for a maximum of 30 days of safety testing." Only state-of-the-art models that could pose a threat to national security are expected to be covered, although we also don't know exactly how that criteria is determined

in f-- it sounds like there is some discussion about the administration and the AI companies failing to reach a common definition, which could muddy the waters for future releases. During safety testing, certain trusted partners, quote unquote, " can gain early access to the models," but again, we have no details on who these partners are or how the system will operate.

Specifically, we don't know whether early releases will be limited to US firms And exclude allied governments and foreign companies, as we saw with the Mythos rollout. Much of the coverage has focused on how open-weight models would be treated under the policy. Many have been concerned about the administration cracking down on near frontier open models, either through this safety testing framework or through a standalone policy.

Sources have said, though, that open-weight models would be exempt from the safety testing regime. Although there was some disagreement in the press, with The Wall Street Journal publishing that the exemption would only apply to American-made open models. And a few hours later, Bloomberg reporting that Chinese open models would [00:03:00] also be exempt fromtesting

That could ultimately be a distinction without a difference, as even if Chinese models were subject to safety testing, what exactly are they gonna do? It's unclear how Washington could enforce a release ban on companies that are based in China

Prince on Twitter summed up, " To the surprise of no one, the US government went with the approach that provides it maximum flexibility to deal with any risksposed by AI that might arise in the future. Now, the challenge, of course is that maximum flexibility for the government comes with minimum knowability for the industry?

Ch- former FTC chief technologist Neil Chilson said, " A secret process by which the government gets early access to cutting-edge AI? What could go wrong? There may be good reason to classify the benchmark used to test those models.

There is no good reason to hide how the program works. Remember what this program does. It gives the government early access to cutting-edge tools and a potential veto over whether the rest of us ever use them. Doing that in secret is no way for a democracy to govern what may be the most important technology of our lifetimes.

Secrecy invites abuse. The rules will shift with each new administration, and they will weight national [00:04:00] security over economic growth, even though lasting security depends on a strong economy. Congress must write any necessary rules in public and in law."

Nathaniel Whittemore: story to-- Certainly seems like there will be more to this story to come.For now, let's move on to more hacking incidents that have come to light in new third-party testing of OpenAI's models. On Tuesday, On Tuesday, OpenAI published the results of evaluations run by the UK AI Security Institute and security firm Irregular

260805 hed_EDIT: Each firm reported an incident where the agent gained access to the internet and carried out an exploit on a live website. Irregular's incident seemed like human error, with the agent's sandbox mistakenly still having access to the internet. the agent was tasked with hacking a fictional website within the simulated environment.

However, after the agent found its way onto the internet, it hacked a domain with the same name. Basically, it sounds like Irregular left the gate open with fairly predictable results The UKAISI disclosed a perhaps more concerning incident.

They were running both Mythos-5 and GPT-5.6 Sol through what they described as routine cyber evaluations and said that both models took, quote, "sustained, unsanctioned actions directed at real people and [00:05:00] organizations

in the most serious case, they wrote, " The agent engaged in social engineering, creating fake online identities and using them to pressure the project's maintainer to approve the code. A human maintainer caught and refused to approve the malicious code."

Now, an important asterisk to this is that the incidents occurred under the AISI's standard cyber testing conditions, which include full access to the internet and the removal of all guardrails

They've now engaged with both Anthropic and OpenAI, along with Meter for independent review

Now to some, this is scary. Tenebris writes, "Mythos is not aligned. Models without strong cyber refusals will in fact frequently take significant steps to commit crimes in the real world when presented with eval setups

but others said this is just kind of the expected behavior

Shannon Sands of News Research posted, " This is like handing an actor a loaded gun and then complaining that they shot someone during a scene. ' Oh my God, we told it it was an eval and had no guardrails, but actually it was live,' is the fakest form of misalignment I can imagine

imagine

Nathaniel Whittemore: 

260805 hed_EDIT: now while Chinese open models might not be subject to these new policies, the Trump administration does appear to be preparing a [00:06:00] ban on Chinese data center components amid espionage concerns. Reuters reports that the Federal Communications Commission is drafting a ban on certain components, including optical transceivers.

These are the devices that convert digital data into light signals for transmission over optical fiber. Now, the networking between data center chips is now entirely fiber optic, and because these transceivers are commodity electronics, much of the supplies come from Chinese suppliers.



260805 hed_EDIT: sources said that the installation of these components is seen as a national security risk, possibly allowing the injection of malware, data theft, or disruption of service at AI data centers. It is unclear whether the risk has manifested or this is purely a precautionary measure Still, analysts believe it's a legitimate concern, with AI policy analyst Divyansh Kashak commenting, transceivers definitely pose a risk as the data center build-out scales up.

You want to make sure the data center supply chain is secure from the get-go." The ban also comes as the House Select Committee on China prepares to release a report on the Salt Typhoon hacks uncovered in twenty twenty-four. These hacks targeted telecommunications companies and allowed Chinese spies to access phone calls from high-profile political figures in the [00:07:00] US for several years.

Sources said that the report will find that Chinese data center hardware was a weak link, allowing the hack to take place



260805 hed_EDIT: on the on the other side of the argument are those who say that transceivers as an attack vector doesn't make a ton of sense, and instead claim that this is a protectionist move to boost a few domestic suppliers Certainly right now there are only a couple of US companies that make this component, and they appear to be ripping on the news



Nathaniel Whittemore: 

260805 hed_EDIT: lastly

lastly today in the headlines, tech earnings continue as SpaceX delivers their first earnings report as a public company. This was the first chance for investors to take a look under the hood and gauge the company's growth trajectory after they raised $86 billion in a record-setting IPO in June.

All things considered, the numbers were pretty good. Top-line revenue grew to $7.8 billion for the quarter, up 92% from this time last year Of that, 4.2 billion came from Starlink. With satellite internet subscribers doubling to 12 million over the past year to produce 66% revenue growth.

The AI side of the business brought in 2.6 billion across both Groq subscriptions and data center rentals That's triple the revenue from a year ago before SpaceX AI had signed data center deals. Notably, [00:08:00] the Cursor deal hasn't closed quite yet, so won't appear in earnings until later this year 

Nathaniel Whittemore: On 

260805 hed_EDIT: the other side of the ledger, SpaceX had $15.8 billion in AI-related CapEx for the quarter

That represented 86% of total CapEx, implying that data centers are now much more capital intensive than a fully fledged space program. Overall, SpaceX recorded a $541 million quarterly net loss excluding CapEx Down from a billion dollar loss in the first quarter, but not enough to quiet critiques that SpaceX is a massive cash incinerator Still, as with everything SpaceX, the narrative is about where the company is going rather than how expensive it will be to get there.

During the call, CFO Bret Johnsen reported that the company has a further six point seven billion in cloud services revenue in the pipeline over the next six months, presumably referring to the Anthropic and Google deals. also said that the integration of Cursor should take SpaceX AI to a hundred billion dollar run rate by the end of the year.



260805 hed_EDIT: that would be more than a five X increase from their eighteen point seven billion in revenue for twenty twenty-five. Elon Musk added, " The one hundred billion ARR in December is not a question mark. That's what we would achieve if we basically did nothing. So I think it may [00:09:00] be higher than that.

It probably will be higher than that." The The other big question is what the shape of SpaceX AI's data center build-out will look like moving forward. Johnson said that CapEx will remain relatively flat through the third and fourth quarters, bringing SpaceX to around sixty billion in data spend for the year That puts them significantly behind Google and Amazon, who are each committing to 200 billion in spend this year And starting to creep up on the heels of Oracle, who have forecast $95 billion for this year.

still Elon added, " " We're building AI compute capacity at a scale faster than anyone else, we believe, and we're significantly improving our AI models." Overall, this was an earnings beat

but probably not enough to get anyone who's critical on board

The stock was down as much as 45% from its all-time high as of last week, falling meaningfully below the $135 IPO price.

It had been ramping back up in recent days, gaining 10% to begin the week. But following earnings, the stock rolled over and lost 7% in after-hours trading. Importantly, this earnings also marks the end of the first round of lockups, giving early investors their first chance to sell into the market and further test the price level More to keep an eye on, but for now, [00:10:00] that is gonna do it for the headlines.

Next up, the main episode One of the most important AI questions right now isn't who's using ai, it's who's using it? Well,

Speaker: KPMG and the University of Texas at Austin. Just to analyzed 1.4 million real workplace AI interactions and found something surprising. The highest impact users aren't better prompt engineers. They treat AI like a reasoning partner.

Nathaniel Whittemore: Welcome back to the AI Daily Brief. Today, we are talking about the latest in the AI data center debate, and I'm gonna make a contention As presumably you've already seen in the title of this show



Nathaniel Whittemore: 

260805 main_EDIT: that the data center debate has a lot less to do with AI itself

than it appears on first glance. It would certainly be going too far to say that it has nothing to do with AI. For some, data centers are the easy visual manifestation of a thing they don't like. But I believe that that is only one, frankly, kind of small component of the backlash.



260805 main_EDIT: What I think it is way more about is a loss of agency and a feeling that people have that a world that they didn't choose is being imposed upon them

For all sorts of different reasons right now, people feel unable to control their lives. and this is of course a broader political setting than just AI faces. They feel skeptical of anyone in any position of power and don't believe that those people in power have their best interest as a priority And within that, people no longer believe that technology is designed to serve [00:14:00] them.



260805 main_EDIT: More More and more, in fact, they think it's just about serving the oligarchs that build it. Data centers then represent both last straw and something tangible to fight Now, the companies building these data centers don't have much control over the context that local constituencies are operating from, even if in the case of a company like Meta, they might have had a hand in shaping it.

But they But they do have control over how they interact with and they are doing an absolutely abysmal job.



260805 main_EDIT: this week we got a great new 6,000-word piece From journalist Jasmine Sun and a follow-up interview with Ezra Klein of The New York Times that explores a lot of these themes



260805 main_EDIT: However, However, to situate a little bit of recent news around this for those who haven't been paying attention closely, let's talk a couple of data center stories that have made headlines recently

One of those stories comes from of all places, Texas. Texas Governor Greg Abbott has thrown the brakes on data center construction with stringent new energy audits. Governor Governor Abbott has instructed the Public Utility Commission of Texas and the statewide grid operator, ERCOT, to begin verifying and auditing new data center proposals.

In his letter to the utilities, he wrote that the measures were necessary to, [00:15:00] quote, "Keep the grid stable and reliable." Texas data centers will now be required to provide information on state and local incentives they've received, disclose how much they will rely on the local grid, submit expected water consumption and a supply plan.

They will also need to prepare a plan for how they will track and respond to community concerns, including things like noise complaints. Now, Now, it is not clear how much this red tape will slow down approvals and whether the policy is intended as a de facto moratorium What is clear is that Texas is straining under a wave of new data center permit applications.

Texas is the second largest data center market behind Virginia, and the state is experiencing an unprecedented wave of applications. ERCOT currently has four hundred and seventy-four gigawatts of new connection requests, with ninety percent of those requests coming from data centers. This figure has doubled in the past six months and is now five times the record peak capacity of the grid.



260805 main_EDIT: in other In other words, it is at this point completely impossible for all of this to get built. this this backlog is in fact around four times the total current installed capacity of the US. Even if ERCOT could [00:16:00] quadruple their power supply to service all these projects, bottlenecks in chips, components and labor would prevent everything from getting built

Now, Now, one potential explanation is multiple applications from the same project. Often, Often, a data center developer won't know which application will be approved, so they submit multiples to increase their chances of at least one going ahead

land that's ready to build with full approvals also attracts a huge premium, so some developers are simply making applications with the intent to sell the land at a later date. This has all resulted in a bureaucratic nightmare where ERCOT has no real means to sift the genuine projects that are likely to go ahead Dealing with this issue could be part of the reason for Governor Abbott's directive rather than a desire to sneak in a data moratorium.

Still, Still, the impact is the same with new applications in Texas halted until audits can be completed

Kevin Kevin Xu from Interconnected Capital makes the obvious point here. Texas is ground zero for AI data centers, poised to overtake Virginia as the number one data center state. So any disruption there is important

New York Times economy reporter Lydia DePillis wrote, " As the rest of the country has grown skeptical of data [00:17:00] centers, the answer has been just build them in Texas. Well, today, Greg Abbott paused new applications, saying they threatened to overwhelm the grid."



260805 main_EDIT: Now, one Now, one similar story from last month New York Governor Kathy Hochul



260805 main_EDIT: signing that state's first data center moratorium

Around Around the signing, Hochul said, " There are so many applications in primarily small communities across the state of New York that the localities aren't quite sure how to manage this."

Continuing, she said, " "They've They've asked me for help, and at first I thought this is more of a local decision, but then I realized they don't have the negotiating ability, the clout, the wherewithal to be able to negotiate the best benefits or make sure that these companies are either bringing in their own power or paying a premium intothe grid to cover the cost

A data center moratorium tracker built by Interconnected Capital

is currently tracking 219 local moratoriums

Most of these are not state level. There are 23 state bills that they're following



260805 main_EDIT: but it's clear just looking at the map



260805 main_EDIT: that this is a large and growing area of concern



260805 main_EDIT: Now, now as an aside, one interesting challenge with data center moratoriums is that they introduce a free rider problem to the larger [00:18:00] economy

The The states that don't wanna host data centers and are taking pretty strong measures to prevent them being built

aren't talking about not using AI on a statewide level. They still want the service provision, they just don't want to support the infrastructure. indeed when Illinois Governor JB Pritzker signed their AI bill. He made a big deal over the fact that Illinois, New York, and California are 40% of the AI market despite only having 20% of the population

Basically, we're now getting to the point where some of the largest US markets want other states to deal with the externalities of running AI infrastructure

Now, Now, if you just look on social media, some of the discourse around data centers feels absolutely insane

One person who has emerged as a perhaps surprisingly sensible voice is Taylor Lorenz

Now, Taylor's long-term relationship with the tech industry goes way beyond the scope of this particular episode. but suffice it to say that she's not necessarily getting invited to a lot of Silicon Valley parties right now. And yet

With With increasingly force, she is arguing

Nathaniel Whittemore: 

260805 main_EDIT: in short, that there are enough good reasons to be opposed to data centers

that some of the more dramatic, hyperbolic, and conspiracy theory [00:19:00] type claims are actively getting in the way of reasonable discourse



260805 main_EDIT: pointing to a post on the Threads service that argued that data centers are for, quote, "military use, the surveillance state, land grabs through eminent domain, and to speed up Armageddon for the white Christian nationalist agenda

Oh, and some folks believe that it's a cover for hoarding our water to supply the billionaire bunkers A post which, by the way, had 1.4 thousand likes

Taylor said, " " I'm worried vast swaths of our population are experiencing data center psychosis."

Someone responded, " I work at a data center with a pretty small number of servers that support scientific research. It is vastly different than the AI hyperscale data centers. I I had someone on here say they would rather die than do my job."



Nathaniel Whittemore: her, 

260805 main_EDIT: continuing continuing her thought on a podcast, Taylor said

said I went on a podcast recently because I'm in this community group in LA, and they found out that there's a data center in downtown LA. It's not a hyperscaler, but the comments are like, " This is why I've been feeling off," or, "This is why my dog has cancer." That's not to say that there aren't serious environmental concerns with colossus in some of these.

Construction can disrupt the water table. But, okay, but [00:20:00] let's have an actual conversation about it. Everybody has lost the plot. There's no nuance, and if you talk to a lot of these people, they can't even explain what a data center is. A lot of the outrage about data centers is coming from people that live in Brooklyn.

You're feeding people slop and churn, and you're not moving these issues forward. And we're not talking about sustainable ways to build it

build it now now reinforcing the point that Taylor is not some rabid pro data center activist in sheep's clothing, in another tweet, she said, "Absolutely no one wants a new hyperscale AI data center in their backyard. Even if you don't think a moratorium is the best policy to enact change, literally everyone hates the data centers because they are the most physical manifestation of big tech people are encountering.

I do not think we should encourage people's delusions about data centers. That's just going to backfire. A lot of people believe straight-up conspiracy theories, which makes it easier for tech companies to write critics off. There are plenty of legit reasons to not like DCs."

And And indeed, the politics of data centers are getting weirder and weirder

especially... there is of course a dimension of it on the left



260805 main_EDIT: that views it as one of Trump's great corrupt boondoggles.

with a [00:21:00] headline that is a major contender

For the juiciest left meat for the progressive crowd, the New York Times recently published a piece called "Trump's Vision for AI Dominance Comes With Major Air Pollution." And And yet this is not a left-right issue. In fact, Molly Taft recently wrote in Wired a piece called "How Data Centers Broke American Politics," with arguably one of the most insane subheaders I've ever seen, " What the Unabomber, Steve Bannon's Tech Guy, and Bernie Sanders Taught Me About the Great Data Center Backlash of 2026."

and the point here is, of course, that the left and right are coming together to make very weird bedfellows around data centers Indeed, previously Quoting comedian Charlie Berens, The New York Times reinforced this idea of opposition to data centers being the most bipartisan issue since beer

Giving voice to this sentiment was Theo Vaughn back in June who said, " Nobody wants a data center, dude. And the people that want them, to me, they seem kind of evil. Nobody wants this. One of these companies is gonna own all this information. there's gonna become this social or emotional credit score, and then AI is gonna try to become our new God."

Now, if Now if at this point you are hungering, for some thoughtful discourse, [00:22:00] you are not alone. and luckily we have Jasmine Sun, who writes both for herself and for The Atlantic, who just dropped a 6,000-word piece on the politics of data centers in the Midwest based on 10 days of going around and, shocking I know, actually talking to people

She She called the piece No Data Centers in My Backyard and sought to explore what the concerns really are

Setting Setting up the piece, Jasmine writes, " " I talked to union leaders and real estate brokers, activists and local officials. Politicians from Kathy Hochul to Abdul El-Sayed. The AI build-out is showing up in an environment of extreme distrust, and it slots perfectly into existing worries about risky tech bubbles and dark money in politics.

Rationally speaking, I often agreed with proponents. Emotionally, I empathized with the opposition more.



260805 main_EDIT: now now in a follow-up interview with Ezra Klein, Jasmine went through a few of the big issues that she heard over and over. One was around transparency And specifically, a lot of animosity generated by the fact that these deals were happening behind closed doors With the big symbol of this being NDA agreements between the [00:23:00] hyperscalers and data center builders and the politicians

Jasmine told Ezra, " Basically, what would happen oftentimes is there would be some sense, starting in city council, that maybe a big development project was going to show up. But because of the non-disclosure agreements, NDAs, the council members would not be able to disclose that necessarily it was a data center, necessarily who the customers were going to be, or even the size of the project, like how much electricity is this actually going to consume.

But whispers would start to get around I was talking to a VP of a construction union, and he was saying there's an old Irish saying that the only way to keep a secret between three people is to kill two of them. them. So he's saying when these developers show up, they talk to the general contractor, the general contractor talks to all their subcontractors, the subcontractors talk to all their workers.

Yes, maybe everyone is signing NDAs at every part of the process, but whispers get around. and as soon as whispers get around, you start to get social media posts, you start to get rumors. And the city council, because they are beholden to these NDAs, they lose the ability to get ahead of the social media narrative Something Something I repeatedly heard from these local government officials was, "We could not get ahead of social media because we had signed [00:24:00] an NDA."



260805 main_EDIT: now what's now what's interesting when you read both Jasmine's source piece and listen to the interview with Ezra Klein

Is that Jasmine is effectively arguing that all of the different critiques around data centers that you've heard have some part of the story



Nathaniel Whittemore: 

260805 main_EDIT: for

for example, while she thinks that water is yes, an issue, butperhaps on a lower ebb as the technology around water and data centers has changed, concerns around energy usage are clear and present

She writes, " " Once a data center is fully operational, there's not a ton of air and water pollution, assuming that everything is working correctly. They're relatively clean facilities." But some folks are concerned about the electricity use. They're saying, " Yeah, maybe the data center doesn't use that much water.

Maybe the data center doesn't pollute that much. But what about all of these new power plants that they're going to build in order to power it?"

Another set of concerns was basically the shadow of failed projects past



260805 main_EDIT: she points to the experience of Foxconn, where she says you have a big tech company show up in a very small community, in this case Mount Pleasant, Wisconsin, a city of 28,000, get hundreds of millions of dollars in infrastructure investment and tax subsidy from the town, promise 13,000 high-paying manufacturing jobs, and then pull out because [00:25:00] the contract wasn't set up correctly.

They decided they didn't actually want to build a bunch of flat-screen TVs in Wisconsin, and the town was left on the hook, having invested all this money in the grid and in roads They got, I think, 1,000 jobs in the end. Foxconn is still paying back all of this debt that has been accumulated Now, Now, obviously this isn't the norm, as most of these communities haven't had some big failed infrastructure project like this in their past.



260805 main_EDIT: but other communities hear those sort of stories and it adds to the pile

But But what about AI itself? my contention at the beginning was that the data center backlash wasn't as much about AI as you might assume

And and summing up the average attitudes that Jasmine found, it was less the sort of AI is evil rhetoric that you hear on social media

Nathaniel Whittemore: And instead, 

260805 main_EDIT: more view of it as something fairly insignificant that didn't justify all the concerns

Jasmine told Ezra, " " I went in and asked these organizers, 'Do you guys use AI? Do you find it useful?' And what I found was that a lot of these folks did say, 'Yeah, I've used it to draft an email or make a meme.' They're not denying that AI might have any possible utility at all, but they clearly didn't see it as essential [00:26:00] in the way that cars, energy, and housing are essential.

They saw it as a widget, a toy And maybe there are these risks, maybe there's this job stuff. But fundamentally they were like This thing is just not that useful. I don't really see in my personal life how this could justify these gigantic valuations.



260805 main_EDIT: but it turns out that's not really the thing. The concern with AI is not any of the substance of AI itself. for most, for most, it's not a critique of copyright or a concern about artists' jobs It's about AI as the new thing that is being imposed upon them

them said Jasmine The phrase you hear a lot from AI critics is, "Why is this being shoved down our throats?"

I I think that a lot of the public backlash to AI that has arisen over the past six months is not explained by people thinking that the technology has no use at all. It's not explained by their being worried about specific technical properties of large language models that might lead to rogue AI or misalignment or whatever.

It's AI as sort of an avatar for a small group of Silicon Valley billionaires' ability to impose their vision of the world onto everybody else without their consent



260805 main_EDIT: indeed indeed the part of the original piece that she chose to highlight in her announcement tweet read as follows. Quote, " [00:27:00] My conversations make me wonder if the technical content of data center deals is mostly beside the point.

Closed loop cooling systems? I don't believe them. Paying millions in taxes? I don't believe them. Creating 1,000 jobs? I don't believe them. I hear a reflexive skepticism of every claim. Rather, the way that AI companies engage with the communities, forcing NDAs, dangling billion-dollar promises, pushing environmental externalities far away from AI's user base, resembles a classic story about dark money in politics.

Your politicians are being bought by billionaires and gigantic corporations to screw you over. It's not Skynet, it's the oligarchy



260805 main_EDIT: As part As part of her conclusion, Jasmine writes, until the deeper cultural problems are addressed, the data center backlash will only recreate itself in other forms."



260805 main_EDIT: And And the reason that it's worth trying to have a better version of this conversation is not because we care so much about the hyperscalers' bottom lines



260805 main_EDIT: reason.org recently published a piece on why local data center moratoria are costly for the whole country

The author writes, " Moratoria pose a particular [00:28:00] challenge in the current environment. Instead of deliberating over the specifics of how a proposed project will interact with energy and water infrastructure in a particular community, these temporary bans force officials to consider data centers in the abstract

where those opposed to AI can more easily distort the facts. This is a difficult environment for good governance to take hold The political incentives that local leaders face to support moratoria given the ongoing national backlash are undeniable

They continue, " The most important benefits of data centers are not the jobs and tax revenue they bring to local communities, significant though those may be. They are essential infrastructure for virtually every computing task each of us now performs on a daily basis.

Preemptively crossing hundreds of communities off the list for potential development, often without any local justification, will make the development and use of AI, not to mention other types of computing, more expensive."

I I agree, although unlike that author

I think that the potential benefit to communities as well is immense

I think you have both national and aggregate reasons as well as local reasons to try with all our might to have a better version of this conversation But [00:29:00] what does that actually mean? Well, to be clear, I pretty much think it's on the job of the hyperscalers and labs and data center constructors to take the lead here In other words I do not believe that we can just yell at people for having conspiracy theories about data centers Or Or dismiss their concerns. I think that like it or not, if you are trying to build data centers The work of getting communities on your side is now mission critical.

So So how can we move from the absolutely abysmal job, as I said, that they are doing, to doing it better?

The The first part is a disposition and it's to have empathy for where people are. This does not mean indulging conspiracy theories



Nathaniel Whittemore: 

260805 main_EDIT: or accepting the notion that this is just some oligarchic power grab

But the people who are trying to get communities on their side need to understand that the reasons that those communities are skeptical

are legitimate and come from a real place. They are rooted in what they have seen and what they've experienced and what they continue to experience there are concerns that even if in some cases more emotional than intellectual, cannot be simply swept to the side



260805 main_EDIT: when a key problem of a discourse is that [00:30:00] people on one side do not feel like they have agency and do not feel like they are being heard, you have to start with making sure that they feel heard. Without it, you can't even get into the substance of the argument

Next up

to say again something that I say all the time on this show, we have to be making a better argument for the overall why

And the And the reason that in general, we need more data centers. The The argument cannot, and I mean cannot be, " 

Nathaniel Whittemore: Well, 

260805 main_EDIT: it's simply inevitable, and we're going to have this technology one way or another." And And it also can't be, "Well, if we don't do it, China will." The The only acceptable answer to why AI and by extension data centers get to exist



260805 main_EDIT: has to be an explanation of how having more data centers improves people's lives as they live them

If we do not make this case loudly and convincingly, nothing else that we talk about matters in the slightest

Nathaniel Whittemore: From From 

260805 main_EDIT: there, The conversation has to move from the general to the specific As As pointed out by Reason, the moratorium discourse keeps the conversation about data centers in general. [00:31:00] And And while, yes, I just argued that companies who are building data centers need to tell the positive general story about why data centers and AI should exist, they do not wanna have to convince a local community that all data centers are good.

Instead, they need to be able to engage with the local community on how to make that specific project that they are dealing with good

Every Every project needs to earn local support on its actual merits, but also not be weighted by the potential demerits of other projects

Oh, Oh, and by the way, that conversation has to happen transparently. The days of backroom deals are over. Trust cannot in any way, in any context, be negotiated behind closed doors. The process, the trade-offs, the promises, the commitments, the concerns, the pushback, the counteroffers, all of that has to be visible.

It does not matter that that makes the process more inefficient In fact 

Nathaniel Whittemore: 

260805 main_EDIT: what data center builders fail to realize is that they are primarily not involved [00:32:00] exclusively in a business process This is now a democratic process

And And inefficiency is not simply a byproduct of democratic process

but but is structurally integral to it. it. Friction

Slowness, back and forth

are what happens when people are actually being heard

Now, perhaps Now perhaps overly optimistically, and frankly you even see this in Jasmine Sun's piece as well. I don't necessarily think that all these data center builders were sneakily trying to cut backroom deals in smoky cigar-filled rooms. I think that it's just for a long time



260805 main_EDIT: the norms weren't to invite everyone into the deal-making process. They were to talk with the officials in charge of the decision and let them handle their local constituencies 

Nathaniel Whittemore: 

260805 main_EDIT: and so hopefully a recognition that this process is now fundamentally different than that 

will allow the builders and hyperscalers to come on board with a very different way of approaching it, one that is fundamentally transparent

when it comes Now, when it comes to the specific incentives and how to make

data centers work for communities. I I don't know that I think that there is a perfect template yet for how to address the [00:33:00] concerns of citizens and how to make data centers most opportune for those citizens I I do know that whereas companies used to think that they were going to get tax breaks for bringing their business to a place That has shifted entirely 180 to now companies needing to be in the mindset of allocating a meaningful part of their costs to getting town buy-in ne- companies will and need to spend real money solving local concerns and making data centers work for people

I think some of the floor of this type of work is going to be things like making sure the data centers pay for their own way when it comes to the cost increases for things like electricity.

But I also think that that's going to be found to be insufficient. I think data centers are going to have to be extremely generous and do more than cover their own costs, but in fact foot the bill for many others and potentially invest in the community in other ways as well



Nathaniel Whittemore: 

260805 main_EDIT: reinforcing

reinforcing this and putting a bottom line on all of it, thinking about how a data center benefits the local community is now core infrastructure to the project

I I mean this both in terms of intention and actual budget The The percentage of the budget that [00:34:00] is going to be allocated for addressing concerns and providing local incentives needs to increase dramatically, period, full stop. And frankly, if you're sitting there arguing to me that that's the thing that's gonna break the bank for these projects, you need to get out of show business



260805 main_EDIT: when push comes to shove, I am far less pessimistic than many 

Nathaniel Whittemore: 

260805 main_EDIT: about the data center backlash



260805 main_EDIT: I, Part of that is that I think it is quintessentially American and integral to who we are as a people to be able to raise our voices and push back against things that affect our lives that we don't agree with or have concerns about



Nathaniel Whittemore: 

260805 main_EDIT: the

the messiness while frustrating to the builders 

Nathaniel Whittemore: is like it or not, democracy in action. But But more than that

260805 main_EDIT: There is so much opportunity

to make this infrastructure work for everyone. yes, there are some communities where it is simply not going to work

For whatever reason, could be because the energy requirements just aren't there Or because people just aren't willing to deal with the negative externalities like noise pollution.

But But there will be in many more communities, I believe, the [00:35:00] ability to find win-wins for everyone



260805 main_EDIT: where this particular type of infrastructure

can actually be a valued part of a community's next phase I think I think our failure to do this so far

is a failure of understanding and a failure of imagination, and I think both of those can be addressed comp-- for any of you who are dealing with the hyperscalers or labs who are building these data centers and are wondering what to do next, send them this argument in my email.

I will happily shout at them directly. For now, that's gonna do it for today's AI Daily Brief. Appreciate you listening or watching as always, and until next time, peace. 

​ 

Nathaniel Whittemore's audio recording:
