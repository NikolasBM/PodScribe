---
podcast: "latent-space"
podcast_title: "Latent Space"
title: "Segment Anything 2: Demo-first Model Development"
date: 2024-08-07
url: "https://www.latent.space/p/sam2"
guid: "substack:147418165"
host: "Swyx"
transcript_source: "publisher"
---

# Segment Anything 2: Demo-first Model Development

[00:00:00] [music intro]

**AI Charlie** [00:00:00] Happy Yoga! This is your AI co host Charlie. Thank you for all the love for our special 1 million downloads Wins of AI Winter episode last week, especially Sam, Archie, Trellis, Morgan, Shrey, Han, and more. For this episode, we have to go all the way back to the first viral episode of the podcast Segment Anything Model and the Hard Problems of Computer Vision, which we discussed with Joseph Nelson of Roboflow.

**AI Charlie** [00:00:00] Since Meta released SAM 2 last week, we are delighted to welcome Joseph back as our fourth guest co host to chat with Nikhila Ravi, Research Engineering Manager at Facebook AI Research and lead author of SAM 2. Just like our SAM 1 podcast, this is a multimodal pod because of the vision element, so we definitely encourage you to hop over to our YouTube at least for the demos, if not our faces.

**AI Charlie** [00:00:00] Watch out and take care.

## [00:03:10] Introducing Nikhila

**Swyx** [00:00:00] Welcome to the latest podcast. I'm delighted to do segment anything to our first, one of our very first viral podcasts was segment anything one with Joseph. Welcome back. Thanks so much. And this time we are joined by the lead author of Segment Anything 2, Nikki Ravi, welcome.

**Nikhila Ravi** [00:00:00] Thank you. Thanks for having me.

**Swyx** [00:00:00] There's a whole story that we can refer people back to episode of the podcast way back when for the story of Segment Anything, but I think we're interested in just introducing you as a researcher, as a, on the human side what was your path into AI research? Why, you know, why did you choose computer vision coming out of your specialization at Cambridge?

**Nikhila Ravi** [00:00:00] So I did my undergraduate. Degree in engineering at Cambridge university. The engineering program is very general. So first couple of years, you sort of study everything from mechanical engineering to fluid mechanics, structural mechanics, material science, and also computer science.

**Nikhila Ravi** [00:00:00] Towards the end of my degree, I started taking more classes in machine learning and computational neuroscience, and I really enjoyed it. And actually after graduating from undergrad, I had a place at Oxford to study medicine. And so I was. Initially planning on becoming a doctor, had everything planned and then decided to take a gap year after finishing undergrad.

**Nikhila Ravi** [00:00:00] And actually that was around the time that sort of deep learning was emerging. And in my machine learning class in undergrad, I remember one day our professor came in and that was when Google acquired DeepMind. And so that became like a huge thing. We talked about it for the whole class. It kind of really stuck.

**Nikhila Ravi** [00:00:00] And I was kicked off thinking about, okay, maybe I want to try something different other than medicine. Maybe this is a different path I want to take. And then in the gap year, I did a bunch of coding, worked on a number of projects. Did some sort of freelance contracting work. And then I got a scholarship to come and study in America.

**Nikhila Ravi** [00:00:00] So I went to Harvard for a year, took a bunch of computer science classes at Harvard and MIT, worked on a number of AI projects, especially in computer vision. I really, really enjoyed working in computer vision. I applied to Facebook and got this job at Facebook, and I've now at Facebook at the time, now Meta, and I've been here for seven years, so very circuitous path, probably not a very unconventional, I didn't do a PhD, I'm not like a research, typical research scientist, definitely came from more of an engineering background, but since being at Meta, Have had amazing opportunities to work across so many different interesting problems in computer vision from 3D computer vision.

**Nikhila Ravi** [00:00:00] How can you go from images of objects to 3D structures and then going back to 2D computer vision and actually understanding the objects and the pixels and the images themselves. So it's been a very interesting journey over the past seven years.

**Swyx** [00:00:00] It's weird because like, I guess with segment anything too, it's like 4D because you solve time, you know, you started with 3D and now you're solving the 4D.

**Nikhila Ravi** [00:00:00] Yeah, it's just going from 3D to images to video. It's really covering the full spectrum. And actually, one of the nice things has been, so I think I mentioned I, Wanted to become a doctor, but actually Sam is having so much impact in medicine, probably more than I could have ever had as a doctor myself. So I think, you know, hopefully Sam too can also have a similar sort of impact in medicine and other fields.

## [00:06:39] The Impact of SAM 1 in 2023

**Swyx** [00:00:00] Yeah. I want to give Joseph a chance to comment. Does that also mirror your, we know your story about going into, into vision, but like in the past year, since we did our podcast on Sam what's been the impact that you've seen?

**Joseph Nelson** [00:00:00] Segment anything. Set a new standard in computer vision, you know recapping from from the first release to present Sam introduces the ability for models to near zero shot meaning without any training identify kind of perfect polygons and outlines of items and objects inside images and that capability previously required a Lots of manual labeling, lots of manual preparation, clicking very meticulously to create outlines of individuals and people.

**Joseph Nelson** [00:00:00] And there were some models that attempted to do zero shot segmentation. of items inside images, though none were as high quality as segment anything. And with the introduction of segment anything, you can pass an image with SAM1, SAM2 videos as well, and get perfect pixel perfect outlines of most everything inside the images.

**Joseph Nelson** [00:00:00] Now there are some edge cases across domains and Similar to the human eye, sometimes you need to say, like, which item maybe you most care about for the downstream task and problem you're working on. Though, SAM has accelerated the rate at which developers are able to use computer vision in production applications.

**Joseph Nelson** [00:00:00] So, at RoboFlow, we were very quick to enable the community of computer vision developers and engineers to use SAM and apply it to their problems. The principle ways of using SAM, you could kind of use SAM as is to like pass an image and receive back masks. Another use case for SAM is in preparation of data for other types of problems.

**Joseph Nelson** [00:00:00] So, for example, in the medical domain, let's say that you're working on a problem where you have a bunch of images from a wet lab experiment. And from each of those images, you need to count the presence of a particular protein that reacts to some experiment. To count all the individual protein reactions, You can go in and lab assistants to this day will still like kind of individually count and say what are the presence of all those proteins.

**Joseph Nelson** [00:00:00] With Segment Anything, it's able to identify all of those individual items correctly. But often you may need to also add like a class name to what the protein is. Or you may need to say, hey, like, I care about the protein portion of this. I don't care about the rest of the portion of this in the image.

**Joseph Nelson** [00:00:00] And, or what it encourages and asks for the user to do is to provide some visual prompting to say, hey, which part, like, Sam says, hey, I can find segments of anything, but which segments do you care about? And so you can do visual prompting, which is kind of a new primitive that Sam introduced. And so at RoboFlow, we have one portion of our tool stack enables users to very quickly label data.

