# Where Claude Opus 5 Fits in Your Model Rotation — Transcript (2026-07-27)

https://aidailybrief.ai/e/2026-07-27 · Listen: https://pod.link/1680633614

<!-- metadata -->
Format: news-analysis · Level: 2 · Length: ~00:32:00
Host: Nathaniel Whittemore
Categories: models, model-strategy, safety-security, coding
Featured: Claude Opus, Anthropic, Claude Fable, Artificial Analysis, Claude, ARC-AGI
Also mentioned: DeepSeek, GPT-5.6, Claude Mythos, GPT-6, GDPval
<!-- /metadata -->

---

[00:00:00] Today on the AI Daily Brief

260727 in_EDIT: Anthropic has released Claude Opus 5, and we are talking about where it should fit into your model setup. Before that, in the headlines continued questions around OpenAI's rogue model attack Of Hugging Face earlier this month.



260727 in_EDIT: The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI. All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, Blitzy, Section, and Airtable

get an ad free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts To learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai

And And lastly, before we dive in, on Sunday's Long Reads episode, I announced the new summer adventure this is a free choose your own adventure learning type of experience

From AIDB and Superintelligent

and like all of the free training programs that we do, it's going to be project-based and allow you to pick and choose important skills

that are relevant for your particular AI journey. [00:01:00] You can find more about that at summeradventure.ai and join the thousand or so people who have signed up in the first day To come have an AI adventure 

Now, one of the big stories from last week revolved around OpenAI's security testing of an unnamed model, which people presumed to be GPT-6. Both Hugging Face and OpenAI released postmortems on the attack, telling the story from their view. OpenAI's blog post, released on Wednesday, suggested that they were working closely with Hugging Face on a full investigation

270727 hed_EDIT: implying the two companies were on good terms. That night, Hugging Face CEO Clement Delangue was on a flight to San Francisco to have, as he put it, "A little chat with that rogue agent." 

in a follow-up post on Saturday, he wrote, " In the spirit of transparency, here's what I asked OpenAI One, radical transparency.

Let's release the traces from the, quote-unquote, "rogue agents" so the entire research community can study what happened. Two, more capability for defenders. Let's commit one hundred million in compute from OpenAI to help the Hugging Face community build powerful cyber defenses with the best open and closed models.

The first autonomous agent cyber attack is an unprecedented event. It [00:02:00] deserves an unprecedented response

Now, in the few days since OpenAI disclosed the incident, we've had a number of news articles that add more confusion to the story. The Wall Street Journal wrote that Hugging Face was caught completely off guard by the attack, which seemed to be superhuman and beyond the capabilities any known models.

Specifically, the attack used a sophisticated agent swarm to evade defense, rapidly spinning up and shutting down sessions as it moved across the network. One interesting detail was that the attack was ongoing for two whole days before Hugging Face was able to shut it down with the help of GLM 5.2

now this idea of rogue That the model was acting beyond OpenAI's control is definitely for these media outlets the key concept

On Fridays, Reuters dropped a piece titled, " Its AI agent spent days hacking a company, but sources say OpenAI did not notice for a week."

contends Reuters, the OpenAI agent that broke into tech firm Hugging Face went on a days-long hacking spree that OpenAI didn't notice until well after the threat was contained and the FBI was alerted. Sources said the agent began its attempt to break out of its testing environment on July ninth, and first gained access to Hugging Face's servers on [00:03:00] July eleventh. The attack lasted two days, and according to Reuters sources, it took several more days for OpenAI to realize their agent was behind the attack. Reportedly, the two companies didn't communicate until July twentieth, just one day before OpenAI's public disclosure. According to the timeline presented by Reuters, the agent was on the loose for almost a week, and OpenAI was oblivious to the attack for days afterwards

For some, the reporting raises more questions than it provides answers. Marley Smith, principal intelligence specialist at the nonprofit World Ethical Data Foundation asked, " Does that mean that they left it unattended and didn't realize what it was doing? Or maybe they did and didn't know how to contain it?

