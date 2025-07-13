# Development Guidelines

## Overview

This document outlines the development standards, best practices, and guidelines for contributing to the Uruguay News Analysis System. Following these guidelines ensures code quality, maintainability, and consistency across the project.

## Code Quality Standards

### Python Development Standards

#### Code Style
```python
# Follow PEP 8 with specific project adaptations
# Use type hints for all function signatures
def analyze_sentiment(text: str, context: Optional[dict] = None) -> SentimentResult:
    """
    Analyze sentiment of Uruguayan Spanish text.
    
    Args:
        text: Input text to analyze
        context: Optional context for cultural adjustment
        
    Returns:
        SentimentResult containing score, confidence, and explanation
        
    Raises:
        ValueError: If text is empty or invalid
        APIError: If external API call fails
    """
    if not text.strip():
        raise ValueError("Text cannot be empty")
    
    # Implementation with proper error handling
    try:
        result = self.sentiment_model.predict(text)
        return SentimentResult(
            score=result.score,
            confidence=result.confidence,
            explanation=result.explanation
        )
    except Exception as e:
        logger.error(f"Sentiment analysis failed: {e}")
        raise APIError("Sentiment analysis service unavailable")
```

#### Project Structure
```
backend/
├── src/
│   └── uruguay_news/
│       ├── __init__.py
│       ├── models/              # Pydantic models
│       │   ├── __init__.py
│       │   ├── article.py
│       │   ├── analysis.py
│       │   └── user.py
│       ├── services/            # Business logic
│       │   ├── __init__.py
│       │   ├── sentiment.py
│       │   ├── bias.py
│       │   └── entities.py
│       ├── api/                 # FastAPI endpoints
│       │   ├── __init__.py
│       │   ├── routes/
│       │   └── middleware/
│       ├── utils/               # Utility functions
│       │   ├── __init__.py
│       │   ├── cache.py
│       │   └── validators.py
│       └── config/              # Configuration
│           ├── __init__.py
│           └── settings.py
├── tests/                       # Test files
├── pyproject.toml              # Dependencies and config
└── README.md
```

#### Error Handling
```python
# Custom exception hierarchy
class UruguayNewsError(Exception):
    """Base exception for Uruguay News system"""
    pass

class ValidationError(UruguayNewsError):
    """Raised when data validation fails"""
    pass

class ProcessingError(UruguayNewsError):
    """Raised when processing fails"""
    pass

class ExternalServiceError(UruguayNewsError):
    """Raised when external service calls fail"""
    pass

# Proper error handling in functions
def process_article(article: Article) -> ProcessingResult:
    """Process article with comprehensive error handling"""
    
    try:
        # Validate input
        if not article.content:
            raise ValidationError("Article content is required")
        
        # Process with retries
        for attempt in range(3):
            try:
                result = self.ai_service.analyze(article.content)
                return ProcessingResult(success=True, result=result)
            except ExternalServiceError as e:
                if attempt == 2:  # Last attempt
                    raise
                time.sleep(2 ** attempt)  # Exponential backoff
                
    except Exception as e:
        logger.error(f"Article processing failed: {e}", exc_info=True)
        return ProcessingResult(success=False, error=str(e))
```

#### Testing Standards
```python
# Test structure and naming
import pytest
from unittest.mock import Mock, patch
from uruguay_news.services.sentiment import SentimentAnalyzer
from uruguay_news.models.analysis import SentimentResult

class TestSentimentAnalyzer:
    """Test suite for sentiment analysis"""
    
    @pytest.fixture
    def analyzer(self):
        """Create analyzer instance for testing"""
        return SentimentAnalyzer()
    
    @pytest.fixture
    def sample_text(self):
        """Sample Uruguayan Spanish text for testing"""
        return "El gobierno uruguayo anunció nuevas medidas económicas"
    
    def test_analyze_positive_sentiment(self, analyzer, sample_text):
        """Test positive sentiment analysis"""
        # Arrange
        positive_text = "Excelente noticia para el país"
        
        # Act
        result = analyzer.analyze(positive_text)
        
        # Assert
        assert isinstance(result, SentimentResult)
        assert result.score > 0.5
        assert result.confidence > 0.7
        assert "positive" in result.explanation.lower()
    
    def test_analyze_empty_text_raises_error(self, analyzer):
        """Test that empty text raises ValueError"""
        with pytest.raises(ValueError, match="Text cannot be empty"):
            analyzer.analyze("")
    
    @patch('uruguay_news.services.sentiment.openai_client')
    def test_analyze_with_api_failure(self, mock_client, analyzer):
        """Test graceful handling of API failures"""
        # Arrange
        mock_client.analyze.side_effect = Exception("API Error")
        
        # Act & Assert
        with pytest.raises(ExternalServiceError):
            analyzer.analyze("test text")
```

