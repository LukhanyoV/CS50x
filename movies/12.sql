SELECT m.title FROM stars AS s
JOIN movies AS m ON m.id = s.movie_id
JOIN people AS p ON p.id = s.person_id
WHERE p.name = 'Bradley Cooper'

INTERSECT

SELECT m.title FROM stars AS s
JOIN movies AS m ON m.id = s.movie_id
JOIN people AS p ON p.id = s.person_id
WHERE p.name = 'Jennifer Lawrence';
