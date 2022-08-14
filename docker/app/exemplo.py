from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
async def root():
    return {"messege": "You are doing fine with FastAPI..."}

@app.get("/api/{name}")
async def get_user(name):
    return {
        "name": name, 
        "message": f"Hello, {name} from FastAPI."
    }