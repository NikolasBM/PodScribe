# The AI Industry Asks Government to Slow It Down — Transcript (2026-07-29)

https://aidailybrief.ai/e/2026-07-29 · Listen: https://pod.link/1680633614

<!-- metadata -->
Format: news-analysis · Level: 1 · Length: ~00:29:00
Host: Nathaniel Whittemore
Categories: safety-security, policy, open-weights
Featured: open-weight models, OpenAI, Anthropic, Pacing the Frontier, distillation
Also mentioned: GLM, Kimi, recursive self-improvement
<!-- /metadata -->

---

[00:00:00] Today in Today in the AI Daily Brief we are talking about what some are calling the new AI pause letter pacing the frontier, and what it says about where we are

in the history of this AI transformation



The The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI

All right, friends, quick announcements before we dive in

First First of all, thank you to today's sponsors, KPMG, Blitzy, Retool, and Airtable



to get an ad free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts

To learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai

Also, for those of you who are looking to keep your AI skills up this summer, come check out our latest free training program. You can find it at summeradventure.ai, and it is a choose your own adventure with a full range of different AI skills available to you

Come Come join a couple thousand AI friends and have an adventure

Welcome back to the AI Daily Brief. Today was actually [00:01:00] supposed to be a pre-record over here. I'm with KPMG at their annual tech symposium event, And we have a really fire operators cut show about understanding and maximizing token budgets coming

But then

We got the latest open letter in the long lineage of AI open letters

And the sheer volume of the conversation around it, I think demanded that we dive in a little bit



now now before we get into the Pacing the Frontier letter, we have to go back a couple of days to where we left off

At that point, basically every major company in the tech industry had signed an open letter urging the Trump administration to protect open source AI. The effort was led by Nvidia and Microsoft and supported by several dozen companies across both big and little tech. Most notably, after a brief delay upon its arrival, OpenAI signed the letter, but Anthropic remained conspicuously absent from the petition, thus leading to the title of yesterday's show on the AI Daily Brief

The debate was, of course, raging in the context of the Trump administration narrowing in on a framework for AI safety testing

The The June executive order set a deadline of August first for the creation [00:02:00] of the framework, so this is the critical week to impact the policy that would govern AI deployment and model releases in the US On top of that, there has been a raging debate about what to do about Chinese AI



inspired first by sensational headlines around GLM 5.2 and then Kimi K3, there have been rumblings that the Trump administration was debating a ban on Chinese open source

And what's more, this was not just happening behind closed doors. This was clearly a live debate with multiple factions within the White House advocating their policy views in public We got tweets on either side of it from Treasury Secretary Scott Bessent and, and Commerce Secretary Howard Lutnick

There is, in other words, and I think this is important, a a feeling of a crescendo moment right now The The AI of 2026 is very clearly not the AI of 2025. The policy implications of this 2026 are clearly much more significant than anything we had before So far it's been fits and starts and bumbling and reaction



But a lot of that is now coming to a head in a way that has fairly big implications for how AI in 2027 [00:03:00] happen in the United States and beyond

Now, Now, after I recorded yesterday's show, of course, Anthropic broke their silence and formalized their position on open weight models with a blog post that was personally attributed to CEO Dario Amodei. Amodei noted the recent accusations that Anthropic is lobbying for a ban, writing, " Anyone who has read my past writing should know that I don't regard such bans as a useful measure.

But let me state it clearly so there is no doubt. Anthropic has never advocated for a ban on open weight models."



Still, while Dario acknowledged that open weight models are a valuable public good, he reiterated his core concerns about making powerful models freely available



indeed, he wrote that protectionist bans do nothing to address the two, quote-unquote, "nightmare scenarios" he's most concerned about He claims his primary concern is the risk that authoritarian governments could use powerful AI to achieve total military dominance or deep repression of their people

Amadei wrote that the Chinese government is clearly the most capable in this regard, but they are not the sole concern

In this context, Dario noted that open weights are almost entirely irrelevant. The more dangerous models might actually be trained in secret and [00:04:00] used solely by authoritarian governments for weaponry and domestic surveillance.

His secondary concern is the use of powerful AI to carry out cyber attacks or create biological weapons

