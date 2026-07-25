# Desafio 05 — Menor Janela para Atingir uma Meta

Este exercício treina o raciocínio de **janelas consecutivas em uma lista**.

A ideia é encontrar o menor grupo de vendas consecutivas cuja soma seja maior ou igual a uma meta.

## Dados do exercício

```python
vendas = [
    120,
    80,
    150,
    90,
    180,
    50,
    350,
    40
]

meta = 400
```

## Objetivo

Criar uma função chamada:

```python
def menorjanela(vendas, meta):
    ...
```

A função deve encontrar, entre todas as sequências consecutivas possíveis, aquela que:

1. possui soma maior ou igual à meta;
2. utiliza a menor quantidade de elementos.

## Exemplo de janelas válidas

A janela:

```text
[120, 80, 150, 90]
```

possui soma:

```text
120 + 80 + 150 + 90 = 440
```

Ela é válida porque `440 >= 400`, mas possui tamanho `4`.

Outra janela válida é:

```text
[50, 350]
```

Sua soma é:

```text
50 + 350 = 400
```

Ela possui tamanho `2`, portanto é melhor que a janela anterior.

## Resultado esperado

```text
Início: 5
Fim: 6
Tamanho: 2
Soma: 400
```

Uma possível representação do retorno é:

```python
(5, 6, 2, 400)
```

## Modelo mental

Dois índices representam uma janela:

```text
i = posição inicial
f = posição final
```

Quando:

```text
i = 5
f = 6
```

A janela corresponde a:

```text
[50, 350]
```

O tamanho da janela é calculado por:

```python
tamanho = f - i + 1
```

O `+1` é necessário porque as posições inicial e final fazem parte da janela.

## Estratégia inicial: força bruta

Nesta primeira versão, o exercício deve ser resolvido com dois loops.

```text
Para cada posição inicial i:
    zerar a soma

    Para cada posição final f, começando em i:
        adicionar vendas[f] à soma

        Se a soma atingir ou ultrapassar a meta:
            calcular o tamanho da janela
            comparar com a menor janela encontrada
            parar a expansão dessa janela
```

Estrutura inicial:

```python
def menorjanela(vendas, meta):
    # TODO: criar as variáveis que guardam a melhor janela

    for i in range(len(vendas)):
        soma = 0

        for f in range(i, len(vendas)):
            soma += vendas[f]

            if soma >= meta:
                tamanho = f - i + 1

                # TODO: comparar esta janela com a melhor encontrada
                break

    # TODO: retornar a melhor janela ou None
```

Este arquivo não contém a solução completa. A comparação e o retorno final fazem parte do exercício.

## Por que usar `>=` em vez de `==`?

A meta é atingir **pelo menos** `400`.

Portanto, estas somas são válidas:

```text
400
440
500
```

Uma soma maior que a meta não é um erro. A prioridade é encontrar a janela com menos elementos.

## Diferença entre `break` e `return`

### `break`

Encerra apenas o loop mais próximo.

Neste exercício, ele interrompe a expansão da janela atual e permite que o loop externo teste outro início.

### `return`

Encerra a função inteira.

Se o `return` for colocado dentro do loop externo cedo demais, o algoritmo testará somente a primeira posição inicial.

## Erros encontrados durante o desenvolvimento

### Começar o segundo loop sempre em `1`

```python
for f in range(1, len(vendas)):
```

Isso ignora o início escolhido por `i`.

O segundo loop deve começar na posição atual:

```python
for f in range(i, len(vendas)):
```

### Somar o mesmo valor duas vezes

Depois de executar:

```python
soma += vendas[f]
```

não é necessário somar novamente quando `soma < meta`.

O próximo ciclo do loop adicionará o próximo elemento automaticamente.

### Zerar a soma quando ela ainda está abaixo da meta

A soma só deve voltar para zero quando uma nova posição inicial for testada.

Enquanto a janela atual não atingir a meta, ela deve continuar acumulando valores.

### Usar uma variável antes de ela ser criada

Se `tamanho` só recebe valor dentro de uma condição e essa condição nunca acontece, tentar retornar `tamanho` causa:

```text
UnboundLocalError
```

Por isso, o retorno deve considerar o caso em que nenhuma janela válida foi encontrada.

## Casos de teste

### Caso principal

```python
vendas = [120, 80, 150, 90, 180, 50, 350, 40]
meta = 400
```

Resultado esperado:

```python
(5, 6, 2, 400)
```

### Um único valor atinge a meta

```python
vendas = [100, 150, 500, 20]
meta = 400
```

Resultado esperado:

```python
(2, 2, 1, 500)
```

### Nenhuma janela atinge a meta

```python
vendas = [20, 30, 40]
meta = 200
```

Resultado esperado:

```python
None
```

### Lista vazia

```python
vendas = []
meta = 100
```

Resultado esperado:

```python
None
```

## Conceitos treinados

- Percorrer listas usando índices.
- Trabalhar com loops aninhados.
- Representar uma janela com início e fim.
- Acumular estado dentro de uma tentativa.
- Reiniciar o estado ao começar uma nova tentativa.
- Calcular o tamanho de um intervalo inclusivo.
- Diferenciar `break` de `return`.
- Guardar e comparar o melhor resultado encontrado.
- Tratar casos em que não existe resposta.
- Entender uma solução de força bruta com complexidade aproximada de `O(n²)`.

## Próxima evolução

Depois de concluir a solução com dois loops, o mesmo problema poderá ser resolvido com **janela deslizante**, reduzindo a complexidade para aproximadamente `O(n)` quando todos os valores forem positivos ou zero.
