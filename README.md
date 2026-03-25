#  Modelo de Classificação de Dificuldade de Palavras

Este projeto tem como objetivo desenvolver um algoritmo em Python capaz de classificar palavras da língua portuguesa de acordo com seu nível de dificuldade, com base em métricas linguísticas.

A proposta está vinculada a um projeto de Iniciação Científica da Universidade Católica de Pernambuco (UNICAP). Construído pela aluna Quezia Costa, futura cientista da computação. 

---

##  Objetivo

Criar um sistema que analisa palavras e atribui um índice de dificuldade com base em três critérios:

- Frequência de uso
- Complexidade silábica
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

### Cálculo Final

C = 0.20F + 0.40CS + 0.40SO

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
| Nível               | Valor numerico |
| Classificação       | Classificação final |

---

## ▶️ Como executar

pip install pandas spacy openpyxl (verificar se já estão baixadas antes, com pip show)
python -m spacy download pt_core_news_sm (verificar se já está baixado)
python logica.py