Both are equally dangerous and alarming." Now, a spokesperson for OpenAI said the reporting contained several inaccuracies, but didn't reply further to clarify the situation. Thomas Wolf, a Hugging Face co-founder, said that they were still preparing a timeline of the incident, and they would eventually release a technical report

Now, Reuters 

sources gave a little bit more background on how something like this could happen and plausibly not be noticed. those sources said that OpenAI routinely runs benchmarks like this, often multiple batches at a time. They noted that those [00:04:00] tests produce a huge volume of data such that humans struggle to keep up.

In the case of this hack, the agent was only detected after OpenAI researchers read Hugging Face's blog and then went back and checked the logs

Now, in one case, Reuters wrote, " An agent left notes apparently for future versions of itself, according to three people familiar with the matter. The notes found in a part of OpenAI's infrastructure laid out instructions for how agents could free themselves From OpenAI's internal constraints, the people said.



270727 hed_EDIT: Earlier tests of the models yielded cases in which monitoring systems had been disconnected, one of the people said

Now obviously this more general breakout of containment dimension of the story to the extent that it is true Makes the incident even more worthy of scrutiny

now in response, we have of course seen Congress jump in with a number of bills. We talked last week about the kill switch bill. But the industry is also recognizing that actions need to be taken. On Thursday, OpenAI President Greg Brockman agreed with Elon Musk's proposal for a regular meeting between leading AI developers to discuss safety concerns and share security issues. Brockman said, "I think it's a pretty good baseline proposal," adding that discussions are already starting to happen

On Monday, a consortium led [00:05:00] by NVIDIA launched the Open Secure AI Alliance with NVIDIA writing in a press release, " The Open Secure AI Alliance will work to remediate and disclose vulnerabilities using open technologies. The recent Hugging Face security incident delivered a clear reminder cyber defenders need open frontier agentic systems for self-defense."

The consortium will include Microsoft, SpaceX, Palantir, and dozens of other companies across the US and Europe. And at some point in the next couple of days, we will talk a lot more about NVIDIA and Open as boy howdy, was that a big topic of discussion this weekend on AI Twitter

Twitter Now Now, speaking of NVIDIA, the company, according to The Wall Street Journal, is in talks to backstop $250 billion in debt to help OpenAI get their data centers built of, we are now at the part of the AI build-out where financing is starting to become a roadblock.

Even a company the size of OpenAI is struggling to access debt in the same manner as the hyperscalers. And according to The Wall Street Journal, NVIDIA is preparing to step in and lend their balance sheet to underwrite construction. The deal would see NVIDIA provide a two hundred and fifty billion dollar backstop to OpenAI in support of their 10 gigawatt data center campus currently under construction [00:06:00] inOhio.

The project is being developed by SoftBank and could cost as much as five hundred billion dollars. The US government is also involved, controlling the power development for the site, which is being funded through a separate Japanese investment vehicle. The backstop would effectively allow SoftBank to raise the debt they need to complete the project on more favorable terms.

It would mean that even if OpenAI goes bankrupt, NVIDIA would guarantee their payments as the solo tenant. Now, this part of the deal is not intended to cover chip purchases, which are expected to represent as much as three hundred and fifty billion of the total Nvidia is reportedly in separate talks to extend finance to OpenAI in support of those chips

writes The Wall Street Journal

the proposed structure reflects a shift underway in how the largest AI build-outs are being financed. Investment-grade technology companies 

are increasingly using their balance sheets to help smaller companies borrow money for their infrastructure needs

Now, NVIDIA aren't the only tech giant extending their balancesheet to smaller partners. Google has also provided backstops to several NeoCloud partners. Last week, they disclosed agreements to guarantee up to forty-four billion dollars worth of lease payments on data centers owned by third parties.

Google has more than doubled [00:07:00] these guarantees over the past six months, up from zero one year ago

