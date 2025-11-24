# Project Overview
Multi-language website for VoorVoet podiatry practice built with Reflex (Python web framework). Supports Dutch (primary), German, and English.
## Development Commands
```bash
uv sync                          # Install dependencies
uv run reflex compile            # Test if page compiles
```
## Architecture
### Application Entry Point
Main app is in [voorvoet_website/voorvoet_website.py](voorvoet_website/voorvoet_website.py):
- All routes use language prefixes: `/[lang]`, `/[lang]/blog/`, `/[lang]/blog/[slug]`
- Root paths redirect to `/nl` (Dutch default)
- Pages connect to state handlers via `on_load` callbacks
### State Management
Reflex uses centralized state classes inheriting from `rx.State`:
- **WebsiteState**: Navigation, modals, toasts, language switching
- **BlogState**: Blog post loading/display
- **ContactState**: Contact form with Turnstile verification
- **OrderInsolesState**: Insole order form
### Theme System
Design system in [voorvoet_website/theme.py](voorvoet_website/theme.py):
- **Colors**, **FontSizes**, **Spacing**, **Layout** classes define all visual constants
- Responsive values use 4-breakpoint arrays: `[mobile, sm, md, lg]`
- Always reference theme constants, never hardcode values
### Blog System
- Markdown files in `voorvoet_website/data/blog_content/`
- Naming: `{number}_{slug}.{lang}.md` (e.g., `001_post.nl.md`)
- Blog service caches posts globally; use `clear_cache()` during development
### Configuration
[voorvoet_website/config.py](voorvoet_website/config.py) loads from `.env` (see `.env.example`):
- Cloudflare Turnstile keys
- SMTP credentials
- Blog display preferences
## Key Patterns
### Adding a New Page
1. Create page module in `voorvoet_website/pages/`
2. Add route in `voorvoet_website.py` with language prefix
3. Update `page_title_translations.py` for page titles
### Reusable Components
- Always check `voorvoet_website/components/` for existing components before creating new ones
- If creating reusable UI elements, add them to `components/` for consistency
- Import from `voorvoet_website.components`
### Multi-language Support
- All text must support nl/de/en
- Access current language: `WebsiteState.current_language`
- Blog posts need separate `.nl.md`, `.de.md`, `.en.md` files
