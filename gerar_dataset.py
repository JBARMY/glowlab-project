import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)
random.seed(42)


produtos = {
    "Sérum Vitamina C": {"preco": 189.90},
    "Hidratante Facial FPS50": {"preco": 134.90},
    "óleo Facila Reparador": {"preco": 219.90},
    "Esfoliante Enzimático": {"preco": 99.90},
    "Contorno Ocular Premium": {"preco": 259.90}
    
}

registros  = []

data_inicio = datetime(2026, 1, 1)

for i in range(500):
    data = data_inicio + timedelta(days=random.randint(0,180))
    produto = random.choice(list(produtos.keys()))
    preco = produtos[produto]["preco"]
    qtd = random.randint(1, 5)
    receita = round(preco * qtd, 2)
    
    registros.append({
        "id_venda": f"VND-{1000 + i}",
        "data": data.strftime("%Y-%m-%d"),
        "produto": produto,
        "preco_unitario": preco,
        "quantidade": qtd,
        "receita_total": receita,
        
    })
    
    df = pd.DataFrame(registros)
    df.to_csv("vendas_glowlab.csv", index=False, encoding="utf-8-sig")
    
    print("Arquivo gerador com sucesso!")
    print(f"Total de linhas: {len(df)}")