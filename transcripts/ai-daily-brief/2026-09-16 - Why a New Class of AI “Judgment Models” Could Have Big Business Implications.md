# Why a New Class of AI “Judgment Models” Could Have Big Business Implications — Transcript (2026-09-16)

https://aidailybrief.ai/e/2026-09-16 · Listen: https://pod.link/1680633614

<!-- metadata -->
Format: news-analysis · Level: 1 · Length: ~00:25:00
Host: Nathaniel Whittemore
Categories: models, safety-security, agents, model-strategy
Featured: Jev
Also mentioned: ChatGPT
<!-- /metadata -->

---

[00:00:00] 

It's not every day that we get a new model to play around with, and it's certainly not every day that we get an entirely new approach to model building with some fairly different implications for how we even use it



Today though, we are talking about a new class of models which you might refer to as AI judgment models 

rather than producing long strings of text, these judgment models, like the one we're discussing today, Jev from TypeSafe produce probabilities around specific questions. Is this customer angry?

Is there a new dependency in this email?

Do we need to change the operational plan because of this?

Today we're exploring the idea behind these models, how they're trained differently

how they can produce these judgments much more quickly and much less expensively, and most importantly, where they're going to fit in your overall model stack

Daily Brief The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI. All right, friends, quick announcements before we dive in. First All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, Blitzy, Section, and Hyperagent. [00:01:00] To get an ad-free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts.

Subscriptions are just $3 a month for ad-free. And if you wanna learn about sponsoring the show, send us a note at sponsors@aidailybrief.ai, or just go to aidailybrief.ai where you can learn all about it. 

Welcome back to the AI Daily The AI safety discourse continues to trickle out through the tech industry as well as mainstream society



but but for now, unless something absolutely seismic happens, we're gonna move it into the headlines and away from the main episode. With that in mind, after staying quiet over the weekend, Mark Zuckerberg has made his thoughts known on this idea of an AI slowdown On Tuesday, Zuckerberg wrote in a post on X, " Every lab has the responsibility and incentive to move at the pace required to train its models safely and the ability to take its own actions to ensure that happens."

Basically, his view is that pacing is the responsibility of individual labs rather than a collective action. and that view hinges on two core ideas. First, that, quote, " People don't want to [00:02:00] use agents that are misaligned with them and that don't do what they ask, so labs have a strong natural incentive to make their models more aligned."

And two, labs face significant liability if their models cause harm, so they have a strong incentive to prevent this as well. Emphasizing the point, Zuckerberg said that Meta had delayed the release of Muse by several months to work on safety.



He continued, " We didn't call for everyone else to do this before we would. We just did it as part of our day-to-day work because it was clearly the right thing for people and for us." Essentially, Essentially, Zuckerberg is saying that the individual incentives and consequences that are already in place are enough to force AI labs to work on alignment and to pace the frontier correctly, rather than needing some exogenous government-enforced slowdown. Now, Zuckerberg did support the idea of independent evaluators and advisors as a matter of best practice rather than regulation.

He claimed that Meta has already engaged outside evaluators, not because it's required of them, but because it helps produce better work

Finally, he concluded, " Committing the significant majority of compute towards serving people rather than [00:03:00] racing towards recursive self-improvement is one of the best ways to ensure that we develop this technology safely. Meta has made this commitment, and other labs can do this as well. I believe the key to building a positive future for everyone is maintaining the right balance of power.

This is within our power to do

It's carefully worded, but basically this whole thing says, "Come on, guys, let's please stop with the theatrics."



and and a lot of people frankly found this a breath of fresh air. YouTuber Joseph Carlson wrote, " Hold up a minute. You are telling me companies can slow down, make sure things are safe without telling all their competitors to slow down?"



and and I would say that broadly speaking, reactions fell into one of two categories. The first was like that one and like this from Matthew Berman: " Love this. Model safety and alignment is a feature and economically incentivized."

Or Bill Ackman, who simply called this the proper approach to AI development. But then on the other side were those

