
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException

POSTGRES_USER=os.getenv('POSTGRES_USER', '')
POSTGRES_PASSWORD=os.getenv('POSTGRES_PASSWORD', '')
POSTGRES_SERVER=os.getenv('POSTGRES_SERVER', '')
POSTGRES_DB=os.getenv('POSTGRES_DB', '')


DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Types(Base):
    __tablename__ = "types"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String, index=True)


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, unique=True)
    description = Column(String)
    type_id = Column(Integer, ForeignKey('types.id'), index=True)
    type = relationship("Types", back_populates="tasks")

Types.tasks = relationship("Tasks", back_populates="type")


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True)
    password = Column(String)

def init_db():
    Base.metadata.create_all(bind=engine)