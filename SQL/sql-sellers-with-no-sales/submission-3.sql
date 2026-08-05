-- Write your query below

Select seller_name FROM seller
Where seller_id not in (SELECT distinct(seller_id)FROM orders where sale_date between '2020-01-01' and '2020-12-31')
ORDER BY seller_name ASC;