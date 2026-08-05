-- Write your query below



Select name from customers
FULL OUTER JOIN orders ON customers.id = orders.customer_id
WHERE customer_id IS NULL;