Arguing effectively that Zuckerberg just does not have the trust or standing to make this argument, regardless of the merits of the argument itself. Hard Fork's Kevin Roose wrote, " Whether you're a Democrat or a Republican, an EA [00:04:00] or an EACC, I think we can all agree that the person best suited to protect us against the harms of powerful new technology is Mark Zuckerberg

Now meanwhile, over in Strange Bedfellows Daily, Bernie Sanders and Steve Bannon have joined forces to call for human-centric AI regulations in the strangest alliance of this political cycle. The two highly ideological leaders spoke from the same stage on Tuesday at the Future of Life Institute's Pro-Human Assembly in Washington

Sanders told the crowd, " If the lives of every man, woman, and child are going to be fundamentally changed by this technology, then the people of this country must make decisions about AI and not just a handful of oligarchs

Bannon had very similar remarks stating, " The American citizens are not going to be supplicants to the oligarchs anymore. We can't do it. This is a hinge in history. We have to handle this correctly. To handle it correctly, number one, we can never trust what an oligarch says."

Now, I will note that while this seems strange at first, these two highly ideologically opposed people sharing the same stage

the broader movements they connect to [00:05:00] have a fair bit of shared context and history

The 2016 presidential election



in which Bernie was narrowly beaten by Hillary to miss out on becoming the Democrat nominee, and in which Bannon obviously architected the first Trump administration Both had their roots in populist anger

at the post-GFC financial landscape and the lack of accountability for the institutions and institutional leaders who were involved in creating that particular economic crisis Obviously, the left and the right's reaction to that particular context were different



but it is, I would contend perhaps less surprising than you think, that at some point these two would find common ground



and to be clear, I am not dismissing the common ground that they find just on the merits of this particular issue itself, and and the power of this particular issue to scramble existing political alliances

I'm just making the point that their stories are actually more intertwined than you might think at first glance. In any case, the event seemed somewhat less about the existential risks of AI that have filled the headlines this week and more about the class struggle the technology has come to represent.

TV screens played a parody interview from a fictional AI described as someone who loves people but isn't crazy [00:06:00] about humans. Throughout the event, it seemed that AI itself wasn't the risk that needs addressing, but rather the unchecked power of oligarchs



now now you might remember that back in August, journalist Jasmine Sun toured the country speaking to real people who were working in opposition to data centers, and found that the most common complaint was not about electricity, water use, or noise pollution, but a lack of control and the

sense that the future was being forced upon their communities with little input

The same was true about this event. Across multiple speakers, the risk of AI was not framed around cybersecurity, bioterrorism, or other x-risks It was about a lack of agency in determining the shape of the future

From this followed their main concern which was simply the idea of losing control of AI. As Texas Democrat Greg Casar, who is sponsoring Bernie Sanders' superintelligence bill said, " The answer is simple. We ban AI systems that are too powerful for humans to control."

And And as strange as it might seem

despite all the intensity of this rhetoric recently, I still contend that we've moved into a new phase that's all about negotiating the relationship where citizens and [00:07:00] governments have a stake in this



and we're given that that is now pretty much where everyone is

The next phase is likely to include a lot more specificity and dare I say nuance



Glenn Beck, for example, had a long monologue on his show about how he can both have signed the Pro-Human AI alongside them, but also disagree with them on specifics of data centers And honestly, as crazy as it sounds, I think that the more that the political discourse kind of frags your brain for how confusing and all over the place it is

That might just be a sign that we're actually making progress



the conversation also found its way into Salesforce's annual Dreamforce event where the company unveiled a new AM- a new AI model, but where a lot of the chatter on social media focused on appearances 

from Sam Altman, Jensen Huang, and Dario Amodei, who each iterated their own safety views



Dario argued that he was just trying to put forward a set of standards that the industry could organize around. while while Altman said that he was very confident in our company's ability and our industry's ability to do this safely



Jensen Huang meanwhile reiterated the Zuckerbergian view saying, "Run as fast as you can, but if you feel at any given point in time the company's out of [00:08:00] control or the product's not going to be safe, take a pause and make sure you get it right

