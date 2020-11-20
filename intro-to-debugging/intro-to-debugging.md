# Intro to Debugging

## Introduction

Imagine finishing a coding exercise. You had to loop through an array and print out the numbers 1-5. You run your Python program, and there it goes... printing... `1`...`2`...`3`...`16`... What?! That's not what's supposed to happen.

Didn't you write all the code you needed to? Did you forget something? Or did you add too many things? Is the syntax correct?

When you're in this state, we tend to scramble, and try to retrace our steps... or undo the last 30 minutes of our life.

Sometimes, your program isn't doing what it should be doing, and you stare at the code and you're unsure about what part of the code isn't correct.

In programming, [debugging](https://en.wikipedia.org/wiki/Debugging) is the process of finding and resolving bugs (defects or problems that prevent correct operation). If we have a set of steps and tools to help us resolve bugs, we'll have a cleaner, more effective, and happier process to writing good software.

## Learning Goals

By the end of this lesson, we will be able to...

- Apply the model of "What, Why, How" to debug
- Use techniques to print a variable's value to a console as a form of debugging
- Define rubber duck debugging
- Explain how rubber duck debugging can help debug logic

## Vocabulary and Synonyms

| Vocab | Definition | Synonyms | How to Use in a Sentence
| --- | --- | --- | ---
Debugging | The process of identifying and removing errors from computer hardware or software | Fixing, inspecting | "I need to debug my view and figure out why it wasn't displaying right," "Have you tried to debug your error?"

## Debugging is a Way to Ask and Answer Questions

When we encounter a bug, debugging should be our way of asking and answering the following questions, typically in this order:

1. **What** is happening? What did we expect to happen? What actually happened?
2. **Why** is this happening? What line(s) of code are making this happen?
3. **How** do we fix it? What do we need to change, add, or delete about our existing code?

If we approach debugging as a way to ask and answer questions, it'll make it smoother for us to work through, and easier for others to help us.

## Generic Debugging Steps

Now that we have a general set of questions and order to debugging, here is a generic set of steps to follow for each bug:

### What is happening?

1. What is the bug? How are you observing it?
2. When you observe the bug, what things are true? What is the value for each variable that is relevant? How do you know that is true? Have you confirmed that it's true?

### Why is this happening?

3. What is the most specific piece of code that does something different than what you expect it to do? **What is the expected result, and how does it compare to the actual result?**

### How do we fix it?

4. Come up with a theory of what is happening and why it's happening
5. Test your theory by trying one approach to fix it!
6. Document what you tried and what the results were... Probably on a piece of paper or a separate file.
7. Repeat this process until the bug is fixed!

True or false: It is okay to come up with theories about the bug and to test & experiment, as long as you document what you tried and what the results are in your notes

## Debugging is Utilizing Your Tools and Resources

What is debugging? Debugging is not only asking and answering questions, but also it's using your tools and resources to ask and answer questions.

We will learn **many** different debugging tools and strategies over time, and you will develop your own favorite debugging strategies. Today, we will introduce the following tools and resources:

1. Reading the Stack Trace
1. Using `print`
1. Rubber Ducking

### Reading your Errors and Stack Trace Closely

When we come across errors, we should take notes of three things:

1. What is the description of the error
2. What is the name of the error
3. What is the line number of the error

<!-- ![Screenshot of two windows: One is a .rb file with a bug, and one is Terminal running the file, and showing a NameError](images/intro_debugging-stack_trace.png) -->

From this example, our answers are:

<!-- 1. Description of the error: `undefined local variable or method 'world'`
2. Name of the error: `NameError`
3. Line number of the error: `hello_world.rb:2`, so line 2 -->

When we start to take notes about the errors, we'll start to see patterns, and be able to debug them faster.

### Confirm Your Values with `print`

Variables and their values change over time, during one program. When the computer starts reading code from the top, line-by-line, and then different pieces of data are flying all over the place, we can get lost.

It's important to predict accurately what the value of any given variable can be on a given line.

**If you find yourself unsure of what a variable's value is on a given line, it's important to confirm it, because that may be the source of your bug!**

To verify the value of any given variable on any given line of code, one thing we can do is use `print` and check our output from the Terminal.

We can often use the line `print(f"The value of the variable is: {variable}")`

<!-- ![One window with Ruby code with a bug, and one window with terminal showing that bug](images/intro_debugging-puts_1.png)

![One window with Ruby code with a bug and a lot of puts statements, and one window with terminal showing those puts statements](images/intro_debugging-puts_2.png)

If you observe the process in the images above, we'll see that using `puts` statements helps us see the bug more clearly, and points us closer to where the bug occurs. -->

## Make `print` work for you

Make the `print` lines helpful to you! Sometimes there's a lot of text to read, and it's hard to actually see it.

Programmers are funny, and often write statements like this:

```python
print("*****************************************")
print(variable)
print("*****************************************")
```

or

```python
print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
print(variable1)
print(variable2)
print(variable3)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
```

Don't be afraid to make your `print` statements your own!

### `print` Can Take As Many Comma-Separated Values You Give It

The `print` function can actually print as many values as you give it. It will separate these values by spaces.

Just be sure to take note of the syntax: inside of the parentheses in `print()`, we should separate each value with a comma.

For example, observe this code:

```python
variable_message = "variables"
print("We", "can", "give", "this", "many", "strings", "or", variable_message, "or", "expressions:", 4+3, len("rainbow"))
```

More practically, we might use it like this:

```python
apples = "red"
oranges = "orange"
blueberries = "blue"

print("apples is:", apples, "oranges is:", oranges, "blueberries is:", blueberries)
```

### Rubber Ducking

[Rubber Duck Debugging, or Rubber Ducking](https://en.wikipedia.org/wiki/Rubber_duck_debugging) is a method of debugging code. It describes the idea that sometimes the best way to debug code is to talk things through out loud, and that sometimes talking out loud to a rubber duck will do.

Sometimes, the solution to your problem is solved just by trying to explain your code out loud.

The idea of Rubber Ducking is common and often joked about, to the point that many software development teams will provide literal rubber ducks to developers.

## All Together: Ask and Answer Questions with Debugging

When we combine all these concepts, we get:

- a generic flowchart of how to debug, and what questions to ask and answer
- a generic set of some debugging tools to help us ask and answer those questions

We can even break it up this way:

1. Figure out **what** is happening
    - Use your error messages and `print` statements
2. Figure out **why** it's happening
    - Use `print` statements, rubber ducking skills, and other future debuging tools
3. Figure out **how** to fix it
    - Make theories and then test them!
    - Use rubber ducking skills, experimentation, research, and ask for help!

In conclusion, debugging is one of the main things we'll be doing as programmers. We will learn so many more debugging tools in the future!

## Check for Understanding

Select all methods that are valid ways to approach debugging


* Asking "what" is happening
* Talking to a literal rubber duck
* Talking to a classmate
* Writing down what you expected to happen vs. what actually happened
* Taking a break and looking at it again in an hour
* Using `print` statements to confirm the value of a variable on a given line
* Making theories and experiments on why the bug is there and how to fix it
* Taking notes about the bug
* Making a table or diagram


* Asking "what" is happening
* Talking to a literal rubber duck
* Talking to a classmate
* Writing down what you expected to happen vs. what actually happened
* Taking a break and looking at it again in an hour
* Using `print` statements to confirm the value of a variable on a given line
* Making theories and experiments on why the bug is there and how to fix it
* Taking notes about the bug
* Making a table or diagram

