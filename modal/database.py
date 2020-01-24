import sqlite3

def open_connection():
    connection = sqlite3.connect("movies.db")
    cursor = connection.cursor()
    return connection, cursor


def close_connection(connection, cursor):
    connection.close()

def db_query(query, params=None):
    try:
        connection, cursor = open_connection()
        if params:
            cursor.execute(query)
            connection.commit()
        else:
            for i in cursor.execute(query):
                print(i)
    except sqlite3.DatabaseError as error:
       print(error)
    finally:
        close_connection(connection, cursor)