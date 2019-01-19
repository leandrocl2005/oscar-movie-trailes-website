# run movie trailer website

# libraries
import media
import fresh_tomatoes
import pandas as pd


# load database
df = pd.read_csv("final_database_movie.csv")

# create movie list
movies = []
for i in range(df.shape[0]):
    movies.append(media.Movie(
            df.iloc[i, 0],  # movie name
            df.iloc[i, 4],  # movie description
            'movie_images/'+df.iloc[i, 3],  # movie image path
            df.iloc[i, 5]  # movie url trailer
        )
    )

# run website
fresh_tomatoes.open_movies_page(movies)
