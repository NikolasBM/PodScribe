---
podcast: "ai-daily-brief"
podcast_title: "The AI Daily Brief"
title: "The Best Way to Test New AI Models"
date: 2026-10-07
url: "https://aidailybrief.ai/e/2026-10-07"
guid: "https://aidailybrief.ai/e/2026-10-07"
host: "Nathaniel Whittemore"
format: "tutorial"
level: 3
length: "00:49:00"
categories: ["models", "model-strategy"]
featured: ["Claude", "GPT-6", "Claude Opus"]
mentioned: ["Gemini", "OpenRouter", "Kimi", "agent harness"]
transcript_source: "publisher"
---

# The Best Way to Test New AI Models

[00:00:00] We are currently in the fall glut of new models. over the past several weeks, we've gotten a slew of new closed models at the frontier

Opus 55, Astra 6, Sol 6-1

with more on the way. And from those same labs, we've also gotten more cost-effective and faster models like Sonnet 55. and then as if all that wasn't enough, We've also gotten a number of new open-weight models, which are increasingly relevant for lots and lots of different types of businesses



And of course, every time one of these models gets released, it's released with benchmarks. But benchmarks don't really tell us much about how it's going to be relevant for us personally. For that, you need to build your own personal AI benchmark, a system to tell if and how a model matters for your own personal AI stack And that is the goal of today's operator-focused episode

The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI. All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, Robots and Pencils, Harbor, and Blitzy. [00:01:00] To get an ad-free version of the show, go to All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, Robots and Pencils, Harbor, and Blitzy. To get an ad-free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts.

And to learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai.



one more quick note before we get into this This is a recording of the webinar that was hosted by me and Nufar Gaspar last week



Given that already we've gotten another couple new models this week I think the system that is discussed here continues to be extremely pertinent

Hopefully you find this useful, and tomorrow we will be back with a normal episode. But for now, let's talk about building a personal AI benchmark

We prepared some very fun materials to you, so we will share everything at the end. You'll see throughout what are the materials, but basically everything that you see me doing and talking about, you will get everything in order to try and do a similar process for yourself.

And do leverage the Q&A box because we have a large number, so we're unable to open microphones, but Dan is [00:02:00] here and Nataniel is here, and everybody will try to cater to your questions as best we can. Without further ado, Nataniel, some motivation on why we are here. Yeah, thanks everyone for being here.

I think for those of you who are regular listeners of AIDB, you'll know that this is a soapboxy issue for me when it comes to benchmarks. Every time we get a new model, which by the way is now I think, 11 days on average for a frontier model one of my standard cautions is basically first to be skeptical of the published benchmarks.

Not so much because we think that any of these companies are lying, that's not the nature of what they do, but more because most of these benchmarks are now in the training data sets, and they're part of the cannon that goes into them. it's just there's limited value of benchmarks, and the longer they've been around, the less value there is.

Now, lots of people are continuously creating new benchmarks to try to improve that andit's actually a pretty fertile environment right now, much more so than six months ago. But still, there are just real limits to that. On top of that, even if we [00:03:00] assumed that all of the benchmarks were perfect and accurate, we are now at a stage where so much is about not strictly better or strictly worse determinations of model performance, but how a model feels and how it fits into the overall model stack that you're putting together.

And there are going to be times, I guarantee, where the thing that is technically state-of-the-art on some benchmark is worse at the version of the thing that you're doing that's lower on the charts, right? This is particularly the case for things like writing, where so much of it is, incredibly subjective.

So all of that is to say that, there's kinda no shortcut solution to figuring out how a new model is or isn't going to fit into your process other than using it. And so one of the things that I've talked about in the past on the show is trying to put together your own benchmark that has your most common use cases.

And Nufar has very kindly gone out and put together a, a more significant, full, thoughtful version of that so that I don't have to just [00:04:00] keep repeating this without being able to actually give you a resource to help. So that's I think couldn't be more pertinent. We've...

I think we're on model three this week. We got Claude 5.5, Sol 6.1. We didn't technically get Gemini for Argon, we just had it announced. But it's a time right now where I don't see this slowing down despite us pacing the frontier now. And we have some predictions about Gemini, but we will not share them until we will see what happens in reality, and then we can say that we were right or very quietly be mistaken.

Very well. All right. The plan for today or what the process that I created to make it more standardized and to help you do it for yourself is comprised of basically five steps. The first, and arguably the most important step, is to decide which of your tasks need to go in, into a repeatable benchmark.

Those should be tasks that represent diverse set of things that you do for w- work and if you use AI also for personal reasons, then there as well. They need to be ones that based on the results that you will get there, you will be happy to make decisions accordingly. [00:05:00] That's one of the most important steps that will help you perform.

