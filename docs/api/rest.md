# REST API Documentation

## Overview

The Uruguay News Analysis System provides a comprehensive REST API for analyzing news articles with AI-powered sentiment analysis, bias detection, and entity recognition. The API is designed for high performance, cultural accuracy, and ease of integration.

## Base URL

```
Production: https://api.uruguaynews.com
Staging: https://api-staging.uruguaynews.com
```

## Authentication

### Bearer Token Authentication
```http
Authorization: Bearer <your-access-token>
```

### Getting an Access Token
```http
POST /api/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "your-password"
}
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "expires_in": 3600,
  "user": {
    "id": "user-123",
    "email": "user@example.com",
    "role": "user"
  }
}
```

## API Endpoints

### Health Check

#### Check API Health
```http
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00Z",
  "version": "1.0.0",
  "services": {
    "database": "healthy",
    "cache": "healthy",
    "ai_services": "healthy"
  }
}
```

### Article Analysis

#### Analyze Article
Analyze a news article for sentiment, bias, and entities.

```http
POST /api/articles/analyze
Content-Type: application/json
Authorization: Bearer <token>

{
  "title": "Nuevas medidas económicas en Uruguay",
  "content": "El gobierno uruguayo anunció nuevas medidas para estimular la economía local...",
  "source": "El País",
  "url": "https://elpais.com.uy/news/article-123",
  "author": "Juan Pérez",
  "published_at": "2024-01-15T08:00:00Z",
  "tags": ["economía", "gobierno", "política"]
}
```

**Response:**
```json
{
  "id": "analysis-456",
  "article": {
    "id": "article-123",
    "title": "Nuevas medidas económicas en Uruguay",
    "content": "El gobierno uruguayo anunció...",
    "source": "El País",
    "url": "https://elpais.com.uy/news/article-123",
    "author": "Juan Pérez",
    "published_at": "2024-01-15T08:00:00Z",
    "word_count": 245,
    "language": "es"
  },
  "analysis": {
    "sentiment": {
      "score": 0.65,
      "confidence": 0.87,
      "emotions": ["positive", "hopeful"],
      "explanation": "El artículo presenta un tono optimista sobre las medidas económicas",
      "cultural_factors": {
        "source_adjustment": 0.95,
        "political_context": "neutral"
      }
    },
    "bias": {
      "score": 0.15,
      "direction": "center",
      "confidence": 0.73,
      "evidence": [
        "Uso de lenguaje neutral",
        "Presentación equilibrada de hechos"
      ],
      "political_spectrum": "center-right",
      "explanation": "El artículo muestra una ligera tendencia hacia el centro-derecha"
    },
    "entities": [
      {
        "name": "Uruguay",
        "type": "LOCATION",
        "confidence": 0.98,
        "sentiment": 0.7,
        "mentions": 3,
        "context": "país beneficiario de las medidas"
      },
      {
        "name": "gobierno uruguayo",
        "type": "ORGANIZATION",
        "confidence": 0.95,
        "sentiment": 0.6,
        "mentions": 2,
        "context": "entidad que implementa las medidas"
      }
    ],
    "topics": {
      "primary": "economía",
      "secondary": ["política", "medidas gubernamentales"],
      "confidence": 0.91
    },
    "summary": "El gobierno uruguayo implementa nuevas medidas económicas con recepción positiva"
  },
  "metadata": {
    "processed_at": "2024-01-15T10:05:00Z",
    "processing_time_ms": 187,
    "model_version": "1.2.0",
    "confidence_score": 0.84
  }
}
```

#### Batch Analyze Articles
Analyze multiple articles in a single request.

```http
POST /api/articles/analyze/batch
Content-Type: application/json
Authorization: Bearer <token>

{
  "articles": [
    {
      "title": "Artículo 1",
      "content": "Contenido del artículo 1...",
      "source": "El País"
    },
    {
      "title": "Artículo 2",
      "content": "Contenido del artículo 2...",
      "source": "El Observador"
    }
  ]
}
```

