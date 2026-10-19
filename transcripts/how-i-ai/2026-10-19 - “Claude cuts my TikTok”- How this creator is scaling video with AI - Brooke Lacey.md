---
podcast: "how-i-ai"
podcast_title: "How I AI"
title: "“Claude cuts my TikTok”: How this creator is scaling video with AI | Brooke Lacey"
date: 2026-10-19
url: "https://podcasters.spotify.com/pod/show/pen-name/episodes/Claude-cuts-my-TikTok-How-this-creator-is-scaling-video-with-AI--Brooke-Lacey-e3qgmsh"
guid: "7fd66152-3bb1-4bc7-bf5d-1bcb3267cf87"
host: "Claire Vo"
guests: ["Brooke Lacey"]
format: "interview"
level: 2
length: "00:36:05"
categories: ["design", "marketing", "agents"]
featured: ["Claude", "Claude Code"]
mentioned: []
transcript_source: "azure-asr"
transcribed_by: "MAI-Transcribe-2"
---

# “Claude cuts my TikTok”: How this creator is scaling video with AI | Brooke Lacey

**Brooke Lacey** [00:00:00] No timeline, no project file, no editor.

**Claire Vo** [00:00:02] You figured out a way to use Claude Code to encode editing that really fits the form, which is short form content.

**Brooke Lacey** [00:00:09] The file's in the computer, it doesn't upload anywhere. The only thing that's happening is the instructions are being pulled, and it's doing all of the things. It's just running the computer, and not only that, but it's listening and goes, oh, I just heard you say cut that out. And then it also was like, you repeated this a couple of times, and I took the one that was the best cadence. And I was like, what?

**Claire Vo** [00:00:34] And what just happened is Claude descended upon our videos and cut them. It just pulled up the raw video. There was a really well clipped vertical short form video, perfect to TikTok cadence, and you did it with no hands.

**Brooke Lacey** [00:00:49] So literally, I do everything in the terminal. I like it better. It just has way more access to everything. So let's say, okay, my dude, I'm ready to show the audience the magic. And look, no hands. This is probably the 15th or 16th time in the last 6 months that I literally like fell to the floor. What just happened?

**Claire Vo** [00:01:16] Welcome back to How I AI. I'm Claire Vo, product leader and AI obsessive, here on a mission to help you build better with these new tools. Today we have Brooke Lacey, and she is going to walk us through her Claude Code for video editing flow. She has over 200,000 followers on TikTok, and she's figured out how to get Claude to edit her videos to be funny and have the right jump cuts, create scripts for new content, and generally understand her cadence, her vibe, and her style. Let's get to it.

[00:02:17] Brooke, thanks for joining How I AI.

**Brooke Lacey** [00:02:35] I'm so excited. I think that you know, but I would like your audience to know that I'm like the biggest fangirl. I really love what you do, and I'm just so excited to be here.

**Claire Vo** [00:02:46] Well, I love what you do, and so we're going to talk about why I got you on this podcast, which is you have a Claude Code video editing, social empire building stack that I need to steal, because before we got on, we were talking about how a little while ago I was like on my way to being a big deal on TikTok, and then a girl gets tired, like a girl gets tired.

**Brooke Lacey** [00:03:13] Tell me about it.

**Claire Vo** [00:03:14] Of all the short form.

**Brooke Lacey** [00:03:15] Yes.

**Claire Vo** [00:03:17] And I loved when I saw you posting about your system, about how Claude Code helps you produce not just like slop content, but actually really great high quality short form, which is its own special little art. And so dive us into what were you trying to solve, what were you trying to do, and how did you figure out that Claude was going to help you on the way?

**Brooke Lacey** [00:03:37] Let me just start this, like video, short form video and like little live stream stuff has not, I've been doing that for a long time, like before Facebook even had, you know, video stuff, I was on the news, like video content is not new for me. The short form was kind of a big deal when I got on TikTok, like 2020, and the trick there is those jump cuts. They're very difficult. I do a lot of funny stuff. I was known for ogling shirtless lumberjacks and like doing some funny stuff and then also, you know, teaching tech. But it's not funny unless you are jumped at the very exact moment. And let me tell you, that is tedious. I tried teaching video editors, like, how to do it and how I wanted it, and it just never, it never worked the way I needed it to. Like, they got to be the, you know, the facial expressions. This is actually how I talk in real life, and you got to, like, you know, cut it correctly.

