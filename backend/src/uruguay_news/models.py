"""
Pydantic models for Uruguay News data structures.
These models define the schema for Firestore documents and API responses.
"""

from datetime import datetime
from typing import Dict, List, Optional, Union
from enum import Enum

from pydantic import BaseModel, Field, HttpUrl, validator


class BiasType(str, Enum):
    """Types of bias that can be detected in news content."""

    POLITICAL_LEFT = "political_left"
    POLITICAL_RIGHT = "political_right"
    SENSATIONALISM = "sensationalism"
    CONFIRMATION_BIAS = "confirmation_bias"
    SELECTION_BIAS = "selection_bias"
    FRAMING_BIAS = "framing_bias"
    NONE = "none"


class SentimentType(str, Enum):
    """Sentiment classification types."""

    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"
    MIXED = "mixed"


class NewsSource(BaseModel):
    """News source information."""

    name: str = Field(..., description="Name of the news source")
    url: HttpUrl = Field(..., description="Base URL of the news source")
    country: str = Field(default="Uruguay", description="Country of origin")
    language: str = Field(default="es", description="Primary language")
    credibility_score: float = Field(
        default=0.0, ge=0.0, le=1.0, description="Credibility score (0-1)"
    )


class NewsArticle(BaseModel):
    """News article document model for Firestore."""

    # Basic article information
    title: str = Field(..., description="Article title")
    content: str = Field(..., description="Full article content")
    summary: Optional[str] = Field(None, description="Article summary")
    url: HttpUrl = Field(..., description="Article URL")

    # Source information
    source: NewsSource = Field(..., description="News source details")

    # Metadata
    published_at: datetime = Field(..., description="Publication timestamp")
    scraped_at: datetime = Field(
        default_factory=datetime.utcnow, description="Scraping timestamp"
    )

    # Content classification
    category: Optional[str] = Field(None, description="Article category")
    tags: List[str] = Field(default_factory=list, description="Article tags")

    # Processing status
    processed: bool = Field(default=False, description="AI processing status")

    # Firestore document ID
    document_id: Optional[str] = Field(None, description="Firestore document ID")

    @validator("content")
    def content_must_not_be_empty(cls, v):
        """Validate that content is not empty."""
        if not v or not v.strip():
            raise ValueError("Content cannot be empty")
        return v.strip()


class SentimentResult(BaseModel):
    """Sentiment analysis result."""

    # Primary sentiment
    sentiment: SentimentType = Field(..., description="Primary sentiment")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score")

    # Detailed scores
    scores: Dict[str, float] = Field(..., description="Detailed sentiment scores")

    # Emotional analysis
    emotions: Dict[str, float] = Field(
        default_factory=dict, description="Emotional analysis scores"
    )

    # Context information
    model_version: str = Field(..., description="AI model version used")
    processed_at: datetime = Field(
        default_factory=datetime.utcnow, description="Processing timestamp"
    )

    # Performance metrics
    processing_time_ms: float = Field(
        ..., description="Processing time in milliseconds"
    )


class BiasAnalysis(BaseModel):
    """Bias detection analysis result."""

    # Primary bias detection
    bias_type: BiasType = Field(..., description="Detected bias type")
    bias_score: float = Field(..., ge=0.0, le=1.0, description="Bias intensity score")

    # Detailed analysis
    political_leaning: Optional[str] = Field(None, description="Political leaning")
    bias_indicators: List[str] = Field(
        default_factory=list, description="Specific bias indicators found"
    )

    # LangBiTe integration
    langbite_prompts_used: List[str] = Field(
        default_factory=list, description="LangBiTe prompts used in analysis"
    )

    # Confidence metrics
    confidence: float = Field(..., ge=0.0, le=1.0, description="Analysis confidence")

    # Processing information
    model_version: str = Field(..., description="Bias detection model version")
    processed_at: datetime = Field(
        default_factory=datetime.utcnow, description="Processing timestamp"
    )

    # Performance metrics
    processing_time_ms: float = Field(
        ..., description="Processing time in milliseconds"
    )


class EntityExtraction(BaseModel):
    """Named entity extraction result."""

    # Extracted entities
    people: List[str] = Field(default_factory=list, description="People mentioned")
    organizations: List[str] = Field(
        default_factory=list, description="Organizations mentioned"
    )
    locations: List[str] = Field(
        default_factory=list, description="Locations mentioned"
    )
    dates: List[str] = Field(default_factory=list, description="Dates mentioned")

    # Processing information
    model_version: str = Field(..., description="Entity extraction model version")
    processed_at: datetime = Field(
        default_factory=datetime.utcnow, description="Processing timestamp"
    )


class AnalysisResult(BaseModel):
    """Complete analysis result for a news article."""

    # Article reference
    article_id: str = Field(..., description="Reference to NewsArticle document")

    # Analysis results
    sentiment: SentimentResult = Field(..., description="Sentiment analysis")
    bias: BiasAnalysis = Field(..., description="Bias detection")
    entities: EntityExtraction = Field(..., description="Entity extraction")

    # Overall metrics
    overall_score: float = Field(
        ..., ge=0.0, le=1.0, description="Overall content quality score"
    )

    # Processing metadata
    total_processing_time_ms: float = Field(
        ..., description="Total processing time in milliseconds"
    )
    processed_at: datetime = Field(
        default_factory=datetime.utcnow, description="Analysis timestamp"
    )

    # Firestore document ID
    document_id: Optional[str] = Field(None, description="Firestore document ID")


class APIResponse(BaseModel):
    """Standard API response wrapper."""

    success: bool = Field(..., description="Request success status")
    message: str = Field(..., description="Response message")
    data: Optional[Union[Dict, List, str, int, float]] = Field(
        None, description="Response data"
    )
    error: Optional[str] = Field(None, description="Error message if failed")
    timestamp: datetime = Field(
        default_factory=datetime.utcnow, description="Response timestamp"
    )


class HealthCheck(BaseModel):
    """Health check response model."""

    status: str = Field(..., description="Service status")
    service: str = Field(..., description="Service name")
    version: str = Field(..., description="Service version")
    timestamp: datetime = Field(
        default_factory=datetime.utcnow, description="Health check timestamp"
    )

    # Service-specific health metrics
    firestore_connected: bool = Field(..., description="Firestore connection status")
    redis_connected: bool = Field(..., description="Redis connection status")
    ai_models_loaded: bool = Field(..., description="AI models loading status")
