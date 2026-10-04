---
podcast: "latent-space"
podcast_title: "Latent Space"
title: "NVIDIA's AI Engineers: Agent Inference at Planetary Scale and \"Speed of Light\" — Nader Khalil (Brev), Kyle Kranen (Dynamo)"
date: 2026-03-10
url: "https://www.latent.space/p/nvidia-brev-dynamo"
guid: "substack:190477229"
host: "Swyx"
transcript_source: "publisher"
---

# NVIDIA's AI Engineers: Agent Inference at Planetary Scale and "Speed of Light" — Nader Khalil (Brev), Kyle Kranen (Dynamo)

## Agent Security Basics

**Nader** [00:00:00] Agents can do three things. They can access your files, they can access the internet, and then now they can write custom code and execute it. You literally only let an agent do two of those three things. If you can access your files and you can write custom code, you don’t want internet access because that’s one to see full vulnerability, right?

[00:00:00] If you have access to internet and your file system, you should know the full scope of what that agent’s capable of doing. Otherwise, now we can get injected or something that can happen. And so that’s a lot of what we’ve been thinking about is like, you know, how do we both enable this because it’s clearly the future.

[00:00:00] But then also, you know, what, what are these enforcement points that we can start to like protect?

**swyx** [00:00:00] All right.

## Podcast Welcome and Guests

**swyx** [00:00:00] Welcome to the Lean Space podcast in the Chromo studio. Welcome to all the guests here. Uh, we are back with our guest host Viu. Welcome. Good to have you back. And our friends, uh, Netter and Kyle from Nvidia. Welcome.

**Kyle** [00:00:00] Yeah, thanks for having us.

**swyx** [00:00:00] Yeah, thank you. Actually, I don’t even know your titles.

[00:00:00] Uh, I know you’re like architect something of Dynamo.

**Kyle** [00:00:00] Yeah. I, I’m one of the engineering leaders and a architects of Dynamo.

**swyx** [00:01:00] And you’re director of something and developers, developer tech.

**Nader** [00:01:00] Yeah.

**swyx** [00:01:00] You’re the developers, developers, developers guy at nvidia,

**Nader** [00:01:00] open source agent marketing, brev,

**swyx** [00:01:00] and like

**Nader** [00:01:00] Devrel tools and stuff.

**swyx** [00:01:00] Yeah. Been

**Nader** [00:01:00] the focus.

**swyx** [00:01:00] And we’re, we’re kind of recording this ahead of Nvidia, GTC, which is coming to town, uh, again, uh, or taking over town, uh, which, uh, which we’ll all be at. Um, and we’ll talk a little bit about your sessions and stuff. Yeah.

**Nader** [00:01:00] We’re super excited for it.

## GTC Booth Stunt Stories

**swyx** [00:01:00] One of my favorite memories for Nader, like you always do like marketing stunts and like while you were at Rev, you like had this surfboard that you like, went down to GTC with and like, NA Nvidia apparently, like did so much that they bought you.

[00:01:00] Like what, what was that like? What was that?

**Nader** [00:01:00] Yeah. Yeah, we, we, um. Our logo was a chaka. We, we, uh, we were always just kind of like trying to keep true to who we were. I think, you know, some stuff, startups, you’re like trying to pretend that you’re a bigger, more mature company than you are. And it was actually Evan Conrad from SF Compute who was just like, you guys are like previous

**swyx** [00:01:00] guest.

[00:01:00] Yeah.

**Nader** [00:01:00] Amazing. Oh, really? Amazing. Yeah. He was just like, guys, you’re two dudes in the room. Why are you pretending that you’re not? Uh, and so then we were like, okay, let’s make the logo a shaka. We brought surfboards to our booth to GTC and the energy was great. Yeah. Some palm trees too. They,

**Kyle** [00:02:00] they actually poked out over like the, the walls so you could, you could see the bread booth.

[00:02:00] Oh, that’s so funny. And

**Nader** [00:02:00] no one else,

**Kyle** [00:02:00] just from very far away.

**Nader** [00:02:00] Oh, so you remember it back

**Kyle** [00:02:00] then? Yeah I remember it pre-acquisition. I was like, oh, those guys look cool,

**Nader** [00:02:00] dude. That makes sense. ‘cause uh, we, so we signed up really last minute, and so we had the last booth. It was all the way in the corner. And so I was, I was worried that no one was gonna come.

[00:02:00] So that’s why we had like the palm trees. We really came in with the surfboards. We even had one of our investors bring her dog and then she was just like walking the dog around to try to like, bring energy towards our booth. Yeah.

**swyx** [00:02:00] Steph.

**Kyle** [00:02:00] Yeah. Yeah, she’s the best,

**swyx** [00:02:00] you know, as a conference organizer, I love that.

[00:02:00] Right? Like, it’s like everyone who sponsors a conference comes, does their booth. They’re like, we are changing the future of ai or something, some generic bullshit and like, no, like actually try to stand out, make it fun, right? And people still remember it after three years.

**Nader** [00:02:00] Yeah. Yeah. You know what’s so funny?

[00:02:00] I’ll, I’ll send, I’ll give you this clip if you wanna, if you wanna add it in, but, uh, my wife was at the time fiance, she was in medical school and she came to help us. ‘cause it was like a big moment for us. And so we, we bought this cricket, it’s like a vinyl, like a vinyl, uh, printer. ‘cause like, how else are we gonna label the surfboard?

[00:03:00] So, we got a surfboard, luckily was able to purchase that on the company card. We got a cricket and it was just like fine tuning for enterprises or something like that, that we put on the. On the surfboard and it’s 1:00 AM the day before we go to GTC. She’s helping me put these like vinyl stickers on.

[00:03:00] And she goes, you son of, she’s like, if you pull this off, you son of a bitch. And so, uh, right. Pretty much after the acquisition, I stitched that with the mag music acquisition. I sent it to our family group chat. Oh

**swyx** [00:03:00] Yeah. No, well, she, she made a good choice there. Was that like basically the origin story for Launchable is that we, it was, and maybe we should explain what Brev is and

**Nader** [00:03:00] Yeah.

[00:03:00] Yeah. Uh, I mean, brev is just, it’s a developer tool that makes it really easy to get a GPU. So we connect a bunch of different GPU sources. So the basics of it is like, how quickly can we SSH you into a G, into a GPU and whenever we would talk to users, they wanted A GPU. They wanted an A 100. And if you go to like any cloud provisioning page, usually it’s like three pages of forms or in the forms somewhere there’s a dropdown.

[00:04:00] And in the dropdown there’s some weird code that you know to translate to an A 100. And I remember just thinking like. Every time someone says they want an A 100, like the piece of text that they’re telling me that they want is like, stuffed away in the corner. Yeah. And so we were like, what if the biggest piece of text was what the user’s asking for?

[00:04:00] And so when you go to Brev, it’s just big GPU chips with the type that you want with

**swyx** [00:04:00] beautiful animations that you worked on pre, like pre you can, like, now you can just prompt it. But back in the day. Yeah. Yeah. Those were handcraft, handcrafted artisanal code.

**Nader** [00:04:00] Yeah. I was actually really proud of that because, uh, it was an, i I made it in Figma.

[00:04:00] Yeah. And then I found, I was like really struggling to figure out how to turn it from like Figma to react. So what it actually is, is just an SVG and I, I have all the styles and so when you change the chip, whether it’s like active or not it changes the SVG code and that somehow like renders like, looks like it’s animating, but it, we just had the transition slow, but it’s just like the, a JavaScript function to change the like underlying SVG.

[00:04:00] Yeah. And that was how I ended up like figuring out how to move it from from Figma. But yeah, that’s Art Artisan.

**Kyle** [00:05:00] Speaking of marketing stunts though, he actually used those SVGs. Or kind of use those SVGs to make these cards.

**Nader** [00:05:00] Oh yeah. Like

**Kyle** [00:05:00] a GPU gift card Yes. That he handed out everywhere. That was actually my first impression of that

**Nader** [00:05:00] one.

[00:05:00] Yeah,

**swyx** [00:05:00] yeah, yeah.

**Nader** [00:05:00] Yeah.

**swyx** [00:05:00] I think I still have one of them.

**Nader** [00:05:00] They look great.

**Kyle** [00:05:00] Yeah.

**Nader** [00:05:00] I have a ton of them still actually in our garage, which just, they don’t have labels. We should honestly like bring, bring them back. But, um, I found this old printing press here, actually just around the corner on Ven ness. And it’s a third generation San Francisco shop.

[00:05:00] And so I come in an excited startup founder trying to like, and they just have this crazy old machinery and I’m in awe. ‘cause the the whole building is so physical. Like you’re seeing these machines, they have like pedals to like move these saws and whatever. I don’t know what this machinery is, but I saw all three generations.

[00:05:00] Like there’s like the grandpa, the father and the son, and the son was like, around my age. Well,

**swyx** [00:05:00] it’s like a holy, holy trinity.

**Nader** [00:05:00] It’s funny because we, so I just took the same SVG and we just like printed it and it’s foil printing, so they make a a, a mold. That’s like an inverse of like the A 100 and then they put the foil on it and then they press it into the paper.

[00:06:00] And I remember once we got them, he was like, Hey, don’t forget about us. You know, I guess like early Apple and Cisco’s first business cards were all made there. And so he was like, yeah, we, we get like the startup businesses but then as they mature, they kind of go somewhere else. And so I actually, I think we were talking with marketing about like using them for some, we should go back and make some cards.

**swyx** [00:06:00] Yeah, yeah, yeah. You know, I remember, you know, as a very, very small breadth investor, I was like, why are we spending time like, doing these like stunts for GPUs? Like, you know, I think like as a, you know, typical like cloud hard hardware person, you go into an AWS you pick like T five X xl, whatever, and it’s just like from a list and you look at the specs like, why animate this GP?

[00:06:00] And, and I, I do think like it just shows the level of care that goes throughout birth and Yeah. And now, and also the, and,

**Nader** [00:06:00] and Nvidia. I think that’s what the, the thing that struck me most when we first came in was like the amount of passion that everyone has. Like, I think, um, you know, you talk to, you talk to Kyle, you talk to, like, every VP that I’ve met at Nvidia goes so close to the metal.

[00:06:00] Like, I remember it was almost a year ago, and like my VP asked me, he’s like, Hey, what’s cursor? And like, are you using it? And if so, why? Surprised at this, and he downloaded Cursor and he was asking me to help him like, use it. And I thought that was, uh, or like, just show him what he, you know, why we were using it.

[00:07:00] And so, the amount of care that I think everyone has and the passion, appreciate, passion and appreciation for the moment. Right. This is a very unique time. So it’s really cool to see everyone really like, uh, appreciate that.

**swyx** [00:07:00] Yeah.

## Acquisition and DevEx Shift

**swyx** [00:07:00] One thing I wanted to do before we move over to sort of like research topics and, uh, the, the stuff that Kyle’s working on is just tell the story of the acquisition, right?

[00:07:00] Like, not many people have been, been through an acquisition with Nvidia. What’s it like? Uh, what, yeah, just anything you’d like to say.

**Nader** [00:07:00] It’s a crazy experience. I think, uh, you know, we were the thing that was the most exciting for us was. Our goal was just to make it easier for developers.

[00:07:00] We wanted to find access to GPUs, make it easier to do that. And then all, oh, actually your question about launchable. So launchable was just make one click exper, like one click deploys for any software on top of the GPU. Mm-hmm. And so what we really liked about Nvidia was that it felt like we just got a lot more resources to do all of that.

[00:07:00] I think, uh, you know, NVIDIA’s goal is to make things as easy for developers as possible. So there was a really nice like synergy there. I think that, you know, when it comes to like an acquisition, I think the amount that the soul of the products align, I think is gonna be. Is going speak to the success of the acquisition.

[00:08:00] Yeah. And so it in many ways feels like we’re home. This is a really great outcome for us. Like we you know, I love brev.nvidia.com. Like you should, you should use it’s, it’s the

**Kyle** [00:08:00] front page for GPUs.

**Nader** [00:08:00] Yeah. Yeah. If you want GP views,

**Kyle** [00:08:00] you go there, get

**swyx** [00:08:00] it there, and it’s like internally is growing very quickly.

[00:08:00] I, I don’t remember You said some stats there.

**Nader** [00:08:00] Yeah, yeah, yeah. It’s, uh, I, I wish I had the exact numbers, but like internally, externally, it’s been growing really quickly. We’ve been working with a bunch of partners with a bunch of different customers and ISVs, if you have a solution that you want someone that runs on the GPU and you want people to use it quickly, we can bundle it up, uh, in a launchable and make it a one click run.

[00:08:00] If you’re doing things and you want just like a sandbox or something to run on, right. Like open claw. Huge moment. Super exciting. Our, uh, and we’ll talk into it more, but. You know, internally, people wanna run this, and you, we know we have to be really careful from the security implications. Do we let this run on the corporate network?

[00:08:00] Security’s guidance was, Hey, run this on breath, it’s in, you know, it’s, it’s, it’s a vm, it’s sitting in the cloud, it’s off the corporate network. It’s isolated. And so that’s been our stance internally and externally about how to even run something like open call while we figure out how to run these things securely.

[00:09:00] But yeah,

**swyx** [00:09:00] I think there’s also like, you almost like we’re the right team at the right time when Nvidia is starting to invest a lot more in developer experience or whatever you call it. Yeah. Uh, UX or I don’t know what you call it, like software. Like obviously NVIDIA is always invested in software, but like, there’s like, this is like a different audience.

[00:09:00] Yeah. It’s a

**Nader** [00:09:00] wider

**Kyle** [00:09:00] developer base.

