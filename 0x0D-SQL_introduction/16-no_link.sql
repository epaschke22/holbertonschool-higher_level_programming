-- Lists all items of a table except rows without names
Select score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
