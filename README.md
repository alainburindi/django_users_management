# Users_management

[![Django CI](https://github.com/alainburindi/django_users_management/actions/workflows/django.yml/badge.svg)](https://github.com/alainburindi/django_users_management/actions/workflows/django.yml)

[![codecov](https://codecov.io/gh/alainburindi/django_users_management/branch/main/graph/badge.svg?token=Q4IHETDJPC)](https://codecov.io/gh/alainburindi/django_users_management)

## Installing

```shell
    git clone https://github.com/alainburindi/django_users_management.git
    cd django_users_management
    python3 -m venv venv
    source venv/bin/activate
```

- Create .env and copy paste the environment variable from `.env_example` file that's already existent in the root directory

- Run the following commands

```shell
    pip install -r requirements.txt
```

- Create a postgreSQL database called `django_users_management` or any other name and provide the credentials(DB_NAME, DB_USER, DB_PASSWORD) in your `.env` file.

- Run the following commands to make the database migrations.

```shell
    python3 manage.py migrate
```

### Running the application

Run the command below to run the application locally.

```shell
  python3 manage.py runserver
```

### Running the tests

Run the command below to run the tests for the application.

```shell
    python manage.py test
```

## Endpoints

### Users

`GET /users`
Get all users list

`POST /users`

ceate a user

```source-json
{
 "name": "Alain Burindi",
 "email": "al3@test.com",
 "password": "Password@123",
 "role": "user"
}
```

`DELETE /users/{id}`

delete a user

## Swagger documentation

<https://umangement.herokuapp.com/swagger>

## Deployment

Stagging link on heroku: [click here](https://umangement.herokuapp.com)
