# How People Are Actually Using Jev — Transcript (2026-09-25)

https://aidailybrief.ai/e/2026-09-25 · Listen: https://pod.link/1680633614

<!-- metadata -->
Format: commentary · Level: 2 · Length: ~00:25:00
Host: Nathaniel Whittemore
Categories: marketing, model-strategy, models, agents
Featured: Jev
Also mentioned: GPT-6, agent harness, Claude Opus, Claude Fable, OpenAI Codex, Claude Code
<!-- /metadata -->

---

[00:00:00] Jev is one of the buzziest models we've had in a long time, and that's because it's not just another LLM like a GPT-6 or an Opus or Fable model. It is something fundamentally different 

But because it's different, it's not necessarily clear at the beginning exactly what it's going to be best used for

With the benefit of a week and a half under our belts now though, people are discovering and sharing a slew of different use cases that take advantage of what makes Jev unique And today we're going to get into the best of them and where they might be relevant for you

The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI. All right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, KPMG, Blitzy, Harbor, and Hyperagent. To get an ad-free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts.

And to learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai.

One more [00:01:00] 

quick announcement

We have our next free webinar coming up shortly

It's all about how you can build your own personal AI benchmark so that when a new model comes out, you can test it and see how good it is for you and where it will fit into your AI stack. it's led once again by Nufar It will be free, and you can get all the info you need at aidailybrief.ai 



Over the last couple of weeks, one of the buzziest new things to come up in the AI world

has been a new model called Jev

now what makes Jev interesting is that it is not just another LLM

that you would use for the same thing as GPT-6 or Opus 5.5

but actually works in a slightly differently and as we will see, complementary way

In the 10 days or so since launch

Not only has there been a ton of buzz, I'm talking hundreds of different posts on X which each themselves have hundreds or even thousands of likes and shares

But that attention is also translated into significant

financial opportunity

With the information reporting that the company is in talks to raise as much as one billion dollars at a ten billion dollar or higher [00:02:00] valuation

That is a decent jump from its $40 million seed that was completed at a $200 million valuation

but now that we've had a chance for people to actually get their hands on Jev itself, I wanted to go back through and talk about how people are actually using this thing



Outside of the buzzy visual and game demos that have been all over social media

media 

Basically, is JEV something that the average person who's not a game designer or not a developer should be paying attention to and even thinking about as part of their larger AI stack?

Now to recap what JEV is, previously I called it a judgment model What Jev can't do is write in the traditional way that you think about chatbots writing the team, instead the team at TypeSafe who built Jev calls it a system one model After a concept from Daniel Kahneman's Thinking Fast and Slow. System one thinking is fast, instinctive pattern matching, i.e. snap judgments, and that's what Jev is built for

about, a good way to think about a test for whether something is a good job for Jev

is where you repeatedly read something, make a small judgment, then [00:03:00] take a predictable next step

so take for example a file landing in your downloads folder An ordinary rule that existing software might have would be to classify it as a PDF

But what Jev can do is go a step further, identifying is it an invoice, which projects is it for, and does someone need to see it?

Once the judgment is made, it can be predictably moved on to the next step in a system

types, there are three core types of questions that you can ask Jev

The first is pick one, or what Jev calls choice. It answers which of these fits

You list up to 255 options, and Jev can find the best fit. this, so an example of this might be which team should handle this ticket? Is it billing, tech support, sales, or other?

The JEV model is going to give you back the pick plus a probability for every other option The second type of question that you can ask Jev is what they call a score, which is basically rating on a scale. You describe each level in words from two to 10 levels, And Jev can answer where something falls.

So for example, on the scale from calm to very angry, how frustrated is this customer?

[00:04:00] you're gonna get back from Jev a position on that scale 

as well as an indication of how sure the model is The last type of question is a yes or no question, what Jev calls a null, which is short for Bernoulli And it simply answers, is this true? So to stay on this customer service example, is this person explicitly asking for a refund?

What you're gonna get back is a probability from zero to one that the statement is true

Hey Stefan and Ax did a really cool, verysimple visualization where he put a pile of emojis at the bottom of a screen, and then into a text box he wrote, 

