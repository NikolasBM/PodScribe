---
podcast: "how-i-ai"
podcast_title: "How I AI"
title: "How a solo founder used Codex and ChatGPT to launch a fashion brand without engineers | Yana Welinder"
date: 2026-08-17
url: "https://podcasters.spotify.com/pod/show/pen-name/episodes/How-a-solo-founder-used-Codex-and-ChatGPT-to-launch-a-fashion-brand-without-engineers--Yana-Welinder-e3nc7u2"
guid: "433928ee-1f1f-4634-a06d-4e3d2c317d3e"
host: "Claire Vo"
guests: ["Yana Welinder"]
format: "interview"
level: 2
length: "00:32:24"
categories: ["design", "coding", "agents"]
featured: ["OpenAI Codex", "computer use", "ChatGPT"]
mentioned: ["Nano Banana"]
transcript_source: "azure-asr"
transcribed_by: "MAI-Transcribe-2"
---

# How a solo founder used Codex and ChatGPT to launch a fashion brand without engineers | Yana Welinder

**Yana Welinder** [00:00:00] Normally, I would hire a technical team, like engineers. I didn't, right? I sort of just came to Codex and asked it to build the website. The idea is to use AI really anywhere in the process where that makes sense. Literally my technical co-founder.

**Claire Vo** [00:00:15] There's so much you couldn't do before, practically, from a cost perspective, even from an execution perspective, that is now totally possible, and so you can like unlock your creativity in a way that wasn't possible before.

**Yana Welinder** [00:00:29] Really does unlock so much creativity. A lot of my designs start from a hand-drawn sketch, but the other piece of this is I sort of developed the fashion prompt that's behind it, and it describes a lot of sort of what goes into a garment. So it has like the silhouette, the proportion or the volume of the dress, like kind of like the fabric, how it flows, how it behaves, the construction details, how it moves, even how it sounds. The other piece that is still unsolved, and I'm sort of still banging my head against the wall, is to get it to create patterns based on my design. And there I'm kind of running humans and AI in parallel. So I am working with human pattern makers, Codex, and just saying, who's going to get to making my thing fastest?

**Claire Vo** [00:01:17] Welcome to How I AI. I'm Claire Vo, product leader and AI obsessive, here on a mission to help you build better with these new tools. Today I have Yana Wellender, and she is building an AI-native fashion startup, and she's going to show us how AI can intersect art, creativity, and real-world production, and why computer use plus software means SaaS really isn't dead, at least not yet. Let's get to it.

[00:02:17] Yana, thanks for joining How I AI. I'm an art and fashion girl. You know this. There are like 5 of us AI art and fashion girls on Twitter, and we all find each other, but I am one, and I love what you're working on. So immerse us in this new thing that you're working on, and then we'll talk about how you're using AI in this really unique fashion.

**Yana Welinder** [00:03:00] Cool. Yeah, I'm so excited to be here. Thanks for having me. I am building this AI native fashion brand, and the idea is to use AI really anywhere in the process where that makes sense. So obviously heavily in the design and production process, but also it's literally my technical co-founder, and so I, that's what I use it for, everything.

**Claire Vo** [00:03:26] And can you show us, like, it's probably hard for people to conceptualize what, like, an AI-powered fashion brand looks like. Can you just, like, show us a little bit of kind of like some of the stuff that you're working on, and then we can get into how it actually, how you actually got there?

**Yana Welinder** [00:03:41] So this is Yana Bana, the fashion brand, and you can kind of see, like, everything here is built with AI, and so you have some of the different garments that I designed, and I'll show later that, like, different ones start from different, like, from different inspiration or from different points. And so oftentimes I start from a sketch. You can see that when you hover over some of these. So I start with a hand-drawn, humanly, manually, you know, old school hand-drawn sketch, and then I use AI to turn that into different types of fashion collateral and kind of technical specs and everything along the line to ultimately get to a garment. And I kind of use AI for all the things to visualize it, to create photos, to create videos of some of these garments. There, a lot of them kind of allude to different, like, technical, you know, computer things in a lot of ways because I feel like that should be really part of the theme.

