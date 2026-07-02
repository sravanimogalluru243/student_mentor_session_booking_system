CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL REFERENCES students(id) ON DELETE CASCADE,
    mentor_id INTEGER NOT NULL REFERENCES mentors(id) ON DELETE CASCADE,
    subject VARCHAR(200),
    booking_date DATE,
    booking_time TIME,
    status VARCHAR(30) DEFAULT 'Pending',
    attendance VARCHAR(20) DEFAULT '-',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
