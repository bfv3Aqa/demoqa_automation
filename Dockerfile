FROM python:3.9-slim-bullseye

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

CMD pytest --allure-dir=/app/allure-results test/elements_test.py