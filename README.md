# Sonar

Tech challenge for SonarHealth

## Technology Stack

-   Python 3.10
-   Django 4

## Installation and running

### Without Docker

- Create virtual environment and activate it. Example: `virtualenv venv`
- Enter environment: Example: `venv\Scripts\activate`
- Install requirements:
    -   Development: `pip install -r requirements/development.txt`
    -   Production: `pip install -r requirements/production.txt`
- Create `.env` file at project root. File .env-example is provided as a guide of this file's content.
Make sure you copy your SECRET_KEY there.
- Generate migration files: `python manage.py makemigrations`
- Run migrations: `python manage.py migrate`. Heads up: this will take some time since it will
insert the test data, watch the console for progress.
- Create superuser: `python manage.py createsuperuser`
This is the user you will use to log in and create new users if needed.
To create new users, go to http://localhost:8000/admin and login with the superuser credentials.
- Run using `python manage.py runserver`


## WIP

[//]: # (### With Docker)

[//]: # ()
[//]: # (-   Create `docker-compose.yml` &#40;you may use docker-compose.example.yml as reference&#41;)

[//]: # (-   Make sure to have Docker running on your system &#40;in mac, you should have docker icon in top menu&#41;.)

[//]: # (-   Run using: `docker-compose up`)

[//]: # ()
[//]: # (## Testing)

[//]: # ()
[//]: # (### Without Docker)

[//]: # ()
[//]: # (-   Run the tests with `python manage.py test`)

[//]: # (- Get test coverage with:)

[//]: # (  - `coverage run --source='.' manage.py test`)

[//]: # (  - `coverage report --skip-covered --show-missing`)

[//]: # ()
[//]: # (### With Docker)

[//]: # ()
[//]: # (-   Make sure your service name for the django app is `web` or change it accordingly in the following commands.)

[//]: # (-   Run the tests with `docker-compose run web python manage.py test`)

[//]: # (-   Get test coverage with:)

[//]: # (    -   `docker-compose run web coverage run --source='.' manage.py test`)

[//]: # (    -   `docker-compose run web coverage report --skip-covered --show-missing`)
