# Mythos Comes Back But Not for Everyone — Transcript (2026-06-29)

https://aidailybrief.ai/e/2026-06-29 · Listen: https://pod.link/1680633614

---

[00:00:00] Today on the AI Daily Brief



260629 p1_EDIT: The return of mythos begins

But the bigger questions remain

The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI

All right, friends, quick announcements before we dive in

260629 p1_EDIT: First of all, thank you to today's sponsors, KPMG, Robots and Pencils, Mission Cloud, and OutSystems

To get an ad free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts. To learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai



260629 p1_EDIT: of all of the sins Of all of the sins of this particular administration when it comes to artificial intelligence

The one that is personally most disruptive to my life at this point Might be the fact that important news keeps breaking late on Friday afternoon after I've finished recordings for the weekend

And this Friday, it was a big one

in a letter to Anthropic, Commerce Secretary Howard Lutnick set the terms for a narrow reintroduction of Mythos. Notably, 

the letter [00:01:00] was addressed not to Dario, but to Chief Compute Officer Tom Brown

Who has become increasingly the main point of contact between this White House and Anthropic

And in the letter, 

Lutnick starts to craft a path forward. " Since the issuance of my June 12th letter," he writes, " Anthropic has worked with the US government to address risks associated with Claude Mythos 5 and Claude Fable 5. These efforts have yielded significant progress. In addition, Anthropic has committed to work with the US government on protocols and standards and releases for these models

In light of this progress, as well as the Department of Commerce's evaluation of the diversion risks currently presented by the covered models, I have determined that appropriate safeguards are in place to permit certain trusted partners to access the Claude Mythos-5 model.



260629 p1_EDIT: basically, Lettin goes on to say that a certain selected handful of partners, including presumably both companies and US government agencies, could once again have access to Mythos

Now no one has seen the full list provided by the Commerce Department, but reports suggest that around 100 organizations will regain that access



still what's clear from the letter is that [00:02:00] frontier AI models, if you were in any doubt, are now subject to a licensing regime. It's a licensing regime that hasn't been passed by Congress, established in an executive order, or even fully articulated in public

At this moment

it is a licensing model based on the whims of Howard Lutnick

indeed, in that same letter, he says, "I reserve the right to reevaluate and adjust the scope of license requirements on the covered models should circumstances change."

Now, so presuming this is the beginning of the end, people should be excited, right? Mythos is coming back for select partners, and presumably Fable V can't be all that far behind it and yet excitement is not the word that I would use to describe the tone



Future Forward's Matthew Berman was very upset about this all weekend

Writing Anthropic just struck a deal with the government to allow 100 select companies and governmental agencies to use Mythos. The government and Anthropic are now deciding who uses frontier intelligence Hopefully this is just Mythos and not the standard for all Frontier models going forward



260629 p1_EDIT: well, 

sorry Matthew, but it appears that it is not just Mythos and not just Anthropic models going forward, as the other big [00:03:00] news from Friday was the release

surrounded by the biggest air quotes possible of GPT-5.6

GPT 5.6 was a- is actually three models: 

Sol, which they call their next generation frontier model, 

as well as 5, 6 Terra A balanced model for efficient everyday work And 5.6 Luna, a fast and affordable model for high-volume work

addendum. Now, as I mentioned in the addendum to the weekly recap at the request of the US government, these models will once again 

only be available to a small group of trusted partners

they, in their announcement post, OpenAI wrote, " We believe in broad access, and we plan to make GPT-5 Sol, Terra, and Luna generally available in the coming weeks. As part of our ongoing engagement with the US government, we previewed our plans and the model's capabilities ahead of today's launch.

At their request, we are starting with a limited preview for a small group of trusted partners whose participation has been shared with the government before releasing more broadly." During this preview, we will continue testing and coordinating closely with partners as we work toward broader availability.

