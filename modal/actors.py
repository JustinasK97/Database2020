from modal.actors import actors

def create_actors_table():
    try:
        connection, cursor = open_connection()
        query =  """CREATE TABLE IF NOT EXIST actors(
                    actor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    actor_name TEXT)
                 """

        cursor.execute(query)

    except sqlite3.DatabaseError as error:
        print(error)

    finally:
        close_connection(connection, cursor)