[00:04:41] It should be obvious that what it comes from, and so the fabrics will use a lot of kind of the punch card, like computer punch card patterns and things like that, so that you can really see that. And the other way in which it sort of appears is you can see, for example, for this like post keyboard t-shirt, which I'm wearing myself right now, it also is alluding to the fact that now we are not going to be using keyboards and a lot of this stuff, but can we now have, like, give it a second life, essentially, and to make sure that it's like obvious, the world we live in and the world we're entering.

**Claire Vo** [00:05:20] And I just want to pause because when I first saw this, I was like, what a fun, like, little art project. Like, I once made this, like, I vibe coded this app, which was Anthropic as an anthropology website because I thought it was very funny. But you're actually bringing these designs to life. Like, you are actually wearing this keyboard shirt, which is super cool. And so what, you know, I hear a lot of people who are in the creative fields be really fearful of AI because I think it is like displacement in a lot of ways. Like, let's all be honest here. There's like videos and sketching and all sorts of stuff that AI can do, and yet, if you step on the other side of this like post-keyboard future, there's so much you couldn't do before practically, from a cost perspective, even from an execution perspective, that is now totally possible, and so you can like unlock your creativity in a way that wasn't possible before. So I want you to show us step by step kind of what goes into creating a garment like this, creating and imagining a design like this, and then actually getting it to production and getting a website like this up.

**Yana Welinder** [00:06:31] I think you're absolutely right that it really does unlock so much creativity. A lot of my designs start from a hand-drawn sketch, but the other piece of this is I sort of kind of developed this technical, it's essentially a stack, but I've, for the purpose of visualizing what it looks like, I have this sort of set up as just like the fashion prompt that's behind it, and it describes a lot of sort of what goes into a garment. So it has like the silhouette, the proportion or the volume of the dress, like kind of like the fabric, how it flows, how it behaves, the construction details, how it moves, even how it sounds. I can show in one of the pieces it kind of has this really interesting kind of sound as you're walking in the dress. And I take all of this and put it together in essentially kind of when we, if we take it out of my flow, you can see that it's at the core of it, there's sort of this prompt that we could take and plug into ChatGPT.

[00:07:44] And oftentimes in when I'm working with this, I will also have an actual sketch of what I want, and I sort of am then defining this in addition to the sketch. But just for the sake of us kind of playing in real time, I just thought it'd be cool to just just use prompts to start with. So here we have a sharply tailored, waist-defined jacket with exaggerated shoulders and blah, blah, blah, right? So now we're putting this in. Oh, I should have told it to make an image, but maybe it'll figure out to do that. Yeah, there we go. Sometimes it's smarter than you think, even on instant. And so now it's going to generate an image, and oftentimes this will give me kind of like a product photo, but usually what I then want to do with this is to then take it to kind of the next level, and I will have very specific types of like collateral that I want to get out of it. So once we have this ready, I will ask it to generate a Vogue style runway photo. Oh, there we go. So this is kind of like the product photo of this.

[00:08:46] so it has these exaggerated shoulders, the waist, a lot of kind of the stuff that I asked it to. And if I had a specific sketch, it would really adhere to my sketch much more so than what was in the prompt. But then if we go to here, we say, like, now make it into a Vogue style. Can you tell that I normally do not type anymore? And so I usually just use voice for all these things.

**Claire Vo** [00:09:14] Well,

**Yana Welinder** [00:09:15] So it's just, like, so

**Claire Vo** [00:09:16] voice.

**Yana Welinder** [00:09:16] hard.

**Claire Vo** [00:09:16] It's easier for our podcast guests, um, when you use voice because they don't have to imagine what you're typing. So she's- you know, you're typing, "Make it into a Vogue style photo.

