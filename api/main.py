from fastapi import FastAPI, Request
from pydantic import BaseModel
import redis

app = FastAPI()
r = redis.Redis(host='redis', port=6379, decode_responses=True)

class Vote(BaseModel):
    option: str

@app.post("/vote")
def vote(vote: Vote):
    r.publish("votes", vote.option)
    return {"status": "vote submitted", "option": vote.option}