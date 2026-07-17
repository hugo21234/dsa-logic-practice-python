from collections import Counter

events = [
    {"tipo": "login", "usuario": "u1", "timestamp": 10},
    {"tipo": "pagamento", "usuario": "u1", "timestamp": 15},
    {"tipo": "login", "usuario": "u2", "timestamp": 20},
    {"tipo": "erro", "usuario": "u1", "timestamp": 25},
    {"tipo": "pagamento", "usuario": "u2", "timestamp": 30},
    {"tipo": "login", "usuario": "u1", "timestamp": 35},
]


def quanto_eventos(eventos):
    eventos_por_tipo = {}
    eventos_por_usuario = {}

    # conta eventos por tipo
    for evento in eventos:
        tipo = evento["tipo"]

        if tipo not in eventos_por_tipo:
            eventos_por_tipo[tipo] = 0
        eventos_por_tipo[tipo] += 1

    # conta eventos por usuario
    for evento in eventos:
        usuario = evento["usuario"]

        if usuario not in eventos_por_usuario:
            eventos_por_usuario[usuario] = 0
        eventos_por_usuario[usuario] += 1

    maior_tipo = None
    maior_valor = -1
    segundo_tipo = None
    segundo_valor = -1

    for tipo in eventos_por_tipo:
        valor = eventos_por_tipo[tipo]

        if valor > maior_valor:
            segundo_tipo = maior_tipo
            segundo_valor = maior_valor

            maior_tipo = tipo
            maior_valor = valor

        elif valor > segundo_valor:
            segundo_tipo = tipo
            segundo_valor = valor

    dois_maiores = []
    if maior_tipo is not None:
        dois_maiores.append((maior_tipo, maior_valor))
    if segundo_tipo is not None:
        dois_maiores.append((segundo_tipo, segundo_valor))

    resultado = {
        "eventos_por_tipo": eventos_por_tipo,
        "eventos_por_usuario": eventos_por_usuario,
        "dois_tipos_mais_frequentes": dois_maiores,
    }

    return resultado


q = quanto_eventos(events)
print(q)
