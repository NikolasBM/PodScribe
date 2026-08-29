# The Most Useful New AI Features and Tools to Try — Transcript (2026-08-28)

https://aidailybrief.ai/e/2026-08-28 · Listen: https://pod.link/1680633614

---

[00:00:00] 

Which of these sound most exciting to you? A new ability for Claude to use a browser window to be able to do tasks for you

the ability for ChatGPT to effectively switch in and out of temporary mode as suits you

A new voice model that not only can faithfully transcribe what you actually say, but even clean it up and get at your intent

a new video model from Google with massively more controllability for actually generating videos that you can use for real things or a totally different video model that takes you less time to generate the video than it does to watch it These are just some of the new features, models, and tools that released this week

The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI.

All right, friends, quick announcements before we dive in. First of all, thank you to today's All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG

Harbor, Blitzy, and Hyperagent. to get an ad-free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts To learn more about sponsoring the show, send us a note at [00:01:00] sponsors@aidailybrief.ai

And lastly, if you listen to today's episode and think to yourself, "Man, I wanna use all those features, but I feel behind. I need to catch up in my AI skills the next cohort of super intelligent training programs which are incubated over here at AIDB are coming up in September.

You can find a link to them on the Daily Brief website, or you can just go to training.besuper.ai 

Welcome back to 

Kicking off, confirmation that Hugging Face is being sold and that, yes, it is to NVIDIA. The Information broke the story late on Wednesday night following the earnings call, with their sources saying that NVIDIA has agreed to buy Hugging Face for $12.9 billion.



Now, rumors of the deal only started emerging over the weekend and while of course this could have all been going on before anyone externally knew, it seems like it might have been a pretty speedy negotiation



much of the reporting focused on the strong valuation multiple. Hugging Face only has a hundred and fifty million in annualized revenue, meaning that NVIDIA is technically paying around eighty times revenue as a price. as a point of reference, SpaceX's sixty billion dollar acquisition of Cursor was aroundfifteen times revenue.

Still, as I said the other day when I talked about the [00:02:00] potential of this deal, NVIDIA is very much not buying Hugging Face for their revenue. Instead, the deal seems to confirm that NVIDIA is acquiring their way into a full stack open business model.



Hugging Face is the premier distribution channel for open models. NVIDIA's six billion dollar licensing deal with Poolside announced last week allowed them to hire about a hundred veteran AI researchers to staff up their team

And other investments like their strategic partnership with Perplexity give them solid harnesses as well as an app layer play. What's more, over the course of around six months, NVIDIA has taken their open model series NeMo-Tron from a tech demo to a real contender among open models



Gupta suggests that as much as it might be an offensive play, it's also a defensive play. He writes, Google

Google has run its own TPUs for a decade. the labs writing Nvidia the largest checks are the ones working hardest to stop."

Open models are the counterweight. When Meta or Mistral or DeepSeek releases weights, millions of developers download them, fine-tune them, and serve them, overwhelmingly on NVIDIA GPUs through CUDA. Custom silicon has no answer for that ecosystem

I think the defensive [00:03:00] positioning is not just relative to NVIDIA's chip business, but also its positioning for the world that we keep talking about, where companies simply use a diversity of models And many of their common and core day-to-day processes are run not on the state-of-the-art frontier models But on something open, lighter, more nimble, more customizable.

A while ago, Nvidia spotted that opening and has been careening towards it ever since



is r- Now in terms of how folks are receiving it



no one has a hard time understanding why NVIDIA made the move. Fumbler writes, " "NVIDIA NVIDIA clearly don't just wanna sell the picks and shovels, they wanna own more of the AI economy built on top of them

Gianluca writes, " NVIDIA owns the GPUs, CUDA owns the developers, Hugging Face the open source AI ecosystem. Jensen is slowly putting the whole stack together. NVIDIA is becoming much more than a chip company."

Others though are wondering if people will stick around Hugging Face given its new ownership

Todd Saunders writes, " Hugging Face is valuable partly because it is perceived as independent and broadly neutral. their users include researchers, startups, enterprises, cloud providers, hardware companies, and competitors to [00:04:00] Nvidia. Today, developers can use the platform without believing that it is designed to push them towards one vendor.

