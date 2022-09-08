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


first_movie_by_title = min(movies, key=lambda movie: movie["title"])
lowest_rated_movie = min(movies, key=lambda movie: movie["rating"])
earliest_movie = min(movies, key=lambda movie: movie["release_year"])

print(first_movie_by_title)
print(earliest_movie)
print(lowest_rated_movie)
