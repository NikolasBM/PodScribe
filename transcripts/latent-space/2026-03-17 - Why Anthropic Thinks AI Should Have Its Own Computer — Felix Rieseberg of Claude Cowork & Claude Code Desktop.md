---
podcast: "latent-space"
podcast_title: "Latent Space"
title: "Why Anthropic Thinks AI Should Have Its Own Computer — Felix Rieseberg of Claude Cowork & Claude Code Desktop"
date: 2026-03-17
url: "https://www.latent.space/p/felix-anthropic"
guid: "substack:191097767"
host: "Swyx"
guests: ["swyx", "Felix"]
format: "interview"
level: 2
length: "00:00:00"
categories: ["agents", "work", "coding", "safety-security"]
featured: ["Claude Cowork", "Claude Code", "Claude", "computer use", "agent harness", "Anthropic"]
mentioned: ["Slack", "MCP", "Figma"]
transcript_source: "publisher"
---

# Why Anthropic Thinks AI Should Have Its Own Computer — Felix Rieseberg of Claude Cowork & Claude Code Desktop

**Alessio** [00:00:00] Hey everyone. Welcome to the Latent Space Podcast, our first one in the new studio. This is Alessio, founder of Kernel Labs, and I’m joined by swyx, editor of Latent Space.

**swyx** [00:00:00] Yeah, so nice to be here. Thanks to, uh, TJ, Alessio, Allen helping to set everything up. It looks beautiful. We even have the logo outside.

[00:00:00] Yeah, kind.

**Felix** [00:00:00] It’s like really nice, right? When you walk in here as a guest, you’re like, ah, this is a serious production. You’re like, feel it immediately.

**swyx** [00:00:00] Yeah. Felix, you’ve been, you’re, you’re currently a product manager of Cowork or,

**Felix** [00:00:00] uh, really Technic

**swyx** [00:00:00] Eng. Yeah. The, the identities are kind of vague member technical staff.

**Felix** [00:00:00] I know member staff is like, the official title will carry around forever.

**swyx** [00:00:00] Yeah. I basically kind of wanted, like we’ve been. Kinda obsessed. I, I’ve been using it a lot, even for managing latent space. Like, uh, cowork helps me upload videos and like title things and like edit and everything. It’s, it’s like really amazing.

**Alessio** [00:00:00] Cool. He said multiple times Cowork has said gi in the group track.

**swyx** [00:00:00] Yeah, yeah, yeah. So, so we have a second, uh, we have a second channel, uh, for latent space tv. Uh, and I, uh, and uh, we basically, this is our Discord meetup. Um, and I I, we have like Claude Coworks, it might be a GI, I don’t know if we, we have, uh, uploaded it yet, but one of the sessions was like a, like a Claude cowork thing.

**Felix** [00:00:00] I, you have to see, I would love to see it. Like, I’m so curious, like one of the most fun parts of my job is like constantly see the weird things people use Cowork for because it’s obviously like very hard for us to actually design for specific use cases we do. But like every single person who’s like most amazed is usually amazed about a thing that I didn’t even expect cowork would be good at.

[00:00:00] Um, we have a new designer and it’s one of the first small tasks. I was like, Hey, we need like a new emoji for cowork for our internal stock. It’s like a pretty small thing. I like, can you please do it? And he drew an SVG and just gave it to coworker was like, can you animate this emoji? And now it has like this beautiful loopy animation.

[00:00:00] Um, and I mean, I think obviously this goes down to like, it turns out you can do more things with code than you expected, but it, it’s like that kind of stuff that is really fun to me. So, long story short, I would love to see like, the kind of things you’re doing.

**swyx** [00:00:00] I’ll pull it up. I’ll pull it up.

**Felix** [00:00:00] Yeah. Yeah.

**swyx** [00:00:00] Uh, but before we get into it, I, I think always wanna start with like a top level. What is Claude Cowork for people who haven’t heard of it? Haven’t tried it out.

**Felix** [00:00:00] Okay. Uh, real quick, Claude Cowork is a user friendly version of Claude Code. So the way it basically works is we have Claude Code and for us, fairly impressive agent harness that over December we noticed more and more people are using either, even though they’re not technical, they, they’re not at home in the terminal or they are at home in the terminal, but they started using Claude Code for non-coding workloads, right?

[00:00:00] Like managing expenses or like filling out receipts or organizing a knowledge base. Like there was a big obsidian moment that a lot of people liked and we wanted to capitalize on that, but also bring, bring this capability to people who are not terminal native and who might not know how to like brew and store something.

[00:00:00] So cowork is Claude Code running in original machine with a little bit of padding, a little bit more guardrails, making it a little safer and a little bit more convenient for people who don’t wanna first open up the terminal when they go to work.

**swyx** [00:00:00] It’s interesting, uh, that is kind of. Pitch that way as a more user friendly thing because I always feel like it, it, to me, I I treat it as like why I’m familiar with Claude Code.

[00:00:00] Like we, we did a Claude Code episode Yeah. A year ago. But this one is like even more power user tools ‘cause it, uh, it kind of integrates much better with like clotting Chrome and, uh, in all the, all the other tooling. But like, maybe, maybe that’s like a perception thing, right? Like

**Felix** [00:00:00] No, honestly, I don’t think you’re wrong.

[00:00:00] This is like a, a thing I’ve been thinking a lot about for like the last two weeks. So,

**swyx** [00:00:00] but when they say user friendly, it’s like, oh, it’s the dumb down version. But no, actually this is the superset.

**Felix** [00:00:00] Yeah. Like, I think a similar thing happened, A similar thing happened to me about 10 years ago, like maybe 12 years ago when I was at Microsoft and we started working on, on Electron and like browser-based technologies and cross-platform stuff.

[00:00:00] And one of the first use cases was Visual Studio Code, which used to be a website. And the initial narrative was, or Visual Studio Code is, is like a more user-friendly version of Visual Studio. But in a similar vein, I think there was some voices saying, oh, this is. For serious developers, like, we’re not gonna use this.

[00:00:00] Right? For like anything. And I think in the end what happened is people have different stories about why Visual Studio Code became such a big thing. But my personal, my personal belief is that the Hackability and the extendability has like played a pretty big role, right? You can hook in Visual Studio Code that like almost any workload, it’s so easy to hack on, so easy to put extensions for it.

[00:00:00] And I think cowork might be hitting a similar thing where it’s very easy to extend and it’s very easy to bring into your workflows. Uh, so the convenience I think is a bit of a, it’s obviously the thing we strive for as developers, but I think the way people find value in it then is by probably mapping it onto whatever they actually have to do in their job.

**Alessio** [00:00:00] So end of last year, you see the spike of like non-technical usage and clock code. What’s the design process to say we should make clock code work? Because I mean, you built it in only 10 days. Um, I’m sure there was some discussion before on whether it’s easier to use mean. You know, like making, making like a desktop GUI is obviously one way to do it, but like there’s a lot of nuance in the product.

[00:00:00] Like maybe talk people through what was like the trigger of like, we should build a separate thing. We should not build like a different plot code thing. And then maybe some of the more interesting design decisions that maybe you didn’t take.

**Felix** [00:00:00] Yeah, I think philanthropic, we’ve been thinking about ways to move people who are comfortable with using Claude to answer questions and bring more of the power of like this thing to now like, execute tasks for you.

[00:00:00] I can like solve problems for you can like build things for you. How do we bring that capability to people who are currently mostly comfortable with like a like question answer paradigm within the chat. And we’ve had a lot of prototypes around that. Just going back as far as like easily a year and a half.

[00:00:00] Like we had a lot of people working on that. Um, and internally philanthropic is a very prototype demo, first culture. We have a lot of like internal prototypes that don’t reach the public. What Cowork actually became is like we sort of picked the right pieces out of the many prototypes that we had.

[00:00:00] Right. And that’s, that’s maybe also like, I think an important qualifier whenever people mention this like 10 day number. I do think it’s important to me to mention that within Double Scratch there was like a lot of stuff already happening, right? Like, and I think it’s important for people to remember that when you build a website, you use React, you use like a bunch of other things.

[00:00:00] And this is like a similar scenario with like a lot of pieces we already had. Um, and in terms of decision path, I think we live in like an interesting new world where execution is actually quite cheap.

**swyx** [00:00:00] Mm-hmm.

**Felix** [00:00:00] So maybe, maybe what you would do That’s so crazy. The year. I know it’s wild.

**swyx** [00:00:00] You should be, ideas are cheap.

[00:00:00] Execution is the hard part. I

**Felix** [00:00:00] know. And like the, we, we used to live in this world maybe where you would take a product manager and the product manager would go to a number of potential customers and in this like very low bandwidth way, would try to. Try to like tease out what are the problems they’re having, what are they willing to buy?

[00:00:00] Um, and then maybe what can you build to like drive out that need and then you go back and you like draft a spec and you think about it and then like you make a design and you execute it. We internally philanthropic app, not pretty much closer to the point where we’re like, don’t even write a memo, just like build, like let’s build all the candidates very quickly.

[00:00:00] Let’s just build all of them and then pick the best ones. I think the, the decision that is most impactful both for the product as well for the users right now is like the way we put value on your local computer. I think that’s a big decision point a lot of people have thought about. Should this thing, whatever it is, should it ultimately run into computer or should it run in the cloud?

[00:00:00] ‘cause they’re big trade offs, right?

**Alessio** [00:00:00] I guess like if we solve auth, it would be easy to do in the cloud. But I think like the fact that I can just download any file from anywhere and then put it and cowork there, it’s like a big unlock. Um, I mean it’s interesting you mentioned reusing certain pieces. I think this is something I’ve been thinking about even with Claude Code, right?

[00:00:00] The price of like writing code is going to zero, blah, blah, blah. But it actually seems like the value of having some sort of platform substrate is like increasing because as you build these new things, you can kind of plug them together.

**Felix** [00:00:00] Yeah.

**Alessio** [00:00:00] So I almost feel like when people are saying, oh, the value of a lot of software is gonna zero because you can recreate it, to me it’s almost like the opposite.

[00:00:00] It’s like having an existing platform to build on top of. It’s like even more valuable because you can kind of bolt things on.

**Felix** [00:00:00] Yeah.

**Alessio** [00:00:00] You have obviously mcps, you have skills, you have like obviously the models, which is a big part. All these things kind of come together. Do you feel like that’s a valid way to think about it, where people should invest even more in kind of like primitives.

[00:00:00] To rebuild on or are you like recreating a lot of it each time because like things change and it’s easier to rewrite than reuse?

**Felix** [00:00:00] You know, I think, I think you’re right. I think you’re right that the holistic platform is really useful. And this is maybe a whole like a somewhat contrarian view to a lot of people in ai.

[00:00:00] I actually don’t think that the future is going to be hyper personalized software down to the point where everyone is running their own version. Like, I actually think it’s going to be quite hard for all of us to have our own internal chat tool and like, if I wanna talk to you, like

**swyx** [00:00:00] how

**Felix** [00:00:00] is that gonna work, right?

[00:00:00] In the, in the context of cowork and how we build it, I think it’s a bit of a combination. Like what the, the execution that gets cheap is not necessarily rebuilding all the primitives. I think our priori, there’s also not a lot of value in it. So for instance, my team did not think about rebuilding clock code.

[00:00:00] We’re like very much started with the. The core thesis of this should be Claude Code.

[00:00:00] Mm-hmm.

**Felix** [00:00:00] And then we’ll like build things on top of it. The part of the execution that gets a little cheaper is like, how do you take all of these Lego pieces and put them together in a way that makes sense for users?

[00:00:00] It’s like actually valuable. You have so many different approaches now in terms of what kind of, what kind of things do you actually elevate to a primitive, do you strongly believe that all your products should be built by just combining primitive that the public also has available? Do you keep some things internal?

[00:00:00] Um, and I think that’s still evolving, but I think what’s probably gonna go away is like, I’m not sure if it’s gonna fully go away, but I’m gonna say, I think for me personally, I will probably no longer try to come up with a really good product without testing up with people. This is not a new concept, but wherever you used to have to make costly decisions around, do we pick technology A or technology B, or do we like, um, build it this way, build it the other way.

[00:00:00] I really strongly believe now you just build all of them and try them out with a small focus group and then whatever, whatever is better is what you go with. Right. And that, that is probably quite different even from how we maybe worked a year ago. Right. Like, I think, I think this happened very recently.

