import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("vendas_glowlab.csv", encoding="utf_8_sig")
df["data"] = pd.to_datetime(df["data"])
df["mes"] = df["data"].dt.month

print("Dataset carregado!")

fig, axs = plt.subplots(2, 2, figsize=(14, 10))

fig.suptitle("Dashboard Executivo - GlowLab Skincare Q1+Q2 2026",
             fontsize=16, fontweight="bold")

receita_mes = df.groupby("mes")["receita_total"].sum()
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]

axs[0, 0].bar(meses,receita_mes.values, color="#D4537E")
axs[0, 0].set_title("Receita por Mês")
axs[0, 0].set_ylabel("Receita(R$)")
        

receita_produto = df.groupby("produto")["receita_total"].sum().sort_values()

axs[0, 1].barh(receita_produto.index, receita_produto.values,
               color=["#D4537E", "#F0997B", "#FAC775", "#9FE1CB", "#85B7EB"])
axs[0, 1].set_title("Receita por Produto")
axs[0, 1].set_xlabel("Receita (R$)")


qtd_produto = df.groupby("produto")["quantidade"].sum().sort_values()

axs[1, 0].barh(qtd_produto.index, qtd_produto.values,
               color=["#D4537E", "#F0997B", "#FAC775", "#9FE1CB", "#85B7EB"])
axs[1, 0].set_title("Quantidade Vendida por Produto")
axs[1, 0].set_xlabel("Unidades")



axs[1, 1].plot(meses, receita_mes.values, marker="o",
               color="#D4537E", linewidth=2, markersize=8)
axs[1, 1].set_title("Tendência de Receita Mensal")
axs[1, 1].set_ylabel("Receita (R$)")
axs[1, 1].grid(True, linestyle="--", alpha=0.5)


plt.tight_layout(pad=3.0)
plt.savefig("dashboard_glowlab.png", dpi=150, bbox_inches="tight")
plt.show()

print("Dashboard salvo!")