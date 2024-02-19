

from passlib.context import CryptContext
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

class Settings(BaseModel):
    authjwt_secret_key: str = "secret"


@AuthJWT.load_config
def get_config():
    return Settings()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)




# def authenticate_user( username: str, password: str):
#     if not user:
#         return False
#     if not verify_password(password, user.hashed_password):
#         return False
#     return user
