# Oscars Trailers

Oscar Trailers is a automated generated webpage to watch movie trailer of oscars from 2010 to 2017.

# Very Quick start

  - Make download or clone this repository
  - Click on *oscars_2010_to_2017.html*
  - Choose the movie and enjoy it.

# Quick start

  - This project is a 3.7.2 Python project. So, you need install Python 3.7.2
  - Make download or clone this repository
  - Enter on *oscar-movie-trailes-website* folder
  - Install the requirements
  - Execute *entertainment_center.py* to create the *oscars_2010_to_2017.html*

To steps 2, 3 and 4, type the following commands in terminal:

```sh
$ git clone https://github.com/leandrocl2005/ud036_StarterCode.git
$ cd ud036_StarterCode
$ pip install -r requiments.txt
$ python entertainment_center.py
```

# Do it yourself 

In this project the list of movie names, description, url trailers and images was automatically generated. If you want to do it yourself, follow the steps:

### Delete some things and prepare the environment

  - Make download or clone this repository
  - Enter on *oscar-movie-trailes-website* folder
  - delete the following files (you will create them): *movie_images* folder, *initial_database_movie.csv*, *final_database_movie.csv*
  - Install the requirements

### Create the initial movie database

  - Get your OMBD api key here: http://www.omdbapi.com/apikey.aspx
  - In *create_initial_movie_database.py* replace "***YOUR_OMDB_API_KEY***" with you api key
  - Execute *create_initial_movie_database.py* to create *initial_database_movie.csv*
  - Let's fix a decoding bug! Open *initial_database_movie.csv* and replace the movie name *Les Misérables* by *Les Miserables*

### Create the images folder 

  - To create the *movie_images* folder, excecute *create_images_folder.py*
  - Some images won't work. So, move *confused.jpg* to *movie_images* folder. 

### Create the final movies database

  - Get you TMDb api key here: https://www.themoviedb.org
  - In *create_final_movie_database.py* replace "***YOUR_TMDb_API_KEY***" with you api key
  - Execute *create_final_movie_database.py* to create the final_movie_database.csv

### Check if all works fine


```sh
$ python entertainment_center.py
```

Click in some movie poster to check the trailer. If incorrect url, must show the Trololo song: https://www.youtube.com/watch?v=oavMtUWDBTM

# Credits

  - the *fresh_tomatoes.py* script was provided by udacity
  - the *confused.jpg* image was provided by Pixaby (https://pixabay.com/pt/)
