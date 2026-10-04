---
podcast: "latent-space"
podcast_title: "Latent Space"
title: "The AI Architect — Bret Taylor"
date: 2025-02-11
url: "https://www.latent.space/p/bret"
guid: "substack:156886978"
host: "Swyx"
transcript_source: "publisher"
---

# The AI Architect — Bret Taylor

## [00:02:05] Introduction and Guest Welcome

**Alessio** [00:00:00] Hey everyone, welcome to the Latent Space Podcast. This is Alessio, partner and CTO at Decibel Partners, and I'm joined by my co host swyx, founder of smol.ai.

**Swyx** [00:00:00] Hey, and today we're super excited to have Bret Taylor join us. Welcome. Thanks for having me. It's a little unreal to have you in the studio.

**Swyx** [00:00:00] I've read about you so much over the years, like even before. Open AI effectively. I mean, I use Google Maps to get here. So like, thank you for everything that you've done. Like, like your story history, like, you know, I think people can find out what your greatest hits have been.

## [00:02:40] Bret Taylor's Early Career and Education

**Swyx** [00:00:00] How do you usually like to introduce yourself when, you know, you talk about, you summarize your career, like, how do you look at yourself?

**Bret** [00:00:00] Yeah, it's a great question. You know, we, before we went on the mics here, we're talking about the audience for this podcast being more engineering. And I do think depending on the audience, I'll introduce myself differently because I've had a lot of corporate and board roles. I probably self identify as an engineer more than anything else though.

**Bret** [00:03:00] So even when I was. Salesforce, I was coding on the weekends. So I think of myself as an engineer and then all the roles that I do in my career sort of start with that just because I do feel like engineering is sort of a mindset and how I approach most of my life. So I'm an engineer first and that's how I describe myself.

**Bret** [00:03:00] You majored in computer

**Swyx** [00:03:00] science, like 1998. And, and I was high

**Bret** [00:03:00] school, actually my, my college degree was Oh, two undergrad. Oh, three masters. Right. That old.

**Swyx** [00:03:00] Yeah. I mean, no, I was going, I was going like 1998 to 2003, but like engineering wasn't as, wasn't a thing back then. Like we didn't have the title of senior engineer, you know, kind of like, it was just.

**Swyx** [00:03:00] You were a programmer, you were a developer, maybe. What was it like in Stanford? Like, what was that feeling like? You know, was it, were you feeling like on the cusp of a great computer revolution? Or was it just like a niche, you know, interest at the time?

## [00:03:57] Stanford and the Dot-Com Bubble

**Bret** [00:03:00] Well, I was at Stanford, as you said, from 1998 to 2002.

**Bret** [00:04:00] 1998 was near the peak of the dot com bubble. So. This is back in the day where most people that they're coding in the computer lab, just because there was these sun microsystems, Unix boxes there that most of us had to do our assignments on. And every single day there was a. com like buying pizza for everybody.

**Bret** [00:04:00] I didn't have to like, I got. Free food, like my first two years of university and then the dot com bubble burst in the middle of my college career. And so by the end there was like tumbleweed going to the job fair, you know, it was like, cause it was hard to describe unless you were there at the time, the like level of hype and being a computer science major at Stanford was like, A thousand opportunities.

**Bret** [00:04:00] And then, and then when I left, it was like Microsoft, IBM.

## [00:04:49] Joining Google and Early Projects

**Bret** [00:04:00] And then the two startups that I applied to were VMware and Google. And I ended up going to Google in large part because a woman named Marissa Meyer, who had been a teaching assistant when I was, what was called a section leader, which was like a junior teaching assistant kind of for one of the big interest.

**Bret** [00:05:00] Yes. Classes. She had gone there. And she was recruiting me and I knew her and it was sort of felt safe, you know, like, I don't know. I thought about it much, but it turned out to be a real blessing. I realized like, you know, you always want to think you'd pick Google if given the option, but no one knew at the time.

**Bret** [00:05:00] And I wonder if I'd graduated in like 1999 where I've been like, mom, I just got a job at pets. com. It's good. But you know, at the end I just didn't have any options. So I was like, do I want to go like make kernel software at VMware? Do I want to go build search at Google? And I chose Google. 50, 50 ball.

**Bret** [00:05:00] I'm not really a 50, 50 ball. So I feel very fortunate in retrospect that the economy collapsed because in some ways it forced me into like one of the greatest companies of all time, but I kind of lucked into it, I think.

## [00:05:47] The Google Maps Rewrite Story

**Alessio** [00:05:00] So the famous story about Google is that you rewrote the Google maps back in, in one week after the map quest quest maps acquisition, what was the story there?

**Alessio** [00:05:00] Is it. Actually true. Is it being glorified? Like how, how did that come to be? And is there any detail that maybe Paul hasn't shared before?

**Bret** [00:06:00] It's largely true, but I'll give the color commentary. So it was actually the front end, not the back end, but it turns out for Google maps, the front end was sort of the hard part just because Google maps was.

**Bret** [00:06:00] Largely the first ish kind of really interactive web application, say first ish. I think Gmail certainly was though Gmail, probably a lot of people then who weren't engineers probably didn't appreciate its level of interactivity. It was just fast, but. Google maps, because you could drag the map and it was sort of graphical.

**Bret** [00:06:00] My, it really in the mainstream, I think, was it a map

**Swyx** [00:06:00] quest back then that was, you had the arrows up and down, it

**Bret** [00:06:00] was up and down arrows. Each map was a single image and you just click left and then wait for a few seconds to the new map to let it was really small too, because generating a big image was kind of expensive on computers that day.

**Bret** [00:06:00] So Google maps was truly innovative in that regard. The story on it. There was a small company called where two technologies started by two Danish brothers, Lars and Jens Rasmussen, who are two of my closest friends now. They had made a windows app called expedition, which had beautiful maps. Even in 2000.

**Bret** [00:07:00] For whenever we acquired or sort of acquired their company, Windows software was not particularly fashionable, but they were really passionate about mapping and we had made a local search product that was kind of middling in terms of popularity, sort of like a yellow page of search product. So we wanted to really go into mapping.

**Bret** [00:07:00] We'd started working on it. Their small team seemed passionate about it. So we're like, come join us. We can build this together.

## [00:07:42] Technical Challenges and Innovations

**Bret** [00:07:00] It turned out to be a great blessing that they had built a windows app because you're less technically constrained when you're doing native code than you are building a web browser, particularly back then when there weren't really interactive web apps and it ended up.

**Bret** [00:07:00] Changing the level of quality that we wanted to hit with the app because we were shooting for something that felt like a native windows application. So it was a really good fortune that we sort of, you know, their unusual technical choices turned out to be the greatest blessing. So we spent a lot of time basically saying, how can you make a interactive draggable map in a web browser?

**Bret** [00:08:00] How do you progressively load, you know, new map tiles, you know, as you're dragging even things like down in the weeds of the browser at the time, most browsers like Internet Explorer, which was dominant at the time would only load two images at a time from the same domain. So we ended up making our map tile servers have like.

**Bret** [00:08:00] Forty different subdomains so we could load maps and parallels like lots of hacks. I'm happy to go into as much as like

**Swyx** [00:08:00] HTTP connections and stuff.

**Bret** [00:08:00] They just like, there was just maximum parallelism of two. And so if you had a map, set of map tiles, like eight of them, so So we just, we were down in the weeds of the browser anyway.

**Bret** [00:08:00] So it was lots of plumbing. I can, I know a lot more about browsers than most people, but then by the end of it, it was fairly, it was a lot of duct tape on that code. If you've ever done an engineering project where you're not really sure the path from point A to point B, it's almost like. Building a house by building one room at a time.

**Bret** [00:09:00] The, there's not a lot of architectural cohesion at the end. And then we acquired a company called Keyhole, which became Google earth, which was like that three, it was a native windows app as well, separate app, great app, but with that, we got licenses to all this satellite imagery. And so in August of 2005, we added.

**Bret** [00:09:00] Satellite imagery to Google Maps, which added even more complexity in the code base. And then we decided we wanted to support Safari. There was no mobile phones yet. So Safari was this like nascent browser on, on the Mac. And it turns out there's like a lot of decisions behind the scenes, sort of inspired by this windows app, like heavy use of XML and XSLT and all these like.

**Bret** [00:09:00] Technologies that were like briefly fashionable in the early two thousands and everyone hates now for good reason. And it turns out that all of the XML functionality and Internet Explorer wasn't supporting Safari. So people are like re implementing like XML parsers. And it was just like this like pile of shit.

**Bret** [00:10:00] And I had to say a shit on your part. Yeah, of

**Alessio** [00:10:00] course.

**Bret** [00:10:00] So. It went from this like beautifully elegant application that everyone was proud of to something that probably had hundreds of K of JavaScript, which sounds like nothing. Now we're talking like people have modems, you know, not all modems, but it was a big deal.

**Bret** [00:10:00] So it was like slow. It took a while to load and just, it wasn't like a great code base. Like everything was fragile. So I just got. Super frustrated by it. And then one weekend I did rewrite all of it. And at the time the word JSON hadn't been coined yet too, just to give you a sense. So it's all XML.

**Swyx** [00:10:00] Yeah.

**Bret** [00:10:00] So we used what is now you would call JSON, but I just said like, let's use eval so that we can parse the data fast. And, and again, that's, it would literally as JSON, but at the time there was no name for it. So we just said, let's. Pass on JavaScript from the server and eval it. And then somebody just refactored the whole thing.

**Bret** [00:11:00] And, and it wasn't like I was some genius. It was just like, you know, if you knew everything you wished you had known at the beginning and I knew all the functionality, cause I was the primary, one of the primary authors of the JavaScript. And I just like, I just drank a lot of coffee and just stayed up all weekend.

**Bret** [00:11:00] And then I, I guess I developed a bit of reputation and no one knew about this for a long time. And then Paul who created Gmail and I ended up starting a company with him too, after all of this told this on a podcast and now it's large, but it's largely true. I did rewrite it and it, my proudest thing.

**Bret** [00:11:00] And I think JavaScript people appreciate this. Like the un G zipped bundle size for all of Google maps. When I rewrote, it was 20 K G zipped. It was like much smaller for the entire application. It went down by like 10 X. So. What happened on Google? Google is a pretty mainstream company. And so like our usage is shot up because it turns out like it's faster.

**Bret** [00:11:00] Just being faster is worth a lot of percentage points of growth at a scale of Google. So how

**Swyx** [00:12:00] much modern tooling did you have? Like test suites no compilers.

**Bret** [00:12:00] Actually, that's not true. We did it one thing. So I actually think Google, I, you can. Download it. There's a, Google has a closure compiler, a closure compiler.

**Bret** [00:12:00] I don't know if anyone still uses it. It's gone. Yeah. Yeah. It's sort of gone out of favor. Yeah. Well, even until recently it was better than most JavaScript minifiers because it was more like it did a lot more renaming of variables and things. Most people use ES build now just cause it's fast and closure compilers built on Java and super slow and stuff like that.

