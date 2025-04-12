from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from models.entradas import EntradaModel


class UsuarioModel(BaseModel):
    user_id: str
    nome: Optional[str] = None
    entradas: Optional[List[dict]] = []
    criado_em: Optional[datetime] = None
