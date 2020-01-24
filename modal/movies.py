from modal.movies import movies

def create_movies_table():
    try:
        connection, cursor = open_connection()
        query =  """CREATE TABLE IF NOT EXIST movies(
                    movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    movie_title TEXT UNIQUE,
                    release_date TEXT,
                    rating FLOAT,
                    genre TEXT,
                    box_office_name TEXT,
                    studio_name TEXT UNIQUE)
                 """

        cursor.execute(query)

    except sqlite3.DatabaseError as error:
        print(error)

    finally:
        close_connection(connection, cursor)
