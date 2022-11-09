# Sonar

Tech challenge for SonarHealth.
Important note: you requested the usage of at least one design pattern. I'm using decorator pattern:
https://en.wikipedia.org/wiki/Decorator_pattern

- @login_required
- @require_http_methods

Both provided by Django.

## Technology Stack

- Python 3.10
- Django 4

## Installation and running

### Without Docker

- Create virtual environment and activate it. Example: `virtualenv venv`
- Enter environment: Example: `venv\Scripts\activate`
- Install requirements:
    - Development: `pip install -r requirements/development.txt`
    - Production: `pip install -r requirements/production.txt`
- Create `.env` file at project root. File .env-example is provided as a guide of this file's content.
  Make sure you copy your SECRET_KEY there.
- Generate migration files: `python manage.py makemigrations`
- Run migrations: `python manage.py migrate`. Heads up: this will take some time since it will
  insert the test data, watch the console for progress.
- Create superuser: `python manage.py createsuperuser`
  This is the user you will use to log in and create new users if needed.
  To create new users, go to http://localhost:8000/admin and login with the superuser credentials.
- Run using `python manage.py runserver`

### With Docker

- Create `.env` file at project root. File .env-example is provided as a guide of this file's content.
  Make sure you copy your SECRET_KEY there.
- Make sure to have Docker running on your system (in mac or windows, you should have docker desktop running).
- Run using: `docker-compose up`. Heads up: this will take some time since it will
  insert the test data, watch the console for progress.
- Create superuser: 
  - SSH to container.
  - Run `python manage.py createsuperuser`
  This is the user you will use to log in and create new users if needed.
  To create new users, go to http://localhost:8000/admin and login with the superuser credentials.
