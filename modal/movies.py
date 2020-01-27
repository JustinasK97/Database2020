from modal.database import create_table_database

def create_movies_table():

        query = """CREATE TABLE IF NOT EXISTS movies(
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

def create_movie(movie):
        query = "INSERT INTO movies VALUES (?, ?, ?, ?, ?, ?, ?)"
        params = (movie.movie_id, movie.movie_title, movie.release_date, movie.rating, movie.box_office_name, movie.studio_name)
        query_database(query, params)

movie1 = movie(None, "First Movie", 2012, 8.4, "Profit", "Dalala")

# create_movie(movie1)