# Quick Start Guide

Get the Uruguay News Analysis System running in minutes! This guide assumes you've completed the [installation](installation.md).

## 🚀 Run Your First Analysis

### 1. Start the Backend Services

```bash
# Terminal 1: Start Firestore emulator
gcloud beta emulators firestore start --host-port=localhost:8080

# Terminal 2: Start the backend
cd backend
uv run functions-framework --target=analyze_sentiment --debug
```

### 2. Start the Frontend

```bash
# Terminal 3: Start the frontend
cd frontend/web
npm start
```

### 3. Test the System

Open your browser and navigate to:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8080

## 🧪 Run a Sample Analysis

### Analyze a News Article

```bash
curl -X POST http://localhost:8080/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "text": "El presidente anunció nuevas medidas económicas que beneficiarán a las familias uruguayas.",
    "source": "test",
    "language": "es"
  }'
```

Expected response:
```json
{
  "sentiment": {
    "label": "POSITIVE",
    "score": 0.8234,
    "confidence": 0.9156
  },
  "bias": {
    "political": "NEUTRAL",
    "confidence": 0.7892
  },
  "entities": [
    {
      "text": "presidente",
      "type": "PERSON",
      "confidence": 0.9234
    }
  ]
}
```

### Analyze Multiple Sources

```bash
curl -X POST http://localhost:8080/batch-analyze \
  -H "Content-Type: application/json" \
  -d '{
    "articles": [
      {
        "text": "La economía uruguaya muestra signos de recuperación.",
        "source": "el_pais"
      },
      {
        "text": "Preocupación por el aumento del desempleo en el país.",
        "source": "la_diaria"
      }
    ]
  }'
```

## 📊 View Results in Dashboard

1. Open http://localhost:3000
2. Navigate to **Analysis Dashboard**
3. View real-time sentiment trends
4. Explore bias detection results
5. Check entity recognition

## 🔧 Development Workflow

### Make Changes

1. **Backend Changes**:
   ```bash
   # Edit files in backend/
   # Functions Framework auto-reloads
   ```

2. **Frontend Changes**:
   ```bash
   # Edit files in frontend/web/src/
   # React dev server auto-reloads
   ```

### Run Tests

```bash
# Backend tests
cd backend
uv run pytest tests/

# Frontend tests
cd frontend/web
npm test
```

### Check Code Quality

```bash
# Python linting
cd backend
uv run ruff check .
uv run mypy .

# JavaScript linting
cd frontend/web
npm run lint
```

## 🌐 Test with Real News Sources

### Scrape Live Content

```bash
# Scrape from El País
curl -X POST http://localhost:8080/scrape \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://www.elpais.com.uy/informacion/politica",
    "source": "el_pais"
  }'
```

### Monitor Social Media

```bash
# Monitor Twitter trends
curl -X POST http://localhost:8080/monitor \
  -H "Content-Type: application/json" \
  -d '{
    "platform": "twitter",
    "keywords": ["Uruguay", "política", "economía"]
  }'
```

## 📈 Performance Monitoring

### Check System Health

```bash
# Health check
curl http://localhost:8080/health

# Metrics
curl http://localhost:8080/metrics
```

### Monitor AI Performance

```bash
# Sentiment analysis accuracy
curl http://localhost:8080/metrics/sentiment

# Bias detection performance
curl http://localhost:8080/metrics/bias
```

## 🐛 Troubleshooting

### Common Issues

#### Backend Not Starting
```bash
# Check if port is in use
netstat -tulpn | grep :8080

# Kill existing process
kill -9 $(lsof -ti:8080)
```

#### Frontend Build Errors
```bash
# Clear cache
cd frontend/web
rm -rf node_modules
npm install
```

#### Firestore Connection Issues
```bash
# Check emulator status
gcloud beta emulators firestore env-init

# Restart emulator
gcloud beta emulators firestore start --host-port=localhost:8080
```

### Performance Issues

#### Slow Analysis
- Check if models are cached
- Verify GPU acceleration (if available)
- Monitor memory usage

#### High Memory Usage
```bash
# Monitor resources
top -p $(pgrep -f "functions-framework")
```

## 🚀 Deploy to Production

### Deploy Backend to Google Cloud

```bash
cd backend
gcloud functions deploy analyze-sentiment \
  --runtime python311 \
  --trigger-http \
  --allow-unauthenticated
```

### Deploy Frontend to GitHub Pages

```bash
cd frontend/web
npm run build
npm run deploy
```

## 📚 Next Steps

Now that you have the system running:

1. **[Architecture](../architecture/overview.md)** - Understand the system design
2. **[Development](../development/setup.md)** - Set up your development environment
3. **[API Reference](../api/rest.md)** - Explore the API endpoints
4. **[AI Models](../ai/sentiment.md)** - Learn about our AI models

## 🤝 Get Involved

- **Report Issues**: Found a bug? [Create an issue](https://github.com/JuanFKurucz/uruguay-news/issues)
- **Contribute**: [Contributing Guide](../community/contributing.md)
- **Discuss**: Join our community discussions

Happy analyzing! 🇺🇾✨ 