FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libc-dev

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY .env .env


COPY . /app/

CMD ["python", "app.py"]


