# My first django shop

## Getting started
--------

1. First of all create .env file and put this with your settings:
***
    SECRET_KEY=

    ENGINE_DB=
    NAME_DB=
    USER_DB=
    PASSWORD_DB=
    HOST_DB=
    PORT_DB=
***
2. Create venv, activate it and upgrade pip:
***
    python3 -m venv venv
    . ./venv/bin/activate
    pip install -U pip

***
3. Migrate db
***
    python manage.py migrate
***
4. Create admin user
***
    python manage.py createsuperuser
***
5. Run Server
***
    python manage.py runserver
***
Run tests
***
    ./manage.py test
***