import mysql.connector

__mydb = None

def get_sql_connection():
    
    global __mydb

    if(__mydb==None):
        __mydb = mysql.connector.connect(
            host="localhost",
            username="root",
            password="221223",
            database="medicine_inventory"
        )

    return __mydb
