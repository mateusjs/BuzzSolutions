ifeq ($(UNAME_S), Linux)
    OPEN_EXECUTABLE ?= xdg-open
else ifeq ($(UNAME_S), Darwin)
    OPEN_EXECUTABLE ?= open
endif
OPEN_EXECUTABLE ?= :

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "*.DS_Store" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".pytest_cache" -type d | xargs rm -rf
	@find . -name "*.cache" -type d | xargs rm -rf
	@find . -name "*htmlcov" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -rf sonar-scanner*
	@rm -rf build
	@rm -rf dist
	@rm -rf app.egg-info

requirements:
	@pip install -r requirements.txt

lint:
	@flake8 . --exclude=venv,migrations
	@isort --check .

isort-fix:
	@isort app

#RUN

run:
	@python -m uvicorn app.main:app --reload

test:
	@python -m pytest

test-coverage:
	@python -m pytest --cov=app --cov-report=xml --cov-report=html

migrate:
	@alembic upgrade head

populate:
	@python data_populate.py