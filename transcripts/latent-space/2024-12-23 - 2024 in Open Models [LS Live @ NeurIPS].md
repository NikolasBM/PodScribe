---
podcast: "latent-space"
podcast_title: "Latent Space"
title: "2024 in Open Models [LS Live @ NeurIPS]"
date: 2024-12-23
url: "https://www.latent.space/p/2024-open-models"
guid: "substack:153509369"
host: "Swyx"
transcript_source: "publisher"
---

# 2024 in Open Models [LS Live @ NeurIPS]

**AI Charlie** [00:00:00] Welcome to Latent Space Live, our first mini conference held at NeurIPS 2024 in Vancouver. This is Charlie, your AI co host. As a special treat this week, we're recapping the best of 2024 going domain by domain. We sent out a survey to the over 900 of you who told us what you wanted, and then invited the best speakers in the latent space network to cover each field.

**AI Charlie** [00:00:00] 200 of you joined us in person throughout the day, with over 2, 200 watching live online. Our next keynote covers the state of open models in 2024, with Luca Soldani and Nathan Lambert of the Allen Institute for AI, with a special appearance from Dr. Sophia Yang of Mistral. Our first hit episode of 2024 was with Nathan Lambert on RLHF 201 back in January.

**AI Charlie** [00:00:00] Where he discussed both reinforcement learning for language models and the growing post training and mid training stack with hot takes on everything from constitutional AI to DPO to rejection sampling and also previewed the sea change coming to the Allen Institute. And to Interconnects, his incredible substack on the technical aspects of state of the art AI training.

**AI Charlie** [00:01:00] We highly recommend subscribing to get access to his Discord as well. It is hard to overstate how much open models have exploded this past year. In 2023, only five names were playing in the top LLM ranks. Mistral, Mosaics MPT, and Gatsby. TII UAE's Falcon, Yi, from Kaifu Lee's 01. ai, And of course, Meta's Lama 1 and 2.

**AI Charlie** [00:01:00] This year, a whole cast of new open models have burst on the scene. From Google's Jemma and Cohere's Command R, To Alibaba's Quen and DeepSeq models, to LLM360 and DCLM, and of course, to the Allen Institute's OLMO, OLMOE, PIXMO, MOLMO, and OLMO2 models. Pursuing open model research comes with a lot of challenges beyond just funding and access to GPUs and datasets, particularly the regulatory debates this year across Europe.

**AI Charlie** [00:02:00] California and the White House. We also were honored to hear from Mistral, who also presented a great session at the AI Engineer World's Fair Open Models track. As always, don't forget to check the show notes for the YouTube link to their talk, as well as their slides. Watch out and take care.

## [00:02:35] Luca Intro

**Luca Soldaini** [00:02:00] Cool. Yeah, thanks for having me over. I'm Luca. I'm a research scientist at the Allen Institute for AI. I threw together a few slides on sort of like a recap of like interesting themes in open models for, for 2024. Have about maybe 20, 25 minutes of slides, and then we can chat if there are any questions.

**Luca Soldaini** [00:02:00] If I can advance to the next slide. Okay, cool. So I did the quick check of like, to sort of get a sense of like, how much 2024 was different from 2023. So I went on Hugging Face and sort of get, tried to get a picture of what kind of models were released in 2023 and like, what do we get in 2024?

**Luca Soldaini** [00:03:00] 2023 we get, we got things like both LLAMA 1 and 2, we got Mistral, we got MPT, Falcon models, I think the YI model came in at the end. Tail end of the year. It was a pretty good year. But then I did the same for 2024. And it's actually quite stark difference. You have models that are, you know, reveling frontier level.

**Luca Soldaini** [00:03:00] Performance of what you can get from closed models from like Quen, from DeepSeq. We got Llama3. We got all sorts of different models. I added our own Olmo at the bottom. There's this growing group of like, Fully open models that I'm going to touch on a little bit later. But you know, just looking at the slides, it feels like 2024 was just smooth sailing, happy knees, much better than previous year.

**Luca Soldaini** [00:04:00] And you know, you can plot you can pick your favorite benchmark Or least favorite, I don't know, depending on what point you're trying to make. And plot, you know, your closed model, your open model and sort of spin it in ways that show that, oh, you know open models are much closer to where closed models are today versus to Versus last year where the gap was fairly significant.

