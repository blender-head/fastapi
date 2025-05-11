from typing import List, Union
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

'''
add validation tu url field to be valid URL
'''
class Image(BaseModel):
    url: HttpUrl
    name: str

'''
"tags" body parameter is an array of any value
"num" body parameter is an array os string
"size body parameter is a unique set
"item" body parameter now can contain Image data
"images" contain array of Image

{
    "name": "Foo",
    "description": "The pretender",
    "price": 0,
    "tax": 3.2,
    "tags": ["1","tes",3],
    "num": [1,2,3,3]
    "size": ["1","2","3"]
    "image": {
        "url": "http://google.com",
        "name": "name"
    },
    "images": [
        {
            "url": "http://google.com",
            "name": "name"
        },
        {
            "url": "http://google.com",
            "name": "name"
        }
    ]
}
'''
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list = []
    num: List[str] = []
    size: set[str] = set()
    image: Image | None = None
    images: list[Image] | None = None

'''
"items" contain array of Item

{
    "name": "test",
    "description": "description",
    "price": 10.5
    "items"[
        {
            "name": "test",
            "description": "description",
             "price": 10.5
        }
    ]
}
'''
class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer

'''
multiple image body parameter define in method parameter
'''
@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
    return images

'''
Bodies of arbitrary dicts

{
    "10": 10
}
'''
@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    return weights
