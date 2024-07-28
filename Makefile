format:
	poetry run ruff format src
	poetry run ruff check src --fix
	poetry run toml-sort pyproject.toml
up:
	docker-compose up --build