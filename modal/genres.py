from modal.genres import genres

def create_genres_table():

        query =  """CREATE TABLE IF NOT EXIST genres(
                    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    genre_title TEXT)
                 """

        cursor.execute(query)

create_genres_table()