[00:04:38] So I've just always done it myself, and it would take hours out of my day just to make one video. Even though my videos on TikTok, if, you know, we were talking about earlier, if you go look at the- it's just my face, the- my entire TikTok feed is my face. Uh, you're welcome for people, just so you know. It's a rabbit hole, but also you're welcome. Um, and even though there's some videos that I'm like literally just sitting in my car, no makeup on, and have, you know, hundreds of thousands of views, you still have to get it correct so that it even looks natural. So all that being said, I had kind of stopped posting for the last year and was like, I'm obsessed with Twitter. I had a viral video, this Women in Web 3 panel video, which also goes with Women in Tech, like it's the most absurd thing to be like, be on a panel to talk about being a woman in tech on a panel, and you're like, what?

[00:05:39] So that particular video was about a minute and 5 seconds, and my friends were like, it's not funny. So I cut it to about 55 seconds and had those jump cuts really precise, and that's what was funny. So, and it was a two person, so I do some videos are two person. That takes forever. that being said, so now I'm doing all of this other, I'm not doing like videos for other brands. I have my own products. I need to do my own videos because what do you know, UGC content doesn't do as well as this face. So I have to do all the videos for the app that I built, that took off that I didn't even like realize was going to take off. So I needed, I needed long form to then be able to upload and cut up. So I went outside. I thought for some reason being outside would be better light. It was not. I probably did 25 to 30 minutes of just, you know, I didn't, it was just all the whole thing, didn't cut it up, didn't stop the video, it was just all of it, and then I'd be like, ah, no, cut that out, meaning I was saying it to me.

[00:06:51] And then I came in and was like, all right, let's just fuck around and find out. So I was like, okay, I'm a new Mac user. I used to just be a PC user. I'm like, ah, I got to get this video up into Google and then, you know, download it, and thank God for AirDrop. So I'm just like, AirDrop to the computer, which I think is silly being a tech person, not having known like we should, you know, I should be a Mac person, but I just never was. So that was cool for me. And then it just was on the computer, and I go into Claude Code and was like, let's see what you got, my dude, and said, and it just loaded. Okay, so TLDR is that it just used the boring tools that are already on our computers. FFmpeg, Whisper, Python, like it didn't upload the video anywhere. It's just, the files are in the computer. If I could like get the GIF of Zoolander, I say it all the time, like the files in the computer, it doesn't upload anywhere.

[00:07:54] The only thing that's happening is the instructions are being pulled, and it's doing all of the things. It's just running the computer, the files in the computer, and all of a sudden it's like pop, and then it opens the video, and I'm like, what? And then not only that, but it's listening and goes, oh, I just heard you say cut that out. And then it also was like, you repeated this a couple of times, and I took the one that was the best cadence, and I was like, what? What did you do? And I mean, sat back, this is probably the 15th or 16th time in the last 6 months that I literally like fell to the floor. Like, I'm so dramatic anyway, but I was like, what just happened? Like, what?

**Claire Vo** [00:08:44] And what just happened is Claude descended upon our videos

**Brooke Lacey** [00:08:48] No.

**Claire Vo** [00:08:48] and cut them. So let's show it because I have been doing this a little bit, but I think you have a much better system than me, so I'm just going to sit here and learn it. So show us.

**Brooke Lacey** [00:08:57] And again, it's only going to be fun because of the way I'm talking about it, because it's really, really frigging boring. Like, it's just boring, but of course you and I think it's amazing, and hopefully your audience too, but yeah. Yes.

**Claire Vo** [00:09:09] This is the How I AI vibe. We will make your Markdown and Python files feel like the most exciting thing you have seen in a few years. So.