### TypeScript/JavaScript Standards

#### Code Style
```typescript
// Use strict TypeScript configuration
interface ArticleAnalysis {
  id: string;
  sentiment: {
    score: number;
    confidence: number;
    emotions: string[];
  };
  bias: {
    score: number;
    direction: 'left' | 'right' | 'center';
    confidence: number;
  };
  entities: Entity[];
  createdAt: Date;
}

// Proper error handling
class ArticleService {
  async analyzeArticle(articleId: string): Promise<ArticleAnalysis> {
    try {
      const response = await fetch(`/api/articles/${articleId}/analyze`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error(`Analysis failed: ${response.statusText}`);
      }

      const data = await response.json();
      return this.validateAnalysisResult(data);
    } catch (error) {
      console.error('Article analysis failed:', error);
      throw new AnalysisError('Failed to analyze article');
    }
  }

  private validateAnalysisResult(data: any): ArticleAnalysis {
    // Runtime validation using Zod or similar
    return articleAnalysisSchema.parse(data);
  }
}
```

#### React Component Standards
```typescript
// Proper component structure
interface NewsAnalysisProps {
  articleId: string;
  onAnalysisComplete?: (analysis: ArticleAnalysis) => void;
}

const NewsAnalysis: React.FC<NewsAnalysisProps> = ({
  articleId,
  onAnalysisComplete,
}) => {
  const [analysis, setAnalysis] = useState<ArticleAnalysis | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const analyzeArticle = useCallback(async () => {
    setLoading(true);
    setError(null);
    
    try {
      const result = await articleService.analyzeArticle(articleId);
      setAnalysis(result);
      onAnalysisComplete?.(result);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Analysis failed');
    } finally {
      setLoading(false);
    }
  }, [articleId, onAnalysisComplete]);

  return (
    <div className="news-analysis">
      {loading && <LoadingSpinner />}
      {error && <ErrorMessage message={error} />}
      {analysis && <AnalysisDisplay analysis={analysis} />}
    </div>
  );
};
```

## Performance Standards

### Backend Performance
```python
# Performance monitoring decorator
import time
import functools
from typing import Callable

def monitor_performance(func: Callable) -> Callable:
    """Monitor function performance"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            execution_time = time.time() - start_time
            logger.info(f"{func.__name__} executed in {execution_time:.2f}s")
            
            # Send metrics to monitoring
            metrics_client.record_metric(
                name=f"function.{func.__name__}.duration",
                value=execution_time,
                unit="seconds"
            )
    return wrapper

# Usage
@monitor_performance
def analyze_article_sentiment(article: Article) -> SentimentResult:
    """Analyze sentiment with performance monitoring"""
    return sentiment_analyzer.analyze(article.content)
```

### Caching Strategy
```python
# Multi-level caching implementation
class CacheManager:
    def __init__(self):
        self.memory_cache = {}
        self.redis_cache = redis.Redis.from_url(settings.REDIS_URL)
        self.cache_ttl = {
            'analysis': 3600,    # 1 hour
            'trending': 300,     # 5 minutes
            'user_data': 1800    # 30 minutes
        }
    
    def get(self, key: str, cache_type: str = 'default') -> any:
        """Get from cache with fallback strategy"""
        
        # Level 1: Memory cache
        if key in self.memory_cache:
            return self.memory_cache[key]
        
        # Level 2: Redis cache
        cached_value = self.redis_cache.get(key)
        if cached_value:
            value = json.loads(cached_value)
            self.memory_cache[key] = value  # Promote to memory
            return value
        
        return None
    
    def set(self, key: str, value: any, cache_type: str = 'default'):
        """Set in cache with TTL"""
        
        ttl = self.cache_ttl.get(cache_type, 3600)
        
        # Store in both levels
        self.memory_cache[key] = value
        self.redis_cache.setex(key, ttl, json.dumps(value))
```