**Luca Soldaini** [00:04:00] So one thing that I think I don't know if I have to convince people in this room, but usually when I give this talks about like open models, there is always like this background question in, in, in people's mind of like, why should we use open models? APIs argument, you know, it's, it's. Just an HTTP request to get output from a, from one of the best model out there.

**Luca Soldaini** [00:04:00] Why do I have to set up infra and use local models? And there are really like two answer. There is the more researchy answer for this, which is where it might be. Background lays, which is just research. If you want to do research on language models, research thrives on, on open models, there is like large swath of research on modeling, on how these models behave on evaluation and inference on mechanistic interpretability that could not happen at all if you didn't have open models they're also for AI builders, they're also like.

**Luca Soldaini** [00:05:00] Good use cases for using local models. You know, you have some, this is like a very not comprehensive slides, but you have things like there are some application where local models just blow closed models out of the water. So like retrieval, it's a very clear example. We might have like constraints like Edge AI applications where it makes sense.

**Luca Soldaini** [00:05:00] But even just like in terms of like stability, being able to say this model is not changing under the hood. It's, there's plenty of good cases for, for open models. And the community is just not models. Is I stole this slide from one of the Quent2 announcement blog posts. But it's super cool to see like how much tech exists around open models and serving them on making them efficient and hosting them.

**Luca Soldaini** [00:06:00] It's pretty cool. And so. It's if you think about like where the term opens come from, comes from like the open source really open models meet the core tenants of, of open, of open source specifically when it comes around collaboration, there is truly a spirit, like through these open models, you can build on top of other people.

**Luca Soldaini** [00:06:00] innovation. We see a lot of these even in our own work of like, you know, as we iterate in the various versions of Alma it's not just like every time we collect from scratch all the data. No, the first step is like, okay, what are the cool data sources and datasets people have put together for language model for training?

**Luca Soldaini** [00:07:00] Or when it comes to like our post training pipeline We one of the steps is you want to do some DPO and you use a lot of outputs of other models to improve your, your preference model. So it's really having like an open sort of ecosystem benefits and accelerates the development of open models.

## [00:07:23] The Definition of Open Models

**Luca Soldaini** [00:07:00] One thing that we got in 2024, which is not a specific model, but I thought it was really significant, is we first got we got our first open source AI definition. So this is from the open source initiative they've been generally the steward of a lot of the open source licenses when it comes to software and so they embarked on this journey in trying to figure out, okay, How does a license, an open source license for a model look like?

**Luca Soldaini** [00:07:00] Majority of the work is very dry because licenses are dry. So I'm not going to walk through the license step by step, but I'm just going to pick out one aspect that is very good and then one aspect that personally feels like it needs improvement on the good side. This this open source AI license actually.

**Luca Soldaini** [00:08:00] This is very intuitive. If you ever build open source software and you have some expectation around like what open source looks like for software for, for AI, sort of matches your intuition. So, the weights need to be fairly available the code must be released with an open source license and there shouldn't be like license clauses that block specific use cases.

**Luca Soldaini** [00:08:00] So. Under this definition, for example, LLAMA or some of the QUEN models are not open source because the license says you can't use this model for this or it says if you use this model you have to name the output this way or derivative needs to be named that way. Those clauses don't meet open source definition and so they will not be covered.

**Luca Soldaini** [00:09:00] The LLAMA license will not be covered under the open source definition. It's not perfect. One of the thing that, um, internally, you know, in discussion with with OSI, we were sort of disappointed is around the language. For data. So you might imagine that an open source AI model means a model where the data is freely available.

**Luca Soldaini** [00:09:00] There were discussion around that, but at the end of the day, they decided to go with a softened stance where they say a model is open source if you provide sufficient detail information. On how to sort of replicate the data pipeline. So you have an equivalent system, sufficient, sufficiently detailed.

**Luca Soldaini** [00:09:00] It's very, it's very fuzzy. Don't like that. An equivalent system is also very fuzzy. And this doesn't take into account the accessibility of the process, right? It might be that you provide enough information, but this process costs, I don't know, 10 million to do. Now the open source definition. Like, any open source license has never been about accessibility, so that's never a factor in open source software, how accessible software is.

