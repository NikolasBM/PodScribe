# 9 AI Techniques You Probably Haven't Tried — Transcript (2026-08-20)

https://aidailybrief.ai/e/2026-08-20 · Listen: https://pod.link/1680633614

---

260820 COLD_EDIT: [00:00:00] What if I told you you were using AI all wrong?

Nathaniel Whittemore: Well, 

260820 COLD_EDIT: then I'd be lying, and I'd clearly be trying to get you to click on something by using an absolutely ridiculous and preposterous hook. But instead, what if I told you that there were nine AI techniques that were delivering some really awesome results to some people that you might not have had the time to try just yet?

that would be a lot more true because over the last couple of months, we've seen a slew of new features and new tools become available like Claude/Design and Codex's live voice mode And GrokBot's ability for a user to train it on an entire workflow by watching the screen

One of the things that makes AI so exciting is also the thing that makes it the most challenging, that it's changing all of the time

But today's episode is gonna get you up to speed in no time at all

The AI Daily Brief is the daily podcast and video about the most important news and discussions in AI. All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, [00:01:00] KPMG, Blitzy, Harbor, and Hyperagent

260820 IN_EDIT: To get an ad-free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts. To learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai. And while you're on aidailybrief.ai, you can check out the link to next week's free webinar about agentic loops for knowledge workers.

If you have heard me or others talk about loops as basically the second coming but aren't exactly sure how to apply them to your work, this free webinar is for you. I will be there. Nufar Gaspar will be leading most of it. You can register for free, and even if you can't make it, we will send you the recording after.

Again, all that information is at aidailybrief.ai. 

260820 hed_EDIT: Welcome back to the AI Well, my goodness, friends, the AI hype train is a-hypin'



260820 hed_EDIT: but what is AI's real role in this story?



260820 hed_EDIT: Recently, there was a whole discussion bet-CEO Dario Amodei and some of his critics about the tone of his messaging. One of Dario's responses to the critique that he had been overly negative was basically to say that it wasn't going to be marketing that [00:02:00] changed people's opinions about AI, it was going to be AI actually delivering results Specifically, he posted, " "I I don't think that a glitzy marketing campaign with a positive spin is the way to win back trust.

At this point, saying that AI will cure cancer is more a cliché than it is inspiring, and most people think it is deceptive. The thing that will work is actually curing cancer." Which is why there were a lot of folks basically saying that that's what had happened yesterday.

On On Wednesday, Moderna and Merck announced a successful stage three trial for a personalized cancer vaccine, the first late stage trial that's shown promise. The treatment functions very differently to chemotherapy-based approaches. Instead of blasting the cancer with radiation, the new method involves analyzing the cancerous cells, identifying the DNA mutation causing the cancer, and creating a personalized mRNA vaccine that can correct the mutation.

The trial found the treatment was successful in more than 1,100 patients with advanced melanoma by extending their time in remission. Moderna and Merck have similar trials underway for lung cancer, and scientists hope the [00:03:00] treatment can be applied to many different cancers

Nathaniel Whittemore: Dr. 

260820 hed_EDIT: Ryan Sullivan, director of the Center for Melanoma at Mass General said, " " It's a big deal for the field in general. With this positive study, there is a hope and likely investment to follow that these approaches may change the way we treat cancer more broadly."

This gave rise to a lot of very excited posts from the AI community, like this one from Chubby. " This is freaking huge," they wrote. " " For the first time, an AI-assisted personalized mRNA cancer treatment has succeeded in a phase III trial." Moderna and Merck sequence each patient's tumor and compare it to their healthy DNA.

AI then helps identify which of the tumor's mutations are most likely to trigger an immune response

Absolutely incredible. Daria was right. Cancer will be cured in just a few years



260820 hed_EDIT: some of course took issue with the labeling of this as AI. Antibody 42 summed up the criticism saying, " " This is so dumb. They're using AI in place of machine learning because the distinction doesn't matter to people who don't care about reality. AI for mRNA design has been around for a while.

It's not an LLM."



260820 hed_EDIT: and and holding aside semantics, [00:04:00] it is important to note that this is not scientists just plugging a bunch of results into ChatGPT and asking it to come up with a personalized cancer cure. I.e., cure cancer, make no mistakes

These are advanced machine learning methods that have more similarities to the technology underpinning AlphaFold