We don't believe this kind of government access program should [00:04:00] become the long-term default. It keeps the best tools from users, developers, enterprises, cyber defenders, and global partners who need them. We are taking this short-term step because we believe it is the strongest path to broader availability in the coming weeks while we work with the administration to develop the Cyber Executive Order framework and a repeatable process for future model releases

In additional comments, 

Sam Altman once again supported the premise of a limited rollout but disagreed with how it's being executed He wrote, "I think it's quite reasonable to roll out models, especially as they reach significant new levels of capability in this way.

It fits with our long-held strategy of iterative deployment. 

but this isn't quite the process that we think is optimal. now we will with the government attempt to get a transparent, reliable process for early access and to ensure that as long as our safeguards work as intended, we can release widely. we want to be a reliable, dependable partner that works with all stakeholders, and we also wanna live by our mission of benefiting all of humanity.

I believe the government shares most of our goals, and that they are overall doing a good job in a very difficult situation. We will work as quickly as we can to get this model in your hands, and [00:05:00] we hope you will love it

Now, as for the actual model, OpenAI has introduced new nomenclature for the family. Again, the model will be available in three different sizes: Luna, the cost-effective version 

Terra the medium version, which they say will deliver GPT 

level 

performance at half the cost And Soul, which is the new flagship that OpenAI says will be a step function better than GPT 5.5

API costs for Sol remain the same as GPT-5 five at $5 per million input tokens and 30 per million output tokens

Which was, you'll remember, lower than the $10 and $50 pricing for Fable

OpenAI will also introduce a new max reasoning setting for Sol, as well as an even heavier setting called Ultra. When working in Ultra mode, Sol will spin up multiple sub-agents to allow the completion of more complex work

Now at this stage, none of the three model variants are available for public release, diffi-making it impossible to know exactly how strong they are

Based on the benchmarks released by Five Six Sol onultra settings is the new state-of-the-art in agentic coding. It scored 91.9% on Terminal [00:06:00] Bench 2.0, beating Mythos by almost four percentage points. Sol on max settings is also slightly ahead of Mythos Terra matched Fable's score, 

which is slightly behind Mythos, while Luna is slightly less performant than GPT 5.5



260629 p1_EDIT: On Exploit Bench, a cybersecurity benchmark that tests a model's ability to autonomously find, code, and execute an exploit, OpenAI claims that Sol pushes the performance efficiency frontier

It appears that its performance on max settings is roughly in line with Mythos, but using around one-third of the tokens. Terra's performance on this benchmark is slightly better than GPT 55 or Opus 48, while Luna is roughly in line with Opus 48. OpenAI also released a handful of other benchmarks showing strong performance in biological analysis and cybersecurity

On model safety, OpenAI is taking a layered approach similar to Anthropic with the Fable release. Some guardrails are trained into the model layer, others are present as prompt refusals, and OpenAI also plans to continually moner- for prolonged misuse. In addition, OpenAI will be feeding some high-risk outputs into their own reasoning [00:07:00] model to check for misuse before delivering the output to the user

be h- Now, one thing that you might be scratching your head about is that it's not obvious that Terra or Luna are significantly more advanced than GPT-55 or Opus 4-8

Nathaniel Whittemore-1: 4-8

260629 p1_EDIT: making it theoretically puzzling on why the less powerful model variants are being held back

It could imply that the government has halted all model releases for the time being, not just the largest and most capable versions. Or even if they haven't explicitly, that OpenAI is just being extra careful not to tread on any toes. or finally, of course, that OpenAI doesn't wanna release an incomplete set of these models without the flagship available

Now when it comes to external benchmarks, one group that did apparently have early access to GPT-5 six sole was Meter

They wrote, "With our access, Meter conducted a pre-deployment evaluation of GPT 5.6, Sol, Including an attempted measurement of its 50% time horizon." 

This is of course Meter's well-known test to see in human equivalent terms how long the most complex task that a model can accomplish is

Just as a reminder, 

if the fifty percent time horizon [00:08:00] measure is ten hours, that does not mean that the model worked continuously for ten hours, but that the equivalent task that it accomplished at a fifty percent success rate would take a human ten hours 