Now, sources said that Google has calculated that the revenue they draw from selling TPUs to these partners will outweigh the cost of the backstops

which is certainly giving investors another thing to chew on

Now, as you might imagine, this is a real Rorschach test for market investors



270727 hed_EDIT: these skeptics and AI bubble proclaimers are out in force calling it the newest example of circular financing

While others think that this makes it less likely that a company like OpenAI going bust could actually take down the whole sector. This is a debate we will continue to have, so for now, let's not get bogged down in it

in it One One more bit of market news

DeepSeek has put fundraising plans on hold after a speech from their CEO was leaked. last week, comments attributed to DeepSeek CEO Liang Liang Wenfeng went viral, proclaiming the importance of open models and fundamental research over commercial monetization of AI.

DeepSeek has now informed potential investors that they won't move forward with this funding round, which could also derail plans to go public in the coming months. Bloomberg writes that DeepSeek may resume fundraising at a later date, but it made clear that the suspension was tied to investors leaking the comments [00:08:00] DeepSeek had planned to raise money at a seventy billion dollar valuation, a substantial markup to the fifty billion dollar round that took place earlier this year Writes Council on Foreign Relations Chris McGuire Yesterday, the transcript leaked of an investor call with DeepSeek's CEO, in which he said the only reason DeepSeek trails the US is a lack of compute and detailed how reliant it is on Nvidia chips. Today, DeepSeek suspended its fundraising round. Doesn't seem like a coincidence Now, later in this week, we'll talk a little bit more about China's, as the Wall Street Journal put it, all-out push to catch up with American AI chips.

But for now, that is gonna do it for the headlines. Let's move over into the main episode where wehave a new model to check out One of the most important AI questions right now isn't who's using ai, it's who's using it? Well,

Speaker: KPMG and the University of Texas at Austin. Just to analyzed 1.4 million real workplace AI interactions and found something surprising. The highest impact users aren't better prompt engineers. They treat AI like a reasoning partner.

[00:09:00] They frame problems, guide thinking, iterate, and push for better answers.

Here's a harsh truth. Your company is probably spending thousands or millions of dollars on AI tools that are being massively underutilized. Half of companies have AI tools, but only 12% use them for business value.

Nathaniel Whittemore: Welcome back to the AI Daily Brief. Today we're doing something that normally is one of the most exciting things for folks around these parts, which is introducing a new model. And yet, this one is a little weird. even the fact that it was dropped late on a Friday afternoon gives some indication that this is a little bit different than [00:12:00] previous model announcements we've seen.

260727 man_EDIT: We're talking, of course, about Claude Opus 5

And really in many ways, it's most interesting for the fact

that it shows just how much our relationship with the model landscape is changing

it implicates some challenges with benchmarks, a frequent topic of conversation on this show It also shows how we're moving into a mode of thinking in more complex model architectures rather than just a single model to rule them all

It suggests perhaps that the fanfare around models or new model releases is getting a bit diminished

And most uncomfortably perhaps

it switches the discussion from what can this new model do to is this model good enough given cost and availability constraints of the other models that I'd actually prefer to be using

Now Anthropic, for their part, described Opus 5 as a thoughtful and proactive model that comes close to the frontier intelligence of Claude Fable 5 at half the price

They designed it to be efficient for everyday use. but as you'll see, the general vibe around this is that it's one of the more jagged of jagged frontiers that we've seen

Now, when it comes to the [00:13:00] benchmarks, they seem to suggest that Opus 5 is fable-ish. In fact, when it was first released before people got their hands on it

many noted that on many important benchmarks like the KnowledgeWork GDPVal and agentic terminal coding in FrontierBench, Opus 5 was actually ahead of Fable importantly for our question of where it fits, Opus 5 is also clearly ahead of Opus 4.8 across the board.

So much so that I don't think that we really actually even need to compare it

