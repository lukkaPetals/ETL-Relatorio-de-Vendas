import pandas as pd

relatorio = pd.read_excel('relatorio.xlsx')

bateram_meta = relatorio[relatorio['Números de Vendas'] >= relatorio['Meta de Vendas do Mês do Vendedor']].sort_values(by='Números de Vendas', ascending=False)

bateram_meta.to_excel('relatorio - vendedores que bateram meta.xlsx', index=False)
