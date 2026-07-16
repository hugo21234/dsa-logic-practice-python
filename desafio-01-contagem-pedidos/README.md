# Desafio DSA 01 — Contagem de Pedidos por Cliente

## Objetivo

Construir uma solução em Python para processar uma lista simples de pedidos e descobrir:

1. Quantos pedidos cada cliente fez.
2. Qual cliente fez mais pedidos.
3. Quantos pedidos tiveram valor acima de 100.

Este desafio existe para fortalecer três fundamentos:

- `for` para percorrer listas.
- `if` para tomar decisões.
- `dict` para acumular valores por chave.

---

## Contexto

Uma loja pequena registrou pedidos no formato abaixo:

```python
pedidos = [
    {"cliente": "Ana", "valor": 120},
    {"cliente": "Bruno", "valor": 80},
    {"cliente": "Ana", "valor": 150},
    {"cliente": "Carlos", "valor": 90},
    {"cliente": "Bruno", "valor": 200},
    {"cliente": "Ana", "valor": 50},
    {"cliente": "Carlos", "valor": 130},
]
```

Cada item da lista representa **um pedido**.

---

## Problema

### Parte 1 — Contagem por cliente

Crie uma função `contar_pedidos_por_cliente(pedidos)` que:

- percorra a lista de pedidos;
- olhe o nome do cliente em cada pedido;
- acumule quantos pedidos cada cliente fez;
- retorne um dicionário no formato:

```python
{"Ana": 3, "Bruno": 2, "Carlos": 2}
```

### Parte 2 — Cliente com mais pedidos

Depois de obter o dicionário de contagem, descubra qual cliente fez mais pedidos.

Saída esperada:

```python
("Ana", 3)
```

### Parte 3 — Pedidos acima de 100

Crie uma função `contar_pedidos_acima_de_100(pedidos)` que retorne quantos pedidos tiveram valor maior que 100.

Saída esperada:

```python
4
```

---

## O que este desafio treina

| Conceito | Aplicação |
|---|---|
| Lista | Percorrer pedidos um a um com `for` |
| Dicionário | Acumular contagem por chave (cliente) |
| Acumulação | Inicializar chave + incrementar a cada ocorrência |
| Filtragem | `if` para contar apenas pedidos acima de 100 |

---

## Requisitos de raciocínio

Antes de codar, responda:

1. Por que lista não é boa para acumular contagem por cliente?
2. Por que dicionário é melhor?
3. Qual é a complexidade de percorrer a lista uma vez?
4. O que muda entre contar pedidos e somar valores?

---

## Padrão mental de acumulação

1. criar acumulador vazio
2. percorrer a lista
3. verificar se a chave já existe
4. inicializar se necessário
5. somar ou incrementar

---

## Perguntas socráticas

Antes de implementar, responda:

1. O que exatamente está sendo acumulado?
2. Qual é a chave do dicionário?
3. O que acontece quando um cliente aparece pela primeira vez?
4. O que acontece quando ele aparece de novo?

---

## Extensão opcional

- Descobrir o valor total gasto por cada cliente.
- Retornar o top 2 clientes que mais gastaram.

---

## Entregáveis esperados

Seu arquivo `solution.py` deve conter:

- a lista `pedidos`
- `contar_pedidos_por_cliente(pedidos)`
- `contar_pedidos_acima_de_100(pedidos)`
- lógica para encontrar o cliente com mais pedidos
- comentário curto com análise Big O