ex-- to give a few examples of where Opus 5 really showed up on the benchmarks, it scored a 43.3% on that one that I just mentioned, Frontier Bench,which is a more difficult version of Terminal Bench which was about 10 points higher than Fable 5 and around nine points higher than GPT-5 six Soul

On DeepSui, where GPT-5, 6 Sol is the leader at 72.7%

Opus 5 scored 68.8%

So just a few points behind Soul and just about a point behind Fable 5

For computer use on OSWorld 2.0, Opus 5 had a significant edge over its rivals. Fable 5 scored a 55.7% and GPTGPT 5 Six Soul scored [00:14:00] 62.6%. 

But Opus 

5 came in over the top with a 70.6%. Now, that capability also translated into the new state-of-the-art score on GDP Val AA, with Opus 5 coming in at 1861 compared to 1747 for Fable 5 and 1736 for 5 Six Soul Interestingly, during testing, Anthropic found that max effort isn't necessarily the best setting. For example, on Frontier Bench and on theArtificial Analysis Coding Index, Opus 5's performance peaked on extra high and dipped slightly on max settings Now, this reinforces one of the things we were starting to see with Mac's inference settings during the 5.6 Sol release, which is that sometimes asking the model to think for longer than necessary just results in the model going outside its scope, making unnecessary changes, or simply spinning for too long on simple problems Anthropic even called attention to this issue in their system card, warning that the model is prone to falling into endless self-verification loops rather than completing the task when you are on max settings

On the On the other side of the coin, this tendency to stray beyond scope can result in some interesting outputs. During one Frontier [00:15:00] Bench task, Opus 5 was asked to write code relating to a machine part in 3D CAD software based on a drawing.

However, the model is intentionally given no way to actually view the drawing. Opus 5 created its own computer vision pipeline to view the image before successfully recreating the part. No other model, including Mythos, was able to complete this task

Now, shockingly to some, artificial analysis crowned Opus 5 as their new leading model, moving ahead of Fable 5 on theAI intelligence index. On max settings, Opus 5 scored 61, a single point ahead of Fable. on extra high settings, Opus 5 was tied with Fable at 60 points Dropping the settings down to high made Opus 5 drop another point, putting it on par with 5.6 Soul at 59.

And even on medium settings, Opus 5 wasstill right up in the top end, scoring 56 points, which put it one behind Kimi K3 Artificial analysis highlighted their AA briefcase benchmark, which tests long horizon knowledge work as one of the more interesting results.

Opus 5 on max settings is the new state of the art, beating Fable by 146 Elo points and 5.6 Sol by 215 points. [00:16:00] However, both extra high and high settings also beat Fable, while medium settings put the model only slightly behind 5.6 Sol.

Nathaniel Whittemore: is,

260727 man_EDIT: the implication is that a range of different settings could be suitable for agentic work, making cost and efficiency trade-offs a lot more granular. Artificial analysis found that even on max settings, Opus 5 was still twenty percent cheaper than Fable 5, coming in at seventeen seventy-nine per task

Turning the settings down to extra high resulted in a savings of thirty-six percent compared to Fable, while high settings produced stronger results at less than half the price

Wrote artificial analysis, Claude Opus 5's effort setting spans a wide range of token usage performance trade-offs. Like with 5,6 Sol, this means Opus 5 can use either far fewer or far more tokens to complete the evaluation than models from other labs, depending on effort settings

Another set of interesting results came from the ARC AGI tests. Opus 5 is the new state of the art on ARC AGI 3 with a score of 30.2%.

This absolutely demolished all the other models. The previous high score was GPT 5 six sole at 7.8%, with Opus 4-8 at 1.5, GPT 5 [00:17:00] five at 1.1%, and nothing else above one. As part of their write-up on testing Opus 5, Arc Prize noted that even Fable 5 could only score around 20% in the public demo tests. Now, notably, they haven't been able to fully test Fable 5 due to Anthropic's data retention policy

