from datetime import datetime, timezone
from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

from util import str_objectid

import pytz

fuso_horario = pytz.timezone("America/Sao_Paulo")

class UsuarioModel(BaseModel):
    user_id: str
    nome: Optional[str] = None
    criado_em: Optional[datetime] = datetime.now(fuso_horario)

    class Config:
        json_encoders = {ObjectId: str_objectid}