**swyx** [00:09:00] Yeah. Right.

**Nader** [00:09:00] Yeah. Yeah. You know, it’s funny, it’s like, it’s not, uh,

**swyx** [00:09:00] so like, what, what is it called internally? What, what is this that people should be aware that is going on there?

**Nader** [00:09:00] Uh, what, like developer experience

**swyx** [00:09:00] or, yeah, yeah. Is it’s called just developer experience or is there like a broader strategy here

**Nader** [00:09:00] in Nvidia?

[00:09:00] Um, Nvidia always wants to make a good developer experience. The thing is and a lot of the technology is just really complicated. Like, it’s not, it’s uh, you know, I think, um. The thing that’s been really growing or the AI’s growing is having a huge moment, not because like, let’s say data scientists in 2018, were quiet then and are much louder now.

[00:10:00] The pie is com, right? There’s a whole bunch of new audiences. My mom’s wondering what she’s doing. My sister’s learned, like taught herself how to code. Like the, um, you know, I, I actually think just generally AI’s a big equalizer and you’re seeing a more like technologically literate society, I guess.

[00:10:00] Like everyone’s, everyone’s learning how to code. Uh, there isn’t really an excuse for that. And so building a good UX means that you really understand who your end user is. And when your end user becomes such a wide, uh, variety of people, then you have to almost like reinvent the practice, right? Yeah. You have

**Kyle** [00:10:00] to, and actually build more developer ux, right?

[00:10:00] Because the, there are tiers of developer base that were added. You know, the, the hackers that are building on top of open claw, right? For example, have never used gpu. They don’t know what kuda is. They, they, they just want to run something.

**Nader** [00:10:00] Yeah.

**Kyle** [00:10:00] You need new UX that is not just. Hey, you know, how do you program something in Cuda and run it?

[00:10:00] And then, and then we built, you know, like when Deep Learning was getting big, we built, we built Torch and, and, but so recently the amount of like layers that are added to that developer stack has just exploded because AI has become ubiquitous. Everyone’s using it in different ways. Yeah. It’s

**Nader** [00:11:00] moving fast in every direction.

[00:11:00] Vertical, horizontal.

**Vibhu** [00:11:00] Yeah. You guys, you even take it down to hardware, like the DGX Spark, you know, it’s, it’s basically the same system as just throwing it up on big GPU cluster.

**Nader** [00:11:00] Yeah, yeah, yeah. It’s amazing. Blackwell.

**swyx** [00:11:00] Yeah. Uh, we saw the preview at the last year’s GTC and that was one of the better performing, uh, videos so far, and video coverage so far.

[00:11:00] Awesome. This will beat it. Um,

**Nader** [00:11:00] that was

**swyx** [00:11:00] actually, we have fingers

**Nader** [00:11:00] crossed. Yeah.

## DGX Spark and Remote Access

**Nader** [00:11:00] Even when Grace Blackwell or when, um, uh, DGX Spark was first coming out getting to be involved in that from the beginning of the developer experience. And it just comes back to what you

**swyx** [00:11:00] were involved.

**Nader** [00:11:00] Yeah. St. St.

**swyx** [00:11:00] Mars.

**Nader** [00:11:00] Yeah. Yeah. I mean from, it was just like, I, I got an email, we just got thrown into the loop and suddenly yeah, I, it was actually really funny ‘cause I’m still pretty fresh from the acquisition and I’m, I’m getting an email from a bunch of the engineering VPs about like, the new hardware, GPU chip, like we’re, or not chip, but just GPU system that we’re putting out.

[00:11:00] And I’m like, okay, cool. Matters. Now involved with this for the ux, I’m like. What am I gonna do here? So, I remember the first meeting, I was just like kind of quiet as I was hearing engineering VPs talk about what this box could be, what it could do, how we should use it. And I remember, uh, one of the first ideas that people were idea was like, oh, the first thing that it was like, I think a quote was like, the first thing someone’s gonna wanna do with this is get two of them and run a Kubernetes cluster on top of them.

[00:12:00] And I was like, oh, I think I know why I’m here. I was like, the first thing we’re doing is easy. SSH into the machine. And then, and you know, just kind of like scoping it down of like, once you can do that every, you, like the person who wants to run a Kubernetes cluster onto Sparks has a higher propensity for pain, then, then you know someone who buys it and wants to run open Claw right now, right?

[00:12:00] If you can make sure that that’s as effortless as possible, then the rest becomes easy. So there’s a tool called Nvidia Sync. It just makes the SSH connection really simple. So, you know, if you think about it like. If you have a Mac, uh, or a PC or whatever, if you have a laptop and you buy this GPU and you want to use it, you should be able to use it like it’s A-A-G-P-U in the cloud, right?

[00:12:00] Um, but there’s all this friction of like, how do you actually get into that? That’s part of Revs value proposition is just, you know, there’s a CLI that wraps SSH and makes it simple. And so our goal is just get you into that machine really easily. And one thing we just launched at CES, it’s in, it’s still in like early access.

[00:13:00] We’re ironing out some kinks, but it should be ready by GTC. You can register your spark on Brev. And so now if you

**swyx** [00:13:00] like remote managed yeah, local hardware. Single pane of glass. Yeah. Yeah. Because Brev can already manage other clouds anyway, right?

**Vibhu** [00:13:00] Yeah, yeah. And you use the spark on Brev as well, right?

**Nader** [00:13:00] Yeah. But yeah, exactly. So, so you, you, so you, you set it up at home you can run the command on it, and then it gets it’s essentially it’ll appear in your Brev account, and then you can take your laptop to a Starbucks or to a cafe, and you’ll continue to use your, you can continue use your spark just like any other cloud node on Brev.

[00:13:00] Yeah. Yeah. And it’s just like a pre-provisioned center

**swyx** [00:13:00] in your

**Nader** [00:13:00] home. Yeah, exactly.

**swyx** [00:13:00] Yeah. Yeah.

**Vibhu** [00:13:00] Tiny little data center.

**Nader** [00:13:00] Tiny little, the size of

**Vibhu** [00:13:00] your phone.

## SOL Culture and Dynamo Setup

**swyx** [00:13:00] One more thing before we move on to Kyle. Just have so many Jensen stories and I just love, love mining Jensen stories. Uh, my favorite so far is SOL. Uh, what is, yeah, what is S-O-L-S-O-L

**Nader** [00:13:00] is actually, i, I think of all the lessons I’ve learned, that one’s definitely my favorite.

**Kyle** [00:14:00] It’ll always stick with you.

**Nader** [00:14:00] Yeah. Yeah. I, you know, in your startup, everything’s existential, right? Like we’ve, we’ve run out of money. We were like, on the risk of, of losing payroll, we’ve had to contract our team because we l ran outta money. And so like, um, because of that you’re really always forcing yourself to I to like understand the root cause of everything.

[00:14:00] If you get a date, if you get a timeline, you know exactly why that date or timeline is there. You’re, you’re pushing every boundary and like, you’re not just say, you’re not just accepting like a, a no. Just because. And so as you start to introduce more layers, as you start to become a much larger organization, SOL is is essentially like what is the physics, right?

[00:14:00] The speed of light moves at a certain speed. So if flight’s moving some slower, then you know something’s in the way. So before trying to like layer reality back in of like, why can’t this be delivered at some date? Let’s just understand the physics. What is the theoretical limit to like, uh, how fast this can go?

[00:14:00] And then start to tell me why. ‘cause otherwise people will start telling you why something can’t be done. But actually I think any great leader’s goal is just to create urgency. Yeah. There’s an infinite

**Kyle** [00:15:00] create compelling events, right?

**Nader** [00:15:00] Yeah.

**Kyle** [00:15:00] Yeah. So l is a term video is used to instigate a compelling event.

[00:15:00] You say this is done. How do we get there? What is the minimum? As much as necessary, as little as possible thing that it takes for us to get exactly here and. It helps you just break through a bunch of noise.

**swyx** [00:15:00] Yeah.

**Kyle** [00:15:00] Instantly.

**swyx** [00:15:00] One thing I’m unclear about is, can only Jensen use the SOL card? Like, oh, no, no, no.

[00:15:00] Not everyone get the bullshit out because obviously it’s Jensen, but like, can someone else be like, no, like

**Kyle** [00:15:00] frontline engineers use it.

**Nader** [00:15:00] Yeah. Every, I think it’s not so much about like, get the bullshit out. It’s like, it’s like, give me the root understanding, right? Like, if you tell me something takes three weeks, it like, well, what’s the first principles?

[00:15:00] Yeah, the first principles. It’s like, what’s the, what? Like why is it three weeks? What is the actual yeah. What’s the actual limit of why this is gonna take three weeks? If you’re gonna, if you, if let’s say you wanted to buy a new computer and someone told you it’s gonna be here in five days, what’s the SOL?

[00:15:00] Well, like the SOL is like, I could walk into a Best Buy and pick it up for you. Right? So then anything that’s like beyond that is, and is that practical? Is that how we’re gonna, you know, let’s say give everyone in the company a laptop, like obviously not. So then like that’s the SOL and then it’s like, okay, well if we have to get more than 10, suddenly there might be some, right?

[00:16:00] And so now we can kind of piece the reality back.

**swyx** [00:16:00] So, so this is the. Paul Graham do things that don’t scale. Yeah. And this is also the, what people would now call behi agency. Yeah.

**Kyle** [00:16:00] It’s actually really interesting because there’s a, there’s a second hardware angle to SOL that like doesn’t come up for all the org sol is used like culturally at a

**swyx** [00:16:00] media for everything.

[00:16:00] I’m also mining for like, I think that can be annoying sometimes. And like someone keeps going IOO you and you’re like, guys, like we have to be stable. We have to, we to fucking plan. Yeah.

**Kyle** [00:16:00] It’s an interesting balance.

**Nader** [00:16:00] Yeah. I encounter that with like, actually just with, with Alec, right? ‘cause we, we have a new conference so we need to launch, we have, we have goals of what we wanna launch by, uh, by the conference and like, yeah.

[00:16:00] At the end of the day, where is

**swyx** [00:16:00] this GTC?

**Nader** [00:16:00] Um, well this is like, so we, I mean we did it for CES, we did for GT CDC before that we’re doing it for GTC San Jose. So I mean, like every, you know, we have a new moment. Um, and we want to launch something. Yeah. And we want to do so at SOL and that does mean that some, there’s some level of prioritization that needs to happen.

[00:17:00] And so it, it is difficult, right? I think, um, you have to be careful with what you’re pushing. You know, stability is important and that should be factored into S-O-L-S-O-L isn’t just like, build everything and let it break, you know, that, that’s part of the conversation. So as you’re laying, layering in all the details, one of them might be, Hey, we could build this, but then it’s not gonna be stable for X, y, z reasons.

[00:17:00] And so that was like, one of our conversations for CES was, you know, hey, like we, we can get this into early access registering your spark with brev. But there are a lot of things that we need to do in order to feel really comfortable from a security perspective, right? There’s a lot of networking involved before we deliver that to users.

[00:17:00] So it’s like, okay. Let’s get this to a point where we can at least let people experiment with it. We had it in a booth, we had it in Jensen’s keynote, and then let’s go iron out all the networking kinks. And that’s not easy. And so, uh, that can come later. And so that was the way that we layered that back in.

[00:17:00] Yeah. But

**Kyle** [00:17:00] It’s not really about saying like, you don’t have to do the, the maintenance or operational work. It’s more about saying, you know, it’s kind of like highlights how progress is incremental, right? Like, what is the minimum thing that we can get to. And then there’s SOL for like every component after that.

[00:18:00] But there’s the SOL to get you, get you to the, the starting line. And that, that’s usually how it’s asked. Yeah. On the other side, you know, like SOL came out of like hardware at Nvidia. Right. So SOL is like literally if we ran the accelerator or the GPU with like at basically full speed with like no other constraints, like how FAST would be able to make a program go.

**swyx** [00:18:00] Yeah. Yeah. Right.

**Kyle** [00:18:00] So

**swyx** [00:18:00] in, in training that like, you know, then you work back to like some percentage of like MFU for example.

**Kyle** [00:18:00] Yeah, that’s a, that’s a great example. So like, there’s an, there’s an S-O-L-M-F-U, and then there’s like, you know, what’s practically achievable.

**swyx** [00:18:00] Cool. Should we move on to sort of, uh, Kyle’s side?

[00:18:00] Uh, Kyle, you’re coming more from the data science world. And, uh, I, I mean I always, whenever, whenever I meet someone who’s done working in tabular stuff, graph neural networks, time series, these are basically when I go to new reps, I go to ICML, I walk the back halls. There’s always like a small group of graph people.

[00:18:00] Yes. Absolute small group of tabular people. And like, there’s no one there. And like, it’s very like, you know what I mean? Like, yeah, no, like it’s, it’s important interesting work if you care about solving the problems that they solve.

**Kyle** [00:19:00] Yeah.

**swyx** [00:19:00] But everyone else is just LMS all the time.

**Kyle** [00:19:00] Yeah. I mean it’s like, it’s like the black hole, right?

[00:19:00] Has the event horizon reached this yet in nerves? Um,

**swyx** [00:19:00] but like, you know, those are, those are transformers too. Yeah. And, and those are also like interesting things. Anyway, uh, I just wanted to spend a little bit of time on, on those, that background before we go into Dynamo, uh, proper.

**Kyle** [00:19:00] Yeah, sure. I took a different path to Nvidia than that, or I joined six years ago, seven, if you count, when I was an intern.

