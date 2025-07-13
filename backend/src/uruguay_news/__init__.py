"""
Uruguay News - AI-powered news analysis platform for Uruguay.

This package provides sentiment analysis, bias detection, and content
processing for Uruguayan news sources using Google Cloud serverless
architecture.
"""

__version__: str = "0.1.0"
__author__: str = "Uruguay News Team"
__email__: str = "contact@uruguay-news.org"

# Public API exports
from .models import NewsArticle, BiasAnalysis, SentimentResult
from .services import ContentExtractor, SentimentAnalyzer, BiasDetector

__all__ = [
    # Models
    "NewsArticle",
    "BiasAnalysis",
    "SentimentResult",
    # Services
    "ContentExtractor",
    "SentimentAnalyzer",
    "BiasDetector",
]