**Alessio** [00:00:00] Yeah. I started building something in on Electron since you’re here. Coincidence. Uh, but then Electron and like SQL Light are like, there’s like some issues that like between development and like, uh, building anyway. And I was like, let’s just rebuild the whole thing in Swift and just recreated the whole thing in Swift.

[00:00:00] And it’s like, I. It’s done.

**swyx** [00:00:00] You know, I didn’t take any effort. I, I, I don’t even know Swift.

**Alessio** [00:00:00] Yeah, exactly. I was like, I’m the, I’m not reviewing it anyway, whatever. You can write in whatever language you pick, but the important stuff that I did was not write the electron bindings. Yeah. It was like the logic of what happens in the app, you know, and then the model is like, yeah, I can just recreate the same thing as with

**swyx** [00:00:00] Yeah.

[00:00:00] I, I think you still want, especially for people who are doing like high performance software or like very complex software, uh, you still want like, some view of the architecture. Uh, but you can use markdown for that,

**Felix** [00:00:00] right? Yeah.

**swyx** [00:00:00] Uh, you don’t actually have to read the code again. I, I’m still like on a sort of like a definitional thing.

[00:00:00] Um, can we build a good mental model of Claude Cowork? Um, this is what I have, right? Like you you said it’s like fundamentally cloud co. We don’t wanna touch it. There’s the cloud app, there’s clouding Chrome. I think you guys do something different in planning, but, uh, I’ve been talking with Tariq who is on the cloud co team, and you guys are, he’s like, no, we just exposed planning.

[00:00:00] Maybe we can clarify like, what are the major pieces. That people should be aware. It goes into cowork, like,

**Felix** [00:00:00] okay, I think you basically have them. So really, um, you can, you can take planning more or less out. I think there’s a few things that are really valuable in cowork. Um, the virtual machine is probably the most powerful thing.

[00:00:00] So we currently run like a, we currently run like a lightweight VM and we put clocked out into the vm and we do that for, for, um, a number of reasons. Safety and security is a big one, but even if you, even if you ignore for a second safety and security and you’re just like, okay, Yolo, I want this thing to do whatever.

[00:00:00] It is quite powerful to give Claus on computer that is like generally a good idea. And in terms of architecture and UX and everything else that we’ve been working on, philanthropic, it often is quite useful for you to like anthropomorphize, um, clot aggressively and just be like, this is a person. What will you do if you give a, if you had a person, right?

[00:00:00] Yeah. And the analogy I’ve given my dad this morning who is still like quite insistent on using chat even for like coding things, is if you were a developer and your employer told you that you don’t need a computer, they’re just gonna like, send you emails with a code and you send emails with code back like that, maybe work for Patrick Miles in the back, but that it’s not very effective.

[00:00:00] Um, so what we can do with the VM is because it’s a, it’s a Linux system, Claude Code has more or less free reign to install whatever needs to install. It can install Python, it can install no js. We do have strict network ingress and egress controls. So you can still, as, as a user in like plain human language, make it clear to, to the entire system what you’re okay with and what you’re not okay with.

[00:00:00] But at no point do we have to ask a real person, like a, like a person who might be in marketing or a lawyer. I’d have to go to a lawyer and be like, are you okay with me installing Homebrew?

**Alessio** [00:00:00] Yeah, yeah.

**Felix** [00:00:00] Right. Because the implications of the question and the answer are complex and nuanced and like, not, not easy to reason about.

[00:00:00] This gives us a lot of distraction that makes Cloud very powerful. Now then around it, we, we do probably have a number of things that also keeps growing almost every single week that you’re probably noticing that make cowork maybe better for certain tasks than just cloud. Cloud on its own. Yeah. But most of those actually live in the system prompt.

[00:00:00] They’re about like, what can we infer about the work that you do? What can we, what can we intru in the system prompt to make that more effective? It’s of course the like very tight integration with Cloud and Chrome. You’re noticing that a lot of people, especially as the models get better, a lot of people throw up their hands when it comes to MCP connectors in this area.

[00:00:00] I’m not gonna, I’m not gonna go through like 25 M CCP connectors, click off everywhere and then like half of them don’t let me do the things anyway. So Cloud and Chrome is quite powerful because we can just talk to the cloud and Chrome sub agent and that will just do things for you.

**swyx** [00:00:00] Yeah, so, so one example right in MCPI, honestly, I think that the state of MCP is kind of, kind of.

[00:00:00] Really hard to integrate. Um, I need to, I needed to add, uh, Figma MCP to the coding agent that I use.

**Felix** [00:00:00] Yeah.

**swyx** [00:00:00] Uh, and, but I didn’t wanna read the docs, so I just had caught to it. And it’s, it’s great at reading docs and the same, same way I had to set up like a Google Cloud, um, account for some project I was working on and get some API keys somewhere.

[00:00:00] And Google Cloud is famously super hard to navigate, so I just didn’t wanna deal with any of it. I just used Claude Cowork

**Felix** [00:00:00] within the first week of developing on Core. This happened very, very quickly. Um, I caught myself by starting to use cowork for coding tasks, which is not ostensibly what we built it for, right?

[00:00:00] We don’t need to. But I found myself, um, I found myself like on our internal, internal tool that we have for, to collect crashes and just like debugging information and I found myself sort like picking out the ones that I think we can easily fix versus the ones that might be like kernel corruption or something else on the operating system.

[00:00:00] And I found myself sort of picking these out and then just telling Clark, go fix this bug. I was like, what am I doing here? Go one level up, tell a cowork, I want you to go to all these crash tools. I want you to find all the bugs that you think are fixable and not like an operating system crash. And then I want you to tell another cloud to like fix all of that.

[00:00:00] Um, and that’s, that’s, that’s sort of another cloud,

**swyx** [00:00:00] just so it can spin up another instance or,

**Felix** [00:00:00] uh, it, currently what I do is, um, and this is a bit of a hack, but I tell it to use clockwork remote to which website itself? Yeah, that’s interesting. So you basically take, if you, if you imagine like a dashboard with like 20 bucks, you, this is remote control or clock or remote, or, sorry, I just wanted to confirm what, the way I’m using it is.

[00:00:00] I have cowork running and I’m telling cowork, here’s where I normally go every morning to find the latest bugs. Go read the entire bug list, separate out which ones are fixable, which ones are, are fixable, and then for the fixable ones, four is this almost loop. For each bug, write a markdown file with a prompt.

[00:00:00] And then for each markdown v, that is a prompt. Start of a cloud set. So natively Claude Code has

**swyx** [00:00:00] this concept of subagents. Mm-hmm. And this is basically a subagent, but you’re not using the subagent functionality.

**Felix** [00:00:00] I’m not using the subagent functionality. And the reason I’m not is because I’m firing that off as a Claude Code remote

**swyx** [00:00:00] task.

**Felix** [00:00:00] Yes. That’s kind of nice. ‘cause then I can just fire it off. I can go to my next meeting and in Claude Code remote. Now the work is happening.

**swyx** [00:00:00] Mm-hmm. Yeah. You, you see like you’re already starting to use the cloud over your local machine. And I think this is one of those things where like. Shouldn’t just everything just be cloud first, right?

**Felix** [00:00:00] Ah, this is such a good group. I’m like solely bad about this. I have so many thoughts about that. Okay. So I generally believe that Silicon Valley overall is undervaluing the local computer. And my default argument for that is always how come we’re all using MacBooks and not like an iPad or a Chromebook?

[00:00:00] Um, that there is like still value in, in having a local machine. And now when I think about Clot, it’s this entity that is supposed to be very useful to you, like it tremendously useful to you. I think that entity needs to have access to all the same tools you have access to. Otherwise it’s gonna be hamstrung in like all these complex ways.

[00:00:00] And there’s, there’s sort of two approaches we could take. We could say, okay, we’re gonna like one by one chip away at everything that is at your computer and move it into the cloud. That’s, that’s one way to do it. Um, and I think other products have taken that path. I personally, this is a very personal opinion, but I personally, for the amount of tools that I use.

[00:00:00] Just don’t have the patience to give another tool like permissions to every single thing and keep those permissions up to date. The second thing that I’m still grappling with, and I don’t have a good answer for anyone just yet, but the second thing I’m still grappling with is what does it look like for someone to slurp up your entire work and put that in the cloud?

[00:00:00] Like if I, just as an example, like if you could click a button and it just clone your entire computer into the cloud, is that something that you would want? I’m not totally convinced yet that all everyone will. Mm-hmm. And that is sort of like upstream of all the technical issues we’re gonna have. ‘cause like in general, I think the world is not ready for this kind of stuff.

[00:00:00] Like, I’ll give you one quick example that would probably be very easy for us. So as a desktop app, we in theory with your permission, can do a lot of things on your computer, including reading your Chrome cookies. If we really want to do right, we could take your Chrome cookies, you would have to decrypt them for us.

[00:00:00] We could put those on the cloud if we really felt like it. Pretty easy solution. That would be super cool. We could just be like, oh, we can do all your tasks in the cloud now. Um, a lot of websites, thanks, include it. If, if they see the same authentication from like two different locations, we’ll just lock down your account and now you have to go to the branch and be like, okay, I, I’m here with my passport.

[00:00:00] You actually know that. Wow. Yeah. As tired as well are of the term agent for the age agent future, I think there’s a lot of stuff that sort of slowly needs to catch up and until that’s the case, the way I, as someone’s working on clock and make Cloud most effective is to like put it where you are working.

**swyx** [00:00:00] Anything else? I thought with our mental model, so like, basically like, uh, part of me also just want, like the more I understand how it works, the more I can use it to its full potential. Right?

**Felix** [00:00:00] Yeah.

**swyx** [00:00:00] And so what I’m get hearing from you is you told me to delete the planning thing. You’re not doing anything special on, on the, that’s only exclusive to Qua cowork.

**Felix** [00:00:00] We have some tricks for this sort of like change week over week. We eval cowork maybe against different use cases than he would evil clock code, right? If you think about it this way. Okay, so like clock code is our eval clock cowork. Yeah. So clock code is like quite optimized for coding tasks and we mostly value it whether or not we’re getting better or worse depending on how good it is at like a typical suite job.

[00:00:00] And Clark Cowork on the other hand, we evaluate more against typical knowledge work, the kind of stuff he would find in finance or in like maybe a, like in like a legal office. Um, my personal use case is always like managing my things, like managing my personal mortgage or something like that, right? Or like wealth planning for me and my family.

[00:00:00] Those are the kinds of use cases we eval, clock cowork on. And what you might be picking up on is like the subtle changes we make to the system. Prompt what we put in the system, prompt how we steer, clot with the tools we give it. Um, like either it’d be better in one or the other direction and whether there’s a trade off, try us exist a lot.

[00:00:00] CLO code will be better of a code and Claude Cowork will be better. For non-coding tasks, will those gaps still exist in the next three generations of models? It’s like a little unclear to me though.

**swyx** [00:00:00] Yeah,

**Felix** [00:00:00] because right now these like hyper optimizations we make, I’m not sure for how long they’re still be relevant.

**swyx** [00:00:00] I think what I was referring to was also, it, it just, uh, it qualitatively felt different when I probably, it’s just all prompting and I’m reading too much into it, but like the, the fact that it comes out with like a nine step plan, I can edit the plan and give feedback and, and, and see it execute the plan.

[00:00:00] Yeah. It felt more long range than in Claude Code, but maybe that already existed in Claude Code and you just build a nicer UI for it.

**Felix** [00:00:00] It’s kind of both. Um, like if the Clark Code people who build the planning functionalities would city, they probably say yes, we have all of those things in Clark code and they do.

[00:00:00] Um, I think people tend to give cowork. Tasks that are maybe of longer time horizon, I thought is

**swyx** [00:00:00] so long. Yeah.

**Felix** [00:00:00] That’s like one thing, right? It’s just like that the, the chunk of work tends to be maybe a little bigger. And then the second thing is that because the work, when it gets longer, it gets a little bit more ambiguous.

[00:00:00] We do tell co-work to make heavy use of the planning tool or to make heavy use of the ask user question tool, right? We do want it to come up with like. Different scenarios of, okay, tease out what the user actually wants. Don’t go off to work for like four hours and then come back with the wrong thing.

[00:00:00] And you’re probably picking up on that.

**swyx** [00:00:00] Yeah.

**Felix** [00:00:00] Um, I wish I could tell you I like built this magical thing and it’s like, there’s some secret sauce,

**swyx** [00:00:00] but No, no, no. I mean, it’s, it’s just clarity is good that, you know, engineers just want to know. Yeah. They can, they can plan around it. And then I think also for me, um, I am realizing I have to switch to my, my other machine because this is a new machine that doesn’t have my session.

