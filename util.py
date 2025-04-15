from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId

import spacy
import re


def str_objectid(v):
    if isinstance(v, ObjectId):
        return str(v)
    return v


def pingDB(MONGO_URI):
    # Create a new client and connect to the server
    client = MongoClient(MONGO_URI, server_api=ServerApi("1"))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


nlp = spacy.load("pt_core_news_md")


def interpretar_mensagem(mensagem: str):
    doc = nlp(mensagem.lower())

    tipo = "despesa"
    if any(
        t.lemma_ in ["receber", "ganhar", "depositar", "salário", "entrada"]
        for t in doc
    ):
        tipo = "receita"

    valor_match = re.search(r"(\d+[.,]?\d*)", mensagem)
    valor = float(valor_match.group(1).replace(",", ".")) if valor_match else 0.0

    categoria = None
    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"] and token.text not in ["reais", "dinheiro"]:
            categoria = token.text
            break
    if not categoria:
        categoria = "geral"

    return {"tipo": tipo, "valor": valor, "categoria": categoria}