It's also frankly important not to lose the brilliant human scientists that are working with machine learning techniques to come up with these new treatments by simply attributing the breakthrough to AI



260820 hed_EDIT: that that said, I do also think it would be dismissive to say that this is just the AI hype train. Although it's still early days, this has genuine potential to be a major step towards curing cancer. And while it isn't directly related to LLMs and chatbots, this technology has still benefited greatly from all of the investment into compute, research, and talent over recent years.



260820 hed_EDIT: the the AI era, LLMs or not, is setting the stage for some truly remarkable breakthroughs, and that is something worth celebrating Certainly the market's celebrating it Shay Belur pointed out that Moderna stock was up 70% after the announcement, rocketing up to 125% growth just a few hours later.

Said Elon Musk, " So [00:05:00] many breakthroughs are coming."

coming." next up, a next up, a topic which seems extremely pedestrian next to curing cancer, but is extremely important for lots of enterprises. OpenAI has come up with a new safety technique that will allow them to offer frontier AI without constantly monitoring their users

They're calling the process private safety processing and will be applying it to eligible API customers with zero data retention agreements. OpenAI says this will allow them to fulfill their promise of not retaining prompts or outputs after a request has been completed and ensure that sensitive corporate data is not available to OpenAI staff 

Nathaniel Whittemore: Since 

260820 hed_EDIT: the rise of long horizon agents, safety monitoring has become much more difficult.

Older system designs can only evaluate individual interactions rather than assessing the entire arc of agentic work. Anthropic's solution to this problem has been to simply disable zero data retention for Fable, gathering full data from each session to scan for harmful activity for for many enterprise customers, this is a complete non-starter and has shown up in fairly dismal adoption of Fable in the enterprise

OpenAI's new system extends automated safety scanning across an entire [00:06:00] session, including customer-controlled data storage used for context in multiple agentic steps. This scanning is still fully automated and encrypted, meaning that no human ever lays eyes on sensitive data.

If an issue is flagged, an OpenAI, employee gets a summary of the activity with a category and severity rating, but stripped of any customer data. This means that false positives will no longer cause data exposure, as well as allowing OpenAI to develop more powerful models without the need for fully transparent review



260820 hed_EDIT: a-- the TLDR is that this is a change that could help make AI in the enterprise less of atrade-off around risk and security

OpenAI's head of product policy, Alia Howze said, " We've been talking to a bunch of enterprise customers, and they really, really care about their enterprise data privacy and security. We've heard very loud and clear from businesses that this is important. They often have their own commitments that they have made to their customers."



260820 hed_EDIT: summing it up, OpenAI staff member Adam GPT added, " " This is one of those small things that is actually a huge thing." and based on my ongoing conversations with enterprises around AI as well, that is absolutely true

OpenAI also announced a new partnership

providing the model for Replit's newly [00:07:00] launched free mode Now, despite the name, free mode isn't literally free. Instead, it gives users on the $20 a month plan the ability to use Replit without spending usage credits. Free mode routes all queries through GPT 56 Luna, which Replit says will allow users to create 30 times more on their normal subscription.

When Luna isn't enough for a complex task, users can still shift to another mode to select a more powerful model. But for everyday tasks like ideating or spinning up a slide deck, many are finding Luna to be more than enough. In their launch blog post, Replit wrote, " AI models are now capable and affordable enough to make once unreachable outcomes practical."



260820 hed_EDIT: And I And I think what's interesting to me is more OpenAI's focus on marketing and promoting Five, Six Luna

As opposed to the specifics of this Replit partnership. If If you've been watching closely, it's clear that OpenAI sees themselves as competing on two very different axes at once. They are, of course, competing at the state of the art with Five, Six, Sol, and the Astra model to come.

But especially since they launched Luna It's very clear that they are also looking behind them to the Chinese open weight [00:08:00] models



260820 hed_EDIT: And are completely unwilling to surrender that ground as well

well I would I would expect that as we see more maturation among users in terms of their understanding of which power levels are required for which different types of tasks, we're gonna see a lot more of this competition on the efficiency frontier, not just the capability frontier

frontier Now Now moving off of Replit but stayingaround AI coding startups Bloomberg reported this week that SpaceX had approached coding agent startup Cognition about a potential deal. Citing anonymous sources familiar with the matter, Bloomberg wrote, " " The deal talks are not currently active, but the companies continue to hold discussions about working together, including potentially arranging for Cognition to use SpaceX's computing capacity," said the people.

