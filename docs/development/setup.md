# Development Setup Guide

This guide covers setting up a complete development environment for the Uruguay News Analysis System.

## Prerequisites

### Required Software
- **Python 3.11+** - Backend development
- **Node.js 18+** - Frontend development  
- **UV Package Manager** - Fast Python dependency management
- **Google Cloud SDK** - Cloud services integration
- **Git** - Version control

### Optional Tools
- **Docker** - For running Redis locally
- **VS Code** - Recommended IDE with extensions:
  - Python
  - TypeScript and JavaScript
  - Tailwind CSS IntelliSense
  - GitLens

## Backend Development Setup

### 1. Install UV Package Manager

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
irm https://astral.sh/uv/install.ps1 | iex
```

### 2. Setup Backend Environment

```bash
# Navigate to backend directory
cd backend

# Install dependencies with UV
uv sync

# Activate virtual environment
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows

# Install development dependencies
uv sync --extra dev --extra test
```

### 3. Configure Environment Variables

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your credentials
# - Google Cloud project ID
# - OpenAI API key
# - Other service credentials
```

### 4. Start Local Services

```bash
# Terminal 1: Start Firestore emulator
gcloud beta emulators firestore start --host-port=localhost:8080

# Terminal 2: Start Redis (Docker)
docker run -d -p 6379:6379 redis:alpine

# Terminal 3: Start backend server
cd backend
uv run functions-framework --target=main --port=8081 --debug
```

## Frontend Development Setup

### 1. Install Dependencies

```bash
# Navigate to frontend directory
cd frontend/web

# Install npm dependencies
npm install

# Or using yarn
yarn install
```

### 2. Configure Environment

```bash
# Create environment file
cp .env.example .env.local

# Edit .env.local with API endpoints
REACT_APP_API_URL=http://localhost:8081
REACT_APP_WS_URL=ws://localhost:8081/ws
```

### 3. Start Development Server

```bash
# Start React development server
npm start

# Or using yarn
yarn start
```

The frontend will be available at `http://localhost:3000`

## Documentation Development

### 1. Install Documentation Dependencies

```bash
# From project root
uv sync --extra docs
```

### 2. Start Documentation Server

```bash
# Serve documentation locally
uv run mkdocs serve

# Documentation available at http://localhost:8000
```

## Development Workflow

### Code Quality

```bash
# Backend code formatting
cd backend
uv run black .
uv run ruff check .
uv run mypy .

# Frontend code formatting
cd frontend/web
npm run lint
npm run format
```

### Testing

```bash
# Backend tests
cd backend
uv run pytest
uv run pytest --cov=src

# Frontend tests
cd frontend/web
npm test
npm run test:coverage
```

### Pre-commit Hooks

```bash
# Install pre-commit hooks
cd backend
uv run pre-commit install

# Run hooks manually
uv run pre-commit run --all-files
```

## Troubleshooting

### Common Issues

1. **Port conflicts**: Ensure Firestore emulator (8080) and backend (8081) use different ports
2. **Permission errors**: Check Google Cloud credentials and project permissions
3. **Module not found**: Ensure virtual environments are activated
4. **Build failures**: Clear node_modules and reinstall dependencies

### Environment Reset

```bash
# Reset backend environment
cd backend
rm -rf .venv
uv sync

# Reset frontend environment
cd frontend/web
rm -rf node_modules package-lock.json
npm install
```

## IDE Configuration

### VS Code Settings

Create `.vscode/settings.json`:

```json
{
  "python.defaultInterpreterPath": "./backend/.venv/bin/python",
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.ruffEnabled": true,
  "typescript.preferences.importModuleSpecifier": "relative",
  "tailwindCSS.includeLanguages": {
    "typescript": "javascript",
    "typescriptreact": "javascript"
  }
}
```

## Next Steps

- [Configuration Guide](../getting-started/configuration.md) - Configure services and credentials
- [Testing Guide](testing.md) - Learn about testing strategies
- [Deployment Guide](deployment.md) - Deploy to production environments 