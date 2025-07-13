# Installation Guide

This guide will walk you through setting up the Uruguay News Analysis System on your local machine.

## Prerequisites

Before you begin, ensure you have the following installed:

### Required Software
- **Python 3.11+** - [Download Python](https://www.python.org/downloads/)
- **Node.js 18+** - [Download Node.js](https://nodejs.org/)
- **Git** - [Download Git](https://git-scm.com/)
- **Google Cloud CLI** - [Install gcloud](https://cloud.google.com/sdk/docs/install)

### Accounts Needed
- **Google Cloud Account** - [Create Account](https://cloud.google.com/) (free tier sufficient)
- **GitHub Account** - [Create Account](https://github.com/) (for version control)

## Quick Installation

### 1. Clone the Repository

```bash
git clone https://github.com/JuanFKurucz/uruguay-news.git
cd uruguay-news
```

### 2. Install UV Package Manager

UV is 10-100x faster than pip and is our recommended package manager:

=== "Linux/macOS"

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

=== "Windows"

    ```powershell
    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

=== "Alternative (pip)"

    ```bash
    pip install uv
    ```

### 3. Backend Setup

```bash
cd backend
uv sync
uv run python -m pip install functions-framework
```

### 4. Frontend Setup

```bash
cd frontend/web
npm install
```

### 5. Google Cloud Setup

```bash
# Install Google Cloud CLI components
gcloud components install cloud-firestore-emulator
gcloud components install cloud-functions-emulator

# Initialize Google Cloud
gcloud init
gcloud auth application-default login

# Enable required APIs
gcloud services enable cloudfunctions.googleapis.com
gcloud services enable firestore.googleapis.com
gcloud services enable run.googleapis.com
```

## Detailed Installation

### Backend Environment

1. **Create Virtual Environment**
   ```bash
   cd backend
   uv venv
   source .venv/bin/activate  # Linux/macOS
   # or
   .venv\Scripts\activate     # Windows
   ```

2. **Install Dependencies**
   ```bash
   uv sync
   uv add functions-framework
   uv add google-cloud-firestore
   uv add google-cloud-logging
   ```

3. **Environment Variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

### Frontend Environment

1. **Install Dependencies**
   ```bash
   cd frontend/web
   npm install
   ```

2. **Environment Configuration**
   ```bash
   cp .env.example .env.local
   # Edit .env.local with your API endpoints
   ```

### Google Cloud Configuration

1. **Create Project**
   ```bash
   gcloud projects create uruguay-news-[YOUR-ID]
   gcloud config set project uruguay-news-[YOUR-ID]
   ```

2. **Enable Billing** (Required for some services)
   ```bash
   # Link billing account through Google Cloud Console
   ```

3. **Setup Firestore**
   ```bash
   gcloud firestore databases create --region=us-central1
   ```

4. **Setup Local Emulators**
   ```bash
   # Start Firestore emulator
   gcloud beta emulators firestore start --host-port=localhost:8080
   
   # In another terminal, set environment
   $(gcloud beta emulators firestore env-init)
   ```

## Development Tools

### MCP (Model Context Protocol) Setup

1. **Install MCP Servers**
   ```bash
   # GitHub MCP Server
   docker pull ghcr.io/github/github-mcp-server:v1.0.0
   
   # Filesystem MCP Server
   docker pull ghcr.io/modelcontextprotocol/server-filesystem:v0.6.0
   ```

2. **Configure MCP**
   ```bash
   cp .cursor/mcp.env.template .cursor/mcp.env
   # Edit .cursor/mcp.env with your GitHub token
   ```

### IDE Setup

#### VS Code
1. Install recommended extensions:
   - Python
   - Pylance
   - Google Cloud Code
   - MCP Inspector

#### Cursor
1. MCP integration is pre-configured in `.cursor/mcp.json`
2. Ensure Docker is running for MCP servers

## Verification

### Test Backend

```bash
cd backend
uv run python -m pytest tests/
```

### Test Frontend

```bash
cd frontend/web
npm test
```

### Test Google Cloud Connection

```bash
gcloud auth list
gcloud config list
```

### Test MCP Servers

```bash
# Test GitHub MCP
docker run --rm -e GITHUB_PERSONAL_ACCESS_TOKEN=your_token ghcr.io/github/github-mcp-server:v1.0.0

# Test Filesystem MCP
docker run --rm -v $(pwd):/workspace ghcr.io/modelcontextprotocol/server-filesystem:v0.6.0 /workspace
```

## Troubleshooting

### Common Issues

#### Python Version Issues
```bash
# Check Python version
python --version
uv python list
```

#### Google Cloud Authentication
```bash
# Re-authenticate
gcloud auth revoke
gcloud auth login
gcloud auth application-default login
```

#### Port Conflicts
```bash
# Check port usage
netstat -tulpn | grep :8080
# Kill process if needed
kill -9 $(lsof -ti:8080)
```

#### Docker Issues
```bash
# Restart Docker
sudo systemctl restart docker  # Linux
# or restart Docker Desktop
```

### Performance Optimization

#### UV Configuration
```bash
# Use UV for faster installs
export UV_CACHE_DIR=/tmp/uv-cache
export UV_PYTHON_PREFERENCE=only-managed
```

#### Node.js Optimization
```bash
# Increase Node.js memory
export NODE_OPTIONS="--max-old-space-size=4096"
```

## Next Steps

Once installation is complete:

1. **[Configuration](configuration.md)** - Configure your environment
2. **[Quick Start](quick-start.md)** - Run your first analysis
3. **[Development](../development/setup.md)** - Start developing

## Getting Help

If you encounter issues:

1. Check the [troubleshooting section](#troubleshooting)
2. Search [GitHub Issues](https://github.com/JuanFKurucz/uruguay-news/issues)
3. Create a new issue with:
   - Your operating system
   - Python/Node.js versions
   - Full error messages
   - Steps to reproduce

Happy coding! 🚀 