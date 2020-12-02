# Big O Notation

## Learning Goals

- Define Big O Notation
- Recognize Big O Notation and common notations: constant, logarithmic, constant, loglinear, quadratic, exponential
- Compare and rank the complexity of the common notations between least and most complex

## Introduction

Imagine that we're developers working on a unique project: we are writing software not for a laptop, but something much smaller! Imagine we're coding for an Arduino microcontroller, which has limited RAM. It's entirely possible that our program would crash if it takes up to much memory.

Let's imagine that we could write our Arduino program with two different solutions. We know that we should compare the space complexity between the two algorithms. However, **_how_** do we compare space complexity?

Computer science uses concepts from mathematics to measure time and space complexity. By using Big O notation, we can concretely evaluate which is more efficient. Then, our program will work better on the Arduino!

## Vocabulary and Synonyms

| Vocab | Definition                                                                                           | Synonyms | How to Use in a Sentence                                                                                                                                     |
| ----- | ---------------------------------------------------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Big O | A notation style to describe **how** the run time or space requirements grow as the input size grows | -        | "The Big O of the linear search algorithm is O(n) ("O of n"), or linear," "The Big O of "n log n" is less complex than Big O of "n squared," so it's better" |

## Big O Describes How Complexity Grows

Big O Notation, pronounced "Big Oh notation," is a notation style that describes **how** the run time or space requirements grow as the input size grows.

The formal definition of Big O Notation is rooted in mathematics: Big O Notation "describes the limiting behavior of a function when the argument tends towards infinity." Let's parse this language:

- The "function" is the algorithm
- The "argument" is likely the input data set that the algorithm operates on
- "tends towards infinity" describes that we are considering all hypothetical situations... We consdier the complexity when the argument being a million rows long a million + 1 rows long, a million + 2 rows long, all the way towards infinity
- "Limiting behavior" describes the rate at which complexity grows. Sometimes, as the argument grows bigger and bigger, the complexity grows rapidly! Sometimes, as the argument grows, the complexity grows slowly.

This limiting behavior is the most important information; we are looking for a mathematical expression to describe the growth of complexity.

To quantitatively represent the worst case performance for speed and memory utilization of an algorithm, we use the Big O notation. Leveraging the big O notation, we can:

- Make quantitative judgments about the efficiency of one algorithm over another
- Predict whether the software will meet any efficiency constraints that exist

## "Syntax"

This is an example of Big O notation:

> O(n)

- `O(...)` is the recognizable form of Big O notation
- Inside the parentheses is some mathematical expression that describes the relationship between the size of the input vs. the complexity of the algorithm

Overall, the contents inbetween the parens is the information we care most about.

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
| O(1)             | Constant    | The algorithm which will take the same amount of time to execute regardless of the size of the input.                                                                                                                                                                                         |
| O(log n)         | Logarithmic | The algorithm which will grow in time or space complexity proportional to the **log** of the input size. Logorithmic algorithms increase **very** slowly as the size of the input increases. They usually involve an algorithm which excludes 1/2 of the input with each iteration of a loop. |
| O(n)             | Linear      | The algorithm will grow in time or space directly proprotional to the input size. The complexity increases at the same rate that the input increases.                                                                                                                                         |
| O(n log n)       | Log Linear  | A term used to describe an algorithm which will grow in time or space complexity proportional to the n log n of the input size.                                                                                                                                                               |
| O(n<sup>2</sup>) | Quadratic   | The algorithm which will have a runtime or memory usage proportional to the size of the input squared. This often involves 2 nested loops.                                                                                                                                                    |
| O(2<sup>n</sup>) | Exponential | The algorithm's complexity doubles each time the input size increases by one.                                                                                                                                                                                                                 |

### !callout-info

## How do we say it out loud?

Developers talk about Big O a lot, so it's useful to know how to talk about this out loud. Here are some example sentences to help start the pattern:

- "The Big O of linear search is O of 1. It runs in constant time."
- "An algorithm with a Big O of log n is better than O of n log n."
- "O of n-squared is one of the slowest!"

### !end-callout

### Examples

Let's consider and compare some "real-world" algorithms.

Consider the problem: You have an address book, and you want to find the contact information for your friend Taylor.

| Algorithm                                                                                                                                                                                                                                                                                                   | Big O    |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| Start at the first page of the address book. Read through each page. If you see Taylor's name, you found their phone number                                                                                                                                                                                 | O(n)     |
| Assume your contacts are alphabetically sorted. Flip to the half-way point of the address book, then determine which half of the address book "Taylor" is in. Then look through that half of the address book, split that in half, and determine which half to look through. Do this until we find "Taylor" | O(log n) |
| Use a bookmark you inserted before that is labeled "Taylor", that leads straight to Taylor's phone number.                                                                                                                                                                                                  | O(1)     |

## Time Complexity: Code to Big O

