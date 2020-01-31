from modal.database import create_table_database, query_database
from entities.studio import studio

def create_studio_table():

        query =  """CREATE TABLE IF NOT EXIST studio(
                    studio_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    studio_name TEXT)
                 """
        create_table_database(query)

def insert_studio(studio):
    query = """INSERT INTO studios (studioId, studioName) 
                      VALUES(?, ?)"""
    params = (studio.studio_id, studio.studio_name)
    query_database(query, params)


def get_studio():
    query = "SELECT * FROM studio"
    query_database(query)

def update_studio(studio):
    query = "UPDATE studios SET studioName = ? WHERE studioId = ?"
    params = (studio.studio_name, studio.studio_id)
    query_database(query, params)

def delete_studio(studio_id):
    query = "DELETE FROM studios WHERE studio_id = ?"
    params = (studio_id, )
    query_database(query, params)

create_studio_table()
studio1 = studio(None, "Golden Gates")
# insert_studio(studio1)
studio2 = studio(None, "Golden")
# insert_studio(studio2)
studio3 = studio(1, "Gates")
# update_studio(studio3)
# delete_studio_table(3)

get_studio()