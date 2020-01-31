from modal.database import create_table_database, query_database
from entities.directors import directors

def create_directors_table():

        query = """CREATE TABLE IF NOT EXIST directors(
                    director_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   director_name TEXT)
                 """
        create_table_database(query)

def create_directors_movies_table():

        query = """CREATE TABLE IF NOT EXIST directors_movies(
                                directors_movies_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                directors_id  FOREIGN KEY (directors_id) REFERENCES actors(directors_id),
                                movies_id FOREIGN KEY (movies_id) REFERENCES movies(movies_id)))"""
        create_table_database(query)


def insert_directors(directors):
    query = """INSERT INTO directors (director_is, director_name) 
                      VALUES(?, ?)"""
    params = (directors.director_id, directors.director_name)
    query_database(query, params)

def insert_directors_movies(director_name, movie_title):
    query = """INSERT INTO directors_movies (director_id, movie_id)
                                        SELECT(SELECT director_id FROM directors WHERE director_name=?), 
                                        (SELECT movie_id FROM movies WHERE movie_title=?)"""
    params = (director_name, movie_title)
    query_database(query, params)


def get_directors():
    query = "SELECT * FROM directors"
    query_database(query)


def get_directors_movies():
    query = "SELECT * FROM directors_movies"
    query_database(query)


def update_directors(director):
    query = "UPDATE director SET director_name = ? WHERE director_id = ?"
    params = (director.director_name, director.director_id)
    query_database(query, params)


def delete_directors(director_id):
    query = "DELETE FROM directors WHERE director_id = ?"
    params = (director_id,)
    query_database(query, params)


create_directors_table()
create_directors_movies_table()
director1 = directors(None, "Pirmas")
# insert_into_directors(directors1)
insert_directors_movies("Pirmas", "update Test")
get_directors()
get_directors_movies()