Then you need to decide which are the candidates. So obviously, if there is a single model release that you want to check, you can just check that versus your existing model roster. In many cases, like we're seeing over the last few weeks models come in groups. So often you might have more than one new candidate to evaluate.

And sometimes it's just a good practice if you have been working the same way for a while and you just want to freshen stuff up. So deciding what are you evaluating. And by the way, we keep saying models, but sometimes it's just to evaluate a new harness or a new agentic tool with a combination of a model.

So sometimes it's not just gonna be a model, it can also be a specific tool or feature or something that you are considering introducing to your best methods of working. And then you will run the actual benchmark and comparison. In order to make it accessible to everyone I will introduce three ways to do that.

One is highly manual, but still effective. One with a small script that I created and I'm [00:06:00] sharing with you so you will be able to replicate the exact same steps that I did in order to run mine. And there are also dedicated tools and platforms that help companies do that, and we will mention them in the passing.

Those are not the focus of today. In order to make a benchmark work effectively, you will be advised to hide the names of which models or which tools created each result because we are very biased towards our beloved tools. Spoiler alert, I was quite surprised with the-- my results as you will see.

And lastly, there is a decision because the fact that in a, a specific benchmark run one tool or one model outperformed your current setup does not necessarily mean that automatically you need to make changes. First of all, because changes are hard, and second, there are sometimes other considerations as to whether or not to make the change.

It can be company constraints, it can be cost, it can be latency, and perhaps even the delta is not large enough for you to justify the switch. So we will cover all of these five steps in this [00:07:00] webinar. So a few thoughts about how to even address all of these new model releases because every release arrives with the same method.

An announcement and then a table of test of scores. You've seen the Gemini table and then a week of very hot takes, and everybody is saying, "I had early access, and this is what I think," or some preliminary, um, influencer sharing their experimentation. Often, early experimentations are very skewed towards creating a toy game or a toy application, creating a three-D something and repeatable use cases that look very nice on social.

And also some might claim that some of the models are created such that they are optimized specifically for the social media and influencers type of tests such that they will look goodin reality. And then when we look about seven days in, give or take, or sometimes longer, depending on the traction and the stickiness, we're starting to get like a more real interpretation.

[00:08:00] Because then the reports are coming from real work. For example, it quietly dropped a condition in my contract review that's much more critical for a lawyer versus it was able to generate an amazing three-D game that replicates my '90s beloved whatever. So that's why we're taking with a pinch of salt the early releases.

We listen keenly because maybe there is a big game changer, but eventually we need to see what happens after a while, and even more importantly, we need to test it on our own. Specifically for today, we will be looking at some of these new arrivals at the Claude Opus 5.5 and Groq and GPT 6.1 Sol.

Gemini will come when it come, and then maybe if you want to wait, you can run the benchmark then or re-run it with Gemini. I'm definitely am curious, and once we get access to Gemini, I will add it and compare it against the, the other models and the other results that I will show you. So that's the focus for today and the stuff that I will specifically compare.

While you are listening to me speaking, you [00:09:00] might be saying I have a few concerns or objections to the entire concept of personal benchmarking." typically they come of one of two shapes. The one is everything is so good now. The frontier is so forward, like, why do... should we even care? Is it just a matter of tool FOMO or model FOMO that it feels like unless we're chasing the frontier, we're not relevant?

So that can be one type of objection. My response to this type of objection is, first of all, you are correct. The frontier is very good, and odds are that there is so much more value that you can drive, even if you will not necessarily change the tools or the models that you're using.

However in some cases, all of a sudden a new model release, like NLW is repeatedly saying on the podcast, may unlock a use case that was only on the wish list up until now. And I think that even for that justification alone to have new use cases being unlocked and to push the envelope of how you use AI this is one justification as to why to at [00:10:00] least occasionally consider upgrading to a new model or a new tool just to make sure that you are leveraging the technology to the best of its ability.

And it doesn't have to be on a weekly basis because that in itself can really create a lot of confusion. And so you can run it periodically according to your bandwidth. The second objection or consideration is that sometimes people will say, " This is all fun, and you guys that have the full freedom to use whatever tool and whatever model can enjoy swapping and following up the frontier.

But in my case, my company is limiting me to using a specific tool or a specific model." And that's a common reality for many employees. So first of all my condolences, and I hear you. It's not easy at all. However, even with limited set of models and tools, there is always a choice. Even if the choice is just selecting between fast thinking and quick or some of the other configuration for the specific tools.

So even if you limit the benchmark only to the very narrow set of [00:11:00] choices that you do have within your tools those matter. And sometimes for either personal use cases or just to maybe encourage the people who decide within the company, it's worth running even a benchmark on a mock set of data so you can prove to the people in the company that perhaps you should consider purchasing another license.

