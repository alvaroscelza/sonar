FROM python:3.9.1

ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
RUN pip install -r requirements/base.txt
