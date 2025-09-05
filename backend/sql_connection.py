import mysql.connector

__mydb = None

def get_sql_connection():
    
    global __mydb

    if(__mydb==None):
        __mydb = mysql.connector.connect(
            host="",
            username="",
            password="",
            database=""
        )

    return __mydb

