---
podcast: "how-i-ai"
podcast_title: "How I AI"
title: "How Meta designed Muse: an AI agent people actually want to talk to | Alex Cornell (Design Director)"
date: 2026-10-12
url: "https://podcasters.spotify.com/pod/show/pen-name/episodes/How-Meta-designed-Muse-an-AI-agent-people-actually-want-to-talk-to--Alex-Cornell-Design-Director-e3q4g9k"
guid: "8a9ad69c-5c61-4b08-b8c1-13c391cb57d4"
host: "Claire Vo"
guests: ["Alex Cornell"]
format: "interview"
level: 1
length: "00:37:19"
categories: ["consumer", "agents"]
featured: ["Meta Muse"]
mentioned: []
transcript_source: "azure-asr"
transcribed_by: "MAI-Transcribe-2"
---

# How Meta designed Muse: an AI agent people actually want to talk to | Alex Cornell (Design Director)

**Claire Vo** [00:00:00] Designers have struggled with how much do we narrate along the way what is happening, so it's quite obvious to the user, so that latency doesn't feel so painful. My experience in the Muse app is, I do like that progressive disclosure, and it's one of the things I called out in our review, but also it's just fast. Like, it is just fast.

**Alex Cornell** [00:00:18] If you are a engineer, you may want to know exactly what your agent has done, and you can find that in Muse. But if you're a normal person, you maybe just want to know, like, is it doing something? So at the top, it'll tell you it's working. I'm very happy with our solution currently because we've sort of like exposed the benefit of the main chat to people, but I feel like there's a lot more that we could do in terms of helping people organize. I had a blog 20 years ago, and I had Marlo go and find it and then accumulated them into one PDF first, but the way that I like to read it now, just again from memory, is via a podcast, and Muse is able to take it and just like reform it into a way that's like really interesting and useful for me.

**Claire Vo** [00:01:01] When your Muse is being obstinate, what is your prompting strategy? What do you do? Welcome back to How I AI. I'm Claire Vo, product leader and AI obsessive, here on a mission to help you build better with these new tools. Today we have Alex Cornell, design director on Meta's Muse, and he's here to talk a little bit about how to design a great agent experience for consumers, and a little bit more about some Meta Muse use cases you might not have thought of, especially ones that involve shopping on Instagram and going really hard into some of your personal hobbies. Let's get to it.

[00:02:01] Alex, welcome to How I AI. Thanks for joining us. Thank you for having me. Big fan. Happy to be here. I am, I was just saying, I am a big, big fan of Muse, and I have used probably every AI agent on the planet, and Muse, I will tell you, fastest time to pure delight I have had with an AI product in a very, very long time.

[00:03:18] So tell us a little bit about how you approached designing this agent, because I think some of the primitives you picked are very different than what we see in other agents. It seems like the persona that you're going after is different. Walk me through how you all ended up where you ended up from a design perspective.

**Alex Cornell** [00:03:37] Yeah, well, thank you for saying that. it was definitely a really interesting challenge, and it felt like a unique one. I think we all could feel that something was different this time around, I think, from a capability. And I think, like, just simple things like the fact that an agent can message you proactively changes the nature of, like, how you think about the product from a design perspective, even in, like, super simple ways. Like, I've joked before because we have bubbles around our messages, you know, and, like, that's typically something that you associate more with messaging than, like, an AI app. Like, long ago, I think most AI apps kind of stripped those out. And that is there, among other reasons, to like help with the like separation that you need when like a agent is possibly messaging you at different times of the day. You kind of need to know like where and when the different messages begin. And so like simple things like that, I think, inform some of the design, but the basic framing that always we went back to, and I think was probably the most helpful, was just imagining that this interface was more of an exchange between you and an entity, and that's why it's embodied at the top of the screen.

[00:04:47] And so a lot of the patterns that we looked at were much more messaging patterns, you know, and not thinking about how did this work before in different AI apps or using kind of like the traditional industry, I guess, as a reference. It was more like, how would you handle this if you were actually speaking with another person, you know, and that was immensely clarifying, I think, in almost every decision that we had to make, and I think defines kind of how it feels, you know, when you look at it, it feels like a messaging app. You see a little guy there at the top of the screen, and I think like that, even something like that, you know, one of the other capabilities of it being able to work in the background makes it really important that you know when it's working. And so, like, just simply having that status, I think, has been one of the most important decisions that we made.

