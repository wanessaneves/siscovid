import sqlite3

def get_connection():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    return (connection, cursor)