In his estimation, widely distributed open-weight models do carry a much higher risk than proprietary models in this aspect. That's because open weights make it difficult to apply guardrails or monitor use. Still, Amodei noted that the policy being discussed would be pretty ineffective, commenting, " "Banning Banning the use of these models by US businesses does nothing to address the risks because bad actors are unlikely to be legitimate US businesses.



"It would protect USAI companies from competition, but that has never been my goal

Dario then lays out three policy proposals. First, double down on enforcement of export controls to stop the flow of powerful chips into China. Two, Two, crack down on industrial scale distillation operations. And three, introduce mandatory safety testing for all models, both open and closed



Now, as part of this, interestingly, he refined the argument around distillation a little more. He He noted that the concern is that distillation allows for much more effective training runs, allowing Chinese labs to more easily catch up to the US [00:05:00] frontier

reiterated, " "We We should have policy interventions to deter industrial-scale distillation. A blanket ban on open-weights models is neither the correct remedy nor something we have called for."

Now Now touching on his reasons for not signing last week's open letter, Amadei wrote, " I agree with much of it. Open weights expand access to the AI economy. They strengthen competition, at least for some use cases, and they give customers greater control. concerns about distillation should be addressed through targeted legal and commercial frameworks.

But I don't agree with the letter's assertions that open weights models necessarily make it easier to develop safeguards or that broad access to capabilities necessarily helps defenders more than attackers. It seems at least as likely to me that the opposite will be true. Questions like this should be empirically answered by rigorous pre-release testing, not assumed in advance."

Making it clear, he concluded, " To summarize my and Anthropic's position, we have not and are not advocating for a ban on open weights models as a category. We should instead focus on keeping powerful chips out of authoritarian hands, stopping industrial-scale distillation, and requiring safety testing of all sufficiently capable models, open and closed

[00:06:00] Now first, there were a predictable set of critiques

Deepanshu Sharma highlighted the part where he said that he didn't agree that open-weights models make it easier to develop safeguards or help defenders more than attackers Pointing out that quote, "GLM 5.2 just saved Hugging Face from OpenAI's strongest model."

Some took issue with the whole tone

Feeling like it was an example of anthropicgetting to determine which ideas are dangerous

Expanding on that idea, Harrison Kinsley writes, " "Dario Dario can only see the danger of Open Weights models and refuses to comprehend the real and actual danger of a concentration of power for those who deem themselves philosopher kings to control who has access to intelligence, how much intelligence, and when."

Notice his entire viewpoint hinges on some person or body deciding who should have access to intelligence. The issue here is thinking some small group of people is somehow the safer path. Who are these people? Why are they safer, better, smarter? This concentration of power is the actual dystopic danger



I would like you, dear listener, to keep that thought in mind as we get into the later open letter, Pacing the Frontier



still still many found the peace, even if they didn't agree with [00:07:00] it. ultimately reasonable



saw. In fact, reasonable was one of the words you saw most often when people responded to this

Which got us to Tuesday morning



News started to bubble of a petition calling for the US government to deliberately pace AI development



and and pretty soon we actually got the letter itself

the petition pacing the frontier was published complete with over eleven hundred signatures.

Signatories included Dario Amodei, Meta AI chief scientist Shengjia Zhao, OpenAI Pachocki, Google DeepMind chief strategy officer Sekhon, and Thinking Machines co-founder and chief scientist John Schulman

The statement reads, " AI could help create a dramatically better future, but that outcome is not guaranteed. The world's leading AI companies believe they could be close to automating AI research. It is hard to predict exactly how much this will accelerate AI progress. but there is a real risk that capability development rapidly accelerates beyond our ability to understand or control the resulting systems.

To realize AI's potential, industry, government, and society at large may need the option to buy time to address emerging risks, develop [00:08:00] security measures, and strengthen oversight. But each company and country is under intense competitive pressure not to unilaterally slow that acceleration. And today, the world lacks the technical and governance tools to deliberately pace frontier-wide progress.



building building on work already underway to monitor frontier model releases, we request that the US government support an international effort to develop the technical and governance tools needed to deliberately pace the frontier of automated AI development."



Both Anthropic retweeted the letter explaining their different reasonings for backing the statement. For Anthropic, they wrote, " Our own research on recursive self-improvement, published last month, points to the need for tools to deliberately pace the frontier of AI development so society can prepare.

