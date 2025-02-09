import sqlite3
import csv

# Connexion à la base de données SQLite
db_path = "database/my_database.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Fonction pour importer un fichier CSV dans une table
def import_csv(file_path, table_name, columns):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Ignorer l'en-tête
        for row in reader:
            placeholders = ', '.join(['?'] * len(row))
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            cursor.execute(query, row)

# Importation des fichiers CSV
import_csv('data/customers.csv', 'customers', 'id,name, email')
import_csv('data/orders.csv', 'orders', 'id,customer_id, amount, date')

print("✅ Données importées avec succès !")

# Valider et fermer la connexion
conn.commit()
conn.close()

