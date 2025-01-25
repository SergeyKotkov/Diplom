FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY .env /app/

COPY task_tracker /app/task_tracker

# Команда для запуска приложения с использованием manage.py
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
