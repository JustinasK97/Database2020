from modal.directors import directors

def create_directors_table():
    try:
        connection, cursor = open_connection()
        query =  """CREATE TABLE IF NOT EXIST directors(
                    director_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   director_name TEXT)
                 """

        cursor.execute(query)

    except sqlite3.DatabaseError as error:
        print(error)

    finally:
        close_connection(connection, cursor)
