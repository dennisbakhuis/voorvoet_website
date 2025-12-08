.PHONY: format test types

format:
	uv run ruff check --fix .
	uv run ruff format .

test:
	uv run pytest

types:
	uv run mypy .
