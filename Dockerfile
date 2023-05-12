FROM python:3.10-slim-bullseye
ENV PYTHONBUFFERED=1

WORKDIR /notification_service

COPY . .

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root
