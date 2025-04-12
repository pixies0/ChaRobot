from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Pensar em substituir isso aqui futuramente
constants = [{1: "receita", 2: "despesa"}]


class Entradas(BaseModel):
    tipo: str
    valor: int
    categoria: str
    data: Optional[datetime] = None