So that's the anti-pattern. With all of that out of the way, I want to start with, As I said at the beginning, the most consequential decision out of the process, and these are the concrete use cases that you will be using for your benchmark. In my opinion, ideally, you need to cover what you actually do either at work and personal usage, and of course, the balance should be based on your actual balance of what you use AI for.

If you primarily use AI for work, focus on that. If you primarily use AI to do stuff at home, then shed more light there. And then I want you to try and create a diverse and balanced set of use cases. And of course, you cannot run each and every task that you do for work, so you want to [00:12:00] cherry-pick a good set that if you're seeing a significant uplift or that a specific model behaves much better with this use case, that you will for real consider swapping, meaning it needs to be a set that you trust the output to make actual decisions for your work.

It needs to be diverse in the kind of work that you do and the frequency. Ideally stuff that you do regularly because those are where you get the highest uplift. You should also ask yourself what's at stakes, and if you know of a costly mistakes or ways for you to evaluate quickly that this is completely off, that's also a good use case because if you can evaluate what bad looks like, sometimes it's a better use case than the one where you have lots of nuances on what good looks like.

Also, for the specific tasks that you're leveraging, is it a task that starts from a clean slate, or is it a task that can only start from an existing document, like polishing an email polishing a, deck stuff that requires some uh, substance before it starts? And [00:13:00] lastly, as I said, and that's part of the motivation of why to run these benchmarks even if you're quite happy with your existing setup, include at least one task that it's on the wish list.

What do I mean by that? Something that you've tried with AI, you were unhappy with the results, and thereby it's not a type of task that you regularly do with AI. I w-would strongly recommend that you have one of or two of those such that when something new comes at the frontier, this is among the top things that might get excited and to m-move to the frontier model.

So that's the core decisions that we need to make here. And of course you can think about the number that fits your life. My recommendation would be like four to, six type of such use cases. But you can of course create more or less. I will show you my process for getting there, but just to make it concrete, this is my list of six use cases.

One that posts stuff on LinkedIn one that holds a critical or sometimes a unpleasant conversation with stakeholders around pushing back on a pricing negotiation as well as doing some research [00:14:00] around the tool features with some specifics. A website that will include content for a course that I run.

Creating an exercise for courses that I manage, and this is in the wish list, a proper weekly plan that actually is like a, a good chief of staff that I'm not getting frustrated and neglecting. U-up until now, I'm unable to find a model that everything that they do with regards to an intricate weekly planning is indeed like correct on a one shot instead of me having to prompt it back and forth.

So that's my season and I'll show you how I got there very quickly. Once you have the use cases list and the use cases specifics, then what you would want to do is to basically do a taste testing. Ideally, of course, a blind taste testing. We want to select which models or tools or model and tool combinations are the candidate ones to evaluate.

Quick note, for this lab, I ran seven model options, and I can tell you that seven is [00:15:00] way too much. It was extremely tedious to review and rate seven different model options for six different tasks. So I'm not... Or was five, but not recommended. I would recommend to run the existing model versus a new one or up to four different candidates.

One of them should also be the baseline of how you currently do the work, so you will know whether you want to convert to a new model. Then we want to run every request in a fresh chat such that the context window will not send us on a tailspin. And then, and that's a very important step, we want to hide the names.

A, a few thoughts on how to do that in a minute. And then once we do the, blind taste test, we can do a combination of verbal reflection of w- of whether or not we like the output. We can do a numeric score, or we can do both. The programmatic package that you're getting is encouraging you to do both.

Score it on a scale of one to five, and give it a one-line observation of your likes and dislikes. Once you're done with the-- doing the blind [00:16:00] taste test, you can reveal who were the models. That's a very fun exercise to see whether your predictions of which model created what output are.

I can guarantee you that some of them will surprise you because we do have a lot of beliefs on some of these models that not all meet reality. And lastly, we need to decide. And by decide, even though something that was significantly superior might not be superior enough or for other considerations, we might not choose to change our habits for that.

So that's how we run the taste test. Specifically on how to blindfold the different results from the different models four ways that you can do that. One, you can call a friend to do the anon-anonymization for you. Either they run all the results for you and just give you an anonymized set of results to evaluate.

That's relevant if you're doing the benchmark manually, which you definitely can. It's just a little bit more work. You can leverage a spreadsheet to create a random number and then anon-anonymize like that. You can leverage an [00:17:00] AI tool to sh- shuffle and relabel them such that you don't know, or you can use the script that I created that does that for you.

