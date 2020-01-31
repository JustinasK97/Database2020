from modal.database import create_table_database, query_database
from entities.actors import actors

def create_actors_table():

        query = """CREATE TABLE IF NOT EXIST actors(
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

def insert_actor(actor):
    query = """INSERT INTO actors (actor_id, actor_name) 
                      VALUES(?, ?)"""
    params = (actor.actor_id, actor.actor_name)
    query_database(query, params)


def insert_actors_movies(actor_name, movie_title):
    query = """INSERT INTO actors_movies (actors_id, movies_id)
                                        SELECT(SELECT actors_id FROM actors WHERE actor_name=?), 
                                        (SELECT movies_id FROM movies WHERE movie_title=?)"""
    params = (actor_name, movie_title)
    query_database(query, params)

def get_actor():
    query = "SELECT * FROM actors"
    query_database(query)


def get_actors_movies():
    query = "SELECT * FROM actors_movies"
    query_database(query)


def update_actors(actor):
    query = "UPDATE actors SET actor.name = ? WHERE actor_id = ?"
    params = (actor.actor_name, actor.actor_id)
    query_database(query, params)

def delete_actors(actor_id):
    query = "DELETE FROM actors WHERE actor_id = ?"
    params = (actor_id,)
    query_database(query, params)

create_actors_table()
create_actors_movies_table()
actor1 = actors(None, "Rob Doubler")
actor2 = actors(None, "Jake Baker")
# insert_actor(actor1)
# insert_actor(actor2)
actor3 = actors(None, "Will Deed")
# update_actors(actor3)
# delete_actors(2)
insert_actors_movies("Jake Baker", "Pirmas Filmas")
get_actor()
get_actors_movies()