**Response:**
```json
{
  "batch_id": "batch-789",
  "results": [
    {
      "article_index": 0,
      "status": "success",
      "analysis": { /* analysis result */ }
    },
    {
      "article_index": 1,
      "status": "success", 
      "analysis": { /* analysis result */ }
    }
  ],
  "summary": {
    "total_articles": 2,
    "successful": 2,
    "failed": 0,
    "processing_time_ms": 341
  }
}
```

### Article Management

#### Get Articles
Retrieve articles with optional filtering.

```http
GET /api/articles?source=El+País&limit=20&offset=0&from_date=2024-01-01&to_date=2024-01-15
Authorization: Bearer <token>
```

**Query Parameters:**
- `source`: Filter by news source
- `category`: Filter by category
- `sentiment_min`: Minimum sentiment score (-1 to 1)
- `sentiment_max`: Maximum sentiment score (-1 to 1)
- `bias_direction`: Filter by bias direction (left, center, right)
- `from_date`: Start date (ISO 8601)
- `to_date`: End date (ISO 8601)
- `limit`: Number of results (default: 20, max: 100)
- `offset`: Pagination offset

**Response:**
```json
{
  "articles": [
    {
      "id": "article-123",
      "title": "Nuevas medidas económicas",
      "source": "El País",
      "published_at": "2024-01-15T08:00:00Z",
      "analysis": {
        "sentiment": { "score": 0.65, "confidence": 0.87 },
        "bias": { "score": 0.15, "direction": "center" }
      }
    }
  ],
  "pagination": {
    "total": 1500,
    "limit": 20,
    "offset": 0,
    "has_next": true,
    "has_previous": false
  }
}
```

#### Get Article by ID
```http
GET /api/articles/{article_id}
Authorization: Bearer <token>
```

**Response:**
```json
{
  "id": "article-123",
  "title": "Nuevas medidas económicas en Uruguay",
  "content": "El gobierno uruguayo anunció...",
  "source": "El País",
  "author": "Juan Pérez",
  "published_at": "2024-01-15T08:00:00Z",
  "analysis": {
    "sentiment": { /* sentiment analysis */ },
    "bias": { /* bias analysis */ },
    "entities": [ /* entity list */ ],
    "topics": { /* topic classification */ }
  },
  "metadata": {
    "analyzed_at": "2024-01-15T10:05:00Z",
    "model_version": "1.2.0"
  }
}
```

### Analytics

#### Get Sentiment Trends
```http
GET /api/analytics/sentiment/trends?period=7d&source=El+País
Authorization: Bearer <token>
```

**Query Parameters:**
- `period`: Time period (1d, 7d, 30d, 90d)
- `source`: Filter by news source
- `category`: Filter by category

**Response:**
```json
{
  "period": "7d",
  "data": [
    {
      "date": "2024-01-15",
      "sentiment_avg": 0.32,
      "sentiment_std": 0.21,
      "article_count": 45,
      "sources": {
        "El País": 0.35,
        "El Observador": 0.28,
        "La Diaria": 0.33
      }
    }
  ],
  "summary": {
    "overall_sentiment": 0.31,
    "trend_direction": "positive",
    "confidence": 0.78
  }
}
```

#### Get Bias Distribution
```http
GET /api/analytics/bias/distribution?period=30d
Authorization: Bearer <token>
```

**Response:**
```json
{
  "period": "30d",
  "distribution": {
    "left": {
      "count": 234,
      "percentage": 23.4,
      "avg_score": -0.45
    },
    "center": {
      "count": 567,
      "percentage": 56.7,
      "avg_score": 0.05
    },
    "right": {
      "count": 199,
      "percentage": 19.9,
      "avg_score": 0.38
    }
  },
  "by_source": {
    "El País": {
      "left": 15, "center": 65, "right": 20
    },
    "El Observador": {
      "left": 20, "center": 60, "right": 20
    },
    "La Diaria": {
      "left": 40, "center": 45, "right": 15
    }
  }
}
```

