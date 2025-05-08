from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class Book(BaseModel):
    title: str
    description: str | None = None
    price: float

'''
"item" parameter is a request body. it will be a JSON body of Item model

{
    "name": "Item #1",
    "description": "test" #optional
    "price": 10.00,
    "tax": 0.5 #optional
}

"name" and "price" are required, and FastAPI will throw error if they are not sent

'''
@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    
    # update Item model, add price_with_tax field if tax is not null
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    
    return item_dict

'''
Request body (item) + path parameters (item_id)
'''
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    # **item.dict() = will be unpacked 
    return {
        "item_id": item_id,
        **item.dict()
    }

'''
Request body (book) + path (book_id) + query parameters (q)
FastAPI recognized "q" as query parameter because it's not part of path parameter and Book model
'''
@app.put("/books/{book_id}")
async def update_book(book_id: int, book: Book, q: str | None = None):
    result = {
        "book_id": book_id,
        **book.dict()
    }

    if q:
        result.update({ "q": q })

    return result