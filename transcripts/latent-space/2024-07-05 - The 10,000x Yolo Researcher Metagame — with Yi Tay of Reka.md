---
podcast: "latent-space"
podcast_title: "Latent Space"
title: "The 10,000x Yolo Researcher Metagame — with Yi Tay of Reka"
date: 2024-07-05
url: "https://www.latent.space/p/yitay"
guid: "substack:145606648"
host: "Swyx"
guests: ["AI Charlie", "Yi Tay"]
format: "interview"
level: 2
length: "01:44:39"
categories: ["infrastructure", "models", "open-weights", "work"]
featured: ["Google", "open-weight models"]
mentioned: ["Gemini", "distillation", "ChatGPT"]
transcript_source: "publisher"
---

# The 10,000x Yolo Researcher Metagame — with Yi Tay of Reka

**Swyx** [00:00:00] Thanks for watching. Bye bye.

**AI Charlie** [00:00:00] Welcome back, friends. It's only been a week since the World's Fair, and it was incredible gathering the community to see the latest and greatest in AI engineering. You can catch up now on the four live stream track days on the AI Engineer YouTube, and our team is busy editing the remaining workshops and five other tracks, including the surprisingly popular AI Leadership track.

[00:00:00] Thank you all for your support, and stay tuned for news about the next event. The 2025 AI Engineer Summit. Last week, we did a very special deep dive with Josh and John of InView and Databricks Mosaic on training LLMs and setting up massive GPU clusters. And today, we're pleased to follow that up with a very special conversation with Yi Tai, formerly tech lead of Palm 2 at Google Brain, and now chief scientist of Reka.

[00:00:28] ai. Raker's largest model, Raker Core, was at launch. The fifth best model in the world. And the only GPT 4 class model not trained by a big lab like OpenAI, Google, Anthropic or Meta. In fact, while Google Gemini has 950 co authors, Raker only has 20 employees. With up to five people actually working on pre training.

[00:00:56] Swyx was excited to return to Singapore to delve into Yi Reka and building a new AI model lab outside of Silicon Valley. Stay tuned to the very end for a special bonus clip from Yi's recent appearance at the Tekinesia meetup for his spiciest take on why senior management is overrated and why this is the time to build up senior 10, 000x individual contributors like himself.

[00:01:21] Watch out and take care.

**Swyx** [00:01:46] Welcome to lay space. This is a long time coming, but I'm so excited to have you here.

**Yi Tay** [00:01:46] Yeah, thanks for, thanks for inviting and excited to be here. chat about a lot of stuff.

## [00:01:57] Yi Tay Intro

**Swyx** [00:01:46] Yeah. So you are interesting to research and introduce. You are now chief scientist of Rega, which is a super interesting model lab, but before that you were at Google Brain, you were architecture co-lead on POM two, you were inventor of UL two.

[00:01:46] You're a core contributor on Flan, you're a member of the Bard core team, and you also did some work on generative retrieval. That's a very, very illustrious three year career at Google Brain.

**Yi Tay** [00:02:10] Yeah, thanks, thanks, thanks, yeah.

**Swyx** [00:02:10] And then since then, Reka, you joined in March 2023, announced a 58 million series in June 2023.

[00:02:10] I don't know if you know, the post money valuation, or the pre money valuation is public. So it's, crunch basis is, is, Oh, okay, okay. I

**Yi Tay** [00:02:26] did not know that yet. 50

**Swyx** [00:02:26] something million. So you don't even have to leak it. It's on the internet. Okay. Rekha's stated goals were to work on universal intelligence, including general purpose multimodal and multilingual agents, self improving AI, and model efficiency.

[00:02:26] In February You released Rekha Flash. In April, you released Rekha Core and Edge. And then, most recently, you released VibeEval. Is that a good summary of the last six years? No, it's not. Four years? Four years, yeah. Oh my god. We're talking about AI I was wondering, since when did I,

**Yi Tay** [00:02:45] like, step into a time machine or something?

## [00:03:02] Path into LLMs

**Swyx** [00:02:45] Yeah, okay, so can we just talk about your transition into, you know, you did your PhD, and we can talk about your PhD, transition into brain and research and all that. You know, I saw you do some work on recommender systems, I saw you do some work on quaternions. What the fuck was that?

**Yi Tay** [00:02:45] Okay, let, let, let's, let's forget about

**Swyx** [00:02:45] that.

[00:02:45] Just describe your path into modern L lms, right? Because you were, you were, you didn't start there.

**Yi Tay** [00:03:18] Yeah. Okay. Sure. Sure. I, I, I think the world also didn't start start there, right? I mean, I think in so I joined Google in 2019, end of 2019. And the world looked like really different at the time, right?

[00:03:18] I think that was around the time the first GBT was released by. GPT 1 or something was released by OpenAI. So, research, like ML research and NLP research looked very different at that time. So I was mostly, I identified as like a language researcher. I don't like to use the word NLP, Jason will kill me if I use the word NLP.

[00:03:34] But like, I was like, okay, a language researcher. I, , but I was more like an architecture kind of researcher. And when I joined Google, I was also I continued on this as a model architecture researcher. I worked a lot on efficient transformers. That was your first viral paper. Yeah, yeah, and like, you know, I worked in the long range arena.

[00:03:51] I spent quite a lot of time looking at what we could do without attention. Like, there was a synthesizer paper back in 2020. I think that was like my early days in Google. There wasn't like a At that point of time transformer research was mainly like WMT, like machine translation and like perplexity and stuff like that.

[00:04:09] It's not really about You know, there wasn't like, I think it was in field short, field short learning and field short in context learning came only about like, you know, when GPT 3 came out and beyond, right? And then, so I think that at that time, the meta, I would say, the meta looked very different. And at that time, a lot of the work was focused on Like fine tuning things like T5 or BERT or something like that, right?

[00:04:25] So I think a lot of the research, not only myself, but like around me or like even the broader community were working on those kind of things. And so I think that was, which I feel that in hindsight today is actually pretty useful to like kind of think about because a lot of people came into like, AI into right after ChatGPT came out, right, so they saw AI as kind of, I think there's a lot of benefits of you know, understanding how, you know, transformers and like, I've broken this thing apart so many times, trying to, it's like, these things actually, you know, help to improve intuition and it's not totally disconnect I think a lot of things are still relevant today and, and it's just the scale has gotten much larger and also the paradigms shift a little bit from Single task, fine tuning to like generally do everything kind of universal foundation models.

[00:04:45] Foundation models, right. I think it's just a slight change in paradigm, but fundamentally, I don't think like the underlying principles of research hasn't really changed that much except for like compute. Yeah. So basically algorithms

**Swyx** [00:05:29] stay put and then compute and data scale.

**Yi Tay** [00:05:29] So I have some thoughts about this.

[00:05:29] So I think back then a lot of the academic research, I think people have talked about this, like Sasha Rush has talked about this, or other people have talked about this, it's like, the conferences were always organized by like, Applications, right? They were always organized by like, Oh, like question answering.

[00:05:47] It was always by this, right? I think there was, there's like a bit of a transpose going on. Things become universal and then becoming like, okay, there's a data work stream, there's a model architecture work stream, and then people work on improving like a universal model and general purpose algorithms to improve this model rather than finding domain specific tricks.

[00:06:02] I think for, even in 2019, I think I've already been Like focusing on works that are like you know, you could improve on general architecture at that time. It was like, like maybe LSTMs in 2017 or something, and then you try on like 10 different tasks and the kind of thing, right? But like a lot of the research community have been focused more on like, how do I get that extra 2 percent on question answering or like, and then sentiment analysis.

[00:06:20] I think. There was this phrase of like, in 2017, 2018, where this style of work was still very fashionable in academia and conferences, right? And then, I think the big thing about the chat GPT moment of like, 2022, the thing that changed drastically is like, it completely like, it was like this sharp, Make all this work like kind of like

**Swyx** [00:06:44] obsolete.

[00:06:44] So November 2022, you're saying? Exactly, Charged GPT launch? Because I feel like if you're in the research community, this was coming.

**Yi Tay** [00:07:03] Yeah, yeah. That's what I'm saying. I'm saying that like the big labs and stuff, like people have already been moving towards general, like even T5 was already like general purpose.

[00:07:03] Yeah. And that's the thing, right? But like, there was, it's like, there's a bit of a time okay, like places like Google and Meta, OpenAI, we will be working on things like three years ahead of everybody else. And academia will be like, Still working on like this path specific things, Got it, got it. And then like, I think the faulty function was the, the ChatGPT moment actually really like, It was coming, it was coming, it was just like the final, the last straw, and then it's finally like, Yeah,

**Swyx** [00:07:15] now it's serious.

**Yi Tay** [00:07:15] Yeah, now it's really, the thing completely changed. I don't know how it turned from my, from my background to like, talking about the meta.

**Swyx** [00:07:15] I think that you navigate the meta very well, and part of my goal here is to also isolate how you think about the meta for other people to reflect on, because I think obviously you do it very well.

[00:07:15] Oh, thanks. I'm looking at your papers published somewhere around 2021. You had a hard cut to 22 Y two and Palm, and you did Y two Palm Emerge Abilities, DSI, REIT recitation, augmented Generation, all in the same year-ish. Mm-Hmm. So like there was, did you change teams? Did you, did you like have a research focus?

[00:07:57] Like when did you become,

**Yi Tay** [00:08:17] oh, you're still saying that like language research became the

**Swyx** [00:08:17] model guy.

**Yi Tay** [00:08:17] My research became emergent. It was like, it's very obvious. No, I don't think I'm like a person that like, I'm not like super, super great at like forcing a trend, like two years ahead. And then especially, especially like, Plan for that, right?

[00:08:17] Yeah. I think I smoothly and as like, kind of like as like I, I never actually really thought about this, this way. I just did like at every step, I just like optimized for like what I found to be most impactful and most promising. And then that gradually, and also it is, it is also a lot of influence by talking to people.

[00:08:34] Right? And then at the time I started working more with. I had some close collaborations with Jason and other people. I mean, Google is, you can work with anybody you want, basically. So you're kind of like, also like, partly it's like the environment shift. And I think the environment shifts like very quickly, but like, I was always like pulling for like the environment.

[00:08:52] I was not like, I think it's always good to like have an open mind and move along with the field rather than, okay, this is my research area. I'm going to get stuck in it two years. I think I just move along to find like things that interest me. And naturally I think like that turned out to be like, The things that were most impactful at that time.

[00:09:10] In retrospect, I kind of did well, but like, I never actually really saw it as intentional. Sure. I didn't do anything really intentional, except that's doing what I find interesting, actually.

**Swyx** [00:09:27] Cool. Well, we'll just talk about the main work at Google Brain, and then we'll move to Rekha.

## [00:09:41] Google Brain: PaLM, UL2, DSI, Emergent Abilities

**Swyx** [00:09:27] So out of UL2, Palm, Emergent Abilities, which of these came first?

**Yi Tay** [00:09:27] Yeah, I, wait, I did, I need, I can't really actually re remember. Okay. What will make you talk about year two then? Year two and DSI, the differential search index? I I was working on it like the December of 2021. So like at Google they were like projects that are like big efforts that are like a researcher will be like part of the effort and then this will be kind of top downish to some extent.

[00:09:27] Right. And then they are, they were also like. Bottom up research that one could do I can't speak for the Google now for sure, but like, at least at that time, right? So UL2 and DSI, Differentiable Search Index, were like, works that I kind of tinkered with in the December break where nobody was around.

[00:10:04] Palm also has this kind of differentiation because there's Palm 1 and there's Palm 2. Right. So Palm 2, I was actually like the co lead of one of the work streams, but like Palm 1, I was more of a contributor and Palm 2, I was like, so, so they were like, now I have to think back of like, okay, what's the timeline, which came first, right?

[00:10:19] In general, they were like three categories of works. One is like broader efforts that are efforts. And then there are some that like UL2 and DSI were like my own projects, like projects I use to compute that. That I had, and then I just played with it. You accidentally left the auto run in for a month.

[00:10:35] Yeah, yeah, yeah, that was in the paper. It was fun, I think. It was really fun. And then, there was also like a third category where those were like, the efforts that my good friends were driving and I contributed. So Flan was just one of them. I know like, maybe on, I would like to just maybe say this publicly, like a lot of people like, I talk a lot about Flan.

[00:10:50] You're Flan's show number one. But like, yeah, but like, the first author is actually Hsiung Wan, who is great, and then like, another guy, Le, I was her cook. core contributor but I mean just because I'm a little more visible so I kind of Accidentally took a little bit more credit for that, but I was a co contributor, but I was not like The lead authors are obvious.

[00:11:08] Yeah, so the third category was projects that my friends Emergence was also like Emergence Abilities No, actually, that paper was supposed to be only me and Jason on the paper. And I actually became friends with Jason From the paper and then that led to like this streak of like, I dunno, 10 papers or something together with Jason and now we are like super good friends, the Ultimate Romance.

[00:11:25] But that was like the immersion paper. But I, emergent paper was also like a belonged to be like a, a bottom up kind of like a thing. And fun times. Yeah, it was fun. ,

## [00:11:54] PaLM 2

**Swyx** [00:11:44] maybe I'll pick on Palm two. Because I feel like, I'll pick on Palm 2 and Emergence, because I really want to make sure I tell those stories.

[00:11:44] Those are important stories. Palm 2, I think it's a career story. It effectively became a co lead on the second version of a very high profile, company wide effort. How did that happen? I think people would like to know, to know how to, you know, what's like the sort of career strategy there.

**Yi Tay** [00:12:01] To be clear I was one of the co leads, but there were a lot of co leads, so, so I don't want to take too much credit for that.

[00:12:01] But my involvement with Palm 2 came from the after UL2 was working well, and then it was getting some visibility within Google. Was UL2 the largest model that Google had released

**Swyx** [00:12:21] at the time? Yeah, I think so. That was the largest. And you just, it was a personal project? It was a personal project.

[00:12:21] Yeah. Yeah. Isn't that unusual? How can it be like one person's decision to like suddenly release something that, you know, effectively changed the trajectory of, I think how, how, how, how people brain, how,

**Yi Tay** [00:12:37] how we work was that, I mean, 20 B is not that much larger, but from 11 B to 11 B T five, actually at that time there was starting BT five, right?

[00:12:37] So I think UL two is code decoder 20 B model. I think when we got it approved, it was like. It was released as like, kind of like, like the big brother of T5, you know? Kind of like, okay, we updated T5 with like a new objective and train this new model into DBM we want to, and it uses the same pre training data set and everything, right?