**Joseph Nelson** [00:00:00] With segment anything, Sam can already provide, hey, here's where I see the outlines of objects. Or a user can click to prompt to say, Hey, here's where the outlines of objects matter. And I recently pulled statistics from the usage of SAM in RoboFlow over the course of the last year. And users have labeled about 49 million images using segment anything on the hosted side of the RoboFlow platform.

**Joseph Nelson** [00:00:00] And that's like 5 million in the last 30 days alone. And of those images, We did kind of like a rough bafka napkin calculation of like how much time that has saved. Because, again, the alternative is you're clicking individual points to create a polygon, and with SAM you just click once and it guesses where the polygon is.

**Joseph Nelson** [00:00:00] And I'm sure in a bit we can maybe screen share and show some examples of what this experience is like. And in that time estimation, it's like, On average saves, you know, maybe a dozen or so seconds. And we estimate that this is probably saved on the order of magnitude of 35 years of time for users.

**Nikhila Ravi** [00:00:00] That's incredible.

**Joseph Nelson** [00:00:00] So, I mean, basically like in the first, the first year of a model being available, not only can you say, Hey, I'm just going to go use this model, those numbers that like 49 million images. is an estimate directly related to just the hosted side. So imagine all of the users that are self hosting or using SAM for robotics applications or out in the field or offline where it's not even, like, the time or the image counts are tabulated.

**Joseph Nelson** [00:00:00] And we're probably talking about, you know, just a fraction of the amount of value that's actually being produced for a number of downstream tasks. So to say that the impact has been You know, people use terms like game changing and these sorts of things. It has changed the industry. It's set a new standard.

**Joseph Nelson** [00:00:00] And with the release of SAM 2, I think we're about to see an acceleration of those capabilities for a lot of reasons.

**Nikhila Ravi** [00:00:00] That's really great to hear. I think one of the, really SAM 1 was. How many fields actually rely on manual segmentation? I think we're not really exposed to that. Maybe you are at Roboflow because you get to see all the users of these tools.

**Nikhila Ravi** [00:00:00] But for me, it was, you know, people working on understanding coral reef bleaching or farmers counting their cows and so many different applications that as a researcher. You never get exposed to, but you can have impact towards. So I think that was really awesome to hear.

## [00:12:15] Do People Finetune SAM?

**Swyx** [00:00:00] So as sort of audience surrogate, who knows less than the two of you, I'm going to ask a really dumb question maybe, but is everyone using stock, a segment, anything?

**Swyx** [00:00:00] Are they fine tuning for the medical domain? Like how on earth could it work for the medical field without fine tuning, right? Like, is that a thing?

**Nikhila Ravi** [00:00:00] So I mean, I can give a quick perspective from the research side. So one of the things, design decisions we made in SAM was to not have class labels. And so all the data is annotated in a class agnostic way.

**Nikhila Ravi** [00:00:00] So anything that has a boundary, we consider to be an object. So for example, in any image, there's lots of small objects. We might not know what the name of them are, but they're If you can draw a boundary around it, so you can imagine that we have 11 million images in the SA 1B dataset, we annotated all the objects, there's many, many small objects.

**Nikhila Ravi** [00:00:00] And so if you think about cells, they're also kind of small objects, there's probably things in the training data. That looked like it, but we didn't have to label it. And so that means that even when you use SAM for applications that it wasn't really trained for, because we didn't restrict it to a certain set of categories, you can actually use it out of the box without custom adaptation.

**Nikhila Ravi** [00:00:00] But having said that, there's probably certain domains where you need some expertise in order to be able to segment something properly. And for those use cases, Having some extra fine tuning data would probably help, and we've sort of seen that there's some papers that have come out that do this, and, you know, we'd love to hear, Joseph, how people are collecting data with SAM and fine tuning for their use cases.

**Joseph Nelson** [00:00:00] Once SAM came out, there were adaptations that said, could we use SAM to be, you know, like, efficient SAM? Like, basically take SAM and maybe accelerate it. And then there were domain adapted SAMs, like CellSAM, for example, out of the UC system. Now, what's interesting is, there's, like, adapting SAM to a domain, there's kind of two ways by which that's done.

**Joseph Nelson** [00:00:00] One is, as you mentioned, like, potentially SAM doesn't have a good concept of The objects of interest. And so you need to do domain adaptation and increase the accuracy for zero shot prediction. The second way though, is it's not fine tuning. It's actually just prompting. It's just guiding the model existing knowledge.

**Joseph Nelson** [00:00:00] to say which segments you care about. And both those are actually kind of equally important on the application side. You need to, like, a priori ensure that the objects of interest can be correctly segmented and maybe collect data to do that. But even if you had, like, a perfect SAM, like an omniscient SAM that could see every segment in every domain with all pixels perfectly outlined, in production, you would still need some way to Almost like signal to the model what you care about like to paint this picture if you are like a retailer and you are providing Photos of models wearing your clothing on your retail site You may care about you know only the shirt and Sam by default might segment the full person And so there's you know visual prompting that you can do to ensure that you only outline Maybe the shirt for the purposes of swapping in and out different shirts for displaying a given model on a retail page You And so I think what's interesting is that's where, like I wouldn't call it domain adaptation, but that's where, like, when you apply to industry, like, one thing that's particularly important with tooling and enabling SAM to reach its full potential.

**Swyx** [00:00:00] That's really encouraging to hear. I should also think, like, you know, the last time we talked about this, we wanted to, the very natural addition on the class labeling side is the grounding Dino work, right? So I think people, built a grounding SAM and all the other extensions.

## [00:16:05] Video Demo of SAM

**Swyx** [00:00:00] I think it's, it's probably a good time to cut to a quick demo of SAM2 for people who are, who are tuning in for SAM2 and who better to demo SAM2 than Nikki.

**Nikhila Ravi** [00:00:00] Sure. So I'll try to narrate what I'm what I'm doing. So audio listeners can also understand. So we have a web demo where anyone can try SAM2 on a video. Here we have a video of someone kicking a football, and I'm going to click on the football to select the object in the first frame. But you can actually select the object in any frame of the video, and this will work.

**Nikhila Ravi** [00:00:00] The next step is to hit track. So the model's now tracking this in real time. We don't save any of this, it's all running in real time. And now you can see the ball has been tracked throughout the entire video. There's even like a little bit of a challenging case here where the shoe covers the football.

**Nikhila Ravi** [00:00:00] And actually, you know, the model makes a little bit of a mistake, but that's okay. Because we can actually, here, the model makes a little bit of a mistake here. But you know, we can actually add a refinement click. You can add negative clicks until we get the mask that we want on this frame. And then you can hit track again, and the model will track the object, taking into account the additional information I've provided at that frame.

