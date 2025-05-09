from typing import Annotated
from fastapi import FastAPI, Path, Query

app = FastAPI()

'''
validate path parameter to >= 1
'''
@app.get("/items/{item_id}")
async def read_items(item_id: Annotated[int, Path(title="The ID of the item to get", ge=1)], q: str):
    results = {"item_id": item_id}
    
    if q:
        results.update({"q": q})
    
    return results

'''
validate path parameter to > 0 and <= 1000
'''
@app.get("/products/{product_id}")
async def read_products(
    product_id: Annotated[int, Path(title="The ID of the item to get", gt=0, le=1000)],
    q: str,
):
    results = {"product_id": product_id}
    if q:
        results.update({"q": q})
    return results

'''
validate float path parameter
'''
@app.get("/shoes/{shoe_id}")
async def read_shoes(
    shoe_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    size: Annotated[float, Query(gt=0, lt=10.5)],
    q: str | None = None,
):
    results = {"shoe_id": shoe_id}
    if q:
        results.update({"q": q})
    if size:
        results.update({"size": size})
    return results
