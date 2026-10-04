# The AI Challenges Businesses Are Actually Focused On Right Now — Transcript (2026-09-18)

https://aidailybrief.ai/e/2026-09-18 · Listen: https://pod.link/1680633614

<!-- metadata -->
Format: news-analysis · Level: 1 · Length: ~00:30:00
Host: Nathaniel Whittemore
Categories: safety-security, enterprise, open-weights, policy
Featured: Anthropic, OpenAI, open-weight models, recursive self-improvement, Claude, Pacing the Frontier
Also mentioned: GLM, Hugging Face incident, Claude Mythos, GPT-6, Gemini
<!-- /metadata -->

---

[00:00:00] 

It has been a heck of a last couple of weeks when it comes to the AI discussion in society, and yet in all of that, one group that's left trying to figure out if anything has actually changed for them or if they are just on the same path that they were before, is the businesses and enterprises that have been trying to figure out how to maximize AI for their own value for, at this point, a number of years. Today we're discussing both how enterprises are thinking about, if at all, this new era of AI safety, and also digging a little bit deeper to find out what the real concerns that businesses have and the real AI challenges they're facing right now

As always, we're in a moment where new challenges are creating new opportunities as well.

The AI Daily Brief is the daily podcast and video about the most important news and discussions in AI

All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, Blitzy, Robots and Pencils, and Hyperagent. To get an ad-free version of the show, [00:01:00] go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts. And to learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai. 

Welcome back to the AI We are now two weeks into the AI safety discourse absolutely dominating the conversation

For those who think that awareness of these issues had been sorely lacking, it has been a very good period Although now seeing polling numbers that suggest that something like 17% of Americans are completely convinced that AI is going to end humanity

There is certainly some reasonable concern that we might have over-calibrated. holding that discussion aside for a moment

One thing that I think almost everyone is looking for is increasing specificity

that is specificity of policy, but also specificity of monitoring And it's to that that Anthropic speaks with their new proposed set of measurements to help the public understand just how quickly advanced AI is developing.

Once you move past the scariest headlines, this month's safety debate has been largely about recursive 

self-improvement and the idea that [00:02:00] AI development is, A, moving too fast, but B, really about to move much more quickly

The threat of societal destruction makes for a good headline But the AI researchers issuing the warnings have had a difficult time describing exactly what they've seen inside the labs. To better inform the public, Anthropic has proposed a three-axis measurement to understand the current pace of AI development.

The first access is AI's ability to build the next version of itself

The second is Anthropic's ability to oversee and intervene in the actions of agents. And the third is the scale of resources that go intoAI model development. Now, Anthropic explicitly notes that these measurements only look at how models are built In other words, they are measuring only the inputs to model development.

But they argue that these inputs are correlated to the growth in model capabilities

On the first measure, the use of AI models in future model training, Anthropic put together a measure they called the R&D Automation Index training. It seeks to measure every aspect of model training, rate how automated each task currently [00:03:00] is, and aggregate those rankings to express them as a single number

By Anthropic's measure, Claude now, quote, unquote, "leads" 26% of their R&D work and, quote, unquote, "collaborates" on more than 90%. Anthropic's definition of AI-led R&D was tasks where a human provides a high-level goal and the AI completes it end-to-end with human oversight

And here you see the challenge even as they are trying to be precise. they are talking about AI's leading R&D, but that definition of leading still includes the human providing a high-level goal rather than the AI determining the goal, which is what I think some might assume when they hear AI-led R&D For their part, Anthropic was careful to note that, quote, " Claude is not operating fully autonomously for any measured subset of AI R&D work."

Still, they noted that research automation has massively increased since Mythos finished its training run and has continued to ramp in recent months. in March prior to Mythos, only 1% of Anthropic's R&D was led by Mythos boosted this to 12% in May, and it has doubled since then

Regarding oversight of agents, [00:04:00] Anthropic measured coverage, review latency, and escalation rates within their agent oversight systems. They said that around thirty thousand agents are currently doing research and engineering work at any particular time.

Anthropic claims to have one hundred percent coverage of agentic actions for this work, instant AI review of any flagged actions, and around a zero point zero zero two percent escalation rate for real-time review, meaning around one in forty-seven thousand actions are blocked by the monitoring system Anthropic also maintains an after-the-fact review system with 100% coverage.