**Nikhila Ravi** [00:00:00] We've also added a couple of other fun things you can do on top of the track, like add effects. We can add you know, foreground effects, background effects. And these are just ways of showing how we can use the output from SAM2 as part of other tools like video editing tools. Other systems, so this is just a preview of what you can do with SAM2, but the really cool use cases are places where we might not have even imagined SAM2 being useful.

**Nikhila Ravi** [00:00:00] So we have a number of examples of things you might want to use it for. There's like underwater videos that it works actually really well for even though we, models never really seen an octopus before and octopus have a lot of moving parts that SAM2 can actually quite effectively. Keep track of all the different tentacles and we can probably see it more clearly if I desaturate the background.

**Nikhila Ravi** [00:00:00] We can see that actually the tracking of all the different tentacles is Quite accurate. Another challenge with video is that objects can actually become occluded. They can disappear from view and reappear. And a really fun example here is the shuffling cup game, which many of you might have seen. And so here I can click on the ball in the first frame.

**Nikhila Ravi** [00:00:00] I can also, You know, click on a different cup. And so here, the additional challenge is that there's three cups that look exactly the same. And then there's the ball that will get occluded by the cup. So the ball's no longer visible, the cups are all moving around, they all look the same. But the model actually keeps track of the cup that we selected.

**Nikhila Ravi** [00:00:00] And, as you can see at the end, here I'll jump to the end so you can see. It actually finds the cup again. I wanted to point out a couple of fun demo UX features that we added that actually really helped with this. So if you can see at the bottom, there's these swim lanes and then the swim lanes, actually the thickness of the swim lane tells you if the object's visible or not.

**Nikhila Ravi** [00:00:00] So at the beginning, the object's visible,

**Swyx** [00:00:00] the object

**Nikhila Ravi** [00:00:00] disappears, and then the object comes back. So you can actually visually tell. When the object's being occluded and when it's not, and so it's a nice way of like, knowing if you need to go in and fix the model prediction or not. And so these are some of the UX innovations that we came up with, as well as the model innovations.

**Joseph Nelson** [00:00:00] One thing that I think is really notable here, there's two things. One is that like, I'd love to have a little bit of a discussion about how the models keeping track of the embedded scene to keep track of the ball and the cup in different places. Put a pause on that for a second.

## [00:19:59] Why the Demo is so Important

**Joseph Nelson** [00:00:00] One thing that Meta has put an emphasis on here in a much greater degree than other model releases is the demo experience of recognizing that in addition to having a model that can do zero shot segmentation, you've created a web experience that allows folks to kind of experience both the video effects but the types of UX innovations that encourage usage and adoption.

**Joseph Nelson** [00:00:00] It's actually kind of reminiscent of The underlying technology of ChatGPT was available prior to the web experience of ChatGPT. Can you talk a bit about why that was a consideration to your team and how you thought about the creation of The demo experience in tandem with training and releasing a new model.

**Nikhila Ravi** [00:00:00] Yeah, absolutely. I think that's a really great example of how, you know, Chad, GPT was really more of a UX innovation. Obviously it was like a number of research innovations that helped to get to this point. But as you said, like the underlying technology was around for a while. And, you know, putting this UX around as a chat interface helped tremendously with the.

**Nikhila Ravi** [00:00:00] Adoption and people understanding how it could be useful for real world use cases. And in computer vision, especially, it's so visual. The best way to show how these models work. Is by trying it on your own image or your own video with the original SAM, we put a lot of effort in building like a high quality demo.

**Nikhila Ravi** [00:00:00] And the other piece here is that the demo is actually the annotation tool. So we actually. Use the demo as a way to improve our annotation tool. And so then it becomes very natural to invest in building a good demo because it speeds up your annotation and improves the data quality and that will improve the model quality.

**Nikhila Ravi** [00:00:00] With this approach, we found it to be really successful. And obviously externally, people really liked being able to try it. I think, you know, people in fields outside of machine learning would never have tried SAM if we didn't have that demo. And I think that definitely led to a lot of the adoption in, like, diverse fields.

**Nikhila Ravi** [00:00:00] And so because we saw that with SAM 2, like, the demo was a priority first class citizen from day one. And so we really invested in making that. And I think with SAM2 as well, we wanted to have like a step change in the demo experience. Interactive video segmentation, I think that experience is something that maybe has not had much thought given to it.

**Nikhila Ravi** [00:00:00] And we really wanted to be like, okay, if we are to design a step changing video segmentation experience, what would that look like? And that really did influence our model. And annotation design as well.

**Joseph Nelson** [00:00:00] It's a really encouraging trend for not thinking about only the new model capability, but what sort of applications folks want to build with models as a result of that downstream.

**Nikhila Ravi** [00:00:00] I think it also really forces you to think about many things that you might postpone, for example, efficiency.

**Joseph Nelson** [00:00:00] Yes.

**Nikhila Ravi** [00:00:00] For a good demo experience. Making it real time is super important. No one wants to wait. And so it really forces you to think about these things much sooner and actually makes us think about how to, what kind of image encoder we want to use or like other hardware efficiency improvements.

**Nikhila Ravi** [00:00:00] So those kinds of things, I think, become a first class citizen when you put the demo first.

## [00:23:19] SAM 1 vs SAM 2 Architecture

**Joseph Nelson** [00:00:00] That's one thing I was going to ask about, and this is related to the architecture change. So SAM1 and the SAM1 demo experience. You have the encoder that's creating the embeddings of all the potential spaces.

**Joseph Nelson** [00:00:00] That needs to be run on a GPU. That's a relatively intensive operation. But then the query of those embeddings can be run independently and on a cheaper process. So in the SAM1 demo, the way that it was structured, and also this is the way that we have our SAM tool structured in Robloflow as well, is images go to a GPU to get all the SAM based embeddings.

**Joseph Nelson** [00:00:00] But then for querying those embeddings, we do that client side, in the browser, so that the user can very quickly, you know, you can move your mouse over and you get the proposed candidate masks that Sam found for that region of the image. In SAM 2 you dropped that in the web demo. And I think that's because you made some notable improvements to the rate at which encoding happens.

**Joseph Nelson** [00:00:00] Can you talk a bit about what led to those speed increases and, again, how that interplays with providing a fast encryption? user experience for interacting with the model.

**Nikhila Ravi** [00:00:00] Yeah. So the SAM2 web demo is primarily focused on video. We, we decided to just keep it simple and focus on video and on GitHub, we have a Colab notebook that shows how to run SAM2 on images.

