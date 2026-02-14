import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from pathlib import Path

plt.style.use("seaborn-v0_8-whitegrid")

plt.rcParams.update({
    "figure.figsize": (12, 8),
    "axes.titlesize": 22,
    "axes.titleweight": "bold",
    "axes.labelsize": 14,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12
})

BASE_DIR = Path(__file__).resolve().parent.parent
CAMINHO_ARQUIVO = BASE_DIR / "data" / "raw" / "vendas.csv"

df = pd.read_csv(CAMINHO_ARQUIVO)

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

receita_produto = (
    df.groupby("produto")["valor_total"]
    .sum()
    .sort_values()
)

plt.figure()

cores = ["#d3d3d3"] * len(receita_produto)
cores[-1] = "#2a9d8f" 

bars = plt.barh(receita_produto.index, receita_produto.values, color=cores)

plt.title("Receita Total por Produto", pad=20)
plt.xlabel("Receita (R$)")
plt.ylabel("")

ax = plt.gca()

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

plt.grid(axis="x", linestyle="--", alpha=0.2)

ax.xaxis.set_major_formatter(
    ticker.FuncFormatter(lambda x, pos: f"R$ {x:,.0f}")
)

for bar in bars:
    largura = bar.get_width()
    plt.text(
        largura,
        bar.get_y() + bar.get_height()/2,
        f" R$ {largura:,.0f}",
        va="center",
        fontsize=11,
        fontweight="bold"
    )

plt.tight_layout()
plt.show()

quantidade_produto = (
    df.groupby("produto")["quantidade"]
    .sum()
    .sort_values()
)

plt.figure()

cores = ["#d3d3d3"] * len(quantidade_produto)
cores[-1] = "#264653"

bars = plt.barh(quantidade_produto.index, quantidade_produto.values, color=cores)

plt.title("Quantidade Vendida por Produto", pad=20)
plt.xlabel("Quantidade Vendida")
plt.ylabel("")

ax = plt.gca()

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

plt.grid(axis="x", linestyle="--", alpha=0.2)

for bar in bars:
    largura = bar.get_width()
    plt.text(
        largura,
        bar.get_y() + bar.get_height()/2,
        f" {int(largura)}",
        va="center",
        fontsize=11,
        fontweight="bold"
    )

plt.tight_layout()
plt.show()