
-- Create Users Table for GlowAI
-- Run this script in pgAdmin to create the users table

-- Drop table if exists
DROP TABLE IF EXISTS glowai_users CASCADE;

-- Create users table
CREATE TABLE glowai_users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    age INTEGER,
    gender VARCHAR(20),
    skin_type VARCHAR(50),
    skin_concerns TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    email_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP,
    login_count INTEGER DEFAULT 0,
    profile_image TEXT,
    address TEXT,
    city VARCHAR(100),
    country VARCHAR(100),
    pincode VARCHAR(20)
);

-- Create index for faster lookups
CREATE INDEX idx_users_email ON glowai_users(email);

-- Add some sample test users
INSERT INTO glowai_users (full_name, email, password_hash, age) VALUES 
('Test User', 'test@glowai.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 25),
('Demo User', 'demo@glowai.com', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92', 30);

-- View all users
SELECT id, full_name, email, age, created_at, last_login FROM glowai_users;