**Nikhila Ravi** [00:00:00] So if you're interested in using, replacing SAM with SAM2 for images, check out GitHub, but on the SAM2 demo, it's not as straightforward to adopt the same architecture as SAM. For video, because we can't send the per frame image embeddings for an entire video back to the front end. In SAM, each frame embedding was like four megabytes, but if you have a long video and that's like per frame, it would become impossible to send that back to the front end.

**Nikhila Ravi** [00:00:00] So, SAM 2 actually, in terms of the architecture details, I was actually just looking at this earlier, but SAM1 model was around 630 million parameters. It's a fraction of the size of these large language models, but very small. Actually, SAM2, the largest model, is around 224 million parameters. So it's actually One third the size of the SAM original model.

**Nikhila Ravi** [00:00:00] So we changed the imaging coder from A-V-I-T-H and SAM to a higher model, which has also developed by by meta. So that definitely was something that helped. And in terms of the efficiency compared to sam, so if we were to run SAM per frame on a video or run SAM two, it's around six times faster to run SAM two versus run SAM per frame.

**Nikhila Ravi** [00:00:00] A number of things improved the efficiency of SAM2 such that we were actually able to run this entirely on the server and not have any component in the front end. But I am very curious to see who puts this on device, like I'm pretty sure soon we'll see like an on device SAM2 or, you know, maybe even running in the browser or something, so.

**Nikhila Ravi** [00:00:00] I think that could definitely unlock some of these edge use cases that we were able to make a compelling web demo without having to do that.

**Swyx** [00:00:00] Hugging face is probably already working on Transformers. js version of it, but totally makes sense. I want to talk about more about things from the paper, but I think we're still in this sort of demo section.

## [00:26:42] Video Demo of SAM on Roboflow

**Swyx** [00:00:00] And so I want to hand it to Joseph for his demo to see what the RoboFlow site looks like.

**Joseph Nelson** [00:00:00] So I can, I can give some context into one key area that Nicola, you mentioned earlier, which is. Sam has made the decision, both Sam 1 and Sam 2, to be class agnostic in terms of its predictions. And that, you then have the ability to have a generalizable, model for zero shot capability.

**Joseph Nelson** [00:00:00] However, in a lot of domain applications, you do want the class wise name. And so a lot of the challenge can be adding that class wise name for the, at least the annotation to an experience that we've created. That's one of the key considerations. So I will similarly Share my screen and show an example.

**Joseph Nelson** [00:00:00] Here, I have a bunch of images, and there's a number of ways that I could annotate things, like I could prompt a large multimodal model with like grounding capabilities, you know, you could outsource it, or I can do manual labeling. And with the manual labeling, this is where we make use of models like segment anything.

**Joseph Nelson** [00:00:00] to propose candidate masks and make it faster. So we have, you know, this annotation pane and what we call the smart poly tool, which is powered by Segment Anything. This is currently Segment Anything 1. We're accelerating and seeing improvements from similar to what the paper shows of Segment Anything 2 performed better on E3.

**Joseph Nelson** [00:00:00] Images as well as video, but with a segment, anything I'm able to basically prompt regions of my image of interest. So for example, if like, I wanted to say, I want to like add the drum set. You'll see here that like, the original candidate proposal is just the base drum, but let's say I wanted the whole drum set.

**Joseph Nelson** [00:00:00] So the UX primitive of being able to add and subtract candidate regions of interest is really intuitive here. And now, great, I have this outline, but in fact what I want is, I want to name that as a class. Because maybe for the model that I'm building, I want to build like a task specific model, you know, like an object detection model or an instant segmentation model.

**Joseph Nelson** [00:00:00] Or, you know, maybe I'm even using like a multimodal model and I want that multimodal model to refer to regions of interest in the images as a specific thing. And so I think what's, you know, really powerful is, of course, like, I get this really rich zero shot prediction. And here we have our friend Rick.

**Joseph Nelson** [00:00:00] So I get this really rich candidate set of predictions. But then by adding the class wise label, I can, you know, very quickly make sure that any downstream tasks are aware not just of the segment, but also of the, what is inside that segment. Which actually takes me to A separate point of something that I predict that's probably going to happen and Nikhil, I'm actually kind of interested why maybe your team made a conscious decision to not do this initially with SAM2.

**Joseph Nelson** [00:00:00] There's been an emergent set of models that are also adding open text prompting capabilities to grounding models. So for example, like you've seen models like Grounding Dino or Owlvit, which, you know, you can do. Even image to image or text to image based prompting to find regions of interest. And maybe maybe I can actually give an example of that even in the context of this same data.

**Joseph Nelson** [00:00:00] So if I wanted to try out, you know, grounding dino on this same set of images, I could try out, you know, prompting grounding dino for a set of different classes. And what's notable is let's do, I don't know, let's prompt for person and we'll prompt for person and prompt for I don't know, microphone.

**Joseph Nelson** [00:00:00] NLASC or microphone. Here I can text prompt the image and then the understanding, in this case Grounding Dino's understanding, of where people are in this image allows me to create, in this case, bounding boxes, but, you know, soon you can do segmentations or in tandem with SAM do segmentations. And, you know, we've already seen applications of using SAM2 in tandem with models like Grounding Dino or Florence 2.

**Joseph Nelson** [00:00:00] So that people can basically text prompt and then get the benefits of the zero shot segmentation at the same time as getting the open form querying. And in doing so, you know, we maintain a framework called like autodistill so like folks can very quickly, you know, bring some images and then using autodistill to find some ontology and then prompt and say what you want from that ontology.

**Nikhila Ravi** [00:00:00] So you already do this for video as well?

**Joseph Nelson** [00:00:00] You can apply videos or groups of images, yes. So this is using a project called Autodistill. And the concept of Autodistill is, use a base model, like a big base model, which could be like SAM or Grounding Dino, and then you pass a directory of images, which also could be video, broken into individual frames, and you pass an ontology as well.

**Joseph Nelson** [00:00:00] So an example I was just showing was like the hello world we have, which is like a shipping container. And then the combination of the grounding capabilities of, in the example I was showing, Florence 2 plus SAM, looks for the concept of container, and then SAM does the rich segmentation of turning that concept of container into the candidate proposal of the region, so that a user could just say, hey, I want all the shipping containers, run this across a bunch of images or video frames, And then get back the class wise labels plus the regions of interest.

**Joseph Nelson** [00:00:00] And this feels like a natural extension. And in fact, like the open form grounding capabilities between SAM1 and SAM2 became something the field was broadly doing. So I'm curious, like, from your perspective, one of the things I thought maybe SAM2 would do is actually add this capability natively. So I'm curious to hear, like, the conscious decision to say, hey, we want to continue to be class agnostic.

## [00:32:39] Extending SAM 2 with other models