This system flags around 100,000 agentic transcripts per week that are then parsed for false positives, with around 50 escalated to human review. In other words, around one or two transcripts per thousand cause any material concern.

Finally, on resource allocation, Anthropic expressed their measure in terms of a percentage of overall compute dedicated to safety systems. Around six percent of the compute allocated to AI-assisted R&D went towards safety, and around twelve percent of the compute allocated to AI-led R&D went [00:05:00] towards safety.

Anthropic noted that this measure classifiers that constantly monitor agentic activity and is a, quote, "imperfect proxy for how much a company focuses on safety. This is because safety research consists of individual researchers designing experiments, which is time-consuming, even though running the experiments is not particularly compute intensive."

Overall, Anthropic's goal was not to provide perfect measures. Instead, it was to define and propose a set of metrics that any AI lab could report as part of a regulatory system

They conclude, " As the world considers pacing the frontier, we should do everything possible to minimize the gap between what frontier labs know and what the public knows. This means better measuring the development of AI, reporting on it publicly, and giving society an opportunity to decide how to use this information.



we hope to model that transparency by releasing these measurements and will continue to do so."

Now, the response to this announcement I think shows the good, bad, and difficult of this particular moment

on the one hand, it is the rare move where people on all different sides of the AI safety debate

largely [00:06:00] think that this existing is better than it not existing

AI safety researcher Jeffrey Ladish writes, " Great to see this from Anthropic. A few weeks ago, I wrote that the company could be a lot more transparent, and I appreciate how they've stepped up, both with this and the recent incident investigation report and misuse report."

At the same time, there were plenty of people who also wanted to see more

Prime Intellect's Elie Bakoush writes, " Interesting that OpenAI gives us the breakdown of usage per R&D task andAnthropic gives us automation levels. Would be great to combine both and get the evolution of automation per R&D task



there are also some who argue that the self-reporting, while a fine start, isn't enough. 



Rao writes, " We need standard measures across all labs to measure progress to RSI and publicly report on it weekly to monthly

Now, one discussion that we'll see a lot more of, especially as markets digest all of this

Is that one way, perhaps a cynical way, perhaps a realistic way, 

to look at an increase in safety monitoring is to view it as really expensive overhead for R&D? meaning that these measures of percentage of spend on safety is basically a measurement of that overhead.



will markets [00:07:00] reward companies that spend more on safety? or will they punish them for cutting into their own margins? This shows another complication 

for having these companies operate in a public market environment



for what it's worth, this week also reminded

That recursive self-improvement is notjust the province of the US labs. ZAI released a blog post on Thursday called "Towards Recursive Self-Improvement: How GLM Built Its Own Inference Infrastructure." The first sentence reads, "As we develop GLM

The model sometimes exhibits capabilities that surprise us and even unsettle us The most recent moment that shook us, GLM is increasingly helping build AI itself. We watched the model complete an infrastructure task that would have previously taken a team of experienced infrastructure engineers weeks

When we realized that this work would directly change how the next generation of models is trained, we became even more convinced. Our successors are the AI systems we are creating ourselves



It's certainly beyond the scope of the headlines, but it is a reminder that any slowdown discourse that does not include China is basically no discourse at all

at all Meanwhile, Meanwhile, if I am correct that we have now entered [00:08:00] this new negotiation period for the next generation of AI, where it is no longer just the AI labs that determine our pacing Lots of people are now stepping in



with proposals for what the new overall system might look like Gre- Bridgewater CIO Greg Jensen made headlines this week by suggesting that concentration of power is the major AI risk to be regulated Bridgewater is one of the world's most successful hedge funds and has used AI extensively over recent years.

in an interview with The Information, Jensen discussed his views on where AI risk actually resides and how he would approach regulation. He said, " There's a huge problem with open source models because you can train them. We do this at Bridgewater. It's extremely effective reinforcement learning training on powerful open source models. It's extremely powerful, a great technology, and at the same time, clearly a very dangerous one. You don't know what people are doing with them. There's no way to track that, so it's dangerous from that perspective. We haven't even begun the conversation on how to deal with that issue."

And And yet, in Jensen's view, that risk pales in comparison to the risk posed by the frontier labs themselves. He continued

