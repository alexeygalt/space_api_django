# Simple space api 1.0

## General Information

## Install:

- Use git clone `https://github.com/alexeygalt/space_api_django.git`
- To start app use :  `docker-compose up -d`

## Check URL's:

- You can check project at with swagger : `http://localhost:8000/`
- You can  also create one test user (Send POST to `http://localhost:8000/users/`) :
        `username : test`
        `password : test`
- Use these user's options to take Token by url `'users/token/'` method POST     

## Testing:
- To install requirements : use `pip install -r requirements.txt`  or `poetry install`(first `pip install poetry`)


- Start tests : `pytest --cov`