**Joseph Nelson** [00:00:00] We don't want to add yet maybe open form text prompting as a part of finding the segments and parts of images. And I'd love to hear about like the decision to think about it that way. And if you are encouraged or if you want kind of like what's happening here where people are naturally combining these capabilities as something that you would expect and encourage to happen despite not having it.

**Joseph Nelson** [00:00:00] In the base model itself.

**Nikhila Ravi** [00:00:00] Yeah, it's a great question. So I think it's really cool that the community is taking SAM and taking SAM 2 and building on top of it and coming up with cool applications. We love to see that. That's exactly why we open source our work. And then in terms of why we didn't put it into SAM 2, so as you've probably seen with SAM and SAM 2, it's a fairly narrow problem.

**Nikhila Ravi** [00:00:00] But we really tried to make it a step change in the capability. And so with each version, we are trying to limit the focus on one thing that we can know we can do really well. And in this case, like the first SAM, it was class agnostic segmentation, but can we do it so well that it's effectively solved?

**Nikhila Ravi** [00:00:00] And similarly, can we do that same thing, but with Video segmentation. So one step at a time, we are working on each of these problems one at a time so that we can actually deliver something that's really world class and step changing.

**Joseph Nelson** [00:00:00] So does that mean SAM 3 will have the text prompting? Problem is like the next challenge.

**Nikhila Ravi** [00:00:00] Who knows, who knows? Maybe the community will, will we'll build that too. So

**Joseph Nelson** [00:00:00] it makes sense to like very narrowly do something very well. And that's, I think, proven to be well accomplished.

**Nikhila Ravi** [00:00:00] It's like taking the, the, both the data, the model and the demo, and how can we push all three towards solving one thing really well?

**Nikhila Ravi** [00:00:00] So we found that. That's like a good recipe and that's what we've limited the focus of these, of each of these models.

**Swyx** [00:00:00] This development reminds me of how, you know, when you do, and you break out the interpretability of ConvNets and you can see like, Oh, this is the edge detection one. I feel like SAM is the edge detection version equivalent.

**Swyx** [00:00:00] And then you build up to whatever the next feature is on top of that.

## [00:34:54] Limitations of SAM: Screenshots

**Joseph Nelson** [00:00:00] Can I bring up one? Limitation of SAM. So like we've like even SAM one, SAM two, and the monitor is released at 4 PM Pacific on Monday. We're recording this on 11 AM Pacific on, on, on Thursday. So the, it's very fresh for a lot of the capabilities and.

**Joseph Nelson** [00:00:00] It is so clear that it is a stepwise change in the capability that, Nikhila, you mentioned your team wants to do, which is extend SAM's zero shot class agnostic capability to video, like, A plus, kind of mission accomplished. One thing that's interesting is finding, like, domain problems where there might be still domain applicability and domain adaptation that is available.

**Joseph Nelson** [00:00:00] One benchmark that we introduced at CBPR is this thing called RF100, which is like, seven different domain type problems that the industry commonly is working on in vision, like underwater document processing, aerial examples, medicine examples. And one place where interestingly segment anything maybe less performant than other models is handling screenshots.

**Joseph Nelson** [00:00:00] For example, like a lot of folks that are building agents to interact with the web are particularly interested in that challenge of given a screenshot of a computer, what are all the buttons. And how could I autonomously navigate and prompt and tell it to click? And I can show an example of like maybe what, how like Sam kind of performs on this challenge just to outline some of the context of this problem.

**Joseph Nelson** [00:00:00] But I'm curious like how you think about limitations like this and what you would expect to want to be the case. So here I just have a notebook where I run Sam on the source image on the left. Or the source image on the left and then Sam output is on the right. And this is just a screenshot of, of a website where we just grab like the top 100 websites by traffic and grab screenshots from them.

**Joseph Nelson** [00:00:00] One example of a place where I could see the community improving on Sam, and I'm curious how you think about this challenge and maybe why Sam is less well adapted for this type of problem. Is processing screenshots. So I'll share my screen to give an example for, for viewers that are participating here, you see like an example, a screenshot of a website on the left, and then right is SAM two running on that image.

**Joseph Nelson** [00:00:00] And in the context of agents, folks usually want to have like, Hey, tell me all of the buttons that a, an agent could press. Tell me like maybe the headlines of the articles tell me the individual images and Sam two behaves perhaps predictably, where it outlines like people in the images and like some of like the, the screen text.

**Joseph Nelson** [00:00:00] I'm curious, like, how you think about a challenge like this for a model that sees everything in the world, what about handling digital contexts? And Why maybe it could perform better here and how you would expect to see improvement for domains that might have been out of distribution from the training data?

**Nikhila Ravi** [00:00:00] Yeah, this is a good question. So fair, we don't really build with a specific use case in mind. We try to build like these foundational models that can be applied to lots of different use cases out of the box. So I think in this kind of example, potentially people might want to annotate some data.

**Nikhila Ravi** [00:00:00] Fine tune on top of what we release. I think we probably won't build things that are very custom for different use cases. I think that's not a direction we'll go in, but as you said, like the model is an annotation tool to improve the model. And so I think that's definitely the approach we want to take is we provide the tools for you to improve the model as well as the model itself.

**Joseph Nelson** [00:00:00] That makes sense. Focus on like as many. Multi or zero shot problems and then allow the community to pick up the torch for domain adaptation.

**Nikhila Ravi** [00:00:00] Yeah, absolutely. Like, we can't solve all the problems ourselves. Like, we can't solve all the different domains. But if we can provide a sort of base hammer tool, and then people can apply it to all their different problems.

## [00:38:48] SAM 2 Paper

**Swyx** [00:00:00] If you don't mind, I guess we want to transition to a little bit on like asking more questions about the paper.

**Udio AI** [00:00:00] Sure.

**Swyx** [00:00:00] There's a lot in here. I love the transparency from Meta recently with like LLAMA 3 last week and then, and was it last week? Maybe, maybe a little bit less than last week. But just like just really, really well written and a lot of disclosures, including the data set as well.

## [00:39:08] SA-V Dataset and SAM Data Engine

**Swyx** [00:00:00] I think the top question that people had on the data set, you know, you release a diverse videos and there was, there's a lot of discussion about the data engine as well, which I really love. And I think it's innovative if you wanted. I think the top question is like, how do you decide the size of data set?

**Swyx** [00:00:00] You know, what were you constrained by? People are asking about scaling laws. You had some ablations, but as a research manager for this whole thing, like how do you decide what you need?

**Nikhila Ravi** [00:00:00] Yeah. I mean, it's a great question. I think it's, as with all papers, you write them at the end of the project, so we can put these nice plots at the end, but going into it, I think, you know, the data engine design really follows.

