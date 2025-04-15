from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from bson import ObjectId

from util import str_objectid

# Pensar em substituir isso aqui futuramente
constants = [{1: "receita", 2: "despesa"}]

class Entradas(BaseModel):
    user_id: str
    tipo: str
    valor: float
    categoria: str
    data: Optional[datetime] = None

    class Config:
        json_encoders = {ObjectId: str_objectid}
