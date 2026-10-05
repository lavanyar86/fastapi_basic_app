from fastapi import FastAPI

# Initialize the FastAPI application instance
app = FastAPI()

# 1. Root endpoint: GET /
@app.get("/")
def read_root():
    return {"message": "Welcome to my first basic FastAPI app!"}

# 2. Parameter endpoint: GET /greet/{name}
@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name}! Your FastAPI endpoint works perfectly."}
