from fastapi import APIRouter, Request
from datetime import datetime, timezone

from config.database import entradas_collection, usuarios_collection
from schema.schemas import entrada_lista_serializer
from util import interpretar_mensagem
from models.entradas import Entradas
from bson import ObjectId

import pytz

fuso_horario = pytz.timezone("America/Sao_Paulo")

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


@router.post("/mensagem")
async def receber_mensagem(request: Request):
    dados = await request.json()
    mensagem = dados.get("mensagem")
    telefone = dados.get("telefone")

    if not mensagem or not telefone:
        return {"erro": "Mensagem ou telefone ausente"}

    resultado = interpretar_mensagem(mensagem)

    if not resultado:
        return {"erro": "Não foi possível interpretar a mensagem"}

    usuario = usuarios_collection.find_one({"user_id": telefone})

    if not usuario:
        novo_usuario = {"user_id": telefone, "criado_em": datetime.now(fuso_horario)}
        usuarios_collection.insert_one(novo_usuario)

    nova_entrada = Entradas(
        user_id=telefone,
        tipo=resultado["tipo"],
        valor=resultado["valor"],
        categoria=resultado["categoria"],
        data=datetime.now(fuso_horario),
    )
    entradas_collection.insert_one(nova_entrada.model_dump())

    return {
        "mensagem": "Entrada registrada com sucesso!",
        "dados": nova_entrada.model_dump(),
    }