**Brooke Lacey** [00:09:17] Your life is about to get so much better, y'all. Okay. I love you. Okay.

**Claire Vo** [00:09:24] All right, here we go. So how does it work?

**Brooke Lacey** [00:09:27] Okay, so literally I do everything in the terminal. I have for a long time. I like it better. It just has way more access to everything, in my opinion. So let's say, okay, my dude, I'm ready to show the audience the magic. Go again.

**Claire Vo** [00:09:51] And did you pre-populate this with a skill or with a prompt?

**Brooke Lacey** [00:09:54] Oh, and look, no hands. Okay, so this one is the, this one is like the non-edited. I'm so dumb. Sorry. Okay, you can like

**Claire Vo** [00:10:09] This is what it's like to be a creator.

**Brooke Lacey** [00:10:11] Everyone at work talks about AI as if you're already supposed to know how to use it, and you just nod along, smile and nod, boys. Everyone at work talks about AI as if you're already supposed to know how to use it. It's an app I built called Jayla. The first three are free. It's jayla.app. I'll see you in there.

**Claire Vo** [00:10:27] Wait, quick pause. Okay, so for people that are listening, not watching, she said, okay, my dude, let's go. I'm presuming that called some sort of skill on the back, and maybe you can walk us through exactly how the prompt works. It just pulled up the raw video.

**Brooke Lacey** [00:10:41] Yeah.

**Claire Vo** [00:10:42] And then approximately 4 seconds later, there was a really well clipped vertical short form video with captions, with jump cuts, with a little zoom when you made a funny face, perfect TikTok cadence, and you did it with no hands. Okay, so let's look at what it did. You want to walk us through?

**Brooke Lacey** [00:11:06] Yeah, he, I said, walk us through what you're doing. You're live online, my guy. And it said one phone take, which is what I was telling you before, was actually the one that I showed you, let's just see, this one right here, if you see my mouse, that was the, the rough cut, and I was in my co-work space, which, I love because you can get all kinds of different backgrounds. I liked this because it had this, side wall that he could put. Well, I thought me, I thought, oh, I can put, like, graphics or whatever, and filmed it with my phone, airdropped it to the, the MacBook, got myself a new fancy MacBook, and then this is what happened. And so he's telling us one phone take, five minutes of me talking, went in on the left. Here's what the chain did in the 15 seconds it ran. Find the speech. So silence detection marks where she's talking. Word timing from Whisper sharpens each edge because neither alone can place a cut cleanly.

[00:12:09] So it, the word timing from the tool whisper sharpens each edge. So it ha- like I was telling you earlier, off camera, for your audience, the, it has to hit right after that word ends, right? You, we don't think about that when we're talking, like right there, the G that it talking,

**Claire Vo** [00:12:33] Yeah.

**Brooke Lacey** [00:12:34] like the sound ends before you think it does. and then it tracked my face, so every frame, it's just like taking a picture every frame, just like film. So the crop follows, follows her, follows me, and each cut gets a shot size, wide, mid, and close, because I was asking it to do all the video sizes.

**Claire Vo** [00:12:55] This is so smart.

**Brooke Lacey** [00:12:56] Yeah. Then place the cuts, so 8 of them picked from its own TSV file. Each row is a start, an end, a shot size, which I could show you that file, but it's literally just cut, you know,

**Claire Vo** [00:13:07] Yeah.

**Brooke Lacey** [00:13:07] it's just a folder, or it's just a, yeah. it's got, every row has a start, an end, a shot size, a label. That file is the whole edit. So the edit... in video editing, I didn't actually know this, but I was telling my friend, there's a thing called the edit is text, and that just means that, like, you can type it out and it'll edit. It, Claude kept telling me that, and I was like, okay, so the file is the whole edit. So drop in the app screens. I literally just said, go find the, by the way, my app is not called Jayla anymore, it's called Zosia. I had to rename it, so you'll see the old name on there, but I went and said, find my branding info and graphics, put together a graphic to, and the app screen, take a screenshot, open up the simulator, take a screenshot of the app, and use that to put into this video.