**Bret** [00:12:00] But, so we did have that, that was it. Okay.

## [00:12:39] The Evolution of Web Applications

**Bret** [00:12:00] So and that was treated internally, you know, it was a really interesting time at Google at the time because there's a lot of teams working on fairly advanced JavaScript when no one was. So Google suggest, which Kevin Gibbs was the tech lead for, was the first kind of type ahead, autocomplete, I believe in a web browser, and now it's just pervasive in search boxes that you sort of see a type ahead there.

**Bret** [00:13:00] I mean, chat, dbt

**Swyx** [00:13:00] just added it. It's kind of like a round trip.

**Bret** [00:13:00] Totally. No, it's now pervasive as a UI affordance, but that was like Kevin's 20 percent project. And then Gmail, Paul you know, he tells the story better than anyone, but he's like, you know, basically was scratching his own itch, but what was really neat about it is email, because it's such a productivity tool, just needed to be faster.

**Bret** [00:13:00] So, you know, he was scratching his own itch of just making more stuff work on the client side. And then we, because of Lars and Yen sort of like setting the bar of this windows app or like we need our maps to be draggable. So we ended up. Not only innovate in terms of having a big sync, what would be called a single page application today, but also all the graphical stuff you know, we were crashing Firefox, like it was going out of style because, you know, when you make a document object model with the idea that it's a document and then you layer on some JavaScript and then we're essentially abusing all of this, it just was running into code paths that were not.

**Bret** [00:13:00] Well, it's rotten, you know, at this time. And so it was super fun. And, and, you know, in the building you had, so you had compilers, people helping minify JavaScript just practically, but there is a great engineering team. So they were like, that's why Closure Compiler is so good. It was like a. Person who actually knew about programming languages doing it, not just, you know, writing regular expressions.

**Bret** [00:14:00] And then the team that is now the Chrome team believe, and I, I don't know this for a fact, but I'm pretty sure Google is the main contributor to Firefox for a long time in terms of code. And a lot of browser people were there. So every time we would crash Firefox, we'd like walk up two floors and say like, what the hell is going on here?

**Bret** [00:14:00] And they would load their browser, like in a debugger. And we could like figure out exactly what was breaking. And you can't change the code, right? Cause it's the browser. It's like slow, right? I mean, slow to update. So, but we could figure out exactly where the bug was and then work around it in our JavaScript.

**Bret** [00:14:00] So it was just like new territory. Like so super, super fun time, just like a lot of, a lot of great engineers figuring out new things. And And now, you know, the word, this term is no longer in fashion, but the word Ajax, which was asynchronous JavaScript and XML cause I'm telling you XML, but see the word XML there, to be fair, the way you made HTTP requests from a client to server was this.

**Bret** [00:15:00] Object called XML HTTP request because Microsoft and making Outlook web access back in the day made this and it turns out to have nothing to do with XML. It's just a way of making HTTP requests because XML was like the fashionable thing. It was like that was the way you, you know, you did it. But the JSON came out of that, you know, and then a lot of the best practices around building JavaScript applications is pre React.

**Bret** [00:15:00] I think React was probably the big conceptual step forward that we needed. Even my first social network after Google, we used a lot of like HTML injection and. Making real time updates was still very hand coded and it's really neat when you see conceptual breakthroughs like react because it's, I just love those things where it's like obvious once you see it, but it's so not obvious until you do.

**Bret** [00:16:00] And actually, well, I'm sure we'll get into AI, but I, I sort of feel like we'll go through that evolution with AI agents as well that I feel like we're missing a lot of the core abstractions that I think in 10 years we'll be like, gosh, how'd you make agents? Before that, you know, but it was kind of that early days of web applications.

**Swyx** [00:16:00] There's a lot of contenders for the reactive jobs of of AI, but no clear winner yet. I would say one thing I was there for, I mean, there's so much we can go into there. You just covered so much.

## [00:16:32] Product Management and Engineering Synergy

**Swyx** [00:16:00] One thing I just, I just observe is that I think the early Google days had this interesting mix of PM and engineer, which I think you are, you didn't, you didn't wait for PM to tell you these are my, this is my PRD.

**Swyx** [00:16:00] This is my requirements.

[00:16:00] mix: Oh,

**Bret** [00:16:44] okay.

**Swyx** [00:16:44] I wasn't technically a software engineer. I mean,

**Bret** [00:16:44] by title, obviously. Right, right, right.

**Swyx** [00:16:44] It's like a blend. And I feel like these days, product is its own discipline and its own lore and own industry and engineering is its own thing. And there's this process that happens and they're kind of separated, but you don't produce as good of a product as if they were the same person.

**Swyx** [00:17:00] And I'm curious, you know, if, if that, if that sort of resonates in, in, in terms of like comparing early Google versus modern startups that you see out there,

**Bret** [00:17:00] I certainly like wear a lot of hats. So, you know, sort of biased in this, but I really agree that there's a lot of power and combining product design engineering into as few people as possible because, you know few great things have been created by committee, you know, and so.

**Bret** [00:17:00] If engineering is an order taking organization for product you can sometimes make meaningful things, but rarely will you create extremely well crafted breakthrough products. Those tend to be small teams who deeply understand the customer need that they're solving, who have a. Maniacal focus on outcomes.

**Bret** [00:17:00] And I think the reason why it's, I think for some areas, if you look at like software as a service five years ago, maybe you can have a separation of product and engineering because most software as a service created five years ago. I wouldn't say there's like a lot of like. Technological breakthroughs required for most, you know, business applications.

**Bret** [00:18:00] And if you're making expense reporting software or whatever, it's useful. I don't mean to be dismissive of expense reporting software, but you probably just want to understand like, what are the requirements of the finance department? What are the requirements of an individual file expense report? Okay.

**Bret** [00:18:00] Go implement that. And you kind of know how web applications are implemented. You kind of know how to. How databases work, how to build auto scaling with your AWS cluster, whatever, you know, it's just, you're just applying best practices to yet another problem when you have areas like the early days of mobile development or the early days of interactive web applications, which I think Google Maps and Gmail represent, or now AI agents, you're in this constant conversation with what the requirements of your customers and stakeholders are and all the different people interacting with it.

**Bret** [00:18:00] And the capabilities of the technology. And it's almost impossible to specify the requirements of a product when you're not sure of the limitations of the technology itself. And that's why I use the word conversation. It's not literal. That's sort of funny to use that word in the age of conversational AI.

**Bret** [00:19:00] You're constantly sort of saying, like, ideally, you could sprinkle some magic AI pixie dust and solve all the world's problems, but it's not the way it works. And it turns out that actually, I'll just give an interesting example.

## [00:19:26] AI Agents and Modern Tooling

**Bret** [00:19:00] I think most people listening probably use co pilots to code like Cursor or Devon or Microsoft Copilot or whatever.

**Bret** [00:19:00] Most of those tools are, they're remarkable. I'm, I couldn't, you know, imagine development without them now, but they're not autonomous yet. Like I wouldn't let it just write most code without my interactively inspecting it. We just are somewhere between it's an amazing co pilot and it's an autonomous software engineer.

**Bret** [00:19:00] As a product manager, like your aspirations for what the product is are like kind of meaningful. But if you're a product person, yeah, of course you'd say it should be autonomous. You should click a button and program should come out the other side. The requirements meaningless. Like what matters is like, what is based on the like very nuanced limitations of the technology.

**Bret** [00:20:00] What is it capable of? And then how do you maximize the leverage? It gives a software engineering team, given those very nuanced trade offs. Coupled with the fact that those nuanced trade offs are changing more rapidly than any technology in my memory, meaning every few months you'll have new models with new capabilities.

**Bret** [00:20:00] So how do you construct a product that can absorb those new capabilities as rapidly as possible as well? That requires such a combination of technical depth and understanding the customer that you really need more integration. Of product design and engineering. And so I think it's why with these big technology waves, I think startups have a bit of a leg up relative to incumbents because they tend to be sort of more self actualized in terms of just like bringing those disciplines closer together.

**Bret** [00:21:00] And in particular, I think entrepreneurs, the proverbial full stack engineers, you know, have a leg up as well because. I think most breakthroughs happen when you have someone who can understand those extremely nuanced technical trade offs, have a vision for a product. And then in the process of building it, have that, as I said, like metaphorical conversation with the technology, right?

**Bret** [00:21:00] Gosh, I ran into a technical limit that I didn't expect. It's not just like changing that feature. You might need to refactor the whole product based on that. And I think that's, that it's particularly important right now. So I don't, you know, if you, if you're building a big ERP system, probably there's a great reason to have product and engineering.

**Bret** [00:21:00] I think in general, the disciplines are there for a reason. I think when you're dealing with something as nuanced as the like technologies, like large language models today, there's a ton of advantage of having. Individuals or organizations that integrate the disciplines more formally.

**Alessio** [00:22:00] That makes a lot of sense.

**Alessio** [00:22:00] I've run a lot of engineering teams in the past, and I think the product versus engineering tension has always been more about effort than like whether or not the feature is buildable. But I think, yeah, today you see a lot more of like. Models actually cannot do that. And I think the most interesting thing is on the startup side, people don't yet know where a lot of the AI value is going to accrue.

**Alessio** [00:22:00] So you have this rush of people building frameworks, building infrastructure, layered things, but we don't really know the shape of the compute. I'm curious that Sierra, like how you thought about building an house, a lot of the tooling for evals or like just, you know, building the agents and all of that.

**Alessio** [00:22:00] Versus how you see some of the startup opportunities that is maybe still out there.

**Bret** [00:22:00] We build most of our tooling in house at Sierra, not all. It's, we don't, it's not like not invented here syndrome necessarily, though, maybe slightly guilty of that in some ways, but because we're trying to build a platform that's in Dorian, you know, we really want to have control over our own destiny.

**Bret** [00:23:00] And you had made a comment earlier that like. We're still trying to figure out who like the reactive agents are and the jury is still out. I would argue it hasn't been created yet. I don't think the jury is still out to go use that metaphor. We're sort of in the jQuery era of agents, not the react era.

**Bret** [00:23:00] And, and that's like a throwback for people listening,

**Swyx** [00:23:00] we shouldn't rush it. You know?

**Bret** [00:23:00] No, yeah, that's my point is. And so. Because we're trying to create an enduring company at Sierra that outlives us, you know, I'm not sure we want to like attach our cart to some like to a horse where it's not clear that like we've figured out and I actually want as a company, we're trying to enable just at a high level and I'll, I'll quickly go back to tech at Sierra, we help consumer brands build customer facing AI agents.

**Bret** [00:23:00] So. Everyone from Sonos to ADT home security to Sirius XM, you know, if you call them on the phone and AI will pick up with you, you know, chat with them on the Sirius XM homepage. It's an AI agent called Harmony that they've built on our platform. We're what are the contours of what it means for someone to build an end to end complete customer experience with AI with conversational AI.

