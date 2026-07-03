SELECT mentor_id,COUNT(*) total_bookings
FROM bookings GROUP BY mentor_id ORDER BY total_bookings DESC;

SELECT AVG(rating) FROM feedback;

SELECT DATE_TRUNC('month',created_at) month,COUNT(*)
FROM bookings
GROUP BY month
ORDER BY month;
