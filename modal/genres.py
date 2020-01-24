from modal.genres import genres

def create_genres_table():
    try:
        connection, cursor = open_connection()
        query =  """CREATE TABLE IF NOT EXIST genres(
                    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    genre_title TEXT)
                 """

        cursor.execute(query)

    except sqlite3.DatabaseError as error:
        print(error)

    finally:
        close_connection(connection, cursor)
