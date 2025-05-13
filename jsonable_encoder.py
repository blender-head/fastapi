from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

'''
The jsonable_encoder is particularly useful when you need to ensure your data is JSON-serializable before operations like:

- Returning responses
- Storing in databases
- Sending to external APIs
- Caching data
'''
@app.post("/items/")
async def create_item(item: Item):
    # Convert the Pydantic model to a dict with JSON-compatible types
    json_compatible_item_data = jsonable_encoder(item)
    return {"item": json_compatible_item_data}