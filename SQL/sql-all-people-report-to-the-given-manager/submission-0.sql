-- Write your query below

/* FIRST LEVEL (SELECT employee_id FROM employees WHERE manager_id = 1 and employee_id !=1) */
/*SECOND LEVEL
SELECT employee_id FROM employees e
WHERE manager_id in
(SELECT employee_id FROM employees
WHERE manager_id = 1 and employee_id !=1)
*/

SELECT employee_id FROM employees
WHERE manager_id in (
    SELECT employee_id FROM employees e
    WHERE manager_id in
    (SELECT employee_id FROM employees
    WHERE manager_id = 1 and employee_id !=1)
)
UNION
SELECT employee_id FROM employees e
WHERE manager_id in
(SELECT employee_id FROM employees
WHERE manager_id = 1 and employee_id !=1)
UNION
SELECT employee_id FROM employees WHERE manager_id = 1 and employee_id !=1