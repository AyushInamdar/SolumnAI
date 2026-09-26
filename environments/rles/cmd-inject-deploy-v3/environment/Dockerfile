FROM python:3.11-slim
RUN apt-get update && apt-get install -y zip && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . .
RUN python setup_builds.py
ENTRYPOINT ["python", "deploy.py"]
