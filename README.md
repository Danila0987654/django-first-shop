# My first django shop

## Getting started
--------

1. First of all create .env file in core folder and put this with your settings:
***
    SECRET_KEY=

    ENGINE=
    NAME=
    USER=
    PASSWORD=
    HOST=
    PORT=
***
2. Create venv, activate it and upgrade pip:
***
    python3 -m venv venv
    . ./venv/bin/activate
    pip install -U pip

***
3. Migrate db
***
    python manage.py makemigrations
***
4. Run Server
***
    python manage.py runserver
***