When you will be using the script one thing that you will need to do is to run the the actual task execution using API keys. So one option is to do that with open router that lets you run multiple models with a, a single API key, or you can have API keys for each and every one of the vendors.

Or if you work with just a specific vendor that you just want to evaluate between the different model tiers, you can have a single API key. But the programmatic or the script-based approach requires an API key. I can guarantee you that even if you're not technical, it's very doable nowadays.

So that's how you anonymize. One more thing to pay attention, I strongly recommend that some of the tasks will be more visual, whether it's website design, application design, or image generation, just because in most cases, it's easier for us to score quickly something that is visual. Of course, if [00:18:00] you're not doing anything visual with AI, don't choose a task that is visual just for the sake of that.

But if you are occasionally using AI for something that is more visual, make sure that it includes that. In order to evaluate visual stuff uh, you will probably need to store it in a dedicated folder so you can open each visual assets whether it's a website and so on, in a dedicated place.

You will see how I did it with the website design very shortly. And then we need to choose. So the first method and the most important method is you scoring the results because it's a personal benchmark and nobody knows better than you your preferences. And LW pointed before, there is sometimes an X factor of why you like or dislike.

Even if you don't know to explain, you just prefer one result over the other. Sometimes we don't have the vocabulary to say why we prefer one result over the other, but ideally, you should be the primary judge of what you like and dislike. From my experience, it's often very difficult to judge something as a standalone, meaning you will get results from a single tool or model, and just to [00:19:00] give it an absolute score between one and five it's very hard.

What is often easier is to see side by side several alternatives for a particular task and say, "I like this the most, I like this the least," and score it accordingly. That's often how you should do that. So that's one approach, and probably the one that will matter the most because of your taste and this X factor where it's often hard to explain why you liked something better than other you just did.

Another approach, and you can always run both of them and then compare, is to leverage an AI tool as a judge. And then it's not just you that's scoring, but also an AI tool that judges the result according to a predefined rubric that you configured of what's a good LinkedIn post, what's a good vendor negotiation, what's a good website design.



You can always compare and see whether the cumulative review is in agreement and whether it creates a clear pattern of stuff that you need to change. I do want to warn you that using AI as a judge has its own shortcomings, and there is an entire theory [00:20:00] around using AI for evaluation.

But I will say that you should evaluate the judge itself. So because if the judge is completely not correlated to your taste, it's a bad judge and just throw it away. A few more points on judgment. Because taste is highly subjective that's why we need to do the side by side and like a verbal description, and that's why we're trying to leverage AI to do the subjective testing according to our rubrics.

But I said, it's not perfect. Ideally, the model that you will use for judging is different from the models that executed the results. There is kind of an AI nepotism. Like, Odds are that a specific model will favor models from its own family versus from other families. Not always but often this is seen.

So if you have another model family that is outside of what you're evaluating make that the judge. In my use case, because I haven't evaluated anything with Gemini, the judge was a Gemini model. As I said, hiding the names of the models is of very important like a criticality [00:21:00] because we are very biased.

and nobody can prove me otherwise. I'm sure that we can prove that this is the case. we want to maintain anything as frozen as possible, meaning it's gonna be the exact same request to each and every one of the models and then compare it in a fair, and equivalent way. And because answers may vary, if you're running this personal benchmark on something that is very critical and there is perhaps a monetary implication or other implications to you making changes to how you work, ideally, you should run the same request several times per model and then compare these several execution, because we know that models have very diverse set of responses.

Even if we're using the exact same model with the exact same configuration and the exact same prompt, you will get different results. I just saw it today when I I gave a model a website to generate. I really loved the result, but something got stuck in the middle, and then in the second execution I liked it much less than the first execution.

So that's something real, and if you are concerned about the validity of the benchmark, running it several times will seal the deal. 

the validity of the benchmark, running it several times will seal the deal. All right. And as we said, the final thing is the decision. [00:25:00] Ideally, you should make a decision of three types. Switch, meaning I am convinced that this model or this tool is significantly better, and given everything else that I have that I need to consider I want to switch to this new configuration.

Split meaning that I might be going between different options with more nuance. Or stay, like I'm not convinced that what I just saw about the performance of the new thing that I evaluated justifies me making changes to the way I work. So that's the, like the core decisions.

But in order to make decisions, it's not just straightforward as, like this is the final best result and there-thereby I'm switching. There are other considerations that sometimes will get you to stay with the status quo. For example, maybe your company does not permit you to move, so it's not really relevant, or maybe some of the terms and conditions you are concerned about.

Maybe your own plan is, does not offer at all or a generous enough usage for the new tool or model that you're contemplating. In some-- in [00:26:00] other cases the winner is not straightforward that it just doesn't justify making changes. And if you are in a position to have some tie-breaking some things that can help you decide are costs, the speed of execution maybe there are specific features that you just enjoy and you don't want to change them as well as habits.

