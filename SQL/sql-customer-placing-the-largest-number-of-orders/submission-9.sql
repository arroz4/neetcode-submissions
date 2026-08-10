-- Write your query below
SELECT customer_number
FROM orders
Group by customer_number
ORDER BY count(*) DESC
LIMIT 1;