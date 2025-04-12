from fastapi import APIRouter

from schema.schemas import entrada_unica_serializer, entrada_lista_serializer
from config.database import entradas_collection
from models.entradas import Entradas
from bson import ObjectId

router = APIRouter()


@router.get("/entradas")
async def get_entrada():
    entradas = entrada_lista_serializer(entradas_collection.find())
    return entradas


@router.post("/entradas")
async def create_entrada(entrada: Entradas):
    entradas_collection.insert_one(dict(entrada))


@router.put("/entradas/{id}")
async def update_entrada(id: str, entrada: Entradas):
    entradas_collection.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(entrada)}
    )


@router.delete("/entradas/{id}")
async def delete_entrada(id: str):
    entradas_collection.find_one_and_delete({"_id": ObjectId(id)})