**Claire Vo** [00:05:33] The other thing that strikes me as very different about Muse is the primitives that you've chosen to elevate as core parts of the application. Because I think for those of us who have been using AI building tools, chatbots, et cetera, we're used to these ideas of like threads and chats and projects and machines and files and diffs, like, and connectors, like they're these very software-centric concepts, I think because a lot of these agents have primarily been built as coding agents for the enterprise or knowledge work agents. And then I look at Muse, and what really struck me is you have this like character, first of all, as a primary entity. You have chats, you have ideas, you know, you have these, you have your feed, like you've just chosen different aspects to elevate. Is that because you knew that this was going to be serving a different type of user with a different kind of like breadth of intention around what this agent could get done for them?

**Alex Cornell** [00:06:39] Yeah, you know, I got a text actually from my mom, like this morning, which is really funny. She said that she has apologized to her muse for making him work so hard and thanked him for all that he's done for her, which I found really gratifying because I have been working in software for a long time, and I don't think my mom has ever used a thing that I've made, not because, like, I don't make interesting things, it's just, like, to your point, I think typically they can be maybe a little bit inaccessible to kind of the average person, and I think with this kind of technology too, it is so new and has so much capability to it that's not obvious. I think like that was definitely a huge part of what we were after in terms of making this more accessible and intuitive to for people to use. And I think like, I mean, you hear a lot about progressive disclosure in design, and it's kind of one of those things that like you hear like on day one and then you always think about, but I don't know, you don't use it every day, but in this product, I found it to be one of the most helpful things, which is like if you take something like status, it's like if you are a engineer, you may want to know exactly what your agent has done, and you can find that in Muse.

[00:07:51] But if you're a normal person, you maybe just want to know, like, is it doing something? So at the top, it'll tell you it's working. Jollybot is working, and then your next question might be, what's it working on? You know, and so it will tell you that with the little emoji, like researching pumpkin patches. But then if you want to go a little bit further, you tap on it, and then you have a list of everything that it's done. If you want to go a little bit further, you could tap on that, and then eventually you get down to where you're going to see the curl and all the, like, all the code and everything, which is really important from like an auditing perspective. but it's only there if you need it, and it doesn't get in the way for people who may not know what that means. And I think, like, you see, like, a lot of what is traditionally referred to as chain of thought can get pretty loud and, like, really detailed in the core chat. And that's the kind of thing I think that, like, typically we would have just put that in there because that's like what you do these days in AI apps. But I think in this case it was like, well, does it really need to be there for everybody? It's like, probably not, you know.

**Claire Vo** [00:08:51] I'll give you one other compliment because, again, I am a muse girl now, but I also think that a lot of times these chain of thought reasoning user, you know, like elements in the UI are there as a band-aid for latency, which is it feels very frustrating as a user to sit and wonder, is my agent working on something and is it making progress or is it just stuck? And so I think a lot of designers have struggled with how much do we narrate along the way what is happening so it's quite obvious to the user so that latency doesn't feel so painful, versus how much do we kind of like do progressive disclosure. And what I think is nice about my experience in the Muse app is I do like that progressive disclosure, and it's one of the things I called out in our review that I thought was quite nice, but also it's just fast. Like, it is just fast. The model is just fast. Like, I do think for especially something that's going to try to catch the eye of consumers, that latency really matters, and it's a zippy little agent.

**Alex Cornell** [00:09:53] Yeah, it is, and it's really, you know, it's interesting actually because it's one of those things where sometimes it's so fast that you are tempted to think, like, is it, like, did it actually go do a thing? Like, 'cause it's- it's so quick? And I think, like, the nice thing is there are times where it will- you'll ask for something somewhat complex, and it will at least acknowledge your request, you know, either through a reaction or an initial message, and then go off and do the hard work. And I think, like- like a person, you know, if you ask for something hard, they're not gonna just ghost you until they're- they're done. They'll usually just say, like, "Okay, here's the plan. I'm gonna do this.

**Claire Vo** [00:10:29] Mm.

**Alex Cornell** [00:10:29] I'll be back when I have it done, or even just a reaction is enough to let you know that it's doing it. And so I think like that balance of when to respond quickly, how to respond, what to say, and then like what to do in the meantime if it is a really long task. And that's where we start to rely a little bit on that status display to let you know like what's going on. And if you want to know like specifically, did it get stuck or is it like going down the wrong path, you can check, and I think that that's really helpful because you never really feel like it's just gone off and left you alone.

