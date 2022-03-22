def get_unique_movie_titles(movie_titles):
    unique_movie_titles = []
    for i in range(0, len(movie_titles)):
        if movie_titles[i] not in movie_titles[i + 1:]:
            unique_movie_titles.append(movie_titles[i])
    return unique_movie_titles
