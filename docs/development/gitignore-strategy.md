# .gitignore Strategy

This document explains the layered `.gitignore` strategy used in the Uruguay News project to keep the repository clean and organized.

## Overview

The project uses a **layered .gitignore approach** with specific ignore files for each component:

```
uruguay-news/
├── .gitignore              # Project-level ignores
├── backend/.gitignore      # Python/Google Cloud specific
├── frontend/.gitignore     # Node.js/React specific  
├── docs/.gitignore         # Documentation specific
└── .cursor/.gitignore      # Development tooling specific
```

## Strategy Benefits

1. **Separation of Concerns**: Each component manages its own ignore patterns
2. **Maintainability**: Easier to update technology-specific patterns
3. **Clarity**: Developers know exactly what's ignored where
4. **Reusability**: Component-specific files can be reused in other projects
5. **Reduced Conflicts**: Less chance of merge conflicts in ignore files

## File Breakdown

### Root Level `.gitignore`

**Purpose**: Project-wide patterns and coordination

**Contains**:
- Environment variables (`.env` files)
- UV lock file (`uv.lock`)
- IDE and editor files
- OS-specific files
- Logs and temporary files
- Secrets and credentials
- Infrastructure files (Terraform, Docker)
- Project-specific data directories

```gitignore
# Project-level ignores
.env
.env.local
.env.development
.env.test
.env.production

# UV lock file (keep this at root level)
uv.lock

# IDE and editors
.vscode/
.idea/
*.swp
*.swo
*~
```

### Backend `.gitignore`

**Purpose**: Python, Google Cloud, and AI/ML development

**Contains**:
- Python bytecode and packages
- UV virtual environments
- Generated requirements.txt files
- Google Cloud credentials
- AI/ML artifacts (models, weights, datasets)
- Testing and coverage reports
- Python-specific caches

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class

# UV - Python package manager
.venv/
venv/
uv.lock

# Generated requirements files (use UV instead)
requirements.txt
*requirements*.txt

# Google Cloud
.gcloudignore
service-account-key.json
*-credentials.json

# AI/ML specific
models/
weights/
checkpoints/
experiments/
wandb/
```

### Frontend `.gitignore`

**Purpose**: Node.js, React, and web development

**Contains**:
- Node.js dependencies (`node_modules/`)
- Build outputs (`build/`, `dist/`)
- Package manager lock files
- Frontend-specific caches
- Environment variables for web apps
- Mobile development artifacts

```gitignore
# Dependencies
node_modules/
.pnp
.pnp.js

# Production builds
build/
dist/
out/

# Package manager lock files
package-lock.json
yarn.lock
pnpm-lock.yaml

# Environment variables
.env.local
.env.development.local
.env.test.local
.env.production.local
```

### Documentation `.gitignore`

**Purpose**: MkDocs and documentation generation

**Contains**:
- MkDocs build output (`site/`)
- Documentation caches
- Generated documentation files
- Temporary documentation files

```gitignore
# MkDocs
site/
.mkdocs_cache/

# Sphinx documentation
_build/
_static/
_templates/

# Generated files
*.pdf
*.epub
*.mobi
```

### Cursor `.gitignore`

**Purpose**: Development tooling and MCP configuration

**Contains**:
- MCP environment files with API keys
- Cursor AI caches
- Development tool artifacts
- AI model caches

```gitignore
# MCP Environment Files (CRITICAL - Contains API Keys)
mcp.env
*.env
*.env.local
*.env.production
*.env.staging

# Cursor AI cache
.cursor-cache/
.cursor-logs/

# AI model cache
.ai-cache/
.model-cache/
```

## Best Practices

### 1. Security First

- **Never commit secrets**: All credential patterns are ignored
- **Environment files**: Multiple patterns to catch all `.env` variations
- **API keys**: Specific patterns for MCP and cloud credentials

### 2. Technology-Specific Patterns

- **Backend**: Focus on Python, UV, Google Cloud, AI/ML
- **Frontend**: Focus on Node.js, React, build tools
- **Docs**: Focus on documentation generators
- **Tooling**: Focus on development environment

### 3. Performance Considerations

- **Cache directories**: All major cache types ignored
- **Build outputs**: Prevent committing generated files
- **Large files**: AI models, datasets, and media files ignored

### 4. Development Experience

- **IDE files**: Common editor configurations ignored
- **OS files**: Platform-specific system files ignored
- **Temporary files**: Various temp file patterns covered

## Maintenance

### Adding New Patterns

1. **Identify the scope**: Which component does it belong to?
2. **Add to appropriate file**: Use the most specific `.gitignore`
3. **Document if needed**: Update this guide for major changes
4. **Test thoroughly**: Ensure patterns work as expected

### Common Additions

```bash
# Backend - new AI framework
backend/.gitignore:
.langflow/
.chainlit/

# Frontend - new build tool
frontend/.gitignore:
.turbo/
.nx/

# Docs - new generator
docs/.gitignore:
.quarto/
.hugo/
```

### Troubleshooting

#### File Still Being Tracked

If a file is still being tracked despite being in `.gitignore`:

```bash
# Remove from git tracking
git rm --cached filename

# Or for directories
git rm -r --cached directory/

# Commit the removal
git commit -m "Remove tracked file from repository"
```

#### Pattern Not Working

1. **Check file location**: Ensure `.gitignore` is in the right directory
2. **Test pattern**: Use `git check-ignore -v filename` to debug
3. **Escape special characters**: Use backslashes for regex characters
4. **Check precedence**: More specific patterns override general ones

## Integration with Tools

### UV Package Manager

- `uv.lock` kept at root level for project coordination
- `requirements.txt` files ignored (generated dynamically)
- Virtual environments ignored in all locations

### GitHub Actions

The CI/CD workflows work seamlessly with this strategy:

```yaml
# Workflows automatically handle:
- name: Generate requirements.txt
  run: uv export --format requirements-txt --output-file requirements.txt

# No need to commit generated files
```

### MCP Development

- API keys safely ignored in `.cursor/.gitignore`
- Development caches ignored for performance
- Template files committed for team coordination

## Examples

### Checking What's Ignored

```bash
# Check if a file is ignored
git check-ignore filename

# See which .gitignore rule matches
git check-ignore -v filename

# List all ignored files
git ls-files --others --ignored --exclude-standard
```

### Adding New Technology

When adding a new technology stack:

1. **Create component directory**:
   ```bash
   mkdir new-component
   ```

2. **Add specific .gitignore**:
   ```bash
   touch new-component/.gitignore
   ```

3. **Add technology-specific patterns**:
   ```gitignore
   # Technology-specific ignores
   *.technology-cache
   .technology-config/
   ```

4. **Update root .gitignore if needed**:
   ```gitignore
   # Project-specific data for new component
   new-component-data/
   ```

## Resources

- [Git Documentation - gitignore](https://git-scm.com/docs/gitignore)
- [GitHub's gitignore templates](https://github.com/github/gitignore)
- [Python gitignore patterns](https://github.com/github/gitignore/blob/main/Python.gitignore)
- [Node.js gitignore patterns](https://github.com/github/gitignore/blob/main/Node.gitignore) 