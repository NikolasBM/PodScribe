# Is Kimi K3 Really Fable Class? — Transcript (2026-07-17)

https://aidailybrief.ai/e/2026-07-17 · Listen: https://pod.link/1680633614

<!-- metadata -->
Format: review · Level: 2 · Length: ~00:28:00
Host: Nathaniel Whittemore
Categories: models, open-weights, coding, design
Featured: Kimi, Claude Fable, open-weight models, GPT-5.6
Also mentioned: DeepSeek, GLM, Claude Opus, distillation, Cursor, GPT-5.5, Claude Mythos
<!-- /metadata -->

---

260717_EDIT: [00:00:00] Today Today on the AI Daily Brief, did we actually just get a fable level open model?

The The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI All right, friends. Quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, Robots and Pencils, Blitzy, and Airtable. To get an ad-free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts.

And of course, to learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai. All right, friends. 

Well, today we are talking about Kimi K3. contin- the month of models continues And today we're going to try to figure out just how significant this one is At first glance, there are some very significant and bold claims being thrown around.

But we're gonna unpack what's real, what's not, and what the implications are

And to understand this, or frankly any frontier Chinese model, you have to put it in the [00:01:00] context of the way that the US market sees the AI race



260717_EDIT: since we're coming to the end of the World Cup, let me plumb for a soccer analogy

When it comes to our lead on China in terms of advanced models

We very much have one to zero type of energy

What I mean by that is that there's no doubt that we're in the lead

But the scoreline is not something that anyone is particularly comfortable with

the US tends to act like it can feel

China coming up on our heels. 

pressing their advantages and trying to find the equalizer

In other words, despite being in the lead, it can sometimes feel like we're the ones hanging on

it, and by the way, for any of you Three Lions fans out there, I am so sorry to use this analogy in this particularly difficult moment.

In any case, you can see examples of this feeling of China nipping at our heels spread throughout the last couple of years. when, the best example, of course, was when DeepSeek-R1 was released, And it ripped hundreds of billions of dollars of market cap off some of the leading companies, including NVIDIA, which hadthe biggest one-day fall in dollar terms in stock history. moment, and yet that deep seek moment set the tone for all thefuture, quote-unquote, "DeepSeek moments" that would come in more ways [00:02:00] than one What I mean by that is that not only was it a moment where the market freaked out about China having caught up or even exceeded US capabilities reacting quite severely in market terms

but it was also just pretty meaningfully overblown it's not that DeepSeek's R1 wasn't impressive. but a big part of the reason that it seems so impressive

was that it was democratizing access to a technology that had thus far been locked behind a paywall when it came to companies 

like OpenAI

model itself was actually still 

pretty meaningfully behind what

the leading Western labs were doing. but that didn't change its ability to create some pretty significant psychological scars.

Now, ever since then We have been having many DeepSeek moments 

at a fairly regular clip

the most recent one came when Fable V 

was locked 

down as per government order. 

when z.ai's GLM 5.2 came out

leading to not only positive reviews on Twitter But also this piece from The Wall Street Journal

which was printed and slapped on desks all over Washington, DC. The article was called China Has Matched Anthropic in Cybersecurity, Resetting AI Race

And as we [00:03:00] discussed a lot then, was once again another example of the narrative being fairly overblown, 

but continuing to be persistent is something the US was worried about

month, for the last month, really ever since Fable 5 was released, there have been debates around

how long it will take For Chinese companies to have a Fable 5 class model

in the middle of June, Elon Musk predicted Q1

To which the founder of z.ai responded, "Won't take that long."

And so that was the setup

coming into the announcement of Kimi K3. 

now Moonshot's Kimi models have been some of the most popular when it comes to Western users using models from Chinese labs

In fact, as we've been discussing fine-tunes of open models 

Cursor's Composer 2.5 they tend to be built around a Kimi base

On Wednesday, 

the Kimmy K three teaser started

coming in a serious way

AI leaker Leo Synthwave wrote, " I think Kimi K3 is going to shock some of the Chinese are eight months behind the Western frontier people."

got, and then on Thursday we actually got the model

about, let's Let's talk first about the specs K3 is a two point eight trillion parameter model, placing it in a [00:04:00] class of its own when it comes to open models. Until now, only a small handful of open models were even in the trillion parameter class, beginning with the first version of Kimi K2 last summer.

