from typing import Annotated

from fastapi import FastAPI, Form
from pydantic import BaseModel, SecretStr

app = FastAPI()


class FormData(BaseModel):
    username: str
    password: SecretStr


@app.post("/login/")
async def login(data: Annotated[FormData, Form()]):
    return data