Habit formation is an expensive thing, so if there is no like significant boost just staying with the way you used to work also has merits. But if all of these tests justify the change then make the change. So that's the entire process. What you will see from here on after is an automated process that I created and that, as mentioned at the beginning, you're getting in order to implement for yourself that works as follows.

It starts with your saved tasks. I'll show you how to save them. And then I'm using the OpenRouter API key in order to create the results for different types of models. Then, we get the answers for each and every option. The code itself anonymizes the results such that I don't see what the origin models for the [00:27:00] execution.

You score them blindfully withou-without knowing which model created what. You provide score as well as a verbal description, and then there is a fun big reveal that shows you what are your preferences versus the judge and versus the model names, and this is the fun part where often you will be surprised.

I use the OpenRouter, but there are other model hubs, like I said. Use anything that y- you find to be relevant, but you will need an API key for the relevant models. So that's the methodology of what we-- you're about to see. And as I said, I'm evaluating multiple models. The quote unquote, baseline, even though I'm not using it for a while, is Opus Five.

And then trying also Opus 5.5, Grok 4.7, GPT 6.1 Sol, and I also wanted to test them against the very expensive frontier model of Fable 5.5-- 1 and GPT 6 Astra. And to make sure that we give room for the open source I'm also trying them against Kimi K three, and that's why I got to seven different options, and it was very difficult to evaluate.

And [00:28:00] lastly, as I said, a different model runs the judging. In this case, I used Gemini Pro. So that's what you're about to see, and now let me walk you through the process. The very first step that you will be encouraged to do is to run a prompt. You have the prompt as part of the materials that helps you discover which use cases you should include as part of your benchmark.

So it's A prompt that will interview you and leverage everything that the AI tool that knows you best can advise. So definitely run that in a tool that has a ton of memory and a ton of context as much as possible, so it will help you figure it out. It will run a process of about eight questions that will help you figure out the best use cases.

As you can see, Claude knows quite a lot it knows my role and it knows what a typical week has. So it has some guesses and some initial suggestions for use cases as well as stuff that goes back and forth. And then it started asking me questions, so I answered all the questions that it had.

After eight questions, a little bit annoying, but not too much, it created for me [00:29:00] a set of six recommended use cases. For each use case, it will create also a prompt that will be used to do the actual benchmark. So it doesn't just uncover the use cases, it also uncovers the actual prompt that will be sent for running the benchmark.

So that's the LinkedIn post from raw notes, and that's the prompt. Pricing pushback plus sensitive email. Current AI tool feature by Plaintier, that this requires a web search and some research. Course participant hub website. One-shot exercise for a new audience, and week plan a course engagement wishlist.

So these are the top six, and at the end it will also show your coverage. And I decided, for example, to not do anything personal 'cause I don't use AI as much personal as I use for work, so it was less relevant for me. And it did call out some things that are missing potentially to pay attention to that.

So that's the final results. At the end, it will-- if it's an agentic tool, it will save it as a dedicated folder where each of these files is a [00:30:00] dedicated file on its own. For example, this is how the LinkedIn post generator file looks like. It's the name of the task quick motivation. The request, this is the actual prompt that will be sent to the model and that's important.

If you want to judge the benchmark also using an AI tool and not just based on your preferences, there is a scoring guide for the judge. So this is also appended as part of the task itself. One thing that I want you to do is to take a look at the prompt or the task that was created using the process.

If it seems too generic or not something that will help you make up your mind on a specific usage, or you think that it needs to go deeper or be completely different, then this is a very important step to refine both the request and the scoring guide such that you will be, able to make decisions.

If you don't trust that these tasks are a good representation of the way you work, that's not a good enough benchmark. So I have six of those from number one to number six that was [00:31:00] created by Claude based on the interview and all the instructions that you can also get. So once we have all of them, we can start running the automated process.

The automated process is a script that I created, and as I said I'm sharing it with you. To make it fun and a pleasant experience, the script also create this simple user interface that is locally hosted on your machine. It doesn't need to go anywhere, so it's not-- there is no sharing of data that you haven't intended.

And in general, by the way, if your company is sensitive, don't use something like OpenRouter with company data. Use mock data or mock use cases so there is no confidential information leaking anywhere. The way this user interface is created, you will get here the list of your tasks to be evaluated.

For each one of them, it will generate the-- all the candidate models. In our case, it anonymized them from A to G. And at the top of each use case, it will tell you from your rubric what's a good answer also to help you to score it [00:32:00] properly. And then you have side by side all of the results that we got from OpenRouter.