#### Get Top Entities
```http
GET /api/analytics/entities/top?period=7d&limit=10
Authorization: Bearer <token>
```

**Response:**
```json
{
  "period": "7d",
  "entities": [
    {
      "name": "Luis Lacalle Pou",
      "type": "PERSON",
      "mentions": 156,
      "avg_sentiment": 0.23,
      "sources": ["El País", "El Observador", "La Diaria"],
      "trend": "increasing"
    },
    {
      "name": "Uruguay",
      "type": "LOCATION", 
      "mentions": 234,
      "avg_sentiment": 0.45,
      "sources": ["El País", "El Observador"],
      "trend": "stable"
    }
  ]
}
```

### Trending Topics

#### Get Trending Topics
```http
GET /api/trending/topics?period=24h&limit=10
Authorization: Bearer <token>
```

**Response:**
```json
{
  "period": "24h",
  "topics": [
    {
      "topic": "economía",
      "score": 0.89,
      "article_count": 34,
      "growth_rate": 0.23,
      "sentiment": {
        "avg": 0.45,
        "distribution": {
          "positive": 0.65,
          "neutral": 0.25,
          "negative": 0.10
        }
      },
      "key_entities": ["gobierno", "medidas económicas", "Uruguay"]
    }
  ]
}
```

#### Get Breaking News
```http
GET /api/trending/breaking
Authorization: Bearer <token>
```

**Response:**
```json
{
  "breaking_news": [
    {
      "id": "breaking-123",
      "title": "Importante anuncio gubernamental",
      "source": "El País",
      "published_at": "2024-01-15T14:30:00Z",
      "urgency_score": 0.94,
      "sentiment": {
        "score": -0.23,
        "confidence": 0.87
      },
      "engagement": {
        "views": 1500,
        "shares": 89,
        "comments": 23
      }
    }
  ]
}
```

### User Management

#### Get User Profile
```http
GET /api/users/profile
Authorization: Bearer <token>
```

**Response:**
```json
{
  "id": "user-123",
  "email": "user@example.com",
  "role": "user",
  "created_at": "2024-01-01T00:00:00Z",
  "preferences": {
    "sources": ["El País", "El Observador"],
    "categories": ["política", "economía"],
    "notifications": true
  },
  "usage": {
    "analyses_this_month": 45,
    "quota_limit": 1000,
    "quota_remaining": 955
  }
}
```

#### Update User Preferences
```http
PUT /api/users/preferences
Content-Type: application/json
Authorization: Bearer <token>

{
  "sources": ["El País", "La Diaria"],
  "categories": ["política", "economía", "sociedad"],
  "notifications": true,
  "language": "es"
}
```

### Error Handling

#### Error Response Format
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid article content",
    "details": {
      "field": "content",
      "reason": "Content must be at least 100 characters"
    }
  },
  "timestamp": "2024-01-15T10:30:00Z",
  "request_id": "req-789"
}
```

#### Common Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `VALIDATION_ERROR` | 400 | Invalid request data |
| `UNAUTHORIZED` | 401 | Authentication required |
| `FORBIDDEN` | 403 | Insufficient permissions |
| `NOT_FOUND` | 404 | Resource not found |
| `RATE_LIMIT_EXCEEDED` | 429 | Too many requests |
| `ANALYSIS_FAILED` | 422 | AI analysis failed |
| `INTERNAL_ERROR` | 500 | Internal server error |
| `SERVICE_UNAVAILABLE` | 503 | Service temporarily unavailable |

### Rate Limiting

The API implements rate limiting to ensure fair usage:

- **Free tier**: 100 requests per hour
- **Pro tier**: 1,000 requests per hour
- **Enterprise tier**: 10,000 requests per hour

Rate limit headers are included in responses:
```http
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1642262400
```

### Webhooks

#### Configure Webhooks
```http
POST /api/webhooks
Content-Type: application/json
Authorization: Bearer <token>

