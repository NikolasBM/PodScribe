# Jev: 8 real use cases for the fastest, cheapest model I’ve ever used | John Lindquist — Transcript (2026-09-30)

https://podcasters.spotify.com/pod/show/pen-name/episodes/Jev-8-real-use-cases-for-the-fastest--cheapest-model-Ive-ever-used--John-Lindquist-e3pj45k · How I AI · Transcribed with MAI-Transcribe-2

<!-- guid: 0871a705-f488-49f6-9654-3df1b900a22d -->

<!-- metadata -->
Format: interview · Level: 2 · Length: ~00:45:35
Host: Claire Vo · Guests: John Lindquist
Categories: agents, model-strategy, coding, models
Featured: Jev, computer use
Also mentioned: Grok Bot, OpenAI Codex
<!-- /metadata -->

---

**Claire Vo** [00:00:00] In some ways, managers are really at risk. This concept of like org design and role design, you can put those skills to use when crafting your agents, which is why I am currently running, no joke, 40 Grok bots right now.

**John Lindquist** [00:00:13] Whenever you have constrained inputs that are interacting with apps, it's Jev is a good thing to reach for. This one is a favorite of mine because it represents like a workplace where you have multiple agents that could all have their own tasks and avoiding collisions so that they never end up on the same space. At each step, it's going to be able to control these different agents and make sure that they get to their specific task as quickly as possible and that they never collide or interfere with the other agents. This one's really fun to me because it's a presentation coach. I click the microphone, I'd start talking, I'd have a list of bullet points in either a podcast or something that I want to make sure I cover or an interview or anything. It listens through everything I say and then starts checking the boxes to make sure that I covered everything.

**Claire Vo** [00:00:56] This model, which is basically free and incredibly fast, allows you to do discovery over data in a way that feels like it's opening up my opportunities and allowing me to like look at things that I thought weren't high ROI before. Welcome back to How I AI. I'm Claire Vo, product leader and AI obsessive, here on a mission to help you build better with these new tools. Today I have repeat guest John Lindquist, who has done one of our most popular episodes to date on the podcast. And here he is joining us on Jev Week at How I AI to talk about our favorite new model and all the amazing product-facing use cases that he's discovered testing Jev from TypeSafe AI. Let's get to it. John, welcome back to How I AI. I have to say this is Jev week on How I AI, and the reason it's Jev week is a lot of models have come out in the past 7 days.

[00:01:58] You and I do a lot of AI things, and yet when we're DMing back and forth, we're talking about one thing and one thing only, which is Jev. So, folks who maybe listened to my episode earlier this week about why I'm hyped on Jev, I would love to hear why you're so excited. I'm looking up here, you have 23 demos we could probably look at, so you are going deep Jev as well. What about this model, this framework, this way of thinking about building has gotten you excited?

**John Lindquist** [00:02:31] Fast and free are both amazing, if you've ever been tired, sending a basic request to an LLM and waiting around for a bit just to have it like call a function, this is now essentially instant. And I think of all the time I've spent on this and the hundreds of demos I made, I think I've spent 73 cents on it. And I love the one quote someone said, I think I'm going to pass this inheritance of Jev on to my children once I die.

**Claire Vo** [00:03:01] Yeah, I like the one where it was like, TypeSafe- TypeSafe is really taking off. They have to have made double digits in revenue by now.

**John Lindquist** [00:03:08] Yes.

**Claire Vo** [00:03:09] So yes, fast and

**John Lindquist** [00:03:10] Yeah.

**Claire Vo** [00:03:11] free. I also have had that experience where it ran over, like, I don't know, 20,000 records, and it was like, "I have charged you 0.4 cents.

**John Lindquist** [00:03:21] Right. And- and it- it exposes those scenarios where I thought, like, I had 5 gigabytes of JSON. I'm like, I had never passed this into an LLM. I just ne- like, I don't have that budget, on and on. I'm like, let's see what happens. And it was 40 cents, you know, and I wasted it on a really stupid thing, like trying to organize this or whatever. But 5 gigabytes of JSON is a lot of text, and it went through and did the whole thing in probably a couple minutes.

**Claire Vo** [00:03:51] That's been my experience too, which is I'm looking at corpuses of data that I would never just dump into an LLM, both from a cost perspective and honestly from a time perspective. It's like this is not worth my time to even see if something's here. But then this model, which is basically free and incredibly fast, allows you to do discovery over data in a way that feels like it's opening up my opportunities and allowing me to like look at things that I thought weren't high ROI before.

**John Lindquist** [00:04:27] Yeah, absolutely same. It's just opening doors that weren't or closed before, yeah.

**Claire Vo** [00:04:32] So just quick reminder for folks, Jev is not like a the LLMs that you're used to and love. It does not output text. It outputs basically like decisions and scores and yes, no probabilities. And so you kind of put information in out in, and then you get out very structured, type safe, very structured, limited set of options. But the ways you can use this are almost unlimited. And so John's going to walk us through some of his favorite demos of how he's using it. And hopefully we'll get a combination of inspiration on where a real-time, fast, cheap model can build cool things, and a little insight of like, what else is around this? Because what I found is I see a lot of these like shiny demos on the timeline, and then you're like, you're hiding your, you know, your embeddings, and you're hiding like how this is actually working. And so I think if you can lift the veil for us on how some of this works and where it's Jev alone, where it's Jev plus, that would be awesome.

