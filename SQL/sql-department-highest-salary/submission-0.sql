-- Write your query below


SELECT d.name as department,e.name as employee, e.salary as salary FROM (SELECT *, RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) FROM employee e) as e
JOIN department d ON e.department_id= d.id
WHERE rank = 1