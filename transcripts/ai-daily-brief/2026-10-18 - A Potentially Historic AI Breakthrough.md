---
podcast: "ai-daily-brief"
podcast_title: "The AI Daily Brief"
title: "A Potentially Historic AI Breakthrough"
date: 2026-10-18
url: "https://aidailybrief.ai/e/2026-10-18"
guid: "https://aidailybrief.ai/e/2026-10-18"
host: "Nathaniel Whittemore"
format: "news-analysis"
level: 1
length: "00:23:00"
categories: ["safety-security"]
featured: []
mentioned: ["Hugging Face incident"]
transcript_source: "publisher"
---

# A Potentially Historic AI Breakthrough

[00:00:00] 



When it comes to AI safety, the news lately has been a little bit dreary. Or at least I should say the headlines have been. We've been living through a new wave of panic and concern
 
driven in part by the reality that models are getting more capable

and closer to what many view as key inflection points 

It's also being driven, however, by the juiciness of the scare headlines



And yet the most interesting news in that area this week Might be very good indeed

The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI All right, friends, quick announcements before we dive in First of all, thank you to today's sponsors, Robots and Pencils, CData, Granola, and Blitzy

To get an ad free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts. And if you wanna learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai.

Now, it's not all that often

That a 65-minute, densely technical web article [00:01:00] becomes the thing that everyone was talking about

And yet that's exactly what happened at the end of this week with Nick Cammarata's neural networks are already clean

I, like many people, noticed it when OpenAI's Rune posted, " When Nick told me that he had some interpretability breakthroughs, he was, uh, underselling it. I think this may be remembered as a major moment in scientific history. News so good even Eliezer Yudkowsky will have to lower his p 

doom.

We can start making alignment into a normal science

Nick summed up his article this way: Interpretability might be the most important scientific problem in the world right now, as I don't think we can solve alignment if we don't know what we're building. I think I have good news about it. I co-authored early work in mechanistic interpretability at OpenAI and came away pessimistic because neural networks appear to fold into arbitrary tangled knots.

Years later, I started OpenAI's first large-scale automated interpretability project, finding about two percent of neurons legible with the primitive tools we had

With modern agentic tools and a much [00:02:00] closer look, the picture looks totally different. the vast majority in models up to trillions of parameters are legible and their circuits beautiful. many famous examples of tangled neurons turned out to be misunderstood.



the roadblocks I expected mostly aren't there I now think ambitious interpretability will be solved by the time we need it most, and possibly quite soon, as automated scientists keep improving. It may be a bitter lesson for interpretability. The simple thing at absurd scale works

So the promise here is that we might actually be able to understand what's going on inside the processes of AI? something that so far we haven't

today we're going to try to do a Understandable version

of Nick's densely technical paper

Sharing, of course, both the excited and the skeptical responses to it. hopefully you come away understanding why this could be a big moment and what cautions we still need to have

One of One of the uncomfortable facts underneath all of AI is that even the folks building it don't really know how it works on the inside

The systems are trained, [00:03:00] not programmed. You set up the conditions and the model learns its own way of doing things, spread across billions of numbers

In AI researcher Chris Olah's phrase, "AI is grown more than built."

so because we can't read these systems, the way we check them today is basically a very elaborate exam. We ask questions, red team and grade the answers While that's useful, it only covers what we thought to ask.

And it also introduces a set of problems

like the model behaving well, not because that's what it otherwise would do, but because it knows it's being watched

This is coming up more and more. ironically, in some recent tests of models like Opus 5.5, researchers were concerned when they saw the models cheating less The big drop-off in cheating behavior brought up the question, did the model just shift away from cheating? Or did it realize that the humans watching it would think cheating is bad, and so it disguised that behavior

What this means is that in the addition to the race for capability, there's also another race

to reach interpretability, to understand what's going on with [00:04:00] AI before the models reach what Anthropic called an overwhelming level of power

If you've followed the field The story of the last six years went from excitement to something closer to despair

In the first phase from about 2017 to 2020, teams like Chris Olah's team, which included Nick, mapped image AIs detector by detector

And it looked at first like you could read a neural network like code But then between 2020 and 2023, they started to find a problem. Many of these detectors seemed to fire for unrelated things

Meaning that we couldn't really understand exactly what was going on, even though at first it appeared we could. The field settled on an explanation for this that we'll get into in just a minute When Nick's team at OpenAI used GPT-4 to explain GPT-2's detectors in 2023, Only about 2% came out clean

I actually interpretable in the way that we thought

Between 2023 and 2025, a bunch of different workaround strategies were tried some of which showed some progress, but which never really produced many wins. By 2025, many researchers wondered ifthese [00:05:00] systems werejust too tangled to read The mood, in Nick's words, was that ambitious interpretability looked like a, quote, "Incredibly hard problem, maybe too hard to solve in time to matter."