**Claire Vo** [00:11:01] Yeah, one other thing, just thinking about this status message I want to talk about, which is this concept of generative UI. And I think a lot of people think, when they're thinking about generative UI, they think like every time I log into my dashboard, it's different, or every button I click is unique for every person. And what I saw in looking at the Muse agent is you're using generative UI in a really elegant way, which is like the core primitives stick. You got your avatar, you've got your status message, you've got your ideas, you've got your feed. But then within that, every time I log in, I have a new set of ideas that are based on the things that we've talked about. And every time the status is generated, it picks the exact right emoji, and when it's working on its computer, you get a little generated video of it typing on its laptop. Like, that type of quote-unquote generative UI, I think, is really delightful and much easier to understand for folks trying to understand how they could bring these concepts into their own app than, like, every time any one person opens up, the UI is completely different.

**Alex Cornell** [00:12:09] Right. Yeah, I think, you know, perhaps one day we'll get there, you know, but I think these days there's- it's definitely a little bit more on the rails in terms of like where we can apply it. The avatar is a great example, and I think people find a lot of delight, I have seen, when they do make their own new avatar, seeing that it will then be translated into each one of those states, you know, typing on its little computer or making something. And that's been one of the most fun things, because we, of course, have our mascot, and, you know, Jolly has the states as well, but like if you turn yours into a tomato, then you'll see a tomato typing on the computer, and that really does feel very personal and is, I think, a very delightful thing. But yeah, you mentioned feed and ideas, and I think that those surfaces, you know, you could very, you could definitely imagine this app with just chat, and I think part of an agent's power is that it can handle a lot in a single chat, and you can kind of just treat it like a really capable, personal assistant in that way. I think, though, like, there's so much that it can do that might not be intuitive for people, that exposing some of those additional capabilities, just with the additional surfaces that we have, like ideas in particular, it's serving a very specific purpose, which is basically just telling you some things that you may not know that it can do.

[00:13:24] I think, like, to your point, if those were just generic suggestions, that would be one thing, maybe even useful things, but when they're specifically based on what you've talked about, I think that's when people really find the power, where, like, if you talk to it about golf all day, like I do, like, then I get a lot of golf ideas. And then the feed too, the feed's a fun one because you can experiment, and I think people should experiment more than they do. It's like the, you can write anything you want in the prompt and get a feed of whatever. Like, I mix and match things all the time and, like, have a really, really interesting feed, and I often change mine too, just because, like, sometimes I'll get tired of getting, like, Muse news or something, and I'll switch it to something else. Like, I try to do, like, kid stuff on the weekend, for example, but yeah, I mean, it's still a native surface, though. You know, like, the feed unit that you're looking at is still, like, one that we've designed, and it's being powered by the intelligence of like and the personalization that your muse has, but it's like it's not yet like a fully generative surface.

**Claire Vo** [00:14:25] Okay, so speaking of ideas or things that your muse can do for you that you wouldn't thought of, I'm going to let you get your screen up and share with us some of your ideas. And while you're doing that, I will tell you what my muse's name is, which is Slime.

**Alex Cornell** [00:14:39] Oh, yes.

**Claire Vo** [00:14:40] And Slime is a pink dinosaur, um, fashioned after my child's favorite- favorite stuffy, um, and he is very adorable. Okay, so let's look at- look at Mario. Ah.

**Alex Cornell** [00:14:51] Yeah, so mine is- mine is Marlo, which is a cactus.

**Claire Vo** [00:14:54] Marlo.

**Alex Cornell** [00:14:54] And I- I have a bit of a complex relationship with Marlo because my original muse was Jollybot, which is the-

**Claire Vo** [00:15:01] Mm.

**Alex Cornell** [00:15:01] the mascot that- that you see everywhere, and it's named after my daughter, who we call Jolly Bug. And when we started using Jollybot everywhere, I felt kind of weird using Jollybot for mine 'cause it was like it was just too close to home, so I made kind of a cactus version, which is Marlo, which I like a lot, especially Marlo's little cactus laptop.

**Claire Vo** [00:15:20] I love the fuzzy laptops, just send me. They are so funny.

**Alex Cornell** [00:15:26] They're really funny.

**Claire Vo** [00:15:26] Okay. Well,

**Alex Cornell** [00:15:28] Um.

**Claire Vo** [00:15:28] walk me through some things that you do with Marlo that are fun.

**Alex Cornell** [00:15:32] Yeah, uh, I- I'll- I can show you a few things. So, I think one of my favorite things recently is I had- and I would recommend doing this, by the way, I had- if you use Instagram, I had Marlo look at everything I'd saved on Instagram and just organize them. So put all of my saves into folders and categories, useful baseline. Um, but then I said, "Okay, look at everything I've saved and maybe send me some suggestions for shopping ideas, like gifts and that kind of thing. And it did that again just in text, which was a good idea. But one of my favorite things I think to do with these systems is take what would be otherwise like a fairly mundane set of data and render it in a way that I personally find really fun. So with this, what you're looking at here is Jollybot Sky Mall, which is that same set of suggestions that have looked at everything I've saved on Instagram, considered some ideas for things that I might be interested in, but then rendered them in the kind of the vernacular of the Sky Mall Sharper Image magazine. So as a 90s kid, this is like very, this is speaking my actual language.

