-- Displays all the cities followed by their states
SELECT id, cities.name, state.name FROM cities
LEFT JOIN states ON cities.state_id = states.name;
