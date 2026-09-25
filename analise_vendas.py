print("projeto de Análise de vendas")
print("Iniciando análise dos dados...")
vendas = [
    ["Notebook", 3, 3500, "Sudeste"],
    ["Mouse", 12, 80, "Sudeste"],
    ["Mouse", 33, 80, "Sul"],
    ["Teclado", 10, 120, "Sudeste"],
    ["Monitor", 14, 900, "Sudeste"],
]
for venda in vendas:
    produto = venda[0]
    quantidade = venda[1]
    preco = venda[2]
    regiao = venda[3]

    total = quantidade * preco

    print(produto, "-", quantidade, "unidades - R$", total, "-", regiao)
    total_geral = 0

for venda in vendas:
    quantidade = venda[1]
    preco = venda[2]
    total = quantidade * preco
    total_geral += total

print("Total geral de vendas: R$", total_geral)
produto_maior_venda = ""
maior_venda = 0

for venda in vendas:
    produto = venda[0]
    quantidade = venda[1]
    preco = venda[2]
    total = quantidade * preco

    if total > maior_venda:
        maior_venda = total
        produto_maior_venda = produto

print("Produto com maior venda:", produto_maior_venda)
print("Valor da maior venda: R$", maior_venda)
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

print("Vendas por região:")
print(vendas_por_regiao)
print("Porcentagem de vendas por região:")

for regiao, total in vendas_por_regiao.items():
    porcentagem = (total / total_geral) * 100
    print(regiao, "-", round(porcentagem, 2), "%")
    print("\n--- RESUMO DA ANÁLISE ---")
print("Total de vendas: R$", total_geral)
print("Produto com maior venda:", produto_maior_venda)
print("Valor da maior venda: R$", maior_venda)