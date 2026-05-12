import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("vendas_glowlab.csv", encoding="utf-8-sig")

df["data"] = pd.to_datetime(df["data"])

print("Dataset carregando!")

df["mes"] = df["data"].dt.month

receita_mes = df.groupby("mes")["receita_total"].sum()
print(receita_mes)

meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]

receita_mes.plot(kind="line", marker="o", color="#D4537E", linewidth=2, markersize=8)

plt.title("Tendência de Receita Mensal — GlowLab 2026")
plt.xlabel("Mês")
plt.ylabel("Receita (R$)")
plt.xticks(ticks=range(1, 7), labels=meses)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("grafico_tendencia_mensal.png", dpi=150, bbox_inches="tight")
plt.show()

print("Gráfico salvo!")
