from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_cliente_deve_ser_aprovado():
    response = client.post("/simular", json={
        "nome": "Ana Souza",
        "cpf": "12345678910",
        "salario": 5000.0,
        "parcela_desejada": 1000.0,
        "tipo_trabalho": "CLT Privado"
    })
    
    assert response.status_code == 200
    assert response.json()["resultado"] == "APROVADO"

def test_cliente_parcela_alta_deve_ser_reprovado():
    response = client.post("/simular", json={
        "nome": "Carlos Mendes",
        "cpf": "10987654321",
        "salario": 5000.0,
        "parcela_desejada": 3000.0,
        "tipo_trabalho": "CLT Privado"
    })
    
    assert response.status_code == 200
    assert response.json()["resultado"] == "REPROVADO"

def test_cliente_com_dados_invalidos_deve_dar_erro():
    response = client.post("/simular", json={
        "nome": "João",
        "cpf": "123",
        "salario": 5000.0,
        "parcela_desejada": 1000.0,
        "tipo_trabalho": "Estudante"
    })
    
    assert response.status_code == 422