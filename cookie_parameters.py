from fastapi import FastAPI, Response, Cookie

app = FastAPI()

@app.get("/set-cookie/")
def set_cookie(response: Response):
    response.set_cookie(key="username", value="john_doe", max_age=3600)
    return {"message": "Cookie set successfully"}

@app.get("/read-cookie/")
def read_cookie(username: str = Cookie(None)):
    return {"username": username}

@app.get("/delete-cookie/")
def delete_cookie(response: Response):
    response.delete_cookie(key="username")
    return {"message": "Cookie deleted"}

@app.get("/")
def read_root(user_id: str = Cookie(None), session_id: str = Cookie(None)):
    return {"user_id": user_id, "session_id": session_id}

'''
You can customize cookies with several parameters:

response.set_cookie(
    key="session_token",
    value="abc123xyz",
    max_age=86400,  # 1 day in seconds
    expires=86400,  # same as max_age but in different format
    path="/",       # cookie path
    domain=None,    # specify domain
    secure=True,    # only send over HTTPS
    httponly=True,  # not accessible via JavaScript
    samesite="lax"  # or "strict" or "none"
)
'''
@app.post("/login/")
def login(response: Response):
    response.set_cookie(key="user_id", value="12345")
    response.set_cookie(key="session_id", value="abcdef")
    return {"message": "Logged in"}