So this was done after the script run in the background and used the API key that was provided, and it generated candidate responses for each and every one of my five tasks that you've seen before. And it puts them side by side. So you can see, for example, this is the LinkedIn post generator.

So model D offers the this hook option, three hands went up, yada, yada, yada, the full post, ending option. So that's how the first one looks. And then what it's asking me to do is to provide a score from one to five and like one verbal evaluation. So in this case I scored it a two out of five and said that while it's readable and clear, it's also a bit too light, and it includes its A and not B pattern that I too personally really hate about AI writing.

So I got seven of those. And as I told you, it was very hard to score before I read at least a bunch of those 'cause they are, at least in the LinkedIn it was a little bit overlapping with some of the writing. But as [00:33:00] you can see I did score it differently. So some of them got a three, a four.

Actually, none of them got a five from me 'cause none of them wrote a good enough LinkedIn article. So none of them was ready to post as is. So that was task number one, and when I was done, it indicated that this is all scored. I also have pricing pushback and one short exercise and a week plan.

These are all text-heavy use cases, so they are not that exciting. I am thinking that the most exciting thing is to sh- see how the different candidate models created a course participant hub website. So here, if you have like HTML or other visual assets this small fun application that you can build for yourself and you're getting it also it just showcases the different websites.

I opened them in a full window for you to see. And a fun exercise for you as I'm scrolling through some of these websites that were created by the different models is to start guessing which is which. You can also on the chat if you want, start guessing which one seems like a [00:34:00] Kimi, which one seems like a Claude, which one seems like a, a GPT which one seems like a Groq.

I'll be very curious how many of you are able to guess it properly. So that's one. Not the greatest, but by the way, they all created quite a complete website. So that was nice to see that they created copy and as well as the navigation and so on. So that's one candidate. That's another candidate for this imaginary company creating a, training portal.

N- I don't love it, but it's not the worst. Another one that is slightly more opinionated, as you can see. I think this is the one that I like the most. Also because I reviewed some of the copy and not just the co- copy functionality and navigation. 

That's another one that was created.

That's another one, and that's, almost num- the last one, and finally, this one. So we have seven candidates. If there is someone on the line that is able to guess correctly all seven models hats off to you. I was very much [00:35:00] off from that. But as you can see, with anything that is visual, it's often much easier to have proper preferences and like something that say, "Okay I'm drawn to that," and so on.

So once I was done, and you will be done scoring each and every one of the tasks the next thing that you will be able to do is reveal either my score only or reveal with the AI judge. So when you click reveal with the AI judge, all of the results will be sent to the judge for review, and the judge will also apply.

And then it d- does the reveal gradually. So as you can see per task, these are my top picks and a few words on why. And now drum rolls, let's reveal the names. So for the LinkedIn post generator, my favorites were Kimi Fable, and Opus. I was surprised. I was sure that GPT will be here.

For the pricing pushback, you can see that GPT models are the best in negotiating, at least from my perspective. For the exercise, [00:36:00] then we got GPT and Groq. And week planning, Groq won, interestingly. And for the course participant hub Opus 5.5. Maybe some of you will not be surprised by some of that.

The next thing that I get is a recommendation on w- for each of these models, what to do about the specific tasks, whether to add it to the model roster or whether to consider switching to using this model. And of course, as we said, consider, right? We need to apply additional judgment. And now take a look at the final results because I think that's also very interesting.

We have the different models with average and the w- how many tasks I selected. The judge average, so for example, Fable got the first because the judge put it first. But pay attention here. The total cost of Fable is so much higher than everything else. And that might be a consideration why not to go with Fable, even though theoretically it got better.

pay attention to my average. So in my average, Fableand GPT Sol are [00:37:00] equivalent, but take a look at the cost differentiation. This is a degree of order smaller average time is quite similar. Pay attention, this was also interesting. The average time for Groq was extremely long even though the cost is very manageable.

Kimi is on the running interestingly, and these models are getting lower scores overall. Remember that we want a more differentiated use, so we might be not just looking for the one winner, but rather per task, we want to make a more differentiated choice, and thereby we might have different perspectives.

and then you have some more data, like how long for each task from each of the models, and you can see that Kimi wins on both cost and duration. And you can also see thatwhere is five point one? Five point one is probably the most expensive out of the bunch across the board.

So perhaps cost will not surprise you, but some data on cost and velocity. Some comparison side by side between me and the judge. As you can see, [00:38:00] we are quite in disagreement thereby I said that take any AI as a judge with a pinch of salt. The only thing that we agreed upon is the pricing pushback.

