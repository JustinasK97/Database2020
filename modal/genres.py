from modal.database import create_table_database

def create_genres_table():

        query =  """CREATE TABLE IF NOT EXIST genres(
                    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    genre_title TEXT)
                 """

        create_table_database(query)

create_genres_table()
