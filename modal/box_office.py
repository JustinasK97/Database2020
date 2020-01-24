from modal.box_office import box_office

def create_box_office_table():
    try:
        connection, cursor = open_connection()
        query =  """CREATE TABLE IF NOT EXIST box_office(
                    box_office_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    box_office_name TEXT)
                 """

        cursor.execute(query)

    except sqlite3.DatabaseError as error:
        print(error)

    finally:
        close_connection(connection, cursor)
