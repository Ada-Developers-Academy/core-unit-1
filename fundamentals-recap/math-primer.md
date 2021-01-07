# Math Primer

## Goal

Problem-solving in programming is almost always centered on _data_. Often times, it's useful to be aware of the following math concepts. Knowing the definition of these concepts can become tools you remember to use in the future.

The goal of this document is to be a resource. We recommend spending your energy on this document reading through it and taking notes on it once, and then reviewing briefly every few months.

This document covers the following:

Thinking about numbers:

1. Decimal Number System
1. Using _n_ as a Variable in Math
1. Coordinate Planes

Working with collections of numbers:

1. Maximum and Minimum
1. Sorting
1. Average or Mean
1. Floor and Ceiling Functions

## Decimal Number System

The _decimal number system_ or _base-ten number system_ is the numbering system most humans use in everyday life.

This numbering system includes - ten unique symbols known as digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 - the decimal point (floating point/dot) symbol to represent decimal fractions, such as 2.45

### !callout-info

## Origin of Base 10

"Legend says" that most base-ten systems possibly originate from counting on ten fingers.

### !end-callout

## Using _`n`_ as a Variable in Math

When we describe problems, we might want to say, "any number of things."

For example, we might be building an email webapp, and we want to say, "An email can have any number of recipients... It can have 1 recipient, 3, 13, or 50 recipients."

We wouldn't want to say "An email can have infinite recipients," because that just may not be true. However, when we want to discuss numbers of things, we may start to use variables as we talk.

We can imagine a variable _`n`_ as the name of a variable that holds any number.

We could also use variable names _`x`_, _`y`_, _`tacocat`_, or whatever is most appropriate in the situation, but _`n`_ is a good default.

Examples of using _`n`_:

- "We have a bug with sending emails. If every email has one sender and _`n`_ recipients, let's check if one or _`n`_ emails were sent."
- "Our feature is good at sending emails to _`n`_ recipients when _`n`_ is 1-99, but have we checked if our feature works when _`n`_ is zero?

## Coordinate Planes

A coordinate plane is a representation of a two-dimensional space.

Coordinate planes help us solve problems where we need to consider points that have a location in a 2D space.

2D space means that we define locations with _**two**_ axes that cross each other. These two axes are typically named _`x`_ and _`y`_.

If you've seen certain kinds of bar graphs or line graphs, and there's a horizontal x-axis, and a vertical y-axis, this is the exact same concept.

## Maximum and Minimum

The **maximum** value in a list of numbers is the largest value in the list.

The **minimum** value in a list of numbers is the smallest value in the list.

Consider the following list of numbers:

```
21, 4, 9, 20, 17, 42, 13, 8.
```

- The maximum value is 42
- The minimum value is 4

## Sorting

Sorting is the action of arranging a list of items following a certain logical pattern. A list of objects that can be ordered may be sorted in **ascending** or **descending** order.

Consider the following list of numbers:

```
21, 4, 9, 20, 17, 42, 13, 8.
```

When the objects are _ordered from lowest value to highest value, the sorting order is said to be in ascending order_. In our example, that would be `4, 8, 9, 13, 17, 20, 21, 42`.

When the objects are _ordered from highest value to lowest value, the sorting order is said to be in descending order_. In our example, that would be `42, 21, 20, 17, 13, 9, 8, 4`.

We can also sort things other than numbers, like words. Programming the logic for how to sort words must be very precise.

For example, the list

```
banana, strawberry, coconut, apple
```

sorted in **ascending** order is

```
apple, banana, coconut, strawberry
```

## Average or Mean

The **average** or **mean** of a collection of numbers is the sum of the numbers divided by the total count of numbers.

"Average" and "mean" are synonymous.

For example, given the list

```
42, 14, 73, 5, 10
```

1. Sum of the numbers: 144
1. Total count of numbers: 5
1. Sum / Total count: 144 / 5
1. Average or mean: 28.8

## Floor and Ceiling Functions

Given any number _`n`_...

- The **floor** of _`n`_ is the biggest integer that's less than or equal to _`n`_
- The **ceiling** of _`n`_ is the smallest integer that's greater than or equal to _`n`_

| Example | Floor | Ceiling |
| ------- | ----- | ------- |
| 2.4     | 2     | 3       |
| 58.7    | 58    | 59      |
| 10.99   | 10    | 11      |
| 10.01   | 10    | 11      |
| -2.4    | -3    | -2      |
| 2       | 2     | 2       |

## Check for Understanding

<!-- Question 1 -->
<!-- prettier-ignore-start -->
### !challenge
* type: ordering
* id: EQ4kZ3
* title: Math Primer
##### !question

Order the definitions below so that they match this order of vocabulary words, from top-to-bottom:

1. Decimal Number System
1. _`n`_
1. Coordinate Planes
1. Floor
1. Ceiling

##### !end-question
##### !answer

1. A counting system based around ten and the digits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
1. A common generic variable name for a number
1. A 2D space where points can be placed using x and y coordinates
1. The biggest integer that's less than or equal to _`n`_
1. The smallest integer that's greater than or equal to _`n`_

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->