Cognition most recently raised at twenty-six billion in May and is reportedly seeking a valuation of at least forty billion in a new round that's still in the early stages. importantly, the report suggests that SpaceX is looking at Cognition as an addition to Cursor rather than an alternative



260820 hed_EDIT: and certainly it's not surprising to people who have been watching closely that Elon Musk would be willing tospend around $100 billion on acquiring startups that are building the AI app layer. [00:09:00] However, shortly after the report was published, Cognition CEO Scott Wu disavowed the entire thing.

In an X post, he wrote, " " This is not true. Huge respect for the SpaceX team, but Cognition is not for sale and we haven't been talking." Bloomberg Bloomberg journalist Rebecca Torrens stood by her reporting and decried the death of media literacy, commenting, " " To be clear, according to our sources, SpaceX approached Cognition with a bid.



260820 hed_EDIT: The story does not say Cognition engaged with that attempt." later in the evening, Elon put the matter to bed saying, " " What Scott says is accurate. We haven't talked with Cognition about anything except making sure Grok works well for their needs."



260820 hed_EDIT: This This is one of those rare cases where I don't think you actually have to doubt anyone

Specifically because of the blurriness of what it even means to actually approach someone about a potential deal. If Elon and Scott were talking one afternoon about how Grok was working inside Devin

And Elon gives him a little shoulder nudge and says, "Hey, listen, man, if you ever think about where you wanna see cognition in the future..." approaching them about a potential deal?

That is genuinely how a lot of these offers start



260820 hed_EDIT: and I certainly think that Elon's [00:10:00] appetite for acquisitions has not, been sated just because the Cursor deal is done



260820 hed_EDIT: Lastly today, continued questions around the details of the administration's safety testing framework. When the framework was rolled out a couple of weeks ago, one of the big concerns for many was that the details wouldn't be made public, leaving everyone outside of the major labs in the dark. The White House unveiled the new framework in a closed-door meeting attended only by technical staff from OpenAI, Anthropic, and Google.

But it seems that even the companies invited to the meeting are still struggling to get a full picture of the new framework

Sources said that during the meeting, they were handed paper copies of the framework but were only allowed to take notes. Those sources also said that the White House still hasn't distributed written versions of the framework or shared any further details about a public AI event intended to be held this month

Now, Now, obviously this lack of clarity hasn't been a roadblock for Frontier AI development so far

Given recent decisions like OpenAI's voluntary slowdown in research as an example of the industry pacing itself

Still, there Still, there is a clear call for more transparency as this framework is rolled out

out Last week, Juan Ladano of the Libertarian Cato Institute criticized the secretive approach, [00:11:00] writing, " the White House is essentially putting the AI testing regime in a black box. This approach contravenes the rule of law, risks becoming as prescriptive as a licensing regime, and most importantly, fails to fulfill its most basic objective, to build trust in the population.



260820 hed_EDIT: a framework that raises more questions than the one it answers is worse than no framework at all."

Especially in light of all of our discussions around data centers and trust this week, I fully agree. For now, though, that is gonna do it for the AI Daily Brief headlines edition. Next up, the main episode A new study from KPMG and the University of Texas at Austin found that when people work with AI, similar skills don't guarantee similar outcomes. Researchers studied more than five hundred early career professionals and found that the best performers consistently amplified the value of AI by guiding, evaluating, and refining its outputs.

KPMG Aug_EDIT: These top performers, called AI amplifiers, weren't defined by what they knew alone, but by how they worked with [00:12:00] AI. Learn more about what separates AI amplifiers from everyone else at kpmg.com/us/aiamplifiers. Blitzy's deep code base understanding unlocks the thing every roadmap owner cares about: shipping new features. Here's the truth about building inside a massive enterprise code base. Writing code was never the bottleneck. Context is Which system does this touch? Which contracts can't break? Which standards apply? Blitzy already knows because it reverse-engineered your entire code base into a dynamic knowledge graph before feature work began. With that complete picture, Blitzy builds features end to end.

blitzy July_EDIT: Architecture, APIs, UI, and tests all validated against your existing systems

One Blitzy customer built an AI native application from scratch with 100% autonomous completion, saving over 2,700 engineering hours. Features that respect your code base instead of fighting it Stop letting your backlog grow faster than your team.

