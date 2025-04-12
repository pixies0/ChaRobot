import os

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client.piloto_db

entradas_collection = db["entradas"]
usuarios_collection = db["usuarios"]
