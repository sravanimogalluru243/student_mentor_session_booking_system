CREATE TABLE mentors (
    id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE NOT NULL,
    subject VARCHAR(200),
    availability VARCHAR(200),
    bio TEXT,
    CONSTRAINT fk_mentor_user FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);