Accelerate your roadmap at blitzy.com. That's B-L-I-T-Z-Y.com 

If you listen to this show, you likely have a thesis. Maybe it's enterprise adoption, [00:13:00] maybe it's compute, maybe it's a specific lab. Harbor Capital's AI Lab Ecosystem ETFs let you express it via five actively managed ETFs, each seeking exposure to the ecosystem around one major lab: Anthropic, OpenAI, DeepMind, Meta, or SpaceX AI.

Harbor_EDIT: your view of the AI race in ETF form. Harbor Capital Advisors AI Lab Ecosystem ETF suite gives investors a way to invest in the AI ecosystem they believe is best positioned for success. Search Harbor AI Lab Ecosystems ETFs wherever you invest or follow @HarborCapital on X to learn more

Visit harborcapital.com for a prospectus containing investment objectives, risks, fees, expenses, and other important information.

Read and consider it carefully before investing. Risks include principal loss and artificial intelligence related risks. Harbor ETFs are distributed by Foresight Fund Services LLC. Harbor is not affiliated with AI Daily Brief, and the funds are not affiliated with, sponsored by, or endorsed by any AI lab This is a paid advertisement and not personalized investment advice. Investing involves risk, including possible loss of principal. 

Nathaniel Whittemore: This episode of the AI Daily Brief is brought to you by Hyperagent where you run fleets of agents your team can manage together New users [00:14:00] get 1000 in inference Forget local agents and chat workflows waiting on your laptop to be prompted Hyperagent deploys alwayson agents in the cloud doing real work across the tools your team already uses Marketing's agent turns competitor moves into landing pages sales agent enriches leads drafts emails and updates the CRM ops agent chases the paperwork and tracks the budget Every agent has access to shared context and follows your rules about scope and approvals It's time you add agents that feel like teammates Hire yours at Hyperagent built by the team at Airtable Claim your 1000 in inference at hyperagent.com/aidailybrief. 

Welcome back to the AI Daily Welcome back to the AI Daily Brief



260820 main_EDIT: today we are getting a little bit operatory



260820 main_EDIT: One One of the things that's really interesting, and I'm sure that a lot of you have felt, is that even if you consider yourself a power user of AI, or at least someone who pays attention to how AI changes, which presumably if you're listening to this show you are The ways that people interact with AI change so much that it's not hard at all to fall a little [00:15:00] bit behind in how people are actually using these tools.



260820 main_EDIT: we get settled and comfortable into the way that we've been doing things



Nathaniel Whittemore: 

260820 main_EDIT: and honestly, sometimes we get really good at working in that new way. And so to upturn that apple cart

and try new ways of working with AI is something that we don't always prioritize. 

given that we are coming towards the end of the summer and the beginning of back to school, back to work, et cetera

I wanted to share a bunch of the chatter that I've seen recently about new techniques and tricks and, features that people are using and doing that might be useful for you. you. Now, probably it is the case that some number of these are things that you are already doing



260820 main_EDIT: but maybe there's something that on your next experimental day might be the thing to try



260820 main_EDIT: Now before we get into these nine techniques, tips, tricks, et cetera



260820 main_EDIT: I I wanna provide one meta tip thatreally runs across this entire show

In this particular episode, what I'm providing youis not my experience with specific techniques necessarily But instead an aggregation of what other people are sharing about how they're learning. One of the things that makes AI so cool is that people are learning and experimenting in public

And honestly, for as cesspool-y as they can be, if you're [00:16:00] not on LinkedIn or especially X and watching the AI conversation there 

Nathaniel Whittemore: Well, 

260820 main_EDIT: I guess you're in good hands 'cause you're here. but there is a lot to learn from other people and the experiments that they're running

runningthat I want now technique number one that I want to discuss is voice mode On the one hand, voice mode is nothing new if you have ever done any of the AIDB or super intelligent training programs, you will have heard or read me haranguing you to set up something like Whisper on your computer so you can use your voice more effectively



260820 main_EDIT: But recently we've new live voice mode

And for a lot of people, it has been a complete game changer back at the end of July, Dan Shipper from Every 

shared their discussion in Slack about the feature and added, " Almost every single person at Every is freaking out about how good voice mode in ChatGPT for work is. Have not seen vibes this high in a while. If you haven't tried it yet, you should."