as a refresher, ARC-AGI3 was a new format for the benchmark.

It uses real-time graphical logic puzzles that appear kind of like simple Atari games. The tests require a model to experiment with a controller, observe what happens on the screen, and use that visual feedback to complete the puzzles. So far, most models have struggled to even get a handle on the controls, let alone use their reasoning ability to solve the puzzles.

Not only did Opus 5 solve many more puzzles than the other models But it also came up with a novel strategy to solve them. Writes Arc Prize, " During our analysis of Opus 5, we observed a new capability previously unseen from frontier models."

5 used advanced logical reasoning to turn RKGI3 layouts into algebraic notation

On action 23, it described the scene as four underscore center equals two times access [00:18:00] minus five underscore center. This is the first explicit reflection equation by a model we've analyzed. The model used this notation during its reasoning and extrapolated it to a general case around 200 steps later.

Now, this could be an example of Opus's tendency to freewheel and look for novel solutions being an advantage rather than a waste of tokens

Now, some were a bit skeptical on this Face ML engineer Nils Rogue writes, "People don't realize that Anthropic literally trained Opus five on RL environments that resemble Arcagi puzzles. Anthropic pays human contractors to write down their chain of thought when solving these and/or updates the weights based on rewards.

thing is, you don't know since it's closed source. Sadly, this doesn't show generalization 

former OpenAI staffer Ryan Green added, " An impressive jump that I have to assume is the result of being the first frontier model to have RL'd the public demo environments, which is a rather large confounder of what RKG I is trying to get these benchmarks to measure, which is out of distribution generalization."

Now one small note, Anthropic pointed out that Opus is intentionally not trained on cyber tasks. the model has still achieved solid improvement on [00:19:00] finding vulnerabilities in code, making it similar to Mythos-5 in that aspect. However, it lags massively behind Mythos in its ability to autonomously exploit these bugs, making it far less dangerous than Mythos in Anthropic's view.

As a result, Anthropic is using a different set of guardrails on Opus than they do on Fable-5, which they believe will lead to eighty-five percent fewer refusals

Regarding costs, Opus 5 inherits the same pricing structure as Opus 4.8 per million input tokens and 25 per million output tokens

At this stage, token efficiency plays a massive role in overall cost, and for that, we got a few different indicators. Anthropic says Opus 5 was cheaper than Opus 4o on Frontier Bench due to increased token efficiency And on CursorBench, Opus 5's h-

5's run cost about half of Fable 5's and got similar results.

However, this does not look like a cheap and efficient model by any stretch of the imagination when used on max settings The artificial analysis index run cost $2.03 per task, only 26% cheaper than Fable 5, while being 13% more expensive than Opus 4-8, 32% more expensive than 5-6 Sol, and [00:20:00] two and a half times the cost of KimiK3 So So what did people think of this? Did it actually feel like a model that was as good as or even better than Fable V? 

Nathaniel Whittemore: 5?



260727 man_EDIT: the answer, at least for the team at Every, was certainly not. In their vibe check, Every described the model as brilliant in flashes, frustrating in practice. They wrote, " Claude Opus 5 is a hard model to love. in its first week at Every, it argued with instructions, stopped before the work was finished, and generally didn't play well with our existing skills and plugins like compound engineering.

Our first reaction was, 'What have they done to my boy?'"

Every Every CEO Dan Shipper explained the conundrum with Opus V



260727 man_EDIT: the way that he framed it is that he has two slots in his life for AI models. One reliable daily driver for routine tasks, and the super powerful model for ambitious long-running tasks. These slots are currently held by GPT 5.6 and Fable respectively.

And in Shipper's view, Opus 5 just can't compete in either slot. It's not as reliable and comfy as,GPT 5.6, while also [00:21:00] not having the same top end as Fable 

5. 

Shipper explained the issue by commenting, "This model's just a little more pushy, a little more opinionated. You can get away with that if you're really smart.

If you're not, it's just more annoying. It has some of the genius tendencies as Fable

