---
podcast: "latent-space"
podcast_title: "Latent Space"
title: "97% Cheaper, Faster, Better, Correct AI — with Varun Mohan of Codeium"
date: 2023-03-02
url: "https://www.latent.space/p/varun-mohan"
guid: "substack:106013498"
host: "Swyx"
transcript_source: "publisher"
---

# 97% Cheaper, Faster, Better, Correct AI — with Varun Mohan of Codeium

**Alessio Fanelli** [00:00:00] Hey everyone. Welcome to the Latent Space podcast. This is Alessio, partner and CTO in residence at Decibel Partners. I'm joined by my cohost, swyx, writer, editor of L Space Diaries.

**Swyx** [00:00:00] Hey, and today we have Varun Mohan from Codeium / Exafunction on. I should introduce you a little bit because I like to get the LinkedIn background out of the way.

[00:00:00] So you did CS at MIT and then you spent a few years at Nuro where you were ultimately tech lead manager for autonomy. And that's an interesting dive. Self-driving cars in AI and then you went straight into Exafunction with a few of your coworkers and that's where I met some of them and started knowing about Exafunction.

[00:00:30] And then from out of nowhere you cloned GitHub Copilot. That's a lot of progress in a very short amount of time. So anyway, welcome .

**Varun Mohan** [00:00:51] That's high praise.

**Swyx** [00:00:51] What's one thing about you that doesn't appear on LinkedIn that is a big part of what people should know?

**Varun Mohan** [00:00:51] I actually really like endurance sports actually.

[00:00:51] Like I, I've done multiple triathlons. I've actually biked from San Francisco to LA. I like things that are like suffering. I like to suffer while I, while I do sports. Yeah.

**Swyx** [00:01:09] Do you think a lot about like code and tech while you're doing those endurance sports or are you just,

**Varun Mohan** [00:01:09] your mind is just focused?

[00:01:09] I think it's maybe a little bit of both. One of the nice things about, I guess, endurance athletics, It's one of the few things you can do where you're not thinking about, you can't really think about much beyond suffering. Like you're climbing up a hill on a bike and you see like, uh, you see how many more feet you need to climb, and at that point you're just struggling.

[00:01:26] That's your only job. Mm-hmm. . Yeah. The only thing you can think of is, uh, pedaling one more pedal. So it's actually like a nice, a nice way to not think about work. Yeah,

**Alessio Fanelli** [00:01:45] yeah, yeah. Maybe for the audience, you wanna tell a bit about exa function, how that came to be and how coding came out

**Varun Mohan** [00:01:45] of that. So a little bit about exo function.

[00:01:45] Before working at exa function, I worked at Neuro as Sean was just saying, and at neuro, I sort of managed large scale offline deep learning infrastructure. Realized that deep learning infrastructure is really hard to build and really hard to maintain for even the most sophisticated companies, and started exa function to basically solve that gap, to make it so that it was much easier for companies.

[00:02:02] To serve deep learning workloads at scale. One of the key issues that we noticed is GPUs are extremely hard to manage fundamentally because they work differently than CPUs. And once a company has heterogeneous hardware requirements, it's hard to make sure that you get the most outta the hardware. It's hard to make sure you can get, get great GPU utilization and exa function was specifically built to make it so that you could get the most outta the hardware.

[00:02:24] Make sure. Your GP was effectively virtualized and decoupled from your workload to make it so that you could be confident that you were running at whatever scale you wanted without burning the bank.

**Swyx** [00:02:50] Yeah. You gave me this metric about inefficiency,

**Varun Mohan** [00:02:50] right? Oh, okay. Like flop efficiency. Yeah. Yeah. So basically, I think it comes down to, for most people, one of the things about CPUs that's really nice is with containers, right?

[00:02:50] You can end up having a single. You can place many containers on them and all the containers will slowly start eating the compute. It's not really the same with GPUs. Like let's say you have a single. For the most part, only have one container using that gpu. And because of that, people heavily underestimate what a single container can sort of do.

[00:03:13] And the GPU is left like heavily idle. And I guess the common term now with a lot of LM workloads is like the flop efficiency of these workloads. M F U, yeah. Yeah. Model flop utilization. The model flop utilization, which is basically like what fraction of the flops or compute on the hardware is actually getting used.

[00:03:33] And sort of what we did at exa function. Not only make it so that the model was always running, we also built compiler technology to make it so that the model was also running more efficiently. And some of these things are with tricks like operator fusion, like basically you could imagine fusing two operations together such that the time it takes to compute.

[00:03:49] the fused operation is lower than the time it takes for each individual operation. Oh my God. Yeah. .

**Alessio Fanelli** [00:04:07] Yeah. And you have this technique called dynamic multiplexing, which is basically, instead of having a one-to-one relationship, you have one GP for multiple clients. And I saw one of your customers, they went from three clients to just one single GPU and the cost by 97%.

[00:04:07] What were some of those learning, seeing hardware usage and efficiencies and how that then played into what, what

**Varun Mohan** [00:04:29] you're building? Yeah, I think it basically showed that there was probably a gap with even very sophisticated teams. Making good use of the hardware is just not an easy problem. I think that was the main I, it's not that these teams were like not good at what they were doing, it's just that they were trying to solve a completely separate problem.

[00:04:29] They had a model that was trained in-house and their goal was to just run it and it, that should be an easy. Easy thing to do, but surprisingly still, it's not that easy. And that problem compounds in complexity with the fact that there are more accelerators now in the cloud. There's like TPUs, inferential and there's a lot of decisions, uh, that users need to make even in terms of GPU types.

[00:04:50] And I guess sort of what we had was we had internal expertise on what the right way to run the workload was, and we were basically able to build infrastructure and make it so that companies could do that without thinking. So most

**Alessio Fanelli** [00:05:10] teams. Under utilizing their hardware, how should they think about what to own?

[00:05:10] You know, like should they own the appearance architecture? Like should they use Xlo to get it to production? How do you think

**Varun Mohan** [00:05:26] about it? So I think one thing that has proven to be true over the last year and a half is companies, for the most part, should not be trying to figure out what the optimal ML architecture is or training architecture is.

[00:05:26] Especially with a lot of these large language models. We have generic models and transformer architecture that are solving a lot of distinct problems. I'll caveat that with most companies. Some of our customers, which are autonomous vehicle companies, have extremely strict requirements like they need to be able to run a model at very low latency, extremely high precision recall.

[00:05:45] You know, GBT three is great, but the Precision Recall, you wouldn't trust someone's life with that, right? So because of that, they need to innovate new kinds of model architectures. For a vast majority of enterprises, they should probably be using something off the shelf, fine tuning Bert models. If it's vision, they should be fine tuning, resonant or using something like clip like the less work they can do, the better.

[00:06:05] And I guess that was a key turning point for us, which is like we start to build more and more infrastructure for the architectures that. The most popular and the most popular architecture was the transformer architecture. We had a lot of L L M companies explicitly reach out to us and ask us, wow, our GT three bill is high.