[00:12:55] So like from PRC4. Yeah, from, yeah, that was the easiest because there was precedence, right? It was like, okay.

**Swyx** [00:13:13] But yeah, there was some architecture, like the mixture of denoisers. Yeah,

**Yi Tay** [00:13:13] yeah, yeah. So, so back to Palm two, I think my involvement with Palm Two came from the work to, to, to, to add UL two, to Palm two.

[00:13:13] And then I, I, I mean, it was from the top down point of view. I, I mean, the leads were decided in a top down manner. It's not like, like there was not much like fighting or like, or any major things, right? It was like. It was a mixture of bottom up, top down ish, half half situation, and then from the top it was like, Okay, these are the people who are the most visible in contributing to this workstream, and then, okay, how about E and this other guy will be in charge of this modeling workstream, and something like that, right?

[00:13:28] So I think it just happened that way organically, and yeah, I think that was how I kind of was co leading the modeling workstream.

**Swyx** [00:13:58] I think in retrospect, you understand now that this is a very valuable experience. And I think now, today, it will be much more competitive to get the job that you got, whereas you didn't, you know, two years ago, you didn't have to try that hard to get it.

[00:13:58] Or like, you kind of lucked into it with you all too, and then like, it just compounded from that initial good decision.

**Yi Tay** [00:14:20] I think it's very hard to counterfactually analyze these type of things. I think it's definitely true that there are more people working on generative AI now, and, you know, if you are in a big company, it's way harder to navigate.

[00:14:20] Like these type of things, right? I wouldn't say that there were like nobody or so wanting to work on this at that time. In fact, there were actually But you were the obvious choice. There were less people. There were definitely less people, but I think I would say that maybe it's slightly harder now, but like, it's also not like it was easy at the time.

[00:14:35] Yeah.

**Swyx** [00:14:50] Yeah. I imagine it's sensitive. But also in my mind this is now the most And this is the most valuable on the job training in the world. And so people want to know how to get it. This is what I'm trying to figure out.

**Yi Tay** [00:14:50] Like, actually, individually we also cannot pick somebody else's experience and then try to replicate it on, because everybody's circumstances, their initialization point, their, That thing is kind of also like in different This is not only true for LLMs in general, right?

[00:14:50] Because a lot of times like, oh, okay, you did this in this position, and then because of this It's very hard to trace all this down to to find the causal path for this thing. So I think everything in life, there's some luck involved, I guess. Yeah,

**Swyx** [00:15:16] there is.

## [00:15:27] Emergent Abilities

**Swyx** [00:15:16] Emergent Abilities. Very influential paper.

[00:15:16] Subsequently contested by the Mirage paper. Oh, yeah, yeah. So before we get to the Mirage, was there a story behind Emergent Abilities? You know, I'm sure it's Jason's Thesis or like what? Just tell, just tell more about like the behind the scenes, like was was, was there a discussion that led to

**Yi Tay** [00:15:30] it that, you know, this one was like this, the idea, the inception of it was like mostly Jason.

[00:15:30] Okay. Right. I think I, I helped out to like. You know, shape up a little bit of the paper get some stakeholders involved and stuff. I was discussing quite a bit with Jason, but this, the idea itself was Jason itself. So, actually, when the Mirage thing and everything came out I didn't okay, I was just hot takes for the sake of hot takes.

[00:15:49] I didn't feel, I believe in emergence I have to just go on the record and just say I mean, I believe in emergence. And then I was not feeling very strongly because I think that, I can't speak for Jason, but I would just imagine that he would be Maybe personally offended because because I know Jason is a person that takes a lot of like feedback like very well He's a very like he's not offended by harsh feedback and he rebuts well like online as well, right?

[00:16:06] But like I would imagine he will be the one that is the most like affected by Criticisms of emergence. I was believing in it, but I have to say that the paper, I mean, that's why he's the first author and I'm second, but that was mostly Jason's thesis, and I have to really say that Jason has really good ideas, and I was more of a support role for that paper, yeah.

**Swyx** [00:16:29] Sure, yeah, you know, lots more to discuss there, but you believe in emergence, that's enough for me to work with.

**Yi Tay** [00:16:29] I also think that the, the, the Mirage paper is mostly like I don't know who, actually I don't even remember who wrote it. Ryland

**Swyx** [00:16:29] Schaefer. Yeah, I, I covered him on, on my NeurIPS podcast.

**Yi Tay** [00:16:29] Okay, okay.

**Swyx** [00:16:29] He's a very good speaker, and the paper was well done. It's just that people drew the wrong conclusions from the paper. Because they had a very good title. Do you believe in emergence?

**Yi Tay** [00:16:29] Of course. Okay, high five.

**Swyx** [00:16:29] I mean, how can you read any paper, read any, the progress of LLMs and not believe in emergence?

[00:16:29] It's so stupid. Like, just because you re parameterize some benchmarks in evals and, you know, make it linear, doesn't mean emergence is completely gone. And even in the Mirage paper, they acknowledged that there were some metrics that were true, genuine emergence, according to them. I think it was something like 25 ish percent in the ballpark.

[00:17:20] That's not the exact number, but it's in the ballpark. So I was like, okay, fine, like some benchmarks you disagree with, but on the whole, there is emergence, it's just, now we're just talking about the magnitude.

**Yi Tay** [00:17:38] Yeah, yeah, yeah, for sure, for sure. I don't think the authors of the paper had really very Like they, they didn't, I mean, nobody, we, we should just assume people don't have bad intentions.

[00:17:38] Right. But like, no, they, they definitely were just doing this. But like the, the, I think the Popul media, I was more like annoyed by the nearest best people. I mean, okay. Best people was, let's take the thing, take of a grain of salt, right? Yes. But like, there were people come to me like, oh, you should care about this because it's the nearest best disprove because it's the nearest best paper.

[00:17:55] I'm like, paper awards like mean anything. Actually, it doesn't mean anything. Right? Like. I think that was more of my where my angst was coming from. I don't, I don't think I really had, I don't even remember who were the authors of that paper, right?

**Swyx** [00:18:11] I'm sure they're doing well for themselves, and we don't have to dwell too much on that.

## [00:18:26] Quoc Le as manager

**Swyx** [00:18:11] Okay, so a couple more things from Google, and then we can go to Rekha. Kwok Le was your manager.

**Yi Tay** [00:18:11] Yeah, yeah. What is I had another manager called Don. Like, I had two managers during my time at Google.

**Swyx** [00:18:11] So I'm just basically going to ask for quick hits from what did you learn from Kwok? What did you learn from Jason?

[00:18:11] What did you learn from, you know, Juan? Who they are, who they represent to you,

**Yi Tay** [00:18:38] like, how they advise you and all that. So Kwok as a manager, he was more like a friend, and we would like talk a lot about, I think Kwok is a very researchy person, he has a lot of like, he's more of like an intuition, I learned a lot about like from him about like, there was no like concrete, like it was more like over time, and it was very implicit, soft kind of feeling, but I think like a lot of research science, we were like brainstorming a lot about like, , I quite like that, you know, when we were But there was this U palm paper that, that didn't like get much, like as much attention that I feel it deserves, but like, I think that was one of the works that I, I kind of like discussed with court quite a bit and like and that time you're releasing the fund two stuff and everything.

[00:18:38] And then like, I think court has a lot of good sense about like what makes a work a good hit and like you know, publicly a good hit. And like a lot of research sense about like what what makes like. like research cool, you know, so I think he has good like intuition as a researcher and I learned quite a little bit about and I also I was going to say that I think Jason also probably learned like quite a bit from Quark and and this also influences like more of like it was not only just like me getting influenced but that there was like Jason getting influenced and then Jason influenced me so I think overall what I learned from Quark's like intuition, research taste, people like chat about AGI sometimes, singularity and stuff like this it was Like, he's nice to talk to as a friend, manager, kind of, he's like kind of a friend figure to me.

[00:19:16] He's very much a researcher more than like a corporate, you know, manager kind of thing.

**Swyx** [00:20:01] I totally expect that. It

**Yi Tay** [00:20:01] was fun, it was fun.

## [00:20:08] Jason Wei

**Swyx** [00:20:01] Jason Wei, what did you learn from him? What is your distillation?

**Yi Tay** [00:20:01] Okay, Jason is very interesting. So, I learned in my career, I learned two or three things, major things from Jason, right?

[00:20:01] So, I think the first thing I learned from him is that so Jason was actually, okay, I'm going to talk about the more casual, more fun stuff first. Jason was the most spicy on Twitter first before me. There was an era where I was a goody two shoes, I only had my main account, I only tweet my only tweets Newspaper alert, you know?

[00:20:18] Right. And then Jason was starting to post like, like hot takes, right? Yeah. And I just thought to myself, oh damn. Like, you know, and there were, there were types that I was like, Jason, you should not post this. You're gonna get cancer. Right. And he, he, he was fine. He, he always break through the storm and everything until I, I looked at him and I'm like, maybe it's not that bad after all.

[00:20:34] Just be, be, I love it. Right. So there was like kind of like, which is very interesting 'cause Jason is much younger than me and I. And the other thing also, our accounts, right, we created them around the same time, right? And the interesting story behind it was that Jason's account and my account has our own, our original it was not like an anime character that nobody know who is it.

[00:20:50] We have our identity. It's pseudonymous. It's pseudonymous, right? And then I asked Jason why do you want to have a So like, why don't you just make like, and he told me this thing which was quite true was that like, Okay, you can post a thing that is spicy and it's hot, but if you cannot stand by the opinion, then you should not have the opinion in the first place, right?

[00:21:09] Wow. Right, so there was something that, oh, okay, I thought that was profound because so far this, I mean, there are times where, okay, I post something and it's spicy and then, okay, it gets a little bit bad, and then I, okay, I kind of agree that, okay, this is bad, then I will retract it. But if I could stand by the opinion, then I would just stand by it because that's the point of making it It should be said.

[00:21:25] Right, it should be said because. I can put my name behind it, right? So that was This is part of the first bucket about how it kind of influenced my online persona like, a little bit, and then, I mean, and then it turns out that now AGI Hippo is so much more spicy than the cola The cola is just hibernating somewhere, it's not even around, right?

[00:21:42] So, I mean, Jason is also more constrained because he works for he has Like an actual employer, right? And he has to be a little bit

**Swyx** [00:22:00] more The worst thing about Twitter is that, you know, anytime anyone from OpenAI tweets anything, they're like Did you see this researcher from OpenAI said something?

[00:22:00] And they read tea leaves that are not there, and it makes you very cautious to tweet anything. And so it kills the golden goose, is what I say.

**Yi Tay** [00:22:15] There was one tweet, I mean, at the time when somebody was, people were speculating the GPT 2 chatbots, right? And then Jason just posted something on his main account something excited about new experiments being run just a random just, and then people screenshot that, and post like, Yeah, I hate that.

[00:22:15] So I think, I, now I think for, All the count is mostly like personal, like personal stuff , very personal I think he would stay away from non work things non work things.

**Swyx** [00:22:35] The golden goose has been killed because people on Twitter cannot control themselves from drawing random conclusions from, you know, all these hints and all that Yeah, yeah, yeah, yeah,

**Yi Tay** [00:22:35] but Going to like the actual, this is like filler, filler, this is not canon, it's filler.

[00:22:35] I think the second thing I learned from Jason is more about like, from my you know, kind of like, from my own career, it's like, the importance of like marketing and PR. So Jason is actually like, I mean, I was just like, he was actually like really, you know, the emergence, like how many blog posts you wrote about the emergent abilities and how many talks he's given about, about emergent, like a lot, probably like the other day I was just at this webcom keynote and he was giving a keynote again about emergent abilities and it's been two years, right?

[00:22:57] So I, I think one big success of him is that like he, he does the work. Okay. Thanks a lot about like marketing the work itself. I did not like in my early parts of my career, early parts in Google, right? I was putting out a lot of work, but I didn't put in a lot of like effort in like thinking about the, like how the work is going to be received.

[00:23:25] I'll just be like, here's a paper, here's a paper, here's a paper, right? But Jason will be like, I'm going to write this paper and I'm going to like market the shit out of it. So I, I, I think I learned a lot about like, so every single first author paper that Jason writes in the last, he has like 1000 citations in one year.

[00:23:42] Oh my god. Like no, I mean, not every, but like most of it that he leads. So his hit rate is very high. His hit rate, like impact density, like it's very high, right? So, It's pretty interesting but I kind of see him as like a peer and I learn a lot from his basically some, some people are just like talented in, in different ways.

[00:23:56] And, and I think that like, I, I looked at how he markets his own work and markets himself actually, right?

## [00:24:16] Marketing Research: How to Start from Zero with No Reach

**Yi Tay** [00:24:11] If someone is starting from zero,

**Swyx** [00:24:11] like no Twitter presence, what is the second best thing to do? You mean as a researcher? For marketing, yeah.

**Yi Tay** [00:24:11] I, I think you would like the, the, the most obvious. If you're like a re like say hypothetically, you're like a researcher in like a place without visibility or without an end.

[00:24:11] You have no personal visibility. The first goal is always to try to find a mentor or coworker that is like within this circle, and then you start from there, right. Because, and then you get, you get, you know. people from like, who has a visibility and following to retweet. So you will like, work with them the big goal is not about like, I learned this, I mean, this is like, probably a career mistake in my early days, was that you know, instead of like, focusing on like, so called people okay, if you do good work, it's more of like, okay, how am I going to I see this visible researcher from DeepMind, right, or how can I collaborate with this person, and then kind of do something that feels cool, and like, I can win their respect, and that they would like.

[00:24:32] You know, they will be willing to co author for me because the exercise itself was so about how to, you're not trying to please reviewers or anything, you're just, if you can find one semi visible, you don't even have to be like a famous person, that's like a semi few thousands of followers, has a good reputation of research, and then you collaborate with this person, and then when you post the work, you are co authored with this person, and then you get the person to vouch for you, or just, over time, this would It could be from internships, it could be from, you know, just DMs.

[00:25:09] I think, you know, people are nicer than some people, they seem scary, but if you DM them, they're actually willing to collaborate, actually.

**Swyx** [00:25:38] I was scared of you, actually. And when I DMed you, you turned out a lot nicer than I feared. So thank you for being nice. That's really great advice for people.

[00:25:38] I just want to leave that out there for people. For others who follow, you know the work that the career advice that I give, the title topic of this is pick up what others put down and specifically pick up what your mentors put down. Like, mentors always have more work to do than they have personally time for.

[00:25:55] The high visibility mentors, and if you can show that you're a good collaborator with them, they will lift you up. Accordingly, that's a pretty good formula for career growth. Should I ask about Hyungwon? Or I don't know how close you are. Oh, we're

