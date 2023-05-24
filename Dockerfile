FROM python:3.11-slim-bullseye

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

CMD pytest --alluredir=/app/allure-results -n 5
