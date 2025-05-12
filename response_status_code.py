from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

'''
In Response Status Codes
'''
@app.post("/items-example/", status_code=status.HTTP_201_CREATED)
async def create_item():
    return {"message": "Item created"}

'''
In Direct Responses
'''
@app.get("/protected/")
async def protected_route():
    return JSONResponse(
        content={"message": "Unauthorized"},
        status_code=status.HTTP_401_UNAUTHORIZED
    )

@app.get("/admin/")
async def admin_panel():
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Admin access required"
    )

items = {"foo": "The Foo Wrestlers"}

@app.get("/items/{item_id}", status_code=status.HTTP_200_OK)
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    return {"item": items[item_id]}

@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(item_id: str, item: str):
    if item_id in items:
        return JSONResponse(
            content={"message": "Item already exists"},
            status_code=status.HTTP_400_BAD_REQUEST
        )
    items[item_id] = item
    return {"message": "Item created successfully"}