[00:14:10] So 40 of the 441 frames, that's just blowing my mind, carry a screen of the app at the moments the cut list says, so as I'm saying it, it pops up cards on the wall beside her. So her right edge is measured per cut off the rendered footage. So the cards sit in that real empty wall sized to it, and then it does captions, one word at a time, 57 words, white with a black outline, because I'm just like, hey, do white with a black outline, each held until the next arrives. I didn't tell it to do that. He decided that those captions need, people don't realize that's how captions are generated, is that the word has to stay there until the next sentence. So he knew not to go further than that. And then check sync. So 441 frames at 30 FPS, audio and video 0 milliseconds apart.

[00:15:11] The finished 15 second vertical ad is playing on the right. No timeline, no project file, no editor, and because the whole edit is a text file, the same command makes the 30 and 60 and the landscape versions from the same take.

**Claire Vo** [00:15:59] Okay, just, I'm like, dear Claude, make a funny video, and it doesn't work because of exactly what you're talking about. I also just have to empathize as a TikTok girly. Do you know how often I'm sitting in CapCut being like, cut it right, like right here, like right at this, because I know what funny sounds like. But just a couple things that I want people to know is you've actually really structured what a good short form edit looks like. Jump cuts between times, clip to words. I love

**Brooke Lacey** [00:16:33] Yes.

**Claire Vo** [00:16:33] this idea of three frames. I was like, just zoom

**Brooke Lacey** [00:16:36] Yep.

**Claire Vo** [00:16:36] in when it's funny, but I like this idea of like frame

**Brooke Lacey** [00:16:39] You did.

**Claire Vo** [00:16:39] wide and close cuts

**Brooke Lacey** [00:16:41] Yep.

**Claire Vo** [00:16:41] because if you all don't know, you got to do like this when you're on TikTok.

**Brooke Lacey** [00:16:46] Yeah.

**Claire Vo** [00:16:46] Um, and then, uh, the auto captions, and what people don't understand is that can all run with existing tools and files on your computer really well.

**Brooke Lacey** [00:16:57] Yes.

**Claire Vo** [00:16:58] But I have to imagine this took some zhuzhing to get right

**Brooke Lacey** [00:17:05] Yes.

**Claire Vo** [00:17:05] because I think I'm a smart cookie, and I have not nailed it.

**Brooke Lacey** [00:17:08] Yes.

**Claire Vo** [00:17:08] So show us how you used your existing TikTok corpus to actually

**Brooke Lacey** [00:17:12] Yes.

**Claire Vo** [00:17:12] like, learn how to do this.

**Brooke Lacey** [00:17:16] And I do, I gotta tell your audience watching, listening, I know I said it before, but video content is not new to me. So I'm not a video editor. It was just by way of I had to do it because I was starting to do content, and I realized how important social media content is, even for old people. so I had to learn. This is not just something that I just like, oh, I picked up, you know, you do have to have some capacity, just like, you know, being a developer just make this just makes you a better developer. So you do have to learn like the basics of video editing, just so everyone knows that like I've been doing short form for a really long time, so I was able to orchestrate Claude the way that I would actually do it, if that makes sense. So the thing with TikTok, first of all, on a technical level, is that their algorithm, their back-end software, their back-end whatever, is so precise that you can't scrape it. You can't have an AI, even with their API, just scraping it for data or like doing multiple downloads, doesn't like it.

[00:18:23] But if you're already logged in, which I'll show you this since I'm logged in, then I can go down here and say, okay, let's show them the TikTok corpus. I am logged in and use the video in the Google Drive like you did before so that you can read the comments and use those comments to put together new content ideas based on what they said. So which one did it pull? I think it pulled this one. Yeah, so this was the first video I did, so this was the first video I did, after I created the app, the Jayla app, which is a free app to learn AI. At first I was calling it the Duolingo of learning AI, but that's silly, but that's what I thought in my head.

