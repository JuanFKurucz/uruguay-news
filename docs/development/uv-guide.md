# UV Package Management Guide

This guide explains how to use UV for package management in the Uruguay News project.

## Why UV?

UV is an extremely fast Python package installer and resolver, written in Rust. It's 10-100x faster than pip and provides better dependency resolution.

### Key Benefits
- **Speed**: 10-100x faster than pip
- **Reliability**: Better dependency resolution
- **Compatibility**: Drop-in replacement for pip
- **Modern**: Built for modern Python packaging standards

## Project Structure

The project uses UV for dependency management:

```
uruguay-news/
├── pyproject.toml          # Main project dependencies
├── uv.lock                 # Lock file (committed to repo)
├── backend/
│   └── pyproject.toml      # Backend-specific dependencies
└── frontend/web/
    └── package.json        # Frontend dependencies (npm)
```

## Installation

### Install UV

```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.sh | iex"

# Or with pip
pip install uv
```

### Verify Installation

```bash
uv --version
```

## Development Workflow

### 1. Initial Setup

```bash
# Clone the repository
git clone https://github.com/juanfkurucz/uruguay-news.git
cd uruguay-news

# Create and activate virtual environment
uv sync
```

### 2. Backend Development

```bash
# Navigate to backend
cd backend

# Install backend dependencies
uv sync

# Run the backend server
uv run uvicorn main:app --reload

# Run tests
uv run pytest

# Run linting
uv run ruff check .
uv run black --check .
uv run mypy .
```

### 3. Documentation

```bash
# Install documentation dependencies
uv sync --extra docs

# Serve documentation locally
uv run mkdocs serve

# Build documentation
uv run mkdocs build
```

### 4. Adding Dependencies

```bash
# Add a new dependency
uv add requests

# Add a development dependency
uv add --dev pytest

# Add a dependency to specific group
uv add --extra docs mkdocs-material
```

### 5. Managing Dependencies

```bash
# Update all dependencies
uv sync --upgrade

# Update specific dependency
uv add "fastapi>=0.105.0"

# Remove dependency
uv remove requests

# Show dependency tree
uv tree
```

## Deployment

### Google Cloud Functions

The deployment workflow automatically generates `requirements.txt` for Cloud Functions:

```bash
# Generate requirements.txt (done automatically in CI/CD)
cd backend
uv export --format requirements-txt --output-file requirements.txt
```

### Local Cloud Functions Testing

```bash
# Install Functions Framework
cd backend
uv sync

# Run locally
uv run functions-framework --target=main --debug
```

## Common Commands

### Environment Management

```bash
# Create virtual environment
uv venv

# Activate virtual environment (if not using uv run)
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# Install dependencies
uv sync

# Install with specific groups
uv sync --extra dev --extra docs
```

### Dependency Management

```bash
# Add dependency
uv add package-name

# Add development dependency
uv add --dev package-name

# Add optional dependency
uv add --extra group-name package-name

# Remove dependency
uv remove package-name

# Update dependencies
uv sync --upgrade
```

### Running Commands

```bash
# Run Python script
uv run python script.py

# Run module
uv run python -m module

# Run installed tool
uv run pytest
uv run black .
uv run ruff check .
```

## Configuration

### pyproject.toml Structure

```toml
[project]
name = "uruguay-news"
dependencies = [
    "fastapi>=0.104.0",
    "pydantic>=2.5.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "black>=23.11.0",
]
docs = [
    "mkdocs>=1.5.3",
    "mkdocs-material>=9.4.0",
]

[tool.uv]
dev-dependencies = [
    "pytest>=7.4.0",
    "black>=23.11.0",
]
```

### Environment Variables

Create `.env` file for local development:

```bash
# Copy example file
cp .env.example .env

# Edit with your values
GOOGLE_CLOUD_PROJECT=your-project-id
OPENAI_API_KEY=your-api-key
```

## Troubleshooting

### Common Issues

1. **UV not found**: Ensure UV is installed and in PATH
2. **Permission errors**: Use `--user` flag or virtual environment
3. **Dependency conflicts**: Use `uv sync --upgrade` to resolve

### Clean Installation

```bash
# Remove virtual environment
rm -rf .venv

# Remove lock file
rm uv.lock

# Fresh installation
uv sync
```

### Performance Tips

1. **Use UV for all Python operations**: `uv run python` instead of `python`
2. **Keep uv.lock committed**: Ensures reproducible builds
3. **Use dependency groups**: Organize dependencies by purpose
4. **Regular updates**: Keep dependencies current with `uv sync --upgrade`

## CI/CD Integration

The project uses UV in GitHub Actions:

```yaml
- name: Install UV
  run: curl -LsSf https://astral.sh/uv/install.sh | sh

- name: Install dependencies
  run: uv sync

- name: Run tests
  run: uv run pytest

- name: Generate requirements.txt
  run: uv export --format requirements-txt --output-file requirements.txt
```

## Best Practices

1. **Never commit requirements.txt**: Let UV generate it dynamically
2. **Use uv.lock**: Commit lock file for reproducible builds
3. **Group dependencies**: Use optional dependencies for different purposes
4. **Pin versions**: Use specific versions for production dependencies
5. **Regular updates**: Keep dependencies current and secure

## Migration from pip/requirements.txt

If migrating from pip:

```bash
# Convert requirements.txt to pyproject.toml
uv add $(cat requirements.txt)

# Or import directly
uv pip install -r requirements.txt
uv pip freeze > requirements.txt
# Then manually convert to pyproject.toml
```

## Resources

- [UV Documentation](https://docs.astral.sh/uv/)
- [Python Packaging Guide](https://packaging.python.org/)
- [pyproject.toml Specification](https://peps.python.org/pep-0621/)
- [Modern Python Packaging](https://hynek.me/articles/python-packaging/) 