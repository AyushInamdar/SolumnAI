FROM python:3.11-slim
RUN apt-get update && apt-get install -y tmux asciinema && rm -rf /var/lib/apt/lists/*
RUN pip install flake8 --no-cache-dir
WORKDIR /app
COPY . .
RUN python setup_builds.py
