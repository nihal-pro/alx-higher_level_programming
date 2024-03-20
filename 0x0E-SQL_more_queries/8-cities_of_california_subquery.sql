-- lists cities in localhost
SELECT id, name FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name = 'California')
ORDER BY id;
