FROM python:3.11.3-slim-bullseye

ENV POETRY_VERSION=1.3.1

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR /app
COPY poetry.lock pyproject.toml /app/

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY . /app
WORKDIR /app

COPY . .

CMD pytest --alluredir=/app/allure-results -n 5
