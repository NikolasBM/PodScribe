# 10+ Things You Should Build With AI Instead of Sending Files — Transcript (2026-06-07)

https://aidailybrief.ai/e/2026-06-07 · Listen: https://pod.link/1680633614

---

[00:00:00] Today on the AI Daily Brief, 

10 or 15 or even 20 sites that knowledge workers should build with AI The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI. [00:00:15] All righty, friends, quick announcements before we dive in. First of all, thank you to today's Robots and Pencils, Assembly, Zencoder, and To get an ad-free version of the show, go to patreon.com/aidailybrief, [00:00:30] or you can, of course, subscribe on Apple Podcasts. To learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai. is also where you can find out about other things going on in the ecosystem. For example

one more call to sign up for thefour-week Sprint [00:00:45] Executive Catch-Up program. This is being led by Nufar Gaspar, and she gave a bit of a preview on our episode a couple of weeks ago

if you have been feeling behind in practice and wanna be up to speed and moving ahead, This could be the program for you

registration is closing in the next day or so, [00:01:00] so check it out at aiexecutivecatchup.com. Obviously, that link will be in the show notes as well

Now, happy Now, happy weekend, friends. It being a weekend, this is, of course, a long read style or big think episode. Although today we're gonna do something a bit more practical

that was [00:01:15] inspired directly by a launch from this week. an- on Tuesday, OpenAI announced a bunch of updates to Codex

One of them was called CITES

and effectively, Sites is just a simplified way To take the things that you're building with Codex and [00:01:30] publish them as a website or a web app that your team or friends or colleagues can interact with

is, I think the idea is

Whereas in the past, to actually publish something



you'd either need to have

hosting platform like Vercel and a database platform like Supabase, and wire that [00:01:45] together with Claude Code or Codex, or alternately be using an all-in-one vibe code experience like Replit or Lovable. of, now that sort of all-in-one experience is native to Codex. 

Simplify, simplifying the whole process. 



now one of the things that I think this both recognizes but also [00:02:00] amplifies is the idea of the website 

or simple web app 

As a new unit of work output i e

a new anchor artifact in the knowledge worker's toolkit

toolkit 

Now,

Now, for decades, knowledge workers have packaged thinking into different types of documents, decks, spreadsheets, [00:02:15] PDFs, email threads, shared folders, et cetera, whatever the menu of formats available was. Importantly, though, that menu wasn't chosen because the formats were the best way to carry knowledge necessarily

But the ability to use code to turn those artifacts into something [00:02:30] more interactive, dynamic, updatable was limited to a very specific few, and the literal cost in terms of money or distraction of other people in the company meant that a website wasn't really on the table as a format AI has of course changed that cost structure [00:02:45] entirely

Any,

any semi-capable person can now generate a useful, fairly good-looking website

as easily, if not more easily than they used to throw together a deck

And increasingly what we're seeing is that there are many artifacts in the knowledge worker kit right now

[00:03:00] that are actually better suited to being websites. So that's what we're gonna talk about today First though, let's talk about the problems of traditional documents and artifacts that websites solve

the, the first one is the update versioning currency [00:03:15] problem

I would be willing to bet that on your computer somewhere There's 18 different versions of some file with a confusing set of file names like plan\_v2, plan\_v3, plan\_final, plan\_finalfinal, plan\_finalv3, [00:03:30] plan\_finalv8, et cetera, et cetera, et cetera

The problem is that any sort of downloadable file is a snapshot of a moment in time And as soon as you send it off, the clock starts running on it going out of date

A URL and doing things [00:03:45] as a website fixes that It gives the knowledge a canonical home

update, when you continue to control the ability to update it, 

it means that whenever people land on that URL, it is the most up-to-date version

This saves time, cognitive back and forth

and creates information [00:04:00] consistency across the whole organization

Now this is such a big problem that obviously there are lots of intermediate solutions for this DocSend, for example, gives you the ability to update PDFs on the same link

collaboration suites like Google Docs 

are meant to give you tools

So that everyone can be working off the same [00:04:15] version. But building things as a website is a more generalist solution to this set of problems

of,

speaking of sending things off, distribution is the second problem 

that websites as knowledge work artifact solves



downloadable files create friction

you have to make sure that the place you're sending them [00:04:30] works with the file format in question. The person on the other side has to have the bandwidth to do the download

that download then becomes part 

of the endless set of files that they eventually need to organize or trash on their computer

And if they need to pass it on They have to go through that whole process again

A A link does none of [00:04:45] that. It moves through email, Slack, a text, a CRM, a calendar invite, a newsletter, and it works the same on a laptop or a phone without anyone touching an attachment