[00:00:00] But, uh, yeah, the, the, the planning is really important for, for me to like approve or like to see whether it’s like, it’s right. The ask is, the question is so beautifully presented. I mean, it also, it also available in like cursor and, and in Claude Code. But like, I, I think like it’s so nice to see that it, like it’s kind of for me like to understand that it gets me, it gets what I want to do.

**Felix** [00:00:00] Yeah.

**swyx** [00:00:00] Yeah.

**Felix** [00:00:00] It probably very hard

**swyx** [00:00:00] just on the topical evals. Mm-hmm. When you say eval, I think people are very vague about what it means. Is it just like vibe testing or do you have like automated programmatic evals of Claude Cowork?

**Felix** [00:00:00] When we say eval, uh, what we really mean is that we essentially take the entire transcript, including all the tools that clot has available ultimately to it, and we then measure what are the outputs, depending on what we tweak, right?

[00:00:00] So we do run that a lot. We use that in training. Um, we use that in, in like, if you sort of separate out post training from like the scaffolding around it. Cowork sort of exists in the scaffolding space, but obviously we also train on it a little bit. Um, so when we say eval, we mean given the certain transcript, what do the outputs look like?

[00:00:00] Including the file outputs as well as like the actual token outputs, like the ones that you see in the chat window.

**Alessio** [00:00:00] I’m curious, um, how much of the failure modes are the model intelligence versus like the usage of the end tool to put the intelligence in? Like the well planning is like a good example, right?

[00:00:00] It’s like one thing is to come up with a plan. The other thing is like make a nice spreadsheet. Yeah. That kind of runs you through the plan. Like how have you seen that? Well,

**Felix** [00:00:00] the thing that I grapple with a lot is that whatever scaffolding you come up with, I think we still have a bit of sort of like model overhang where the model is dramatically more capable than right.

[00:00:00] Users end up using it for. And I think part of that is that we’re just not getting the model all the tools to do all the things that’s theory capable of, right? There’s like one thing, um, however, whenever you do build the scaffolding, I’m sort of wondering at what point, at what point will that scaffolding go away and like how much you invest in figuring out what the right scaffolding is.

[00:00:00] It’s kind of up to, it’s a little bit of a bet. And one thing that I as an NJ quite enjoy is that like working in philanthropic and working at a frontier lab, I maybe have a little bit more insight into what’s coming, coming down the chute in terms of like, what’s the next model, what is the model capable of?

[00:00:00] What is good at, what is it bad at? And I’m, I’m increasingly wondering, is the right thing for us to like really invest too much in sort of these like scaffolding corrections where the model might otherwise not misbehave, but just not do the thing that you want?

**Alessio** [00:00:00] Yeah.

**Felix** [00:00:00] Or is it to just like give it as many capabilities as possible, try to make those safe so there’s the worst case scenarios, likeno status might be otherwise.

[00:00:00] And then just simply wait a second for the next model drop. I’m personally, currently more leaning into the ladder. I think we’re gonna see a lot of like applications and companies that do very impressive things with ai that in the short term might seem very effective ‘cause they’re very specialized to individual use cases.

[00:00:00] But I think once models get better generalization and get better at like those specific use cases without being super guided on those, I’m not sure how long that’s gonna stick around. And you can kind of, kind of already see this in like skills and NCP servers, right? Mm-hmm. We’ve, we’ve already seen sort of this like slow shift from MCP service to skills.

[00:00:00] And like, maybe a good example is Barry who made skills. He was initially hacking on something that honestly looked a lot, looked, looked a lot like what Cowork does today. It was sort of thinking about what if cowork, but for like people who don’t wanna build code. Mm-hmm. And, um, he too did that as a prototype inside the desktop app.

[00:00:00] One of the first use cases we thought of were, okay, what, what are like coding like use cases that could really benefit from graphical interfaces and like from being a little separated from the actual underlying code. And everyone comes with the same answers. Data analysis,

**Alessio** [00:00:00] right?

**Felix** [00:00:00] Yeah. Or saying how many users do we have today?

[00:00:00] How many, like, it’s always data analysis. And I think the thing that ultimately led to skills is that we wanted to connect this little prototype to our data warehouse and. The team very quickly discovered that like instead of building a custom tool for the thing to talk our data warehouse, they just like meet and embarked on follow like mm-hmm.

[00:00:00] Dear Claude, if you want to get data, here’s the end point. Here’s what the API looks like. You’ll figure it out.

**swyx** [00:00:00] Ah.

**Felix** [00:00:00] And then it be hand over control. Yeah, yeah. Also just like maybe go one step up in the layer of abstractions, right. Just, yeah. Instead of, instead of telling the thing, here’s ACL I, please call the CLI, or here’s an MCP.

[00:00:00] Please call this ECT shape. Just like this is the end point. If you wanna know something, if you post here, maybe you can do post sql. It’s gonna be okay. And that ended up being so effective that they started trying the same pattern of like just giving the model a markdown file that describes whatever it needs to do.

[00:00:00] That the whole thing eventually became skills and we’re like. We should package this up. This is a good idea.

**swyx** [00:00:00] Yeah. Um, we’ve had Barry Mahesh, uh, on, on our conference and uh, he’s uh, definitely got a good idea there.

**Felix** [00:00:00] Yeah.

**swyx** [00:00:00] I wanted to show you the, how I’ve been using Claude Cowork.

**Felix** [00:00:00] Uh, this is was my favorite part.

**swyx** [00:00:00] This is this. So this is like me, uh, this is how we run the Discord. Uh, we literally, uh, at first I didn’t trust Cloud Core. This was my very first usage.

**Felix** [00:00:00] Okay.

**swyx** [00:00:00] Right. So then I was like, okay, I will just try to manually download from Zoom all my recordings and upload it to YouTube. Yeah. Because this is a very laborious process.

[00:00:00] I got a click, click, click YouTube, um, isn’t super user friendly. Uh, and it just did it. And then I was like, actually, you know, even the download from Zoom part, I should also. Put into Claude Cowork, and then I did it right. Here’s a bunch of, and it starts compacting here, and it, and it, it starts to even be able to do things like look through the individual frames of the video to name the video so I can upload it auto automatically.

[00:00:00] Oh, that is, and this replaces my job as a YouTuber. We will forever appreciate your creative Yes. You know, and so that’s great. Uh, but then by the way, it compacts and makes, makes like a new thing, right? So I, I don’t, I don’t have the initial, initial thing, but then I asked it to make its own skills so that it, so that something that’s repetitive and one-off and human guided becomes more automated and I can use the skills independently and reuse them.

[00:00:00] Uh, and it obviously you can write skills and that goes into context and skills at the bottom here, which is, which is so nice. Um, so I have all these skills that, that I now sort of do on a weekly basis. Uh, I know you’ve released scheduled Coworks, which I haven’t done yet, but

**Felix** [00:00:00] course I should try them. I, I think this is like so wonderful and fun for me to see because.

[00:00:00] One thing that is very fun for me about skills in particular is that they’re so easy to make. Like anyone can make a skill, like a text message, could be a skill, and they can be so hyper personalized to you. And this is like sort of the subtraction layer, right? Like, um, I, I’m just guessing, but I assume, heck, you are very good at your job.

[00:00:00] You’re probably given this thing some guidance about how to do it, right? I,

**swyx** [00:00:00] I just said, wrap everything up into, into a skill, right?

**Felix** [00:00:00] Yeah.

**swyx** [00:00:00] And then, uh, and then I was like, actually, sometimes I might need to break, uh, things apart because some parts fail or some parts might be needed in individually. So I told it to split one skill into three skills.

[00:00:00] So it’s like a skill splitting thing, and then there’s like a parent skill that just orchestrates all of them if I want to use that. You know, like, um, I think that’s, that’s like really good. Uh, and, and, uh, there’s, there’s one more part, which is the, uh, Google Chrome thing that I told you about.

**Felix** [00:00:00] Yeah.

**swyx** [00:00:00] Where I’m like, okay, you know, what’s better than uploading, using Claude Coworks to YouTube?

[00:00:00] Like actually. Looking at the docs to like programmatically upload to YouTube and then putting that in a skill. And I’ve never done that before. I don’t want to deal with Google Cloud. Yeah. So Claude Cowork does it for me.

**Felix** [00:00:00] That is really cool.

**swyx** [00:00:00] So, so I, I just, I don’t care. I just, like, I do a thing. I don’t, it doesn’t really matter.

**Felix** [00:00:00] That is really cool. And then you’ve, I assume paired the skill just with the script that it’s built.

**swyx** [00:00:00] Yeah, no, I just update, update the skills.

**Felix** [00:00:00] Oh, that is beautiful. Yeah. That’s wonderful.

**swyx** [00:00:00] It’s kind of like a skill, like, uh, uh, basically I think like the way that people ease into Claude Cowork is like take a knowledge work task that you would normally be clicking around for and then, uh, try to turn, turn that, and then you do the, okay, well what if you went further?

[00:00:00] Okay. And then when, if you went further, when, if you, and it sort of expand the scope of cowork as you gain trust with it and, and also teach it how to replace you.

**Felix** [00:00:00] Yeah. It’s like a little bit like playing factorial, but for your own life. Uh, like you say, you start really small.

**swyx** [00:00:00] Yeah.

**Felix** [00:00:00] You start automating something really tiny and like.

[00:00:00] Once it clicks, you keep adding onto this like automation empire. Just like make your life easier and easier. My favorite skill has been, um, every single morning Kohlberg starts looking at my calendar and make sure that there’s conflicts because people tend to schedule a lot of meetings, sometimes last minute, sometimes miss it soft and painful.

[00:00:00] And a lot of products have existed like that A lot. I’ve written in the custom prompt there. I haven’t made it a skill, um, honestly should.

**swyx** [00:00:00] Yeah.

**Felix** [00:00:00] But I’ve given it like pretty clear instructions about okay, here are some people, if they book over other meetings, I’m probably gonna go to their meeting. Like if Dario schedules a meeting.

**swyx** [00:00:00] Right.

**Felix** [00:00:00] Not try to reschedule down. Right. Um, and I think there’s some other rules in there about like what kind of meetings I care more about what kind of meetings I care less about. What is okay to like, maybe pun like when I want to be, when I want to be working, when I don’t want to be working. And it’s those really small things that I can think kind of click with people.

[00:00:00] Right. When we launch co-work, I think one of the US races that went most viral on Twitter. X was clean up your desktop, which is stuff, because silly, that’s such a smart thing, right? Like you don’t need to model to clean up your desktop. Not really. Um,

**swyx** [00:00:00] like this, like clean up my desktop.

**Felix** [00:00:00] Yeah, exactly. Yeah.

**swyx** [00:00:00] I need to, I need to choose my desktop, right? I guess give it access to my desktop.

**Felix** [00:00:00] Yeah.

**swyx** [00:00:00] Okay. Uh, okay. This is very scary. Oh, we’ll do it.

**Alessio** [00:00:00] I did, I did it with my downloads folder. It was like, you have so many term sheets and there’s like eight copies of your rental lease for your office. I was like, all right.

[00:00:00] Like, don’t yell at me.

**Felix** [00:00:00] It’s like, it’s not such a small task. And then like, I, I would never go out there and normally otherwise and tell people I’ve pulled a product. It can organize your folder. Right. Um, because it feels small. But I think to your point like,

**swyx** [00:00:00] oh, here’s, here’s the, here’s the ask user questions.

**Felix** [00:00:00] Yeah.

**swyx** [00:00:00] Uh,

**Felix** [00:00:00] beautiful. Right. Elite obvious junk. You probably shouldn’t click that.

**Alessio** [00:00:00] No.

**Felix** [00:00:00] If he’s not done right.

**swyx** [00:00:00] As long as it’s reversible, I don’t

**Alessio** [00:00:00] make up blend to,

**swyx** [00:00:00] yeah. Uh, yeah. No, I, I have a, I have a typical, everything is super messy folder. So, yes. I think this, this is super helpful. So this is a pretty simple task.

[00:00:00] Mm-hmm. But I’ve, okay, here it is. Right. Here’s the progress. I don’t see this in, that’s why I’m like, this gotta be something different than, uh, than Claude Code, because I’m like, we

**Felix** [00:00:00] do. Yeah. That’s, we do system prompt that. We’re like, all right. We want you to think about like, this task Yeah. Methodology.

[00:00:00] Yeah.

