SELECT s.id,u.name,COUNT(b.id) total_bookings
FROM students s
JOIN users u ON s.user_id=u.id
LEFT JOIN bookings b ON s.id=b.student_id
GROUP BY s.id,u.name;

SELECT m.id,u.name,COUNT(b.id) sessions_taken
FROM mentors m
JOIN users u ON m.user_id=u.id
LEFT JOIN bookings b ON m.id=b.mentor_id
GROUP BY m.id,u.name;
