# Exercício – Notas, Nota de Corte e Maior Sequência de Aprovados

Este exercício treina lógica de programação básica e raciocínio de algoritmos
em cima de um problema simples de notas de alunos.

Você recebe:

- Uma lista de notas (inteiros de 0 a 100).
- Uma nota de corte para aprovação.

Exemplo usado no código:

```python
notas = [40, 55, 70, 90, 100, 30, 75]
nota_corte = 70
```

## Objetivos do programa

O programa calcula três coisas principais:

1. **Quantidade de alunos aprovados e reprovados**

   Um aluno é considerado aprovado se:

   ```python
   nota >= nota_corte
   ```

   A função:

   ```python
   def calcular_score(notas, nota_corte):
       ...
       return alunos_Aprovados, alunos_Reprovados
   ```

   retorna uma tupla `(aprovados, reprovados)`.

2. **Média das notas da turma**

   A função:

   ```python
   def media(notas):
       ...
       return resultado  # média arredondada
   ```

   soma todas as notas, divide pelo tamanho da lista e retorna a média
   arredondada com `round`.

3. **Maior sequência (streak) de aprovados consecutivos**

   Aqui o objetivo é descobrir qual foi o maior número de alunos aprovados
   seguidos na lista de notas.

   A função:

   ```python
   def StreakMax(notas, nota_corte):
       ...
       return Streak_max_Aprovados
   ```

   percorre a lista uma vez e mantém duas variáveis:

   - `Streak_Atual_Aprovados`: quantos aprovados seguidos temos **agora**.
   - `Streak_max_Aprovados`: o recorde histórico de aprovados seguidos
     encontrado até o momento.

   Regra:

   - Se a nota é maior ou igual à nota de corte, a streak atual aumenta 1.
   - Se a streak atual ultrapassa a streak máxima, o recorde é atualizado.
   - Se a nota é menor que a nota de corte, a streak atual é zerada
     (a sequência de aprovados foi quebrada).

   Para o exemplo:

   ```python
   notas = [40, 55, 70, 90, 100, 30, 75]
   nota_corte = 70
   ```

   a maior sequência de aprovados consecutivos é `3`
   (as notas `70, 90, 100`).

## Saída esperada para o exemplo

Com as notas e nota de corte do exemplo, o programa imprime algo como:

```text
Aprovado e Reprovados(4, 3) Média: 66 StreakMax: 3
```

Isso significa:

- 4 alunos aprovados.
- 3 alunos reprovados.
- média das notas ≈ 66 (após arredondar).
- maior sequência de aprovados consecutivos = 3.

## Como executar

1. Salve o código Python em um arquivo, por exemplo:

   ```text
   notas_corte_streak.py
   ```

2. Execute com Python 3:

   ```bash
   python notas_corte_streak.py
   ```

3. Você pode alterar a lista `notas` e o valor de `nota_corte` no arquivo
   para testar outros cenários.

## Conceitos treinados

- Percorrer listas com `for`.
- Contar elementos que satisfazem uma condição.
- Calcular média manualmente (sem biblioteca).
- Raciocinar com **streak atual vs streak máxima** (padrão muito usado em
  problemas de algoritmos).
- Manter o código em funções separadas por responsabilidade de cálculo
  (aprovados/reprovados, média, streak).
