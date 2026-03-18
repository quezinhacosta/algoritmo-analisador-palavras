import spacy
import pandas as pd
import os

nlp = spacy.load("pt_core_news_sm")
BASE = os.path.dirname(os.path.abspath(__file__))
ARQUIVO = os.path.join(BASE, "catalogo_palavras.xlsx")

if os.path.exists(ARQUIVO):
    df = pd.read_excel(ARQUIVO)
    df.columns = ["Palavra", "Tipo", "Palavra original", "Palavra derivada"]
else:
    df = pd.DataFrame(columns=["Palavra", "Tipo", "Palavra original", "Palavra derivada"])

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

def adicionar_palavra(palavra):
    global df

    if buscar_palavra(palavra):
        return

    tipo, original, derivada = analisar_palavra(palavra)

    if tipo == "Original":
        base = encontrar_derivada(palavra)
        if base:
            tipo = "Derivada"
            original = base
            derivada = palavra

    novo_dado = pd.DataFrame([[palavra, tipo, original, derivada]], columns=df.columns)
    df = pd.concat([df, novo_dado], ignore_index=True)
    df.to_excel(ARQUIVO, index=False)
    print(f"'{palavra}' adicionada como {tipo} (original: {original})")

def listar_catalogo():
    print("\nCatálogo atual:")
    print(df)

def excluir_palavra(palavra):
    global df
    df = df[df["Palavra"].str.lower() != palavra.lower()]
    df.to_excel(ARQUIVO, index=False)
    print(f"'{palavra}' removida do catálogo.")

while True:
    print("\n1 - adicionar nova palavra")
    print("2 - ver lista de palavras")
    print("3 - excluir palavra")
    print("4 -  encontrar uma palavra")
    print("5 - sair")
    print("oh ")
    print("6 - mudar de derivada para original")
    print("7 - mudar de original para derivada")

    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == "1":
        palavra = input("qual palavra? ").strip().lower()
        adicionar_palavra(palavra)
    elif opcao == "2":
        listar_catalogo()
    elif opcao == "3":
        palavra = input("qual palavra deseja excluir?").strip().lower()
        excluir_palavra(palavra)
    elif opcao == "4":
        palavra = input("qual palavra deseja encontrar?").strip().lower()
        if encontrar_derivada(palavra) is None:
            print("nenhuma palavra base encontrada")
        else:
            print(f"A palavra base encontrada é: {encontrar_derivada(palavra)} na posicao {df[df['Palavra'] == encontrar_derivada(palavra)].index[0]}")
    elif opcao == "5":
        break
    elif opcao == "6":
        palavra = input("qual palavra deseja mudar de derivada para original?").strip().lower()
        if palavra in df["Palavra"].values:
            df.loc[df["Palavra"] == palavra, "Tipo"] = "Original"
            df.loc[df["Palavra"] == palavra, "Palavra original"] = palavra
            df.loc[df["Palavra"] == palavra, "Palavra derivada"] = ""
            df.to_excel(ARQUIVO, index=False)
            print(f"'{palavra}' mudou para Original.")
        else:
            print("palavra não encontrada no catálogo.")
    elif opcao == "7":
        palavra = input("qual palavra deseja mudar de original para derivada?").strip().lower()
        original = input("qual é a palavra original dessa derivada?").strip().lower()
        if palavra in df["Palavra"].values:
            df.loc[df["Palavra"] == palavra, "Tipo"] = "Derivada"
            df.loc[df["Palavra"] == palavra, "Palavra derivada"] = palavra
            df.loc[df["Palavra"] == palavra, "Palavra original"] = original
            df.to_excel(ARQUIVO, index=False)
            print(f"'{palavra}' mudou para Derivada de '{original}'.")
        else:
            print("palavra não encontrada no catálogo.")
    else:           
        print("opcap invalida")

#coisas pra arrumar ainda: ordenar as palvras pela ordem alfabetica; diferenciar a original e derivação melhor, nn pela ordem que é inserido