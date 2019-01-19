# create a final database with url movies

# libraries
import pandas as pd
import time
import requests
import webbrowser
from tmdbv3api import TMDb
from tmdbv3api import Movie

# get a api here: https://www.themoviedb.org/documentation/api
API_KEY = "***YOUR_TMDb_API_KEY***"

# instancie the api client
tmdb = TMDb()
tmdb.api_key = API_KEY
tmdb.language = 'en'
tmdb.debug = True
movie = Movie()

now = time.time()

# load initial database
df = pd.read_csv("initial_database_movie.csv")

# create a empty url movie trailers list
movie_trailers_url = []

# fill url the movie trailers list
for i in range(df.shape[0]):

    try:
        # try get url
        search = movie.search(df.iloc[i, 0])
        movie_id = search[0].id
        movie_url = 'http://api.themoviedb.org/3/movie/{}/videos?api_key=d0fb898e3b33d37bba5795bd82c296d0&append_to_response=videos'.format(movie_id)
        res = requests.get(movie_url)
        key = dict(res.json())['results'][0]['key']
        url = "https://www.youtube.com/watch?v="+key
        movie_trailers_url.append(url)
    except:
    	# if error, set trololo song
        movie_trailers_url.append(
            "https://www.youtube.com/watch?v=oavMtUWDBTM"
        )

df['movie_trailer_url'] = movie_trailers_url
df.to_csv("final_database_movie.csv", index=None)

print("Time to finish: {:.2f} segundos".format(time.time()-now))
