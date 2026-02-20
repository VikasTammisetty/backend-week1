from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Backend is running!"}

@app.get("/hello/{name}")
def greet(name: str):
    return {"message": f"Hello {name}"}