And as for Salesforce CEO Marc Benioff, he believes that every company has a responsibility to uphold ethical standards. Still, to give the safety debate a bit of a rest, Salesforce also had two big practical AI announcements. First, they're releasing their first in-house model in quite some time.

Called Qoa, the model is a fine tune of NVIDIA's and is designed to handle sales management within the CRM

The announcement reinforces the role that open source has to play in the enterprise by enabling this sort of narrow vertical model. Secondly, Salesforce unveiled a new initiative called AI Force. This will be the umbrella term for Salesforce's connectors that will allow third-party agents to access Salesforce data.

The release reinforces Salesforce's commitment to moving towards headless software in a platform-agnostic way, allowing any agent to become the interface



now now obviously these are big conversations that are important and are going to continue, but for now, that is where we will close the headlines.

On today's main episode, we are looking at something [00:12:00] really different and quite rare, which is, in short, a totally different approach to AI that is not just another LLM



Now, in the nearly four years since ChatGPT was released and the three and a half that this show has been around



the vast majority of the things that we and the rest of the industry have focused on have been in some ways related to large language models

And yet, as some have pointed out



although often in a way that didn't get much traction and was more or less screaming into the void. LLMs are not in fact the totality of artificial intelligence

Yesterday



Almeida posted on X, " After co-inventing ChatGPT, I kept asking myself, why have superhuman chat models not led to AGI? I've spent the last two years in stealth building a new way to train models, RLCD

or reinforcement learning for calibrated decisions, and a new type of Frontier AI model that we are releasing today, Jev. Jev is twenty to two hundred times faster, forty to four hundred times cheaper with output tokens free. Frontier [00:13:00] composable intelligence optimized for decisions. As far as I can tell, the shortest path to AI-based economic revolution



for-- Now one could absolutely be forgiven For seeing numbers like 20 to 200 times faster and 40 to 400 times cheaper And being a bit skeptical of the claims to say the least

And were this just another LLM

that skepticism would be entirely warranted. however, with JEV and this new strategy



We're dealing with something that is quite different



The company behind Dev is called Typesafe, and in the announcement blog post, they talk a little bit more about what makes their approach different. They write, " We built a new stack entirely focused on automation with a new model architecture, parallel sampler for maximum efficiency, and training method we call reinforcement learning for calibrated decisions

Whereas existing LLMs optimize for human preference, i.e., write-ups and chat responses that human raters prefer

The new System 1 models, the first of which is Jev optimize for calibrated decisions or answers with epistemically honest probabilities

So what does that [00:14:00] actually mean? Well, let's look at how Mike Taylor from Every describes it. He writes, " Think of it as a smart if-then statement that determines what happens next when you're automating a workflow. Say you're building software that prioritizes customer service requests, and you write code that asks the model, ' Does this customer sound angry?'

JEV might answer zero point nine, which means there's an estimated ninety percent probability that the answer is yes based on what the model learned in training. You could also provide categories you define like annoyed, irritated, offended, furious, and enraged, and learn that the customer was sixty percent likely to be classified as furious with only a ten percent probability of being enraged."

Going on to explain why this matters and how it differs than LLMs

Mike continues, " With an answer of zero point nine, very likely to be angry, the software might automatically proceed to escalate the customer concern to a manager. Or if it answers zero point one, not likely to be angry, that request might be deprioritized. However, chatbots are trained to respond with flowery [00:15:00] text like, 'You're absolutely right.

This customer does sound very angry. Would you like me to compose a draft email response in a friendly, supportive tone?' This text response would cause the program you're building to crash because it was expecting a number between zero and one, not an essay."

Teal fellow Michael Lee says this allows a class of decision-making that was neither suited to dumb, unintelligent code nor to slow, expensive LLMs

As Chubby sums up, Jev is an AI model built for decisions rather than text generation. And it is important to note that the trade-off here is that this model does not generate text

It is not, in other words, a replacement for LLMs in general. It's a replacement for a certain category of work that LLMs do where they've been very square peg mashed into a round hole to do it. The idea, continues Chubby, is to embed fast, cheap AI decisions into software