Problem number three that websites solve, navigation



every current type of downloadable knowledge work artifact [00:05:00] has a navigation constraint. Docs are linear, spreadsheets are tabular, PDFs are paged

Each one forces a structure onto every reader in the order that it was written. Now, sometimes that's the goal but knowledge work tends not to be consumed by one generic reader in one linear [00:05:15] setting. People arrive with different questions and different amounts of time. A website can organize that same material in a variety of different ways: by topic, by role, by urgency, by depth

It allows for dynamism in the consumption. The exec reads the summary, the analyst jumps straight to the [00:05:30] evidence, someone else searches the glossary And all that happens without everyone having to read your table of contents

Now, so far we've just been talking about single documents as if they exist alone

But a lot of knowledge work has context that lives across multiple different types of documents. The charts in a [00:05:45] spreadsheet, the explanations in a memo, the sources in a browser tab, the decisions in an email thread

m- an HTML site gives you a much more dynamic environment to layer context together

You can ship everything that used to be spread across four or five different places, all with one single [00:06:00] URL

And what's more, the shipping doesn't have to be unidirectional

In the downloadable document paradigm of knowledge work The artifacts that you send are passive for the consumer. You're gonna choose the order, the format, what's included 

a site on the other hand opens up all sorts of different 

[00:06:15] interactive possibilities

way, this also, by the way

Makes it easier, 

for a single artifact to serve very different types of audiences

which gets to our sixth problem

that site solve, which is audience fit



Docu- downloadable documents tend to force people to flatten everyone into an imaginary [00:06:30] average reader

Websites create a much better canvas 

for helping people navigate through the experience based on who they are and what information they're trying to get

Sites also add easier and more native actionability

When the report says something important or the DEC recommends an action, that [00:06:45] action necessarily has to happen elsewhere

At best, you have a PDF that opens up, you guessed it, a website. If you just build the thing as a website in the first place the artifact can actually hold the action layer natively

Websites also increase artifact [00:07:00] reusability hand, this goes hand in hand withthe first problem we solved around currency

But web work is modular by nature A section can link out, a chart can embed elsewhere, a page can expand, a private version can become a public one, a proposal can become a client portal, a report can become a hub, a [00:07:15] training page can become part of onboarding

Instead of documents getting copied and degraded each time, they can build on top of each other and compound

And as they compound, you can see who's actually interacting

sending a deck out is dropping something into the void and hoping it works

A site, if [00:07:30] designed well, can produce signal around what got read, what got clicked, what got searched, what got shared, what got revisited, what got abandoned. The feedback means the artifact itself can become improvable And there are so many use cases, sales, training, fundraising, internal communications, change management, [00:07:45] where understanding where the message actually landed is essential for whatever the next steps are

Last Last couple problems that websites can help with

The next is presentation

A spreadsheet looks like a spreadsheet. A PDF feels final but inert

a website can look intentional and polished. [00:08:00] isn't, now obviously this isn't always going to be the case and you do have to put intention behind it. In the same way that there's a big difference between a good deck and a bad deck

But especially in vibe coding world and with tools like Codex's new sites, the ability to present things well and make them feel and look intentional goes way [00:08:15] up

To the extent you have lots of different audiences, websites can also help with permissioning

And making sure the right people have access to the right parts And finally, one that will be increasingly important, especially as this week Cloudflare reported

that agent and bot browsing accounted for more web use 

[00:08:30] than human browsing for the first time ever



websites can be designed 

for agent consumption

big deal, that might not be a big deal now But in a paradigm where knowledge work artifacts have to interact with agents, the old messy system of PDFs and docs and CSVs and [00:08:45] PowerPoints starts to look really brittle, 

especially compared to the comparatively designed for agent 

HTML and other weblanguages One thing I keep seeing in enterprise AI, companies hedging [00:09:00] across every cloud, every model, every framework, or paying a GSI for a pilot that never ends. The teams actually shipping, they've picked a lane and they move fast.

No sign-up needed Coding agents are basically solved at this point. They're incredible at writing code. But here's the thing nobody talks about. Coding is maybe a quarter of an engineer's actual day. The rest is standups. Stakeholder updates, meeting [00:10:45] prep, chasing context across six different tools, and it's not just engineers.

Sales spends more time assembling proposals than selling finances, manually chasing subscription requests. Marketing finds out what shipped two weeks after it merged. Zen Coder just launched Zen Flow work. It takes their [00:11:00] orchestration engine, the same one already powering coding agents connects it to your daily tools.

Jira Gmail, Google Docs, linear calendar notion. It runs goal-driven workflows that actually finish

