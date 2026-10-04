# The Self-Driving Company — Transcript (2026-07-19)

https://aidailybrief.ai/e/2026-07-19 · Listen: https://pod.link/1680633614

---

[00:00:00] Today on the AI Daily Brief

260719 in_EDIT: What it means for AI to create self-driving companies. The AI Daily Brief is a daily podcast and video about the most important news and discussions in AI. 

AI. All 

260719 in_EDIT: right, friends, quick announcements before we dive in. First of all, thank you to today's sponsors, Robots and Pencils, Blitzy, Section, and Airtable.

To get an ad-free version of the show, go to patreon.com/aidailybrief, or you can subscribe on Apple Podcasts. To learn more about sponsoring the show, send us a note at sponsors@aidailybrief.ai.



260719 in_EDIT: This is of course a weekend episode, a big thing/long reads episode. and the CEO of Replit just dropped a great big think piece. So let's dive in 

260719 lrs_EDIT: Welcome back to the AI One of the things that is happening, and really has been happening all year is that AI has advanced in such a way that it's no longer just making us rethink how we do work on an individual level or even a team level, but is starting to implicate the entire design of the company itself

people, some of the [00:01:00] experiments that people have been really excited about this year

are things like Pulsia

which started as a framework for entirely no human companies, and that has evolved a bit 

to be a new AI native company operating system 

that dramatically minimizes the base activation energy neededto build and maintain a company, even if it doesn't require there being no humans at all.

But it's not just totally new efforts that are seeing the impact of new agentic ways of working

In fact As cool as some of these brand new startup style experiments are, 

ultimately their examples can be a little bit hard to see how they apply to today's existing companies. 

which is why it's really interesting to see when companies that are at least slightly larger, even if one might still consider them startups

are sharing their totally new ways of working that are, well, working. this, we got a great example of this last week when Replit CEO Amjad Masad published a new post called The Self-Driving Company

I'm going to read that blog post from X, and then we'll come back and talk about some of the implications

The self-driving company. We're beginning to see what happens when a company [00:02:00] learns to operate itself. In the past six months

Engineers at Replit have nearly tripled code output. Review times held steady. Reversions and product incidents have stayed flat. Quality metrics improved and releases have accelerated. All the typical trade-offs you might expect have not occurred. While the code is the visible part, what's happening under the surface is much more interesting.



260719 lrs_EDIT: agents now investigate production incidents, review pull requests, answer questions, analyze business data, triage support tickets, 

research sales accounts, and improve the systems that power Replit Agent itself. It feels like a single master intelligence threaded through every employee, even though it is not.

It is an expanding system of agents operating across the company, taking goals from people, gathering context, performing work, checking the results, and escalating when human judgment is needed. We think this represents the beginning of a new kind of organization, the self-driving company. A self-driving company is not one without people.

People still choose the destination. [00:03:00] They decide which problems matter, make difficult trade-offs, exercise taste, and take responsibility for the outcome. But increasingly, they do not perform every step required to get there. The shift began late last year. Like many people working in AI, we returned from the Christmas break feeling that something fundamental had changed.

Models could sustain work over much longer horizons. 

Tasks that 

had repeatedly failed, like alert triage and root cause investigation, began working. AI started solving some of our most stubborn bugs. We stopped treating agents as tools that lived inside an editor or chat window. We wove them carefully into the fabric of the company itself.

Once engineering proved the value, adoption took on a life of its own. Team after team started offloading their most tedious work, reclaiming time for the strategic and creative thinking that actually moves the business. People don't feel like they've been automated.

They feel like they've been promoted. This is the story of how AI has completely changed the way that we work at Replit

Engineering saw the impact first. In late [00:04:00] January, we turned up infrastructure to experiment with internal agent use cases quickly

We leveraged our agent harness, microVMs, and remote file systems infrastructure so any engineer could orchestrate swarms of agents in parallel. Then we locked the whole thing behind access policies, token proxies, audit logging, and our zero trust network

