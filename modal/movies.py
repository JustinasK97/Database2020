import sys
from modal.database import create_table_database

def create_movies_table():

        query = """CREATE TABLE IF NOT EXIST movies(
                    movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    movie_title TEXT UNIQUE,
                    release_date TEXT,
                    rating FLOAT,
                    genre TEXT,
                    box_office_name TEXT,
                    studio_name TEXT UNIQUE)
                 """

        create_table_database(query)

create_movies_table()