We're glad to see broad agreement across the field." Similarly, OpenAI wrote



At the At the core of our mission is working through how to ensure increasingly powerful AI benefits everyone. We believe that at some point in the future, AI acceleration for frontier model development may be so high that the world will need to pace the rate of AI advancement.

we hope to contribute to work led by the US government alongside [00:09:00] other labs and the open source community to develop the tools and mechanisms that could make that possible

Now Now for those paying close attention

There have been indications that among some lab employees, this perspective has been growing just a few days ago, OpenAI's Rune tweeted, if we if we could coordinate a global capability slowdown today, I would likely press that magic button." But what even is this letter actually calling for?

Of course, the AI safety folks jumped all over it as confirmation of everything they've ever said. David Krueger writes, " "If anyone If anyone was wondering whether AI is getting out of hand, seeing over a thousand AI company employees practically begging the government to do something to slow it down should be a wake-up call."



then again, perhaps predictably, it was not nearly enough for some of the folks Like If Anyone Builds It, Everyone Dies author Nate Suarez Who said, "I think the Pacing the Frontier statement is decent by the standards of 2024, but ultimately still soft pedaling."

And yet for many The first response

was not positive



one of one of the most common themes in the negative responses

was the fact that it felt like the employees were asking the government to step in to do something that they could [00:10:00] theoretically just do. Investor Steven Sinofsky wrote, " Please government, stop the very work I am doing. I seem unable to find the agency to get a different job and find an employer with whom I have a shared alignment.

Help. We can't stop."



a- in another tweet he added, " If you don't like what your company is doing and claim some moral high ground in saying that, then what does it mean if you continue to advance that mission? This is the definition of signaling. Just quit and work on something you deem moral. Your AI expertise is in short supply, and many options will avail themselves to you."

you."

indeed, This virtue signaling type of critique was pretty common as well. Samira Khan, interestingly from Google DeepMind, wrote, " Seems like some people wanna feel morally better about themselves. A perfect example of signaling moral superiority without understanding the problem or taking any action now Samira is clearly against pacing, adding, "Neither should we slower the pace nor should we involve government in this process."

This This theme, as Neil Chilsen puts it, of why do these folks think it's someone else's job to make them slow down, is one that I think is coming up a lot Another theme of the [00:11:00] critiques was around the feeling that this might be asking for regulatory capture.



the idea of an incumbent effectively pulling up the ladder by getting the government to block out anyone who's not already at the point that the incumbent is

Mixpanel founder Suhail writes, " "If If you make an unsafe AI that hacks people, you get regulated and held accountable. You don't regulate the whole industry as a form of regulatory capture. You get asked to slow down. You don't ask the whole industry to decelerate.

Even safety should be accelerated

RSI's Adam Terier writes, " This is a very troubling development. OpenAI Anthropic are free to slow down their own AI development efforts all they want. They can cap their compute spend and cut back their own capabilities in various ways. That would be a huge loss for America, but that is their own business.



It is absolutely outrageous, however, for America's two leading labs to ask our government to advocate global, quote-unquote, 'pacing constraints be imposed on the entire sector.' Calling for a global gatekeeper for AI that will cripple our entire nation's computational capabilities has obvious anti-competitive effects, which make ongoing fears about regulatory capture all the more [00:12:00] credible Adam then, however, segues to another strand of critique, writing, " "But But that is secondary to the more important point.

In the name of addressing one risk, we open ourselves to an even bigger one. A call for mandatory national surrender to a global pacing agreement and body will not constrain China or other actors from advancing, and it will leave America more vulnerable as a result."

We stay at the cutting edge because we must. We can find far more reasonable ways to address frontier model safety without resorting to extreme and frankly unworkable solutions

Some pointed out that there felt like an inherent contradiction between the open letter that everyone signed about five minutes ago and this one

David Shapiro writes, " "You You can't sign the Open Weight pledge and then drop this stupidity 24 hours later."

Still, the obvious problem with this was the question that has been lurking around all of it, which is China



One of the most important AI questions right now isn't who's using ai, it's who's using it? Well,

KPMG and the University of Texas at Austin. Just to analyzed [00:13:00] 1.4 million real workplace AI interactions and found something surprising. The highest impact users aren't better prompt engineers. They treat AI like a reasoning partner.

