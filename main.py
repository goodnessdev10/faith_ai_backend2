from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Faith AI Backend Running"}from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Faith AI Backend Running"}
