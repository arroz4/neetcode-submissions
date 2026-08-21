-- Write your query below

 SELECT p.product_name, p.product_id, o.order_id,o.order_date FROM products p
 JOIN (SELECT *,rank() OVER (PARTITION BY product_id order by order_date DESC) FROM orders) as o
 ON p.product_id = o.product_id
 WHERE rank = 1
 ORDER BY product_name,product_id,order_id