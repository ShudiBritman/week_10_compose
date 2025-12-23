import mysql.connector



def get_connection():
    cnx = mysql.connector.connect(
    user='root',
    host='localhost',
    password="1234",
    database='contacts_manager')
    return cnx