**swyx** [00:00:00] And then I can, I can, I can do like little suggestions for, for, for these things. It’s beautiful. Look at this. I, I can, I can like say like, oh, don’t do that. Don’t do this. It’s amazing.

**Felix** [00:00:00] I’m so happy. You like it. Um, I mean, the other way around, like we’re part of the Clark core team, if you would like this in Clark COVID.

**swyx** [00:00:00] Yeah. Yeah. Yeah. Uh, so, so yeah, I mean, uh, this is really good. Obviously I, I’m like kind of raving about it. Uh, you know, I have other things like sign up for pg e so if you can do phone calls for me, that’d be great. Um, I, I do, people

**Felix** [00:00:00] have done that. Obviously you can’t do that natively, but people have done that with like, various other providers.

**swyx** [00:00:00] Yeah. Uh, and then this is like signing up for the Figma MCP. Um, I, I really am trying to do like everything, um, data analysis as well. I do think, um, oh, design to code, uh, very, very good. Right? So like, here’s a Figma file, take it. And then this is where like a lot of other tasks is like knowledge work, like replace my manual clicking, but this is no, I would normally use Claude Code or uh, Claude Code for this, but because I perceive that you have better Chrome integration

**Felix** [00:00:00] mm-hmm.

**swyx** [00:00:00] I, I think you can actually do a better job of this. And I, this, this is one shot at my, uh, conference website.

**Felix** [00:00:00] That’s pretty cool. Like at some point I would love to like, hear how you feel about code. In the desktop apps, which is like I never use, which is the, the same team. Same team.

**swyx** [00:00:00] So I use the call code in terminal, which I, I perceive to be the default way of cloud coding.

**Felix** [00:00:00] So one thing this has,

**swyx** [00:00:00] sorry, I’m just like, I’m not

**Felix** [00:00:00] here, I’m not here. All products. Can I talk about other stuff? Like I, I’m not sure if people out there wanna like hear me advertise my stuff for like an hour. Please do that. Um, this thing is like a builtin browser, which is a thing a lot of products have said.

[00:00:00] Yeah, it’s a builtin browser. And I think giving cloud eyes into like what you’re actually working on makes it so much more effective. And that’s probably what you’ve seen in cohort because it can see Chrome, it can like debug the dom, it can like see things. Um, that does make it more powerful.

**swyx** [00:00:00] Yeah. So, so I think, uh, my mental model was kind broken.

[00:00:00] ‘cause I only use this cowork because I thought it had a, a browser thing in it. But I understand that the Claude Code app. The app version of Claude Code does have a built-in browser. I’ve seen, I’ve seen this preview thing.

**Felix** [00:00:00] Yeah.

**swyx** [00:00:00] I just, I’ve never used it.

**Felix** [00:00:00] But in the end, in the end, you sort of have it by hard.

[00:00:00] Yeah. You basically get the same thing. Right? Like the, the, the additional skill that you’re describing is chart is better if we can see what it’s working on. Right. That’s, that’s sort of like the summary here and like whether it’s using your Chrome

**swyx** [00:00:00] Yeah.

**Felix** [00:00:00] Or it’s just like making up its own little like browser.

[00:00:00] It doesn’t really make a big difference because either way it’s gonna see what it’s working on and that just makes it much better. And then you don’t have to run QA for your cloud.

**swyx** [00:00:00] Why doesn’t it pick up my existing Claude Code sessions? ‘cause I, I mean, obviously I’ve used Claude Code, but Excellent question.

[00:00:00] Um, don’t have a good answer other than like, we’re honest. Just haven’t Yeah. This is what the Open AI team does. Okay. Uh, cool. I I I don’t have other, like, I, I just, I, I do wanna expand people’s minds and also maybe show people if they haven’t really done it, but like, I, I think it’s very interesting how I sometimes use this more than I use, I mean, I use dia, right?

[00:00:00] Yeah. Um, I, and I use, uh, I’ve used like all the other agentic browsers and philanthropic didn’t have to build an agentic browser because you just had Claude Cowork and that’s enough.

**Felix** [00:00:00] Yeah. I also think like maybe integrating with number of excellent browsers out there, it’s like currently on my personal priority list, a little higher than like trying to rebuild a browser from scratch.

[00:00:00] Yeah. You know, never say never, but I think going back to this idea of like, we wanna plug this into an entire existing workflow, I think our goal is actually to not replace any of the applications we have in your computer. But instead of like, work really well within a new workflow,

**Alessio** [00:00:00] make the new one. Yeah.

[00:00:00] Are, it seems that nowadays, especially on the browser, most of the innovation is like user ergonomics. It’s not really like the underlying browser engine. So I feel like to call it, it doesn’t really matter if it’s like the, uh, or Chrome or Alice, whatever.

**Felix** [00:00:00] Yeah. We wanna, we wanna meet you wherever you are.

[00:00:00] Which is like, like obviously I would say that, but it’s also just generally true because I don’t wanna shrink my potential user base artificially by saying, okay, like, I’m gonna start building for the people who are willing to switch browsers.

**Alessio** [00:00:00] Right.

**Felix** [00:00:00] That’s such a, like, you know, like many lawsuits have been filed over who gets to review the browser and like a lot of money has switched hands over the question of like, which browser is default and which search engine is default within the browser.

[00:00:00] Um, I just wanna build for, yeah, I wanna build for swyx essentially. Like, I wanna, I wanna, I wanna build for people who have a number of annoying tasks that they feel like. Maybe clock could do it. Could do it for them.

**Alessio** [00:00:00] Yeah. What do you think about skills portability? I think there’s been one thing, I use another thing called zo, which is kinda like a cloud computer plus agent.

[00:00:00] And I have a skill to add visitors to the office. Yeah. So whenever somebody has to come in after hours, they need to check in downstairs. Um, but I wanna like text the thing, so it doesn’t really work in, in cowork, but now that skill is in the zone harness and it’s not in my cowork thing. And then if I make a change, it’s gotta, I gotta sync them.

[00:00:00] How do you see that going? Like I see memory as like. Cloud personal, kinda like, I don’t necessarily want my memories to be cross thing.

**Felix** [00:00:00] Yeah.

**Alessio** [00:00:00] But I do want my skills to be cross agent that I use. I think with MTPs, people do the same thing. It’s like, oh, Mt. P Gateway. Mt P registry. I don’t really know if that’s like a business.

[00:00:00] So I’m curious like if you’ve had any thoughts in the area.

**Felix** [00:00:00] I think for me, this is sort of where I go back to the really basic primitives for our skills are file-based instead of like this complicated thing that exists inside a place somewhere that is like super proprietary. I’m really leaning into the idea of like, it’s all just files and vultures, and that makes it very portable on its own.

[00:00:00] Right. We do have skills as part of this container format, which was just called plugins.

**Alessio** [00:00:00] Mm-hmm.

**Felix** [00:00:00] And plugins are available both for Claude Code and Claude Code work the same format, and you can install plugins. This works in cowork today. You can basically say, I’m gonna add a whole, like just a GitHub repo as a.

[00:00:00] Skills marketplace or like a plugin marketplace. And that’s how we’re doing portability. I think we have a lot of room left to grow in. How do we make it easy for people to know that they can write skills? How do we make it easy for them to just like, share a skill with you? Because obviously all the words I just said, right?

[00:00:00] Like I’m losing most of the knowledge worker base out there, right. And start by saying, oh, you can connect to GitHub repo. It’s not exactly how most people will end up working in like a general knowledge worker space. Um, but I think there’s something there. And another thing that’s there that I think has not really been properly explored is the, the, the combination of which part of the skill is very portable and then which part of the skill is like very personal to you.

[00:00:00] Right. And I think that’s something we haven’t really solved as an industry. Hmm.

**swyx** [00:00:00] It’s like, which, how you wanna introduce more structure to the skill or have always have like. Public skill, private skill, you know, pair. Yeah, yeah. Kind of. I think there’s

**Felix** [00:00:00] like a, like the easiest way to do this, which is we do like use string interpolation or something.

[00:00:00] Right, right. Yeah, yeah. Insert username here, insert like phone number, insert, like known folder, locations, that kind of stuff. Um, that’s probably clunky. That’s why we haven’t built it. Um, but I do think someone is going to come up with like an interesting way to keep everything we like about skills. The portability is just a file, it’s just marked down.

[00:00:00] It’s just text, honestly. Right. Like a text file words. The complete lack of structure, which means you don’t need any kind of tutorial to write a skill. Just like explain it to Claude the way he would explain it to me and Claude will probably get it before I work. Mm-hmm. Right? You’re just like, for booking a flight, tell Claude how to book a flight the same way we tell him somewhere.

[00:00:00] I just started working here today. But combine that with a very like, personal thing. Um, maybe we’ll stick with a booking a flight example. I don’t actually think. AI should be booking flights. I think the tools we have is yes.

**swyx** [00:00:00] Yeah. Finally, somebody says it. It’s the default demo that everyone’s making.

**Felix** [00:00:00] I’m

**swyx** [00:00:00] like, I even against like booking demos, it is not a good showcase.

**Felix** [00:00:00] Yeah. I’m like, I just wanna book my flight myself. But, um, I think there’s a lot of things that have a personal and a non-personal component and that’s maybe why people reach for flight booking because some things are very universal. Yeah. Super flight is usually better, right? Like few people try to book the most expensive flight.

[00:00:00] And then some things are quite personal about like what times you prefer, which seat you prefer, which airports you prefer. Combining that and like a skill format that is actually portable, compatible, easy to understand for people. I think that would be very exciting. We just haven’t figured it out yet.

**Alessio** [00:00:00] Yeah, I think the text part every, I think everybody by now has some sort of like cloud file thing. Either Dropbox, Google Drive, whatever. So it feels like in a way it should basically like sim link. My skills into all my agent harnesses. Yeah. Just keep those ing like we have internally this like valuable tokens repo, which is like all the commands sub agents.

[00:00:00] It’s good. Uh, and then I build like a TUI where you can start it and be like, you know, install this command and this three sub agents into this agent in this folder and just copy paste this. It doesn’t do anything. It literally cp the file into that. But I feel like there should be something similar where like whenever I go into a new thing, it’s like, hey, here’s like the link to exactly the cloud folder and just bring down these skills into this.

[00:00:00] Yeah. Like today it doesn’t quite work like that. Like if I install a new agent, I cannot, I have to like copy paste all the skills and I don’t even know where they are.

**Felix** [00:00:00] Yeah.

**Alessio** [00:00:00] That’s like the big problem. It’s like where do I find them?

**Felix** [00:00:00] Yeah.

**Alessio** [00:00:00] Um, so I’m curious like in the future like that, that almost feels like my personal productivity thing will be my skills.

**Felix** [00:00:00] Yeah.

**Alessio** [00:00:00] Is not really the product that I use. Everybody has access to the same product. But today there’s, that just looks like copy pasting ME files, I

**Felix** [00:00:00] think so many things I, I really like thinking about agents and LLMs just as like another coworker. So many attempts have made to build documentation companies that are like, oh, we’re gonna solve oil documentation problems.

[00:00:00] Um, I myself, like spend a little bit of time working in notion, right? I’m like deeply familiar with the concept of let’s get everyone on the same page. Mm-hmm. Right? And what you’re basically saying here is you want all your agents to be on the same page about your preferences, about the skills, about the way they ought to work and like how they ought to execute.

[00:00:00] And I’m not sure what the right thing is going to be if it’s going to be some, some company that can say, all right, we’re as an independent body, we’re not trying to like, push into any particular product. It’s our job to be like the skill authority, and we provide, I don’t know, we’re gonna be the Dropbox of skills and we can just sim link us into all the products we want to use.

[00:00:00] I’m not sure that’s gonna be viable business, but as, as an idea, it would be cool.

**Alessio** [00:00:00] Yeah. Yeah. I think so many things are just going away as businesses. It’s like, how am I supposed to do it? I’m not even asking somebody to make a product about it. Like yeah. I wanna personally know. And there’s things like you said, it’s like you almost wanna skill and then interpolate it between personal and work.

[00:00:00] So if I’m booking a fly for work, it’s different than I’m booking a flight personally.

**Felix** [00:00:00] Yeah.

**Alessio** [00:00:00] In some ways, yeah. But like a lot of the scaffolding is the same, you know? Cool.

**Felix** [00:00:00] I mean, as an engineer I will tell you like, you know, technic a person to technic a person. I will just be like siblings.

**Alessio** [00:00:00] Well that’s what, that’s what I do.

[00:00:00] We call that MD and agents that MD’s just the same how sim length. And so it is like, that works, but it feels like, yeah, I don’t know. Maybe

