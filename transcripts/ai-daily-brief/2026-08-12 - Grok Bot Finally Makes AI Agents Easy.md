# Grok Bot Finally Makes AI Agents Easy — Transcript (2026-08-12)

https://aidailybrief.ai/e/2026-08-12 · Listen: https://pod.link/1680633614

---

260812 cold_EDIT: [00:00:00] The promise of AI agents might finally be becoming a reality. At the beginning of this year, it was clear that 2026 was going to be the year of agents. The combination of the advancement of models plus harnesses meant that around the turn of this year, It was clear that some critical inflection point had been reached, and people came into January racing to uncover all of the new capabilities that tools like Claude Code and OpenAI's Codex made available to them when the agent excitement really popped off, however, was with the introduction of OpenClaw

with Open Claw, people were able to spin up entire teams of agents, chief of staffs, researchers, writers, anything you could imagine, and have them actually coordinate and interact with one another, doing big chunks of your work and coordinated all through easy chat interfaces like Telegram The problem was, of course, that it was extremely technically complex and difficult to do so. we even dropped an entire course, Claw Camp, just to help people figure that out

and throughout the year there have been some attempts to make those sort of interfaces for [00:01:00] agentic work more straightforward for broader adoption. Yet none of them have really hit the mark. Some think that with this week's introduction of Grokbot, that has all changed

Grokbot allows users to spin up multiple agents for different tasks. You can give them access to whatever systems they need, and they go off and do work while you watch or while you're doing other things

It's one of the first products from the combined efforts of Cursor and SpaceX AI, and the companies even say that the bots will learn and get better over time so is this the agent platform that we've been waiting for?

The agent platform that can bring the capabilities of agentic working to a much wider array of people? Let's find out 

260812 in_EDIT: The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI

All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, Blitzy, Section, and Hyperagent. To get an ad-free version of the show, you can go to patreon.com/aidailybrief or you can subscribe on [00:02:00] Apple Podcasts To learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai, or you can actually visit the website at aidailybrief.ai and click around to the sponsor section. While you are on aidailybrief.ai, you can alsofind the complete companion to each episode. Every single episode is broken down into shareable chunks, meaning that if there's just one quote or some number that you wanna share with a colleague, it's probably there waiting for you

You can also sign up to our newsletter from there. So again, aidailybrief.ai

With that though 

Let's first cruise through the headlines and then talk about this exciting new release of GrokBot 

260812 hed_EDIT: Welcome We kick We kick off today with a story that has gotten enough attention that it honestly might make it into a main later this week. Anthropic has stirred up huge amounts of controversy by introducing watermarks for AI-generated text. As of this month, all new Anthropic models will now include invisible watermarks in their generations.

Anthropic models will be able to detect the watermarks to help identify AI-generated content, and Anthropic will support third-party AI detectors to do the same. This new policy is part of Anthropic's [00:03:00] commitment to the EU Code of Practice on AI-generated content



260812 hed_EDIT: part of the EU AI Act. Now, Now, the controversial part is that Anthropic is not just including watermarks in images or videos to combat the harms of deepfakes as other companies have done. Instead, they're embedding the watermarks in all generated text. And importantly, it is not in the metadata But instead, the watermark is somehow included in the text itself

Anthropic claims you won't see it, and it doesn't change the meaning, quality, or readability of Claude's response. Because the watermark is part of the text, it will travel with the text when it's copied and pasted elsewhere and may persist through some editing

The policy is being applied to all models in all regions, so even if you're not in the EU, your Claude outputs will still be watermarked



260812 hed_EDIT: folks were very skeptical

That Anthropic can achieve this 

Nathaniel Whittemore: 

260812 hed_EDIT: without degrading the quality of the outputs

Writes Orf, " " The watermark will basically be the statistical signature or word choice of the models. Anthropic claims this won't affect quality, but this seems non-obvious given that they'll be constraining the model sampling and [00:04:00] biasing token choice, and potentially making the model less creative and inventive downstream."