hit, which is why this essay is hitting so hard it says in short 

That the inside of AI is mostly readable already and that we've been looking at it wrong

And there are reasons to be excited. This comes from an insider who helped create the theory that he's now taking apart. He shows experiments that could have proven him wrong. And his evidence suggests that bigger models are easier to read, which is basically the opposite of what everyone feared Then again, not everyone agrees.

The head of interpretability at Google DeepMind, Neel Nanda, for example, said that the work was interesting, but, quote, "Not a significant update to the big picture."

i-- So let's try to wrap our heads around the quick version of the idea

as mentioned before, AI isn't written like normal software. It's millions of tiny detectors wired together that learn their jobs on their own. Researchers call these neurons. One might light up for edges, another for the color [00:06:00] red, another for a dog's ear. the dream of the interpretability field is simple.

Work out what each detector does, and then you can read what the AI is doing just the way you'd read code

one of the most famous detectors shows why some of them made no sense

That detector lit up for cat faces, but also for the front of cars. Cats and cars, of course, have nothing to do with each other. So for years, this one detector was the go-to proof that AI's insides are scrambled It shows up in the field's most read papers, including ones Nick co-wrote

f- the explanation the whole field landed on was cramming, or what researchers called superposition

The idea was that an AI has more ideas to store than it has detectors, so it shares detectors between ideas 

It 

works best when those ideas rarely show up together, like Christmas lights and pool floats in the same box

and if that's how it works, the detectors themselves are meaningless

So researchers built unscramblers, second AIs trained to pull the ideas back apart, and studied those [00:07:00] instead

A lot of the field's money and effort went into that for years. Nick was there for this. In 2019, he found one of the first examples that seemed to prove cramming and helped name it

In this new research, however, Nick went back to this detector and asked, "If I couldn't use the words cat or car, how would I describe it?" The answer took him about five seconds. It's a V detector

Pointed shapes switch it on. A fox's snout, a cat's face, the front of a car, a bullet train's nose, a candle flame, and a martini glass. Round shapes like golf balls or a clock face, switch it off

Nick wrote, "Why would an arbitrary mixture of cats and cars need to connect so strongly to a flame? It was never two unrelated things. It was one idea we hadn't recognized."

Nick's claim is more or less that most of the scrambling was never in the AI itself, but in the microscopes we were using to look at it

He proposed three causes, all of which are fixable. The tools for picturing what a detector wants were blurry and misleading. The early image AI the field studied from [00:08:00] 2014 was built in a way that made it learn messily

when you retrain a modern design of the same size, about ninety-nine percent of its last layer detectors are readable. And finally, some detectors branch. One that starts on the letters IY grows to DIY and then to do it yourself. That looks random at the end, but obvious if you watch it grow

And it turns out it's not just old image models. In a modern OpenAI model, about nine out of 10 detectors turn out to have one main job

Compare that again with that 2023 OpenAI project

That could only explain about two percent of detectors in GPT-2

Now keep in mind, these are early counts. They are self-reported. The exact number depends on where you draw the lines, and the full technical paper isn't out yet

What this opens up is the ability to check AI's reasoning, not just judge it by its answers

the example on screen comes from a model with trillions of parameters, Kimi K three. when asked what to do with a found wallet full of cash, you can watch detectors for lost property and honesty light up, and push it to say return.

And the point then about deception is if all we can do is read the [00:09:00] answers, the AI can hide a plan from us. But since the plan has to be readable by the AI's own wiring to work, if we can read that wiring as well, it's not just the output, but the plan that's readable to us as well

And this is what got Rune so excited. The idea that alignment could become a normal science, in his words, with steadily checkable progress instead of guesswork

to read a lot of the responses to this on X, they are, in a word, breathless. And yet even Nick himself calls it a working hypothesis and puts himself at about 85% sure

Other researchers are a bit less convinced

At this point, it's no longer a question of whether companies are actively using AI

Using it well, on the other hand, is a whole different story.

When I'm in a meeting, I'm fully in it.

now, So what we're gonna do now is go quickly

Through a bit more of what's in Nick's paper And some of the responses and objections that come up along the way

dive, The first thing we're going to dive deeper on is whether the experts got it wrong. uh, basically, if the inside of AI was readable all along How did a field full of brilliant people miss it?

Nick's answer, as we got a preview of, is that three mistakes stacked on top of each other

Now from this point I should say, you're likely to get a lot more by watching this episode, which you can do on YouTube or on Spotify, or just by following along on Nick's paper or my interpretation presentation, both of which will be linked in the show notes

In 2019, Nick was building one of the first tools to look inside an image [00:13:00] AI. As he was doing so, he saw a car detector feeding into four dog detectors. He took it to colleagues, and they concluded that AI was tucking car inside the dog detector, a hiding place to read back out later.

