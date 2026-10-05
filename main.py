from fastapi import FastAPI
from schemas import SolicitacaoCredito
from services import calcular_limite

app = FastAPI()

@app.post("/simular")
def simular_credito(dados: SolicitacaoCredito):
    resultado = calcular_limite(
        salario=dados.salario,
        parcela_desejada=dados.parcela_desejada,
        tipo_trabalho=dados.tipo_trabalho
    )
    
    return resultado