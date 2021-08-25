# Debugging Continued

## Introduction

Early on in our programming journey we all discover that we spend a lot of time debugging!  When it comes to debugging, there are a few traps that new programmers sometimes find themselves in.

__My code doesn't work, I must be bad at programming!__

*It's a trap!*  The reality is ALL CODE HAS BUGS!  The term __bugs__ comes from the earliest days of computer science when actual insects could get into the inner workings of computers and gum things up!  From those early days, programmers have used the term bugs to describe errors and problems in our code.

No matter how long we've been programming, our code will have bugs!  Nobody writes perfect code.  Learning to effectively debug our code is perhaps the most important skill that we will need to learn to be a successful developer.  

*Ways to free ourselves from the trap:* Approach code with the perspective that it will have bugs.  Our job as programmers isn't to write perfect code, it's to write buggy code and then fix it!  Mistakes and failure are an important part of the process of writing code.

__My code isn't doing what it's supposed to be doing!__

*It's a trap!*  Our code is doing __exactly__ what it's supposed to be doing because that's all it can do!  Ada Lovelace, namesake of our school, wrote about this very thing in 1843 in her notes on "Sketch of the Analytical Engine invented by Charles Babbage":

... Granted that the actual mechanism is unerring in its processes, the *cards* may give it wrong orders. [source](https://en.wikisource.org/wiki/Page%3AScientific_Memoirs%2C_Vol._3_(1843).djvu/708)

The cards that she is referring to are what are supplying the "Analytical Engine" with it's operating instructions.  Our code works in the same way, the computer follows the instructions exactly as written.

*Ways to free ourself from the trap:* Think of ourselves as a detective.  Our first task in debugging is to figure out exactly what our code is doing.  That can be hard to do if we're focused on what our code isn't doing!  First, we need to ask ourselves the questions "What is my code doing?" and "Why is it doing this?".   Once we've answered those two questions, we can move onto "How do we fix our code?".

## Finding Bugs

The first step in debugging is the detective step, the *What* and *Why* of bugs.  Here is a list of practical steps that we can take to help identify the what and why of our bugs:

* Google Errors
* Add Print Statements
* Comment Out Code and Add It Back Line by Line
* Use a Debugger

### Google Errors.

Every language handles errors differently.  Python has a decent error naming system and even provides line numbers for errors.  That doesn't mean it's always easy to see what's causing an error!  Chances are, if we're getting an error, someone else has gotten a very similar error.  One of the great things about being a programmer is that there is a large online community of people who share programming information and are willing to help each other.  If we're not sure what our error means, we can start by looking it up!  Drop the entire error message into a search bar and see what comes up.  Often we'll find someone with a very similar error and while we might not find an exact solution to our problem, we'll likely find things to try.

### Add Print Statements.

When we're debugging, more information is key!  The more information we have, the easier it will be to identify where problems are coming from.  Adding print statements all over code is a simple way to quickly pull more information out of code.  

Unsure of where to start adding print statements?  Use this list as a jumping off point:

* At the beginning of each function.
* Before return statements, print out the value that is being returned.
* Inside of loops.
* After important variable assignments, print out the value of the variable.

In addition, make print statements easy to read.  Printing out a variable is good, but printing out the variable name along with the value is even better!

### Comment Out Code and Add It Back Line by Line.

Sometimes it's hard to know where to start looking for a bug.  Sometimes an error doesn't quite make sense and it's not clear where it's coming from.  Commenting out code is a great way to remove big chunks so that we can slowly start re-adding things one small piece at a time.  Combining this with print statements to verify that each line is behaving as expected is a great way to work through code line by line.

### Use a Debugger.

A debugger is like print statements magnified!  A debugger will allow us to walk through our code line by line and see the value of each variable at each step.  

[TODO: Debugger Video](Debugger Video)


## Fixing Bugs

Once we have a handle on what our code is doing, it's time to look at the last question in debugging, "How do we fix our code?".  We suggest these strategies as places to start when fixing bugs:

* Make the Bugs Smaller
* Check for Logical Errors
* Verify Library Functions
* Take a Break
* Try Something

### Make the Bugs Smaller

Once we accept that our code will have bugs, our goal can shift from writing code without bugs to writing code with bugs that are easier to fix.  One important way to do that is to catch bugs early when they are small.  It's much simpler to debug one function than it is to debug a series of functions with bugs that compound together.  We recommend adding these practices:

*  Test Early and Often.
Rather than writing long blocks of code and then trying to test and run things, test code after each small chunk of code that is added.  Use print statements to verify that variables have the expected data and loops are running as planned.  A function doesn't have to be finished to test it!

*  Use Helper Functions.
Tracing a problem through long functions can be very time consuming and frustrating.  Breaking code into smaller named chunks makes it easier to read through code and figure out where problems are coming from.  Smaller functions are also easier to test and verify, so they can be eliminated as potential sources of bugs.

### Check for Logical Errors

Minor errors often have big consequences.  Many bugs can be found in the small details.  Start by checking things like:

* Conditional statements - are they testing for the correct thing?  Are less than, greater than, nots, etc, all in the correct order?
* Are loops running the correct number of times?
* Are counters being incremented/decremented properly?
* Are variables changing in the correct or incorrect places?  
* Is something being added when it should be subtracted?

Errors like these sometimes hide in plain sight!

### Verify Library Functions

Some of the hardest bugs to find are the bugs that result from calling functions incorrectly.  The code looks like it should work, but it just doesn't!  Maybe the function doesn't return what we assume it does, or handles the inputs different than we expect.  Taking a minute to read the docs about a function may save hours of debugging time.

### Take a Break

There are times when we find ourselves staring at code feeling frustrated and confused, and the most useful thing to do is to take a break.  Walking away from a problem may seem counterintuitive to solving the problem, but it is an important part of debugging!  

Walking away makes it possible to come back with new eyes and see things from a fresh perspective.  It gives us time to rest and refresh ourselves.  Coding is hard work, and it's hard to do our best work when we're exhausted.  It's important that we give ourselves permission to take the breaks that we need to be effective.

### Try Something

Writing code isn't about writing perfect code.  It's about writing broken code and debugging it.  Similarly, debugging code isn't about applying a perfect solution to a problem.  It's about attempting many solutions, some of which may not work!  Sometimes the most important thing is to try many things and see what happens.  A simple way to test a solution is to copy the section of code and comment it out so that it's easy to see the previous version, and then make a minor change to the code and then see what happens.  Often times debugging is about making many small changes that get a little bit closer to the end goal with each step.

## Summary

There is no such thing as writing perfect code!  We will always have bugs in our code.  Becoming better programmers is not about writing better code, it's about becoming better debuggers.

Debugging code is about figuring out:

* What our code is doing?
* Why our code is doing what it's doing?
* How we can fix our code?

## Check for Understanding
<!-- Question Takeaway -->
<!-- prettier-ignore-start -->
### !challenge
* type: paragraph
* id: 4c986d86-1d8b-4aff-b6d5-9ebf5101fced
* title: Debugging Continued
##### !question

What was your biggest takeaway from this lesson? Feel free to answer in 1-2 sentences, draw a picture and describe it, or write a poem, an analogy, or a story.

##### !end-question
##### !placeholder

My biggest takeaway from this lesson is...

##### !end-placeholder
### !end-challenge
<!-- prettier-ignore-end -->