**John Lindquist** [00:05:30] Yeah, I would just, just to add to your definition of Jev, of it being type safe, I think of LLMs being unstructured to unstructured,

**Claire Vo** [00:05:39] Mhm.

**John Lindquist** [00:05:39] where you put text in, you get text out. And this one is similar, you put in unstructured sentences and data, but then you get structured data out. And the power there is it's humans talking to machines, and they're the scenarios where you have functions and APIs and everything set up, but I want to communicate with them using unstructured data. And, we're so used to chatbots, and it's just not a chatbot anymore. You need services, you need functions, you need things you want to throw data at first, but you can talk to it however you want, which is incredible.

**Claire Vo** [00:06:14] Yep. Well, let's talk about talking to it.

**John Lindquist** [00:06:17] All right, yeah. so let's go ahead and try this out right away. so traditional to-do app, we have a list of to-dos, and the fascinating thing here, which I'll try right away, is I'll just say something like, book dentist appointment, remove. Buy oat milk, complete. Review pull request, low priority. Now the speed there was all done through Jev. It does a few passes of looking through the text where it ensures that it lines up. If there's any like dictation mistakes and you say it doesn't get oat milk quite right, it'll go through and see, does this quite match up with something, or do I need to do a different, do I need to categorize this into something that exists, like a confidence score? Like, it's all a lot of confidence scores there. it matches it with the thing in the list, and then it matches it with the function that it's going to call, right, based on the way that the operation that you want to perform on top of that data.

[00:07:23] So it's multiple layers of analyze the dictation itself to see if that's like a valid dictation, then analyze if it matches up with the task, and then analyze if it matches up with the operation you want to perform on the task. And it can do that all live, and it even, while you're dictating, it classifies if you've spoken to a point where it can take an action. So as the words come in, it's like, is now a time where I can, where I have enough data to make a function call, where I can reliably keep on talking? Because you notice that entire time I was talking, I never paused, I never hit enter. It was able to classify, is this a moment where I have enough information to take action? So it's just showing all these pieces of Jev fitting together to give you this real time, like, give me kind of streaming data in, like unstructured streaming data in, and I'll start putting it in all the places it needs to go.

**Claire Vo** [00:08:17] I have a question for

**John Lindquist** [00:08:18] Which is

**Claire Vo** [00:08:19] for

**John Lindquist** [00:08:19] Yeah.

**Claire Vo** [00:08:19] folks that have just have no idea how to actually put this into place and want more of the tactics, which is, are those, you know, are those like sequential Jev calls? Are you like, yes, no, it's time to analyze, yes, no, it's, this is a good transcript, score, here's the top task that relates to it, and score, this is the top tool call that relates to it. You know, is this like, because people are trying, I'm sure trying to put in their mental model, like a tool call where you get all that structured data back, like, how have you set this up so people can kind of understand how they chain these Jev tools together?

**John Lindquist** [00:08:56] My mental model is, remember back when we used to write code by hand.

**Claire Vo** [00:09:00] I do remember.

**John Lindquist** [00:09:01] There is no conditions, if, if else, switch statements, all these things that were the moment of classification. And if you just think of a line by line program where things execute, you think of where do I need those conditions? And so as you're breaking the problem apart, whatever the thing is that you're building, just think of all the conditions, the if-else, the moments where it either needs to be put into this bucket or that bucket. And so as I was going through this, I built a lot of it backwards because I started with what I was building, marking the to-do as either done or removing it or adding a new one and such. And I'm like, oh wait, no, now I want the dictation to be able to select it. And so I just kind of built it backwards. And with- it was so easy with the Opus 5.5 recently just to kind of wing it and like s- take it different directions and go through scenarios and see- see the cases that- that were exposed, because I had that final idea of I just want to- if you've ever used a Siri or a Google Assistant or any of those, and you tried to manage, like, add to my to-do list, and they're all terrible.

[00:10:09] And like, how can I build, like, does Jev enable this to actually be good? And I think it does. Like, it's one of the most common things, like managing. You could integrate your calendar into this. You could integrate it because they're all behind function calls, right? Or MCPs or however you want to build it out. You could integrate anything with this and just have this top level dictation live inference running, and it's something anyone could build cheap and free, like it's

**Claire Vo** [00:10:36] Amazing.

**John Lindquist** [00:10:37] Amazing, yeah.

**Claire Vo** [00:10:38] Okay, so you and I both did live voice apps. Mine was much more emo, which was just talking to the screen and getting a color and an inspirational quote. Yours is much more practical, which maybe reflects our different personalities. let let's see what other use cases you have, and what I like about what you're showing us is, I talked a lot about like internal data analysis and clustering and all this stuff. You have such great inspiration for how you can use this inside products or to do things that were previously really tedious. So I'd love to see another one of your favorite demos.

