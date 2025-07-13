# Quick Start Guide

Get the Uruguay News Analysis System running in 5 minutes.

## Prerequisites

- **Python 3.11+** with UV package manager
- **Node.js 18+** with npm
- **Google Cloud SDK** (optional, for deployment)

## 1. Clone and Setup

```bash
git clone https://github.com/JuanFKurucz/uruguay-news.git
cd uruguay-news
```

!!! info "Google Cloud Credentials"
    The project requires Google Cloud credentials for Firestore and other services. Place your service account key file in the `credentials/` directory and set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to it (see [Configuration Guide](configuration.md) for details).

## 2. Start Services

### Firestore Emulator (Terminal 1)

```bash
gcloud emulators firestore start --host-port=localhost:8080
export FIRESTORE_EMULATOR_HOST=localhost:8080
```

### Backend (Terminal 2)

```bash
cd backend
uv sync --extra dev
uv run python -m functions_framework --target=main --port=8081
```

### Frontend (Terminal 3)

```bash
cd frontend/web
npm install
npm start
```

The application will be available at:
- **Frontend**: <http://localhost:3000>
- **Backend API**: <http://localhost:8081>
- **Firestore Emulator**: <http://localhost:8080>

## 3. Test the System

### Analyze a News Article

```bash
curl -X POST http://localhost:8081/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://www.elpais.com.uy/informacion/politica/elecciones-2024",
    "content": "El gobierno anunció nuevas medidas económicas para impulsar el crecimiento.",
    "source": "El País"
  }'
```

### Expected Response

```json
{
  "status": "success",
  "analysis": {
    "sentiment": {
      "overall": "positive",
      "confidence": 0.85,
      "scores": {
        "positive": 0.7,
        "neutral": 0.2,
        "negative": 0.1
      }
    },
    "bias": {
      "score": 0.2,
      "type": "slight_positive",
      "confidence": 0.75
    },
    "entities": [
      {"text": "gobierno", "type": "ORG", "confidence": 0.9}
    ]
  }
}
```

### Batch Analysis

```bash
curl -X POST http://localhost:8081/batch-analyze \
  -H "Content-Type: application/json" \
  -d '{
    "articles": [
      {
        "url": "https://www.montevideo.com.uy/contenido/Politica",
        "content": "La oposición critica las nuevas políticas económicas.",
        "source": "Montevideo Portal"
      }
    ]
  }'
```

## 4. Access the Dashboard

1. Open <http://localhost:3000>
2. Navigate to the **Dashboard** tab
3. View real-time analytics:
   - Sentiment trends
   - Bias detection results
   - News source analysis
   - Entity recognition

## 5. Monitor System Health

### Health Check

```bash
curl http://localhost:8081/health
```

### System Metrics

```bash
curl http://localhost:8081/metrics
```

## Development Workflow

### Add New News Sources

1. **Configure scraper** in `backend/src/scrapers/`
2. **Add source metadata** to configuration
3. **Test extraction** with sample URLs
4. **Deploy** to staging environment

### Scrape News Content

```bash
curl -X POST http://localhost:8081/scrape \
  -H "Content-Type: application/json" \
  -d '{
    "source": "elpais",
    "category": "politica",
    "limit": 10
  }'
```

### Monitor Real-time Analysis

```bash
curl -X POST http://localhost:8081/monitor \
  -H "Content-Type: application/json" \
  -d '{
    "sources": ["elpais", "montevideo", "ladiaria"],
    "keywords": ["elecciones", "política", "economía"]
  }'
```

## API Endpoints

### Core Analysis

- `GET /health` - System health check
- `GET /metrics` - Performance metrics
- `POST /analyze` - Single article analysis
- `POST /batch-analyze` - Multiple articles

### Metrics Endpoints

- `GET /metrics/sentiment` - Sentiment analysis metrics
- `GET /metrics/bias` - Bias detection metrics
- `GET /metrics/sources` - News source statistics

### Data Collection

- `POST /scrape` - Manual content scraping
- `GET /sources` - Available news sources
- `POST /monitor` - Start real-time monitoring

## Troubleshooting

### Port Conflicts

If you encounter port conflicts:

```bash
# Check what's using the ports
netstat -tulpn | grep :3000
netstat -tulpn | grep :8080
netstat -tulpn | grep :8081

# Kill processes if needed
lsof -ti:3000 | xargs kill -9
lsof -ti:8080 | xargs kill -9
lsof -ti:8081 | xargs kill -9
```

### Firestore Connection Issues

1. **Start Firestore emulator**:
   ```bash
   gcloud emulators firestore start --host-port=localhost:8080
   ```

2. **Set environment variable**:
   ```bash
   export FIRESTORE_EMULATOR_HOST=localhost:8080
   ```

### Common Errors

- **Port 8081 in use**: Stop other processes or change port
- **Missing dependencies**: Run `uv sync --extra dev` in backend
- **Node modules**: Delete `node_modules` and run `npm install`
- **Firestore timeout**: Ensure emulator is running

## Next Steps

1. **[Configuration Guide](configuration.md)** - Set up Google Cloud services
2. **[Development Setup](../development/setup.md)** - Full development environment
3. **[API Documentation](../api/rest.md)** - Complete API reference
4. **[Contributing](../community/contributing.md)** - Join the community

## Production Deployment

### Quick Deploy

```bash
# Deploy backend to Google Cloud Functions
gcloud functions deploy uruguay-news-api \
  --runtime python311 \
  --trigger-http \
  --entry-point main \
  --source backend/ \
  --allow-unauthenticated

# Deploy frontend to GitHub Pages
cd frontend/web
npm run build
npm run deploy
```

### Environment Variables

```bash
# Production API endpoint
export REACT_APP_API_URL=https://us-central1-your-project.cloudfunctions.net/uruguay-news-api

# Google Cloud project
export GOOGLE_CLOUD_PROJECT=your-project-id
```

---

**Need Help?** Join our [community discussions](https://github.com/JuanFKurucz/uruguay-news/discussions) or check the [development setup guide](../development/setup.md). 