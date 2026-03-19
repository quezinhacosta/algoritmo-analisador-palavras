import spacy
import pandas as pd
import os
import re
from collections import Counter


nlp = spacy.load("pt_core_news_sm")
BASE = os.path.dirname(os.path.abspath(__file__))
ARQUIVO = os.path.join(BASE, "catalogo_palavras.xlsx")

if os.path.exists(ARQUIVO):
    df = pd.read_excel(ARQUIVO)
    df.columns = ["Palavra", "Frequência", "Numero_de_silabas", "Derivações", "Fonemas", "Nível"]
else:
    df = pd.DataFrame(columns=["Palavra", "Frequência", "Numero_de_silabas", "Derivações", "Fonemas", "Nível"])

def buscar_palavra(palavra):
    resultado = df[df["Palavra"].str.lower() == palavra.lower()]
    if not resultado.empty:
        print("a palavra mencionada já existe")
        return True
    else:
        print("a palavra será adicionada na lista.")
        return False

    
def verificar_derivacao(palavra, outra):
    if palavra in outra or outra in palavra:
        return True
    prefixo_comum = os.path.commonprefix([palavra, outra])
    proporcao = len(prefixo_comum) / max(len(palavra), len(outra))
    return proporcao >= 0.5  

def analisar_palavra(palavra):
    doc = nlp(palavra)
    lema = doc[0].lemma_
    tipo = "Original"
    palavra_original = palavra
    derivada = ""

    for _, linha in df.iterrows():
        palavra_existente = linha["Palavra"]
        if verificar_derivacao(palavra, palavra_existente):
            tipo = "Derivada"
            palavra_original = palavra_existente
            derivada = palavra
            break

    return tipo, palavra_original, derivada


def complexidade_silabica(palavra,maior_n_silaba):
    #CS = NÚMERO DE SÍLABAS DA PALAVRA / MAIOR NÚMERO DE SÍLABAS NO CONJUNTO DE PALAVRAS ANALISADO
    cs = Numero_de_silabas.palavra / maior_n_silaba
    if Numero_de_silabas.palavra > maior_n_silaba:
        maior_n_silaba = numero_de_silabas
    return cs

def complexidade_fonologica(palavra,maior_n_fonemas):
    #CF = NÚMERO DE FONEMAS / MAIOR NÚMERO DE FONEMAS OBSERVADOS NO CONJUNTO DE PALAVRAS
    cs = fonemas.palavra / maior_n_fonemas
    return cf

def similaridade_ortografica(palavra, n_derivadas):
    #SO = NÚMERO DE PALAVRAS SEMELHANTES NO CONJUNTO DE PALAVRAS / MAIOR NÚMERO ENCONTRADO DE PALAVRAS SEMELHANTES NO CONJUNTO DE PALAVRAS
    

def frequencia_de_uso(palavra, frequencia_max):
    #F = FREQUÊNCIA PALAVRA (CORPUS BRASILEIRO) / (CORPUS BRASILEIRO) FREQUENCIA MAXIMA PRESENTE NA BASE DE PALAVRAS
    if df.empty:
        return 0
    frequencia_max = df["Frequência"].max()
    linha = df[df["Palavra"].str.lower() == palavra.lower()]
    f = palavra.frequencia / frequencia_max
    if palavra.frequencia > frequencia_max:
        palavra.frequencia = frequencia_max
    return f

def encontrar_derivada(palavra): 
    doc_novo = nlp(palavra)
    maior_sim = 0
    palavra_base = None

    for existente in df["Palavra"]:
        doc_existente = nlp(str(existente))
        sim = doc_novo.similarity(doc_existente)
        if sim > maior_sim:
            maior_sim = sim
            palavra_base = existente

    if maior_sim > 0.75 and palavra_base:
        return palavra_base
    return None
