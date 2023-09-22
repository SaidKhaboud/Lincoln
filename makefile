# Makefile for local development

# Docker Compose command
DC=docker-compose

# Build the Docker images
build:
    docker build -t my_airflow .
    docker build -t my_postgres -f Dockerfile.postgres .

# Run Airflow and PostgreSQL locally using Docker Compose
up:
    $(DC) up -d

# Stop Airflow and PostgreSQL and remove containers
down:
    $(DC) down

# Restart Airflow and PostgreSQL containers
restart:
    $(DC) restart

# View Airflow logs
logs:
    $(DC) logs -f airflow

# Run Airflow CLI commands (e.g., airflow list_dags)
cli:
    $(DC) exec airflow airflow $(cmd)

# Open an interactive shell inside the Airflow Docker container
shell:
    $(DC) exec -it airflow /bin/bash

# Open an interactive PostgreSQL shell inside the PostgreSQL Docker container
psql:
    $(DC) exec -it postgres psql -U myuser mydatabase

# Format Python code using Black
format:
    $(DC) exec airflow black .

# Check Python code style using Pylint
style:
    $(DC) exec airflow pylint .

check-format:
    @echo "Checking code formatting with Black..."
    $(DC) exec airflow black --check .

# Check Python code style using Pylint
check-style:
    @echo "Checking code style with Pylint..."
    $(DC) exec airflow pylint --disable=C,R,W .

test:
    $(DC) exec airflow pytest tests/unit_tests