**John Lindquist** [00:11:09] Yeah, let's dive in. So this one kind of breaks it down into its smallest pieces. if you think of a grocery store and if you think of, I have a function call like get cart, if we remember programming, and you type in something like what's in my cart, and that's how, if you think of classification of regular text to functions, like this is just demoing back if the previous demo didn't make enough sense, think of like plain English language mapped to a function name, and that's one of the core foundation foundational pieces of what Jev does. That's that demo. classifying documents sounds like kind of covered that. This one I think is incredible because if you've ever run a scenario in, I use Google Contacts, and often you put in the same contact twice, and you've probably gone through the process of like merging them together. very common scenario where you have messy data of someone typed in something wrong and they hit submit, and now you have two company entries in your database or whatever.

[00:12:14] This can go through and go through all of the records and kind of merge those records together. So let's click on that, and it can go through and say this one wants to merge. So Cedar Grove Office Products obviously matches with Cedar Grove Office. Ridgeway Data is Ridgeway Analytics, and it can go through and apply those merges for you by matching together and classifying, is this one close enough to that one? And again, it's huge data sets merged together in milliseconds.

**Claire Vo** [00:12:48] This is like my favorite use case of Jev, which is like pairwise comparison of a lot of data to create grouping and clusters. And so in the episode that I just did, we, I did that over PRs. I were like, were these PRs on the same product area or the same thing

**John Lindquist** [00:13:03] Yes.

**Claire Vo** [00:13:03] or the same theme? But you could do data reconciliation, I think is a really useful one. I went through recently and I had like 2,000 passwords in my 1Password. And you know how like whenever you do your 1Password, it's like update, save, make new, and I'm just like all over the place, had a whole bunch of different ones, and like I was just thinking how much faster it would have been to use Jev and some of the metadata to just pair those up and merge them. Um,

**John Lindquist** [00:13:29] Absolutely.

**Claire Vo** [00:13:30] And again, it's not like you're giving an example where there's like 6, you know, things. You're talking about when you have 60,000 or 600,000

**John Lindquist** [00:13:39] Yep.

**Claire Vo** [00:13:39] things. Those pairs feel very expensive until you use

**John Lindquist** [00:13:43] Mhm.

**Claire Vo** [00:13:44] something like this.

**John Lindquist** [00:13:45] And something we haven't shown is that there is a confidence score that comes back.

**Claire Vo** [00:13:49] Mhm.

**John Lindquist** [00:13:49] So if there is a North Star clinic and there's North- North Star clinic services and it's not- and they don't quite line up, like, if you want- you want them only to merge if you're, like, 99% or more confident, you can s- you can set those parameters in there. So that- that- that is a knob you can turn if- as you go through a few checks. And I think, like you mentioned before, is after you do this pass, you can send a smarter LLM against the result and say, we were, the data did look like this, please, either random sampling or the entire data set, ensure that this was done correctly. And then you can gain more and more confidence over time as you run more and more, large data runs.

**Claire Vo** [00:14:32] One other thing you can do on that, in addition to validating the data pairs, is you can describe them. And so what I've done is do the pairs and then run- it doesn't even have to be an expensive model, but say, like, we've decided these two are the same, explain to me why. And it can give a short kind of like, it's the same because they both say services and, you know, whatever it is. and so you can get sort of a quantitative matching and then a like qualitative explanation with two relatively cheap models once you've narrowed that down.

**John Lindquist** [00:15:06] Yeah, yeah, great stuff.

**Claire Vo** [00:15:08] Okay, great stuff. We are just psyched about. I was like,

**John Lindquist** [00:15:12] Yeah.

**Claire Vo** [00:15:12] I can watch all of these.

**John Lindquist** [00:15:14] Th- th- this one's fun. It's kind of hard to show off, but essentially, if you think of having, your entire application, and so you have go back, going back to the to-do list and say that's one part of your much larger app, you can build additional abstractions around that so that if on your landing page someone comes up and either has a command bar, like a command K, or other demos, or sorry, other parts, Omnibar, any place to put in text, and they start typing in the dictate or voice or something, they can't remember what the to-do app was called, and you notice this is to-do, to-do, and I typed in to-do. It's able to go in and match against the tool, and then you could type additional things where you'd say, go to the to-do app and then take this action, like I would know in my head, oh yeah, there was that pull request, and then take all the pull requests and mark those as low priority.

[00:16:19] And so if you think of this multi-step, multi-step classification where you can build your smallest tools and then build another abstraction of Jev around them where it can pick which of the smallest tools to use, this kind of goes back if you people have set up MCPs where there's abstractions around them, I think Executor and others where it picks which MCP to use. There's the tool itself, and then there's a layer where you're picking which tool to use, and you can build that as, as many layers of that as you want. That, that's what this is kind of talking about. It's, it's difficult to show off, but just imagine saying, go to the to app, do this, and yeah.

**Claire Vo** [00:16:59] What I would say is like Jev is a router is maybe like what's helpful.

**John Lindquist** [00:17:05] Jev is a router, love it.

