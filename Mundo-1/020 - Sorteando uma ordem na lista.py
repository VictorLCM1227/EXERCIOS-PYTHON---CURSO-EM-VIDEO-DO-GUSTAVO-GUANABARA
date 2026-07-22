import random
alunos = []
for contador in range(4):
    alunos.append(input(f'{contador + 1}° aluno: '))
random.shuffle(alunos)
print(f'A ordem de apresentação será: ')
for aluno in alunos:
    print(aluno)