At that point, we felt safe giving the agent access to all the things we use to get our jobs done: GitHub, GCP, Azure, Linear, Notion, Slack, Zendesk, and more

With context across systems, we saw a leap forward in productivity. Experiments that previously failed became easy. impact was in coding stats. We were in a sprint week leading up to Agent release in March, where we typically see a big spike. Meetings disappear, scope is known, and engineering shifts into pure execution mode, often for up to 16 hours per day.

But this time was different. Our productivity curve bent upward in a way none of us had seen before, which can be traced to the adoption of our new internal agentic system. From early January to late June, [00:05:00] increase in the lines of code contributed

Part of this increase can be attributed to hiring well. Our new agent accelerates time to productivity, which is great, but we can remove the hiring effect for cleaner data. Keeping a consistent cohort of authors, we see two point nine X as much code as before. Traditionally, it's considered excellent if you keep output per engineer flat as you scale a team.

We just tripled per engineer rate while doubling the team now you might wonder who is reviewing all this new code and whether we've created 

a new bottleneck in the review process. Our code latency is flat

largely because we put our agent to work in reviewing code. It's now able to assess risk levels and only call in a second human reviewer when necessary. That means 30% and growing of human PR review time has been saved

With our agent writing and reviewing more code, we should be worried about quality. If we look at PR reversion rates and incidents opened, trends are flat. This means we're actually improving on a relative basis. One reason is that these processes are also agent-assisted. Human [00:06:00] code reviews have the benefit of an agentic co-reviewer, so more bugs get caught.

Incident investigations, i.e., meaningful bugs or actual incidents, are assisted by an agent that attempts to find the root cause, so mean time to mitigation or MTTM is going down. The final test is whether additional code inputs represent real value output. at the end of the day, engineering is delivering features for users.

We track projects in Linear so that sales and marketing teams know when to communicate with users about new features. You can see the rate of project completion is sharply up along with our coding volume. Conclusion: A self-driving engineering team can ship more while raising quality at the same time

Section. Our agent of agents is enabling loop engineering at scale Zooming in gives us an idea of what this looks like. When engineers find ways to generate loops, sending a fleet of agents off to complete a verifiable task, we see the most dramatic change. Every employee gets access to a manager agent that can spawn multiple agents, enabling orchestration of [00:07:00] agents working in loops on your behalf Loops, loops result in some very unique-looking PR graphs.

One engineer completed a long-stalled migration of our CSS system and shared his learnings. Another engineer automated a migration that enabled us to localize the product. yet another automated flaky test maintenance. Our CTO finally cracked one of our hardest networking bugs related to PSC and FT shutdown with a swarm of agents. All of our assumptions about what is possible have changed

The The most exciting self-driving example comes from our AI team. They built a continual learning system that analyzes user feedback, proposes improvements, and uses a combination of benchmarks and A/B tests to validate the wins. Replit Agent is self-improving



260719 lrs_EDIT: section. The build versus buy conversation has changed. Our new internal agent also changed conversations about whether we build or buy software. We regularly try out new AI tooling. Buying solutions can help us go faster, and we also assess the market constantly. But the more we build, the less [00:08:00] of this we will need to do.

Our internal agent now outperforms products we test that are seen as market-leading. We just churned a seven-figure SaaS solution because our internal app, built entirely in Replit, was superior 

and employees had migrated over. All of a sudden, tools feel like they are built for us. The deep integration with our knowledge bases and customization we've done makes other solutions feel inferior.

What surprised us more was that our internal agent also beat out vertical-specific products we evaluated. A tool to help engineers 

triage alerts, 

and root cause incidents came back with similar 

quality, but at 10X the cost of running it on our agent.

A tool that runs automated penetration testing found fewer vulnerabilities than our internal version at 10X higher cost. Both our versions were put into production with ease, 

reducing MTTM in incidents and hardening critical systems against attacks

With how much we're still learning and how models are improving, it's clear this is only the beginning

Section: Beyond engineering and into the whole business. A self-driving company doesn't stop at engineering. Every function at Replit is [00:09:00] changing. Usage spread quickly out of engineering, mostly because of a Slack interface. The rest of the company noticed engineers tagging our agent with tasks and tried it for themselves.

Initially, the most popular use case was asking questions. By combining our knowledge base with the state of the code base, anybody could clarify product expectations without waiting for engineering input. Those employees could then fix copy or documentation as a follow-up. It was an immediate boost in being able to respond to users faster.

But that was just the beginning. From there, contributions of new skills and integrations started to come in from all parts of the company. The The first big unlock came from our data team. They gave the agent a semantic layer over our data warehouse, so it knows which tables are sources of truth and how they relate to one another

Now anyone at Replit can ask business intelligence questions and get a reliable answer. They can build charts and presentations from live data. The data team spends its time going deeper on the hardest problems instead of fielding requests

Recently, a PM was able to self-serve complex launch analysis Because our agent understands [00:10:00] events in the code base, how they show up in our customer data platform, and how to join those with complex subscription states.

Sales found the same leverage. The sales development team uses the agent to find and enrich product qualified leads, drawing on internal knowledge that more generic tools can't see, so outreach lands with more context

Account executives use it to prepare for customer conversations to understand who is getting the most value, what projects are most active, and how credit usage tracks against their contract. This is all then packaged up into branded slides customized to the account.

A self-driving sales team has more higher quality touch points with their customers

Our marketing team can use the agent to draft product specs from scratch with a single prompt. Based on conversations and documents produced across engineering and product. This gives them the ability to start moving on launches sooner and stay up to date without needing to be in every single meeting.

They have more time to plan and be creative, which will ensure our releases have greater impact when they are out in the world

Our support team gave the agent skills to investigate issues and follow standard playbooks. It can choose to [00:11:00] offer a response in our standard customer service voice or escalate to engineering along witha summary of the ticket and investigation. A self-driving support team closes the hardest tickets, those escalated to humans, sixty percent faster.

Users get back to building sooner. In every example, the human didn't get automated out. They got promoted. Self-driving turns doers into directors, and the people thriving are the ones who think in outcomes and set directions. That is the most valuable work there is now. Where to next? making ourselves more productive is exciting, but what really motivates the people at Replit is democratizing technology.

We want to bring this new way of working to all of our users. We're hard at work making sure we can do this with the policy, permission, security, and cost controls needed to deploy this at scale. Replit's most active users are entrepreneurs and enterprise users building real businesses.

Nathaniel Whittemore: That's S-E-C-T-I-O-N ai com.

260719 lrs_EDIT: All [00:15:00] right. All right. So I think this is both a super interesting case study

But also even more than that, frankly, a really interesting new mental model for how to think about company building

So let's talk about a number of different takeaways

And things that you, as a person thinking about how your company can become more self-driving, can take away from this post The first part, I think, is the way that you think about what AI can do in general. and to move out of thinking about AI as something that can change how individuals or even small teams work, and instead assume that the true implications of this technology are huge structural change to how work gets done This is easy to say but hard to do in practice.

We are wired by decades of doing things in certain ways to evolve only incrementally. But the implications here are not incremental evolutions. they are massive shifts in the very nature of what it means to work and what our relationship to work is, and in some ways, we have to continually hold that as the implications and goal Rather than something to be frankly [00:16:00] scared by.

Next, I think one of the most reasonable questions to come out of this 

is, 

is this for engineering native organizations only? So much of what Amjad talked about is specific to the work of software development. And given that Replit's business not only requires software development, but is in fact providing software development to everyone, There's even more of a reasonable question here, I think, about whether this is limited 

to engineering-led organizations, let's say.

I wanna come back to that question in a minute, but I will say that no matter what, one takeaway which was explicit at Replit, is to start with engineers. That is not only because they're more comfortable with this technology than others, but because the domain in which they work 

