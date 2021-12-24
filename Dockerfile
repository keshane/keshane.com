# syntax=docker/dockerfile:1

FROM python:3.6

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

COPY . .

RUN touch db.sqlite3
RUN python manage.py migrate --no-input
CMD ["gunicorn", "keshane_com.wsgi", "-b", "0:8000", "--reload"]