The EU does it again

Now, it would be hard to describe in just a couple of tweets how upset people are about this

Recognizing that this is not justfor regular word writing but also for code writing, developer Nick Dobos wrote, " "Claude Claude adding invisible watermarks inside my code base? Total BS. Diabolical precedent to be setting. What TF are we even doing here?"

Simon Smith writes, " Question about Anthropic's watermarker. If I task Claude with doing research and that research requires quoting something like a legal document, will the quote be subtly changed from the source to introduce the watermark? Because that's terrifying. If not, how can we be sure?"

And And while Andrew Curran points out that Gemini has been doing something like this since 2024, people, that didn't make people feel much better. Now, this is a debate that's worthy of more than just the headlines, but for now

That's the primer on the topic, and I am sure it is not the last that we will be hearing about this

this Speaking Speaking of Google, the company has announced that they have reached abillion users for the Gemini [00:05:00] app. CEO Pichai announced the milestone on Tuesday, posting, " One billion-plus people are now using the Gemini app every month to spark new ideas and get things done. It's our fastest-growing product ever and our 14th to hit the one billion user mark."

mark." Now, Now, some are a bit skeptical of this. given that Gemini is integrated into Search, YouTube, and other platforms

But The Verge confirmed that this week's billion user milestone applies specifically to the Gemini app Google has begun pre-installing Gemini onto Android handsets, but those users still need to engage with the app to be included in these numbers Google Google also shared some interesting details about how users are interacting with their chatbot.



Nathaniel Whittemore: Sixty-three percent 

260812 hed_EDIT: of users are using the voice interface, demonstrating how eager people are to ditch the keyboard. 

Nathaniel Whittemore: 

260812 hed_EDIT: Gemini has also retained massive volume for their image model, with users generating 150 million images per day



260812 hed_EDIT: what's what's really interesting is what this says about the state of models Olga Zircon points out that Google doesn't have an AI model in the top 10 right now, suggesting this means what wins in consumer markets isn't the product, it's distribution

But you also have to think that a [00:06:00] lot of those billion users have no idea what they're missing, given that all of their AI use is stuck in a model that is at this point at least six months behind the frontier

Now staying Now staying on the product side for a minute, Manus is returning as an independent company after finalizing their split with Meta. Manus was acquired by Meta for two billion in December, but in the following months, Chinese officials scrutinized the deal and in April ordered it to be unwound The national security concern, it seemed, was that the big payday would encourage more Chinese startups and talent to seek an exit in the West In the interim, there has been swirling discussion on how Manus will raise the money to repay Meta, given that the funds had already been distributed to investors.

On Tuesday, however, Manus announced that they'll soon return as an independent company serving their millions of users. However, to complete their separation from Meta, they need to delete some user data generated after December twenty-ninth. They advised all users to back up their data ahead of the transition date on August twenty-third, and said that independent systems will be online from August twenty-fifth Now the Now the big question is whether this is a fresh start for Manus that will let them get back in the agent race.

race. In a post on X, they wrote, " As we look [00:07:00] ahead, we couldn't be more excited by the future. We're preparing a series of new features that will push the boundaries of what's possible for general AI agents once again."



260812 hed_EDIT: and frankly, while it's reasonable to be skeptical you gotta think that the innovation that they will pursue now as their backs are against the wall and as they remain independent is a lot more than what we would've seen from inside the behemoth that is Meta

As Peter Corbett points out, going back to $0 ARR and starting again is going to make for an interesting case study

study Now on the Now, on the topic of hot segments of the AI industry, OpenRouter's $10 billion price tag has apparently triggered a bidding war across the router segment. The Information reports that interest in token router acquisitions is off the charts, with multiple large software companies looking to add the infrastructure to their stack.

Snowflake is reportedly in the market alongside Base10, Cloudflare, and and the interest is reaching some very small startups in the space