**Yana Welinder** [00:09:27] Of a model walking down the runway in this outfit. And so then I kind of just, like, iterate on this, and there's, um, I go to photo, um, that's a runway photo, then I go to, like, a, uh, influencer photo, and you kind of see this in a lot of- from a lot of different angles and also iterate on it based on kind of what you're seeing. Now make it, you know, red, make it shorter, make it longer, and all those different things, but I usually just start from a specific point and then iterate from there.

**Claire Vo** [00:10:02] I have a question for you, which is, why ChatGPT and why Image Gen 2 as the model you're using? There's a lot of Image Gen models out there. why that particular one?

**Yana Welinder** [00:10:15] Yeah, so I've done a lot of experimentation with lots and lots of different image models, and what I found was ultimately Nano Banana and Image 2.0, really Image 1.5 was already pretty good at this, are the best at following visual directions. And often I'm not doing this. Usually I'm sort of, as I mentioned, I'm mostly giving them a physics, like a sketch that I want them to turn into a picture. And what Image 1.5 did better than Nano Banana and Image, images, ChatGPT Images 2.0 does even better is it really well follows the sketch. In fact, it follows the sketch sometimes a little bit too precisely, and so you get something that doesn't look like fabric anymore, and you have to kind of be like, no, no, no, no, no, you gotta like, it's gotta flow. Like, this is kind of why I have this very detailed kind of prompting, where I tell it how the fabric should flow, because otherwise it can get into the mindset of, oh, she really wants it to look like paper, you know?

[00:11:21] But the flip side, though, with all the other image models that I've tried is that they will make it look beautiful and realistic, but it will look very, very different from my design. And obviously, when you're designing fashion, you need it to look new and different. You don't need it to look like the most similar thing that's walked the runway some other time, and that's usually what you get with a lot of other image models.

**Claire Vo** [00:11:43] What I love, and if you can go back to your prompt, um, flow,

**Yana Welinder** [00:11:46] Yeah.

**Claire Vo** [00:11:46] what I love about this is this is just- okay, so people are gonna be like, "I'm not a fashion designer, I don't have any use for this." What I think is the takeaway here generally for folks is write down your process and write down what a definition of complete or good is. Y- you and I, like, you were product ladies,

**Yana Welinder** [00:12:05] A product people, yeah, it's a stack.

**Claire Vo** [00:12:06] Once upon a time, we were like official product ladies, and you need a spec, like your prompt is a spec. And so if you can put into the effort of saying, like, what makes a really good garment? Like, what makes a really good photo? What makes a really good illustration? And come up with like five things that you can define for the prompt, you can get a really good output of AI. And then what I love, my friend Zach says, what's good for AI is good for humans. Like, let's just say you had- you were gonna have a human sketch this out or build this. This is the exact information they would need as well to do a good job. And so whether or not you're doing, like, fashion illustrations or coding, right? Like this- at the spec, the PRD matters, people, like the spec matters. And so getting- forcing yourself to sit down and be a little bit more precise is gonna get you that exact outcome that you want. And, you know, to be honest, I think that jacket's pretty rad. I would, I'd wear it.

[00:13:10] I love it. So you've created this image. I also love this idea of taking like a core image and iterating it through like runway photo, influencer photo, like, you know, standalone catalog, like photo product shot.

[00:14:19] What do you do next? Like, what's the next part of your flow?

**Yana Welinder** [00:14:22] So a lot of what I do is kind of iterate on it. And so I have this like, you know, change the color, change the, you know, change the fabric. And so I have kind of a lot of these different ways to do that. But then the next piece really comes to kind of like, what is the production process? And the production process is going to be very different depending on what I'm doing. And so, to give you an idea from one of these, so for example, I had this dress that actually did not come from a sketch. It came from, I had this one day where I was just being bombarded with Ruth Asaba's artwork in different places. Like, I went to, I went with my son to this like kids event, and there was an exhibit across the street that I like accident, like we were just early, so we went and watched it, and we were like, at SFMOMA, there's like a permanent exhibit there. He had a piano recital, and the church had one of her pieces hanging like literally almost above my head, and I was like, I keep, I don't know.

