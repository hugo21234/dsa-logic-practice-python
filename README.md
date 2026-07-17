# 🧠 Lógica & DSA — Python

Repositório de prática de **lógica de programação** e **Estruturas de Dados e Algoritmos (DSA)** com Python.

Cada exercício é resolvido do zero — sem bibliotecas que escondam a mecânica. O foco é construir intuíção sobre **por que** uma estrutura funciona, não apenas **como** usá-la.

---

## Princípios

- Implementar antes de abstrair
- Justificar cada escolha de estrutura
- Medir o custo de cada decisão (Big O)
- Escrever código legível, não código esperto

---

## Exercícios

| # | Pasta | Tema | Estruturas | Complexidade |
|---|---|---|---|---|
| 01 | [desafio-01-contagem-pedidos](./desafio-01-contagem-pedidos/) | Contagem de pedidos por status | `dict`, frequency map | O(N) |
| 02 | [desafio-02-contagem-eventos](./desafio-02-contagem-eventos/) | Contagem de eventos + top 2 por frequência | `dict`, top-K linear | O(N + M) |
| 03 | [player-ranking-dsa](./player-ranking-dsa/) | Ranking de jogadores por score de impacto | `dict`, `sorted`, heap | O(N log N) |

---

## Perguntas-guia para cada desafio

> Qual estrutura representa melhor esse domínio?  
> Qual operação precisa ser rápida?  
> Quanto custa essa decisão?  
> Eu precisaria de uma biblioteca aqui — ou consigo construir?

---

## Temas cobertos

- Frequency maps e contagem linear
- Top-K sem ordenação completa
- Ranking e heaps
- *(em breve)* Pilhas, filas, busca binária, sliding window
