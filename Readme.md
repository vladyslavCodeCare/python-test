### Requirements

Docker

### To start

Create .env with next vals POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_SERVER, POSTGRES_DB.
Then run:

```
  docker-compose up --build -d
```

### Migrations

```
  alembic revision --autogenerate -m "[message]"
  alembic upgrade head
```

To set new requirements:

```
  pip3 freeze > requirements.txt
```
