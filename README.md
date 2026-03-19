#  Modelo de Classificação de Dificuldade de Palavras

Este projeto tem como objetivo desenvolver um algoritmo em Python capaz de classificar palavras da língua portuguesa de acordo com seu nível de dificuldade, com base em métricas linguísticas.

A proposta está vinculada a um projeto de Iniciação Científica da Universidade Católica de Pernambuco (UNICAP).

---

##  Objetivo

Criar um sistema que analisa palavras e atribui um índice de dificuldade com base em quatro critérios:

- Frequência de uso
- Complexidade silábica
- Complexidade fonológica
- Similaridade ortográfica

---

##  Metodologia

Cada palavra é avaliada a partir das seguintes métricas:

### 🔹 Frequência de Uso (F)
Baseada na frequência da palavra em um conjunto de dados.

F = frequência da palavra / maior frequência do conjunto

---

### 🔹 Complexidade Silábica (CS)

CS = número de sílabas / maior número de sílabas do conjunto

---

### 🔹 Complexidade Fonológica (CF)

CF = número de fonemas / maior número de fonemas do conjunto

---

### 🔹 Similaridade Ortográfica (SO)

SO = número de palavras semelhantes / maior número de similaridades no conjunto

---

### Cálculo Final

C = 0.15F + 0.25CS + 0.25CF + 0.35SO

---

## ⚙️ Tecnologias utilizadas

- Python 3
- pandas
- spaCy
- openpyxl (para leitura de Excel)

---
## 📥 Entrada de dados

Os dados são armazenados em um arquivo Excel com as seguintes colunas:

| Coluna              | Descrição |
|---------------------|----------|
| Palavra             | Palavra analisada |
| Frequência          | Frequência de uso |
| Numero_de_silabas   | Número de sílabas |
| Derivações          | Relação com outras palavras |
| Fonemas             | Número de fonemas |
| Nível               | Classificação final |

---

## ▶️ Como executar

1. Instale as dependências:

```bash
pip install pandas spacy openpyxl
python -m spacy download pt_core_news_sm