Allie K. Miller, who is gonna feature prominently across this show, and who is a great follow if you're not yet

has been beating this drum consistently. Right around the same time of that everypost

She separately said, " It's nearly 2:00 AM, and the only reason I finished all of my urgent work is [00:17:00] Codex voice mode. Good God, how is everyone not freaking out about this? I feel like the way I'm working looks completely different than a month ago



260820 main_EDIT: some basic examples of what I say to it, " Hey, take a look at this paragraph. What do you think? What else is on my list? I'm going to edit this while you find that doc. download my latest Instagram reel. Make a good thumbnail for it. I'm gonna go fill up my water.

Holler if you need me. just sent the 15 client emails. Check against the list while I start on the script."

Ali Ali clarifies, though, " It's less about use case and more about ambient interaction. It probably sounds like a negligible difference to speak to an ambient assistant versus click-to-speak, but it is a world of distance in practice."



260820 main_EDIT: more recently in a tweet where Ali was talking about what she thinks isn't getting enough attention in AI, she said, " Some will say Codex Live Voice Mode is an ambient chief of staff. I think that undersells It's an ambient workforce, an ambient voice-controlled operating system.

I go on walks, talk to AI, fire off multiple computer tasks, triage my day, and improve my system architecture all via natural language and yapping



260820 main_EDIT: and in yet another post she discussed how she uses this on the go or as a [00:18:00] background process during the weekend to keep things moving even as she's out enjoying her life, taking walks, hiking, et cetera

cetera now now one final entry to the Ali K. Miller Codex canon. She actually wrote and published a full setup guide on X, which I will include in the show notes

So you can go try it out for yourself



260820 main_EDIT: Now, I've been Voicepilled for a while, and what I will say is that this is the type of thing that you're not really going to get from just the descriptions. It's worth committing to some period of time where you're interacting in a new way, even if it feels weird at first, to see if and how it changes how you work and whether you like that shift

Next Next technique is teaching AI your workflows

This is something we discussed on an episode last week. But increasingly, because of advances in computer use It's getting easier than ever to get AI to do more advanced parts of your work because you can simply let it watch how you currently do things. Two Two big examples of where this has become available



260820 main_EDIT: the first is ChatGPT's computer history feature



Nathaniel Whittemore: 

260820 main_EDIT: computer history

Keeps a timeline and a review of the specific things that you do and the [00:19:00] specific ways that you work so that you can turn that into ongoing repeatable processes

This was also one of the most exciting features from the new Grokbot, which as we will see in a few minutes, people are still really just exploring how to get the most out of. One of the most obviously useful parts of Grokbot, however, is the fact that you can press a little button To teach it a task by having it specifically watching

that particular set of activities that you're doing as you're doing them

Computer history then is sort of an ambient approach to teaching a task, while GrokBot is a much more deliberative approach where you specifically tell it when to watch and how long to watch for In both cases, though, if there are complex things that previously you would have assumed that AI couldn't do because it was too hard to explain how to do it, The TLDR is that that might have changed significantly

Number Number three, create a skill to make your AI writing better



260820 main_EDIT: now when it comes to AI writing, I am not wading into the debate here about the value of writing as thinking and the importance of using writing as a way to figure out your own thoughts about something. I'm talking about the sheer [00:20:00] voluminous writing that we do that we are all very comfortable outsourcing to AI.

Emails, memos, summaries or more important areas like website copy. even though AI's writing has in many cases gotten better

There are still so many tropes that make AI's writing instantly recognizable

tiny compressed sentences of just a word or two separated by periods to sound dramatic. It's not this, it's that



260820 main_EDIT: anytime there's a quote unquote honest caveat or concern

You know the drill



260820 main_EDIT: basically, if ever you found yourself saying to an LLM, "Rewrite this without all the I think there's a slightly better way to do that



260820 main_EDIT: Ruben Haseed recently posted on X about some of the dead giveaways of using AI

A bunch of them are the ones that I just mentioned, and he also adds, for example, clapping for itself. And that matters. That's the part everyone misses, which is exactly the point

You You can genuinely 

print this post as a PDF



260820 main_EDIT: and just drop it into Claude and ask it to make it a skill so that that doesn't happen anymore. Other people are experimenting with different versions of this



Nathaniel Whittemore: like giving the AI specific style guides