[00:15:29] And so this was literally from my phone, so I didn't have a sketch, right? Normally I start with a sketch, but in this case I was like, you know, make a photo of a model walking down the runway in a dress inspired by Ruth Asaba's loop-wired sculptures. And it was important that it had a beige undergarment because otherwise ChatGPT will not, like, it's like, no, you're trying to make me make nude pictures, and I don't do that.

**Claire Vo** [00:15:56] Very artistic nude pictures.

**Yana Welinder** [00:15:59] Just, no, I don't do that. actually, I think even here I tried to make it to remove the sculptures in the background, and I was like, we're sorry, this violates our nudity guidelines, right? This is like happens all the time.

**Claire Vo** [00:16:11] I have to tell you.

**Yana Welinder** [00:16:12] It's very, very frustrating.

**Claire Vo** [00:16:14] Quick side, you know what, if I showed up to a date with my husband in this gown, I do not think he would be thrilled. I don't think he'd be like, "Ooh. It's not quite,

**Yana Welinder** [00:16:22] True, exactly,

**Claire Vo** [00:16:23] not quite the erotic

**Yana Welinder** [00:16:23] exactly,

**Claire Vo** [00:16:24] vibe

**Yana Welinder** [00:16:24] right?

**Claire Vo** [00:16:24] that

**Yana Welinder** [00:16:24] It's like- it's not- exactly, it's not- it's not, um, it's not nudity, it's not, you know, it's not torn, um, but-

**Claire Vo** [00:16:32] No.

**Yana Welinder** [00:16:33] but here we are. And so- so this one, right? Like, this is- uh, and I think that, um, uh, a lot of garments you would do, like, some- some garments I will drape, right? Like on the model behind me, or some garments go into they become, you create a kind of a pattern, and I have different some AI processes and some non-AI processes that I've done for patterns. But this garment is previously unmanufacturable. And so what I, and I ended up kind of taking this and also creating a video of it. This is kind of like, you can see a little bit more of how what it looks like. But the next step for this particular garment will be to take it and 3D print it. And the particularly these kind of big ball pieces will need to be 3D printed. And so I then went on to Codex and had it help me create CAD

**Claire Vo** [00:17:36] No.

**Yana Welinder** [00:17:36] files for these balls. So I first prepped it and had it like, I was like, okay, so I made that into sketch, then I made these pieces into, into kind of more sketch illustrations. Then I, it didn't do well, it still didn't do well. We had a bunch of back and forth. Eventually, it started doing something that was a little bit more similar. I had to do, this is a really, really long process, and then ultimately I had it using computer use, go and build this in 3D software so that I could create like an STL file and send off to 3D print. So that's the process for this particular garment, to sort of to 3D print it.

**Claire Vo** [00:18:22] I have to, again, like I have to pause because if we're just talking about the creative, like, generation process, again, this is now a garment that would have been previously, like, almost inconceivable to make. Not just because it was, it's difficult to construct, but even if you were like, of course, we could 3D print that before AI, we could 3D print it after AI, the, like, tedium of creating the CAD models was so onerous that like even getting to the point where you could execute on it is really hard. And so I just think this moment of like unlocking the previously impossible, whether the impossible was technically impossible or if it was just like practically infeasible, is super important. The other thing that I love, bless computer use and like Codex plus computer use, love you so much because I can just be like, I don't need to know how to use this software, like you go use that software, you do whatever you want.

[00:19:26] I've gone through this like trough of despair of like SaaS is dead, maybe like we're never gonna touch a website again to you know what, like agents are really good at pressing buttons, so like a software is back for, but agents are gonna use it. It's very, very kind of like interesting shift I'm seeing.