### Database Optimization
```python
# Efficient database queries
class ArticleRepository:
    def __init__(self, firestore_client):
        self.db = firestore_client
    
    def get_articles_by_sentiment(
        self, 
        sentiment_range: tuple,
        limit: int = 100,
        offset: int = 0
    ) -> List[Article]:
        """Get articles with optimized query"""
        
        # Use composite index for efficient querying
        query = (
            self.db.collection('articles')
            .where('analysis.sentiment.score', '>=', sentiment_range[0])
            .where('analysis.sentiment.score', '<=', sentiment_range[1])
            .order_by('published_at', direction=firestore.Query.DESCENDING)
            .limit(limit)
            .offset(offset)
        )
        
        # Execute query and convert to models
        docs = query.stream()
        return [Article.from_firestore(doc) for doc in docs]
    
    def get_trending_articles(self, hours: int = 24) -> List[Article]:
        """Get trending articles with efficient aggregation"""
        
        # Use cached aggregation when possible
        cache_key = f"trending:articles:{hours}h"
        cached_result = cache_manager.get(cache_key)
        if cached_result:
            return cached_result
        
        # Calculate trending score
        cutoff_time = datetime.utcnow() - timedelta(hours=hours)
        
        articles = (
            self.db.collection('articles')
            .where('published_at', '>=', cutoff_time)
            .order_by('engagement_score', direction=firestore.Query.DESCENDING)
            .limit(50)
            .stream()
        )
        
        result = [Article.from_firestore(doc) for doc in articles]
        cache_manager.set(cache_key, result, 'trending')
        
        return result
```

## Security Standards

### Authentication & Authorization
```python
# JWT token management
from jose import JWTError, jwt
from datetime import datetime, timedelta

class AuthManager:
    def __init__(self, secret_key: str):
        self.secret_key = secret_key
        self.algorithm = "HS256"
        self.access_token_expire = timedelta(minutes=30)
    
    def create_access_token(self, data: dict) -> str:
        """Create JWT access token"""
        
        to_encode = data.copy()
        expire = datetime.utcnow() + self.access_token_expire
        to_encode.update({"exp": expire})
        
        return jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
    
    def verify_token(self, token: str) -> dict:
        """Verify JWT token"""
        
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except JWTError:
            raise AuthenticationError("Invalid token")

# FastAPI dependency
async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """Get current authenticated user"""
    
    try:
        payload = auth_manager.verify_token(token)
        user_id = payload.get("sub")
        
        if not user_id:
            raise AuthenticationError("Invalid token")
        
        user = await user_service.get_user(user_id)
        if not user:
            raise AuthenticationError("User not found")
        
        return user
    except Exception as e:
        raise HTTPException(status_code=401, detail="Authentication failed")
```

### Input Validation
```python
# Comprehensive input validation
from pydantic import BaseModel, validator, Field
from typing import Optional, List

class ArticleCreateRequest(BaseModel):
    title: str = Field(..., min_length=10, max_length=200)
    content: str = Field(..., min_length=100, max_length=50000)
    source: str = Field(..., min_length=1, max_length=100)
    url: Optional[str] = Field(None, regex=r'^https?://.+')
    tags: Optional[List[str]] = Field(None, max_items=10)
    
    @validator('title')
    def validate_title(cls, v):
        if not v.strip():
            raise ValueError('Title cannot be empty')
        return v.strip()
    
    @validator('content')
    def validate_content(cls, v):
        # Remove potential XSS
        cleaned = html.escape(v)
        
        # Check for spam patterns
        if cls.is_spam(cleaned):
            raise ValueError('Content appears to be spam')
        
        return cleaned
    
    @staticmethod
    def is_spam(content: str) -> bool:
        """Check if content appears to be spam"""
        spam_patterns = [
            r'click here',
            r'free money',
            r'urgent!!!'
        ]
        
        for pattern in spam_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                return True
        
        return False
```

## Testing Standards

### Test Coverage Requirements
- **Unit Tests**: 80% minimum coverage for business logic
- **Integration Tests**: 70% minimum coverage for API endpoints
- **End-to-End Tests**: Critical user flows must be covered
- **Performance Tests**: All AI models must have performance benchmarks

### Test Structure
```python
# Test organization
tests/
├── unit/
│   ├── test_services/
│   │   ├── test_sentiment.py
│   │   ├── test_bias.py
│   │   └── test_entities.py
│   ├── test_models/
│   └── test_utils/
├── integration/
│   ├── test_api/
│   ├── test_database/
│   └── test_external_services/
├── e2e/
│   ├── test_user_flows/
│   └── test_admin_flows/
└── performance/
    ├── test_ai_models/
    └── test_api_performance/
```

