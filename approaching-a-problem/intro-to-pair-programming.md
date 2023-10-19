# Intro to Pair Programming

## Learning Goals

- Define pair programming and its parts: navigator and driver

## Introduction

Different contexts call for different methods of programming: sometimes it's best to pair, and sometimes it's best to work solo.

![Comic of two coworkers deciding to pair program](../assets/approaching-a-problem_pair-programming_pair-meme.png)  
[(source)](https://www.monkeyuser.com/2020/pair-programming/)


## Pair Programming is Collaborative Problem-Solving

Pair programming is a method of programming in which two people problem-solve together on the same code simultaneously. Typically, during a pair-programming session, the two people trade and alternate the two roles "drive" and "navigator."

The driver is responsible for using the keyboard and mouse. This usually means this person types code and browses through the projects directories and files.

![Comic of two coworkers deciding to pair program](../assets/approaching-a-problem_pair-programming_driver-navigator.jpeg)  
[(source)](https://medium.com/swlh/writing-code-efficiently-with-a-partner-e9c969674a3b)


The navigator is responsible for guiding the problem-solving process. The navigator actively reviews each line of code as it is typed, checks for errors, and thinks about the overall solution and how to get there.

### It Benefits Everyone

Study after study states that software built with the pair-programming process often has higher quality code than code written solo.

![Patrick and Spongebob](../assets/approaching-a-problem_pair-programming_spongebob-patrick.jpg)  
*Fig. A great pair makes a great team* [(source)](https://spongebob.fandom.com/wiki/Patrick-SpongeBob_relationship)


When two people collaborate and pair, it often results in:

- more simple design choices, and more readable code
- fewer bugs and logical errors
- higher morale
- shared knowledge through your team
- accountable time management
- improves focus
- mitigating the <abbr title="How many of your team would have to win the lottery for you to be unable to function?">"Lottery Factor"</abbr> AKA the <abbr title="Like the 'Lottery Factor' but instead they get hit by a bus">"Bus Factor"</abbr>

## The Process of Pair Programming
![Patrick and Spongebob drawing](../assets/approaching-a-problem_pair-programming_collaborative-problem-solving.png)  
[(source)](https://www.facebook.com/patrickstar/photos/pretty-good-spongebob-but-its-lacking-basic-construction-and-your-perspective-le/10151824823840951/)


When two developers begin a session of pair programming, they should begin the process by talking about the goal of the session. **Often, the goal of pair programming is to learn or explore.**

Following these steps can help pairs be aligned and focused:

1. Start with a reasonably well-defined task before you sit down
1. Agree on one tiny goal at a time
1. Rely on your partner, support your partner
1. Talk a lot!
1. Sync up frequently
1. Take a moment to celebrate as you complete tasks and overcome problems
1. Switch roles often - at least every half hour

## Pairing Remotely

Sometimes it won't be possible to pair in person. You may be far away from each other, have transportation issues or there might be a global pandemic.

You can still accomplish pair programming remotely by following the principles above.

There are many software solutions you can use to make remote pairing go smoothly but even something as simple as screen sharing during a video call can do the trick.

You can also use some tools specifically made for remote pairing. If developing in VS Code, [VS Code's plugin Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare) is an example of one of these tools. The Live Share extension allows teams to write code, debug, chat, and have audio calls in Visual Studio Code. Tools like these will make it easier to do hand off between driving and navigating like you would if you were sitting next to each other in person.

![Audrey and Claire on VS Code Liveshare](../assets/approaching-a-problem_pair-programming_vs-code-liveshare.png)  
*Fig. Audrey and Claire collaborating on VS Code* [(source)](https://www.monkeyuser.com/2020/pair-programming/)

### Rotating Roles

It is unhealthy in pair programming to stay in either the driver role or the navigator role for too long.

A common pattern is to set a timer for thirty minutes, and to switch roles every thirty minutes.

## Suggested Readings: Wisdom from the Industry

### How to Improve Pair Programming

#### **Skill Imbalance**

> Most of the time, what looks like a skill imbalance, isn’t. I’m going to argue here that the perception that you are “ahead of” or “behind” your partner is less accurate and less important than it may seem. ... A really important assumption to make is that each person has a lot of value to contribute to the work, regardless of experience or a perception of skill level. Assume that you and your partner are both amazing.
>
> — [Lauren Mendoza, Humans’ Guide to Pair Programming](https://medium.com/@loorinm/pair-programming-b5fa56744a0f)

#### Empathy for yourself and others

> Radical self-acceptance is a skill like any other.
>
> — [Lauren Mendoza, Humans’ Guide to Pair Programming](https://medium.com/@loorinm/pair-programming-b5fa56744a0f)

#### Asking for and Receiving Feedback

> Make eye contact, observe your partner’s body language, tone of voice, and stay silent while they are talking. Repeat their words in your head, and let them sink in. Nod or say “hm” to show that you are actively listening to their words. ...

> It’s normal to feel defensive and to want to show that you haven’t done anything wrong, but realize that’s not needed here. Thank your partner for sharing what most likely was a difficult thing to say. Take some silent time to consider the feedback from a calm place before responding.
>
> — [Lauren Mendoza, Humans’ Guide to Pair Programming](https://medium.com/@loorinm/pair-programming-b5fa56744a0f)

#### Giving Feedback

> Here’s a good format:

> > During **\_**, when you did **\_**,I felt **\_**. In the future, I’d like to try **\_**.
> > Is that something you’d be willing to do?

> Your partner’s answer might be “no”, and that’s totally ok! In that case, accept their answer, ask why, and keeping talking until you can agree on a course of action.
> — [Lauren Mendoza, Humans’ Guide to Pair Programming](https://medium.com/@loorinm/pair-programming-b5fa56744a0f)

### 10 Ways to Improve Your Pairing Experience

![Excited Patrick and Spongebob Raising arms](../assets/approaching-a-problem_pair-programming_improve-pairing-experience.jpg)  
[(source)](https://nerdist.com/article/spongebob-squarepants-spinoff-patrick-star-show/)

1. Do not centralize driving
1. Manage the focus together
1. Avoid working alone
1. Alternate moments of concentration and relaxation
1. Celebrate your achievements!
1. Synchronize with your partner
1. Give context appropriately
1. Learn to deal with disagreements
1. Be ready to learn and to teach
1. Give and receive feedback when you're done

[Tarso Aires, 10 Ways to Improve Your Pairing Experience](https://www.thoughtworks.com/insights/blog/10-ways-improve-your-pairing-experience)

## Check for Understanding

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: short-answer
* id: 4810dbd6-286c-4eb9-976e-4480811114f1
* title: Pair Programming Tools
<!-- * points: [1] (optional, the number of points for scoring as a checkpoint) -->
<!-- * topics: [python, pandas] (optional the topics for analyzing points) -->

##### !question

Describe how [VS Code Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare) works as a tool that enables remote collaborating.

##### !end-question

##### !placeholder

Enter notes here

##### !end-placeholder

##### !answer

/.*/

##### !end-answer

<!-- other optional sections -->
<!-- !hint - !end-hint (markdown, hidden, students click to view) -->
<!-- !rubric - !end-rubric (markdown, instructors can see while scoring a checkpoint) -->
<!-- !explanation - !end-explanation (markdown, students can see after answering correctly) -->

### !end-challenge

<!-- ======================= END CHALLENGE 1======================= -->

<!-- Question 2 -->

<!-- prettier-ignore-start -->
### !challenge

* type: short-answer
* id: dbb0ce80-a6b9-4d5e-bd4e-9f1590ce4d49
* title: Pair Programming Reflection

##### !question

Write a reflection and impression you have about the above material. Include thoughts on feedback and skill imbalance based on the quotes above.

##### !end-question

##### !placeholder

Enter notes here

##### !end-placeholder

##### !answer

/.*/

##### !end-answer

### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question Takeaway -->
<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: 76kaNR
* title: Intro to Pair Programming
##### !question

What was your biggest takeaway from this lesson? Feel free to answer in 1-2 sentences, draw a picture and describe it, or write a poem, an analogy, or a story.

##### !end-question
##### !placeholder

My biggest takeaway from this lesson is...

##### !end-placeholder
### !end-challenge
<!-- prettier-ignore-end -->
