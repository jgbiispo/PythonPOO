from rich import print
from rich.table import Table

produtos = {"Notebook": "R$ 2.500", "Smartphone": "R$ 1.500", "Tablet": "R$ 1.000"}

tabela = Table(title="Tabela de Preço")

tabela.add_column("Produto", justify="right", style="cyan")
tabela.add_column("Preço", style="magenta", no_wrap=True)

for produto, preco in produtos.items():
    tabela.add_row(produto, preco)
print(tabela)