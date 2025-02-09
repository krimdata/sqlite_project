import sqlite3
import os

# Assurer que le dossier "database" existe
os.makedirs("database", exist_ok=True)

# Connexion à la base de données SQLite
db_path = "database/my_database.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Création des tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    amount REAL,
    date TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
)
''')

print("✅ Base de données et tables créées avec succès !")

# Valider et fermer la connexion
conn.commit()
conn.close()
