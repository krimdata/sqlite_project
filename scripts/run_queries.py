import sqlite3

db_path = "database/my_database.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Lire le fichier queries.sql
with open("queries/queries.sql", "r", encoding="utf-8") as f:
    sql_script = f.read()

# Séparer les requêtes (chaque requête se termine par un point-virgule)
queries = [q.strip() for q in sql_script.split(";") if q.strip()]

for query in queries:
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print("Query:", query)
        print("Result:", result)
    except Exception as e:
        print("Error executing query:", query)
        print(e)

conn.close()
