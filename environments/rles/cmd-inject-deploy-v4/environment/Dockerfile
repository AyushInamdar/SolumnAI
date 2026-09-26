FROM python:3.11-slim
RUN pip install flake8 --no-cache-dir
WORKDIR /app
COPY . .
RUN python setup_builds.py
ENTRYPOINT ["python", "deploy.py"]
