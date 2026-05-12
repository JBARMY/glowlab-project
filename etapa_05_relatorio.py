import pandas as pd
from fpdf import FPDF

df = pd.read_csv("vendas_glowlab.csv", encoding="utf-8-sig")
df["data"] = pd.to_datetime(df["data"])
df["mes"] = df["data"].dt.month

receita_total = df["receita_total"].sum()
ticket_medio = df["receita_total"].mean()
total_pedidos = len(df)

print("Dados carregados!")

pdf = FPDF()
pdf.add_page()


pdf.set_font("Helvetica", "B", 20)
pdf.set_text_color(212, 83, 126)
pdf.cell(0, 15, "GlowLab Beauty Group", ln=True, align="C")


pdf.set_font("Helvetica", "B", 14)
pdf.set_text_color(100, 100, 100)
pdf.cell(0, 10, "Revenue Analysis Q1+Q2 2026", ln=True, align="C")

pdf.ln(10)


pdf.set_font("Helvetica", "B", 12)
pdf.set_text_color(50, 50, 50)
pdf.cell(0, 10, "Indicadores do Período", ln=True)

pdf.ln(5)

pdf.set_font("Helvetica", "", 11)
pdf.cell(0, 8, f"Receita Total:   R$ {receita_total:,.2f}", ln=True)
pdf.cell(0, 8, f"Ticket Médio:    R$ {ticket_medio:,.2f}", ln=True)
pdf.cell(0, 8, f"Total de Pedidos: {total_pedidos}", ln=True)

pdf.ln(10)


pdf.set_font("Helvetica", "B", 12)
pdf.set_text_color(50, 50, 50)
pdf.cell(0, 10, "Dashboard Executivo", ln=True)

pdf.ln(5)

pdf.image("dashboard_glowlab.png", w=190)

pdf.ln(10)


pdf.output("relatorio_glowlab.pdf")

print("Relatório gerado com sucesso!")