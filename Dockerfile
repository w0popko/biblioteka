FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app
COPY ./.env /app

ENV PYTHONPATH=/app

WORKDIR /
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["sleep", "1000000"]