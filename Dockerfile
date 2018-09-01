FROM python:3.7.0-slim
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends \
    gdal-bin \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY src /app/
RUN pip3 install -r requirements.txt && pip3 install gunicorn

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]