**Felix** [00:00:00] you can always go one, you can always tell cowork problem and then cowork will solve it for you. Just make the siblings. That’s like one way to do it.

**Alessio** [00:00:00] That’s true.

[00:00:00] That’s true. All right. Everything is called cowork.

**Felix** [00:00:00] Uh, potentially spicy. Question for both of you.

**swyx** [00:00:00] Uh, which of these industries will go away?

**Alessio** [00:00:00] Okay, so what Felix was saying before is interesting. There’s busy like. The short term pressure of like, we need to turn these tokens into valuable things, which is I should build the last mile product that harness the model.

[00:00:00] And then there’s the question of like, long term, which ones are gonna still be valuable? And I think you’re kind of seeing this today with like, uh, you know, the coding space in a way is kind of like everybody’s moving up and up in stack because you need more than just turning tokens into code. I think search, like enterprise search is kind of saying the same thing.

[00:00:00] Like with G Clean and like all these different companies is like, at the end of the day, if Cowork is the one doing all the work, the search itself is like such a small part that like, I don’t know if I’m really gonna pay that much money just to do search. It’s almost like everything is like a cowork vertical.

[00:00:00] So like how much can cowork first party support?

**swyx** [00:00:00] Mm-hmm.

**Alessio** [00:00:00] And how much can it not? I think for a lot of these things, the planning thing that you were showing do Which one? The planning. The planning.

**swyx** [00:00:00] Okay. Yeah. Yeah.

**Alessio** [00:00:00] That’s one thing where like most of the value that these agents provide is like they’re better at planning for specific tasks.

[00:00:00] Yeah. And have better tools for it.

**swyx** [00:00:00] Yeah.

**Alessio** [00:00:00] But I think the models are now moving in that direction and they have the right harnesses and they’re on your computer. So for me it’s almost like if for the end customer trusts your startup to be the provider of that task result, then I think that works. This is, uh, something that, this is a short

**swyx** [00:00:00] spike that we’re, we’re working on.

[00:00:00] Uh, yeah.

**Felix** [00:00:00] I think, look, I’ll, I’ll, I’ll tell you this, like I don’t think I’m the best person to like actually estimate which industry is going to be hit the hardest. But I do think that at philanthropic as a group of people, we’re deeply worried about the impact. That the tools are going to have on the labor market, especially for like junior employees that, because I think, I think it’s only honest to say that when we talk about automating a lot away, a lot of the work that we personally find annoying that we maybe think’s not the best use of our time.

[00:00:00] In a lot of industries, that kind of work would’ve been given to a junior entry level employee. Yeah. Right. And I think it’s, it’s only, it’s only right to be really worried about that and like worry what that’s going to do in particular to people like enter the shop market.

**Alessio** [00:00:00] Mm-hmm. I have a solution for that.

[00:00:00] Which you make them, you create simulative jobs for them.

**Felix** [00:00:00] Okay.

**Alessio** [00:00:00] So this is, this is like half joke, half true. So if you think about software engineering, when you’re like a junior engineer, you work like 1, 2, 3 years. And in those three years there’s like maybe like a handful of moments where like you really learn something.

[00:00:00] And then a bunch of other days where like you’re not really progressing.

**Felix** [00:00:00] Yeah.

**Alessio** [00:00:00] I think now we can use AI and these models to actually like shortcut these careers and almost like simulate the early years of your work and like just make them like super dense and like these learnings, it’s like, hey, we’re working on this feature, which is like a distributed system and you need to learn this thing that might take three months at a company.

[00:00:00] And so you take three months here, it’s like we’re just simulating the whole thing. It’s actually not a real thing. And in one week we kind of speed run through the whole thing and you kind of learn your lesson from there. And we kind of repeat that in like one year. You basically get like three years worth of like projects and experience.

[00:00:00] Yeah. I think it’s harder for like things like sales or for things like, you know, marketing because you don’t really have a way to get the feedback loop. But I think a lot of it, it sounds kind of silly, it’s like you’re making the new effect job, but it’s almost like you go to college, right? People pay to learn how to do it, and this might feel similar where it’s like, hey, we have the.

[00:00:00] Jane Street Simulator is like, you wanna come work at Jane Street? We’ll just put you in the simulator for like three months.

**Felix** [00:00:00] Wow.

**Alessio** [00:00:00] And you’ll come out of it. It’s like, you know, I’m ready.

**Felix** [00:00:00] So there, there is an aspect here. I’m not an expert enough to like actually know what, what is going to happen to marketing or legal or finance, right?

[00:00:00] Like, I don’t work in those jobs and I, I don’t think I should talk about them, but I am an engineer and I think I have a pretty good idea of what engineering is like. And I think one thing we’re sort of seeing is that as a company and also as, as the public, we’re like deeply worried about entry level, but we’re also seeing more senior engineers accelerate it.

[00:00:00] If like they’re more productive. They, they actually increase the value they provide. And the thing that I’m thinking about a lot is the fact that even before all of this happened, um, I’ve always had a lot of respect for the University of Waterloo and the, the new grads that have joined my teams as from coming from the University of Waterloo always felt like.

[00:00:00] More ready than new grads will like literally spend their entire time at the university regardless of how good, but never actually had to work inside an environment where you have to ship things that eventually will be used by users. And I’m, I’m, I’m German. I like initially went to German University and I think the, the, the like information systems programs, there tend to be very theoretical, right?

[00:00:00] Like I often give people the example of like trying to become a doctor, but you first have to do four years of biology and as a result when you get a new grad, you sort of have to teach them what it’s like to actually build products and to work in a company and like work with other people. And like some people will have different opinion and like, how do you do all of those things?

[00:00:00] And the University of Ulu, it seems like they just. Spend half of their time. I dunno if it’s true, but I think it’s, it’s a year, right? They spend so much time,

**swyx** [00:00:00] part of your job, uh, a cu a curriculum to do spend a year in internships.

**Felix** [00:00:00] Yeah. They just like go from company to company. They show up on your team as like a junior engineer who spend like 20 companies.

[00:00:00] Not really, but like, it seems like a lot of my new grads have also briefly worked at Apple, Google, Tesla. Yes. And uh, there’s a common meme where they like collect all these logos, like infinity stones, but, and they always put it on LinkedIn and it is very unclear that they’re an intern. Like Yeah, yeah, exactly.

[00:00:00] But it does actually make them so much better compared to other new grads. And I wonder if that’s a useful model maybe for the future when we also have to like, crunch down the amount of time you have as a junior employee. ‘cause the value you have as a junior employee is going to like, be impacted.

**swyx** [00:00:00] My sort of pro young people take is that they’re, you’re more, uh, you have higher neuroplasticity, you can learn more, you have less preexisting biases.

[00:00:00] And, uh, what I is assuming is true for you, what OpenAI often says is that. Actually it’s the, the younger, like fresh grad engineers that use Codex or their coding stuff, uh, more innovatively than the, uh, experienced engineers who have a set and preferred way of doing things.

**Felix** [00:00:00] Yeah. As I talk to people, I, I someone experience.

**swyx** [00:00:00] Yeah. So maybe you’re more AI native. Yeah. And therefore you’re, you, you get cut. But like, I think the problem is you don’t need that many of them.

**Felix** [00:00:00] I mean, philanthropic is on the record as saying we do believe that the impact on the market is going to be sizable and we do not think that people overall are ready.

[00:00:00] Right. And we do actually think we should probably talk about it as a society much more. Yeah. I’m not sure that I’m like the individual that can add like anything useful there. But I think as societies with economists and, and governments that need to wrestle those questions in a way that is probably more meaningful than me wrestling with them, we’re probably not doing good enough.

**swyx** [00:00:00] Well, we, we’ll try to educate and then I think also just releasing frequently as, as, as you guys do, or probably maybe too frequently

**Felix** [00:00:00] Yeah.

**swyx** [00:00:00] Uh, is helping people to adjust over time. Right. Rather than one big bang thing. There’s like sort of this gradual takeoff that people are living through that we

**Felix** [00:00:00] Yeah.

**swyx** [00:00:00] Waking people up. Right.

**Felix** [00:00:00] Yeah. And I, but I think a lot of us like wondering at what point do we actually have full takeoff, right? Like at what point is there, we’re all sort of expecting this like big bang moment where things will accelerate so quickly that it becomes a self-reinforcing loop.

**swyx** [00:00:00] Mm-hmm.

**Felix** [00:00:00] And at that point, it’s sort of like off to the races and there will be no more like slowly catching up.

[00:00:00] You notice just have cloud being so good at everything.

**swyx** [00:00:00] Yeah. It’s when cowork is training models, it’s when it’s looking at tensor board and Exactly. Weight and biases and training things.

**Felix** [00:00:00] I like we can all debate like how many years it’s away, right? Like some people make a better route, like maybe it’s 10 years away, maybe it’s a year away.

[00:00:00] Um, I’m not entirely sure where, where I come on this time, but I’m not totally sure that ultimately it matters all that much, whether or not it happens in four or five years. If we have a decent one, certainly that’s going to happen. It’s probably something we should wrestle with.

**swyx** [00:00:00] I wanted to talk, so by the way, the, the scheduled task complete, uh, the, the, there’s the clean my desktop task complete and it did it organized by file type, which, okay.

[00:00:00] But, you know, I was trying to get it to do more sort of thematic, like read the file, understand what it’s about, group by, uh, the, the topic rather than the file type. But

**Felix** [00:00:00] I mean, you can just follow up and have it do that. Oh yeah. Here, like it did, it is proposing That’s right.

**swyx** [00:00:00] Yeah. So it’s, it’s got some like topical things, but uh, yeah, I could probably do better.

[00:00:00] Like, yeah, so like I probably need to give it a skill to read video files so that it understands here’s how I like to,

**Felix** [00:00:00] honestly though, like, um, I see that you’re using Opus 4.6, right? Like my recommendation for people is increasingly don’t worry about it anymore. Just like tell it what you want it to do.

**swyx** [00:00:00] Yeah.

**Felix** [00:00:00] And it’s probably gonna figure out a way to do it. It might not be the way that you like necessarily or the way that you’ve gone about it.

**swyx** [00:00:00] Videos, deeper,

**Alessio** [00:00:00] lower outsourcing, organizing all of this. So let’s fight. Yeah. Yeah.

**Felix** [00:00:00] I’m honestly like, so curious what cloud is gonna come up with.

**swyx** [00:00:00] I’ll kick that off.

[00:00:00] I wanted to also just talk about the, the overall, uh, you know, you talk about data analysis, you talk about like, uh, your, your personal finances. You also said, uh, which by the way for us is very timely tax season, right? Like Yeah. Use cloud core for tax season. It is not responsible for any mistakes, but might as well, right?

[00:00:00] Like it’s, it’s free knowledge work for you. Yeah. Uh, so I just like, I think cloud for finance is a big deal. Um, and this is definitely like in that mix. I wonder, is it like, do you, is it a separate team? Do you talk to them? How important is it? Right. Like, because you can also natively output Excel files now.

**Felix** [00:00:00] Yeah.

**swyx** [00:00:00] Just

**Felix** [00:00:00] talk about the

**swyx** [00:00:00] finance effort

**Felix** [00:00:00] grow. Yeah. We care about the verticals quite a bit. So we do have a dedicated verticals team. We have a dedicated enterprise team,

**swyx** [00:00:00] and those is business engineering, not sales.

**Felix** [00:00:00] It’s engineering. Yeah, yeah, yeah. It’s engineering. So we do have people who sort of come to work every single day and they, they ask themselves, how do we make co-work extremely effective for people in those specific industries?

[00:00:00] How do we make it easier for them to understand, how do we make it easier for them to plug into this and like sort of get the same value out of it that software engineers get? I think it’s no real surprise that software engineers ended up being sort of at the forefront of the entire AI moment because so much of it is this like Rub Goldberg machine nest where like we’re already used to automating things, right?

[00:00:00] Like it’s part of our job. Yeah. So we care about it quite a bit. I think it also like really matches what we see. Cloud being very good and as a model, I think it provides tremendous amount of value to those customers in particular because. We can do so much with the amount of data they have. Those are like data heavy industries.

[00:00:00] Their industries for correctness matters quite a bit.

**swyx** [00:00:00] So for us of, I’ve used it to analyze my business, I just can’t show it. So

**Felix** [00:00:00] it’s two sense. I had a similar question about, about taxes. Like, I did tweet, I did tweet about the fact, I did tweet about, oh, COVID is doing my taxes. This is honestly incredible.

