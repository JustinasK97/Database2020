from modal.database import create_table_database, query_database

def create_genres_table():

        query = """CREATE TABLE IF NOT EXIST genres(
                    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    genre_title TEXT)
                 """
        create_table_database(query)

def create_movies_genres_table():

        query = """CREATE TABLE IF NOT EXISTS movies_genres(
                     movies_genres_id INTEGER PRIMARY KEY AUTOINCREMENT,
                     genres_id  FOREIGN KEY (genres_id) REFERENCES genres(genres_id),
                     movies_id FOREIGN KEY (movies_id) REFERENCES movies(movies_id))))"""
        create_movies_genres_table(query)


create_genres_table()
create_movies_genres_table()