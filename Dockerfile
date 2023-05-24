FROM python:3.11-slim-bullseye

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