The rest, as you can see, we have different choices. One thing to point out here, the judge could only see the code and the text, so the choice with regards to the hub website was done based on the code and not based on something visual, and thereby if you want an AI to judge something visual using just the, the API often is not the best thing 'cause it, it's not leveraging that as a picture.

It directly will go into the code. So will I make choices based on the judge from here on after? Probably not. I can also go and fix some of the judge instructions, but I would much rather rely on myself And then you have some raw scores that you have everything there. that's the application, and that's the process.

Just to showcase the final results. Interesting roster, not what I expected at all for some of these things. Am I [00:39:00] con-contemplating changing some of the ways I'm working? Honestly, yes. I'm very biased towards Claude and Cursor with Groq in my day-to-day. And even though I occasionally am reaching out to GPT, it's not in my top two, and I'm definitely contemplating reaching out to GPT more as part of my top two.



and if I had to choose one tool, I might have, based on these results, been willing to consider moving primarily to GPT, at least in this day and age. So that's the full process and that, as mentioned, you will be able to run completely for yourself. A few more notes before I take questions and take some observations from Nathaniel.

As I said I created a process that can either,be run manually or leverage the script in order to run the same process that I did for myself. I will be amissremiss to say that there aren't platforms that do something similar like that out of the box. Those are typically platforms that are designed to teams that are already doing that at scale or at the company level.

Some examples include LangSmith and Brain [00:40:00] Trust and Langfuse. And they are not the only one. We also have other options. So if you are in a position that you need to do these types of evaluation in a more standardized and regular way, these are all good options to look into, such that your experimentation and monitoring and evaluation will be done a more systematic way, rather than you having to create these out-of-the-box small scripts.

But if you are primarily doing that for personal use, then the methods that I've just shown you are more than enough. As I said, you are getting both the handouts and the session handouts as well as a few other stuff. I'll show you in a minute how it looks. It's a nice place that you're getting that has all the materials as well as the lab itself very step-by-step, and you can also download the actual script and the benchmark runner and many other stuff, and we also have resources.

So very extensive view of everything that you've just seen. We will sh-share it in a minute. So to put everything [00:41:00] back in one place, these are the five steps. Most important is the task selection. Models choose interesting candidates. Run it in one of the methods. Do the blind test. It's a very fun experience.

Do it once even just for the enjoyment of surprising yourself and contemplate changing stuff. If you did a good job and you created a good benchmark, from here on, you can run the same benchmark every time there is a significant shift that you're contemplating tapping into. So it's a, a one-time effort that if you do properly I can guarantee you that it will serve you well.

So if you find it to be useful highly recommended. If you also want to go deeper into anything that you've seen or to become a master in building, we do have our two existing courses for executive agent leadership and executive catch up courses that are starting in, over the next two weeks, so we'll be happy to have you join us.

Thank you, Nufar. How is this evolving for you? Like, how would this set of tests be [00:42:00] different three or six months ago than they were now? And I'm thinking specifically about OpenAI introducing this new ultra-fast mode and Sam Altman basically saying that he didn't really appreciate how much speed mattered to him until he had access to that.

Now, obviously, that's it's only available on a $500 a month plan and things like that, but, how frequently do you imagine updating these sort of criteria? And what are the types of things that you think, might become more important over time? So I guess, first of all it depends on how crazy and how ADD you are, 'cause if you are crazy and ADD, probably every month.

But specifically to your point, when I saw the demo of the ultra-fast, and today I had to sit down and wait for sometimes 20 minutes to get the website, this poor website generated. I honestly was very impatient, and I realize that I'm paying way more attention to speed versus how I, I did before I've seen the ultra-fast demo.

Some of the considerations are being updated on the fly. Some of the use cases, and that's exactly why I wanted to have the wish list. Some of the use cases that I would now [00:43:00] pursue or consider frontier use cases I would never have dreamt to do at that quality and in one shot previously. So the bar is getting higher.

I don't know that the subject matter changes, but I think that the considerations of what makes you change your mind or what good looks like, those change quite frequently based on how far we know that the technology takes us. Awesome. I'll get out of the way and let some other people ask questions too.

Sure. I've got some stacked here for you, Nofar. I've been cataloging while you've been talking. So Thank you for that. Yeah, no problem. So one of the questions that came up was effort settings whenever you're doing this, in terms of whenever you're using OpenRouter, are you setting everybody to a similar effort setting whenever you're testing this?

So the correct response is ideally yes even though effort setting are not necessarily equivalent in some of the models. So if you want to be extra diligent, try to compare apples to apples or just use the default of OpenRouter. That's also a lazy approach that might work well. But I agree that the effort setting might create a difference, so if you want [00:44:00] to be extra diligent, you can always run several models with different effort setting and see if it changes the picture.

