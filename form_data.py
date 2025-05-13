from typing import Annotated

from fastapi import FastAPI, Form

app = FastAPI()

'''
You must install python-multipart for form data handling
Form data is sent with application/x-www-form-urlencoded or multipart/form-data content types.
'''
@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}