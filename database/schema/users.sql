-- Drop table if it already exists
DROP TABLE IF EXISTS users CASCADE;

-- Create users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,

    name VARCHAR(100) NOT NULL,

    email VARCHAR(150) UNIQUE NOT NULL,

    password_hash TEXT NOT NULL,

    role VARCHAR(20) NOT NULL
        CHECK(role IN ('student','mentor','admin')),

    phone VARCHAR(15),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);