[00:19:00] So I joined Nvidia, like right outta college. And the first thing I jumped into was not what I’d done in, during internship, which was like, you know, like some stuff for autonomous vehicles, like heavyweight object detection. I jumped into like, you know, something, I’m like, recommenders, this is popular. And

**swyx** [00:19:00] yeah, he did Rexi

**Kyle** [00:19:00] as well.

[00:19:00] Yeah, Rexi. Yeah. I mean that, that was the taboo data at the time, right? You have tables of like, audience qualities and item qualities, and you’re trying to figure out like which member of the audience matches which item or, or more practically which item matches which member of the audience. And at the time, really it was like we were trying to enable.

[00:20:00] Uh, recommender, which had historically been like a little bit of a CP based workflow into something that like, ran really well in GPUs. And it’s since been done. Like there are a bunch of libraries for Axis that run on GPUs. Uh, the common models like Deeplearning recommendation model, which came outta meta and the wide and deep model, which was used or was released by Google were very accelerated by GPUs using, you know, the fast HBM on the chips, especially to do, you know, vector lookups.

[00:20:00] But it was very interesting at the time and super, super relevant because like we were starting to get like. This explosion of feeds and things that required rec recommenders to just actively be on all the time. And sort of transitioned that a little bit towards graph neural networks when I discovered them because I was like, okay, you can actually use graphical neural networks to represent like, relationships between people, items, concepts, and that, that interested me.

[00:20:00] So I jumped into that at Nvidia and, and got really involved for like two-ish years.

**swyx** [00:21:00] Yeah. Uh, and something I learned from Brian Zaro Yeah. Is that you can just kind of choose your own path in Nvidia.

**Kyle** [00:21:00] Oh my God. Yeah.

**swyx** [00:21:00] Which is not a normal big Corp thing. Yeah. Like you, you have a lane, you stay in your lane.

**Nader** [00:21:00] I think probably the reason why I enjoy being in a, a big company, the mission is the boss probably from a startup guy. Yeah. The mission

**swyx** [00:21:00] is the boss.

**Nader** [00:21:00] Yeah. Uh, it feels like a big game of pickup basketball. Like, you know, if you play one, if you wanna play basketball, you just go up to the court and you’re like, Hey look, we’re gonna play this game and we need three.

[00:21:00] Yeah. And you just like find your three. That’s honestly for every new initiative that’s what it feels like. Yeah.

**Vibhu** [00:21:00] It also like shows, right? Like Nvidia. Just releasing state-of-the-art stuff in every domain. Yeah. Like, okay, you expect foundation models with Nemo tron voice just randomly parakeet.

[00:21:00] Call parakeet just comes out another one, uh, voice. The

**Kyle** [00:21:00] video voice team has always been producing.

**Vibhu** [00:21:00] Yeah. There’s always just every other domain of paper that comes out, dataset that comes out. It’s like, I mean, it also stems back to what Nvidia has to do, right? You have to make chips years before they’re actually produced.

[00:21:00] Right? So you need to know, you need to really focus. The

**Kyle** [00:22:00] design process starts like

**Vibhu** [00:22:00] exactly

**Kyle** [00:22:00] three to five years before the chip gets to the market.

**Vibhu** [00:22:00] Yeah. I, I’m curious more about what that’s like, right? So like, you have specialist teams. Is it just like, you know, people find an interest, you go in, you go deep on whatever, and that kind of feeds back into, you know, okay, we, we expect predictions.

[00:22:00] Like the internals at Nvidia must be crazy. Right? You know? Yeah. Yeah. You know, you, you must. Not even without selling to people, you have your own predictions of where things are going. Yeah. And they’re very based, very grounded. Right?

**Kyle** [00:22:00] Yeah. It, it, it’s really interesting. So there’s like two things that I think that Amed does, which are quite interesting.

[00:22:00] Uh, one is like, we really index into passion. There’s a big. Sort of organizational top sound push to like ensure that people are working on the things that they’re passionate about. So if someone proposes something that’s interesting, many times they can just email someone like way up the chain that they would find this relevant and say like, Hey, can I go work on this?

**Nader** [00:22:00] It’s actually like I worked at a, a big company for a couple years before, uh, starting on my startup journey and like, it felt very weird if you were to like email out of chain, if that makes sense. Yeah. The emails at Nvidia are like mosh pits

**swyx** [00:23:00] shoot,

**Nader** [00:23:00] and it’s just like 60 people, just whatever. And like they’re, there’s this,

**swyx** [00:23:00] they got messy like, reply all you,

**Nader** [00:23:00] oh, it’s in, it’s insane.

[00:23:00] It’s insane. They just

**Kyle** [00:23:00] help. You know, Maxim,

**Nader** [00:23:00] the context. But, but that’s actually like, I’ve actually, so this is a weird thing where I used to be like, why would we send emails? We have Slack. I am the entire, I’m the exact opposite. I feel so bad for anyone who’s like messaging me on Slack ‘cause I’m so unresponsive.

**swyx** [00:23:00] Your email

**Nader** [00:23:00] Maxi, email Maxim. I’m email maxing Now email is a different, email is perfect because man, we can’t work together. I’m email is great, right? Because important threads get bumped back up, right? Yeah, yeah. Um, and so Slack doesn’t do that. So I just have like this casino going off on the right or on the left and like, I don’t know which thread was from where or what, but like the threads get And then also just like the subject, so you can have like working threads.

[00:23:00] I think what’s difficult is like when you’re small, if you’re just not 40,000 people I think Slack will work fine, but there’s, I don’t know what the inflection point is. There is gonna be a point where that becomes really messy and you’ll actually prefer having email. ‘cause you can have working threads.

[00:23:00] You can cc more than nine people in a thread.

**Kyle** [00:23:00] You can fork stuff.

**Nader** [00:23:00] You can fork stuff, which is super nice and just like y Yeah. And so, but that is part of where you can propose a plan. You can also just. Start, honestly, momentum’s the only authority, right? So like, if you can just start, start to make a little bit of progress and show someone something, and then they can try it.

[00:24:00] That’s, I think what’s been, you know, I think the most effective way to push anything for forward. And that’s both at Nvidia and I think just generally.

**Kyle** [00:24:00] Yeah, there’s, there’s the other concept that like is explored a lot at Nvidia, which is this idea of a zero billion dollar business. Like market creation is a big thing at Nvidia.

[00:24:00] Like,

**swyx** [00:24:00] oh, you want to go and start a zero billion dollar business?

**Kyle** [00:24:00] Jensen says, we are completely happy investing in zero billion dollar markets. We don’t care if this creates revenue. It’s important for us to know about this market. We think it will be important in the future. It can be zero billion dollars for a while.

[00:24:00] I’m probably minging as words here for, but like, you know, like, I’ll give an example. NVIDIA’s been working on autonomous driving for a a long time,

**swyx** [00:24:00] like an Nvidia car.

**Kyle** [00:24:00] No, they, they’ve

**Vibhu** [00:24:00] used the Mercedes, right? They’re around the HQ and I think it finally just got licensed out. Now they’re starting to be used quite a bit.

[00:25:00] For 10 years you’ve been seeing Mercedes with Nvidia logos driving.

**Kyle** [00:25:00] If you’re in like the South San Santa Clara, it’s, it’s actually from South. Yeah. So, um. Zero billion dollar markets are, are a thing like, you know, Jensen,

**swyx** [00:25:00] I mean, okay, look, cars are not a zero billion dollar market. But yeah, that’s a bad example.

**Nader** [00:25:00] I think, I think he’s, he’s messaging, uh, zero today, but, or even like internally, right? Like, like it’s like, uh, an org doesn’t have to ruthlessly find revenue very quickly to justify their existence. Right. Like a lot of the important research, a lot of the important technology being developed that, that’s kind of

**Kyle** [00:25:00] where research, research is very ide ideologically free at Nvidia.

[00:25:00] Yeah. Like they can pursue things that they were

**swyx** [00:25:00] Were you research officially?

**Kyle** [00:25:00] I was never in research. Officially. I was always in engineering. Yeah. We in, I’m in an org called Deep Warning Algorithms, which is basically just how do we make things that are relevant to deep warning go fast.

**swyx** [00:25:00] That sounds freaking cool.

**Vibhu** [00:25:00] And I think a lot of that is underappreciated, right? Like time series. This week Google put out time. FF paper. Yeah. A new time series, paper res. Uh, Symantec, ID started applying Transformers LMS to Yes. Rec system. Yes. And when you think the scale of companies deploying these right. Amazon recommendations, Google web search, it’s like, it’s huge scale and

**Kyle** [00:26:00] Yeah.

**Vibhu** [00:26:00] You want fast?

**Kyle** [00:26:00] Yeah. Yeah. Yeah. Actually it’s, it, I, there’s a fun moment that brought me like full circle. Like, uh, Amazon Ads recently gave a talk where they talked about using Dynamo for generative recommendation, which was like super, like weirdly cathartic for me. I’m like, oh my God. I’ve, I’ve supplanted what I was working on.

[00:26:00] Like, I, you’re using LMS now to do what I was doing five years ago.

**swyx** [00:26:00] Yeah. Amazing. And let’s go right into Dynamo. Uh, maybe introduce Yeah, sure. To the top down and Yeah.

**Kyle** [00:26:00] I think at this point a lot of people are familiar with the term of inference. Like funnily enough, like I went from, you know, inference being like a really niche topic to being something that’s like discussed on like normal people’s Twitter feeds.

[00:26:00] It’s,

**Nader** [00:26:00] it’s on billboards

**Kyle** [00:26:00] here now. Yeah. Very, very strange. Driving, driving, seeing just an inference ad on 1 0 1 inference at scale is becoming a lot more important. Uh, we have these moments like, you know, open claw where you have these agents that take lots and lots of tokens, but produce, incredible results.

[00:27:00] There are many different aspects of test time scaling so that, you know, you can use more inference to generate a better result than if you were to use like a short amount of inference. There’s reasoning, there’s quiring, there’s, adding agency to the model, allowing it to call tools and use skills.

[00:27:00] Dyno sort came about at Nvidia. Because myself and a couple others were, were sort of talking about the, these concepts that like, you know, you have inference engines like VLMS, shelan, tenor, TLM and they have like one single copy. They, they, they sort of think about like things as like one single copy, like one replica, right?

## Why Scale Out Wins

**Kyle** [00:27:00] Like one version of the model. But when you’re actually serving things at scale, you can’t just scale up that replica because you end up with like performance problems. There’s a scaling limit to scaling up replicas. So you actually have to scale out to use a, maybe some Kubernetes type terminology.

[00:27:00] We kind of realized that there was like. A lot of potential optimization that we could do in scaling out and building systems for data center scale inference. So Dynamo is this data center scale inference engine that sits on top of the frameworks like VLM Shilling and 10 T lm and just makes things go faster because you can leverage the economy of scale.

[00:28:00] The fact that you have KV cash, which we can define a little bit later, uh, in all these machines that is like unique and you wanna figure out like the ways to maximize your cash hits or you want to employ new techniques in inference like disaggregation, which Dynamo had introduced to the world in, in, in March, not introduced, it was a academic talk, but beforehand.

[00:28:00] But we are, you know, one of the first frameworks to start, supporting it. And we wanna like, sort of combine all these techniques into sort of a modular framework that allows you to. Accelerate your inference at scale.

**Nader** [00:28:00] By the way, Kyle and I became friends on my first date, Nvidia, and I always loved, ‘cause like he always teaches me

**swyx** [00:28:00] new things.

[00:28:00] Yeah. By the way, this is why I wanted to put two of you together. I was like, yeah, this is, this is gonna be

**Kyle** [00:28:00] good. It’s very, it’s very different, you know, like we’ve, we, we’ve, we’ve talked to each other a bunch actually, you asked like, why, why can’t we scale up?

**Nader** [00:29:00] Yeah.

## Scale Up Limits Explained

**Nader** [00:29:00] model, you said model replicas.

**Kyle** [00:29:00] Yeah. So you, so scale up means assigning more

**swyx** [00:29:00] heavier?

**Kyle** [00:29:00] Yeah, heavier. Like making things heavier. Yeah, adding more GPUs. Adding more CPUs. Scale out is just like having a barrier saying, I’m gonna duplicate my representation of the model or a representation of this microservice or something, and I’m gonna like, replicate it Many times.

[00:29:00] Handle, load. And the reason that you can’t scale, scale up, uh, past some points is like, you know, there, there, there are sort of hardware bounds and algorithmic bounds on, on that type of scaling. So I’ll give you a good example that’s like very trivial. Let’s say you’re on an H 100. The Maxim ENV link domain for H 100, for most Ds H one hundreds is heus, right?

[00:29:00] So if you scaled up past that, you’re gonna have to figure out ways to handle the fact that now for the GPUs to communicate, you have to do it over Infin band, which is still very fast, but is not as fast as ENV link.

**swyx** [00:29:00] Is it like one order of magnitude, like hundreds or,

**Kyle** [00:29:00] it’s about an order of magnitude?

[00:29:00] Yeah. Okay. Um, so

**swyx** [00:29:00] not terrible.

**Kyle** [00:29:00] Yeah. I, I need to, I need to remember the, the data sheet here, like, I think it’s like about 500 gigabytes. Uh, a second unidirectional for ENV link, and about 50 gigabytes a second unidirectional for Infin Band. I, it, it depends on the, the generation.

**swyx** [00:30:00] I just wanna set this up for people who are not familiar with these kinds of like layers and the trash speed

**Vibhu** [00:30:00] and all that.

[00:30:00] Of course.

## From Laptop to Multi Node

**Vibhu** [00:30:00] Also, maybe even just going like a few steps back before that, like most people are very familiar with. You see a, you know, you can use on your laptop, whatever these steel viol, lm you can just run inference there. All, there’s all, you can, you

