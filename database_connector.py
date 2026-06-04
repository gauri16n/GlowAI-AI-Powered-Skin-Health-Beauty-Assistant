"""
PostgreSQL Database Connector for GlowAI
Using pgAdmin - ai_dermal database
"""
import psycopg2
from psycopg2.extras import RealDictCursor
import hashlib
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'ai_dermal',
    'user': 'postgres',
    'password': 'Gauri@2005'
}

DB_AVAILABLE = True


def hash_password(password):
    """Hash password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()


class GlowAIUser:
    """User model class"""
    def __init__(self, id=None, username=None, email=None, full_name=None, age=None):
        self.id = id
        self.username = username
        self.email = email
        self.full_name = full_name
        self.age = age


def get_connection():
    """Get PostgreSQL database connection"""
    return psycopg2.connect(**DB_CONFIG)


def init_db():
    """Initialize PostgreSQL database and create tables"""
    conn = get_connection()
    c = conn.cursor()
    
    # Create users table - check if exists and create
    c.execute("""CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100),
        email VARCHAR(255) UNIQUE NOT NULL,
        password_hash VARCHAR(255) NOT NULL,
        full_name VARCHAR(100),
        age INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
    
    # Create analysis_logs table
    c.execute("""CREATE TABLE IF NOT EXISTS analysis_logs (
        id SERIAL PRIMARY KEY,
        user_id INTEGER,
        filename TEXT,
        wrinkle_score FLOAT,
        dark_spot_score FLOAT,
        puffy_eye_score FLOAT,
        acne_score FLOAT,
        blackheads_score FLOAT,
        predicted_skin_age FLOAT,
        health_score FLOAT,
        health_category TEXT,
        confidence FLOAT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
    
    conn.commit()
    conn.close()
    print("✅ PostgreSQL Database initialized!")


def save_user(full_name, email, password, age=25):
    """Create new user"""
    username = email.split('@')[0]
    password_hash = hash_password(password)
    created_at = datetime.now()
    
    try:
        conn = get_connection()
        c = conn.cursor()
        c.execute("""INSERT INTO users (username, email, password_hash, full_name, age, created_at) 
                     VALUES (%s, %s, %s, %s, %s, %s)""",
                  (username, email, password_hash, full_name, age, created_at))
        conn.commit()
        conn.close()
        return True, "User created!"
    except psycopg2.IntegrityError:
        return False, "Email already exists"
    except Exception as e:
        return False, str(e)


def verify_user_login(email, password):
    """Verify user login"""
    password_hash = hash_password(password)
    
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id, full_name, age FROM users WHERE email=%s AND password_hash=%s", (email, password_hash))
    row = c.fetchone()
    conn.close()
    
    if row:
        return True, {'id': row[0], 'full_name': row[1], 'age': row[2]}
    return False, None


def get_user_by_email(email):
    """Get user by email"""
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=%s", (email,))
    row = c.fetchone()
    conn.close()
    
    if row:
        columns = ['id', 'username', 'email', 'password_hash', 'full_name', 'age', 'created_at']
        return dict(zip(columns, row))
    return None


def save_analysis_log(result, user_id=None):
    """Save analysis to database"""
    try:
        conn = get_connection()
        c = conn.cursor()
        timestamp = datetime.now()
        
        c.execute("""INSERT INTO analysis_logs 
                     (user_id, filename, wrinkle_score, dark_spot_score, puffy_eye_score, 
                      acne_score, blackheads_score, predicted_skin_age, health_score, health_category, confidence, timestamp)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                  (user_id, result.get('filename'), result.get('wrinkle_score'), result.get('dark_spot_score'),
                   result.get('puffy_eye_score'), result.get('acne_score'), result.get('blackheads_score'),
                   result.get('predicted_skin_age'), result.get('health_score'), result.get('health_category'),
                   result.get('confidence'), timestamp))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Save log error: {e}")
        return False


def get_logs(limit=100, user_id=None):
    """Get analysis logs"""
    conn = get_connection()
    c = conn.cursor()
    
    if user_id:
        c.execute("SELECT * FROM analysis_logs WHERE user_id=%s ORDER BY id DESC LIMIT %s", (user_id, limit))
    else:
        c.execute("SELECT * FROM analysis_logs ORDER BY id DESC LIMIT %s", (limit,))
    
    columns = ['id', 'user_id', 'filename', 'wrinkle_score', 'dark_spot_score', 'puffy_eye_score', 
                'acne_score', 'blackheads_score', 'predicted_skin_age', 'health_score', 
                'health_category', 'confidence', 'timestamp']
    
    rows = c.fetchall()
    conn.close()
    return [dict(zip(columns, row)) for row in rows]


# Auto-initialize on import
try:
    init_db()
    print("✅ Database module loaded successfully!")
except Exception as e:
    print(f"⚠️ Database init: {e}")
    DB_AVAILABLE = False


if __name__ == "__main__":
    init_db()
    print("✅ Database ready!")

