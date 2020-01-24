from modal.actors import actors

def create_actors_table():

        query =  """CREATE TABLE IF NOT EXIST actors(
                    actor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    actor_name TEXT)
                 """

        cursor.execute(query)

create_actors_table()