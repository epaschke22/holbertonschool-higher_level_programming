-- Lists all the cities of Calafornia
SELECT * FROM cities WHERE stat_id = (
SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
