-- Write a script max hbtn_0c_0 database
SELECT state, MAX(value) AS max_temp FROM temperatures
GROUP BY state
ORDER BY state;
