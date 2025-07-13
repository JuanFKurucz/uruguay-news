# Uruguay News Backend

Backend API for Uruguay News platform - Google Cloud Functions with AI-powered sentiment analysis and bias detection.

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- [UV package manager](https://docs.astral.sh/uv/) (10-100x faster than pip)
- Google Cloud SDK (for deployment)

### Installation

```bash
# Navigate to backend directory
cd backend

# Install dependencies with UV
uv sync

# Activate virtual environment
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows
```

### Development

```bash
# Run local development server
uv run functions-framework --target=main --debug

# Run tests
uv run pytest

# Code formatting
uv run black .
uv run ruff check .

# Type checking
uv run mypy .
```

## 🏗️ Architecture

### Google Cloud Functions
- **Serverless**: Auto-scaling, pay-per-use
- **FastAPI**: High-performance async API framework
- **Firestore**: NoSQL document database
- **Redis**: Caching layer for AI results

### AI/ML Pipeline
- **Sentiment Analysis**: 84%+ accuracy for Spanish content
- **Bias Detection**: LangBiTe integration for political bias
- **Content Processing**: Web scraping and NLP analysis

## 📁 Project Structure

```
backend/
├── src/uruguay_news/          # Main package
│   ├── models.py             # Data models
│   └── __init__.py
├── config/                   # Configuration files
├── tests/                    # Test suite
├── main.py                   # Cloud Functions entry point
├── pyproject.toml           # Dependencies and tools
└── README.md                # This file
```

## 🔧 Configuration

### Environment Variables
```bash
# Google Cloud
GOOGLE_CLOUD_PROJECT=your-project-id
FIRESTORE_EMULATOR_HOST=localhost:8080  # For local dev

# AI Services
OPENAI_API_KEY=your-openai-key

# Redis
REDIS_URL=redis://localhost:6379
```

### Local Development with Emulators
```bash
# Start Firestore emulator
gcloud emulators firestore start --host-port=localhost:8080

# Start local Redis (Docker)
docker run -d -p 6379:6379 redis:alpine

# Run Functions Framework
uv run functions-framework --target=main --debug
```

## 🚀 Deployment

### Google Cloud Functions
```bash
# Deploy function
gcloud functions deploy uruguay-news-api \
  --runtime python311 \
  --trigger-http \
  --allow-unauthenticated \
  --source .

# Deploy with environment variables
gcloud functions deploy uruguay-news-api \
  --runtime python311 \
  --trigger-http \
  --set-env-vars GOOGLE_CLOUD_PROJECT=your-project-id
```

## 🧪 Testing

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src

# Run specific test types
uv run pytest -m unit        # Unit tests only
uv run pytest -m integration # Integration tests only
uv run pytest -m ai          # AI/ML model tests only
```

## 📊 Dependencies

### Core Dependencies
- **functions-framework**: Google Cloud Functions runtime
- **fastapi**: Web framework
- **google-cloud-firestore**: Database client
- **openai**: AI/ML models
- **langchain**: AI workflow orchestration

### Development Dependencies
- **pytest**: Testing framework
- **black**: Code formatting
- **ruff**: Fast Python linter
- **mypy**: Type checking

## 🔗 Related

- [Frontend](../frontend/web/README.md) - React web application
- [Documentation](../docs/README.md) - Project documentation
- [Main Project](../README.md) - Overall project information 