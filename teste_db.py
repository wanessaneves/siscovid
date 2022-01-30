import sqlite3

connection = sqlite3.connect('database.db')

cursor = connection.cursor()

cursor.execute("INSERT INTO cities (name, uf) VALUES('Fortaleza', 'CE')")

connection.commit()

connection.close()
