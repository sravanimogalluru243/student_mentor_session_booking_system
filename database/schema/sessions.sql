CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    mentor_id INTEGER NOT NULL REFERENCES mentors(id) ON DELETE CASCADE,
    session_title VARCHAR(200),
    session_date DATE,
    session_time TIME,
    duration INTEGER,
    status VARCHAR(30) DEFAULT 'Available',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
