-- Write your query below


SELECT c.name as customer_name,o.customer_id,o.order_id,o.order_date FROM 
(SELECT *, RANK() OVER (PARTITION BY customer_id ORDER BY order_date DESC) FROM orders) as o
JOIN customers c ON c.customer_id = o.customer_id
WHERE rank <=3
ORDER BY customer_name ASC,customer_id ASC,order_date DESC;