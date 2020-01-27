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
                                actors_id  FOREIGN KEY (actors_id) REFERENCES actors(actors_id),
                                movies_id FOREIGN KEY (movies_id) REFERENCES movies(movies_id))"""
        create_table_database(query)


create_actors_table()
create_actors_movies_table()