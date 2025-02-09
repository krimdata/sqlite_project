import sqlite3

# Connexion à la base de données SQLite
conn = sqlite3.connect('orders.db')
cursor = conn.cursor()

# Fonction pour exécuter les requêtes SQL depuis un fichier
def execute_sql_from_file(file_path):
    with open(file_path, 'r') as file:
        sql_queries = file.read()
        cursor.executescript(sql_queries)  # Exécute plusieurs requêtes SQL à partir du fichier
        conn.commit()

# Exécution des requêtes SQL à partir du fichier
execute_sql_from_file('queries/queries.sql')

# Affichage des résultats pour chaque requête
cursor.execute('SELECT SUM(total_amount) FROM orders')
print("Total des ventes:", cursor.fetchone()[0])

cursor.execute('SELECT AVG(total_amount) FROM orders')
print("Moyenne des montants des commandes:", cursor.fetchone()[0])

cursor.execute('''
    SELECT customers.name, COUNT(orders.id) AS order_count
    FROM customers
    JOIN orders ON customers.id = orders.customer_id
    GROUP BY customers.id
''')
for row in cursor.fetchall():
    print(f'{row[0]}: {row[1]} commandes')

cursor.execute('''
    SELECT order_tracking.status, COUNT(order_tracking.order_id) AS order_status_count
    FROM order_tracking
    GROUP BY order_tracking.status
''')
for row in cursor.fetchall():
    print(f'{row[0]}: {row[1]} commandes')

cursor.execute('''
    SELECT products.name, SUM(orders.total_amount) AS product_sales
    FROM orders
    JOIN products ON orders.id = products.id
    GROUP BY products.id
''')
for row in cursor.fetchall():
    print(f'{row[0]}: {row[1]} ventes')

# Fermeture de la connexion à la base de données
conn.close()
