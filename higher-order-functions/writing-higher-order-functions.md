# Writing Higher Order Functions

## Learning Goals

* Review one example of writing a higher order function

## Introduction

Thus far we have learned how to pass a function as an argument and how to write an anonymous function using lambda expressions. In this lesson we'll look at an example of writing a custom higher order function. 

## Movie Example Review

Let's return to our movie example. In the [lesson on passing functions as arguments](./min-max-sorted.md) we first considered the following three functions to find the movie with the first title alphabetically, the earliest release year, and the lowest rating:

```py    
def get_first_movie(movies):
    min_movie = movies[0]
    min_title = movies[0]["title"]
    for movie in movies:
        if movie["title"] < min_title:
            min_movie = movie
            min_title = movie["title"]
    return min_movie

def get_earliest_movie(movies):
    min_movie = movies[0]
    min_date = movies[0]["release_year"]
    for movie in movies:
        if movie["release_year"] < min_date:
            min_movie = movie
            min_date = movie["release_year"]
    return min_movie

def get_lowest_rated_movie(movies):
    min_movie = movies[0]
    min_rating = movies[0]["rating"]
    for movie in movies:
        if movie["rating"] < min_rating:
            min_movie = movie
            min_rating = movie["rating"]
    return min_movie
```

We then saw how we could DRY up this code with the `min` function and the optional `key` parameter.

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

Finally, in the lesson on [lambda expressions](./lambdas.md), we achieved the functionality above with more concise code:

```py
first_movie_by_title = min(movies, key=lambda movie: movie["title"])
lowest_rated_movie = min(movies, key=lambda movie: movie["rating"])
earliest_movie = min(movies, key=lambda movie: movie["release_year"])
```

## Writing a Custom Min Function

Now, let's demystify the optional `key` parameter of the `min` function by writing our own custom min function `min_function_custom`. We will use `get_first_movie` as a reference:

```py
def get_first_movie(movies):
    min_movie = movies[0]
    min_title = movies[0]["title"]
    for movie in movies:
        if movie["title"] < min_title:
            min_movie = movie
            min_title = movie["title"]
    return min_movie
```

Notice that we can replace each occurrence of an expression of the form `movie_dict["title"]`, with a function call `get_title(movie_dict)` without changing the behavior of the function.

```py
def get_title(movie):
    return movie["title"]


def get_first_movie(movies):
    min_movie = movies[0]
    min_title = get_title(movies[0])
    for movie in movies:
        if get_title(movie) < min_title:
            min_movie = movie
            min_title = get_title(movie)
    return min_movie
```

Now, let's take it one step further to generalize our function to find the minimum movie by any key (i.e. `"title"`, `"rating"`, or `"release_year"`). 

We will generalize our variable names changing `movies` to `collection` and `movie` to `item`. We will also add a second parameter, a function that gets the comparison value that should be used for each movie, now renamed to item: `get_value_from_item`. Each line from `get_first_movie` that has the expression `get_title(movie)` will be replaced with `get_value_from_item(item)`.

<!-- available callout types: info, success, warning, danger, secondary, star  -->
### !callout-info

## There's Always Another Way

In an actual project, if we only need to be able to change the dictionary key that a function is using, we might simply add a parameter for that key. But when writing a more general purpose function, a parameter accepting a function often provides greater flexibility.

<br>

We'll see there are other structures we can use to store related data values which must be accessed using different syntax. A parameter accepting a function can be used to adapt to a wider variety of data structures!

### !end-callout

| Specific Function | Generalized Function |
| -- | -- |
| `movies` | `collection`|
| `movie` | `item` |
| `get_title(movie)` | `get_value_from_item(item)` |
| `def get_first_movie(​movies)`|`def min_function_custom(​collection, get_value_from_item)`|  

*Table. Relationship between variables in specific function and generalized function.*

```py
def min_function_custom(collection, get_value_from_item):
     min_item = collection[0]
     min_value = get_value_from_item(collection[0])
     for item in collection:
         if get_value_from_item(item) < min_value:
             min_item = item
             min_value = get_value_from_item(item)
     return min_item
```

We can now call `min_function_custom` just like the built in `min` function. We can pass in a named function or a lambda expression for the `get_value_from_item` parameter

```py
first_movie_by_title = min_function_custom(
    movies, get_value_from_item=get_title)

lowest_rated_movie = min_function_custom(
    movies, get_value_from_item=get_rating)

earliest_movie = min_function_custom(
    movies, get_value_from_item=get_release_year)
```
or 

```py
first_movie_by_title = min_function_custom(
    movies, get_value_from_item=lambda movie: movie["title"])

lowest_rated_movie = min_function_custom(
    movies, get_value_from_item=lambda movie: movie["rating"])

earliest_movie = min_function_custom(
    movies, get_value_from_item=lambda movie: movie["release_year"])
```

We can also pass the second parameter as a positional argument rather than a keyword argument:

```py
first_movie_by_title = min_function_custom(movies, get_title)

lowest_rated_movie = min_function_custom(movies, get_rating)

earliest_movie = min_function_custom(movies, get_release_year)
```
or 

```py
first_movie_by_title = min_function_custom(
    movies, lambda movie: movie["title"])

lowest_rated_movie = min_function_custom(
    movies, lambda movie: movie["rating"])
    
earliest_movie = min_function_custom(
    movies, lambda movie: movie["release_year"])
```

<!-- available callout types: info, success, warning, danger, secondary, star  -->
### !callout-info

## Writing Higher Order Functions

This lesson provides one example of how to write a higher order function in order to provide initial exposure to writing higher order functions. We do not need to be fluent with this skill at this stage of our learning. We will see more examples in Unit 3 (Javascript) that will allow us to gain fluency with writing higher order functions.

### !end-callout