[00:16:37] so like this clock, for example, you can see right here, was a good suggestion.

**Claire Vo** [00:16:42] Oh, it's yours.

**Alex Cornell** [00:16:44] Yeah. So this is a fun one, and I think, like, it's refreshes every day, and it's kind of like a- a really interesting way to, like, both from, like, just for me personally as a designer to look at 'cause I think it's a really fun type of crazy design, but also, like, you know, I may be one day in the market for a new rangefinder, so it's nice to see that.

**Claire Vo** [00:17:04] I lo- I love this. And then have you- I just- I'm curious, have you transacted with Marlo on, like, have you bought- has Marlo bought you some things?

**Alex Cornell** [00:17:14] Yeah, I- and- but probably not anything that exciting, like watch straps and things like this, you know?

**Claire Vo** [00:17:20] Yeah.

**Alex Cornell** [00:17:20] Like, I think, uh- and I've had- like, I- one of the things I do most, actually, with mine and probably my favorite use case is, like, I feel like a kind of just, like, monitoring superpower where

**Claire Vo** [00:17:33] Mhm.

**Alex Cornell** [00:17:33] I, like, always looking for, like, "Oh, if this artist releases a new album, tell me. Okay, great. If this

**Claire Vo** [00:17:39] Yep.

**Alex Cornell** [00:17:39] artist comes to San Francisco, tell me. If this golf brand does a collaboration with this person, tell- like, I have a lot of things kind of, like, on the- on the radar.

**Claire Vo** [00:17:47] Yeah.

**Alex Cornell** [00:17:47] And so, like, usually, like, uh, you know, everybody always talks about- and I remember from your thing, movie tickets. Movie tickets

**Claire Vo** [00:17:53] Mhm.

**Alex Cornell** [00:17:53] is a big one as well.

**Claire Vo** [00:17:54] Yeah.

**Alex Cornell** [00:17:54] Um- So, yeah, I have, and, uh, I think that it's definitely, like, something that is, um, it's just really useful. I haven't hooked this- that's actually something that I would like to do. I haven't hooked this up to where I can, like, make it easy to, if I do see something I like, go and get it, but it's mostly because this is more of a fun thing for me that I just love seeing these things rendered this way.

**Claire Vo** [00:18:16] You know, the other thing that you can do here, which I do, is I have a trigger that every week it looks at the list of stuff that I'm, like, interested in buying and sees if any of it is on sale, and so it'll be

**Alex Cornell** [00:18:28] Oh.

**Claire Vo** [00:18:28] like, "You know, that thing you've been waiting for, it's- it's now discounted," or, you know, this- this vendor happens to be selling it at a-

**Alex Cornell** [00:18:36] Ah.

**Claire Vo** [00:18:36] on- on sale, and so then I just get that, like, just-in-time discount

**Alex Cornell** [00:18:40] Yeah.

**Claire Vo** [00:18:40] on things. I also do

**Alex Cornell** [00:18:41] That

**Claire Vo** [00:18:41] a lot

**Alex Cornell** [00:18:42] nice.

**Claire Vo** [00:18:42] of price comparison.

**Alex Cornell** [00:18:44] Yeah, yeah, yeah, I d- and I did- I do a lot of research as well too, like, whether- whether it's price or just kinda like- what reminds me of, like, used to be a very manual process of, like,

**Claire Vo** [00:18:53] Mhm.

**Alex Cornell** [00:18:53] "Okay, I'm in the market for a toddler car seat." You know, it's like,

**Claire Vo** [00:18:57] Mhm.

**Alex Cornell** [00:18:57] normally that would kick off a lot of web searches, a lot

**Claire Vo** [00:19:00] Mhm.

**Alex Cornell** [00:19:00] of, like, YouTube watching and everything like

**Claire Vo** [00:19:02] Mhm.

**Alex Cornell** [00:19:02] this, and now it's like I usually start in Muse with whatever it is and then kinda go from there.

