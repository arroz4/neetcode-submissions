-- Write your query below

SELECT id, 
    CASE
        WHEN p_id is NULL THEN 'Root'
        WHEN id in (SELECT p_id FROM tree WHERE p_id is not NULL) THEN 'Inner'
        ELSE 'Leaf'
    END as type
FROM tree