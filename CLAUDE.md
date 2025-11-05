# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Reflex** web application for VoorVoet - Praktijk voor Podotherapie (a podiatry practice). Reflex is a Python web framework that allows you to build full-stack applications using only Python.

## Architecture

### Core Structure
- **Main app**: `voorvoet_website/voorvoet_website.py` - Entry point, defines routes and app configuration
- **Configuration**: `rxconfig.py` - Reflex app configuration with plugins and settings
- **Theme**: `voorvoet_website/theme.py` - Color scheme and visual styling constants
- **State Management**: `voorvoet_website/state/website_state.py` - Global app state using Reflex's state system

### Page Structure
- **Pages**: `voorvoet_website/pages/` - Page components organized by feature
  - `home_page/` - Home page with hero section and content sections
  - `shared_components/` - Reusable components like header, footer, modal
- **Components**: `voorvoet_website/components/` - Reusable UI components (button, container, responsive_grid, section)

### Key Components Architecture
- Pages are built using composition of sections (hero, content sections)
- Components follow a pattern of accepting props and returning `rx.Component`
- State is managed centrally through `WebsiteState` class extending `rx.State`
- Responsive design using grid systems and breakpoint-based styling

## Development Commands

### Testing the Application
```bash
reflex compile
```

### Building
```bash
reflex export           # Export static site
```

### Dependencies
The project uses UV for dependency management:
```bash
uv sync                 # Install/sync dependencies
uv add <package>        # Add new dependency
```

## Key Conventions

### Component Structure
- Components should return `rx.Component` type
- Use functional component style with type hints
- Import theme constants from `voorvoet_website.theme`
- Follow existing naming patterns for consistency

### State Management
- Extend `WebsiteState` for new state variables
- Use event handlers (methods) for state mutations
- Modal and navigation state already implemented

### Styling
- Use theme constants: `PRIMARY`, `ACCENT`, `LIGHT`, `MUTED`, `DARK`
- Color palette defined in `COLORS["voorvoet"]` with shades 50, 100, 300, 500, 700
- Responsive design using array notation: `width=["100%", "50%"]` for mobile/desktop

### File Organization
- New pages go in `voorvoet_website/pages/`
- Reusable components in `voorvoet_website/components/`
- Page-specific components in respective page directories
- Assets in `assets/` directory at project root