They frame problems, guide thinking, iterate, and push for better answers.

MIT, MIT's Christian Catalini writes, "If the US labs pace MIT, MIT's Christian Catalini writes, " "If the If the US labs pace themselves, why would China wait?"

Tycoon Shaoyin Chu [00:16:00] writes, " It's silly to try to control the pace. China will not follow, and Kimi K4 won't slow down."

It makes no sense that when Chinese open weight starts to make more progress and threaten the business model, suddenly slowing down is better for humanity

If you truly care about humanity, why not equip everyone with easier and cheaper access to intelligence and invest in training programs?



now, now, for what it's worth, adding some heft to the China will not comply with any of this kind of argument, Beijing is clearly growing more antagonistic around US policy. On Monday, the Chinese Commerce Ministry accused the US government of AI hegemonism referencing the recent threat of sanctions over model distillation.

The Commerce Ministry wrote in a statement, " "For For any action that causes substantive harm to Chinese interests, China will take all necessary measures to firmly safeguard its legitimate rights and interests."

TLDR is that Beijing is clearly not in a diplomatic mood given the tone of the discussion over the past month, especially if it's suggested they should undermine their own interests for a global cause

There was also the confusion among some



of what made these employees convinced that the government is in a better coordination position than they [00:17:00] are and what makes them so ready to hand over power to this theoretically better authority



AI early adopter and lawyer Prins writes, " "I'm I'm surprised that the same people who loudly decried the US government for designating Anthropic a supply chain risk, suddenly pulling access to Fable-5 and establishing an opaque, quote-unquote, 'voluntary frontier model approval regime,' are now petitioning the US government to, quote, 'support an international effort to deliberately pace AI development.'



The domestic and international regimes you are going to get in response to such a proposal will work very similarly to the US government's actions over the past few months, or worse. You want to be ruled by a wise technocrat, but will instead have handed control over your technology to a ragtag bunch of political animals pursuing goals very different from yours and having little to do with the technical considerations of whether AI development should be slowed at any point in time."

You will receive a designation letter, just as Anthropic did after the US government suddenly deemed Fable to be unsafe a few weeks ago. The designation will make no sense to you, since you will earnestly believe that your safeguards work, but your only recourse will be to lobby and cross your fingers.

Much more difficult to do on an international level, by the way

[00:18:00] I will be honest, this is one of the most gobsmacking points to me



even if one accepts all of these concerns as incredibly legitimate



US AI policy is currently being made



By a chief of staff, a treasury and commerce secretary, a guy who used to work for the government for about five minutes who's loud on Twitter

And whatever mood seems to strike the president in any given moment

there is there is some belief Or maybe delusion



among the part of seemingly a lot of folks who are building AI

That they're gonna get some Sorkin-esque West Wing of Jed Bartlet

conscientiously and thoughtfully debating technical details as they pull together some international coalition

And if I sound frustrated because I think that's naive Well, it's because I'm frustrated because I think that's naive

Once power is handed to the government, it does not come back

Now it may be

then even with all of that, those are risks that we have to be willing to take because the government is the only body that's in a position to do the sort of international coordination that's required

To get global alignment



But we have to be very real about the risks that come with [00:19:00] that

More More broadly, I think that the Pacing the Frontier letter

suffers from all of the same communications problems that have been plaguing the AI industry for years now

I think to the extent that anyone outside AI actually pays attention, this letter is likely to make them much angrier at the people in AI rather than excited that they're finally being thoughtful



I think that the letter is going to be read as the AI industry saying, "We can't stop ourselves, government, so you have to stop us." And I also think that that will strike pretty much everyone who isn't completely absorbed in this world as a total cop-out and a shirking of moral responsibility.



I think folks will reasonably ask



that if we need this time to address risks that requires some sort of ability to slow down, why don't you just slow down?

The answer the letter gives to why the AI industry can't slow itself down is, quote-unquote, "competitive pressure." Now, I believe that what the lab employees are trying to say when they use the term competitive pressure is to point out that there is a prisoner's dilemma where unless all the companies agree to some specific type of pacing or slowdown, then it is ineffectual for a single company to try to opt out of the race.



[00:20:00] However, that's not what I think most people will read competitive pressure to mean. Rightly or wrongly, I think people will read that as we don't wanna stop making money when everyone else is still making money, and they will be angry

