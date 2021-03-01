-- Displays all scors and number of enerties with that same score
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score DESC;
