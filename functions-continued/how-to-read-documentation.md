# How to Read Documentation

## Learning Goals

- Identify parts of programming documentation: Method description, name, parameter list, return value; Method list

## Introduction

Ultimately, we programmers will use functions that others have defined over and over again. But the function bodies and implementations of those functions could be obscured to us! So, if we can't see the implementations of these functions, how could we use them?

We could use these functions by studying the function's documentation. Documentation is a set of text resources whose purpose is to share details of some body of code with others.

Documentation might call the code it's documenting the **"API,"** or Application Programming Interface. This name refers to the fact that we are studying an _interface_, or something specifically designed to allow access to a wide audience.

There are plenty of functions we want to use, but it isn't necessary for us to understand its implementation (or "source code"):

- Python built-in functions, like `len()` and `type()`
- Functions from a library, such as [`pandas.Series.mad`](https://pandas.pydata.org/docs/reference/api/pandas.Series.mad.html)
- External APIs made for exposing a service's data. One example is [Slack's `admin.conversations.unarchive`](https://api.slack.com/methods/admin.conversations.unarchive)

## Vocabulary and Synonyms

| Vocab         | Definition                                                                                                                                  | Synonyms                                                                                     | How to Use in a Sentence                                                         |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Documentation | Any written text, illustrations or video that describe a software or program to its users                                                   | Docs                                                                                         | "We use Python documentation to understand Python functionality in-depth"        |
| Source code   | The original code that creates a program, usually the human-readable version                                                                | Implementation code                                                                          | "It's fascinating to read through Python's source code and see how it was made!" |
| API           | A set of rules and tools that allows software to communicate with other software. Specifically designed to allow access to a wide audience. | "To learn how to interact with the external Slack service, we should look at the Slack API." |

## Documentation Varies

Let's compare the documentation between the pandas library API and the Slack API. We should see that they're dramatically different in a lot of ways:

- how they look
- the literal words
- how the words are structured
- how to navigate the page

Documentation is typically written by the service itself. For example, the documentation for the Twitter API is provided by Twitter itself.

There is no standard for documentation. Because there's no standard, documentation between different libraries and APIs will vary... some will be clear and readable, and others will be obscure or sparse. (Feel free to feel frustrated at this.)

Because documentation varies, there could never be a "right" way to read documentation. Instead, let's cover some pointers and tips. When you need to clarify how to use a function, and you found its documentation:

- Recognize the version of the docs
- Recognize the sections of the docs
- Read through the function signature
- Take time to understand and rework the examples

## Recognize Versions and Sections

As we know, software changes over time. Take one piece of software, and the codebase for it today, compared to the codebase it had two years ago. They may have the same name, but different functions, implementations, details, and results! A set of docs is often tied to a specific version of that API.

The version of the docs you use should **match** the version of the library or API you're using.

### !callout-info

## Example: Comparing Python 2 and Python 3 docs

Let's compare the docs between [Python 2](https://docs.python.org/2/library/functions.html) and [Python 3](https://docs.python.org/3/library/functions.html). The docs are visually incredibly different. We can see that there are plenty of differences between the docs, even though they're both Python. Python 2 has a `cmp()` function, where Python 3 does not. Python 3 has a `bytes()` function, and Python 2 doesn't. The consequences of using mismatched versions of docs and tools could result in a lot of broken code!

### !end-callout

Documentation can be huge in size. [Python 3's documentation](https://docs.python.org/3/) has a lot of material to cover, and a lot of sections!

Commonly, docs reserve a sidebar or column to for navigating different methods and different pages. Use these to help you navigate!

Sections and words to look out for:

- The word **"reference"**
- The words **"methods"** or "**functions"**
- Lists of function names
- Sections dedicated to the _kind_ of functionality you're looking for by it's purpose
- A search bar
- For external APIs, the word "endpoints"

## Look for the Function Signature

Once we find a function we want to study, we should study the function signature defined in the docs.

We should always look for these things:

1. An explanation of the function's responsibility
2. What the function returns
3. An explanation of the parameters
4. Special cases or notes

**Look at this example:** Let's look at the docs for [Python's `sum()` function](https://docs.python.org/3/library/functions.html#sum)

<!-- Written in 2020 with Python 3 docs -->

> `sum(iterable, /, start=0)`
>
> Sums _start_ and the items of an _iterable_ from left to right and returns the total. The _iterable_'s items are normally numbers, and the start value is not allowed to be a string.
>
> ...

From this example:

1. This method is responsible for summing an _iterable_ and a _start_, usually numbers.
2. The function returns the total sum
3. This function always takes in the positional argument `iterable`. It has a _keyword argument_ `start`, which has a default value of `0`.

### !callout-info

## What's with the `/`?

Python docs have a unique pattern: the docs will put a `/` inbetween the positional and keyword arguments

### !end-callout

### !callout-info

## What does _iterable_ mean?

_Iterable_ is a word that describes something valid to iterate over. In general, lists and dictionaries are iterables. For programming words like _iterable_, it's valuable to look up their definitions and examples.

### !end-callout

### !callout-info

## What's with the `*args`?

`*args` is a way to notate a variable number of arguments. It wasn't shown in this example, but it's a good phrase to know.

### !end-callout

## Practice Examples in the REPL

The last step to go from documentation to understanding a function is to read, understand, and play with examples.

Before using a function in your own code, **it is always valuable to play around with examples first.** Playing around with examples _before_ you include a function into your code lessens the frustration of making it work directly in your code.

**Look at this example:** For [Python's `sum()` function](https://docs.python.org/3/library/functions.html#sum), a top Google/Bing/DuckDuckGo/what-search-engine-have-you result for "python sum example" might list this example:

```python
sum([1, 2, 3, 4, 5])
```

With this example, we should make sure we understand how to use the parameters and get the correct return result by:

1. Opening REPL and typing this example
1. Opening REPL and altering this example
1. And/or making a small Python script that uses examples

```bash
# Observe this example Python REPL output
>>> sum([1, 2, 3, 4, 5])
15
>>> sum([1, 2, 3])
6
>>> sum([-1, 100])
99
>>> sum([])
0
```

## Summary

Our summarized workflow for reading documentation:

1. Clarify your goal: What are you researching?
1. Find the right version of docs
1. Navigate the docs
1. Use the docs to understand responsibility, return value, and parameters
1. Practice using the function with examples

Our pro tips:

- Match the version of docs you're using to the version you're using
- Take time to learn how to navigate the docs
- Always play around with examples before using it in your own code
