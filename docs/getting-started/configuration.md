# Configuration Guide

This guide covers how to configure the Uruguay News Analysis System for your environment.

## Environment Variables

### Backend Configuration

Create a `.env` file in the `backend/` directory:

```bash
# Google Cloud Configuration
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_APPLICATION_CREDENTIALS=path/to/service-account.json
FIRESTORE_EMULATOR_HOST=localhost:8080

# AI Model Configuration
OPENAI_API_KEY=your-openai-key
HUGGINGFACE_API_KEY=your-huggingface-key

# Application Settings
DEBUG=true
LOG_LEVEL=INFO
```

### Frontend Configuration

Create a `.env.local` file in the `frontend/web/` directory:

```bash
# API Configuration
REACT_APP_API_URL=http://localhost:8080
REACT_APP_WS_URL=ws://localhost:8080/ws

# Feature Flags
REACT_APP_ENABLE_ANALYTICS=true
REACT_APP_ENABLE_REAL_TIME=true
```

## Google Cloud Setup

### 1. Create Project

```bash
gcloud projects create uruguay-news-[YOUR-ID]
gcloud config set project uruguay-news-[YOUR-ID]
```

### 2. Enable APIs

```bash
gcloud services enable cloudfunctions.googleapis.com
gcloud services enable firestore.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable bigquery.googleapis.com
```

### 3. Create Service Account

```bash
gcloud iam service-accounts create uruguay-news-sa \
  --display-name="Uruguay News Service Account"

gcloud projects add-iam-policy-binding uruguay-news-[YOUR-ID] \
  --member="serviceAccount:uruguay-news-sa@uruguay-news-[YOUR-ID].iam.gserviceaccount.com" \
  --role="roles/editor"
```

## MCP Server Configuration

The MCP servers are configured in `.cursor/mcp.json`. Update the GitHub token:

```bash
cp .cursor/mcp.env.template .cursor/mcp.env
# Edit .cursor/mcp.env and add your GitHub token
```

## Next Steps

- [Quick Start](quick-start.md) - Run your first analysis
- [Development Setup](../development/setup.md) - Set up development environment 