**Bret** [00:24:00] You know, we really want to dive into the deep end of, of all the trade offs to do it. You know, where do you use fine tuning? Where do you string models together? You know, where do you use reasoning? Where do you use generation? How do you use reasoning? How do you express the guardrails of an agentic process?

**Bret** [00:24:00] How do you impose determinism on a fundamentally non deterministic technology? There's just a lot of really like as an important design space. And I could sit here and tell you, we have the best approach. Every entrepreneur will, you know. But I hope that in two years, we look back at our platform and laugh at how naive we were, because that's the pace of change broadly.

**Bret** [00:24:00] If you talk about like the startup opportunities, I'm not wholly skeptical of tools companies, but I'm fairly skeptical. There's always an exception for every role, but I believe that certainly there's a big market for frontier models, but largely for companies with huge CapEx budgets. So. Open AI and Microsoft's Anthropic and Amazon Web Services, Google Cloud XAI, which is very well capitalized now, but I think the, the idea that a company can make money sort of pre training a foundation model is probably not true.

**Bret** [00:25:00] It's hard to, you're competing with just, you know, unreasonably large CapEx budgets. And I just like the cloud infrastructure market, I think will be largely there. I also really believe in the applications of AI. And I define that not as like building agents or things like that. I define it much more as like, you're actually solving a problem for a business.

**Bret** [00:25:00] So it's what Harvey is doing in legal profession or what cursor is doing for software engineering or what we're doing for customer experience and customer service. The reason I believe in that is I do think that in the age of AI, what's really interesting about software is it can actually complete a task.

**Bret** [00:25:00] It can actually do a job, which is very different than the value proposition of software was to ancient history two years ago. And as a consequence, I think the way you build a solution and For a domain is very different than you would have before, which means that it's not obvious, like the incumbent incumbents have like a leg up, you know, necessarily, they certainly have some advantages, but there's just such a different form factor, you know, for providing a solution and it's just really valuable.

**Bret** [00:26:00] You know, it's. Like just think of how much money cursor is saving software engineering teams or the alternative, how much revenue it can produce tool making is really challenging. If you look at the cloud market, just as a analog, there are a lot of like interesting tools, companies, you know, Confluent, Monetized Kafka, Snowflake, Hortonworks, you know, there's a, there's a bunch of them.

**Bret** [00:26:00] A lot of them, you know, have that mix of sort of like like confluence or have the open source or open core or whatever you call it. I, I, I'm not an expert in this area. You know, I do think that developers are fickle. I think that in the tool space, I probably like. Default towards open source being like the area that will win.

**Bret** [00:27:00] It's hard to build a company around this and then you end up with companies sort of built around open source to that can work. Don't get me wrong, but I just think that it's nowadays the tools are changing so rapidly that I'm like, not totally skeptical of tool makers, but I just think that open source will broadly win, but I think that the CapEx required for building frontier models is such that it will go to a handful of big companies.

**Bret** [00:27:00] And then I really believe in agents for specific domains which I think will, it's sort of the analog to software as a service in this new era. You know, it's like, if you just think of the cloud. You can lease a server. It's just a low level primitive, or you can buy an app like you know, Shopify or whatever.

**Bret** [00:27:00] And most people building a storefront would prefer Shopify over hand rolling their e commerce storefront. I think the same thing will be true of AI. So I've. I tend to like, if I have a, like an entrepreneur asked me for advice, I'm like, you know, move up the stack as far as you can towards a customer need.

**Bret** [00:28:00] Broadly, but I, but it doesn't reduce my excitement about what is the reactive building agents kind of thing, just because it is, it is the right question to ask, but I think we'll probably play out probably an open source space more than anything else.

**Swyx** [00:28:00] Yeah, and it's not a priority for you. There's a lot in there.

**Swyx** [00:28:00] I'm kind of curious about your idea maze towards, there are many customer needs. You happen to identify customer experience as yours, but it could equally have been coding assistance or whatever. I think for some, I'm just kind of curious at the top down, how do you look at the world in terms of the potential problem space?

**Swyx** [00:28:00] Because there are many people out there who are very smart and pick the wrong problem.

**Bret** [00:28:00] Yeah, that's a great question.

## [00:28:48] Future of Software Development

**Bret** [00:28:00] By the way, I would love to talk about the future of software, too, because despite the fact it didn't pick coding, I have a lot of that, but I can talk to I can answer your question, though, you know I think when a technology is as cool as large language models.

**Bret** [00:29:00] You just see a lot of people starting from the technology and searching for a problem to solve. And I think it's why you see a lot of tools companies, because as a software engineer, you start building an app or a demo and you, you encounter some pain points. You're like,

**Swyx** [00:29:00] a lot of

**Bret** [00:29:00] people are experiencing the same pain point.

**Bret** [00:29:00] What if I make it? That it's just very incremental. And you know, I always like to use the metaphor, like you can sell coffee beans, roasted coffee beans. You can add some value. You took coffee beans and you roasted them and roasted coffee beans largely, you know, are priced relative to the cost of the beans.

**Bret** [00:29:00] Or you can sell a latte and a latte. Is rarely priced directly like as a percentage of coffee bean prices. In fact, if you buy a latte at the airport, it's a captive audience. So it's a really expensive latte. And there's just a lot that goes into like. How much does a latte cost? And I bring it up because there's a supply chain from growing coffee beans to roasting coffee beans to like, you know, you could make one at home or you could be in the airport and buy one and the margins of the company selling lattes in the airport is a lot higher than the, you know, people roasting the coffee beans and it's because you've actually solved a much more acute human problem in the airport.

**Bret** [00:30:00] And, and it's just worth a lot more to that person in that moment. It's kind of the way I think about technology too. It sounds funny to liken it to coffee beans, but you're selling tools on top of a large language model yet in some ways your market is big, but you're probably going to like be price compressed just because you're sort of a piece of infrastructure and then you have open source and all these other things competing with you naturally.

**Bret** [00:30:00] If you go and solve a really big business problem for somebody, that's actually like a meaningful business problem that AI facilitates, they will value it according to the value of that business problem. And so I actually feel like people should just stop. You're like, no, that's, that's unfair. If you're searching for an idea of people, I, I love people trying things, even if, I mean, most of the, a lot of the greatest ideas have been things no one believed in.

**Bret** [00:31:00] So I like, if you're passionate about something, go do it. Like who am I to say, yeah, a hundred percent. Or Gmail, like Paul as far, I mean I, some of it's Laura at this point, but like Gmail is Paul's own email for a long time. , and then I amusingly and Paul can't correct me, I'm pretty sure he sent her in a link and like the first comment was like, this is really neat.

**Bret** [00:31:00] It would be great. It was not your email, but my own . I don't know if it's a true story. I'm pretty sure it's, yeah, I've read that before. So scratch your own niche. Fine. Like it depends on what your goal is. If you wanna do like a venture backed company, if its a. Passion project, fucking passion, do it like don't listen to anybody.

**Bret** [00:31:00] In fact, but if you're trying to start, you know an enduring company, solve an important business problem. And I, and I do think that in the world of agents, the software industries has shifted where you're not just helping people more. People be more productive, but you're actually accomplishing tasks autonomously.

**Bret** [00:31:00] And as a consequence, I think the addressable market has just greatly expanded just because software can actually do things now and actually accomplish tasks and how much is coding autocomplete worth. A fair amount. How much is the eventual, I'm certain we'll have it, the software agent that actually writes the code and delivers it to you, that's worth a lot.

**Bret** [00:32:00] And so, you know, I would just maybe look up from the large language models and start thinking about the economy and, you know, think from first principles. I don't wanna get too far afield, but just think about which parts of the economy. We'll benefit most from this intelligence and which parts can absorb it most easily.

**Bret** [00:32:00] And what would an agent in this space look like? Who's the customer of it is the technology feasible. And I would just start with these business problems more. And I think, you know, the best companies tend to have great engineers who happen to have great insight into a market. And it's that last part that I think some people.

**Bret** [00:32:00] Whether or not they have, it's like people start so much in the technology, they lose the forest for the trees a little bit.

**Alessio** [00:33:00] How do you think about the model of still selling some sort of software versus selling more package labor? I feel like when people are selling the package labor, it's almost more stateless, you know, like it's easier to swap out if you're just putting an input and getting an output.

**Alessio** [00:33:00] If you think about coding, if there's no ID, you're just putting a prompt and getting back an app. It doesn't really matter. Who generates the app, you know, you have less of a buy in versus the platform you're building, I'm sure on the backend customers have to like put on their documentation and they have, you know, different workflows that they can tie in what's kind of like the line to draw there versus like going full where you're managed customer support team as a service outsource versus.

**Alessio** [00:33:00] This is the Sierra platform that you can build on. What was that decision? I'll sort of

**Bret** [00:33:00] like decouple the question in some ways, which is when you have something that's an agent, who is the person using it and what do they want to do with it? So let's just take your coding agent for a second. I will talk about Sierra as well.

**Bret** [00:33:00] Who's the customer of a, an agent that actually produces software? Is it a software engineering manager? Is it a software engineer? And it's there, you know, intern so to speak. I don't know. I mean, we'll figure this out over the next few years. Like what is that? And is it generating code that you then review?

**Bret** [00:34:00] Is it generating code with a set of unit tests that pass, what is the actual. For lack of a better word contract, like, how do you know that it did what you wanted it to do? And then I would say like the product and the pricing, the packaging model sort of emerged from that. And I don't think the world's figured out.

**Bret** [00:34:00] I think it'll be different for every agent. You know, in our customer base, we do what's called outcome based pricing. So essentially every time the AI agent. Solves the problem or saves a customer or whatever it might be. There's a pre negotiated rate for that. We do that. Cause it's, we think that that's sort of the correct way agents, you know, should be packaged.

**Bret** [00:34:00] I look back at the history of like cloud software and notably the introduction of the browser, which led to software being delivered in a browser, like Salesforce to. Famously invented sort of software as a service, which is both a technical delivery model through the browser, but also a business model, which is you subscribe to it rather than pay for a perpetual license.

**Bret** [00:35:00] Those two things are somewhat orthogonal, but not really. If you think about the idea of software running in a browser, that's hosted. Data center that you don't own, you sort of needed to change the business model because you don't, you can't really buy a perpetual license or something otherwise like, how do you afford making changes to it?

**Bret** [00:35:00] So it only worked when you were buying like a new version every year or whatever. So to some degree, but then the business model shift actually changed business as we know it, because now like. Things like Adobe Photoshop. Now you subscribe to rather than purchase. So it ended up where you had a technical shift and a business model shift that were very logically intertwined that actually the business model shift was turned out to be as significant as the technical as the shift.

**Bret** [00:35:00] And I think with agents, because they actually accomplish a job, I do think that it doesn't make sense to me that you'd pay for the privilege of like. Using the software like that coding agent, like if it writes really bad code, like fire it, you know, I don't know what the right metaphor is like you should pay for a job.

**Bret** [00:36:00] Well done in my opinion. I mean, that's how you pay your software engineers, right? And

**Swyx** [00:36:00] and well, not really. We paid to put them on salary and give them options and they vest over time. That's fair.

