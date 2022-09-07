# Lambda Expressions

## Learning Goals

* Define lambda expressions
* Describe how to pass lambda expressions as a parameter.

## Introduction 

In the previous lesson, we passed a named function to the `key` parameter in the `sorted` function.

In this lesson, we will use the list of movie dictionaries example to learn about *lambda expressions* and how they are used with the `key` parameter in the `sorted` function. 

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

