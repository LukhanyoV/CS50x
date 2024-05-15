SELECT DISTINCT(p.name) FROM stars AS s
JOIN movies AS m ON m.id = s.movie_id
JOIN people AS p ON p.id = s.person_id
WHERE m.year = 2004
ORDER BY birth;
