FROM python:3.11.3-slim-bullseye

WORKDIR /app

COPY . .

RUN pip3 install -U pip poetry
RUN poetry config virtualenvs.create false
RUN poetry install

CMD pytest --alluredir=/app/allure-results -n 5