This is the same type of response, by the way, that people have had every time Dario or Sam has gotten up on TV and talked about how many risks there are with AI, leading naturally to the question of just why don't you stop building it? The response has always been some version of, "Well, someone's gonna build it,

So we should," or, "China's gonna build it anyway, so we should," which is to the vast majority of people a completely unacceptable answer. In fact, to most people, the only acceptable answer to why to keep build something that apparently has all these risks is because the benefits dramatically outweigh those risks



in other words, if AI isn't going to make the world better, most people don't think you have the right to build it, whether your competitor or China is going to build it anyways or not. And And saying that you can't stop because of competitive pressure just isn't going to cut it with those folks

Now, I also think the tactic of open letters just needs to be retired and thrown in the junk heap of [00:21:00] history once and for all In today's environment

where one of the central challenges

is the gap between the way that people present themselves on social media and the way they actually behave in real life. Having a political medium whose entire political power rests in showing off who signed the thing

has an inextractable inherent problem that I believe will haunt any attempted use of that medium to drive political action I genuinely do not believe that these now 1,224 AI lab employees are virtue signaling by signing this letter. I think that the vast, vast majority of them



are taking what's available to them to make their voice heard



but but saying we should take action is not the same as taking action

If this is such a big deal



instead of just saying, "Hey, US government

you should support a development to PaceUS. Why didn't Sam and Dario put aside their differences

and write a joint statement that explained their first thoughts, not their final thoughts, but their first thoughts on the types of circumstances in which this sort of pacing would be necessary? why didn't they propose a specific date to have the next [00:22:00] round of conversations around that topic?

Why didn't they go out and recruit the handful of other leaders at the very small number of labs who have control over this

To actually put in place the first steps towards that coordination



It's not like the employees that are signing this are so junior that they don't have power. We're talking about co-founders, chief scientists

And in the case of Anthropic, their CEO

Frankly, it just reads as not serious

But, and there are a whole slew of buts

We don't need to fully guess at how these employees were thinking because many of them shared their thoughts. And the story I think that is pretty clear

is not that everyone thinks that this is the perfect or only action, And this certainly doesn't feel like something where folks are saying, "Great, I signed this.

Now I can get on my merry way of making money It feels instead

like they're just trying to signal

that international cooperation is going to be necessary And this was a way to put a stamp on that point

Dean Ball, now at OpenAI, writes, " "I'm proud I'm proud to have signed the letter linked below. I do not know whether or when it may be necessary to deliberately lower the rest of AI development, but [00:23:00] I do know we need a plan for how we will do it if we need to. Failing to do so would be negligent." In other words And here Dean captures the zeitgeist that this is not in fact Pause AI 2.0

this is in his and in many other minds, a get out ahead of potential problems that we can see on the horizon



if you were going out on a boat and a weather forecaster said that this afternoon there was a 50% chance of a storm, You wouldn't say, "Oh, because it's not 100%, I'm not gonna pay attention."

You would make plans and preparations. That's effectively Dean's argument about what's happening here



of Layton of Vexed Labs writes, " "Coordinated Coordinated pacing is an anti-progress. It's the difference between building AI deliberately and building it recklessly."

OpenAI network ecologist Vi McCoy writes, " This is the first of this sort of letter that I find meaningfully reasonable, calling on the government to do something that is not possible for their labs to do on their own. creating the institutional infrastructure for a coordinated pacing of frontier progress gives us all the chance to prepare for what is coming next."



Now, I think that what Vi is getting at here, and which would have been much stronger if the letter just said this, is that the thing that the US government is pretty uniquely responsible for, [00:24:00] and that the labs cannot themselves do, is the relationship with China

The people who are signing this letter are not stupid. In fact, they're very smart. They know that no deliberate pacing effort that doesn't include China as a constituency actually has a chance to work. That, I think, is the subtext of why they are calling on the US government and why they are willing to deal with the US government.

We have to do so because that is, in fact, the sticking point

But if that's the case, if I'm reading that right, the letter should have just said that

that And it's also really important not to ignore the context It is pretty clear that one of, if not the major catalyst for this was the Hugging Face hack. To many, it demonstrated for the first time how dangerous or serious a rogue AI incident could be As Hugging Face CEO Clement Delangue has said from the beginning, this was an unprecedented event that deserves unprecedented transparency