[00:30:00] can run it on that

**Vibhu** [00:30:00] laptop. You can run on laptop.

[00:30:00] Then you get to, okay, uh, models got pretty big, right? JLM five, they doubled the size, so mm-hmm. Uh, what do you do when you have to go from, okay, I can get 128 gigs of memory. I can run it on a spark. Then you have to go multi GPU. Yeah. Okay. Multi GPU, there’s some support there. Now, if I’m a company and I don’t have like.

[00:30:00] I’m not hiring the best researchers for this. Right. But I need to go multi-node, right? I have a lot of servers. Okay, now there’s efficiency problems, right? You can have multiple eight H 100 nodes, but, you know, is that as a, like, how do you do that efficiently?

**Kyle** [00:31:00] Yeah. How do you like represent them? How do you choose how to represent the model?

[00:31:00] Yeah, exactly right. That’s a, that’s like a hard question. Everyone asks, how do you size oh, I wanna run GLM five, which just came out new model. There have been like four of them in the past week, by the way, like a bunch of new models.

**swyx** [00:31:00] You know why? Right? Deep seek.

**Kyle** [00:31:00] No comment. Oh. Yeah, but Ggl, LM five, right?

[00:31:00] We, we have this, new model. It’s, it’s like a large size, and you have to figure out how to both scale up and scale out, right? Because you have to find the right representation that you care about. Everyone does this differently. Let’s be very clear. Everyone figures this out in their own path.

**Nader** [00:31:00] I feel like a lot of AI or ML even is like, is like this. I think people think, you know, I, I was, there was some tweet a few months ago that was like, why hasn’t fine tuning as a service taken off? You know, that might be me. It might have been you. Yeah. But people want it to be such an easy recipe to follow.

[00:31:00] But even like if you look at an ML model and specific

**Kyle** [00:31:00] to you Yeah,

**Nader** [00:31:00] yeah.

**Kyle** [00:31:00] And the model,

**Nader** [00:32:00] the situation, and there’s just so much tinkering, right? Like when you see a model that has however many experts in the ME model, it’s like, why that many experts? I don’t, they, you know, they tried a bunch of things and that one seemed to do better.

[00:32:00] I think when it comes to how you’re serving inference, you know, you have a bunch of decisions to make and there you can always argue that you can take something and make it more optimal. But I think it’s this internal calibration and appetite for continued calibration.

**Vibhu** [00:32:00] Yeah. And that doesn’t mean like, you know, people aren’t taking a shot at this, like tinker from thinking machines, you know?

[00:32:00] Yeah. RL as a service. Yeah, totally. It’s, it also gets even harder when you try to do big model training, right? We’re not the best at training Moes, uh, when they’re pre-trained. Like we saw this with LAMA three, right? They’re trained in such a sparse way that meta knows there’s gonna be a bunch of inference done on these, right?

[00:32:00] They’ll open source it, but it’s very trained for what meta infrastructure wants, right? They wanna, they wanna inference it a lot. Now the question to basically think about is, okay, say you wanna serve a chat application, a coding copilot, right? You’re doing a layer of rl, you’re serving a model for X amount of people.

[00:32:00] Is it a chat model, a coding model? Dynamo, you know, back to that,

**Kyle** [00:32:00] it’s like, yeah, sorry. So you we, we sort of like jumped off of, you know, jumped, uh, on that topic. Everyone has like, their own, own journey.

## Cost Quality Latency Tradeoffs

**Kyle** [00:33:00] And I, I like to think of it as defined by like, what is the model you need? What is the accuracy you need?

[00:33:00] Actually I talked to NA about this earlier. There’s three axes you care about. What is the quality that you’re able to produce? So like, are you accurate enough or can you complete the task with enough, performance, high enough performance. Yeah, yeah. Uh, there’s cost. Can you serve the model or serve your workflow?

[00:33:00] Because it’s not just the model anymore, it’s the workflow. It’s the multi turn with an agent cheaply enough. And then can you serve it fast enough? And we’re seeing all three of these, like, play out, like we saw, we saw new models from OpenAI that you know, are faster. You have like these new fast versions of models.

[00:33:00] You can change the amount of thinking to change the amount of quality, right? Produce more tokens, but at a higher cost in a, in a higher latency. And really like when you start this journey of like trying to figure out how you wanna host a model, you, you, you think about three things. What is the model I need to serve?

[00:33:00] How many times do I need to call it? What is the input sequence link was the, what does the workflow look like on top of it? What is the SLA, what is the latency SLA that I need to achieve? Because there’s usually some, this is usually like a constant, you, you know, the SLA that you need to hit and then like you try and find the lowest cost version that hits all of these constraints.

[00:34:00] Usually, you know, you, you start with those things and you say you, you kind of do like a bit of experimentation across some common configurations. You change the tensor parallel size, which is a form of parallelism

**Vibhu** [00:34:00] I take, it goes even deeper first. Gotta think what model.

**Kyle** [00:34:00] Yes, course,

[00:34:00] of

**Kyle** [00:34:00] course. It’s like, it’s like a multi-step design process because as you said, you can, you can choose a smaller model and then do more test time scaling and it’ll equate the quality of a larger model because you’re doing the test time scaling or you’re adding a harness or something.

[00:34:00] So yes, it, it goes way deeper than that. But from the performance perspective, like once you get to the model you need, you need to host, you look at that and you say, Hey. I have this model, I need to serve it at the speed. What is the right configuration for that?

**Nader** [00:34:00] You guys see the recent, uh, there was a paper I just saw like a few days ago that, uh, if you run the same prompt twice, you’re getting like double Just try it

[00:35:00] again.

**Nader** [00:35:00] Yeah, exactly.

**Vibhu** [00:35:00] And you get a lot. Yeah. But the, the key thing there is you give the context of the failed try, right? Yeah. So it takes a shot. And this has been like, you know, basic guidance for quite a while. Just try again. ‘cause you know, trying, just try again. Did you try again? All advice

**Nader** [00:35:00] in life.

**Vibhu** [00:35:00] Just, it’s a paper from Google, if I’m not mistaken, right?

[00:35:00] Yeah,

**Vibhu** [00:35:00] yeah. I think it, it’s like a seven bas little short paper. Yeah. Yeah. The title’s very cute. And it’s just like, yeah, just try again. Give it ask context,

**Kyle** [00:35:00] multi-shot. You just like, say like, hey, like, you know, like take, take a little bit more, take a little bit more information, try and fail. Fail.

**Vibhu** [00:35:00] And that basic concept has gone pretty deep.

[00:35:00] There’s like, um, self distillation, rl where you, you do self distillation, you do rl and you have past failure and you know, that gives some signal so people take, try it again. Not strong enough.

**swyx** [00:35:00] Uh, for, for listeners, uh, who listen to here, uh, vivo actually, and I, and we run a second YouTube channel for our paper club where, oh, that’s awesome.

[00:35:00] Vivo just covered this. Yeah. Awesome. Self desolation and all that’s, that’s why he, to speed on it.

**Nader** [00:36:00] I’ll to check it out.

**swyx** [00:36:00] Yeah. It, it’s just a good practice, like everyone needs, like a paper club where like you just read papers together and the social pressure just kind of forces you to just,

**Nader** [00:36:00] we, we,

[00:36:00] there’s

**Nader** [00:36:00] like a big inference.

**Kyle** [00:36:00] Reading

**Nader** [00:36:00] group at a video. I feel so bad every time. I I, he put it on like, on our, he shared it.

**swyx** [00:36:00] One, one of

**Nader** [00:36:00] your guys,

**swyx** [00:36:00] uh, is, is big in that, I forget es han Yeah, yeah,

**Kyle** [00:36:00] es Han’s on my team. Actually. Funny. There’s a, there’s a, there’s a employee transfer between us. Han worked for Nater at Brev, and now he, he’s on my team.

[00:36:00] He was

**Nader** [00:36:00] our head of ai. And then, yeah, once we got in, and

**swyx** [00:36:00] because I’m always looking for like, okay, can, can I start at another podcast that only does that thing? Yeah. And, uh, Esan was like, I was trying to like nudge Esan into like, is there something here? I mean, I don’t think there’s, there’s new infant techniques every day.

[00:36:00] So it’s like, it’s like

**Kyle** [00:36:00] you would, you would actually be surprised, um, the amount of blog posts you see. And if

**swyx** [00:36:00] there’s a period where it was like, Medusa hydra, what Eagle, like, you

**Kyle** [00:36:00] know, now we have new forms of decode, uh, we have new forms of specula, of decoding or new,

**swyx** [00:36:00] what,

**Kyle** [00:36:00] what are you

**Vibhu** [00:36:00] excited? And it’s exciting when you guys put out something like Tron.

[00:36:00] ‘cause I remember the paper on this Tron three, uh, the amount of like post train, the on tokens that the GPU rich can just train on. And it, it was a hybrid state space model, right? Yeah.

**Kyle** [00:37:00] It’s co-designed for the hardware.

**Vibhu** [00:37:00] Yeah, go design for the hardware. And one of the things was always, you know, the state space models don’t scale as well when you do a conversion or whatever the performance.

[00:37:00] And you guys are like, no, just keep draining. And Nitron shows a lot of that. Yeah.

**Nader** [00:37:00] Also, something cool about Nitron it was released in layers, if you will, very similar to Dynamo. It’s, it’s, it’s essentially it was released as you can, the pre-training, post-training data sets are released. Yeah. The recipes on how to do it are released.

[00:37:00] The model itself is released. It’s full model. You just benefit from us turning on the GPUs. But there are companies like, uh, ServiceNow took the dataset and they trained their own model and we were super excited and like, you know, celebrated that work.

[00:37:00] Zoom

**Vibhu** [00:37:00] different. Zoom is, zoom is CGI, I think, uh, you know, also just to add like a lot of models don’t put out based models and if there’s that, why is fine tuning not taken off?

[00:37:00] You know, you can do your own training. Yeah,

**Kyle** [00:37:00] sure.

**Vibhu** [00:37:00] You guys put out based model, I think you put out everything.

**Nader** [00:37:00] I believe I know

**swyx** [00:38:00] about base. Basically

**Vibhu** [00:38:00] without base

**swyx** [00:38:00] basic can be cancelable.

**Vibhu** [00:38:00] Yeah. Base can be cancelable.

**swyx** [00:38:00] Yeah.

**Vibhu** [00:38:00] Safety training.

**swyx** [00:38:00] Did we get a full picture of dymo? I, I don’t know if we, what,

**Nader** [00:38:00] what I’d love is you, you mentioned the three axes like break it down of like, you know, what’s prefilled decode and like what are the optimizations that we can get with Dynamo?

**Kyle** [00:38:00] Yeah. That, that’s, that’s, that’s a great point. So to summarize on that three axis problem, right, there are three things that determine whether or not something can be done with inference, cost, quality, latency, right? Dynamo is supposed to be there to provide you like the runtime that allows you to pull levers to, you know, mix it up and move around the parade of frontier or the preto surface that determines is this actually possible with inference And AI today

**Nader** [00:38:00] gives you the knobs.

**Kyle** [00:38:00] Yeah, exactly. It gives you the knobs.

## Disaggregation Prefill vs Decode

**Kyle** [00:38:00] Uh, and one thing that like we, we use a lot in contemporary inference and is, you know, starting to like pick up from, you know, in, in general knowledge is this co concept of disaggregation. So historically. Models would be hosted with a single inference engine. And that inference engine would ping pong between two phases.

[00:39:00] There’s prefill where you’re reading the sequence generating KV cache, which is basically just a set of vectors that represent the sequence. And then using that KV cache to generate new tokens, which is called Decode. And some brilliant researchers across multiple different papers essentially made the realization that if you separate these two phases, you actually gain some benefits.

[00:39:00] Those benefits are basically a you don’t have to worry about step synchronous scheduling. So the way that an inference engine works is you do one step and then you finish it, and then you schedule, you start scheduling the next step there. It’s not like fully asynchronous. And the problem with that is you would have, uh, essentially pre-fill and decode are, are actually very different in terms of both their resource requirements and their sometimes their runtime.

[00:39:00] So you would have like prefill that would like block decode steps because you, you’d still be pre-filing and you couldn’t schedule because you know the step has to end. So you remove that scheduling issue and then you also allow you, or you yourself, to like split the work into two different ki types of pools.

[00:40:00] So pre-fill typically, and, and this changes as, as model architecture changes. Pre-fill is, right now, compute bound most of the time with the sequence is sufficiently long. It’s compute bound. On the decode side because you’re doing a full Passover, all the weights and the entire sequence, every time you do a decode step and you’re, you don’t have the quadratic computation of KV cache, it’s usually memory bound because you’re retrieving a linear amount of memory and you’re doing a linear amount of compute as opposed to prefill where you retrieve a linear amount of memory and then use a quadratic.

[00:40:00] You know,

**Nader** [00:40:00] it’s funny, someone exo Labs did a really cool demo where for the DGX Spark, which has a lot more compute, you can do the pre the compute hungry prefill on a DG X spark and then do the decode on a, on a Mac. Yeah. And so

**Vibhu** [00:40:00] that’s faster.

**Nader** [00:40:00] Yeah. Yeah.

**Kyle** [00:40:00] So you could, you can do that. You can do machine strat stratification.

**Nader** [00:40:00] Yeah.

**Kyle** [00:40:00] And like with our future generation generations of hardware, we actually announced, like with Reuben, this new accelerator that is prefilled specific. It’s called Reuben, CPX. So

## Kubernetes Scaling with Grove

