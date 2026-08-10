-- Write your query below
Select name as warehouse_name, sum(product_volume) as volume FROM
(Select w.name,w.product_id,sum(w.units * p.width* p.length* p.height) as product_volume FROM warehouse w
LEFT JOIN products  p ON w.product_id = p.product_id
GROUP BY w.name,w.product_id) AS result
GROUP BY warehouse_name