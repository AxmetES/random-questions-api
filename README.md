# Test_FastAPI_PostgreSQL_Docker

## Technologies
The project makes use of the following technologies:

Python 3.11.4

Docker version 24.0.5

Docker Compose version v2.17.2

Python 3.11.4

FastAPI 0.95.2

Sqlalchemy 2.0.15

PostgreSQL: 16.0

## Getting started

#### Clone project:

``` git clone https://gitlab.com/me4533521/test_fastapi_postgresql_docker.git```

#### Move to directory:

add .env file, for example:
```
POSTGRES_PASSWORD = admin
POSTGRES_USER = admin
POSTGRES_DB = db
POSTGRES_HOST = db

QUESTIONS_URL = https://jservice.io/api/random?count={}
```

```cd test_fastapi_postgresql_docker```

#### Build Docker Compose:

```sudo docker-compose build```

#### Run Docker Compose:

```sudo docker-compose up```

## Using

Run POST request on ur Postman:

```http://127.0.0.1:8000/questions_num/5```

or user fast api swagger:

```/api/random```

## logging:

```sudo journalctl CONTAINER_NAME=test_fastapi_postgresql_docker-app-1 -f```

## License
For open source projects, say how it is licensed.