import sqlite3

def open_connection():
    connection = sqlite3.connect("movies.db")
    cursor = connection.cursor()
    return connection, cursor


def close_connection(connection, cursor):
    connection.close()

def query_database(query, params=None):
    try:
        connection, cursor = open_connection()
        if params:
            cursor.execute(query)
            connection.commit()
        else:
            for row in cursor.execute(query):
                print(row)

    except sqlite3.DatabaseError as error:
        print(error)
    finally:
        close_connection(connection, cursor)


def create_table_database(query):
    try:
        connection, cursor = open_connection()
        cursor.execute(query)
        connection.commit()
    except sqlite3.DatabaseError as error:
        print(error)
    finally:
        close_connection(connection, cursor)