```
# array is the input integer array to the algorithm

if array.length <= 1
  return # nothing to reverse

i = 0
j = array.length - 1

while i < j
  # swap values at i and j
  temp = array[i]
  array[i] = array[j]
  array[j] = temp

  increment i
  decrement j
```

### Always Looking for the Biggest Big O

Constants are dropped. Constants only shift our graph slightly, but do not affect the overall look of the graph by much. O(2n) is shortened to O(n). O(1⁄2 n) is shortened to O(n).
Usually when an algorithm's growth rate is a mix of orders, the dominant order is shown, and the rest are dropped. O(n^2) + O(n) or O(n^2 + n) would be shortened to O(n^2). This is because O(n^2) + O(n) is smaller than O(n^2) + O(n^2).In other words, O(n^2) + O(n) is in the order of O(n^2) + O(n^2). O(n^2) + O(n^2) can be simplified to O(n^2) _ 2 or O(2 _ n^2). Then, we can drop the constant, and simply state that the complexity is O(n^2).

## Space Complexity: Code to Big O

```
# array is the input integer array to the algorithm

if array.length <= 1
  return # nothing to reverse

i = 0
j = array.length - 1

while i < j
  # swap values at i and j
  temp = array[i]
  array[i] = array[j]
  array[j] = temp

  increment i
  decrement j
```

You must have noticed the three memory allocations done by the program: i, j and temp. These are three integers created. Regardless of the size of the input array (be it 500 or 900,000), there will always be only and exactly three integers created. As such, the new memory allocations in this algorithm do not change as the size or value of the input changes. Such algorithms are said to have constant space complexity or O(1) space complexity.

## Example: Comparing Two Algorithms

These are two algorithms for the same thing. Consider the time and space complexity for each algorithm. Afterwards, we'll compare the two algorithms.

Algo 1

```
# array is the input integer array to the algorithm

if array.length <= 1
  return # nothing to reverse

i = 0
j = array.length - 1

while i < j
  # swap values at i and j
  temp = array[i]
  array[i] = array[j]
  array[j] = temp

  increment i
  decrement j
```

You must have noticed the three memory allocations done by the program: i, j and temp. These are three integers created. Regardless of the size of the input array (be it 500 or 900,000), there will always be only and exactly three integers created. As such, the new memory allocations in this algorithm do not change as the size or value of the input changes. Such algorithms are said to have constant space complexity or O(1) space complexity.

Algo 2

```
# array is the input integer array to the algorithm

if array.length <= 1
  return # nothing to reverse

i = 0
j = array.length - 1

# create a new array of the same size as input array
temp_array = new array of size array.length

while i < array.length
  # copy over the values in input array 
  # into the temp array in reverse order
  temp_array[i] = array[j]
  increment i
  decrement j


i = 0
while i < array.length
  # copy over values from the temp array 
  # into the input array
  array[i] = temp_array[i]

# array is reversed
```

The first while loop copies over each of the elements in the input array into a new array in reverse order of their position. The means, if there are 100 elements in the input array, then the loop will execute 100 times. If there are 700,000 elements in the input array, then the loop will execute 700,000 times and so on. Therefore, we can conclude that in the first loop, the number of operations performed are linearly changing in accordance with the size of the input.
The second loop copies for each element of the temporary array back into the input array. Following the same logic, in the second loop, the number of operations performed are linearly changing in accordance with the size of the input.
The time complexity of each loop is linear, or O(n) where n is the number of elements in the input array. Together, since they perform the operations one after another, the time complexity of the overall algorithm is linear or O(n), where n is the number of elements in the input array.

There are two integers, i and j that are used to index into the arrays. Each of these take up additional memory of the size of an integer each. Also, in addition to the input array, the algorithm creates a new array. This new array, temp_array takes up as much space as the size of the input array. If there are 100 elements in the input array, then the temp_array needs to be able to hold 100 elements. If the input array holds 900,000 elements, then the temp_array should also be able to hold 900,000 elements. In other words, the new temp_array created takes up space that is linearly proportional to the size of the input array. Therefore, the space complexity of this algorithm is linear or O(n), where n is the number of elements in the input array.

### Comparing

Time complexity: As we saw above, Algorithm 1 as well as Algorithm 2, both have the same time complexity. They both execute in linear time as compared to the size of the input, or are said to have O(n) time complexity, where n is the number of elements in the input array. From the view point of time complexity, both the algorithms are equally efficient.
Space complexity: We noted that Algorithm 1 above has a space complexity of O(1) or constant, since the amount of additional memory used does not change as the size of the input array changes. In contrast, Algorithm 2 creates a new array. The size of this new array created is the same as the input array. Therefore, Algorithm 2 has a space complexity of O(n), where n is the number of elements in the input array. Comparing Algorithm 1's constant space complexity with Algorithm 2's linear space complexity, we can conclude that Algorithm 1 is more space efficient than Algorithm 2.
In conclusion, although the two algorithms are equally time efficient, Algorithm 1 is more space efficient as compared to Algorithm 2 and hence, Algorithm 1 is a better choice.

## Check for Understanding


