"""
Main FastAPI Application for AI Dermal Platform
Entry point for the REST API
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging
from datetime import datetime
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.api.endpoints import router as api_router
from src.api.database import init_db

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager"""
    # Startup
    logger.info("Starting AI Dermal API...")
    logger.info(f"Started at: {datetime.utcnow()}")
    
    # Initialize database
    try:
        init_db()
        logger.info("Database initialized")
    except Exception as e:
        logger.warning(f"Database initialization skipped: {e}")
    
    yield
    
    # Shutdown
    logger.info("Shutting down AI Dermal API...")


# Create FastAPI application
app = FastAPI(
    title="AI Dermal - Facial Aging Intelligence & Skin Health Analytics",
    description="""
    ## Overview
    
    AI-Powered Facial Aging Intelligence & Skin Health Analytics Platform provides
    comprehensive skin health analysis using deep learning.
    
    ### Features
    
    - **Multi-Task Learning**: Simultaneous prediction of 4 skin health indicators
    - **Face Detection**: MediaPipe-based facial landmark extraction
    - **Explainable AI**: Grad-CAM heatmaps for model interpretability
    - **Health Scoring**: Custom skin health metric with severity categorization
    - **Analytics Dashboard**: Interactive visualizations
    
    ### Skin Health Score
    
    ```
    Skin Health Score = 100 - (0.4 × Wrinkle Score + 0.3 × Dark Spot Score + 0.3 × Puffy Eye Score)
    ```
    
    ### Categories
    
    | Score | Category |
    |-------|----------|
    | 80-100 | Excellent |
    | 60-79 | Moderate |
    | 0-59 | Needs Care |
    """,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include routers
app.include_router(api_router, prefix="/api/v1", tags=["Analysis"])


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to AI Dermal API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/api/v1/health"
    }


@app.get("/api/v1/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "version": "1.0.0",
        "timestamp": datetime.utcnow().isoformat()
    }


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "src.api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
