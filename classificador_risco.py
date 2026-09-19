import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

ARQUIVO = "base_risco.csv"

df = pd.read_csv(ARQUIVO)

print("Quantidade de exemplos:", len(df))
print("\nDistribuição das classes:")
print(df["situacao"].value_counts())

X_train, X_test, y_train, y_test = train_test_split(
    df["frase"],
    df["situacao"],
    test_size=0.30,
    random_state=42,
    stratify=df["situacao"]
)

# TF-IDF transforma as frases em vetores numéricos.
# O Logistic Regression é um classificador simples e adequado para um exemplo didático.
modelo = Pipeline([
    ("tfidf", TfidfVectorizer(lowercase=True, ngram_range=(1, 2))),
    ("classificador", LogisticRegression(max_iter=1000))
])

modelo.fit(X_train, y_train)

predicoes = modelo.predict(X_test)

print("\nAcurácia:", round(accuracy_score(y_test, predicoes), 3))
print("\nRelatório de classificação:")
print(classification_report(y_test, predicoes, zero_division=0))

print("\nMatriz de confusão:")
print(confusion_matrix(y_test, predicoes))

# Testes qualitativos com frases novas.
frases_novas = [
    "estou com dor no peito e dificuldade para respirar",
    "tenho apenas uma dor muscular leve depois de caminhar",
    "comecei a ter falta de ar intensa de repente",
    "estou com espirros leves desde ontem"
]

print("\nPredições para frases novas:")
for frase in frases_novas:
    classe = modelo.predict([frase])[0]
    print(f"- {frase} -> {classe}")

# Limitações:
# - A base é pequena e artificial, portanto a acurácia não representa desempenho clínico.
# - Palavras muito associadas a uma classe podem gerar vieses.
# - O sistema não entende contexto clínico de forma abrangente.
# - Não deve ser usado para triagem ou diagnóstico real.
