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

movie_titles = [
    "Recursion",
    "Zero Dark Python",
    "2 JavaScript 2 React",
    "Javascript 3: VS Code Lint"
]


def get_length(movie_title):
    return len(movie_title)


movie_titles_sorted_by_length = sorted(movie_titles, key=get_length)

print(movie_titles_sorted_by_length)
# print(sorted(movie_titles))
# print("")

# print(min(movie_titles))
# print(max(movie_titles))


def get_title(movie):
    return movie["title"]


def get_release_year(movie):
    return movie["release_year"]


def get_rating(movie):
    return movie["rating"]


gry = get_release_year
gry(INTRIGUE_1)

movies = [INTRIGUE_1, INTRIGUE_2, ACTION_1, ACTION_2, ]


def min_movie_title(movies):
    min_movie = movies[0]
    min_title = movies[0]["title"]
    for movie in movies:
        if movie["title"] < min_title:
            min_movie = movie
            min_title = movie["title"]
    return min_movie


# print("*********")
# print(min_movie_title(movies))


def get_lowest_rated_movie(movies):
    min_movie = movies[0]
    min_rating = movies[0]["rating"]
    for movie in movies:
        if movie["rating"] < min_rating:
            min_movie = movie
            min_rating = movie["rating"]
    return min_movie


# lowest_rated_movie = get_lowest_rated_movie(movies)
# print(lowest_rated_movie)


def get_earliest_movie(movies):
    min_movie = movies[0]
    min_date = movies[0]["release_year"]
    for movie in movies:
        if movie["release_year"] < min_date:
            min_movie = movie
            min_date = movie["release_year"]
    return min_movie


# earliest_movie = get_earliest_movie(movies)
# print(earliest_movie)

print(min(movies, key=get_rating))
print(min(movies, key=get_release_year))
print(min(movies, key=get_title))

movies_sorted_by_title = sorted(movies, key=get_title)
print(movies_sorted_by_title)
print("")

movies_sorted_by_release_year = sorted(movies, key=get_release_year)
print(movies_sorted_by_release_year)
print("")

movies_sorted_by_title = sorted(movies, key=lambda movie: movie["title"])
print(movies_sorted_by_title)
print("")


# def min_function(titles):
#     min_title = titles[0]
#     for title in tiles:
#         if title < min_title:
#             min_title = title
#     return min_title


# def min_function_release_year(collection):
#     min_item = collection[0]
#     min_key = collection[0]["release_year"]
#     for item in collection:
#         if item["release_year"] < min_key:
#             min_item = item
#             min_key = item["release_year"]
#     return min_item


# print(min_function_release_year(movies))


def min_function_custom(collection, key):
    min_item = collection[0]
    min_key = key(collection[0])
    for item in collection:
        if key(item) < min_key:
            min_item = item
            min_key = key(item)
    return min_item


print(min_function_custom(movies, lambda movie: movie["title"]))
print(min_function_custom(movies, lambda movie: movie["rating"]))
print(min_function_custom(movies, lambda movie: movie["release_year"]))

first_movie_title = min(movies, key=lambda movie: movie["title"])
lowest_rated_movie = min(movies, key=lambda movie: movie["rating"])
earliest_movie = min(movies, key=lambda movie: movie["release_year"])
