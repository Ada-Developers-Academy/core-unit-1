# How to Read Documentation

## Learning Goals

* Identify parts of programming documentation: Method description, name, parameter list, return value; Method list

## Introduction

Ultimately, we programmers will use functions that others have defined over and over again. But the function bodies and implementations of those functions could be obscured to us! So, if we can't see the implementations of these functions, how could we use them?

We could use these functions by studying the function's documentation. Documentation is a set of text resources whose purpose is to share details of some body of code with others.

Documentation might call the code it's documenting the "API," or Application Programming Interface. This name refers to the fact that we are studying an _interface_, or the specific ways for how to interact with this code.

Examples of functions we could use, but we won't study the implementation (or "source code"):

- Python built-in functions, like `len()` and `type()`
- Functions from a library, such as [`pandas.Series.mad`](https://pandas.pydata.org/docs/reference/api/pandas.Series.mad.html)
- External APIs that enable large audiences to affect a service, such as [Slack's `admin.conversations.unarchive`](https://api.slack.com/methods/admin.conversations.unarchive)

## Vocabulary and Synonyms

| Vocab | Definition | Synonyms | How to Use in a Sentence
| --- | --- | --- | ---
Documentation
Source code
API

## Documentation Varies

When we compare the documentation between the pandas library API and the Slack API, we should see that they're absolutely different in every way:
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

As we know, software changes over time. The codebase from two years ago compared to the codebase today may have the same name, but different functions, implementations, details, and results! A set of docs is often tied to a specific version of that API. The version of the docs you reference _should match_ the version of the library or API you're using.

We can compare the docs between [Python 2](https://docs.python.org/2/library/functions.html) and [Python 3](https://docs.python.org/3/library/functions.html). The docs are visually incredibly different. Through these docs, we can see that there are plenty of differences between Python 2 and Python 3, even though they're both Python. Python 2 has a `cmp()` function, where Python 3 does not. Python 3 has a `bytes()` function, and Python 2 doesn't. The consequences of using mismatched versions of docs and tools could result in a lot of broken code.

Documentation can be huge in size. [Python 3's documentation](https://docs.python.org/3/) has a lot of material to cover, and a lot of sections to help organize them. It's crucial to take the time to understand and navigate the sections intentionally. Sections and words to look out for:

- The word "reference"
- The words "methods" or "functions"
- Sections dedicated to the _kind_ of functionality you're looking for, such as 
- For external APIs, the word "endpoints"

There is a common pattern that the different methods or interesting pages will be listed in a side column, with links to jump to their details. Use this section to help you navigate!

## Look for the Function Signature



## Understand the Examples

### Take Time to Rework the Examples



## Python: You Can Also Rely on `help()`


## Summary

## Check for Understanding