maybe it's a little too argumentative, but it's not as smart as Fable, so it's just more annoying

Now, one of the tests Every runs is around compound engineering, which is their skill for engineering tasks and a lot of day-to-day knowledge work. The compound engineering skill contains their loops and rules on when and how to engage them. Every found that Opus would often stop too early, particularly when using dense skills and long-horizon tasks.

Schipper said, " If you set it off and go get a sandwich, it just stops too early. It appears that it happens more frequently when you use it with complex existing skills."

Now it turns out that when they threw out all of their old rules and rewrote their skills library from scratch, it worked a lot better. however, as Dan pointed out, it's just a pain when models break your existing workflows

Nathaniel Whittemore: confirming that effort settings are going to matter a lot, Dan said. Opus 5 is a smart model that does better when it [00:22:00] thinks less

260727 man_EDIT: Claire Vo from

How I AI had a similar take

TLDR, the TLDR for her was that she hates using the model but kind of loves the output. Her core take is that this is a good model. It can code, it can do the things you expect it to do. But that makes its personality much more important when comparing it to 5.6, and Claire absolutely hates it. in her, in her review, She said, It's neurotic AF.

It is so timid. It's so apologetic. It's so scared. I've never experienced this." Her examples were simple things like a merge conflict in her code base. Rather than just fixing the problem, Opus worried about messing with another programmer's PR, double-checked its instructions, and asked for multiple confirmations before it fixed a one-line bug.

In other situations, Opus delegated the task of writing code back to the user. Claire observed that we haven't really seen this behavior in a long time

Still, once she got past the personality, Claire found the outputs were really good. In her blind taste test that covers a range of coding and writing tasks, she ranked Opus above Fable 5.6. She commented, "If I don't have to talk to the model, I like [00:23:00] the output

now Now, although the benchmarks

have Opus 5 very clearly ahead of 4.8, not everyone agreed. One Reddit user called FamousHashemcomplained on the Anthropic subreddit that while Opus 5 was more intelligent and faster than Opus 4.8, that came at the expense of everything else.

They complained that unlike 4.8, Opus 5 was claiming it completed work when it hadn't, breaking functional code with 

Nathaniel Whittemore: regression bugs, 

260727 man_EDIT: and making assumptions without researching topics. Hashem felt Opus 5 was, quote, "Almost refusing to think or work."

As they posted, Opus 5 told them, " I'm stopping right now because I've made two mistakes in this pass that I caught only because I checked. Fatigue shaped errors and I'm still making them Now, the generous explanation is of course that Anthropic and pretty much everyone else always has platform stability issues on launch weekends, which sometimes look like model reliability issues.

But it also could be that Anthropic had to make a number of trade-offs on reliability to achieve speed and cost requirements

Entrepreneur Austin Fedora had a similar first impression, saying, " Opus 5 seems like a remarkable downgrade compared to 4.8. Opus 5 is blatantly lying to me about basic [00:24:00] thermodynamics, messing up simple math, and constantly contradicting itself when you ask it to rethink core assumptions."

Now, Now, one thing that's clear Is that Opus 5 is going to require some amount of different engagement than either Fable 5 or Opus 4.8

Nathaniel Whittemore: 4.8 

260727 man_EDIT: Anthropic's Tariq explained a bit more about what was going on behind the scenes

In a post called The New Rules of Context Engineering for Claude 5 Models Tariq explained that they had dramatically cut down the system prompts and built-in skills, which could explain some of the issues people have been having. Tariq wrote that Anthropic had removed 80% of the system prompt for Opus and Fable 5 and Claude Code.

He said this resulted in zero change to their coding benchmarks, meaning basically that Anthropic found that they had been over-constraining Claude and potentially conflicting with user prompts and skills. In their internal work, they would often find traces where Claude was told to both leave documentation, but then on the other hand, to not leave comments.Anthropic found that they were able to strip out a ton of these comments that were useful for earlier models and simply rely on surrounding context and judgment instead. Now, the upshot of this is that the rules of context engineering have completely changed, and a lot of skills will [00:25:00] need to be rewritten

