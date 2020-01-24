from modal.studio import studio

def create_studio_table():
    try:
        connection, cursor = open_connection()
        query =  """CREATE TABLE IF NOT EXIST studio(
                    studio_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    studio_name TEXT)
                 """

        cursor.execute(query)

    except sqlite3.DatabaseError as error:
        print(error)

    finally:
        close_connection(connection, cursor)
