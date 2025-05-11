# Fast API
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+, based on standard Python type hints. It is designed to be easy to use, highly efficient, and capable of producing high-performance APIs with minimal code.

## Key Features of FastAPI:
1. Fast & High Performance
    - Built on top of Starlette (for web routing) and Pydantic (for data validation).
    - One of the fastest Python frameworks, comparable to Node.js and Go (thanks to ASGI support).
2. Automatic API Documentation
    - Generates Swagger UI (/docs) and ReDoc (/redoc) automatically.
    - Helps developers test APIs interactively.
3. Type Hints & Data Validation
    - Uses Python type hints to define request/response models.
    - Validates data automatically using Pydantic.
4. Asynchronous Support (Async/Await)
    - Supports async and await for handling concurrent requests efficiently.
5. Dependency Injection
    - Simplifies managing dependencies (e.g., database connections, authentication).
6. Standards-Based
    - Fully compatible with OpenAPI (formerly Swagger) and JSON Schema.

# Installation

```
pip install fastapi uvicorn
```

# Run FastAPI Application

## Run App Using uvicorn

```
uvicorn main:app
uvicorn main:app --port=8080
uvicorn main:app --reload
```

## Run App Using fastapi[standard]

```
pip install fastapi[standard]
fastapi dev main.py
```

# Application's Doc

## Swagger Docs
```
http://127.0.0.1/docs
```

## OpenAPI Docs
```
http://127.0.0.1/redoc
```


# File List
- `first.py`: 
    - first FastApi app
- `path_parameter.py`: 
    - basic path parameter
    - typed path parameter
    - predefined path parameter using enum
- `query_parameters.py`: 
    - basic query parameter
    - optional query parameter
    - required query parameter
- `request_body.py`: 
    - using post / put to get request
    - define request body using pydantic model
    - mix request body, path parameters and query parameter 
- `query_parameters_validation.py`: 
    - apply query parameter validation using Annotated and Query method
    - implement multiple query with the same name
    - adding metadata to Swagger / OpenApi doc using Query method
    - apply custom validation after Query validation
- `path_parameter_validation.py`:
    - apply path parameter validation using Annotated and Query method
- `query_parameter_model.py`:
    - use pydantic model to define query parameters
- `body_multiple_parameter.py`:
    - mix Path, Query and body parameters
    - multiple body parameters
    - add singular values in body
    - multiple body params and query
    - embed a single body parameter
- `body_model_validation.py`:
    - validate body parameter using pydantic model