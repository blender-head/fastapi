from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse

class UserPreferences(BaseModel):
    theme: str = "light"
    font_size: int = 14
    language: Optional[str] = "en"

app = FastAPI()

'''
Using Pydantic Models for Cookies
'''
@app.get("/preferences/")
async def get_preferences(request: Request):
    cookies = request.cookies
    try:
        preferences = UserPreferences.parse_obj(cookies)
        return preferences
    except ValueError as e:
        return JSONResponse(
            status_code=400,
            content={"message": "Invalid cookie data", "detail": str(e)}
        )

'''
Set cookies with Pydantic model
'''
@app.post("/preferences/")
async def set_preferences(prefs: UserPreferences, response: Response):
    # Set individual cookies
    response.set_cookie(key="theme", value=prefs.theme)
    response.set_cookie(key="font_size", value=str(prefs.font_size))
    if prefs.language:
        response.set_cookie(key="language", value=prefs.language)
    
    return {"message": "Preferences set"}

'''
JSON-encoded Cookie
'''
@app.get("/preferences2/")
async def get_preferences2(request: Request):
    preferences_cookie = request.cookies.get("preferences")
    if not preferences_cookie:
        return UserPreferences()  # Return defaults
    
    try:
        return UserPreferences.parse_raw(preferences_cookie)
    except ValueError as e:
        return JSONResponse(
            status_code=400,
            content={"message": "Invalid cookie data", "detail": str(e)}
        )

@app.post("/preferences2/")
async def set_preferences2(prefs: UserPreferences, response: Response):
    response.set_cookie(
        key="preferences",
        value=prefs.json(),
        max_age=30*24*60*60,  # 30 days
        httponly=True,
        secure=True
    )
    return {"message": "Preferences set"}