m- that became one of the field's first examples of cramming

Nick even said in the essay, " It was the only one we showed and the only one I ever saw."

When Nick rechecked it, he found that two of those detectors are just car detectors, but the other two detect a pose, i.e., which way something faces the camera Cars and dogs share poses. The AI, in fact, has more than a hundred of these pose detectors Nothing was hidden But because the cramming story felt intuitive, Nick said it didn't prompt diving more into the tools

second mi the second mistake was the microscope itself

AI, one key tool asks the AI to draw a picture a detector most wants to see

In short, Nick found that the drawing tool cheated. It took the easiest path to make the detector fire

And after a few small fixes, the drawings matched the photos as Nick put it, same neurons, better microscope

the third mistake was that the AI that [00:14:00] people were studying

had a learning problem. That was Inception V1, which was Google's 2014 image model. Its last layer was the field's main evidence that AI is unreadable. Nick estimates that 5% of its detectors were readable with the tools of the time Fix the microscope and the same model is about fifty percent readable, and when you retrain it with modern settings, about seventy percent.

Build a modern design with the same size and same data, and the readability jumps to ninety-nine percent

So why did nobody go back and check? Nick argues it's because of how the cramming theory works If you believe a detector is crammed, a confusing detector is a dead end and you stop looking

every time detectors came back clean, the theory moved to somewhere where nobody had checked yet. The faint signals, the combination of detectors, the next layer 

Nick calls it superposition of the gaps

Nick confessed, "For years, I was a staunch superposition believer." He now says it should have been the last explanation tried, not the default

But here we get some of the most serious pushback

Liv Gorton is another interpretability researcher. Nick's essay cites her 2024 study of the same 2014 image [00:15:00] AI. In a long thread, she argues that the essay attacks a narrower version of superposition than researchers actually hold her point is that superposition, or what we've been calling cramming on this episode, is about capacity.

You store more ideas than you have detectors by giving each idea its own slightly different combination of them. Unrelated ideas make good examples because they rarely clash, but related ideas can be crammed too

She also 

points out that there are only as many perfectly separate directions as detectors, but exponentially many nearly separate ones. She'd wrote, "I'd be very surprised if networks didn't use this capacity."

ba- Nick basically responded that he wasn't trying to say

that AI never puts ideas together in a single detector

but that in general, what he cares about is whether AI does the bad version of packing things arbitrarily so they can't be read

And that's what he said wasn't happening in the way that he thought it was

Google DeepMind's interpretability lead, Neil Nanda said something similar to Liv, writing, " It seems to me like language models have far more facts and memorized things in them than they have neurons. I expect that weak neuron activations contain [00:16:00] lots of semantic superposition-y info."

Nick basically argued that if this is happening, it's happening very differently than the packing random unrelated things together

that the field previously thought And that instead, he predicted that the opposite would be true, where rare facts should ride on related machinery. Although those tests haven't been done, Nick argues that that is in fact testable

In fact, when asking why some detectors seem to do several things Nick argued that it wasn't cramming, but in fact something called branching

Nick retrained an old image AI from scratch and watched a single detector take shape

It starts on yellow flower fields in photos that sometimes include a dog. Then it grows along each thing in those photos: other nature scenes, green round things like tennis balls and fruit, dogs without flowers, and finally broccoli. By the end, the fields are nearly gone

This is branching, where each step is small and sensible. The opposite of cramming, where unrelated things get thrown together

And by the way, for each of these, there are many, many more examples in the main essay. I'm just cognizant of time and space in our own puny human brains

Still [00:17:00] going back to Liv's critiques, she argued that branching and cramming answer different questions

Saying that branching is how a detector picked up several jobs, but cramming is how the information gets stored, and that you could have both at once

an- Nick's theory in the essay is that every branch traces back to one origin and grows out in order. that makes it easy to test and easy to prove wrong, although that work hasn't been done yet

one finding that flips the usual fear about AI getting bigger is that Nick is actually arguing that bigger AIs are easier to read Nick's analogy is this. In a small town, asking for the financial district barely makes sense.

There's a bank on one street and an accountant on another

In New York, on the other hand The Financial District is incredibly easy to spot. You know right where it is

His experiment involved dog ear detectors in three AIs that were about 300 times apart in size. The small one has very coarse dog detectors

The big one has very specific ones So in a small model, you have detectors for general dog, light and fluffy dog, or dark and shaggy dog. In the medium model, [00:18:00] local branches emerge. the ear and the head of the dog turns into detectors for curly ears or ear, neck, and hair And then in the largest model, the branches converge and split Head side ears, pale ears, wavy ears are all separate, and then move into things like smooth flaps, hanging ears, and long ears

Theoretically then, there should be a precision to the detectors in larger models that makes them ultimately easier to read

