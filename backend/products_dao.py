#dao(data access object)

import mysql.connector

cnx = mysql.connector.connect(user='root', password='Tanjin@133060#',
                              host='127.0.0.1',
                              database='grocery_store1')
cnx.close()