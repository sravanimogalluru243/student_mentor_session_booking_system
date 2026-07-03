CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE NOT NULL,
    course VARCHAR(120),
    CONSTRAINT fk_student_user FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);
