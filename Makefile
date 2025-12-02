.PHONY: format lint check

format:
	uv run ruff check --fix .
	uv run ruff format .

lint:
	uv run ruff check .

check:
	uv run ruff check .
	uv run ruff format --check .
