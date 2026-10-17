-- Write your query below

-- person table with country code
SELECT country FROM (SELECT c1.caller_id,c1.duration FROM calls c1
UNION ALL
SELECT c2.callee_id,c2.duration FROM calls c2) callers
LEFT JOIN
(
SELECT p.id,c.name as country FROM person p
LEFT JOIN country c ON c.country_code = LEFT(p.phone_number,3)
) country
ON country.id = callers.caller_id
GROUP BY country
HAVING avg(duration) > (SELECT avg(duration) as global_avg FROM calls)



--GLOBAL AVG
--SELECT avg(duration) as global_avg FROM calls