# <<Project Name>>

<<Project description.>>

## Technology Stack

-   Python 3.10.3
-   Django 4

## Installation and running

### Without Docker

- Create virtual environment and activate it. Example: `virtualenv venv`
- Enter environment: Example: `venv\Scripts\activate`
- Install requirements:
    -   Development: `pip install -r requirements/development.txt`
    -   Production: `pip install -r requirements/production.txt`
- Install pre-commit hooks feature: `pre-commit install`
- Create `.env` file at project root. File .env-example is provided as a guide of this file's content. 
Make sure you copy your SECRET_KEY there.
- Generate migration files: `python manage.py makemigrations`
- Run migrations: `python manage.py migrate`
- Create superuser: `python manage.py createsuperuser`
- Run using `python manage.py runserver`
- To see the documentation diagrams you require [Graphviz](https://graphviz.org/).

### With Docker

-   Create `docker-compose.yml` (you may use docker-compose.example.yml as reference)
-   Make sure to have Docker running on your system (in mac, you should have docker icon in top menu).
-   Run using: `docker-compose up`

## Testing

### Without Docker

-   Run the tests with `python manage.py test`
- Get test coverage with:
  - `coverage run --source='.' manage.py test`
  - `coverage report --skip-covered --show-missing`

### With Docker

-   Make sure your service name for the django app is `web` or change it accordingly in the following commands.
-   Run the tests with `docker-compose run web python manage.py test`
-   Get test coverage with:
    -   `docker-compose run web coverage run --source='.' manage.py test`
    -   `docker-compose run web coverage report --skip-covered --show-missing`

### Using Swagger for API documentation
- Run project
- Go to `<project URL>/api/<API version>/swagger/`, example: `http://127.0.0.1:8000/api/v1/swagger/` for localhost
- There you can see all endpoints. To use them you have to get the JWT token using the SESSIONS endpoint:
  - Search in Swagger for the `POST /sessions/` endpoint.
  - Use it. You need to provide with a valid `username` and `password` credentials pair.
  - You will receive two tokens: one for `refresh`, the other for `access`. Copy the `access` token in the clipboard.
  - Scroll all up in the Swagger page, find the button called `Authorize`, it has a lock image attached to it. Click it.
  - You will see a modal small window with the information of the type of authorization that is going to be used, in this case JWT.
  - You will also see a lonely input with the `Value:` label. In this input you have to insert `Bearer <access token copied in the clipboard>`.
  Example with fake token: `Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1N` (bear in mind that the real token tends to be far longer that this).
  - Click `Authorize` and now all endpoints should start working.
  - Have fun.
