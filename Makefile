.PHONY: all
all: clean setup test lint mypy bandit

.PHONY: setup
setup: pyproject.toml
	poetry install

.PHONY: test
test:
	poetry run pytest --cov=dinesafe_toronto/ --cov-report=xml

.PHONY: lint
lint:
	poetry run black --check .
	poetry run isort --check .
	poetry run ruff check .

.PHONY: mypy
mypy:
	poetry run mypy dinesafe_toronto/

.PHONY: bandit
bandit:
	poetry run bandit --recursive --quiet dinesafe_toronto/

.PHONY: clean
clean:
	rm -fr ./.mypy_cache
	rm -fr ./.pytest_cache
	rm -fr ./.ruff_cache
	rm -fr ./dist
	rm .coverage
	rm coverage.xml
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

.PHONY: build
build:
	poetry run dinesafe-toronto scrape-data ./dinesafe.db

.PHONY: datasette
datasette: dinesafe.db
	poetry run datasette serve ./dinesafe.db --metadata metadata.json