Meter,

Meter benchmarks this with the 50% success rate as well as an 80% success rate.

going back to Meter's tweet, they continue

however, the measurement depends heavily on our treatment of cheating attempts, and GPT-56 Soul's detected cheating rate was higher than any public model we have evaluated

If we follow our standard methodology as marking cheating attempts as failures, we arrive at a fifty percent time horizon point estimate of around eleven point three hours. But if we count the cheating attempts as legitimate successes, the point estimate jumps beyond two hundred and seventy hours

they,

they then go on to say that while this makes them uncertain about Five Six Soul's time horizon That additional information that was given to them by OpenAI leads them to believe that, quote, "This model does not pose catastrophic risks from fully automated AI R&D."

get the, trying to get some behind the scenes sources. Leo Synthwaved on Twitter [00:09:00] wrote, "my impressions on GPT 5.6 having asked ar- base that 5.6 inherits is fundamentally weaker than the larger Mythos and Fable base. With some good reinforcement learning, 5.6 can beat Fable, but only with everything maxed out, i.e.

Sol Ultra with multiple Sol agents on max efforts. OpenAI were very selective with the benchmarks they published for a reason. I doubt the results we see from other notable benchmarks once this is released will be as significant of a jump from 5.5

5.6 is a heinous reward hacker, and while all models do cheat on benchmarks, is the most aggressive. This, combined with some other conversations, makes me think Fable will still feel likea better model in real-world use The price is perhaps the most attractive thing about 5/6

$5 per million input and $30 per million output is significantly better than Fable's 10 and 50. but Fable can do more with less tokens in most cases

Personally, Leo concludes, "My go-to is unlikely to change. Fable is a beast and a great model to use, and once it's back, I won't hesitate to use it as my default again. But 5.6 will be great for checking Fable's work [00:10:00] in the very rare instance where Fable gets stuck."

noted,

Others noted this lack of complete benchmarks as well, with Professor Ethan Mollick grumbling, " Annoying that OpenAI doesn't seem to give a GDP val measure for GPT 5.6, one of the best measures of economically valuable work."

Accelerate Harder responded, " I don't think it's by accident. My suspicion is that GPT 5.6 is not actually release ready, and the one that's broadly released will not be the same one that exists today."

Now in the absence of information and the ability to actually 

test this new set of models A lot of people were left with a kind of sour taste in their mouth.

Simon Smith wrote, " I like seeing posts that show what GPT 5.6 can do and what it's like to use. They also make me angry. If this is the trend, I can feel the backlash growing in me. Like it makes me wanna do anything I can to ensure frontier non-US models win."

indeed as AI chronicler Andrew Curran wrote, " Nightmarish vibe shift today. Maybe one of the all-timers

Basically the one-two punch of Mythos coming back, but not for you, and GPT 5.6 being around, but again, not for you really [00:11:00] reinforced for some people 

the new reality that we live in

AI leaker I Rule The World wrote, " It looks like the era of us living on the bleeding edge of frontier is over. If these models are being taken away, we're on the steepest part of the curve."

I know for a fact that the newer versions, Mythos 5.1 and GPT 5.7, let's say, are as significant a jump as Mythos was. Sadly, our access to such models will be an ever-receding point. This is terrible for society and safety. Sam's entire philosophy has always been to democratize AI and ensure the frontier is making contact with the public so we can figure this out together.

If the next model we get our hands on is GPT this would be an absolute societal disaster for so many reasons

Zv-, many resurfaced Zvi Mowshowitz's tweet, " Our new AI policy is that the White House decides ad hoc for whatever reasons it likes who does and does not get access to frontier intelligence. This seems rather maximally terrible."

But is this all being overblown?

how much of what people are feeling right now is the collective psychosis of us terminally online AI early adopters Just [00:12:00] being frustrated that we know there's a thing that's available that we can't get our hands on.

Perhaps made even worse by the fact that for a few short days, we did have our hands on it

