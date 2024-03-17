-- lists records with name from tables by order
SELECT score, name FROM second_table WHERE name IS NOT NULL 
ORDER BY score DESC;