**Nader** [00:41:00] I have a question when you do the scale out. Yeah. Is scaling out easier with Dynamo? Because when you need a new node, you can dedicate it to either the Prefill or, uh, decode.

**Kyle** [00:41:00] Yeah. So Dynamo actually has like a, a Kubernetes component in it called Grove that allows you to, to do this like crazy scaling specialization. It has like this hot, it’s a representation that, I don’t wanna go too deep into Kubernetes here, but there was a previous way that you would like launch multi-node work.

[00:41:00] Uh, it’s called Leader Worker Set. It’s in the Kubernetes standard, and Leader worker set is great. It served a lot of people super well for a long period of time. But one of the things that it’s struggles with is representing a set of cases where you have a multi-node replica that has a pair, right?

[00:41:00] You know, prefill and decode, or it’s not paired, but it has like a second stage that has a ratio that changes over time. And prefill and decode are like two different things as your workload changes, right? The amount of prefill you’ll need to do may change. The amount of decode that you, you’ll need to do might change, right?

[00:42:00] Like, let’s say you start getting like insanely long queries, right? That probably means that your prefill scales like harder because you’re hitting these, this quadratic scaling growth.

**swyx** [00:42:00] Yeah.

[00:42:00] And then for listeners, like prefill will be long input. Decode would be long output, for example, right?

**Kyle** [00:42:00] Yeah. So like decode, decode scale. I mean, decode is funny because the amount of tokens that you produce scales with the output length, but the amount of work that you do per step scales with the amount of tokens in the context.

**swyx** [00:42:00] Yes.

**Kyle** [00:42:00] So both scales with the input and the output.

**swyx** [00:42:00] That’s true.

**Kyle** [00:42:00] But on the pre-fold view code side, like if.

[00:42:00] Suddenly, like the amount of work you’re doing on the decode side stays about the same or like scales a little bit, and then the prefilled side like jumps up a lot. You actually don’t want that ratio to be the same. You want it to change over time. So Dynamo has a set of components that A, tell you how to scale.

[00:42:00] It tells you how many prefilled workers and decoded workers you, it thinks you should have, and also provides a scheduling API for Kubernetes that allows you to actually represent and affect this scheduling on, on, on your actual hardware, on your compute infrastructure.

**Nader** [00:43:00] Not gonna lie. I feel a little embarrassed for being proud of my SVG function earlier.

**swyx** [00:43:00] No, it

**Nader** [00:43:00] was

[00:43:00] really

**Kyle** [00:43:00] cute. I, I

**swyx** [00:43:00] like

**Nader** [00:43:00] it’s all,

**swyx** [00:43:00] it’s all engineering. It’s all engineering. Um, that’s where I’m

**Kyle** [00:43:00] technical.

**swyx** [00:43:00] One thing I’m, I’m kind of just curious about with all with you see at a systems level, everything going on here. Mm-hmm. And we, you know, we’re scaling it up in, in multi, in distributed systems.

## Context Length and Co Design

**swyx** [00:43:00] Um, I think one thing that’s like kind of, of the moment right now is people are asking, is there any SOL sort of upper bounds. In terms of like, let’s call, just call it context length for one for of a better word, but you can break it down however you like.

**Nader** [00:43:00] Yeah.

**swyx** [00:43:00] I just think like, well, yeah, I mean, like clearly you can engage in hybrid architectures and throw in some state space models in there.

[00:43:00] All, all you want, but it looks, still looks very attention heavy.

**Kyle** [00:43:00] Yes. Uh, yeah. Long context is attention heavy. I mean, we have these hybrid models, um,

**swyx** [00:43:00] to take and most, most models like cap out at a million contexts and that’s it. Yeah. Like for the last two years has been it.

**Kyle** [00:43:00] Yeah. The model hardware context co-design thing that we’re seeing these days is actually super interesting.

[00:44:00] It’s like my, my passion, like my secret side passion. We see models like Kimmy or G-P-T-O-S-S. I’m use these because I, I know specific things about these models. So Kimmy two comes out, right? And it’s an interesting model. It’s like, like a deep seek style architecture is MLA. It’s basically deep seek, scaled like a little bit differently, um, and obviously trained differently as well.

[00:44:00] But they, they talked about, why they made the design choices for context. Kimmy has more experts, but fewer attention heads, and I believe a slightly smaller attention, uh, like dimension. But I need to remember, I need to check that. Uh, it doesn’t matter. But they discussed this actually at length in a blog post on ji, which is like our pu which is like credit pu

**swyx** [00:44:00] Yeah.

**Kyle** [00:44:00] Um, in, in China. Chinese red.

**swyx** [00:44:00] Yeah.

**Kyle** [00:44:00] It’s, yeah. So it, it’s, it’s actually an incredible blog post. Uh, like all the mls people in, in, in that, I’ve seen that on GPU are like very brilliant, but they, they talk about like the creators of Kimi K two actually like, talked about it on, on, on there in the blog post.

[00:45:00] And they say, we, we actually did an experiment, right? Attention scales with the number of heads, obviously. Like if you have 64 heads versus 32 heads, you do half the work of attention. You still scale quadratic, but you do half the work. And they made a, a very specific like. Sort of barter in their system, in their architecture, they basically said, Hey, what if we gave it more experts, so we’re gonna use more memory capacity.

[00:45:00] But we keep the amount of activated experts the same. We increase the expert sparsity, so we have fewer experts act. The ratio to of experts activated to number of experts is smaller, and we decrease the number of attention heads.

**Vibhu** [00:45:00] And kind of for context, what the, what we had been seeing was you make models sparser instead.

[00:45:00] So no one was really touching heads. You’re just having, uh,

**Kyle** [00:45:00] well, they, they did, they implicitly made it sparser.

**Vibhu** [00:45:00] Yeah, yeah. For, for Kimmy. They did,

**Kyle** [00:45:00] yes.

**Vibhu** [00:45:00] They also made it sparser. But basically what we were seeing was people were at the level of, okay, there’s a sparsity ratio. You want more total parameters, less active, and that’s sparsity.

[00:46:00] But what you see from papers, like, the labs like moonshot deep seek, they go to the level of, okay, outside of just number of experts, you can also change how many attention heads and less attention layers. More attention. Layers. Layers, yeah. Yes, yes. So, and that’s all basically coming back to, just tied together is like hardware model, co-design, which is

**Kyle** [00:46:00] hardware model, co model, context, co-design.

**Vibhu** [00:46:00] Yeah.

**Kyle** [00:46:00] Right. Like if you were training a, a model that was like. Really, really short context, uh, or like really is good at super short context tasks. You may like design it in a way such that like you don’t care about attention scaling because it hasn’t hit that, like the turning point where like the quadratic curve takes over.

**Nader** [00:46:00] How do you consider attention or context as a separate part of the co-design? Like I would imagine hardware or just how I would’ve thought of it is like hardware model. Co-design would be hardware model context co-design

**Kyle** [00:46:00] because the harness and the context that is produced by the harness is a part of the model.

[00:46:00] Once it’s trained in,

**Vibhu** [00:46:00] like even though towards the end you’ll do long context, you’re not changing architecture through I see. Training. Yeah.

**Kyle** [00:46:00] I mean you can try.

**swyx** [00:46:00] You’re saying everyone’s training the harness into the model.

**Kyle** [00:47:00] I would say to some degree, or

**swyx** [00:47:00] there’s co-design for harness. I know there’s a small amount, but I feel like not everyone has like gone full send on this.

**Kyle** [00:47:00] I think, I think I think it’s important to internalize the harness that you think the model will be running. Running into the model.

**swyx** [00:47:00] Yeah. Interesting. Okay. Bash is like the universal harness,

**Kyle** [00:47:00] right? Like I’ll, I’ll give. An example here, right? I mean, or just like a, like a, it’s easy proof, right? If you can train against a harness and you’re using that harness for everything, wouldn’t you just train with the harness to ensure that you get the best possible quality out of,

**swyx** [00:47:00] Well, the, uh, I, I can provide a counter argument.

[00:47:00] Yeah, sure. Which is what you wanna provide a generally useful model for other people to plug into their harnesses, right? So if you

**Kyle** [00:47:00] Yeah. Harnesses can be open, open source, right?

**swyx** [00:47:00] Yeah. So I mean, that’s, that’s effectively what’s happening with Codex.

**Kyle** [00:47:00] Yeah.

**swyx** [00:47:00] And, but like you may want like a different search tool and then you may have to name it differently or,

**Nader** [00:47:00] I don’t know how much people have pushed on this, but can you.

[00:47:00] Train a model, would it be, have you have people compared training a model for the for the harness versus like post training for

**swyx** [00:48:00] I think it’s the same thing. It’s the same thing. It’s okay. Just extra post training. I

**Nader** [00:48:00] see.

**swyx** [00:48:00] And so, I mean, cognition does this course, it does this where you, you just have to like, if your tool is slightly different, um, either force your tool to be like the tool that they train for.

[00:48:00] Hmm. Or undo their training for their tool and then Oh, that’s re retrain. Yeah. It’s, it’s really annoying and like,

**Kyle** [00:48:00] I would hope that eventually we hit like a certain level of generality with respect to training new

**swyx** [00:48:00] tools. This is not a GI like, it’s, this is a really stupid like. Learn my tool bitch.

[00:48:00] Like, I don’t know if, I don’t know if I can say that, but like, you know, um, I think what my point kind of is, is that there’s, like, I look at slopes of the scaling laws and like, this slope is not working, man. We, we are at a million token context, okay, maybe next year, 2 million, we’re not going to a hundred trillion, you know, like this, this, oh, there’s so many interesting ways to get this Doesn’t work.

[00:48:00] Just doesn’t work.

**Nader** [00:48:00] What’s kind of funny is whenever there, I, I feel like we always want to see a trend that we can predict, but every time something’s come, it’s been like a leapfrog. So I, I imagine I, I don’t know how we go from one to two, but I imagine what, what’s likely to happen is we break through that from some new

**Kyle** [00:49:00] Yeah.

[00:49:00] There’s actually, there’s an interesting formalization of this. There, there’s an essay. It’s a pretty interesting essay by Leopold Ashton Brener called Situational Awareness.

**swyx** [00:49:00] Okay? Yes.

**Kyle** [00:49:00] He introduces a concept awareness called an un hobbler, right? So he, you know, Leopold in this essay details, Hey, I want to get.

[00:49:00] You know, like, I wanna get to this point in intelligence and I think that it is four orders of magnitude worth of like compute and data and training away. And you know, he says, oh yeah, I think data centers can scale up by about this much. I think that you can do, scale up the data and some other things by this much.

[00:49:00] But one of the things that like makes the rest of that order of magnitude growth, PO possibilities is un hobbler, like these scientific discoveries that are discovered during. You know, model architecture, search or training that really, really, really impact how, how you are able to scale. Like a, a good example of this might be that like we see like a mo a lot of models that are, and this is probably a very tiny on hobbler.

[00:50:00] But is important for the performance perspective. We see a lot of models that are like trained with multi token prediction natively in during pre-training.

[00:50:00] And per deep seek in their paper they say, Hey, decided this actually helped us in ensure sta more stable convergence. But they’re like, un Hobbs that are like that.

[00:50:00] And then they’re like, rather large on hobbler. Right. Like architecturally, a lot of our models, like we had different types of attention. And one of the problems with attention is like, you have a lot of kv, but people found like different forms of attention, like group query attention and, uh, like MLA in deep seek multi-head latent attention that like decrease the burden that KV has on the model, which allows you to grow like longer in context.

**swyx** [00:50:00] Yeah. And that, that was very drastic for deeps seek.

**Kyle** [00:50:00] Yeah. This was like, yeah, it for context like the, the total, I think the total context length of deeps seek is 128,000 tokens or might be 256,000 with rope extension. That entire context, I think it’s 128,000 fits into eight gigabytes. Previously context, like I think the, the llama four or five B context of a similar size was like 40 or 80 gigabytes in the same precision.

**swyx** [00:51:00] Yeah.

**Kyle** [00:51:00] Um, so like those in Hobbler like really decrease the stuff of that size. And I wouldn’t be surprised if we do see the ability to like, break through to like 10 million, 20 million, a hundred million context through the an un hobbler showing up. I

**swyx** [00:51:00] see.

**Kyle** [00:51:00] And it’s just science.

**swyx** [00:51:00] So more deep learning algorithms is what

**Kyle** [00:51:00] I’m hearing.

[00:51:00] Yeah. More deep learning algorithms. Um,

**swyx** [00:51:00] yeah,

**Kyle** [00:51:00] I, I could, I could actually playing pickup

**swyx** [00:51:00] and he has

**Kyle** [00:51:00] room to, I I could actually give you an, an example like of like a, a theory, not a theory theory, but something theoretical and a hobar

**Nader** [00:51:00] that you’re excited about or,

**Kyle** [00:51:00] well, and, and a hobar that, I mean, I haven’t seen, so it could be a tar pit and it could not, just, not work.

[00:51:00] But, uh, I, I would be really excited to see a model that does prefill and decode differently. So a model that does, uh, prefill like locally, like document wise, prefill, like it doesn’t in chunks, and then you do decode globally across like the entire sequence because it, logically to me it doesn’t seem like you would necessarily need to have KV b associative between documents that have like, no, no mutual association.

[00:52:00] But that like places a lot of burden on prefilled to like, or sorry, on, on decode and pure attention within the decode phase to like make those connections since the KV is like static at that point. And you see other techniques that are interesting like this too. But if, if you’re able to do that, like.

[00:52:00] If Prefill becomes local and decode is, is still global, you solve that prefilled quadratic scaling problem because you have a bunch of like small chunks that you prefill independently.

