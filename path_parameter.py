from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/product/{product_id}", description="You can declare path parameters or variables with the same syntax used by Python format strings")
async def read_product(product_id):
    return {
        "product_id": product_id
    }


@app.get("/items/{item_id}", description="Path parameters with types")
async def read_item(item_id: int):
    return {
        "item_id": item_id
    }

'''
Order matters

When creating path operations, you can find situations where you have a fixed path. Like /users/me, let's say that it's to get data about the current user.
And then you can also have a path /users/{user_id} to get data about a specific user by some user ID. Because path operations are evaluated in order, you need to make sure 
that the path for /users/me is declared before the one for /users/{user_id}
'''
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

'''
Predefined values

If you have a path operation that receives a path parameter, but you want the possible valid path parameter values to be predefined, you can use a standard Python Enum
Will throw error if model name other than "alexnet", "resnet" or "lenet"
'''
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
