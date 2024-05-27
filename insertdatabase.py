import sqlite3

# Lista cu datele despre mașini
cars = [
    {"id": 1, "brand": "Toyota", "model": "Corolla", "an": 2019},
    {"id": 2, "brand": "Honda", "model": "Civic", "an": 2020},
    {"id": 3, "brand": "Lancia", "model": "Delta", "an": 2006},
    {"id": 4, "brand": "Skoda", "model": "Octavia", "an": 2007},
    {"id": 5, "brand": "VW", "model": "Polo", "an": 2021},
    {"id": 6, "brand": "Hyundai", "model": "I30", "an": 2018},
    {"id": 7, "brand": "Opel", "model": "Astra", "an": 2012},
    {"id": 8, "brand": "Daewoo", "model": "Cielo", "an": 1997},
    {"id": 9, "brand": "Mitsubishi", "model": "Lancer", "an": 2003}
]

# Conectare la baza de date
conn = sqlite3.connect('cardata.db')

# Creare cursor pentru a executa comenzi SQL
cur = conn.cursor()

# Creare tabel "Cars" (dacă nu există deja)
cur.execute('''CREATE TABLE IF NOT EXISTS Cars
               (id INTEGER PRIMARY KEY, brand TEXT, model TEXT, an INTEGER)''')

# Inserare date în tabel
for car in cars:
    cur.execute("INSERT INTO Cars (id, brand, model, an) VALUES (?, ?, ?, ?)",
                (car["id"], car["brand"], car["model"], car["an"]))

# Salvare modificări și închidere conexiune
conn.commit()
conn.close()

print("Datele au fost introduse cu succes în baza de date.")
