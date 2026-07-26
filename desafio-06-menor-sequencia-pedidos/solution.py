pedidos = [
    90,
    40,
    120,
    60,
    30,
    200,
    20,
    180
]

meta = 250


def menorJanela(pedidos, meta):
    menorTamanho = None

    for i in range(len(pedidos)):
        soma = 0

        for f in range(i, len(pedidos)):
            soma += pedidos[f]

            if soma >= meta:
                tamanho = f - i + 1

                if menorTamanho is None or tamanho < menorTamanho:
                    menorTamanho = tamanho

                print(i, f, soma, tamanho, menorTamanho)
                break

    return


print(menorJanela(pedidos, meta))
