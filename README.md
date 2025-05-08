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

# Run App

```
uvicorn main:app
```