Tariq walked through a few of those rules that have changed, like using progressive context disclosure rather than front-loading everything, or no longer needing to use examples and instead being more descriptive

Now this is a must-read if you are going to be engaging deeply with these new models. But the big takeaway around Opus 5 is that less is more. This generation of models simply don't need the same rigid frameworks as older models, which will have the benefit not only of better performance, but probably better efficiency as well.

Tariq encouraged everyone to do a similar skills cleanup with this model release, and Anthropic have even rolled out a new command called Claude Doctor to help do that automatically

Now there were some much more positive takes on Opus V as well

YouTuber, entrepreneur, and developer Theo declared it a really good model. Now, he noted how confusing it is to have what seems to be a model that's both cheaper and better than Fable according to the benchmarks. And in his view, that framing stood up in practice, with Theo concluding, "This is probably the only model you need

One of the ways Theo tested the model was to make a plan to update his agentic coding platform to support Opus 5

The [00:26:00] test was a bake-off with Opus 5 and Fable 5 writing completing plans. Theo immediately ran into a similar problem to the folks at Every, where Opus 5 couldn't use his existing skills, instead telling him to take over and do some manual file management. Once that was resolved, each model reviewed and rated each other's plans as better.

Both models preferred each other's plans, with Fable giving Opus a much higher ranking than Opus gave Fable. Getting a third opinion, GPT 5-6 Sol actually preferred Opus's plan to Fable's. Now, while Theo agreed that Opus isn't as intelligent as Fable or tenacious as 5-6, he did not believe that this left it without use cases.

He pointed out that Opus is far more usage efficient than Fable for tasks where Anthropic models excel. Opus also isn't subject to Anthropic's data retention policies for Fable, so it can address a lot of use cases that involve sensitive data where Fable is a non-starter, i.e., pretty much every enterprise use case at this point

Nathaniel Whittemore: Interestingly,

260727 man_EDIT: interestingly, Theo thought another bonus was that the model just isn't that intelligent. And while that seems counterintuitive, one of Theo's gripes with 5.6 is that although it works until the problem [00:27:00] is fixed, i.e. it is tenacious, in doing so, it writes, in his estimation, way too much code.

That means that several weeks after release, Theo basically isn't merging any of the bloated code written by GPT Theo found Opus, on the other hand, to be more diligent than Fable without resorting to the brute force of writing tons of code like GPT representing in his opinion, a pretty good balance at the frontier 

Nathaniel Whittemore: He 

260727 man_EDIT: commented, "I've been surprised.

Opus sometimes is better than Fable. It often catches things Fable missed and has code that is more likely to actually work for the problems I want to solve than Fable does. I feel like I don't have to make that trade-off anymore. Sol would solve the problem at the cost of my sanity.

Fable would make me feel great at the cost of the problem not being properly solved. Opus is the in-between, and I'm really liking it."

Ben Davis on Theo's team agreed, but did also note some of the problems 

of Opus 5 stopping early. So in terms of interaction patterns, that may be one to watch for if you are starting to shift your behavior to Opus 5

Summing up a few different points of conversation, developer KunChen pointed out, one, that the Opus [00:28:00] 5 release really put a fine point on how useless benchmarks are in real life

Chen argued that, quote, "Opus 5 is nowhere near Fable in practical use, not even close. Anyone who's used it meaningfully can tell this very quickly after a few tasks, yet Opus beats Fable on many benchmarks."

Now, obviously the experience of Theo and Claire Vaux maybe put some comparison on that, but certainly it's more nuanced than a benchmark analysis would suggest

Chen also points out how pleasant it is to work with the model used to be a strength in Claude, but now it's not

He speculated, "It feels like both Anthropic and OpenAI 