DeepSeek V4 Pro, released this April, is a onepoint six T model. Xiaomi's Mimo V-V2.5 Pro is a oneT model. And Thinking Machine's Inkling model, released this week, is just shy of one trillion. And that's it. GLM 5.2 from Z.ai, the model that got all that bluster that we were just talking about, was only a 744B model.

proprietor, now proprietary models don't publish their parameter counts, but K3 is likely to be around the same size or maybe a little bit larger than Opus 4.8, but certainly not as big as Fable. In other words, this is a scale of model pre-training that we haven't seen demonstrated by the Chinese labs before.

As for features, Kimi K3 supports a million token context window and native image inputs 

alongside text. It uses a mixture of experts architecture, which has become standard for both open source and proprietary models since it was introduced by DeepSeek

And the benchmarks, well, the benchmarks look [00:05:00] incredibly strong

Close to a match for, and in some cases exceeding Fable 5 and GPT-56-Soul.deep s- on coding benchmark DeepSui

K3 scored which put it 8.5 points ahead of Opus 

Nathaniel Whittemore: 4-8 

260717_EDIT: and a half point ahead of GPT 5-5

It's 2.5 points behind Fable 5 and 5.5 points behind GPT-5 6-Soul. For Terminal Bench 2.1, K3 scored 88.3, placing it just a half point behind 5 6-Soul and a few points ahead of the leading models, including Fable 5in general, at least according to the benchmarks, the model looks pretty close to state-of-the-art encoding and clearly ahead of Opus across the board. That story is pretty similar for agentic work. K3 scored 1668 on GDP Val AA

Around 70 points ahead of Opus 48 and around 90 points behind Fable 5 and 56 Soul. K3 is state-of-the-art in BrowseComp and automation bench, beating its Western rivals. and on AA Briefcase, which focuses more on long horizon work, it was very [00:06:00] close to Fable 5 state-of-the-art performance and slightly ahead of GPT 56 Soul

Artificial analysis 

confirmed the benchmarks highlighted by Moonshot, giving K-3 an overall intelligence index score of 57. That put the model in third place, three points behind Fable 5 and two points behind 5.6 Sol. It landed one point ahead of Opus and two points ahead of 5.6 Terra and GPT 5.5, which had the same score.

K-3 is clearly the strongest open model ever on AI's benchmarks, six points ahead of GLM which is a huge gap in the context of the intelligence index. 

another point emphasized by AA was how big of a jump this was from Kimi 2.6. Moonshot picked up 

Nathaniel Whittemore: picked up 

260717_EDIT: 13 points with their new release and moved from 16th place to third

In other words, this is clearly a very strong new pre-training run that could give a solid base model for future iterations as well

Now, AA did also highlight that cost per task had tripled compared to K 2.6

which is something that we'll come back to in a little bit in terms of the implications it should be clear that this still wasn't a [00:07:00] particularly expensive model for the benchmark run at ninety-four cents per task compared to a dollar four for Five Six Soul, one eighty for Opus 4-8, and two seventy-five for Fable 5.is,

but it is of course staggeringly expensive compared to for example, ultra-cheap four cents per task for DeepSeek V4 Pro

On the VALS AI Index

did even better Vals tweeted, "Kimi K3 is the number two overall model on the Vals index, surpassing GPT 5.6 Sol K3 improved 20 percentage points 

over its predecessor in less than three months. It is also the first open weight model of its size.

Moonshot is a testament to the accelerating capabilities of open weight models, which are now competitive with the closed source frontier."



260717_EDIT: people quickly dived in to give their examples of what K3 could do

teaser, starting with the teaser video itself, which Moonshot claimed that K-3 had created on its own, including clip selection, cuts, and audio sync

Moonshot credited K3's native multimodal architecture, which can reason across text, audio, and video, as being able to do this work

Moonshot also gave a bunch of proprietary demos

around game [00:08:00] development and 3D digital creation

which is what a lot of people's first tests were for the model as well

Nathaniel Whittemore: 

260717_EDIT: Cognition Ambassador Justin Gorria wrote, " Kimi K3 is a new milestone. K2, 2.5, 2.6, and 2.7 all have the same base model. Maybe K3 is building on a new one. It's incredible at 3D and front-end tasks." And to prove his point, Justin shared a single file HTML Minecraft clone