you can type in classifiers like things you can wear or things you can wear in winter. The emojis that match race to the top or fall off 

if the classification has changed

And so what's happening in the background is that every emoji is getting the same yes or no question. Does this match what you typed?



and importantly, nobody labeled or tagged the emoji as would happen in traditional machine learning. There's no rule, in other words, for winter

Every emoji gets the same question at the same moment, does this match?

be rec- and part of what you might be recognizing if you're watching this demo is that because [00:05:00] what Jev does is limited and specific, it can do it incredibly fast

launched,

when TypeSafe launched the model, they said it could work 20 to 200 times faster and 40 to 400 times cheaper than comparable processes with LLMs



now instead of this pile of emojis, imagine that the pile is your leads, your tickets, your documents, or some other big undifferentiated mass of information

Importantly, you can ask many questions about the same item all at once

Because questions run in parallel, asking the ninth or tenth question doesn't cost more time, it just costs more tokens

say for example you have a single customer email. You might wanna ask three yes or no questions at once. Is the customer angry? Did they get a delayed response? Are they dealing with an incorrect item?

These are three separate questions that are each going to have their own probability

In their testing, Typesafe found that 13 questions handled in a single call was 12.2 times cheaper and 10 times faster than one at a time, and got to the identical answers

Matthew Berman of seven hundred and twenty-four live ads

with each ad being asked 12 [00:06:00] questions one about the hook archetype, one about the format, one about the offer, one about the CTA intent, one about the awareness, et cetera, et cetera

He found that that single request For the 12 questions for that ad took just 173 milliseconds to complete 

and this is really where the power of the model comes in. It's not just that it's good at judgment, it's that it's fast enough and cheap enough

to ask and make judgments about everything A million input tokens cost just 4.2 cents, and output tokens are free

And each call is going to take between 70 and 500 milliseconds, and as we've seen, can combine a bunch of different questions in a single call

Now importantly, Jev makes trade-offs that allow it to be good at the things that it does, but that also means that it doesn't do certain things



it's not gonna write code. It's not gonna draft contracts

and it's not gonna make nuanced decisions that involve a variety of factors that aren'tquantifiable and clear It's gonna be used for small judgments at volume.

Which bucket? How urgent? Is it relevant? Is it safe?

So now let's talk about six different ways that people are actually putting JEP to [00:07:00] work outside of just cool demos

A first category is analyzing what you already have. A second category is searching by meaning. A third category is triaging what comes in. A fourth category is checking work against your rules. A fifth category is speeding up AI agents, and a sixth category is responding instantly So let's move to category one, analyzing what you already have, AKA what's in this pile?

This is basically where you're gonna take a collection you already have, ask Jev the same questions about every item, and then count the answers. This is analysis that previously could not be justified doing by hand, but is now gonna take seconds and cost cents

was, one example was that from Matthew Berman that we just talked about, where he analyzed and broke down 724 live ads from 37 brands to identify every hook, every format, every offer, every CTA

to be able, the idea is to be able to then take this data and compare it to what actually performed

giving you incredibly deep and complex fine-grained information about advertising performance

that would have been extremely difficult before

It took [00:08:00] 40 seconds and nine cents worth of tokens for Berman to get the full breakdown of those 724 live ads

Two days later, Berman went further

And instead of just asking those questions in general

This time he had Jeff scroll 723 ads as 30 different buyer personalities

thing, the personalities were archetypes like gym owner, dental office manager, toddler mom, or AI curious engineer

Jeff's job was to ask for every buyer and every ad, would this person stop scrolling or keep going?

It costs 22 cents to get 21,690 stop or scroll decisions. Now, of course, this is not data

this wasn't 30 actual buyers, it was just buyer archetypes as considered by an AI. could-- In other words, it's better to view this as a hypothesis generator

but it's hard not to think that marketing will shift to using this as a key part of its process to pressure test ad or landing page angles before paying for real tests



lots of other folks are running JEV over whole archives

whether that's email archives

Past X posts

folders of documents

or [00:09:00] databases of research projects



And in each case, what Jev is doing is asking the same few questions, but about every single item in the archive

