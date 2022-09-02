# Sort / Lambda

## Learning Goals

* Define lambda functions
* Describe how to use the key parameter in the `sorted` function to sort a list of dictionaries by a specific key

## Introduction

Imagine we have a list of movie titles we'd like to sort alphabetically. Python provides a couple convenient functions for this task. The [`sort`](https://docs.python.org/3/howto/sorting.html#sorting-basics) method can be called on a list and sorts the list in place. The `sorted` function take a list as a parameter and returns the sorted list.  

But what if we have a list of dictionaries representing movies that we want to sort by title, or perhaps by rating. Or perhaps we want to find the most recent movie or oldest movie in a list.

Python provides the `key` parameter for `sorted` function. The `key` parameters takes a function that provides the key to use for sorting purposes. 

In this lesson, we will use the list of movie dictionaries example described above to learn about *lambda expressions* and how they are used with the key parameter in the `sorted` function. 

## Definitions

| Term | Definition | Used in A Sentence |
| -- | -- | -- |
|Lambda Expression | | |

## Movie Example

## Check For Understanding

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: checkbox
* id: be152c53-2f78-40e1-8c6c-9b3f8b086c17
* title: Higher Order Functions
<!-- * points: [1] (optional, the number of points for scoring as a checkpoint) -->
<!-- * topics: [python, pandas] (Checkpoints only, optional the topics for analyzing points) -->

##### !question

Which of the following are true for lambda expressions [reference](https://www.freecodecamp.org/news/lambda-expressions-in-python/)? 

##### !end-question

##### !options

a| [Lambda expressions are also known as anonymous functions]
b| [Lambda expressions only contain one expression]
c| [Lambda functions can only have one argument]
d| [Lambda functions can have any number of arguments]
e| [Lambda expressions are good for chained conditionals with multiple `elif`s]


##### !end-options

##### !answer

a|
b|
d|

##### !end-answer

##### !explanation

The [key](https://docs.python.org/3/howto/sorting.html#key-functions) parameter takes a callable, which can be a named function or a lambda expression.

##### !end-explanation

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: checkbox
* id: c51e0bad-6a27-43d7-acb5-a570c87163d2
* title: Higher Order Functions
<!-- * points: [1] (optional, the number of points for scoring as a checkpoint) -->
<!-- * topics: [python, pandas] (Checkpoints only, optional the topics for analyzing points) -->

##### !question

Which of the following are valid to pass to the `key` parameter in the `sorted` function?

##### !end-question

##### !options

a| [A variable that points to a list of integers]
b| [A variable that points to a list of dictionaries]
c| [A variable that points to a function]
d| [A lambda expression]

##### !end-options

##### !answer

c|
d|

##### !end-answer

##### !explanation

The [key](https://docs.python.org/3/howto/sorting.html#key-functions) parameter takes a callable, which can be a named function or a lambda expression.

##### !end-explanation

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: paragraph
* id: 9ecfb979-f766-49e9-82ca-79e900f57abe
* title: Higher Order Functions
<!-- * points: [1] (optional, the number of points for scoring as a checkpoint) -->
<!-- * topics: [python, pandas] (Checkpoints only, optional the topics for analyzing points) -->

##### !question

What is the benefit of passing a lambda function to the key parameter in the `sorted` function.

##### !end-question

##### !placeholder

The benefit of...

##### !end-placeholder

##### !explanation

Lambda functions provide a succinct way...

##### !end-explanation

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->