**Nikhila Ravi** [00:00:00] So, this is sort of the model design, how we thought about the task, how we thought of the model capabilities. You can really see it's reflected in the different phases of the data engine. We started with just SAM, we apply SAM per frame. That's like the most basic way of extending SAM to video. Then the most obvious thing to do is to take the output masks from SAM and then provide it as input into a video object segmentation model that takes the mask as the first frame input.

**Nikhila Ravi** [00:00:00] And that's exactly what we did. We had SAM plus a version of SAM2 that only had mask as input. And then in the last phase, we got rid of SAM entirely and just had this one unified model that can do both image. And video segmentation. And I can do everything in just one model. And we found that, you know, going from each phase, it both improved the efficiency and it improved the data quality.

**Nikhila Ravi** [00:00:00] And in particular, when you get rid of this two part model, one of the advantages is that when you make refinement clicks, so, You prompt the model in one frame to select an object, then you propagate those predictions to all the other frames of the video to track the object. But if the model makes a mistake and you want to correct it, when you have this unified model, you only need to provide refinement clicks.

**Nikhila Ravi** [00:00:00] So you can provide maybe a negative click to remove a region or a positive click to add a region. But if you had this decoupled model, you would have to Delete that frame prediction and re annotate from scratch. And so you can imagine for more complex objects, this is actually adding like a lot of extra time to redefine that object every time you want to make a correction.

**Nikhila Ravi** [00:00:00] So both the data and the data engine phases really follow, like how we thought about the model design and the evolution of the capabilities, because it really helped us to do that. improve the data quality and the annotation efficiency as well.

**Swyx** [00:00:00] Yeah, you had a really nice table with like time taken to annotate and it was just going down and down.

**Swyx** [00:00:00] I think it was like down by like 90 percent by the time you hit stage

**Joseph Nelson** [00:00:00] three, which is kind of cool. We joke that when SAM 1 came out at RoboFlow, we're like, was this purpose built for our software? Like you have like the embedding, you have the embedding take like a big model and the querying of the embeddings A smaller model that happens in browser, which felt remarkably aligned.

**Joseph Nelson** [00:00:00] Now hearing you talk about how you think about building models with a demo in mind, it makes sense. Like, you're thinking about the ways that folks downstream are going to be consuming and creating value. So, what felt like maybe a coincidence was perhaps a deliberate choice by Meta to take into account how industry is going to take Seminal advances and apply them.

**Nikhila Ravi** [00:00:00] Yeah. And it's not just humans. Like it could also be a model that outputs boxes that then get fed into this model. So really thinking about this as a component that could be used by a human or as a component, as part of a, of a larger AI system. And that has, you know, a number of design requirements. It needs to be promptable.

**Nikhila Ravi** [00:00:00] It needs to be, have the zero shot generalization capability. We, you know, need it to be real time and. Those requirements really are very core to how we think about these models.

## [00:43:08] Memory Attention to solve Video

**Swyx** [00:00:00] I cannot end this podcast without talking about the architecture, because this is your, effectively the sort of research level, architecture level innovation that enabled what I've been calling object permanence for SAM.

**Swyx** [00:00:00] And it's memory retention. What was the inspiration going into it? And you know, what did you find?

**Nikhila Ravi** [00:00:00] Yeah, so at a high level, the way we think about extending SAM to video is that an image is just a special case of a video that just has one frame. With that idea in mind, we can extend the SAM architecture to be able to support segmentation across videos.

**Nikhila Ravi** [00:00:00] So this is a quick video that shows how this works. So SAM architecture, we have the image encoder, we have a prompt encoder, we have a mask decoder. You can click on an image. And that basically is a prompt, we use that prompt along with the image embedding to make a mask prediction for that image. Going to SAM2, we can also apply SAM2 to images because we can, you know, as I said, treat an image as a video with a single frame.

**Nikhila Ravi** [00:00:00] And so when we, in the SAM2 architecture, we introduce this new memory mechanism that consists of three main components. There's memory attention, there's a memory encoder, and then there's a memory bank. And when we apply SAM2 to images, these are effectively not used. And the architecture just collapses down to the original SAM architecture.

**Nikhila Ravi** [00:00:00] But when we do apply this to video, the memory components become really useful because they provide the context of the target object from Other frames. And so this could be from past frames. It can be from, there's two types of memory. So there's like the condition, conditional frames or the prompted frames, which are basically the frames at which a user or a model provides input like clicks.

**Nikhila Ravi** [00:00:00] And then there's like the surrounding frames. And say we use six frames around the current frame as memory of the object. So there's, there's those, those, both those types of memory that we use to make the prediction. Going into a little bit more detail about that, there's like two kinds of memory that we use.

**Nikhila Ravi** [00:00:00] So one is like spatial memory. So it's like this high resolution memory that captures the spatial details. And then we also have this like longer term object pointer memory that captures some of the sort of higher level concepts. And I think Swyx, you had a comment about how does this relate to sort of context window and LLMs.

**Nikhila Ravi** [00:00:00] And both of these types of memories have some relation to context window, so they both provide different types of information on the spatial side or in terms of the concept of the objects that we want to track. And so we found that having like six frame length for the spatial memory, Coupled with this longer period of the object pointer memory provides strong video segmentation accuracy at high speed.

**Nikhila Ravi** [00:00:00] So, as I mentioned, the real time aspect is really important. We have to find this speed accuracy trade off. And one way in which we sort of circumvent this is by allowing additional prompts on subsequent frames. So even if the model makes a mistake, maybe it loses the object. After an occlusion, you can provide another prompt, which actually goes into the memory.

**Nikhila Ravi** [00:00:00] And so the prompted frames are always in the memory. And so if you provide a prompt on a frame, we will, or the model will always remember what you provided. And so that's a way in which we can sort of avoid some of the model failure cases that actually is a big limitation of current models, current video object segmentation models.

**Nikhila Ravi** [00:00:00] Don't allow any way to recover if the model makes a mistake. And so, Joseph, going back to your point about the demo, that's something that we found just by playing with these models. There's no way to make a correction, and in many real world use cases, like, it's not going to be a one time prediction, but you actually want to be able to intervene, like, if an LLM makes a mistake, you can actually be like, no, actually do it this way, and provide feedback, and so, We really want to bring some of that thinking into how we build these computer vision models as well.

## [00:47:16] "Context Length" in Memory Attention

**Swyx** [00:00:00] Amazing. My main reaction to finding out about the context length of eight input frames and six pass frames as their default is why not 60? Why not 600? In text language models, we're very used to severely extending context windows. And what does that do to the memory of your model?

**Nikhila Ravi** [00:00:00] So I think maybe one, one thing that's different is that the object in video, it is challenging.

