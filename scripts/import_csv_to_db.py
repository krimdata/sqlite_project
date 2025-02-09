import sqlite3
import csv

# Connexion à la base de données SQLite
conn = sqlite3.connect('orders.db')
cursor = conn.cursor()

# Création des tables si elles n'existent pas
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT,
    price REAL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date TEXT,
    total_amount REAL,
    FOREIGN KEY(customer_id) REFERENCES customers(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS order_tracking (
    order_id INTEGER,
    status TEXT,
    timestamp TEXT,
    FOREIGN KEY(order_id) REFERENCES orders(id)
)
''')

# Validation et fermeture de la connexion
conn.commit()
conn.close()

print("Les tables ont été créées avec succès.")