**Bret** [00:36:00] But my point is that you don't pay them for how many characters they write, which is sort of the token based, you know, whatever, like, There's a, that famous Apple story where we're like asking for a report of how many lines of code you wrote.

**Bret** [00:36:00] And one of the engineers showed up with like a negative number cause he had just like done a big refactoring. There was like a big F you to management who didn't understand how software is written. You know, my sense is like the traditional usage based or seat based thing. It's just going to look really antiquated.

**Bret** [00:36:00] Cause it's like asking your software engineer, how many lines of code did you write today? Like who cares? Like, cause absolutely no correlation. So my old view is I don't think it's be different in every category, but I do think that that is the, if an agent is doing a job, you should, I think it properly incentivizes the maker of that agent and the customer of, of your pain for the job well done.

**Bret** [00:37:00] It's not always perfect to measure. It's hard to measure engineering productivity, but you can, you should do something other than how many keys you typed, you know Talk about perverse incentives for AI, right? Like I can write really long functions to do the same thing, right? So broadly speaking, you know, I do think that we're going to see a change in business models of software towards outcomes.

**Bret** [00:37:00] And I think you'll see a change in delivery models too. And, and, you know, in our customer base you know, we empower our customers to really have their hands on the steering wheel of what the agent does they, they want and need that. But the role is different. You know, at a lot of our customers, the customer experience operations folks have renamed themselves the AI architects, which I think is really cool.

**Bret** [00:37:00] And, you know, it's like in the early days of the Internet, there's the role of the webmaster. And I don't know whether your webmaster is not a fashionable, you know, Term, nor is it a job anymore? I just, I don't know. Will they, our tech stand the test of time? Maybe, maybe not. But I do think that again, I like, you know, because everyone listening right now is a software engineer.

**Bret** [00:38:00] Like what is the form factor of a coding agent? And actually I'll, I'll take a breath. Cause actually I have a bunch of pins on them. Like I wrote a blog post right before Christmas, just on the future of software development. And one of the things that's interesting is like, if you look at the way I use cursor today, as an example, it's inside of.

**Bret** [00:38:00] A repackaged visual studio code environment. I sometimes use the sort of agentic parts of it, but it's largely, you know, I've sort of gotten a good routine of making it auto complete code in the way I want through tuning it properly when it actually can write. I do wonder what like the future of development environments will look like.

**Bret** [00:38:00] And to your point on what is a software product, I think it's going to change a lot in ways that will surprise us. But I always use, I use the metaphor in my blog post of, have you all driven around in a way, Mo around here? Yeah, everyone has. And there are these Jaguars, the really nice cars, but it's funny because it still has a steering wheel, even though there's no one sitting there and the steering wheels like turning and stuff clearly in the future.

**Bret** [00:39:00] If once we get to that, be more ubiquitous, like why have the steering wheel and also why have all the seats facing forward? Maybe just for car sickness. I don't know, but you could totally rearrange the car. I mean, so much of the car is oriented around the driver, so. It stands to reason to me that like, well, autonomous agents for software engineering run through visual studio code.

**Bret** [00:39:00] That seems a little bit silly because having a single source code file open one at a time is kind of a goofy form factor for when like the code isn't being written primarily by you, but it begs the question of what's your relationship with that agent. And I think the same is true in our industry of customer experience, which is like.

**Bret** [00:39:00] Who are the people managing this agent? What are the tools do they need? And they definitely need tools, but it's probably pretty different than the tools we had before. It's certainly different than training a contact center team. And as software engineers, I think that I would like to see particularly like on the passion project side or research side.

**Bret** [00:40:00] More innovation in programming languages. I think that we're bringing the cost of writing code down to zero. So the fact that we're still writing Python with AI cracks me up just cause it's like literally was designed to be ergonomic to write, not safe to run or fast to run. I would love to see more innovation and how we verify program correctness.

**Bret** [00:40:00] I studied for formal verification in college a little bit and. It's not very fashionable because it's really like tedious and slow and doesn't work very well. If a lot of code is being written by a machine, you know, one of the primary values we can provide is verifying that it actually does what we intend that it does.

**Bret** [00:40:00] I think there should be lots of interesting things in the software development life cycle, like how we think of testing and everything else, because. If you think about if we have to manually read every line of code that's coming out as machines, it will just rate limit how much the machines can do. The alternative is totally unsafe.

**Bret** [00:41:00] So I wouldn't want to put code in production that didn't go through proper code review and inspection. So my whole view is like, I actually think there's like an AI native I don't think the coding agents don't work well enough to do this yet, but once they do, what is sort of an AI native software development life cycle and how do you actually.

**Bret** [00:41:00] Enable the creators of software to produce the highest quality, most robust, fastest software and know that it's correct. And I think that's an incredible opportunity. I mean, how much C code can we rewrite and rust and make it safe so that there's fewer security vulnerabilities. Can we like have more efficient, safer code than ever before?

**Bret** [00:41:00] And can you have someone who's like that guy in the matrix, you know, like staring at the little green things, like where could you have an operator of a code generating machine be like superhuman? I think that's a cool vision. And I think too many people are focused on like. Autocomplete, you know, right now, I'm not, I'm not even, I'm guilty as charged.

**Bret** [00:42:00] I guess in some ways, but I just like, I'd like to see some bolder ideas. And that's why when you were joking, you know, talking about what's the react of whatever, I think we're clearly in a local maximum, you know, metaphor, like sort of conceptual local maximum, obviously it's moving really fast. I think we're moving out of it.

**Alessio** [00:42:00] Yeah. At the end of 23, I've read this blog post from syntax to semantics. Like if you think about Python. It's taking C and making it more semantic and LLMs are like the ultimate semantic program, right? You can just talk to them and they can generate any type of syntax from your language. But again, the languages that they have to use were made for us, not for them.

**Alessio** [00:42:00] But the problem is like, as long as you will ever need a human to intervene, you cannot change the language under it. You know what I mean? So I'm curious at what point of automation we'll need to get, we're going to be okay making changes. To the underlying languages, like the programming languages versus just saying, Hey, you just got to write Python because I understand Python and I'm more important at the end of the day than the model.

**Alessio** [00:43:00] But I think that will change, but I don't know if it's like two years or five years. I think it's more nuanced actually.

**Bret** [00:43:00] So I think there's a, some of the more interesting programming languages bring semantics into syntax. So let me, that's a little reductive, but like Rust as an example, Rust is memory safe.

**Bret** [00:43:00] Statically, and that was a really interesting conceptual, but it's why it's hard to write rust. It's why most people write python instead of rust. I think rust programs are safer and faster than python, probably slower to compile. But like broadly speaking, like given the option, if you didn't have to care about the labor that went into it.

**Bret** [00:43:00] You should prefer a program written in Rust over a program written in Python, just because it will run more efficiently. It's almost certainly safer, et cetera, et cetera, depending on how you define safe, but most people don't write Rust because it's kind of a pain in the ass. And the audience of people who can is smaller, but it's sort of better in most, most ways.

**Bret** [00:44:00] And again, let's say you're making a web service and you didn't have to care about how hard it was to write. If you just got the output of the web service, the rest one would be cheaper to operate. It's certainly cheaper and probably more correct just because there's so much in the static analysis implied by the rest programming language that it probably will have fewer runtime errors and things like that as well.

**Bret** [00:44:00] So I just give that as an example, because so rust, at least my understanding that came out of the Mozilla team, because. There's lots of security vulnerabilities in the browser and it needs to be really fast. They said, okay, we want to put more of a burden at the authorship time to have fewer issues at runtime.

**Bret** [00:44:00] And we need the constraint that it has to be done statically because browsers need to be really fast. My sense is if you just think about like the, the needs of a programming language today, where the role of a software engineer is to use an AI to generate functionality and audit that it does in fact work as intended, maybe functionally, maybe from like a correctness standpoint, some combination thereof, how would you create a programming system that facilitated that?

**Bret** [00:45:00] And, you know, I bring up Rust is because I think it's a good example of like, I think given a choice of writing in C or Rust, you should choose Rust today. I think most people would say that, even C aficionados, just because. C is largely less safe for very similar, you know, trade offs, you know, for the, the system and now with AI, it's like, okay, well, that just changes the game on writing these things.

**Bret** [00:45:00] And so like, I just wonder if a combination of programming languages that are more structurally oriented towards the values that we need from an AI generated program, verifiable correctness and all of that. If it's tedious to produce for a person, that maybe doesn't matter. But one thing, like if I asked you, is this rest program memory safe?

**Bret** [00:45:00] You wouldn't have to read it, you just have to compile it. So that's interesting. I mean, that's like an, that's one example of a very modest form of formal verification. So I bring that up because I do think you have AI inspect AI, you can have AI reviewed. Do AI code reviews. It would disappoint me if the best we could get was AI reviewing Python and having scaled a few very large.

**Bret** [00:46:00] Websites that were written on Python. It's just like, you know, expensive and it's like every, trust me, every team who's written a big web service in Python has experimented with like Pi Pi and all these things just to make it slightly more efficient than it naturally is. You don't really have true multi threading anyway.

**Bret** [00:46:00] It's just like clearly that you do it just because it's convenient to write. And I just feel like we're, I don't want to say it's insane. I just mean. I do think we're at a local maximum. And I would hope that we create a programming system, a combination of programming languages, formal verification, testing, automated code reviews, where you can use AI to generate software in a high scale way and trust it.

**Bret** [00:46:00] And you're not limited by your ability to read it necessarily. I don't know exactly what form that would take, but I feel like that would be a pretty cool world to live in.

**Alessio** [00:47:00] Yeah. We had Chris Lanner on the podcast. He's doing great work with modular. I mean, I love. LVM. Yeah. Basically merging rust in and Python.

**Alessio** [00:47:00] That's kind of the idea. Should be, but I'm curious is like, for them a big use case was like making it compatible with Python, same APIs so that Python developers could use it. Yeah. And so I, I wonder at what point, well, yeah.

**Bret** [00:47:00] At least my understanding is they're targeting the data science Yeah. Machine learning crowd, which is all written in Python, so still feels like a local maximum.

**Bret** [00:47:00] Yeah.

**Swyx** [00:47:00] Yeah, exactly. I'll force you to make a prediction. You know, Python's roughly 30 years old. In 30 years from now, is Rust going to be bigger than Python?

**Bret** [00:47:00] I don't know this, but just, I don't even know this is a prediction. I just am sort of like saying stuff I hope is true. I would like to see an AI native programming language and programming system, and I use language because I'm not sure language is even the right thing, but I hope in 30 years, there's an AI native way we make software that is wholly uncorrelated with the current set of programming languages.

**Bret** [00:48:00] or not uncorrelated, but I think most programming languages today were designed to be efficiently authored by people and some have different trade offs.

## [00:48:15] Evolution of Programming Languages

**Bret** [00:48:00] You know, you have Haskell and others that were designed for abstractions for parallelism and things like that. You have programming languages like Python, which are designed to be very easily written, sort of like Perl and Python lineage, which is why data scientists use it.

