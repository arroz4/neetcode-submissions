-- Write your query below
--apple.sale_date, abs(apple.sold_apples - orange.sold_oranges) as diff
SELECT apple.sale_date, apple.sold_apples - orange.sold_oranges as diff FROM
(SELECT sale_date, 
    CASE
    WHEN fruit = 'apples' THEN sold_num
    END AS sold_apples
FROM sales ) as apple
LEFT JOIN 
(SELECT sale_date, 
    CASE
    WHEN fruit = 'oranges' THEN sold_num
    END as sold_oranges
FROM sales) as orange
ON orange.sale_date = apple.sale_date
WHERE apple.sold_apples is not null and orange.sold_oranges is not null