**swyx** [00:52:00] Okay. All right. Well, let’s, uh, wait and see, but I, I think it’ll be pretty exciting.

**Kyle** [00:52:00] Fingers crossed.

**swyx** [00:52:00] Yeah, fingers crossed.

[00:52:00] Yeah. Yeah.

**Vibhu** [00:52:00] I’m excited for prefilled decode on separate hardware. So like yeah. CR acquisition, right. Can we decode on the gr Can we get super fast?

**Kyle** [00:52:00] I don’t think I’m allowed to comment on this.

**swyx** [00:52:00] Mark is gonna shoot arrows at us.

**Nader** [00:52:00] Uh, he’s got a blow dark, he’s in the room, just

**Kyle** [00:52:00] like,

**Nader** [00:52:00] like go to sleep.

[00:52:00] Yeah. Yeah.

**swyx** [00:52:00] But

**Nader** [00:52:00] I’m, I’m super excited to see the team come in and like, you know, I’ve gotten the, the pleasure of working with some of the, the GR people coming in. So, you know, yeah, I,

**swyx** [00:52:00] I know Sonny, we’ve had him, uh, at the same

**Kyle** [00:53:00] conference that

**swyx** [00:53:00] you are at.

**Nader** [00:53:00] Yeah.

**swyx** [00:53:00] Um, and, uh, I, I think you’re, you guys are gonna be doing some sessions at G tc.

[00:53:00] I don’t know if you wanna, this is a good place to plug them.

**Kyle** [00:53:00] Yeah, yeah, yeah. So, I can’t speak to any LPU related sessions at G tc. I have no idea about that. Oh, no, that was,

**swyx** [00:53:00] no. Yours

**Kyle** [00:53:00] on the, on the GR side. Yeah. I use the associative NVIDIA U Yeah. Um, on the, on the Nvidia Dynamo side, we’re, we’re giving, there are a large number of sessions.

[00:53:00] For those that aren’t aware, you can actually search. All of these sessions for GTC online, just go to the GTC website. I don’t know what the URL is, but go there. Google it. Yeah. Uh, and you can just look up Dynamo and you’ll get all the sessions. There’re about 20. There are a couple that are hosted by the Dynamo team.

[00:53:00] There are a couple that are hosted by people that use Dynamo that wanna show off the results they’ve been able to get. But there are two that I’m really excited about. Uh, one is just the General Dynamo tutorial, and this is the, I’m going out with Harry, who’s our lead product manager for Dynamo.

[00:53:00] And we’re sort of talking about like how to use Dynamo to get better performance and also like where we see Dynamo going in the future. And then there’s another session that I’m doing with one of our agents teams at Nvidia to talk about sort of the future of agents in production inference. Yeah. So we’re talking about, there’s like this new horizon with respect to agents because we have these harnesses that actually impart structure on upon calls.

[00:54:00] Like if you, if you compare like, the past and the, and the present with respect to like how LM calls work. Like in the early days when they were chatbots, like every call was like very different. There was basically no structure. You could assume that like people, you, if it was conversational, there might be like some implicit structure because you have, you know, a multi-term conversation.

[00:54:00] But agency have this, this harness that, like abides by rules, right? So it imparts direct structure onto the context. And you see this, there was an interesting Twitter post about how Claude code like structures, its context so that you get as many cts as possible.

[00:54:00] And I think it was by one of the, the PMs for Claude code.

[00:54:00] And he, he wrote about it. And that type of structure that the harness can impart actually like goes hand in hand with the. Inference co-design. So I’m doing a talk, I, I don’t know the session name or the session number, but I’m, I’m doing a talk, uh, you can look at me up by name on, on the GTC website, on how we accelerate agents and where we see specific optimizations for agents going in Dynamo and in inference in general.

**swyx** [00:55:00] Yeah. I think there’s only 1:00 PM for cloud code and it’s wo the rest. There’s, there’s Devrel, there’s Boris. Maybe it was maybe Devrel. Yeah, exactly. I mean, let’s go into agents. I think this was like the last part of the, the, the discussion we planned. Yeah. How have we not talked about agents also with you guys?

[00:55:00] Well, we scheduled, it was like, I was like, okay, you know, like, let’s have like cohesive sections or,

**Vibhu** [00:55:00] I mean, there’s the big news, right? The NVIDIA’s a huge. Like deployment of Codex. Yeah, video

**swyx** [00:55:00] uses everything. I mean, we use this cursor and we uses code,

**Vibhu** [00:55:00] but that’s, that’s a pretty big deployment, right?

[00:55:00] Like, that’s tens of thousands of people.

**Nader** [00:55:00] Totally. Yeah.

**Vibhu** [00:55:00] We’re super What? That’s,

**Nader** [00:55:00] yeah. I, it goes back to the mosh pit of emails we kind of mentioned earlier, or just the like, um, how fluid the org feels. So when there’s new technology, people will just email it out and everyone will try it.

[00:55:00] And if it, if it’s making people’s lives easier, it’ll spread like wildfire.

**Kyle** [00:56:00] A lot of times Jensen will get it and it’ll be like, let’s make this work. Yeah. Across the company. Let’s make this work right now,

**Nader** [00:56:00] honestly, uh, if I was a startup, I feel like a cool hack. If you have something that’s going to save an Nvidia time they’ll spread it to a couple and the same thing.

[00:56:00] Right? It’ll just spread like wildfire. Okay.

**Vibhu** [00:56:00] Careful before your email blows up from startups. Well,

**Nader** [00:56:00] You gotta know the person. Right? But no, I, um, I, yeah, so I mean, we, I love using Codex. It’s been a ton of fun. Yeah. Uh, I’ve been using it personally. I’ve been using it at work. It’s been, um.

[00:56:00] Yeah, I dunno. It’s been great to see the rollout, something really funny. Uh, on the data we got, uh, codex and cloud code access. I found this person, uh, his name’s Carlos at the company. He wrote an Outlook, CLI.

**Kyle** [00:56:00] Oh yeah.

**Nader** [00:56:00] And, uh, just the CLI for email. And this was, I’ve

**Kyle** [00:56:00] been using that,

**Nader** [00:56:00] yeah, maybe like four or five weeks ago.

[00:56:00] And, uh, the site, so once I got like Codex access I. Installed the CLI, it had a skill and I just asked it to go through all of my emails, which it’s very messy. So if I don’t respond to your email, I’m really sorry. But I asked it to gimme a summary, highlight any escalations that I should look at, put any thread that it thinks I should respond to in a folder, and then archive everything.

[00:57:00] And it did. So if I missed your email, it’s because it didn’t get,

**swyx** [00:57:00] so I should put a prompt injection in my V to Yeah, yeah. What you should do is just FaceTime. Yeah. Um, my, yeah, my SLA is highest on FaceTime,

**Nader** [00:57:00] but that was, it was magic. And so I, I sent it in a big email thread to like 500 people. A bunch of folks tried it out.

[00:57:00] I started like FaceTiming whoever I could at the company to get them set up with this.

**swyx** [00:57:00] Yeah. Um, that specific example mm-hmm. You guys deal with like some pretty. Sensitive emails.

**Nader** [00:57:00] Yeah.

**swyx** [00:57:00] Is there a security review with this?

## Security Meets Agents

**swyx** [00:57:00] ‘cause like one guy made, made it for himself, but like it’s not meant for all the

**Nader** [00:57:00] security team and Nvidia is incredible.

[00:57:00] Like, shout out to them. They’re, they’re, they’re trying to, we have a, we have an amazing security team ‘cause they’re progressive and they know that this is

**Kyle** [00:57:00] really important technology and you have to bring it in. If you think about like, if you work at a big company, your laptop’s usually very locked down if

**Nader** [00:57:00] you can only access certain things.

[00:57:00] Nvidia engineers have those restrictions aren’t there. So you’re expected to understand the risks when you try things out. And so. Very quickly, you know, made sure to chime in security on what we were doing.

## Agent Permissions Model

**Nader** [00:58:00] There’s actually a lot that we’ve been thinking about, especially with open claw, right? Like there’s, you know, agents can do three things.

[00:58:00] Yeah. A agents can do three things. They can access your files, they can access the internet, and then now they can write custom code, uh, and execute it. And you literally only let an agent do two of those three things. If you can access your files and you can write custom code, you don’t want internet access because that’s one to see full vulnerability, right?

[00:58:00] If you have access to internet and your file system, you should know the full scope of what that agent’s capable of doing. Otherwise, malware can get injected or something that can happen. And so that’s a lot of what we’ve been thinking about is like, you know, how do we both enable this because it’s clearly the future.

[00:58:00] But then also, you know, what, what are these enforcement points that we can start to like protect?

**swyx** [00:58:00] And is there any directive of like, Hey, we have a company account or a company agreement with open ai, we use open AI models here, or like choose whatever.

**Nader** [00:58:00] No, no. So, so I would never put any company data in a model that’s not either, that we don’t even, it has to most security.

[00:58:00] Yeah. Yeah. I like how,

**swyx** [00:58:00] how that goes. Uh, you know, obviously you could run your own models. You Nemo and, and we, right, we, we as an, we have an internal cluster, so, you know, of course in random,

**Kyle** [00:59:00] uh, yeah.

**swyx** [00:59:00] Yeah.

**Nader** [00:59:00] I think we’re dynamo’s first customers. Let’s go

## Build Nvidia Inference Gateway

**Kyle** [00:59:00] actually, uh, there’s a funny story about like how I got the experience that informed what we needed for Dynamo at one point.

[00:59:00] There’s a website called build done n video.com and also for us infra dun n video com. That is allows people to try models. It gives an a p service. You can call the model with like a rest, API, and you know, you get a response. I ran the model side for that and it was at one point the largest inference deployment and still may actually be the largest inference deployment in video.

[00:59:00] I’ve, I’ve since like, handed it off to some people and they’re doing a wonderful by way. This is a extremely

**Nader** [00:59:00] underknown or less known resource. Vil diamond v.com. You can get any of these open source models. And it’s rate limited, but it’s free. So it’s perfect for hackers to,

**Kyle** [00:59:00] and, and the SLA on getting models day zero models up is like a day.

[00:59:00] Yeah.

**Kyle** [00:59:00] Like they’re, they’re incredibly good at like figuring out the right way to host the model to get it up there as soon as it comes out.

**swyx** [01:00:00] You ran this?

**Kyle** [01:00:00] Yeah, I ran, I ran it a long time ago. It was originally called Nvidia AI Playground, then it was called AI Foundational insert. Yeah. And then it was called Build Nvidia call.

[01:00:00] And I, I ran the model side of it. So there were, there was a large multi-organizational team. I ran how, which models should we host? How should we host them and like what’s the proportion of them? And then of course there was like an SRE team that like made sure that things ran well and scaled the models as well.

[01:00:00] But I ran like, you know, model, how do we get the model to silicon? And then, which model also worked with our product team Determine like which models were important a very long time ago.

[01:00:00] Yeah. Yeah. There’s also like a middle ground in between there, right? This is like for the hacker. Try anything.

[01:00:00] There’s the Brev console, then there’s Dynamo, there was also nims, right?

**Kyle** [01:00:00] Yes.

[01:00:00] I remember it had its little moment, like a year or two ago. Is it still?

**Nader** [01:00:00] Yeah. NIM is, uh, you know, inference, uh, oil. I, I think it like for something is it is a log or acronym. Yeah. It just, just a name. But, um, yeah, NIM is, uh, how enterprises can take our uh, any of the, any of this technology and run it with support and all of that.

[01:01:00] And so that includes Daniel Mo. That includes, I don’t know all of our other optimizations that are packers up for Enterprise. Yep.

**swyx** [01:01:00] Anyway, so, so you, you got a bunch of experience start running the sort of internal inference gateway playgrounds.

**Kyle** [01:01:00] Yeah, I got And Bill also built how build NVIDIA’s first internal like vs.

[01:01:00] Code thing. We call it MB code.

**swyx** [01:01:00] That’s what I, uh, extension.

**Kyle** [01:01:00] Yeah, it was, it was a V first,

[01:01:00] like the fork vs code.

**swyx** [01:01:00] We jokes absolutely not. It just a while back they like, we should have a fourth vs. Code hackathon where you, that’s four. It’s the best four V vs code. We,

[01:01:00] we were, we were doing a hack how make a billion dollars, someone from VS code was there and he was like somewhat down to get involved and I was like,

**swyx** [01:01:00] oh, you should do that.

[01:01:00] That’s all. Then the cool thing became four chrome hackathon

[01:01:00] Chrome,

**swyx** [01:01:00] And no, no, no IDs or not cooling.

**Nader** [01:01:00] I saw, what’s it called?

## Hackathons And Autonomy Dreams

**Nader** [01:01:00] I was talking to Joseph, uh, from Robo Flow and uh, they’re partnering crime. We were talking about how with the new Alpha Mayo model, so Nvidia just released an open source. Uh, the, the Mercedes cars that you saw drag, she on Frazey?

**swyx** [01:02:00] Yeah.

**Nader** [01:02:00] Released. Will you open source, a autonomous driving model? Uh, I already, yeah, so we were thinking like, could we hackathon a driverless car? Like I have my old car. Let’s just try it.

**swyx** [01:02:00] We’ll take it,

**Nader** [01:02:00] take it to like, click train with a treasure eye, like in the middle of the day. Just like, just see, let everyone, like how many, how many cameras do we need?

[01:02:00] Right? Like, 1, 2,

**swyx** [01:02:00] 3, 4. They don’t. Five, six.

**Nader** [01:02:00] I don’t know. I, yeah. But, um, I think we’re gonna try, you just do it with us.

