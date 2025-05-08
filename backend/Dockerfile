# Dockerfile para Django + Gunicorn en Google Cloud Run
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Variables de entorno típicas para Cloud Run
ENV PORT=8080

# Comando de inicio para Gunicorn
CMD ["gunicorn", "config.wsgi:application", "--bind", ":8080"]
