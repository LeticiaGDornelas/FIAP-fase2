<div align="center">

<a href="https://www.fiap.com.br/">
  <img alt="FIAP - Faculdade de Informática e Administração Paulista" src="assets/logo-fiap (2).png" width="160px">
</a>

</div>

<br>

# Fase 2 — NLP para Extração de Sintomas e Classificação de Risco

## Projeto de Processamento de Linguagem Natural

---

## 👨‍🎓 Integrantes

- Laura de Andrade Castilho — RM568507
- Leticia Grossi Dornelas — RM568172
- Leonardo Borges Alves da Mota — RM566939
- Bernardo Naves Doti Avelar — RM566867
- David Eduardo da Silva Correia — RM567525

---

## 👩‍🏫 Professores

### Tutor(a)
- Ana Cristina dos Santos

### Coordenador(a)
- André Godoi Chiovato

---

## 📜 Descrição

Este projeto foi desenvolvido no âmbito da **Fase 2** do curso de Inteligência Artificial da FIAP, com foco em **Processamento de Linguagem Natural (NLP)** e **Machine Learning**.

O projeto simula um sistema básico capaz de receber relatos textuais de pacientes, identificar expressões relacionadas a sintomas e consultar um **mapa de conhecimento** para encontrar possíveis associações. Em uma segunda etapa, foi desenvolvido um classificador de texto para categorizar relatos simulados em **baixo risco** ou **alto risco**.

O projeto está dividido em duas partes:

1. **Extração de informações e mapa de conhecimento**
2. **Classificação básica de risco utilizando TF-IDF e Logistic Regression**

> **Importante:** todos os relatos e rótulos utilizados são simulados e têm finalidade exclusivamente acadêmica. O projeto não realiza diagnóstico médico real, não é uma ferramenta clínica validada e não deve ser utilizado para decisões de saúde.

---

## 📁 Estrutura de Pastas

```text
FIAP-fase2-NLP/
├── assets/                         # Recursos visuais do projeto
│   └── logo-fiap (1).png
├── frases_sintomas.txt             # 10 relatos simulados de sintomas
├── mapa_conhecimento.csv           # Associação entre sintomas e possíveis condições
├── extracao_sintomas.py            # Código da Parte 1
├── extracao_sintomas.ipynb         # Notebook da Parte 1
├── base_risco.csv                  # Dataset rotulado de risco
├── classificador_risco.py          # Código da Parte 2
├── classificador_risco.ipynb       # Notebook da Parte 2
├── requirements.txt                # Dependências Python
└── README.md                       # Este arquivo
```

---

## 🗂️ Parte 1 — Relatos e Mapa de Conhecimento

### Relatos de sintomas

O arquivo `frases_sintomas.txt` contém **10 frases completas** simulando relatos de pacientes. Os textos apresentam informações como:

- sintomas percebidos;
- quando os sintomas começaram;
- impacto dos sintomas na rotina;
- diferentes combinações de sintomas.

### Mapa de conhecimento

O arquivo `mapa_conhecimento.csv` organiza associações entre expressões de sintomas e possíveis condições, utilizando as colunas:

| Sintoma 1 | Sintoma 2 | Doença Associada |
|-----------|-----------|------------------|
| dor no peito | aperto no peito | Angina (possível associação) |
| cansaço constante | fadiga | Insuficiência cardíaca (possível associação) |
| falta de ar | dificuldade para respirar | Doença respiratória (possível associação) |
| dor de cabeça | sensibilidade à luz | Enxaqueca (possível associação) |
| dor ao urinar | vontade frequente de urinar | Infecção urinária (possível associação) |
| congestão nasal | espirros | Rinite alérgica (possível associação) |

O código utiliza esse mapa para procurar expressões presentes nos relatos e apresentar as associações encontradas.

---

## 🔧 Código de Extração de Informações

O arquivo `extracao_sintomas.py` realiza:

1. Leitura do arquivo de relatos;
2. Normalização básica do texto;
3. Leitura do mapa de conhecimento;
4. Identificação de expressões de sintomas;
5. Associação dos sintomas encontrados às possíveis condições;
6. Exibição das principais correspondências.

### Exemplo de funcionamento

```text
Relato do paciente
        ↓
Normalização do texto
        ↓
Identificação das expressões
        ↓
Consulta ao mapa de conhecimento
        ↓
Possíveis associações
```

A versão em notebook está disponível em:

`extracao_sintomas.ipynb`

---

## 🧠 Parte 2 — Classificador Básico de Texto

Para a segunda etapa foi criada uma base simulada no arquivo `base_risco.csv`.

A base possui duas colunas:

| Coluna | Descrição |
|--------|-----------|
| `frase` | Relato textual simulado |
| `situacao` | Rótulo `baixo risco` ou `alto risco` |

O objetivo é demonstrar como técnicas de NLP podem transformar textos em dados numéricos e utilizá-los em um algoritmo de classificação.

---

## 🔢 TF-IDF

Foi utilizado o método **TF-IDF (Term Frequency–Inverse Document Frequency)** para transformar as frases em vetores numéricos.

O processo utilizado é:

```text
Frases
   ↓
TF-IDF
   ↓
Vetores numéricos
   ↓
Logistic Regression
   ↓
Baixo risco / Alto risco
```

Foi utilizado `ngram_range=(1, 2)` para considerar tanto palavras individuais quanto combinações de duas palavras.

---

## 🤖 Modelo de Classificação

O classificador escolhido foi a **Logistic Regression**, utilizando o `scikit-learn`.

O modelo foi treinado com uma divisão entre dados de treinamento e teste e posteriormente avaliado utilizando:

- **Acurácia**
- **Classification Report**
- **Matriz de Confusão**
- Testes com novas frases

O código está disponível em:

`classificador_risco.py`

e a versão em notebook em:

`classificador_risco.ipynb`

---

## 📊 Avaliação

A avaliação permite observar:

- quantas frases foram classificadas corretamente;
- desempenho separado entre as classes;
- possíveis erros de classificação;
- comportamento do modelo diante de novas frases.

Como a base utilizada é pequena e artificial, os resultados devem ser interpretados **apenas como demonstração acadêmica**. A acurácia obtida não representa desempenho de uma ferramenta clínica real.

---

## 🔧 Como Executar no Google Colab

### Pré-requisitos

- Conta Google;
- Google Colab;
- Python 3;
- Bibliotecas `pandas` e `scikit-learn`.

### 1. Abrir o notebook

Os notebooks disponíveis são:

- `extracao_sintomas.ipynb`
- `classificador_risco.ipynb`

Eles podem ser enviados diretamente para o Google Colab.

### 2. Instalar as dependências

Execute:

```python
!pip install pandas scikit-learn
```

### 3. Fazer upload dos arquivos

Para a Parte 1:

```text
frases_sintomas.txt
mapa_conhecimento.csv
```

Para a Parte 2:

```text
base_risco.csv
```

Os arquivos `.py` também podem ser executados diretamente no Colab com:

```python
%run extracao_sintomas.py
```

e:

```python
%run classificador_risco.py
```

---

## 🎥 Vídeo Demonstrativo

> 📹 **Link do vídeo no YouTube (não listado):** A inserir após a gravação.

O vídeo deverá demonstrar, em até **4 minutos**:

1. Estrutura do projeto;
2. Leitura dos relatos;
3. Extração dos sintomas;
4. Consulta ao mapa de conhecimento;
5. Transformação TF-IDF;
6. Treinamento do classificador;
7. Avaliação do modelo;
8. Classificação de novas frases.

---

## 🗃️ Histórico de Lançamentos

### 1.0.0 — Entrega Final Fase 2

- Criação de 10 relatos simulados;
- Criação do mapa de conhecimento;
- Implementação da extração de sintomas;
- Criação do dataset de classificação;
- Aplicação de TF-IDF;
- Treinamento com Logistic Regression;
- Avaliação do classificador;
- Criação dos notebooks e documentação.

---

## 📋 Observações

Este projeto possui finalidade **educacional** e demonstra conceitos de:

- Processamento de Linguagem Natural;
- Extração de informações;
- Representação vetorial de textos;
- TF-IDF;
- Classificação supervisionada;
- Avaliação de modelos de Machine Learning.

As associações entre sintomas e condições são simplificadas e **não representam diagnósticos médicos**.

---

## 📄 Licença

Projeto acadêmico desenvolvido para a **FIAP — Faculdade de Informática e Administração Paulista**.