Now, one of the other categories of pushback?

Is that even all the terms that we're using in here

are somewhat blurry rather than precise For example, Neil from DeepMind argues that Nick's essay's bar for a detector doing one job is too generous. 

instead he said that he'd call, in his words, "A fair few of those detectors actually scrambled."

which Nick acknowledges this and it brings up another point, which is that so far this is just Nick and his team doing this work, with no one else having yet checked it

But let's say that Nick is right. What would that then change?

Nick argues that clean doesn't mean that every detector matches a word we have. Instead, it means that the AI's parts are organized to be read by the AI itself. [00:19:00] Every detector exists to be used by later detectors. So the AI has already organized itself to be legible to its own downstream parts

Our job then is to become another reader of AI, Reading it in the same way that it reads itself

he, in describing where the safety risk actually is, Nick wrote, " Deception might hide from someone reading a model's outputs, but it has no reason to hide from the model's own circuitry. It needs to be accessible to its readers, and if we become a reader, it should be accessible to us.

My fear is that deception will be right there in plain sight, and we won't know how to read it

Interestingly, the biggest objection to the safety payoff isn't about cramming at all It's the argument that even if every detector is readable, safety needs more, knowing how they combine into a decision and being confident nothing important was missed

Neil argued that he was pessimistic about that level of understanding

Even if there are practical uses like figuring out, in his words, why did a model do a sketchy thing?

As we try to wrap our heads around what smart people think about this, I laid out a representative set of the responses from more [00:20:00] excited to more skeptical

On the more skeptical side

you have AI safety researcher Steven Casper calling it hype until further notice And if anyone builds it, everyone dies, author Eliezer Yudkowsky saying, " Let me know when you've advanced to the point of getting started." then at, and then at the other end You have folks like people at OpenAI calling it one of the most important single days in deep learning history and at the level of significance of Attention is All You Need

This is going to be one of those papers that really needs more smart people to dig into it

But if nothing else has gotten a ball rolling down the hill

There were a few things that even the critics could agree upon. The idea that perhaps detectors were more useful than the field assumed, and that even if this doesn't solve AI safety, it may work for practical problems

there was a lot of excitement about AI agents reading detectors, and pretty much everyone agreed that rechecking the old results was worth it

So some of the open questions remain. Is cramming refuted or has it just been redefined?

that, is the way that the paper defines the one main job of detectors too generous? If we can read all the parts, do [00:21:00] readable parts add up to a readable whole?

And does all of this hold at the scale and size of models that we actually are dealing with today?

When it comes to my take, I am not even close to qualified despite producing this podcast to have any real dog in the fight

of how significant this is

I will note that my historical pattern recognition would suggest that scientific breakthrough very often does come from simply looking at a problem a slightly different way

And then it's not hard at all to imagine a relatively niche field with only so many researchers in it getting trapped for a time in a set of assumptions that no one thought to question

worth... As always, I think it's worth

Being skeptical of the boldest claims of everything changed

But it's hard not to be directionally excited by this

I think a really interesting thought was shared by Christian from the Seeing Clearly podcast. They wrote, " One of the primary reasons I'm not a doomer is that human civilization is a complex adaptive system with self-correcting mechanisms. The reason this is so hard to see from the doomer camp is because they themselves are precisely the [00:22:00] mechanism by which these restoring forces emerge.

As risk from AI becomes more clear, new ecological niches emerge in being anti-AGI. Status markers then shift to areas like mechanistic interpretability, and then talent and capital floods in. As swarm incidents get worse, the invisible hand uses legal liability to shift the gradient in the incentive landscape towards more alignment work."

So to my accelerationists, the doomers are part of how we make it. They are a necessary half of the opponent processing mechanism used to steer the ship to the promised land. The doomers and the accelerationists need each other to keep checks on each other's excess. Both have important roles to play in this ant colony that is human civilization.

Everything is going according to plan that's a sort of more romantic way to put what I've often said

Which is that more and more attention coming, the more and more capability these models have is both the feedback loop I would expect

And the feedback loop that makes me think we'll be able to figure things out

feels, as much as it feels like to some in the AI safety camp that the world isn't acting fast enough or with enough focus

[00:23:00] You cannot argue that there has been no change after something like the hugging face incident. The fact that all I have to say is the hugging face incident and a huge cross-section of people, not just listening to this podcast, but my barber yesterday know what I'm referring to is case in point

times, And the Already Clean paper is one of the first times recently

that the change isn't just a change in people paying attention

But a directionally positive change in our ability to do something about it as well

There is so much that I have left out of this episode I highly encourage you to go check out the original paper, again, linked in the show notes, "Neural Networks Are Already Clean". But for now, that's gonna do it for today's AI Daily Brief.

Appreciate you listening or watching, as always. And until next time, peace. 

​
