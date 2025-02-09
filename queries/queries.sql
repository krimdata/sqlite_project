-- Total Sales (calculé en multipliant quantity par price)
SELECT SUM(orders.quantity * products.price) AS total_sales
FROM orders
JOIN products ON orders.product_id = products.id;

-- Average Order Value
SELECT AVG(orders.quantity * products.price) AS average_order_value
FROM orders
JOIN products ON orders.product_id = products.id;

-- Number of Orders per Customer
SELECT customers.name, COUNT(orders.id) AS order_count
FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id
GROUP BY customers.id;

-- Product Sales (total quantity sold per product)
SELECT products.name, SUM(orders.quantity) AS total_quantity_sold
FROM orders
JOIN products ON orders.product_id = products.id
GROUP BY products.id;
