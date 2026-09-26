FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN python setup_builds.py

ENTRYPOINT ["python", "deploy.py"]
