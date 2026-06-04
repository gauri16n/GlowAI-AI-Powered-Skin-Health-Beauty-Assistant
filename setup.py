##streamlit run src\dashboard\app.py



from setuptools import setup, find_packages

setup(
    name="ai_dermal",
    version="1.0.0",
    description="AI-Powered Facial Aging Intelligence & Skin Health Analytics Platform",
    author="AI Developer",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=[
        # Core ML/DL Dependencies
        "tensorflow>=2.15.0",
        "keras>=2.15.0",
        "numpy>=1.24.0",
        "pandas>=2.0.0",
        "scikit-learn>=1.3.0",
        "opencv-python-headless>=4.8.0",
        "Pillow>=10.0.0",
        
        # Face Detection & Preprocessing
        "mediapipe>=0.10.0",
        "mtcnn>=0.1.1",
        
        # API & Backend
        "fastapi>=0.109.0",
        "uvicorn[standard]>=0.27.0",
        "python-multipart>=0.0.6",
        "pydantic>=2.5.0",
        "pydantic-settings>=2.1.0",
        
        # Database
        "psycopg2-binary>=2.9.9",
        "sqlalchemy>=2.0.0",
        "alembic>=1.13.0",
        
        # Dashboard & Visualization
        "streamlit>=1.30.0",
        "plotly>=5.18.0",
        "altair>=5.1.0",
        "matplotlib>=3.8.0",
        "seaborn>=0.13.0",
        
        # MLOps
        "mlflow>=2.10.0",
        "tensorboard>=2.15.0",
        
        # Utilities
        "python-dotenv>=1.0.0",
        "tqdm>=4.66.0",
        "joblib>=1.3.0",
        "scipy>=1.11.0",
        
        # Image Processing
        "imageio>=2.31.0",
        "imageio-ffmpeg>=0.4.9",
        
        # Logging
        "loguru>=0.7.0",
        
        # For notebook support
        "ipykernel>=6.26.0",
        "ipywidgets>=8.1.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "httpx>=0.26.0",
        ]
    }
)
