-- Write your query below

SELECT project_id, employee_id FROM
(
SELECT *, RANK() OVER (PARTITION BY project_id ORDER BY total_experience DESC) as r FROM
(
SELECT p.project_id, p.employee_id, xp.total_experience 
FROM project p
JOIN 
(SELECT e.employee_id, e.experience_years as total_experience FROM employee e) xp
ON xp.employee_id = p.employee_id
) ranking
) result
WHERE r = 1