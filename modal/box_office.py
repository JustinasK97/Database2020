from modal.box_office import box_office

def create_box_office_table():

        query =  """CREATE TABLE IF NOT EXIST box_office(
                    box_office_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    box_office_name TEXT)
                 """

        cursor.execute(query)

create_box_office_table()