**Bret** [00:48:00] It's it can, it has a. Interactive mode, things like that. And I love, I'm a huge Python fan. So despite all my Python trash talk, a huge Python fan wrote at least two of my three companies were exclusively written in Python and then C came out of the birth of Unix and it wasn't the first, but certainly the most prominent first step after assembly language, right?

**Bret** [00:48:00] Where you had higher level abstractions rather than and going beyond go to, to like abstractions, like the for loop and the while loop.

## [00:49:01] The Future of Software Engineering

**Bret** [00:49:00] So I just think that if the act of writing code is no longer a meaningful human exercise, maybe it will be, I don't know. I'm just saying it sort of feels like maybe it's one of those parts of history that just will sort of like go away, but there's still the role of this offer engineer, like the person actually building the system.

**Bret** [00:49:00] Right. And. What does a programming system for that form factor look like?

## [00:49:25] React and Front-End Development

**Bret** [00:49:00] And I, I just have a, I hope to be just like I mentioned, I remember I was at Facebook in the very early days when, when, what is now react was being created. And I remember when the, it was like released open source I had left by that time and I was just like, this is so fucking cool.

**Bret** [00:49:00] Like, you know, to basically model your app independent of the data flowing through it, just made everything easier. And then now. You know, I can create, like there's a lot of the front end software gym play is like a little chaotic for me, to be honest with you. It is like, it's sort of like abstraction soup right now for me, but like some of those core ideas felt really ergonomic.

**Bret** [00:50:00] I just wanna, I'm just looking forward to the day when someone comes up with a programming system that feels both really like an aha moment, but completely foreign to me at the same time. Because they created it with sort of like from first principles recognizing that like. Authoring code in an editor is maybe not like the primary like reason why a programming system exists anymore.

**Bret** [00:50:00] And I think that's like, that would be a very exciting day for me.

## [00:50:28] The Role of AI in Programming

**Swyx** [00:50:00] Yeah, I would say like the various versions of this discussion have happened at the end of the day, you still need to precisely communicate what you want. As a manager of people, as someone who has done many, many legal contracts, you know how hard that is.

**Swyx** [00:50:00] And then now we have to talk to machines doing that and AIs interpreting what we mean and reading our minds effectively. I don't know how to get across that barrier of translating human intent to instructions. And yes, it can be more declarative, but I don't know if it'll ever Crossover from being a programming language to something more than that.

**Bret** [00:51:00] I agree with you. And I actually do think if you look at like a legal contract, you know, the imprecision of the English language, it's like a flaw in the system. How many

**Swyx** [00:51:00] holes there are.

**Bret** [00:51:00] And I do think that when you're making a mission critical software system, I don't think it should be English language prompts.

**Bret** [00:51:00] I think that is silly because you want the precision of a a programming language. My point was less about that and more about if the actual act of authoring it, like if you.

## [00:51:32] Formal Verification in Software

**Bret** [00:51:00] I'll think of some embedded systems do use formal verification. I know it's very common in like security protocols now so that you can, because the importance of correctness is so great.

**Bret** [00:51:00] My intellectual exercise is like, why not do that for all software? I mean, probably that's silly just literally to do what we literally do for. These low level security protocols, but the only reason we don't is because it's hard and tedious and hard and tedious are no longer factors. So, like, if I could, I mean, just think of, like, the silliest app on your phone right now, the idea that that app should be, like, formally verified for its correctness feels laughable right now because, like, God, why would you spend the time on it?

**Bret** [00:52:00] But if it's zero costs, like, yeah, I guess so. I mean, it never crashed. That's probably good. You know, why not? I just want to, like, set our bars really high. Like. We should make, software has been amazing. Like there's a Mark Andreessen blog post, software is eating the world. And you know, our whole life is, is mediated digitally.

**Bret** [00:52:00] And that's just increasing with AI. And now we'll have our personal agents talking to the agents on the CRO platform and it's agents all the way down, you know, our core infrastructure is running on these digital systems. We now have like, and we've had a shortage of software developers for my entire life.

**Bret** [00:52:00] And as a consequence, you know if you look, remember like health care, got healthcare. gov that fiasco security vulnerabilities leading to state actors getting access to critical infrastructure. I'm like. We now have like created this like amazing system that can like, we can fix this, you know, and I, I just want to, I'm both excited about the productivity gains in the economy, but I just think as software engineers, we should be bolder.

**Bret** [00:53:00] Like we should have aspirations to fix these systems so that like in general, as you said, as precise as we want to be in the specification of the system. We can make it work correctly now, and I'm being a little bit hand wavy, and I think we need some systems. I think that's where we should set the bar, especially when so much of our life depends on this critical digital infrastructure.

**Bret** [00:53:00] So I'm I'm just like super optimistic about it. But actually, let's go to what you said for a second, which is correct.

## [00:53:33] The Importance of Specifications

**Bret** [00:53:00] Specifications. I think this is the most interesting part of A. I. Agents broadly, which is that most specifications are incomplete. So let's go back to our product engineering discussions.

**Bret** [00:53:00] You're like, okay, here's a P. R. D. Product requirements document and there's it's really detailed mockups and this like when you click this button, it does this and it's like 100 percent you can think of a missing requirement that document. Let's say you click this button And the internet goes out, what do you do?

**Bret** [00:54:00] I don't know if that's in the PRD. It probably isn't, you know, there's, there's always going to be something because like humans are complicated. Right. So what ends up happening is like, I don't know if you can measure it, like what percentage of a product's actual functionality is determined by its code versus the specification, like for a traditional product, Oh, 95%.

**Bret** [00:54:00] I mean, a little bit, but a lot of it. So like. Code is the specification.

## [00:54:29] Open Source and Implicit Standards

**Bret** [00:54:00] It's actually why if you just look at the history of technology, why open source has won out over specifications, like, you know, for a long time, there was a W3C working group on the HTML specification and then, you know, once web kit became prevalent.

**Bret** [00:54:00] The internet evolved a lot faster and it's not the expense of the standards organizations. It just turns out having a committee of people argue is like a lot less efficient than someone checking in code and then all of a sudden you had vector graphics and you had like all this really cool stuff that, you know, someone who, in the Google maps days, a guy like, God, that would have made my life easier.

**Bret** [00:55:00] You know, it's like. SVG support, life would have been a breeze. Try drawing a driving directions line without vector graphics. And so, you know, in general, I think we've gone from these protocols defined in a document to basically open source code that becomes an implicit standard, like systems calls and Linux, like.

**Bret** [00:55:00] There is a specification. There is post X as a standard, but like the Colonel is the like, that's what people write against and it's both the documented behavior and all of the undocumented behaviors as well for better for worse. And it's why, you know, Linus and others are so adamant about things like binary compatibility and all that, like this stuff matters.

**Bret** [00:55:00] So one of the things that I really think about is like working with agents broadly is how do you, it's. I don't want to say it's easy to specify the guardrails, you know, but what about all those unspecified behaviors? So so much of like being a software engineer is like, you come to the point where you're like the internet's out and you get back the error code from the call and you got to do something with it.

**Bret** [00:56:00] And you know, what percent of the time do you just be like. Yeah, I'm going to do this because it seems reasonable. And what percentage of time do you like write a slack to your PM and be like, what do I do in this case? It's probably more the former than the latter. Otherwise it'd be really fricking inefficient to write software.

## [00:56:27] AI Agents and Decision Making

**Bret** [00:56:00] But what happens when your AI makes that decision for you? It's not a wrong decision. You didn't say anything about that case. The AI agent, the word agent comes from the word agency, right? So it's demonstrating its agency and it's making a decision. Does it document it? That would probably be tedious to like, because there's so many implicit decisions.

**Bret** [00:56:00] What happens when you click the button and the internet's out? It does something you don't like. How do you fix it? I actually think that we are like entering this new world where like the, how we express to an AI agent, what we want is always going to be an incomplete specification, and that's why agents are useful because they can fill in the gaps with some decent amount of reasoning.

**Bret** [00:57:00] How you actually tune these over time. And imagine like building an app with an AI agent as your software engineering companion, there's like an infinitely long tail. Infinite is probably over exaggerating a bit, but there's a fairly long tail of functionality that I guarantee is not specified how you actually tune that.

**Bret** [00:57:00] And this is what I mean about creating a programming system. I don't think we know what that system is yet. And then similarly, I actually think for every single agentic domain, whether it's customer service or legal or software engineering, that's essentially what the company building those agents is building is like the system through which you express the behaviors you want, esoteric and small as it might be anyway, I think that's a really exciting area though, just because I think that's where the magic or that's where the product insights will be in the space is like, how do you encounter that those moments?

**Bret** [00:57:00] It's kind of built into the UX

**Swyx** [00:57:00] and it can't just be, the answer can't just be prompt better, you know? No, no, it's impossible.

**Bret** [00:58:00] The prompt would be too long. Like, imagine getting a PRD that literally specified the behavior of everything that was represented by code. The answer would just be code. Like at that point.

**Bret** [00:58:00] So here's my point, like prompts are great, but it's not actually a complete specification for anything. It never can be. And so, and I think that's. How you do interactivity, like the sort of human in a loop thing, when and how you do it. And that's why I really believe in, in domain specific agents, because I think answering that in the abstract is like a interesting intellectual exercise.

**Bret** [00:58:00] But I, that's why I like talking about agents in the abstract kind of, I'm actively disinterested in it because I don't think it actually means anything. All it means is software is making decisions. That's what, you know, at least in a reductive way. But in the context of software engineering, it does make sense.

**Bret** [00:58:00] Cause you know, like what is the process of first you specify what you want in a product, then you use it, then you give feedback. You can imagine building a product that actually facilitated that closed loop system. And then how is that represented that complete specification of both what you knew you wanted, what you discovered through usage, the union of all of that is what you care about, and the rest is less to the AI.

**Bret** [00:59:00] In the legal context, I'm certain there's a way to know, like, when should the AI ask questions? When shouldn't it? How do you actually intervene when it's wrong? And certainly in the customer service case, it's very clear, you know, and how, like how we, our customers review every conversation, how we. Help them find the conversations they should review when they're having millions so they can find the few that are interesting how when something is wrong in one of those conversations, how they can give feedback.

**Bret** [00:59:00] So it's fixed the next time in a way where we know the context of why I made that decision. But it's not up to us what's right, right? It's up to our customers. So that's why I actually think for right, you know, right now when you think about building an agent and domain to some degree, how you actually interact with the people specifies behavior is actually where a lot of the magic is.

**Swyx** [01:00:00] Stop me if this is a little bit annoying to you, but I have a bit of a trouble squaring. domain specific agents with the belief that AGI is real, or AGI is coming, because the point is general intelligence. And some part, some way, one way to view the bitter lesson is we can always make progress on being more domain specific.

**Swyx** [01:00:00] Take whatever SOTA is, and you make progress being more domain specific, and then you will be wiped out. The next advance happens. Clearly, you don't believe in that, but how do you personally square those things?

