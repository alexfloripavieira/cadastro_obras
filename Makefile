NAMEIMAGE=neoway
PYTHON_VERSION := 3.10.0
PROJECT_NAME := neoway
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)
DATABASE_PASS := postgres

create-venv: .create-venv setup

.create-venv: 
	pyenv install -s $(PYTHON_VERSION)
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)


.pip:
	pip install pip --upgrade

setup: .pip
	pip install -U setuptools
	pip install -r requirements.txt

# Postgres Local
run-postgres:
	docker start neoway-postgres 2>/dev/null || docker run --name neoway-postgres -p 5432:5432 -e POSTGRES_PASSWORD='$(DATABASE_PASS)' -d postgres:10-alpine

check:
	pytest -vv -x --cov=apps --cov-report html:coverage --cov-fail-under=70


