from modal.database import create_table_database, query_database
from entities.box_office import box_office


def create_box_offices_table():
    query = """CREATE TABLE IF NOT EXISTS box_office (
                        box_office_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        sales REAl)"""
    create_table_database(query)


def insert_box_office(box_office):
    query = """INSERT INTO box_office (box_office_id, sales) 
                      VALUES(?, ?)"""
    params = (box_office.boxoffice_id, box_office.sales)
    query_database(query, params)


def get_box_office():
    query = "SELECT * FROM box_office"
    query_database(query)

def update_box_office(box_office):
    query = "UPDATE box_offices SET sales = ? WHERE box_office_id = ?"
    params = (box_office.sales, box_office.box_office_id)
    query_database(query, params)

def delete_box_offices_table(box_office_id):
    query = "DELETE FROM box_office WHERE box_office_id = ?"
    params = (box_office_id, )
    query_database(query, params)

create_box_offices_table()
box_office1 = box_office(None, 35000)
# insert_box_office(box_office1)
box_office2 = box_office(None, 19000)
# insert_box_office(box_office2)
box_office3 = box_office(2, 999959)
update_box_office(box_office3)
box_office4 = box_office(None, 595555)
# insert_box_office(box_office4)
delete_box_offices_table(4)
get_box_office()