MARGENS_CREDITO = {
    "INSS": 0.45,
    "SIAPE": 0.35,
    "CLT Privado": 0.30
}

def calcular_limite(salario: float, parcela_desejada: float, tipo_trabalho: str) -> dict:
    margem = MARGENS_CREDITO.get(tipo_trabalho)
    
    parcela_maxima = salario * margem
    
    limite_estimado = parcela_maxima * 24
    
    if parcela_desejada <= parcela_maxima:
        return {"resultado": "APROVADO", "parcela_maxima": parcela_maxima, "limite_estimado": limite_estimado}
    else:
        return {"resultado": "REPROVADO", "parcela_maxima": parcela_maxima, "limite_estimado": limite_estimado}