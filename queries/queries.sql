-- Total des ventes
SELECT SUM(total_amount) AS total_sales
FROM orders;

-- Moyenne des montants des commandes
SELECT AVG(total_amount) AS average_order_value
FROM orders;

-- Nombre de commandes par client
SELECT customers.name, COUNT(orders.id) AS order_count
FROM customers
JOIN orders ON customers.id = orders.customer_id
GROUP BY customers.id;

-- Statut des commandes
SELECT order_tracking.status, COUNT(order_tracking.order_id) AS order_status_count
FROM order_tracking
GROUP BY order_tracking.status;

-- Chiffre d'affaires par produit
SELECT products.name, SUM(orders.total_amount) AS product_sales
FROM orders
JOIN products ON orders.id = products.id
GROUP BY products.id;