**Yana Welinder** [00:19:43] I think that that's a great point, and one fascinating piece is that a lot of these things, like for actual end product, like a CAD file, Codex, as amazing as it is, is not great at generating a final CAD file if you asked it to do it on its own. But if you use, yeah, if you use computer use and have it go and do it in a piece of software that's designed for that purpose, and I have both for like actually for 3D printing, and there's a fashion software called Claw that I've used as well, and it generates this like, it generates patterns, and it then fits them on the 3D model. And I tell Codex to go and use the software that I haven't learned how to use myself, and it does such a great job at something that it itself couldn't do. So it's sort of like SaaS in combination with Codex works so well on a lot of these things that don't, and I'm sure it's just a matter of time, but that's where we are today.

[00:20:45] And I want to do it today. I don't want to wait. I don't want to wait like a year, you know.

**Claire Vo** [00:20:49] I love it so much. Okay, so you like generated an idea, we've sketched it, we've created images, we've even started to prototype the construction of it. How are you getting something built? And maybe not the gown, like, maybe this, like, keyboard shirt that you're wearing. Like, how are we actually getting this manufactured?

**Yana Welinder** [00:21:08] Yeah. So for something like that, um, what I've done, and I do this a lot, is I will go and now, uh, now this same tool be- is becomes my research assistant, and I ask it to identify, like, you know, find 10 US-based custom apparel manufacturing companies that are similar to the one that I liked, but I want to see if there's other ones. And then I just like, there's a bunch of things I want, and I kick off a deep research on extra high so that it's extra high while doing it, and not in that way. and then I get back a bunch of things, but usually so for a lot of my work, I end up like I'm doing something else. So I'm like, I am kicking off this research, and then I go and like drape fabric on model, or I do like I'm on my sewing machine doing prototypes, like I'm doing something else. And so a lot of them, kind of the next steps end up being via voice.

[00:22:12] And so I, like in this case, I came back to it and I was like, well, do you see the, because I'm talking, apparel and using voice, right? Like the apparel manufacturers that I asked you to find. Now, can you like put together an email that I can, that you can send off to them, but like you may want to make sure that you get my approval to do that. And then I have, and then I use browser, uh, use to let it go into Superhuman and, like, set all of these up for me, but I really want to click the send button before.

**Claire Vo** [00:22:42] The send button. I love

**Yana Welinder** [00:22:44] Just to

**Claire Vo** [00:22:44] this.

**Yana Welinder** [00:22:45] check its work.

**Claire Vo** [00:22:46] Again, like, something that is just so tedious, and, you know, if I was like- you're much more diligent at this than I am, but if I was like, "Oh my gosh, I have this vision. We're gonna make- we're gonna make these keyboard shirts. They're gonna be amazing." And then I'd be like, how can I make it? And they're like, ugh, I have to like look up vendors. I would just practically give up because it feels so boring. But

**Yana Welinder** [00:23:08] So boring.

**Claire Vo** [00:23:08] If you can, if you can get that work off to someone, again, like the next step and the next step and the next step, and then what you're going to end up with is this like incredible business. And so I just am like so inspired by people like you that take AI and create like a niche and like can then take that and build out a business where maybe one wouldn't have been available or possible before, I just think is super cool. Okay, so you're doing this vendor outreach, you're actually going to get this thing, this thing produced. Side note for all the cool girls out there, when they're ready, we all want one. Put me on the- put me on the pre-order- pre-order list.

**Yana Welinder** [00:23:49] There actually is. I'm gonna- I'm gonna- I'm gonna be that person, but you can pre-order it.

**Claire Vo** [00:23:54] Amazing. Perfect. Okay, and then last kind of- kind of flow you have is, like, again, going back to, like, pre-orders and how to actually run this business, how are you using it to, like, be your technical co-founder in all this?

**Yana Welinder** [00:24:08] That's- I- I- I gotta say that that's probably, like, my favorite piece because this- I mean, apart from the fact that it is like there's so much AI in this, but it's basically like an AI native like Everlane or something, right? Like normally I would hire like a technical team, like engineers. I would have possibly have it, I probably wouldn't, let's be real, I wouldn't have a technical co-founder, but like I could have had a technical co-founder. I'm a solo founder girl, like this is just my nature.

