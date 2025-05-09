from fastapi import FastAPI
from typing import Annotated, Literal
from pydantic import BaseModel, Field

app = FastAPI()

class FilterParams(BaseModel):
    limit: int = Field(100, gt=0; le=1000)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []

'''
FastAPI will extract the data for each field from the query parameters in the request and give you the Pydantic model you defined
'''
@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query