It's partially what they love about it. An Nvidia acquisition could threaten that trust, but this could be a home run."

run." Pratham Pratham thinks that this is a bigger trend as well. They write, " The real question isn't why NVIDIA bought Hugging Face. It's what happens to open source AI when its biggest players start buying the places where it lives?"



Eric Eric Hartford thinks that we will see an opportunity

He writes, "I'm happy for Hugging Face for their exit, but this is gonna be a loss for open source AI. HF is no longer hardware agnostic. This is an opportunity for a new standard bearer to arise."



still, still, that's the kind of concern that people always have around acquisitions, and relative to expecting that to be the case, I would suggest that there is a lot more optimism around this particular acquisition than you normally see Which shows what a good job NVIDIA has done building trust in the AI community.

Connor Dart writes, " I can't think of a better company to buy Hugging Face other than NVIDIA, and it makes sense as it aligns with what they are doing as a whole. I bet we will be seeing loads of more amazing [00:05:00] features and ways to train and use models on Hugging Face going forwards."

Ramez Naam writes, "Such a great fit and such a great push towards plural AI. NVIDIA sells compute. Hugging Face makes it easy to access a plethora of ways to turn that into value. Reduces the odds that any one lab, company, or nation will monopolize frontier AI. The world is better with plural AI."

Nvidia also reported earnings this week and kinda blew the doors off. Revenue growth accelerated to one hundred and six percent over the past year, twenty-one points higher than their growth rate at the end of Q1. quarterly sales for the quarter came in at ninety-six point two billion, tantalizingly close to the one hundred billion dollar a quarter milestone that only five other companies have achieved

Still, while forecasts were ahead of expectations, NVIDIA is still flagging that growth will slow slightly to eighty-nine point five percent for Q3. CFO Colette Kress said that supply chain snarls would continue to weigh on growth, limiting NVIDIA to seventy percent for fiscal year 2027. NVIDIA also disclosed that major customers are asking for more time to pay.

Free cash flow fell by fifty percent compared to a year ago, coming [00:06:00] in at twenty-one billion. This fall was mirrored by a fifty percent rise in accounts receivable. NVIDIA said the cause was, quote, " extended payment terms on large multi-quarter agreements with certain investment-grade customers." Certainly this was the big red flag for investors with days sales outstanding rising from forty-five days to sixty days alongside the numbers, NVIDIA announced that they are officially back in the Chinese market.

They reported a small volume of sales of H200 chips under new export control rules, but noted that the figure was well short of the total permitted by the Trump administration



Ultimately, while there was room to find some negatives in the report, it's difficult to overlook the raw sales numbers. Nvidia was already shipping an incredible number of chips by last summer, and they've almost doubled sales since then Reinforcing that point, Amazon announced that they would be buying an additional two million NVIDIA chips as they accelerate their data center build-out.

NVIDIA doesn't disclose how many total chips they sell per year, but it's believed to be less than ten million, meaning that this is a huge additional order that will keep demand solid for years into the future

The earnings [00:07:00] were enough to drive investors back to NVIDIA, sending the stock up by four point eight percent in after-hours trading



one one interesting sub-story given the unique role that NVIDIA is increasingly playing in the AI ecosystem, the company has paused revenue sharing deal with Neoclouds as they rethink their approach to industry backstops.

Less than two months ago, NVIDIA announced that they would start offering new financing deals where customers could receive credit support in exchange for a cut of the profits. This was seen at the time as an improvement on NVIDIA's previous model, where they would guarantee data center demand and hope that translated into cheaper financing from private credit firms or banks.

Sources told The Wall Street Journal that this program has been put on hold after some employees expressed concerns. there is a belief that the arrangement could attract scrutiny for antitrust, and there were sensitivities around how much control NVIDIA would exert over customer businesses



The journal noted that the precise reason for the pause couldn't be learned, and so theoretically the program could return in the future with some tweaks

Nvidia, for their part, denied the reporting and stated, " The new business model we introduced in July that opens up compute access to the fast-growing AI ecosystem [00:08:00] is still in place and continues to evolve due to high demand."