Thibaud Jaigoo, the CEO of Requestly, said that his five-person startup has fielded interest from 25 different companies looking to invest, acquire, or partner with Requestly

Dean Mai of Meria Ventures Partners, which has a small Token Router [00:08:00] play in his portfolio, thinks it's a seller's market, commenting, " It would be unwise for data infrastructure players and hyperscalers not to entertain acquisitions right now." Ari Ari Jacoby, the co-founder of token router Concentrate AI, said that he's been approached by seven companies so far this month, commenting, " " We've been unbelievably popular for the past two weeks in a way that I could have never imagined before."

In In other words, it seems at this moment 

Nathaniel Whittemore: 

260812 hed_EDIT: that the large companies and incumbents have decided that even if they could build this sort of functionality, the need for speed trumps all and it is time to buy

buy Moving over Moving over to markets for a moment, another story which could easily be an entire main. Nvidia is putting together a $500 billion platform to help improve the financing landscape for data centers. Announced on Monday, the platform will provide financing from investment banking and private credit giants, including Apollo, BlackRock, and Blackstone.

These firms will provide credit to NeoClouds to help fuel the data center build-out. The details of the arrangement aren't entirely clear, but it appears the approach could bring together multiple lenders to standardize data center debt

It also appears that NVIDIA GPUs will be accepted as [00:09:00] collateral and revenue sharing could be part of the arrangement

In a press release, Jensen Huang said, " " NVIDIA has reached an important milestone. We began by building chips. Today, we are helping create a new class of productive, investable infrastructure, AI factories. In AI, compute is revenue. NVIDIA Compute is uniquely suited for this role. It is broadly adopted, flexible across models and workloads, fungible and transferable across customers and operators.

These financing platforms will help customers access scarce compute at scale and build the AI factories that will power every industry and country in the age of AI

In a CNBC interview, Huang presented this as a new paradigm for AI financing Saying, this is really the first time that technology chips have become an investable asset class. These are revenue-generating assets now. They're productive, they're long-lived, they're fungible, they're flexible

Now, of course, for the bears who are worried about circular funding

This is just pouring absolute gasoline on the fires of their concerns



Nathaniel Whittemore: 

260812 hed_EDIT: but for other more neutral market actors The move seems to be paying dividends. Tuesday saw Nvidia's credit spreads close, implying a lower risk of default, and their bonds [00:10:00] also rallied, reducing the implied interest rate for the next round of borrowing So at least when it comes to NVIDIA themself, essentially the market interpreted the new vehicle as NVIDIA spreading the risk of losses across multiple other parties

If we see an AI slowdown, investors no longer expect Nvidia to take a double hit from reduced revenue and bad debt from data centers. 

Nathaniel Whittemore: Sal 

260812 hed_EDIT: Naro, the CIO at Coherence Credit Strategies said Nobody knew what the $500 billion potential Financing meant. today you have an idea that they're getting everybody involved and that their exposure isn't as serious as investors originally feared

feared

Nathaniel Whittemore: 

260812 hed_EDIT: lastly today,

lastly today, keeping track of things in Washington, Senator Bernie Sanders has officially joined the Pause movement and is calling on Sam Altman, Dario Amodei, and Mark Zuckerberg to do the same. In a letter to the trio, he wrote, " Almost every day there is a new story about how your companies are losing control of the AI technology you are developing with potentially cataclysmic results

He referenced the recent scientific research about using AI to create novel viruses as the prime example, claiming, " This type of development in the wrong hands could lead to new bioweapons that result in the deaths of tens of millions of people." This is, of [00:11:00] course, despite the actual research having no connection to any of these three companies and using a completely different type of AI to their LLMs.

But for the sake of Sanders' argument, it's all AI

Sanders also referenced the Hugging Face hack, arguing it was a clear violation of federal law



Nathaniel Whittemore: 

260812 hed_EDIT: and

and leaving the letter on a slightly threatening note, Sanders concluded, " Let me be very clear. If you do not take appropriate action now, my colleagues and I in the Senate will."

Just Just another example of the temperature rising in Washington. For now, though, that is gonna do it for today's,headlines. Next up, the main episode 

main episode 

If you're leading AI inside an enterprise, you already know that the gap right now isn't capability, but execution. That's why KPMG's You Can with AI is back with a new season featuring conversations with leaders like Serojia Chatterjee of Emma, May Habib of Writer, Ellery Fisher, and others focused on practical execution.

Here's a harsh truth. Your company is probably spending thousands or millions of dollars on AI tools that are being massively underutilized. Half of companies have AI tools, but only 12% use them for business value.

260812 main_EDIT: Nathaniel Whittemore: Welcome back to the AI Daily Brief



260812 main_EDIT: I genuinely don't remember the last time I saw people as excited about a product announcement



260812 main_EDIT: as people have been about the newly announced Grokbot

And And when push comes to shove, I think the reason why is pretty simple

Ever since OpenClaw came out at the beginning of the year



260812 main_EDIT: People have been looking for ways to build and deploy agents on their behalf 

ideally in a simpler way than what that sort [00:15:00] of technically complex system required There have been a variety of shots on that goal, but nothing has really stuck



260812 main_EDIT: but first impressions suggest that that's what Grok Bot might be

be The The interface for interacting with GrokBot 

Nathaniel Whittemore: 

260812 main_EDIT: looks looks frankly like Telegram, which is of course where most people were interacting with OpenClaw when it first came out

Nathaniel Whittemore: To To get started, 

260812 main_EDIT: you can either create a new bot



260812 main_EDIT: Or you can interact with a bot that you've already initiated



260812 main_EDIT: you you interface with your GroqBots through the chat window

Exactly as you had with OpenClaw, and frankly, exactly as you do with Claw or Codex

And GrokBots work in the background in their own virtual computer Meaning you can keep working while the task is running on the cloud

It's It's also capable of using its computer through human interfaces

So it can sign into web apps and operate software without APIs



260812 main_EDIT: When it needs you to authorize something, it'll simply bring up that window

And have you sign in on its virtual machine in the same way that you would on yours

GrokBot is of course powered by the family of SpaceX AI models



260812 main_EDIT: which are once again getting competitive. 

m- 

meaning that while it might not be as good as Fable or Five Six Soul on certain tasks



260812 main_EDIT: the [00:16:00] agent likely will be good enough to handle a wide range of work tasks end to end. In fact, as we'll see, SpaceX says they've been testing GrokBot internally, and it has basically taken over as a core work tool

Now, Now, none of this is net new functionality But the way that they put together the elements and the ease of use has made a huge leap

Like The interface, again, that simple Telegram-style interface

abstracts all the complexity away



Nathaniel Whittemore: 

260812 main_EDIT: and that includes the native integration of a lot of advanced features that have been difficult to use or disappointing in other products



260812 main_EDIT: For For example, you can run multiple bots at the same time, but rather than being overwhelming, the inter-bot messaging system and clean interface makes it feel way more achievable to manage a team of agents.

You can even build a whole team of agents, each with a specific role and individual name. Your GroqBots can coordinate with one another, allowing them to function like a single integrated agentic system

And while Grokbot doesn't currently live in workplace messaging apps like Slack or Microsoft Teams



260812 main_EDIT: You can set them up to work together across individuals' accounts



260812 main_EDIT: integrating a promise that's been around with us since the days of RPA

Because the Grok bot is at core a computer [00:17:00] use bot using its virtual machine



260812 main_EDIT: You can really easily train it on common workflows by asking it simply to follow along the next time you do a particular task AI says that the bot will watch the steps and remember how the work gets done, saving the workflow as a routine

You can also iterate on this process, providing corrections that improve the bot's workflow 



Nathaniel Whittemore: Kind of 

260812 main_EDIT: like being able to create a skill with a screen recording, but much more native

The company says that the Grok bots will learn over time and get better

Adjusting things like writing style or handling of edge cases, or even knowing when tostop and ask for clarification



260812 main_EDIT: Now, Now, one thing that I always watch when a new product gets launched is how the team that built it is talking about it. 

And while you might wonder how valuable that is because, of course, the team that built it is going to shill it, right? I think you can actually get a lot of signal for how a team talks about the thing that they've built

And the team at Cursor and SpaceX AI

for whom this is one of their first major collaborative products, are absolutely raving about this thing. Zheng writes, " " Our relationship with AI is shifting from chatting back and forth to entrusting a team of agents with real work. Grok Bot is a glimpse of that future."

Sam [00:18:00] Socolan writes, " "This This is one of the coolest projects I've worked on. GroqBot had insane product market fit internally almost instantly. For much of the company, bots have become the interface for all of their work."

Cursr's Ricky Dora writes, " Grokbot is not a new concept, but its execution is flawless. It's mind-blowing what a good harness, cloud computing, massively advanced computer use, and state-of-the-art models are capable of. Every day I automate 20% more of my job So I can discover the next frontier 20% to focus on

on First impressions of the community were similarly positive



Nathaniel Whittemore: Singh's brain exploded with all sorts of different use cases. Calling GrokBot actually kind of ridiculous, he says, "It can open a computer by itself, log into your apps, use websites like a human, work while you sleep, clean your inbox, send emails, update your CRM, research people and companies, write LinkedIn and email drafts in your style, remember how you work, learn a workflow after watching you once, run that workflow forever, coordinate with other bots, only bother you when it needs a decision, and so much more that I'm yet to decipher.

260812 main_EDIT: This is less AI assistant and more the intern who somehow became COO overnight."



260812 main_EDIT: Prasenjeet Prasenjeet writes, " First impression with [00:19:00] Grok Bot, I gave it a GitHub link and told it to read the code. Not only the read me, it pulled every file through the API and broke down the entire code base. This thing is not just a chatbot

Mike Mike P writes, " "My My first impression after chatting with the bot to understand how it works is that this is currently the best mainstream interface for agentic AI that I've seen from any leading company."



260812 main_EDIT: he explains that it uses a virtual machine but can also access your local file system. " The magic," he says, "and the key differentiator is that you don't actually have to toggle a bunch of UI options or set anything up."

Writes Mike, " "I I think a lot of people open Claude Cowork or Code or GPT Work or Codex and don't know WTF is going on and just bail because they don't feel like figuring it out

I 

just installed GrokBot, hooked up my connectors, and just started asking it stuff, and it just handled the rest. I was actually shocked when it jumped into a local folder on my Mac just from me asking. new-- there's no UI toggle or anything you need to do to point it where you want it to go. You just tell it what to do, and it asks for your permissions and handles everything in the background.

It also claims that when I use the iOS app 

It reaches for my Mac as a primary machine if I prompt it with something that [00:20:00] requires using my Mac. So basically it's a remote control, but you don't have to go into a specific part of the UI like you did with Dispatch. It just does it

This, This, he concludes, is what it's going to take to get mass adoption. Agentic AI wrapped up in a product so easy to use that people will be able to just unwrap it and start cooking

Now Now another notable thing in the early discourse to me is that a lot of times you hear people raving about it without being specific about how they used it. but I saw a ton of folks actually talking about their use cases and what had impressed them in specific Yun-Tu Tsai writes, " writes, GrokBot was able to A, go through the calendars and find anything I need to make reservations for beforehand that I hadn't done yet.

B, determine the best time to make reservations. And C, navigate the reservations on a website. While I was walking in the parking lot before getting to my cars, I was talking to it in mixed Chinese and English." Color me impressed

Matt Matt Schumer writes, " "The The little details are what makes GrokBot special. For example, I set up a researcher bot and a writer bot, then made a chief of staff bot and asked it to get theand asked it to get the other two working together on a project. I checked in fully expecting that to fall apart because there was no way it would work out of the [00:21:00] box. 

It worked out of the box."

Honestly, he says, "This feels like it could be the thing that gets millions of normal people using agents for the first time."



260812 main_EDIT: and that was really the gut sense for a lot of folks. That the promise we first saw in places like OpenClaw and then Hermes 

might finally be getting its moment to scale with something like GrokBot

a16z's Martin Casado says, "This is the first product I've used that really nails the virtual coworker. I suspect we'll view this launch as a pivotal moment in getting the abstraction for AI in the workplace right."

Hiten 

Shah, who if you follow him, has been going deep on agent building ever since Open Cloud came about, wrote, " I spent months building agents the hard way. I gave them servers, memory, skills, tools, and loops. I put them in Slack and built recovery around them. One helped me ship a product in six days.

The same system also stalled, lost context, and handed the unfinished edges back to me. I became the infrastructure. That's why Grokbot hit me so hard. I've been testing it early. Its bots coordinate with each other, work from a persisted computer, and keep going across your files and logged in apps while you are away.

[00:22:00] I recognize what the team built because I had assembled so much of it by hand. Grokbot moves more of the invisible work around the agent into the product. This is the missing work agent I have been waiting for."

But no product can be perfect right out of the box, right? so where are people's complaints?

One small one is around the naming conventions between Cursor and SpaceX. Mike P again writes, " " The Cursor SpaceX AI overlap is giving Venmo PayPal vibes. Are Cursor and Groq going to stay separate things? This is called GroqBot, but I'm getting routed to a Cursor login portal.

I need to connect my Groq account to Cursor to launch a Groq product. What are we doing here, fam?"

And indeed for some, Grok has too much baggage to be excited about this new product. Ben Barry writes, " I would have excitedly tried Cursor Bot, but have little to no interest in trying Grok Bot. Way too much negative baggage for me to ever trust it with access to anything.

I'll wait for the inevitable offerings from OpenAI and Anthropic."

Beyond that, some people just didn't have a great experience

Gurbax Chahal writes, " Sorry guys, but Grokbot feels like a shiny object that looks incredible in demos but simply isn't ready for prime time. The [00:23:00] economics are broken. You burn through tokens just trying to onboard it, then get pushed towards spending more just to keep going.

That's not a sustainable workflow. It feels like a broken slot machine. The bigger issue is memory. It forgets context, loses track of tasks, and struggles to maintain continuity across longer projects." An AI coding agent needs to remember the mission, not act like it has amnesia every few hours



260812 main_EDIT: now I now I wanna provide a full range of views, so I'm including this



260812 main_EDIT: however, this was definitely not a common take that I saw So contextualize it or give it whatever grain of sand you want

want

Nathaniel Whittemore: 

260812 main_EDIT: other other complaints include this one from June Saying that while GrokBot has a really clean UI, quote, "It still heavily relies on integrations. No one wants to connect 20-plus tools during onboarding. Plus, I'm not sure people want to create a specialized agent for every task."

Matt Matt Schumer writes, " My my only real complaint, which if they nail it will end up being a huge win, was the model router, which wasn't great when I tested it. it. You don't choose a model for your Grok bot. It's done automatically on the back end. Incredible for regular users when it's done well, but frustrating for power users when done poorly."

Schumer did add, "I'm told they've [00:24:00] made it much better since I tested."

Max Blade points out a functional issue of logging into your services through GrokBot's virtual computer He says the biggest issue right now is the data center IP address creates bot blockages on everyday websites, which make things like ordering groceries from Walmart problematic Although he notes, quote, " "This This will be solved by expanding their built-in connectors and plugins to give official support everywhere."

Maybe beyond that, there's just a broader question of trust that is not unique to Grok Bot, but becomes more poignant the more powerful and the more deeply integrated into our work and personal lives these tools get

Peter Peter Yang wrote, " The challenge with this, and I'm sure upcoming products from the other major labs is, one, how do you get regular users to trust sharing their credentials and logins with a remote computer? Two, how do you reassure them that this remote computer is secure and truly theirs to play with?"

with?"

And honestly, this one resonates with me. When I was playing around and testing GrokBot, which spoiler alert, I am incredibly impressed with and share a lot of the same excitement that you've heard from other folks in this episode

I did have this moment where I was about to log it into my [00:25:00] Spotify for Creators account, which by the way, was a relatively simple process of signing in via its virtual computer interface but then paused

Thinking about just how devastating it would be if 

something went wrong By nature of the computer use paradigm, I wouldn't just be giving it access to, for example, some analytics API. I would be letting it have access to my actual account to click around and do things. now I certainly don't think that some errant command of mine would lead it to go delete all past episodes of this show But the fact that that's even possible gave me pause Peter, and like Peter noted, this is certainly not a problem for GrokBot alone, but it is a major barrier

to fully transitioning to new ways of working

Still, it's important not to overstate this. For example, I had no problem giving it access to my email because frankly, it's sending a bunch of emails that it shouldn't or even deleting a bunch of emails. would not be nearly as devastating as anything having to do with the show

One One very practical knock on the tool so far is that it is only for extremely expensive accounts



260812 main_EDIT: You're either talking about a $300 a month Groq Heavy [00:26:00] account that includes it, or a $200 a month Cursor Ultra account, which doesn't have access to the top Groq model. So at least for the moment, this is pretty well price-gated that said, I would be very surprised if that was a permanent feature



260812 main_EDIT: rather than an inference preservation mechanism first and foremost at this stage

One interesting conversation, which is actually an episode that I was thinking about doing later this week



260812 main_EDIT: is about whether the AI teammate metaphor is actually the right mental model

I've been wondering and plan on exploring



260812 main_EDIT: whether in fact AI teammates are for a variety of reasons the wrong model and a better might be something like consultants. But clearly I'm not the only person thinking about this, as Type.com's Fletcher Richmond wrote: " wrote: we also thought a bunch of AI teammates was the right paradigm, but we've learned from customers that having dozens of AI teammates is actually counterproductive.

It's a vanity metric. Instead, teams need a shared workspace where they can work with any model, build a company brain of skills, integrations, and context/memory mapped to their permissions, build and host custom apps, and interact from Slack, email, or wherever they work. Grok Bot is pretty slick, but it's not how people are going to [00:27:00] work."



260812 main_EDIT: now I'm not convinced that it's as binary is posting it



260812 main_EDIT: But I would agree that I believe we are going to discover that there are two very different modes when it comes to this sort of agentic support 

Nathaniel Whittemore: 

260812 main_EDIT: the things that you use personally and the things that interact with and integrate your team, and they might be pretty significantly different



260812 main_EDIT: still I expect that over the next couple of weeks, we're going to see a lot of exciting experiments



Nathaniel Whittemore: 

260812 main_EDIT: that harken back to those early awesome days of OpenClaw when people were spinning up entire teams



260812 main_EDIT: and to Parco on Twitter has built a core team that includes a chief of staff, an engineering manager, five engineers, a data analyst, and a product manager

and shares how they interact and work together.



260812 main_EDIT: Farzad has given his team names. Webby is his web designer, Shotri is his short form content creator, Wrighty is his article/newsletter writer. You get the idea

I I fully intend to do a bunch of experiments and come back and report to you on where I'm finding value

But for now, I agree with Kettlebell Dan when he says the excitement around Grok Bot has been off the charts today. I haven't seen this kind of reception for a new product in a while



260812 main_EDIT: I, for one, am extremely excited to dig [00:28:00] deeper and will report back when I do

That, That, however, is going to do it for today's AI Daily Brief. Appreciate you listening or watching as always, and until next time, peace 

​ 

Nathaniel Whittemore's audio recording:
