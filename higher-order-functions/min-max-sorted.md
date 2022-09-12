# Passing Functions as Arguments: Min, Max, and Sort

## Learning Goals

* Demonstrate how to pass a function as an argument
* Describe how to use the key parameter in the `sorted` function to sort a list of dictionaries by a specific key
* Describe how to use the key parameter in the `min` function to find the minimum in a list of dictionaries by a specific key

## Introduction

Imagine we have a list of movie titles we'd like to sort alphabetically. Python provides a couple convenient functions for this task. The [`sort`](https://docs.python.org/3/howto/sorting.html#sorting-basics) method can be called on a list and sorts the list in place. The `sorted` function takes a list as a parameter and returns the sorted list.  

But what if we have a list of dictionaries representing movies that we want to sort by title, or perhaps by rating. Or perhaps we want to find the most recent movie or oldest movie in a list.

Python provides the `key` parameter for `min`, `max`, and `sorted` functions, just to name a few. The `key` parameters takes a function that provides the key to use to indicate which attribute to use for finding the minimum, finding the maximum, or to sort. 

## Movie Example

### List of Movie Titles

Let's consider to the following list of movie titles.

```py
movie_titles = [
    "Recursion",
    "Zero Dark Python",
    "2 JavaScript 2 React",
    "Javascript 3: VS Code Lint"
]
```

To sort the titles alphabetically in place we can use `sort` method:

```py
movie_titles.sort()

# movie_titles = [
#   '2 JavaScript 2 React', 
#   'Javascript 3: VS Code Lint', 
#   'Recursion',
#   'Zero Dark Python'
# ]
```

Alternatively, we can use the function `sorted` to return a copy of the list sorted alphabetically:

```py
sorted_movie_titles = sorted(movie_titles)

# sorted_movies_titles = [
#   '2 JavaScript 2 React', 
#   'Javascript 3: VS Code Lint', 
#   'Recursion',
#   'Zero Dark Python'
# ]
```

Similar to sorting, to find the first movie title alphabetically we can use the `min` function and to find the last movie alphabetically we can use the `max` function.

```py
first_movie_title = min(movie_titles)
last_movie_title = max(movie_titles)

# first_movie_title = '2 JavaScript 2 React'
# last_movie_title = 'Zero Dark Python'
```


### List of Movie Dictionaries

Let's now consider that we may like to store information about each movie beyond it's title. A dictionary is a great data structure for this. However, finding the first or last movie title and sorting a list of movie dictionaries by title is more involved than performing these operations on a list of strings.

Let's consider the following list of movie titles:

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

Consider how to implement a function using a loop that returns the movie dictionary with the first title alphabetically, then review the code below.

```py
def get_first_movie(movies):
    min_movie = movies[0]
    min_title = movies[0]["title"]
    for movie in movies:
        if movie["title"] < min_title:
            min_movie = movie
            min_title = movie["title"]
    return min_movie


first_movie_by_title = get_first_movie(movies)
# first_movie_by_title = {
#    "title": "2 JavaScript 2 React",
#    "genre": "Action",
#    "rating": 4.2,
#    "release_year": 2015
#}
```

We can implement a similar function to get the movie dictionary with the earliest release date:

```py
def get_earliest_movie(movies):
    min_movie = movies[0]
    min_date = movies[0]["release_year"]
    for movie in movies:
        if movie["release_year"] < min_date:
            min_movie = movie
            min_date = movie["release_year"]
    return min_movie


earliest_movie = get_earliest_movie(movies)
# earliest_movie = {
#    "title": "Recursion",
#    "genre": "Intrigue",
#    "rating": 2.0,
#    "release_year": 1999
#}
```

And we can implement yet another similar function to get the movie with the lowest rating.

```py
def get_lowest_rated_movie(movies):
    min_movie = movies[0]
    min_rating = movies[0]["rating"]
    for movie in movies:
        if movie["rating"] < min_rating:
            min_movie = movie
            min_rating = movie["rating"]
    return min_movie


lowest_rated_movie = get_lowest_rated_movie(movies)
# lowest_rated_movie = {
#    "title": "Recursion",
#    "genre": "Intrigue",
#    "rating": 2.0,
#    "release_year": 1999
#}
```

<!-- available callout types: info, success, warning, danger, secondary, star  -->
### !callout-info

## DRY: Don't Repeat Yourself

Take a moment to notice the amount of repeated code. We will now look at one way to DRY up this functionality, passing a function to the `key` parameter of the `min` function.

### !end-callout


## The `key` parameter.

The [`key` parameter in the `min` function](https://docs.python.org/3/library/functions.html#min) specifies an ordering function that is used to extract a comparison key for each item in the list.

For example, to find the lowest rated movie in a list of dictionaries, we need to pass the `key` parameter in the `min` function that returns value corresponding to the `"rating"` for a movie.

Such as function is defined below:

```py
def get_rating(movie):
    return movie["rating"]
```

We then can pass this function to the `key` parameter in the `min` function.

```py
lowest_rated_movie = min(movies, key=get_rating)
# lowest_rated_movie = {
#    "title": "Recursion",
#    "genre": "Intrigue",
#    "rating": 2.0,
#    "release_year": 1999
#}
```

We can use the same pattern to find the movie with the earliest release date and the first title alphabetically.

```py
def get_release_year(movie):
    return movie["release_year"]

def get_title(movie):
    return movie["title"]

earliest_movie = min(movies, key=get_release_year)
# earliest_movie = {
#    "title": "Recursion",
#    "genre": "Intrigue",
#    "rating": 2.0,
#    "release_year": 1999
#}

first_movie_by_title = min(movies, key=get_title)

# first_movie_by_title = {
#    "title": "2 JavaScript 2 React",
#    "genre": "Action",
#    "rating": 4.2,
#    "release_year": 2015
#}
```

## Keyword Arguments

### !callout-info

## Keyword Arguments

The `key` parameter is an example of a keyword argument. 

### !end-callout

Thus far we've defined functions with positional arguments. The table below describes the difference between defining and calling functions with positional and keyword arguments. 

| Type | Function Definition | Function Call |
| -- | --| --|
| Positional Arguments | `def function_name(parameter1, parameter2)` | `function_name(argument1, argument2)`|
| Keyword Arguments |`def function_name(parameter1, parameter2)` | `function_name(parameter1=argument1, parameter2=argument2)` |

Functions can be called with a mix of keyword and positional arguments, but positional arguments cannot follow keyword arguments in the function call. To learn more, [here is an article we recommend](https://treyhunner.com/2018/04/keyword-arguments-in-python/).

Consider the following function:

```py
def sum(a, b):
    return a + b
```

The following table describes valid and invalid syntax for calling `get_the_sum`:

| Function Call | Valid Syntax (yes/no) | Explanation |
|--|--|--|
|`sum(1, 2)` | yes | This is an example of calling a function with two positional arguments. |
|`sum(a=1, b=2)` | yes | This is an example of calling a function with two keyword arguments. |
|`sum(1, b=2)` | yes | This is an example of calling a function with a mix of positional and keyword arguments. |
|`sum(a=1, 2)` | no | This is invalid. Positional arguments cannot follow keyword arguments. <br> `SyntaxError: positional argument follows keyword argument`|

## Higher Order Functions

The `min` function with the `key` parameter is an example of a higher order function.

### !callout-info

## Higher Order Functions

A higher order function is a function that takes another function as an argument.

### !end-callout

A function is an object in memory that is a set of instructions. A function name is a variable that points to this set of instructions. 

When we use the `()` syntax, we are calling the address of that variable. When we leave off the `()`, we are looking up the address that the variable is pointing to.

Just like variables that point to other objects (strings, integers, lists, etc.), we can assign a function to another variable:

```py
get_the_title = get_title

first_movie_by_title = min(movies, key=get_the_title)

# first_movie_by_title = {
#    "title": "2 JavaScript 2 React",
#    "genre": "Action",
#    "rating": 4.2,
#    "release_year": 2015
#}
```

## Check For Understanding

For the questions below, refer to the variables and functions defined in the lesson.

<!-- >>>>>>>>>>>>>>>>>>>>>> BEGIN CHALLENGE >>>>>>>>>>>>>>>>>>>>>> -->
<!-- Replace everything in square brackets [] and remove brackets  -->

### !challenge

* type: multiple-choice
* id: a1681db0-2b2d-48cb-bdf5-2f434cc04676
* title: Passing Functions As Parameters: Max, Min, and Sort
<!-- * points: [1] (optional, the number of points for scoring as a checkpoint) -->
<!-- * topics: [python, pandas] (Checkpoints only. optional the topics for analyzing points) -->

##### !question

Which of the following will return the list of `movies` sorted by their `"rating"`.

##### !end-question

##### !options

a| `sorted(movies, key=get_rating())`
b| `sorted(movies, key=get_rating)`
c| `sorted(movies, key="rating"`

##### !end-options

##### !answer

b|

##### !end-answer


##### !explanation

The `key` parameter takes a function as an argument. Recall that a function can be assigned to a variable just like any other object in Python. The `()` call a function, whereas the function name is a variable that points to the function object in memory, just like any other variable.

##### !end-explanation

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->