Now, Now, staying on Wall Street for a minute, believe it or not, Salesforce, who we will talk about in the main episode as well, is leading a SaaS comeback with a strong earnings report. Six months ago, one major market narrative was that software was done for, and companies would soon be vibe coding their own SaaS replacements.

This was the much-discussed SaaSpocalypse, if you remember that term. That level of disruption obviously did not play out, And increasingly what we're actually seeing is adoption of AI tools within traditional software products is leading to a revenue boost.

That was certainly the story on Wednesday night when Salesforce reported that their Agentforce product is on track to deliver one point five billion in revenue this year, up from a forecast of one point two billion in the first quarter. overall sales were eleven point five billion for the quarter, growing at an eleven percent pace.

So AI revenue is still a relatively modest part of the picture This was still enough though for the market to identify Agent Force as a successful and growing product. the stock was up a staggering twenty-two percent on Thursday, with Salesforce now just five percent away from [00:09:00] filling the entire drawdown from the SaaSpocalypse period taking a step back, one by one, we have seen some of the most beaten down software stocks deliver solid financials and surge back to life.

ServiceNow, Figma, Atlassian, CrowdStrike, Okta have all staged major comebacks over the past months. KeyBank analyst Jackson Ader noted that these companies haven't even needed to post blockbuster earnings to generate a huge return

Said Ader, " We're all coming around to the idea that things are going to be more durable and are not going away. That's why you see Salesforce come out with fine but not stellar results, but you see a really outsized reaction." Benioff certainly took a victory lap on the earnings call saying, " I really wanna start here at the beginning and talk about the SaaSpocalypse.



Skeptics said that seats would decline, and Agentforce, sales, service, and Slack, all seats grew year over year. Skeptics said customers would leave, but attrition was near its lowest level ever. Skeptics said pricing power would erode

But bookings more than doubled quarter over quarter and contract length terms improved across all segments, new business and renewals. And agentic use of the platform surged sixfold via model context protocol calls and [00:10:00] CLA calls. Apps are not dying



Former AI czar David Sacks pounced on the news posting, " "The The AI CapEx is a bubble and the SaaS is dead narratives getting shredded this morning

Box's Aaron Levie writes, " "This This week's tech earnings call were a critical reminder of how valuable the relationship is between software and AI. Software and agents are going to work together and ultimately grow the size of the IT TAM dramatically as a result over time."

Now bringing the booming revenue story to the app layer According to new numbers sourced by The Information, Cognition has hit nine hundred million in annualized revenue. That's more than a three X increase since the beginning of the year for the creators of coding agent Devin



and it appears to be a similar story across the board. Higgs Field, an interface wrapper for video and image models, has also tripled this year to reach sevenhundred million in annualized revenue. Perplexity has tripled their run rate to seven hundred and fifty million.

OpenEvidence, the chatbot for doctors, has doubled to three hundred million. And even Manus, after the messy unwind of the Meta acquisition, claims they have a run rate of four hundred million, quadrupling from last year

[00:11:00] And And if the total numbers still remain far behind the US Leading Chinese AI companies are seeing similar types of growth. The The Information again reports that DeepSeek has generated seventy million in revenue this year, which is a 10X increase from their full year numbers for twenty twenty-five

Now Now as we round the corner, a quick check-in on the policy side of the house A new executive order on AI regulation has stalled out after drafts were quietly circulated in recent weeks

Reports say that the Trump administration recently proposed an executive order that would create a self-regulatory body for the AI industry You You might remember this idea starting to gather support after DeepMind chairman Demis Hassabis formally proposed it in a July blog post.

The new body would be modeled on FINRA, the self-regulatory organization for the financial services industry. Essentially, this approach would require AI labs to share notes on security issues, conduct safety testing for new models, and create regulations that govern the industry. Treasury Secretary Scott Bessent, who for whatever reason has a key role in AI policy, publicly supported the idea.

Reportedly, senior officials drafted and circulated an executive order that would [00:12:00] create this new body over the past month.

And while it's not totally clear exactly why the effort has stalled out



some sources flagged opposition from former White House AI czar David Sacks as a potential cause

During last weekend's episode of the All In podcast, Sachs called FINRA for AI a, quote, "horrible idea and a Trojan horse for an open source model ban." He believes that once the body is set up, the frontier labs will push for standards that apply equally to all models, i.e., standards that open model developers will find impossible to comply with