[00:00:00] And, um, it’s like annoying. He is like, this is so cool, but I’m not gonna, Twitter is maybe not the audience that needs to like see my tax return.

**swyx** [00:00:00] Yeah. That way. Here, here it is. It’s it’s reading on the videos, so it’s like Yeah, it’s getting more, yeah.

**Felix** [00:00:00] How did it actually do it? I’m actually curious.

**swyx** [00:00:00] Oh, usually it just like, takes a screenshot and then it reads the screenshot vi by vision.

[00:00:00] So this is what I do for my, my Zoom upload thing, right? Because I, I have paper club sessions that I need to upload to Zoom and I want it to automatically. Uh, title them and do show notes and everything. So it just take screenshots and try to try its best. Yeah. It wouldn’t probably benefit from transcribing, which it’s doing by, it’s operating by Pure Vision now, but it’s good enough.

**Felix** [00:00:00] Yeah.

**swyx** [00:00:00] And then I, uh, I do have to call, uh, out to Nano Banana to do images. So unless you guys do images for me, uh, I have to call other people your images.

**Felix** [00:00:00] We’re aware. We’re aware. It’s, it’s just like so fun for me because like, this is the thing that I’m increasingly doing, like increasingly curious about cloud’s, creativity and like figuring out what is great Claude’s approach is like some problem.

**swyx** [00:00:00] Yeah. Vision for everything is, is like the, the superpower, right? Like, you know, and computer use, you guys were the first to do computer use, right. And when it was launched, I was very unimpressed. I was like, it’s slow, it’s unreliable, it’s wild. How much better? ‘cause it is one year ago.

**Felix** [00:00:00] Yeah, I know. Like it was barely usable.

[00:00:00] Yeah. I, I remember it was very usable, but is it wild how much better things have gotten? Yeah.

**swyx** [00:00:00] Yeah.

**Felix** [00:00:00] Over that one year

**swyx** [00:00:00] we went to the anthropic office because you, uh, for the launch event for computer use. Like there was like this hackathon. Yeah. And like nobody hack on computer use.

**Felix** [00:00:00] But I did see, I, I I don’t know if you’re okay with me saying that, but I did see briefly that you do have like a, like an automate Mac, SMCB server installed.

[00:00:00] Right. Uhhuh, you use that ever.

**swyx** [00:00:00] What? Sorry? Which one? Where?

**Felix** [00:00:00] Um, if you go to your settings.

**swyx** [00:00:00] Oh, settings. Okay. Uh, where, sorry, this one?

**Felix** [00:00:00] Yeah.

**swyx** [00:00:00] Yeah.

**Felix** [00:00:00] Um, I noticed that in your connectors,

**swyx** [00:00:00] Uhhuh. Uh, I probably said it at one time, but I don’t use it actively.

**Felix** [00:00:00] Oh, okay. The

**swyx** [00:00:00] a max automated. Yeah. Yeah. So, so I, yeah, this one I really wanted to like, just automate everything in my thing.

[00:00:00] I didn’t find, I didn’t find it super reliable.

**Felix** [00:00:00] Okay.

**swyx** [00:00:00] Why?

**Felix** [00:00:00] No, no, no question at all.

**swyx** [00:00:00] Cloud is much better writing Apple Script and executing its own Apple Script than relying on these, uh, third party tools.

**Felix** [00:00:00] Yeah.

**swyx** [00:00:00] Uh, so I’ve increased, I, I initially installed Im CP and like all these other fcps that people built, and, but now I don’t use any of them anymore.

[00:00:00] Like just, just let cloud write its own thing.

**Felix** [00:00:00] Yeah. It’s

**swyx** [00:00:00] gonna be more custom made. We keep going up the stack,

**Felix** [00:00:00] but if using computer uses like a fairly interesting area to me, and it’s like also interesting in the sense that I don’t think we’re far away from, I don’t think we’re far away from clapping, very effective, but like using your computer and not just it’s theoretical computer.

**Alessio** [00:00:00] Mm-hmm. What’s the relationship between the user and the computer? Like, uh, there, there were some tweets about how huge some of the VMs, the Claude Cowork creates ours, like 12, 15 gigabytes and people complain. Yeah. But at some point it’s like, if you’re using the computer, you’re taking action on, it’s, it’s just your computer.

[00:00:00] And I’m just looking at it, you know, it’s like, I, I think that’s why people like the idea of like the Mac mini and the open claw or whatever on it because it’s like, it got its own home. You know? It is doing its thing, I’m doing my thing. I think there’s some kind of like, not like risk condition, but it’s like, okay, if I kickstart this task now I can’t really use the computer.

**Felix** [00:00:00] Yeah.

**Alessio** [00:00:00] You know, because car coworkers doing things on it and it’s kind of awkward, like, yeah. I’m not sure.

**Felix** [00:00:00] I, I do think it’s a super interesting area because I, I can maybe tell you like some of the things I thought about that I think are actually a bad idea. So when, when we initially started working on cowork, I, I did have some dreams about, well, would it look like for cloud of its own cursor?

[00:00:00] Could be cool, right? Like it’s a computer, we can write code, we can touch everything. Like who says that computers need to have one cursor? We could do a second cursor, but that actually breaks down quite a bit. Even if you go and like present cool dreams to both Apple and Microsoft, you’re like, wouldn’t it be cool if, um, it breaks down quite a bit?

[00:00:00] ‘cause so many of our models on a computer are built around this idea of like, there’s only one thing working on it. Yeah, there’s like a foreground app, a background app, cloud and Chrome can work in the background, but that’s like within one application. But the operating system layer, that is a lot harder to implement.

[00:00:00] So I’m, I’m still grappling with what, what does it mean for cloud to actually act on your computer. It’s the right format for cloud to have its own computer that you set up. And maybe every now and then you like zoom in and you play with it. Or is the right format for Claude to just like, wait until you are.

[00:00:00] Stepping away for a little bit and take over while you’re gone. Or it’s the right move for cloud. Just like if it’s on computer in the cloud, and like whatever you want cloud to do, you have to set up yourself. Right. There’s like a, there’s like a number of different options. Um, this is the thing I think about a lot, like what is the relationship between you and your computer and you and your data on their computer?

[00:00:00] Because how intimate that relationship is kind of depends on the tool and Right. The thing that you’re current looking at, right? Like we’re quite comfortable sharing some things, very uncomfortable, sharing other things. And I think whatever product is gonna be successful, we’ll have to deal with those, like, with those different things.

[00:00:00] But you probably, even if Claude was capable of making a determination, would you want Claude to make that determination in the first place? It’s tricky, Barry, because it’s like, it’s more than just privacy. It’s like almost intimacy and it’s like tricky to reason about in a way that will make everyone comfortable.

**Alessio** [00:00:00] Yeah, I could see. You know, a virtual box, like actual virtual box app where like you run the VM and then you have like a screen within the screen, you know, you can put it in the background, but then you can like jump in the screen and like you,

**Felix** [00:00:00] that’s not a bad idea. Yeah.

**Alessio** [00:00:00] You know, like, I mean I used it, you know, people used to do it virtualizing like C Linux in a Windows machine.

**Felix** [00:00:00] Yeah.

**Alessio** [00:00:00] And like you would just jump in and then you would jump out. But it’s like, it’s not like a dual boot. It’s like within the thing. The problem is that you need twice the amount of ram, twice the amount of, you know, it’s like, it’s kind of taxing on the machine. But I think that would be cool. Kinda like see, you know, the little quad window.

[00:00:00] I can see desktop look cute. It is clicking around things

**swyx** [00:00:00] I was gonna bring up. He’s the original machine and the machine guy, because he has the uh, windows. Windows 95 project. Where’s, where’s the Windows 85 project at?

**Felix** [00:00:00] It’s probably somewhere in my GI guitar,

**swyx** [00:00:00] right? No, no, no, no, no. It is like the first thing you see is this one.

[00:00:00] Nice. Yeah,

**Felix** [00:00:00] yeah,

**swyx** [00:00:00] exactly.

**Felix** [00:00:00] That was honestly a very fun project though. Like, obviously I didn’t, I, I should say this, just so that No, it’s the wrong impression. I did not write the actual, the actual, obviously I didn’t build Windows only five because I was a child, but also I did not build the actual engine that is capable of like simulating an X 86 processor and JavaScript and m um, that’s a tool called V 86, which is very cool and everyone should try.

[00:00:00] But this came out of a, this came out of like a debate we had at work where people were like, they often are in the into debating the merits of electron and whether or not we should be building software in JavaScript, yes or no. And I still am very upset that I can run all of Windows 95 in JavaScript.

[00:00:00] And launch Microsoft Excel inside the virtualized JavaScript Windows only five machine, and do things that pro, I can do that entire chain faster than I can do a lot of other things in like traditional SaaS applications. Mm-hmm. Uh, this is sort of like a, like a performance rampage that I went on. So I’m mostly built this as a joke for some of my colleagues at Slack.

[00:00:00] This took, took like one night. Um, what, but then that I, it was, it was not hard to do. It was all the hard work is in V 86. Yeah. Like if, go to the repo, it’s gonna say like, 99% of his work is done by, by um, a guy who goes after the, by the name. Copy. His name is Fabian.

**swyx** [00:00:00] Yeah.

**Felix** [00:00:00] Um,

**swyx** [00:00:00] cool. I think you’re, you’re kind of back on the Windows grind ‘cause you’re building out the Windows support.

[00:00:00] Uh, I thought there was some really cool technical stories to tell. Uh, and it gives people an appreciation of like, well here’s how hard it is and here’s how important here, how, how you invested the sandbox. So maybe this is like a good opportunity to talk about something in the details.

**Felix** [00:00:00] Oh yeah, the, the VM honestly is like so cool.

[00:00:00] There’s a lot of things we dislike about the vm, right? Like there, there’s a lot of things that are real trade offs and you want to know why you making those trade offs. Um, and you’re right, like a lot of people write me like, Hey, how, how come cloud is taking up 10 gigabytes? I could say on the point, it’s not actually taking up 10 gigabytes.

[00:00:00] It’s just like a way that macros displays bites is like wrong, but the way we actually ride it to disc is by we collapse the empty space and the image, so it’s not actually taking up 10 gigs. But that’s a technical differentiation. That’s probably not gonna matter to, like,

**swyx** [00:00:00] to me, the the, the outcome is it takes too long to start.

[00:00:00] Yeah. It’s like 30 seconds sometimes. So I don’t know. Oh, it should be faster than that. Whatever it be te about this feels like 30.

**Felix** [00:00:00] Yeah. Like even either way, like whatever it is, it’s going to be, it’s going to be slower than just running Log Ultra on your computer. Right. So the trade offs are real, but what we’re doing on Windows, we’re using the Windows, windows, uh, host compute system.

[00:00:00] It’s the same thing that WSL two runs on, like the Windows subsystem for Linux that I think a lot of developers appreciate quite a bit. Yeah. Um, and it’s, it’s pretty cool because we sort of like have to separate out which system space the virtual machine runs in, in who gets to talk the virtual machine because obviously you give this virtual machine a decent amount of power.

[00:00:00] How do we optimize not just the connection between the two systems, but also how do we make sure that random other application doesn’t get to talk to Clot inside the vm?

**swyx** [00:00:00] Hmm.

**Felix** [00:00:00] We do some pretty interesting things. Um, last week we started writing a new networking service. A networking driver. That optimizes how Claw talks to the internet.

[00:00:00] If your company’s doing like weird internet things like pack inspection and like, like, you know, taking your part as a cell and inside your company, I think there was probably like a very small, easy version to build of cowork that is much simpler but also breaks on most com most users, computers. And this one is quite nice because it works on most users computers.

[00:00:00] Um, and the default example I always go for is I, I really want this to be highly effective on like a, on like a machine that most people pick up. And that machine will probably not have Python, it will not have no j And even if I just take away those two things, cloud is going to be so much less effective from

**swyx** [00:00:00] your computer.

[00:00:00] So what do you do? You don’t even, I mean, may maybe require people to install Node in Python.

**Felix** [00:00:00] Oh, like, you mean for like a, what does the feature look like without a vm?

**swyx** [00:00:00] No, no, no. So, so like, like you said, right? Let’s say a target machine is whatever’s a default spec, windows laptop.

**Felix** [00:00:00] We do this, which is quite cool.

[00:00:00] So on, on, uh, mes, we use the, um, apple virtualization framework, which is pretty solid, optimized, like it’s good stuff, and instead simple a p call, right?

**swyx** [00:00:00] It’s

