-- Write your query below

/* THIS IS WRONG BECAUSE I DIDNT SPECIFY iN THE STAR SIGN the proper t.team_id vs t2.team_id
SELECT * FROM matches 
LEFT JOIN teams t ON t.team_id = matches.guest_team 
LEFT JOIN teams t2 ON t2.team_id =  matches.host_team
*/

--GUEST GOALS 

SELECT team_id,team_name,coalesce(sum(points),0) as num_points FROM
(SELECT 
    team_id,team_name,
    COALESCE(
    CASE
        WHEN host_goals < guest_goals THEN 3
        WHEN host_goals = guest_goals THEN 1
        ELSE 0
    END,0) AS points
FROM matches m
FULL OUTER JOIN teams t ON t.team_id = m.guest_team 
UNION ALL
-- HOST GOALS
SELECT 
    team_id,team_name,
    COALESCE(
    CASE
        WHEN host_goals > guest_goals THEN 3
        WHEN host_goals = guest_goals THEN 1
        ELSE 0
    END,0) AS points
FROM matches m
FULL OUTER JOIN teams t2 ON t2.team_id = m.host_team) as combined
GROUP BY team_id,team_name 
ORDER BY num_points DESC,team_id; 

