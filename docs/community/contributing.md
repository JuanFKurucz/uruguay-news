# Contributing Guidelines

## Welcome Contributors

Thank you for your interest in contributing to the Uruguay News Analysis System! This project is open-source and welcomes contributions from developers, researchers, and domain experts.

## Getting Started

### Prerequisites
- Python 3.11+
- UV package manager
- Git
- Google Cloud SDK (for cloud features)

### Setup Development Environment
```bash
# Clone the repository
git clone https://github.com/JuanFKurucz/uruguay-news.git
cd uruguay-news

# Install dependencies
cd backend
uv sync

# Start development services
firebase emulators:start --only firestore &
redis-server &
uv run python -m main
```

## Ways to Contribute

### Code Contributions
- **Bug fixes**: Help fix issues in the codebase
- **New features**: Implement new functionality
- **Performance improvements**: Optimize existing code
- **Documentation**: Improve code documentation

### AI Model Contributions
- **Training data**: Contribute annotated Uruguayan news articles
- **Model improvements**: Enhance sentiment analysis accuracy
- **Bias detection**: Improve political bias detection models
- **Cultural context**: Add Uruguayan cultural understanding

### Documentation Contributions
- **User guides**: Write helpful tutorials
- **API documentation**: Improve API reference
- **Architecture docs**: Document system design
- **Translation**: Translate documentation to Spanish

## Development Process

### 1. Fork and Clone
```bash
git clone https://github.com/YOUR_USERNAME/uruguay-news.git
cd uruguay-news
git remote add upstream https://github.com/JuanFKurucz/uruguay-news.git
```

### 2. Create Feature Branch
```bash
git checkout -b feature/your-feature-name
```

### 3. Make Changes
- Follow the coding standards in [Development Guidelines](../development/guidelines.md)
- Write tests for new functionality
- Update documentation as needed

### 4. Test Your Changes
```bash
# Run tests
uv run pytest

# Run linting
uv run ruff check .
uv run mypy .

# Test with emulators
firebase emulators:start --only firestore &
uv run pytest tests/integration/
```

### 5. Submit Pull Request
- Create a clear PR description
- Reference related issues
- Ensure all tests pass
- Request review from maintainers

## Code Standards

### Python
- Follow PEP 8 style guidelines
- Use type hints for all functions
- Write comprehensive docstrings
- Maintain 80%+ test coverage

### JavaScript/TypeScript
- Use strict TypeScript configuration
- Follow ESLint rules
- Write unit tests for components
- Use consistent naming conventions

## AI Model Guidelines

### Data Contributions
- Ensure data privacy compliance
- Provide proper attribution
- Use consistent annotation formats
- Follow ethical guidelines

### Model Improvements
- Document model changes thoroughly
- Provide performance benchmarks
- Include cultural context considerations
- Test with diverse data sources

## Community Guidelines

### Code of Conduct
- Be respectful and inclusive
- Provide constructive feedback
- Help newcomers learn
- Follow ethical AI principles

### Communication
- Use GitHub Issues for bug reports
- Use Discussions for questions
- Be clear and concise
- Provide context and examples

## Recognition

### Contributors
All contributors are recognized in:
- README.md contributors section
- Release notes
- Documentation credits
- Annual contributor reports

### Contributions Types
- 🐛 Bug fixes
- ✨ New features
- 📚 Documentation
- 🎨 Design improvements
- 🔧 Maintenance
- 🌐 Translation

## Getting Help

### Resources
- [Development Setup](../development/setup.md)
- [Architecture Overview](../architecture/overview.md)
- [API Documentation](../api/rest.md)
- [Testing Guide](../development/testing.md)

### Support Channels
- GitHub Issues: Bug reports and feature requests
- GitHub Discussions: Questions and community chat
- Email: maintainers@uruguaynews.com
- Discord: [Uruguay News Discord](https://discord.gg/uruguaynews)

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing to the Uruguay News Analysis System! 🇺🇾 