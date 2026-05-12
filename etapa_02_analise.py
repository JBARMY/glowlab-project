import pandas as pd
df = pd.read_csv("vendas_glowlab.csv", encoding="utf-8-sig")
print("Dataset carregado!")

receita_total = df["receita_total"].sum()
print("Receita Total:", receita_total)

ticket_medio = df["receita_total"].mean()
print("Ticket Médio:", ticket_medio)

mais_vendido = df.groupby("produto")["quantidade"].sum().sort_values(ascending=False)
print(mais_vendido)

receita_produto = df.groupby("produto")["receita_total"].sum().sort_values(ascending=False)
print(receita_produto)

import matplotlib.pyplot as plt

receita_produto.plot(kind="bar",  color=["#D4537E", "#F0997B", "#FAC775", "#9FE1CB", "#85B7EB"])

plt.title("Receita por Produto - GlowLab Skincare Q1+Q2 2026")
plt.xlabel("Produto")
plt.ylabel("Receita (R$)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("grafico_receita_produtos.png", dpi=150, bbox_inches="tight")
plt.show()

print("Gráfico salvo!")
