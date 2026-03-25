import spacy
import pandas as pd
import os

nlp = spacy.load("pt_core_news_sm")

BASE = os.path.dirname(os.path.abspath(__file__))
ARQUIVO = os.path.join(BASE, "catalogo_palavras_ATUALIZADO (5).xlsx")

# =========================
# CARREGAR BASE
# =========================
if os.path.exists(ARQUIVO):
    df = pd.read_excel(ARQUIVO, usecols="A:F")
    df.columns = ["Palavra", "Frequência", "Numero_de_silabas", "Derivações", "Nível", "Classificação"]
else:
    df = pd.DataFrame(columns=["Palavra", "Frequência", "Numero_de_silabas", "Derivações", "Nível", "Classificação"])


# =========================
# FUNÇÕES AUXILIARES
# =========================

def buscar_linha(palavra):
    linha = df[df["Palavra"].str.lower() == palavra.lower()]
    return linha


# =========================
# FREQUÊNCIA
# =========================
def frequencia_de_uso(palavra):
    if df.empty:
        return 0

    linha = buscar_linha(palavra)
    if linha.empty:
        return 0

    freq_palavra = linha["Frequência"].values[0]
    freq_max = df["Frequência"].max()

    if freq_max == 0:
        return 0

    return freq_palavra / freq_max


# =========================
# COMPLEXIDADE SILÁBICA
# =========================
def complexidade_silabica(palavra):
    if df.empty:
        return 0

    linha = buscar_linha(palavra)
    if linha.empty:
        return 0

    silabas = linha["Numero_de_silabas"].values[0]
    max_silabas = df["Numero_de_silabas"].max()

    if max_silabas == 0:
        return 0

    return silabas / max_silabas


# =========================
# SIMILARIDADE ORTOGRÁFICA (VIZINHOS REAIS)
# =========================
def palavras_semelhantes(p1, p2):
    if p1 == p2:
        return False

    # diferença de caracteres (tipo Levenshtein simplificado)
    diferencas = abs(len(p1) - len(p2))

    for a, b in zip(p1, p2):
        if a != b:
            diferencas += 1

    return diferencas <= 1  # apenas 1 mudança


def similaridade_ortografica(palavra):
    palavra = palavra.lower()
    if df.empty:
        return 0
    linha = df[df["Palavra"].str.lower() == palavra]
    derivada_palavra = linha["Derivações"].values[0]
    maior_derivada = df["Derivações"].max()

    if maior_derivada == 0:
        return 0
    SO = derivada_palavra / maior_derivada

    return SO
 

def calculo_final(F, SO, CS):
    return (0.20 * F) + (0.35 * CS) + (0.45 * SO)


def classificar(nivel):
    if nivel <= 0.3:
        return "facil"
    elif nivel <= 0.6:
        return "medio"
    else:
        return "dificil"
def processar_planilha():
    global df

    if df.empty:
        print("DataFrame vazio.")
        return

    niveis = []
    classificacoes = []

    for _, linha in df.iterrows():
        palavra = str(linha["Palavra"]).lower()

        F = frequencia_de_uso(palavra)
        CS = complexidade_silabica(palavra)
        SO = similaridade_ortografica(palavra)

        nivel = calculo_final(F, SO, CS)
        classificacao = classificar(nivel)

        niveis.append(round(nivel, 4))
        classificacoes.append(classificacao)

    df["Nível"] = niveis
    df["Classificação"] = classificacoes

    df.to_excel(ARQUIVO, index=False)
    print("Planilha atualizada com sucesso!")
processar_planilha()