FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

RUN pip install gunicorn
COPY .env /app/

COPY . /app/

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "task_tracker.wsgi:application"]
