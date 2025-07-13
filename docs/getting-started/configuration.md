# Configuration

This guide covers how to configure the Uruguay News Analysis System for your environment.

## Environment Variables

> **Security Note**: Never commit `.env` files or API keys to version control. Ensure these files are included in `.gitignore` and use secure credential management in production environments.

The system uses environment variables for configuration. Create a `.env` file in your project root:

```bash
# Google Cloud Configuration
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_APPLICATION_CREDENTIALS=credentials/your-service-account-key.json

# Database Configuration
FIRESTORE_COLLECTION_PREFIX=uruguay_news
REDIS_URL=redis://localhost:6379

# API Configuration
API_BASE_URL=http://localhost:8081
CORS_ORIGINS=http://localhost:3000,https://juanfkurucz.github.io

# AI Configuration
OPENAI_API_KEY=your-openai-key-here
MODEL_TEMPERATURE=0.7
MAX_TOKENS=2000

# Frontend Configuration
REACT_APP_API_URL=http://localhost:8081
REACT_APP_ENVIRONMENT=development

# Development Settings
ENVIRONMENT=development
DEBUG=true
LOG_LEVEL=INFO
```

!!! danger "Critical Security Warning"
    **Never commit sensitive information to version control!**
    
    - Place your Google Cloud service account key in `credentials/` directory
    - The entire `credentials/` directory is gitignored for security
    - Use environment variables for all sensitive configuration
    - Never hardcode project IDs, API keys, or credentials in documentation
    - Use GitHub Secrets for CI/CD deployment configuration

!!! info "Google Cloud Credentials Setup"
    The project requires Google Cloud credentials for local development:
    - **Project ID**: Set via `GOOGLE_CLOUD_PROJECT` environment variable
    - **Credentials File**: Place your service account key in `credentials/` directory
    - **GitHub Secrets**: Configure `GOOGLE_APPLICATION_CREDENTIALS` and `GOOGLE_CLOUD_PROJECT` for CI/CD deployment
    
    For local development, ensure the credentials file is in the correct location and the `GOOGLE_APPLICATION_CREDENTIALS` environment variable points to it.

## Google Cloud Setup

### 1. Project Creation

```bash
# Set your project as default
gcloud config set project your-project-id
```

### 2. Enable Required APIs

```bash
# Enable necessary Google Cloud APIs
gcloud services enable firestore.googleapis.com
gcloud services enable cloudfunctions.googleapis.com
gcloud services enable redis.googleapis.com
gcloud services enable secretmanager.googleapis.com
```

### 3. Service Account Setup

```bash
# Create service account
gcloud iam service-accounts create uruguay-news-sa \
    --display-name="Uruguay News Service Account"

# Grant necessary permissions
gcloud projects add-iam-policy-binding your-project-id \
    --member="serviceAccount:your-service-account@your-project-id.iam.gserviceaccount.com" \
    --role="roles/datastore.user"

# Download service account key
gcloud iam service-accounts keys create credentials/your-service-account-key.json \
    --iam-account=your-service-account@your-project-id.iam.gserviceaccount.com
```

## Database Configuration

### Firestore Setup

```bash
# Initialize Firestore in your project
gcloud firestore databases create --region=us-central1
```

### Redis Configuration

For local development:

```bash
# Install Redis locally
brew install redis  # macOS
sudo apt-get install redis-server  # Ubuntu

# Start Redis
redis-server
```

For production, use Google Cloud Memorystore:

```bash
# Create Redis instance
gcloud redis instances create uruguay-news-cache \
    --size=1 \
    --region=us-central1 \
    --redis-version=redis_6_x
```

## Frontend Configuration

Create `frontend/web/.env.local`:

```bash
REACT_APP_API_URL=http://localhost:8081
REACT_APP_GOOGLE_ANALYTICS_ID=G-XXXXXXXXXX
REACT_APP_ENVIRONMENT=development
```

## Backend Configuration

The backend uses `pyproject.toml` for dependency management and configuration:

```toml
[tool.ruff]
line-length = 88
target-version = "py311"

[tool.mypy]
python_version = "3.11"
strict = true
```

## Development Environment

For detailed development setup instructions, see [Development Setup](../development/setup.md).

### Port Configuration

- **Frontend**: `3000` (React development server)
- **Backend**: `8081` (FastAPI with Functions Framework)
- **Firestore Emulator**: `8080`
- **Redis**: `6379`

Make sure these ports are available on your system.

## Production Deployment

### Environment-Specific Settings

```bash
# Production environment variables
ENVIRONMENT=production
GOOGLE_CLOUD_PROJECT=your-project-id
CORS_ORIGINS=https://yourdomain.github.io
API_BASE_URL=https://us-central1-your-project-id.cloudfunctions.net/uruguay-news-api
```

### Security Configuration

1. **CORS**: Restrict origins to your frontend domain
2. **Authentication**: Configure Google Identity Platform
3. **Rate Limiting**: Set up Cloud Endpoints for API protection
4. **Monitoring**: Enable Cloud Monitoring and Error Reporting

## Troubleshooting

### Common Issues

1. **Port conflicts**: Ensure ports 3000, 8080, 8081, and 6379 are available
2. **Credentials**: Verify `GOOGLE_APPLICATION_CREDENTIALS` path is correct
3. **Firestore**: Check that Firestore is enabled and properly configured
4. **Redis**: Ensure Redis is running and accessible

### Verification

Test your configuration:

```bash
# Test backend health
curl http://localhost:8081/health

# Test Firestore connection
python -c "from google.cloud import firestore; print('Firestore OK')"

# Test Redis connection
redis-cli ping
```

For more detailed troubleshooting, see our [Development Guide](../development/setup.md).

## Next Steps

Now that you have configured your environment, you can:

- [Quick Start](quick-start.md) - Run your first analysis
- [Development Setup](../development/setup.md) - Set up development environment
- [Installation Guide](installation.md) - Complete installation instructions
- [Project Overview](overview.md) - Learn about the system architecture 