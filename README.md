# Django-CRUD-Rest-Api with JWT Authentication

## Quick Start

``` bash
$ virtualenv env

# Activate venv
$ source env/bin/activate

# Install requirements
$ pip3 install -r requirements.txt

# Create DB
'NAME': 'CRUD',
'USER': 'postgres',
'PASSWORD': 'rc',
'HOST': 'localhost',

$ python manage.py makemigrations
$ python manage.py migrate

# Run Server (http://localhst:8000)
python3 manage.py runserver
```

## Endpoints

* GET ==> /api/product

* GET ==> /api/product/:id

* POST ==> /api/product

* PUT ==> /api/product/:id

* DELETE ==> /api/product/:id

## For Search

* GET ==> /api/product/?pname=<yoursearch>

## Obtain Jwt Token

* POST ==> api-token-auth/
