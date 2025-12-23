import mysql.connector

cnx = mysql.connector.connect(
    user='root', 
    host='localhost',
    passwords="",
    database='contacts_manager')

def get_cursor():
    cursor = cnx.cursor()
    return cursor