your standup brief is written before you sit down, review cycle. Coming up, it pulls six months of tickets and writes [00:11:15] the Prep Doc.

Now you might be thinking, didn't open Claw try to do this?

It did, but it has come with a whole host of security and functional issues. which can take a huge amount of time to resolve. Zen Coder took a different approach. SOC two. Type two certified.



Okay so we've talked through about adozen or [00:12:30] more problems with traditional knowledge work artifacts that websites can solve.

But what are some of the best examples that you as a knowledge worker could actually go out and try

18, I've got 18 different examples here, so we'll go through them pretty quickly 

but I do want you to watch out

for some common [00:12:45] patterns

is, one pattern is about distribution. A lot of these things are the types of things that get forwarded around a committee without you in the room Another pattern is things that keep evolving after you, quote unquote, "finish them." The third pattern is things that scatter across different channels

The goal in sharing these is notthat you're going to use [00:13:00] all of these examples, but instead that if these types of artifacts are things that you regularly interact with or create in the course of your work, they're worth considering whether building a website Might be, in some cases, a better alternative

The first and perhaps most obvious one is exactly what I'm doing now, [00:13:15] building a narrative website instead

of a traditional slide deck. Now, if you've used any of the AI native presentation tools like Gamma, You'll know that they're already collapsing the space between a slide deck and a website, and I think 

that 

that's a mega trend that's just going to continue

lot of the, Also directionally, a [00:13:30] lot of the SaaS tools that are used 

to distribute PDFs

are just approximating with features the things that websites can do natively, 

including updating them to the latest version

and doing access provisioning. but what those tools don't have 

that native 

website, that native 

websites do is a lot of the other stuff we just talked about, [00:13:45] like the ability to build interactive features



or the ability to break out of the 16 by 9 aspect ratio 

to,

the ability to easily link things out

And connect your presentation to other parts of the context



if you do nothing else in this, I would very much suggest starting [00:14:00] to explore whether on average and by default, the slide decks that you build currently should just become narrative websites instead

Similar Now next up we have the shift from a strategy memo to a strategy site

and here's where the breadth that a website can give you I think 

really starts to play out [00:14:15] Strategy memos, by virtue of the fact that they're trying to argue for something, 

often tend to be overloaded by design. They have to provide a bunch of context, the problem, the argument, the objections, the evidence, the action



and they have to do that all linearly in a PDF, whereas a site can layer [00:14:30] that in a way that's much more navigable and gives different audiences the ability to very quickly hone in on the parts that matter to them

Our next example, moving from a research report to a research hub, is very similar. Taking one big dense thing and organizing it in a [00:14:45] way with a website 

that's layered, more navigable, has links out to relevant context and sources and just generally makes 

the important information contained within that report 

more accessible to a wide variety of readers

Our Our next example, moving from a spreadsheet to a data site

is a recognition that [00:15:00] spreadsheets are a powerful tool for their creator, but in general, a pretty poor interface for anyone but the creator

Spreadsheets 

have all sorts of hidden or semi-hidden information Formulas, the way the tabs are designed

A A site, meanwhile, can [00:15:15] take all that data and turn it into a guided view. It can turn it into dashboards, filters, summaries, charts. It can visualize the data To the extent that the goal of your spreadsheet

is people coming to the same conclusion that you're trying to suggest to them, a database website [00:15:30] is often going to be a much better example

The next The next example is one that I'm already seeing quite a bit of, a shift from sales proposals to proposal microsites Whereas proposals are against static documents Microsites can carry all sorts of interactive elements, [00:15:45] like the ability to toggle different variables to see how that would change the price or the expected ROI

A proposal microsite does a better job of actually selling when you're not in the room. And what's more, the observability allows you to see how people are interacting with it in a way that a PDF [00:16:00] just can't

The next example is another one that I'm seeing a lot in production already, especially from agencies, which is the shift from a client update to a client portal. current-- The failure mode is recurring client updates that are scattered across email, docs, decks, and one-off links

Versus a portal which [00:16:15] gives them a single place to go with the current status, the milestones, the deliverables, the open questions

Perfectly queued up for that particular project

The The next example, moving from a project brief to a project homepage

is a way to keep a canonical source for the changing goals, [00:16:30] stakeholders, decisions, et cetera, of a particular project over time

Now, this may not always be relevant, 

especially if a brief kicks off a process that moves into some existing project management software

But for those companies that aren't using existing project management [00:16:45] tools or who just want something a little bit similar and more bespoke A website is a muchmore dynamic tool than just a simple brief

Use case eight, a case study becomes an interactive case page

and this is all about leveraging that presentation capacity of websites