We have to deal with the [00:09:00] concentration of power. In two years, OpenAI and Anthropic are going to control to 50% of the world's compute. That's a crazy outcome for a society to allow on something as powerful as compute. Would we let one entity control that much of some other form of or commodity?

Now, one of the common observations over the past month has been that the Hugging Face incident and other security breaches like it require immense amounts of resources to power agent swarms. It's unclear that they could be replicated by threat actors outside of the frontier labs, at least with current models, because of limits in their access to compute.

Jensen argued that part of the solution needs to be clear guidance on liability for actions taken by AI so the companies and individuals understand the risks they're taking

When asked how he would deal with the concentration of power, Jensen responded, " We should take anybody that has more than X percent, let's say five percent of the world or US' compute resources, say, 'Okay, those are systemically important institutions.' We're going to put them into some sort of thing like we do with systemically important banks and say there's going to be regulation.

I also think it's [00:10:00] fine to say we're going to have caps on how much you can own. There's a cap on how many commodity futures you can own. There's a cap on much less important things. We may be able to do that with current law. You may need new laws. Either way, let's get going on sorting that out legally.

There should be a bipartisan recognition that you shouldn't want monopolistic control on what I think most people will agree is one of the most important resources in the world."

now now I could spend the next week's worth of episodes 

discussing the implications and challenges of trying to apply GCIB style regulation to existing compute. but what I like about this discourse



Is that not only does it leave behind overly simplistic binaries, it starts to ask questions about where the actual locus of power is

Is the problem in the models or is theproblem in the power to run the models? those have very different intervention points if we're trying to stop bad outcomes, and that's exactly the sort of conversation we need to be having.



Now, Now, one additional dynamic of the safety question that has been playing out is a legal question of whether the labs can actually coordinate on safety or whether that implicates antitrust issues. The Trump administration is reportedly considering an [00:11:00] antitrust carve-out to allow frontier labs to collude on safety

Now, the theory that this deals with is basically that an AI slowdown could mean a coordinated reduction in research spending and therefore an increase in profitability at the expense of the consumer. In the abstract, and in very loose analogy, it would not be dissimilar to if Apple and Samsung agreed to stop working on new phones.

Associate US Attorney General Stanley Woodward said the administration is considering an update to interagency antitrust guidance to provide a carve-out for AI safety coordination. The guidelines already allow for coordination on cybersecurity risks, so a change would extend that guidance to AI safety Interestingly, Woodward said that although multiple AI executives have publicly called for an antitrust carve-out, no one has contacted his office on the matter as of yet.



uh, even without guidance though, Woodward has indicated that the DOJ has no objections to a coordinated slowdown, commenting, " It doesn't occur to me that coordinating on cybersecurity or security is anti-competitive." Europe's antitrust chief, Theresa Ribera, agreed.

Speaking at the same event, she said, "[00:12:00] This is a classic game theory problem. When the risks are shared, cooperation is in everyone's interest."

At the At the same time all of this is happening, there arecertainly still many out there who are trying to tone down the tenor of the conversation in general Legendary AI researcher and Coursera co-founder Andrew Ng, In an interview with Bloomberg TV, dismissed extinction risk as science fiction and warned that AI doomers have pushed this narrative numerous time over the past decade in a bid to gain publicity for their cause and help shape regulation. He said, " I was quite dismayed over the past two weeks. This wave of PR has kicked up again for probably similar purposes."

Andrew acknowledged that there are genuine risks associated with AI, largely around cybersecurity, but said, " This recent fear about AI leading thehuman extinction and so on is much more science fiction than science. It's very damaging." In his view, the dangers posed by AI are, quote, "practical engineering problems," and the industry needs to continue focusing on, quote, "many of the wonderful things it can do

do And And speaking of real here and now cybersecurity issues, Mistral has been hacked for the second time [00:13:00] with their intellectual property now available for purchase on the dark web. In May, around five gigabytes of internal source code and around four hundred and fifty private repos were exfiltrated and offered for sale.

And now it's happened again 

with hackers offering full source code, internal development files, web app code, and additional proprietary information an X user called Benny said that they contacted the seller and confirmed the file dump included model weights, post-training pipelines, and dataset construction.

The hacker was asking $25,000, but deleted their post shortly afterwards, likely either because they found an exclusive buyer or got sloppy with their OPSEC and needed to disappear.