**Claire Vo** [00:24:38] It's the life.

**Yana Welinder** [00:24:40] It's the life, but I would hire engineers, and I didn't, right? Like, I had it build this website, and I did it, and I sort of just came to Codex and asked it to build the website. There's a lot of pieces here that aren't just like a static website in that it, like, you can obviously pre-order things, and I could, like, add Stripe to it, which is, like, in prior lives have been, like, a tedious big exercise, but I can go back and kind of show you the Stripe flow. But adding that was just like, you know, a second. I had to create, like, databases to be able to, like, track votes as people are voting on these different garments, so I can decide, kind of figure out which are the most popular ones to bring to life. And so, like, I had to do that. in an earlier phase of this, I had to create a separate dashboard for me to track the votes in real time. and so I did that.

[00:25:40] Now I really just like, I just use voice and I'm like, oh, hey, how many votes do I have for this thing now, right? So like, why would I even have a dashboard? I know. So I don't do that, but like, just to kind of show you like the Stripe flow as an example of like, yeah, I came here and I was like, oh yeah, I use browser to add Stripe to my site. It was like, I don't know, you're like, I'm not signed in. I'm like, no, you gotta sign in in my own in-app browser. I'm like, no, no, no, you got go to mine. I'm already signed up there. And then I was like, yeah, you gotta do it. I'm like, no, you can do it. You know, now just like back and forth. It's like, "No, no, you can do it." Um, and, and yeah, this is it. And then I had done, everything's added, and now pre-order is live. This is like a very, very fast process, and literally whenever I like need to change something about like the process, I can really just come here and just like list out all the things I want to change, and it goes off and it finds the Vercel project.

[00:26:49] It has, like, finds the repository in GitHub and does all the things. I will say, like, this weekend, my son built his own websites by using like ChatGPT sites, and I'm sort of just like sitting there going like, do I, should I really like, do I want to migrate off of herself? Do I really want like- you know, like, is this- is this a whole new- like now- like now a 9-year-old can have his technical co-founder like do this and like build a company for him, right? Like just- it's just so cool to see this all evolve, you know?

**Claire Vo** [00:27:26] Your 9-year-old and my 9-year-old are going to be best buds. We can create like a Codex club for fourth graders.

**Yana Welinder** [00:27:33] We should.

**Claire Vo** [00:27:32] 4th graders, for

**Yana Welinder** [00:27:33] We should

**Claire Vo** [00:27:34] 4th graders.

**Yana Welinder** [00:27:34] totally do that.

**Claire Vo** [00:27:35] Um, this is a very- sorry, we are doing San Francisco, uh, Silicon Valley moming stuff right now. I just wanna- I wanna, like, go back to one thing because ripped from the headlines, Codex prompting, I too am like, "Hey, Codex, do this thing," and it's like, "Nah, no thanks, I can't." And I'm like, "No, I'm pretty sure you can." And then, like,

**Yana Welinder** [00:27:55] Yes, you can.

**Claire Vo** [00:27:55] after 2, like, "I'm pretty sure you can," it's like, "You're right, I can." I, um, I'm gonna post about this later, but I have this, like, smart light bulb. You can see it's on my- on my thing.

**Yana Welinder** [00:28:04] Mhm.

**Claire Vo** [00:28:04] And I was like, "Hack it." And it was like, "No, I really shouldn't." I was like, "You can do it." And it was like, "Done." So- So just be a little bit insistent, um,

**Yana Welinder** [00:28:15] Yes.

**Claire Vo** [00:28:15] you know, and- and you can get- get stuff done. This has been so, so fun. Again, just, like, recapping for folks, a business that I think, like, would probably be inconceivable before AI, fully stacked from the creative process, creating images, creating videos, imagining product ideas, all the way through like hardcore manufacturing and sourcing vendors to just like being able to voice note your virtual CTO and update anything you need to do and have your engineering team on demand in ChatGPT. Pretty incredible. I want to get through some lightning round questions, and then we're going to get you out of here. You know, my first question for you is like, what is the hardest part of this? Like, what is still, maybe like, what is still hard? What isn't solved? What, where are you still feeling friction?