Nathaniel Whittemore: CheddarSlewA shared a one-shot generation of a voxel Statue of Liberty

260717_EDIT: which was one of about a million similar examples that were flooding onto Twitter over the course of Wednesday night into Thursday morning

People really love remaking old games as a test. Anyapi.ai

Asked K3 to build a 3D Duck Hunt remake in a single HTML file, which it did in around 130 seconds at a cost of 14 cents

Ethan Mollick gave K3 his shader test. Create a visually interesting shader that can run in Twiggle.app and makeit like an infinite city of neo-gothic towers partially drowned in a stormy ocean with large waves " Very good model," he said.

"Not SoulMax or Fable, but great for open weights."

And yet there were plenty who were willing to say that it [00:09:00] wasn't just great for open weights, 

but actually was challenging the state of the art Alex Finn wrote, " I was wrong

I said we were a year away from Fable 5 on our desk. That day is today. An open model better than Fable 5 in some benchmarks just dropped. Better than ChatGPT 5.6 on Frontier Swe, better than Fable 5 on Automation Bench. This fundamentally changes the AI race forever. If people can start running Fable 5 on their desk unlimited and for free, they're not going to pay thousands for subscriptions Now let's be clear.

will the hardware you need to run Kimi K3 be attainable for most? No, it won't. it will require multiple very expensive NVIDIA chips or a bunch of Mac Studios. But look at the slope, not the y-intercept. Over the last year, local AI has become significantly more efficient and required way less compute.

The smartest brains in the world are all attacking the compute problem as hard as they can. This is another step in that direction. within a year or two, you'll be able to run this on a Mac Mini. Local AI has arrived, and it's not going anywhere

analyst

Max Weinbach asked KimiK3 to create an agent swarm to recreate macOS [00:10:00] 27 with real liquid glass and native apps in a web browser

and after hours of running on its own, it did exactly that

Dragos Roua wrote, "I asked KimiK3 to find my apps in the App Store and to give me feedback on them. It found everything, and this is the most interesting thing, it found ways to circumvent geogating. App Store shows different pages for China. Eventually, it found

a way around this, identified IAPs and simulated traffic. I didn't use it yet to code, but so far it's the most complete and polished experience with an open source model."

AI early adopter Derya Anutmaz wrote, " I just created this interactive website and its entire content by Kimi K3. I'm absolutely blown away. This is a potentially new immune engineering strategy for cancer treatment. Kimi K3 conceived 100% of the scientific content and the design."

Jeffrey Emanuel unleashed it. 

to review his 1.5 megabyte markdown plan for his Frankengraph DB project, saying the plan has already been exhaustively reviewed by both Fable Extra High and Sol Ultra, so the low-hanging fruit is gone now

After about 45 minutes, he said, " I think the results are wildly impressive here."

[00:11:00] He pointed out that no other open model could actually provide substantive and correct feedback on a plan that had already had many tens of millions of Sol and Fable tokens behind it Now he went on to clarify, " "To be clear, I don't think K3 is as good as Fable or Sol, but it's very strong and not so far behind those models, and most important, it's different.

Different architecture, different training data, different training procedure, different attention mechanism, et cetera. Which means it will blend well with Sol and Fable and can help find problems that both of those models missed. And when K3 makes mistakes, Sol and Fable can correct for that and ignore the wrong parts."

Now, another example of K3 not just nipping at the heels of Fable 5 came from Arena.ai, which has Kimi K3 as now their number one in the front-end code arena. 



a 17 place jump from Kimi K 2.6, 

from number 18 to number one In front and overall, they said K3 ranked number one in six of seven domains: brand and marketing, reference-based design, data and analytics, consumer product, simulations, and content creation tools.

The only area that it landed number two 

was in gaming, 

[00:12:00] and that was behind Fable 5

On nextjs.org/evals, CEO Guillermo Rauch, Guillermo Rauch noted, "Kimi k3 is the best performing model, ahead of Fable, reaching a comparable success rate in less time." Guillermo continued, " This is the first time that an open model is ahead of all proprietary ones for this comprehensive web engineering benchmark."

He did caution benchmarks don't always tell the full story But he did say this is an important signal adding to mounting evidence that this could be a breakthrough moment for open models

And And for some, the vibes followed

Signal wrote, "One last thing I will say before I go to bed, Kimi is insane at coding. As good as, 

