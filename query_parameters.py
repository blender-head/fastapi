from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {
        "item_name": "Foo"
    },
    {
        "item_name": "Bar"
    },
    {
        "item_name": "Baz"
    }
]

'''
When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters

skip and limit are query parameters as they don't declared in the url (path parameter), and they are optional because they have default value

So, going to the URL:

http://127.0.0.1:8000/items/

would be the same as going to:

http://127.0.0.1:8000/items/?skip=0&limit=10

But if you go to, for example:

http://127.0.0.1:8000/items/?skip=20

The parameter values in your function will be:
- skip=20: because you set it in the URL
- limit=10: because that was the default value
'''
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

'''
q query parameter is optional parameter with default value of None
'''
@app.get("/product/{product_id}")
async def get_product(product_id: int, q: str = None):
    if q:
        return {
            "product_id": product_id,
            "q": q
        }

    return {
        "product_id": product_id
    }

'''
Query parameter type conversion
short=1 (True)
short=True (True)
short=on (True)
short=yes (True)
'''
@app.get("/book/{book_id}")
async def get_book(book_id: int, q: str | None = None, short: bool = False):
    book = { "book_id": book_id}

    if q:
        book.update({ "q": q})

    if not short:
        book.update({"description": "This is an amazing item that has a long description"})

    return book

'''
Multiple path and query parameters
path parameters = user_id & item_id
query parameters = q & short (optional)
url: http://127.0.0.1:8000/users/100/items/1?short=off&q=test
'''
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {
        "item_id": item_id,
        "owner_id": user_id
    }

    if q:
        item.update({ "q": q })

    if not short:
        item.update({"description": "This is an amazing item that has a long description"})

    return item

'''
continent is a required query parameter
'''
@app.get("/country/{country_name}")
async def get_country(country_name: str, continent: str):
    return {
        "country": country_name,
        "continent": continent
    }

