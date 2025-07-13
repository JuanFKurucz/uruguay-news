# Security Policy

## 🔒 Protecting Sensitive Information

This is an open-source project. **Never commit sensitive information** to version control.

### ❌ **Never Commit:**
- Google Cloud project IDs
- Service account keys or credentials
- API keys (OpenAI, etc.)
- Database connection strings
- Private keys or certificates
- Environment-specific URLs or domains

### ✅ **Always Use:**
- Environment variables for configuration
- GitHub Secrets for CI/CD deployment
- Generic placeholders in documentation
- The `credentials/` directory (gitignored)

### 📁 **Protected Directories:**
- `credentials/` - Service account keys (fully gitignored)
- `.env*` - Environment files (gitignored)
- Any files matching `*secret*`, `*credential*`, `*key*.json`

### 🔧 **Local Development:**
1. Place your Google Cloud service account key in `credentials/your-service-account-key.json`
2. Create `.env` file with your project-specific values
3. Use `GOOGLE_APPLICATION_CREDENTIALS=credentials/your-service-account-key.json`
4. Set `GOOGLE_CLOUD_PROJECT=your-actual-project-id`

### 🚀 **CI/CD Deployment:**
- Use GitHub Secrets for `GOOGLE_APPLICATION_CREDENTIALS` (JSON content)
- Use GitHub Secrets for `GOOGLE_CLOUD_PROJECT` (project ID)
- Never hardcode sensitive values in workflow files

### 🚨 **If You Accidentally Commit Sensitive Data:**
1. **Immediately** remove the sensitive information
2. Force push to overwrite git history: `git push --force`
3. Rotate any compromised credentials (create new service account keys)
4. Update GitHub Secrets with new credentials

### 📝 **Documentation Guidelines:**
- Use `your-project-id` instead of actual project IDs
- Use `your-service-account-key.json` instead of actual filenames
- Use `yourdomain.com` instead of actual domains
- Always include environment variable examples

### 🔍 **Security Audit:**
Before committing, always check:
```bash
# Check for sensitive patterns
git diff --cached | grep -E "(key|credential|secret|password|token)"

# Verify gitignore is working
git status --ignored
```

### 🐛 **Reporting Security Issues:**
If you discover a security vulnerability, please report it privately to the maintainers rather than creating a public issue.

---

**Remember**: Security is everyone's responsibility. When in doubt, use environment variables! 