### Mocking Strategy
```python
# Proper mocking for external dependencies
import pytest
from unittest.mock import Mock, patch, MagicMock

class TestArticleService:
    @pytest.fixture
    def mock_openai_client(self):
        """Mock OpenAI client"""
        with patch('uruguay_news.services.openai_client') as mock:
            mock.chat.completions.create.return_value = MagicMock(
                choices=[MagicMock(message=MagicMock(content='{"sentiment": 0.8}'))]
            )
            yield mock
    
    @pytest.fixture
    def mock_firestore(self):
        """Mock Firestore client"""
        with patch('uruguay_news.services.firestore.Client') as mock:
            mock_db = MagicMock()
            mock.return_value = mock_db
            yield mock_db
    
    def test_analyze_article_with_mocks(self, mock_openai_client, mock_firestore):
        """Test article analysis with mocked dependencies"""
        # Test implementation with mocked dependencies
        service = ArticleService()
        result = service.analyze_article("test content")
        
        # Verify mocks were called correctly
        mock_openai_client.chat.completions.create.assert_called_once()
        assert result.sentiment > 0.5
```

## Documentation Standards

### Code Documentation
```python
# Comprehensive docstrings
def analyze_uruguayan_sentiment(
    text: str,
    cultural_context: Optional[dict] = None,
    model_version: str = "v1.0"
) -> SentimentResult:
    """
    Analyze sentiment of Uruguayan Spanish text with cultural context.
    
    This function uses a fine-tuned model specifically trained on Uruguayan
    Spanish text to provide culturally-aware sentiment analysis. The model
    accounts for regional expressions, political context, and cultural nuances.
    
    Args:
        text: The input text to analyze. Must be non-empty string.
        cultural_context: Optional dictionary containing:
            - 'source': News source name (e.g., 'El País')
            - 'category': Article category (e.g., 'política')
            - 'region': Geographic region if applicable
        model_version: Model version to use for analysis
    
    Returns:
        SentimentResult containing:
            - score: Sentiment score between -1 (negative) and 1 (positive)
            - confidence: Confidence score between 0 and 1
            - emotions: List of detected emotions
            - cultural_factors: Cultural adjustments made
            - explanation: Human-readable explanation of the result
    
    Raises:
        ValueError: If text is empty or invalid
        ModelError: If the sentiment model fails to load
        APIError: If external API calls fail
    
    Examples:
        >>> analyzer = SentimentAnalyzer()
        >>> result = analyzer.analyze_uruguayan_sentiment(
        ...     "Excelente noticia para el país",
        ...     cultural_context={'source': 'El País', 'category': 'política'}
        ... )
        >>> print(f"Sentiment: {result.score:.2f}")
        Sentiment: 0.85
        
        >>> # Handle negative sentiment
        >>> result = analyzer.analyze_uruguayan_sentiment(
        ...     "Grave crisis económica en Uruguay"
        ... )
        >>> print(f"Sentiment: {result.score:.2f}")
        Sentiment: -0.72
    
    Note:
        The model is specifically trained on Uruguayan Spanish and may not
        perform as well on other Spanish dialects. For best results, provide
        cultural context when available.
    """
```

### API Documentation
```python
# FastAPI endpoint documentation
@app.post("/api/articles/{article_id}/analyze", response_model=AnalysisResponse)
async def analyze_article(
    article_id: str,
    request: AnalysisRequest,
    current_user: User = Depends(get_current_user)
) -> AnalysisResponse:
    """
    Analyze a news article for sentiment, bias, and entities.
    
    This endpoint provides comprehensive analysis of Uruguayan news articles
    including sentiment analysis, political bias detection, and entity recognition.
    The analysis is culturally-aware and specifically tuned for Uruguayan Spanish.
    
    - **article_id**: Unique identifier for the article
    - **request**: Analysis configuration and options
    - **current_user**: Authenticated user making the request
    
    Returns comprehensive analysis results including:
    - Sentiment score and confidence
    - Political bias direction and strength
    - Named entities and their sentiment
    - Topic classification
    - Cultural context analysis
    
    The analysis typically takes 200-500ms to complete.
    """
```

## Deployment Standards