Later in the day, Mistral said that they found no evidence of unauthorized access after a thorough investigation

suggesting perhaps that this is the same material from the May break-in coming up for sale again

again Lastly Lastly today, one model release that went a little under the radar this week was Gemini

3.8 Live Extended Thinking. The model is another live speech model, meaning it can process continuous conversations rather than using a turn-based structure

it topped the artificial analysis speech-to-speech index, beating out [00:14:00] GPT Live 1 Astra and GroqVoice ThinkFast Aside from the smooth conversation style, the model also supports near real-time visual inputs, automatic detection for 97 languages, and handoff for tool calls to allow it to complete tasks in the background

Tim Messerschmitt, a developer relations lead at Google, published a cool tech demo showing, the model powering a Ricci mini robot Tim demonstrated the model's ability to keep up a seamless conversation that weaves between English and German

Speculating about the implications, Greg Isenberg wrote, " Are invisible interfaces coming? Google just announced Gemini 3.8 Live. It can talk through a task with you and then keep working after the conversation ends. I think 90% plus of vertical SaaS will need a voice front door. By that I mean the way you use the software becomes talking to it, and the typing, clicking, and form filling happens on the other side without you

So a contractor standing on a job site just says what went wrong out loud, and by the time he's back in the truck, the quote is sent, inventory is checked, the CRM is updated, the customer got a text, and anything risky is flagged for him. Kinda the dream, right? The same thing works for [00:15:00] nurses, dispatchers, recruiters, brokers, insurance agents, et cetera.

The person talks and the agent finishes the admin. Lots of opportunities here to build voice-first businesses. I think this is how vertical software becomes invisible. Nobody logs in, nobody fills out a form, and nobody learns your interface. You just talk and the work gets done behind you. This is a glimpse of where SaaS is going.

Not fully there yet, but it's coming

long Read, in this weekend's Long Read/Big Think episode, I get a little bit more into this particular shift, as well as a bunch of other shifts in how we use AI. But for now, that's gonna do it for the headlines.

Welcome back to Welcome back to the AI Daily Brief

The background context for today's episode is, of course, the AI safety debate, which has completely broken containment over the last couple of weeks.

And yet, even as we have seen the political resonance of this issue

absolutely explode and polling showing very dynamic, fast-shifting attitudes around it



Enterprises and businesses of all shapes and sizes are still stuck out here figuring out whether it has any real implications for them or whether they just need to keep on keeping on

Today we're looking at some specific answers to that question as well as a few of the broader AI challenges that enterprises and businesses are actually focused on right now

way, certainly the safety debate has found its way 

to the business leader conversation

When the [00:19:00] Wall Street Journal asked for a show of hands at the WSJ Technology Council Summit on Monday, only a few people said that they were worried that AI might kill us all At the same time, around half of attendees said that they were in favor of slowing down frontier AI research and prioritizing better guardrails

my, This sort of comports with my thesis That I shared, I think in last Thursday's big AI safety episode, that while I believe that the markets would view any sort of slowdown as initially a big risk for AI, I actually think that there is a very compelling economic counterargument

that a slower pace of new development 

might actually increase the amount that companies were spending on AI the thesis was basically that the incredible speed and pace of change actually in some ways creates a disincentive forcompanies to try to do comprehensive transformation on the logic that they're gonna spend all this time and energy on transforming into something that isn't even relevant anymore by the time the transformation is complete.

indeed, moving back to the Technology Council Summit, on the panels, the big takeaway was that an AI slowdown actually doesn't really have that many implications [00:20:00] for the way enterprises are using AI right now. Talwar, thepresident of FedEx Dataworks said, " It's in our hands, and it's up to us to apply AI for good, and I think it can do a lot of good for society."

still, the discussion basically still centered around the need for prudent AI governance

around normal business risks rather than the existential risks that are dominating the media discourse

Up north at the Canada Investment Summit, BlackRock CEO Larry Fink was far more worried about the data center backlash than X risk. He warned that construction delays could make AI the, quote, "domain of large firms." Fink added, " The faster we can build out more capacity, the more we can democratize and make it available for everyone."

In the startup world, meanwhile, founders are starting to think about the governance and monitoring tools that businesses will need as agents get more powerful. One venture investor told The Information that they're beginning to focus on startups building tech that improves model security and infrastructure

In other words, private markets are responding to all of this concern 

