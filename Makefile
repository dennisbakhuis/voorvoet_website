.PHONY: format test types

format:
	uv run ruff check --fix .
	uv run ruff format .

test:
	uv run pytest

types:
	uv run mypy --config-file=pyproject.toml --disable-error-code=unused-ignore --exclude='^tests/' .
