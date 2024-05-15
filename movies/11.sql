SELECT m.title FROM stars AS s
JOIN movies AS m ON m.id = s.movie_id
JOIN people AS p ON p.id = s.person_id
JOIN ratings AS r ON r.movie_id = m.id
WHERE p.name = 'Chadwick Boseman'
ORDER BY r.rating DESC
LIMIT 5;