by 

funding startups that can address specifics around this concern which to me is part of [00:21:00] exactly what you wanna see

Microsoft also tried to bring the AI safety discussion back to some of the broader AI business sovereignty points that they've been trying to make for the past several months

they, this week the company dropped a very extensive 15,000-word code of conduct document

That has, as they put it, a single overriding objective, that humans must retain meaningful control over AI so that it can help people live healthier, happier, and more productive lives

A lot of the discourse around this document was its outright rejection of AI consciousness

And a prohibition of designing AI to even imitate consciousness



but in his post about this on X, Microsoft CEO Satya Nadella

also brought up the implications for businesses themselves, writing, " For firms, it's imperative that they retain full control over their unique and tacit knowledge. Every organization should be able to build its own continuous learning loop and hill climbing machine without becoming dependent on any one model provider, and have the ability to embed its own knowledge into models and weights they control."

Basically, part of this is power concentration in the firms, and a way to deal with power concentration in the firms is to not [00:22:00] surrender power to the firms in the form of your unique and proprietary data

Now Now meanwhile, outside of the AI safety conversation

there had started to be some debate

about AI market signals in the form of enterprise spend. On September ninth, Ramp released its latest AI index that found that AI spend declined among the top 1% of businesses spending on AI In August, wrote Ramp lead economist Eric Carrezziin, the top 1% of businesses $7,200 per employee per month, which was down 10% from a July peak of $8,000.

about-- Now we've Now we've talked a lot about the limits of Ramp data. Ramp has a very, very highly concentrated tech-forward early adopter type of audience. It is also pushing products that are specifically about cost efficiency. but of course, when you take all those caveats, it still provides an interesting and important signal Now, when it comes to their analysis in this particular area, I personally think that they are underestimating summer seasonality 

as 

a driving force

But their take is that this is about the most sophisticated AI users getting more adept at complex model architectures that don't rely on the most expensive [00:23:00] models at all times Era wrote, " My take is that it's not because of Chinese open models, it's model wars.

Price cuts plus a growing share of spend is shifting to standard and light models which are already cheaper over the frontier."

and revi- Now, speaking of Ramp not necessarily having exactly the right analysis all the time, even though their data is really valuable, while they had

previously caused a bunch of frantic headlines when they showed that businesses weren't adopting Fable arguing all sorts of reasoning for that besides the obvious one which is data retention policies

But to their credit in more recent reporting

They found that Fable 5.1, which got rid of the data retention requirements 

had started to make up twenty-two point five percent of enterprise spend and was rising very quickly

But what about overall?

On On September 10th, Box's Aaron Levie wrote a long post on X

about the issues that he was hearing about from executives across industries including banking, media, information services, and insurance when thinking about AI and agents in the enterprise

the big trends that Aaron heard about were cyber Model battles agent security and identity, process re-engineering

architecture adjustment, evals, [00:24:00] and the hurdle of legacy systems

On On cyber and security, he wrote, " Everyone is nervous about the growing rate of vulnerabilities coming at them from AI and the implications of the OpenAI Hugging Face incident. The conversation is not as existential as it is in Silicon Valley, but still highly concerned and pragmatic about what to do about it operationally in their environments.

Lots of new discoveries due to AI and still hard to keep up with all the changes they have to execute now."

Adding in what he wrote about agent security, he continues, " Somewhat tied to Hugging Face, there's much more awareness to the new challenges around agent security and identity management in a world where agents are trying to get into every system they can. In a perfect world, enterprises could set up identities for all their agents and control what they're doing, but of course, sometimes the agent needs to act exactly as the user as well."

lot is-- This is certainly something that we've seen a lot in our conversations, in the podcast context as well as 

Superintelligent.

And interestingly, a lot of the security concerns aren't just about malicious actors. It is to some extent rooted in just the general power of these systems 



now that it's not just engineers who have access to agents, many companies are finding that the agents are powerful enough that [00:25:00] they escape the containment of the non-engineers that are using them, even ifthose non-engineers aren't trying to do anything problematic

This is also showing up in the numbers. once again, looking at ramp data Lead economist Eric Karazian writes, " One area companies are increasing their spend is AI security software. In the wake of the Hugging Face hack, three of our trending software vendors make software specifically designed to monitor agents in production."

