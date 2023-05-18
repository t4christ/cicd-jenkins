FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd -r django && useradd --no-log-init -r -g django t4cdigital

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN chown -R t4cdigital /app
USER t4cdigital

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "t4c.wsgi"]
