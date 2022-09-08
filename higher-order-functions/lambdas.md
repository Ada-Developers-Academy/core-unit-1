# Lambda Expressions

## Learning Goals

* Define lambda expressions
* Describe how to pass lambda expressions as an argument to the `key` parameter

## Introduction 

In the previous lesson, we passed a named function to the `key` parameter in the `sorted`, `min`, and `max` functions.

In this lesson, we will use the list of movie dictionaries example to learn about *lambda expressions* and how they are used with the `key` parameter in the `min` function. 

## Vocabulary and Synonyms
| Vocab	| Definition| Synonyms |	How to Use in a Sentence |
|--|--|--|--|
|Lambda Expression| An unnamed function with a any number of arguments and a single expression | Anonymous Function | Lambda functions can be passed to the `key` parameter in the `min` function. |

## Lambda Expression Syntax

In this lesson we will work with the same list of movie dictionaries as the previous lesson:

```py
INTRIGUE_1 = {
    "title": "Recursion",
    "genre": "Intrigue",
    "rating": 2.0,
    "release_year": 1999
}
INTRIGUE_2 = {
    "title": "Zero Dark Python",
    "genre": "Intrigue",
    "rating": 3.0,
    "release_year": 2022
}
ACTION_1 = {
    "title": "2 JavaScript 2 React",
    "genre": "Action",
    "rating": 4.2,
    "release_year": 2015
}
ACTION_2 = {
    "title": "JavaScript 3: VS Code Lint",
    "genre": "Action",
    "rating": 3.5,
    "release_year": 2013
}

movies = [INTRIGUE_1, INTRIGUE_2, ACTION_1, ACTION_2]
```

Let's recall the code we wrote that used the `key` parameter with named functions to find the movie with the first title alphabetically, the lowest rating, and the earliest release date.

```py
def get_title(movie):
    return movie["title"]

def get_rating(movie):
    return movie["rating"]

def get_release_year(movie):
    return movie["release_year"]

first_movie_by_title = min(movies, key=get_title)
lowest_rated_movie = min(movies, key=get_rating)
earliest_movie = min(movies, key=get_release_year)
```

Note that the function `get_title`, `get_rating`, and `get_release_year` all have a single expression. These simple functions are a great candidate for lambda expressions.

The syntax for a lambda expression is as follows:

```py
lambda arguments : expression
```

The expression is executed and the result is returned [source](https://www.w3schools.com/python/python_lambda.asp). Lambda expressions are a single line and they do not use parentheses.

The function `get_title`:

```py
def get_title(movie):
    return movie["title"]
```
is equivalent to the following lambda expression:

```py
lambda movie:movie["title"]
```

As such, we can replace the named functions passed to the `key` parameter in the `min` functions with the following lambda expressions:

```py
first_movie_by_title = min(movies, key=lambda movie: movie["title"])
lowest_rated_movie = min(movies, key=lambda movie: movie["rating"])
earliest_movie = min(movies, key=lambda movie: movie["release_year"])
```

<!-- available callout types: info, success, warning, danger, secondary, star  -->
### !callout-info

## Lambda Expression Usage

Lambda expressions are ideally suited to simple and concise functionality. They can take any number of arguments, but must have a single line expression.

### !end-callout


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

a| Lambda expressions are also known as anonymous functions
b| Lambda expressions only contain one expression
c| Lambda functions can only have one argument
d| Lambda functions can have any number of arguments
e| Lambda expressions are good for chained conditionals with multiple `elif`s


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

Which of the following are valid to pass to the `key` parameter in the `min` function?

##### !end-question

##### !options

a| A variable that points to a list of integers
b| A variable that points to a list of dictionaries
c| A variable that points to a function
d| A lambda expression

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