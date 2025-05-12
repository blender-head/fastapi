from fastapi import FastAPI, Header, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Define your Pydantic model for headers
class MyHeaders(BaseModel):
    user_agent: Optional[str] = None
    content_language: Optional[str] = "en"
    x_custom_header: Optional[str] = None

class AuthHeaders(BaseModel):
    authorization: str = Header(..., alias="Authorization")
    x_api_key: str = Header(..., alias="X-API-Key")

    def validate(self):
        if not self.authorization.startswith("Bearer "):
            raise HTTPException(status_code=400, detail="Invalid auth scheme")
        if len(self.x_api_key) != 32:
            raise HTTPException(status_code=400, detail="Invalid API key")

'''
Using Pydantic Models for Headers in FastAPI
'''
@app.get("/")
async def read_root(headers: MyHeaders = Header(...)):
    return {"headers": headers.dict()}

'''
Using a Pydantic Model with Dependency Injection
'''
async def get_headers(
    authorization: str = Header(..., alias="Authorization"),
    x_api_key: str = Header(..., alias="X-API-Key")
) -> AuthHeaders:
    headers = AuthHeaders(authorization=authorization, x_api_key=x_api_key)
    headers.validate()
    return headers

@app.get("/protected")
async def protected_route(headers: AuthHeaders = Depends(get_headers)):
    return {"message": "Access granted", "headers": headers.dict()}