Sachs also pointed out that FINRA doesn't have a good reputation for promoting competition and innovation. Many startups looking to enter the financial industry view FINRA as largely concerned using regulation to protect incumbents



Whatever the case for now, no FINRA for AI

But that doesn't mean that industry self-regulatory efforts are not happening

Notably, OpenAI and Anthropic and more than 100 other companies have called for an urgent new approach to cyber defense. The call came in the form of an open letter, my God, the open letters, signed by companies across the tech, finance, and industrial sectors.



alongside Google, Microsoft, and AWS, [00:13:00] the list also includes companies like Visa, General Motors, and PwC. The letter warned, "We have a limited window to strengthen cyber defenses. In the coming months, AI-enabled cyberattacks will become far more widespread and sophisticated as models around the world become increasingly capable.

The companies and public services our communities depend on, from hospitals to water treatment plants to the infrastructure that powers the internet, are at risk. Today's AI advances are already giving defenders new way to fix weaknesses that have accumulated for years. If we act decisively, we can use the defender's window tomake our digital world much more secure."

The letter proposes a collective response. the st- it asserted that the status quo isn't going to cut it, with longstanding bugs, unpatched vulnerabilities, and technical debt across all computerized systems. 

The letter called for cyber defenders to be provided with access to better AI tools as well as better coordination across industries A global response is necessary, it argues, requiring new partnerships to raise security standards and find new solutions for emerging cyber threats



remarking on the open letter, Sam Altman positioned security as more important than competition, posting, " This is a [00:14:00] critically important moment for cyber defense with AI. There is not much time to act. We are happy if you want to work with us or any of our competitors or partners, but please take this moment seriously.

Only an urgent and intense collective response will work."



putting putting an exclamation point on it, Professor Ethan Mollick writes, " Your organization is not spending enough of its effort bolstering cybersecurity during the window before open-weights Mythos class models and harnesses become available. The Hugging Face incident shows us you don't even need intentional bad actors to be exposed to AI hacking

Like I said, quite a meaty headlines to end the week, but for now, let's move into the main episode and talk about the slew of new features and tools that you could be using and trying right now 

A new study from KPMG and the University of Texas at Austin found that when people work with AI, similar skills don't guarantee similar outcomes. Researchers studied more than five hundred early career professionals and found that the best performers consistently amplified the value of AI by [00:15:00] guiding, evaluating, and refining its outputs.

These top performers, called AI amplifiers, weren't defined by what they knew alone, but by how they worked with AI. Learn more about what separates AI amplifiers from everyone else at kpmg.com/us/aiamplifiers. 

If you listen to this show, you likely have a thesis. Maybe it's enterprise adoption, maybe it's compute, maybe it's a specific lab. Harbor Capital's AI Lab Ecosystem ETFs let you express it via five actively managed ETFs, each seeking exposure to the ecosystem around one major lab: Anthropic, OpenAI, DeepMind, Meta, or SpaceX AI.

your view of the AI race in ETF form. Harbor Capital Advisors AI Lab Ecosystem ETF suite gives investors a way to invest in the AI ecosystem they believe is best positioned for success. Search Harbor AI Lab Ecosystems ETFs wherever you invest or follow @HarborCapital on X to learn more

Visit harborcapital.com for a prospectus containing investment objectives, risks, fees, expenses, and other important information.

Read and consider it carefully before investing. [00:16:00] Risks include principal loss and artificial intelligence related risks. Harbor ETFs are distributed by Foresight Fund Services LLC. Harbor is not affiliated with AI Daily Brief, and the funds are not affiliated with, sponsored by, or endorsed by any AI lab This is a paid advertisement and not personalized investment advice. Investing involves risk, including possible loss of principal. 

Blitzy's understanding of massive code bases unlocks autonomous security fixes, modernization, and new features. So what happens when there's no legacy code at all? Greenfield is supposed to be the easy part. Clean slate, no technical debt.

But even Greenfield moves at human speed one sprint at a time. Blitzy changes the unit of work from the developer to the project, autonomously planning, building, testing, and validating entire applications from scratch. Hundreds of thousands of lines of production-ready code

