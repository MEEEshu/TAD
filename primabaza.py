import sqlite3
conn = sqlite3.connect("myDB.db")

#print(conn)

q='SELECT * FROM Meteo'

cursor = conn.execute(q)

print(cursor)

for line in cursor:
    print(line)