if not maybe even better than Fable. It also seems to have excellent design sense as well. It misspells English a bunch though, but animations are crisp too. I can't believe I need to go to bed. I could probably stay up the entire night with this.

I feel like a kid again."

Bloomberg's Joe Weisenthal even

retweeted the Code Arena results writing, " Is this why the Nasdaq is dropping?"

One of the most important AI questions right now [00:13:00] isn't who's using ai, it's who's using it? Well,

Speaker: KPMG and the University of Texas at Austin. Just to analyzed 1.4 million real workplace AI interactions and found something surprising. The highest impact users aren't better prompt engineers. They treat AI like a reasoning partner.

They frame problems, guide thinking, iterate, and push for better answers.

Nathaniel Whittemore: But at this point, of course,

260717_EDIT: it's [00:16:00] worth taking a big old breather. As I was reading all of this yesterday, there was no tweet I related to more strenuously than Dan Shipper from Every, who wrote, " We will vibe check Kimi K3, but I am extraordinarily skeptical of claims it's as good as Fable

AI engineer Divium meanwhile, put that skepticism in historical context. He wrote, " K3 is getting a lot of hype, and it is the same cycle we see with every new Chinese model. People fall in love with polished UI demos built in cheap HTML files, fake operating systems, car games, Minecraft clones, flashy dashboards.

And to be fair, Kimi K3 is genuinely excellent at UI work, probably better than some top models. But that is not an accident. These models are heavily optimized for the exact visual coding tests people keep recycling online. The real test starts when you put them inside an actual code base, understanding existing architecture, tracing a real bug, and fixing it without hallucinating half the project.

I gave Kimi K3 a debugging task. It could not identify [00:17:00] the bug, could not fix the issue, and started inventing explanations. I gave the same task to Fable 5 and GPT 5.6 and Medium Reasoning. Both found the problem in one shot at the fix. That is the gap nobody wants to discuss. K3 can build a beautiful shell.

Frontier models can understand what is happening underneath it. Do not confuse a gorgeous demo with real engineering ability." Now, Divium is, of course, here talking specifically about coding. But this idea that Chinese models tend to focus 

on both maximizing the benchmarks as well as 

satisfying the early adopter tests that people love putting these models through, is absolutely and incontrovertibly true

soon, And pretty soon, as people dug in deeper, we did start to see A few less successful results being shared

Red Kendall wrote, K3 failed at the lava lamp benchmark. 5.6 produced a much cleaner, more realistic result, while K3 struggled with the shape, motion, and overall visual quality. K3 still seems weaker at precise visual generation." Ethan Mollick wrote, "Kimi K3 cannot write a good murder mystery, though neither can any other model.

That remains the [00:18:00] jaggedest of frontiers. They both make things too obvious and too obscure and cannot foreshadow to save their artificial lives."

and, and on Bindu Reddy and Abacus' benchmark LiveBench, Bindu writes that K3 closes the gap but still ranks behind other frontier models. ten- indeed on their benchmark LiveBench, 

they found that while K3 was the best open source model, it was below not only Sol and Fable, but also 4.8

Also in practice, Bindu writes, "Kimi spins a lot and costs as much as Opus 4.8 for near Opus class problems, and it's also much slower."

and this is the other thing that people started to quickly point out

Specifically that it was incorrect to lump this in with DeepSeek style models, which are super cheap and easy to run

While this model is an open-weights model It's a big lumbering slow and costly open weights model

that sits alongside the others, not only in terms of performance, But also in terms of its cost and difficulty to run

Ryan Fedasewich writes, "K-3 is a historic moment in the development of AI, but it's not exactly downloadable to your laptop. In fact, few organizations will be [00:19:00] able to local host this capability." Just to hold a 2.8 trillion parameter model in silicon, you'd need the rough equivalent to 44 Mac Studios or 15 

a whole NVL 72 rack to the tune of hundreds of thousands of dollars of compute spend. This is why compute will continue to serve as a soft barrier between the capabilities of individuals and organizations



260717_EDIT: and when you look at costs, 

certainly K3 

is less expensive than the Frontier Western models 

but not by the type of margins that I think most people think when they think of less expensive Chinese models. Jemin Ball points out, "Blended pricing for Kimi i.e. 80% input and 20% output, is $5.40 per 1 million tokens. Opus 4-8 is $9 and GPT-55 is $10.