One Blitzy customer stood up a brand new application, five hundred and thirty-four thousand lines of code, compressing a sixty-five-week roadmap into two weeks. Another shipped an entire application with no front-end engineer Legacy or greenfield, the answer is the same: software at the speed of compute.

Build what's next at blitzy.com. That's [00:17:00] B-L-I-T-Z-Y.com 

This episode of the AI Daily Brief is brought to you by Hyperagent where you run fleets of agents your team can manage together New users get 1000 in inference Forget local agents and chat workflows waiting on your laptop to be prompted Hyperagent deploys alwayson agents in the cloud doing real work across the tools your team already uses Marketing's agent turns competitor moves into landing pages sales agent enriches leads drafts emails and updates the CRM ops agent chases the paperwork and tracks the budget Every agent has access to shared context and follows your rules about scope and approvals It's time you add agents that feel like teammates Hire yours at Hyperagent built by the team at Airtable Claim your 1000 in inference at hyperagent.com/aidailybrief. 



Welcome back to the AI Daily Brief. Welcome back to the AI Daily Brief. Welcome back to the AI Daily Brief. Just like it is nearly impossible to keep up with

The onslaught of AI news So too is it extremely difficult for any one person to keep track of all of [00:18:00] the new features and models and tools that come out in any given week

Mostly our attention just goes to when there are big model announcements that might more fundamentally shift how we interact with AI although over the course of 2026, we've also gotten a lot more adept at harness updates as well.

Still, sometimes it's worth going through and just taking an inventory of all of the feature updates and quality of life upgrades and new capabilities that the model and harness companies have released to see if any of them can be relevant for the way that we work. Today

And with that in mind, today we are going through, I don't know, a dozen updates that I have seen over the last seven days or so, that are things that you might find extremely useful and practical in the immediate term First up, we have an update for Claude.



Cloud Cowork now has a built-in browser to make web-based tasks more convenient

If your task includes something that happens on a website, like filling out a form, interacting with a web app, a browser window will open alongside your session for Claude to use The feature can also be used for agentic browsing, similar to [00:19:00] some of the early features that caught people's attention from AI browsers like Perplexity's Comet or Dia from the browser company Claude points out that there is nothing new to install, that it's built directly into the desktop app and stays separate from your own browsers and logins In other words, this is its own browser.

it's not taking over yours

Although for those who wanna stay in their own browser, that feature exists via Claude and Chrome for many this one was a big old finally. Dan Shipper from Every says, "They did it, folks."

Santi from Mercado Libre writes, "It was about time. Very good feature."

Vibe Absintie gets at why althoughthis seems like a small feature update, when you combine it with ChatGPT Work



and and other new things like GrokBot It all adds up to a fairly meaningful inflection AI, he writes, went from writing text to browsing the web on your behalf in the same month

Or as Enums put it, " Feels like the line between AI assistant and AI operator just got a lot thinner."

Sally Stockholm writes, " "This This feels like a much bigger update than just Claude got a browser. the interesting part is that Claude can now actually do the web work instead of [00:20:00] just telling you how to do it. Need to research something, navigate a website, fill out forms, or complete a task?

The browser opens inside Cowork and Claude handles the process alongside you. We're slowly moving away from AI that just gives answers. The next phase is AI that opens the tab and gets the job done."

Now, as some pointed out



Anthropic is at least a little late to the party here

Token Gremlin says, "OpenAI has already had basically this in ChatGPT work for weeks." Julia CEO Rahul

Points to the browser agent that they released back in July. Points And basically said, "Welcome to the party."



still for many, the obvious inspiration for this was Grokbot. When Grokbot was released, the ability for it to work in its own browser was one of the things that people latched onto as really powerful, and frankly, most likely to be copied by all the other labs. a16z's Martin Casado writes, I

I find ChatGPT work more like fancy RPA. It works well, but it is more workflow oriented, where Grokbot really is a virtual Go worker. Give it its own browser, chat over Slack. It does a great job adapting to your style and preferences."

Now in terms of ChatGPT Works version of [00:21:00] this feature, the official ChatGPT account

