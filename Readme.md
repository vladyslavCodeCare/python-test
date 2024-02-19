alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
docker-compose up --build -d
pip3 freeze > requirements.txt