exam- Ian Nuttall, for example, had Jev ask eight questions each topic, hook, and tone

about nearly 3,300 of their previous X posts to be able to then compare that data with engagement metrics to get a better sense of what actually worked. And by the way, those eight questions each across 3,300 posts cost about 13 cents this?

So So how might we try something like this?

Basically any big pile of data you have, a year of customer emails, CRM notes, a folder of meeting transcripts



anything where you can write a few simple questions and run them against all of those queries

That's a potentially useful place for a JEV job

Category 

two is searching by meaning. in other words, which of these match what I mean?

the the idea is to be able to describe what you're looking for in plain words and let Jev check every candidate



The power is that it can find what you mean even when the words don't match

There were a bunch of examples of this with people basically [00:10:00] using it as a new approach to natural language search on websites

Justine Moore from A16Z gave the example of scanning thousands of Zillow listings and classifying properties by things you can't normally filter for, such as architectural style, renovation status, or proximity to freeways

in one example that piqued my interest

Burhan took a 90-minute video and was able to clip it based on themes that they described in natural language. So for example, across that 90-minute video 

they were able to look for and clip, quote, "Their predictions for when AI will automate AI research."

And they were able to find a bunch of examples of that in under two seconds for under two cents

SE-- another example of this is an SEO audit

where Borgia deployed Jev to read all 586 pages

of their website

to rebuild the site's internal link map, which it was able to do in 45.1 seconds for 21 cents

Claude Opus 5 only got through 21 of those pages and spent a buck 43

Borja explains, "Internal linking is the perfect JEV job. It's not writing. It is 8,790 yes or no calls. [00:11:00] Does this page have a real reason to link to that one? And is there anchor text already sitting in the copy? That is a classification problem, and we have been paying frontier prices to do it one page at a time."

searching, a final subcategory of this searching by meaning

is filtering what you read by what you care about. So for example, Robin Billgillbuilt a real-time AI slop detector 

as they scroll X, The slop detector gives a confidence score 

on that zero to one scale about how much it thinks a post is AI slop or not, blocking out the ones that reach a certain confidence threshold



filtering, this sort of filtering though can be applied in a bunch of different ways. Elvis Sannon X 

gave an example of letting Jeff browse 384 morning news stories And identifying which of them 15 different brands should be paying attention to. that was completed in 24.9 seconds for 19 cents

and by way of comparison, in that same time period, Opus Five got through four of those articles leaving three hundred and eighty unread



JEV use case category three is triaging what comes in. In other words, what is this and where does it go?

the kinds of questions that people are experimenting with are [00:12:00] things like, how important is this email? Is this downloaded file an invoice? Is this link malicious? Should this lead go to sales, self-serve, or nurture?

One really interesting experiment came from Jonathan Yunikowski

He wrote, "Every email app shows your inbox in reverse chronological order. What if it was live prioritized by importance instead?"

Jeff's job in this case was to rate every email's importance

And in the test, it was able to rate 100 emails in 453 milliseconds for about a tenth of a cent

with Jonathan reporting that Jeb's rating matched his own on every single one

use, this is a use case that I want right now, not tomorrow In fact, I won it yesterday, and so do all of the people who are sitting there beating their heads against the wall because I haven't responded to them yet



Some other folks are experimenting with apattern of asking one quick question per item. Marcel Pokio, the CTO of Beyond Code writes, " I built a macOS app that monitors my downloads folder along with a customizable set of rules. Is the downloaded file an invoice?

Move it to a special folder with the correct file name. No other LLM calls involved, just [00:13:00] Jev."



DevEd used Jev for live chat moderation, removing swearing and negative comments as they arrive

Stephen Tay of the Dub link shortener fed JEV 10,000 malicious domains they'd caught before to flag bad links on their free shortener service

He wrote, "This has been something that we've been wrestling with since day one. With Jev, we solved it in two hours."



in fact, this sort of triage

is so integral to so much of business

mar-- in a post about 10 Jev use cases for a marketer, 



Umonx identified workflow decisions as one, saying, " Most workflows eventually hit the same question: What should happen next?" That's probably the best place to use Jev

