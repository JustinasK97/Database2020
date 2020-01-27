from modal.database import create_table_database

def create_studio_table():

        query =  """CREATE TABLE IF NOT EXIST studio(
                    studio_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    studio_name TEXT)
                 """
        create_table_database(query)

create_studio_table()