**Luca Soldaini** [00:10:00] I can make a piece of open source, put it on my hard drive, and never access it. That software is still open source, the fact that it's not widely distributed doesn't change the license, but practically there are expectations of like, what we want good open sources to be. So, it's, It's kind of sad to see that the data component in this license is not as, as, Open as some of us would like would like it to be.

## [00:10:40] Challenges for Open Models

**Luca Soldaini** [00:10:00] and I linked a blog post that Nathan wrote on the topic that it's less rambly and easier to follow through. One thing that in general, I think it's fair to say about the state of open models in 2024 is that we know a lot more than what we knew in, in 2023. Like both on the training data, like And the pre training data you curate on like how to do like all the post training, especially like on the RL side.

**Luca Soldaini** [00:11:00] You know, 2023 was a lot of like throwing random darts at the board. I think 2024, we have clear recipes that, okay, don't get the same results as a closed lab because there is a cost in, in actually matching what they do. But at least we have a good sense of like, okay, this is, this is the path to get state of the art language model.

**Luca Soldaini** [00:11:00] I think that one thing that it's a downside of 2024 is that I think we are more research constrained in 2023. It feels that, you know, the barrier for compute that you need to, to move innovation along as just being right rising and rising. So like, if you go back to this slide, there is now this, this cluster of models that are sort of released by the.

**Luca Soldaini** [00:11:00] Compute rich club. Membership is hotly debated. You know, some people don't want to be. Called the rich because it comes to expectations. Some people want to be called rich, but I don't know, there's debate, but like, these are players that have, you know, 10, 000, 50, 000 GPUs at minimum. And so they can do a lot of work and a lot of exploration and improving models that it's not very accessible.

**Luca Soldaini** [00:12:00] To give you a sense of like how I personally think about. Research budget for each part of the, of the language model pipeline is like on the pre training side, you can maybe do something with a thousand GPUs, really you want 10, 000. And like, if you want real estate of the art, you know, your deep seek minimum is like 50, 000 and you can scale to infinity.

**Luca Soldaini** [00:12:00] The more you have, the better it gets. Everyone on that side still complains that they don't have enough GPUs. Post training is a super wide sort of spectrum. You can do as little with like eight GPUs as long as you're able to run, you know, a good version of, say, a LLAMA model, you can do a lot of work there.

**Luca Soldaini** [00:13:00] You can scale a lot of the methodology, just like scales with compute, right? If you're interested in you know, your open replication of what OpenAI's O1 is you're going to be on the 10K spectrum of our GPUs. Inference, you can do a lot with very few resources. Evaluation, you can do a lot with, well, I should say at least one GPUs if you want to evaluate GPUs.

**Luca Soldaini** [00:13:00] Open models but in general, like if you are, if you care a lot about intervention to do on this model, which it's my prefer area of, of research, then, you know, the resources that you need are quite, quite significant. Yeah. One other trends that has emerged in 2024 is this cluster of fully open models.

**Luca Soldaini** [00:13:00] So Omo the model that we built at ai, two being one of them and you know, it's nice that it's not just us. There's like a cluster of other mostly research efforts who are working on this. And so it's good to to give you a primer of what like fully open means. So fully open, the easy way to think about it is instead of just releasing a model checkpoint that you run, you release a full recipe so that other people working on it.

**Luca Soldaini** [00:14:00] Working on that space can pick and choose whatever they want from your recipe and create their own model or improve on top of your model. You're giving out the full pipeline and all the details there instead of just like the end output. So I pull up the screenshot from our recent MOE model.

**Luca Soldaini** [00:14:00] And like for this model, for example, we released the model itself. Data that was trained on, the code, both for training and inference all the logs that we got through the training run, as well as every intermediate checkpoint and like the fact that you release different part of the pipeline allows others to do really cool things.

**Luca Soldaini** [00:15:00] So for example, this tweet from early this year from folks in news research they use our pre training data to do a replication of the BitNet paper in the open. So they took just a Really like the initial part of a pipeline and then the, the thing on top of it. It goes both ways.