Box gave an example having already experimented with incident triage, where Jev is used to judge customer impact and severity, as well as things like which routes it can be escalated to

Odoo CRM has a proposed module that asks three things about every new lead: their priority, their buying readiness, and whether it's spam or not

ex-- if you had to look at just one area to explore especially if you were in a company with multiple people touching the same leads or customers or contacts This sort of triage and [00:14:00] routing is, I think, where Jev is going to become absolutely integral

Basically from the moment that it gets integrated into the systems

A fourth category of JEV use cases is checking work against rules, i.e., does this meet the bar? Instead of the standard LLM question of please review this, you turn please review this into specific questions and then ask those questions about every draft

One example of this came from LangChain, 

which was grading an AI agent's work the same way every time

Harrison Chase from LangChain pointed out that Jev is, quote, "Great for evals, especially online evals where you want to grade lots of traces."



now this might feel initially like something that is 

more for devs than for other types of knowledge workers and companies. But given how much all of us are going to start putting agents into production or managing agents that already exist, think support bots, research agents, et cetera, having a better tool to build evaluation systems into how we judge those agents' work

Seems like it could very easily become core infrastructure

Every, and the team at Every showed how youcould use this sort of ability to check work against rules

at mass scale and at incredible speed as a way to [00:18:00] improve AI writing



they planted mistakes on 12 passages of writing

with Jev catching six of seven, as compared to Claude Fable 5.1's catching all seven

Jev, however, caught it six in 0.35 seconds as compared to 8.83 seconds for Fable 5.1. and it did so at about 580 times cheaper 

meaning that you could rerun that same check a huge number of times and still have it be both cheaper and faster than using a frontier model for the same sort of review

So how might you actually turn this into something that you would use?

You basically need to go through a translation process for your rules for writing. So let's imagine that you had a style guide or a list of phrases you never wanna see

you could turn each of those into a yes or no question, and then run those yes or no questions on every paragraph of your next long document

as a way to ensure no AI-isms or other writing third rails in your key communications

and this gets, I think, at one of the biggest rewiring's that we're going to need to do with JEV

of,

a lot of the unique value of Jev is not just being able to do a thing, it's being able to do a thing at such [00:19:00] scale

that it actually becomes a difference in kind rather than a difference in scale

Being able to realistically check every single sentence in minute detail for AI-isms in other words, becomes categorically different from just running a generic LLM check across the document as a whole

The fifth category of use cases that lots of people were experimenting with admittedly does get a little bit closer to the developer realm. but I think at least for the sake of completeness, it's still worth discussing.

these use cases you might sum up as speeding up your AI agents And a lot of this is around the sort of model routing that we've been talking about for the past several months

The kinds of questions people were asking were things like, which model can handle this task? st- how much reasoning does this step need? Which skill fits this request, if any? Is this old tool output still relevant? You can see how in each of these cases the common thread

Is people using, 

these small automated micro judgments

to route an agent to the right level ofintelligence, the right context, the right skills, the right tools to do whatever its job is in the most efficient way possible

Vi Chen [00:20:00] wrote, "People use JEV to pick a model before a task. I made it change GPT-6 reasoning's effort inside Codex during the task. More thinking when stuck, less for routine steps." and in their test they found 50% lower Astra costwhile also getting faster runs

also, people are also using Jev to manage the context window

really, Daniel Son built something called Jev Skill Suggestion for Claude Code Where, quote, "For every request, Jev classifies which skill best matches the task, then injects only that skill into Claude's context."

this led to an 88% decrease in tokens and cost

I know a lot of even you formerly non-developers have started to be sufficiently proficient withthings like Codex and Claude Code, that you've built up big skills libraries



and these sorts of JEV-based tools are potentially a way to stop sending all of those libraries to the model with every single request

And one thing to note here

is that while a lot of these use cases that we're discussing are at this stage individual experiments, You're also going to see JEV and judgment models like it built natively into the tools and harnesses we use

AJ Asver, [00:21:00] for example, wrote, " We built a new harness using Jev that cuts the cost of repetitive work by 90%. The harness learns the job as it runs, moving steps from LLM calls to code

the example they gave was compliance alerts