**Yana Welinder** [00:29:03] So I'd say it's kind of two things. One is that, like, getting it to really do, getting image models to do really unique things per your vision while still making it realistic. That has been really, really hard. I feel like I've solved it, like I've kind of cracked that nut, but it still is, and every now and again, I'm sort of still get something that is really two-dimensional or whatever, and I have to really refine it. the other piece that is still unsolved, and I'm sort of still banging my head against the wall, is to get it to create patterns. So to get it to create like actually accurate patterns based on my design. And there I'm kind of running humans and AI in parallel, so I am working with human pattern makers and Codex and just saying, who's going to get to like making my thing fastest, like most accurate, like to my vision, you know? And so that's been really cool to see. I'm not there yet with either, actually, with either flow.

[00:30:04] So.

**Claire Vo** [00:30:05] Okay. I love it. All right, and then my last question that I ask everybody, speaking of like when it's hard and when it fails you and not getting there quite yet, which is, how do you prompt AI when it's not working? What's your- are you nice? Are you a nice mom or a mean mom?

**Yana Welinder** [00:30:21] I can be both, but I think I'm mostly a nice mom, and the reason is that I find that I get better output. So, uh, like, I mean, I am very direct, and I'm sort of like, "Yes, you can," uh, you know, "You go do that." Like, I'm not just like, "Oh, yeah, I'm gonna do this for you." Um, but I'm c- I will be, like, very polite. I will still say please and thank you. Um, and I do think that it's because, like- ...the- the- it's- it's trained on body of text, and so if it sees poor text output that is, like, rude and mean, it will, like, kind of get in the mind frame of that part of the internet, right? Like, versus, like, kind of more professional business context, and then it will deliver something that's a little bit more what I want it to be. So that's that I do it for selfish reasons,

**Claire Vo** [00:31:12] I love

**Yana Welinder** [00:31:12] not

**Claire Vo** [00:31:12] it.

**Yana Welinder** [00:31:13] because I'm afraid of the future AI overlords.

**Claire Vo** [00:31:17] Perfect. Well, this has been super, super fun and inspirational and just like a breath of fresh air in terms of a new use case, a creative space that we haven't seen before, and something sort of like manifesting the world. So where can we find you and how can we be helpful to you?

**Yana Welinder** [00:31:32] You can find me on X mostly. I am Yana Bana on X. I am now Yana Bana at X. I changed my handle to match the brand. but yeah, uh, but yeah, the- in- in terms of just, like, helpfulness is getting feedback on all the stuff. Like, you can come- you can come to Yanabana and, like, vote on the garments that you like, um, so I can get feedback on, like, what's- what's working for people and what's not. Like, I'm all about user feedback and customer input. Um, and yeah, uh, tell me- tell me what you like.

**Claire Vo** [00:32:06] I love it. Well, I love Poppy Love.

**Yana Welinder** [00:32:10] That's

**Claire Vo** [00:32:11] Smash that like button. It is very cool.

**Yana Welinder** [00:32:13] Awesome. Thank you.

**Claire Vo** [00:32:14] Awesome.

**Yana Welinder** [00:32:14] I will, I'll let you know when that one is ready to go.

**Claire Vo** [00:32:17] Available for purchase. Perfect. Well, thank you so much for joining How I AI.

**Yana Welinder** [00:32:22] Thanks for having me.

**Claire Vo** [00:32:24] Thanks so much for watching. If you enjoyed the show, please like and subscribe here on YouTube, or even better, leave us a comment with your thoughts. You can also find this podcast on Apple Podcasts, Spotify, or your favorite podcast app. Please consider leaving us a rating and review, which will help others find the show. You can see all our episodes and learn more about the show at howiaipod.com. See you next time.
