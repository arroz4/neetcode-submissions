-- Write your query below

SELECT transaction_id FROM 
(SELECT transaction_id,date(day) as date,amount,rank() OVER (PARTITION BY date(day) ORDER BY amount DESC) FROM transactions) as t
WHERE rank = 1
ORDER BY transaction_id ASC;