[00:06:25] Is there a way to serve G P T three or some open source model much more cheaply? And that's sort of what we viewed as why we were maybe prepared for when we internally needed to deploy transform models our.

**Alessio Fanelli** [00:06:44] And so the next step was, Hey, we have this amazing infrastructure. We can build kind of consumer facing products, so to speak, at with much better unit economics, much better performance.

[00:06:44] And that's how code kind

**Varun Mohan** [00:07:08] of came to be. Yeah. I think maybe the, the play is not maybe for us to be just, we make a lot of consumer products. We want to make products with like clear ROI in the long term in the enterprise. Like we view code as maybe one of those things. Uh, and maybe we can, we can talk about code maybe after this.

[00:07:08] We. Products like co-pilot as being extremely valuable and something that is generating a lot of value to professionals. We saw that there was a gap there where a lot of people probably weren't developing high intensive L L M applications because of cost, because of the inability to train models the way they want to.

[00:07:27] And we thought we could do that with our own infrastructure really quickly.

**Swyx** [00:07:44] I wanna highlight when you say high intensive, you mean basically generate models every key, uh, generate inferences on every keystroke? That's

**Varun Mohan** [00:07:44] right. Yeah. So I would say like, there's probably two kinds of L l M applications here.

[00:07:44] There's an L L M application where, you know, it rips through a bunch of data and maybe you wait a couple minutes and then you see something, and then there's an application where the quality is not exactly what you want, but it's able to generate enough, sorry, low enough latency. It's still providing a ton of value.

[00:07:59] And I will say there's like a gap there where the number of products that have hit that co-pilot spot is actually not that high. Mm. A lot of them are, are kind of like weight and, you know, just generate a lot of stuff and see what happens because one is clearly more compute intensive than the other Basically.

**Swyx** [00:08:16] Well co uh, I don't know if we told the whole story yet, you were going to

**Varun Mohan** [00:08:16] dive into it. . Yeah, so I guess, I guess the story was I guess four or five months ago we sort of decided internally as a team we were like very early adopters of co-pilot. I'm not gonna sit here and say co-pilot, it's not a great tool.

[00:08:16] We love co-pilot. It's like a fantastic tool. We all got on the beta. The moment it came out we're like a fairly small T, but we, like we all got in, we were showing each other completions. We end up writing like a lot of cuda and c plus plus inside the company. And I think there was probably a thought process within us that was like, Hey, the code we write is like very high aq.

[00:08:45] You know? So like there's no way it can help. And one of the things in c plus plus that's like the most annoying is writing templates. Writing template programming is maybe one of those things. No one, maybe there's like some people in the C plus O standards community that can do it without looking at the, looking at anything online.

[00:09:04] But we struggle. We struggle writing bariatric templates and COPA just like ripped through. Like we had a 500 line file and it was just like writing templates like, and we didn't really even test it while we were running it. We then just compiled it and it just, We're like, wow. Like this is actually something that's not just like it's completing four loops, it's completing code for us.

[00:09:19] That is like hard in our brains to reach, but fundamentally and logically is not that complicated. The only reason why it's complicated is there's just a lot of rules, right. And from then we were just like, wow, this is, that was maybe the first l l m application for us internally, because we're not like marketers that would use, uh, Jasper, where we were like, wow, this is like extremely valuable.

[00:09:38] This is not a toy anymore. So we wanted to take our technology to build maybe apps where these apps were not gonna be toys, right? They were not gonna be like a demo where you post it on Twitter and then you know there's hype and then maybe like a month later, no one's using.

**Swyx** [00:09:58] There's a report this morning, um, from co-pilot where they, they were estimating the key tabs on amount of code generated by a co-pilot that is then left in code repos and checked in, and it's something like 60 to 70%

**Varun Mohan** [00:09:58] That's, that's nuts, but I totally believe it given, given the stats we have too. There's this flips in your head once you start using products like this, where in the beginning there's like, there's like skepticism, like how, how valuable can it be? And suddenly now like user behavior fundamentally changes so that now when I need to write a function, I'm like documenting my code more because I think it's prompting the model better, right?

[00:09:58] So there's like this crazy thing where it's a self-fulfilling prophecy where when you get more value from it, more of your code is generated. From co-pilot

**Swyx** [00:10:43] just to walk through the creation process, I actually assumed that you would have grabbed your data from the pile, which is the Luther ai, uh, open source, uh, code information.

[00:10:43] But apparently you scraped your own

**Varun Mohan** [00:11:00] stuff. Yeah. We ended up basically using a lot of open, I guess, permissively licensed code, uh, in the public internet, mainly because I think also the pile is, is fairly a small subset. Uh, I think maybe after we started there was the, that was also came to be, but for us, we had a model for ourselves even before that, uh, was the point.

[00:11:00] Ah, okay. So the timing was just a little bit off. Yeah, exactly. Exactly. But it's awesome work. It's, it seems like there's a good amount of work that's getting done Decentrally. Yeah. Which is a little bit surprising to me because I'm like more bullish on everyone needs to get together in a room and make stuff happen.

[00:11:21] Like we're all in person in Mountain View. But yeah, no, it's pretty impressive. Yeah. Luther in general, like everything they've done, I'm pretty impressed with it. Yeah, and we're

**Swyx** [00:11:35] gonna talk about that. Cause I, I didn't know you were that involved in the community

**Varun Mohan** [00:11:35] that early on I wasn't involved. It was more of like a, I was watching and maybe commenting from time to time.

[00:11:35] So they're a very special community for sure. Yeah,

**Swyx** [00:11:50] yeah, yeah. That's true. That's true. My impression is a bunch of you are geniuses. You sit down together in a room and you. , get all your data, you train your model, like everything's very smooth sailing. Um, what's wrong with that

**Varun Mohan** [00:11:50] image? Yeah, so probably a lot of it just in that a lot of our serving infrastructure was already in place, Uhhuh before then.

[00:11:50] So like, hey, we were able to knock off one of these boxes that I think a lot of other people maybe struggle with. The open source serving offerings are just, I will say, not great in that. That they aren't customized to transformers and these kind of workloads where I have high latency and I wanna like batch requests, and I wanna batch requests while keeping latency low.

[00:12:09] Mm-hmm. , right? One of the weird things about generation models is they're like auto regressive, at least for the time being. They're auto aggressive. So the latency for a generation is a function of the amount of tokens that you actually end up generating. Like that's like the math. And you could imagine while you're generating the tokens though, unless you batch a.

[00:12:29] It's gonna end up being the case that you're not gonna get great flop utilization on the hardware. So there's like a bunch of trade offs here where if you end up using something completely off the shelf, like one of these serving thing, uh, serving frameworks, you're gonna end up leaving a lot of performance on the table.

[00:12:46] But for us, we were already kind of prepared. To sort of do that because of our infrastructure that we had already built up. And probably the other thing to sort of note is early on we were able to leverage open source models, sort of bootstrap it internally within our company, but then to ship, we finally had some requirements like, Hey, we want this model to have fill in the middle capabilities and a bunch of other things.

[00:13:00] And we were able to ship a model ourselves. So we were able to time it so that over the course of multiple months, different pieces were like working out properly for us. So it wasn't. . You know, we started out and we were just planning the launch materials. The moment we started there was like maybe some stuff that was already there, some stuff that we had already figured out how to train models at scale internally.

[00:13:20] So we were able to just leverage that muscle very quickly. I think the one

**Swyx** [00:13:38] thing that you had figured out from the beginning was that it was gonna be free forever. Yeah. Yeah, co-pilot costs $10

**Varun Mohan** [00:13:38] a month. Co-pilot costs $10 a month. I would argue significantly more value than $10 a month. The important thing for us though, was we are gonna continue to build more great products on top of code completion.

[00:13:38] We think code completion is maybe day one of what the future looks like. And for that, clearly we can't be a product that's like we're $10 a month and we're adding more products. We want a user base that loves using us. And we'll continue to stay with us as we continue to layer on more products. And I'm sure we're gonna get more users from the other products that we have, but we needed some sort of a differentiator.

[00:13:58] And along the way we realized, hey, we're pretty efficient at running these workloads. We could probably do this. Oh, so it wasn't,

**Swyx** [00:14:17] it was a plan to be free from the start. You just

**Varun Mohan** [00:14:17] realized we, yeah. We realized we could probably, if we cut and optimized heavily, we could probably do this properly. Part of the reasoning here was we were confident we could probably build a pro tier and go to the enter.

[00:14:17] But for now, originally when we, when we started, we weren't like, we're just gonna go and give every, all pieces of software away for free. That wasn't like sort of the goal there. And

**Swyx** [00:14:35] since you mentioned, uh, adoption and, you know, traction and all that, uh, what can you disclose about user growth? Yeah, user adoption.

**Varun Mohan** [00:14:35] Yeah. So right now we have. We probably have over 10,000 users and thousands of daily actives, and people come back day over day. Our growth is like around, you know, four to 5% day over day right now. So all of our growth right now is sort of like word of mouth, and that's fundamentally because like the product is actually one of those products where.

[00:14:35] Even use COT and use us, it's, it's hard to tell the difference actually. And a lot of our users have actually churned off of cot isn't Yeah. I,

**Swyx** [00:15:08] I swept Yeah. Yeah. To support you guys, but also also to try

**Varun Mohan** [00:15:08] it out. Yeah, exactly. So the, the crazy thing is it wasn't like, Hey, we're gonna figure out a marketing motion of like, Going to the people that have never heard of co-pilot and we're gonna like get a bunch of users.

[00:15:08] We wanted to just get users so that in our own right we're like a really great product. Uh, and sort of we've spent a lot of engineering time and obviously we co-wrote a blog post with you, Sean, on this in terms of like, there's a lot of engineering work, even beyond the latency, making sure that you can get your cost down to make a product like this actually work.

**Swyx** [00:15:27] Yeah. That's a long tail of, of stuff that you referenced,

**Varun Mohan** [00:15:27] right? Yes. Yeah, exactly.

**Swyx** [00:15:27] And you, you said something to the order of, um, and this maybe gets into co-pilot for X uh, which is something that everybody is keen about cuz they, they see the success of co-pilot. They're like, okay, well first of all, developer tools, there's more to do here.

[00:15:27] And second of all, let's say the co-pilot idea and apply for other disciplines. I don't know if you wanna Yeah.

**Varun Mohan** [00:16:00] There's

**Alessio Fanelli** [00:16:00] gonna some. Key points that, that you touched on. Um, how to estimate, inference a scale, you know, and the latency versus quality trade-offs. Building on first party. So this is free forever because you run your own models, right?

[00:16:00] That's right. If you were building on open ai, you wouldn't be able to offer it for free real-time. You know, when I first use coding, It was literally the same speed as Copi is a little bit

**Swyx** [00:16:19] faster. I don't know how to quantify it,

**Varun Mohan** [00:16:19] but we are faster. But it's one of those things that we're not gonna like market as that's the reason because it's not in and of itself a right for you to like, I'm just gonna be open with you.

[00:16:19] It's not a reason for you to like suddenly turn off a copilot where if our answers were trash, uh, but we were faster. You know what I mean? But your focus

**Alessio Fanelli** [00:16:39] was there. We used the alpha, I think prem on our discord came to us and say, you guys should try this out. So it was really fast. Even then, prompt optimization is another big thing, and model outputs and UX kind of how you bring them together.

[00:16:39] Which ones of these things are maybe like the one or two that new founders should really think about first?

**Varun Mohan** [00:17:00] Yeah, I think, I think my feeling on this is unless you are ex, you probably should always bootstrap on top of an existing a. Because like even if you were to, the only reason why we didn't is because we knew that this product was actually buildable.

[00:17:00] Probably if we worked hard enough to train a model, we would actually be able to build a great product already. But if you're actually going out and trying to build something from scratch, unless you genuinely believe, I need to fine tune on top of, you know, terabytes of data terabyte is a very large amount of data, but like tens of gigabytes of data.

[00:17:22] Probably go out and build on top of an API and spend most of your time to make it so that you can hit that quality latency trade off properly. And if I were to go out and think about like the three categories of like an LM product, it's probably like latency, quality, and correct ability. The reality is, you know, if I were to take a product like co-pilot or Coum, the latency is very low.

[00:17:37] The quality I think, is good enough for the task, but the correct ability is, is very easy. Credibility. What, what is correct ability? Correct ability means, let's say the quality is not there. Like you consider the the case where, The answer is wrong. How easy is it for your user to actually go and leverage parts of the generation?

[00:17:58] Maybe a, a concrete example. There's a lot of things people are excited about right now where I write a comment and it generates a PR for me, and that's like, that's like really awesome in theory. I think that's like a really cool thing and I'm sure at some point we will be able to get there. That will probably require an entirely new model for what it's worth that's trained on diffs and commits and all these other things that looks at like improvements and code and stuff.

[00:18:16] It's probably not gonna be just trained on generic code. But the problem with those, those sort of, I would say, applications are that, let's suppose something does change many files, makes large amounts of changes. First of all, it's guaranteed not gonna be. Because even the idea of like reviewing the change takes a long time.

[00:18:37] So if the quality and the correct ability is just not there, let's say you had 10 file, a 10 file change and you modified like, you know, file two and four, and those two modifications were consistent, but the other eight files were not consistent. Then suddenly the correct ability is like really hard.

[00:18:54] It's hard to correct the output of the model. And so the user interface is 100% really important. But maybe until you get the latency down or the correct ability, like correct ability, like a lot better, it's probably not gonna be shippable. And I think that's what you gotta spend your time focusing on.

[00:19:10] Can you deliver a product that is actually something users want to use? And I think this is why I was talking about like demo. It's like very easy to hand to handpick something that like works, that works for a demo, exceedingly hard for something that has large scope, like a PR to work consistently. It will take a lot of engineering effort to make it work on small enough chunks so that a user is like, wow, this is value generative to me.

[00:19:26] Because eroding user trust or consumer trust is very easy. Like that is, it is is much, much, it's very easy to erode user trust versus enterprise. So just be mindful of that, and I think that's probably like the mantra that most of these companies need to operate under. Have you done any

**Alessio Fanelli** [00:19:49] analysis on. What the ratio between code generated and latency is.

[00:19:49] So you can generate one line, but you could also generate the whole block. You can generate Yeah. A whole class and Yeah. You know, the more you generate the, the more time it takes. Like what's the sweet spot that, that you

**Varun Mohan** [00:20:11] found? Yeah, so I think there was a great study and, and I'm not sure if it's possible to link it, but there was a great study about co-pilot actually that came out.

[00:20:11] Basically what they said was there were two ways that developers usually develop with a code assistant technology. They're either in what's called like acceleration mode or exploration mode. And exploration mode is basically you're in the case where you don't even know what the solution space for the function is.

[00:20:28] and you just wanna generate a lot of code because you don't even know what that looks like. Like it might use some API that you've never heard of. And what you're actually doing at that point is like you're writing a clean comment, just wishing and praying that you know, the generation is long enough and gets you, gets you far enough, right?

[00:20:43] acceleration mode is basically you are doing things where you are very confident in what you're doing and effectively. Code gives you that muscle so that you can basically stay in flow state and you're not thinking about like exactly what the APIs look like, but push comes to shove. You will figure out what the APIs look like, but actually like mentally, it takes off like a load in your head where you're like, oh wow.

[00:20:57] Like I can just do this. The intent to execution is just a lot, a lot lower there. And I think effectively you want a tool that captures that a little bit. And we have heuristics in terms of captur. Whether or not you're in acceleration versus exploration mode. And a good heuristic is, let's say you're inside like a basic block of a piece of code.

[00:21:18] Let's say you're inside a a block of code or an IF statement, you're probably already in acceleration mode and you would feel really bad if I started generating the ELs clause. Because what happens if that else causes really wrong? That's gonna cause like mental load for you because you are the way programmers think.

[00:21:37] They only want to complete the if statement first, if that makes sense. So there are things where we are mindful of like how many lines we generate if you use the product, like multi-line generations happen and we are happy to do them, but we don't want to do them when we think it's gonna increase load on developers, if that makes sense.

[00:21:51] That

**Alessio Fanelli** [00:22:07] makes sense. So co-pilot for x. , what are access that you think are interesting for people to build

**Varun Mohan** [00:22:07] in? Didn't we see some, some tweet recently about Harvey ai, uh, company that, that is trying to sell legal? It's like a legal, legal assistance. That's, that's pretty impressive, honestly. That's very impressive.

[00:22:07] So it seems like I would really love to see what the product looks like there, because there's a lot of text there. You know, looking at bing, bing, ai, like, I mean, it's, it's pretty cool. But it seems like groundedness is something a lot of these products struggle with, and I assume legal, if there's one thing you want them to.

[00:22:23] To get right. It's like the groundedness. Yeah.

**Swyx** [00:22:39] Yeah. I've made the analogy before that law and legal language is basically just another form of programming language. You have to be that precise. Yes. Definitions must be made, and you can scroll to find the definition. It's the same thing. Yes. ,

**Varun Mohan** [00:22:39] yes. Yeah. But like, I guess there's a question of like comprehensiveness.

[00:22:39] So like, let's say, let's say the only way it generates a suggestion is it provides like, you know, citations to other legal. You don't want it to be the case that it misses things, so you somehow need the comprehensiveness, but also at the same time, you also don't want it to make conclusions that are not from the site, the things at sites.

[00:22:59] So, I don't know, like that's, that's very impressive. It's clear that they've demonstrated some amount of value because they've been able to close a fairly sizable enterprise contract. It was like a firm with 3,500 lawyers, something nuts, honestly. Very cool. So it's clear this is gonna happen, uh, and I think people are gonna need to be clever about how they actually make it work.

[00:23:15] Within the constraints of whatever workload they're operating in. Also, you, you guys

**Swyx** [00:23:34] are so good at trading stuff, why don't you, you try

**Varun Mohan** [00:23:34] cloning it. Yeah. So I think, I think that's, that's, uh, preview the roadmap. Yeah, yeah, yeah, yeah. No, no, no, but I'm just kidding. I think one of the things that we genuinely believe as a startup is most startups can't really even do one thing properly.

[00:23:34] Mm-hmm. Focus. Yeah. Yeah. Usually doing one thing is really hard. Most companies that go public have like maybe a couple big products. They don't really have like 10, so we're under no illusions. Give the best product experience, the amount of engineering and attention to detail, to build one good product as hard.

[00:23:52] So it's probably gonna be a while before we even consider leaving code. Like that's gonna be a big step because the amount of learning we need to do is gonna be high. We need to get users right. We've learned so much from our users already, so, yeah, I don't think we'd go into law anytime soon.

**Swyx** [00:24:08] 3,500 lawyers with Ellen and Ry, uh, is, is is apparently the, the new

**Varun Mohan** [00:24:08] That's actually really big.

[00:24:08] Yeah. Yeah. I can congrat.

**Swyx** [00:24:28] Yeah, it's funny cuz like, it seems like these guys are moving faster than co-pilot. You know, co-pilot just launched, just announced enterprise, uh, like co-pilot for teams or co-pilot for Enterprise. Yeah. After like two years of testing.

**Varun Mohan** [00:24:28] Yeah, it does seem like the co-pilot team has built a very, very good product.

[00:24:28] Um, so I don't wanna like say anything, but I think it is the case to startups will be able to move faster. I feel like that is true, but hey, like GitHub has great distribution. Whatever product they do have, they will be able to sell it really. Shall

**Swyx** [00:24:44] we go into model numbers and infra estimates? our favorite

**Varun Mohan** [00:24:44] topics.

[00:24:44] Nice small models. Nice.

**Swyx** [00:25:02] So this is, um, relevant to basically I'm researching a lot of skilling law stuff. You have a lot of thoughts. You, you host paper discussions

**Varun Mohan** [00:25:02] in your team. Yeah, we, we try to like read papers that we think are really interesting and relevant to us. Recently that's been, there's just a fire hose of papers.

[00:25:02] You know, someone even just curating what papers we should read internally as a company. Yeah, I think, I think there's, there's so much good content

**Swyx** [00:25:21] out there. You should, you guys should have a podcast. I mean, I told you this before. Should have a podcast. Just, just put a mic near where, where you guys are

**Varun Mohan** [00:25:21] talking.

[00:25:21] We gotta, we gotta keep developing coding though, . No, but you're doing this discussion

**Swyx** [00:25:34] anyway. You

**Varun Mohan** [00:25:34] might as well just, oh, put the discussion on a podcast. I feel like some of the, some of the thoughts are raw, right? Like, they're not gonna be as, as nuanced. Like we'll just say something completely stupid during our discussions.

[00:25:34] I don't know, , maybe that's exciting. Maybe that's, it's kinda like a justin.tv, but for ML papers, Okay, cool. I watched that.

**Swyx** [00:25:48] Okay, so co-pilot is 12 billion parameters. Salesforce cogen is up to 16. G P t three is 175. GP four is gonna be 100 trillion billion. Yeah. So what, what we landed on with you is with, uh, with Cilla, is that we now have an idea of what compute optimal data scaling is.

[00:25:48] Yeah. Which is about 20 times parameters. Is that intuitive to you? Like what, what did that

**Varun Mohan** [00:26:14] unlock? I think basically what this shows is that bigger models are like more data efficient, like given the same number of tokens, a big model like trained on the same number of tokens. A bigger model is like, is gonna learn more basically.

[00:26:14] But also at the same time, the way you have to look at it is there are more flops to train a bigger model on the same number of tokens. So like let's say I had a 10 billion parameter model and I trained it on on 1 million tokens, but then I had a 20 billion parameter model at the end of it will be a better.

[00:26:32] It will have better perplexity numbers, which means like the probability of like a prediction is gonna be better for like the next token is gonna be better. But at the end of it, you did burn twice the amount of compute on it. Right? So Shinto is an interesting observation, which says if you have a fixed compute budget, And you want the best model that came out of it because there's like a difference here where a model that is, that is smaller, trained on the same number of tokens as fewer flops.

[00:26:47] There's a a sweet spot of like number of tokens and size a model. I will say like people probably like. Are talking about it more than they should, and, and I'll, I'll explain why, but it's a useful result, which is like, let's say I have, you know, some compute budget and I want the best model. It tells you what that, what you should generate.

[00:27:12] The problem I think here is there is a real trade off of like, you do need to run this model somewhere. You need to run it on a piece of hardware. So then it comes down to how much memory does that piece of hardware have. Let's say for a fixed compute budget, you could train a 70 billion parameter. What are you gonna put that on?

[00:27:31] Yeah, maybe you could, could you put that on an 80 gig, A 100? It would be a stretch. You could do things like f, you know, in eight F p a, to reduce the amount of memory that's on the box and do all these other things. But you have to think about that first, right? When you want to go out and train that model.

[00:27:47] The worst case is you ended up training that mo, that model, and you cannot serve it. So actually what you end up finding is for a lot of these code completion models, they are actually what you would consider over-trained . So by that I mean like, let's look at a model like Cogen. It's actually trained on, I believe, and, and I could be wrong by, you know, a hundred billion here or there.

[00:27:59] I got some data. Oh, okay. Let's look at the 3 billion parameter model. It's a 2.7. I think it's actually a 2.7 billion barometer model. It's weird because they also trained on natural language on top of code, but it's trained on hundreds of billions of tokens. If you applied that chinchilla, Optimization to it, you'd be like, wow, this is, this is a stupid use of compute.

[00:28:18] Right? Because three, they should be going to 60, any anything more than 60. And they're like, they should have just increased the model size. But the reality is if they had like the compute optimal one might not be one that's easy to serve, right? It could just have more parameters. And for our case, our models that we train internally, they might not be the most compute.

[00:28:36] In other words, we probably could have had a better model by making it larger, but the trade off would've been latency. We know what the impact of having higher latency is, and on top of that, being able to fit properly on our hardware constraints would've also been a concern.

**Swyx** [00:28:56] Isn't the classic stopping point when you, you see like loss kind of levels off.

[00:28:56] Right now you're just letting chinchilla tell you,

**Varun Mohan** [00:29:12] but like you should just look at loss. The problem is the loss will like continue to go down. It'll just continue to go down like, like in a, in a way that's like not that pleasing. It's gonna take longer and longer. It's gonna be painful, but it's like one of those things where if you look at the perplexity number of difference between.

[00:29:12] Let's say a model that's like 70 billion versus 10 billion. It's not massive. It's not like tens of percentage points. It's like very small, right? Mm. The reality is here, like, I mean this comes down to like IQ of like these models in some sense, like small wins at the margins are massive wins in terms of iq.

[00:29:31] Like it's harder to get those and they don't look as big, but they're like massive wins in terms of reasoning. They can now do chain of thought, all these other things. Yeah, yeah, yeah.

**Swyx** [00:29:47] It's, and, and so apparently unlocked around the

**Varun Mohan** [00:29:47] 20 billion. Yes. That's right. Some kind of magic. Yeah. I think that was from the UL two or maybe one of those land papers.

[00:29:47] Any thoughts on why? Like is there is? I don't know. I mean, emergence of intelligence, I think. I think maybe one of the things is like we don't even know, maybe like five years from now of what we're gonna be running are transformers. But I think it's like, we don't, we don't 100% know that that's true. I mean, there's like a lot of maybe issues with the current version of the transformers, which is like the way attention works, the attention layers work, the amount of computers quadratic in the context sense, because you're like doing like an n squared operation on the attention blocks basically.

[00:30:03] And obviously, you know, one of the things that everyone wants right now is infinite context. They wanna shove as much prop as possible in here. And the current version of what a transformer looks like is maybe not ideal. You might just end up burning a lot of flops on this when there are probably more efficient ways of doing it.

[00:30:30] So I'm, I'm sure in the future there's gonna be tweaks to this. Yeah. Uh, but it is interesting that we found out interesting things of like, hey, bigger is pretty much always better. There are probably ways of making smaller models significantly better through better data. That is like definitely true. Um, And I think one of the cool things that the stack showed actually was they did a, like a, I think they did some ablation studies where they were like, Hey, what happens if we do, if we do decontamination of our data, what happens if we do de-duplication?

[00:30:45] What happens if we do near dup of our data and how does the model get better? And they have like some compelling results that showcase data quality really matters here, but ultimately, Yeah, I think it is an interesting result that at 20 billion there's something happening. But I also think like some of these things in the future may look materially different than what they look like right now.

[00:31:14] Hmm. Do you think

**Alessio Fanelli** [00:31:30] the token limitation is actually a real architectural limitation? Like if you think about the tokens need as kind of like atic, right? Like once you have. 50,000 tokens context, like 50,000 or infinite. For most use cases, it's like the same. Where do you think that number is, especially as you think about code, like some people have very large code bases, there's a lot.

[00:31:30] Have you done any work there to figure out where the sweet

**Varun Mohan** [00:31:53] spot is? Yeah, look, I think what's gonna really end up happening is if people come up with a clever way and, and it, there was some result research that I believe came out of Stanford. I think the team from the Helm group, I think came out with some architecture that looks a little bit different than Transformers, and I'm sure something like this will work in the future.

[00:31:53] What I think is always gonna happen is if you find a cheap way to embed context, people are gonna figure out a way to, to put as much as possible in because L LM so far have been like virtually stateless. So the only thing that they have beyond fine tuning is like just shoveling everything you can inside.

[00:32:13] And there are some interesting papers, like retro, actually there are maybe some interesting pieces of thought like ideas that have come out recently. Yeah, let's go through them. So one of the really interesting ideas, I think is retro. It's this paper that came out of DeepMind and the idea is actually, let's say you send out, you send out, uh, a prompt.

[00:32:28] Okay? Send out a prompt. You compute the burt embedding of that. And then you have this massive embedding database. And by massive, I'm not talking about like gigabytes, I'm talking about terabytes. Like you have, geez, you actually have 10 times the number of tokens as what was used to train the model. So like, let's say you had a model that was trained on a trillion tokens, you have a 10 trillion embed, uh, like embedding database.

[00:32:44] And obviously Google has this because they have all content that ever existed in humanity and they have like the best data set and sort of, they were able to make one of these, uh, embedding databases. But the idea here, which is really cool, is you end. Taking your prompt, computing, the bird, embedding you find out the things that were nearby.

[00:33:04] So you do roughly like a semantic search or an embedding search within that. And then you take those, you take the documents that were from those embeddings and you shove those in the model too, in what are called like cross chunked attention. So you like shove them in the model with it as well.

[00:33:20] Suddenly now the model is able to take in external. Which is really exciting actually, because suddenly now you're able to get dynamic context in, and the model in some sense is deciding what that context is. It's not deciding it completely. In this case, because the Bert model in this case was actually frozen.

[00:33:34] It wasn't trained with the retro model as well, but. The idea is you're somehow adding or augmenting context, which I think is like quite exciting. There's probably two futures. Either context becomes really cheap. Right now it's quadratic. Maybe there's a future where it becomes linear in the, in the size of the context, but the future might actually be the model itself dictates, Hey, I have this context.

[00:33:50] You have this data source. Give me this. The model itself is going out into your database and like being like, I want this information, and this is kind of like. What Bing search is looking like. Right? Or bing chat is sort of looking like where it's like I, the model is probably, there's probably some model that's saying I want this information.

[00:34:10] And that is getting augmented into the context. Now the model itself knows what context it sort of has and it can sort of like build a state machine of sort of what it needs. And that's probably what the future of this looks like. So you, you

**Swyx** [00:34:27] predict monster embedding database

**Varun Mohan** [00:34:27] companies? Probably Monster embedding database companies or, yeah.

[00:34:27] The model in some sense will need to talk to, Talk to these embedding databases. I'm actually not convinced that the current breed of embedding database companies are like ready for what the future sort of looks like. I think I'm just looking at their pricing, how much it costs per gigabyte and it's prohibitive at the scale we're talking about, like let's say you actually did want to host a 10 terabyte embedding database.

[00:34:43] A lot of them were created, let's say two years ago, two, three years ago, where people were like, you know, embedding databases are small and they need to make the cost economics work. But maybe, yeah, there's probably gonna be a big workload there. I will just say for us, we will probably just build this in-house to start with, and that's because I think the technology probably isn't there.

[00:35:03] And I think that the technology isn't there yet. Like waiting on point solutions to come up is a lot harder, um, than probably building it up. The way I, I like to think about this is probably the world looks on the LM space. Looks like how the early internet days were, where I think the value was accrued to probably like Google and Google needed to figure out all the crazy things to make their workload work.

[00:35:20] And the reason why they weren't able to outsource is, is no one else was feeling the pain. ,

**Swyx** [00:35:41] they're just solving their own pain points. They're just solving their own pain points. They're so far ahead of everyone else. Yes, yes. And just wait

**Varun Mohan** [00:35:41] for people to catch up. Yes. Yes. And that's maybe different than how things like Snowflake look where the interface has been decided for what SQL looks like 50 years ago.

[00:35:41] And because of that, you can go out and build the best database and Yeah, like everyone's gonna be like, this doesn't make my beer taste better. And buy your database basically. That's

**Swyx** [00:35:58] a great reference, by the way. Yeah. We have some friends of the, the pod that are working on embedding database, so we'll try to connect you Toroma

**Varun Mohan** [00:35:58] and see.

[00:35:58] Yeah. Oh, I actually know Anton. I worked with him at Neuro. Oh. Although, there you go. Yeah. Uh, what do you, well, what do you think about, I mean,

**Swyx** [00:36:14] so chromas pivoting towards an embedding

**Varun Mohan** [00:36:14] database. I think it's an interesting idea. I think it's an interesting idea. I wonder what the early set of workloads that.

[00:36:14] They will hit our, and you know what the scaling requirements are. This is maybe the classic thing where like, the teams are great, but you need to pick a workload here that you care about the most. You could build anything. You could build anything. When you're an infrastructure company, you can go in, if I was selling, serving in for, I could build, serving for like linear aggression.

[00:36:27] I could build this, but like, unless you hit the right niche for the end user, it's gonna be. . So I think it, I'm excited to see what comes out and if they're great, then we'll use it. Yeah.

**Swyx** [00:36:44] I also like how you slowly equated yourself to Google there. Oh, we're not, we're not Google. You're, you're gonna be the Google of ai.

**Varun Mohan** [00:36:44] We're definitely, we're definitely not Google. But I was just saying in terms of like, if you look at like the style of companies that came out. Yeah. You know? Absolutely. Or maybe we should live in the cutting edge in

**Swyx** [00:36:44] the future. Yeah. I think that's the pitch.

**Varun Mohan** [00:36:44] Okay, thanks for bitch us.

**Alessio Fanelli** [00:36:44] So you just mentioned the older vector embedding source are kind of not made for the L l M generation of compute size.

[00:36:44] what does l LM ops look like? You know, which pieces need to be drastically different? Which ones can we recycle?

**Varun Mohan** [00:37:21] Yeah. One of the things that we've found, like in our own thing of building code that's been just shows how much is missing, and this is the thing where like, I don't know how much of this you can really outsource, which is like we needed to build eval infrastructure.

[00:37:21] That means how do you build a great code? And there are things online like human eval, right? And uh, I was telling, which is the benchmark telling Sean about this, the idea of human eval is really neat for code. The idea is you provide a bunch of functions with Docstrings and the eval instead of being, did you predict next token?

[00:37:40] It's like, did you generate the entire function and does the function run correctly against a bunch of unit tests? Right. And we've built more sophisticated evals to work on many languages, to work on more variety of code bases. One of the issues that ends up coming up with things like human eval is contam.

[00:37:56] Because a lot of these, uh, things that train models end up training on all of GitHub GitHub itself has human eva, so they end up training on that. And then the numbers are tiny, though. It's gonna be tiny, right? But it doesn't matter if it's tiny because it'll just remember it. It'll remember that it's, it's not that it's that precise, but it will, it's like, it's basically like mixing your, your training and validation set.

[00:38:12] It's like, oh, yeah, yeah, yeah, yeah. But we've seen cases where like online where someone is like, we have a code model that's like, they we're like, we did this one thing, and HU and human eval jumped a ton and we were just like, huh, did human eval get into your data set? Is that really what happened there?

[00:38:32] But we've needed to build all this eval. And what is shown is data cleaning is massive, but data cleaning looks different by. Like code data cleaning is different than what is a high quality piece of code is probably different than what's a high quality legal document. Yeah. And then on top of that, how do you eval this?

[00:38:46] How do you also train it at scale at whatever cost you really want to get? But those are things that the end user is either gonna need to solve or someone else is gonna need to solve for them. And I guess maybe one of the things I'm a little bearish on is if another company comes out and solves eval properly for a bunch of different verticals, what was the company that they were selling to really?

[00:39:01] What were they really doing at that point? If they themselves were not eval for their own workload and all these other things? I think there are cases where, let's say for code where we probably couldn't outsource our eval, like we wouldn't be able to ship models internally if we didn't know how to eval, but it's clear that there's a lot of different things that people need to take.

[00:39:21] Like, Hey, maybe there's an embedding piece. How large is this embedding database actually need to be? But hey, this does look very different than what classic ML ops probably did. Mm-hmm. . How

**Alessio Fanelli** [00:39:38] do you compare some of these models? Like when you're thinking about model upgrading and making changes, like what does the testing piece of it internally?

[00:39:38] Yeah. For us look like.

**Varun Mohan** [00:39:56] For us, it's like old school AB testing. We've built like infrastructure to be able to say, ramp up users from one to 10 to. 50% and slowly roll things out. This is all classic software, uh, which

**Swyx** [00:39:56] you do in-house. You don't, you don't buy any

**Varun Mohan** [00:39:56] services. We don't buy services for that.

[00:39:56] There are good services, open source services that help you just don't need them. Uh, yeah, I think that's just like not the most complicated thing for us. Sure. Basically. Yeah. Uh, but I think in the future, maybe, we'll, obviously we use things like Google Analytics and all this other stuff, but Yeah. For things of ramping our models, finding out if they're actually better because the eval also doesn't tell the whole story because also for us, Even before generating the prompt, we do a lot of work.

[00:40:13] And the only way to know that it's really good across all the languages that our users need to tell us that it's actually good. And, and they tell us by accepting completions. So, so GitHub

**Swyx** [00:40:36] co-pilot, uh, the extension does this thing where they, they like, they'll set a timer and then within like five minutes, 10 minutes, 20 minutes, they'll check in to see if the code is still there.

[00:40:36] I thought it was a

**Varun Mohan** [00:40:54] pretty creative way. It's, it's a very, it's honestly a very creative way. We do do things to see, like in the long term, if people did. Accept or write things that are roughly so because they could accept and then change their minds. They could accept and then change their minds. So we, we are mindful of, of things like that.

[00:40:54] But for the most part, the most important metric is at the time, did they actually, did we generate value? And we want to know if that's true. And it's, it's kind of, it's honestly really hard to get signal unless you have like a non-trivial amount of usage, non-trivial, meaning you're getting, you're doing hundreds of thousands of completions, if not millions of completions.

[00:41:09] That sounds like, oh wow. Like, that's like a very small amount. But like it's classic. Maybe like if you look at like when I used to be an intern at Quora, like, you know, now more than seven, eight years ago. When I was there, I like shipped a change and then Cora had like millions of daily actives and then it looked like it was good, and then a week later it was just like way worse.

[00:41:25] And how is this possible? Like in a given hour we get like hundreds of thousands of interaction, just like, no, you just need way more data. So this is like one of those things where I think having users is like genuinely very valuable to us, basically. Users is all you need. . Yeah.

**Swyx** [00:41:43] Um, by the way, since you brought out Quora, have you tried po any, any thoughts

**Varun Mohan** [00:41:43] on po I have not actually tried po I've not actually tried.

[00:41:43] I

**Swyx** [00:42:05] mean, it seems like a question answering website that's been around for 20 years or something. Would be very, would be very good at question answering. Yeah.

**Varun Mohan** [00:42:05] Also Adam, the ceo, is like incredibly brilliant. That guy is like insanely smart, so I'm sure they're gonna do,

**Swyx** [00:42:05] they have accidentally built the perfect like data collection company for For qa.

**Varun Mohan** [00:42:05] Yeah. . It takes a certain kind of person to go and like cannibalize your original company like the in, I mean, it was kinda stagnant for like a few years. Yeah, that's probably true. That's

**Swyx** [00:42:05] probably true. The observation is I feel like you have a bias to its domain specific. , whereas most research is skewed towards, uh, general models, general purpose models.

[00:42:05] I don't know if there's like a, a deeper insight here that you wanna go into or, or not, but like, train on all the things, get all the data and you're like, no, no, no. Everyone needs like customized per task,

**Varun Mohan** [00:42:40] uh, data set. Yeah. I think I'm not gonna. Say that general intelligence is not good. You want a base model that's still really good and that's probably trained on normal text, like a lot of different content.

[00:42:40] But I think probably one thing that old school machine learning, even though I'm like the kind of person that says a lot of old school machine learning is just gonna die, is that training on a high quality data set for your workload is, is always gonna yield better results and more, more predictable results.

[00:43:00] And I think we are under no illusions that that's not the case. Basical. And

**Swyx** [00:43:15] then the other observation is bandwidth and connectivity, uh, which is not something that people usually think about, but apparently is a, is a big deal. Apparently training agreed in the synchronous needs, high GPU coordination.

[00:43:15] These are deleted notes from Sam Altman talking about how they think about training and I was like, oh yeah, that's an insight. And

**Varun Mohan** [00:43:29] you guys have the same thing. Yeah. So I guess for, for training, you're right in that it is actually nuts to think about how insane the networks are for NVIDIA's most recent hardware, it's.

[00:43:29] For the H 100 boxes, you shove eight of these H 100 s on a. Between two nodes. The bandwidth is 3,200 gigabits a second, so 400 gigabytes a second between machines. That's like nuts when you just sit and think about it. That's like double the memory bandwidth of what a CPU has, but it's like between two machines.

[00:43:46] On top of that, within the machine, they've created this, this fabric called envy link that allows you to communicate at ultra low latency. That's even lower than P C I E. If you're familiar, that's like the communication protocol. . Yeah, between like the CPU and the other devices or other P C I E devices.

[00:44:04] All of this is to make sure that reductions are fast, low latency, and you don't need to think about it. And that's because like a lot of deep learning has sort of evolved. Uh, training has evolved to be synchronous in the OG days. There is a lot of analysis in terms of how good is asynchronous training, which is like, Hey, I have a node, it has a current state of the model.

[00:44:21] It's gonna update that itself locally, and it'll like every once in a while, go to another machine and update the weights. But I think like everyone has converged to synchronous. I'm not exactly sure. There's not a lot of good research on asynchronous training right now. Or maybe there is an, I haven't read it.

[00:44:39] It's just that there isn't as much research because people are just like, oh, synchronous works. Uh, and the hardware is continually upleveled to handle

**Swyx** [00:44:52] that. Yeah. It was just un unintuitive to me cuz like the whole purpose of GPUs could train things. A lot of things in parallel. Yes.

**Varun Mohan** [00:44:52] But the crazy thing is also, maybe I can, I can give some dumb math here.

[00:44:52] Sure. Here, which is that, uh, let's go with uh, G B T three, which is like 170 billion per. The optimizer state, so while you're training is 14 times the size of the model, so in this case, if it's like 170 billion parameters, it's probably, I'm not great at mental math here, but that's probably around 2.5 terabytes to just store the optimizer state.

[00:45:09] That has gotta be sharded across a lot of machines. Like that is not a single gpu. Even if you take an H 100 with 80 gigs to just shard that much, that's like 40, at least 30 machines. So there's like something there where these things need to communicate with each other too.

**Swyx** [00:45:30] You need to vertically scale horizontally.

**Varun Mohan** [00:45:30] Yeah. You gotta co-located, you gotta somehow feel like you have this massive, the, the ideal programming paradigm is you feel like you have this massive computer. That has no communication, you know, overhead at all, but it has like infinite computer and infinite memory bandwidth.

**Swyx** [00:45:30] That's the AI cluster. Um, okay, well, uh, we want to head to the questions.

**Alessio Fanelli** [00:45:30] So favorite AI product that you are not

**Varun Mohan** [00:45:30] building? Yeah, I'm friends with some of the folks at Mid Journey and I really think the Mid Journey product is super cool, especially seeing how the team is iterating and the quality of generations. It consistently gets upleveled. I think it's like quite neat and I think internally at at exa functional, we've been trying out mid Journey for like random content to like generate images and stuff.

[00:45:30] Does it bother

**Swyx** [00:46:26] you that they have like a style. I don't know. It, it seems like they're hedging themselves into a particular, like you want mid journey art, you go there.

**Varun Mohan** [00:46:26] Yeah. It's a brand of art. Yeah, you're right. I think they do have a style, but it seems more predictably good for that style. Okay. So maybe that's too, so just get good at, uh, domain specific thing.

[00:46:26] Yeah. Yeah. maybe. Maybe I, maybe I'm just selling, talking to a booker right now. . Yeah. Uh, okay.

**Swyx** [00:46:41] Uh, next question. Uh, favorite AI people and

**Varun Mohan** [00:46:41] communities? Yeah, so I think I mentioned this before, but I think obviously the open. The opening eye folks are, are insane. Like we, we only have respect for them. But beyond that, I think Elu is a pretty special group.

[00:46:41] Especially it's been now probably more than a year and a half since they released like G P T J, which was like back when open source G PT three Curri, which was comparable. And it wasn't like a model where like, It wasn't good. It was like comparable in terms of perplexity to GT three curity and it was trained by a university student actually, and it just showed that, you know, in the end, like I would say pedigree is great, but in if you have people that are motivated know how computers work and they're willing to just get their hands dirty, you can do crazy things and that was a crazy project that gave me more hope.

[00:46:59] Decentral training being potentially pretty massive. But I think that was like a very cool thing where a bunch of people just got on Discord and were chatting and they were able to just turn this out. Yeah. I did

**Swyx** [00:47:34] not know this until I looked in further into Luther, but it was not a formal organization.

[00:47:34] Was a company was a startup. It's not, yeah. Bunch of guys on Discord.

**Varun Mohan** [00:47:45] They gotta you, they gotta keep you research grant and they somehow just wrote some codes. .

**Alessio Fanelli** [00:47:45] Yeah. Yeah. Listen to APAC with Connor, who's the person, and basically Open Eye at the time was like, we cannot release G P T because it's like too good and so bad.

[00:47:45] And he was like, He actually said he was sick, so he couldn't leave home for like a, a few weeks. So it was like, what else am I gonna do? And ended up getting through the Google like research programs through his university and they were like, oh, we'll give you TPUs. And he was like, cool. And that's how, that's,

**Varun Mohan** [00:48:01] that's amazing.

[00:48:01] So I came to you. I love the story. Yeah, it's a great story. .

**Alessio Fanelli** [00:48:18] So a year from now, what do you think people will be most surprised by

**Varun Mohan** [00:48:18] In ai? Yeah. I think the thing people will be most surprised by is, I think they, the models are gonna, More good at SP special tasks for sure, but even the existing models, I think people will come up with more creative ways of leveraging them to build like world class products.

[00:48:18] I think that's just like human creativity is gonna go wild. It seems like Cha GBT has already kind of unleashed that. I think I'm just excited to see what the future of these products look like. I guess law was not something I expected in such a short, well,

**Swyx** [00:48:39] totally expected. I, I, I was actually watching a different company that I thought was gonna be the winner, and then Harvey just came outta nowhere,

[00:48:39] Oh, wow. Okay. Okay. Well that's, that's awesome. But yeah. So my, my takeaway from what you're saying is like, foundation models have kind of shot way too far ahead of the apps and people need to build

**Varun Mohan** [00:48:56] apps. Yes. I think people should be building apps, but I. The reality is the model is like probably at a state right now where it can do crazy enough things.

[00:48:56] Uh, and I think great apps will, will come out of this. Yeah.

**Swyx** [00:49:12] AI thing you would pay for if someone else built it personal or work.

**Varun Mohan** [00:49:12] I think if, if someone else built like a proper assistant, like a proper like fitness assistant, I would probably pay for that actually. I know that, that sounds weird, but someone that actually tells me like, how should I end up, like, you know, doing fitness today, I ended up injuring my knee from over biking.

[00:49:12] I ended up biking like 150 miles a week and I ended up just injuring my knee outta nowhere. So, so you need, you need an app to tell you to exercise less. Exercise less, but tell me what my training regimen is. Uh, tell me what I should do to prepare for things. I know that this is like a big niche, but I think the fact that Strava is such a big group of people and like swyx is a big group of people, seems to suggest that I think a lot of people would be willing to pay for something like this.

**Alessio Fanelli** [00:49:35] what's one thing you want everyone to take away about AI and our

**Varun Mohan** [00:49:35] conversation? Probably the most important thing to take away is there's probably a lot out there if people continue to tinker. I think that's probably like the biggest takeaway I've had. Uh, and it's, you know, being a pure infrastructure company, I think like, uh, six to eight months ago, I think it was like very hard to watch everyone tinkering and us just, you know, building, building infrastructure.

[00:49:35] But I think there's gonna be some crazy things that come out over the next year or. Um, excited to just see what that looks like. Awesome. Yeah, man. That's it. This was fantastic. Thanks so much. Thanks for coming.