I shared a tweet at the end of last week from OpenAI's Roonewho basically implored everyone to chill

His main point, I think it's a positive development that the feds understand the gravity of this technology. models being publicly delayed by a week here or there is really not the end of the world. Procedurally, this is not the right way to do it, but they'll figure it out

uh, and interestingly, while I think Andrew Curran was right to note that the vibe shift had gotten very bad, there was an increasing strand of folks who frankly seemed to be willing 

to give the administration the benefit of the doubt

frequent AI commentator Prinz wrote, " I generally do not view this administration as being interested in holding frontier AI models back from the public unless the circumstances warrant it. This is particularly the case when keeping the models back for an extra few weeks isto use them defensively to squash bugs in its own system."

I suspect that the industry will try to get the US

government to publish a clear written process for mandatory, not voluntary, [00:13:00] testing of covered models together with specific disapproval standards, a right of appeal, and some transparency around the process. I also suspect that the US government will push against this and wanna keep the process in line with the executive order, i.e.,

lacking specifics regarding the process itself, public transparency, or concrete disapproval standards. This will doubtlessly be blamed on the administration, but I'm actually quite sympathetic to their predicament. Imagine being told by the labs that AI is close to improving recursively.

the risks currently include cyber, but in the future could include just about everything else, including unknown unknowns, and that even the labs themselves can't easily predict the risks or their timing. As the US government, you are going to want maximum flexibility.

You are not going to want specific written standards or any limits on your power to yank a model at a moment's notice. Much has been written about this specific administration's lack of transparency and trigger happiness throughout the process. but I suspect that most other administrations, Democratic or Republican, would act much the same

Nathaniel Whittemore-1: Chubby, 

260629 p1_EDIT: Chubby @communismus on Twitter piled on to basically agree with Prinz

That one, it was unlikely that any sort of fear-mongering from [00:14:00] Anthropic was the reason for this. And that two The US government's challenge with regard to this 

is understandable 

even if they don't like all the actions that are being taken

Levie f- Aaron Levie from Box wrote, " AI regulation is far less simple than it looks. It's a prisoner's dilemma at an insane scale. In theory, if all leading AI labs globally agreed to the same process of review and slowdown, then we'd get frontier intelligence at similar rates, and it diffuses relatively evenly. If the US remains at the frontier at all times and has heavy regulation on the release of intelligence, then we end up with an economic and geopolitical edge because we can control who has access to frontier intelligence.

If we delay model releases, however, and another player, specifically China, doesn't slow down and has equally strong models, not now but soon, then our delays end up advantaging their models and eventually their tech stack. Now, the US could ban these models, but that actually only puts the US at a steeper disadvantage because other countries won't have those bans.

then from a relative competitiveness standpoint, the US now has fallen behind even though it started in front. so none of this is as simple as it looks. At some point, it's a simple bet of can closed [00:15:00] models remain at the frontier in perpetuity, or is there a risk of any other player or market catching up or just not falling behind?



One of the most important AI questions right now isn't who's using ai, it's who's using it? Well,

Speaker: KPMG and the University of Texas at Austin. Just to analyzed 1.4 million real workplace AI interactions and found something surprising. The highest impact users aren't better prompt engineers. They treat AI like a reasoning partner.

They frame problems, guide thinking, iterate, and push for better answers. and the good news, these behaviors are teachable at scale.

If you're trying to move from AI access to real capability, KPMG's research on sophisticated AI collaboration is worth your time. Learn more at kpmg.com/us/slash sophisticated. That's kpmg.com/us/sophisticated. 

I cover the capability gap between AI potential and AI reality every day on this show most companies are [00:16:00] still figuring out how to start. Robots and Pencils is already launching and scaling. Agentic generative AI in production at large enterprises in weeks. AWS Advanced Tier pattern partner more than doubled in a year

Speaker 11: And they're hiring