So what is this model actually built for? Well, think of how much of office work consists of reading something and deciding what should happen next. Does this message need a [00:16:00] response? Which department should handle it? Does this document answer the question? Is this customer describing a bug or asking for a feature?

does this draft make a claim its source doesn't support? Is the situation routine enough to automate or should someone review it? These are judgments about meaning, and they're often difficult to express as fixed rules Jev then is designed to take the relevant information and answer narrowly defined questions with probabilities, categories, or scores.

The surrounding software then uses those answers to route, rank, flag, or proceed

In the type-safe documentation, they explicitly recommend breaking complex decisions into small questions and then combining their results in code



So where would this show up in normal business?

One obvious area is customer support

Where the small judgment the model could make would be something like, " Is the customer frustrated, and have previous replies failed to address it?" With those small judgments in hand, the software could then next route the ticket, raise its priority, or request human review

In the sales domain? The model could judge, is this a buying inquiry? Does the [00:17:00] prospect fit the product? Are they requesting a meeting? The software could then take those judgments to sort inbound leads and assign follow-up



in marketing and editorial. The model might judge whether the copy meets specific style rules, or whether the offer is clear

The software that surrounds it could then flag passages for revision before publication

And importantly, where a lot of people went was not just understanding where they would use this instead of LLMs, but how they might use it alongside LLMs

YC founder Nathan Fleury wrote, " "I'd I'd imagine a lot of workflows that look like LLM proposes options, Jev decides, code executes."

To To put a clear example on this, imagine that a customer writes, "This is the third time I've contacted you. We still can't export our reports, and our renewal is next week." A support workflow supported by something like Jev could ask several questions together.

One, is the customer describing a product problem? Two, does the message indicate repeated unsuccessful support? Three, is a commercially significant deadline approaching? Four, which team is best equipped to [00:18:00] help?

So the software that surrounds it could then combine those signals with actual account information, such as the renewal date, and escalate the ticket. From there, you would still have a generative model draft a reply, but Jev, once again, could check the draft against narrow criteria.

Does the response acknowledge the repeated contacts? Does it address the export problem? Does it promise something unsupported by the information provided?



and part of what people are excited about opening up with this new approach is that cheap judgment makes frequent checking more practical

If a check adds a noticeable delay or expense, a team may run it only on selected cases or at the end of a task. If it becomes sufficiently fast and inexpensive, it could run on every incoming request after each draft revision across many candidate documents before an agent takes a consequential step

Back in Mike Taylor's article from Every, he gave Jev the text from all 27 of his articles alongside 10 deliberately AI-styled counterpoints, then asked the same 21 questions [00:19:00] concurrently across all articles to check for AI tells. Basically, the check that he was doing with Jev Was does this essay do specific things that indicate to people that it is AI composed?

Things like, does the text repeat an idea without adding evidence? Does it force a symmetrical both sides argument? Does it overexplain a straightforward point? In less than 0.7 seconds, Mike said

Jev quote unquote read all 37 documents and answered all 21 questions for each, returning 777 judgments for an estimated quarter of a cent. As he points out, that's fast and cheap enough to AI check everything everyone at your company has ever written and get the results back in an instant.

A comparison that Mike makes is a code linter for knowledge work. He writes, " "In In software development, a code linter is a tool that analyzes your work and almost instantly flags syntax errors, catches bugs, spots bad patterns, and enforces stylistic consistency. TypeSafe's model is so fast at turning fuzzy tasks into clear, structured answers that it could act as a kind of code linter for knowledge [00:20:00] work.

Give Codex or Claude access to JEV and a list of questions, and it can quickly check its own work for problems you've told it to avoid

Parengrat says, " Most software is ultimately a giant tree of if this, do that, if this, route here, if this, escalate, if this, reject, if this, ask a human. Jev is basically asking, what if those if statements could understand messy human context?' That's a much more interesting framing than another AI model.



I can see this being very useful for fraud and risk, support routing, moderation, PR and QA automation, lead scoring, compliance, workflow orchestration and agent routing Early tech, obviously, he says, but the category itself makes a lot of sense

