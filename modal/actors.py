from modal.database import create_table_database

def create_actors_table():

        query =  """CREATE TABLE IF NOT EXIST actors(
                    actor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    actor_name TEXT)
                 """
create_table_database(query)


def create_actors_movies_table():
        query = """CREATE TABLE IF NOT EXISTS actors_movies (
                                actors_movies_Id INTEGER PRIMARY KEY AUTOINCREMENT,
                                actorsId  FOREIGN KEY (actorsId) REFERENCES actors(actorsId),
                                moviesId FOREIGN KEY (moviesId) REFERENCES movies(moviesId))"""
        create_table_database(query)


create_actors_table()
create_actors_movies_table()