### Environment Configuration
```python
# Environment-specific settings
class Settings:
    # Database
    DATABASE_URL: str = Field(..., env='DATABASE_URL')
    REDIS_URL: str = Field(..., env='REDIS_URL')
    
    # AI Services
    OPENAI_API_KEY: str = Field(..., env='OPENAI_API_KEY')
    GOOGLE_AI_KEY: str = Field(..., env='GOOGLE_AI_KEY')
    
    # Security
    SECRET_KEY: str = Field(..., env='SECRET_KEY')
    JWT_SECRET: str = Field(..., env='JWT_SECRET')
    
    # Performance
    CACHE_TTL: int = Field(3600, env='CACHE_TTL')
    MAX_WORKERS: int = Field(4, env='MAX_WORKERS')
    
    # Monitoring
    SENTRY_DSN: Optional[str] = Field(None, env='SENTRY_DSN')
    LOG_LEVEL: str = Field('INFO', env='LOG_LEVEL')
    
    class Config:
        env_file = '.env'
```

### CI/CD Pipeline
```yaml
# GitHub Actions workflow
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install UV
        run: curl -LsSf https://astral.sh/uv/install.sh | sh
      
      - name: Install dependencies
        run: uv sync
      
      - name: Run linting
        run: |
          uv run ruff check .
          uv run mypy .
      
      - name: Run tests
        run: uv run pytest --cov=src --cov-report=xml
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml
  
  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Deploy to Google Cloud
        run: |
          gcloud functions deploy analyze-news \
            --runtime python311 \
            --trigger http \
            --entry-point main \
            --memory 512MB \
            --timeout 60s
```

## Monitoring Standards

### Logging
```python
# Structured logging
import logging
import json
from datetime import datetime

class StructuredLogger:
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        # Configure handler
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    
    def log_analysis(self, article_id: str, analysis_type: str, 
                    duration: float, success: bool, **kwargs):
        """Log analysis operation"""
        
        log_entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'event': 'analysis_completed',
            'article_id': article_id,
            'analysis_type': analysis_type,
            'duration_ms': duration * 1000,
            'success': success,
            'metadata': kwargs
        }
        
        self.logger.info(json.dumps(log_entry))
```

### Metrics Collection
```python
# Custom metrics
from google.cloud import monitoring_v3
import time

class MetricsCollector:
    def __init__(self):
        self.client = monitoring_v3.MetricServiceClient()
        self.project_name = f"projects/{PROJECT_ID}"
    
    def record_analysis_metrics(self, analysis_type: str, 
                               duration: float, accuracy: float):
        """Record analysis performance metrics"""
        
        # Duration metric
        self.send_metric(
            name="analysis.duration",
            value=duration,
            labels={"type": analysis_type}
        )
        
        # Accuracy metric
        self.send_metric(
            name="analysis.accuracy",
            value=accuracy,
            labels={"type": analysis_type}
        )
    
    def send_metric(self, name: str, value: float, labels: dict):
        """Send custom metric to Google Cloud Monitoring"""
        
        series = monitoring_v3.TimeSeries()
        series.metric.type = f"custom.googleapis.com/uruguay_news/{name}"
        series.resource.type = "global"
        
        # Add labels
        for key, val in labels.items():
            series.metric.labels[key] = val
        
        # Add data point
        point = monitoring_v3.Point()
        point.value.double_value = value
        point.interval.end_time.seconds = int(time.time())
        series.points = [point]
        
        self.client.create_time_series(
            name=self.project_name,
            time_series=[series]
        )
```

## Code Review Standards

### Review Checklist
- [ ] Code follows style guidelines
- [ ] All functions have proper docstrings
- [ ] Error handling is comprehensive
- [ ] Tests are included and passing
- [ ] Performance implications considered
- [ ] Security vulnerabilities addressed
- [ ] Documentation is updated

### Review Process
1. **Self-Review**: Author reviews their own code
2. **Automated Checks**: CI/CD pipeline runs all checks
3. **Peer Review**: At least one team member reviews
4. **AI Review**: CodeRabbit provides automated insights
5. **Final Approval**: Senior developer approves merge

## Next Steps

1. **Adopt** these guidelines in your development workflow
2. **Set up** automated checks and linting
3. **Implement** proper testing strategy
4. **Configure** monitoring and logging
5. **Follow** code review process

For more information, see:
- [Testing Documentation](testing.md)
- [Deployment Guide](deployment.md)
- [Setup Instructions](setup.md)
- [Architecture Overview](../architecture/overview.md) 