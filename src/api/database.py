"""
Database connection and session management for GlowAI.
Uses SQLAlchemy with PostgreSQL - falls back to demo mode if unavailable
"""
import os
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import hashlib

# Get database URL from environment or use default
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:Gauri@2005@localhost:5432/ai_dermal")

# Create engine - will be None if connection fails
engine = None
db_connected = False

try:
    engine = create_engine(DATABASE_URL, pool_pre_ping=True, pool_recycle=3600)
    # Test the connection
    with engine.connect() as conn:
        pass
    db_connected = True
    print(f"✅ Database connected successfully to {engine.url.database}!")
except Exception as e:
    print(f"❌ Database connection failed: {e}")
    print("Running in demo mode without database.")
    engine = None

# Create base class
Base = declarative_base()


class GlowAIUser(Base):
    """User table model for login/registration"""
    __tablename__ = "glowai_users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    phone = Column(String(20))
    age = Column(Integer)
    gender = Column(String(20))
    skin_type = Column(String(50))
    skin_concerns = Column(Text)
    is_active = Column(Boolean, default=True)
    email_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime)
    login_count = Column(Integer, default=0)
    profile_image = Column(Text)
    address = Column(Text)
    city = Column(String(100))
    country = Column(String(100))
    pincode = Column(String(20))


class AnalysisLog(Base):
    """Analysis log table model"""
    __tablename__ = "analysis_logs"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    filename = Column(String(255))
    wrinkle_score = Column(Float, nullable=False)
    dark_spot_score = Column(Float, nullable=False)
    puffy_eye_score = Column(Float, nullable=False)
    predicted_skin_age = Column(Float, nullable=False)
    health_score = Column(Float, nullable=False)
    confidence = Column(Float, nullable=False)
    health_category = Column(String(50), nullable=False)
    user_id = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    image_path = Column(Text)
    notes = Column(Text)


def init_db():
    """Initialize database and create tables"""
    if engine:
        try:
            Base.metadata.create_all(engine)
            print("✅ Database tables created successfully!")
        except Exception as e:
            print(f"Error creating tables: {e}")
    else:
        print("Database not connected.")


def hash_password(password: str) -> str:
    """Hash password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()


def save_user(full_name: str, email: str, password: str, age: int = None, **kwargs) -> tuple:
    """Save new user to database"""
    if not engine:
        return False, "Database not connected"
    
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # Check if email exists
        existing = session.query(GlowAIUser).filter_by(email=email).first()
        if existing:
            session.close()
            return False, "Email already registered!"
        
        # Create new user
        user = GlowAIUser(
            full_name=full_name,
            email=email,
            password_hash=hash_password(password),
            age=age,
            created_at=datetime.utcnow()
        )
        
        session.add(user)
        session.commit()
        session.close()
        print(f"✅ User saved: {email}")
        return True, "User created successfully!"
    except Exception as e:
        return False, f"Error: {str(e)}"


def verify_user_login(email: str, password: str) -> tuple:
    """Verify user login and return (success, user_data)"""
    if not engine:
        return False, None
    
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        
        user = session.query(GlowAIUser).filter_by(email=email).first()
        if user and user.password_hash == hash_password(password):
            # Update last login
            user.last_login = datetime.utcnow()
            user.login_count = (user.login_count or 0) + 1
            session.commit()
            
            user_data = {
                'id': user.id,
                'full_name': user.full_name,
                'email': user.email,
                'age': user.age,
                'skin_type': user.skin_type
            }
            session.close()
            return True, user_data
        
        session.close()
        return False, None
    except Exception as e:
        print(f"Login error: {e}")
        return False, None


def get_user_by_email(email: str):
    """Get user by email"""
    if not engine:
        return None
    
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        user = session.query(GlowAIUser).filter_by(email=email).first()
        session.close()
        
        if user:
            return {
                'id': user.id,
                'full_name': user.full_name,
                'email': user.email,
                'age': user.age,
                'created_at': user.created_at.isoformat() if user.created_at else None
            }
        return None
    except:
        return None


def save_analysis_log(data: dict) -> bool:
    """Save analysis result to database"""
    if not engine:
        print("Database not connected. Cannot save.")
        return False
    
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        
        log = AnalysisLog(
            filename=data.get('filename', 'unknown'),
            wrinkle_score=data.get('wrinkle_score', 0),
            dark_spot_score=data.get('dark_spot_score', 0),
            puffy_eye_score=data.get('puffy_eye_score', 0),
            predicted_skin_age=data.get('predicted_skin_age', 0),
            health_score=data.get('health_score', 0),
            confidence=data.get('confidence', 0),
            health_category=data.get('health_category', 'Unknown')
        )
        
        session.add(log)
        session.commit()
        session.close()
        print(f"✅ Saved to database: {data.get('filename')}")
        return True
    except Exception as e:
        print(f"Error saving to database: {e}")
        return False


def get_logs(limit: int = 100):
    """Get analysis logs from database"""
    if not engine:
        return []
    
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        
        logs = session.query(AnalysisLog).order_by(
            AnalysisLog.created_at.desc()
        ).limit(limit).all()
        
        results = []
        for log in logs:
            results.append({
                'id': log.id,
                'filename': log.filename,
                'wrinkle_score': log.wrinkle_score,
                'dark_spot_score': log.dark_spot_score,
                'puffy_eye_score': log.puffy_eye_score,
                'predicted_skin_age': log.predicted_skin_age,
                'health_score': log.health_score,
                'confidence': log.confidence,
                'health_category': log.health_category,
                'created_at': log.created_at.isoformat() if log.created_at else None
            })
        
        session.close()
        return results
    except Exception as e:
        print(f"Error fetching logs: {e}")
        return []