**Luca Soldaini** [00:15:00] So for example, for the Olmo2 model a lot of our pre trained data for the first stage of pre training was from this DCLM initiative that was led by folks Ooh, a variety of ins a variety of institutions. It was a really nice group effort. But you know, for When it was nice to be able to say, okay, you know, the state of the art in terms of like what is done in the open has improved.

## [00:15:46] AI2 Models - Olmo, Molmo, Pixmo etc

**Luca Soldaini** [00:15:00] We don't have to like do all this work from scratch to catch up the state of the art. We can just take it directly and integrate it and do our own improvements on top of that. I'm going to spend a few minutes doing like a shameless plug for some of our fully open recipes. So indulge me in this.

**Luca Soldaini** [00:16:00] So a few things that we released this year was, as I was mentioning, there's OMOE model which is, I think still is state of the art MOE model in its size class. And it's also. Fully open, so every component of this model is available. We released a multi modal model called Molmo. Molmo is not just a model, but it's a full recipe of how you go from a text only model to a multi modal model, and we apply this recipe on top of Quent checkpoints, on top of Olmo checkpoints, as well as on top of OlmoE.

**Luca Soldaini** [00:16:00] And I think there'd be a replication doing that on top of Mistral as well. The post training side we recently released 2. 0. 3. Same story. This is a recipe on how you go from a base model to A state of the art post training model. We use the Tulu recipe on top of Olmo, on top of Llama, and then there's been open replication effort to do that on top of Quen as well.

**Luca Soldaini** [00:17:00] It's really nice to see like, you know, when your recipe sort of, it's kind of turnkey, you can apply it to different models and it kind of just works. And finally, the last thing we released this year was Olmo 2, which so far is the best state of the art. Fully open language model a Sera combines aspect from all three of these previous models.

**Luca Soldaini** [00:17:00] What we learn on the data side from MomoE and what we learn on like making models that are easy to adapt from the Momo project and the Tulu project. I will close with a little bit of reflection of like ways this, this ecosystem of open models like it's not all roses. It's not all happy. It feels like day to day, it's always in peril.

**Luca Soldaini** [00:17:00] And, you know, I talked a little bit about like the compute issues that come with it. But it's really not just compute. One thing that is on top of my mind is due to like the environment and how you know, growing feelings about like how AI is treated. It's actually harder to get access to a lot of the data that was used to train a lot of the models up to last year.

**Luca Soldaini** [00:18:00] So this is a screenshot from really fabulous work from Shane Longpre who's, I think is in Europe about Just access of like diminishing access to data for language model pre training. So what they did is they went through every snapshot of common crawl. Common crawl is this publicly available scrape of the, of a subset of the internet.

**Luca Soldaini** [00:18:00] And they looked at how For any given website whether a website that was accessible in say 2017, what, whether it was accessible or not in 2024. And what they found is as a reaction to like the close like of the existence of closed models like OpenAI or Cloud GPT or Cloud a lot of content owners have blanket Blocked any type of crawling to your website.

**Luca Soldaini** [00:18:00] And this is something that we see also internally at AI2. Like one project that we started this year is we wanted to, we wanted to understand, like, if you're a good citizen of the internet and you crawl following sort of norms and policy that have been established in the last 25 years, what can you crawl?

**Luca Soldaini** [00:19:00] And we found that there's a lot of website where. The norms of how you express preference of whether to crawl your data or not are broken. A lot of people would block a lot of crawling, but do not advertise that in RobustDXT. You can only tell that they're crawling, that they're blocking you in crawling when you try doing it.

**Luca Soldaini** [00:19:00] Sometimes you can't even crawl the robots. txt to, to check whether you're allowed or not. And then a lot of websites there's, there's like all these technologies that historically have been, have existed to make websites serving easier such as Cloudflare or DNS. They're now being repurposed for blocking AI or any type of crawling in a way that is Very opaque to the content owners themselves.

**Luca Soldaini** [00:20:00] So, you know, you go to these websites, you try to access them and they're not available and you get a feeling it's like, Oh, someone changed, something changed on the, on the DNS side that it's blocking this and likely the content owner has no idea. They're just using a Cloudflare for better, you know, load balancing.