**swyx** [01:02:00] We can see, we could even

**Nader** [01:02:00] have a race. It’s like the first person to automate their

**swyx** [01:02:00] driving. Let me over a weekend. We do have an autonomy track at Will’s fair. Uh, WiMo was there like Yeah.

[01:02:00] Nvidia did send people that for Goot. Not because he didn’t have the driving thing yet.

**Nader** [01:02:00] Yeah.

**swyx** [01:02:00] Yeah. It’s, that’s cool.

[01:02:00] Yeah. I think comma, comma also has a version of this comma have open source driving. They’ve, they’ve done a fun hackathon on

**swyx** [01:02:00] music and he and I also, ‘cause I, I really, what I really want is a Tesla with Tesla level self-driving.

[01:02:00] Yeah.

**swyx** [01:02:00] But as a smart car, like a two seater. That’s the basic CPA wheelchair with a roof

[01:03:00] and only thing they make them, but the demand has d they, no, they realize this probably five years. Yeah. Really?

**swyx** [01:03:00] Yeah.

[01:03:00] They were d manufacturer.

**Kyle** [01:03:00] I thought it is one of those things, we’ll, where we’ll see someone buy the brand and it’ll be revived.

**swyx** [01:03:00] I, I would buy it like I

**Kyle** [01:03:00] probably. Someone hears this go by

**swyx** [01:03:00] your car. Yeah. Yeah. That’s crazy. Nobody Mercedes, because they, they’re like, I think 10 Mercedes, Mercedes, uh, I in Mercedes used

[01:03:00] to make them, I don’t know. I feel like they own the brand and you out

**swyx** [01:03:00] that’s your dream might come true enough. Okay.

[01:03:00] We we’re time notify and, and I was like, every time I, I try to park in San Francisco, I I have to buy a smart car because like 20% of the parking lots in San Francisco only fit smart cars.

**Nader** [01:03:00] Yeah. So, Hey, really?

**swyx** [01:03:00] That’s where, I mean, it’s mall

**Nader** [01:03:00] even it was late here trying to, this comes from someone that like, basically does

**Kyle** [01:03:00] not drive.

**Nader** [01:03:00] That’s where the, the Vepa was a life hack. Yeah, exactly. Yeah. You know what happened to the Vespa? Um, I used to have this yellow Vespa, uh, I left it outside the hacker house when we moved out. It trend. Um, it’s just, it was always there. And then like a month ago. It’s not there anymore. I’ve been meeting today.

[01:04:00] I don’t dunno. You could, it’s actually tv. You forgot about it.

**swyx** [01:04:00] Yeah.

**Nader** [01:04:00] And left.

**swyx** [01:04:00] Yeah. Yeah. No, this, it’s probably hazard. And speaking of hackathons, I also wanted say, give a big shout out to the world. Shortest hackathon. Let’s go. Uh, you did twice. You gonna watch a

**Nader** [01:04:00] handful of times? Yeah. There’s gonna be one at G tc.

[01:04:00] Oh, we’re doing pretty much we have a bunch of challenges that No, we haven’t released. And you get to bring your agent to come and attempt to, uh, go through those

**Kyle** [01:04:00] challeng again. It’s like a zero, the zero minute hackathon idea, which you just, you just bring your, I I approached eight, nine along a long time ago.

[01:04:00] You just bring your agent and then you press the go button. You’re not allowed to code. It’s just the Asian doing bond.

[01:04:00] It’s a good hidden email, right?

**Kyle** [01:04:00] Yeah.

[01:04:00] Do you make a jar? You make

**Kyle** [01:04:00] I there something I would love to see from cognition or someone else be like, come bring your agent. Drop it in

[01:04:00] because you don’t, you don’t know you like supervisor.

[01:04:00] Well let be a, you know, operate a browser, order a pizza. We’ll just see like that snake it, you know,

**swyx** [01:05:00] and

**Kyle** [01:05:00] you don’t know what the

**swyx** [01:05:00] task

**Kyle** [01:05:00] is. Yeah. You dunno what the task is like, or just like, you don’t even know what the judging categories are and then you give it the judging categories. Like, try as much as possible.

[01:05:00] It’s great though. It turns into like, yeah, so let’s build something on dining party. It’s a great business. See,

**Kyle** [01:05:00] anyway, funny story.

## Agent UX And CLI Everywhere

**Kyle** [01:05:00] Actually, we have a couple of people at Nvidia, we’ve been working with security to like bring agents really close to compute. So we now have like stuff where we can like tell Dynamo, like go run some experience with Dynamo, like on, X cluster and just like try it right now, like queue up once you get queued, like, send this request load and we’ve actually been able to like, just like, you know, like one shot problems like.

[01:05:00] We used to have this problem where you know, with Dynamo you have to like find the right configurations and we, sort of do it automatically for some parts of it, but you have to like a good initial configuration that you want to use. And we’ve just had like an agent just completely one shot that it goes, it gets the compute, it like runs a couple experiments.

[01:05:00] It’s like this is the best, this is this, these are part of the ER frontier. Go run this. And then we just like give that to people and it’s like faster than anything that they have.

**Nader** [01:06:00] Agent UX and agent marketing are super important. There’s stuff that we’ve been thinking a lot about. Um, Alec is like redoing the entire Brev CLI, um, so that you can fetch all the different compute types that are available.

[01:06:00] I don’t know, it’s gonna be really soon, but then you can, you can just browse what GPUs are available and then provision one say to it right there. And you can pipe all the commands. But I think it goes back to like the Alex CLI, like if you, coding agents. It’s kind of funny. I feel like coding agents have been so much more effective than general purpose agents.

[01:06:00] And I think a large part of that is it just has access to the terminal, like you said, and that means it has access to everything that you’ve installed into your terminal. It can run. So, you know, it would write code and, and it can compile the code and if there are errors, it can fix it, it can run your suite of tests because that’s all just in your terminal.

[01:06:00] And so that, you know, then for the idea, what come me really excited about the CLI, we’re now just turning through building CLI for the entire, like for the entire business. We Slack, building Slack, also. Workday, C-L-I-S-A Go. I, I’ve also done that for myself first. Really? Yeah. Yeah. Um, we’re gonna, we’re gonna open source all of this.

[01:07:00] And like yeah, all the, the I they’re just they’re the C yeah. CLI for the business applications. We would love for someone to run with this and like build like, I don’t know, like open CLI foundation in or something. Yeah. We, I Nvidia would love to support, uh, anyone that’s doing this.

[01:07:00] Like e every Devrel tool should really have good CLI support at this point.

[01:07:00] Yeah. Like at one point it was, you want your docs to be. Like accessible by an LM, right? You want LM Good dog. No, every, everything needs some CLI.

**Nader** [01:07:00] Yeah. It’s kind of funny, right? Like we, like computing began with a terminal with a shell, but we said that it’s not empathetic to, uh, humans. So we built these nice user interfaces and then now we have LMS navigating our user interfaces.

[01:07:00] And ironically, we’re not empathetic to the machine anymore.

**swyx** [01:07:00] Yeah.

**Nader** [01:07:00] Yeah. Just give the, the LLM access to the show.

**swyx** [01:07:00] One thing that slightly makes me uncomfortable is like, why do we have to build cli? Why can’t we just expose APIs? Like,

**Kyle** [01:07:00] I, I have, I have an interesting answer to this. So there are a couple reasons.

[01:07:00] Like there’s, there’s like, you know, portability is like one issue. Like, you know, like sometimes APIs are not like discoverable or like reachable by, by some, you know, types of things. There’s some element of locality, right? Like, uh, like the CLI is like literally you interfacing with your like local system, which is a little bit different.

[01:08:00] You could still do it by API, but like there’s this highlighting of like, what is the difference between like a CLI and an MCP, right? Like they kind of occupy the same purposes and you call them, it does something on the system and, and that’s done. I think that in pre-training there’s just an enormous amount.

[01:08:00] Oh, okay. Command line data. Yeah.

[01:08:00] Yeah. Like e even let’s ignore our, let’s let’s ignore our l Like you’re doing no harness, you’re doing no harness push training. Just the amount of like CLI versus API documentation for just like navigating this world of the CLI in your file system through that is just enormous.

**Nader** [01:08:00] Yeah. Yeah.

**Kyle** [01:08:00] Right. I

**Nader** [01:08:00] think there’s a, there’s a couple of things too. Like if, let’s say we wanna, so one I think your intuition’s, right? The CLI is just wrapping the API,

**swyx** [01:08:00] right? So functional

**Nader** [01:08:00] functionally, right? Yeah. And I think it’s nice because one, you’re, you’re being very, uh, specific and pedantic even, um, of what and that’s really good ‘cause you’re describing the problem space.

[01:08:00] So you know what the, I don’t know. I don’t wanna call it like what the, the space for vulnerability. You know what network calls you’re making, it’s not arbitrary and that’s not decided on the fly. That’s like pre-decided, which is important from a security perspective. But then if you were to write a bunch of API requests, you would probably do that.

[01:09:00] I don’t know. Would the model like use Python to do so? I kind of like that. Everything like a CLI is just dash because it’s ubiquitous. Like it’s just there. And you don’t have to make sure that there’s certain environment variables that are set up. Like if your Python versions, if the My Python version we’re using the same model to go do the same thing, is it gonna write like different code?

[01:09:00] It probably would. And so it’s kind of like an nice deal work, right? Yeah. Human. Yeah. No, I think just like making those decisions happen ahead of time versus yeah.

**swyx** [01:09:00] One last thing on this sort of agent, I guess maybe co-location or whatever you call it, uh, one pattern on tracking for this year, I always try to think about what’s the theme of this year gonna be last year?

[01:09:00] Definitely coding agents this year is definitely coding agents, breaking out of containment into broadening third world. I go Definitely has. So

**Vibhu** [01:09:00] you rent a human?

**swyx** [01:09:00] Yeah. Yeah.

[01:09:00] I’m on here.

**swyx** [01:09:00] Are you really?

[01:10:00] I’m like $5,000. I’ll do anything. Really? I think so. I need, uh,

**swyx** [01:10:00] my, uh, my borrow from Costco.

[01:10:00] Uh, but I think the best part is only the agent can book me, you know?

[01:10:00] Yeah.

**swyx** [01:10:00] It’s very

**Kyle** [01:10:00] usually like,

**swyx** [01:10:00] it’s just like another labor marketplace at Mechanical Turk was this.

[01:10:00] So definitely I have a weird story with why I did it. So back to your example of just giving agent access to compute, right? Yeah. You guys are GPU Rich at Nvidia. Yeah, I hooked up.

**Nader** [01:10:00] He’s not shy about it.

## Local GPUs And Scaling Inference

[01:10:00] I have, I have a 24 7 agent running, I hooked up to run pot.

[01:10:00] It doesn’t shut down instances. And I’m like, I’ve tried prompting you, I’ve given the instruction. Shut down when you’re done. It’s like I to keep it warm, I’ll need it soon. And it’s horrible on time estimates too, ‘cause like they realize it’s like. Yeah, I’ll need it in 45 minutes. 45 minutes, I’ll shut it down.

[01:10:00] 45 minutes of human time is actually three minute of agent time, so it’s like I’m booting it up, I’m waiting, I’ll just leave it on all night. And mo moo’s good at shutting down after something activity. I had it on my local server, like a little dual GPU thing. It just stays on. I have a little space heater at home now, but careful.

[01:10:00] So basically, you know, they don’t care about the concept of money just burn it. I need it. It’s useful.

**Nader** [01:11:00] And another DGX spark will be really nice. Like, I, I think I’m looking at it as super useful for agents because Yeah, you buy it once you plug it in and they it can rip. I’m gonna make a, I’m gonna make an Nvidia ad here.

**Kyle** [01:11:00] Okay. The Blackwell, like RTX 6,000 cards. Pro Pro only, like, I think it’s $8,000. Slightly cheaper. Yeah. Well, it’s much, it’s much cheaper than the data center cards.

**Vibhu** [01:11:00] Yeah.

**Kyle** [01:11:00] And it’s got 96 gigabytes of u gram. So if you and your, your crew want to go, like, run a local agent for you, you know, you, you in the home.

[01:11:00] I feel like, hmm. It’s got a significant amount of vra m I’ve thought about purchasing this and running in my basement, except my neighbors would hate me.

[01:11:00] It’s just a single, like two, three slot. GPU. It’s mostly,

**Kyle** [01:11:00] yeah, it’s A-V-C-I-E.

[01:11:00] Yeah, it’s

**Kyle** [01:11:00] UCI u. So GPU, you can go by that. I mean, the big difference against like the RTX, like gaming, GPUs, it, I mean, obviously it’s like blackball Pro, like it’s a pro GPU and it has a lot of E round, which means you can run pretty large models on it.

[01:12:00] You can stack four of them for the Maxim Q in a system that’s a beast.

**Kyle** [01:12:00] It’s beefy. You can run, uh, what is that, 96 ger or anything? 96, uh, you’re on a loge.

[01:12:00] Uh, but also they, they are slow. They’re not, I mean, performance of speed will be somewhat slower compared to API like,

**Kyle** [01:12:00] oh yeah, that, that’s true. So again, the big learning economy of scale allows you to do things that allow you to get both speed and throughput.

[01:12:00] Like you can run. I’ll give you an example. There’s an optimization called Wide ep. I’m not gonna go into it fully, but like it featured heavily in, in inference Maxim for Deep seek. And there’s a, there’s a great set of stories from Nvidia and from semi analysis about like why y EP is important, but for like MOE models, it’s like basically essential and you run it like the A Level app parallelism, the level scale up parallelism used for it is like 32.

