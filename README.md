# 🚀 API de Simulação de Crédito Consignado

Uma API REST construída em Python e FastAPI para atuar como o sistema de avaliação de crédito de um banco, simulando a liberação e o cálculo de limites de cartões consignados com base no perfil e convênio do cliente.

Desenvolvi este projeto como um desafio pessoal de **Desenvolvimento Back-End**, com o objetivo de aprimorar minhas habilidades técnicas e aplicar na prática os conceitos exigidos por empresas reais do mercado financeiro. A construção de toda a API foi guiada para solucionar um problema de negócio real, mantendo o foco em **Arquitetura Limpa**, **Boas Práticas de Versionamento** e **Qualidade de Software**.

## 🧠 Arquitetura e Decisões Técnicas

* **Abordagem Fail-Fast (Segurança na Entrada):** Utilização do `Pydantic` para validação estrita de dados. O sistema barra imediatamente requisições com CPFs inválidos ou tipos de convênios inexistentes antes de qualquer processamento, poupando recursos do servidor.
* **Lógica de Negócios Extensível:** Eliminação de blocos `if/else` infinitos. As regras de margem de crédito (INSS, SIAPE, CLT Privado) foram abstraídas em um dicionário de mapeamento. Facilita a adição de novos convênios sem alterar o código principal, aplicando conceitos do SOLID.
* **Auditoria e Persistência:** Implementação de um banco de dados relacional leve (SQLite) via `SQLAlchemy` (ORM) para manter o histórico de todas as simulações executadas, garantindo rastreabilidade.
* **Qualidade e Confiabilidade:** Cobertura das regras de negócio através de Testes Automatizados utilizando `Pytest`, assegurando que o motor de decisão não falhe em atualizações futuras.

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) ![Pytest](https://img.shields.io/badge/pytest-%23ffffff.svg?style=for-the-badge&logo=pytest&logoColor=2f9fe3)

* 🐍 **Linguagem:** Python 3.x
* ⚡ **Framework Web:** FastAPI (com documentação interativa via Swagger)
* 🛡️ **Validação de Dados:** Pydantic
* 🗄️ **Banco de Dados / ORM:** SQLite + SQLAlchemy
* 🧪 **Testes Automatizados:** Pytest + Httpx
* 📦 **Gerenciador de Pacotes:** uv

## ⚙️ Como Executar o Projeto Localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/isaonline/API-Sim-Cred-Consig]

2. **Crie e ative o ambiente virtual:**
    ```bash
    python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No Linux/Mac:
    source venv/bin/activate

3. **Instale as dependências:**
    ```bash
    pip install uv
    uv pip install -r requirements.txt

4. **Inicie o servidor local:**
    ```bash
    uvicorn main:app --reload

5. **Acesse a documentação interativa (Swagger):**
    Abra o navegador e acesse: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 🧪 Como Executar os Testes Automatizados

Com o ambiente virtual ativado, rode o comando:
```bash
    python -m pytest