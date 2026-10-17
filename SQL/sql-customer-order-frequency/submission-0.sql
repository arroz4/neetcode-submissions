-- Write your query below


--June 2020
SELECT customer_id, name FROM customers
WHERE customer_id in
(SELECT june.customer_id FROM 
    (SELECT customer_id FROM orders o 
    LEFT JOIN product p 
    ON p.product_id = o.product_id
    WHERE order_date >= '2020-06-01' and order_date < '2020-07-01'
    GROUP BY customer_id
    HAVING sum(o.quantity*p.price) >= 100) june
    JOIN 
    (SELECT customer_id FROM orders o 
    LEFT JOIN product p 
    ON p.product_id = o.product_id
    WHERE order_date >= '2020-07-01' and order_date < '2020-08-01'
    GROUP BY customer_id
    HAVING sum(o.quantity*p.price) >= 100) july
ON july.customer_id = june.customer_id)