**Bret** [01:00:00] Yeah, it's a really heavy question.

## [01:00:36] The Impact of AGI on Industries

**Bret** [01:00:00] And you know, I think a lot about AGI given my role at open AI but it's even hard for me to really conceptualize.

**Bret** [01:00:00] And I love spending time with open AI researchers and actually just like people in the community broadly just talking about the implications because there's the first order of fact and I effects of something that is super intelligent in some domains. And then there's the second and third order effects are harder to predict.

**Bret** [01:00:00] So first as I think that. It seems likely to me that, you know, at first and something that is AGI will be good in digital domains. You know, because it's software. So if you think about something like AI discovering a new say like pharmaceutical therapy, the barrier to that is probably less the discovery than the clinical trial.

**Bret** [01:01:00] And, and AI doesn't necessarily help with a clinical trial, right? That's a process that's. Independent of intelligence and it's, it's a physical process. Similarly, if you think about the problem of climate change or like carbon removal, there's probably a lot of that domain that requires great ideas, but like whatever great idea you came up with, if you wanted to sequester that much carbon, there's probably a big physical component to that.

**Bret** [01:01:00] So it's not really limited by intelligence. It might be, I'm sure it could be accelerated somewhat by intelligence. There's a really interesting conversation with an economist named Tyler Cohen, California. And recently he just, I just watched a video of him and he was just talking about how there's parts of the economy where intelligence is sort of the limited resource that will take on AI slash AGI really rapidly and will drive incredible productivity gains.

**Bret** [01:02:00] But there are other parts of the economy that aren't and those will interact. It goes back to these complex second artifacts like prices will go up in the domains that can absorb absorb intelligence rapidly, which will actually then slow down, you know, so it's going to, I don't think it'll be evenly spread.

**Bret** [01:02:00] I don't think it would be perhaps as rapidly felt in all parts of the economy as people think I might be wrong, but I just think you can generalize in terms of its ability to. Reason about different domains, which I think is what AGI means to most people, but it may not actually. Generalized in the world and tell, because there's a lot of intelligence is not the limiting factor and like a lot of the economy.

**Bret** [01:02:00] So going back to your, your more practical question is like, why make software at all of, you know, AGI is coming and say it that way. Should we learn to

**Swyx** [01:03:00] code?

**Bret** [01:03:00] There's all variations of this. You know, my view is that I really do view AI as a tool and AGI as a tool for humanity. And so my view is when we were talking about like.

**Bret** [01:03:00] Is your job as a maker of software to author a code in an editor? I would argue no just like a generation ago. Your job wasn't to punch cards in a punch card That is not what your job is. Your job is to produce digital something, whatever it is, what is the purpose of the software that you're making?

**Bret** [01:03:00] Your job is to produce that. And so I think that like our jobs will change rapidly and meaningfully, but I think the idea that like our job is to type in a. And an editor is, is an artifact of the tools that we have, not actually what we're hired to do, which is to produce a digital experience, to, you know, make firmware for a toaster or whatever, whatever it is we're doing.

**Bret** [01:04:00] Right. Like that's our job. Right. And. As a consequence, I think with things like AGI, I think the certainly software engineering will be one of the disciplines most impacted. And I think that it's very, so like, I think if you're in this industry and you define yourself by the tools that you use, like how many characters you can type into them every day, that's probably not like a long term stable place to be, because that's something that certainly AI can do better than you.

**Bret** [01:04:00] But your judgment about what to build and how to build it still apply. And that will always be true. And one way to think about it's like a little bit reductive is like, you know, look at startups versus larger companies. Like companies like Google and Amazon have so many more engineers than a startup, but then some startups still win.

**Bret** [01:04:00] Like, why was that? Well, they made better decisions, right? They didn't type faster or produce more code. They did the right thing in the right market, the right time. And, and similarly. If you look at some of the great companies, it wasn't the lack of they had some unique idea. Sometimes that's a reason why a company succeeds, but it's often a lot of other things and a lot of other forms of execution.

**Bret** [01:05:00] So like broadly, like the existence of a lot of intelligence will change a lot and it'll change our jobs more than any other industry, or maybe not, maybe it's exaggerated, but certainly as much as any other industry. But I don't think it like changes, like why the economy around digital technology exists.

**Bret** [01:05:00] And as a consequence, I think I'm really bullish on like the future of, of the software industry. I just think that like some things that are really expensive today will become almost free. And but I think that, I mean, let's be honest, the half life of technology companies is not particularly long as it is.

**Bret** [01:05:00] Yeah, I, I brought this anecdote in a recent conversation, but When I started at Google, we were in one building in Mountain View and then eventually moved into a campus, which was previously the Silicon Graphics campus. That was the first campus Google, I'm pretty sure it still has that campus. I think it's got a billion now.

**Bret** [01:06:00] SGI was a company that was like really, really big, big enough to have a campus and then went out of business. And it wasn't that old of a company, by the way, it's not like IBM, you know, it was like. Big enough to get a campus and go to business in my lifetime, you know, that type of thing. And then at Facebook, we had an office in pallets.

**Bret** [01:06:00] I moved, I didn't go into the original office when I joined. It was the second office, this old HP building near Stanford. And then we got big enough to want to campus and we bought some microsystems campus. Sun Microsystem famously came out of Stanford, went high flying, was one of the. com darlings, and then eventually sort of like bought for pennies on the dollar by Oracle.

**Bret** [01:06:00] And you know, like all those companies, like in my lifetime were big enough to like go public, have a campus and then go out of business. So I think a lot will change. I don't mean to say this is going to be easy or like no one's business model is under threat, but. Will digital technology remain important?

**Bret** [01:06:00] Will entrepreneurs having good judgment about where to apply this technology to create something of economic value still apply like a hundred percent. And I've always used the metaphor, like if you went back to 1980 and describe many of the jobs that we have, it would be hard for people to conceptualize.

**Bret** [01:07:00] Like imagine. I'm a podcaster. You're like, what the hell does that mean? Imagine going back to like 1776 and describing to Ben Franklin, our economy today, like let alone the technology industry, just the services economy. It would be probably hard for him to conceptualize just like who grows the food, just because the idea that so few people in this country are necessary to produce the food for so many people would defy.

**Bret** [01:07:00] So much of his conception of just like how food is grown, that it would just be like, it would probably take a couple hours of explaining. It's kind of like the same thing. It's like we, we have a view of like how this world works right now. That's based on just the constraints that exist, but there's gonna be a lot of other opportunities and other things like that.

**Bret** [01:07:00] So I don't know. I mean, it's certainly writing code is really valuable right now and it probably will change rapidly. I think people just need a lot of agility. I always use the metaphor where like a bunch of accountants and Microsoft Excel was just invented. Are you going to be the first person who sets down your HP calculator and says, I'm going to learn how to use this tool because it's just a better way of doing what I'm already doing.

**Bret** [01:08:00] Or are you going to be the one who's like, you know, begrudgingly pulling out their slide rule and HP calculator and saying these kids these days, you know, their Excel, they don't understand, you know, it's been a little bit reductive, but I just feel like the, the probably the best thing all of us can do, not just in software industry, but I do think it's really.

**Bret** [01:08:00] Kind of interesting just reflection that we're disrupting our own industry as much as anything else with this technology is to lean into the change, try the tools, like install the latest coding assistance, you know, when Oh three mini comes out, write some code with it that you don't want to be the last accountant to embrace Excel.

**Bret** [01:08:00] You might not have your job anymore, so.

**Swyx** [01:08:00] We have some personal questions on like how you keep up with AI and you know, all that, all the other stuff. But I also want to, and I'll let you get to your question. I just wanted to say that the analogy that you made on food was really interesting and resonated with me.

**Swyx** [01:09:00] I feel like we are kind of in like an agrarian economy of like a barter economy for intelligence and now we're sort of industrializing intelligence. And I, that really just was an aha

**Alessio** [01:09:00] moment for me. I just wanted to reflect that. Yeah. How do you think about. The person being replaced by an agent and how agents talk to each other.

**Alessio** [01:09:00] So even at Sierra today, right, you're building agents that people talk to, but in the future, you're going to have agents that are going to complain about the order they placed to the customer support agents all the way down. Exactly. And you know, you were the CTO of Facebook, you built OpenGraph there.

**Alessio** [01:09:00] And I think there were a lot of pros, things that were being enabled, then maybe a lot of cons that came out of that. How do you think about how the agent protocols should be built, thinking about all the implications of it, you know, privacy, data, discoverability and all that?

**Bret** [01:09:00] Yeah, I think it's a little early for a protocol to emerge.

**Bret** [01:10:00] I've read about a few of the attempts and maybe some of them will catch on. One of the things that's really interesting about large language models is because they're trained on language as they are very capable of using the interfaces built for us. And so. My intuition right now is that because we can make an interface that works for us and also works for the AI, maybe that's good enough.

**Bret** [01:10:00] You know, I mean, a little bit hand wavy here, but making a machine protocol for agents that's inaccessible to people, there's some upsides to it, but there's also quite a bit of downside to it as well. I think it was Andrej Karpathy, but I can't remember. But like one of the more well known AI researchers wrote, like I spent half my day writing English, you know, in my software engineering I have an intuition that agents will speak to agents using language for a while.

**Bret** [01:10:00] I don't know if that's true. But there's a lot of reasons why there, that may be true. And so, you know, when. Your personal agent speaks to a Sierra agent to help figure out why your Sonos speaker has the flashing orange light. My intuition is it will be in English for a while. And I think there's a lot of, like, benefits to that.

**Bret** [01:11:00] I do think that we still are in the early days of Like long running agents I don't know if you tried the deep research agent that just came up,

**Swyx** [01:11:00] we have one for you. Oh, that's great.

**Bret** [01:11:00] It was interesting cause it was probably the first time I really got like notified by open AI when something was done and I brought up before the interactive parts of it.

**Bret** [01:11:00] That's the area that I'm most interested in right now. It just is like most agentic workflows are relatively short running and. The workflows that are multi stakeholder, long running and multi system we deal with a lot of those and, and at Sierra, but broadly speaking, I think that those are interesting just because I, I always use the metaphor that prior to the mobile phone, every time you got like a notification from some internet service, you get an email, not because email was like the best way to notify you, but it's the only way.

**Bret** [01:12:00] And so you know, you used to get tagged on a photo in Facebook and you get an email about it. Then once. This was in everyone's pocket. Every app had equal access to buzzing your pocket. And now, you know, for most of the apps I use, I don't get email notifications. I just get, get it directly from the app.

**Bret** [01:12:00] I sort of wonder what the form factors will be for agents. How do you address and reach out to other agents? And then how does it bring you the, the operator of the agent into the loop at the right time? You know, I certainly think there's companies like, you know, with chat GPT, that will be one of the major consumer surfaces.

**Bret** [01:12:00] So there's like, there's a lot of like gravity to those services. But then if I think about sort of domain specific workflows as well, I think there's just a lot to figure out there. So I'm less. The agent agent protocols. I actually think I could be wrong. I just haven't thought about a lot. Like it's sort of interesting, but actually just how it engages with all the people in it is actually one of the things I'm most interested to sort of see how it plays out as well.

**Alessio** [01:13:00] Yeah. I think to me, the things that are at the core of it is kind of like our back, you know, it's like, can this agent access this thing? I think in the customer support use cases, maybe less prominent, but like in the enterprises is more interesting. And also like language, like you can compress the language.

**Alessio** [01:13:00] If the human didn't have to read it, you can kind of save tokens, make things faster. So yeah, you mentioned being notified about deep research. Is there a open AI deep research has been achieved internally notification that goes out to everybody and the board gets summoned and you get to see it. Can you give any backstory on that process?

**Bret** [01:13:00] OpenAI is a mission driven nonprofit that I think of primarily as a research lab. It's obviously more than that, you know, in some ways like chat GPT is a cultural defining product. But at the end of the day, the mission is to ensure that artificial general intelligence benefits all of humanity. So a lot of our board discussions are about.

**Bret** [01:14:00] Research and its implications on humanity, which is primarily safety. Obviously, I think the one cannot achieve AGI and not think about safety as a primary responsibility for that mission, but it's also access and other things. So things like deep research, we definitely talk about because it's a big part of, if you think about what does it mean to build AGI, but we talk about a lot of different things, you know, so it's like Sometimes we hear about things super early.

**Bret** [01:14:00] Sometimes if it's not really related, if it's sort of far afield from the core of the mission, you know, it's like more casual. So it's pretty fun, fun to be a part of that just because it's my favorite part of every board discussion is just hearing from the researchers about. How they're thinking about the future and just like the next, next milestone and creating AGI.

**Swyx** [01:14:00] Well, lots of milestones. Maybe we'll just start at the beginning. Like, you know, there are very few people that have been in the rooms that you've been in. How do these conversations start? How do you get brought into opening? I obviously there's, there's a bit of drama that you can go into if you want.

**Swyx** [01:14:00] Just take us into the room. Like what happens? What is it like?

**Bret** [01:15:00] Was it a. Thursday or Friday when Friday was fired. Yeah. So I heard about it like everyone else, you know, just like saw it on, on social media. And I remember

**Swyx** [01:15:00] where I was walking here and I was

**Bret** [01:15:00] totally shocked and messaged my co founder clay.

**Bret** [01:15:00] And I was like, gosh, I wonder what happened. And then. On Saturday, trying to just protect sort of like people's privacy on this. But I ended up talking to both Adam D'Angelo and Sam Altman and basically getting a kind of synopsis of what was going on and my understanding that you could, you'd have to ask them for sort of their perspective on this was just basically like they, both the board and Sam both felt some trust in me.

**Bret** [01:15:00] And it was a very complicated situation because the, the company was reacted pretty negatively, understandably negatively to Sam's being fired. I don't think they really understood what was going on. And so the board was, you know, in a situation where they needed to sort of figure out a path forward and they reached out to me and then I talked to Sam and basically ended up kind of the mediator for lack of a better word, not really formally that, but fundamentally that.

**Bret** [01:16:00] And as the board was trying to figure out a path forward, you know, we, we ended up with a lot of discussions with like how to reinstate Sam is a CEO of the company, but also do a review of what happens so that the board's concerns could be fully sort of adjudicated, you know because they obviously did have concerns going into it.

**Bret** [01:16:00] So it ended up there. So I think broadly speaking, I was just like a known, like a lot of the stakeholders in it knew of me and, and I'd like to think I have some integrity, so it was just sort of like, you know, they were trying to find a way out of a very complex situation. So I ended up kind of meeting in that and have formed a.

**Bret** [01:16:00] A really great relationship with Sam and Greg and pretty challenging time for the company didn't plan to be, you know, on the board. I got pulled in because of the crisis that happened. And I don't think I'll be on the board forever either. I, I posted when I joined that I was going to do it temporarily.

**Bret** [01:17:00] That was like a year ago. You know, I really like to focus on Sierra, but I also really care about, it's just an amazing mission. So

## [01:17:15] Navigating High-Stakes Situations

**Swyx** [01:17:00] I've been maybe been in like high stakes situations like that, like twice, but obviously not as high stakes, but like, what principles do you have? When you know, like, this is the highest egos, highest amount of stakes possible, highest amount of money, whatever.

**Swyx** [01:17:00] What principles do you have to go into something like this? Like, obviously you have a great reputation, you have a great network. What are your must do's and what are your must not do's?

**Bret** [01:17:00] I'm not sure there's a If there were a playbook for these situations, there'd be a lot simpler. You know, I just probably go back to like the way I operate in general.

**Bret** [01:17:00] One is first principles thinking. So I, I do think that there's crisis playbooks, but there was nothing quite like this and you really need to understand what's going on and why. I think a lot of. Moments of crisis are fundamentally human problems. You can strategize about people's incentives and this and that and the other thing, but I think it's really important to understand all the people involved and what motivates them and why, which is fundamentally an exercise in empathy.

**Bret** [01:18:00] Actually. Like, do you really understand. Why people are doing what they're doing and then getting good advice, you know, and I think people What's interesting about a high profile crisis is everyone wants to give you advice So there's no shortage of advice, but the good advice is the one I think that really involves judgment Which is who are people based on first principles analysis of the situation based on your assessment?

**Bret** [01:18:00] Of what, you know, all the people involved who would have true expertise and good judgment, you know, in these situations so that you can either validate your judgment if you have an intuition or if it's an area that's like a area of like, say, a legal expertise that you're not expert and you want the best in the world to give you advice.

**Bret** [01:19:00] And I actually find people often seek out. The wrong people for advice and it's really important in those circumstances.

**Swyx** [01:19:00] Well, I mean, it's super well navigated. I have, I've got one more and then we can sort of move on on this topic. The the, the Microsoft offer was real, right? For Sam and team to move over at some, at one point in that weekend.

**Bret** [01:19:00] I'm not sure. I was sort of in it from one vantage point, which was actually, it's interesting. It's like, I didn't really have. Particular skin in the game. So like I came up with this, I still don't own any equity in open AI. I was just I was just a meaningful bystander in the process. And the reason I got involved and and it will get to answer your question, but the reason I got involved was just because I cared about open AI.

**Bret** [01:19:00] So. You know, I had left my job at Salesforce and by coincidence, the next month chat GBT comes out and, you know, I got nerd sniped like everyone else. I'm like, I want to spend my life on this. This is so amazing. And I wouldn't, I don't know if I'd be, I wouldn't, I'm not sure I would have started another company if not for open AI, kind of inspiring the world with chat GPT, maybe I would have, I don't know, but it was like, it had a very significant impact on you, all of us, I think.

**Bret** [01:20:00] So the idea that it would dissolve in a weekend just like bothered me a lot. And I'm very, like, I'm very grateful for, for open AI's existence. And, and I, my guess is that is probably shared by a lot of the competing research labs to different degrees too. It's just like it kind of that rising tide lifted all boats.

**Bret** [01:20:00] Like I think it created the proverbial iPhone moment for AI and, and changed, changed the world. So there were lots of. Microsoft is an investor in open AI. It has a vested interest in it. The Sam and Greg had their interests. The employees had their interests and there's lots of wheeling and dealing.

**Bret** [01:20:00] And I, you know, you can't AB test decision making. So I don't know if like things had fallen apart with that. I don't, I don't actually know. And you also don't know, like what's real, what's not. I mean, so you'd have to talk to, to them to know it was really real. So.

**Swyx** [01:21:00] Mentioning advisors. I heard it seems like Brian Armstrong was.

**Swyx** [01:21:00] surprisingly strong advisor on during, during the whole journey, which is

**Bret** [01:21:00] the my understanding was both Brian Armstrong and Ron Conway were really close to Sam through it. And I ended up talking to him, but also tried to. Talk a lot to the board to, you know, trying to be the mediator. I was trying to, you obviously have a position on it.

**Bret** [01:21:00] Like, and I, I felt that, you know, from the outside looking in, I just really wanted to understand, like, why did this happen? And the process seemed, you know perhaps, you know, to say the least. But I was trying to remain sort of dispassionate because one of the principles was like, if you want to put Humpty Dumpty back together again, you can't be a single issue voter, right?

**Bret** [01:21:00] Like you have to go in and say like, so it was a pretty sensitive moment. But yeah, my, I think Brian's one of the great entrepreneurs and a true true, true friend and ally to, to Sam through that he's

**Swyx** [01:21:00] been through a lot. As well. The reason I bring up Microsoft is because, I mean, obviously Huge Backer.

**Swyx** [01:22:00] We actually talked to David Juan who pitched, I think it was Satya at the time, on on the, the first billion dollar investment in OpenAI. The understanding I had was that the best situation was for Open OpenAI, for Microsoft was open. The As is second best was Microsoft Echo hires Sam and Greg and, and whoever else.

**Swyx** [01:22:00] And that was the relationship at the time. Super close, exclusive relationship and all that. I think now things have evolved a little bit. And you know, with, with the evolution of Stargate and there's some, some uncertainty or FUD about the relationship between Microsoft and OpenAI. And I just wanted to, just kind of bring that up.

**Swyx** [01:22:00] Because like, we're also working, like, one, Satya's, we're fortunate to have Satya as a subscriber to InSpace. And we're working on an interview with him. And we're trying to figure out. How this has evolved now, like what, what is, how would you characterize the relationship between Microsoft and OpenAI?

**Bret** [01:22:00] Microsoft's, you know, the most important partner of OpenAI, you know, so we have a really like deep relationship with them on many fronts.

**Bret** [01:23:00] So I think it's always evolving just because the scale of this market is evolving and in particular the capital requirements for infrastructure. Are well beyond what anyone would have predicted two years ago, let alone whenever the Microsoft relationship started. Well, what was that six years ago? I actually don't, I should know off the top of my head, but it was a long time long in this, in the world of AI, a long, longer time ago.

**Bret** [01:23:00] I don't really think there's anything to share. I mean, it's I don't, I think the relationships evolved because the markets evolved, but the core tenants of the partnership have remained the same. And it's, you know, by far open eyes, most important partner.

**Swyx** [01:23:00] Just double clicking a little bit more, just like a lot of, obviously a lot of our listeners are, you know, care a lot about the priorities of OpenAI.

**Swyx** [01:23:00] I've had it phrased to me that OpenAI had sort of five Top level priorities, like always have frontier models always be on the frontier sort of efficiency as well. Be the first in sort of multi modality, whether it's video generation or real time voice, anything like that. How would you characterize the top priorities of OpenAI?

**Swyx** [01:24:00] Apart from just the highest level AGI thing.

**Bret** [01:24:00] I always come back to the highest level AGI as you put it, it is a mission driven organization. And I think a lot of companies talk about their mission, but OpenAI is literally like the mission defines everything that we do. And I think it is important to understand that if you're trying to like.

