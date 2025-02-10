import sqlite3
import csv

db_path = "database/my_database.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

def import_csv(file_path, table_name, columns):
    # columns doit être une chaîne de colonnes séparées par une virgule, par exemple "name, email"
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cols = [col.strip() for col in columns.split(',')]
            values = [row[col] for col in cols]
            placeholders = ', '.join(['?'] * len(values))
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            cursor.execute(query, values)
        conn.commit()

# Importer les données pour chaque table ok
import_csv("data/products.csv", "products", "name, description, price, stock")
import_csv("data/customers.csv", "customers", "name, email")
import_csv("data/orders.csv", "orders", "customer_id, product_id, quantity, date")

conn.close()
print("✅ CSV data imported successfully!")


