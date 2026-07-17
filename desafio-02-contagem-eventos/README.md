# Contagem de eventos

Este desafio treina **lógica de programação** e **estruturas de dados básicas** em Python, usando apenas listas e dicionários (sem `Counter` nem ordenação pronta), para contar frequências e encontrar os tipos mais comuns de eventos.

---

## Problema

Dada uma lista de eventos do sistema, cada um representado por um dicionário com:

- `tipo`: tipo do evento (por exemplo, `"login"`, `"pagamento"`, `"erro"`),
- `usuario`: identificador do usuário,
- `timestamp`: inteiro representando o momento em que o evento aconteceu,

implementar uma função capaz de responder:

1. Quantos eventos existem de cada tipo.
2. Quantos eventos cada usuário gerou.
3. Quais são os **dois tipos de evento mais frequentes** (tipo e contagem).

---

## Exemplo de entrada

```python
eventos = [
    {"tipo": "login", "usuario": "u1", "timestamp": 10},
    {"tipo": "pagamento", "usuario": "u1", "timestamp": 15},
    {"tipo": "login", "usuario": "u2", "timestamp": 20},
    {"tipo": "erro", "usuario": "u1", "timestamp": 25},
    {"tipo": "pagamento", "usuario": "u2", "timestamp": 30},
    {"tipo": "login", "usuario": "u1", "timestamp": 35},
]
```

---

## Assinatura da função

```python
def quanto_eventos(eventos: list[dict]) -> dict:
    ...
```

A função recebe:

- `eventos`: uma lista de dicionários, onde cada dicionário representa um evento.

A função retorna um dicionário com três chaves:

- `"eventos_por_tipo"`: dicionário `tipo -> contagem`,
- `"eventos_por_usuario"`: dicionário `usuario -> contagem`,
- `"dois_tipos_mais_frequentes"`: lista com até dois pares `(tipo, contagem)`.

---

## Exemplo de saída

Para a lista de eventos do exemplo, a saída esperada é:

```python
{
    "eventos_por_tipo": {
        "login": 3,
        "pagamento": 2,
        "erro": 1,
    },
    "eventos_por_usuario": {
        "u1": 4,
        "u2": 2,
    },
    "dois_tipos_mais_frequentes": [
        ("login", 3),
        ("pagamento", 2),
    ],
}
```

---

## Ideia da solução

1. **Contagem de eventos por tipo**  
   - Percorrer a lista de eventos uma vez.  
   - Usar um dicionário `eventos_por_tipo` onde a chave é o `tipo` e o valor é a quantidade de eventos daquele tipo.  
   - Para cada evento:
     - se o `tipo` ainda não existir no dicionário, inicializar com `0`;
     - incrementar a contagem.

2. **Contagem de eventos por usuário**  
   - Fazer a mesma lógica, agora com um dicionário `eventos_por_usuario`, onde a chave é o `usuario` e o valor é a quantidade de eventos gerados por ele.

3. **Dois tipos mais frequentes (top 2)**  
   - Percorrer o dicionário `eventos_por_tipo` uma vez.  
   - Manter duas variáveis para o tipo mais frequente (`maior_tipo`, `maior_valor`) e para o segundo mais frequente (`segundo_tipo`, `segundo_valor`).  
   - Para cada tipo:
     - se a contagem for maior que `maior_valor`, empurrar o antigo `maior` para `segundo` e atualizar o `maior`;
     - senão, se a contagem for maior que `segundo_valor`, atualizar apenas o `segundo`.  
   - No final, montar a lista `dois_tipos_mais_frequentes` com até dois pares `(tipo, contagem)`.

---

## Complexidade

Se `N` é a quantidade de eventos e `M` é a quantidade de tipos distintos:

- Contagem por tipo: `O(N)`.
- Contagem por usuário: `O(N)`.
- Cálculo dos dois tipos mais frequentes: `O(M)`.

Complexidade total em tempo: **O(N + M)**  
Uso de memória adicional: **O(M + U)**, onde `U` é a quantidade de usuários distintos.

---

## Objetivo de aprendizado

- Praticar a construção de **dicionários de frequência** sem depender de `collections.Counter`.
- Implementar um algoritmo de **top K (K = 2)** em tempo linear, sem ordenar toda a coleção.
- Reforçar a análise de complexidade de tempo e espaço em um problema simples, mas muito comum em processamento de logs e dados de sistemas.