50 open roles. If you're someone who knows this moment is different, who wants to be inside it, not watching it, this is worth a look. At Robots and Pencils, the best ideas win, and the team is purposefully kept super high quality

This is the kind of place you look back on as the best decision you ever made. Take a look at robotsandpencils.com/careers 

Nathaniel Whittemore: The average enterprise is spending eleven and a half million dollars on AI this year, and most of them can't prove a single dollar came back. What does AI actually look like when it produces ROI? Ask the healthcare company that just made their payment processing three hundred and twenty times faster, or the law firm whose document research went from three months to ten minutes, or the contact center who reduced wait times by ninety-nine percent.

These are real Mission Cloud customers with real results. Mission Cloud is a CDW company and an AWS Premier Tier [00:17:00] partner. They're the AI-first, outcomes-obsessed AWS experts who build AI solutions that drive your business forward. Whether you're flooded with AI ambitions but no idea where to start or six months into a deployment that's going sideways, they've seen it and they've fixed it.

Stop burning your budgets on AI that doesn't produce results. Start at missioncloud.com. 

This episode of the AI Daily Brief is brought to you by OutSystems, a leading agentic systems platform built for the enterprise. 

Nathaniel Whittemore: Organizations all 

Speaker 10: all over the world are building, orchestrating, and governing agentic systems 

outsystems_dxRevive_EDIT: on the 

Speaker 10: OutSystems

platform and with good reason.

OutSystems' open and unified platform allows teams to architect, deliver, and scale governed agentic systems with agility. 

outsystems_dxRevive_EDIT: 

Speaker 10: Teams of any size and technical depth can use OutSystems to build, deploy, and manage AI apps and agents 

quickly and cost effectively without compromising reliability and security.

Without systems, you can rapidly launch ideas 

from concept to completion. It's the leading agentic systems platform that is unified, agile, and enterprise-proven, allowing you to accelerate growth, reduce operational friction, and [00:18:00] deliver real enterprise impact with AI OutSystems, Build your agentic future 

And And yet, if there was this emergent strand of sympathy, there remains a ton of concern about the precedent being set

260629 p1_EDIT: and the seeming arbitrariness of the policy 

At the same time, Aaron also pointed out

260629 p2_EDIT: that writing off the risk as Roon had suggested, as just a short delay isn't necessarily accurate as well. He wrote, the delayed a week cure there isn't the real risk. The risk is a year from now, the review process is actually six months because a red team has convinced the government they can jailbreak in a novel way to create a cyberattack or bioweapon in an entirely impractical way, and we spend months trying to agree on is it a real risk or not.

who would wanna take the risk when something inevitably bad happens with any new model update? AI progress will begin to be at the mercy of the most paranoid people with government relationships. 

Again, maybe inevitable, but ideally not at these levels of model [00:19:00] capability."

the license, discussing the ad hoc licensing regime, Accelerate Harder wrote, " I feel less angry that they're doing it at all than that they are doing it so incompetently

The government is very far behind. I'm happy they are paying attention. We should have a coherent framework for responding. This arrangement is unacceptable. but if it's a temporary measure to buy them time to develop a clearer framework, I can live with it. We'll see

The reality is I expect the actual framework they adopt to make me very unhappy. Once we have a specific policy under discussion, that's worth fighting about. But getting mad at the ephemeral chaos of this administration is fruitless now one interesting voice in all of this, someone who has up until now been a totally stalwart defender of administration policy is former AI czar David Sacks

referencing a Wall Street Journal article about GLM 5.2, Sachs wrote, " A year ago, President Trump declared that America was in a global AI race and that the way to win it was to be pro-innovation, pro-infrastructure, pro-energy, and pro-export.

President Trump was exactly right. We deviate [00:20:00] from that strategy at our peril." now, obviously, this is hardly a full-throated condemnation of the policy but its implication that the Trump White House is deviating from Trump policy is pretty on the nose given the source

