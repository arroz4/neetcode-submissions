-- Write your query below


WITH top_bottom_students AS (
    SELECT student_id FROM (
        SELECT student_id, 
               RANK() OVER (PARTITION BY exam_id ORDER BY score DESC) AS rnk
        FROM exam
    ) t WHERE rnk = 1
    UNION
    SELECT student_id FROM (
        SELECT student_id, 
               RANK() OVER (PARTITION BY exam_id ORDER BY score ASC) AS rnk
        FROM exam
    ) t WHERE rnk = 1
)
SELECT s.student_id, s.student_name
FROM student s
WHERE s.student_id IN (SELECT student_id FROM exam)
  AND s.student_id NOT IN (SELECT student_id FROM top_bottom_students)
ORDER BY s.student_id;