that it's-- Now, he did point out that these specific vendors might not have done anything to stop the Hugging Face hack, but it's clearly a category of focus For business buyers as well as startup builders

Another interesting area that Aaron talks about is the nascent exploration of open source and alternative model architectures

He wrote, " Most companies are deploying multiple frontier models withinwithin their enterprise. Too hard to standardize on anything And seeing different preferences across their teams and use cases. But the dollars are still concentrated on just a few vendors. Open weight's still in infancy at scale in most of these organizations, often due to lack of domestic frontier open source options.

Plenty of appetite for more options here, but so far, few places to go

[00:26:00] Now paired with that, I think, is Aaron'sobservation that there is a ruthless adjusting of architectures. " Most companies," he wrote, "had examples of changing systems out multiple times just in the past year or two with different vendors. I probably haven't heard, 'We tried X and it didn't work, so have gone with Y,' more than in today's environment.

The lesson here is that because innovation is happening so fast, no one hangs around until a vendor gets something right. They just move on to the next one."

re- now I think this sets really interesting context for watching some of the competitive dynamics right now around how different types of actors are trying to appeal to different types of businesses

Labs like OpenAI and Anthropic are clearly trying to keep everything consolidated in their own environment. Part of that, especially for OpenAI, has been a real focus on cheaper models and pushing the price of their models down as far as they possibly can. That's something we've seen a lot over the past couple of weeks.



but they also are, as they have been all year, focused on vertical solutions, such as the newly launched Astra for Law from OpenAI

alongside the Astra for Law launch, OpenAI and law firm Cooley also co-launched a product that they called Go Public that's [00:27:00] designed to draft S1 filings, which are the documents that companies must submit to the SEC before they can go public

And yet, as if to give us a perfect comparison of the different types of options that different companies are taking

Another law firm, and Watkins was recently reported to be buying Nvidia servers to set up their own in-house systems, specifically as an alternative to models from OpenAI and Anthropic Latham, which is the US's second largest law firm

said, quote, sometimes we may have information that is so sensitive, client information that we really wanna protect, we don't wanna put it on any cloud vendor

seeming seeming to make the point thatone of the ways that enterprises can stay out of the fray of the AIsafety discourse isto own their own models.

Mistral CEO Arthur Mensch posted

Don't pace building and owning your own AI models and systems as an enterprise, and there will be no doomsday for you

Foundation Capital's Jaya Gupta Also thinks that this pacing the frontier moment could be a good one for the software incumbents

She wrote, " If you're the CEO of any software company and you're not offering open weight models as a SKU right now, you're asleep. Pace the frontier may be the greatest invitation [00:28:00] software incumbents have ever gotten. While the labs debate how quickly intelligence should advance, software companies should be racing to commoditize the intelligence we already have.

Pharma and banks are already picking up open weight models partly for margins, partly because a revocable lab API is a dependency they increasingly don't want. AI natives and tech companies that care about cost of goods sold are doing the same. Most software companies that tried had failed attempts because the open weight models sucked.

But now open weight models are good enough. I believe that every major software company should become a model factory for its own vertical. Own the evals, post-train open weights on the workload it uniquely sees, serve those models to its customers, and use production feedback to continuously improve them."

And And so on the one hand, to some extent the response from businesses to the AI safety discussion seems to be business as usual. a-- The pace and challenges of adoption within the enterprise were always unique and distinct to them And the challenges of big institutional inertia that comes with them

But on the other, there are some ways that the conversation is reinforcing trend lines that were already starting

companies will needto spend more time and [00:29:00] resources on cyber and security issues that was always coming, but the point has been made even more crisply now

r-- and while already there were some compelling reasons to explore and consider

Open weights are more owned model alternatives to just getting in bed with the big vendors

There are now even more reasons to be willing to walk down that path

not least of which is the increasing likelihood of regulatory disruption

I think that if I had to summarize my advice In a single thought it's that while overall the changing AI safety discourse doesn't really impact the short term for enterprises, it certainly reinforces the fact that the companies that are willing to try the hardest things

like actually investing in their own owned architectures have even more potential to differentiate from their peers and competitors than they did before. I will, of course, continue to watch these trends as they evolve, but for now, that's gonna do it for today's AI Daily Brief.

Appreciate you listening or watching as always, and until next time, peace. 

​ 

[00:30:00]