**Nikhila Ravi** [00:00:00] Objects can, you know, change in appearance. There's different lighting conditions. They can deform, but I think a difference to language models is probably the amount of context that you need is significantly less than maintaining a long multi time conversation. And so, you know, coupling this. Short term spatial memory with this, like, longer term object pointers we found was enough.

**Nikhila Ravi** [00:00:00] So, I think that's probably one difference between vision models and LLMs.

## [00:48:09] Object Tracking

**Joseph Nelson** [00:00:00] I think so. If one wanted to be really precise with how literature refers to object re identification, object re identification is not only what SAM does for identifying that an object is similar across frames, It's also assigning a unique ID.

**Joseph Nelson** [00:00:00] How do you think about models keeping track of occurrences of objects in addition to seeing that the same looking thing is present in multiple places?

**Nikhila Ravi** [00:00:00] Yeah, it's a good question. I think, you know, SAM2 definitely isn't perfect and there's many limitations that, you know, we'd love to see. People in the community help us address, but one definitely challenging case is where there are multiple similar looking objects, especially if that's like a crowded scene with multiple similar looking objects, keeping track of the target object is a challenge.

**Nikhila Ravi** [00:00:00] That's still something that I don't know if we've solved perfectly, but again, the ability to provide refinement clicks. That's one way to sort of circumvent that problem. In most cases, when there's lots of similar looking objects, if you add enough refinement clicks, you can get the perfect track throughout the video.

**Nikhila Ravi** [00:00:00] So definitely that's one way to, to solve that problem. You know, we could have better motion estimation. We could do other things in the model to be able to disambiguate similar looking objects more effectively.

**Swyx** [00:00:00] I'm just interested in leaving breadcrumbs for other researchers, anyone interested in this kind of architecture.

**Swyx** [00:00:00] Like, are there papers that you would refer people to that are influential in your thinking or, you know, have, have other interesting alternative approaches?

**Nikhila Ravi** [00:00:00] I think there's other ways in which you can do tracking and video. You might not even need the full mask. I think that's it. Some other works that just track like points on objects.

**Nikhila Ravi** [00:00:00] It really, really depends on what your application is. Like if you don't care about the entire mask, you could just track a bounding box. You could just track a point on an object. And so having the high fidelity mask might not actually be necessary for certain use cases. From that perspective, you might not need the full capabilities.

**Nikhila Ravi** [00:00:00] of SAM or SAM2. There's many different approaches to tracking, I think I would encourage people to think about like what actually they need for their use case and then try to find something that that fits versus, yeah, maybe SAM2 is too much, you know, maybe you don't even need the full mask.

**Swyx** [00:00:00] Makes total sense, but you have solved the problem that you set out to solve, which is no mean feat, which is something that we're still appreciating even today.

## [00:50:44] The Future of FAIR

**Swyx** [00:00:00] If there are no further questions, I would just transition to sort of forward looking, future looking stuff. Joseph already hinted at, like, you know, our interest in SAM and the future of SAM, and obviously you're the best person to ask about that. I'm also interested in, like, How should external people think about FAIR, you know, like there's this stuff going on, this llama, this chameleon, this voice box, this image bind, like, how is, how are things organized?

**Swyx** [00:00:00] And, you know, where are things trending?

**Nikhila Ravi** [00:00:00] Yeah, so in FAIR, we, you know, we have a number of different research areas. I work in an area called perception. So we built vision systems that solve basically, Look at all the fundamental problems in Compute Division. Can we build a step change in all of these different capabilities?

**Nikhila Ravi** [00:00:00] SAM was one example. SAM2 is another example. There are tons of other problems in Compute Division where we've made a lot of progress, but can we really say that they're solved? And so that's really the area in which I work on. And then there's a number of other research areas in language and in embodied AI.

**Nikhila Ravi** [00:00:00] And more efficient models and various other topics. So fair in general is still very much pushing the boundaries on solving these foundational problems across different domains. Well,

**Swyx** [00:00:00] fair enough, maybe just outside of fair, just the future of computer vision, right?

## [00:52:10] CVPR, Trends in Vision

**Swyx** [00:00:00] Like you are very involved in the community. What's the talk of the town at CVPR? Both of you went, who's doing the most interesting work? It's a question for both of you.

**Joseph Nelson** [00:00:00] I think the trends we're seeing towards more zero shot capability for common examples will accelerate. I think Mutu modality, meaning using, you know, images in tandem with text for richer understanding or images and video in tandem with audio and other mixed media will be a continued acceleration trend.

**Joseph Nelson** [00:00:00] The way I kind of see the field continuing to progress, the problem statement of computer vision is making sense of visual input. And I think about the world as the things that need to be observed follow your traditional bell curve, where like things that most frequently exist out in the world are on the center of that bell curve.

**Joseph Nelson** [00:00:00] And then there's things that are less frequently occurring that are in those long tails. For example, you know, as back as like 2014, you have the Cocoa data set, which sets out to say, Hey, can we find 80 common objects in context, like silverware and fridge and these sorts of things. And we also conceptualized the challenge of computer vision in terms of breaking it down into individual task types, because that's like the tools we had for the day.

**Joseph Nelson** [00:00:00] So that's why, you know, you have the origination of classification, object detection, instant segmentation. And then as you see things continue to progress. You have models and things that need to observe areas in the long tails. And so if you think of the Cocoa dataset as the center of that bell curve, I think of like the long tails, like really edge case problems.

**Joseph Nelson** [00:00:00] Some of our customers like Rivian, for example, only Rivian knows what the inside of like a Rivian should look like as it's assembled and put together before it makes its way to a customer and they're making custom parts. Right? So how could a model you've been trained on the things that go inside the componentry of producing a vehicle and Andreesen, What's kind of happening with computer vision is you're seeing models that generalize in the middle of the bell curve push outward faster.

**Joseph Nelson** [00:00:00] That's where you see the advent of like open text models or the richness of understanding of multimodal models. To allow richer understanding without perhaps any training, or maybe just using pre training and applying it to a given problem. And then, there's like, you know, kind of like the messy middle in between those two, right?

**Joseph Nelson** [00:00:00] So like, Akila kind of talked about examples where SAM does well out of distribution, where like, it finds an octopus, even though there wasn't octopi in the training data. I showed an example where, like, screenshots, where Sam isn't yet super great at screenshots, so maybe that's, like, in the messy middle or in the longer tails for now.

**Joseph Nelson** [00:00:00] But what's going to happen is there needs to be systems of validating the point of view that I think about, like, tooling to also validate that models are doing what we want them to do, adapting to datasets that we want them to adapt to. And so there's a lot of things on a forward looking basis that allow propelling that expansion of generalizability.

**Joseph Nelson** [00:00:00] That's for open text problems. That's where scaling up of training, of dataset curation, continues to play a massive role. Something that's notable, I think, about SAM2 is it's, what, 57, 000 videos? 51,

