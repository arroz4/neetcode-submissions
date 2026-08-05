-- Write your query below
SELECT users.name,COALESCE(sum(rides.distance),0) as travelled_distance FROM users
LEFT JOIN rides on rides.user_id= users.id 
GROUP BY users.name
ORDER BY travelled_distance DESC,users.name ASC;