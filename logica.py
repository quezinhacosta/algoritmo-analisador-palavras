import spacy
import pandas as pd
import os
import re
from collections import Counter


nlp = spacy.load("pt_core_news_sm")
BASE = os.path.dirname(os.path.abspath(__file__))
ARQUIVO = os.path.join(BASE, "catalogo_palavras_ATUALIZADO (2).xlsx")
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


def complexidade_silabica(palavra):
    #CS = NÚMERO DE SÍLABAS DA PALAVRA / MAIOR NÚMERO DE SÍLABAS NO CONJUNTO DE PALAVRAS ANALISADO
   palavra = palavra.lower()
   if df.empty:
<<<<<<< HEAD
        return 0
   linha = df[df["Palavra"].str.lower() == palavra]
   silaba_palavra = linha["Numero_de_silabas"].values[0]
   maior_n_silaba = df["Numero_de_silabas"].max()
=======
        return 0;
   linha = df[df["Palavra"].str.lower() == palavra]
   silaba_palavra = linha["Silabas"].values[0]
   maior_n_silaba = df["Slabas"].max()
>>>>>>> b55b47868f58063eb1764eb686a31d86174bdf89
   if maior_n_silaba == 0:
        return 0
   CS = silaba_palavra / maior_n_silaba

   return CS

def complexidade_fonologica(palavra):
    #CF = NÚMERO DE FONEMAS / MAIOR NÚMERO DE FONEMAS OBSERVADOS NO CONJUNTO DE PALAVRA
    palavra = palavra.lower()
    if df.empty:
<<<<<<< HEAD
        return 0
    linha = df[df["Palavra"].str.lower() == palavra]
    fonema_palavra = linha["Fonemas"].values[0]
    maior_n_fonema = df["Fonemas"].max()
=======
        return 0;
    linha = df[df["Palavra"].str.lower() == palavra]
    fonema_palavra = linha["Fonema"].values[0]
    maior_n_fonema = df["Fonema"].max()
>>>>>>> b55b47868f58063eb1764eb686a31d86174bdf89
    if maior_n_fonema == 0:
        return 0
    CF = fonema_palavra / maior_n_fonema

    return CF


<<<<<<< HEAD
def similaridade_ortografica(palavra):
    #SO = NÚMERO DE PALAVRAS SEMELHANTES NO CONJUNTO DE PALAVRAS / MAIOR NÚMERO ENCONTRADO DE PALAVRAS SEMELHANTES NO CONJUNTO DE PALAVRAS
    palavra = palavra.lower()
    if df.empty:
        return 0
    contador = 0
    for outra in df["Palavra"]:
        outra = str(outra).lower()
        if palavra == outra:
            continue
        if verificar_derivacao(palavra, outra):
            contador += 1
    max_sim = 0
    for p in df["Palavra"]:
        count = 0
        for outra in df["Palavra"]:
            if p != outra and verificar_derivacao(str(p).lower(), str(outra).lower()):
                count += 1
        if count > max_sim:
            max_sim = count

    if max_sim == 0:
        return 0
    
    SO = contador / max_sim

    return SO
=======
def similaridade_ortografica(palavra, n_derivadas):
    #SO = NÚMERO DE PALAVRAS SEMELHANTES NO CONJUNTO DE PALAVRAS / MAIOR NÚMERO ENCONTRADO DE PALAVRAS SEMELHANTES NO CONJUNTO DE PALAVRAS
    palavra = palavra.lower()
    if df.empty:
        return 0;
>>>>>>> b55b47868f58063eb1764eb686a31d86174bdf89


def frequencia_de_uso(palavra):
    #F = FREQUÊNCIA PALAVRA (CORPUS BRASILEIRO) / (CORPUS BRASILEIRO) FREQUENCIA MAXIMA PRESENTE NA BASE DE PALAVRAS
    palavra = palavra.lower()
    if df.empty:
        return 0
    linha = df[df["Palavra"].str.lower() == palavra]
    freq_palavra = linha["Frequência"].values[0]
    frequencia_max = df["Frequência"].max()
    if frequencia_max == 0:
        return 0
    F = freq_palavra / frequencia_max

    return F

<<<<<<< HEAD
def calculo_final(F, SO, CF, CS):
    if df.empty:
        return 0 
    nivel = (0.15 * F) + (0.25 * CS) + (0.25 * CF) + (SO * 0.35)
    return nivel

def df_nivel(nivel, palavra):
    if df.empty:
        return "indefinido"
    
    if 0 <= nivel <= 0.5:
        return "facil"
    elif 0.51 <= nivel <= 0.75:
        return "medio"
    else: 
        return "dificil"

=======
>>>>>>> b55b47868f58063eb1764eb686a31d86174bdf89
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
<<<<<<< HEAD

def processar_planilha():
    global df
    if df.empty:
        return

    niveis = []
    classificacoes = []

    for _, linha in df.iterrows():

        palavra = str(linha["Palavra"]).lower()
        F = frequencia_de_uso(palavra)
        CS = complexidade_silabica(palavra)
        CF = complexidade_fonologica(palavra)
        SO = similaridade_ortografica(palavra)
        nivel = calculo_final(F, SO, CF, CS)

        classificacao = df_nivel(nivel, palavra)
        niveis.append(nivel)
        classificacoes.append(classificacao)
    df["Nível"] = niveis
    df["Classificacao"] = classificacoes
    df.to_excel(ARQUIVO, index=False)

processar_planilha()
=======
>>>>>>> b55b47868f58063eb1764eb686a31d86174bdf89
