from importlib import metadata

from fastapi import FastAPI

from pyteacher.db import PyTeacherDB
from pyteacher.models import User

app = FastAPI()


@app.get("/version")
def version():
    return {"version": metadata.version("pyteacher")}


@app.post("/register")
def register(user: User):
    with PyTeacherDB() as db:
        db.add_user(user)
