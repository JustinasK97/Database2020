from modal.directors import directors

def create_directors_table():

        query =  """CREATE TABLE IF NOT EXIST directors(
                    director_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   director_name TEXT)
                 """

        cursor.execute(query)

create_directors_table()
