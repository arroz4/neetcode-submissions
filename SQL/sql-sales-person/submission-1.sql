-- Write your query below

Select name FROM sales_person
WHERE sales_id not in (SELECT DISTINCT sales_id FROM orders 
LEFT JOIN company ON orders.com_id = company.com_id
WHERE name = 'CRIMSON');