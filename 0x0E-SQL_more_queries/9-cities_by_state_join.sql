-- Script that lists all cities contained in the database hbtn_0d_usa
SELECT cities.id, cities.name, (
	SELECT states.name
	FROM states
	WHERE cities.state_id = states.id
)
AS state_name
FROM cities
ORDER BY cities.id
ASC;