260820 main_EDIT: like the [00:21:00] ASD-STE-100 Writing Standard for Plane Manuals and turning those into a skill. TLDR

Capture the things you don't want AI to do in a consolidated place, and make sure it has that in mind as it's writing every time

time Technique Technique number four is actually a new feature, which is the /design command in Claude



260820 main_EDIT: Claude-- When you're using Claude Code, 

you can now type /design and it's going to bring up this artboard that gives you a different type of interface for interacting with a design question.

You can leave it specific notes, highlight particular areas you want to change, preview different styles



260820 main_EDIT: and what's interesting about it is that in my experience, This is an improved design experience on both the macro and the micro level. On the macro level, if you don't know how you want a thing to work, having it design a bunch of templates that you can look at all at once and give pretty high level feedback on to iterate with is a really valuable approach.

But then also when you get down to the micro, being able to edit very specific parts of a design rather than having to just give a big prompt that changes the whole thing all over again is incredibly valuable. Now, Claude and ChatGPT are [00:22:00] constantly adding new commands like this, and so it's always worth keeping an eye on that.

But design is one that I've found really useful already, and I think you might too if you are a Claude user

user Now Now speaking of skills



Nathaniel Whittemore: 

260820 main_EDIT: agent skills are simply put a new discipline



260820 main_EDIT: as we give our agents more and more complex tasks, 

Nathaniel Whittemore: knowing where to insert skills, which skills to give it, where to back off and just let it work natively, all of those become really

260820 main_EDIT: important human capabilities or agent management capabilities one of the best repositories of skills that you can find, as well as resources for how to use them, comes from Matt Pocock over at his site aihero.dev, specifically aihero.dev/skills



260820 main_EDIT: he grips the skills there

based on when you would actually use them: getting started The main flow, shaping, upkeep, et cetera So as an example of a skill in the main flow he's got a skill called Grill with Docs

Nathaniel Whittemore: Docs 

260820 main_EDIT: It's a skill that interviews you about a plan or a design until you and the agent, quote, "share one understanding of it," and writes the vocabulary and the hard decisions into your repo while it does

[00:23:00] Importantly, it is not just an interview, but an interview that comes with a leave behind



260820 main_EDIT: And in each of these cases, Matt is not just explaining what the skill does, he's giving you a simple



260820 main_EDIT: copyable way to install the skill directly



260820 main_EDIT: skill hygiene, skill practice is one of those things that I think we should not view as a binary between whether we can or whether we can't But instead just an ongoing discipline that we are always trying to get better at And this is definitely an area where the best thing that you can do is stand on the shoulders of the people who have have already spent a ton of time figuring out what is and isn't working The The next AI technique that you might not have tried yet is one that I'm gonna be spending a lot more time on this fall, which some people are referring to as multiplayer AI, or which you could think about as team agents. And the idea of this is pretty simple As agents have become real this year, 

Nathaniel Whittemore: 

260820 main_EDIT: we've mostly interacted with them in single player mode.

What I mean by that is that when Open Claw came out, you got a Mac Mini. You built a personal chief of staff. You built research agents or [00:24:00] developer agents or whatever agents you built You all of a sudden were the manager of perhaps a team of agents working for you But they were working for you you I think what a lot of folks are finding is that in the context of their companies This leaves a big opportunity on the table

Work is not just a matter of everyone getting briefed and then going off and doing things on their own and then coming back together. Work is often highly collaborative, with handoffs and shared context and shared spaces where that work happens

It's nascent, but one of the things that I think is going to be a big trend moving forward is agentic tools and interaction patterns and platforms that focus on agents that live in the intersection where teams come together rather than just where individuals work on their own

own maybe maybe the best example of this so far is Claude Tag

Now, even before Claude Tag came out at the end of June, there had been an integration between Claude and Slack where you could summon your Claude instances by tagging it in. The difference with Claude Tag is that Claude [00:25:00] joins as a team member with access to the entire context of a particular channel that you're summoning it in.

The Claude instance that lives in that channel can have specific permissions, specific tool access, specific context access, and that can be different than the Claude in other channels. But that Claude that exists inside that team channel doesn't just live on one team member's computers.



260820 main_EDIT: it is a shared resource across the team Obviously not everyone has access to Claude Tag right now, But I think that this pattern of use of agents that are shared across teams is going to be one of the biggest and most important trends for AI this fall