**Yi Tay** [00:26:09] still good friends. Hyungwon is a great engineer and he's very systematic in the way he thinks.

[00:26:09] I think Hyungwon is without going into detail, I still spend a lot of time talking to Hyungwon, even like in the, even after we both are different places, about like very interesting algorithm, arithmetic ways to think about life. Very interesting like, perspectives on life rather than research.

[00:26:26] But Hyungwon is a great engineer. And the one thing that scares me about Hyungwon is he doesn't have multiple monitors. He just codes with one small screen. And he does everything with very hyper optimized. And then I

**Swyx** [00:26:43] want those U curve where one screen, one screen, and then many screens.

[00:26:43] Yeah, yeah, yeah.

**Yi Tay** [00:26:57] So I think Hyungwon scares me because it's like, I think that was at NeurIPS 2022. Like, we were doing some work at the New Orleans. And then He'll be coding perfectly fine with this 13 inch MacBook with one terminal, and then he'll be like, he keeps telling us okay, it's more optimal to using keyboard is more optimal than moving your head, because if you can switch your screen fast enough, it's faster than your head, like moving to different screens and stuff.

[00:26:57] I did not actually distill that, because it's too painful to do that, but it's very interesting in a way that I'm he belongs to one of those hardcore people with one monitor and

## [00:27:34] What's needed to be a successful AI Researcher?

**Swyx** [00:27:24] Maybe this is a relevant question to just close out the Google site. What do you think is a good programmer for AI research?

**Yi Tay** [00:27:24] You mean set up or eating? No, no, not set up.

**Swyx** [00:27:24] Not even lifestyle. It's more about skills. Like what should people have? What do you interview for, maybe? What do you see that the high performers do differently than less high performers?

**Yi Tay** [00:27:24] I mean, okay, like generally, there's like, I think like for AI researchers, like being a strong IC is like probably like the thing that I feel like is like important for AI researchers.

[00:27:24] Like not, not I think There's a certain level of sacrifice to be an AI engineer, AI researcher, especially if you're training at LNs, because you cannot really be detached from your jobs could die on a Saturday at 4am, right, and then there are people who will just leave it dead until Monday morning, and then, or but there will be people who will crawl out of bed at 4am to restart the job, or to Check the, you know, TensorBoard or something like that, right?

[00:28:03] I think a lot of being a successful AI researcher, I don't want to say passion is also the entire thing, but it's more of just the a kind of personality that, if something, there's a bug at 3am on Saturday night or something, right? And then you would like, be like, you couldn't go back to sleep unless you, you, I'm not, this is very unhealthy by the way.

[00:28:31] People should not do this for a long time. You know, I think this kind of things actually like, allows people to make progress faster. But it's unhealthy, so I'm also not even sure like, what's like the, checking out on like, Friday, Saturday, Sunday, and like, 9 to 5 if you want to like, make progress, or like, some people are just so good at detaching like, okay like 8pm, I'm not going to My job can die and then the chips can stay idle for like the whole night, but I want to watch Netflix, right?

[00:28:50] You cannot, I think there's a level, it's like a sport you cannot win an Olympic gold if you want to have super, ultra good work life balance, right?

**Swyx** [00:29:15] Yeah, passion, intensity, dedication. Yeah, intensity, right? So those are really good personal qualities. Just technical qualities wise, how much of the stack should people know?

[00:29:15] You know, if I Okay, so

**Yi Tay** [00:29:32] that was the question.

**Swyx** [00:29:32] No, no, no, but that was important as well. Okay. It's just harder to interview for because you really just see it on the job.

**Yi Tay** [00:29:32] I think stack is not not, not, stack is not that, like Like, should I know CUDA kernels? I don't know CUDA kernels.

**Swyx** [00:29:32] Exactly, right? Okay, good.

[00:29:32] So for all you listening out there, you don't have to feel like an imposter. No, but, but you need to be willing to learn if you have to, I think. Well, you haven't had to so far. Yeah, I haven't had to so far, right. So if I sling pie torch, okay, great. You know, what kind of do, do I do I know like distributed systems, like do I know, like what, what is the, what is the stack that you recommend for people that get, gets you like a well-rounded end-to-end researcher.

**Yi Tay** [00:29:47] I don't, I, I don't think there's any specific thing. In fact, I will try to be as I don't really say like, okay, you need to learn Jax, you need to learn this. By the time you think there's a new frame out anyway, so, so it's more of like. Staying like constantly, like trying to, being able to continuously learn and update.

[00:29:47] I, I don't think that's a single, single stack or like a single single like workflow or I don't think that's a single one. Yeah.

## [00:30:31] Reka Origin

**Yi Tay** [00:30:24] Well, that, that leads us to Rebecca. Yeah. What's the founding story? So, I, I met some of my other co-founders while we were collaborating at that did my end. I was at, at brand and they were like a DeepMind.

[00:30:24] I'm not like a, a, a startup person. I, I I, I identify even today. As a scientist and a researcher more than like a startup person, right? My co founder, Danny, started this story. Right. And then this, this record was like, in the works from like, late 2022. I, I finally left in 2023. Then he kept asking me, he wants to do something.

[00:30:41] Do I want to go with him and do it? And, and it took, took a while for for me. Also, I was like, kind of the last co founder to kind of form the Was

**Swyx** [00:31:01] the plan always for you to leave at some point and join him? No, no. He was convincing you to do it. It was

**Yi Tay** [00:31:01] like, it was like a six months, more or less, in fact I think more than six months period of like, I always had this at the back of my mind for since like, what, August actually, I didn't want to do it in the first place.

[00:31:01] But I think eventually in March, I felt that okay, it's time for me to experience something new. Like, my leap of faith was more of like, I want to experience something new. I've, okay, I've like, Wrapped up this palm to work at Google and then like more of like, okay, let me experience this new life and see Where we can go with this and I also I mean, we don't have a lot of like, okay The funny thing was that like many many years ago before I PhD I wanted to do a startup actually at that point and then over time I realized that like I was better off as a researcher And I just forgot about the startup thing and it's quite funny that today I end up doing a bigger startup, right?

[00:31:25] but even until now I I actually I did identify more as like a researcher and scientist. Well, I mean, it's not, when you

**Swyx** [00:31:58] left you already had a high profile coming out of Brain. You could have gone to any startup out there. They all had wanted you. Yeah, okay, okay, yeah. So why did you choose this one, basically?

[00:31:58] Like, is it just because of pre existing relationships? Because, you know, It wasn't obvious to me. A lot of it, the other coworkers went to OpenAI, others went to, the, if you're, if you're fair, you went to Misra, you know, that kind of stuff. Right? Like Rico, Rico was like not on the, on

**Yi Tay** [00:32:13] the map.

[00:32:13] Yeah. I, I, I think it was, for me, it was the ion between staying at, at, at Google and like co-founding something. I, I, I didn't want to like, like it was more of the experience of like being a co-founder. And this is like what attracted me, right, and wanted to experience that. I wouldn't have left for Inflection, or something like that.

[00:32:26] Like, I mean, Inflation is gone, but

**Swyx** [00:32:42] like RAP? They're still alive. They're selling themselves as a model foundry or something. I don't know, there's a services company now.

**Yi Tay** [00:32:42] Yeah, I know, but I also think that like Like, for example if you were to join another, it would be like a very big tech experience again, right?

[00:32:42] I don't know, I felt like, the experience I get is very complementary to what I have that's the experience I had at Google, right? But if I were to join something else, right, then I wouldn't have, I would have just stayed at Google, to be honest. Because to me, it was very clear just two decisions that, that I didn't really I was talking to a bunch of other startups, but I didn't really actually had the intention to I was happy at Google, actually, to be honest.

[00:32:58] I'm sure,

**Swyx** [00:33:19] I'm sure they have a lot of things to keep you happy. I was happy at Google, yeah, actually.

## [00:33:24] Starting Reka Infra

**Swyx** [00:33:19] So, you describe yourself as GPU poor, but also you had 60 million dollars to play with. You got a whole bunch of GPUs. I think you disclosed somewhere, but I don't remember the exact number. And you had a good training run for Flash and Core and Edge.

[00:33:19] How would you tell that sort of story? Like, people can read the technical report. But also you know, what was that overall experience like? And you should also point

**Yi Tay** [00:33:39] people to the blog post that you wrote. There were a lot of interesting things that happened along the way that So I think I left around like early April, the end of March, April and everything, right?

[00:33:39] But most of our compute actually came in December, actually. And there were delays. So H100, there were major delays, right? So we were sitting around, right? And to be clear,

**Swyx** [00:33:58] you don't own the compute, you are renting.

**Yi Tay** [00:33:58] Yeah, yeah, yeah. So we were sitting around. Like, we've, you know, for a long period of time, we had 500 A100s, because we made a commitment and they were constantly being delayed, I think because of H100 supply, demand, whatever reasons.

[00:33:58] And it was also very hard to get a lot of compute in one place, right? And then we were locked in, and we had to wait for the compute to come, right? So, I think, It was very painful because even when the compute came, it was mostly broken most of the time. And it was broken to a very bad extent that, you know, before I left Google I was like, even in the early stage I was very optimistic about You Okay, this compute translates to this amount of flops, this is the model, right?

[00:34:23] But I never expected the reliability to be so poor that it just threw off all the calculations and then we had to, work ten times harder just to make the thing go smoothly. So, it was a bearable pain. I think the pain was bearable, but it was just way, way more than expected.

## [00:35:04] Why not to use TPUs outside Google

**Swyx** [00:34:48] I think you addressed this in your post, but the temptation would have been just to run everything on TPUs. Which is the stack that you already know very well. That that works very

**Yi Tay** [00:34:48] well. Oh, no, no. So, so, so TPUs outside Google and t inside Google are probably very different things, I think. Oh, how come?

[00:34:48] Okay. First thing is like infrastructure. Like, there was, there wasn't like a lot of good code bases like outside Google that was like still, right. And, and the code base that I was most familiar with was like T five X. It was a jack space. It would have been like, by, by the time we wanted to consider it, it was really like.

[00:35:16] Debrigaded for nine months, right? And then, TPUs I mean, we weren't sure about I mean, the availability of TPUs was not great, great.

**Swyx** [00:35:31] Oh, my perception is that it was a lot better. People have the learning curve.

**Yi Tay** [00:35:31] Yeah, but at the point of time, we had our infra set up, we were training already, training models, and it would be so much cost to, TPUs.

[00:35:31] So I think TPUs, the experience of TPUs inside and outside Google, I have not actually run a single TPU job outside Google, by the way, but just looking through documentation from what I see outside, it's great. And from like, how much I think that people inside Google don't care about what people think outside Google, I kind of feel like, okay, we were a bit like, I don't think we considered, I mean, not like forever not considering this, but like, just like, At that point of time, it was like, The obvious choice is to stick to PyTorch.

[00:35:50] Just stick to GPUs and PyTorch and make like, I mean, it's not as if the chips we ordered were not there, they were there, they're just not. In the best shape. Reliable. Right? Yeah. So I think it was too much work to, to kind of migrate suddenly to TPUs. Yeah.

## [00:36:29] Chaotic vs Stable Infra

**Swyx** [00:36:15] For those who haven't read the report, you had a very traumatic description about the chaotic and stable phases of various compute providers, and I was just wincing when I was reading all those things.

**Yi Tay** [00:36:15] Yeah, no, that was like a 3 body problem reference, the chaotic and stable phases. I mean, I was watching 3 body problems at the time, and I thought it was fun to, there was a lot of like, I think we had a lot of fun adding a lot of references and memes into the tech report. I think like, you know, it goes to show like how fun the environment is within, within record, right.

[00:36:15] We had a lot of fun with this, but so I think chaotic and stable face mostly. It's like we, we actually found that, like usually when like provider provisions, new nodes or they would like Yeah. You don't wanna be the first to use it. Yeah. It is usually like, like bad like dog shit. Like at the, like at the start.

[00:36:57] Right. And then. It gets better as you go through the process of returning nodes and, and, , draining them, giving it back to them, they will send it back for repairs, and everything and then over time, because it's more of it's more of a numbers game, right? If there's one bad node, It kills the entire job, right?

[00:37:13] So like, the fact of, the game became like, just eliminating bad nodes from the thing, right? And then, you know, I mean, just because of, maybe because of the supply issue or something, when the deadline comes to ship this, for example I just give rough numbers, let's say you order 1, 000 H100s, right? They will not be able to, usually they don't meet the demand of like 1, 000 H100s at the date.

[00:37:30] They will give you like 500 first, just not to piss you off, and then they'll give you like another 100, like every over 3 weeks, they were just like, okay I added like 4 nodes, added like 8 nodes, that kind of thing. And then over time, you reach like the capacity that you, or maybe you never actually reached the capacity that you ordered for.

## [00:38:04] Risk Sharing of Bad Nodes

**Yi Tay** [00:37:49] And then as they add these nodes, right, sometimes these nodes are bad. And then they just kill entire training runs. And the thing, Which I feel that, I mean for all those people trying to sell GPUs, people trying to sell GPUs now resell, sell, package, whatever, GPUs, right? And I think the most important thing that, that they are obviously they are SLAs, all this, in the contract and everything, and obviously, you know, you might be entitled to something, something, if something goes wrong, right?

[00:37:49] The thing that, for, Large model training runs, is that like one bad note kills the entire job? Right? So should the compute provider be liable to pay for all the note waste stage that No. No. It, it's because it's unlikely because otherwise it's unrealistic. Yeah. No one will take that on. No, no, no one take that on.

[00:38:26] Right. So I think that's also like a, a tricky thing. Who, who is taking the risk? It's the, the LM startup taking the risk. Or is the compute provider taking the risk? I think that, I mean, this is my sense, I'm not 100 percent sure, but I think like as there are more providers trying to sell GPUs inbounds so much about people trying to sell us GPUs.

[00:38:42] Right? The key differentiator is actually to find a way to To balance the risk of node failure with as long as the provider, I'm not going to say 100%, but if somebody can come and tell me that my nodes are so stable that I can share some cost with you if your job dies, this is green flag, green flag, right?

[00:38:59] The moment they start to I cannot Do any of the big clouds do that? As far as I know, no. They have the, you know, the size to guarantee that. But I think, Like for anybody who is watching or if you do like a compute startup or anything, the biggest green flag would be to share the cost of node failures with your customers, right?

[00:39:16] You mean the whole run? No, no, like if the node, it's very hard to go, because you need software to like, you need software to, so let's say you run it for 12 hours, right? And it dies after 12 hours, right? You get 12 hours of throughput, right? But then you get like some wastage because of like the, the you know, the downtime and everything, right?

