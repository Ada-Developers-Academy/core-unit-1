# Debugging Continued

## Introduction

Early on in our programming journey we all discover that we spend a lot of time debugging! When debugging, there are a few traps that new programmers tend to encounter.

- My code doesn't work, I must be bad at programming!
- My code isn't doing what it's supposed to be doing!

### My code doesn't work, I must be bad at programming!

#### It's a trap!

The reality is ALL CODE HAS BUGS! Programmers have used the term **bug** to describe a problem in code ever since the earliest days of programming. Back then, it could actually refer to an insect gumming up the inner workings of a computer!

No matter how long we've been programming, our code will have bugs! Nobody writes perfect code. Learning to debug our code is a very important skill. We need to learn how to do it effectively to become a successful developer.

#### Ways to free ourselves from the trap

Approach code with the perspective that it will have bugs. Our job as programmers isn't to write perfect code. Our job is to write buggy code and then fix it! Mistakes and failure are an important part of the process of writing code.

### My code isn't doing what it's supposed to be doing!

#### It's a trap!

Our code is doing **exactly** what it's supposed to be doing because that's all it can do! Ada Lovelace, namesake of our school, wrote about this very thing:

> Granted that the actual mechanism is unerring in its processes, the _cards_ may give it wrong orders.

_Ada Lovelace from her notes on "Sketch of the Analytical Engine invented by Charles Babbage" (1843)_ [source](<https://en.wikisource.org/wiki/Page%3AScientific_Memoirs%2C_Vol._3_(1843).djvu/708>)

The **cards** in that passage supply the "Analytical Engine" with its operating instructions. Our code works in the same way. The computer follows the instructions exactly as written.

#### Ways to free ourselves from the trap

Let's think of ourselves as detectives. Our first task in debugging is to figure out exactly what our code is doing. That can be hard to do if we're focused on what our code _isn't_ doing!

First, we need to ask ourselves the questions, "What is my code doing?" and, "Why is it doing this?" Once we've answered those two questions, we can move onto, "How do we fix our code?"

## Finding Bugs

The first step in debugging is the detective step, the _What_ and _Why_ of bugs. Here is a list of practical steps that we can take to help identify the what and why of our bugs:

- Search for Errors with Google
- Add Print Statements
- Comment Out Code and Add It Back Line by Line
- Use a Debugger

### Search for Errors with Google

Every language has a different approach to error handling. Python has descriptive error names and even provides line numbers for errors. That doesn't mean it's always easy to see what's causing an error. But chances are, if we're getting an error, someone else has gotten a very similar error in the past!

Programmers are part of a large, helpful online community. We love sharing programming information with one another! This is one of the great things about being a programmer!

If we're not sure what our error means, we can start by looking it up! Drop the entire error message into a search bar and see what comes back. Often we'll get a result with a very similar error message. Sometimes we'll find the exact solution to our problem. But even if we don't, we can get a list of things to try!

### Add Print Statements

When we're debugging, more information is key! The more information we have, the easier it will be to identify where problems are coming from. Adding print statements to our code is a quick way to gather more information about the problem.

Unsure of where to start adding print statements? Use this list as a jumping off point:

- At the beginning of each function
- Before return statements, print out the value that is being returned
- Inside of loops
- After important variable assignments, print out the value of the variable

Additionally, make print statements easy to read. Printing out the value of a variable is good, but printing out the variable name along with the value is even better!

### !callout-info

## Use Python f-strings to Print Expressions

Since Python 3.8, we can add an equals sign `=` at the end of a format expression to make Python print the expression that was within the curly braces `{}`. For example:

```python
my_str = "Hello, Python!"
print(f"{my_str=}")  # prints my_str='Hello, Python!'
print(f"{3+4=}")  # prints 3+4=7
```

### !end-callout

### Comment Out Code and Add It Back Line by Line

Sometimes it's hard to know where to start looking for a bug. Sometimes an error doesn't quite make sense and it's not clear where it's coming from.

Commenting out code can help us narrow in on the problem! We start by commenting out a large chunk of code until the problem goes away. Then, we un-comment our code a small piece at a time until the problem returns.

We can combine this strategy with print statements to verify the behavior of each line. With this approach, we can work through our code line by line.

### Use a Debugger

A debugger is like print statements magnified! A debugger allows us to walk through our code line by line and see the value of each variable at each step.

[TODO: Debugger Video](Debugger Video)

## Fixing Bugs

Once we have a handle on what our code is doing, it's time to look at the last question in debugging, "How do we fix our code?" We recommend these strategies as places to start when fixing bugs:

- Make the Bugs Smaller
- Check for Logical Errors
- Verify Library Functions
- Take a Break
- Try Something

### Make the Bugs Smaller

We know that we are going to write code with bugs. This lets us shift our goal from writing code without bugs, to writing code with bugs that are easier to fix.

One important way to write bugs that are easier to fix is to catch bugs early, when they are small. Finding a single bug in a single function isn't always easy. But finding several bugs across many interacting functions is much harder.

We recommend adopting these practices:

- Test Early and Often

  Test code after adding each small chunk. Doing so lets us focus on a small area of code rather than dealing with a large, complex block.

  We can use print statements to verify that our variables have the expected data. We can also check whether our loops are running as planned. Remember, a function doesn't have to be complete to be testable!

- Use Helper Functions

  Tracing a problem through long functions can be very time consuming and frustrating. Breaking code into smaller named chunks makes it easier to read. This can help make problems easier to notice.

  Smaller functions are also simpler to test and verify. This lets us quickly eliminate them as potential sources of bugs.

### Check for Logical Errors

Minor errors often have major consequences. Many bugs take refuge in the small details of our code. Start by checking things like:

- Conditional statements—are they testing for the correct thing? Are less thans, greater thans, nots, etc, all in the correct order?
- Are loops running the correct number of times?
- Are counters incremented or decremented as needed?
- Are variables changing in the correct or incorrect places?
- Are we adding somewhere when we should be subtracting?

Errors like these sometimes hide in plain sight!

### Verify Library Functions

Some of the hardest bugs to find are the bugs that result from calling functions incorrectly. The code looks like it should work, but it doesn't!

Sometimes the function doesn't return what we assume it does. Sometimes it handles the inputs different than we expect.

Taking a minute to read the documentation about a function may save hours of debugging time.

### Take a Break

Sometimes we find ourselves staring at code feeling lost, frustrated, and confused. When that happens, the most useful thing to do is to take a break! Walking away from a problem may seem counterproductive to finding a solution. Even so, it's an important part of debugging!

Walking away makes it possible to come back with new eyes and see things from a fresh perspective. It gives us time to rest and refresh ourselves. Coding is hard work, and it's hard to do our best work when we're exhausted. It's important that we give ourselves permission to take the breaks that we need to be effective.

### Try Something

Writing code isn't about writing _perfect_ code. It's about writing broken code and debugging it. In the same way, debugging code isn't about applying a _perfect_ solution to a problem. It's about attempting many solutions, some of which may not work!

Sometimes the most useful thing to do is to try many things and see what happens. First, make a commented copy of the problematic code for reference. Then make a small change to the code and see what happens!

Debugging is often the art of making many small changes that get a little bit closer to the end goal with each step.

## Summary

There is no such thing as writing perfect code! We will always have bugs in our code. Becoming better programmers is not about writing better code, it's about becoming better debuggers.

Debugging code is about figuring out:

- What our code is doing
- Why our code is doing what it's doing
- How we can fix our code

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