**Bret** [01:24:00] Predict where open AI is going to go, because if it doesn't serve the mission, it's very unlikely that it will be a priority for open AI. You know, it's a big organization, so occasionally you might have like side projects, you're like, you know what, I'm not sure that's going to really serve the mission as much as we thought, like, let's not do it anymore.

**Bret** [01:24:00] But at the end of the day, like people work at open AI because they believe in the benefits the AGI can have to humanity. Some people are there because they want to build it. And the actual act of building is incredibly intellectually rewarding. Some people are there because they want to ensure that AGI is safe.

**Bret** [01:24:00] I think we have the best AGI safety team in the world. And there's just so many interesting research problems to, to tackle there as these models become increasingly capable, as they have access to the internet, it has access to tools. It's just like really interesting stuff, but everyone is there because they're interested in the mission.

**Bret** [01:25:00] And as a consequence, I think that. You know, if you look at something like deep research, that lens, it's pretty logical, right? It's like, of course, that's if you're going to think about what it means to create AGI, enabling AI to help further the cause of research is, is meaningful. You can see why a lot of the AGI labs are working on.

**Bret** [01:25:00] Software engineering and code generation, because that seems pretty useful if you're trying to make AGI, right? Just because a huge part of it is, is code, you know to do it. Similarly, as you look at sort of tool use and agents right down the middle of what you need to do AGI, that is the part of the company.

**Bret** [01:25:00] I don't think there is like a. Top, I mean, sure, there's like a, maybe an operational top 10 list, but it is fundamentally about building AGI and ensuring AGI benefits all of humanity. And that's all we exist for. And the rest of it is like, not a distraction necessarily, but that's like the only reason the organization exists.

**Bret** [01:26:00] The thing that I think is remarkable is if I had. Describe that mission to the two of you four years ago, like, you know, one of the interesting things is like, how do you think society would use AI? We'd probably think almost maybe like industrial applications, robots, all these other things. I think chat GPT has been the most.

**Bret** [01:26:00] Delightful. And it doesn't feel counterintuitive now, but like counterintuitive way to serve that mission, because the idea that you can go to chat, gpt. com and access the most advanced intelligence in the world. And there's like a free tier is like pretty amazing. So actually one of the neat things I think is that chat GPT, you know, famously was a research preview that turned into this brand, you know, industry defining brand.

**Bret** [01:26:00] I think it is one of the more key parts of the mission in a lot of ways because it is the way many people will use this intelligence for their everyday use. It's not limited to the few. It's not limited to, you know, a form factor that's inaccessible. So I actually think that. It's been really neat to see how much that has led to there's lots of different contours of the mission of, of AGI, but benefit humanity means everyone can use it.

**Bret** [01:27:00] And so I do think like to your point on is cost important. Oh yeah. Cost is really important. How can we have all of humanity access AI if it's incredibly expensive and you need the 200 subscription, which I pay for it. Cause I think, you know, one promote is mind blowing, you know, but it's, you want both cause you need the advanced research.

**Bret** [01:27:00] You also want everyone in the world to benefit. So that's the way, I mean, if you're trying to predict where we're going to go, just think, what would I do if I were running a company to, you know, go build AGI and ensures it benefits humanity. That's, that's how we prioritize everything.

**Alessio** [01:27:00] I know we're going to wrap up soon.

**Alessio** [01:27:00] I would love to ask some personal questions. One, what are maybe. I've been guiding principles for you one and choosing what to do. So, you know, you were Salesforce. You were CTO of Facebook. I'm sure you got it done a lot more things, but those were the choices that you made. Do you have frameworks that you use for that?

**Alessio** [01:28:00] Yeah, let's start there.

**Bret** [01:28:00] I try to remain sort of like present and grounded in the moment. So. No, I wish I, I wish I did it more, but I don't I really try to focus on like impact, I guess, on what I work on, but also do I enjoy it? And sometimes I think, yeah, we talked a little bit about, you know, what should an entrepreneur work on if they want to start a business?

**Bret** [01:28:00] And I was sort of joking around about sometimes like best businesses are passion projects. I definitely take into account both. Like I, I want to have an impact on the world and I also like, want to enjoy building what I'm building. And I wouldn't work on something that was impactful if I didn't enjoy doing it every day.

**Bret** [01:28:00] And then I try to have some balance in my life. I've got a family and one of the values of, of Sierra's competitive intensity, but we also have a value called family. And we always like to say. Intensity and balance are compatible. You can be in a really intense person and I don't have a lot of like hobbies.

**Bret** [01:29:00] I basically just like work and spend time with my family. But I have balanced there. And but I, but I do try to have that balance just because, you know, if you're proverbially, you know, on your deathbed, what do you, what do you want, and I want to be surrounded by people I love and to be proud of the impact that I had.

**Alessio** [01:29:00] I know you also love to make handmade pasta. I'm Italian, so I would love to hear favorite pasta shapes, maybe sauces. Oh,

**Bret** [01:29:00] that's good. I don't know where you found that. Was that deep research or whatever? It was deep research. That's a deep

**Swyx** [01:29:00] cut. Sorry, where is this from?

**Alessio** [01:29:00] It was from,

**Swyx** [01:29:00] from,

**Alessio** [01:29:00] I

**Bret** [01:29:00] forget,

**Alessio** [01:29:00] it was, it was,

**Bret** [01:29:00] the source was Ling.

**Bret** [01:29:00] I do love to cook. So I started making pasta when my kids were little because I found getting them involved in the kitchen made them eat their meals better. So like participating in the act of making the food. Made them appreciate the food more. And so we do a lot of just like spaghetti linguine, just because it's pretty easy to do.

**Bret** [01:30:00] And the crank is turning and the part of the pasta making for me was like, they could operate the crank and I could put it through and it was very interactive. Sauces. I do a bunch probably, I mean. I, the like really simple marinara with really good tomatoes and it's like just a classic, especially if you're a really good pasta, but I like them all.

**Bret** [01:30:00] But I mean, I just, you know, that's probably the go to just cause it's easy. So

**Alessio** [01:30:00] I just said to us when I saw it come up in the research, I was like, I mean, you have to weigh in as the Italian here. Yeah, I would say so. There's one type of spaghetti you called. I like it. That's kind of like they're almost square.

**Alessio** [01:30:00] Those are really good. We're like you do a cherry tomato sauce with oil. You can put undo again there. Yeah, we can do a different pockets on head

**Swyx** [01:31:00] of the Italian Tech Mafia. Very, very good restaurants. I highly recommend going to Italian restaurants with him. Yeah. Okay. So my question would be, how do you keep up on the eye?

**Swyx** [01:31:00] There's so much. going on. Do you have some special news resource that you use that no one else has?

**Bret** [01:31:00] No, but I most mornings I'll try to sort of like read, kind of check out what's going on on social media, just like any buzz around papers. But the thing that I don't The thing I really like, we have a small research team at Sierra and we'll do sessions on interesting papers then.

**Bret** [01:31:00] I think that's really nice. And, you know, usually it's someone who like really went deep on a paper and kind of does a, you know, you bring your lunch and just kind of do a readout. And I found that to be the most rewarding just because, you know, I love research, but sometimes, you know, some simple concepts are, you know, surrounded by a lot of ornate language and you're like, let's get a few more, you know, Greek letters in there to make it seem like we did something smart, you know?

**Bret** [01:32:00] Sometimes just talking it through conceptually, I can grok the, so what, you know, more easily. And so that's also been interesting as well. And then just conversations, you know, I always try to, when someone says something I'm not familiar with, like I've gotten over the feeling dumb thing. I'm like, I don't know what that is.

**Bret** [01:32:00] Explain it to me. And, and yes, you can sometimes just find neat techniques, new papers, things like that. It's impossible to keep up that, to be honest with you.

**Swyx** [01:32:00] For sure. I mean, if you're struggling, I mean, imagine the rest of us. But like, you know, you, you have really privileged and special conversations.

**Swyx** [01:32:00] What research directions do you think people should pay attention to just based on the buzz you're hearing internally, or, you know,

**Bret** [01:32:00] This isn't surprising to you or anyone, but I, I think the I think in general, the reasoning models, but it's interesting because two years ago, you know, the chain of thought reasoning paper was pretty important, you know, and in general, chain of thought has always been a meaningful thing from the time I think it was a Google paper, right?

**Bret** [01:33:00] If I'm remembering correctly and Google authors. Yeah. And I think that. It has always been a way to get more robust results, you know, from models. What's just really interesting is the combination of distillation and reasoning is making the relative performance. And I'll say actually performance is an ambiguous word, basically the latency of these reasoning models, more reasonable, because if you think about say GPT 4, which was, I think, a huge step change in intelligence, it was.

**Bret** [01:33:00] Quite slow and quite expensive for a long time. So it limited the applications. Once you got to 4. 0 and 4. 0 mini, you know, it opened the door to a lot of different applications, both for cost and latency. We know one came out really interesting quality wise, but it's quite slow, quite expensive. So just the limited applications.

**Bret** [01:33:00] Now I just saw like someone post one of they distilled one of the deep seek models and just made it really small. And, you know, it's doing these chains of thoughts so fast, you know, it's achieving latency numbers. I think sort of similar to like GPT four back in the day. And now all of a sudden you're like, wow, this is really interesting.

**Bret** [01:34:00] And I just think. Especially if there's lots of people listening who are like applied AI people, it's basically like price performance quality. And for a long, like for a long time, the market's so young, if you, you really had to pick which quadrant you wanted for the use case and. The idea that we'll be able to get like relatively sophisticated reasoning at like oh, three minutes has been amazing.

**Bret** [01:34:00] If you haven't tried, it's like the speed of it makes me use it so much more than oh, one, just because oh, one, I'd actually often craft my prompts using for, oh, and then put it into a one just because it was so slow, you know, I just didn't want to like the turnaround time. So I'm just really excited about them.

**Bret** [01:34:00] I think we're in the early days in the same way with the rapid change from GPT three to three, five to four. And you just saw like. Every, and I think with these reasoning models, just how we're using sort of inference time compute and the techniques around it, the use cases for it, it feels like we're in that kind of Cambrian explosion of ideas and possibilities.

**Bret** [01:35:00] So I just think it's really exciting. And and certainly if you look at some of the use cases we're talking about, like coding, these are the exact types of domains where these reasoning models. Do and should have better results. And certainly in our domain, there's just some problems that like thinking through more robustly, which we've always done, but it's just been like, these models are just coming out of the box with a lot more batteries included.

**Bret** [01:35:00] So I'm super excited about them.

**Alessio** [01:35:00] Any final call to action? Are you hiring, growing the team? More people should use Sierra, obviously.

**Bret** [01:35:00] We are growing the team and we're hiring software engineers, agent engineers so send me a note, Bret at Sierra dot AI, we're growing like weed. Our engineering team is exclusively in person in San Francisco, though we do have some kind of forward deployed engineers and, and other offices like London, so

**Alessio** [01:36:00] awesome.

**Alessio** [01:36:00] Thank you so much for the time, Bret.

**Bret** [01:36:00] Thanks for having me.