**Felix** [00:00:00] like super simple.

**swyx** [00:00:00] I, I saw the code recently and I’m like, that’s it. What the fuck

**Felix** [00:00:00] would you, once you start like shipping production code on it, you start adding like all of these edge cases, your new

**swyx** [00:00:00] Oh

**Felix** [00:00:00] yeah, it ends up being a little longer, but, um, I think Apple really cooked with a virtualization framework and it’s very, very good.

[00:00:00] It is very fast, it’s very reliable. And same on Windows. The, the host compute system. I think WSL two as well is maybe one of the diamonds within Windows. It’s like one of the few things that developers universally rave about is very, very cool. And like hooking into the same subsystem makes a lot easier for us to say We don’t really care how locked down your computer is.

[00:00:00] Maybe it’s like your employer’s computer and your employer has decided that you get to install nothing.

**Alessio** [00:00:00] Mm-hmm.

**Felix** [00:00:00] Not trusted, but it’s true in a lot of environments, right? Like even at Anthropic, um, our IT department controls what kinda stuff you install, just like a pretty common experience for many companies.

[00:00:00] Um, and this gives it departments a decent amount of, like, it makes their job so much easier because we can say you can separate out cloud’s computer from the user’s computer. And then for cloud’s computer, where you probably care about its data loss, you care about like a potentially hostile actor, you care about maybe data being exfiltrated.

[00:00:00] And once you control the network and the file system layer, you don’t really care necessarily anymore. That cloud might be writing super useful Python scripts. What worries you about the fact is that like once you install Python, now anyone can do anything on a computer. Once you put that in the vm, that risk really goes down.

**swyx** [00:00:00] Yeah.

**Felix** [00:00:00] So that’s why we jumped through all of these hoops.

**swyx** [00:00:00] Yeah. I think you, you had a different, uh, tweet about this. Um, but it, it’s, it’s almost like people have also approved exhaustion. Like, it’s like you can’t approve every single commands. Like sometimes by, by default, some of the theis, I think even early called code, uh, we have to approve every single command.

[00:00:00] Yeah. And, and like it’s so, so there’s this sort of dichotomy between either approve every step or dangerously get permissions.

**Felix** [00:00:00] Yeah.

**swyx** [00:00:00] And actually sandboxing is like, kind of like the middle ground.

**Felix** [00:00:00] Yeah. I do think, I do think it, it’s maybe on us as like the AI industry to come up something better than, oh, this is super safe as long as it doesn’t do anything right.

[00:00:00] Right. But if you want this to be useful, then you have to like approve every single step of the way. And like, computer use is a good example. The only way to make computer use on your host, like super safe, like really super safe is probably if you approve every single action, right. Like models, like, I would like to type the word.

[00:00:00] You’re like, okay, that seems fine. I know, I know. Which, like cursor is focused. Yeah. It’s not

**swyx** [00:00:00] automation if you don’t delegate.

**Felix** [00:00:00] Yeah, exactly. You need to like properly delegate. You need to be able to like delegate and walk away and trust that this thing is not gonna like mess dramatically. And I don’t even think we need to build perfect systems.

[00:00:00] I don’t think we need to wait for like a hundred percent model alignment. We can rely on the same Swiss cheese model we’ve used in the industry for a long time. But I do think we need to like universally maybe eventually invest more. And that’s what we’re doing. We need to invest more in systems where we can say, you do not need to approve everything.

**swyx** [00:00:00] Speaking of Swiss cheese model, he just wrote a thing about this.

**Felix** [00:00:00] Oh cool.

**swyx** [00:00:00] Yeah. Uh, yeah. Um, yeah. Super cool. I mean, yeah, it’s, it’s weird how like, I guess usually I think safety and security is kind of like a boring word to, to engineers. They’re like, just gimme be unsafe, gimme unsecure. But, um, I think.

[00:00:00] Achieving the right thing. Like you are going after a consumer slash prosumer.

**Felix** [00:00:00] Yeah. Yeah. Talking both kind of like both. I think I, I also want to capture people who would’ve no trouble using clock code like yourself, right?

**swyx** [00:00:00] Yeah. Yeah.

**Felix** [00:00:00] But still find it maybe just convenient, easier. You’re like, oh cool.

[00:00:00] That’s like the list on the right. I can edit it. Those things are just easier to do if you have

**swyx** [00:00:00] to. But this is like clearly the knowledge work side. Yeah. Claude Code will clearly capture the development workflow. But like I, I, I do think like you have to sweat this like safety and security details in order for people to trust it.

[00:00:00] And like the even Claude and Chrome, like having the whatever API uses to do the background thing.

**Felix** [00:00:00] Yeah.

**swyx** [00:00:00] Um, that’s the only reason I use it is because otherwise I would have to just get a separate machine.

**Felix** [00:00:00] Yeah.

**swyx** [00:00:00] And just run it, run to the, and that sounds like

**Felix** [00:00:00] super annoying.

**swyx** [00:00:00] Yeah. I mean, like currently doing it, but,

**Felix** [00:00:00] and I think, I think also as developers, um, maybe we’re, we are more risk tolerant, but we’re also just like accepting we are more risk tolerant, but I think we also just have.

[00:00:00] I don’t wanna say arrogance, but like sort of the trust that if like the really bad thing happens, we can probably fix it.

**swyx** [00:00:00] I just tell Claude to like, check with me before doing any irreversible action. Like sending an email or doing permanently. Yeah, it’s good enough.

**Felix** [00:00:00] But like, not even Claude, I mean like simple things such as NPM install, right?

[00:00:00] Like we’re all running NPM install with full user permissions and if it wants to like read SSH, it well crazy that that is the default kind of why. Yeah, I know. I agree. I agree. Fine. Like I’m obviously doing it every single day. No, right. Like, uh, and I think obviously NPM and GitHub too have like done a pretty good job maybe over the last couple months to like clean house and come up with like more specific tokens.

[00:00:00] But generally speaking, I think as engineers we’ve always been a little bit more risk tolerant. And if you do a little bit of introspection and you ask yourself, is that how we should be doing things, you might not always come up with the right answer. And I think for models too, like my approach, like I’m not gonna, the the safest thing is to do nothing.

[00:00:00] We do want products that are quite capable, but to the extent possible, I don’t wanna ask you, are you okay with the script? Because I kind of believe that once it starts becoming a part of your workflow, you’re probably not either, either you don’t have the skill to understand whether or not the python, the script is safe or you’re not gonna read it anyway.

**swyx** [00:00:00] Cool. I guess a, a couple partying questions. Uh, what’s the future of clockwork?

**Felix** [00:00:00] I think we’re still, we’re still such early days. We’re gonna keep shipping things that we’re gonna keep shipping, things that, um, we’re gonna keep iterating on this thing like pretty quickly, but, which I mean, you can sort of continue to expect that every single week there’s gonna be like a small new feature, if not a big new feature.

[00:00:00] Um, I’m going to continue probably to double down on your computer and like making you effective in your computer and making cloud effective in your computer. Um, we’re starting to grapple, as we talked about today, grapple more with a question of like, what does it mean? What does your computer mean? Does it have to be the one in front of you or like a VM on your computer or like a computer somewhere else?

[00:00:00] And then the third thing that I’m quite excited about is. We’re continuing to go off this hill climbing on slowly taking users who are used to asking questions and getting an answer to slowly teaching them to like step more and more away. And that claw take over like bigger and bigger tasks and work both in time as well as in like scope.

[00:00:00] And I think you can probably see most of the, our investments on our feature releases to like work on both of those things, like the ability to do more on your computer and then the ability to do more independently for longer.

**swyx** [00:00:00] Does remote control work for Claude Cowork yet? No. Right.

**Felix** [00:00:00] Excellent question.

**swyx** [00:00:00] Coming soon. I mean, that’s an obvious thing if you want to keep betting on the, on your computer, but I, to me like. You know, we, we talk about like, people are not ready this year. Like the, there’s, there’s no wall. It’s, it’s accelerating to me like what will be we be doing differently at the end of this year that, you know, we are maybe not even thinking about this, uh, at the start of this year.

[00:00:00] Right. Like, I’m just trying to look ahead as to like, what, what’s like a good use case that you’re, that we sort of aim towards? So for, for example, for the machine learning scientists, it’s always, okay, well I want AI scientists, I can automate, automate machine learning, but like for, for knowledge work, I mean, I can already, you know, get it to sign up for Google Cloud to mean as a GI.

**Felix** [00:00:00] Yeah. ‘

**swyx** [00:00:00] cause Google cuts are, but like, what, what is, what’s beyond that? I don’t know.

**Felix** [00:00:00] I think it’s basically the idea that like you still had to tell her to build your script, right? He was still kind of involved.

**swyx** [00:00:00] Yes.

**Felix** [00:00:00] In maybe a way that felt kind of magical to you, but like, maybe to me on the other side is the person building this product still feels kind of heavy handed.

[00:00:00] I see so much process that I’m like, oh, lemme take that away from you. Okay. But like, how do I just go, I will continues to go or continue to go like further and further up the stack. Make your life easier and easier.

**swyx** [00:00:00] Oh, here’s one. Right?

**Felix** [00:00:00] Yeah.

**swyx** [00:00:00] Watch, uh, I, you know, I don’t care about my own privacy or whatever, or I trust cloud, I trust philanthropic.

[00:00:00] So just watch everything I do on a normal day-to-day basis. At the end of the day, tell me what you is called co workable.

**Felix** [00:00:00] Yeah. I

**swyx** [00:00:00] dunno.

**Felix** [00:00:00] I think the funny thing about a lot of these products is that like, for good reason, I don’t enjoy, I, I don’t, throughout my entire career, I’ve never like teased too much what I’m working on because I think you should just like, yeah.

[00:00:00] Release it. Yeah. Build the base and release it, and then talk about it. Like I’m, I’m not a big fan of the like vague posting my own work ahead of time.

**swyx** [00:00:00] Yeah.

**Felix** [00:00:00] But the thing that is like always so fascinating to me is like, both of you all multiple times a day, you’ve like mentioned things and I’m like, yeah, that is obviously like very obvious

**swyx** [00:00:00] Okay.

**Felix** [00:00:00] That someone should be working on those things. Um, and I think we’re still in the space where if you look at cowork. The things that we will be releasing will probably not be a big surprise to either of you. You’re gonna be like, yeah, obviously that’s valuable obviously that we’re working on those things.

**swyx** [00:00:00] Yeah.

[00:00:00] Yeah.

**Felix** [00:00:00] And obviously that’s good and useful. And the more I hit those points, the more our features fit into that category, I think the better it is for us because then we don’t end up building things that are too hyper specialized to difficult harness style.

**swyx** [00:00:00] Yeah. I think the hyper specialized thing is very important.

[00:00:00] It keeps you like general purpose. It, it means you’re not thinking too small. Maybe I don’t, I don’t know what the, the word is.

**Felix** [00:00:00] Yeah, yeah, exactly. It’s like the whole concept that like at no point if we release, you know, there’s no Claude Code for no jazz applications that use React and 10 Stack. I know any of those two things.

[00:00:00] And like if it’s anything else, I know several startups like that. I think that’s pretty, like, I’m not a vc, I’m not an investor. It’s like hard for me to predict where the markets go. But in terms of the building box that I’m interested in, the electron is probably by far the most popular thing I ever built.

[00:00:00] And, um, electron itself is like. Very abstractable and generalizable. Right? Like so many apps run in it. And I think it would’ve been hard for me to predict how many apps actually end up using Electron.

**swyx** [00:00:00] Yeah.

**Felix** [00:00:00] Um, and what would’ve been even less useful for me to predict this in what those apps do. I distinctly remember a bloom coming out of being like, that is cool.

[00:00:00] Like you are a camera in a little circle in the corner. That is pretty smart.

**swyx** [00:00:00] That’s an app. Yeah. Yeah.

**Felix** [00:00:00] Or at least was, I’m not sure if it still is. It was for a while. Or like one password has so many interesting things. Right. It, it’s, it’s, it’s a level of the stack that I’m quite comfortable with. And whenever I give other engineers, advisors actually that layer that I think is most valuable to invest in because the tools of that layer are not that good.

[00:00:00] But that’s where you get the most leverage

**swyx** [00:00:00] for like,

**Felix** [00:00:00] the future in general.

**swyx** [00:00:00] Just quick tangent on Electron. ‘cause I always wonder this, uh, have you looked at Tori?

**Felix** [00:00:00] I have, yeah.

