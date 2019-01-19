# create a .csv file with name, year, image name, image url and description
# of oscar movies from 2010 until 2017

# libraries
import requests
from bs4 import BeautifulSoup
import omdb
import time
import pandas as pd

API_KEY = "***YOUR_OMDB_API_KEY***"
now = time.time()
client = omdb.OMDBClient(apikey=API_KEY)


def format_name(movie_name):
    """Format movie name to use in file name

    Input
    -------
    movie_name: the name of a movie

    Output
    -------
    formatted file name

    """
    return "_".join([x.lower() for x in movie_name
                     .replace(".", "")
                     .replace(":", "")
                     .replace("(", "")
                     .replace(")", "")
                     .replace("]", "")
                     .replace("[", "")
                     .replace("-", "")
                     .replace("'", "")
                     .replace("&", "")
                     .replace("!", "")
                     .replace(",", "")
                     .split()])

# To get the oscar movie names we'll scrapy the wikipedia
URL = "https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films"
page = requests.get(URL)  # get url
soup = BeautifulSoup(page.content, 'html.parser')  # get soup object
trs = soup.find_all('tr')  # get tr tags (the movie names is here)

# building a empty dict to fill with data
oscars_dict = {
    "name": [],
    "year": [],
    "image_url": [],
    "image_path": [],
    "plot": []
}

# Take 104 movies (this number was founded by test)
for tr in trs[1:105]:

    # get movie name and year (oscar from 2010 until 2017)
    tds = tr.find_all('td')
    movie_name = tds[0].text
    movie_year = tds[1].text
    oscars_dict["name"].append(movie_name)
    oscars_dict["year"].append(movie_year)

    # get json data
    res = client.request(t=movie_name, y=movie_year, r='json')
    res_dict = dict(res.json())

    try:
        # Try get poster
        image_url = res_dict['Poster']
        if image_url == "N/A":
            # if not, set a confused image
            oscars_dict["image_url"].append(image_url)
            oscars_dict["image_path"].append("confused.jpg")
        else:
            oscars_dict["image_url"].append(image_url)
            oscars_dict["image_path"].append(format_name(movie_name)+".jpg")
    except:
        # if error, set a confused image
        oscars_dict["image_url"].append(None)
        oscars_dict["image_path"].append("confused.jpg")

    try:
        # Try get description
        plot = res_dict['Plot']
        oscars_dict['plot'].append(plot)
    except:
        # if error, set No Description text
        oscars_dict['plot'].append("No description")

# make a csv file
df = pd.DataFrame(oscars_dict).fillna("N/A")
df.to_csv("initial_database_movie.csv", index=None)

# print spent tiem
print("Time to finish: {:.2f} segundos".format(time.time()-now))