A case study PDF [00:17:00] inherently is going to flatten a potentially rich story into a couple of paragraphs and a logo. the most convincing parts can get compressed out. an interactive case page, because it creates space for people to navigate directly to the parts that matter most to them or are most relevant, creates [00:17:15] way more space for a bigger version of the story.

It can hold more context around the problem, the process, the metrics. It can also embed other types of rich media like videos



anyone who's selling something is going to increasingly put not only their decks but also their case [00:17:30] studies into these sort of interactive webpages, 



I am quite sure





example nine is an interesting archetype where it's not so much that a website is a better version of the thing

but actually changes the thing at core So in this case, we're talking about a competitive analysis. [00:17:45] And it's not just that a website is a better way to present an existing competitive analysis, but that if you use a website for a competitive analysis, it can instead become a competitive intelligence hub, 



a living, dynamic, evolving resource rather than just a one-time [00:18:00] resource

Now, I think that this also gives you a sense of how these sort of website builds could start to interface with agents as they get more mature as well imagine not just that you've shifted the publishing of your competitive analysis to a competitive intelligence hub, but that you've got your professional open [00:18:15] claw style agent 



continuously researching the key information andupdating that hub at regular intervals

The next example is one that will be veryfamiliar to AI Daily Brief listeners, which is moving from static training materials to dynamic learning sites if you've ever participated in [00:18:30] any of our programs

Whether it's Agent OS or Claw Camp before that or the AIDB New Year program you'll know that their entire platform's purpose-built for the particular training experience

And this is despite those programs being offered for free 

because the cost to produce a bespoke [00:18:45] learning management system exactly optimized 

for a particular program has just cratered to the time it takes 

to interact with whatever tool you're using to build it

I think I think there's a similar opportunity

In making employee information the sort of thing that lives in employee handbooks

turn into living interactive [00:19:00] experiences this is a great example of where I think a thing that almost no one would use, which is the PDF version of an employee handbook, or only use when they absolutely have to and don't have any better way of getting that information, could become something that's actually a valuable resource

The fact that a [00:19:15] living handbook site can also be updated with the latest policies just makes it instantly more useful than even a regularly updated PDF that's gonna deal with versioning problems and all sorts of other challenges



The next The next two examples areboth about presenting information to other stakeholders



the first is [00:19:30] board materials, which tend to become massive all-in-one PDFs or folders that have a bunch of PDFs

Whereas a portal or website can separate required reading from backup, 

it can preserve context It can basically provide all of the background information that you might want to make available [00:19:45] without forcing people to wade through that to get to what really matters.

same idea moving from an investor update paradigm to an investor page paradigm Where honestly, depending on how transparent you wanna be, instead of giving investors metrics on an every once in a while basis

you can give them access to [00:20:00] the most up-to-the-date, 

potentially even real-time depending on the APIs you have access to

Anyone who has fielded a request from their investors to give them some specific update 

for, 

for example, their LP board. We'll know that this can also save time by having a single easy link that you can point people [00:20:15] to whenever it is that they need information, which may not be at the same time that you've spent time preparing the latest round of information

Last couple here as we round out

I really like the experience of shifting from recruiting packets and boring job descriptions to full candidate sites. it gives you a [00:20:30] much bigger tapestry to explain the role, give background, help candidates be successful in figuring out 

whether they're a right fit and how to tell you 

so.

overall incomparably better experience Brand guidelines can become brand system sites. This is another one where if you're [00:20:45] constantly digging up some brand PDF in a folder of assets, that is just so much easier to organize 

as a single URL with all the current and up-to-date

Similarly, media kits can become press sites, A single easy link that has everything the press might need

Ultimately the [00:21:00] idea is that with a file, the traditional artifacts of knowledge work, you had a container for a limited amount of information. That container came with constraints. Constraints in how easy to move around it was How up to date it was, versioning issues, access [00:21:15] issues

Issues so pronounced that they created entire companies around solving them for a particular type of document like PDFs. Websites are much more dynamic and rich environments where you can add interaction, access controls, versioning

all in a much more easy to share [00:21:30] format

My observation is that a huge part of the explosion of vibe coding

is simply knowledge workers figuring out that websites are better ways to share information than the traditional artifacts that they used to use. believe that, and you better believe the fact that platforms like Codex are now

[00:21:45] embedding features like sites into them means 

that 

that's gonna do nothing but expand.

Hopefully Hopefully now after this presentation, you can get out ahead of

using this approach to make your 

work 

work better. And I'm excited to see if you come up with any other use cases that I haven't mentioned here. For now, however, that's gonna do it for today's AI Daily [00:22:00] Brief.

Appreciate you listening or watching, as always, and until next time, peace. 

​ 

[00:22:15]
