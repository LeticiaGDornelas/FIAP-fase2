# Fase 2 — NLP aplicado a sintomas e classificação de risco

Projeto acadêmico com dados **simulados** para demonstrar:
1. extração simples de sintomas por expressões;
2. associação de sintomas a possíveis condições em um mapa de conhecimento;
3. transformação de texto com TF-IDF;
4. classificação de frases em baixo risco/alto risco com Logistic Regression;
5. avaliação por acurácia, relatório de classificação e matriz de confusão.

## Estrutura

- `frases_sintomas.txt` — 10 descrições simuladas de sintomas.
- `mapa_conhecimento.csv` — mapa de associações sintoma × possível condição.
- `extracao_sintomas.py` — leitura das frases, extração e sugestão de associações.
- `extracao_sintomas.ipynb` — versão em notebook da Parte 1.
- `base_risco.csv` — base simulada rotulada.
- `classificador_risco.py` — TF-IDF + Logistic Regression + avaliação.
- `classificador_risco.ipynb` — versão em notebook da Parte 2.

## Como executar

Instale as dependências:

```bash
pip install pandas scikit-learn jupyter
```

Depois execute:

```bash
python extracao_sintomas.py
python classificador_risco.py
```

Ou abra os notebooks:

```bash
jupyter notebook
```

## Vídeo

Após publicar o vídeo no YouTube como **Não listado**, coloque o link nesta seção:

`Link do vídeo: COLE_AQUI_O_LINK_DO_YOUTUBE`

## Observação importante

Este projeto é **exclusivamente educacional**, usa frases e rótulos artificiais e não representa uma ferramenta clínica validada. As associações de sintomas são possibilidades simplificadas para demonstrar técnicas de NLP e classificação. Os resultados não devem ser usados para diagnóstico, triagem ou decisão médica.