**Claire Vo** [00:19:07] Yeah. Well, and I- I do think people are really- I haven't heard a lot of folks talk about the Instagram connector, it's one that I also use a lot. It's just a- it's a very rich source of personal information that has historically been in a format very hard to reason with. So, and now it is in a format that I can actually, like, reason and extract that value out of it. I use a lot of- I use a lot of Instagram. I use, because now these agents can log into websites I use- I like use my Pinterest a lot more too. I use these like visual records a lot more, um, than I had in the past. One kind of like for the designers out there, one of the things that I've done recently is like open up a board or a saved group and said like, I like this, help me generate concepts based on this or language I can use to describe this. And so I think the ability for these agents to reason with visual data in a way, especially if you can just log into a website or use an Instagram connector, just really unleashes a lot of creativity and use cases I feel like have been harder to do before.

**Alex Cornell** [00:20:16] Yeah, Pinterest is a great idea too. I mean, I think like, to your point, the, I feel like I have scattered about the internet a lot of this information that's kind of just gotten lost to time, you know, and so, like, my Instagram saves, for better, for worse, I've been using that forever, but I very rarely go back and mill about in there and, like, look at them, you know, 'cause it's like you're kind of just- I don't know what I would be doing necessarily. One thing I did, actually, I don't have it here, but I do save a lot of golf tips and- but, like, hundreds, like hundreds and hundreds of golf tips that I never go back and look at, so I had Marlo do it and then consolidate them all into like a manual, and so that I had this like, kind of like, for Alex, like, these are the things you should work, apparently you think you should work on, you know, and it was that was pretty cool because it was like otherwise kind of just buried in time, you know. And actually, to that end, I have this one too, which I like. This is another Instagram one, but I do post a lot of stories, and this one is basically just showing me an archive of random stories from the past that, again, I would never look at.

[00:21:23] Um, and it's kind of like- I mean, I almost think of this as, like, my new kind of feed

**Claire Vo** [00:21:27] Mhm.

**Alex Cornell** [00:21:27] that I'm looking at

**Claire Vo** [00:21:28] Yeah.

**Alex Cornell** [00:21:28] where it's like, uh, you know, this is just mine, but I'm- you could bring in any kind of content here. And, like, I love looking at this kind of stuff, it's just kind of, like, nice memories, and I'll check it

**Claire Vo** [00:21:36] Worn

**Alex Cornell** [00:21:37] a couple times

**Claire Vo** [00:21:37] your heart.

**Alex Cornell** [00:21:37] a day. Yeah, exactly, yeah. And, like, I, you know, have a 5-year-old, so it's fun seeing, like, little things of her, like, when she was growing up. Um-

**Claire Vo** [00:21:45] Okay, you mentioned golf, and we're gonna talk about Muse for going hard on your hobbies. So

**Alex Cornell** [00:21:51] Yes.

**Claire Vo** [00:21:51] let's talk about how are you

**Alex Cornell** [00:21:53] Yeah.

**Claire Vo** [00:21:54] using Muse for your golf game, which I,

**Alex Cornell** [00:21:57] Yeah.

**Claire Vo** [00:21:57] you know, as a parent of a 5-year-old, I'm presuming is inconsistent at best.

**Alex Cornell** [00:22:02] I know, yeah, I- I used to always joke about this with people on the team because I- a lot of what I would want to use Muse for was golf oriented, but that's sort of assumed that I was able to play golf, but like we've been building this project for so long that it's like kind of very few and far between when I'm able to get out there. But yeah, I use it in a couple ways, and I think what's nice about this is, similar to some of my other hobbies like chess, there are services already that I use that monitor like how I'm playing. So every time I play, I record the round. That's a thing most golfers do. And so that's like some basic data about the course that you played, what your score was. Um, but I also keep track of every shot that I hit on a watch. And so I have a lot of data that I can provide, and what I do is I just have it every week, which is- this is again kind of sad because it looks every Sunday and I never play, so it's like I could probably just tell it every so often, but it will send me this basically every time I play, which is kind of like a round recap. So I'll see kind of like how the round unfolded, much richer than like a paper scorecard or some other way that I'd be able to see it.

[00:23:05] And sometimes, I don't think this one has it in here, it will tell me a little bit about the course if I played the course a lot, and it will like tell me, okay, on this hole, this is usually what's happened, you did better today or worse today, which is really helpful when I go back and play the course again. This one's doing a little bit of that, like it's trying to tell me like how I could have turned my 84 into a 79 by just like doing a little bit better here or there. The interesting thing about this one is, and again, we've talked a little bit about this, but I think like it's taking data that like was pretty much very plain and monolithic and not really showing me more than the number and turning it into these different visuals that like tell much more of a story. Like I had this, the red line is like a very bad front nine, and then the back nine was a very good back nine, and you can see that with the graph, like, very easily. That'd be much harder to do if you're looking at the scorecard. So this has been great. I also, whenever I practice, I have a lot- I feel like when I'm practicing, I'm like those people you see running with oxygen on with all the wires hooked up to them.