**Claire Vo** [00:17:05] A very, very fast router. And so, you know, this use case you're saying like, as I have text, route to the right tool, and then if I can infer from the text the job to do in the tool, I might as well infer that and like route as far down the user journey as I can infer from these like structured options. Other practical use cases I'm seeing, a lot of people start to build these like Jev-powered coding harnesses where it's like, given the first input, let's route to the right model, let's pick the right tool, all this kind of stuff. And so you can imagine very fast configuration, very fast routing, very fast, like I don't just have to take the first step and then think and take the next step. I can actually just build the chain and then execute it. and so I think these decision models like Jev, if they remain fast and cheap, can be a new way to think about navigation of your

**John Lindquist** [00:18:02] Yes.

**Claire Vo** [00:18:02] user experience, whether that's a kind of like front-end experience or a dev tool or whatever it might be.

**John Lindquist** [00:18:09] Yeah, even search

**Claire Vo** [00:18:10] Yep.

**John Lindquist** [00:18:11] to a certain extent of, um, search for a long time has been, has had a lot of really expensive options out there, and I don't know how far you could push this into replacing certain search engines, but yeah.

**Claire Vo** [00:18:24] You know, I gave an example, when I did this, like, I had 4,000 YouTube comments, and I was trying to do live search through this, and I want to demystify some stuff for folks because it actually isn't super fast to, like, search over all of these results and say, like, yes, no, this is a good result and rank it, but you can, like, cluster, like, groups of, like, 30 or 50 or 60 and score them and rank them, and that is a much faster way to build quote unquote real time search with Jev. So, you know, for folks, again, I just want to like give people a little bit more specifics about what you're seeing on the timeline, which is you do have to think about how you're going to architect around Jev. It is fast, it is efficient, but it's not like completely latency free. And so you may need to go look around, see how people have done search, and then if you find one you like, go into GitHub, figure out how they actually made that surf search super performant, because I- I've seen a couple different strategies out there to how to do this.

**John Lindquist** [00:19:25] Yeah. And caching and all that stuff.

**Claire Vo** [00:19:28] All, all the s- all the caching. Yeah. It's easy when everything's locally cached and just you go over the

**John Lindquist** [00:19:34] Yeah.

**Claire Vo** [00:19:34] the full corpus.

**John Lindquist** [00:19:35] Yep.

**Claire Vo** [00:19:35] Let's talk about games, because this is something

**John Lindquist** [00:19:38] All right.

**Claire Vo** [00:19:39] I haven't covered yet, but I think is a really cool demonstration of some of the ideas inside Jev.

**John Lindquist** [00:19:47] Yeah, I built this one because I wanted to show off Jev versus a traditional model. I picked a free model on OpenRouter. This is like a low reasoning model. I think it's a Kimi or something, I'm not sure, but

**Claire Vo** [00:19:57] And for people that aren't watching, it's playing chess.

**John Lindquist** [00:20:01] Yes, this is playing a game of chess, and Jev are the white pieces, the LLM are the black pieces. And here, this is set so that Jev is able to think through all the possible moves, and then it ranks the highest three moves, and then it thinks through all the next possible moves there, and based on that two-step reasoning, picks the best next move. And so, kind of like routering, it's kind of like, spidering into the potential best moves, and then coming back to what the next best move would be. And it's still doing this in sub one second times and using AI and inference. Whereas if you pass the same data set to an LLM, the amount of reasoning it takes, this is playing blitz chess, so there's a one minute timer. Jev would be able to complete this entire game and beat it, and the LLMs would eventually get there.

[00:21:02] They'd be much more expensive, and they might not even perform better, because in scenarios like this where it's focused on routing and the next best thing to happen, the, like, the amount of data that you can crawl into and find the next best move can kind of balance out between these two.

**Claire Vo** [00:21:22] Mhm.

**John Lindquist** [00:21:22] Unless you're getting like really super high level, like creative chess where you're trying to stump someone by feinting certain moves or whatever, but I'm not it. I- I'm decent at chess, I can beat my kids. Perfect.

**Claire Vo** [00:21:35] For now.

**John Lindquist** [00:21:35] Sometimes. For now. And if you look at the, it has some benchmarks over here that Jev was 10 times faster in the average move, and it was 4 times cheaper. And this was a very, um, space money alphas on, uh, low reasoning, so with very, very tiny context windows.

**Claire Vo** [00:21:55] Yeah. What I think this demonstrates is, one, there are scenarios in which speed is a, is an advantage. Um, this is putting in the context of a game, but, um, it's very obvious how much. I mean, 10x faster is not incremental, and so it really does unlock this concept of real time. And I do think about going back to when I was a young product manager and did a lot of like conversion testing and growth work, and like speed did matter in a lot of user experiences, especially consumer on what won. And so I do think, we hear a lot on the coding side about model optimization from a cost perspective, but I think we're going to start to see like latency wars really heat up as well, which is like the faster the response, the more like more magic you can unlock that feels like an if else statement, the better.

[00:22:56] And so I think this is showing one where speed really matters. I think the other thing it's demonstrating is this like multi-step routing that we talked about, where you can think through turn one, turn two, turn three, and then because it's 10 times faster, you could apply another model on top at that point, a more intelligent model at that point, with kind of like a narrowed set of strategies and probably make a stronger decision faster.

**John Lindquist** [00:23:25] Right. And I think this also demonstrates the, again, to the concept of a router, there are a limited set of options in chess and other games.

**Claire Vo** [00:23:34] Yeah.

**John Lindquist** [00:23:35] There's a lot of options, but it's a limited set, and you can pick from the most likely set and narrow it down and optimize, you know, cost and everything. And data structures and your APIs are all the same. Like, they all have a limited set of things you can do, even though it might seem infinite to you because, you know, you never know what somebody's going to type or do in your application. this handles those, when you have those scenarios, it's time to look for a Jev first, I would say, whereas the LLMs are much more, I don't, I have no idea what I want the action to be, or I don't even know if I want it to take an action, or things where it's much more brainstorming and creative and finding, finding what you want to do. But once the actions are set and you have that limited scope, that's where a decision model can really excel, at least from what I've experienced so far.

**Claire Vo** [00:24:30] And I think this can demystify too some of the other kind of fun, eye-popping use cases that I have seen, like browser use, right? If you look

**John Lindquist** [00:24:40] Yes.

**Claire Vo** [00:24:41] like, at a- at a website, navigating it with a mouse feels like an infinite set of possibilities, right? You can, like, move it anywhere,

**John Lindquist** [00:24:48] Right.

**Claire Vo** [00:24:48] any pixel on the screen is where your mouse can go and click. But if you actually look at the DOM, there's probably, like, 10 clickable buttons on a

**John Lindquist** [00:24:55] Yes.

**Claire Vo** [00:24:56] page. And so, if you can very quickly say, "There's 10 clickable buttons on this page, which one do I click? Like, which one do I want to click?" That demystifies that concept of browser use through Jev, because you're really just taking a limited set of interactions available to us and our human brains. It looks like an infinite canvas of pixels, but to a model like this, it can just be a set of decisions. You know, I've also seen on gaming, Jev plays Tetris. It's because Tetris is 4 options of your shape, and then like 10 options left or right. That's all you- that's all you have. And so,

**John Lindquist** [00:25:33] Yep.

**Claire Vo** [00:25:33] um, you know, these like horizontal scroller games are just, you can like jump, you can walk, you can do, you know, any of those things. And so because these decisions can happen so fast, if the interaction of your app, even if it's a game that feels complex or a web app that feels complex, it probably can be distilled down to a dozen choices, and then you can

**John Lindquist** [00:25:54] Yeah.

**Claire Vo** [00:25:54] explore those choices, and because Jev is so fast, it almost feels instantaneous to chain those together.

**John Lindquist** [00:26:00] Yeah, it- I'd almost say in, like you mentioned in a game, in a platformer or in a 3D game, you might be thinking about all the things the character could do, but the input is actually the controller, and so the limited amount of options you have are all the buttons you could press, how you could press them in various ways, which is still a lot, but there's a very constrained input there, and whenever you have constrained inputs like, that are interacting with apps, it's Jev is a good thing to reach for. And to contrast the DOM example, if you think of taking a screenshot of a web page and saying what on the screenshot or what on our product or website might be confusing to a user. That's not a Jev thing. That's an LLM that can look through an image, it can compare it to all the images and products in the past. It can say, it can look through the layouts and the colors and the contrasts and all those sorts of things and come up with a discussion for you of here's some points that might be because the fonts are gnarly or whatever.

[00:27:08] And so that's where trying to delineate between the two, when to go which way.

**Claire Vo** [00:28:14] Okay, let's do one more. Do you have a last favorite one? I love you.

**John Lindquist** [00:28:28] Oh, yummy.

**Claire Vo** [00:28:29] I know there's so many.

**John Lindquist** [00:28:31] This will all run- this is super fast.

**Claire Vo** [00:28:33] Okay.

**John Lindquist** [00:28:34] On Wikipedia, there's every page leads to philosophy.

**Claire Vo** [00:28:38] Uh-huh.

**John Lindquist** [00:28:38] If you've ever done that. So you can put in any person in the world or any topic, so like LeBron James or whatever, run to philosophy. So you give it an end goal, and it looks the entire page, and it's going through the Wikipedia API and mapping that route.

**Claire Vo** [00:28:55] Oh, that's

**John Lindquist** [00:28:55] and finding from the person to philosophy. so mapping routes as well, like giving it a final destination, and it can crawl its way there. This one is a favorite of mine because it represents, if you think of a, like a workplace where you have multiple agents that could be doing multiple, they could all have their own tasks and avoiding collisions so that they never end up on the same space. so this is going to, the job brief is deliver the fragile blue bin to staging, bring medicine to the ward, and inspect the spill. Then you have three people that you can assign to. So this can move one tick, and you can see at each step it's going to be able to control these different agents and make sure that they get to their specific task as quickly as possible, and that they never collide or interfere with the other agents. So if you think of this in like agentic programming or any sort of parallel work you'd be doing to ensure that, you have things running and you want to like analyze to help steer them in different directions so they never collide or disrupt each other or touch the same files or whatever, you can ask Jev to take in like every single, it's fine if it goes in every single step and it checks.

