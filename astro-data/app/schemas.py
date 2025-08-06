from pydantic import BaseModel

class ObjectResponse(BaseModel):
    nome: str
    distancia: float
    velocidade: float