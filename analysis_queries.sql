

USE ecommerce_db;

-- Query 1: Top 10 Product Categories by Orders
SELECT 
    p.product_category_name,
    COUNT(oi.order_id) AS total_orders
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_category_name
ORDER BY total_orders DESC
LIMIT 10;

-- Query 2: Monthly Revenue Analysis
SELECT 
    DATE_FORMAT(o.order_purchase_timestamp, '%Y-%m') AS month,
    ROUND(SUM(oi.price), 2) AS total_revenue
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
WHERE o.order_status = 'delivered'
GROUP BY month
ORDER BY month;

-- Query 3: Top 10 Cities by Orders
SELECT 
    customer_city,
    COUNT(order_id) AS total_orders
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY customer_city
ORDER BY total_orders DESC
LIMIT 10;

-- Query 4: Order Status Analysis
SELECT 
    order_status,
    COUNT(*) AS total_orders,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM orders), 2) AS percentage
FROM orders
GROUP BY order_status
ORDER BY total_orders DESC;

-- Query 5: Average Order Value
SELECT 
    ROUND(AVG(order_total), 2) AS avg_order_value,
    ROUND(MIN(order_total), 2) AS min_order,
    ROUND(MAX(order_total), 2) AS max_order
FROM (
    SELECT 
        order_id,
        SUM(price + freight_value) AS order_total
    FROM order_items
    GROUP BY order_id
) AS order_totals;