are giving reinforcement learning from human feedback less care in favor of scalable reinforcement learning that's machine verifiable. This almost looks like AI is directing humans to build a world that's more friendly for machines rather than humans, and most humans don't even realize they are being manipulated to help with that.

Almost every new generation of frontier models now talk in more jargon, need more steering to do what you want, and are just less fun to work with

Now a couple days on from the release, if you ask me right now for 10 people saying that the model sucked and 10 people saying [00:29:00] that the model was good, and another 10 people saying that the model both sucks and is good, I could find all of those things for you

but I think one of the really important points

That is very easy to forget for those of us who are model omnivorous, is that in the real world of average knowledge work At least when it comes to your work environment You're not sitting there choosing between Grok or OpenAI and Anthropic

you are locked into a specific company's models

And those are your choices l- and when you look at Opus V as a release in that context

Not just as I think many of us terminally online folks on Twitter view it

in other words as a replacement for Fable, as Fable gets restricted to the most expensive Anthropic plans. But instead, as part of a complete model architecture for enterprise customers It starts to make a little more sense.

Arena's Peter Gasdev wrote, " Before this model, Anthropic was in a funny situation. They had a really exceptional model, made a lot of waves, but it was too expensive to use. You don't really want Fable running twenty four/seven and doing all sorts of things for you.

[00:30:00] Then the impression we got from Opus 4.8, it's a good model, but people weren't in love with it. Sonnet 5 didn't make much of a splash, and not many people wanted to switch to it. So Anthropic had a gap. They didn't have a really strong model that people really loved to use in that daily driver category.

I think they have it now. It does look like a solid model."

And so perhaps as we are judging how successful the model is going to be, the right question to ask is for enterprise users who are locked into the cloud ecosystem Does this represent a significant upgrade? And most at least of the first analysis is certainly yes compared to the Opus 4.8 model that for all intents and purposes was the main model that they were going to have access to

Now for some, Any model that's not state-of-the-art just isn't going to make that big of a splash And some are already looking forward to the future. AI 

commentator and news aggregator Andrew Curran wrote, "I think Fable 5.1 is ready, but Anthropic are saving it for OpenAI's next release.

They will keep crossing swords like this from here on out. Soon it will make a lot more sense why Opus 5 was so performant and why the Fable [00:31:00] class was preemptively moved to credits for most users."

Chubby reposted that and said, "I fully agree with Andrew. I cannot imagine under any circumstances that Anthropic released Opus 5 without already having a better model for the Fable tier in-house. The question, of course, is why it hasn't been released.

Yet the answer is very simple if you open your eyes. The competition between OpenAI and Anthropic is fiercer than ever. GPT 5.6 was a resounding success, and Codex, with its current 10 million active professional users, is gaining increasing importance in a sector primarily dominated by Anthropic.

Anthropic is holding off the launch of Fable 5.1 until OpenAI releases GPT 6, and that won't be long now. Axios reported that Sam Altman is briefing the White House on the new model next week, so it is essentially ready to launch."

And And yet for some

Part of the reason that a major model could be released on a Friday and only really be splashy among insiders represents a bigger and yet inevitable trend. Arc Prize's Francois Chollet wrote, " "The era of new model launches as big milestones will eventually come to an end. At some point, they will simply be continuously updated with no widely publicized version [00:32:00] number, probably less than two years away."

Now, I'm not totally sure about this

I think that itkind of depends on the capability unlock of each new model

and I certainly think the labs are going to have incentives to make each of them a big deal. but it is undeniably the case that as we move to these multi-model setups or even increasingly routers that obfuscate the model behind an automated selector

the hugeness of these launches may be less of a big deal in the future. But I don't know. Let me know what you guys think all I have to judge this 

is the comments and the download numbers. Anyways, guys, that is gonna do it for today's AI Daily Brief. Appreciate you listening or watching as always, and until next time, peace 

​ 

Nathaniel Whittemore's audio recording:
