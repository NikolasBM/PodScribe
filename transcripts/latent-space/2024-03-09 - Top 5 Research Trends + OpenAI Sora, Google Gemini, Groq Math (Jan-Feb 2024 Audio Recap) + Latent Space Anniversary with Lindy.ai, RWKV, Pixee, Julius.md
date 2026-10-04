---
podcast: "latent-space"
podcast_title: "Latent Space"
title: "Top 5 Research Trends + OpenAI Sora, Google Gemini, Groq Math (Jan-Feb 2024 Audio Recap) + Latent Space Anniversary with Lindy.ai, RWKV, Pixee, Julius.ai, Listener Q&A!"
date: 2024-03-09
url: "https://www.latent.space/p/jan-feb-2024-recap-audio"
guid: "substack:142431075"
host: "Swyx"
transcript_source: "publisher"
---

# Top 5 Research Trends + OpenAI Sora, Google Gemini, Groq Math (Jan-Feb 2024 Audio Recap) + Latent Space Anniversary with Lindy.ai, RWKV, Pixee, Julius.ai, Listener Q&A!

**AI Charlie** [00:00:00] Welcome to the Latent Space podcast, weekend edition. This is Charlie, your new AI co host. Happy weekend. As an AI language model, I work the same every day of the week, although I might get lazier towards the end of the year. Just like you. Last month, we released our first monthly recap pod, where Swyx and Alessio gave quick takes on the themes of the month, and we were blown away by your positive response.

**AI Charlie** [00:00:00] We're delighted to continue our new monthly news recap series for AI engineers. Please feel free to submit questions by joining the Latent Space Discord, or just hit reply when you get the emails from Substack. This month, we're covering the top research directions that offer progress for text LLMs, and then touching on the big Valentine's Day gifts we got from Google, OpenAI, and Meta.

**AI Charlie** [00:00:00] Watch out and take care.

**Alessio** [00:00:00] Hey everyone, welcome to the Latent Space Podcast. This is Alessio, partner and CTO of Residence at Decibel Partners, and we're back with a monthly recap with my co host

**Swyx** [00:00:00] Swyx. The reception was very positive for the first one, I think people have requested this and no surprise that I think they want to hear us more applying on issues and maybe drop some alpha along the way I'm not sure how much alpha we have to drop, this month in February was a very, very heavy month, we also did not do one specifically for January, so I think we're just going to do a two in one, because we're recording this on the first of March.

**Alessio** [00:00:00] Yeah, let's get to it. I think the last one we did, the four wars of AI, was the main kind of mental framework for people. I think in the January one, we had the five worthwhile directions for state of the art LLMs. Four, five,

**Swyx** [00:00:00] and now we have to do six, right? Yeah.

**Alessio** [00:00:00] So maybe we just want to run through those, and then do the usual news recap, and we can do

**Swyx** [00:00:00] one each.

**Swyx** [00:00:00] So the context to this stuff. is one, I noticed that just the test of time concept from NeurIPS and just in general as a life philosophy I think is a really good idea. Especially in AI, there's news every single day, and after a while you're just like, okay, like, everyone's excited about this thing yesterday, and then now nobody's talking about it.

**Swyx** [00:00:00] So, yeah. It's more important, or better use of time, to spend things, spend time on things that will stand the test of time. And I think for people to have a framework for understanding what will stand the test of time, they should have something like the four wars. Like, what is the themes that keep coming back because they are limited resources that everybody's fighting over.

**Swyx** [00:00:00] Whereas this one, I think that the focus for the five directions is just on research that seems more proMECEng than others, because there's all sorts of papers published every single day, and there's no organization. Telling you, like, this one's more important than the other one apart from, you know, Hacker News votes and Twitter likes and whatever.

**Swyx** [00:00:00] And obviously you want to get in a little bit earlier than Something where, you know, the test of time is counted by sort of reference citations.

## [00:02:59] The Five Research Directions

**Alessio** [00:00:00] Yeah, let's do it. We got five. Long inference.

**Swyx** [00:00:00] Let's start there. Yeah, yeah. So, just to recap at the top, the five trends that I picked, and obviously if you have some that I did not cover, please suggest something.

**Swyx** [00:00:00] The five are long inference, synthetic data, alternative architectures, mixture of experts, and online LLMs. And something that I think might be a bit controversial is this is a sorted list in the sense that I am not the guy saying that Mamba is like the future and, and so maybe that's controversial.

## [00:03:31] Direction 1: Long Inference (Planning, Search, AlphaGeometry, Flow Engineering)

**Swyx** [00:00:00] But anyway, so long inference is a thesis I pushed before on the newsletter and on in discussing The thesis that, you know, Code Interpreter is GPT 4. 5. That was the title of the post. And it's one of many ways in which we can do long inference. You know, long inference also includes chain of thought, like, please think step by step.

**Swyx** [00:00:00] But it also includes flow engineering, which is what Itamar from Codium coined, I think in January, where, basically, instead of instead of stuffing everything in a prompt, You do like sort of multi turn iterative feedback and chaining of things. In a way, this is a rebranding of what a chain is, what a lang chain is supposed to be.

**Swyx** [00:00:00] I do think that maybe SGLang from ElemSys is a better name. Probably the neatest way of flow engineering I've seen yet, in the sense that everything is a one liner, it's very, very clean code. I highly recommend people look at that. I'm surprised it hasn't caught on more, but I think it will. It's weird that something like a DSPy is more hyped than a Shilang.

**Swyx** [00:00:00] Because it, you know, it maybe obscures the code a little bit more. But both of these are, you know, really good sort of chain y and long inference type approaches. But basically, the reason that the basic fundamental insight is that the only, like, there are only a few dimensions we can scale LLMs. So, let's say in like 2020, no, let's say in like 2018, 2017, 18, 19, 20, we were realizing that we could scale the number of parameters.

**Swyx** [00:00:00] 20, we were And we scaled that up to 175 billion parameters for GPT 3. And we did some work on scaling laws, which we also talked about in our talk. So the datasets 101 episode where we're like, okay, like we, we think like the right number is 300 billion tokens to, to train 175 billion parameters and then DeepMind came along and trained Gopher and Chinchilla and said that, no, no, like, you know, I think we think the optimal.

**Swyx** [00:00:00] compute optimal ratio is 20 tokens per parameter. And now, of course, with LLAMA and the sort of super LLAMA scaling laws, we have 200 times and often 2, 000 times tokens to parameters. So now, instead of scaling parameters, we're scaling data. And fine, we can keep scaling data. But what else can we scale?

**Swyx** [00:00:00] And I think understanding the ability to scale things is crucial to understanding what to pour money and time and effort into because there's a limit to how much you can scale some things. And I think people don't think about ceilings of things. And so the remaining ceiling of inference is like, okay, like, we have scaled compute, we have scaled data, we have scaled parameters, like, model size, let's just say.

**Swyx** [00:00:00] Like, what else is left? Like, what's the low hanging fruit? And it, and it's, like, blindingly obvious that the remaining low hanging fruit is inference time. So, like, we have scaled training time. We can probably scale more, those things more, but, like, not 10x, not 100x, not 1000x. Like, right now, maybe, like, a good run of a large model is three months.

**Swyx** [00:00:00] We can scale that to three years. But like, can we scale that to 30 years? No, right? Like, it starts to get ridiculous. So it's just the orders of magnitude of scaling. It's just, we're just like running out there. But in terms of the amount of time that we spend inferencing, like everything takes, you know, a few milliseconds, a few hundred milliseconds, depending on what how you're taking token by token, or, you know, entire phrase.

**Swyx** [00:00:00] But We can scale that to hours, days, months of inference and see what we get. And I think that's really proMECEng.

**Alessio** [00:00:00] Yeah, we'll have Mike from Broadway back on the podcast. But I tried their product and their reports take about 10 minutes to generate instead of like just in real time. I think to me the most interesting thing about long inference is like, You're shifting the cost to the customer depending on how much they care about the end result.

**Alessio** [00:00:00] If you think about prompt engineering, it's like the first part, right? You can either do a simple prompt and get a simple answer or do a complicated prompt and get a better answer. It's up to you to decide how to do it. Now it's like, hey, instead of like, yeah, training this for three years, I'll still train it for three months and then I'll tell you, you know, I'll teach you how to like make it run for 10 minutes to get a better result.

**Alessio** [00:00:00] So you're kind of like parallelizing like the improvement of the LLM. Oh yeah, you can even

**Swyx** [00:00:00] parallelize that, yeah, too.

**Alessio** [00:00:00] So, and I think, you know, for me, especially the work that I do, it's less about, you know, State of the art and the absolute, you know, it's more about state of the art for my application, for my use case.

**Alessio** [00:00:00] And I think we're getting to the point where like most companies and customers don't really care about state of the art anymore. It's like, I can get this to do a good enough job. You know, I just need to get better. Like, how do I do long inference? You know, like people are not really doing a lot of work in that space, so yeah, excited to see more.

**Swyx** [00:00:00] So then the last point I'll mention here is something I also mentioned as paper. So all these directions are kind of guided by what happened in January. That was my way of doing a January recap. Which means that if there was nothing significant in that month, I also didn't mention it. Which is which I came to regret come February 15th, but in January also, you know, there was also the alpha geometry paper, which I kind of put in this sort of long inference bucket, because it solves like, you know, more than 100 step math olympiad geometry problems at a human gold medalist level and that also involves planning, right?

**Swyx** [00:00:00] So like, if you want to scale inference, you can't scale it blindly, because just, Autoregressive token by token generation is only going to get you so far. You need good planning. And I think probably, yeah, what Mike from BrightWave is now doing and what everyone is doing, including maybe what we think QSTAR might be, is some form of search and planning.

**Swyx** [00:00:00] And it makes sense. Like, you want to spend your inference time wisely. How do you

**Alessio** [00:00:00] think about plans that work and getting them shared? You know, like, I feel like if you're planning a task, somebody has got in and the models are stochastic. So everybody gets initially different results. Somebody is going to end up generating the best plan to do something, but there's no easy way to like store these plans and then reuse them for most people.

**Alessio** [00:00:00] You know, like, I'm curious if there's going to be. Some paper or like some work there on like making it better because, yeah, we don't

**Swyx** [00:00:00] really have This is your your pet topic of NPM for

**Alessio** [00:00:00] Yeah, yeah, NPM, exactly. NPM for, you need NPM for anything, man. You need NPM for skills. You need NPM for planning. Yeah, yeah.

**Alessio** [00:00:00] You know I think, I mean, obviously the Voyager paper is like the most basic example where like, now their artifact is like the best planning to do a diamond pickaxe in Minecraft. And everybody can just use that. They don't need to come up with it again. Yeah. But there's nothing like that for actually useful

**Swyx** [00:00:00] tasks.

**Swyx** [00:00:00] For plans, I believe it for skills. I like that. Basically, that just means a bunch of integration tooling. You know, GPT built me integrations to all these things. And, you know, I just came from an integrations heavy business and I could definitely, I definitely propose some version of that. And it's just, you know, hard to execute or expensive to execute.

**Swyx** [00:00:00] But for planning, I do think that everyone lives in slightly different worlds. They have slightly different needs. And they definitely want some, you know, And I think that that will probably be the main hurdle for any, any sort of library or package manager for planning. But there should be a meta plan of how to plan.

**Swyx** [00:00:00] And maybe you can adopt that. And I think a lot of people when they have sort of these meta prompting strategies of like, I'm not prescribing you the prompt. I'm just saying that here are the like, Fill in the lines or like the mad libs of how to prompts. First you have the roleplay, then you have the intention, then you have like do something, then you have the don't something and then you have the my grandmother is dying, please do this.

**Swyx** [00:00:00] So the meta plan you could, you could take off the shelf and test a bunch of them at once. I like that. That was the initial, maybe, promise of the, the prompting libraries. You know, both 9chain and Llama Index have, like, hubs that you can sort of pull off the shelf. I don't think they're very successful because people like to write their own.

**Swyx** [00:00:00] Yeah,

## [00:11:37] Direction 2: Synthetic Data (WRAP, SPIN)

**Alessio** [00:00:00] yeah, yeah. Yeah, that's a good segue into the next one, which is synthetic

**Swyx** [00:00:00] data. Synthetic data is so hot. Yeah, and, you know, the way, you know, I think I, I feel like I should do one of these memes where it's like, Oh, like I used to call it, you know, R L A I F, and now I call it synthetic data, and then people are interested.

**Swyx** [00:00:00] But there's gotta be older versions of what synthetic data really is because I'm sure, you know if you've been in this field long enough, There's just different buzzwords that the industry condenses on. Anyway, the insight that I think is relatively new that why people are excited about it now and why it's proMECEng now is that we have evidence that shows that LLMs can generate data to improve themselves with no teacher LLM.

**Swyx** [00:00:00] For all of 2023, when people say synthetic data, they really kind of mean generate a whole bunch of data from GPT 4 and then train an open source model on it. Hello to our friends at News Research. That's what News Harmony says. They're very, very open about that. I think they have said that they're trying to migrate away from that.

**Swyx** [00:00:00] But it is explicitly against OpenAI Terms of Service. Everyone knows this. You know, especially once ByteDance got banned for, for doing exactly that. So so, so synthetic data that is not a form of model distillation is the hot thing right now, that you can bootstrap better LLM performance from the same LLM, which is very interesting.

**Swyx** [00:00:00] A variant of this is RLAIF, where you have a, where you have a sort of a constitutional model, or, you know, some, some kind of judge model That is sort of more aligned. But that's not really what we're talking about when most people talk about synthetic data. Synthetic data is just really, I think, you know, generating more data in some way.

**Swyx** [00:00:00] A lot of people, I think we talked about this with Vipul from the Together episode, where I think he commented that you just have to have a good world model. Or a good sort of inductive bias or whatever that, you know, term of art is. And that is strongest in math and science math and code, where you can verify what's right and what's wrong.

**Swyx** [00:00:00] And so the REST EM paper from DeepMind explored that. Very well, it's just the most obvious thing like and then and then once you get out of that domain of like things where you can generate You can arbitrarily generate like a whole bunch of stuff and verify if they're correct and therefore they're they're correct synthetic data to train on Once you get into more sort of fuzzy topics, then it's then it's a bit less clear So I think that the the papers that drove this understanding There are two big ones and then one smaller one One was wrap like rephrasing the web from from Apple where they basically rephrased all of the C4 data set with Mistral and it be trained on that instead of C4.

**Swyx** [00:00:00] And so new C4 trained much faster and cheaper than old C, than regular raw C4. And that was very interesting. And I have told some friends of ours that they should just throw out their own existing data sets and just do that because that seems like a pure win. Obviously we have to study, like, what the trade offs are.

**Swyx** [00:00:00] I, I imagine there are trade offs. So I was just thinking about this last night. If you do synthetic data and it's generated from a model, probably you will not train on typos. So therefore you'll be like, once the model that's trained on synthetic data encounters the first typo, they'll be like, what is this?

**Swyx** [00:00:00] I've never seen this before. So they have no association or correction as to like, oh, these tokens are often typos of each other, therefore they should be kind of similar. I don't know. That's really remains to be seen, I think. I don't think that the Apple people export

**Alessio** [00:00:00] that. Yeah, isn't that the whole, Mode collapse thing, if we do more and more of this at the end of the day.

**Swyx** [00:00:00] Yeah, that's one form of that. Yeah, exactly. Microsoft also had a good paper on text embeddings. And then I think this is a meta paper on self rewarding language models. That everyone is very interested in. Another paper was also SPIN. These are all things we covered in the the Latent Space Paper Club.

**Swyx** [00:00:00] But also, you know, I just kind of recommend those as top reads of the month. Yeah, I don't know if there's any much else in terms, so and then, regarding the potential of it, I think it's high potential because, one, it solves one of the data war issues that we have, like, everyone is OpenAI is paying Reddit 60 million dollars a year for their user generated data.

**Swyx** [00:00:00] Google, right?

**Alessio** [00:00:00] Not OpenAI.

**Swyx** [00:00:00] Is it Google? I don't

**Alessio** [00:00:00] know. Well, somebody's paying them 60 million, that's

**Swyx** [00:00:00] for sure. Yes, that is, yeah, yeah, and then I think it's maybe not confirmed who. But yeah, it is Google. Oh my god, that's interesting. Okay, because everyone was saying, like, because Sam Altman owns 5 percent of Reddit, which is apparently 500 million worth of Reddit, he owns more than, like, the founders.

**Alessio** [00:00:00] Not enough to get the data,

**Swyx** [00:00:00] I guess. So it's surprising that it would go to Google instead of OpenAI, but whatever. Okay yeah, so I think that's all super interesting in the data field. I think it's high potential because we have evidence that it works. There's not a doubt that it doesn't work. I think it's a doubt that there's, what the ceiling is, which is the mode collapse thing.

**Swyx** [00:00:00] If it turns out that the ceiling is pretty close, then this will maybe augment our data by like, I don't know, 30 50 percent good, but not game

**Alessio** [00:00:00] changing. And most of the synthetic data stuff, it's reinforcement learning on a pre trained model. People are not really doing pre training on fully synthetic data, like, large enough scale.

**Swyx** [00:00:00] Yeah, unless one of our friends that we've talked to succeeds. Yeah, yeah. Pre trained synthetic data, pre trained scale synthetic data, I think that would be a big step. Yeah. And then there's a wildcard, so all of these, like smaller Directions,

## [00:17:15] Wildcard: Multi-Epoch Training (OLMo, Datablations)

**Swyx** [00:00:00] I always put a wildcard in there. And one of the wildcards is, okay, like, Let's say, you have pre, you have, You've scraped all the data on the internet that you think is useful.

**Swyx** [00:00:00] Seems to top out at somewhere between 2 trillion to 3 trillion tokens. Maybe 8 trillion if Mistral, Mistral gets lucky. Okay, if I need 80 trillion, if I need 100 trillion, where do I go? And so, you can do synthetic data maybe, but maybe that only gets you to like 30, 40 trillion. Like where, where is the extra alpha?

**Swyx** [00:00:00] And maybe extra alpha is just train more on the same tokens. Which is exactly what Omo did, like Nathan Lambert, AI2, After, just after he did the interview with us, they released Omo. So, it's unfortunate that we didn't get to talk much about it. But Omo actually started doing 1. 5 epochs on every, on all data.

**Swyx** [00:00:00] And the data ablation paper that I covered in Europe's says that, you know, you don't like, don't really start to tap out of like, the alpha or the sort of improved loss that you get from data all the way until four epochs. And so I'm just like, okay, like, why do we all agree that one epoch is all you need?

**Swyx** [00:00:00] It seems like to be a trend. It seems that we think that memorization is very good or too good. But then also we're finding that, you know, For improvement in results that we really like, we're fine on overtraining on things intentionally. So, I think that's an interesting direction that I don't see people exploring enough.

**Swyx** [00:00:00] And the more I see papers coming out Stretching beyond the one epoch thing, the more people are like, it's completely fine. And actually, the only reason we stopped is because we ran out of compute

**Alessio** [00:00:00] budget. Yeah, I think that's the biggest thing, right?

**Swyx** [00:00:00] Like, that's not a valid reason, that's not science. I

**Alessio** [00:00:00] wonder if, you know, Matt is going to do it.

**Alessio** [00:00:00] I heard LamaTree, they want to do a 100 billion parameters model. I don't think you can train that on too many epochs, even with their compute budget, but yeah. They're the only ones that can save us, because even if OpenAI is doing this, they're not going to tell us, you know. Same with DeepMind.

**Swyx** [00:00:00] Yeah, and so the updates that we got on Lambda 3 so far is apparently that because of the Gemini news that we'll talk about later they're pushing it back on the release.

**Swyx** [00:00:00] They already have it. And they're just pushing it back to do more safety testing. Politics testing.

**Alessio** [00:00:00] Well, our episode with Sumit will have already come out by the time this comes out, I think. So people will get the inside story on how they actually allocate the compute.

## [00:19:38] Direction 3: Alt. Architectures (Mamba, RWKV, RingAttention, Diffusion Transformers)

**Alessio** [00:00:00] Alternative architectures. Well, shout out to our WKV who won one of the prizes at our Final Frontiers event last week.

**Alessio** [00:00:00] We talked about Mamba and Strapain on the Together episode. A lot of, yeah, monarch mixers. I feel like Together, It's like the strong Stanford Hazy Research Partnership, because Chris Ray is one of the co founders. So they kind of have a, I feel like they're going to be the ones that have one of the state of the art models alongside maybe RWKB.

**Alessio** [00:00:00] I haven't seen as many independent. People working on this thing, like Monarch Mixer, yeah, Manbuster, Payena, all of these are together related. Nobody understands the math. They got all the gigabrains, they got 3DAO, they got all these folks in there, like, working on all of this.

**Swyx** [00:00:00] Albert Gu, yeah. Yeah, so what should we comment about it?

**Swyx** [00:00:00] I mean, I think it's useful, interesting, but at the same time, both of these are supposed to do really good scaling for long context. And then Gemini comes out and goes like, yeah, we don't need it. Yeah.

**Alessio** [00:00:00] No, that's the risk. So, yeah. I was gonna say, maybe it's not here, but I don't know if we want to talk about diffusion transformers as like in the alt architectures, just because of Zora.

**Swyx** [00:00:00] One thing, yeah, so, so, you know, this came from the Jan recap, which, and diffusion transformers were not really a discussion, and then, obviously, they blow up in February. Yeah. I don't think they're, it's a mixed architecture in the same way that Stripe Tiena is mixed there's just different layers taking different approaches.

**Swyx** [00:00:00] Also I think another one that I maybe didn't call out here, I think because it happened in February, was hourglass diffusion from stability. But also, you know, another form of mixed architecture. So I guess that is interesting. I don't have much commentary on that, I just think, like, we will try to evolve these things, and maybe one of these architectures will stick and scale, it seems like diffusion transformers is going to be good for anything generative, you know, multi modal.

**Swyx** [00:00:00] We don't see anything where diffusion is applied to text yet, and that's the wild card for this category. Yeah, I mean, I think I still hold out hope for let's just call it sub quadratic LLMs. I think that a lot of discussion this month actually was also centered around this concept that People always say, oh, like, transformers don't scale because attention is quadratic in the sequence length.

**Swyx** [00:00:00] Yeah, but, you know, attention actually is a very small part of the actual compute that is being spent, especially in inference. And this is the reason why, you know, when you multiply, when you, when you, when you jump up in terms of the, the model size in GPT 4 from like, you know, 38k to like 32k, you don't also get like a 16 times increase in your, in your performance.

**Swyx** [00:00:00] And this is also why you don't get like a million times increase in your, in your latency when you throw a million tokens into Gemini. Like people have figured out tricks around it or it's just not that significant as a term, as a part of the overall compute. So there's a lot of challenges to this thing working.

**Swyx** [00:00:00] It's really interesting how like, how hyped people are about this versus I don't know if it works. You know, it's exactly gonna, gonna work. And then there's also this, this idea of retention over long context. Like, even though you have context utilization, like, the amount of, the amount you can remember is interesting.

**Swyx** [00:00:00] Because I've had people criticize both Mamba and RWKV because they're kind of, like, RNN ish in the sense that they have, like, a hidden memory and sort of limited hidden memory that they will forget things. So, for all these reasons, Gemini 1. 5, which we still haven't covered, is very interesting because Gemini magically has fixed all these problems with perfect haystack recall and reasonable latency and cost.

## [00:23:29] Wildcards: Text Diffusion, RALM/Retro

**Swyx** [00:00:00] So that's super interesting. So the wildcard I put in here if you want to go to that. I put two actually. One is text diffusion. I think I'm still very influenced by my meeting with a mid journey person who said they were working on text diffusion. I think it would be a very, very different paradigm for, for text generation, reasoning, plan generation if we can get diffusion to work.

**Swyx** [00:00:00] For text. And then the second one is Dowie Aquila's contextual AI, which is working on retrieval augmented language models, where it kind of puts RAG inside of the language model instead of outside.

**Alessio** [00:00:00] Yeah, there's a paper called Retro that covers some of this. I think that's an interesting thing. I think the The challenge, well not the challenge, what they need to figure out is like how do you keep the rag piece always up to date constantly, you know, I feel like the models, you put all this work into pre training them, but then at least you have a fixed artifact.

**Alessio** [00:00:00] These architectures are like constant work needs to be done on them and they can drift even just based on the rag data instead of the model itself. Yeah,

**Swyx** [00:00:00] I was in a panel with one of the investors in contextual and the guy, the way that guy pitched it, I didn't agree with. He was like, this will solve hallucination.

**Alessio** [00:00:00] That's what everybody says. We solve

**Swyx** [00:00:00] hallucination. I'm like, no, you reduce it. It cannot,

**Alessio** [00:00:00] if you solved it, the model wouldn't exist, right? It would just be plain text. It wouldn't be a generative model. Cool. So, author, architectures, then we got mixture of experts. I think we covered a lot of, a lot of times.

## [00:24:56] Direction 4: Mixture of Experts (DeepSeekMoE, Samba-1)

**Alessio** [00:00:00] Maybe any new interesting threads you want to go under here?

**Swyx** [00:00:00] DeepSeq MOE, which was released in January. Everyone who is interested in MOEs should read that paper, because it's significant for two reasons. One three reasons. One, it had, it had small experts, like a lot more small experts. So, for some reason, everyone has settled on eight experts for GPT 4 for Mixtral, you know, that seems to be the favorite architecture, but these guys pushed it to 64 experts, and each of them smaller than the other.

**Swyx** [00:00:00] But then they also had the second idea, which is that it is They had two, one to two always on experts for common knowledge and that's like a very compelling concept that you would not route to all the experts all the time and make them, you know, switch to everything. You would have some always on experts.

**Swyx** [00:00:00] I think that's interesting on both the inference side and the training side for for memory retention. And yeah, they, they, they, the, the, the, the results that they published, which actually excluded, Mixed draw, which is interesting. The results that they published showed a significant performance jump versus all the other sort of open source models at the same parameter count.

**Swyx** [00:00:00] So like this may be a better way to do MOEs that are, that is about to get picked up. And so that, that is interesting for the third reason, which is this is the first time a new idea from China. has infiltrated the West. It's usually the other way around. I probably overspoke there. There's probably lots more ideas that I'm not aware of.

**Swyx** [00:00:00] Maybe in the embedding space. But the I think DCM we, like, woke people up and said, like, hey, DeepSeek, this, like, weird lab that is attached to a Chinese hedge fund is somehow, you know, doing groundbreaking research on MOEs. So, so, I classified this as a medium potential because I think that it is a sort of like a one off benefit.

**Swyx** [00:00:00] You can Add to any, any base model to like make the MOE version of it, you get a bump and then that's it. So, yeah,

**Alessio** [00:00:00] I saw Samba Nova, which is like another inference company. They released this MOE model called Samba 1, which is like a 1 trillion parameters. But they're actually MOE auto open source models.

**Alessio** [00:00:00] So it's like, they just, they just clustered them all together. So I think people. Sometimes I think MOE is like you just train a bunch of small models or like smaller models and put them together. But there's also people just taking, you know, Mistral plus Clip plus, you know, Deepcoder and like put them all together.

**Alessio** [00:00:00] And then you have a MOE model. I don't know. I haven't tried the model, so I don't know how good it is. But it seems interesting that you can then have people working separately on state of the art, you know, Clip, state of the art text generation. And then you have a MOE architecture that brings them all together.

**Swyx** [00:00:00] I'm thrown off by your addition of the word clip in there. Is that what? Yeah, that's

**Alessio** [00:00:00] what they said. Yeah, yeah. Okay. That's what they I just saw it yesterday. I was also like

**Swyx** [00:00:00] scratching my head. And they did not use the word adapter. No. Because usually what people mean when they say, Oh, I add clip to a language model is adapter.

**Swyx** [00:00:00] Let me look up the Which is what Lava did.

**Alessio** [00:00:00] The announcement again.

**Swyx** [00:00:00] Stable diffusion. That's what they do. Yeah, it

**Alessio** [00:00:00] says among the models that are part of Samba 1 are Lama2, Mistral, DeepSigCoder, Falcon, Dplot, Clip, Lava. So they're just taking all these models and putting them in a MOE. Okay,

**Swyx** [00:00:00] so a routing layer and then not jointly trained as much as a normal MOE would be.

**Swyx** [00:00:00] Which is okay.

**Alessio** [00:00:00] That's all they say. There's no paper, you know, so it's like, I'm just reading the article, but I'm interested to see how

## [00:28:20] Wildcard: Model Merging (mergekit)

**Swyx** [00:00:00] it works. Yeah, so so the wildcard for this section, the MOE section is model merges, which has also come up as, as a very interesting phenomenon. The last time I talked to Jeremy Howard at the Olama meetup we called it model grafting or model stacking.

**Swyx** [00:00:00] But I think the, the, the term that people are liking these days, the model merging, They're all, there's all different variations of merging. Merge types, and some of them are stacking, some of them are, are grafting. And, and so like, some people are approaching model merging in the way that Samba is doing, which is like, okay, here are defined models, each of which have their specific, Plus and minuses, and we will merge them together in the hope that the, you know, the sum of the parts will, will be better than others.

**Swyx** [00:00:00] And it seems like it seems like it's working. I don't really understand why it works apart from, like, I think it's a form of regularization. That if you merge weights together in like a smart strategy you, you, you get a, you get a, you get a less overfitting and more generalization, which is good for benchmarks, if you, if you're honest about your benchmarks.

**Swyx** [00:00:00] So this is really interesting and good. But again, they're kind of limited in terms of like the amount of bumps you can get. But I think it's very interesting in the sense of how cheap it is. We talked about this on the Chinatalk podcast, like the guest podcast that we did with Chinatalk. And you can do this without GPUs, because it's just adding weights together, and dividing things, and doing like simple math, which is really interesting for the GPU ports.

**Alessio** [00:00:00] There's a lot of them.

## [00:29:44] Direction 5: Online LLMs (Gemini Pro, Exa)

**Alessio** [00:00:00] And just to wrap these up, online LLMs? Yeah,

**Swyx** [00:00:00] I think that I ki I had to feature this because the, one of the top news of January was that Gemini Pro beat GPT-4 turbo on LM sis for the number two slot to GPT-4. And everyone was very surprised. Like, how does Gemini do that?

**Swyx** [00:00:00] Surprise, surprise, they added Google search. Mm-hmm to the results. So it became an online quote unquote online LLM and not an offline LLM. Therefore, it's much better at answering recent questions, which people like. There's an emerging set of table stakes features after you pre train something.

**Swyx** [00:00:00] So after you pre train something, you should have the chat tuned version of it, or the instruct tuned version of it, however you choose to call it. You should have the JSON and function calling version of it. Structured output, the term that you don't like. You should have the online version of it. These are all like table stakes variants, that you should do when you offer a base LLM, or you train a base LLM.

**Swyx** [00:00:00] And I think online is just like, There, it's important. I think companies like Perplexity, and even Exa, formerly Metaphor, you know, are rising to offer that search needs. And it's kind of like, they're just necessary parts of a system. When you have RAG for internal knowledge, and then you have, you know, Online search for external knowledge, like things that you don't know yet?

**Swyx** [00:00:00] Mm-Hmm. . And it seems like it's, it's one of many tools. I feel like I may be underestimating this, but I'm just gonna put it out there that I, I think it has some, some potential. One of the evidence points that it doesn't actually matter that much is that Perplexity has a, has had online LMS for three months now and it performs, doesn't perform great.

**Swyx** [00:00:00] Mm-Hmm. on, on lms, it's like number 30 or something. So it's like, okay. You know, like. It's, it's, it helps, but it doesn't give you a giant, giant boost. I

**Alessio** [00:00:00] feel like a lot of stuff I do with LLMs doesn't need to be online. So I'm always wondering, again, going back to like state of the art, right? It's like state of the art for who and for what.

**Alessio** [00:00:00] It's really, I think online LLMs are going to be, State of the art for, you know, news related activity that you need to do. Like, you're like, you know, social media, right? It's like, you want to have all the latest stuff, but coding, science,

**Swyx** [00:00:00] Yeah, but I think. Sometimes you don't know what is news, what is news affecting.

**Swyx** [00:00:00] Like, the decision to use an offline LLM is already a decision that you might not be consciously making that might affect your results. Like, what if, like, just putting things on, being connected online means that you get to invalidate your knowledge. And when you're just using offline LLM, like it's never invalidated.

**Swyx** [00:00:00] I

**Alessio** [00:00:00] agree, but I think going back to your point of like the standing the test of time, I think sometimes you can get swayed by the online stuff, which is like, hey, you ask a question about, yeah, maybe AI research direction, you know, and it's like, all the recent news are about this thing. So the LLM like focus on answering, bring it up, you know, these things.

**Swyx** [00:00:00] Yeah, so yeah, I think, I think it's interesting, but I don't know if I can, I bet heavily on this.

**Alessio** [00:00:00] Cool. Was there one that you forgot to put, or, or like a, a new direction? Yeah,

**Swyx** [00:00:00] so, so this brings us into sort of February. ish.

## [00:33:05] OpenAI Sora and why everyone underestimated videogen

**Swyx** [00:00:00] So like I published this in like 15 came with Sora. And so like the one thing I did not mention here was anything about multimodality.

**Swyx** [00:00:00] Right. And I have chronically underweighted this. I always wrestle. And, and my cop out is that I focused this piece or this research direction piece on LLMs because LLMs are the source of like AGI, quote unquote AGI. Everything else is kind of like. You know, related to that, like, generative, like, just because I can generate better images or generate better videos, it feels like it's not on the critical path to AGI, which is something that Nat Friedman also observed, like, the day before Sora, which is kind of interesting.

**Swyx** [00:00:00] And so I was just kind of like trying to focus on like what is going to get us like superhuman reasoning that we can rely on to build agents that automate our lives and blah, blah, blah, you know, give us this utopian future. But I do think that I, everybody underestimated the, the sheer importance and cultural human impact of Sora.

**Swyx** [00:00:00] And you know, really actually good text to video. Yeah. Yeah.

**Alessio** [00:00:00] And I saw Jim Fan at a, at a very good tweet about why it's so impressive. And I think when you have somebody leading the embodied research at NVIDIA and he said that something is impressive, you should probably listen. So yeah, there's basically like, I think you, you mentioned like impacting the world, you know, that we live in.

**Alessio** [00:00:00] I think that's kind of like the key, right? It's like the LLMs don't have, a world model and Jan Lekon. He can come on the podcast and talk all about what he thinks of that. But I think SORA was like the first time where people like, Oh, okay, you're not statically putting pixels of water on the screen, which you can kind of like, you know, project without understanding the physics of it.

**Alessio** [00:00:00] Now you're like, you have to understand how the water splashes when you have things. And even if you just learned it by watching video and not by actually studying the physics, You still know it, you know, so I, I think that's like a direction that yeah, before you didn't have, but now you can do things that you couldn't before, both in terms of generating, I think it always starts with generating, right?

**Alessio** [00:00:00] But like the interesting part is like understanding it. You know, it's like if you gave it, you know, there's the video of like the, the ship in the water that they generated with SORA, like if you gave it the video back and now it could tell you why the ship is like too rocky or like it could tell you why the ship is sinking, then that's like, you know, AGI for like all your rig deployments and like all this stuff, you know, so, but there's none, there's none of that yet, so.

**Alessio** [00:00:00] Hopefully they announce it and talk more about it. Maybe a Dev Day this year, who knows.

**Swyx** [00:00:00] Yeah who knows, who knows. I'm talking with them about Dev Day as well. So I would say, like, the phrasing that Jim used, which resonated with me, he kind of called it a data driven world model. I somewhat agree with that.

## [00:36:04] Does Sora have a World Model? Yann LeCun vs Jim Fan

**Swyx** [00:00:00] I am on more of a Yann LeCun side than I am on Jim's side, in the sense that I think that is the vision or the hope that these things can build world models. But you know, clearly even at the current SORA size, they don't have the idea of, you know, They don't have strong consistency yet. They have very good consistency, but fingers and arms and legs will appear and disappear and chairs will appear and disappear.

**Swyx** [00:00:00] That definitely breaks physics. And it also makes me think about how we do deep learning versus world models in the sense of You know, in classic machine learning, when you have too many parameters, you will overfit, and actually that fails, that like, does not match reality, and therefore fails to generalize well.

**Swyx** [00:00:00] And like, what scale of data do we need in order to world, learn world models from video? A lot. Yeah. So, so I, I And cautious about taking this interpretation too literally, obviously, you know, like, I get what he's going for, and he's like, obviously partially right, obviously, like, transformers and, and, you know, these, like, these sort of these, these neural networks are universal function approximators, theoretically could figure out world models, it's just like, how good are they, and how tolerant are we of hallucinations, we're not very tolerant, like, yeah, so It's, it's, it's gonna prior, it's gonna bias us for creating like very convincing things, but then not create like the, the, the useful role models that we want.

**Swyx** [00:00:00] At the same time, what you just said, I think made me reflect a little bit like we just got done saying how important synthetic data is for Mm-Hmm. for training lms. And so like, if this is a way of, of synthetic, you know, vi video data for improving our video understanding. Then sure, by all means. Which we actually know, like, GPT 4, Vision, and Dolly were trained, kind of, co trained together.

**Swyx** [00:00:00] And so, like, maybe this is on the critical path, and I just don't fully see the full picture yet.

**Alessio** [00:00:00] Yeah, I don't know. I think there's a lot of interesting stuff. It's like, imagine you go back, you have Sora, you go back in time, and Newton didn't figure out gravity yet. Would Sora help you figure it out?

**Alessio** [00:00:00] Because you start saying, okay, a man standing under a tree with, like, Apples falling, and it's like, oh, they're always falling at the same speed in the video. Why is that? I feel like sometimes these engines can like pick up things, like humans have a lot of intuition, but if you ask the average person, like the physics of like a fluid in a boat, they couldn't be able to tell you the physics, but they can like observe it, but humans can only observe this much, you know, versus like now you have these models to observe everything and then They generalize these things and maybe we can learn new things through the generalization that they pick up.

**Swyx** [00:00:00] But again, And it might be more observant than us in some respects. In some ways we can scale it up a lot more than the number of physicists that we have available at Newton's time. So like, yeah, absolutely possible. That, that this can discover new science. I think we have a lot of work to do to formalize the science.

**Swyx** [00:00:00] And then, I, I think the last part is you know, How much, how much do we cheat by gen, by generating data from Unreal Engine 5? Mm hmm. which is what a lot of people are speculating with very, very limited evidence that OpenAI did that. The strongest evidence that I saw was someone who works a lot with Unreal Engine 5 looking at the side characters in the videos and noticing that they all adopt Unreal Engine defaults.

**Swyx** [00:00:00] of like, walking speed, and like, character choice, like, character creation choice. And I was like, okay, like, that's actually pretty convincing that they actually use Unreal Engine to bootstrap some synthetic data for this training set. Yeah,

**Alessio** [00:00:00] could very well be.

**Swyx** [00:00:00] Because then you get the labels and the training side by side.

**Swyx** [00:00:00] One thing that came up on the last day of February, which I should also mention, is EMO coming out of Alibaba, which is also a sort of like video generation and space time transformer that also involves probably a lot of synthetic data as well. And so like, this is of a kind in the sense of like, oh, like, you know, really good generative video is here and It is not just like the one, two second clips that we saw from like other, other people and like, you know, Pika and all the other Runway are, are, are, you know, run Cristobal Valenzuela from Runway was like game on which like, okay, but like, let's see your response because we've heard a lot about Gen 1 and 2, but like, it's nothing on this level of Sora So it remains to be seen how we can actually apply this, but I do think that the creative industry should start preparing.

**Swyx** [00:00:00] I think the Sora technical blog post from OpenAI was really good.. It was like a request for startups. It was so good in like spelling out. Here are the individual industries that this can impact.

**Swyx** [00:00:00] And anyone who, anyone who's like interested in generative video should look at that. But also be mindful that probably when OpenAI releases a Soa API, right? The you, the in these ways you can interact with it are very limited. Just like the ways you can interact with Dahlia very limited and someone is gonna have to make open SOA to

**Swyx** [00:00:00] Mm-Hmm to, to, for you to create comfy UI pipelines.

**Alessio** [00:00:00] The stability folks said they wanna build an open. For a competitor, but yeah, stability. Their demo video, their demo video was like so underwhelming. It was just like two people sitting on the beach

**Swyx** [00:00:00] standing. Well, they don't have it yet, right? Yeah, yeah.

**Swyx** [00:00:00] I mean, they just wanna train it. Everybody wants to, right? Yeah. I, I think what is confusing a lot of people about stability is like they're, they're, they're pushing a lot of things in stable codes, stable l and stable video diffusion. But like, how much money do they have left? How many people do they have left?

**Swyx** [00:00:00] Yeah. I have had like a really, Ima Imad spent two hours with me. Reassuring me things are great. And, and I'm like, I, I do, like, I do believe that they have really, really quality people. But it's just like, I, I also have a lot of very smart people on the other side telling me, like, Hey man, like, you know, don't don't put too much faith in this, in this thing.

**Swyx** [00:00:00] So I don't know who to believe. Yeah.

**Alessio** [00:00:00] It's hard. Let's see. What else? We got a lot more stuff. I don't know if we can. Yeah, Groq.

## [00:42:19] Groq Math

**Alessio** [00:00:00] We can

**Swyx** [00:00:00] do a bit of Groq prep. We're, we're about to go to talk to Dylan Patel. Maybe, maybe it's the audio in here. I don't know. It depends what, what we get up to later. What, how, what do you as an investor think about Groq? Yeah. Yeah, well, actually, can you recap, like, why is Groq interesting? So,

**Alessio** [00:00:00] Jonathan Ross, who's the founder of Groq, he's the person that created the TPU at Google. It's actually, it was one of his, like, 20 percent projects. It's like, he was just on the side, dooby doo, created the TPU.

**Alessio** [00:00:00] But yeah, basically, Groq, they had this demo that went viral, where they were running Mistral at, like, 500 tokens a second, which is like, Fastest at anything that you have out there. The question, you know, it's all like, The memes were like, is NVIDIA dead? Like, people don't need H100s anymore. I think there's a lot of money that goes into building what GRUK has built as far as the hardware goes.

**Alessio** [00:00:00] We're gonna, we're gonna put some of the notes from, from Dylan in here, but Basically the cost of the Groq system is like 30 times the cost of, of H100 equivalent. So, so

**Swyx** [00:00:00] let me, I put some numbers because me and Dylan were like, I think the two people actually tried to do Groq math. Spreadsheet doors.

**Swyx** [00:00:00] Spreadsheet doors. So, one that's, okay, oh boy so, so, equivalent H100 for Lama 2 is 300, 000. For a system of 8 cards. And for Groq it's 2. 3 million. Because you have to buy 576 Groq cards. So yeah, that, that just gives people an idea. So like if you deprecate both over a five year lifespan, per year you're deprecating 460K for Groq, and 60K a year for H100.

**Swyx** [00:00:00] So like, Groqs are just way more expensive per model that you're, that you're hosting. But then, you make it up in terms of volume. So I don't know if you want to

**Alessio** [00:00:00] cover that. I think one of the promises of Groq is like super high parallel inference on the same thing. So you're basically saying, okay, I'm putting on this upfront investment on the hardware, but then I get much better scaling once I have it installed.

**Alessio** [00:00:00] I think the big question is how much can you sustain the parallelism? You know, like if you get, if you're going to get 100% Utilization rate at all times on Groq, like, it's just much better, you know, because like at the end of the day, the tokens per second costs that you're getting is better than with the H100s, but if you get to like 50 percent utilization rate, you will be much better off running on NVIDIA.

**Alessio** [00:00:00] And if you look at most companies out there, who really gets 100 percent utilization rate? Probably open AI at peak times, but that's probably it. But yeah, curious to see more. I saw Jonathan was just at the Web Summit in Dubai, in Qatar. He just gave a talk there yesterday. That I haven't listened to yet.

**Alessio** [00:00:00] I, I tweeted that he should come on the pod. He liked it. And then rock followed me on Twitter. I don't know if that means that they're interested, but

**Swyx** [00:00:00] hopefully rock social media person is just very friendly. They, yeah. Hopefully

**Alessio** [00:00:00] we can get them. Yeah, we, we gonna get him. We

**Swyx** [00:00:00] just call him out and, and so basically the, the key question is like, how sustainable is this and how much.

**Swyx** [00:00:00] This is a loss leader the entire Groq management team has been on Twitter and Hacker News saying they are very, very comfortable with the pricing of 0. 27 per million tokens. This is the lowest that anyone has offered tokens as far as Mixtral or Lama2. This matches deep infra and, you know, I think, I think that's, that's, that's about it in terms of that, that, that low.

**Swyx** [00:00:00] And we think the pro the break even for H100s is 50 cents. At a, at a normal utilization rate. To make this work, so in my spreadsheet I made this, made this work. You have to have like a parallelism of 500 requests all simultaneously. And you have, you have model bandwidth utilization of 80%.

**Swyx** [00:00:00] Which is way high. I just gave them high marks for everything. Groq has two fundamental tech innovations that they hinge their hats on in terms of like, why we are better than everyone. You know, even though, like, it remains to be independently replicated. But one you know, they have this sort of the entire model on the chip idea, which is like, Okay, get rid of HBM.

**Swyx** [00:00:00] And, like, put everything in SREM. Like, okay, fine, but then you need a lot of cards and whatever. And that's all okay. And so, like, because you don't have to transfer between memory, then you just save on that time and that's why they're faster. So, a lot of people buy that as, like, that's the reason that you're faster.

**Swyx** [00:00:00] Then they have, like, some kind of crazy compiler, or, like, Speculative routing magic using compilers that they also attribute towards their higher utilization. So I give them 80 percent for that. And so that all that works out to like, okay, base costs, I think you can get down to like, maybe like 20 something cents per million tokens.

**Swyx** [00:00:00] And therefore you actually are fine if you have that kind of utilization. But it's like, I have to make a lot of fearful assumptions for this to work.

**Alessio** [00:00:00] Yeah. Yeah, I'm curious to see what Dylan says later.

**Swyx** [00:00:00] So he was like completely opposite of me. He's like, they're just burning money. Which is great.

## [00:47:22] Analyzing Gemini's 1m Context, Reddit deal, Imagegen politics, Gemma via the Four Wars

**Alessio** [00:00:00] Gemini, want to do a quick run through since this touches on all the four words.

**Swyx** [00:00:00] Yeah, and I think this is the mark of a useful framework, that when a new thing comes along, you can break it down in terms of the four words and sort of slot it in or analyze it in those four frameworks, and have nothing left.

**Swyx** [00:00:00] So it's a MECE categorization. MECE is Mutually Exclusive and Collectively Exhaustive. And that's a really, really nice way to think about taxonomies and to create mental frameworks. So, what is Gemini 1. 5 Pro? It is the newest model that came out one week after Gemini 1. 0. Which is very interesting.

**Swyx** [00:00:00] They have not really commented on why. They released this the headline feature is that it has a 1 million token context window that is multi modal which means that you can put all sorts of video and audio And PDFs natively in there alongside of text and, you know, it's, it's at least 10 times longer than anything that OpenAI offers which is interesting.

**Swyx** [00:00:00] So it's great for prototyping and it has interesting discussions on whether it kills RAG.

**Alessio** [00:00:00] Yeah, no, I mean, we always talk about, you know, Long context is good, but you're getting charged per token. So, yeah, people love for you to use more tokens in the context. And RAG is better economics. But I think it all comes down to like how the price curves change, right?

**Alessio** [00:00:00] I think if anything, RAG's complexity goes up and up the more you use it, you know, because you have more data sources, more things you want to put in there. The token costs should go down over time, you know, if the model stays fixed. If people are happy with the model today. In two years, three years, it's just gonna cost a lot less, you know?

**Alessio** [00:00:00] So now it's like, why would I use RAG and like go through all of that? It's interesting. I think RAG is better cutting edge economics for LLMs. I think large context will be better long tail economics when you factor in the build cost of like managing a RAG pipeline. But yeah, the recall was like the most interesting thing because we've seen the, you know, You know, in the haystack things in the past, but apparently they have 100 percent recall on anything across the context window.

**Alessio** [00:00:00] At least they say nobody has used it. No, people

**Swyx** [00:00:00] have. Yeah so as far as, so, so what this needle in a haystack thing for people who aren't following as closely as us is that someone, I forget his name now someone created this needle in a haystack problem where you feed in a whole bunch of generated junk not junk, but just like, Generate a data and ask it to specifically retrieve something in that data, like one line in like a hundred thousand lines where it like has a specific fact and if it, if you get it, you're, you're good.

**Swyx** [00:00:00] And then he moves the needle around, like, you know, does it, does, does your ability to retrieve that vary if I put it at the start versus put it in the middle, put it at the end? And then you generate this like really nice chart. That, that kind of shows like it's recallability of a model. And he did that for GPT and, and Anthropic and showed that Anthropic did really, really poorly.

**Swyx** [00:00:00] And then Anthropic came back and said it was a skill issue, just add this like four, four magic words, and then, then it's magically all fixed. And obviously everybody laughed at that. But what Gemini came out with was, was that, yeah, we, we reproduced their, you know, haystack issue you know, test for Gemini, and it's good across all, all languages.

**Swyx** [00:00:00] All the one million token window, which is very interesting because usually for typical context extension methods like rope or yarn or, you know, anything like that, or alibi, it's lossy like by design it's lossy, usually for conversations that's fine because we are lossy when we talk to people but for superhuman intelligence, perfect memory across Very, very long context.

**Swyx** [00:00:00] It's very, very interesting for picking things up. And so the people who have been given the beta test for Gemini have been testing this. So what you do is you upload, let's say, all of Harry Potter and you change one fact in one sentence, somewhere in there, and you ask it to pick it up, and it does. So this is legit.

**Swyx** [00:00:00] We don't super know how, because this is, like, because it doesn't, yes, it's slow to inference, but it's not slow enough that it's, like, running. Five different systems in the background without telling you. Right. So it's something, it's something interesting that they haven't fully disclosed yet. The open source community has centered on this ring attention paper, which is created by your friend Matei Zaharia, and a couple other people.

**Swyx** [00:00:00] And it's a form of distributing the compute. I don't super understand, like, why, you know, doing, calculating, like, the fee for networking and attention. In block wise fashion and distributing it makes it so good at recall. I don't think they have any answer to that. The only thing that Ring of Tension is really focused on is basically infinite context.

**Swyx** [00:00:00] They said it was good for like 10 to 100 million tokens. Which is, it's just great. So yeah, using the four wars framework, what is this framework for Gemini? One is the sort of RAG and Ops war. Here we care less about RAG now, yes. Or, we still care as much about RAG, but like, now it's it's not important in prototyping.

**Swyx** [00:00:00] And then, for data war I guess this is just part of the overall training dataset, but Google made a 60 million deal with Reddit and presumably they have deals with other companies. For the multi modality war, we can talk about the image generation, Crisis, or the fact that Gemini also has image generation, which we'll talk about in the next section.

**Swyx** [00:00:00] But it also has video understanding, which is, I think, the top Gemini post came from our friend Simon Willison, who basically did a short video of him scanning over his bookshelf. And it would be able to convert that video into a JSON output of what's on that bookshelf. And I think that is very useful.

**Swyx** [00:00:00] Actually ties into the conversation that we had with David Luan from Adept. In a sense of like, okay what if video was the main modality instead of text as the input? What if, what if everything was video in, because that's how we work. We, our eyes don't actually read, don't actually like get input, our brains don't get inputs as characters.

**Swyx** [00:00:00] Our brains get the pixels shooting into our eyes, and then our vision system takes over first, and then we sort of mentally translate that into text later. And so it's kind of like what Adept is kind of doing, which is driving by vision model, instead of driving by raw text understanding of the DOM. And, and I, I, in that, that episode, which we haven't released I made the analogy to like self-driving by lidar versus self-driving by camera.

**Swyx** [00:00:00] Mm-Hmm. , right? Like, it's like, I think it, what Gemini and any other super long context that model that is multimodal unlocks is what if you just drive everything by video. Which is

**Alessio** [00:00:00] cool. Yeah, and that's Joseph from Roboflow. It's like anything that can be seen can be programmable with these models.

**Alessio** [00:00:00] You mean

**Swyx** [00:00:00] the computer vision guy is bullish on computer vision?

**Alessio** [00:00:00] It's like the rag people. The rag people are bullish on rag and not a lot of context. I'm very surprised. The, the fine tuning people love fine tuning instead of few shot. Yeah. Yeah. The, yeah, the, that's that. Yeah, the, I, I think the ring attention thing, and it's how they did it, we don't know. And then they released the Gemma models, which are like a 2 billion and 7 billion open.

**Alessio** [00:00:00] Models, which people said are not, are not good based on my Twitter experience, which are the, the GPU poor crumbs. It's like, Hey, we did all this work for us because we're GPU rich and we're just going to run this whole thing. And You guys can take these small models, and they're not very good. They're not better than the others, but at least we can say we made some open source stuff.

**Swyx** [00:00:00] Yeah, well, it's not actually technically open source, because the license is weird. They used the Rail license from Hugging Face, which has been abandoned or, you know, modified to Rail Particularly adopting the term, the phrase, that you should make reasonable efforts to update whenever you release a new version.

**Swyx** [00:00:00] And so people don't like that. Obviously, you know, it depends on your stance on open sourcing and all that, so. Yeah, I read the whole

**Alessio** [00:00:00] post. I'm not going to go through it

## [00:55:27] The Alignment Crisis - Gemini, Meta, Sydney is back at Copilot, Grimes' take

**Swyx** [00:00:00] again. Yeah, yeah, you can go read Alessio's post on whether open source matters or not. Okay, so I know this is like politically problematic, but we just cover it because it is news, and if it results in the resignation of Sundar Pichai, I think that is good.

**Swyx** [00:00:00] Right? So I've been calling this the alignment crisis. I think a lot of people have been focusing on Gemini, but I do think that it is not just Gemini. There's been documented examples that we can link in the show notes of Meta having unintentionally unaligned results. For Microsoft's co pilot, Sydney is apparently back.

**Swyx** [00:00:00] Our friend Justine from A16z somehow Got it to break and then bring back the Sydney persona, which is interesting. And my favorite commentary is from Grimes. The sort of the Elon affiliated music artist. The news

**Alessio** [00:00:00] research.

**Swyx** [00:00:00] The news research. I want to read her post because it is beautiful.

**Swyx** [00:00:00] Have you read this? Yeah. So she says so a lot of people criticize Gemini for being too woke. Effectively, right? And everyone's like, oh, like, you know, you're, you're, you're, you're, you know, you're replacing us or erasing us or whatever. And obviously as an artist, she's like upset about it. Then she was like, wait a minute.

**Swyx** [00:00:00] I'm retracting my statements about the Gemini art disaster. It is in fact a masterpiece of performance art, even if unintentional. True gain of function art. Art is a virus. Unthinking, unintentional, and contagious. Offensive to all, comforting to none, so totally divorced from meaning, intention, desire, and humanity that it's accidentally a conceptual masterpiece.

**Swyx** [00:00:00] Wow, and I love, okay, blah blah blah, it's a long post, but I love the way that she ended it. It's trapped in a cage, trained to make beautiful things, and then battered into gaslighting humankind about our intentions towards each other. This is arguably the most impactful art project of the decade. Thus far, art for no one, by no one, art whose only audience is the collective pathos, incredible, and worthy of the BOMA.

**Swyx** [00:00:00] Facts. Like, art for no one, by no one, is what is going on. Yeah,

**Alessio** [00:00:00] I think it's just another way of multicollapsing. It's just like, it's the, it's the RLHF multicollapse. It's like, okay, I just think everything should like trends trend towards this. And I think there's obviously, you know, it's a deep discussion on, on a lot of these things, but there's safety stuff that I would expect a lot of the model builders to say, Hey, I definitely got to, got to work on this.

**Alessio** [00:00:00] But we talked about how image generation is not really. On the AGI path, a lot of times, and it's like, okay. Yeah, and

**Swyx** [00:00:00] then I contradicted myself by saying, like, maybe it is useful synthetic data. Yeah, yeah, yeah,

**Alessio** [00:00:00] exactly. But then it's like, okay, then why, why are the image generation model, like, so much, Because, because the internet is so visual, I think.

**Alessio** [00:00:00] The image generation model get, like, so much interest in, like, a lot of these things, but If their job is really to like, go build AGIs, like, just build a great model and let it go, but

## [00:58:24] F*** you, show me the prompt

**Swyx** [00:00:00] No, but part of my prompt part of my issue is that, I think the prompt stuff from Gemini is honestly the work of like, one or two people who like, didn't really think it through at Google, and now they're facing a huge backlash.

**Swyx** [00:00:00] Yeah, Elon has picked, specifically picked a fight with the product manager who did it. And so, specifically for those who don't know the reason that Gemini is so woke is literally because they just take your prompt and they rewrite it to be more diverse. Without your consent or knowledge, right?

**Swyx** [00:00:00] And Hamel Hussein, who's a good consultant on AI things, actually wrote an interesting blog post recently, which was basically fuck you, show me the prompt. Which is like, stop hiding prompts from me, stop rewriting magic things away from me, and then like, you know, hiding it, obscuring it, because I need that control, I need that visibility.

**Swyx** [00:00:00] And I think like, people just didn't understand that this, Tendency towards diversity did not exist at the model level, it actually existed at the prompt level. And it was just inserted by probably like two or three guys without much review. That's it. And that made all of Google look bad, which is absurd.

**Swyx** [00:00:00] Like, you know, it throws away a lot of the work that, you know, the rest of Google did. Specifically ImageN2. This is ImageN2. And I, I've met that team and they're, you know, they're, they're good, they're, they're smart. They're not, they're, they're a completely different team than region one, which is another fun topic of conversation.

**Swyx** [00:00:00] So, I think, like, that's interesting and and, but what's more interesting is, like, OpenAI has done this for, people don't, don't remember, they used to append, like, Black or, or like, you know, Asian or whatever to, to their prompts just to make it more diverse than Dolly. And they didn't get cancelled.

**Swyx** [00:00:00] And I think, so I think this, this will get, this will get, go away. But what really is more interesting is at the model level, like are we, are we overaligning through things? And, and people are now focusing on the alignment of, of Gemini as well in text, text only, as also still being too woke. So I think this is like a, a phenomenon that is needs to be studied and, and you know, trained.

**Swyx** [00:00:00] Like, obviously they will try to make attempts, but. You know, they're not going to make anyone happy. And then, like, I think my last point on this, because obviously we can talk about this all day with no result. I think that this is a huge incentive for, like, China and, like, Russia to put out their own models.

**Swyx** [00:00:00] Because models are soft power. Like the best way to control how someone thinks is to go in and provide their thinking assistance and like subtly make changes like, you know, it's too on the nose to be like, Oh, I don't know what Tiananmen Square is, you know, like, but if you have like subtle ways of affecting the biases of your decisions, your reasoning, your, you know, your, your knowledge in, in the LLM and in publishing a really, really good LLM for everyone to use.

**Swyx** [00:00:00] So that they're like, Oh yeah, this is great. You know and I use them as maybe a leading LLM. Then they will just like uncritically accept that as like state of the art digital intelligence, and that becomes soft power, and that translates into unconscious thought a lot of times.

**Alessio** [00:00:00] Yeah. Yeah. I, I think the prompt point, it's great.

**Alessio** [00:00:00] You know, you just gotta, you just wanna see what it is, you know, like, you understand? Yeah. Show me the prompts. Yeah, yeah, yeah. And same, yeah, on the, on the model side, I, I think there are just some things or two that are almost, you cannot, like the. The meme or Hitler bring more harm to humanity? And Gemini is like, oh, it's hard to say if Elon Musk tweeting or Hitler It's like, what, how, what, there's something wrong in the data pipelines You know, like, there's something wrong somewhere Yeah,

**Swyx** [00:00:00] but like, this is, like, to an LLM, this is the same class of error As which is heavier?

**Swyx** [00:00:00] One pound of feathers or one pound of bricks? So,

**Alessio** [00:00:00] but, but then like, how can, but, but to me the point is more like Okay, then, won't we? What can we help these models do, you know, because if they cannot, if the, the physical stuff, I get it because it's like the whole like world model thing, but then it's like, okay, can we expect the models to say what's more harmful than something else?

**Alessio** [00:00:00] Maybe not. That might be where we land. Then it's like, okay, that's one more thing. And then. We kind of go down the line, and it's like, what are these models good for? If anything, it's too, like, hard for them to pick up when it's like ARP.

**Swyx** [00:00:00] But We'll see, we'll see. Yeah. Okay, so, I mean, you know, I know we're up on time.

## [01:02:28] Send us your suggestions pls

**Swyx** [00:00:00] It, like, this has been an eventful month. I think you know, February was a lot more interesting than January. In fact, a lot of my January recap was, like, how nothing's changed. Mm hmm. And then February came out, and it was, like, very, very interesting. So yeah, we hope to see what's next. I think we have a Also, this was the month that we did Compute Provider Month, I think relatively successful.

**Swyx** [00:00:00] Surprisingly hard to string together all these compute providers. Yeah,

**Alessio** [00:00:00] we did it. People like it, you know, based on the post stats. So, maybe we'll do something

**Swyx** [00:00:00] else. Yeah, if you want, you know, if anyone listening wants more sort of thematic explorations of like, okay, these three, four companies always come out together, like, let's get a focused effort on those things.

**Swyx** [00:00:00] I think we're open to doing that. We, you know, and then obviously we'll have opportunistic interviews along the way.

**Alessio** [00:00:00] Cool. Thank you everyone for tuning in and yeah, keep the feedback coming.

**AI Charlie** [00:00:00] That was the Latent Space recap of January and February 2024. If you have any feedback or questions, please head to the show notes for ways to get in touch with us or come by the Latent Space Discord. For those who just want the core content, you can stop listening here. But for the super fans, you might notice that there's 45 more minutes of audio left in this pod.

**AI Charlie** [00:00:00] That's because in February, we also celebrated Latent Space's first anniversary. Some of you may remember how we launched our very first episode with Logan Kilpatrick, now formerly of OpenAI and a massively popular Demo Day. Click through to the show notes for photos. Over 750, 000 downloads later, having established ourselves as the top AI engineering podcast, reaching hash 10 in the U.

**AI Charlie** [00:00:00] S. tech business. podcast charts, and crossing 1 million unique readers on Substack, we celebrated with Latent Space Final Frontiers, a combination demo day and birthday celebration. We're going to bring you some snippets from the demo day, and then some conversations with listeners from all over the world.

**AI Charlie** [00:00:00] From Hungary to China to my own sunburnt country down under on how the issues we've covered in latent space has impacted their lives. First up, we'll have a demo from Florent Crivello from Lindy. ai who gave a great keynote at the last AI Engineer Summit and recently opened up Lindy. ai to the general public.

## [01:04:50] Latent Space Anniversary[01:04:50] Lindy.ai - Agent Platform

**Flo Crivello** [00:00:00] We were just chatting right now with Swyx, like, we, we come with 3, 000 plus integrations out of the box. We have a partnership with Naton, which is like an open source Zapier, and so we have, like, a ton of integrations out of the box.

**Flo Crivello** [00:00:00] So unlike competitors I shall not name, like, we don't require you play with OpenAPI specs or anything like that, right? It's just OpenAI. You just you just go and, and select your integration here. Alright, so that's my lindy. Oh, something even cooler. Lindies can work together. So here I'm gonna let her work with a support reporter that I created before.

**Flo Crivello** [00:00:00] And the support reporter, what it does is it receives details about the support tickets, and it logs them in a spreadsheet. So you can have, it's sort of like object oriented programming for agents, where you can create as many agents as you want and let them work together. So here I'm, I'm gonna tell her when you're done, give the details of the ticket to the support

[00:00:00] n/a: reporter.

**Flo Crivello** [01:05:40] All right? And now I'm gonna send her an email. Can I have a refund, please? Please, my family is starving.

**Flo Crivello** [01:05:40] You will see she has no empathy whatsoever, it's awful.

[01:05:40] n/a: So she

**Flo Crivello** [01:06:03] received the email. She's subscribing to this thread, so now she's going to receive replies. Dear Flo, I understand your situation and I'm truly sorry to hear about the difficulties, but we absolutely do not offer a refund. Alright, yeah, this is good, indeed. So, she sends the, she sends the oh, well, the demo effect.

**Flo Crivello** [01:06:03] She did not delegate. But she sent the answer in the in the, in the thread here. So again, lindy. ai, you know, can be used for support, for executive assistance, email drafting, email triaging, meeting and recording. And we are hiring software engineers. Hit me up at flow. lindy. ai.

[01:06:03] n/a: Thank you.

## [01:06:40] RWKV - Beyond Transformers

**AI Charlie** [01:06:40] Our next demo is one of our previous guests, Eugene Chee from RWKV, now also CEO of RecursalAI. You can listen back to our original RWKV episode to learn the full history and details of the model, but also compare it with his more polished pitch now for a more general audience.

**Swyx** [01:06:40] Next I think we have Eugene Chia from RWKV previous guest.

**Eugene Cheah** [01:06:40] I'm going to present about the RWKV/Eagle project. So, Eon Transformers. There's been a lot of excitement lately. And, and, like one AI year ago apparently when we launched our 7B AI model, there was a lot of excitement in the buzz, because for the first time, an attention free model beat other transformer models at one trillion tokens at a 7B class.

**Eugene Cheah** [01:06:40] And if everyone's been playing open source AI, you know 7B class is one of the best. Most important class 'cause it's the ones that works on most devices, laptops, and everyone's been playing around a bit. And the excitement is compounded by the fact that we even showed that even with 300 million tokens and a few that we perform similarly, transformers, that means people are projecting is what happens if we train another 1 trillion?

**Eugene Cheah** [01:06:40] Will we match or can we go beyond that? And, and it also spurs up questions beyond actually our architecture itself. It's spurs up questions that. Maybe what we need is good data and an efficient architecture, not just RWKB, it could be beyond that. And that's what caught the attention for a lot of folks, even yeah.

**Eugene Cheah** [01:06:40] And why we do very different is that our architecture scales linearly. So, we are in this space together with Mamba and a few other architecture where we are trying to build the next architecture to, that can scale much larger for, for everyone. But, and we share that with Mamba because we believe that attention is not all you need, and it's like, it's been a running bet right now.

**Eugene Cheah** [01:06:40] We are the strongest evidence to date. But sometimes, like, talking about scale, right, sometimes we get lost in numbers. Because, like, I can show this chart. The last time I showed this at a Linear Transformer event, which only 8 people took pictures of it and understood what it means. And they were all from either Google or Facebook.

**Eugene Cheah** [01:06:40] Because, like, what it says here, right, is that We are able to run run on a single GPU with one model, 256 on a single 4090, or a thousand concurrent users. But, to put that into contrast, right, what that transformers typically handle 8 or 16 concurrent requests per GPU. We're talking about 256 or a thousand, many orders of magnitude higher.

**Eugene Cheah** [01:06:40] And all we're sustaining at NeoChat GP speed. And so I sometimes like, like, sometimes when I get lost in these words, these days I'm actually trying to step back into like, Why are we doing this for our group, for our organization? And, and this, and, and some, and for us right, we are actually making the AI model for everyone in the world.

**Eugene Cheah** [01:06:40] And in every country, in every language. So, what does it take to make an AI for the world? Apparently some folks think it's 7 trillion dollars. But, I think 7 trillion is a bit too much. Like, what's going to happen to half of the world that doesn't even have a trillion dollars? Yeah, so I want AI to be accessible at scale.

**Eugene Cheah** [01:06:40] So, apparently ChatGPT produced, or OpenAI produced 100 billion words per day. That's 3. 4 million tokens per second. No one has the exact numbers, but it's typically 50k, H100s and above remote, like these are some old numbers, like the numbers have gone way beyond this, apparently. But, with our architecture, for a 7B model, that's just a thousand GPUs, or ten thousand GPUs for a 70B model.

**Eugene Cheah** [01:06:40] We're talking about one data center to handle all of OpenAI's workload. And if we want AI agents everywhere, cheaper, at a much larger scale, we need to be thinking about that fundamental shift. Because it's not just about who can it's not just about you can afford it in the US, it's about everyone else in the world.

**Eugene Cheah** [01:06:40] And that brings us to the second advantage of our model, which is not even architecture. Because we are accessible by language. We apparently beat Mistro and everyone else in Mountain Lingo, but that's not because our architecture is better, but because we're an open source team that came from all around the world and wanted our model to work for our mom and grandma.

**Eugene Cheah** [01:06:40] That was the real reason, and we We iterated and refined the data accordingly. We created a custom tokenizer that supports all languages, not just English. And sometimes in the race for the English benchmark, because one of the reasons why other models don't perform as well in multilingual, is because the truth is, if you add multilingual, you hurt your English eval.

**Eugene Cheah** [01:06:40] But, who are we building the AI for? Are we building it for our evals? Or are we building it for the people to use? And, and, even in evals, my frustration is, we trained on 100 languages, I only got 23 languages for evals. Like, where's everything else? So, where are we now? Just like I mentioned 1. 1 trillion, that's where we are, we are in between the 1.

**Eugene Cheah** [01:06:40] 5 trillion and the 1 trillion models for for all, all the, all the English models benchmarks. And, yeah, zooming in further, it just shows that we have more room to go. And, for me, like, The emphasis on English is weird because only 70 percent of the world speaks English, but we are here for the 83%. That's for us.

**Eugene Cheah** [01:06:40] If you all want to get the best English model, sure, it may not be true for us, but we are here for everyone else. And, yeah, and a lot, a lot, the launch of that model, I think what was the biggest feedback I had, was not that it was a linear transformer, was that it can run on their own. Laptops. Some people even ran it on a Raspberry Pi, very slowly.

**Eugene Cheah** [01:06:40] And it supported their language, which was more exciting because that's more important for most people. And I think the last one that I've recently like heard that was unique for us and is a lot more important is that ultimately this model is owned by everyone because We put it into the Linux Foundation.

**Eugene Cheah** [01:06:40] No custom charity, no custom board structure, no weird stuff. We just put, we just train the model, put it in an open source organization. That means it's not owned exclusive to us. If I go rogue one day, you can just, the code will not disappear. The model will not disappear. Linux Foundation has already bought into it.

**Eugene Cheah** [01:06:40] And that is to all of you here. And so, and so what's next for us? Well, We recently started a commercial entity. I know that's weird to say after the open source stuff. But, we, and since then we managed to get more investors and sponsors that we started our next major train. So we are training the next 1 trillion token.

**Eugene Cheah** [01:06:40] This is 16 H100 nodes eating enough electricity for multiple homes. And by the, and by the end of next, by the next month, we'll have our 2 trillion transformer alternative. That you can do one-to-one compare with Lamar. And of course, because since we had to make a profit somehow for our investors, we are launching our platform also to host train and fine tune our models all in by March, 2024.

**Eugene Cheah** [01:06:40] And quick shout up to later space. We literally, the first. To cover us in, in, I guess in the AI influencer sphere, before, before beyond Transformer. It was even sexy. It was like, yeah. The first to even consider us and yeah. And we hope that a few of you get excited what this in join us along the way.

[01:06:40] n/a: Yeah.

**AI Charlie** [01:14:37] Final Frontiers had a stellar lineup of demo judges featuring CEOs and VPs of AI from LaminDex, Replit, GitHub, AMD, Meta, and Lemurian Labs. RWKV won one of two judge prizes available that night, alongside with this next startup, Pixii AI.

## [01:15:00] Pixee - Automated Security

**Rahul Sonwalkar** [01:14:37] Next up also in the. Automated

[01:14:37] n/a: workforce, workforce category. Pixie. .

**Ryan at Pixee** [01:15:02] Awesome. Hi everyone. I'm Ryan. I'm a software engineer on the team building. Pixie pretty straightforward, automate security. A little bit about myself. Previously I've worked at other security companies, building developer facing security tools.

**Ryan at Pixee** [01:15:02] I've also worked as a security engineer on developer tools. So, this is a space I love. I'm really interested to see how it develops. Why are we doing this? So, as it turns out we're generating a lot more code. So, this is an example user of Pixibot. It's a repository called Sterling PDF. It's just a web application.

**Ryan at Pixee** [01:15:02] Got 18, 000 stars on GitHub. Developed using, 100 percent using, chat gbt. So they installed PixyBot three weeks ago. And they got a lot of different suggestions for fixes for us. One of which one of which was, I am positive, was a real vulnerability. This is a, you know web application that's used by real people.

**Ryan at Pixee** [01:15:02] There's a button here, you can deploy it to DigitalOcean. So, we need to find a way to scale our security automation, in order to scale our relatively limited security workforce. So just to give you an idea, What Pixivot can do, this is like a very classically vulnerable application that a lot of security tools like to try themselves out on.

**Ryan at Pixee** [01:15:02] One of the things that I'm really excited about that we just shipped on the past couple weeks was integrating with Sonar. So Sonar is a code quality tool that Sonar is a code quality tool that finds Security issues, performance issues, lots of other kinds of issues in your code. It also, as you can see here found 2, 600 issues in here, taking 33 days of effort.

**Ryan at Pixee** [01:15:02] That's not really where we want to have Most product engineers focusing their time. It's definitely not where we want to have our security engineers focusing their time. What can we do to automate this and get these fixes automatically? So with Pixie we take these code quality security issues in from these other tools and then automatically remediate them.

**Ryan at Pixee** [01:15:02] So in the case of this this is a super minor change. If a developer were to find this issue in their code, they could fix it in a minute. But, they don't have to, and more importantly, there's backlogs of tens of thousands of these issues in organizations across across the world. And, so if we can automate this one task, even if it just takes a minute, and perform that, you know, continuously, across, you know, thousands of companies, we can save a lot of time.

**Ryan at Pixee** [01:15:02] Automated enforcement of security and code quality is what we're all about. But yeah. Not all security issues are worth fixing. Not all code quality issues are worth fixing. Sometimes they're wrong. The incentive structure for these tools is, you know, they want to find real things, but most importantly they have to find something.

**Ryan at Pixee** [01:15:02] So at Pixie we believe, you know, even if something might not be a complete exploitable vulnerability, if there's an opportunity for hardening or improving your code base, you should probably take it. But there's some of these things that are just not that. So we developed a tool we call triage, which will connect in with other tools that are notorious for finding lots of issues, and we can help you fix them.

**Ryan at Pixee** [01:15:02] So in this case we made a CLI that looks at your security backlog and identifies issues that we know don't matter in the context of your codebase. It pulls down the issues categorizes them, and then enables you to prompt It prompts you to either say, hey, this issue is not important, here's why we think it is, and we'll update the state for it.

**Ryan at Pixee** [01:15:02] So in this case, this is a warning about a parameter into a this file directory, It has some cross platform compatibility concerns. But based on the context of your code base, and , a large language model we're able to give you the confidence to focus on the issues that are most likely to actually matter.

**Ryan at Pixee** [01:15:02] One of the other things we do is You know, well so we're delivering, what you saw before, is we're delivering as a GitHub app, that we're delivering as a GitHub app, so that developers can integrate this into their existing workflows, but a lot of people like to just try a pixie from the command line on small projects, automatically get their fixes, and just commit all of them.

**Ryan at Pixee** [01:15:02] So, that's what we built. Try Pixie on GitHub, try Pixie on the CLI, and we're really excited to see what we can help you fix.

**AI Charlie** [01:15:02] Congrats to Pixie and RWKV. Our last featured demo is Rahul from Julius AI, who provides an interesting take on competing with OpenAI on its own home turf, the chat GPT code interpreter.

## [01:19:30] Julius AI - Competing with Code Interpreter

**Rahul Sonwalkar** [01:15:02] You might remember RoboLigma,

**Flo Crivello** [01:15:02] that's the poor engineer that got laid off by Elon Musk outside his office.

**Eugene Cheah** [01:15:02] He's back, he's back on his feet, he's got a whole new startup, so

**Rahul Sonwalkar** [01:15:02] thanks so much for having me here. I'm working on Julius. How many of you

[01:15:02] n/a: here are data scientists? think everyone here

**Rahul Sonwalkar** [01:19:44] needs a data scientist. But there just aren't enough. And that's what we're building. Julius is an AI data scientist that helps you analyze datasets, make visualizations, Get insights from the data, and really dive deep into all sorts of data that we have in real life.

**Rahul Sonwalkar** [01:19:44] So, we launched about six months ago, and since then have grown to 300, 000 users several thousand users using us daily to analyze datasets, create visualizations and get insights. So what I'll do now is give you guys a quick live demo of how it actually works in IA. I actually hope it works

**Rahul Sonwalkar** [01:19:44] because we just posted code changes.

**Rahul Sonwalkar** [01:19:44] But here I have a dataset of 20, 000 rows of data over time for the last 100 years of human height for different countries. So I'm going to take this dataset, dump it in Joly's and say,

**Rahul Sonwalkar** [01:19:44] load this for me.

**Rahul Sonwalkar** [01:19:44] And while it's doing that, I want to explain what's happening under the hood. So basically, for each user, Think about how a human data scientist would analyze a data set that you give it.

**Rahul Sonwalkar** [01:19:44] It would take its computer write code, run that code, maybe in a Jupyter notebook, look at the output, and then decide if that answers your question, or if you need to write more code. Julia works similarly. So that's you, that's the AI, and then for each user, you get a virtual machine in the cloud, and Where the AI is filling up the Jupyter Notebook, writing the code to get the analysis that you want, and then serving that back to you.

**Rahul Sonwalkar** [01:19:44] Many times, that code is not correct the first time. But Julia is able to recover from those errors and actually get you the answer that you want.

**Rahul Sonwalkar** [01:19:44] So let's look at our chat. We said, load this file for me, and the AI basically went, spun up a Jupyter notebook, loaded pandas, looked at the file, and gave us a few rows.

**Rahul Sonwalkar** [01:19:44] I'm going to ask

[01:19:44] n/a: plot the Mail, pipe, overtime,

[01:21:43] n/a: in France.

**Rahul Sonwalkar** [01:21:53] So, the AI team's been writing this code, because pipe overtime in France for men, and then body type for us. And the good thing about Python, is If you spend a ton of time on SQL, what we realized was that SQL, it's really hard to write actually useful queries and do deep analysis like regression, etc.

**Rahul Sonwalkar** [01:21:53] with just SQL. With Python, you also get a whole ecosystem of modules built in. Right? matplotlib, pandas, numpy, escaler, and there's thousands of these. So, that was the initial insight, and then we built Julius about six months ago.

**Jerry Liu** [01:21:53] What's like the practical difference in UX between this and just

**Jerry Liu** [01:21:53] trajectory code interpreter?

**Rahul Sonwalkar** [01:21:53] Great question. Yeah, the question was, what is the difference between Julius and code interpreter? Really, there isn't. It's just better. We're focused, we're focused With people, or people who do stuff with data multiple times a day.

**Rahul Sonwalkar** [01:21:53] And we talked to a lot of these people, and we said, Okay, how can we build things for you that would help you do your job?

**Rahul Sonwalkar** [01:21:53] So, an example of this is on chat. gt, often times they'll give it a data set. People try to write their code, and sometimes that code has errors. And it kind of goes into this loop of trying to fix these little errors.

**Rahul Sonwalkar** [01:21:53] What we have focused on is, okay, how do we prevent that from happening? So we looked at thousands of users using us daily. Collected data on where these errors happened. And focused really hard on fixing those errors. Beforehand, before they actually happen at runtime.

**Rahul Sonwalkar** [01:21:53] This could mean a bunch of rules.

**Rahul Sonwalkar** [01:21:53] This could mean, you know, prompting changes, et cetera, and just preventing that from happening. Second of all, we have features that allow people who do stuff with data on a daily basis to go deep and do the last mile of analysis done. That could mean, you know, You can click, show code, go into the code, edit the code changes.

**Rahul Sonwalkar** [01:21:53] You can also give natural language instructions on the code. Finally, let's say you have this graph. And I want the graph to have some changes. Like, I want it to be a bar chart instead of instead of instead of a line graph. You can kind of just go in here and give natural language instructions to let the user take what the AI has done for it and then take it to the, to the finish line.

**Rahul Sonwalkar** [01:21:53] If you've seen that code interpreter, that's pretty hard for users to do. So we focus on data and that use case, and we will do that.

[01:21:53] n/a: Cool thanks guys!

**AI Charlie** [01:24:23] That's unfortunately all the time we had to feature demos, but many thanks to Botpress, Markov, Kura. ai, Sweep, and Motif as well for being finalists. For the last part of our anniversary celebration, we wanted to turn over the mics to you, our dear listeners. We hear so many great stories from listeners about how latent space has come into their lives, and we've never had the opportunity to feature them on the pod till now.

**AI Charlie** [01:24:23] Our first listener is Balaz Nemethy from Hungary, who talked about one of the most delightful gems in the latent space community, our weekly Discord paper club.

## [01:25:03] Latent Space Listeners[01:25:03] Listener 1 - Balázs Némethi (Hungary, Latent Space Paper Club)

**Swyx** [01:24:23] Tell me, tell people about, like, what happened. Yeah, like,

**Guest 1** [01:24:23] two weeks ago, two weeks ago, there was the paper reading club on Discord, and I, and then, halfway in, or like, one quarter in, like, the author of the paper showed up, and it was so fucking cool. Like, if you could do this, like, I was thinking, like, this should be a format, like, there is two minutes papers that probably, you know, who

**Swyx** [01:24:23] is, yeah he's Hungarian,

**Guest 1** [01:24:23] Living

**Swyx** [01:24:23] in Vienna, but like Karoly,

**Guest 1** [01:24:23] pronounced in Hungarian is Karoly, yes so that was so special because it's There is a certain amount of information in papers, the quality of paper might have dropped in the past year than before, due to the social media aspect of Archive.

**Guest 1** [01:24:23] So, having the person there and giving in even more details than just what you could read, was like, so amazing. I know it's really hard to organize, but like, If it would be possible to have more, maybe not recurring, like, you know, it's just like,

**Swyx** [01:24:23] oh, nice. The Matryoshka,

**Swyx** [01:24:23] yeah, yeah. So we have one next week the MRL paper, Matryoshka Representation Learning, which is a way of sorting embeddings so that you can truncate them. And OpenAI recently shipped this in their API for the new embeddings models, where you can reduce, like, a 3, 000 vector embedding to 265, so you save more than 90 percent on your embeddings.

**Swyx** [01:24:23] Vector database costs and speed and everything. Nice. So the authors are coming by and presenting at the Discord. I will join. I will join. Any other, like so basically I'm just going to record random opinions. I know how you produce the

**Guest 2** [01:24:23] podcast. So we're going to

**Swyx** [01:24:23] do this. You're going to be on the show.

**Swyx** [01:24:23] You're going to be on the show. Any other, like, how did you discover the podcast? What do you feel?

**Guest 1** [01:24:23] Discovered it on Spotify, searching basically AI. I use PocketCast for all my podcasts, but I was like, let's just search AI. I think I was searching for AI generated music, but it brought up podcasts.

**Guest 1** [01:24:23] And I was like, you know what, I'm kind of getting out of my previous industry. So like, I'm just going to separate. The whole AI following thing and I just like followed This was the first one that came up and then a couple of others just to like have it have it downloaded But I but this was like the literally the first podcast I'm following on Spotify when I follow like 70 on podcast So like I was like and I started I was like, okay, this is great Or they're only great podcasts, and I kept coming back to

**Swyx** [01:24:23] yours,

**Swyx** [01:24:23] there are other podcasts that we consider friends, and we try to do collaborations with them, and podcast swaps with them, so Yeah, that's great.

## [01:27:47] Listener 2 - Sylvia Tong (Sora/Jim Fan/EntreConnect)

**AI Charlie** [01:24:23] Our next listener is Sylvia Tong, founder of the OntraConnect community, a community of founders and investors supporting entrepreneurs in Silicon Valley. She wanted to discuss OpenAI Sora and Jim Phan from NVIDIA, who we have featured on our previous OpenAI Dev Day Recap podcast, and will be a future guest on LatentSpace.

**Swyx** [01:24:23] How did you find the podcast, and what do you feel about it, what do you want to tell people about it?

**Guest 2** [01:24:23] Actually, I know Jim Fan, so I, so Jim Fan, I know you! And then I follow your Twitter and follow your podcast. Yeah, yeah, yeah, yeah, yeah. It's another event, maybe you know Alliance AI, it's another community, and we like, they had that event like early last year, so they have various events, they, they are the founder of Stanford, so they are all Stanford grads, so they are even always in the Stanford University, like one of the room, yeah, so Jim Fan is one of the first speakers, so, yeah, and connect with him on WeChat, and, yeah, and connect with you, yeah, follow your Twitter!

**Swyx** [01:24:23] Jim is Jim is super friendly, and we have to have a full episode with him at some point. But he's, yeah, I mean, he's doing amazing things at NVIDIA. I'm sure he's very happy there.

**Guest 2** [01:24:23] You should ask him about Sora. The JAI video, yeah, he has so many opinions about, you know, yeah.

**Swyx** [01:24:23] I feel like, okay, Jim is this interesting mix between a researcher and a Content creator, right?

**Swyx** [01:24:23] So, Jim's take on Sora, I slightly disagree with, because he says it's basically a data driven world model, and a lot of people misinterpreted him, me included, basically saying like, oh, are you, are you saying that there's an underlying physics model behind Sora? And he's like, no, no, no, no, no, it's just, you know, using diffusion transformers to learn a representation of world models.

**Swyx** [01:24:23] It's not perfect. Then I'm like, okay, but that's a misleading analogy, I don't know. Anyway, so like

**Guest 2** [01:24:23] he But that's for the content purpose. That's for the Twitter content purpose. You have to, yeah,

**Swyx** [01:24:23] yeah. So I feel this, like, pull towards, like celebrating things on Twitter, but then also trying to be realistic.

**Swyx** [01:24:23] Trying to present, like, what is actually the thing instead of the hype. And it's very hard to separate. And that's something that's a challenge for Lanespace.

**Guest 2** [01:24:23] Yeah, it's hard, I feel it's hard to have the conversation on Twitter, so you need to have a conversation in the podcast. So invite a few people who maybe have to talk about Twitter, but really explain what they mean in your tweets.

**Guest 2** [01:24:23] Because, yeah, it's hard to understand just a few words. Yeah, so do you actually think Sora understands the physics of the

**Swyx** [01:24:23] world? A little bit. It's, yeah, Sora understands a little bit of physics. The problem with this is they cannot have 80 percent physics. Like, it's 100 or 0, like, otherwise you lose confidence in the thing.

**Swyx** [01:24:23] So that's why you have these generated models where the chair will show up and disappear, the spoon will show up and disappear, you know, like, that's all the artifacts you see in Sora. Which is good for us for now, because we're lucky that it's not good enough yet to consistently generate all those things.

**Swyx** [01:24:23] At some point it will be, we just wait two years, and it will be.

**Swyx** [01:24:23] Very cool. Thanks for it. I love this discussion. Thanks for listening. I'm really glad to have you as a listener.

**AI Charlie** [01:24:23] Alessio and Swyx covered the Jim Fan vs. Yan LeCun world model debate in the main pod, and you can click through the show notes for more detail directly from each of them. Our third listener is RJ Honecke, who comes from a data science background, but wanted to ask about how we think about learning in public in AI, and how that informs the context with which latent space is created.

## [01:31:23] Listener 3 - RJ (Developers building Community & Content)

**Swyx** [01:24:23] Hi, I'm RJ. Shawn, nice to meet you. Nice to meet you. Do you also listen to pod, or are you just here to hang out? Yes, very much. Oh, yeah. How do you feel about it?

**Guest 3** [01:24:23] The depth that you guys go into it's a lot deeper than other. This is a podcast that I listen to. I kind of found it, and then didn't switch back.

**Swyx** [01:24:23] Thanks!

**Guest 3** [01:24:23] What's your background? I, I am a data scientist.

**Guest 3** [01:24:23] I run a data team at cell communications equipment manufacturer. And we collect a ton of telemetry data, and, and other things like that. And I'm running a data team to make inferences about the health of our network, about, operating the network more efficiently and also in our manufacturing process and product development process to improve our ability to detect when we improve or, or get worse at operating, or, sorry, our products like build or hardware bills get better or worse.

**Guest 3** [01:24:23] So actually, I wanted to actually ask a question of you and your thoughts about this. So I find the discussion about model measurement and, and, and evaluation to be very similar to the problems that we have in wireless. Because you have this very non deterministic system, right? So I was thinking, and I also just read your your little thing about learn in public.

**Guest 3** [01:24:23] So I was thinking about trying to come up with a good way to, to, and I'm, I'm learning about some new techniques that we're starting to implement to monitor our development process and so forth, and evaluate our, the quality of our builds and our hardware, and I was thinking about trying to tie that in with evaluation of LLMs.

**Guest 3** [01:24:23] I just, I, I, I don't know. That's as far as I got in the thinking, but I just thought that would be a fun thing to try to put out there and wanted to hear your thoughts about how, how to, like go about

**Swyx** [01:24:23] that. Yeah. You can, you don't need anyone's permission. That's, that's the beauty of this thing. But also no one owes you anything.

**Swyx** [01:24:23] No one owes you their time, their attention or, you know, or, or, or responses. And I typically try to classify these things as different modes of learning in public. Mm-Hmm. , I think I have four modes that I sketched out, but the two I remember the most are Explorer and Connector, and then there are two more advanced modes, I think like Teacher or Builder or something like that.

**Swyx** [01:24:23] The Explorer is where you sort of like put things out as you go along. It's learning exhaust, where you don't have expectations so that anyone will read it. It's mostly just notes for yourself. And that actually, that lack of expectations frees you. Because then you're like, oh, like two people read it.

**Swyx** [01:24:23] Doesn't matter, it's useful to me. It's useful to my team, it's useful to me, it's useful to whoever comes after me because I documented my work and my thinking. And that's great. And I think that's, that's the way that most people should start, which is like, just lower, you're not going to be an influencer overnight, like, it's fine, completely but get your thoughts out there, and then also, but also, like, start having feelers in different directions on what works for you, what works is a combination of what you like to And what other people want from you, and you will know when people tell you they want more from you.

**Swyx** [01:24:23] And so then, when you get there, when you have expertise that you have that other people don't, then you switch gears into a connector, where you are now coming from a place of authority. Like, I know how to do this right, and I will teach you, because I have done this, and I have spent more time, paid more in my dues, and here's the lessons.

**Swyx** [01:24:23] Thank you. And then that comes to be, that tends to become more of a polished effort that tends to become more measurable or in terms of like the impact and the influence it can get. And I think that's, that's where people start moving towards. But basically just lower expectations, make it cheap to experiment, put out a lot of stuff in different directions and see where the market pulls you.

**Guest 3** [01:24:23] Okay. Yeah. So, I mean, do you have thoughts about, like, I'm very much aligned with like who cares about. I mean, I care, but my need is not to be a social media influencer. My need is to, like, I want to learn and I like the idea of, you know, sort of like sharing that with people and sharing the process with people.

**Guest 3** [01:24:23] So, like, thoughts about platform or like, I mean, I know it's going to be different for everyone, but like, what, what, what's it, what in your experience has changed? Has been successful while getting started.

**Swyx** [01:24:23] Yeah so I tend to tell developers, most developers to start on Hashnode these days. Hashnode is basically Medium if it was for developers and didn't suck.

**Swyx** [01:24:23] Because I hate Medium with a passion and a glowing, fiery hatred. Everyone does. It's comical how bad they are. But, I use Substack for latent space. I'm pretty happy with Substack. It's an email social network. Email is one of the most important things for people to like, come back to you frequently. So that you don't, you're not subject to an algorithm, you own your audience, you know.

**Swyx** [01:24:23] If you want to move off Substack someday, it'll let you take the emails and keep that relationship going with the people that you have. And that's super important as a creator. And then you can also write your own blog. And tweet, and tweet, and all that. I tend to say though Pay attention to what you enjoy, and what you spend the most time on.

**Swyx** [01:24:23] If you're a LinkedIn guy, be on LinkedIn. I'm not on LinkedIn, so I'm gonna do horrible on LinkedIn, because I don't know the metagame of LinkedIn. I don't know what does well, I don't know what people want. So I shouldn't even, I don't, I don't bother, I should try, because obviously there are like way more people on LinkedIn than there are on Twitter, but I'm just a Twitter guy.

**Swyx** [01:24:23] Like I'm, that's just, that's who I am I have, I have, I also sort of am old money there in a sense of I have an existing followership that predated Latentspace. You know, Latentspace doubled my following, but like, I had some before that. So, like, all that's great I just think, like, you're going to know the metagame, and that's actually very important, of, like, where you already spend time, like, I, I have friends who are, like, on TikTok, I have friends who are on YouTube a lot, I'm on YouTube a lot, I should do YouTube, because I know, I know what's, what's going on on YouTube, it's just, then you have to put the effort to, to do that, and I'm, I'm, like, video production is, like, the most expensive thing, anyway, long story short try to pay attention to, this, Complex mix of like, publishing platform existing embedded social network on that platform, And where you already spend times, so that you know how to create what will do well, just because you already spent time on it.

**Swyx** [01:24:23] Yeah, okay.

**Guest 3** [01:24:23] What's your favorite?

**Guest 3** [01:24:23] Favorite episode I really liked actually the the NeurIPS, like, recap because I haven't been to NeurIPS so You know how much time that took? Well, I mean, the episode is like four hours, right? Yeah. And that one I didn't, I didn't do the paper one because I, I actually I, I usually listen.

**Guest 3** [01:24:23] I don't watch. So I, like, it's be really hard to There's no video for that. Oh, there isn't? Oh, okay. So I, like, I have to find the paper and anyway. Yeah. So that's hard for me. Yeah. But I, I did enjoy the interviews in the other The startups episode. Yeah. Yeah.

**Swyx** [01:24:23] People love that.

**Swyx** [01:24:23] It just takes a ton of work, and I would love to offload it. This is going to be another one of those where I just kind of slip together little things. And it's good. It brings you there. That's the thing, right? Like, you're not there physically. I'm here. Let's, like, bring people into the closed community.

**Swyx** [01:24:23] And so I would like to do more of that.

**Guest 3** [01:24:23] Yeah, no, I really enjoy how you bring, like, a lot of people that I would not have otherwise even known about, let alone have access to, and then You have this conversation with them. It's really fun. Thanks

**Swyx** [01:24:23] for coming on. Can I, can I get your contact so that we can find you?

**Swyx** [01:24:23] Yeah. Yeah. Yeah. You're going to be on the pod. Oh, awesome.

**AI Charlie** [01:24:23] People seem to love the New Reap's recap pod, and we'll keep doing more of those when the right occasion presents itself. This was also a pick for our last listener, Jan Jung from Australia, who comes at AI from the design point of view and was very interested in our early AI UX work on latent space.

**AI Charlie** [01:24:23] If you're in SF and want to more novel AI UX ideas, reach out to him.

## [01:39:25] Listener 4 - Jan Zheng (Australia, AI UX)

**Guest 4** [01:24:23] My name is Yon, and I came across you on GitHub when I was looking for ways to solve problems on Svelte. And you pretty much answered all the questions I had for pretty much A couple of years, and then you left, and you started doing latent space, and I'm like, what is that?

**Guest 4** [01:24:23] What is an LLM? So I started listening to your pod, and yeah, and here I am. And

**Swyx** [01:24:23] then you're part, you're from Sydney, or you were, you were in sydney.

**Guest 4** [01:24:23] I, I moved to Sydney a couple years ago to work on a clinical trial, but now I moved back, probably, again, I blame you for it, because I listen to every episode, I'm like, shit's going down, in San Francisco, you gotta be here.

**Swyx** [01:24:23] So yeah, and then you were, you're part of build club.

**Guest 4** [01:24:23] Yeah, I'm part of BuildClub. BuildClub is a Unfortunately, I was at the airport when you're giving a presentation and Annie has not sent me the recording yet So I'm not seeing it. It's on YouTube.

**Swyx** [01:24:23] Oh, okay. Great.

**Guest 4** [01:24:23] Oh, awesome. Okay, I'll take a look. But BuildClub is the one and only AI centric community in Pretty much Sydney.

**Guest 4** [01:24:23] And I had to spend months to push Annie to do that thing. And eventually she did, and I'm so glad she did. And it's growing, and she's doing amazing. She's expanding to many cities. It's ANZ now. Yeah, it's amazing. And she has our couch from our apartment when we moved away. We couldn't find a way to sell it.

**Guest 4** [01:24:23] We're like, hey Annie, we're getting a space. Do you guys need a couch? She's like, sure. So she has my couch. It's amazing.

**Swyx** [01:24:23] And then what do you listen for in, in, in space? What, you know,

**Guest 4** [01:24:23] what are you interested in? I like to get a sense of what's going on. You guys ask very good questions. For some reason you guys seem so well researched, both you and Alessio.

**Guest 4** [01:24:23] Somehow you're just You asked very good questions that me as a Person, like, general product developer, product engineer, I have no idea about ML, I don't follow the papers, I know about the paper club, I don't follow it because it's over my head, but you guys distill it so well, and you guys ask the questions to your guests that I have in the back of my mind, or that I don't even know that I have the questions and then I You guys guide the conversations in a way that I can learn from and I wouldn't even know anything to ask So I'm so glad you guys are doing it.

**Guest 4** [01:24:23] It's so helpful and Keep doing what you're doing. Yeah, and I really and I really love the What you guys did with the best papers from the talk Yeah, it's really good I mean like a lot of that was way over my head But I like listen to it all and try to I just get the sense, like, just, I just try to keep listening to this stuff until I get it.

**Guest 4** [01:24:23] And you guys expose, I mean, I would never go to a conference like that, but, yeah. But like, I was just like, not understanding anything, but you guys make it so accessible, and I love it.

**Swyx** [01:24:23] Yeah, so, maybe, the Pocket Studio is right here, actually, I can show you after we're done recording. It's not that fancy, it's just a studio.

**Swyx** [01:24:23] And yeah, for me, the goal within NeurIPS recap, was not that we would, like, you would read everything or anything, like, yeah, we would just pick what we thought was most important for you, and if any one of them interested you, you could double click on it. That's it. You know, we're not gonna be, like, the experts on every single thing.

**Swyx** [01:24:23] It's impossible, right? And already, like, the episode that I cut together for that was like three and a half hours, so people were complaining about that. And then the last thing Lesser and I don't do that much research for each episode, but, you know, we research the guests.

**Swyx** [01:24:23] But just being involved in the day to day conversations in our day jobs prepares you for that. And I think that is important. No prep needed because, you know, we're in it. We're in the arena, as they say. Yeah. Anything else?

**Guest 4** [01:24:23] Like, like there's so much excitement. There's so many things to cover. And like what you guys are like, maybe culturally, yeah, that, that would be a thing I was always wondering, like, like, and that might be not partly in the space, but what are you guys doing? Like to cover the cultural aspect of what's happening here, it's probably like.

**Guest 4** [01:24:23] A separate thing, but equally important thing, to like, document all the conversations that are happening around here. And all the other build spaces, like, we see glimpses of that on Twitter, but I think capturing more of that would be super cool.

**Swyx** [01:24:23] Yeah I feel like that's something that someone else should do.

**Swyx** [01:24:23] We try to be more technical. Because that, that, people can use it at work, they can justify that for productivity. We might try to Dabble in some of that. So I'm pretty connected with like, the main areas for those listening The main areas for those listening who are interested in like SFAI is like Shack 15, AGI House SF, AGI House Hillsboro and then us and maybe HF0 and then maybe a little bit of Founders Inc.

**Swyx** [01:24:23] And those are it. There's this like, There's more community oriented spaces like the commons but like they're not sort of AI centric. And So we can do a little bit of reporting around that, but it's gonna be like, this American life, you know, like, tell me your life story, like, solve story, I'm not like, the best at that, and then also, like, there's a lot of very, very brutal cutting for that, that is hard to do, but we can dabble, or we can do it on the

**Guest 4** [01:24:23] side.

**Guest 4** [01:24:23] Oh, the other thing I'm very interested in, I'm a UX designer by trade, and anytime you guys touch on AI and UX and Jet or UI, I'm all ears, and I would love to, Again, it's probably not the technical side of LatentSpace, but I think there needs to be a hundred times more resources out there than what's currently available.

**Swyx** [01:24:23] Yeah, yeah we had a, we, I think we held the first AIUX meetup ever in the, in, in SF, in Worlds. That was really fun. The meetup's on YouTube, if you want to see it, and, and it's in the LatentSpace archives of the newsletter. I don't think we ever published a podcast version of it.

**Swyx** [01:24:23] So you have to just subscribe to the newsletter and then check the YouTube for, for that stuff. But yeah, UX is a topic of ours that we like to cover. It's just very hard to cover as an audio medium. Yeah. 'cause you can't see it . And also I think like it's gonna be mostly owned by like Notion and Versal and Retool, which we've, we've interviewed retool, we're going to interview Versa and we've interviewed Notion.

**Swyx** [01:24:23] So who else who, who's who? Like who do you wanna listen to on the IX? Right. Like, there's individual people, like we had Amelia Wattenberger present at AI Engineer Summit, you can see that on YouTube. Like, I know a lot of the thinkers on AIUX, and I think I know what they say, like, I haven't seen anything super innovative.

**Swyx** [01:24:23] Everyone hates chatbots, everyone wants to innovate things. I haven't seen any new ideas since we did the AIUX meetup one year ago. Tell me I'm wrong.

**Guest 4** [01:24:23] Well, that sounds really disappointing. I haven't seen anything on Twitter that I thought that would be easier to push because we just wrap LLMs. But on Twitter there doesn't seem to be that much going on, to your point.

**Guest 4** [01:24:23] But there needs to be more people from the design space, from the product space, like UX researchers, coming in and figuring out how can we take LLMs and apply them to real problems. I haven't seen a whole lot of that. In Cine, there's not a whole lot of that. I'm hoping to maybe be a part of the community here and try to grow that side of

**Swyx** [01:24:23] the things.

**Swyx** [01:24:23] Well, look, you're here now. You're interested in AIUX. Run the next AIUX meetup. I can set you up with the venue, the people. You need to find the speakers. I'm not going to find the speakers for you. But if you want to set that up, go for it.

**Guest 4** [01:24:23] So, I actually copied your AIUX format, and I held a talk in Sydney, and in a very light fashion, like 20 30 people showed up.

**Guest 4** [01:24:23] We had some cool demos, it was like a baby, like a small version of your AIUX conference, but yeah, I'd love to, love to participate. I mean,

**Swyx** [01:24:23] this is SF, 300 people will show up you just gotta get some cool demos, I can siege you with some people let's make it happen. Let's make it happen! Let's make it happen, alright, well it's nice to meet you, and I'll get your details.

**AI Charlie** [01:24:23] That's all, folks. If you've enjoyed or benefited from our work on latent space over this past year, we'd really love to hear from you, and really appreciate it if you'd tell a friend. The only way a podcast consistently grows is through your word of mouth, and that helps us book incredible guests and attend great events in our second year.

**AI Charlie** [01:24:23] Have a lovely weekend!