They write, " " You can ask it to set up utilities for a new apartment, book a DMV or passport appointment, check reimbursement costs through your insurance, find and book an in-network doctor around your availability, check when your car registration expires and prepare the renewal paperwork.

Compare your rental insurance policy with an issue you're emailing your landlord about. Find and save apartment listings that match your criteria. restock something just by uploading a photo." And so on and so forth. There are about a dozen other ideas

Given our ongoing conversations about the balance between AI for life and AI for work, i.e. consumer AI versus B2B it's interesting to me that they're pitching all of these much more life-oriented tasks as a new capability for ChatGPT work

OpenAI's head of developer experience, Romain Huet, writes, " ChatGPT Work now has its own computer in the cloud. When it can use the web and take action for you, the possibilities start to feel almost limitless."

Now, Now, one other small quality of life upgrade from ChatGPT

The company realized recently that they need a better way for people to switch back and forth [00:22:00] between temporality and permanence

On X they posted, " We heard your feedback that sometimes a temporary chat becomes something worth saving. Now you can choose to personalize a temporary chat with your existing memories, custom instructions, and plugins, and and save it to your history if you want to keep it

it temporary chats don't create new memories and stay out of your sidebar unless you choose to save them in other words, for people who have a little bit more concern around privacy and who would want to be perhaps default using the temporary chat feature as opposed to saving everything that they do by default

This feature now makes it easier to pull in relevant ChatGPT context even into temporary chats, as well as to upgrade them to non-temporary when it makes sense to



another big quality of life upgrade, one which will frankly punch way above its weight class in terms of its newsworthiness, I noticed just before I started recording



Jason from OpenAI writes, " " Multiple Gmail accounts available in plugins now." In other words, instead of connecting only one Gmail, you can connect multiple



this has long been on many power users' wish [00:23:00] lists. given that the normal course of business for people of this folks is to have, I don't know, a half dozen different emails that you interact with in some meaningful way How IAI's Claire Vo was recently raving about how this was in fact her favorite feature of the new Grok that it didn't constrain connectors to a single Gmail or a single Slack

And And boy howdy is this one where I don't care who did it first as long as they all do it

it Speaking of that



many of you will always be quite happy to use whatever tools the big companies give us access to, whether it's OpenAI or, Anthropic or SpaceX AI Google or whomever

But for those who want more control And who maybe got hooked on the flexibility that something like OpenClaw enabled. It's worth keeping an eye on the Hermes agent

The team over at Hermes is clearly watching everything that the harness and model companies are doing Because as soon as anything useful gets announced from those companies, inevitably it finds its way over to Hermes extremely quickly

So for example, on Thursday this week They announced that the Hermes agent can now seamlessly browse as you

They write, " " Turn on real profile browsing and your agent acts with your [00:24:00] logins from a managed copy of your existing Chrome profile."

This follows from about 10 days ago, right after the Grok bot announcement

When the company introduced bot mode for Hermes Desktop

With Bot Mode, they write, your agent profiles become a series of named bots. Each bot has its own role, model, memory, skills, and profile picture. Bots can use any model and even communicate with each other. Build a specialist bot once to use it forever

Articulating why this might be of interest to some folks The The news research account who makes Hermes writes, " Hermes Agent has its own remote computer too. You just aren't locked into using and it costs a few dollars per month instead of two hundred. Some other big differences: connect any provider, sub, or model.

Use it completely free on your own machine or with one of several free models on News Portal. Switch between bot mode and classic sessions mode. Self-improving agents that learn to execute tasks cheaper and more effectively. Open source, so you can modify anything you want about the agent itself to suit your needs."



again, again, this is not going to be necessary for everyone

But I think it is pretty rad from a consumer choice perspective that Hermes is very much keeping pace [00:25:00] with all of the major harnesses as these new feature upgrades and capabilities come online

And And by the way, Hermes isn't just copying things. They're also doing some really cool experimentation on their own as well

They have a Hermes HUD mode, which is basically a seamless overlay where you can keep track of things going on in your work life as you're doing other stuff like playing a game



the official news account writes, " I just play games all day and get my work done in that little text box now

Now, if Hermes is on one end of the spectrum, the new collaboration between Salesforce and Claude has to be on the other Salesforce and Anthropic are teaming up for a partnership that they are calling, wait for it, Claude Claude Force. At its core, this is a new set of plugins and skills to allow Salesforce users to access their CRM using Claude agents

