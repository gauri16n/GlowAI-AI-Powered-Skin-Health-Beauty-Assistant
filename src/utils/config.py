"""
Configuration Management for AI Dermal Platform
"""
import os
from pathlib import Path
from typing import Optional
from dataclasses import dataclass
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base Paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
MODEL_DIR = BASE_DIR / "models"
LOG_DIR = BASE_DIR / "logs"


@dataclass
class ModelConfig:
    """Model configuration settings"""
    input_shape: tuple = (224, 224, 3)
    num_classes: int = 4
    learning_rate: float = 0.0001
    batch_size: int = 32
    epochs: int = 50
    early_stopping_patience: int = 10
    k_folds: int = 5
    dropout_rate: float = 0.3
    
    # Class names
    wrinkle_classes: list = None
    dark_spot_classes: list = None
    puffy_eye_classes: list = None
    
    def __post_init__(self):
        self.wrinkle_classes = [f"wrinkle_{i}" for i in range(6)]
        self.dark_spot_classes = [f"spot_{i}" for i in range(6)]
        self.puffy_eye_classes = [f"puffy_{i}" for i in range(6)]


@dataclass
class DataConfig:
    """Data configuration settings"""
    # Point to your new dataset location
    train_dir: Path = BASE_DIR / "DATASET-20251202T142134Z-1-001" / "DATASET"
    processed_dir: Path = DATA_DIR / "processed"
    augmented_dir: Path = DATA_DIR / "augmented"
    img_size: tuple = (224, 224)
    validation_split: float = 0.2
    seed: int = 42


@dataclass
class DatabaseConfig:
    """Database configuration settings"""
    host: str = os.getenv("DB_HOST", "localhost")
    port: int = int(os.getenv("DB_PORT", "5432"))
    name: str = os.getenv("DB_NAME", "ai_dermal")
    user: str = os.getenv("DB_USER", "postgres")
    password: str = os.getenv("DB_PASSWORD", "postgres")
    
    @property
    def url(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


@dataclass
class APIConfig:
    """API configuration settings"""
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = True
    cors_origins: list = None
    
    def __post_init__(self):
        self.cors_origins = ["*"]


@dataclass
class MLflowConfig:
    """MLflow configuration settings"""
    tracking_uri: str = os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000")
    experiment_name: str = "ai_dermal_experiments"
    artifact_location: str = str(MODEL_DIR / "artifacts")


# Create directories if they don't exist
def ensure_directories():
    """Ensure all required directories exist"""
    directories = [
        DATA_DIR,
        DATA_DIR / "raw",
        DATA_DIR / "raw" / "clear skin",
        DATA_DIR / "raw" / "wrinkles",
        DATA_DIR / "raw" / "dark spots",
        DATA_DIR / "raw" / "puffy eyes",
        DATA_DIR / "processed",
        DATA_DIR / "augmented",
        MODEL_DIR,
        LOG_DIR,
    ]
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)


# Initialize directories on module import
ensure_directories()

# Export configurations
model_config = ModelConfig()
data_config = DataConfig()
database_config = DatabaseConfig()
api_config = APIConfig()
mlflow_config = MLflowConfig()
