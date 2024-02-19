# Dockerfile

FROM python:3.8-slim

WORKDIR /project

EXPOSE 3001

RUN apt-get update \
    && apt-get -y install libpq-dev gcc
#     && pip install psycopg2
COPY ./alembic /project/alembic
COPY ./app /project/app
COPY alembic.ini /project/alembic.ini
# COPY . .
COPY requirements.txt /project/requirements.txt
RUN pip3 install -r requirements.txt



CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3001"]
# # Dockerfile

# FROM python:3.8-slim

# WORKDIR /project

# EXPOSE 3001

# RUN apt-get update \
#     && apt-get -y install libpq-dev gcc
# #     && pip install psycopg2
# COPY ./alembic /project/alembic
# COPY ./app /project/app
# COPY alembic.ini /project/alembic.ini

# COPY requirements.txt /project/requirements.txt
# RUN pip3 install -r requirements.txt

# COPY . .

# ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3001", '--reload']