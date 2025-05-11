from fastapi import FastAPI, Path, Body
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None
    price: float
    tax: float | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None

'''
item body is optional. single body pararameter is like this
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}
'''
@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None
):
    results = {
        "item_id": item_id
    }

    if q:
        results.update( {"q": q} )

    if item:
        results.update( { "item": item } )

    return results

'''
multiple body parameter:
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    }
}
'''
@app.put("/user_item/{user_id}")
async def save_user_item(
    user_id: int,
    item: Item,
    user: User
):
    results = {
        "user_id": user_id,
        "item:": item,
        "user": user
    }

    return results

'''
add new body "importance"
{
    "product_id": 10,
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    },
    "importance": 5
}
'''
@app.put("/product_user/{product_id}")
async def save_user_product(
    product_id: int,
    item: Item,
    user: User,
    importance: Annotated[int, Body()]
):
    results = {"product_id": product_id, "item": item, "user": user, "importance": importance}
    return results

'''
add "q" as optional query parameter
'''
@app.put("/employee_item/{employee_id}")
async def save_employee_item(
    *,
    employee_id: int,
    item: Item,
    user: User,
    importance: Annotated[int, Body(gt=0)],
    q: str | None = None,
):
    results = {"employee_id": employee_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results

'''
item: Annotated[Item, Body(embed=True)]) is adding "item" key on single Item body
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
}
'''
@app.put("/books/{book_id}")
async def update_book(book_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"book_id": book_id, "item": item}
    return results
