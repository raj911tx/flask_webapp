# syntax=docker/dockerfile:1
FROM python:3.9-alpine
WORKDIR /blogy
ENV FLASK_APP=blogy
ENV FLASK_ENV='development'
RUN apk add --no-cache gc musl-dev linux-headers
COPY setup.py setup.py
RUN pip install -e .
EXPOSE 5000
COPY . .
CMD ["flask","init-db"]
CMD ["flask","run"]