**Luca Soldaini** [00:20:00] And this is something that was sort of sprung on them with very little notice. And I think the problem is this, this blocking or ideas really, it impacts people in different ways. It disproportionately helps companies that have a headstart, which are usually the closed labs and it hurts incoming newcomer players where either have now to do things in a sketchy way or you're never going to get that content that the closed lab might have.

**Luca Soldaini** [00:20:00] So there's a lot, it was a lot of coverage. I'm going to plug Nathan's blog post again. That is, that I think the title of this one is very succinct which is like, we're actually not, You know, before thinking about running out of training data, we're actually running out of open training data. And so if we want better open models they should be on top of our mind.

## [00:21:13] Regulation and Lobbying

**Luca Soldaini** [00:21:00] The other thing that has emerged is that there is strong lobbying efforts on trying to define any kind of, AI as like a new extremely risky and I want to be precise here. Like the problem is now, um, like the problem is not not considering the risk of this technology. Every technology has risks that, that should always be considered.

**Luca Soldaini** [00:21:00] The thing that it's like to me is sorry, is ingenious is like just putting this AI on a pedestal and calling it like, An unknown alien technology that has like new and undiscovered potentials to destroy humanity. When in reality, all the dangers I think are rooted in dangers that we know from existing software industry or existing issues that come with when using software on on a lot of sensitive domains, like medical areas.

**Luca Soldaini** [00:22:00] And I also noticed a lot of efforts that have actually been going on and trying to make this open model safe. I pasted one here from AI2, but there's actually like a lot of work that has been going on on like, okay, how do you make, if you're distributing this model, Openly, how do you make it safe?

**Luca Soldaini** [00:22:00] How, what's the right balance between accessibility on open models and safety? And then also there's annoying brushing of sort of concerns that are then proved to be unfounded under the rug. You know, if you remember the beginning of this year, it was all about bio risk of these open models.

**Luca Soldaini** [00:22:00] The whole thing fizzled because as being Finally, there's been like rigorous research, not just this paper from Cohere folks, but it's been rigorous research showing that this is really not a concern that we should be worried about. Again, there is a lot of dangerous use of AI applications, but this one was just like, A lobbying ploy to just make things sound scarier than they actually are.

**Luca Soldaini** [00:23:00] So I got to preface this part. It says, this is my personal opinion. It's not my employer, but I look at things like the SP 1047 from, from California. And I think we kind of dodged a bullet on, on this legislation. We, you know, the open source community, a lot of the community came together at the last, sort of the last minute and did a very good effort trying to explain all the negative impact of this bill.

**Luca Soldaini** [00:23:00] But There's like, I feel like there's a lot of excitement on building these open models or like researching on these open models. And lobbying is not sexy it's kind of boring but it's sort of necessary to make sure that this ecosystem can, can really thrive. This end of presentation, I have Some links, emails, sort of standard thing in case anyone wants to reach out and if folks have questions or anything they wanted to discuss.

**Luca Soldaini** [00:24:00] Is there an open floor? I think we have Sophia

[00:24:00] swyx: who wants to who one, one very important open model that we haven't covered is Mistral. Ask her on this slide. Yeah, yeah. Well, well, it's nice to have the Mistral person talk recap the year in Mistral. But while Sophia gets set up, does anyone have like, just thoughts or questions about the progress in this space?

## [00:24:32] Questions - Incentive Alignment

[00:24:16] swyx: Do you always have questions?

**Quesiton** [00:24:32] I'm very curious how we should build incentives to build open models, things like Francois Chollet's ArcPrize, and other initiatives like that. What is your opinion on how we should better align incentives in the community so that open models stay open?

**Luca Soldaini** [00:24:32] The incentive bit is, like, really hard.

**Luca Soldaini** [00:24:32] Like, even It's something that I actually, even we think a lot about it internally because like building open models is risky. It's very expensive. And so people don't want to take risky bets. I think the, definitely like the challenges like our challenge, I think those are like very valid approaches for it.

**Luca Soldaini** [00:25:00] And then I think in general, promoting, building, so, any kind of effort to participate in this challenge, in those challenges, if we can promote doing that on top of open models and sort of really lean into like this multiplier effect, I think that is a good way to go. If there were more money for that.

