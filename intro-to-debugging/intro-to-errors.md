# Intro to Errors

## Introduction

Frequently, we'll see our programs become broken. They're broken because the program isn't running the way we want them to run. So much of our responsibility as developers is to fix broken code.

Broken code is caused by errors. Understanding more about errors and what causes them will help us debug them.

## Learning Goals

- Define syntax errors, runtime errors, and logical errors

## Vocabulary and Synonyms

| Vocab | Definition | Synonyms | How to Use in a Sentence
| --- | --- | --- | ---
Error | When a program does unexpected things | Bug | "The program had an error, so it stopped running," "I need to find the cause of that error and fix it"
Crash | When a program comes to a halt because of an error | Stopped | "When my code tried to divide by zero, it crashed," "The program keeps crashing whenever I try to run it"
Syntax Error | An error caused by incorrect syntax that Python cannot interpret | - | "I was missing a keyword, so it gave me a syntax error"
Runtime Error | An error raised during runtime | - | "I didn't realize I had a bug until I ran my code and got a runtime error"
Logical Error | An error caused by incorrect logic | - | "I got confused with two variables and swapped them, and it caused a logical error."

## What is an Error?

An error in programming is when a program does unexpected things. Errors are often called bugs.

Errors and bugs can cause all sorts of problems, like programs halting and ending prematurely. When a program comes to a halt because of an error, we say that it has crashed.

### !callout-info

## The Origin of `Bugs`
The term "bug" comes from some interesting history! In 1947, Grace Hopper recorded the first bug. As she and her team worked on the Harvard Mark II, which is an old-school computer that read instructions from physical tapes, there was an error. After some investigation, the team found that the source of the problem was a _**literal bug**_ that got stuck on one of the tapes!

### !end-callout

## Three Kinds of Errors

There are three kinds of errors:

1. Syntax Errors
2. Runtime Errors
3. Logical Errors

### Syntax Errors

A syntax error is a kind of error that occurs when we try to run a program, and it's caused by syntax.

When we run a Python program, the Python interpreter looks through and parses our code first. At that moment, it will check our syntax; if there is syntax that the Python interpreter doesn't understand, then it will raise a syntax error.

Most errors that programmers encounter are syntax errors.

Syntax errors are often caused by things such as:

- missing a keyword
- missing a colon
- missing the end of a brace, like `)`, `}`, `]`, etc
- misspelling something
- accessing a list or dictionary with the wrong syntax
- unmatching indentation levels
- mixed-use of tabs or spaces 

To debug syntax errors, we should review the syntax in our code, and compare it to the syntax that Python is looking for.

### Runtime Errors

A runtime error is a kind of error that occurs while our program is already running.

There are actually plenty of actions that Python programs can't do:

- dividing by zero
- performing an operation on incompatible types
- using an identifier which has not been defined
- accessing a list element, dictionary value or object attribute which doesn’t exist
- trying to access a file which doesn’t exist

When our Python program is running, and it tries to do one of those actions, Python will raise a runtime error.

To debug runtime errors, we should debug and try to understand what is causing the runtime error, and then refactor our code so it anticipates that case.

### Logical Errors

A logical error is a kind of error that occurs when a program produces an incorrect result or outcome.

For example, if we write a Python program that should count the number of letters in the string `"Grace Hopper"`, and it produces the number 13 **instead** of the correct 12, and there are no syntax or runtime errors, then we have a logical error.

Logical errors can happen for an infinite number of reasons, but here are some common causes:

- using the wrong variable name
- incorrect indentation
- not having the correct conditional checks
- [off-by-one errors](https://en.wikipedia.org/wiki/Off-by-one_error)

### !callout-danger

## Be Careful!
As programmers, we will copy and paste a lot. However, when we carelessly copy and paste code, it can often lead to a lot of logical errors. Take care when you copy and paste and be sure to update all of the variable names and syntax... Or even try to type out the code entirely, to help slow you down and follow along!

### !end-callout

## Check for Understanding

What kind of error does the following code produce?

```python
```

* Syntax Error
* Runtime Error
* Logical Error

What kind of error does the following code produce?

```python
```

* Syntax Error
* Runtime Error
* Logical Error


What kind of error does the following code produce?

```python
```

* Syntax Error
* Runtime Error
* Logical Error


What kind of error does the following code produce?

```python
```

* Syntax Error
* Runtime Error
* Logical Error
