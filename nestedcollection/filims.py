
movies = [
    # Malayalam Movies
    {
        "title": "Drishyam",
        "year": 2013,
        "language": "Malayalam",
        "genres": ["Crime", "Drama", "Thriller"],
        "rating": 8.6
    },
    {
        "title": "Premam",
        "year": 2015,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    {
        "title": "Bangalore Days",
        "year": 2014,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    # Tamil Movies
    {
        "title": "Kaala",
        "year": 2018,
        "language": "Tamil",
        "genres": ["Action", "Drama"],
        "rating": 7.3
    },
    {
        "title": "Vikram Vedha",
        "year": 2017,
        "language": "Tamil",
        "genres": ["Action", "Crime", "Thriller"],
        "rating": 8.4
    },
    {
        "title": "Super Deluxe",
        "year": 2019,
        "language": "Tamil",
        "genres": ["Drama", "Mystery", "Thriller"],
        "rating": 8.3
    },
    # Hindi Movies
    {
        "title": "Dangal",
        "year": 2016,
        "language": "Hindi",
        "genres": ["Action", "Biography", "Drama"],
        "rating": 8.4
    },
    {
        "title": "3 Idiots",
        "year": 2009,
        "language": "Hindi",
        "genres": ["Comedy", "Drama"],
        "rating": 8.4
    },
    {
        "title": "Gully Boy",
        "year": 2019,
        "language": "Hindi",
        "genres": ["Drama", "Music"],
        "rating": 8.0
    }
]


movies_count=len(movies)

#print("movie count",movies_count)

genre_filter=[m.get("title")for m in movies if "Drama" in m.get("genres")]

#print(genre_filter)

def get_year(mov):

    return mov.get("year")

latest_movie_data=max(movies,key=get_year)

latest_movie=[m.get("title") for m in movies if m.get("year")==latest_movie_data.get("year")]

#print(latest_movie)

def get_rating(mov):

    return mov.get("rating")

top_movie_data=max(movies,key=get_rating)

top_rating_movie=[m.get("title") for m in movies if m.get("rating")==top_movie_data.get("rating")]

#print(top_rating_movie)

Malayalam_movie=[m.get("title") for m in movies if m.get("language")=="Malayalam"]

#print(Malayalam_movie)

year_filter=[m.get("title")for m in movies if m.get("year")>2016]

#print(year_filter)

lowest_rating_movie_data=min(movies,key=get_rating)

lowest_rating_movie=[m.get("title")for m in movies if m.get("rating")==lowest_rating_movie_data.get("rating")]

#print(lowest_rating_movie)

malayalam_action_movie=[m.get("title")for m in movies if "Drama" in m.get("genres")=="Malayalam"]

#print(malayalam_action_movie)

years=[m.get("year") for m in movies]

year_count={y:years.count(y) for y in years}

#print(year_count)

oldest_movie_data=min(movies,key=get_year)

oldest_movie_name=[m.get("title") for m in movies if m.get("year")==oldest_movie_data.get("year")]

#print(oldest_movie_name)

genres={g for m in movies for g in m.get("genres")}

#print(genres)

all_genres=[g for m in movies for g in m.get("genres")]

genre_count={g:all_genres.count(g) for g in all_genres}

#print(genre_count)

sorted_movies=sorted(movies,key=lambda mov:mov.get("title"))

sorted_movie_title=[m.get("title")for m in sorted_movies]

#print(sorted_movie_title)





