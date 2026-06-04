-- =====================================================
-- AI Dermal Platform - PostgreSQL Database Setup
-- Run this script in pgAdmin to create the database
-- =====================================================

-- Step 1: Create the database (run in default 'postgres' database)
-- First, connect to the 'postgres' database and run:
-- CREATE DATABASE ai_dermal;

-- Then connect to 'ai_dermal' database and run everything below:

-- Step 2: Connect to ai_dermal database and run the following:

-- Create analysis_logs table
CREATE TABLE IF NOT EXISTS analysis_logs (
    id SERIAL PRIMARY KEY,
    filename VARCHAR(255),
    wrinkle_score FLOAT NOT NULL,
    dark_spot_score FLOAT NOT NULL,
    puffy_eye_score FLOAT NOT NULL,
    predicted_skin_age FLOAT NOT NULL,
    health_score FLOAT NOT NULL,
    confidence FLOAT NOT NULL,
    health_category VARCHAR(50) NOT NULL,
    user_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    image_path TEXT,
    notes TEXT
);

-- Create index for faster queries
CREATE INDEX IF NOT EXISTS idx_analysis_logs_created_at 
ON analysis_logs(created_at DESC);

CREATE INDEX IF NOT EXISTS idx_analysis_logs_health_category 
ON analysis_logs(health_category);

-- =====================================================
-- Optional: Insert sample data for testing
-- =====================================================
INSERT INTO analysis_logs (filename, wrinkle_score, dark_spot_score, puffy_eye_score, predicted_skin_age, health_score, confidence, health_category)
VALUES 
    ('test_image_001.jpg', 2.5, 15.3, 10.2, 32.5, 78.5, 0.92, 'Moderate'),
    ('test_image_002.jpg', 1.2, 8.5, 5.1, 25.0, 89.2, 0.95, 'Excellent'),
    ('test_image_003.jpg', 4.1, 28.7, 22.3, 48.0, 52.1, 0.85, 'Needs Care');

-- Verify table
SELECT * FROM analysis_logs LIMIT 10;