{
  "url": "https://your-app.com/webhook",
  "events": ["analysis_completed", "breaking_news"],
  "secret": "your-webhook-secret"
}
```

#### Webhook Events

##### Analysis Completed
```json
{
  "event": "analysis_completed",
  "timestamp": "2024-01-15T10:05:00Z",
  "data": {
    "analysis_id": "analysis-456",
    "article_id": "article-123",
    "sentiment_score": 0.65,
    "bias_direction": "center",
    "confidence": 0.84
  }
}
```

##### Breaking News
```json
{
  "event": "breaking_news",
  "timestamp": "2024-01-15T14:30:00Z",
  "data": {
    "article_id": "breaking-123",
    "title": "Importante anuncio gubernamental",
    "urgency_score": 0.94,
    "source": "El País"
  }
}
```

### SDKs and Examples

#### Python SDK
```python
from uruguay_news import UruguayNewsClient

# Initialize client
client = UruguayNewsClient(
    api_key="your-api-key",
    base_url="https://api.uruguaynews.com"
)

# Analyze article
result = client.analyze_article(
    title="Nuevas medidas económicas",
    content="El gobierno uruguayo anunció...",
    source="El País"
)

print(f"Sentiment: {result.sentiment.score}")
print(f"Bias: {result.bias.direction}")
```

#### JavaScript SDK
```javascript
import { UruguayNewsClient } from '@uruguay-news/sdk';

const client = new UruguayNewsClient({
  apiKey: 'your-api-key',
  baseUrl: 'https://api.uruguaynews.com'
});

// Analyze article
const result = await client.analyzeArticle({
  title: 'Nuevas medidas económicas',
  content: 'El gobierno uruguayo anunció...',
  source: 'El País'
});

console.log(`Sentiment: ${result.sentiment.score}`);
console.log(`Bias: ${result.bias.direction}`);
```

#### cURL Examples
```bash
# Analyze article
curl -X POST https://api.uruguaynews.com/api/articles/analyze \
  -H "Authorization: Bearer your-token" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Nuevas medidas económicas",
    "content": "El gobierno uruguayo anunció...",
    "source": "El País"
  }'

# Get sentiment trends
curl -X GET "https://api.uruguaynews.com/api/analytics/sentiment/trends?period=7d" \
  -H "Authorization: Bearer your-token"
```

### OpenAPI Specification

The complete OpenAPI 3.0 specification is available at:
- Production: https://api.uruguaynews.com/docs
- Staging: https://api-staging.uruguaynews.com/docs

### Testing

#### Postman Collection
Download our Postman collection for easy API testing:
```
https://api.uruguaynews.com/postman/collection.json
```

#### Test Environment
Use our test environment for development:
```
Base URL: https://api-test.uruguaynews.com
Test API Key: test_key_123456789
```

### Support

For API support and questions:
- Email: api-support@uruguaynews.com
- Documentation: https://docs.uruguaynews.com/api
- GitHub Issues: https://github.com/JuanFKurucz/uruguay-news/issues

### Changelog

#### v1.2.0 (2024-01-15)
- Added batch analysis endpoint
- Improved cultural context analysis
- Enhanced entity recognition for Uruguayan entities
- Added trending topics endpoint

#### v1.1.0 (2024-01-01)
- Added webhook support
- Improved bias detection accuracy
- Added analytics endpoints
- Enhanced error handling

#### v1.0.0 (2023-12-01)
- Initial API release
- Basic sentiment analysis
- Article management endpoints
- User authentication

For more information, see:
- [GraphQL API](graphql.md)
- [WebSocket API](websocket.md)
- [Architecture Overview](../architecture/overview.md)
- [Development Guidelines](../development/guidelines.md) 