Now interestingly, Matt Stockton points out that in some ways companies adopting this amounts to A post-LLM AI technology making pre-LLM machine learning techniques a little bit more accessible As he writes, " "Lots Lots and lots of problems in business are classification or regression problems.

Lots and lots of companies don't know that the types of problems they have are solvable by [00:21:00] classic machine learning methods. They often solve them with people and process instead of technology. With the emergence and popularity of LLMs, more companies are thinking, ' Maybe we can use AI for that,' and are solving classification and regression problems with LLMs.

This is good in some ways because companies are potentially automating some manual work, but also bad in some ways because it's often the wrong tool for the job and possibly not as good as classic ML methods for what they are trying to do."

But he points out the classical techniques require you to label your data, train a model, and host that model somewhere. They aren't as easy to use compared to calling an LLM API, and it requires you and your org to be aware of those techniques and capable of investing in them



without going too far on the analogy, he basically says one way to look at Jev is as a UX for using LLM style user interaction patterns for classical ML techniques



Now, one interesting question that comes up is whether this is for individuals or teams building systems

And the short answer is that while it is absolutely both, it also puts a fine point on the multiplayer AI themes that we've been talking about recently. Certainly, individuals could use this sort of capability [00:22:00] to have personal tools that sort an inbox against their own priorities, check drafts of their writing against an editorial rubric, rank saved articles against research interests, or flag commitments in meeting transcripts, things like that, that are going to personally help you do your work better



but I think that where this sort of technique is going to really shine is in the domain of teamwork that happens through small judgments about who needs to know, who should act, and whose approval is required

When an agent is serving a single person It gets pretty far simply by learning that person's preferences. An agent operating across a team, however, needs to understand the relationships between people's work. That creates a different set of questions. Who owns this? Whose work does this affect? Is someone waiting on this decision?

Does this promise create an obligation for another team? Can the current owner decide, or does this need broader agreement?

In some ways, the interesting unit of work becomes the handoff

Consider a salesperson telling a customer, " We should be able to support that integration before your renewal." For the salesperson's personal agent, the next steps might be straightforward: update the account record, draft a [00:23:00] follow-up, and create a reminder. But inside the organization, That sentence implicates several responsibilities For the sales folks that sentence means for them a potential way to secure the renewal, i.e.

supporting that integration. For engineering, that sentence means a possible delivery commitment involving uncertain work. For product, it means a potential change to roadmap priorities. And for customer success, it's an expectation they may have to manage

A multiplayer agent would need to recognize the sentence as a possible cross-team commitment, And a judgment model could assess specific questions. does this message imply a delivery promise? Does the promise concern work outside the speaker's authority?

Does it conflict with the supplied roadmap? Is there evidence that the responsible team agreed? The larger system could then create a proposed commitment, identify the necessary owners, and request the missing decisions

Now again, to reinforce costs and benefits the big cost of JEV and this type of judgment model in general, to the extent that this becomes a category, is that it is an incomplete category by definition. It cannot do all the work that we currently have [00:24:00] generative AIs do.

Judgment models are going to have to be part of a more complex model architecture, the type of model stack that we've been discussing for the last several months

The benefit, of course, though, is that it can do this extraordinarily inexpensively

And because this sort of judgment intelligence can be applied so cheaply, it means that done well, it can be integrated incredibly deeply into the automated systems we're all building

This is obviously just the first day of a very new concept, and a concept which is significant enough that thisvery competent team has spent two years working on



So obviously we're going to need to see how it all plays out in practice But it does have the feel when you dig in



of something both important and obvious The type of thing that once it exists, we will be surprised in the future that we didn't have it for so long. Certainly, I'm gonna be keeping an eye on this, and I will continue to look out for more examples of how people are using it, as well as where companies are running into challenges as they try to build these new types of systems.

For now, though, very cool stuff to go check out, and that's gonna do it for today's AI Daily Brief.

Appreciate you [00:25:00] listening or watching as always, and until next time, peace 

​