They can use Salesforce data as context, and thanks to Salesforce's AI harness, which they call AI Force, agentic actions can be taken while respecting existing governance guardrails. in in their press release, Salesforce writes

For decades, enterprise software required users to manually navigate static [00:26:00] UI to get work done. Now that agents can access the data, workflows, and rules directly, software is a system that powers every interface



The move underscores that there is an inevitable shift in how we interact with things like CRM

making it easier for agents to more natively do so. Salesforce CEO Marc Benioff said, " Here the UI is the AI, allowing you to build custom apps dynamically and answer any enterprise question."

Probabilistic intelligence alone doesn't run a company, and deterministic systems don't reason. Which, by the way, is just about the fanciest way to say that AI and software both have roles to play that you could have possibly imagined

Benioff continues, " By fusing Claude's extraordinary reasoning with the trusted data, workflows, and governance every enterprise runs on, we're delivering a dynamic interface that thinks, reasons, and acts. This is how every business will run." And yes, it even got a new Matthew McConaughey ad



Now for Now for some, especially as Dario appeared next to Benioff on CNBC

This was a moment for cracking jokes

Entrepreneur Varun Ram Ganesh writes, " Anthropic while raising [00:27:00] VC money: Our TAM is the US economy. We are the ultimate intelligence. We are killing the entire app layer. We are going to create 50% unemployment and make the entire human workforce redundant. Anthropic in reality: Excited to announce CloudForce in partnership with Salesforce."

But But this sort of joking massively undersells just how much of the enterprise world actually runs on things like Salesforce.

Thomas Fanning writes, " Claude Force is notable enough to make me rethink my priors." The competitive signal is shifting. Beyond the headline, what I find most notable is that the Anthropic CCO saying that CRM integration is the first of many.

Realistically, software vendors always should have been the Frontier Lab's largest customers Up to now, however, it seemed like Anthropic and OpenAI had decided to go direct instead. Their strategy is changing, and in a dynamic market, when the facts change, your view has to change. Anthropic is clearly recognizing that it's hard to displace software outright when the agentic guardrails, governance, and infra doesn't exist in the enterprise and won't for another one to two years.

The question now is, do customers still want to move [00:28:00] data out of systems of record to build natively and avoid paying software platform API fees, or will they accept the utility of enabling AI on an existing software infrastructure? The narrative is shifting, and intuitively, these native integrations should deliver customers the value they want from AI without as much of a lift.

Hard to be bearish on enterprise software at present given the magnitude of this narrative development. Data, operationally embedded workflows, expertise, incumbency are still the moats for software, and Anthropic is sending a market signal acknowledging the persistence thereof.

And look, obviously it's just a handfulof anecdotal examples



fo- but the folks that I spoke to about this Claude Force deal that that actually interact with systems like Salesforce were extremely excited about it



been, and at least one who had been planning on potentially building some alternatives to Salesforce or at least exploring down that path

basically threw the brakes on that so they could figure out if this just did what they wanted in a way that it justified the cost

So while the X posters may get their yucks, over in the real enterprise world, Some of you I imagine are sitting here thinking that this is the biggest deal of anything I've said so far

far Now Now [00:29:00] already we've gone through a ton of features

But there are a couple models that are worth noting, and this week they were clustered around audio and video



Gemini was back in the news this week with the release of a new version of their speech-to-text model, Gemini 3.5 Transcribe



The model supports more than eighty-five languages, and Google says they've made some huge strides in usability. The model can function in verbatim mode if you need a direct transcription, or you can use it in smart translate mode, which strips away filler words, condenses rambling thoughts, and handles self-corrections to deliver a clean version of user intention. You can even create custom vocabulary to enhance the model's ability to deal with jargon and slang.

Google says the model performs well in noisy environments and can distinguish between up to three different speakers. The model can be used across Google's AI suite if voice mode is your preferred way of interacting with AI and is also available as an API to power third-party apps. playing, so this is very much playing in the

space This is then playing very much in the space of something like Whisperflow

Although built not just to be an end application in itself, but also a key piece of infrastructure for other people who can build on top of it

