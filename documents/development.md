# Development Environment Setup
This guide covers setting up a local development environment for the VoorVoet website.

## Prerequisites
- **Python 3.13+** - Required for Reflex framework
- **uv** - Fast Python package installer ([installation guide](https://github.com/astral-sh/uv))

## Setup Steps

### 1. Clone the Repository
```bash
git clone <repository-url>
cd voorvoet-website
```

### 2. Install Dependencies
```bash
uv sync
```
This creates a virtual environment and installs all required packages.

### 3. Configure Environment Variables
```bash
cp .env.example .env
```

Edit `.env` and configure:

**For local development (minimal config):**
```env
# Disable bot protection during development
TURNSTILE_ENABLED=false

# Set a placeholder link
LINK_PLAN_PORTAL=https://example.com

# Blog settings (optional)
BLOG_SHOW_AUTHOR=false
BLOG_SHOW_PUBLICATION_DATE=false
BLOG_SHOW_READING_TIME=false

# Local site URL
SITE_URL=http://localhost:3000
```

**For full functionality (optional):**
- Get Cloudflare Turnstile keys from [Turnstile Dashboard](https://dash.cloudflare.com/?to=/:account/turnstile)
- Configure SMTP credentials (see [SMTP Setup](smpt_server_setup.md))

### 4. Run Development Server
```bash
uv run reflex run
```

The site will be available at `http://localhost:3000`

## Development Workflow

### Testing Compilation
```bash
uv run reflex compile
```
Verifies all pages compile without errors.

### Hot Reload
Reflex automatically reloads when you edit:
- Python files (components, pages, state)
- Theme files

**Note:** Blog content changes require a manual restart.

### Project Structure
```
voorvoet_website/
├── pages/              # Page components
├── components/         # Reusable UI components
├── state/             # State management
├── data/              # Blog content (Markdown)
└── theme.py           # Design system constants
```

See [CLAUDE.md](../CLAUDE.md) for detailed architecture and patterns.

## Testing

### Pre-commit Hooks
The project uses pre-commit hooks to ensure code quality before commits.

**Initial setup:**
```bash
uv run pre-commit install
```

**What runs automatically on commit:**
- **Ruff** - Code linting and formatting
- **Mypy** - Static type checking
- **File checks** - Trailing whitespace, YAML syntax, large files, etc.

**Run manually:**
```bash
# Run on staged files
uv run pre-commit run

# Run on all files
uv run pre-commit run --all-files
```

### Type Checking
```bash
uv run mypy voorvoet_website/
```
Runs static type analysis on the codebase. Configuration in `pyproject.toml`.

### Linting and Formatting
```bash
# Check for issues
uv run ruff check .

# Auto-fix issues
uv run ruff check --fix .

# Format code
uv run ruff format .
```

### Unit Tests
```bash
# Run all tests
uv run pytest

# Run with verbose output
uv run pytest -v

# Run specific test file
uv run pytest tests/test_routes.py

# Skip slow tests
uv run pytest -m "not slow"
```

Test configuration in `pyproject.toml`. Tests are located in `tests/` directory.

### Production Build Test (SSR)
Before deploying, verify the app compiles for server-side rendering:

```bash
uv run reflex run --env prod
```

This ensures all pages compile correctly for production deployment. Critical for catching SSR-specific issues that may not appear in development mode.

## Common Issues

### Module not found
```bash
uv sync  # Re-sync dependencies
```

### Changes not reflecting
- Check terminal for compilation errors
- Restart dev server for blog content changes
- Clear browser cache for style changes

### Port already in use
```bash
# Kill process on port 3000
lsof -ti:3000 | xargs kill -9
```
