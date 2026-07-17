notas = [40, 55, 70, 90, 100, 30, 75]
nota_corte = 70

def calcular_score(notas, nota_corte):
    alunos_Aprovados = 0
    alunos_Reprovados = 0
    for i in notas:
        if i >= nota_corte:
            alunos_Aprovados += 1
        if i < nota_corte:
            alunos_Reprovados += 1

    return alunos_Aprovados, alunos_Reprovados

def media(notas):
    valor = 0
    for i in notas:
        valor += i
    resultado = round(valor / len(notas))
    return resultado

def StreakMax(notas, nota_corte):
    Streak_Atual_Aprovados = 0
    Streak_max_Aprovados = 0
    for i in notas:
        if i >= nota_corte:
            Streak_Atual_Aprovados += 1
            if Streak_Atual_Aprovados > Streak_max_Aprovados:
                Streak_max_Aprovados = Streak_Atual_Aprovados
        elif i < nota_corte:
            Streak_Atual_Aprovados = 0
    return Streak_max_Aprovados


print(f"Aprovado e Reprovados{calcular_score(notas, nota_corte)}", F"Média: {media(notas)}", F'StreakMax: {StreakMax(notas, nota_corte)}')