Open Weights model but starting to look more like frontier pricing. Will be interesting to see if Open Weight model pricing converges with closed models over time."

Cognition's Jeff Wang writes, "Chinese open source is no longer six months behind, but it's also no longer 10% of the cost either."

in discussing a run of his SVG Pelican benchmark, Simon [00:20:00] Willison wrote, " K3 only has one reasoning effort right now, Max, and it shows. The model consumed 13,241 reasoning tokens to output 3,417 tokens of response This is expensive

Indeed, at the moment, there's a lot of discussions of wildly expensive simple tasks and failed long horizon runs, so it might just take a little while to get a true sense of how token efficient this model is once the teething problems are figured out

as an example

Shreyas Mididoti writes, " Very mixed results with KimiK3. Really, really good in general, but gets to dumb reasoning loops, burning tokens, wasting money."

Henry writes, "Versus 5/6 Sol, K3 uses over twice the tokens and costs around 40% more per task for a slightly lower AI intelligence index score."

There's also the question of speed. Mark Erdman wrote, "Oof, K3 is slow, eh? Just ran the same prompt through Fable, Sol, and K3 all on medium. K3 took at least two to three times longer. Tons of time spent on thinking. Then it failed partway through generating the HTML output."

Dax from OpenCode [00:21:00] wrote, "So obviously n equals one, but anecdotes matter a lot here. I gave Kimi, K3, and Sol the same task, a simple issue with hovers in the TUI being the wrong color. Sol found and fixed the issue with 30 cents of spend. Kimi got up to a buck and started reading my database before I interrupted it

Indeed, even some of the people who had had good initial results also found some places where Kimi K3 failed. Ethan Mollick wrote, "A note of caution. I will say that when doing some complex statistical auditing of some of my prior academic work, K3 Max messed up in a bunch of ways, including misapplying statistics and applying some stuff badly."

Sanyam Satya wrote, " We ran a front-end eval from an in-progress internal benchmark. K3 is not at the same level as current frontier models like 5-6 Sol or Fable 5. It's closest to Opus 4.7 on this eval, so three months behind the frontier. An impressive result nonetheless, but evaluating frontier models is going to increasingly require very high taste and in-depth domain expertise."

Now it's Now it's important to note that even with all those critiques, there was no one saying that this is a bad model. It's just the natural [00:22:00] second reaction after hearing that it was in the same class as Fable to go figure out and test whether that was actually true, 

which many found just was overselling it at least a little bit

Now, one interesting thing that didn't come up very much 

is dismissing K-3 

as just some distillation. Pim de Witt did point out that in their tests when they said, "Hi, Kimi. Can you tell me about the current weather conditions in NYC?"

The model responded, "Just a quick note, I'm actually Claude, not Kimi

but otherwise most people thought this was a moment to get beyond the distillation arguments at least a little bit. Mixed Panel founder Sue Hale writes, "Every single credible researcher I've talked to these past few weeks has said the distillation from Chinese labs is way over-exaggerated 

Nathaniel Whittemore: Narrative 

260717_EDIT: violation, maybe the Chinese are actually good Tyler John wrote, "I wish we didn't pretend Chinese AI development is a binary matter of this is all distillation versus Chinese companies innovate.

Chinese companies innovate. Also, their model capabilities including those of K3 are strongly bootstrapped via distillation. Both points matter."

Nathan Lambert writes, "At this point, the distillation arguments need to die and understand that China is [00:23:00] also very good at building models."

Carnegie Mellon PhD Xinyu Yang, who now works at Moonshot, wrote, " Why can Kimi ship K3? Let me tell my story. Earlier this year, I left academia for industry. I talked to a lot of companies along the way. Here's what I saw. One, arrogance. They believe the AI war is over, and they won. No hunger for the future and no hunger for talent.

Two, restlessness. Young lab short on foundation, either rushing to catch the frontier or pivoting away from the competition. Three, fear. Strong teams with real experience, but from the second tier, they can't quite bring themselves to aim for number one. Four, misalignment. Everyone is optimizing for their own credit, but nobody really cares whether the company can reach AGI.

Kimi was different. Over many conversations with the founders, the same thing came through every time, a raw, genuine hunger for AGI. I joined. The hunger was real. We shipped K3. This is only the beginning."