[00:30:11] It doesn't have to plan out the entire thing ahead of time. It can do just in time. Obviously, planning out ahead of time with a decent route probably helps it out, but I think as we get more and more parallel agents and swarms and whatever words you want to use for that, this concept will become even more and more important.

**Claire Vo** [00:30:28] Well, and what, you know, this has made me think is Jev unlocks efficient inefficiency, which is like, it is kind of like inefficient to map out all possible routes, rank them, double check that they're not going to collide. Like, that is actually pretty inefficient. It's effective, it's an effective way to solve the problem, like it's an accurate way to solve the problem, but it feels inefficient. And in the past, we were just like kind of like tossing these problems in the past, last week, we were tossing these problems to these like big brainy LLMs and being like, think really hard, just think really hard and come back with the plan. And instead here, you can really very quickly evaluate all those options, stack rank them, and go through the sort of like inefficient universe of options and come to the right, kind of like the right conclusions. Very, this is why I'm like very excited about this model, because it's all these things that in the past, I think with maybe with regular, regular LLMs, you know, we're trying to do this delineation.

[00:31:32] It felt, it feels like you can do things you never imagined before, right? Like, I can create a 3D video game. I can like generate images out of words. Like, these LLMs are generative and they allow you to create things you never be able to create before. Jev, I feel like, allows me to do all the things I wanted to do, but they felt too cost ineffective, too slow, and not really worth it. And there are a lot more, a lot more things for me on that pile than there are on my like 3D gaming idea pile. And so that's why maybe as a builder, I'm so excited about this particular model.

**John Lindquist** [00:32:09] Yeah, I love that. I 100% agree. It's even like, I have so many APIs and so many apps and so many things available. How could I? And the exploring with this is quick, and the turnaround is quick, and it's exciting to see, like, you feel progress as you're working with it, whereas with generative, and I feel you almost because if you're a developer, you understand the APIs, you understand the reasoning, you understand classification, whereas with the LLMs, a lot of it is guessing, and if something goes wrong, you need to think of a different sentence to say. With decision models, you can think the decisions it made, you're like, oh, well, let's take this different route. It feels much more like programming, to be honest, where you're, you have, I feel much more in control when I see something goes wrong because I know all of its options, and I know what I want, and- ...it's fun, it's just so fun.

**Claire Vo** [00:33:05] It's so fun, and I love that you say it feels like program- it feels like the smartest function. Like, it just feels like a function that has a lot of intelligence built into it, but it's still a function. Like, it's still- I input specific

**John Lindquist** [00:33:19] Yeah.

**Claire Vo** [00:33:19] things and I get out very specific things. I can just, um, reason with it a lot more. Okay, so if you, if you've stayed with this podcast this long, it's just John, Claire, two Jev boys excited about, excited about

**John Lindquist** [00:33:35] Welcome to the club, yeah.

**Claire Vo** [00:33:36] Decision, decision models. John, okay, I'm going to give you, because you were at, we're at example 9 of 23. I'm going to give you one last chance to pick a favorite from your remaining demos before we do lightning round and kind of get you, get you out of here.

**John Lindquist** [00:33:53] Th- this one's really fun to me because- ...it- it's a presentation coach, and so I- I click the microphone, I'd start talking, and as I was talking, I'd have a list of bullet points in either a podcast or something that I want to make sure I cover, or an interview or anything. And as I start talking, it- it listens through everything I say and then starts checking the boxes to make sure that I covered everything. And so let's say this real time, as someone who likes to go off on tangents, you know, I'll get passionate about something, I'll go a different way, you're under the clock, and Jev can be your stay on track. And I think it's kind of a almost a life coach of like, you need to make sure you hit all these things. I'm going to watch every single thing you do, every single word you say, and make sure that- and you could start doing, like, red flashing lights of, you know, you have limited time left, you still need to say all this sort of stuff. So this one speaks to me as a teacher, presenter, workshop giver.

**Claire Vo** [00:34:52] I love this. I just did Lenny's- Lenny's, um, summit recently and gave the kind of like opening talk, and I hate those monitor- 'cause they're like, "Hey, you can only have 3 bullet points on here." I'm like, "That's fine, whatever." But then I like to ramble, I like to work the crowd.

**John Lindquist** [00:35:09] Yeah.

**Claire Vo** [00:35:10] I don't know if I've said that- that bullet point or not, and so imagine you

**John Lindquist** [00:35:13] Yeah.

**Claire Vo** [00:35:13] speaker notes could check off as you go and then even progress your slide for you, like, "You're done here.

**John Lindquist** [00:35:20] Yep.

**Claire Vo** [00:35:20] Let's- let's move on." Um,

**John Lindquist** [00:35:23] Yeah.

**Claire Vo** [00:35:24] and- and does this just take in- I- this- I do have a question about your real time again, because I like to make this very tactical for people, and I'm curious how you approach this. On these real time voice ones, are you constantly putting in the long stream of text to the moment? Like, are you- or are you doing like a moving window of snippets? I'm just curious how you're doing.

**John Lindquist** [00:35:48] Yeah, it's doing a- I can't remember exactly the logic, but it is analyzing what you've said up until then. It is like concatenating each word until it reaches a point where it can take an action, and it essentially transforms that into the payload that it's going to send over to the function. And so that one is, it's stored in the, it's in the history, like you could have undo and whatever because they turn unstructured into structured data.

**Claire Vo** [00:36:13] Yep.

**John Lindquist** [00:36:14] But yeah, it's a window which then gets chopped off, and then you start your new

**Claire Vo** [00:36:19] Well, and it

**John Lindquist** [00:36:20] window of text.

**Claire Vo** [00:36:21] This is a good moment to tell people exactly how much this thing costs. I feel like last time I checked, it was like 4 cents per million input tokens and nothing for output tokens, unless you, like me, are using Vercel AI Gateway right now, and then it's completely free. Completely free. So, so again, like, I can talk, I can yap, but I don't know if I can yap a million tokens quite yet, so.

**John Lindquist** [00:36:49] Challenge accepted, right?

**Claire Vo** [00:36:50] Yeah, exactly. It's pretty, pretty amazing. Well, these have been such good use cases. We've had a lot of real-time voice use cases, sort of like pairing deduplication use cases, routing and navigation and like multi-turn, multi-path kind of scoring, which I think is awesome. And then this one, which is like just keeping you on track. Did you do the things you said you would do while you're talking? Did you present the

**John Lindquist** [00:37:19] The mon- the monitor, right? The thing that's always watching you and making sure you're

**Claire Vo** [00:37:23] Love it. let's

**John Lindquist** [00:37:24] It's fair.

**Claire Vo** [00:37:25] Let's double check. Did we do it? Did we- we covered what Jev is, why speed, what it costs, does the app stay in- where does it fall short? Did we call- did we talk about where it falls short? A little bit about where you'd want to pull in an LLM, but have you ever tried to throw Jev at something and didn't do a good job?

**John Lindquist** [00:37:45] Uh, not yet. I don't think I've spent enough time since it's been out for a matter of days, um, really analyzing how smart it is versus what I would say there there's times it falls short where I add another layer of classification in, so I do multi-step, and I've seen people critique it where they only do a single pass,

**Claire Vo** [00:38:08] Yep.

**John Lindquist** [00:38:08] and they think that's not good enough, I'm not going to use this anymore.

**Claire Vo** [00:38:11] Yeah.

**John Lindquist** [00:38:12] When I run into those scenarios, I'll do multi-pass where I'll do one classification layer and then another and then another. So I think there might be a disconnect there between some people who try it out first and they're like, this isn't good enough at classification, or they don't like define the classifications, or they don't have strong enough APIs or... So I think just when it falls short, because it's fast and free, don't worry about adding just another layer. And then over time, you could compress those down into a single layer as you get more and more data that reinforces what the exact flows are that you need to go from step to step. Again, it's all so brand new that.

**Claire Vo** [00:38:54] Yeah.

**John Lindquist** [00:38:56] And it's getting smarter. Like they said, these models are as, they're as dumb as they'll ever be.

**Claire Vo** [00:39:01] Yep.

**John Lindquist** [00:39:02] And even these models will get much, much smarter.

**Claire Vo** [00:39:04] Well, and I'll give folks one other tactical piece of advice, which is you may use a specific type of Jev call, like a null, and you may say, "I think this is a yes-no question," and you may run it, you may be like, "Actually, it's a choice question, or actually it's a score question." Yeah. And so you can also test different ways to ask for different types of decisions to get it more accurate. So I've had that experience a couple times where, like, my first concept of how I would classify or make a decision was just ultimately, like, not the right one, or I had to layer one and then the other, so that's something nice for people to look at. Okay. Oh, as you said, we could just, I could go on truly forever about this, but I won't. I will spare our audience. Let's get to lightning round, and then you and I will go back to just classifying all the things for zero dollars.

**John Lindquist** [00:39:55] Sure.

**Claire Vo** [00:39:55] It has been, I don't know, a year, I was reflecting, it's been almost a year since we last chatted. It was so cute. We were talking about Claude Code and like aliases to dangerously skip permissions and just like babes in the wood, and now life is completely different. You know, what are you, other than Jev, what are you really into these days? What has changed for you in terms of AI engineering? What are the big, big moves in the last year?

**John Lindquist** [00:40:22] Some of the funniest stuff recently with the latest models, when it gets into multimedia and you're working with video and 3D and everything, is buying extra hard drives and distributing work between Mac Minis and such, which is not a prob- like, it's a problem.

**Claire Vo** [00:40:39] It's a real problem.

**John Lindquist** [00:40:40] Your la- it's a problem. And like, manit- having AIs like watch my disk space on my laptop, being like, bro, it's time to hand some over to the SSD that- anyway.

**Claire Vo** [00:40:53] Um.

**John Lindquist** [00:40:53] Um.

**Claire Vo** [00:40:54] Hold on, I have to pause. You and I are

