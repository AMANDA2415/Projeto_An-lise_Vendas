print("Projeto de Análise de Vendas")
print("Iniciando análise dos dados...")

vendas = [
    ["Notebook", 3, 3500, "Sudeste"],
    ["Mouse", 12, 80, "Sudeste"],
    ["Mouse", 33, 80, "Sul"],
    ["Teclado", 10, 120, "Sudeste"],
    ["Monitor", 14, 900, "Sudeste"],
]

# Mostrar cada venda
for venda in vendas:
    produto = venda[0]
    quantidade = venda[1]
    preco = venda[2]
    regiao = venda[3]

    total = quantidade * preco

    print(produto, "-", quantidade, "unidades - R$", total, "-", regiao)


# Calcular total geral
total_geral = 0

for venda in vendas:
    quantidade = venda[1]
    preco = venda[2]

    total = quantidade * preco
    total_geral += total

print("\nTotal geral de vendas: R$", total_geral)


# Vendas por produto
vendas_por_produto = {}

for venda in vendas:
    produto = venda[0]
    quantidade = venda[1]
    preco = venda[2]

    total = quantidade * preco

    if produto in vendas_por_produto:
        vendas_por_produto[produto] += total
    else:
        vendas_por_produto[produto] = total

print("\nVendas por produto:")

for produto, total in vendas_por_produto.items():
    print(produto, "- R$", total)


# Produto com maior valor de vendas
produto_maior_venda = max(
    vendas_por_produto,
    key=vendas_por_produto.get
)

print("\nProduto com maior valor de vendas:")
print(
    produto_maior_venda,
    "- R$",
    vendas_por_produto[produto_maior_venda]
)


# Vendas por região
vendas_por_regiao = {}

for venda in vendas:
    regiao = venda[3]
    quantidade = venda[1]
    preco = venda[2]

    total = quantidade * preco

    if regiao in vendas_por_regiao:
        vendas_por_regiao[regiao] += total
    else:
        vendas_por_regiao[regiao] = total

print("\nVendas por região:")

for regiao, total in vendas_por_regiao.items():
    print(regiao, "- R$", total)


# Porcentagem de vendas por região
print("\nPorcentagem de vendas por região:")

for regiao, total in vendas_por_regiao.items():
    porcentagem = (total / total_geral) * 100
    print(regiao, "-", round(porcentagem, 2), "%")


# Resumo da análise
print("\n--- RESUMO DA ANÁLISE ---")
print("Total de vendas: R$", total_geral)
print("Produto com maior valor de vendas:", produto_maior_venda)
print(
    "Valor do maior produto: R$",
    vendas_por_produto[produto_maior_venda]
)