import pandas as pd
print("Bibliotecas carregadas!")

df = pd.read_csv("Vendas_glowlab.csv", encoding="utf-8-sig")
print(df.head())
print(df.shape)
print(df.isnull().sum())
print(df.duplicated().sum())