[00:19:25] And so, again, it's a free app, and I was so excited that, like, I got it in the app store and all that. But what was great, and I'm going to I've been in tech for 25 years, and I've never been this scared for people. An AI founder just told 40 million people on Twitter. Okay, so what I'm saying in the video is that Andre Karpathy quote that it was like, you know, he doesn't code anymore, he just like doesn't even know how to keep up. That was actually one of the times I thought to myself, like, yeah, our nervous systems like don't know how to keep up with all of this stuff. So, okay, I said to Claude, go and look at this particular video, which, by the way, I had to download on my phone and upload to the Google Drive because he can't download it. Well, no one can download it from Chrome, but that way he could read it and see it.

**Claire Vo** [00:20:20] Okay, yeah, so just to walk people through if they're not watching, I think what is happening here is you went on your phone and you downloaded all your TikyToky videos, and you put them in Google Drive, and you said, "Here are all my TikTok videos in a Google Drive. That way Claude Code can access Google Drive and actually pull down any one video." Then separately, you said, "TikTok's open.

**Brooke Lacey** [00:20:47] Yep.

**Claire Vo** [00:20:48] Go look at TikTok and read the comments for this particular video.

**Brooke Lacey** [00:20:53] Yes.

**Claire Vo** [00:20:53] Um, pair it with the download of the video that's up in Google Drive.

**Brooke Lacey** [00:20:58] Yep.

**Claire Vo** [00:20:59] And then pull it together and say, based on how this did, the content in this video and the comments.

**Brooke Lacey** [00:21:06] Yes.

**Claire Vo** [00:21:06] Give me new stuff.

**Brooke Lacey** [00:21:08] Correct.

**Claire Vo** [00:21:08] To record.

**Brooke Lacey** [00:21:09] Because

**Claire Vo** [00:21:09] Is that right?

**Brooke Lacey** [00:21:09] This particular one has all these comments, right?

**Claire Vo** [00:21:12] Yep.

**Brooke Lacey** [00:21:13] And yep, and it says like, I wonder if hospitals are going to start using AI for the billing and coding. Okay, cool. well, on the phone, you can reply with a video. And then, you know, see, it like sounds like CEOs can be replaced by AI. AI will replace someone with no skill. I mean, it just goes on and on and on. So the prompt that's happening with Claude Code is go and read those. I have done this before, so it's probably looking for the output that we had from before, from a few months ago when I actually did this, but he's got the post IDs, opening the pin post with the most comments and scraping its comment thread. And it does call Claude and Chrome. Sometimes I have to explain that, no, you need to do this headless, but it doesn't really matter. It's getting the information somewhere. And then it will, the coolest thing for me was that, as people can see, it's my facial expressions, you know, I talk with my hands, there's pauses, everybody knows that that's how videos work, but to train an AI to understand that, in the first part of the video, I say, I've been in tech for 25 years and I've never been more scared for people.

[00:22:31] And that little laugh right there where I'm like scared for people. I had to tell Claude, did you hear the cadence in my voice? Because that is how a hook works for me.

**Claire Vo** [00:22:45] Yep.

**Brooke Lacey** [00:22:45] Is that I'm trying to get people's attention that way, figure that out. And it did, he did.

**Claire Vo** [00:22:52] So, just to kind of like repeat for people, in addition to downloading these videos, and so they can be referenced and combined with comments to come out videos, you actually taught Claude to understand, you know, people ask me all the time, like, how do I get Claude to write emails like me? This is like that on max mode.

**Brooke Lacey** [00:23:12] Yes.

**Claire Vo** [00:23:13] It's like, how do you get Claude to encode my charming self live into something that it can help me replicate? How do I do hooks? How do I do my cadence? What are my jokes like? Where do I do cuts? how do I tell a story? How do I, you know, create a peak in a story, all that kind of stuff? And then it's using all that knowledge not only to make your cuts better, but also give you scripts.

