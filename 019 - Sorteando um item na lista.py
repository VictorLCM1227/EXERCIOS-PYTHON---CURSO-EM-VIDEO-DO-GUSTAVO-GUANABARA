from random import randint
alunos = []
for contador in range(4):
    alunos.append(input(f'{contador + 1}° aluno: '))
escolhido = randint(0, 3)
print(f'O aluno escolhido foi {alunos[escolhido]}') 