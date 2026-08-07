-- Write your query below

Select 
left_operand,operator,right_operand,
CASE
    WHEN operator = '=' and left_operand_value = value THEN true
    WHEN operator = '>' and left_operand_value > value THEN true
    WHEN operator = '<' and left_operand_value < value THEN true
    ELSE false
END AS value
FROM
(SELECT value as left_operand_value,left_operand,operator,right_operand FROM expressions
LEFT JOIN variables ON expressions.left_operand = variables.name) as LO
LEFT JOIN variables ON LO.right_operand = variables.name