**Brooke Lacey** [00:23:41] Correct, which I just brought up on the screen. And this was, I, you know, not to get into the whole, whole story, but there's a style of video that I do, WTF even is, and I was doing it for some complex, like, blockchain terminology because that's already complex, just like the words that are in that industry. And so it made sense where I was doing the two persons, so I would film one and then film the other side so that I'm talking to myself, but the two people are talking to each other. and the one person would say, like, WTF even is blockchain or Ethereum or whatever. And then the other person's like, gives this long, complex, well, it's the, you know, ledger that blah, blah, blah, blah, very complex. And then the other person is me, with the facial expressions, like, what? Like, what are you talking about? That is not something you can script, and but the words back and forth need to be a certain way for it to be absurdity and then the like complexity, like it has to go back and forth.

[00:24:55] So I still haven't really trained Claude in like that particular piece, but we're getting there. And obviously it can't, I mean, obviously my facial expressions are my facial expressions, but I truly believe that, like, we're going to be reality dealers at some point because people are going to know that there's no way that you can create an avatar of Brooke Lacey with the facial expressions. Maybe you can in the future, but

**Claire Vo** [00:25:19] I mean, please, please like and subscribe to my create your digital avatar with Gemini episode, where I created very hilarious, uh,

**Brooke Lacey** [00:25:29] Yes.

**Claire Vo** [00:25:29] tra- trad wife AI versions of myself

**Brooke Lacey** [00:25:31] I love them.

**Claire Vo** [00:25:31] and do videos.

**Brooke Lacey** [00:25:32] I love them so much.

**Claire Vo** [00:25:33] So never say never, but

**Brooke Lacey** [00:25:34] No, you're right.

**Claire Vo** [00:25:35] I get it. Okay.

**Brooke Lacey** [00:25:35] You're right.

**Claire Vo** [00:25:36] All right, zooming way back. Let's just see, okay, um, video creation is not new to you. You figured out a way to use Claude Code to encode editing that really fits the form, which is short form comment content. You, uh, had to do a little human in the loop in terms of downloading your full TikTok corpus to a cloud location, which was Google Drive. But once you had that, you were able to do two things. You were able to kind of like learn your style, but then you also used that like style analysis to do a couple things. One, mine comments for new content. Two, create scripts for that new content. And then three, refine your editing, your Claude editor to make that short form content better. And now, how often are you posting?

**Brooke Lacey** [00:26:26] Okay, so don't be mad, but I don't really have to post that often to still have a really good engaged audience. I did the work. I put in the work for quite a few years, and a lot of my content still gets kind of

**Claire Vo** [00:26:40] Mm-hmm.

**Brooke Lacey** [00:26:42] reposted. So I don't have to post very often because, I think once you have done the work over, you know, a number of years and you do get to the hundreds of thousands of followers, your stuff just kind of keeps getting regurgitated. And, I would say like once a week I'm posting. What I think the next step for me, because I'm really good live, is that I'm going to do more live streaming, and I just don't think there's a lot of people in this space doing that for this particular thing, like what we're talking about, and then going through and like showing how our apps work, kind of DevRel stuff, but live. And so, yeah, I don't have to post that often. And right now I'm building videos for ads right now. Like, I'm going to try to do some, just figure out if TikTok ads work for my products. We'll see. Just kind of throwing stuff at the wall to see what sticks, but that's the video work I'm doing right now.

[00:27:42] And I think I'm telling Claude, hey, this is an ad, and it's like, oh, okay, let's figure this out in terms of it's not the same as the other stuff you were doing. It's more of a, you know, however ads work. I don't even know.

**Claire Vo** [00:27:56] You don't even know.

**Brooke Lacey** [00:27:56] I don't know how, I don't because I just do this.

**Claire Vo** [00:27:58] That's just Claude's business. Brooke, I love this as a

**Brooke Lacey** [00:28:03] Thanks.

**Claire Vo** [00:28:04] as a creator who does long form that like needs to get back in short form but just doesn't have the hours to do editing. I'm going to go steal all of this and you will see

**Brooke Lacey** [00:28:12] Do it.

**Claire Vo** [00:28:12] Chief product officer on TikTok rise the ranks yet again. We will get there.

**Brooke Lacey** [00:28:17] Yes.

**Claire Vo** [00:28:18] Let's do a couple lightning round questions and get you out of here. The first question is despite our charming faces, you and I are like, we're elders on TikTok. And I want

