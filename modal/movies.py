from datetime import date
from modal.database import create_table_database, query_database
from entities.movie import movie

def create_movies_table():

        query = """CREATE TABLE IF NOT EXISTS movies(
                    movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    movie_title TEXT UNIQUE,
                    movie_director TEXT,
                    release_date DATE,
                    rating REAL,
                    genre TEXT,
                    box_office_id INTEGER,
                    studio_id INTEGER,
                    FOREIGN KEY (box_office_id) REFERENCES box_offices(box_office_id)
                    FOREIGN KEY (studio_id) REFERENCES box_offices(studio_id))"""
        create_table_database(query)



def create_movies(movie):
        query = """INSERT INTO movies (movie_id, movie_title, movie_director, release_date, rating, genre, box_office_id, studio_id)
        VALUES(?, ?, ?, ?, ?, ?, ?)"""
        params = (movie.movie_id, movie.movie_title, movie.movie_director, movie.release_date, movie.rating, movie.genre, movie.box_office_id, movie.studio_id)
        query_database(query, params)


def get_movies():
        query = "SELECT * FROM movies"
        query_database(query)

def update_movies(movie):
        query = "UPDATE movies SET movie_title = ? WHERE movie_id = ?"
        params = (movie.movie_title, movie.movie_id)
        query_database(query, params)

def delete_movies(movie_id):
        query = "DELETE FROM movies WHERE movie_id = ?"
        params = (movie_id)
        query_database(query, params)

# query_database("PRAGMA table_info(movies)")
create_movies_table()
create_table_database("DROP TABLE movies")
movie1 = movie(None, "Pirmas Filmas", "John Dust", 2012, 8.5, "Drama", 1, 1)
movie2 = movie(None, "Antras Filmas", "Chul Lee", 2015, 5.6, "Comedy", 2, 2)
create_movies(movie2)
movie3 = movie(None, "Trecias Filmas", "Peter Loop", 2019, 7.7, "Fantastic", 2, 1)
# update_movies(movie3)
# get_movies()