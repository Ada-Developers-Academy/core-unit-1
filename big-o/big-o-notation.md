# Big O Notation

## Learning Goals

- Define Big O Notation
- Recognize Big O notation and the common complexity categories: constant, logarithmic, constant, loglinear, quadratic, exponential
- Compare and rank the common complexity categories between least and most complex

## Introduction

Imagine that we're developers working on a unique project: we are writing software not for a laptop, but something much smaller! Imagine we're coding for an Arduino microcontroller, which has very little RAM. It's entirely possible that our program would crash if it takes up too much memory.

Let's imagine that we could write our Arduino program with two different solutions. We know that we should compare the space complexity between the two algorithms. However, **_how_** do we compare space complexity?

Computer science uses concepts from mathematics to measure time and space complexity. By using Big O notation, we can concretely evaluate which is more efficient. Then, our program will work better on the Arduino!

## Vocabulary and Synonyms

| Vocab | Definition                                                                                           | Synonyms | How to Use in a Sentence                                                                                                                                     |
| ----- | ---------------------------------------------------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Big O | A notation to describe **how** the run time or space requirements grow as the input size grows | -        | "The Big O of the linear search algorithm is O(n) ("O of n"), or linear," "The Big O of "n log n" is less complex than Big O of "n squared," so it's better" |

## Big O Describes How Complexity Grows

Big O Notation, pronounced "Big Oh notation," is a notation style that describes **how** the run time or space requirements grow as the input size grows.

The formal definition of Big O Notation is rooted in mathematics: Big O Notation "describes the limiting behavior of a function when the argument tends towards infinity." Let's parse this language:

- The "function" is the algorithm
- The "argument" is likely the input data set that the algorithm operates on
- "tends towards infinity" describes that we are considering all hypothetical situations... We consider the complexity when the argument (i.e. the input) is:
    - a million rows long
    - a million + 1 rows long
    - a million + 2 rows long
    - ... all the way towards infinity
- "Limiting behavior" describes the rate at which complexity grows. Sometimes, as the argument grows bigger and bigger, the complexity grows rapidly! Sometimes, as the argument grows, the complexity grows slowly.

This limiting behavior is the most important information; we are looking for a mathematical expression to describe the growth of complexity.

To quantitatively represent the worst case performance for speed and memory utilization of an algorithm, we use the Big O notation. Leveraging big O notation, we can:

- Make quantitative judgments about the efficiency of one algorithm over another
- Predict whether the software will meet any efficiency constraints that exist

## The Notation Itself

This is an example of Big O notation:

> O(n)

Details:

- `O(...)` is the recognizable form of Big O notation
- Inside the parentheses is some mathematical expression that describes the relationship between the size of the input vs. the complexity of the algorithm

Overall, the contents in between the parens is the information we care most about.

## The Common Curves

These are common Big O complexities to be familiar with.

These complexities are ordered! We can describe their order in all of these ways:

- going from least complex to most complex
- going from fastest to slowest in time complexity
- going from least operations to most operations in time complexity
- going from most space efficent to least space efficent in space complexity
- going from slower-growing to faster-growing

| Complexity       | Name        | Definition                                                                                                                                                                                                                                                                                    |
| ---------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| O(1)             | Constant    | The algorithm will take the same amount of time to execute regardless of the size of the input.                                                                                                                                                                                         |
| O(log n)         | Logarithmic | The algorithm will grow in complexity proportional to the base 2 **log** of the input size. Logarithmic algorithms increase **very** slowly as the size of the input increases. They usually involve an algorithm which excludes 1/2 of the input with each iteration of a loop. |
| O(n)             | Linear      | The algorithm will grow in time or space directly proprotional to the input size. The complexity increases at the same rate that the input increases.                                                                                                                                         |
| O(n log n)       | Log Linear  | A term used to describe an algorithm which will grow in time or space complexity proportional to the n log n of the input size. "n log n" means that the input size is multiplied by the base-2 log of the input size.                                                                                                                                                              |
| O(n<sup>2</sup>) | Quadratic   | The algorithm will have a runtime or memory usage proportional to the size of the input squared. This often involves 2 nested loops.                                                                                                                                                    |
| O(2<sup>n</sup>) | Exponential | The algorithm's complexity doubles each time the input size increases by one.                                                                                                                                                                                                                 |

### !callout-info

## How do we say it out loud?

Developers talk about Big O a lot, so it's useful to know how to talk about this out loud. Here are some example sentences to help start the pattern:

- "The Big O of linear search is O of 1. It runs in constant time."
- "An algorithm with a Big O of log n is better than O of n log n."
- "O of n-squared is one of the slowest!"
- "The algorithm does a lot of work on each item in the input, but it's still order n!"

### !end-callout

## Examples

Let's consider and compare some "real-world" algorithms.

Consider this problem: You have an address book, and you want to find the contact information for your friend Taylor.

| Algorithm                                                                                                                                                                                                                                                                                                   | Big O    |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| Start at the first page of the address book. Read through each page. If you see Taylor's name, you found their phone number                                                                                                                                                                                 | O(n)     |
| Assume your contacts are alphabetically sorted. Flip to the half-way point of the address book, then determine which half of the address book "Taylor" is in. Then look through that half of the address book, split that in half, and determine which half to look through. Do this until we find "Taylor" | O(log n) |
| Use a bookmark you inserted before that is labeled "Taylor", that leads straight to Taylor's phone number.                                                                                                                                                                                                  | O(1)     |

## Check for Understanding

<!-- Question about comparing Big Os for more efficient -->

<!-- Question about comparing Big Os for more efficient -->

<!-- Question about comparing Big Os for more efficient -->