**Brooke Lacey** [00:28:30] I'm happily in my 50s. All right, just 50, just turned 50.

**Claire Vo** [00:28:33] And I'm happily on my way, so

**Brooke Lacey** [00:28:35] Perfect.

**Claire Vo** [00:28:35] Look at us two gals.

**Brooke Lacey** [00:28:37] That's right.

**Claire Vo** [00:28:38] I would like to make a plea for more experienced technologists to share their knowledge on these new platforms,

**Brooke Lacey** [00:28:47] Yes.

**Claire Vo** [00:28:47] pretty please.

**Brooke Lacey** [00:28:49] Yes.

**Claire Vo** [00:28:49] We need that combination of like wizened experience and

**Brooke Lacey** [00:28:53] Yes.

**Claire Vo** [00:28:53] YOLO energy, especially in AI. But you

**Brooke Lacey** [00:28:56] Yep.

**Claire Vo** [00:28:56] said something to me really interesting ahead of the show about being like a generation or 2 or 3 back

**Brooke Lacey** [00:29:03] Yeah.

**Claire Vo** [00:29:03] from this

**Brooke Lacey** [00:29:03] Yeah.

**Claire Vo** [00:29:04] moment.

**Brooke Lacey** [00:29:04] Yep.

**Claire Vo** [00:29:05] And how you kind of like, what your experience has been kind of going headfirst into AI and what that feels like.

**Brooke Lacey** [00:29:10] Yeah. Oh, I love this, and I wish we had hours and hours, and maybe you'll have me back, or maybe I'll just talk about live stream, and, you know, people can come and listen to me ramble, but I'm a very proud Gen Xer. It's a small but mighty generation. whenever my 21-year-old son calls me a boomer, like, I've disowned him. I'm not a boomer. And I think Gen X had this really incredible time period where we lived in our formative years, high school and college. So yes, my lovely millennial friends, you also grew up sort of like we did with like, you know, no cell phones and the plastic phone on the wall that like, you know, had a cord. And I feel like we were just so lucky that we got to see it go so quickly. And I'll tell you a really quick story. When I got into college, it was 1994 that I started college. I had already fallen in love with computers with Windows 3.1, and got into this computer science 101 class, and I remember the professor, it was one of those big auditorium classes because it was 101, it was intro to computer science.

[00:30:21] And this teacher, this professor was like jumping around the stage and was like, just wait, it's all going to happen so fast, it's going to happen so fast, and it's just going to go crazy. And we're all like, man, chill, like, what? And he was right. I mean, he was going nuts, and it was the next like two or three years that everything just exploded, and we got to see it. We got to like really experience it and watch from the very, very beginning as high school and college age, where we were like actually starting our careers, and it was just such an incredible time to be alive. So the year 2000, I worked on the Y2K bug, and a lot of people don't really know what that was, but it was kind of funny, changing, you know, two numbers to four, and everybody thought, you know, planes were going to fall from the sky and all of us were going to attack us. Right, right. We everyone's worried about AI. Well, back then we were worried about toasters, so you can imagine how different it is for me now with AI.

[00:31:27] But, yeah, I of course don't have quick answers. You can just take from that what you will, but I love being of this generation that is, I appreciate what technology does, and yes, there needs to be more people my age and older telling their stories about, you know, back in the day, you remember watching that movie where the women were actually computers? I can't remember the name of the movie.

**Claire Vo** [00:31:50] Mhm.

**Brooke Lacey** [00:31:51] But they're called computers because they were there sitting there computing, and there's just so many stories of like, you know, the, the tapes that had to be used, the big reels that, you know, hard drives that you couldn't drop because that was where it was. I don't know, there's so many cool stories, so like old people, listen up, go on TikTok.

**Claire Vo** [00:32:12] Well, and if you want a great episode, go back to one of our early How I AI episodes with John Blackman, 91-year-old vibe coder.

**Brooke Lacey** [00:32:21] That's right.

