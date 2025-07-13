"""
Main entry point for Google Cloud Functions with FastAPI integration.
This file serves as the deployment entry point for all Cloud Functions.
"""

import os
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from functions_framework import create_app
from google.cloud import firestore
from google.cloud import logging as cloud_logging

# Initialize Google Cloud Logging
cloud_logging.Client().setup_logging()

# Initialize Firestore client
db = firestore.Client()

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
    allow_origins=["*"],  # Configure for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring."""
    return {"status": "healthy", "service": "uruguay-news-api"}


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


# Cloud Functions entry point
def main(request: Any) -> Any:
    """
    Cloud Functions entry point using Functions Framework.

    Args:
        request: The HTTP request object

    Returns:
        The HTTP response
    """
    # Create ASGI app for Cloud Functions
    asgi_app = create_app(app)
    return asgi_app(request)


# For local development with uvicorn
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8080)),
        reload=True,
        log_level="info",
    )