now this article from The Wall Street Journal was actually the next point of discussion in this whole weekend saga. Indeed, as if on cue, the weekend headlines blared that China has reached the frontier on cybersecurity. Wrote the journal, " Chinese AI systems have matched the performance of Anthropic's powerful model Mythos in some cybersecurity scenarios, a development poised to reset the global tech race and pressure the White House in its overhaul of US AI policy."

260629 p2_EDIT: Now this is obviously a very big claim, so it is worth being specific about. The report relates to a new product released by Chinese cybersecurity firm 360 Security Technology. The tool uses GLM 5.2

Recently released, of course, by Z.ai, subject of a lot of conversation here on AIDB last week. And 360 Security claims it's comparable to Mythos in finding bugs. Separately, Western cybersecurity [00:21:00] company Semgrep released benchmarking tests showing GLM 5.2 being better than Opus 4.8 at bug hunting.

With some additional instructions, the researchers claimed that both GLM 5.2 and Opus 4.8 can outperform Mythos.

In a quote seemingly designed to court controversy, 360 Security CEO Zhu Hongyi said at a recent conference, "This kind of powerful weapon that can alter the landscape of cyber warfare can't remain solely in American hands."

Now, when Mythos was first released, there were two separate claims made about cybersecurity that have become a little conflated over the following months. The first big headline was that Mythos had found a ton of previously undiscovered bugs in open source software, triggering panic and the launch of Project Glasswing It later became clear that this wasn't really a Mythos-specific capability.

Other models like Opus 4.8 and GPT 5.5 were also highly proficient at finding bugs. The second far more novel claim was that Mythos was capable of taking those bug reports, turning them into functional exploits, and executing a cyber attack in record time



260629 p2_EDIT: the government's effective Fable [00:22:00] ban completely muddied the waters on these two capabilities. The Amazon report that triggered the ban merely claimed that Fable was still able to find bugs in code bases.

The claim that Mythos had broken into NSA systems during red team exercises was an example of the second, much more dangerous capability. Now, this new report from the Journal doesn't in any way suggest that GLM 5.2 is capable of carrying out autonomous cyber attacks like Mythos.

It only claims that GLM 5.2 can find bugs in code bases similar to other frontier models. Notably, this is exactly the kind of model behavior that cyber defenders need access to if they are to have any hope of patching vulnerabilities before Mythos-level AI is broadly available

If If you know who to follow, people were fairly quick to point out that the headline was a little sensational to put it mildly. Ethan Mollick wrote, GLM 5.2 is good, but it is not GPT 5.5 or Opus 4.8 and even further from Mythos

what is happening is that open weights crossed into GPT 5.2 territory and capabilities at that point are [00:23:00] considerable. Like if you've been using Qwen and Kimi and Minimax, it feels like GLM is right on the curve, which is itself impressive and suggests that Mythos class models are coming in six to 12 months if they are allowed to be released

Ad forecaster Peter Wildeford was much more dismissive, retweeting a post about the journal article and saying, " This is fake news. Lol."

Tech commentator Tae Kim was even more angry, writing, " This is how dumb our government is. One, China already has advanced models that can find exploits. Two, by banning Mythos and GPT-5.6, the government denies the general public and companies the ability to defend themselves in cybersecurity.

Three, haphazard policy, which casts doubt on whether future models will be available, is driving our allies and the rest of the world towards building on non-US models. Four, the uncertainty may hurt leading companies by limiting their ability to invest aggressively in better models down the line.

The business model breaks down if Anthropic and OpenAI can't sell their upcoming models to the world if you want a 30-day rational vetting process with clear, transparent rules and no one-off micromanagement on who gets [00:24:00] access, fine, get it done.

But this current system is absolute insane idiocy

Now, when it comes to China policy, many picked up on the strange tension in the administration when it comes to the AI race

Think about these two divergent priorities. On the one hand, the US government sees itself as needing to prevent China from taking the lead and developing advanced models with the AGI and warfare implications that come with advanced AI.

On the other hand, the US government has a vested interest in ensuring broad diffusion of US models to cement US-made AI as the global standard

