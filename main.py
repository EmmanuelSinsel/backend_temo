from fastapi import FastAPI, Request
import os
app = FastAPI()


@app.post("/compilar")
async def root(request: Request):
    res = await request.json()
    os.system("ls -l")
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
