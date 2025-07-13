"""
Main entry point for Google Cloud Functions with FastAPI integration.
This file serves as the deployment entry point for all Cloud Functions.
"""

import os
from typing import Any, Optional
import logging
from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from functions_framework import create_app
from google.cloud import firestore
from google.cloud import logging as cloud_logging

# Redis import with optional fallback
try:
    import redis

    REDIS_AVAILABLE = True
except ImportError:
    REDIS_AVAILABLE = False
    redis = None

# Import our models and services
from src.uruguay_news.models import HealthCheck
from src.uruguay_news.services import (
    create_sentiment_analyzer,
    create_bias_detector,
    create_content_extractor,
)

# Initialize Google Cloud Logging
cloud_logging.Client().setup_logging()

# Initialize logger
logger = logging.getLogger(__name__)

# Initialize Firestore client
db = firestore.Client()

# Initialize Redis client (optional)
redis_client: Optional[redis.Redis] = None
if REDIS_AVAILABLE:
    try:
        redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
        redis_client = redis.from_url(redis_url, decode_responses=True)
        logger.info(f"Redis client initialized with URL: {redis_url}")
    except Exception as e:
        logger.warning(f"Failed to initialize Redis client: {e}")
        redis_client = None

# Create FastAPI app
app = FastAPI(
    title="Uruguay News API",
    description="AI-powered news analysis platform for Uruguay",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://juanfkurucz.github.io",  # GitHub Pages
        "http://localhost:3000",  # Local development
    ]
    if os.getenv("ENVIRONMENT") == "production"
    else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health check endpoint
@app.get("/health", response_model=HealthCheck)
async def health_check() -> HealthCheck:
    """
    Health check endpoint for monitoring service connectivity.

    Verifies:
    - Firestore database connectivity
    - Redis cache connectivity
    - AI model loading status (sentiment analyzer and bias detector)

    Returns:
        HealthCheck: Comprehensive health status of all services
    """
    # Initialize status tracking
    firestore_connected = True
    redis_connected = True  # Will be set to False when Redis is configured
    ai_models_loaded = True
    overall_status = "healthy"

    # Test Firestore connectivity
    try:
        # Perform a simple query to verify Firestore is accessible
        db.collection("health").limit(1).get()
        logger.info("Firestore health check passed")
    except Exception as e:
        logger.error(f"Firestore health check failed: {e}")
        firestore_connected = False
        overall_status = "degraded"

    # Test Redis connectivity
    try:
        if redis_client is not None:
            # Test Redis connection with ping
            redis_client.ping()
            redis_connected = True
            logger.info("Redis health check passed")
        else:
            # Redis client not available or not configured
            redis_connected = False
            logger.info("Redis health check: not configured")
    except Exception as e:
        logger.error(f"Redis health check failed: {e}")
        redis_connected = False
        overall_status = "degraded"

    # Test AI models loading status
    try:
        # Test sentiment analyzer
        sentiment_analyzer = create_sentiment_analyzer()
        sentiment_loaded = sentiment_analyzer.model_loaded

        # Test bias detector
        bias_detector = create_bias_detector()
        bias_loaded = bias_detector.prompts_loaded

        # Test content extractor (always available)
        content_extractor = create_content_extractor()
        extractor_available = content_extractor is not None

        ai_models_loaded = sentiment_loaded and bias_loaded and extractor_available

        if not ai_models_loaded:
            overall_status = "degraded"
            logger.warning("AI models not fully loaded")
        else:
            logger.info("AI models health check passed")

    except Exception as e:
        logger.error(f"AI models health check failed: {e}")
        ai_models_loaded = False
        overall_status = "degraded"

    # Create and return structured health check response
    return HealthCheck(
        status=overall_status,
        service="uruguay-news-api",
        version="0.1.0",
        timestamp=datetime.now(timezone.utc),
        firestore_connected=firestore_connected,
        redis_connected=redis_connected,
        ai_models_loaded=ai_models_loaded,
    )


# Root endpoint
@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Uruguay News API",
        "version": "0.1.0",
        "docs": "/docs",
        "health": "/health",
    }


# Analysis endpoints (placeholders)
@app.post("/analyze")
async def analyze_article():
    """Analyze a single article for sentiment and bias."""
    return {"message": "Analysis endpoint - coming soon"}


@app.post("/batch-analyze")
async def batch_analyze():
    """Analyze multiple articles in batch."""
    return {"message": "Batch analysis endpoint - coming soon"}


# Cloud Functions entry point
def main(request: Any) -> Any:
    """
    Cloud Functions entry point using Functions Framework.

    Args:
        request: The HTTP request object

    Returns:
        The HTTP response

    Raises:
        Exception: If ASGI app creation fails
    """
    try:
        # Create ASGI app for Cloud Functions
        asgi_app = create_app(app)
        return asgi_app(request)
    except Exception as e:
        logger.error(f"Failed to create ASGI app: {e}")
        raise


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8081)