**John Lindquist** [00:40:55] Okay.

**Claire Vo** [00:40:56] exactly the same person because truly

**John Lindquist** [00:40:59] Okay.

**Claire Vo** [00:40:59] yesterday I put the SSD in. I have a pinned Codex chat, and the pinned Codex chat

**John Lindquist** [00:41:04] Yeah.

**Claire Vo** [00:41:05] is clear up disk space, and it has 2, um, skills in it I call on a regular basis. One is move media files onto the hard drive, so it's like

**John Lindquist** [00:41:15] Mhm.

**Claire Vo** [00:41:16] it takes- it finds all the places I store all my MP4s, and it goes finds them all in different places, and then it organizes them on my SSD. And the other one is it goes, like, in the crevices of my computer and finds work trees that are, like, still running local servers and, like, clear- like,

**John Lindquist** [00:41:31] Yes.

**Claire Vo** [00:41:31] busts them out of the cache, clears- I, like- I was at a client's, uh, office, and they saw my computer, like, freeze up and you're out of memory, and it's like- they were like, "Can I buy you, like, a new computer?" I was like, "Dude, this is a new computer. This is just

**John Lindquist** [00:41:44] Yeah.

**Claire Vo** [00:41:44] the problem." And then I set up, uh, I killed the open clause, RIP, but then

**John Lindquist** [00:41:50] Yep.

**Claire Vo** [00:41:50] I set up the stack of Mac Minis as remote Codex machines to run all my- all my code on because I-

**John Lindquist** [00:41:59] Yeah.

**Claire Vo** [00:41:59] It's- it is a real problem.

**John Lindquist** [00:42:02] It's a problem.

**Claire Vo** [00:42:03] I- I'm sure-

**John Lindquist** [00:42:04] It's a problem.

**Claire Vo** [00:42:04] I'm sure we'll all just- eh, we'll go to the cloud, right? I l- I like

**John Lindquist** [00:42:08] I like local, I like working on desktop apps. Jev is going to unlock so many things, though, with like removing UI that, I don't know, pushing UI later and stuff, but I don't know. I would say the other thing, the most fascinating thing to me right now are the paradigms around, you've seen Grok bot at all and similar tools where the traditionally as developers, we think in term of, in terms of projects and file structure and co- and code and files and everything, and assigning agents roles and tasks where you don't worry about any of that stuff and you just have a list of agents, and then you can bring them into a group chat where you have, oh, I have this task and I wanted this like research guy and this, and this little code review person and this other agent, and you bring them all in to a group.

[00:43:10] It's kind of inverted the concept of agents being the top layer, and now they care about the structures and the code and Git and versioning and all that. And it's a, I think it's a really big turning point in, like, our relationships with our tools, as we stop thinking about everything we thought about before, other than buying more hard disks for agents to use, but, um.

**Claire Vo** [00:43:38] Yeah. I completely agree, and I say, like, you know, in some ways, in some ways, managers are really at risk, like, the job that you did, people don't want you to, in some ways, this concept of like org design and role design and like, you can put those skills to use when crafting your agents, which is why I am currently running, no joke, 40 Grok bots right now.

**John Lindquist** [00:44:02] Wow.

**Claire Vo** [00:44:02] Across the business. I will do an updated episode on all of them. I covered 7 in my last episode, so we'll get to the remainder in another one. John, this has been so, so fun. Jev has, I agree, been so, so fun, so I really appreciate you coming on, showing us some of your examples. Where can we find you, and how can we be helpful to you?

**John Lindquist** [00:44:23] Oh, my next big stop, I don't know if we're sharing the screen still, but mega.dev is me and Theo and Kent and Angie, we're all doing this big thing in a couple of months. if people want to check that out, all of my effort for the next couple of months is going into this. so I'm putting everything else on pause just to make this the best experience possible.

**Claire Vo** [00:44:42] And I'm going to hype you up a little bit. It is, I'm going to say it's a kind of like course slash program slash workshop, to teach you how to turn agents. I'm going to read the landing page, turn agents into leverage. You can reason about price, debug, and ship. So be an incredible AI engineer. Also, hottest website on the internet right now. I saw it the other day, and it's just- it's real lovely. Um, love it. So check it out, check out John, check out mega.dev, really cool program. And John, we'll have you back maybe in another year, and who knows? We won't- we won't have hardware or hardware at all. Maybe we'll just be carrying around our little MetaMuse keychains and talking to a little fuzzy yeti who's doing all our coding for us.

**John Lindquist** [00:45:28] Be embedded into your brain at that point, I think.

**Claire Vo** [00:45:32] Sounds good.

**John Lindquist** [00:45:32] A year is too far away.

**Claire Vo** [00:45:35] All right, thanks for joining How I AI again. Thanks so much for watching. If you enjoyed the show, please like and subscribe here on YouTube, or even better, leave us a comment with your thoughts. You can also find this podcast on Apple Podcasts, Spotify, or your favorite podcast app. Please consider leaving us a rating and review, which will help others find the show. You can see all our episodes and learn more about the show at howiaipod.com. See you next time.
