# Desafio 06 — Menor sequência de pedidos

Este exercício consolida o padrão de **janelas consecutivas** usando dois índices e soma acumulada.

## Problema

Dada uma lista de pedidos e uma meta de faturamento:

```python
pedidos = [90, 40, 120, 60, 30, 200, 20, 180]
meta = 250
```

O objetivo é encontrar o menor número de pedidos consecutivos cuja soma seja maior ou igual à meta.

## Conceitos treinados

- `for` com índices;
- loop aninhado;
- soma acumulada;
- início e fim de uma janela;
- cálculo de tamanho com `f - i + 1`;
- comparação entre o tamanho atual e o menor tamanho encontrado;
- diferença entre `break` e `return`;
- tratamento do primeiro resultado com `None`.

## Modelo mental

O índice `i` marca onde a janela começa.

O índice `f` expande a janela para a direita.

A cada passo:

```python
soma += pedidos[f]
```

Quando:

```python
soma >= meta
```

uma janela válida foi encontrada.

Seu tamanho é:

```python
tamanho = f - i + 1
```

Depois, o algoritmo compara esse tamanho com o menor tamanho encontrado anteriormente.

## Resultado esperado

Para a lista principal, o menor tamanho é:

```text
3
```

Uma das primeiras janelas mínimas é:

```text
[90, 40, 120]
```

com soma:

```text
250
```

## Estado atual da solução

O arquivo `solution.py` já:

- testa todas as posições iniciais;
- acumula os pedidos consecutivos;
- identifica a primeira janela válida para cada início;
- calcula o tamanho;
- atualiza `menorTamanho` quando encontra uma janela menor;
- interrompe apenas o loop interno com `break`.

## Próxima melhoria

No estado atual, a função termina com:

```python
return
```

Isso faz a função retornar `None`.

Para devolver o resultado calculado, a próxima etapa é decidir o que retornar. A opção mais simples é retornar apenas o menor tamanho. Uma evolução posterior é guardar também:

- melhor posição inicial;
- melhor posição final;
- soma da melhor janela.

## Testes adicionais

### Um pedido sozinho atinge a meta

```python
pedidos = [50, 80, 300, 40]
meta = 250
```

Menor tamanho esperado:

```text
1
```

### Nenhuma janela atinge a meta

```python
pedidos = [20, 30, 40]
meta = 200
```

O algoritmo deve representar que nenhuma janela válida foi encontrada.

### A lista inteira é necessária

```python
pedidos = [50, 60, 70]
meta = 180
```

Menor tamanho esperado:

```text
3
```

## Complexidade

A solução atual usa dois loops e, no pior caso, percorre várias combinações consecutivas.

Complexidade aproximada:

```text
O(n²)
```

Depois de dominar esta versão, o mesmo problema pode ser resolvido com janela deslizante em aproximadamente `O(n)`, desde que os valores sejam positivos ou zero.
