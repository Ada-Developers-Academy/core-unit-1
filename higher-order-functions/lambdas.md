# Lambda Expressions

## Learning Goals

* Define lambda expressions
* Describe how to pass lambda expressions as an argument to the `key` parameter

## Introduction 

In the previous lesson, we passed a named function to the `key` parameter of the `sorted`, `min`, and `max` functions.

In this lesson, we will continue to use the example of a list of movie dictionaries to learn about *lambda expressions* and how they can be used with the `key` parameter of the `min` function. 

## Vocabulary and Synonyms
| Vocab	| Definition| Synonyms |	How to Use in a Sentence |
|--|--|--|--|
|Lambda Expression| An unnamed function with a any number of arguments and a single expression | Anonymous Function, Lambda Function | Lambda functions can be passed to the `key` parameter in the `min` function. |

## Lambda Expression Syntax

Let's quickly recall the list of movie dictionaries we started working with in the last lesson.

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

And here's the code we wrote using the `key` parameter with named functions to find the movie with the first title alphabetically, the lowest rating, and the earliest release date.

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

Note that the functions `get_title`, `get_rating`, and `get_release_year` are each composed of a single expression. These simple functions are great candidates for lambda expressions.

The syntax for a lambda expression is as follows:

```py
lambda arguments: expression
```

The `lambda` syntax creates a new function object, just like `def` does. However, the function has no name, and no variable is created to refer to it. We should also notice that we do not put parentheses `()` around the arguments list, and that the body is restricted to a single expression. We can still assign the created function object to a variables ourselves, or more commonly, pass it directly as an argument to a higher order function.

When called, the lambda's expression is executed and the result is returned, even though we do not explicitly  write a `return` keyword. [(source)](https://www.w3schools.com/python/python_lambda.asp)

Let's see how we can use this syntax.  In the following code, the function object referred to as `get_title`:

```py
def get_title(movie):
    return movie["title"]
```
is equivalent to the following lambda expression:

```py
get_title = lambda movie: movie["title"]
```

The lambda version of `get_title` can be used in exactly the same way as the version of  `get_title` created using `def`.

```py
get_title = lambda movie: movie["title"]

movie_title = get_title(INTRIGUE_1)

# movie_title = "Recursion"
```

But why would we ever create a function this way, with all the limitations of the `lambda` syntax?

Such small, simple functions are often needed only once, in a small section of logic, usually to customize the behavior of a higher order function. In such cases, we may decide that creating a named object is unnecessary. Instead, we might create this function directly where we call the higher order function.

For example, we can replace the named functions passed to the `key` parameter of the `min` function calls with the following lambda expressions:

```py
first_movie_by_title = min(movies, key=lambda movie: movie["title"])
lowest_rated_movie = min(movies, key=lambda movie: movie["rating"])
earliest_movie = min(movies, key=lambda movie: movie["release_year"])
```

<!-- available callout types: info, success, warning, danger, secondary, star  -->
### !callout-info

## Lambda Expression Usage

Lambda expressions are ideally suited to simple and concise functionality. They can take any number of arguments, but must contain only a single expression.

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

Which of the following are true for lambda expressions? [(reference)](https://www.freecodecamp.org/news/lambda-expressions-in-python/)

##### !end-question

##### !options

a| Lambda expressions are also known as anonymous functions
b| Lambda expressions contain only one expression
c| Lambda functions can have only one argument
d| Lambda functions can have any number of arguments
e| Lambda expressions are good for chained conditionals with multiple `elif`s


##### !end-options

##### !answer

a|
b|
d|

##### !end-answer

##### !explanation

Lambda expressions have no name, making them anonymous. They are restricted to containing only a single expression, but may receive as many arguments as needed to perform their calculation. Chained conditionals are statements (they do not evaluate to a single value), and so cannot be used within a lambda.

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

Which of the following are valid to pass to the `key` parameter of the `min` function?

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

The [key](https://docs.python.org/3/howto/sorting.html#key-functions) parameter takes a reference to something "callable", such as a named function or a lambda expression.

##### !end-explanation

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->