has clear structure around it in a way that some other categories of work 

is going to have a harder time with

This I think is fairly intuitive, but to put a fine point on it

When something is wrong with your marketing campaign

It very well might be intangible. A weird feeling about how a certain word or phrase hits that doesn't really comport with the [00:17:00] brand identity that you've been working to build which you know as a marketer and a brand guardian upon seeing it, but which wouldn't necessarily be easy for an AI to pick up itself that there was a problem.

soft- compare that to a software bug, where when the code runs, it does something verifiably wrong. That bug is gonna be much easier for AI to fix

than the much more intangible marketing issue

And while I don't believe 

that 

that means 

that this sort of self-driving should be engineering only, it certainly does make sense to start experimenting with this process in the place where it is most natively fertile, which is going to be with engineers

Now, wherever you start, one of the most important pillars that Amjad almost breezes past too quickly is the fact that the fundamental prerequisite for all of this is not just having an agent that can do stuff for you, it's having that agent or those agents integrated with all of your existing systems.

This goes way beyond having access to good structured data. it is full on cross-org

Context, tool, and system [00:18:00] integration

Amjad talks about engineering giving access to GitHub, GCP, Azure, Linear, Notion, Slack, Zendesk, and more

Without access to the systems that drive the company, there is no way for an agent to help the company become self-driving, period, full stop g-, now both upstream and downstream of that systems access are going to be things like security issues that need to be solved themselves but that systems access has to be assumed as a prerequisite.

Now, Now, speaking of upstream and downstream problems, the next takeaway I think is that new problems will emerge even if overall the system is unlocking new opportunities

post, to take an example from the Replit case study, when you're producing new code, that's a whole lot of new code to review. Now Amjad talked about how they built a new review process that was agent integrated as well, solving the issue and in factimproving PR review time.

But that doesn't mean that that wasn't a new problem to be solved. It just means they solved it I think many organizations that try to move towards this self-driving modality 

will get stopped when they realize that by [00:19:00] moving to this agentic way of working, they're not giving up on problems.

They're switching the problems that they have to deal with. Now, of course, the trade-off is that hopefully those new problems, once solved

are either A, better problems to be solving, or B 

Nathaniel Whittemore: Problems that 

260719 lrs_EDIT: once solved are in service of a better way of working that is soclearly and self-evidently better that it's worth doing. But self-driving does not mean no problems. It means new problems



260719 lrs_EDIT: okay, so you've now assumed huge structural change, you've started with your engineers, you've given systems access, and you've accepted that there will be new problems that emerge that need to be solved.

How do you then move from the engineering section of their organization to others? Another thing that stood out from this post is that their approach was clearly pull, not push In other words, 

by using public spaces like Slack for engineers to interact with the new self-driving system, they allowed others from other parts of the organization to see the benefits of those interactions

without, it seems at least, 

demanding that they dive all the way in before being convinced

I think we sometimes underestimate how valuable it is to [00:20:00] show not tell when it comes to the benefits 

of new big structural changes. 



people inherently, especially outside of engineering but not exclusively, are going to be in many cases reluctant to change.

That is just human nature and it's certainly enterprise inertia

But by creating spaces where people can see not only the results of that new way of working, but how the work actually proceeds itself, a lot of that skepticism can be dealt with in advance

Now once people outside of engineering do start to get interested They, like engineering, are also going 

to have 

to have their systems wired together. and in some cases, this is going to be a technical process. while it might be second nature for engineers to be able to give these new agentic systems access to the right APIs, that might not at all be intuitive or even technically feasible for these other teams.

One pattern that I think is going to be increasingly important and valuable is the pairing of engineers, especially engineers who have already gone through this sort of change, 

with parts of the business organization that can use their help to set up the new way of working

I think as important as forward deployed engineers are, internally [00:21:00] deployed engineers are going to be every bit, if not more important when it comes to this full-scale structural change that's happening

