# create an image folder with all posters

# libraries
import os
import pandas as pd
import urllib
import time

now = time.time()

# create movie_images folder
os.mkdir('movie_images')

# load initial_database
df = pd.read_csv("initial_database_movie.csv")

# download and save movie images
for i in range(df.shape[0]):
    try:
        filename = "movie_images/" + df.iloc[i, 3]
        urllib.request.urlretrieve(df.iloc[i, 2], filename)
    except:
        continue

print("Time to finish: {:.2f} segundos".format(time.time()-now))
print()
print("Don't forget to put confused pic in movie_images_folder")

# pixabay confused photo
# https://pixabay.com/pt/confundido-m%C3%A3os-at%C3%A9-d%C3%BAvidas-2681507/
