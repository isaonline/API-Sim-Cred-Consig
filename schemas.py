from pydantic import BaseModel, Field
from typing import Literal

class SolicitacaoCredito(BaseModel):
    nome: str
    cpf: str = Field(min_length=11, max_length=11)
    salario: float = Field(gt=0)
    parcela_desejada: float = Field(gt=0)
    tipo_trabalho: Literal["INSS", "SIAPE", "CLT Privado"]