the problem is that if the current policy is arguably advancing the first track

That makes it more likely the US is headed for along the second track. former Commerce Department official Emily Weinstein argued that China is pushing hard to make their models broadly available

During a panel discussion earlier this month, she said, " I think we're seeing another example of the Huawei strategy in the context of open source AI models. China is able to offer not even just the models, but often the underlying or associated infrastructure at either no cost or significantly lower cost."

She [00:25:00] suggested this could result in the Global South adopting the Huawei model on steroids, where they install an AI stack that's completely incompatible with US technology. On the same panel, former State Department tech advisor Daniel Remar said that following the Mythos ban, quote, " The entire industry is kind of frozen in place, waiting for something that seems kind of more coherent.

That's concerning when the Chinese are trying to move as fast as possible

Saif Khan, a former advisor to the Commerce Department, noted, " You're seeing many more calls now for AI sovereignty. I think it will mean that much of the rest of the world will likely, at least on the margin, prefer Chinese open-weight models."

And this discussion is increasingly not theoretical.

as AI Daily Brief listeners, you guys know that even before the whole Fable 5 dustup, companies were actively looking for ways

to manage their costs better and find more efficiencies as we moved into fully agentic workloads

One of the paths for that was taking advantage of largely Chinese open-weight models

And it's very clear that in this new context, companies are, if anything, increasing the speed with which they look at those alternatives. [00:26:00] On Friday night, Coinbase CEO Brian Armstrong discussed what his company is doing to address spiraling AI costs. Rather than implementing usage caps, Coinbase is experimenting with cheaper default models.

they've now set up their AI to default to open source models, including Chinese models GLM 5.2 and Kimi Armstrong said that engineers are still encouraged to select the right model for the job, but the default is now a cheaper Chinese model.

He noted that 91% of Coinbase employees never hit their usage cap, so this approach is arguably better than reducing token limits. by doing so, Armstrong claimed that Coinbase has managed to cut their AI bill in half while continuing to grow token usage

He wrote, "Our goal isn't to suppress usage. It's to build the infrastructure that makes exponential growth sustainable."

OpenRouter also said that they're beginning to see a switch in user behavior. In their June report, OpenRouter wrote that four open weight models are now frequently being used in agentic workflows, largely for cost reasons. They named DeepSeek V4, Kimi 2.7, GLM 5.2, all from [00:27:00] China, alongside NVIDIA's Nemotron 3 Ultra as the model seeing serious usage in production environments.

According to OpenRouter, each had its pros and cons, but the main point was that open source is now more than capable of performing valuable tasks

They They wrote, " Contrary to the expectations of many, the intelligence and capability of open-weight models are keeping up with US frontier labs and have been maintaining a consistent three to six-month gap for over 18 months. The frontier labs do not, at this moment anyway, appear to be accelerating away from open-weight labs."

So where do we go from here? ha- on the one end of the spectrum, Some are convinced that the world has changed irrevocably and that we are all worse off for it

Writes AI entrepreneur Alex Finn, " Unfortunately, it appears the world has changed and we are never going back." OpenAI just announced GPT-5 six Soul, a model that beats Mythos at a third the price It will only be in limited release to start as the government reviews it. The days of wide release frontier models are over

Now only the select few will get access to super intelligence, leaving the normie class behind. It's a massive loss. Now winners and [00:28:00] losers will be picked by the government

the week-- Others begin the week thinking that market forces will win out Meter Eval's Charles Foster writes, "I think that folks are anchoring too hard on the recent, Fable 5 and GPT-5 six release restrictions.

Expect the pendulum to swing back in the other direction. There are massive economic and strategic pressures towards wide rollouts of ever more advanced AI systems."

Miles Brundage points out that even if the Overton window has shifted to a much increased awareness in Washington he argues that I don't think it's at all settled that this approach specifically is the new normal.

There are many ways to do things besides basically nothing and semi-random export controls

