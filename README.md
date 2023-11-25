# Bank API - Backend
## Description
This is a simple bank API that allows you to create users, accounts and transactions (deposits and withdrawals).

## Requirements
- Python 3.10
- Docker
- Docker Compose

## Installation

Run the following commands to install the project on local machine:

```shell
pip install poetry
poetry install
docker-compose up -d
DB_DRIVER=postgresql uvicorn main:app --reload
```

Or you can uncomment the following lines in the `docker-compose.yml` file:

```yaml
#  fastapi:
#    build:
#      context: .
#      dockerfile: Dockerfile
#    ports:
#      - "8000:8000"
#    volumes:
#      - .:/app
#    command: uvicorn app.main:app --reload --host
```

Then run the following command:

```shell
docker-compose up -d
```

## Usage

You can access the API documentation at http://localhost:8000/docs

## Tests

To run the tests, run the following command:

```shell
pytest
```

## Project Structure

This project follows the [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) principles.

The project structure is as follows:

- domain: Contains the business entities of the application

- usecase: Contains the use cases of the application

- repository: Contains the interfaces of the repositories

- infrastructure: Contains the implementations of the repositories. In this case, the database implementation is postgresql

    And in the infrastructure folder, we have the provider to adapting create the database to the repository interface based on
    the environment variable `DB_DRIVER`

- setting: Contains the settings of the application

- app: contains the application layer. In this case, the API endpoints functions