fall Another Another example of how people are thinking of this comes from 10x, which is an AI build and implementation partner out of New York City. they recently released a post about the Citizen SDLC, as they call it, which is a six-stage life cycle that takes what non-technical employees build with AI from a personal prototype to a production that the whole company can use In other words, it's trying to take enterprise vibe coding that happens on an individual level and and make it useful across the whole company That That one you can find on their blog, which is 10X, [00:26:00] T-E-N-E-X.co, and it's promoted right near the top

top Technique Technique or feature number seven that you might not have tried yet is a bit of both a cop-out and a catch-all And that is GrokBot. Now, right now GrokBot is still a single player mode tool in that you are spinning up your own GrokBot agents for different tasks that you have.

But I don't think it's going to stay single player for long 

already the Grok bots that you spin up can interact with one another, which creates some really interesting patterns like being able to interact only with a chief of staff, which manages all the other Grok And I think that the obvious next step 

Nathaniel Whittemore: 

260820 main_EDIT: is shared interactions between Grok bots across different members of a team

Now Now it's been about a week and people are doing a ton of experimenting

with how to get the most out of it People are responding very positively to the fact that it has its own virtual computer that it can use to solve certain types of access issues that plague previous agents

go, and if you go poke around on X, there are just a boatload of use cases that people are sharing

Application reviews, sales deck updates from notes

Salesforce reports daily briefings

One common thread that I'm seeing is that [00:27:00] anywhere you interact or could be interacting with a lot of information in a regular and predictable way A Grokbot-style agent is something that might be interesting to check out

out Lenny Lenny Rachitsky from Lenny's Podcast recently gave the idea of using the MCP that has all the transcripts more than 500 of his podcasts to turn GrokBot into your own product strategy, growth, and career advisor



260820 main_EDIT: And And by the way, for those of you who are not interested in working with Groq for whatever set of reasons, let's call them Noose Research recently introduced bot mode for Hermes Desktop



260820 main_EDIT: which is very similar to GrokBot but through the open, much more controllable, much more customizable Hermes system



Nathaniel Whittemore: 

260820 main_EDIT: technique

technique number eight that you might not have tried is local AI. now it's too far beyond the scope of the show to go really deep into what using local AI actually requires. But But luckily for you, back in June, I did an entire episode about why local AI matters and how to use it with Nufar Gaspar that you can go check out. the the reason that it's worth thinking about local AI again is that there are some pretty serious advances in models that are capable of being run on local hardware.

Specifically, I'm referring to [00:28:00] Qwen 3.8 27B

Nathaniel Whittemore: 

260820 main_EDIT: which which is a local model that can run on common hardware that is scoring a 52 on the artificial analysis intelligence index

Which would have been state of the art just a few months ago

In other words, if you have been thinking about experimenting with local AI, Qwen 3.8 27B might be the right context to actually dive in ina f- lastly technique number nine



260820 main_EDIT: Is not so much a technique but a thought starter

And these are two-word prompts to try



260820 main_EDIT: again, once again, this comes from Ali Miller, who recently tweeted out 18 two-word prompts she's kind of obsessed with You have to think that some of these actually come out of her experience using voice mode as well, As they sound a lot like how you would interact with a team member. In fact, her first two-word prompt, "Now what?" Which she says is great for when you've wrapped up a project or big push and you still have energy and want AI to give you more, reminds me a lot of Jed Bartlet from "The West Wing" saying, "What's next?"



260820 main_EDIT: some of the other two-word prompts she points to are, " Please fix," u- usually accompanied with screenshot flagging an issue

Simulate it to get AI to run scenarios, plan for edge cases, and visualize what might happen [00:29:00] into a planning interface

And remember this

Where when Allie has run across a mistake or critical context error, she forces the AI to log it in its memory. she points out that while AI often does this automatically, it doesn't always, and being specific about it can help

help This This is maybe the best example of what I was saying at the beginning Where these aren't necessarily some massive change to your workflow, but just some simple little ideas to get a bit more out of the tools that you now use every day. So So there you have it, nine AI techniques you probably haven't tried, at least not all of them.

Hopefully this gives you some fun ideas for experimenting in the weeksweekend to come. For now, that is gonna do it for today's AI Daily Brief. Appreciate you listening or watching as always, and until next time, peace. 

​ 

Nathaniel Whittemore's audio recording:
