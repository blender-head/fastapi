from fastapi import FastAPI, Request, Header, Response
from typing import Optional

app = FastAPI()

'''
Accessing Headers via Request Object
'''
@app.get("/")
async def read_headers(request: Request):
    headers = request.headers
    user_agent = headers.get("user-agent")
    return {"User-Agent": user_agent}

'''
Using Header Parameters

curl --location 'http://127.0.0.1:8000/header-test' --header 'X-Token: 12345'
'''
@app.get("/header-test")
async def read_headers2(
    user_agent: str = Header(None),
    x_token: str = Header(None, alias="X-Token")
):
    return {"User-Agent": user_agent, "X-Token": x_token}

'''
Getting All Headers
'''
@app.get("/get-all-headers")
async def get_all_headers(request: Request):
    return dict(request.headers)

'''
Setting Response Headers
'''
@app.get("/custom-header")
async def set_custom_header(response: Response):
    response.headers["X-Custom-Header"] = "CustomValue"
    return {"message": "Hello World"}

'''
Using Custom Header Classes
'''
@app.get("/read-header")
async def read_header(x_token: Optional[str] = Header(None)):
    if not x_token:
        return {"error": "X-Token header missing"}
    return {"token": x_token}