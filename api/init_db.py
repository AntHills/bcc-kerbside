import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
  connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO datefetches (updated) VALUES(CURRENT_TIMESTAMP)")

connection.commit()
connection.close()