from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from schemas import SolicitacaoCredito
from services import calcular_limite
from database import SessionLocal, SimulacaoDB 

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/simular")
def simular_credito(dados: SolicitacaoCredito, db: Session = Depends(get_db)):
    resultado_calculo = calcular_limite(
        salario=dados.salario,
        parcela_desejada=dados.parcela_desejada,
        tipo_trabalho=dados.tipo_trabalho
    )
    
    nova_simulacao = SimulacaoDB(
        cpf=dados.cpf,
        resultado=resultado_calculo["resultado"],
        limite_liberado=resultado_calculo["limite_estimado"]
    )
    db.add(nova_simulacao)
    db.commit()
    
    return resultado_calculo

@app.get("/simulacoes")
def listar_simulacoes(db: Session = Depends(get_db)):
    historico = db.query(SimulacaoDB).all()
    return historico