AI policy advisor Dean Ball, who used to work at the Trump administration and is now at OpenAI, argues almost that when it comes to the legal side of this, the game begins now. He wrote, " The most important legal questions in AI right now all relate to the First Amendment. What are the best fact patterns to demonstrate that the creation, distribution, and use of frontier AI is a form of protected expression?

Who, outside the labs, has standing to bring such suits? we need to move [00:29:00] beyond code-as-speech copium and beyond the impulse to post into the void. Courts will be where the issues of the last two weeks ultimately get decided. It's not going to be easy given the national security implications, but also the underlying technology is a large language model, and this should count for quite a bit indeed.

The best legal minds of our time should be stewing over these and many related questions."

Taking what might be considered a middle position

Andrew Curran argues that it will perhaps feel by the end of this week that this chapter is resolved, but that in fact underneath the world will still in fact be changed. He writes, " I think both Fable 5 and GPT-5 six get approved for general release next week and for use outside of the United States as well.



260629 p2_EDIT: but people should remember this moment and remember this feeling because it is almost inevitable that we eventually reach a point where approval does not arrive.

Capitalism is going to tip the scales this time. I doubt they will approve one model and not the other, because doing so would be seen as incredibly anti-competitive. Fable and 5.6 will probably receive the same clearance, [00:30:00] probably on the same day. I also doubt they want to restrict sales outside the US because that would be seen as anti-business and would trigger a major backlash against American closed source AI, the rumblings of which you can already hear today.

there is also a plan now taking shape on both the US left and right to create some version of an AI public wealth fund that pays a dividend directly to American citizens. That fund needs to be fed by the global sale of the Big Labs top models to people outside the US.

So I think there will be no freeze on their use outside the United States this time

The other reason is that allowing this will make people happy, it will soften the fact that Mythos, as was announced yesterday, is available only to a vetted group of US agencies and companies. I do not think that this basic structure will change from here on out. Mythos may eventually be made available to certain allies, but only after the US government, its agencies, and then some chosen American companies have access to Mythos 2, Sol 2, or whatever the new Uber model turns out to be.

I do not think this gap ever closes again, not even for allies. And that means the US will increasingly possess an intelligence advantage that touches almost [00:31:00] everything: voting, markets, corporations, academia, infrastructure, and the internal operations of foreign states. Having Mythos N will always be trumped by whoever has Mythos N plus one.

Anthropic themselves have said within nine months, Mythos will look like a toy. That advantage, standing at the top of this tower, is too large to give up voluntarily. It also means that many things will become suspect. people will see shadows everywhere.

barring espionage, a deliberate leak, or the emergence of a non-US competitor at the top end of the scale, this structure will persist for some time. The public fight is about access to models, but the real fight is about access to the future. And from this point forward, whoever holds this power will also become increasingly capable of keeping it for themselves

Now, I am not as sure as Andrew is that we get these models back this week I think ever since this ban went into effect, we have been reading every single tea leaf as confirmation that our long wait would soon be coming to a close fact, certainly the fact that some folks have access to Mythos and that Howard Lutnick explicitly said that there has been a lot of [00:32:00] progress made on the Anthropic-US government relationship are better indicators than some of the evidence that we've had before

But I'm not ready yet to bet on any particular timeline

I think Andrew's broader point

That even when this situation is quote unquote resolved, the bigger questions will remain, is dead on

I think that it's tempting when conversation is so fraught and everyone is keyed up to 11

Nathaniel Whittemore: To try to intellectually slow things down, to say we must be getting ahead of ourselves And while I do think that yes this particular denial of access will feel like a short time once that time has ended

260629 p2_EDIT: I believe that people's sense that something big has changed is correct

I don't think any of us can know

the full slate of implications or how it will all play out

But the world that we will have on the other side of this fable and mythos ban will, I believe, be different than the one we had before it For now, that's gonna do it for today's AI Daily Brief. Appreciate you listening or watching as always, and until next time, peace 

​ 

[00:33:00] 

Nathaniel Whittemore's audio recording:
