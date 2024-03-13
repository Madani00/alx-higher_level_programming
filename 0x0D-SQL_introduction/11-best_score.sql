-- diplay records of a table by order score(top first)
-- condition score >= 10

SELECT score, name FROM second_table
WHERE score >= 10 ORDER BY score DESC;
