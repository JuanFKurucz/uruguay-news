# .cursor Directory

This directory contains configuration files for Model Context Protocol (MCP) integration and development automation for the Uruguay News project.

## What is MCP?
Model Context Protocol (MCP) is an open standard that allows AI models and development tools to securely interact with external systems (like GitHub, filesystems, databases, and more) through standardized, pluggable servers. MCP enables rapid, secure, and reproducible AI-driven development workflows.

## Files in This Directory

- **mcp.json**: Main configuration file listing all enabled MCP servers for this project. Each server is run as a Docker container for security and reproducibility. Only minimal, essential tools are enabled by default (GitHub, filesystem, fetch, memory).
- **mcp.env.template**: Template for environment variables (API keys, tokens) required by MCP servers. Copy to `.cursor/mcp.env` and fill in your secrets. **Never commit `.cursor/mcp.env` to version control!**
- **rules/**: Directory containing project-specific development rules, best practices, and automation patterns for Cursor and AI-assisted workflows.

## Security Notes
- **Never commit secrets**: `.cursor/mcp.env` is in `.gitignore` and must never be committed.
- **Rotate API keys** regularly and use different keys for development and production.
- **Review Docker images**: All MCP servers are run as containers for isolation and security.

## Extending MCP Tools
- To add more MCP servers (e.g., for databases, search, or cloud services), add them to `mcp.json` following the existing pattern.
- Document any new tools or requirements in this README for future contributors.

## For Contributors
- If you want to propose new MCP integrations, open a PR and update this README and `mcp.json`.
- For questions or suggestions, see the main project README or open an issue.

---

**This directory is the foundation for secure, AI-driven, and automated development in the Uruguay News project.** 