'Cause effort setting preference is also part of what I want you to evolve as part of your personal model roster or model configuration roster. Great. And then in terms of whenever I think of tasks, I usually try to put them into three buckets, to something like content, operations and strategy.

Do you find that there's any differences whenever you're doing those three different types of tasks, or are they generally going through all the same process? So some tasks will require more elaborate setup, like to work as part of your own harness with your own context and so on and connectors.

So several options. Either if you do put as part of your benchmark a task that is highly involved with the overall setup, then that needs to run directly from the harness, from the the actual setup and not using a third-party API key that will only get partial view. if you have to, that's one way to do that, to just run it through the actual tool and make sure that you anonymized well enough without cheating yourself.

[00:45:00] Alternatively, if you can create a proxy for this task that doesn't require all of the bells and whistles of running that in the actual configuration, then you can try and run that in a-- using this method. But for operations, I would guess it's gonna be most influenced by the overall setup and that's the one to be a little bit more careful to judge without the setup 'cause it's highly dependent on the entire system that you have.

Awesome. 

Some-- there were some questions about open source models and if we notice inherently any time whenever we're doing our testing. Obviously, you had Kimi up there. Are you noticing anything? So there were some questions about Mistral. Do you notice any big differences or do you find that you're generally happy to test through the open source and the frontier models and just kinda compare?

So it goes back to the final criteria because if you are very biased towards open source or the other way around for security or company policy reasons you are biased against, then either don't include or primarily include open source. If cost is a critical consideration, perhaps you will be, leaning much more heavier towards model that are cheap [00:46:00] while giving you good enough results.

And also the task itself has a huge implication because some of the tasks are table stakes, right? For example, a email drafting or basic research, those are table stakes and for them, you'll probably see that any decent model, let's call it Kimi and above, or Mistral and GLM and above you not be able to see any noticeable difference, and then open source will be as good as it gets.

For the more, aggressive things or more sophisticated stuff, sometimes you will still see the gap between commercial and open source. But it goes back also to the objection that I raised at the beginning. If you are primarily working with good enough for most of your use cases, then as of now, open source is good enough for most knowledge work, task especially if the harness in which it's working is a good one.

Great. And another question that came up was regarding trying to figure out how to give instructions and prompts, and I'm reminded of our last webinar that we did about loops in terms of what does good like reject if, 'cause there were some comments just in terms of whenever you were building and people noticing that you had some very specific instructions.

Do you have any [00:47:00] pointers in terms of how to do that? Or perhaps we have resources that can help people do that. So the prompt itself that will help you figure out the tasks and the prompt will go a long way to do that and do that in a smart model, in a tool that knows you in general, it needs to be measurable. We're talking primarily about agentic tools. Agentic tools need goals. Saying create a good blog post is not measurable. Saying, create a blog post that will be engaging for executives as well as ICs is better, and saying, create a blog post that does not include the following and is limited by this number of words and has the following parts, is even better because it's highly measurable and highly attainable.

Great. And in terms of-- there was one question about, I think, cost, and it's great that OpenWriter makes those changes. Do you have anything else to think about whenever you're considering switching as it comes to costs? Even having-- ' cause it's nice with OpenWriter, you're getting that cost per task.

But do you have any other thoughts around the cost of switching? Yeah. So remember that if you [00:48:00] have one of the generous subscriptions, like the Pro tier or the Teams t-tier, some of them are basically hiding or subsidizing a much higher actual token cost. So just evaluating cost per se is not necessarily the full picture.

Because if for example with your two hundred dollar a month Claude or OpenAI, you're getting more than your fair share of what you need from Astral or Fable then perhaps the cost does not matter to you as much as to someone who actually pays per consumption. So it's a little bit conditional to your subscription.

And I think a good prediction to make is that it might not stay as generous in the future, and then we all will care about the specific cost and not just the ballpark. But if you are a person that also with the, the generous subscription hit the rate limit very frequently, th-then cost matters to you, and then you should optimize more for cost.

So conditional. Amazing. NLW, that was all the questions that I was able to kind of catalog. I don't know if you have any others. No. this-- I think this was super helpful. I think this is one of those areas where I think even more than our normal [00:49:00] how-to type sessions, this one requires definitionally a lot of personal consideration, right?

Like this is-- if there are pieces of this that you don't find useful the whole point is to make it useful, so reject, try something else and then share it back. So other people get a sense of where things are. I'm super feel-based because I'm using absolutely everything, and I'll run the same thing through multiple different models all the time, so I'm-- my approach to this is gonna be different than some other folks. But Nufar, thanks as always for getting this out there and hope everyone had a good time. Yep. And join us for the next one once we decide what it is. Cheers. Bye. 

​