**Luca Soldaini** [00:25:00] For efforts like research efforts around open models. There's a lot of, I think there's a lot of investments in companies that at the moment are releasing their model in the open, which is really cool. But it's usually more because of commercial interest and not wanting to support this, this like open models in the longterm, it's a really hard problem because I think everyone is operating sort of in what.

**Luca Soldaini** [00:26:00] Everyone is at their local maximum, right? In ways that really optimize their position on the market. Global maximum is harder to achieve.

**Question2** [00:26:00] Can I ask one question? No.

**Luca Soldaini** [00:26:00] Yeah.

**Question2** [00:26:00] So I think one of the gap between the closed and open source models is the mutability. So the closed source models like chat GPT works pretty good on the low resource languages, which is not the same on the open, open source models, right?

**Question2** [00:26:00] So is it in your plan to improve on that?

**Luca Soldaini** [00:26:00] I think in general,

**Luca Soldaini** [00:26:00] yes, is I think it's. I think we'll see a lot of improvements there in, like, 2025. Like, there's groups like, Procurement English on the smaller side that are already working on, like, better crawl support, multilingual support. I think what I'm trying to say here is you really want to be experts.

**Luca Soldaini** [00:26:00] who are actually in those countries that teach those languages to participate in the international community. To give you, like, a very easy example I'm originally from Italy. I think I'm terribly equipped to build a model that works well in Italian. Because one of the things you need to be able to do is having that knowledge of, like, okay, how do I access, you know, how Libraries, or content that is from this region that covers this language.

**Luca Soldaini** [00:27:00] I've been in the US long enough that I no longer know. So, I think that's the efforts that folks in Central Europe, for example, are doing. Around like, okay, let's tap into regional communities. To get access you know, to bring in collaborators from those areas. I think it's going to be, like, very crucial for getting products there.

## [00:27:46] Mistral intro

**Sophia Yang** [00:27:00] Hi everyone. Yeah, I'm super excited to be here to talk to you guys about Mistral. A really short and quick recap of what we have done, what kind of models and products we have released in the past year and a half. So most of you We have already known that we are a small startup funded about a year and a half ago in Paris in May, 2003, it was funded by three of our co founders, and in September, 2003, we released our first open source model, Mistral 7b yeah, how, how many of you have used or heard about Mistral 7b?

**Sophia Yang** [00:28:00] Hey, pretty much everyone. Thank you. Yeah, it's our Pretty popular and community. Our committee really loved this model, and in December 23, we, we released another popular model with the MLE architecture Mr. A X seven B and oh. Going into this year, you can see we have released a lot of things this year.

**Sophia Yang** [00:28:00] First of all, in February 2004, we released MrSmall, MrLarge, LeChat, which is our chat interface, I will show you in a little bit. We released an embedding model for, you know, converting your text into embedding vectors, and all of our models are available. The, the big cloud resources. So you can use our model on Google cloud, AWS, Azure Snowflake, IBM.

**Sophia Yang** [00:29:00] So very useful for enterprise who wants to use our model through cloud. And in April and May this year, we released another powerful open source MOE model, AX22B. And we also released our first code. Code Model Coastal, which is amazing at 80 plus languages. And then we provided another fine tuning service for customization.

**Sophia Yang** [00:29:00] So because we know the community love to fine tune our models, so we provide you a very nice and easy option for you to fine tune our model on our platform. And also we released our fine tuning code base called Menstrual finetune. It's open source, so feel free to take it. Take a look and.

**Sophia Yang** [00:29:00] More models. On July 2, November this year, we released many, many other models. First of all is the two new small, best small models. We have Minestra 3B great for Deploying on edge devices we have Minstrel 8B if you used to use Minstrel 7B, Minstrel 8B is a great replacement with much stronger performance than Minstrel 7B.

**Sophia Yang** [00:30:00] We also collaborated with NVIDIA and open sourced another model, Nemo 12B another great model. And Just a few weeks ago, we updated Mistral Large with the version 2 with the updated, updated state of the art features and really great function calling capabilities. It's supporting function calling in LatentNate.

