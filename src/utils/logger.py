"""
Logging Configuration for AI Dermal Platform
"""
import sys
import logging
from pathlib import Path
from loguru import logger
from datetime import datetime


def setup_logger(name: str = "ai_dermal", log_file: str = None):
    """
    Setup logger with file and console handlers
    
    Args:
        name: Logger name
        log_file: Optional log file path
    
    Returns:
        Configured logger instance
    """
    # Remove default handler
    logger.remove()
    
    # Add console handler with custom format
    logger.add(
        sys.stdout,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>",
        level="INFO",
        colorize=True
    )
    
    # Add file handler if log_file is provided
    if log_file is None:
        log_dir = Path(__file__).resolve().parent.parent.parent / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        log_file = log_dir / f"ai_dermal_{datetime.now().strftime('%Y%m%d')}.log"
    
    logger.add(
        log_file,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function} - {message}",
        level="DEBUG",
        rotation="10 MB",
        retention="30 days",
        compression="zip"
    )
    
    return logger


# Create default logger
default_logger = setup_logger()


class LoggerMixin:
    """Mixin class to add logging capability to any class"""
    
    @property
    def logger(self):
        return default_logger


def log_execution(func):
    """Decorator to log function execution"""
    def wrapper(*args, **kwargs):
        default_logger.info(f"Executing {func.__name__}...")
        result = func(*args, **kwargs)
        default_logger.info(f"Completed {func.__name__}")
        return result
    return wrapper