[00:39:35] You know, I, I think it would be fair to find some middle ground to kind of split the cost of the failures, right? And this brings back to my point about like, work life balance. Because if the nodes fail, fail so badly, right? Like, it, it actually, basically, right, your engineers cannot sleep at all.

[00:39:52] You have babies sitting in rosters and everything, but you are living life with like constant anxiety, because even in the case, right, where the node failures are refunded, right, you still lose time. You lose three hours. You lose everything, right? So I don't know how to go around this, but I think if there are a lot of compute providers like fighting over I think a good A good thing to do is to figure out this pain point, otherwise, or at least, , figure out some hot swapping, but so far, most of the providers that we tried don't have this.

[00:40:06] They will also get confused when you try to ask them so my job is dead can you pay for the food can you refund for, or at least, they will get confused because this is a LLM specific thing that the large nodes, They don't care about, yeah. Yeah, they get confused about this, right.

[00:40:34] So,

**Swyx** [00:40:48] current status quo is the LLM started to pay for everything. Thank you. Maybe you could negotiate some,

**Yi Tay** [00:40:48] like, refunds, but usually they will not be so generous to pay for say you run 500 you break for 4 hours, they, in their mind, they will be thinking, I should refund you for one node, but in your mind, you just think that they should refund you for the full job, right?

## [00:41:05] Checkpointing and Orchestration

**Swyx** [00:40:48] Everyone who is from my background is going to be asking this. How is it so fragile? Like, how is it so brittle? Like, what's your frequency of checkpointing?

**Yi Tay** [00:40:48] Our checkpointing is kind of like we, we see how stable the job is and then we decide, because checkpoint, it takes a we without a good file system checkpoint, it takes actually quite long.

[00:40:48] So it could be, it's like a few

**Swyx** [00:41:21] hundred gigs, right?

**Yi Tay** [00:41:21] Yeah. I, I, I think so. I think so. I, I, I, I, I don't remember offhand, but , that doesn't take that long, but No, no. But sometimes if your, if your file system is slow, right? Your file IO is slow, your checkpoint thing could, for 20 B model could be like, what?

[00:41:21] 30 minutes or something like that. Okay. I don't know this by heart, by heart, by heart. Sure, sure, sure, but it's not hours. If you go larger, what if it's like a 200 bit

**Swyx** [00:41:35] model, right? Okay, so you should have some kind of ideal checkpointing to run ratio that is not catastrophic if you run into a node failure.

**Yi Tay** [00:41:35] Yeah, no, so we see of it as like, like a MFU, like, because you can average out your your flop utilization, and then you can see how many percent hit, like, how much slowdown, right? So you probably go for something like, if it's like, you're taking off 1 percent of your speed, 2 percent of your speed, so basically, it's actually fine to just checkpoint more regularly, right?

[00:41:35] So I think checkpointing, like, you also never fully, you can get, like, from the clean slate, like, nothing, right? If, as you optimize, like, engineer, like, the system to automatically restart everything, you get some of the time back, but you'll never be, like, Like, perfect, perfect. Like, so you still lose, lose stuff like that.

[00:42:09] If you checkpoint too often, like, what, every 30 minutes, then your file system is going to blow up, right? If you're going to checkpoint every, like, like so, like, for us, we just see it as, like, how much Storage is cheap compared to compute. No, when your model is, like, very, very large, your storage can, can, can easily blow up.

[00:42:25] Going on to the models, I feel like

**Swyx** [00:42:40] I digress so much about all these fun side things. You like compute, right? You like, you like hardware and compute, right? I love hardware and compute. Oh, and also, I'm an orchestration guy. Yeah. So, one part of the question, one of the questions I'm skipping right now is, you know, there's, I came from Temporal, I'm familiar with Kubernetes, I've used Airflow, These are all the data eng, cloud, or cloud engineer type tools.

[00:42:40] It's surprising to me that you guys don't have your set of orchestration tools that you, that is solved, right? You wrote in your blog post you had like, the pain of multi cluster setups, and like, to this, to the rest of us, this is completely solved.

**Yi Tay** [00:43:02] Okay. . I don't know if you know that. We use Kubernetes for, for a bunch of stuff, but like, I think like for experimentation and like stuff like this, it's still not fully, like we, we, we didn't have like the time to actually like, like, like build something that is, it should exist in open source.

[00:43:02] Someone should have done this.

**Swyx** [00:43:29] Okay. Okay. I'm not, it is what it is, but I'm surprised that's all. Okay. Say it seems like a valuable problem and someone much should do it. .

**Yi Tay** [00:43:29] Okay. Okay. Okay. Yeah, yeah, yeah, yeah. Good

**Swyx** [00:43:29] to know. Good to know.

## [00:43:39] Reka Flash/Core/Edge

**Swyx** [00:43:29] Okay, so Rico Flash Core Edge. You know, congrats on beating a whole bunch of state of the art models.

[00:43:29] Especially much bigger than, than, than each. People can see the papers for all the other stuff. Was this your expectation from the start that you would basically definitely be frontier? Like how do you, like, from the start of like, you haven't trained anything yet and you're about to kick off the run, like, are you able to like call your shots and say, we will beat GP 3.5?

**Yi Tay** [00:43:44] Nobody can predict the future.

**Swyx** [00:43:44] generally?

**Yi Tay** [00:43:44] No. How much confidence? Okay. We were confident. Like, we were confident. How? Why? Right. It's a good question. 'cause it'll be, it'd be

**Swyx** [00:43:44] a shame to do a whole bunch of work and then end up this in the middle of the pack, which a lot of people end up.

**Yi Tay** [00:43:44] We were confident. I think that a, a lot of it was like Yolo. I mean, I'm, I'm, I'm mentioned in, in, in, in the thing. I think we would. Like, require a lot less iteration than this because of our prior experience in like training these models. Like, so I was confident in myself about like our models will turn out to be, to be, to be, to be good.

[00:43:44] And I, about exactly how, I actually don't really know. Like, pinpoint to a particular reason of like, I mean, we de risk stuff, so a lot of part of it is like de risking and like, okay, you run like 4B applications and you can see, okay, this is like my spice, if you run 4B and your loss is like going crazy, you know that this is going to be a shit model, right?

[00:44:32] But I think it's like, we trained enough, like, okay, we don't have a lot of compute to do a lot of applications, but we did enough experiments to know that, ah, okay, our infrastructure and our, like, everything is set up to be good, right? Obviously, You know, the field moves, right? I won't say that everything was like, smooth, like the first time around, it's like smooth and everything, but I think we were confident in our ability to like, make the list, like we're not, like, really, we're more confident about, like, the ability to like, Move with as little steps as possible to the goal, more so than, like, my model is going to be this, like, level at this time, you know what I mean?

[00:44:52] It's more of like, , for example, let's say we run the first round of human evaluations, right? And then we see our number is this, right? And then we are confident that in five more tries, we will get to this. Kind of like get, get to like, like, like, like this. It's more of that kind of confidence rather than actually like, you know, it's also a little bit of like, you know, you see a new leaderboard hypothetically, like in academic.

[00:45:30] Like if as a researcher you see a release, a, a new leaderboard, right? You, you approach it like a puzzle. You don't know like. Whether you at the start of it, you might not have the answer to the puzzle, but if you're good at solving puzzles, like generally, right, you know that with one hour, I'll be able to solve it.

[00:45:51] You know, that kind of confidence, like, it's like, you know, it's the ability to, to hill climb or the ability to, to improve over arbitrary things, right? Rather than, I think we were confident more about that rather than like, Like, everything is different, right? The stack is different, the infrastructure is different, the data is also different from what, I mean, we have a lot of, which you

**Swyx** [00:46:07] haven't talked about, right?

[00:46:07] It's just, we have a lot of,

**Yi Tay** [00:46:25] yeah, we have a lot of experience from prior, like, our jobs, but, like, it is not going to be that, like, we don't have actually, like, exactly the same thing because, , different companies have different stacks, different everything, right? So it's more about de risking, being confident in, like, solving the general problem of, like, improving over things which is why also I think that the team is valuable in the sense that we are not, like, valued by our model itself, but we are just valued by how we can see one problem and we can just solve it super quickly.

[00:46:25] And that's what we are confident about, actually, like the artifact itself.

## [00:46:59] Recruiting the team

**Swyx** [00:46:55] Mentioning your team, you said at the largest your team was 3 5 people on the pre training side. Was that the team that you recruited? Was it all your ex colleagues? How do you find people that, you know, would have this kind of solid intuition?

**Yi Tay** [00:46:55] So I think that some of the people in our team were like, I worked with them at Google, at ex colleagues and stuff, and some of them were like fresh hires, like they were like fresh PhDs or like and everything.

## [00:47:22] Noam Architecture - Swiglu, GQA, RMSnorm, ROPE

**Yi Tay** [00:46:55] Okay, so,

**Swyx** [00:46:55] I do want to comment on Noam (Shazeer) architecture. So if you want to, people have variants of all these.

[00:46:55] swigloo, gqa, rope, rmsnorm, and then obviously the big one is encoder, decoder versus decoder. Could you comment on each of those, like, were you just like, we're confident that no one got it right? Or did you actually do an evaluation of each of your architecture choices?

**Yi Tay** [00:47:27] Oh, I mean like, okay, architecture wise is something that I feel like I'm easily able to, like, I've run so many architecture experiments that, like, I look at architecture and I'm like, okay, I don't want to be, like, overly, like, I think it's very hard to outperform the old genome.

[00:47:27] Why? It can't, I mean, on the surface of it,

**Swyx** [00:47:57] like, we have to have learned something in the last, like, No,

**Yi Tay** [00:47:57] all the changes, all the changes that, like, Swiglu was this, like, okay, Swiglu is probably one of my favorite papers of all time, just because of the divine benevolence, like, the Noam (Shazeer) actually wrote, like we owe this success to divine benevolence, like, that was, like, it's always a meme thing, right?

[00:47:57] Okay, so, like, GQA, MQA was always, like, the multi career type, was always, like A big controversial thing because MQA usually you get a hit because it's MQA and everything so people kind of know that like it was a very hit or miss like it was like it could you could get a hit in a performance from MQA like MQA alone MQA was always like You know, the choice, right?

[00:48:15] It's always like, okay, should we use MQA, should we not use MQA, right? When GQ came in, right, it became like a no brainer to use GQA because you don't get the hit anymore, and then you just get the fast, like, inference benefits of GQA, right? So I think GQA I mean,

**Swyx** [00:48:36] 2 now. Yeah,

**Yi Tay** [00:48:36] yeah, yeah. So, so, I think Lama 2 already.

[00:48:36] I'm not 2,

[00:48:52] The 70, 70 GQA, right? But, I mean, the reason why we call it Noam (Shazeer) Architecture because MQA came from DOM and GQA was like a follow up paper by some of my colleagues at Google, right? So I think GQA was, became a point where, okay, this is already accepted, like, it is good enough, like, it's a no brainer to use GQA.

[00:48:53] SuiGlu was an interesting thing because there was a very long period of time, so SuiGlu was a single author paper by Noam (Shazeer), and very few papers were, like, SuiGlu had very few citations, like, at the start. Only Google Papers was citing SuiGlu at one time, and a lot of them was like, like, I was like, at one point I was like, probably like, 30 percent of SuiGlu citations.

[00:49:09] Because every time, Like, SuiGroup became popular because of the updated T5, the T5 1. 1 that uses SuiGroup, right? And nobody actually really cared about SuiGroup for a long time, because I was checking why is this underrated paper not getting much citations, and then I think probably now it has like a few hundred citations by now.

[00:49:27] But I think SuiGroup is one of the things that I played around with a lot at Google. So SuiGroup really works. There was also a paper we wrote about Like, do transformer modifications, blah, blah, blah. Like, it was a paper with Noam, and Sharan, and Hyongwan, and stuff like that. And then, we ablated, like, so many transformer variants.

[00:49:46] Yes, yeah, I saw that. Some

**Swyx** [00:50:06] of them matter, but most

**Yi Tay** [00:50:06] of them don't. Most of them don't. And then, the only thing that mattered in that two part paper was, The paper was, in the paper was Swiglu, I forgot which exact Swiglu variant was it, but Ansposity at that time, right? So, so that was strong enough, like, to finding, to

**Swyx** [00:50:06] For, for the listeners, this is the inductive bias scaling loss versus model architectures, how does inductive bias No,

**Yi Tay** [00:50:06] no, no, not this one, there was another one, like to transformer modifications, something, something, something.

[00:50:06] Because portal auto was run, I think. It was run around,

**Swyx** [00:50:33] You gave the keywords. Yeah, yeah.

**Yi Tay** [00:50:33] I think the rms norm rope thing Not controversial. Like, it's, it's, it's not like, like, like, Obviously, I think rope is probably, like, it has that extrapolation thing, which is nice. And then, like, like, it's also, like, default now.

[00:50:33] Nobody wants to add positional embeddings anymore, right? And I think, I mean, I like the T5 style relative attention for a bit, but like, I think, okay, Rope is I actually ran that emulation for Palm, like the T5 relative attention versus Rope. I think Rope is similar to other things, but it has this extrapolation thing, which is nice, and like

**Swyx** [00:50:51] Which is why your long context version can go to 256.

**Yi Tay** [00:50:51] For most of the long context models, they use the Rope extrapolation thing, which is a nice property, right? So that was for Rope. I think there were also some things like the layer norm, like partitions and stuff like that, that were like, it mattered a little bit, maybe not too much and everything. But I think in general, there was not a lot of like, there are not a lot of things that people could do to the transformer.

[00:50:51] It's been like 4 5 years, right? It's amazing. The vanilla transformer, I think if you use it as it is today, will not be like that optimal, but like The transformer that we slowly evolve to now is like, Like the Noam (Shazeer) transformer is probably like very, very, very strong baseline that is very hard to like, I think you need a drastic shift to, to beat that, right?

[00:51:33] Or you could find like more like, like Swiglu is a small change, right? You could find like some small change that are like a big enough impact, widely that don't cost a lot of , because a lot of architecture changes, right? The moment they are Tedious to implement. Like, nobody, SQL is a simple thing, right?

[00:51:55] It's a pretty uneducated thing. It's a very simple thing to implement. Maybe that's why it's caught on, because it has, like, an additional boost. That's for the simplicity of it, right? So there's also a bit of implementation lottery, if you will, right? A little bit of if you propose, some very complicated thing for, like, 0.

[00:52:09] 1%. Yeah,