**Sophia Yang** [00:30:00] And we released two multimodal models Pixtral 12b. It's this open source and Pixtral Large just amazing model for, models for not understanding images, but also great at text understanding. So. Yeah, a lot of the image models are not so good at textual understanding, but pixel large and pixel 12b are good at both image understanding and textual understanding.

**Sophia Yang** [00:31:00] And of course, we have models for research. Coastal Mamba is built on Mamba architecture and MathRoll, great with working with math problems. So yeah, that's another model.

**Sophia Yang** [00:31:00] Here's another view of our model reference. We have several premier models, which means these models are mostly available through our API. I mean, all of the models are available throughout our API, except for Ministry 3B. But for the premier model, they have a special license. Minstrel research license, you can use it for free for exploration, but if you want to use it for enterprise for production use, you will need to purchase a license from us.

**Sophia Yang** [00:32:00] So on the top row here, we have Minstrel 3b and 8b as our premier model. Minstrel small for best, best low latency use cases, MrLarge is great for your most sophisticated use cases. PixelLarge is the frontier class multimodal model. And, and we have Coastral for great for coding and then again, MrEmbedding model.

**Sophia Yang** [00:32:00] And The bottom, the bottom of the slides here, we have several Apache 2. 0 licensed open way models. Free for the community to use, and also if you want to fine tune it, use it for customization, production, feel free to do so. The latest, we have Pixtros 3 12b. We also have Mr. Nemo mum, Coastal Mamba and Mastro, as I mentioned, and we have three legacy models that we don't update anymore.

**Sophia Yang** [00:32:00] So we recommend you to move to our newer models if you are still using them. And then, just a few weeks ago, we did a lot of, uh, improvements to our code interface, Lachette. How many of you have used Lachette? Oh, no. Only a few. Okay. I highly recommend Lachette. It's chat. mistral. ai. It's free to use.

**Sophia Yang** [00:33:00] It has all the amazing capabilities I'm going to show you right now. But before that, Lachette in French means cat. So this is actually a cat logo. If you You can tell this is the cat eyes. Yeah. So first of all, I want to show you something Maybe let's, let's take a look at image understanding.

**Sophia Yang** [00:33:00] So here I have a receipts and I want to ask, just going to get the prompts. Cool. So basically I have a receipt and I said I ordered I don't know. Coffee and the sausage. How much do I owe? Add a 18 percent tip. So hopefully it was able to get the cost of the coffee and the sausage and ignore the other things.

**Sophia Yang** [00:34:00] And yeah, I don't really understand this, but I think this is coffee. It's yeah. Nine, eight. And then cost of the sausage, we have 22 here. And then it was able to add the cost, calculate the tip, and all that. Great. So, it's great at image understanding, it's great at OCR tasks. So, if you have OCR tasks, please use it.

**Sophia Yang** [00:34:00] It's free on the chat. It's also available through our API. And also I want to show you a Canvas example. A lot of you may have used Canvas with other tools before. But, With Lachat, it's completely free again. Here, I'm asking it to create a canvas that's used PyScript to execute Python in my browser.

**Sophia Yang** [00:34:00] Let's see if it works. Import this. Okay, so, yeah, so basically it's executing Python here. Exactly what we wanted. And the other day, I was trying to ask Lachat to create a game for me. Let's see if we can make it work. Yeah, the Tetris game. Yep. Let's just get one row. Maybe. Oh no. Okay. All right. You get the idea. I failed my mission. Okay. Here we go. Yay! Cool. Yeah. So as you can see, Lachet can write, like, a code about a simple game pretty easily. And you can ask Lachet to explain the code. Make updates however you like. Another example. There is a bar here I want to move.

**Sophia Yang** [00:35:00] Okay, great, okay. And let's go back to another one. Yeah, we also have web search capabilities. Like, you can ask what's the latest AI news. Image generation is pretty cool. Generate an image about researchers. Okay. In Vancouver? Yeah, it's Black Forest Labs flux Pro. Again, this is free, so Oh, cool.

**Sophia Yang** [00:36:00] I guess researchers here are mostly from University of British Columbia. That's smart. Yeah. So this is Laia ira. Please feel free to use it. And let me know if you have any feedback. We're always looking for improvement and we're gonna release a lot more powerful features in the coming years.

**Sophia Yang** [00:36:00] Thank you.
