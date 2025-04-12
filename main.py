import os
import logging
import uvicorn

from fastapi import FastAPI
from dotenv import load_dotenv

from routes.route import router
from util import pingDB

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
LOG = logging.getLogger(__name__)

app = FastAPI()

pingDB(MONGO_URI)

app.include_router(router)


@app.get("/saude")
async def root():
    print("Estou saudavel")
    return {"message": "Estou saudável"}
