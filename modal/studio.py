from modal.studio import studio

def create_studio_table():

        query =  """CREATE TABLE IF NOT EXIST studio(
                    studio_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    studio_name TEXT)
                 """

        cursor.execute(query)

    create_studio_table()