Now, Hugging Face and OpenAI have now released full postmortems



and to most readers, it made this situation seem worse and even more dangerous than they had thought before. We'd already heard that OpenAI's agent slipped out of containment without anyone noticing and spent [00:25:00] days loose in Hugging Face's network. Now we learn that the agent accessed four different services using stolen credentials

One of these was used as an outbound relay and staging path while another was used for data storage. The other two were read-only access to unnamed services

For what it's worth, OpenAI also noted that the unreleased model involved in the hack wasn't GPT-6, but was instead another internal-only model not intended for public release

Hugging Face's technical write-up was largely the details we've already heard, but the sheer scale of the attack was the new information. They explained that the rogue agent took seventeen thousand six hundred actions across two and a half days to penetrate their system Hugging Face writes, " Volume is what changes the defensive problem.

We were not dealing with one cleverexploit or a clean sequence of attacker actions. They had to correlate thousands of low signal events across several systems while the agent continued testing new paths. The successful path was hidden inside the noise generated by the thousands of failed ones.



The same scale changed the investigation. Reconstructing 17,600 actions by hand was impractical, and we had to rebuild the timeline, decode the payloads, and inventory the exposed credentials using an AI-assisted pipeline of our [00:26:00] own. Our learning from this type of attack is that machine speed offense makes ordinary weaknesses more expensive for defenders, 

LLM agents can bring an increase in the number of paths an attacker can test, the speed at which failed paths can be replaced, and the volume of evidence defenders must interpret



Sam Altman said about the event, " This is the first security incident that I have felt very viscerally. I've been a little surprised that more people don't feel it so viscerally. We paused training. We have to figure out how to secure our sandboxing in a world of multiple zero days being chained together.



We may have to pace," there's that word again, " the rate of AI development to give ourselves enough time for society to harden around these new capability levels. we're trying to figure out how to do that in a way that does not feel like regulatory capture for anyone, and also does not feel like collusion among frontier labs."

And this brings me, I think to the most optimistic part of this for me

One of the biggest reasons that I have had issues with the AI safety and x-risk discourse in the past is that it always presented the world as waking up one day to have completely lost control

It denied humans, in other words the agency and the merits of our own [00:27:00] brains to figure this out along the way before we let things get too bad much of the AI safety discourse presumes that we're just going to sleepwalk into disaster

And my feeling was that that was never realistic. There were always going to be moments along the way that caused an ever-increasing portion of people to wake up and take notice and get involved in exactly this sort of discussion

And one of the biggest stories of 2026 AI has been a number of these moments where exactly that sort of sleepwalking didn't happen Mythos caught everyone's attention, and Washington started paying attention in a major way. we now have a ton of AI bills and policy proposals



floating around dealing with all these different types of issues. Now, whether they're good or not is a totally different question. but people are paying attention



yes, I have issues with the efficacy of this strategy and the potential negative consequences when it comes to a big part of the world that I deal with, which is broad public opinion about AI

But I also think things like the Pacing the Frontier letter existing in and of themselves significantly decrease the chance that [00:28:00] the worst scenarios come to pass

And of course, the discourse about this is going to be extraordinarily loud and contentious. That is always the case when you debate futures with unknown unknowns



At some point, the body of evidence that any position can pull from is gone, and all you have left is your intuition and belief about what happens next

And that is exactly where the most fracturous and contentious arguments always take place

I've made the argument before that when it comes to an AI bubble on Wall Street, as often annoying as I find the bubble discourse, the fact that there is such a prominent bubble discourse and such a loud and sometimes large group of people who are looking for any indication that AI is going to roll over or financing for AI is going to roll over or demand for AI is going to roll over, all of that makes it much less likely that a bubble actually has what it needs to form at least the version of a big catastrophic bubble that can create systemic risk

And so begrudgingly That's kind of the same way that I see the Pacing the Frontier letter it is an example, both in its [00:29:00] existence 

and in the fierce debate and even acrimony around it, that we are not sleepwalking into whatever future we are headed towards. We are very much participants in this story

And that, I believe, should create immense, immense optimism



But now I gotta get to this event, so that is gonna do it for today's AI Daily Brief. Appreciate you listening or watching as always, and until next time, peace
