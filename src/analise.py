import pandas as pd

clientes = pd.read_csv("data/raw/clientes.csv")
vendas = pd.read_csv("data/raw/vendas.csv")

df = vendas.merge(clientes, on="id_cliente")

receita_total = df["valor_total"].sum()

ticket_medio = df["valor_total"].mean()

produto_mais_vendido = df["produto"].value_counts()

receita_por_estado = df.groupby("estado")["valor_total"].sum()

print("========== RESUMO ==========")
print(f"Receita Total: R$ {receita_total:,.2f}")
print(f"Ticket Médio: R$ {ticket_medio:,.2f}")

print("\nProduto mais vendido:")
print(produto_mais_vendido)

print("\nReceita por estado:")
print(receita_por_estado)