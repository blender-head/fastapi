from fastapi import FastAPI
from pydantic import BaseModel, SecretStr
from typing import Union

app = FastAPI()

# Request model (what the client sends)
class ItemCreate(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# Response model (what the client receives)
class ItemResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float

# Database model (what you store internally)
class ItemDB(ItemResponse):
    tax: float
    owner_id: int

'''
Basic Example with Separate Request/Response Models (request = ItemCreate, response = ItemResponse)
'''
@app.post("/items/", response_model=ItemResponse)
async def create_item(item: ItemCreate):
    # Convert request model to DB model
    db_item = ItemDB(**item.dict(), id=1, owner_id=1, tax=item.tax or 0.0)
    
    # Here you would typically save to database
    # ...
    
    # Convert DB model to response model (excludes sensitive fields)
    return db_item

class ItemBase(BaseModel):
    name: str
    description: str | None = None
    price: float

class ItemCreate2(ItemBase):
    tax: float | None = None

class ItemResponse2(ItemBase):
    id: int

class ItemDB2(ItemResponse):
    tax: float
    owner_id: int

@app.get("/items/{item_id}", response_model=ItemResponse2)
async def read_item(item_id: int):
    # Return an ItemDB2 instance - FastAPI will convert to ItemResponse2
    return ItemDB2(id=item_id, name="Foo", price=42.0, tax=0.2, owner_id=1)

class ErrorResponse(BaseModel):
    error: str
    code: int

'''
Multiple Response Models for One Route
'''
@app.get("/items2/{item_id}", response_model=Union[ItemResponse, ErrorResponse])
async def read_item2(item_id: int):
    if item_id == 0:
        return ErrorResponse(error="Invalid ID", code=400)
    return ItemResponse(id=item_id, name="Foo", price=42.0)

class UserCreate(BaseModel):
    username: str
    password: SecretStr

class UserResponse(BaseModel):
    username: str
    # password is excluded from response

'''
Response Model with Excluded Fields (password won't be included in the response)
'''
@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate):
    return user  # FastAPI will automatically exclude the password