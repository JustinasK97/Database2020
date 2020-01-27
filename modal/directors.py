from modal.database import create_table_database

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


create_directors_table()
create_directors_movies_table()