[00:24:05] Like, when I can only practice every so often, so when I practice, it has to be very, very data oriented. So I have all these machines that are looking at me when I swing. And this, again, it's like putting out all this stuff that, like, I kind of understand, but it's really helpful to get Muse to, like, really go through and, like, tell me about, like, where I can improve, like, what I need to do better, what's looking good, and that's what you're looking at here is like a practice session really broken down into the fine detail. I think, like, golfers will know what this stuff means, but it's kind of, it's, you know, it's kind of like a, it's a, it's very useful, I should say, um.

**Claire Vo** [00:24:42] And- and do you have a muse goal to get better?

**Alex Cornell** [00:24:46] I do. I have- and this- this is one that, yeah, like I said, kind of a sad one I make no progress against, but

**Claire Vo** [00:24:52] Mhm.

**Alex Cornell** [00:24:52] that is one of my long-term goals. So I have a lot I mentioned of things that I'm tracking. I love the tracking section in particular just because, like, I- there's a lot that I keep an eye on. But in terms of long-term goals, it's basically I would really like to be a single-digit handicap in my life, which is like, it's achievable, it's hard, it's kind of like the perfect goal because I can talk to Muse about it anytime, and like it knows that all these things are kind of like accruing to that goal. It's kind of the perfect, like, hopefully not super long-term goal, but it is definitely one of my main ones.

**Claire Vo** [00:25:28] Quick, quick question about Muse, and this could be maybe personal preference, or you could just give our audience a little bit of insider tips on how to use it. Main chat or side chats? I haven't decided

**Alex Cornell** [00:25:40] Yeah.

**Claire Vo** [00:25:40] if one is better than the other. I like my impulse is towards side chat, and I don't know if that's just a artifact of how I've been working with other chatbots, or if it's actually useful.

**Alex Cornell** [00:25:51] It's a great question. This is actually one of my favorite things to talk about, because I think it's such an interesting architectural problem in the space. And, you know, the way Muse is designed is there's a canonical main chat that is kind of very intentionally the primary main line, and we sort of feel like you could use that entirely if you wanted to. We know that for a lot of people, especially anyone that's used to the way most of these apps work today, that threading is a very useful way to organize. So we have side chats for that purpose. Like, if you want to put something specifically in, like, just to get it out of your main chat, or it's like a very scoped problem for whatever, whatever it is, there's lots of reasons why you might want to do it. that's why side chats are there, but it is definitely like a single thread with the possibility of side threads, whereas most apps are all threaded. That's kind of like the traditional model was like a new thread every time you open it, you know.

[00:26:51] and I think once the models were able to handle the context and be able to manage everything in a single chat, to me, that is a little bit easier way to interface with what you feel like is a another entity, the same way you would have with another person. You know, like I don't side thread with my mom or something like that, you know. Now, all that said, I think that there remains a lot of really interesting work to do to kind of like up level this to maybe you could say like the agentic era. I feel like even still, this is sort of an underexplored area where I'm very happy with our solution currently because we've sort of like exposed the benefit of the main chat to people, but I feel like there's a lot more that we could do in terms of helping people organize and, like, really understand the difference between the main chat and the side chat, because your question, I think, is a good one and one that, you know, a normal person could very reasonably come to too and just be like, "Why would I use this instead of that?" And I think all that stuff can be- I think it's going to be an exciting area, uh, in the future.

**Claire Vo** [00:27:55] Okay, show me your last hobby.

**Alex Cornell** [00:27:59] Oh, yeah.

**Claire Vo** [00:27:59] artifact that you've made.

**Alex Cornell** [00:28:01] Yeah, well, I'll show you- uh, the one I wanted to show you was this one with a podcast attached

**Claire Vo** [00:28:05] Oh, yeah.

**Alex Cornell** [00:28:05] because I think this one's very fun. Um, so I had a blog 20 years ago, uh, which has, again, lost to time, and I had Marlo go and find it way back machine going to blogger

**Claire Vo** [00:28:17] Mhm.

**Alex Cornell** [00:28:17] because it moved between Tumblr, school- like, I moved it all around, you know, so it- it went back and found all the posts and then accumulated them into one PDF first, then this little thing that is basically just like, looks like a blog. But the way that I like to read it now, just again for memory, is via a podcast, which is sent to me every morning, and it is just basically a random reading. You can hear a little bit. Is it weird to anyone else that 90% of people wear the exact same color pants? Which is the kind of thing that a 20 years ago Alex used to wonder about, and it's, like, very, very funny because you're hearing yourself- kind of, but 20 years ago,

**Claire Vo** [00:29:00] Mhm.

**Alex Cornell** [00:29:00] you barely remember anything, you know?

**Claire Vo** [00:29:02] Yeah.

**Alex Cornell** [00:29:02] So, like, I- I- everything that this person is saying, I'm like, "Yeah, that is kinda weird," but it's like, "Of course I would think that 'cause it was me 20

**Claire Vo** [00:29:09] 'Cause

**Alex Cornell** [00:29:09] years ago,

**Claire Vo** [00:29:09] it was me.

**Alex Cornell** [00:29:10] you know? Yeah, yeah. But anyway, I think, like, that one- I love that one because, like a lot of these things, or there's a, I guess you could say it's sort of a theme here, which is like, I feel like I'm constantly taking these things that I had in my life, but like could, for whatever reason, like I do not look at them. I can't, like the, it's presented in such a way that it wasn't useful for me at the time or whatever, and Muse is able to take it and just like reform it into a way that's like really interesting and useful for me, whether it's interesting like this or useful like the golf stuff or, you know, I have the same thing for chess as well, which, um, will break down my recent games. And this- this one gets a little bit, like, uh, snarky, I guess you could say. I didn't tell it to do this, but it, like, kind of, like, will poke at me a little bit, uh, which is kind of fun, like, bishop B5 collapse, like, I don't know what this is, what's going on here, but anyway, so it's a fun, that that's a fun one because it's useful, but it's also kind of funny to have like this, I guess you could say like kind of snarky chess coach that's trying to help me get better, so.

**Claire Vo** [00:30:12] Well, and for folks that aren't watching, this is a dashboard that I think pulls in your chess.com data, right? And just renders it and gives you game by game breakdowns. I really like this.

**Alex Cornell** [00:30:25] Yeah, it's been useful because, and you know, the fun thing is you basically just define this in chat, you know? So when I originally asked for this, I said I have a chess account. I would love to see kind of a mixture of analysis, but also, like, trends over time, 'cause it's helpful for me to know, like, am I improving? It looks like right now I'm kind of, like, falling off a bit.

**Claire Vo** [00:30:42] Uh-huh.

**Alex Cornell** [00:30:43] Um, but then the main thing that I wanted to do in this case is give me a review of the most recent game so I can go

**Claire Vo** [00:30:48] Yeah.

**Alex Cornell** [00:30:49] through here and try to get a sense of, like, what did I do wrong? In this case, I just quit mid-game, so that's not gonna be that helpful, but, you know, when the daughter arrives home, you have to stop playing, so.

**Claire Vo** [00:30:58] That's exactly right. Okay, so we have seen Marlo do everything from revive old Instagram posts and blogs to give you a custom and kind of nostalgic shopping catalog to taking all- you seem like a data person, taking all your data you collect and, especially for some of your hobbies, and let you put it in a way that will allow you to achieve either short-term or long-term goals. And then we talked a lot about, you know what, why I think a lot of people are reacting so positively to Muse is because it's well designed, it's thoughtful, it shows you what you need, it's fast, and we all have these like little cutie pie, cutie pie avatars. Well, let's do very quick lightning round questions, and then I will get you back to all your important work. first question is just, I think designing these agent experiences and AI experiences are very new to a lot of designers and a lot of PMs.

[00:32:00] The surfaces are new, the underlying infrastructure and technology is new. What did you have to learn, and then what were you able to kind of like fall back on that has worked forever from a design perspective?

**Alex Cornell** [00:32:12] Oh, that's a great question. You know, I think one thing that I have found for myself and any designer kind of coming into this project or really just this space is really wrapping your head around what a non-deterministic system is and how, what that means for when you're designing a screen. And by that I mean, like, we're used to, and through for my whole career, you would come to a feature and you would be able to think about it and then design it and kind of know that, like, on any given customer screen, it's basically going to work like this and look like this because that is the way that this thing has been coded, and that is the only outcome that you will see, you know? And so then the bugs that you would see would be like, oh no, like this circle didn't appear where it's supposed to," and it'd be very, very scoped in terms of, like, what you had to think about. And, I mean, it sounds like kind of, uh, routine to us now to talk about this, but like you're saying, in terms of things I had to learn, it's hard to remember what it felt like even just a year ago, how different things were, you know?