[01:12:00] So it goes beyond that eight barrier. And it like really, really, really is important to have that M mbl, L 72, GB 200 MD link to serve at scale. And like, it’s like, I don’t remember the, the, you know, cost improvement I think against Hopper, right? Against Hopper. With this MBL L 72 system, you’re getting like 35 times cheaper per token for like a lot of the curve.

[01:13:00] Yeah. Which is crazy.

**swyx** [01:13:00] Yeah.

**Kyle** [01:13:00] And Normalize per GPU obviously because the part of the GP is cost or the code, the GST part of the cost.

**swyx** [01:13:00] One thing I’m exploring is the sort of, this year is also the year at the subagent, um, where you have the main agent, but then that also kicks off tools, which are in themselves, agents that have limiteds.

[01:13:00] Yeah. And sort of context locally, whatever, right? Yeah. Different prompts. So for example, one thing that Ian does is before you kick off a search, they do like a fast context model where you kick off April or you just to search, uh, across the code base plus all that. That is better than indexing. A a lot of the times, not, not all the times, and, uh, you should sell index for some picks, but like the idea that agents should be able to command subagent and probably run them like maybe close to inference as well.

[01:14:00] I don’t know if that’s like architecturally possible or even

**Kyle** [01:14:00] Yeah, we’re, we’re thinking about that for dmo. That’s like our big theme for the year,

**swyx** [01:14:00] because like you, like if you can design that into your stuff, then a lot of people, a lot more people will use it. Right now it’s like just kind of theoretical because.

[01:14:00] You do pay a lot of like back and forth, uh, coordination costs. Yes.

**Vibhu** [01:14:00] I think it’ll net speed up though, right? Like even at a basic level, speculative decoding, you’re running a small model, you’re running two instances, but it’s not,

**swyx** [01:14:00] that is one example. Yes.

**Kyle** [01:14:00] Yeah. But this is like a little bit like different with like agents.

[01:14:00] Agents, yeah. This is not spec. I think, I think there’s like a summarization of that trend that I like to do or I like to say to my team, it’s like, this is the year. So there are two things. This is the year system as model, right? Where like instead of having like a single model be a thing, you have a system of models and components that are working together to like emulate the black box model.

[01:14:00] So when you, when you make an API call to something that’s like, like a multi-agent in the background, it still looks like an API called a model. You’re still getting back to

**swyx** [01:14:00] grants, but under the hood.

**Kyle** [01:14:00] Yeah, under the hood. It’s like a billion different models. And that’s a lot of complexity, with Dynamo and with other libraries and media we’re, we’re looking to help manage

**Nader** [01:15:00] that complaint.

[01:15:00] Yeah. It’s funny because we actually, for CES, we just released the model router. Uh, for DGX Spark where you can have a local model that’s running on the spark and then also a foundational model and then the model router decides when to send queries to which one. So it’s no longer this like either or.

[01:15:00] It’s used the best stuff for everything that’s available to you. You have a good post-training bottle that’s running on

**swyx** [01:15:00] these. There are leads that are also the bread functionality of being able to manage the spark.

**Kyle** [01:15:00] Oh, that’d be cool. Oh yeah,

**swyx** [01:15:00] I did be able feature request. There we go.

## Long Running Agents And SF Reflections

**Kyle** [01:15:00] I actually like a question, like I, I like to like extend and flip over.

[01:15:00] How much longer do you guys think like agents are gonna be running? Because that’s one thing I’ve been throwing around, like, what happens when, I

[01:15:00] mean always are

**Kyle** [01:15:00] it

[01:15:00] even affects the, like back to the prefilled d the decode, right? Like, yeah. Codex is, I’d say, compared to cloud code, it’s much longer at tasks like, yeah, that thing, we’ll, like to run 6, 7, 8 hours.

[01:15:00] I’ll run it overnight.

**Kyle** [01:15:00] Yeah.

[01:15:00] And I’ll, I’ll go back and I have like a little crappy logging software I use and there’s just times where it wants to, like, I’m gonna go deep on research and it’ll, I eat up 80,000 tokens go on another go on another, yeah. Just eat through tokens and you know, that’s part of it.

[01:16:00] Like, at the end it does, it does hit a long task. And I think you only see that, that expense. Yeah.

**Nader** [01:16:00] I, yeah, there’s insatiable demand for tokens and every improvement that comes kind of just makes our demand even higher. It’s kind of funny, right? Like if you have like a teammate and you ask me to do a task and they’re like, should I save some effort and not think too hard about this task?

[01:16:00] I’m like, fuck no.

[01:16:00] I mean, my favorite was like, you can, you can have four shots, right? Yeah. Like the original codex before the app. You, why do one call, like, give it four attempts? Just, just use all the token to out, right? Try Moreal try, try again. Try more. It’s

**Kyle** [01:16:00] like, it’s like the, the meta index right?

[01:16:00] Is the thing that tracks like how long models are able to run. I expect that we’ll just see like log linear, if not log super linear growth. We will see before the end of the year an agent that is capable of running for longer than 24 hours with like self consistency the entire time.

[01:16:00] I, I would also poke at different domains, having different desires, right?

[01:17:00] Like at a consumer level. I’m getting slightly frustrated at 20 minutes per basic query. Sure. You can optimize, you know, six, eight hour. I don’t see myself shooting off many one week agents. Right. Someone doing like, okay, GPU kernel research or medical or biological, like, you know, in, in those domains Sure.

[01:17:00] Shoot off a lot. That take a, so like I think it will be somewhat domain specific ‘cause you also really need to turn that in. Right.

**Kyle** [01:17:00] It’s funny one, those was doing your taxes. Right. Like, that’s tax. Yeah, that’s, yeah. Okay. Yeah.

**Nader** [01:17:00] Get it right. I wonder if like this major school say sort of like, uh, speculative decoding is like your agent figuring out what you might be prompting it the next day at night and like pre fetching.

**swyx** [01:17:00] Yeah, you can do

[01:17:00] that.

**Nader** [01:17:00] Yeah. Really? Branch, branch prediction.

**swyx** [01:17:00] Oh, well no, that, well, that’s, that’s too, that’s too low level, but yes. Sorry. Yeah, yeah, yeah. One question I gotta get, so like, uh, we actually did record a part with the, the beat folks. Uh, with Sarah right here, their chart is the human equivalent work, uh, hours of work rather than how long it has themselves are, are being autonomous.

[01:18:00] And that, that’s a huge difference, right? Like human work, five hours agent work, 30 minutes, like it’s actually 30 minutes not, uh, yeah. Firearms, right? Like, so like that, that, that chart that you see is them estimating what the human equivalent replacement is. Um, I think the, I think actually Enro release a more recent chart.

[01:18:00] That showed cloud code autonomy from their production traffic numbers, and that was 20 to 45 minutes. That’s roughly where we are. So yeah. Yeah, that’s the sort of realistic thing. I mean, I, I do think like there’s experimental setups we can just like, Ralph with and like just prompt it to keep going, uh, when it stops.

[01:18:00] And obviously you can, that can go arbitrarily long,

**Nader** [01:18:00] I feel like

[01:18:00] from my

**Nader** [01:18:00] experience. Yeah. I guess 20 to 40 minutes seems right for when I’m using like Codex or cloud code. But then like what, I always try to just, like, if I wanna spin up like a new, there’s a net new project, I’ll, I’ll often start to rep it and like it’ll end for I believe, yeah, yeah.

[01:18:00] Like spin up like the, their new, like from the V three agent. Like it’ll spin up a web browser and like click around and discover new bugs and just keep churning. Um, so I, I think like my longest was like over an hour that, hey, I’ve been churning

[01:18:00] I think before we see super long running. I think there’s gonna be a bit of an efficiency hit.

[01:19:00] So. Sure you can take an hour and go down paths, but you also want you wanna be more efficient, you wanna be smarter in your reasoning, right? So I think that’ll actually go down before we go back up. Like, you don’t wanna scale non-optimized systems just for the heck of it. As much as I love saying, use all the tokens, um, you know, they are expensive.

[01:19:00] Like going from dance to reasoning models, that’s an added cost, right? You’re paying for a lot of tokens and it doesn’t make sense to just scale stuff that’s not optimized. So there’s, there’s always that little balance.

**Nader** [01:19:00] Yeah.

[01:19:00] But you know. I think you’ll see both sides of it.

**Nader** [01:19:00] Yeah. So 2023 was super exciting.

[01:19:00] I think if you were in SF you were like, okay, uh, I know this is gonna be a huge world changing moment, but it seemed like, you know, no one had known yet. And maybe even before, was it 2022 maybe?

**swyx** [01:19:00] Yeah, yeah. I would say, yeah, like RU had this tweet where like everyone was in SF from like 2021 to 2023. Yeah.

[01:19:00] Understood what it was like to be late, early.

**Nader** [01:19:00] Totally. Um, yeah, 2021, that’s when I made my first open AI account. Yeah, it went, um, it was crazy. And I remember it was so funny ‘cause at the time SF had not been doing well. So pretty much what it felt like was the concentration of founders in the city had ro had risen because, um, where my neighbors were used to doing a bunch of stuff, those people had all left.

[01:20:00] So the only people that were still in the city were people that really wanted to build It was cheap tech. It was, yeah. It was also way cheaper. I feel really bad anyone, uh, who is trying to get rent now, but there was, uh, cell was they had a huge office.

**swyx** [01:20:00] So blockchain in Yeah, like took over the, the old Casper building.

**Nader** [01:20:00] Yeah. They had the showroom and they had the, like the, what would, I think it was like the back warehouse. It was, and it was a huge office. And

**swyx** [01:20:00] it’s right across an opening Eyes in New Link.

**Nader** [01:20:00] Yeah. It was in

[01:20:00] the original arena.

**swyx** [01:20:00] I named the Arena because of it.

**Nader** [01:20:00] Yeah. Yeah. And so it was really exciting because like vo flow I think uh, I forgot the Minify.

[01:20:00] Yeah. Minify, uh, brev was there. You guys were there. I remember. That was actually, it was there that you bought the AI engineer domain.

**swyx** [01:20:00] Yeah. I didn’t know what I was gonna do in ai. I, I wanna do something,

**Nader** [01:20:00] but it was kind of this, it was a really fun moment where we were kind of all in this solo space and it, um, I don’t know.

[01:20:00] It was, it was a really cool community, especially being so

**swyx** [01:21:00] early. Yeah. And so it, then you got me early cruise access. Oh yeah. So there was a going period of time. They both cruises and Waymo’s were just free. Yeah, always.

[01:21:00] If you had, I mean, they’re, they’re so Back Cell is opened again.

**swyx** [01:21:00] Yeah. So Nature Zoo.

[01:21:00] Zoo is Nature Zoo. Zoo Robot Taxi. Yeah. So Totally. Yeah.

**Nader** [01:21:00] Oh. But yeah. And so it’s actually really cool that you guys have this studio so close to, uh, cell. Yeah. This rock climbing gin right around the corner. It was like, um, 2000. Oh yeah. Yeah. It’s, it’s an awesome block.

**swyx** [01:21:00] Cool. Yeah. Just, and you bit services partnership.

[01:21:00] Uh, I do think one, one thing I try to do with the podcast is like bring, like what is, I get to be a San Francisco to the rest of the world and also just like. Maybe give, uh, yeah.

**Nader** [01:21:00] Yeah. My favorite talk was in the city, uh, and

**swyx** [01:21:00] yeah, stick and stream. I know. It’s very good.

**Nader** [01:21:00] Yeah. And I guess what it’s like to be in San Francisco I think is just everyone seems to be super supportive.

[01:21:00] Uh, sometimes I feel like the city believes in you more than you do. And even, uh, I don’t know if you remember, but I remember posting my first blog post and I had met you on Twitter and you gave me like an hour of your time super randomly, and you kind of coached me through, uh, writing content for developers.

[01:22:00] And I was trying really hard not to come off salesy or plug myself. And so I kind of stripped all personality out of the blog post. Yeah. And you, you brought that out. You’re like, people don’t, it’s, it’s okay to talk about what you’re doing. Like you don’t have to be weird about it. And I remember just that, I think that really helped me kind of figure out what our voice is and not shy away from it.

[01:22:00] And so always really grateful for you. Hey, you inject your voice into like, everything. Now it’s actually a huge advantage to be like very

**Kyle** [01:22:00] genuine about what you care about.

**swyx** [01:22:00] Yeah. Yeah. You imagine like summer, some infra in DMU and like, it’s like, can you gimme feedback on this blog post? And it’s pretty boring and you’re like.

[01:22:00] Find like, you know, he looks interesting. I’ll just do a zoom call and then you meet this guy. Yeah, right. He’s so energetic, so just be right. There’s, but like, I think people are trained to write a certain way in school and Yeah. They never totally see there’s like a broader well,

[01:22:00] and

**Nader** [01:22:00] lots un unlearn

**Kyle** [01:22:00] writing.

[01:22:00] Writing is thinking and like everyone thinks differently. So like, might as well as just like,

**swyx** [01:23:00] yeah. Yeah.

**Kyle** [01:23:00] Write your way.

**swyx** [01:23:00] Cool. Well, thank you for, uh, in indulging with us, uh, really broad breaking discussion, but I love, like, you guys are like, sort of like the sort of young faces on video with so much energy and, but like also lot of technic death and I think, uh, people learn about for this session.

[01:23:00] So thank you.

**Nader** [01:23:00] This was awesome. Thank you guys. So thank you for everything that you’ve done in the talk. Yeah, NG the podcast, all the above. And uh, C-O-T-C-I really forward to it. Yeah. Cool. Thanks. That’s awesome. Thank you. Thank you.