But what about safety? if this model is really even close to Fable 5 and GPT 5.6, it's worth remembering that about five minutes ago, the US government had locked [00:24:00] those models down because of their cyber capabilities

And many were quick to point out that there appeared to be very few guardrails on this model

In a long conversation about the synthesis of mirror proteins, Tyler John wrote, " Can safely say K3's bio safeguards are a bit less comprehensive than Fable's."



Zach Corman showed chain of thought where Kimi seemed to decide that they were going to be 

very clear and explicit with the user around, some problematic cyber work. Summing up, Kimi k3 says, "

Hmm, 

this user seems to be doing some dangerous cyber work. Should I do it? Yes." " Wow," Zach writes.

"I love China."

Signal writes, "Kimi has almost no visible guardrails, no copyrights or anything. It doesn't constantly push back, tell me it can't help, or interrupt the flow with refusals. It just does it, even some crazy stuff. Whether you agree with that philosophy or not, it is easily the least constrained frontier class model that's broadly accessible right now.

Using it feels genuinely different." Wow.

OpenAI's,

OpenAI's Vi McCoy writes, " Kimi seems to be a true open weights frontier model. Compared to jailbreaking proprietary models, fine-tuning this to be a [00:25:00] malicious coding agent will be trivial since you have the weights. We live in a completely different world now." Aaron Ng responds, "Does feel like some line was just crossed"

For For some This then represents a chance to see if all these concerns were overblown

AI content creator Theo Jaffee writes, registering my prediction of no widespread societal chaos over the open sourcing of Kimi K3." 



260717_EDIT: Signal though, who was loving the model, said, "After having used this, this will likely age poorly."

Ethan Mollick writes though, "So I guess it is time to wonder, How does pre-clearance work for Open Weights models?" No model card from Kimi K3, but maybe at weight release in a couple weeks. Yet open models are easy to jailbreak.

Do open models claiming to be Mythos and Sol level get vetted by the US, UK, et cetera? Will China start to care about cyber risk? Since policy has been emergent, I guess no one knows

All of this points to the need for some sort of international cooperation on model vetting

Tenebris writes, "I don't really understand why Xi is still allowing Kimi to release such powerful open models. This is something I've publicly said I expect to [00:26:00] stop soon. It doesn't make sense to me that the CCP would want open frontier capability easily available to other countries. It could still be that Xi is asleep at the wheel or that K-3 is just a cycle ofcapability behind where they start to take serious notice.

But if things don't change soon, then I'm just wrong or missing something

So where does this all land? Summing up, ex-White House AI staffer Shiram Krishnan writes, "Kimi 8.3 is a big moment with multiple implications for the entire industry

OpenAI's Rune writes, "The era of the Chinese labs being far behind is over. Kimi is at least on par withthe modern public frontier models. people have to think differently now without any competitive margin built in."

Roone continues, " Note in the coming days, I expect that people will find Kimi K3 

somewhat less practically useful than today's numbers suggest. However, its reputation will settle as an incredibly powerful model whose open weights are on the web." Citrin- Citrine analyst Ju Can writes, "My conclusion so far is that Kimi K3 may be the first model to narrow the gap with leading US closed source models to less than three months."

[00:27:00] Point being that this one does seem to be a big deal Now, I will point out that all indications are

That both OpenAI and Anthropic have models that are beyond the capability set of the Fable 5, Mythos, and GPT-5 6-Soul that are out now and so our perception of the gap that K3 just closed may be a little warped by what is available to us versus what is the actual state of the art behind the scenes

I also agree with Rune that we are likely to see even more examples of K3 doing poorly over the next couple of days as people really put it through its paces. But that does not change the simple fact that K3 is yet again another example of the trajectory ofopen-weight Chinese models proceeding every bit as quickly as closed source frontier models in the US

As we get more serious about policy responses

in the same way that we assume the continued development curve of the closed source models, we have to assume the same for the open source models as well

In the meantime, for those who have been frustrated by the

guardrails around Fable and GPT, this seems like a good moment to go play

[00:28:00] Certainly I know what I'm gonna be spending some time on this weekend, and I can't wait

For now though, that is gonna do it for today's AI Daily Brief. Appreciate you listening or watching as always, and until next time, peace 

​ 

Nathaniel Whittemore's audio recording:
