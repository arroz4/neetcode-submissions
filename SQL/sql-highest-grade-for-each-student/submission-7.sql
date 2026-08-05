-- Write your query below

WITH ranked_scores AS(
SELECT *, ROW_NUMBER() OVER (PARTITION BY student_id ORDER BY student_id, score DESC, exam_id) as score_rank
FROM exam_results
)

Select student_id,exam_id,score
FROM ranked_scores
WHERE score_rank=1
ORDER BY student_id, score DESC, exam_id;