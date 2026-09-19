import re
from pathlib import Path
import pandas as pd

ARQUIVO_FRASES = Path("frases_sintomas.txt")
ARQUIVO_MAPA = Path("mapa_conhecimento.csv")

# Normalização simples para facilitar a correspondência das expressões.
def normalizar(texto):
    texto = texto.lower()
    texto = re.sub(r"[^\w\sáàãâéêíóôõúç]", " ", texto, flags=re.UNICODE)
    return re.sub(r"\s+", " ", texto).strip()

frases = [
    linha.strip()
    for linha in ARQUIVO_FRASES.read_text(encoding="utf-8").splitlines()
    if linha.strip()
]

mapa = pd.read_csv(ARQUIVO_MAPA)
mapa["Sintoma 1"] = mapa["Sintoma 1"].fillna("")
mapa["Sintoma 2"] = mapa["Sintoma 2"].fillna("")

def extrair_e_sugerir(frase):
    texto = normalizar(frase)
    encontrados = set()
    diagnosticos = {}

    for _, linha in mapa.iterrows():
        s1 = normalizar(linha["Sintoma 1"])
        s2 = normalizar(linha["Sintoma 2"])
        sintomas_linha = [s for s in (s1, s2) if s]

        correspondencias = [s for s in sintomas_linha if s in texto]

        if correspondencias:
            encontrados.update(correspondencias)
            doenca = linha["Doença Associada"]
            # Pontuação simples: mais sintomas coincidentes = maior correspondência.
            diagnosticos[doenca] = diagnosticos.get(doenca, 0) + len(correspondencias)

    ordenados = sorted(
        diagnosticos.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return sorted(encontrados), ordenados

for i, frase in enumerate(frases, start=1):
    sintomas, sugestoes = extrair_e_sugerir(frase)

    print(f"\nPaciente {i}: {frase}")
    print("Sintomas/expressões identificados:", ", ".join(sintomas) or "nenhum")

    if sugestoes:
        print("Possíveis associações (apenas para fins educacionais):")
        for diagnostico, pontuacao in sugestoes[:3]:
            print(f"  - {diagnostico} | correspondências: {pontuacao}")
    else:
        print("Nenhuma associação encontrada no mapa.")

# Observação:
# Este código é uma demonstração de NLP baseada em palavras/expressões.
# Não realiza diagnóstico médico real e não deve ser usado para orientar
# decisões clínicas ou substituir avaliação profissional.