**Nikhila Ravi** [00:00:00] 000 videos? About 51, 000, yeah.

**Joseph Nelson** [00:00:00] And 100, 000 internal datasets. That's, like, not Massive, right? And the model size also isn't, you know, the largest, largest model being a couple hundred million parameters.

**Joseph Nelson** [00:00:00] The smallest model is 38 million parameters and can run at 45 FPS on an A100, right? Like the capabilities of, we're going to see more capable, more generalizable models. Being able to run on a higher wide array of problems with zero or multi shot capability on a faster, a faster rate. And I think the architecture innovations and things like SAM2 of memory, of increasingly like transformers making their way into division and probably blended architectures increasingly too.

**Joseph Nelson** [00:00:00] So my viewpoint of like on a go forward basis is we will have that bell curve of what humans can see both in the center of that curve and the long tails. And architectural changes allow richer understanding, multi and zero shot, and putting those into systems and putting those into industry and putting those into contexts that allow using them in practical and pragmatic ways.

**Joseph Nelson** [00:00:00] Nicola, I'd love to hear like your thought and perspective of like how you think the research trends map or don't map to that. And like maybe some of the key innovations that you saw at CVPR this year that, you know, Got you excited about the direction and maybe some promising early directions that you're thinking about researching or pushing the boundaries of further.

**Nikhila Ravi** [00:00:00] Yeah, I just wanted to actually reply to a couple of things that you said about so actually in video object segmentation, the number of classes. that are annotated in these, and then the size of these datasets are really small. So with SAM, it's, you know, we had a billion masks, we had 11 million images, didn't have class labels.

**Nikhila Ravi** [00:00:00] But even before that, there were a lot of datasets that have class labels and are annotated. With significantly more with, with like a lot of class labels, whereas in video datasets, the number of class labels are very small. So there's like YouTube VOS, which has 94 object categories, there's Mose, which has around like 30 or so object categories.

**Nikhila Ravi** [00:00:00] And they're usually like people, there's cars, there's dogs and cats and all these common objects, but not really, they don't really cover a very large number of object categories. And so while Sam learned this general notion of what an object is in an image. These video tracking models actually don't have that knowledge at all.

**Nikhila Ravi** [00:00:00] And so that's why having this data set is really important for the segment anything capability in video because if you just provide the mask as the input to an off the shelf Video object segmentation model. It might not actually be able to track that arbitrary object mask as effectively as a SAM2 model that's actually trained to track.

**Nikhila Ravi** [00:00:00] Any object across the entire video. So doing these sort of combining two models together to try to get a capability that will actually only get you so far and being able to actually create that the dataset to enable that anything capability, it was actually really important and we can actually see that when we do comparisons with baselines where we provide some two with the same input mask and the baseline model with the same input mask.

**Nikhila Ravi** [00:00:00] For example, the t shirt of a person, SAM2 can track the t shirt effectively across the entire video, whereas these baselines might actually start tracking the entire person, because that's what they're used to doing, and isolating it to just one part of the person is not something they were ever trained to do, and so those are sort of some of the limitations.

**Nikhila Ravi** [00:00:00] Another thing is, Segmenting an image and segmenting a video frame are actually two different things. So a video frame is still an image, but there might be motion blur, or it might have lower resolution. Or there's actually, we found that when, in the SAM2 paper, we have this study of where we look at the Sam image segmentation task on images and also on frames from videos.

**Nikhila Ravi** [00:00:00] And we find that actually SAM2 is a lot better than SAM when it comes to segmenting objects in video frames. Because they actually have a sort of slightly different distribution than images. And so I think that's maybe one learning from this project, is like combining two models and sort of just smushing things together might not actually be as effective as if you really think about how to build things in a, in a unified way.

**Nikhila Ravi** [00:00:00] And then another really interesting. The point is that from the COCO dataset, the last author, Piotr Dola, he's the head of our research group. And so he's really seen the whole decade of going from COCO to going from SAM to going from to SAM2. And so that's been very interesting to have that perspective as we build these models and as we think about the type of capabilities we want to build.

**Joseph Nelson** [00:00:00] We hosted this challenge at CBPR when we introduced RF100. Which is kind of meant to be the anti Cocoa. So if like Cocoa is common objects in context, RF100 is like novel objects in weird contexts, like thermal data and like aerial stuff, and you know, things we were talking about earlier. And so we challenged the community as a part of, it's called OD& W with Microsoft, Object Detection in the Wild.

**Joseph Nelson** [00:00:00] And it's basically like how well can you create models that either work zero shot, But really kind of what you end up measuring is how well things can learn domain adaptation. Like how quickly can something be retrained or fine tuned to a given domain problem. And what's really impressive about SAM and SAM2 from what you just described is even with the limited set, the class agnostic approach affords the generalizability even to Out of distribution examples, surprisingly well, like it's, it's like remarkably robust.

**Joseph Nelson** [00:00:00] And so that research direction seems extremely promising.

**Nikhila Ravi** [00:00:00] Yeah, and actually Piotr is always telling us, like, don't care about Coco, even though he built Coco. So that's, that's always fun. And really keeping that zero shot real world use cases in mind as we build and try to do things. In as general a way as possible.

## [01:01:49] Calls to Action

**Swyx** [00:00:00] Okay, I think that just leaves us to calls to action for engineers, researchers, and personal recommendations. What do you have?

**Nikhila Ravi** [00:00:00] Yeah, so please try out all the resources we put out. We, you know, open sourced the SAV dataset, SAM2, various SAM2 models, the paper. The demo, the dataset visualizer, please try all of these things that we've released.

**Nikhila Ravi** [00:00:00] And also, as I said, DSAM2 isn't perfect, there are a number of limitations. Actually, in the blog post, we go through many of these in quite a lot of detail with examples. And so, if you have any ideas of how to improve these, like, please build on top of what we've released. We would love to see some of these problems get solved.

**Nikhila Ravi** [00:00:00] And, You know, maybe we can incorporate them back into, to future model versions. So really cool to, you know, use them too for all your different use cases, build on top of it, improve it, and, you know, share what you've built back with us. We'd love to hear from you.

**Swyx** [00:00:00] Lovely. We'll definitely want people to comment and share their, Buildings on SAM and SAV and all the other stuff that's going on.

**Swyx** [00:00:00] Thank you so much for your time. This is a wonderful and obviously the incredible open source that you've given us. Joseph, thank you as well for guest hosting. It was a much better episode with you than without you. So appreciate both of you coming on in. Whenever SAM 3 is out or whatever else you guys are working on, just let us know and we'll come back on again.

**Nikhila Ravi** [00:00:00] Thank you. Bye.