and they measured the cost per alert batch by batch with each batch representing 50 of those compliance alerts At the beginning, the cost per alert was about $2.95

but by alert one thousand it was down to just twenty five cents

a sixth category of JEV use cases are about instant response. What does this person want right now?

A lot of people were experimenting with some version of this. Marcus Lowe wrote, "What if copy/paste was smart? Copy a resume, paste into an application, and the fields fill themselves."

Norman on X also did a version of this splitting the pasted text into pieces, working out what each field is, matching them, checking against the original, and pasting only the confident matches



given how much work at work is moving details from one format, i.e. emails, PDFs, meeting notes, et cetera, into other [00:22:00] places where that information is supposed to live, like CRMs, intake forms or templates, this is a category of use cases thatfeels very, very relevant



now just as important as knowing where Jev is useful is knowing where you gotta be careful with it as well



w- a couple places that I think warrant greater caution areareas like hiring, money, and security. On hiring you can 

see how if deluged by a set of applications

you might be tempted to use something like JEV to rank them but the problem is that even if you've given it good criteria, Jev is gonna return with a number that doesn't have any reasoning attached

This, by the way, is a great example of where you might wanna build a more complex system that uses multiple types of AI. Imagine you do that same sort of ranking with JEV

but then automatically have other types of LLM review, for example, for bubble candidates that might be deserving of a second look

actually even try to be clear about what they think Jeb is bad at

at 

Some of the things they put include multi-step questions where they see accuracy drop with each hop

They point out that Jev isn't really good at counting math or dates, that it can extract the [00:23:00] facts, but that you're gonna wanna do the actual math elsewhere

And they also point out some other issues like problems with consistency and problems with reading intent

So if you're trying to figure out if a task is a good fit for Jev-

Four criteria might help. The first is that you can write down the answers in advance. Think categories, a yes or no binary, a scale If the answer is a sentence or a calculation, that's probably not a good fit for Jev's sort of judgment model.

Criteria number two is about volume. there's a pile or a stream, such as hundreds of tickets, hundreds of emails Things like that. a third criteria is about stakes, where a wrong answer is cheap or it's easy to catch

Basically, although I'm calling it a judgment model, don't wanna leave things up to its judgment alone 

if getting it wrong has big consequences

is, a final criteria Is whether you can give it the evidence that it needs as text in under 32,000 tokens

once you've figured out a good task, the next step is going to be to write good questions. some of the tips there from across all of these different examples are things like one judgment per question

[00:24:00] 

in other words, a not so good question is, is this a good lead?

' that cause that's actually not one judgment, that's a whole bunch of different judgments embedded in one. Good lead might refer to how good a fit the industry is for your service Whether the company size matches who you like to serve, how strong their buying intent is, et cetera, et cetera, et cetera.

Basically, you're gonna wanna break questions into their constituent parts

que- if your question involves a scale, you need to describe each level of that scale in words

and you also might even wanna take advantage of Jeff's scale opportunities to ask more questions than you think that you need

Lastly, like everything with AI

AI 

You're gonna wanna do some tests before you actually trust it in production

It might be a pain, but if you're using that email classifier, for example, to try to organize things based on priority, 

maybe you wanna label 50 emails yourself as a test and see how it compares to make sure it's actually gonna do for you what you want it to do



posting... Now as we wrap up

I will be posting this presentation that I've been working through 

on this episode's companion site on aidailybrief.ai. And the last couple of pages get a little bit more practical with one idea for each project in the six use [00:25:00] case areas.

Things like a content archive analyzer, a research rater, an inbox triager, a rewrite checker

Et cetera and there'll even be a starter prompt in there as well

In the first 10 days since Jeff was released

We've gone from buzzy, exciting concept to actually valuable production use cases extremely quickly and yet because this is at core a new primitive

and its ability to apply simple judgment at scale, at speed, and for effectively no money, I think it's gonna take some time for us to really figure out just how deeply we can weave this into allsorts of different use cases



As As more and more come online, I willcome back and share the best of them. For now, though, that is gonna do it for today's AI Daily Brief. Appreciate you listening or watching as always, and until next time, peace 

​