**Swyx** [00:52:24] nobody will use that, right?

## [00:52:26] Encoder-decoder vs Decoder-only

**Swyx** [00:52:24] The biggest, biggest, I mean, I can't believe we're taking so long to come to this topic, but the biggest Noam (Shazeer) architecture decision is encoder decoder versus decoder only.

**Yi Tay** [00:52:24] No, so encoder decoder is not like a Noam (Shazeer). The Noam (Shazeer) architecture is more like

**Swyx** [00:52:24] the Okay, maybe like more old school transformers.

[00:52:24] Maybe we want to just talk about the Decision on encoder decoder versus decoder only.

**Yi Tay** [00:52:42] So I, okay, I won't be able to comment about like exactly our setup, but like, I think encoder decoder are kind of very misunderstood from thing, right? So there's encoder decoder, non causal decoder, which is a prefix LLM, and then there's a decoder only model, right?

[00:52:42] Technically, a causal decoder and a non causal decoder are very similar in the sense that it's just a bidirectional mask, right? And then a prefix LLM decoder has only The only difference is that Encoder Decoder splits the inputs and targets into different non shared transformer stacks. And then, like, there's encoder bottleneck in the end, right?

[00:53:02] So, technically, people, like, kind of always associate, like, Encoder I like BERT, or like something like, like, you know, people get confused about these things, right? But I think in the UL2 paper, we really, like, kind of explored this, and also, like, maybe some of the big science papers that also talk about this, right, is that prefix LLM and causal decoders are very similar, that's a must.

[00:53:22] At the end of the day, they're all autoregressive transformers. That's actually, like, the only big benefit of encoder decoders, it has this thing called, like, I mean, what I like to call, like, intrinsic sparsity. So basically, an encoder decoder with, like, n params is, like, basically, if it's, like, It has the cost of like an N over 2 decoder model.

[00:53:43] So it is a bit like a sparse model because you actually spend the same amount of flops. It's just that you have two sets of parameters, like, for encoder and decoder, right? So it's actually flop matched with a decoder model of, like, half the parameters. So like a, like UL220B is actually about A 10 B decoder only model.

[00:54:01] Right. So you get free sparsity from that. It's, it's something that, okay. The, the, the, the OG T five paper talks about this. You, you can look at it. There's this complex detail. I, I did, I didn't like, when doing the UR two paper, I kind of like was mind blown by like, like, wow, I could decode so much more not bounded by The causal mask anymore.

[00:54:18] A lot of the efficient transformers, like a lot of the sparse transformers, like, I mean, the old, early days, that's like, , Linformer and like, whatever, things like this, they cannot maintain the causal mask, and that's why you cannot train a proper language model with this, right?

[00:54:35] If you separate out your very long context into an encoder, this encoder has no loss. Right, you could just do like aggressive pooling, you could do some crazy sparse attention that has like, final transformer or something like that, right? And then you could make that smaller than the decoder, you could make that faster than the decoder, that are just some of the advantages of like, why, , splitting into encoder and decoder could be beneficial to, like, just using a decoder only model.

[00:54:47] At the end of the day, the decoder in Encode decoder is a language model. It's still a regular autoregressive language model. So that's actually, I mean, it's not that much different from, like, a retrieval augmented language model. This is news to me. I don't know if you've ever expressed this, but

**Swyx** [00:55:15] yeah, this actually makes sense.

[00:55:15] Okay, okay, yeah, yeah, yeah. I don't, unfortunately, I don't know enough to push back on this, but on the surface of it, it seems to make sense. Would you make the same choices if you were not so focused on multimodality? You know, that's one of the ways in which I was thinking, like, Oh, encoder decoder makes sense, then it's more natively multimodal.

**Yi Tay** [00:55:32] I just have to say that it's relevant, it's also relevant, yeah, it's relevant, yeah.

## [00:55:52] LLM Trends - Llama 3 and Phi 3 Glowup

**Swyx** [00:55:32] Then we can move on to broader trends in LLMs, just commentary on the ecosystem stuff, like, completely independent from Weka. Commented on a few things, like, Lama 1 to 3 glowed up a lot. I call this the Lama 1 to 3 glow up, like, it improved into, like, an actual top tier.

[00:55:32] Open source model. Yeah. PHY 1 had a lot of criticism, but it seems like PHY 3 is getting a lot of love. Do you just generally see, like, in your open model tier list, like, what's going up and down?

**Yi Tay** [00:56:06] I think Lama 1 and Lama 2 are, like, quite mid, right? But Lama 3 actually got Good, right? I think Lama 3 is actually strong, right?

[00:56:06] I don't really follow Firewatch, it's just that Their whole

**Swyx** [00:56:26] thesis is the textbooks is all you need thing, right? Like that we can, well, we can use way less data than everyone else and still

**Yi Tay** [00:56:26] But I think you cannot cheat the scaling laws, right? Because, like, you, I remember saying, like, vaguely saying that, like, Like, oh, they match, like, Mixtra 8x22, or like, something like that.

[00:56:26] On, like, some Okay, I don't think these academy benchmarks are, like, that meaningful anymore, right? So, but then, like, then when you go, they go on LMCs, And then they get, like, maybe it just, like, seems slightly Maybe it's like I don't know about 5. 3. 5. 3 was

**Swyx** [00:56:44] just released like yesterday.

**Yi Tay** [00:56:44] Oh, I don't even, I didn't even, yeah, but I don't know.

[00:56:44] I think there's some, I don't follow 5. 3 that much, but I don't, like, a model that is synthetically, Actually, I don't even know this, I didn't even read the paper, but I think that a model that is based on the premise of distilling and stuff, something like that, is like, Not that interesting to me, but I think that like Lama tree actually shows that kind of like meta got a pretty good stack around training these models.

[00:57:03] Oh, and I've even started to feel like, oh, they actually, you know, kind of maybe caught up to Google now, right? That kind of feeling. That's also maybe a hot take on itself. But, but yeah, I mean, fire, I don't really kind of follow you that much. And I, I just, There's too much, too much things to follow. So I think it's like, I, I, I think like Lama Tree is probably like the most, the first most legit.

## [00:57:46] LLM Trends - Benchmarks and Evals

**Yi Tay** [00:57:25] When you say these kinds of things,

**Swyx** [00:57:25] like most legit, obviously there's some, there's vibes eval or whatever but I feel like a lot of people, the very common feeling is MML is kind of saturated. Yeah. So like, what do you look at now? Is it just LMSYS?

**Yi Tay** [00:57:25] Okay, so I think that LMSYS has its problems also. So LMSYS is not exactly like I mean, it's probably better than all these regular benchmarks, right?

[00:57:25] But I think, like, a serious LRM that's created their own evals, and a good eval set is one that you don't release.

[00:58:08] na: A good

**Yi Tay** [00:58:14] eval set is the one that you, like, okay, you release some of it, but, like, it's like, you don't, like, you know, let the, like, Let it be contaminated by the community. Yeah, I think iOS 6 is probably the most legit one.

[00:58:14] I mean, like, you know, the things like GSMK, human eval, the coding, they're all, like, Contaminated. Like, not, not, I would say, they're all, like, saturated, contaminated, no, like, you know, GSMK, whether you're 92, 91, like, no one cares, right? That kind of thing, right? But we still report three decimal places in all of our reports.

[00:58:28] Yeah, yeah, yeah, but it's kind of like, almost like this, like obligatory thing to do. You have this table of numbers of your thing at the bowl. It's interesting to see how the, the field evolves also over, over time for, for, for this type of, like, benchmarks. But I think evals are going to be important, and it's on the, actually, interestingly, it's on, probably, probably on the academics to, to set the correct.

[00:58:46] I mean, they, they have Like there been, academics have always been like, like, oh, we have no computer this, but like, okay, this is your chance to like steal the field in the right direction. Right. I think the, the

**Swyx** [00:59:03] challenge is getting attention so, you know, now MMLU, you know, is reaching its end of its life.

[00:59:03] Like what, what is next? Right? There's MMU or there's MMLU hard, which someone recently released. There's Pro MMU Pro, I think it's pro. Oh yeah, that's right, that's right. Pro. But like that only lasts you like a year. Right, and then, you have to find something else. So, I don't really know what is that.

[00:59:16] Well, so, one thing, you know, you had a comment, I think, in your breakup paper about there's two types of evals. This is a Vibe eval paper. One is LLM says judge, and then two is arena style. Right, that's sort of the two ways forward for just general evals that cannot be gamed.

**Yi Tay** [00:59:32] Oh, no, there's also Human evals that you, like instead of LLM as a judge, there's also like human evals that you run.

[00:59:32] Like that's kind of similar to Arena, but kind of different to SummerStand also. Different in the sense that like By

**Swyx** [00:59:54] the way, do you use your own staff to do that? Or do you like hire an outsourcing firm?

**Yi Tay** [00:59:54] No, we don't. We have like, we work with third party data companies to like, there are a bunch of these like around, right?

[00:59:54] But like, obviously we don't like eval them ourselves. Like,

**Swyx** [01:00:07] I don't know how much, how many evals you want to do, right? Like, I do think Andre Capalti mentioned that. Sometimes, like, the best researchers do their own evals.

**Yi Tay** [01:00:07] Yeah, looking at the outputs and stuff is something that, like, researchers should do,

**Swyx** [01:00:07] yeah.

**Yi Tay** [01:00:07] Well, there

**Swyx** [01:00:07] is one element of parametric evals, which I'm hoping that more people come up with, where, like, you kind of The benchmark is formula is generated from a seed, let's say. And you can withhold the seed, or like, you can vary the seed, like, you can report how your model did on the benchmark, given a certain set of seeds or whatever, and you can maybe average them.

[01:00:07] But in that way, it becomes harder, much harder to contaminate. I wonder if that is an example of this. Not specifically, this is just something I'm wondering for myself, but I did someone did recently put out GSM 1K which was Oh,

**Yi Tay** [01:00:47] the scale thing. I think,

**Swyx** [01:00:47] is it scale. ai?

**Yi Tay** [01:00:47] Yeah,

**Swyx** [01:00:47] yeah, yeah. Which this is some similar in that respect, like make it easy to make variations of a, of a one known benchmark, but like that is more likely to be withheld from from training data.

**Yi Tay** [01:00:47] Yeah, yeah, yeah. But eventually those will work. Like, so it, it's always a, like, like even we put out vibe. We also are quite, are quite like upfront with like, if the more people use it, there's a lifetime. It's like a car right. After you drive, run, run a certain mouse, it, it is time to shelf it. Right? Yeah. So I, I don't think there's like a, actually like a.

[01:00:47] Like a good solution. In general, I'm also like a bit I think this is like important for the community to think about, right? But like, is it like a fundamental limitation that any benchmark that goes out? Like, also there's also one thing is that in the past people used to like withhold test set, right?

[01:01:29] Like squat or something. They used to withhold test set. But then, like, after a while, I think people also realize that like, when you withhold, like MMMU, no, like when you withhold, it's like so much extra work for like the community to like eval on this that they just don't do that, right? It's either your.

[01:01:42] Dataset becomes, your benchmark becomes unpopular. I think it's also incentive things, right? So if you, let's say you are, you want to run like a contest, right? And then your goal as an academic is to get as much citations as possible on this benchmark paper, right? Like, then you, or like this, this, you want to be as famous as possible.

[01:01:57] You will not want to withhold the test set, because if you withhold the test set, and then people have, like, there was once, like, I mean, like many years ago, There were even some benchmarks where you had to, like, package your model and send it to them to run. And, like, these benchmarks never ever, like, took off.

[01:02:14] Like, took off. Just because, like, so at the end of the day, right, it's, like, It's the root problem, like, incentives. Like, it's the, also, the benchmark, the benchmarking problem is also, like, an incentive problem, right? So, like, it's also, like, like, people want to show their model is the best. And then the game masters want to gain as much clout as possible.

[01:02:28] And I think, also, LMCs also get caught into some, I don't have a, I don't have a take on this, but, like, there's, like, people who also feel that, They are also optimizing for hype, right? Their own cloud, right? So there's all this, I think it's a lot of interesting, like I don't know what field this will be, but I don't know, like, I think there's a lot of papers to be written, right?

[01:02:42] I mean, about how these incentives like rewards and incentives, like, kind of it might not be soft, so, I don't know.

[01:03:00] I would

**Swyx** [01:03:06] say SweetBench is probably the one that's kind of broken out this year as like now a thing that everyone wants to compete on as if you're a coding agent. I don't know if you have a view on it, but it's just, like, it should be known to be hard.

[01:03:06] You should be able to make progress on it quickly. That makes you popular and cited a lot. Yeah, yeah, yeah, yeah, yeah.

## [01:03:25] LLM Trends - Early vs Late Fusion Multimodality

**Swyx** [01:03:17] Multi modality versus omni modality. So this is a little bit of commentary on GPT 4. 0 and Chameleon. I don't know if you saw the Chameleon paper from Meta.

**Yi Tay** [01:03:17] Briefly saw it yeah, I'm not, I didn't really take a look at

**Swyx** [01:03:17] it.

[01:03:17] Basically, the general idea is that most multimodal models, like Lava or Flamingo, which are late fusion, which is you freeze, freeze, and then you join together, versus early fusion where you do it properly, where, like, everything is, you know, All the modalities are present in, in the, in the early training stage, and it seems like things are trending from late fusion to early fusion.

[01:03:36] Is is the general thesis with GP four Oh being very obviously early fusion, you guys, I I would class it as early fusion. I, I, I don't know if you have commentary on whether this is obvious to you or this is the, this is the way, or they'll just be, they'll coexist.

**Yi Tay** [01:03:55] I think whenever possible, like early fusion is better, I think there will still be a lot of work steps.

[01:03:55] Dual late fusion just because of like it's a GPU, poor No, no, no. GPU. Okay. Par partially, right. I, I see this as like an art, as an artifact of the line between language research researchers and vision researchers, and more of like, okay, like people who are training language models, they put out like LAMA whatever, and then somebody takes it and then.

[01:04:16] Do Lakefusion on top of it. It's more like a It's Conway's Law. They're shipping the org chart. Yeah, yeah, yeah, I think so. I don't know what law it was. Conway's Law. Okay, I didn't know about that. But it's kind of like an artifact of the organization, don't you think?

**Swyx** [01:04:36] No, it's just because people don't have money to train things from scratch.

[01:04:36] I don't know.

**Yi Tay** [01:04:53] No, no, I mean, even in big companies, right? I mean, I don't know how things have evolved in many companies, but like You're talking about Flamingo? Like language and vision and Teams don't use to be the same team. Right? Yeah. So I think this is like a artifact of, of this, but as early fusion models get more traction, I think the, the, the, the teams will start to get more and more.

[01:04:53] It, it is, it is a bit like of how all the tasks that unify like from 29, 2 0 1 9 to like now is like all the tasks are unifying now is like all the modalities unifying. And then I think like eventually everything moved towards like early fusion. Yeah.

**Swyx** [01:05:14] Yeah. The other element of multimodality is I, I've been calling this screen modality.

[01:05:14] Screen vision versus general vision, in the sense that Adept is like very, very focused on Screens, tables, charts, most vision models focus on things in the real world and embodied, sort of, images. Do you have a view on the usefulness for this?

**Yi Tay** [01:05:32] I don't think that's like a huge, like, I mean, I think at the end of the day, like maybe screen intelligence is like more useful in general, but like, what if you have like a natural image in the screen?

[01:05:32] Yeah, I mean, no, no, no, I think at the end of the day it should be mixed, right? If a model can do natural images well, it should be able to do screen. Wow, and everything. I think at the end of the day, like, the models would become like, I don't, I don't see that there will be like, like, screen agents and like, natural image.

[01:06:00] Humans, like, you can read what's on the screen, you can go out and appreciate the scenery, right? You're not, like, say, I only can look at screens. Right? So, I mean, I think eventually the models would, like, be this good on everything. I look at it from a point of, like, capabilities. And screen is, like, you know, there's even screen that's also, like, , like, mobile phone screen and there's also, like, you know, laptop screen, like, also, like, you know, Different type of interfaces and everything like reading emails, whatever, right?

[01:06:16] But like reading a page from a website or like, you know, buying something from like Amazon or something like all kinds of things, right? And then even in the picture of like a shopping website, there could be like a natural, like for example, like picking Airbnb, right? But like, there's then there's a natural image in there.

[01:06:38] Then it's like, you have to understand like how nice is the scenery, right? Or like, , like, where is it? Right? Like, so I think at the end of the day, it's probably like the same. If you want to build a general model. Yeah, yeah, yeah. But I think The natural images is like, way easier, like, as in, just way, like, the models currently, current models are actually already very pretty good at, at this natural, natural images.

[01:06:52] And I think, like, screen images are just something that people need to enhance the capability a little bit more, that's why there's, like, some focus on.

**Swyx** [01:07:12] I'll touch on Three more things, and then we'll just go to career stuff.

## [01:07:22] LLM Trends - Scaling Laws

**Swyx** [01:07:12] Scaling laws. Palm 2 was Chinchilla, which is one to one scaling of model parameters and data.

[01:07:12] Now you are training a 7B model with 5 trillion tokens. What are you thinking about the trend in scaling laws for data?

**Yi Tay** [01:07:28] Chinchilla scaling laws are just like optimal for like with this amount of compute, how much is the thing, right? But like actually the optimal Like, there's no, I mean, this is something that even before I left, we already knew that, like, Chinchilla scaling laws are not the end of it, right?

[01:07:28] Obviously, there's also a inference optimal scaling law, which is, obviously, you take a small model, and then you just blast it with as much compute and data as you can, Until? Until you saturate on everything that you care about, right? So I think, like, Lama tree is for what? 15 T tokens or something, right?

[01:07:48] So I think Which is ridiculous. It is ridiculous to be honest. But at a certain point of time, your value per flop is not great anymore because you just, you know, your models eventually get saturated. But then the problem of, like, the question of, like, where is this saturation is also, like, you always find, like, some metric that you still continue to improve a little bit, and then you're like, okay, maybe, like, like, Oh, 100k it to continue training, like, just a little bit more, right?

[01:08:03] But then it's like, where does it end, right? But I think at the end of the day, like, the thing about Chinchilla scaling laws is that it was a bit misunderstood as though, like, like, this model, you need this compute, and, and, and if you train the Chinchilla scaling laws, like, you kind of, like, Like, I don't know why so many people had this idea that you will not improve past the Chinchilla scaling law.

[01:08:27] And then, people make so much big deal about trading past Chinchilla scaling law, like, Oh, Lamaldu is the first model. Like, T5 base, right, was 1 trillion tokens. That was already so much beyond Chinchilla scaling law, right? Because that was T5 base,

**Swyx** [01:08:46] right? I think OPT and GPT maybe set that as an industry standard.

[01:08:46] It's GPT 3 specifically. No, sorry, wait, GPT 3 was not Chinchilla.

**Yi Tay** [01:09:03] No, I think like OPT and Bloom, right, models like this, they train a large model and with a very small number of tokens, and the model turned out to be bad.

**Swyx** [01:09:03] Yeah, yeah, so I'm talking about Kaplan, the pre Chinchilla one, the Kaplan scaling loss.

**Yi Tay** [01:09:03] Oh, okay, okay, I see, I see.

**Swyx** [01:09:03] That one was from OpenAI. Anyway, dev of Chinchilla covered. Agreed. But Trinidad is still a cool paper, I think Trinidad is still an

**Yi Tay** [01:09:03] important paper. I love any

**Swyx** [01:09:03] scaling laws paper, to be honest. It's like, such a service to the community, in general. Hugging Face recently did one, Datablations, which is like a data scaling laws paper, looking at data constraints, which was kind of nice.

## [01:09:41] LLM Trends - Long Context vs RAG

**Swyx** [01:09:03] Long context, people are touting million token context, two million token from Gemini, magic is everywhere. talking about 100 million tokens. How important is it, do you think? I think we need

**Yi Tay** [01:09:03] to solve benchmarks first before solving long contacts. We have your benchmark. No, no, no, no, not like benchmarks for long contacts.

[01:09:03] OK, yeah. because the needle in haystack is basically like an MNIST, or like a unit test for these sort of things, right? But I think there's one But about, like, hitting the context line and the other part about, like, actually Utilizing. Utilizing, right. I think Gemini's long context is surely, like, amazing.

[01:09:57] Right, but I think, like, for the community to move forward in this, then it comes to a problem of, like, How do we evaluate this? I think I've seen some long context benchmarks, like, coding one, like, And stuff like that. Like, I think Making those are important, and for the community to heal crime, but I think long context is important, it's just that you don't have a very good way to measure them properly now, and yeah, I mean, I think long context is definitely the future, rather than RAC, but I mean, they could be used in conjunction.

[01:10:13] Definitely, okay. Yeah, yeah, yeah. That's a hot

**Swyx** [01:10:42] take. Which part of the Long context is the future rather than RAG. Like, you would, they will coexist, but you are very positive on long context. I will put myself on the other, so your mirror image, which is like, long context is good for prototyping, but any production system will just move to RAG.

**Yi Tay** [01:10:42] There are a lot of application use cases where you want a model to take the time and then come up with the right answer, right? Sure. Because RAG is like

**Swyx** [01:10:42] But you will use those sparingly because they're expensive calls.

**Yi Tay** [01:10:42] Yeah, you, it depends on like the nature of the, the, the application, I think. Because if in rac, right, like you, there's a lot of issues like, okay, how you, like, you, the, the retrieval itself is the issue.

[01:10:42] Or like, you know, you, you, you might get fragmented if it's like, what if it's like a very complex story, right? That you like a storybook or like a complex like thing, right? And then, and then like we, like rec is very like, you kind of chunks, chunks and chunks, right? Yeah. The chunking is like, and you definitely have lots of information, right?

[01:11:18] So there I, there are a lot of application use cases where you just want. The model is like you were like, okay, like a hundred bucks, like take your time, take one whole day, come back to me with like an answer, right? Rather than like, I pay like, like one cent and then like get back a wrong answer. So I think that's like, that is actually very easy to show that RAC is better than long context because there are a lot of tasks that don't need this long context.

[01:11:35] You like, like fact retrieval, you just like RAC and then you do this thing, right? So like, long context may get a unfairly bad rap sometimes because like it's very easy to show like, RAC is like, 100 times cheaper, and it's very easy to show this, right? But then it's also, like, not so easy to emphasize the times where you actually really need, like, the long context to really make, like, very, very, very, very, very good, like, decisions.

[01:11:57] So, yeah, I mean, I think both have pros and cons depending on the use cases. Using them together is also interesting. hyperparameter that you have to wiggle around, right? Yeah.

## [01:12:31] Long Context vs Finetuning

**Swyx** [01:12:21] There's another wiggle on the hyperparameter, or there's another fog on the hyperparameter, which is how much you fine tune. New knowledge into the model. Are you positive on that?

[01:12:21] Do you have any views? So, for example, instead of doing RAG on a corpus and then inserting it into context, you would just fine tune your model on the corpus, so it learns the new knowledge. In whatever capacity,

**Yi Tay** [01:12:39] right? This is cumbersome, I guess. This is cumbersome, and you don't want, like,

## [01:12:56]

**Yi Tay** [01:12:39] You don't want so many of, like, the point of in context learning is so that you don't actually have to do it.

[01:12:39] I think this one is depending on, like, the business use case, right? If fine tuning is actually, like, the, you are very clear, like, you want this knowledge, and then you just fine tune once, and then you don't ever have to pay, like, context, like, in the context window. If there's a cost again, then maybe that makes sense.

[01:13:00] But if the domain keeps changing, then you might not like it.

**Swyx** [01:13:14] Yeah, obviously it doesn't make sense if the domain keeps changing. But I think for the model to maybe update fundamental assumptions, or you know, re weight associations between words, for let's say a legal context versus financial or medical context, like it might Work.

[01:13:14] This, this is the arguments that some, some people are talking about. So, you know, I see this as a trio, like it's long context, it's rag and it's fine tuning. Like people always have this, like whether either of them will kill, rag, basically , because rag is kind of the simplest approach.

**Yi Tay** [01:13:29] Yeah, yeah. Okay. I, I mean I, I could see like, like if you wanna like a model for medical domain, legal domain, then fine tuning really works.

[01:13:29] It's always the move, like the, you know domain specialized model, universal model and, and you know, the kind of this. Tension between both of them. I think it definitely, like makes sense. It also makes sense, like, to, fine tuning can also be, like, an alternative to, to RAC, yeah.

**Swyx** [01:13:49] Yeah, well, there's some, there's some companies that are set up entirely just to do that for people.

[01:13:49] So, it's, it's interesting that, I mean, I, I, I kind of view RACA as, like, not working in that space, but you could potentially offer that if you wanted, wanted to.

## [01:14:14] If emergence is real, when does Efficiency work?

**Swyx** [01:14:07] Okay, I was going to ask about efficiency and scaling. I'll just mention this briefly, and then, and then we can talk about MOEs, because I discovered that you, you, you wrote.

[01:14:07] You're a co author of the Sparse Upcycling paper, which is excellent. Oh, no, I was just advising on that. Oh, okay. Yeah, yeah, yeah. But you can talk about Sparse Upcycling, it's a topic that's hot. But more generally, efficiency, in my mind, when I go to ICI Clear, or I go to NeurIPS, I see efficiency paper, 90 percent of the chance, I'm just going to ignore it.

[01:14:23] Because I don't know if it's going to work. And I think this is related to your Some of your

[01:14:39] scaling work and your inductive Oh, okay,

**Yi Tay** [01:14:43] scaling log Which is

**Swyx** [01:14:43] like, okay, there was this T. R. Texas, I don't know who this person is Yeah, he keeps talking about me. It's fucking amazing Oh, okay. Yeah, he does have some obsessions, but like, he's good.

[01:14:43] I don't know who he is, but he's good. So he says, if 2024 papers are to be trusted, you don't need most attention, you don't need high precision, you don't need most KV cache, you don't need most feedforward network layers, you don't need a reward model, blah blah. Like, it's like, a lot of efficiency papers are just like, hey, on this small example We cut this thing out.

[01:14:56] Works fine, or works great, works better, whatever. And then it doesn't scale. Right? Like, or So it's a very interesting observation where like, most efficiency work is just busy work, or like, it's work at a small scale that doesn't, that just ignores the fact that like, this thing doesn't scale, because you haven't scaled it.

[01:15:14] It's just fine for a grad student, but as for someone who's trying to figure out what to pay attention to, it's very difficult. to figure out what is a worthwhile direction in efficiency.

**Yi Tay** [01:15:30] Yeah, that's, that's, that's a good point. I think there's a couple, I agree with you fundamentally that like, it's actually quite easy to tell, like when you see a paper, okay, this one doesn't work, this one works, this one doesn't work.

[01:15:30] I guess the hippo account will just tell you that, sometimes it's just a diary about this thing doesn't work, this thing works, everything. Right, sometimes it's not like, you know, you can always find a dataset where your efficiency method gets neutral results, right? You can always find one, I have comparable complexity.

[01:15:47] And you know what's the most, the cutest thing ever? Every time some people propose like this, they run like some zero shot score on like some LME Valhannes or something like that. And at 1B scale, all the numbers are random, basically. Like all your boolkill, they're all like, Random chance performance, right?

[01:16:04] And they will be like, okay, I get like 50 versus 54, I'm better. But like, dude, that's all random chance, right? Like, you know, sometimes I see people that run experiments that like, And then it's like

**Swyx** [01:16:21] That's a good tell.

**Yi Tay** [01:16:21] I think it's very, like, the sad truth is that like, it's very hard to tell until you scale up.

[01:16:21] And sometimes the benchmarks that we have don't even probe entirely about what, , I mean, especially all the works about, you know, the transformer alternatives, right? You can always find, like, this alternative that at 7B scale, at 1, 3B scale, you kind of like, okay, I met transformer this and this, this, this, right?

[01:16:39] But then what's the implications when you go to like 200B? What's the implications when you go to 100B? No one knows that, right? So that's, that's one thing, right? And I think developing your own intuition of like what works and what Doesn't work is, is important. For example, if somebody's like, Okay, to be honest, all researchers, like, sometimes are also, like, guilty of this sometimes.

[01:16:55] Because you cannot test on, like, everything. You cannot test on everything, right? So sometimes, you also just want to show your method works on this. But it depends on the objective. If the objective is to write a paper to ICML, sure, you can find two datasets your stuff works, right? But will you get adopted?

[01:17:14] I am not sure.

**Swyx** [01:17:29] Yeah, researcher metagame is one thing, but as a consumer of research, I, like, I'm also trying to figure out, like, what is, how do I know what is a, what is a useful direction, you know, that, that's the interesting thing.

## [01:17:41] MoEs and Upcycling

**Swyx** [01:17:29] So, for example, MOEs seem to have worked out. Yeah, yeah. I, I, I, I'll go so far as to say it's the first form of sparsity that worked, like, Okay.

[01:17:29] 'cause there's, there's so much varsity research, like we can, chop all these parameters and look, we still, still perform the same, but then it, it never actually works. But, but OE is really, oh, you mean like

**Yi Tay** [01:17:50] the pruning line of work?

**Swyx** [01:17:50] Pruning? Pruning line of work. Okay. Sorry, I, I should have used that word.

[01:17:50] So like, you know, I don't know if you have any commentary on like ra, deep seek Snowflake Quinn all these proliferation of Moe e models that seem to all be spars op cycle because, you know, you, you were advisor on, on the spars op cycling paper.

**Yi Tay** [01:18:03] So the spas abstract Bay was mostly vision focused with a little bit of T five.

[01:18:03] Okay. Experiments. So it was, early stage of like abstract. But it was good that Google was really think about this like longer and, and normal so had on it,

**Swyx** [01:18:21] right?

**Yi Tay** [01:18:21] Yeah.

**Swyx** [01:18:21] I think always the way to go. Is it like a hundred experts, a thousand experts , for some reason the, the community settled on eight.

**Yi Tay** [01:18:21] Oh, you probably get more gains from, from more, more than eight, I think. But like, I think in general it's like. MOE's are just a trade off with like, prime and flop, right? And then you're able to like, kind of, make, like, you kind of make that. That, that in like that, that scaling log increase from, from that additional.

[01:18:21] So you, you can keep a low flop but kind of have more parameters. It's just changing the flop parameter ratio. Mm-Hmm. Keeping in mind there's a lot of inefficiency

**Swyx** [01:18:55] between the experts.

**Yi Tay** [01:18:55] Yeah. Yeah. Yeah. I think as a architecture itself, the flop brand ratio makes it like worth it. Right. But I think the, the thing that's not very well understood is that, like, how does like MOE, like, like for me as a research question, is that like when you.

[01:18:55] Like, how does it, like, relate to capabilities and stuff like that, like, does this inductive bias actually, , for example, when you do, like, massive instruction tuning, I think there was this paper, like, Flan MOE or something, like, they showed that, like, , instruction tuning, I'm not, like, fully sure, I don't recall fully, but, like, when you do massive instruction tuning, like, MOE models are, like, they behave differently from a, from dense models and stuff like that.

[01:19:15] Like, I think, Okay, like, fundamentally, I just think that MOEs are just, like, the way to go in terms of, like, flop parameters. They show that they bring the benefit from the scaling curve. If you do it right, they bring the benefit from the scaling curve, right? And then, that's the performance per flop argument, activated params, whatever.

[01:19:36] That's, like, kind of, like, that's a way to slightly cheat the scaling law a little bit, right? By having more parameters, right? I think the more interesting thing is about, like, what trade offs do you make in terms of capabilities? Because of this new architecture. Mm. I think that's actually like the, the question that I, I think I, I guess all the frontier labs, they already know this, but nobody is writing papers anymore about this.

[01:19:52] So like, you just have to live with, with what? Like, but I think OI think I'm, I'm, I'm, I'm bullish about Moes. Yeah.

**Swyx** [01:20:12] Yeah. I had to, I mainly exercise for myself on reading research directions and what their asto asymptotic value is. Mm-Hmm. and I put OS pretty low because I think you have a good base model and then you upcycle it and it bumps you a little bit.

[01:20:12] And I think that's it. But like, I'm always seeking to invalidate my hypothesis, right? Oh,

**Yi Tay** [01:20:34] but like, from scratch, MOE is also promising, right?

**Swyx** [01:20:34] From scratch, MOE is promising I

**Yi Tay** [01:20:34] think in the IU case, you'll do MOE from scratch,

**Swyx** [01:20:34] I think. Okay.

## [01:20:47] The Efficiency Misnomer - Efficiency != Speed

**Swyx** [01:20:34] The last part that makes me uncomfortable about MOE debate is actually it's related to another paper that you wrote about the efficiency misnomer, in the sense that, like, now people are trying to make the debate all about the active parameters rather than total parameters.

[01:20:34] But it seems like, it sounds like that's something that you're comfortable with, like, flops at inference is, is a relevant metric. And it's, it's not that Well, thanks for, like, actually reading all the, like, reading the papers. You're trying, man. It's very hard to copy. You have a lot of papers.

**Yi Tay** [01:20:58] I'm actually very impressed that you're bringing up these papers.

[01:20:58] Yeah, I'm using attention.

**Swyx** [01:21:15] Yeah, thanks, thanks. And also, I mean, I'm interested in efficiency that works. It's just very hard to find efficiency that works. And so, like, anything that helps me have high signal on efficiency is helpful.

**Yi Tay** [01:21:15] So I think for the inefficiency misnomer, by the way, I love the paper, by the way, it's quite a fun time working on it.

[01:21:15] I think inefficiency misnomer was like, we found that a lot of people, like, they use params, like, especially, like, like, to the kind of, like, right, and then MOEs was not very hot, like, in the community at that time, right, but MOEs were, like, a thing long ago. So I think using active params, I'm comfortable with using active params to kind of approximate like cost of the model, but like in the efficiency misnomer paper, we actually made it quite clear that you should always look holistically about like, because you have serving, like additional serving costs, like fitting in the GPUs, like fitting on single node, and something like that.

[01:21:33] The

**Swyx** [01:22:04] interesting one was speed. Nobody really talks about speed, but your paper actually talks about speed.

**Yi Tay** [01:22:04] I have something to say about speed, throughput, right? There are so many methods, right, that are proposed about efficiency, right? They are like, theoretically, like faster because of some complexity or like something like that.

[01:22:04] But because there's no way to work around the implementation, or like your implementation becomes so hard, it becomes like 10x slower. There's so many papers around. It's not hardware aware. It could be hardware, it could be software. Just the way that, like, you have a convenient way to, like, in its mathematical form, it's actually, like, okay, linear complexity, like, whatever, and it's actually theoretically faster.

[01:22:20] But, like, just because you have to, like, do a scan or something like that, and then it becomes, like, actually, like, ten times slower in practice, right? There are a lot of things, like, Not a lot, but like, there are some things that are like, some methods that are like, like this, where you don't take into account throughput, right, which is also the problem of like, sometimes, like, the incentives of like, like people working in efficiency, you can easily just like, sell a paper as like, more efficient, People will not suspect that, because the reason why we wrote the paper is that so many people were confused about, like, efficiency itself, right?

[01:22:42] Yes. And then they will be like, okay, like a lot of these unsuspecting reviewers, especially, like, even academics, or, they, they, they don't have, like, that, that real, real, real feeling. They were less like, okay, less parameters, more efficient, right? So you could have a method that's, like, less parameters, but, like, three times slower, because, you know, a lot of times when you add things to the model, It becomes slow.

[01:23:12] Every time you add complexity, especially if it's like something that's not hardware optimized, no kernels, or like something that is like bad for TPUs or whatever, your model just becomes like slow. Oh, that's a

**Swyx** [01:23:31] temporary issue.

**Yi Tay** [01:23:31] People can fix it, but some things are not like so, some things may not be like so easily fixed, or like it just adds a lot of like, like SWE costs to to optimize it, right, and everything, right.

[01:23:31] But then it's always marketed as like, because I save params, so I save. Right, and then also like, the params will add a different place of the model. Like, for example, like, If let's say you, even in the case where you param match models, right? If I take out like, some brands from like, FFN, right? And I put it to like, embedding layer.

[01:23:51] Embedding layer is like a, it's just, it's a cheap operation for embedding layer, right? But my model becomes like, lopsided, right? I could say I brand match this. But it's not Flo match, it's not throughput match, right?

[01:24:11] na: Yeah.

**Yi Tay** [01:24:21] Because the, it's unbalanced. It is unbalanced or the, the side, right? So there's also of this style of tricky things that like when mixed comm model comparisons like very, very, very, very, very difficult.

[01:24:21] And because you cannot even put like flop throughput and speed flop. Params and speed, like actual speed, right, in the same plot, right, and then there's always like one money shot in a, like, there's always like a Pareto kind of compute, like, whatever, plot, right, like for marketing in papers or something like that, it's always very easy to, like, I mean, not intentionally, but like, to subconsciously, like, show one story when it's actually, like, there's, like, all these other things to consider.

[01:24:31] Yeah, yeah, it's

**Swyx** [01:24:58] a selection bias, self bias, whatever. Very cool. Okay, well that was mostly of most of the technical side.

## [01:25:05] Open Source vs Closed Models

**Swyx** [01:24:58] We have one commentary that will happen today on the future of open source models. Basically Founders Fund said, like, the future is closed source. You were agreeing with it. And a lot of the open source fanatics, you know, are up in arms over this.

[01:24:58] I don't know if you get a comment about just Oh,

**Yi Tay** [01:25:19] okay. Okay.

[01:25:19] Open

**Swyx** [01:25:21] versus

**Yi Tay** [01:25:21] close

**Swyx** [01:25:21] and close, whatever. So, so,

**Yi Tay** [01:25:21] I mean, I, I don't really like when, I mean, like if you're, if you're referring to the tweet that I wrote, but like, I wrote something about, about it, but

**Swyx** [01:25:21] this is huge. Like, so many people are commenting about it 'cause they, they have personally, physically offended their open source cannot catch up.

**Yi Tay** [01:25:21] Okay. No, no. Wait. Okay. So I, I, I want to say it's like I'm not, like I contributed to open source in the past, so I'm not like. against like open source per se. But the interesting thing that I want to talk about here is that like, there's a difference between like, I draw a line with like, open source, as in like, okay, Lala, Luma, Lama tree is like, it's like, metal has a that is like, okay, hypothetically, very similar to to like Gemini or something, but they just didn't decide to release the weights.

[01:25:21] Yeah, it's open weights. Right, it's open weights, everything, right. I think when most people try to say that like, open source is catching up and everything They kind of mean like, this grassroots, like

**Swyx** [01:26:01] Yeah, this distillation No,

**Yi Tay** [01:26:01] this bottom up people that are like these indie developers that are like, coming together to like, like, fight, like it's romanticized and it's dramatized to some extent just to fight against like this, right?

[01:26:01] Definitely, yes. And To be very fair. I think that there isn't really much, like, like so far, if you just look at the, the fractions of people, the big labs are just pushing and pushing and pushing. The academics like Stanford and stuff, they came out with DPO, they came out with things like that. They, they make some like, but they, they're kind of in, in between the line of like open source community and, and then there's also like the developers that are like.

[01:26:23] Fine tuning on GPT 4 distilled models and everything, right? I don't, I think the open source, the underlying, like, thing about, like, collectively improving something, I'm not, like, criticizing it for the sake of criticizing it, but, like, I'm just saying that, like, in order to make progress, right, I think the incentives of Open source, like, what I observe is that, like, people like to do things like, they like to take somebody else's model, they rename it, they make a quick win from there, and then, like, you notice that, like, when people realize that, like, this turning on the GPT 4 tab, and running some DPO, it's not going to give them the reward signal that they want anymore, right?

[01:26:45] Then all these variants gone, right? You know, there was this era where, There's, wow, there's so many of these, like, I can't even, I lost track of this, like, all these model variants. But now they're all gone, because people realize that, that you cannot climb LMSYS, because you need something more than just something that is lightweight, right?

[01:27:22] So I think that was just my overall, like, Honestly, the Hugging Face leaderboard contributed to most of that. It's not LMSYS. No, no, I think LLC is probably they realized that they could not. Yeah, right. The open LLM leaderboard is probably like a big problem, to be honest.

**Swyx** [01:27:37] We're talking to Clementine in one of our future episodes.

[01:27:37] Okay,

**Yi Tay** [01:27:55] okay, okay.

**Swyx** [01:27:55] They dedicate a lot of, I mean, there's so much attention to them, it's a tough problem. But they're providing a public service, for sure.

**Yi Tay** [01:27:55] Yeah, I mean, good intentions are always good. I mean, good intentions are always good. I'm interested in, like,

## [01:28:08] Personal Productivity

**Swyx** [01:27:55] Just like, just career wise what is your productivity practice?

[01:27:55] Or, and so I'll split it into three, three things. Keeping up, like reading papers and whatever, the outside world. And then two, like how you organize your own work. And then three, like work and life. Just use any, any, take that in any order that you wish.

**Yi Tay** [01:28:12] I don't have much of a life, actually. But I am trying more to have more.

[01:28:12] I mean, you're a father now. I have a baby now, so like, I'm trying more to have more life and and everything like this. I think the productivity hack that I have is this, like, I didn't have like a boundary between my life and my work, like, for a long time. So I think I just cared a lot about working most of the time.

[01:28:31] Actually, for the last like, during my PhD, during my, at Google and everything, I'll be just like working all the time. It's not like the most healthy thing, like ever, but I think that that was actually like one of the biggest, like, productivity, like and I spent, like, I like to spend a lot of time, like, writing code and I just enjoy.

[01:28:47] Run experiments, writing code, and stuff like that, right? So you kind of, if you enjoy something, it's not work, right? So like, it's very strange. It's like, it's like, I would get distracted by, sometimes I have to watch some Netflix series, because like my wife asked me to, like, watch it, like, or somebody tells me that I've, I've, I'm, I'm back on time on some, some shows, right?

[01:29:03] But then I get distracted by, My experiment is running and I just end up like, like writing code instead of like, so things like this. It's not the most healthy thing, but I think that's one. I'm

**Swyx** [01:29:19] looking for like a practice where like, okay so Andre recently had a thing where like before, when he wakes up, he doesn't look at social media.

[01:29:19] He only goes to , street to work. Damn, I check Twitter the moment I wake up. I know, see, it's just something I do as well. But I'm like, damn, that's a smart rule. And like, I'm looking for rules like that. No, he doesn't check social media because his phone is exploding all the time. All the time, yeah.

[01:29:35] I don't have so

**Yi Tay** [01:29:48] many likes and followers, so it's

**Swyx** [01:29:48] fine. Yeah, you get there. Rules like that, mantras that you've developed for yourself where you're like, okay, I must do this. So for example, recently for me, I've been trying to run my life on calendar for a long time, and I found that the only way that I work is I write things down on pen and paper, and I cross them off individually.

[01:29:48] And the physical action really, really helps me, you know, get things sorted. And that's work wise. Reading wise, I don't know if you know, but I've been running this AI newsletter. Like all those summarizes, all Twitter, Reddit, discord and all that. So that helps me keep up, because I have like a socially graded, and I personally vetted the entire pipeline from beginning to end, so like, this is my input algorithm, I know how to keep up with news because I now have a Information condenser.

[01:30:06] So like, I'm trying to figure out what is your algorithm or what is your rules for keeping up. I've