but once the systems and data sources that have all the context come online, those non-engineering teams are still gonna need support designing the types of loops that can actually result in true self-driving

love,

now I love this blog post, I think it's great. But if there's a place that I would like to see it push even farther it's actually deepening this analogy of self-driving. about, Amjad is talking about agents taking on a lot of new work

But self-driving isn't just about agents doing work. It's about a pattern 

in which agents have their goals set by people, have access to the systems and data they need

to do the things that are required to achieve those goals and have the criteria

to see how what they're doing

is actually achieving those goals or not. we, now this is what we talk about when we talk about loops. But the reason that loops aren't just a buzzword is that more than anything else

they're this interaction pattern 

of structuring goals, 

with verifiable endpoints so that agents can do more work on their [00:22:00] own. the-- And where I think loops jump from just being an individual or team process 

to actually being the underpinning of a self-driving company

is when they're given the access

to the ongoing continuously updated flow of customer information 

that allows the goals of the loops to evolve in real time

think-- this is why Amjad said that the most exciting self-driving example came from their AI team, who built a continual learning system to analyze user feedback, propose improvements, and use a combination of benchmarks and A/B tests to validate the wins. That, I think, is the best example of full self-driving as I imagine it from the entire article

Now, outside of that full self-driving mode, it's clear that one of the other benefits to doing this, and one of the reasons to perhaps dig into this if you are exploring it 

is the recognition of just how much Every team's work

is to greater or lesser extent being a bottleneck for other teams

Now, the classic example of this is all the non-engineering teams needing engineering to build something, but every team gets called on by every other team

to ask for things or get access to updated information or

get [00:23:00] aligned with goals And I think a big value of this sort of self-driving idea is to allow teams to stop being bottlenecks for one another by having a lot of that operational flow run through agents instead

Now it is worth noting once again that Replit is in a unique position to be doing a lot of these experiments. again, not only are they a software company, they're a software company that builds tools for building software.

They are in the eye of this storm like no one else

But a lot of the solutions that they built for themselves, are going to be productized

And by the way, I assume that a lot of them are gonna be productized by Replit themselves But still I can

see a lot of executives reading this and thinking to themselves, "

Well, 

we don't have the engineering organization that can actually go build tools that could compete with SaaS."

But I don't think you're going to need to, and I think it would be a mistake to not at least explore thinking in this self-driving way because you don't think you have the engineering resources or wherewithal to do so. is... I think that to the extent that we find that the self-driving mode for companies actually produces these sort of gains across lots of different types of companies, that there is such an incredible market [00:24:00] incentive to productize parts of that process, that you have to assume that over the next, honestly, six to 12 months, all the pieces will find their way into some tool somewhere

In other words, I think you can assume That if you start to wander down this road, even if you have severe limitations in your engineering organization, there will be answers to those particular problems

Now, we started with a mindset takeaway, we're gonna end with a mindset takeaway. I think ultimately this is all about changing our assumptions about what is possible

A lot of these things will look like increased lines of code and decreased timelines for new features, 

improved resolution rates on customer support, and all of that at least at the beginning But if we can really set up looping systems, especially that interact with not only the inside of the company, but outside the company as well, the rate at which companies can evolve and improve will be totally different a few years from now than it is today

That is, yes, going to create all sorts of new challenges, but they pale in comparison to the opportunity. And I'll tell you what, if you are listening to this right now, you are in a unique position to be [00:25:00] one of the people and one of the leaders and one of the companies that takes advantage of that before everyone else



260719 lrs_EDIT: so now as we wrap up, go ask your agent to schedule a meeting with all of your top execs about what self-driving means in the context of your company And then tell me what you figure out so I can do a follow-up to this episode. For now, that's gonna do it for today's AI Daily Brief. Appreciate you listening or watching as always, and until next time, peace 

​ 

Nathaniel Whittemore's audio recording:
