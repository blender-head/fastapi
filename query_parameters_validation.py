from typing import Annotated
from fastapi import FastAPI, Query
from pydantic import AfterValidator
import random

app = FastAPI()

'''
"q" query parameter is optional, but if user supply it, FastAPI will do a validation of the length
in example below, if "q" is available, the value should be a minimal of 1 and a maximum of 3
'''
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=1, max_length=3)] = None):
    results = {
        "items": [
            {
                "item_id": "Foo"
            }, 
            {
                "item_id": "Bar"
            }
        ]
    }

    if q:
        results.update( { "q": q})

    return results

'''
"q" query parameter is optional, but if user supply it, FastAPI will do a validation of the length and value
in example below, if "q" is available, the value must be "test"
'''
@app.get("/products/")
async def get_products(
    q: Annotated[
        str | None, Query(min_length=3, max_length=50, pattern="^test$")
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

'''
"q" query parameter is optional, but have default value
'''
@app.get("/books/")
async def get_books(q: Annotated[str, Query(min_length=3)] = "fixedquery"):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

'''
"q" query parameter is now required, with a min length of 3
'''
@app.get("/rooms/")
async def get_rooms(q: Annotated[str, Query(min_length=3)]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

'''
"q" query parameter is now required. this endpoint will accept any string that have a minimum of 3 characters or will accept a None (http://127.0.0.1:8000/employees/?q=None)
'''
@app.get("/employees/")
async def get_employees(q: Annotated[str | None, Query(min_length=3)]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

'''
"q" query paramater is optional, but the endpoint will accept multiple "q" query paramaters (http://127.0.0.1:8000/companies/?q=foo&q=bar)
'''
@app.get("/companies/")
async def get_companies(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items

'''
"q" query paramater is optional, could be multiple, and have multiple default values
'''
@app.get("/shows/")
async def get_shows(q: Annotated[list[str], Query()] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items

'''
"q" is aliased to be "item-query" (http://127.0.0.1:8000/systems/?item-query=test)
'''
@app.get("/systems/")
async def get_system(q: Annotated[str | None, Query(alias="item-query")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

'''
using Query to add more metadata to Swagger or OpenAPI doc
'''
@app.get("/people/")
async def get_people(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}


def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id


'''
apply custom validator after Query validation
'''
@app.get("/library/")
async def get_library(
    id: Annotated[str | None, Query(min_length=3,max_length=50), AfterValidator(check_valid_id)] = None,
):
    if id:
        item = data.get(id)
    else:
        id, item = random.choice(list(data.items()))
    return {"id": id, "name": item}