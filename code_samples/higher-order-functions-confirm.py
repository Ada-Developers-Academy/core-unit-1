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


def get_title(movie):
    return movie["title"]


def get_rating(movie):
    return movie["rating"]


def get_release_year(movie):
    return movie["release_year"]


def min_function_custom(collection, get_value_for_key):
    min_item = collection[0]
    min_value = get_value_for_key(collection[0])
    for item in collection:
        if get_value_for_key(item) < min_value:
            min_item = item
            min_value = get_value_for_key(item)
    return min_item


first_movie_by_title = min_function_custom(movies, get_value_for_key=get_title)
lowest_rated_movie = min_function_custom(movies, get_value_for_key=get_rating)
earliest_movie = min_function_custom(
    movies, get_value_for_key=get_release_year)

print(first_movie_by_title)
print(lowest_rated_movie)
print(earliest_movie)

first_movie_by_title = min_function_custom(
    movies, get_value_for_key=lambda movie: movie["title"])
lowest_rated_movie = min_function_custom(
    movies, get_value_for_key=lambda movie: movie["rating"])
earliest_movie = min_function_custom(
    movies, get_value_for_key=lambda movie: movie["release_year"])

print(first_movie_by_title)
print(lowest_rated_movie)
print(earliest_movie)

first_movie_by_title = min_function_custom(movies, get_title)
lowest_rated_movie = min_function_custom(movies, get_rating)
earliest_movie = min_function_custom(movies, get_release_year)

print(first_movie_by_title)
print(lowest_rated_movie)
print(earliest_movie)

first_movie_by_title = min_function_custom(
    movies, lambda movie: movie["title"])
lowest_rated_movie = min_function_custom(movies, lambda movie: movie["rating"])
earliest_movie = min_function_custom(
    movies, lambda movie: movie["release_year"])

print(first_movie_by_title)
print(lowest_rated_movie)
print(earliest_movie)
