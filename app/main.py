from fastapi import FastAPI, HTTPException, Depends, Query
from databases import Database
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import init_db, SessionLocal,  Tasks, Users, Types
from fastapi_jwt_auth import AuthJWT
from app.auth import verify_password, get_password_hash, User

app = FastAPI()

init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World1"}


@app.post('/login')
def login(username: str, password:str , Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    current_user: Users = db.query(Users).filter(Users.username == username).first()
    if not verify_password(password, current_user.password):
        raise HTTPException(status_code=401,detail="Bad username or password")

    # subject identifier for who this token is for example id or username from database
    access_token = Authorize.create_access_token(subject=username)
    return {"access_token": access_token}

@app.get('/user')
def user(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()
    return {"user": current_user}

@app.post("/signup")
def signup(username: str, password:str , db: Session = Depends(get_db)):
    # Check if the username already exists
    existing_user = db.query(Users).filter(Users.username == username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    passwordHash = get_password_hash(password)

    new_user = Users(username=username, password=passwordHash)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {new_user}

@app.post("/tasks")
def create_task(title: str, description: str, type_id: str, db: Session = Depends(get_db)):
    new_task = Tasks(title=title, description=description, type_id=type_id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@app.post("/types")
def create_task(label: str, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    new_type = Types(label=label)
    db.add(new_type)
    db.commit()
    db.refresh(new_type)
    return new_type

@app.get("/tasks")
def create_task( db: Session = Depends(get_db)):
    tasks = db.query(Tasks).all()
    return tasks

@app.get("/tasks/{task_id}")
def create_task(task_id: str ,  db: Session = Depends(get_db)):
    task = db.get(Tasks, task_id)
    return task

