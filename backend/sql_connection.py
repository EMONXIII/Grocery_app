import mysql.connector

__cnx = None
def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='root',
                                        host='localhost',
                                        database='grocery_store1')

    return __cnx