**Claire Vo** [00:32:21] Who has seen some things. And so, you know, I had the same experience as you, which is I have seen technology shift after technology shift, so this one happened, I was like, I see it.

**Brooke Lacey** [00:32:32] I'm in.

**Claire Vo** [00:32:33] I'm in, I'm in.

**Brooke Lacey** [00:32:35] I'm in.

**Claire Vo** [00:32:35] It is going to change my life like these previous ones have, and so

**Brooke Lacey** [00:32:39] Yes.

**Claire Vo** [00:32:39] um, jump on in, water's warm.

**Brooke Lacey** [00:32:41] Yeah, yeah, truly.

**Claire Vo** [00:32:43] Uh, okay, last question. You're

**Brooke Lacey** [00:32:44] Okay.

**Claire Vo** [00:32:45] you're, um, so lovely. I, I, and, and I like that Claude is a boy for you. That's

**Brooke Lacey** [00:32:51] Oh, yes.

**Claire Vo** [00:32:51] very nice.

**Brooke Lacey** [00:32:52] Oh, yes.

**Claire Vo** [00:32:52] Um, when he is a disappointment, when he's not doing what you want, how do you prompt him?

**Brooke Lacey** [00:32:59] Okay, so also a very long story, but I will keep it concise. The Grok bot person wrote an article the other day about their pee stack. I can't remember the name. It was like banana something or coconut. I don't remember her name, but, and I, sorry, this is me all the time. or it was Petunia or something, and I ran it against my OS. So what I built a while ago with my dear Claude is this lane operating system that is very complex. I do have an open source of it, but it is fairly complex, and it has memory lanes, it has like write restrictions and different things because I have multiple products within the company, and then the OS lane has its own memory.

[00:34:01] So the way that I prompt when it screws up is like, go back to the way that we started, understand those instructions, and then do it again. And there's status MD files, there's project pieces that every time I'm in that session, it should be following those, but then also the global. But it's this entire like operating system just for my business and my life, and there's always something to go reference. So it's kind of nice where I'm like, no, you did that, that doesn't sound right. go back and figure out where you messed up or where you didn't read. Why didn't you read that? Oh, you, okay, now you figured out why you didn't read it correctly on the session hook. Now go back and tell the main operating system spine that you messed up so that it can make the change globally.

**Claire Vo** [00:34:51] I love it. I love it. Brooke, this has been, I don't know if the audience can tell, we're having a good time.

**Brooke Lacey** [00:34:56] We're having a good time.

**Claire Vo** [00:34:56] We're having a good time today.

**Brooke Lacey** [00:34:57] I love you.

**Claire Vo** [00:34:57] This has been a good one.

**Brooke Lacey** [00:34:59] Yes.

**Claire Vo** [00:34:59] Where can we find you and how can we be helpful?

**Brooke Lacey** [00:35:03] I am Brooke J. Lacey on every platform. I've been around a long time. TikTok is definitely my biggest audience. There's a lot of funny stuff that hopefully makes you laugh. It all started in 2020 when everyone was home for COVID, and I just started making people laugh. I am a lot more on Twitter, and I have a really cool app called Zosia that I built, and it's just the, it's just learning AI, and you're kind of doing it on your phone, and it's free. So that would be awesome, if you did that, and really just reach out. Like, I have DMs are open, you know, I love talking to people, and I've got lots of stories. So you can find me everywhere, Brooke J. Lacey, and this has been such a pleasure. And I do travel quite a bit, so I'll be in San Francisco, I'll be in New York, I'm kind of all over the place, so I'm always up for a coffee.

**Claire Vo** [00:35:59] Amazing. Well, thank you for joining How I AI.

**Brooke Lacey** [00:36:02] Thank you for having me.

**Claire Vo** [00:36:05] Thanks so much for watching. If you enjoyed the show, please like and subscribe here on YouTube, or even better, leave us a comment with your thoughts. You can also find this podcast on Apple Podcasts, Spotify, or your favorite podcast app. Please consider leaving us a rating and review, which will help others find the show. You can see all our episodes and learn more about the show at howiaipod.com. See you next time.
