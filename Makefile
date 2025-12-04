.PHONY: format test test-verbose

format:
	uv run ruff check --fix .
	uv run ruff format .

test:
	uv run pytest
