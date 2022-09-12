# Passing Functions as Arguments: Min, Max, and Sort

## Learning Goals

* Demonstrate how to pass a function as an argument
* Describe how to use the `key` parameter of the `sorted` function to sort a list of dictionaries by a specific key
* Describe how to use the `key` parameter of the `min` function to find the minimum in a list of dictionaries by a specific key
* Describe how to use the `key` parameter of the `sorted` function to sort a list of movie titles by length

## Introduction

Imagine we have a list of movie titles we'd like to sort alphabetically. Python provides a couple convenient functions for this task. The [`sort`](https://docs.python.org/3/howto/sorting.html#sorting-basics) method can be called on a list and sorts the list in place. The `sorted` function takes a list (or any iterable datatype) as a parameter and returns the sorted list (or other datatype).  

But what if we have a list of dictionaries representing movies that we want to sort by title, or perhaps by rating. Maybe we want to find the most recent movie in a list, or perhaps the oldest.

There are several functions in Python, including the `min`, `max`, and `sorted` functions, that accept a `key` parameter. This `key` parameter takes a function that will be called on each item in the list to retrieve a special value, called a comparison key, for that item. The comparison keys will then be used to find the minimum, find the maximum, or to sort.

## Vocabulary and Synonyms
| Vocab	| Definition| Synonyms |	How to Use in a Sentence |
|--|--|--|--|
|Higher Order Function| A function that takes a function as an argument | - | When we use the optional `key` parameter with the `sorted` function, `sorted` is a higher order function. |
|Positional Arguments|Arguments that must be passed to a function in the specified order | -|It is not uncommon to introduce a bug by passing positional arguments to a function in the wrong order. |
|Keyword Arguments| Arguments that are passed to a function with the `name=value` syntax |Named Parameters |Keyword arguments can be passed to a function in any order, but cannot be followed by positional arguments.|

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

To sort the titles alphabetically in place, we can use the `sort` method:

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

Similar to sorting, to find the first movie title alphabetically we can use the `min` function, and to find the last movie alphabetically we can use the `max` function.

```py
first_movie_title = min(movie_titles)
last_movie_title = max(movie_titles)

# first_movie_title = '2 JavaScript 2 React'
# last_movie_title = 'Zero Dark Python'
```

### List of Movie Dictionaries

But what if we store more information about each movie than just its title? A dictionary is a great data structure for this! However, finding the movie dictionary with the first or last title, or sorting a list of movie dictionaries by title, is more involved than performing these operations on a list of strings.

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

We could write our own logic to find the movie dictionary with the first title alphabetically. Consider how we might accomplish this, then review one possible implementation below.

<br>

<details>
    <summary>Finding the movie dictionary with the first title alphabetically</summary>

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
# }
```

</details>

We can implement a similar function to get the movie dictionary with the earliest release date.

<br>

<details>
    <summary>Finding the movie dictionary with the earliest release date</summary>

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
# }
```

</details>

And we can implement yet another similar function to get the movie with the lowest rating.

<br>

<details>
    <summary>Finding the movie dictionary with the lowest rating</summary>

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
# }
```

</details>

<!-- available callout types: info, success, warning, danger, secondary, star  -->
### !callout-info

## DRY: Don't Repeat Yourself

After reviewing the implementations above, take a moment to notice the amount of repeated code. We will now look at one way to DRY up this functionality, passing a function to the `key` parameter of the `min` function. Later, we'll look at how we can DRY up our own functions, such as in cases where there might not be a library function for us to use already!

### !end-callout


## The `key` parameter.

The [`key` parameter of the `min` function](https://docs.python.org/3/library/functions.html#min) is used to provide a function that `min` can use to extract a comparison key for each item in the list.

For example, to find the lowest rated movie in a list of dictionaries, we need to pass a function to the `key` parameter of the `min` function that `min` will be able to use to retrieve the `"rating"` for a movie.

Such a function is defined below:

```py
def get_rating(movie):
    return movie["rating"]
```

We then can pass this function to the `key` parameter of the `min` function.

```py
lowest_rated_movie = min(movies, key=get_rating)
# lowest_rated_movie = {
#    "title": "Recursion",
#    "genre": "Intrigue",
#    "rating": 2.0,
#    "release_year": 1999
# }
```

We can use the same pattern to find the movie with the earliest release date, or the first title alphabetically.

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
# }

first_movie_by_title = min(movies, key=get_title)

# first_movie_by_title = {
#    "title": "2 JavaScript 2 React",
#    "genre": "Action",
#    "rating": 4.2,
#    "release_year": 2015
# }
```

### Sorting a List of Movie Titles by Length

Using the `key` parameter is not limited to working with a list of dictionaries.

Similar to using the `key` parameter to find the minimum, the maximum, and sort a list of dictionaries by a particular key, we can use the `key` parameter to customize the sort behavior when sorting a list of strings. 

The default behavior of comparators (i.e. `<`, `>`, etc.) for strings is to compare them alphabetically. But what if we want to sort a list of movie titles by the length of the title? This is a perfect opportunity to use the `key` parameter.

Let's recall the list of movie titles:

```py
movie_titles = [
    "Recursion",
    "Zero Dark Python",
    "2 JavaScript 2 React",
    "Javascript 3: VS Code Lint"
]
```

First we will write a function that returns the length of the movie titles:

```py
def get_length(movie_title):
    return len(movie_title)
```

Then we will pass this function to the `key` parameter of the sorted function:

```py
movie_titles_sorted_by_length = sorted(movie_titles, key=get_length)

# movies_titles_sorted_by_length = [
# 'Recursion', 
# 'Zero Dark Python', 
# '2 JavaScript 2 React',
# 'Javascript 3: VS Code Lint']
# ]
```

## Keyword Arguments

### !callout-info

## Keyword Arguments

The `key` parameter is an example of a keyword argument, also referred to as a named parameter.

### !end-callout

Thus far we've defined functions with positional arguments. The table below describes the difference between defining and calling functions with positional and keyword arguments. 

| Type | Function Definition | Function Call |
| -- | --| --|
| Positional Arguments | `def function_name(​parameter1, parameter2)` | `function_name(​argument1, argument2)`|
| Keyword Arguments |`def function_name(​parameter1, parameter2)` | `function_name(​parameter1=argument1, parameter2=argument2)` |

Functions can be called with a mix of keyword and positional arguments, but positional arguments cannot follow keyword arguments in the function call. Keyword argument can be passed in any order, whereas positional arguments must be passed in the order specified in the function definition. To learn more, [here is an article we recommend](https://treyhunner.com/2018/04/keyword-arguments-in-python/).

Consider the following function:

```py
def add(a, b):
    return a + b
```

The following table describes valid and invalid syntax for calling `add`:

|<div style="min-width:140px;">Function Call</div>| Valid Syntax (yes/no) | Explanation |
|--|--|--|
|`add(1, 2)` | yes | This is an example of calling a function with two positional arguments. |
|`add(a=1, b=2)` | yes | This is an example of calling a function with two keyword arguments. |
|`add(1, b=2)` | yes | This is an example of calling a function with a mix of positional and keyword arguments. |
|`add(a=1, 2)` | no | This is invalid. Positional arguments cannot follow keyword arguments. <br> `SyntaxError: positional argument follows keyword argument`|

Python also provides a way for a function to indicate that certain parameters _must_ be called as either positional or keyword arguments. This is why we must supply our `key` function using a keyword argument. We won't go into how to use this in our own functions, but [PEP 3102](https://peps.python.org/pep-3102/) provides additional details. Follow your curiosity!

## Higher Order Functions

The `min` function with the `key` parameter is an example of a higher order function.

### !callout-info

## Higher Order Functions

A higher order function is a function that takes another function as an argument.

### !end-callout

In Python, a function is an object in memory, just like any other value. But instead of storing a number, string, or collection, it stores a set of instructions. And in the same way that a variable name _isn't_ the value it refers to, a function name isn't the function itself. It's a variable that points to the set of instructions which make up the function.

```py
# my_num is a variable that refers to an integer object with the value 3
my_num = 3

# my_fun is a variable that refers to a function object containing the pass instruction
def my_fun():
    pass
```

When we write parentheses `()` after a variable that refers to a function, we are asking Python to call (run) the function object referred to by the variable. When we leave off the parentheses `()`, we are only getting a reference to the object (here a function object) the variable is pointing at, the same as when we write any other variable name.

So just like variables that point to other objects (strings, integers, lists, etc.), we can assign the function object referred to by one variable to another variable. Assuming `get_title` is a function as defined in the example above, we could write:

```py
get_the_title = get_title
```

And use it just as we could when referring to it by its original name.

```py
movie_title = get_the_title(INTRIGUE_1)

# movie_title = "Recursion"

first_movie_by_title = min(movies, key=get_the_title)

# first_movie_by_title = {
#    "title": "2 JavaScript 2 React",
#    "genre": "Action",
#    "rating": 4.2,
#    "release_year": 2015
# }
```

The fact that functions are objects allows us to reassign them to other variables. And since function parameters are variables themselves, we can pass a reference to a function stored in one variable (such as its original name) as an argument to another function.

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

The `key` parameter takes a function as an argument. Recall that a function can be assigned to a variable just like any other object in Python. The parentheses `()` call a function, whereas the function name is a variable that points to the function object in memory, just like any other variable.

##### !end-explanation

### !end-challenge

<!-- ======================= END CHALLENGE ======================= -->