AI developer [00:30:00] Jan Kronberg wrote, " This is the kind of release a lot of people are going to miss. Until now, voice input required you to basically speak the way you write. Punctuation, well-structured sentences, fewer corrections along the way. Gemini 3.5 Transcribe flips that around. You speak the way you actually think, and the system produces the text you probably wanted to write, cleaning it up and organizing it as you speak."

Now, as an aside, it is really hard to do that cleanup well. For example, I am constantly switching back and forth on Whisperflow from the version where it does light cleanup to the version where it does no cleanup. No cleanup really does look like rambles without good punctuation, and sometimes gets unclear.



but even on the lightest cleanup setting Whisper Flow strips away words that I am using as connectors rather than filler, assuming that they are filler



in any case, for that reason alone, I'm excited to see if Google offers something different here

hereSpaceX AI also dropped Grok Voice Think Fast 2.0, noting that it's now number one on the artificial analysis speech-to-speech index. They write, " "This This index measures whether voice agents can reason over the speech it hears, [00:31:00] resolve real customer issues, and correctly complete tasks using agent tools.

At Starlink," they continue, "we're using Grok Voice to resolve over fifteen thousand inbound customer support and sales calls a day. Grok diagnoses hardware issues, ships replacements, and fulfills over three thousand orders a week via voice calls and chat."



people, a bunch of people showed demos

exploring just how much the speed and latency upgrades really change what you can do with voice in the agentic context

We We also, however, got a new video model from Google as well

The model is called Gemini Omni 1.1 Flash

And And they write that with this update, you can extend your scenes, specify starting and ending frames of a shot, add video input references, upscale your favorite takes to 4K, and test ideas quickly in 360p



In other In other words, this is 100% an update that is not just about, quote-unquote, "better video." it's about massively more usability of video generation in general

Now, once again, we got some new benchmarks. Arena says that Omni 1.1 Flash hit number one in the text-to-video arena and number two in the image-to-video arena. 

although when it comes to a new [00:32:00] video model, the proof is in the pudding

pudding

show, it it seems like people's first impression is that this is indeed an upgrade over the previous Omni model. Choblin writes, " The biggest upgrade is the voice, and it sounds noticeably better, more natural, and it also generates more realistic videos than Omni Flash."

Some found, however, that when they compared it to Seed Dance 2.5

It wasn't as clearly an improvement if it was an improvement at all.

On On the video front, Fall also introduced H3 Max



which they pitched as having better prompt understanding And being just way, way faster They claimed an average latency of three point four nine seconds compared to CDance two point five sixty-eight seconds and Gemini OmniFlash's twenty-six point seven seconds

Justine Moore from Andreessen Horowitz writes, this is an insane model from Fal. I can't describe how wild it feels to generate a long clip in just 15 seconds. This will be transformative for the space."

Adam Holter writes, " Very fuzzy on the detail here, but this generated fast in one point three seconds for twenty cents. That's ridiculous. [00:33:00] H3 Max is a big deal."

Alex, the AI ads guy writes, " writes, H3 Max First impressions. 15-second generation time. Audio is amazing. Voices sound good and sound effects too. Incredibly prompt adherent. It does exactly what you tell it to. Needs more testing, but it's hard to beat the balance and price of H3 Max."

Writes Ethan Mollick, " A line in AI video was crossed. In my experiments with just the web interface, H3 Max can now create reasonably high quality AI video in less time than it takes you to watch it."

it." investor Steve Jang responds, " Yes, the ramifications are super interesting. It opens up live interactive visual environments as a fully generated world. One can have massively multiplayer and completely responsive and unique user experiences With no visible cutting or waiting

Now, for those of you who wanna try H3 Max out You can do it over on venice.ai



Venice is a privacy-focused AI alternative



that recently crossed the threshold of 100 million in ARR suggesting that more privacy conscious AI has a market



So So with all of that, from little quality of life [00:34:00] upgrades to entirely new video generation models, there is a lot of new stuff to go out there and play with. hopefully this episode gave you a few ideas for something you wanna jump in and try.

For now, that's gonna do it for today's AI Daily Brief. Appreciate you listening or watching as always, and until next time, peace. 

​