**Yi Tay** [01:30:34] got something for keeping up. So I used to check archive like every morning when the gate opens, I just check archive. I will wake up 9. 30am Singapore time, the archive gate opens, right? And then I'll be very sad if there's no papers to read.

[01:30:34] But you usually just pick one paper or two papers that you find interesting. I don't read them, I just like skim like the thing, right? So I used to do that. I don't do that anymore. I mean, ever since I have been in the startup, I You have a real job now. I read less papers, right? But I used to cam at the door of archives quite frequently just to see

**Swyx** [01:30:52] That's not a good use of time.

[01:30:52] I'll come out and say it. It's not a good use

**Yi Tay** [01:31:11] of time. It's a newness bias. Sorry, go ahead. It's just because I ran out of things to It's just that the new stuff comes out, right? Yeah. The new stuff comes out, so that's how I keep up to date. So in the space of three years, you read every No, no, I didn't read everything.

[01:31:11] It's just that, it's just that. But these days I realize I don't have to do that anymore. Just because if the paper is important enough, Twitter will show it to me. So I, I, there isn't really, like, And one thing I do is that I actually don't read papers like that, that much anymore. I just like skim them, like, almost, right.

[01:31:27] The so that's for keeping up, like, with papers, research, everything. And the other thing more of like, just like a productivity point of view is that I used to always keep, like, the, like, you know, the text. Like, I usually start writing. The thing while working on that thing itself. Like, so even, like, let's say, like, like, if you want to launch something, like, then the end goal is like a blog post or shipping something, everything, right?

[01:31:42] I like, I'm not, not, not really a launcher or like, like, just papers. I always like to look at it from, like, what's the, the story and the end. And then I just like figure out what I need to do to get to, to, to kind of, right. So I think as a researcher, like, this is something like, I would have, like, Like so many drafts of like, like when I'm start, I start the project.

[01:32:06] I don't know the experiment instead everything. Right. But I like to imagine like what the title would be. Yeah. Right. And then I always check, like, I always like, so I, I mean my friends at Google would know that I always have like, like a like the overly draft of like so many. And then I would just spend time looking at it, like looking the title, is it better to second?

[01:32:24] So I care about, I used to care about a lot of things, but this actually helped my product. 'cause every time I look at it, I'm like, okay, this is the final product. I'm like booking towards it. Right. 'cause I think a lot of researchers, they, they tend to like. They swoo around with their experiments and they never like ship the final story.

[01:32:39] It's like the shipping, like, like I mean, it started out with ship products, but like, as a researcher, your product

**Swyx** [01:32:52] management, yeah, you're shipping

**Yi Tay** [01:32:52] the thing. So I like to, I like to hang around a lot in my, in my drafts and, I get motivated from that. And that's like one productivity thing that I did as a researcher.

[01:32:52] Yeah. So I think that that's other than that, I don't really have any things that I do that. Probably different from others. Yeah, probably you don't know it.

**Swyx** [01:33:08] This is unconscious competence versus

## [01:33:19] Singapore vs US Academic Scene

**Swyx** [01:33:08] what's it like just NTU PhD, you know, just the story of like, how is it coming out from NTU, which is Which is like a good school, but like not, you know, not typical target school for like a big lab.

**Yi Tay** [01:33:08] I did my PhD unknowingly. Like I didn't have very, like when I was, I was a very regular undergrad. I had decent grades, but not the best grades. I was not like super smart in school or something like that. I, I was I wanted to do a PhD just because I was like curious and, and I, I mean, like, and then I wanted to stay in Singapore at that time, so I just like naturally just did a PhD there.

[01:33:08] I didn't even know Vet, my advisor. I didn't even think too much. I just like fell into the PhD program. And then that was when I realized that, oh, actually I can do research. Like, I'm like pretty decent at research. Like, I just fell into a PhD like, like unknowingly. And I definitely like, NTU leaves a lot to be desired.

[01:33:52] Actually, to be honest, I think that I mean, Singapore leaves a lot to be desired in general. Like the research community here is like, like probably not great. So how, how did you like

**Swyx** [01:34:08] break out? , if I was you, I would have, I would have no idea how to break onto the international scene, and

**Yi Tay** [01:34:08] I think, I think it was, okay, to be honest, like, in retrospect, it's a bit of, like, a bit of a miracle, or, like, I mean, it's not easy to, I think, I could not, if I had, like, a product, like, someone to mentor, like, I could not, like, Tell somebody how to replicate the same thing that I did.

[01:34:08] It's much easier now, maybe, compared to in the past, but I've been mostly self supervised during my PhD. Like, my advisor was basically like, like Grammarly. Like a free plan of Grammarly. He won't watch this, so it's fine, but like, there's a lot of things that, that, that, it was like this strange arc of my life where I was figuring out research by myself and, and everything.

[01:34:36] And, and okay, maybe going back to the, the change of opinion is that like the biggest culture shock I had, like, when I was moving from a Singapore PhD to Google, I think my research, like, If you went straight to Mountain View. Yeah, I went to Mountain View. I started at Mountain View. Like my research taste and everything, like, like I was, it was so different.

[01:34:56] Like the research culture is so different in, in US and in Asia. I had to grow so much, like doing my time at Google to like actually evolve. And then whenever I come back, right, I still have friends in like faculty in here and everything. I don't think that I'm a snob or they think that I'm like, Being like a very nasty person.

[01:35:13] Because I think to be honest, the research here is like in Singapore is just basically like, they just care about publishing papers and stuff like that. And then it's not impact driven. I think at US it's mostly focused on impact driven and the thing needs to make real impact, right?

**Swyx** [01:35:31] To be fair, you're also working at an industrial lab versus an academic circle, right?

[01:35:31] Like, you're comparing apples and oranges here a little bit.

**Yi Tay** [01:35:51] I mean, at the end of the day, I think research is still Like fundamentally like, we, as an industry, RIS, you still write papers, your goal is to advance science and everything. To be honest, it's, it's all the, you know, the incentives rewards system is, like, different, and, and maybe, like, slightly different than everything, but, like, at the end of the day, I still feel that researchers are researchers, scientists are scientists, no matter, like, really, like, where you are.

[01:35:51] I, I will get so much dissonance when I come back and I talk to people. Like, I would feel like, oh, why do you think like this? But then I used to think like this. So, like, the environment shapes, like, like, a way a researcher thinks. The taste is very important. Sometimes I try to communicate this to people, and then maybe I come across as a snob.

[01:36:16] To, to, to, like, the local community here, right? But, like, It's, it's just that there's like, maybe there's so much dense information that I want to bring back, but like, there's no like receptive, fast way to like, like transfer, like all the, the like, like transfer all the, the things that I've learned. Yeah.

[01:36:35] Also a big culture shock. 'cause I was in brain in the Singapore office for a while and I reporting to You were the only

**Swyx** [01:36:50] brain

**Yi Tay** [01:36:50] person Yeah. Yeah. Brain in Singapore. And then I had, like, I took on an intern from actually. And the, the research like vibes and the thing was so much of a conflict for me.

[01:36:50] That it was almost like my body was rejecting it, you know? Mm-Hmm. . But this, this person, so like, grew, grew and became, I'm happy with how this person grew with, from, from my mentorship. So he's now in a way better situation. But I would say that like a lot of people in the, in, in universities here are like, not like a bit like, like they, ignorance is blis, right?

[01:37:07] Maybe sometimes . So, well, no.

**Swyx** [01:37:26] It's exposure. I didn't know any better myself until I went to the U. S. for college and then, yeah, my world was expanded and it's a little bit of a Pandora's box because once you've tasted that, you're never happy. Yeah, yeah, yeah. You know?

## [01:37:42] Building Silicon Valley outside Silicon Valley

**Swyx** [01:37:26] So, okay, last question would be, just a sort of Singapore question.

[01:37:26] So, I'd like to know, Be visible, visibly non American, covering the AI scene, because it's very US centric. Every non American I talk to always wants to be like, How can we build Silicon Valley in my city, you know? My country, my city, whatever, that is not Silicon Valley. I feel like you have Basically, just kind of like me, you kind of operate in the US circles, but you just don't live there.

[01:37:46] Do you have any advice for like, if Singapore, okay, so I'm wearing a red shirt today. This is the official Singapore government sort of community group that is trying to guide Singapore AI policy. If we want a hundred more ITAs to come out, what should governments be doing? What should communities, ecosystems should be doing?

**Yi Tay** [01:38:08] So I actually think that like, Sometimes, like, not doing too much is maybe less is more, maybe? I don't think there's actually much the government can do to influence. Like this kind of thing is like a natural, like an organic natural thing, right? The worst thing to do is probably like to create, like, like create a lot of artificial things that like Exchange programs?

[01:38:08] Okay. I mean, Singapore used to have a lot of exchange programs. Like they send people to, to, I mean, just talking about AI specifically, right? I think that, for example, like sometimes like trying to do too much or like moving in the right, wrong direction is just better than not moving at all. Especially if you, if you accelerate in the wrong direction, you actually get into a worse situation.

[01:38:47] Sure. So I think it's very dangerous to move in a bad direction. I think respect your talent more. Maybe the government should just respect their talent more. And I don't know whether this is too much of a No, no, no, no. But maybe not moving in a wrong direction is, to me, is a Already a very good thing.

**Swyx** [01:39:02] Funding, for startups, incubation, holding academic conferences, I think iClear next year is going to be in Singapore, so people come here and get exposed to it.

[01:39:02] But like, I don't know, it's just very interesting. Like, everyone wants to build up AI expertise within their own country, and like, there's a massive brain drain to the US. I'm part of that. I live there. I feel guilty. I don't see any other way around it. It's such a huge problem. I also do think that there is, like, cultural hegemony, let's call it, like, US values basically being asserted on the whole world, right?

[01:39:30] Because we decide our LHF on these models and now you shall use all our models. And it's just troubling for, like, national sovereignty should be AI sovereignty and I don't know how to achieve it for people. It's very scary.

**Yi Tay** [01:39:53] Okay, that's a lot to unpack.

**Swyx** [01:39:53] Yeah, this is not technical, but I was just saying, you know, curious.

[01:39:53] We can make this the ending conversation, which is, I think you're an inspiration to a lot of other people who want to follow your career path, and, you know, I'm really glad that we got the chance to, like, walk through your career a bit. Yeah, I'm sure this is just the start, so.

[01:40:11] Hopefully there's more to come and I want to inspire more of you. Yeah. Yeah. Sounds, sounds good. So I'm just glad that you shared it with us today.

## [01:40:29] Tech in Asia Meetup

**AI Charlie** [01:40:23] As a special coda to this conversation, we were invited to join the Technasia meetup featuring Yi by managing editor Terence Li. Terence asked a similar question on how other countries can create conditions for top AI labs to spring up outside of Silicon Valley.

**Yi Tay** [01:40:23] So, like, where do you see Singapore playing a role in AI? So, like, how, how, how, how would you Oh, okay, right. I got a practical one. Okay. I got a practical one that is actually actionable. I feel like one thing that people don't get, like, like, the advice, that practical advice, like, that is that, like, the era of, like, people who talk versus people who do, like, the people who talk is, like, gone, right?

[01:40:23] So like it's no, it's no longer about like, ah, I have a team, I have like 10 interns from, from Southeast Asia or like the region and then they're going to do this, do this, do this, do this for me, right? So I think one thing that senior people in any government, right, may not get, right, is that the world has shifted into this paradigm where senior ICs, ICs as individual contributors, right, are actually making the most impact in AI, right?

[01:41:08] So. In GDM and in OpenAI, I mean, in Frontier Labs, they're all very driven by individual contributors and not actually this is not even related, this is like, like, I'm talking about, like, This is advice I give, but it's actually general, like, it's a very general thing, so multi purpose, basically. It's not AI specific?

[01:41:37] No, it's also, it's AI, it's very AI specific, because The, the, the level, the difficulty of making impact and making breakthrough has started to become Like, it's no longer about, like, it's not like software engineering where, where, where it's, it's like, you know, I think AI is a little bit, like, harder, like and then, like it's mostly about, like, getting very senior people who are hands on and have a lot of, like, experience rather than, like, management style people that, like, try to, like, think they know what to do.

[01:41:54] They're doing but they actually don't. So I think, I, I mean, I, I'm not going to, like, say, like, names, obviously, right? But, like, I, I mean, I, I meet a lot of, like, people like this like, in general. I mean, not only in Singapore, but, like, right? But AI has shifted quite a lot into this IC driven paradigm where the people making impact are the people who are, like, on the ground fighting the war, right?

[01:42:26] So it's no longer about, like, I have 10 interns, 20 interns, 100 interns, you do this, you do this, you do this, I just take meetings, right? No, right? The senior person writes code. Everybody writes code. Nobody should not write code, right? And then everybody, so I think this is, okay, this is a bit extreme, but, but, but, this is a bit on the extreme side, but I think from people, like, I just the advice is just, like, maybe, like, just take 20 percent of what I say.

[01:42:51] And incorporating, right, right, so instead of, like, you know, like, if you, if you, if you, for example, hypothetical, hypothetical situation, right, say you want, you want to organize, like, an AI conference in Singapore, right, and then you want to make it, like, like, like a, you want to show Singapore as, like, the AI hub in the world, right, maybe you don't invite, like, policy people and, like, you don't invite, like, policy people to come and talk about, ah, AI safety, AI safety, AI safety, right, You invite people who, like, actually know their stuff, right?

[01:43:18] And then, if you organize a conference and then, like, hundred people, like, go there and then they feel very productive and everything, but, like, the problem is that, like, Singapore doesn't have, like, like, people who really can do it, you know? Right? So, I mean, I've, through the grapevines, I mean, I hear about, you know, people, like, fighting for territory here and there.

[01:43:46] I mean, this is what I hear, right? I don't want to hear this, but I hear this somehow, right? And then sometimes I just ask them, like, who's actually going to do it? Right, who's going to do it, right? The model is not going to train itself, right, unless we have AGI, right? So, yeah, I mean understand that, like, times have changed.

[01:44:09] It's no longer about, like, it's no longer about, like, you know, like, Oh, I'm very senior, very senior, very senior. Okay, okay, okay, can you code, right? That's the question, right? I think that's, that's, like, the

[01:44:27] Well said. Spicy or not spicy? Spicy already. Okay, okay. We are like, Cocoa is in Baya, raise the cocoa age in Baya already to the maximum. Yeah, almost there. Okay questions, anyone?

**AI Charlie** [01:44:39] Indeed, questions are very welcome. Head over to the latent space substack to leave a question, or tweet at @YiTayML directly with your feedback.
