from fastapi import FastAPI, status
from typing import List
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

'''
These configurations help you:

- Control API behavior
- Improve documentation
- Set proper status codes
- Organize your API endpoints
- Maintain backward compatibility

The configurations are also reflected in the automatically generated OpenAPI schema and interactive docs (Swagger UI and ReDoc).
'''
@app.post(
    "/items/",
    response_model=Item, #for output data validation and documentation
    status_code=status.HTTP_201_CREATED,
    tags=["items"], # for API documentation grouping
    summary="Create a new item",
    response_description="The created item",
    deprecated=False,
    operation_id="create_item_v1" #for explicit OpenAPI operationId
)
async def create_item(item: Item):
    return item