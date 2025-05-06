from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import redis

app = FastAPI()
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("index.html") as f:
        return f.read()

@app.get("/results")
def results():
    keys = r.keys("count:*")
    return {k.replace("count:", ""): r.get(k) for k in keys}