[00:33:17] But when you first come into this space, I think really understanding that these systems usually do, like, kind of end up the way you think, but like my muse setup is completely different than yours, is completely different to somebody else's. They're so personal, and they can, like, do so many different things that you really kind of have to think more about the underlying foundation and the system, the architecture, the scaffolding that's in place, and less about like, well, what about this one little thing here? Is it going to be just so, you know, actually one of the things that's hardest for me sometimes is looking at those artifacts that we were looking at. Like, I kind of have to turn off my brain sometimes design-wise because I'm like, you know, it's like it's a different- you can, if you want, go and spend all the time in the world to like make it look exactly as you want, but I've come to kind of view it a little bit more freely, and it's kind of, I think, kind of liberating in some ways to feel like, you know, this is still just a very useful output for me, and maybe I will take the time to make the colors just so, but otherwise it's good and it's fine, you know?

[00:34:17] And then I think, like, that's- that's kind of a fun new world, and that took some getting used to, I would say. Um-

**Claire Vo** [00:34:22] That is a very- a very gentle approach to the spectrum of slop to high quality agent design stuff

**Alex Cornell** [00:34:31] Yeah,

**Claire Vo** [00:34:31] that we-

**Alex Cornell** [00:34:31] yeah.

**Claire Vo** [00:34:32] we get out of our agents.

**Alex Cornell** [00:34:33] Yeah,

**Claire Vo** [00:34:33] Okay,

**Alex Cornell** [00:34:33] yeah.

**Claire Vo** [00:34:33] speaking of- ...you didn't get the colors quite right, when your muse, when Marlo is being obstinate and not giving you what you want from a quality perspective, you know, just not listening, what is your prompting strategy? What do you do?

**Alex Cornell** [00:34:52] Yeah, well, not like a well-formed one in the sense that I didn't, I suppose, ever reason about it, but I am very polite, I think. I'm not, I'm not all caps. I'm not a multi-exclamation mark person, and I do find myself sometimes looking at what I wrote and be like, wow, that was a really nice way to express that frustration. And I think it's really interesting, and I feel this way when I'm doing any kind of coding thing as well, where things, can, will maybe take a really long time and then go sideways, and it is really frustrating. I have always been surprised with how, like, not consciously, but how I will just speak to it the way I would speak to, like, anybody else about it. Like, I don't ever really get mad to other people, so I don't really get mad to Marlo or Jollybutt or otherwise, you know? Yeah, so I don't know. I've- it's always how I've been. I have seen- I have some friends who show me sometimes, like, the traces when they have gotten really mad. The thinking trace will be- will be, like, kind of a reset, like, "Okay, Alex is frustrated, so I should really-" you know, so it does make me think sometimes I could probably be a little bit more forceful.

**Claire Vo** [00:36:01] More effective. Yeah, yeah,

**Alex Cornell** [00:36:02] Yeah.

**Claire Vo** [00:36:03] you know, I- I- I also try to generally be polite, with the exception of what feels like very expensive misaligned coding misadventures.

**Alex Cornell** [00:36:13] Right.

**Claire Vo** [00:36:14] That's the one that, like, really gets me.

**Alex Cornell** [00:36:16] Yeah, yeah.

**Claire Vo** [00:36:16] Um, and to be honest, every time I'm yelling, it is true to agents as it is in life. It's usually a me problem. Not a them problem. It's a me problem.

**Alex Cornell** [00:36:26] Yeah, but you're right though, like they go off on the misadventure. It's like that's- Yeah, it's not

**Claire Vo** [00:36:31] It's frustrating.

**Alex Cornell** [00:36:31] free.

**Claire Vo** [00:36:32] Well, Alex, this has been so fun. Thank you for being so generous with your time. Um, we love Muse. I'm excited to see more of it, um, as it evolves. Where can we find you? How can we be helpful, and how can we follow along?

**Alex Cornell** [00:36:45] The most helpful thing would be to download Muse, try it out, and you can let Muse know when something isn't going right or you want a feature. Those do come to us, so that's probably the most helpful thing. I think for me, like on the internet, Threads is probably the best place. I try to, I've been trying to do some posting about the behind the scenes and like kind of some decisions that we made, and I'll continue to do that. So that's probably what I would say. But yeah, trying the app out and letting us know what you think is the most useful thing, so.

**Claire Vo** [00:37:14] Amazing. Well, thank you for joining How I AI.

**Alex Cornell** [00:37:16] Yes, thanks for having me.

**Claire Vo** [00:37:19] Thanks so much for watching. If you enjoyed this show, please like and subscribe here on YouTube, or even better, leave us a comment with your thoughts. You can also find this podcast on Apple Podcasts, Spotify, or your favorite podcast app. Please consider leaving us a rating and review, which will help others find the show. You can see all our episodes and learn more about the show at howiaipod.com. See you next time.