**swyx** [00:00:00] What’s your take? Uh, you know, look, my, my my, my view is like most things should be Tori by default, unless you really need the full power of electron, but.

**Felix** [00:00:00] Yeah, I can give like my take on, I can give my big take. Why do we ship an entire version of chromium inside the thing, right? Like why do we do that? And, um, people ask me this question a lot because it’s like very counterintuitive. Wouldn’t it be much easier to use the web use that are on the operating system?

[00:00:00] Wouldn’t it be much easier not to have to do that? And the answer is yes. And like obviously I did that once upon a time. I did that there was a version of the Slack app that used just the operating system that use Wait, did you, did you start the Slack app? I would, well, team effort and

**swyx** [00:00:00] Yeah, but I was, I was there.

[00:00:00] We built the Slack app.

**Felix** [00:00:00] Yeah. It’s crazy. Um, I mean obviously you get the electron guy to do it, but, well, but this is an interesting point. Like, by the time, by the time I joined Slack, they already had an app that was built with something at the time called Met Gap. It was a little bit like the same app gap thing for mobile.

[00:00:00] It just used the operating systems. Web views. Um, and that didn’t work for like so many reasons. Um, and they were like, all right, maybe we need like bigger guns. We need to like take more control of the rendering stack. And there’s, there’s a few things I always mention here. Um, I think if you’re building a small app, just going with the operating systems web view is perfectly fine.

[00:00:00] If you’re building an app, maybe that doesn’t have too many users who will like cry bloody murder. If it doesn’t work, that is fine. The reason to go with your own embedded rendering engine is because, and this is still true in 2026, the operating system render engines are not that good. They’re just not that good.

[00:00:00] Both Microsoft and Apple are trying to move away from that. They so far really haven’t, the only way to upgrade those is to upgrade your operating system. So if you are, say Slack and you have critical rendering bug in WK WebU and some of the other WebU options, your only recourse is to tell your customer, oh, sorry, you’re too poor.

[00:00:00] You didn’t bother the, its MacBook. Unacceptable.

**swyx** [00:00:00] Mm-hmm.

**Felix** [00:00:00] Unacceptable to user, unacceptable to user developer. So you sort of need to like go down the stack and like find the best rendering engine, then put it in your app. Why chromium, even though it’s very big chromium is by far the best thing. Like I, I often like to remind people the unreal engine, you wanna render some text.

[00:00:00] They use chromium. Like chromium is part of the unreal engine for same purposes. Chromium is very, very good. I think it’s like one of the marvels of engineering. It’s very hard for, we’re in San Francisco right now where we’re recording. Most of the people in the city are web developers. It’s hard for me to like overstate how magical it is.

[00:00:00] They run seat like rendering a YouTube video dynamically. Negotiating a bit rate, figuring out what to do about your extremely broken hardware driver. Actually, this is a fun thing. Um, okay, you can enter Chrome call on Wack Wack GPU. Okay? And if you scroll down a little bit, these are all the enabled workarounds because something is going wrong on your computer.

[00:00:00] If you’re doing this on a Windows computer with like A GPU, that is not the most popular GPO, it will be much longer. And all of these are usually just there to make sure that if I say as a developer, I want a red pixel to appear here, that that actually happens. Chrome is such a marvel because of works on all the machines that user might throw you and it’s gonna work fairly reliably.

[00:00:00] And if it doesn’t, they will probably fix it within 24 hours.

**swyx** [00:00:00] I see. So this is the super operating system, right? That that works everywhere.

**Felix** [00:00:00] Yeah.

**swyx** [00:00:00] Right. Okay. Yeah.

**Felix** [00:00:00] So a lot of the magic of Electron is honestly just that it makes it very easy for you to ch chromium in a way that serves you exactly in your use cases.

[00:00:00] Elect, uh, exactly.

**swyx** [00:00:00] Our next interview is with Morgan Dreesen.

**Felix** [00:00:00] Yeah.

**swyx** [00:00:00] Who had the phrase like, desktop OSS are just poorly deep, uh, poor implications of the, the actual os, which is Chrome, which like actually works everywhere. And this is this, this is the platform where you ship apps.

**Felix** [00:00:00] I, I think the wild thing is that like as engineers, we so often sort of assume that the platform, like the layer below us is like super stable.

[00:00:00] Mm-hmm. And then you talk to those people and they’re like, ah, we are also just like guessing. Um, uh, and I had like a distinct moment at Slack where one of our customers at Slack was Nvidia, and for a while I really put GPU developers on this pedestal in my head. And I do think they’re still probably much smarter than I am.

[00:00:00] But I was like hardware engineers who built the chips, who then like built the drivers. Their work must be so much harder than mine. They must be very good. And we had like one bug in Slack where like if you had a YouTube video in Slack, it wouldn’t quite render why. Like it would have these weird artifacts.

[00:00:00] And, um, that ended up being a chromium bug. And I ended up on this like giant thread. So I got to see a lot of the source code. And they also are just like common to do. We don’t know why this is weird, but if you flip this bit, things work. You know, this is just like happening with every layer of the stack.

[00:00:00] Maybe the, uh, you know, the,

**swyx** [00:00:00] the end of year a GI prediction is that clock can build chromium. You see, you see you, you laugh now. But yeah, like, you know, someday

**Felix** [00:00:00] it’s, it’s sounding, it could get pretty good. Like it used to be completely useless. Um, mostly just like overwhelmed, both with how hyper specialized tools are inside the chromium repo.

[00:00:00] Like for, for a long time. Chrome has like sort of reinvent all the tools because none of them are capable of ending Chrome. I think the EGI moment I am kind of waiting for is at what point are we gonna say Electron is probably no longer necessary because you can just build fully native apps. The Swifty?

[00:00:00] Yeah. Like not just in Swift because this is one thing, like it’s pretty easy if you, I think our current models are quite capable of taking an electron app and replicating it Swift, are they gonna be capable of like building an app that is actually more performant, which is less memory? All of that stuff, um, is gonna go into the same hyper optimization that developers have done for like a long time.

[00:00:00] We’re not quite there yet. Work and like point even our best models at a thing and say, just replicate this, a native code. Make no mistakes. Ultra think. Right? We’re not quite there yet. Um, ultra

**swyx** [00:00:00] think is bad

**Felix** [00:00:00] today. Think is back. Yes. Okay.

**swyx** [00:00:00] Or we’ll get an ultra think for like days,

**Felix** [00:00:00] just a pretty long time before,

**swyx** [00:00:00] but he worked on Ultra think for days.

[00:00:00] Yeah. Why he just, it’s just. Front,

**Alessio** [00:00:00] I’ll let it, the

**Felix** [00:00:00] more goes into

**swyx** [00:00:00] it. Yeah. Okay.

**Alessio** [00:00:00] Another question I had is like coworks. So if I have my Claude Cowork, like what’s kinda like the multiplayer mode? I think sub agents is like single player Split up the context.

**Felix** [00:00:00] Yeah.

**Alessio** [00:00:00] And the multiplayer cowork is like, my colleague is some file on their machine that I wanna know about or I wanna know how their task is going to then update my thing.

[00:00:00] Like is that interesting? Is that something that makes sense for you to build or for like

**Felix** [00:00:00] It’s like super interesting to me it, it almost goes back to like some of the scaffolding room. Like okay, are we gonna be end up, are we, will we end up building scaffolding that will just go away? And like a question I have here is at what point do we just assign these things, like their own Gmail account?

[00:00:00] We just give them their like Slack handle and then they will just like use the same tools we humans use to interact with each other. You mentioned our finance people, they’ve been working pretty hard on very good office integrations. And I think for a while we’ve been like, we built so much tech around cloud, leaving useful comments inside a Google Doc, and now it just does, it just like leaves a comment in your Google Doc and that’s how you interact with it.

[00:00:00] Maybe like the similar thing where I still have open questions around what is the best interaction mode? Is it for us to build something super custom for cowork agents to talk to each other? Or is it okay, let’s just jump straight to the finish line and say, well, we’re just gonna give this thing, if you use Slack at work, we’re just gonna give this thing a Slack handle.

[00:00:00] And that’s going to be the way, it’s like multiplayer capable.

**Alessio** [00:00:00] They communicate with each other. Yeah. Yeah. Like, you know, as a, as a fun project, I build this thing called piq, which basically takes any repo and the PI agent, uh, coding agent, it puts it in a VPS, and then there’s a public web hook where anybody can submit a coding task.

[00:00:00] Oh. And then there’s a dashboard in which you review the task and then piq pi, pi, uh, queue.

[00:00:00] Yeah. You basically get all these like tasks, anybody can submit a task.

**Felix** [00:00:00] Mm-hmm.

**Alessio** [00:00:00] And to me it’s almost like in the organization of the future, it’s like the sales people are talking to the engineering team that is talking to the marketing team, to the product team, and all these coworker are going to like queue up decisions for other people to approve in a way.

**Felix** [00:00:00] Yeah.

**Alessio** [00:00:00] You know, and I’m kind of curious what that looks like and like how do you, how do I give my cowork the ability to build a proof task without asking me

**Felix** [00:00:00] Yeah.

**Alessio** [00:00:00] And how to decide which one I need to review. Yeah. You know, because for some of these things it’s like, you know, you wanna change the color of something that’s kinda like a branding decision.

[00:00:00] Or another one is like, hey, your thing is just broken. It’s like, this is like how you fix it. Yeah. And Claude can actually review whether or not that prompt matches what he’s trying to do today. Everything is still very, it’s like multiplayer within the single player, you know? Yeah. I guess spin up many of them, but like, how do I get multiple people to hand off to each other things using their particular context?

**Felix** [00:00:00] Yeah. And for both of your coworkers to like talk to each other. Right,

**Alessio** [00:00:00] right. Yeah. Hey, we got an episode today. Can you like, have you, you know, or

**Felix** [00:00:00] Yeah. This is like a, uh, I know we’re like running out of time here, but like we, we previously talked about sharing skills and I did have this question of like, what if your cowork would just like ask the other coworks if they have a skill for this task?

[00:00:00] Doesn’t matter. These could do.

**swyx** [00:00:00] Right. Like, okay, so skill transfer.

**Felix** [00:00:00] Yeah, like,

**swyx** [00:00:00] um, and again, that’s, maybe

**Felix** [00:00:00] this maybe goes back into the territory of like building something very powerful and building something creepy often goes hand in hand. Um, because I could tell from the reaction that my fellow engineers said that this is probably not what we’re gonna do, but like.

[00:00:00] We have Bluetooth le right? Like I, this computer can figure out that it’s sitting right next to this computer. So you’re probably working on the same thing. Um, well, you see that in cowork, probably not. But, um, there’s like, I think really creative solutions to problems that we really haven’t tried yet.

[00:00:00] Yeah,

**Alessio** [00:00:00] yeah, yeah. Yeah.

**swyx** [00:00:00] Excellent. I guess the, the last thing is, uh, philanthropic labs. Uh, I always have this mental model of a model lab versus, uh, agent lab. And this is basically Anthropics internal agent lab, which co Claude Code, uh, is now under, right? It’s part of the whole org.

**Felix** [00:00:00] I mean, people are so fungible, right?

[00:00:00] Like,

**swyx** [00:00:00] okay, this is just, I, I don’t know how, I don’t know real. This is, I don’t know.

**Felix** [00:00:00] No, it’s a real team. It’s a very, um, the, the last team is primarily working though on things that you don’t see in public yet. Um, they’re trying like really wild out there, ideas that seem quite improbable. Um, the mad science

**swyx** [00:00:00] thing.

[00:00:00] But you, you’re, are you officially under this thing or

**Felix** [00:00:00] No? We’re, where is the Claude Code is, but now Claude Code is like a fairly big group where. I actually know many people we are like, like I remember yesterday coming into our weekly COVID meeting. I was like, woo,

**Alessio** [00:00:00] this is hot.

**Felix** [00:00:00] There’s a lot of people here.

[00:00:00] Um, but we still have a labs team and we actually made the labs team a lot bigger. Mike just joined the labs team as a, as an ic, which I think is very cool and very fun. But they’re, they’re working on things that you have not seen yet that are extremely out there and probably half broken. Right? Like the sort of the idea of a lab team is that it should only work on things that make really no sense for anyone else to work on.

**swyx** [00:00:00] Okay. Well, looking for exciting things from there, but thank you so much. I know we’re out of time, but uh, appreciate your joining us. I appreciate co cowork, everyone go use it. Uh, it is the closest I’ve felt to a I this year. That’s so nice you to say. Thank you very much. Yeah. Thank you for your time. Yeah.
