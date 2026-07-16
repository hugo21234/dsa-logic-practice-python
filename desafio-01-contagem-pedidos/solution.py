pedidos = [
    {"cliente": "Ana", "valor": 120},
    {"cliente": "Bruno", "valor": 80},
    {"cliente": "Ana", "valor": 150},
    {"cliente": "Carlos", "valor": 90},
    {"cliente": "Bruno", "valor": 200},
    {"cliente": "Ana", "valor": 50},
    {"cliente": "Carlos", "valor": 130},
]

# O(n) — percorre a lista uma vez para contar pedidos acima de 100
def contagem2(pedidos):
    valor = 0
    for pedido in pedidos:
        if pedido['valor'] > 100:
            valor += 1
    return valor

# O(n) — percorre a lista uma vez para acumular contagem por cliente
def contagem(pedidos):
    resumo = {}
    quantidade_por_cliente = {}     # 1. dicionário de contagem

    for pedido in pedidos:          # 2. loop sobre a lista
        cliente = pedido['cliente'] # 3. nome do cliente

        if cliente not in quantidade_por_cliente:  # 4. inicializar
            quantidade_por_cliente[cliente] = 0

        quantidade_por_cliente[cliente] += 1       # 5. incrementa

    # 6. achar o cliente com mais pedidos — O(n) sobre o dicionário
    maior_comprador = max(
        quantidade_por_cliente,
        key=lambda nome: quantidade_por_cliente[nome]
    )

    resumo['contagem'] = quantidade_por_cliente
    resumo['Maior_Comprador'] = maior_comprador
    resumo['Quantidade_Maior_100'] = contagem2(pedidos)
    return resumo

c = contagem(pedidos)
print(c)
