from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from pydantic.generics import GenericModel
from typing import Union, Generic, TypeVar

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

'''
Basic Return Type Annotations
'''
@app.get("/items/{item_id}")
async def read_item(item_id: int) -> dict:
    return {"item_id": item_id, "name": "Example Item"}

'''
Using Pydantic Models
'''
@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item

'''
Primitive types
'''

'''
int
'''
@app.get("/count")
async def get_count() -> int:
    return 42

'''
Lists
'''
@app.get("/items2")
async def read_items2() -> list[Item]:
    return [Item(name="Item 1", price=10.00), Item(name="Item 2", price=5.00)]

'''
Response objects (for headers, cookies, etc.)
'''
@app.get("/custom")
async def custom_response() -> Response:
    content = "Hello World"
    return Response(content=content, media_type="text/plain")

'''
Union types (multiple possible return types)
'''
@app.get("/item-or-error")
async def get_item_or_error(item_id: int) -> Union[Item, dict]:
    if item_id == 0:
        return {"error": "Item not found"}
    return Item(name="Example", price=9.99)

'''
Status codes with responses
'''
@app.post(
    "/items3/",
    response_model=Item,
    status_code=status.HTTP_201_CREATED
)
async def create_item2(item: Item) -> Item:
    return item

T = TypeVar('T')

class ResponseModel(GenericModel, Generic[T]):
    data: T
    success: bool
    message: str | None = None

'''
Generic responses
'''
@app.get("/items4/{item_id}")
async def read_item4(item_id: int) -> ResponseModel[Item]:
    return ResponseModel(
        data=Item(name="Example", price=9.99),
        success=True
    )