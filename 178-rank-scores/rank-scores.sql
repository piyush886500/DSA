-- Write your PostgreSQL query statement below
SELECT score, dense_rank() over (order by score DESC) AS rank 
FROM Scores;