
alunos = []
while True:
    aluno = []
    notas = []
    nome = input('Nome: ')
    nota1= float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    aluno.append(nome)
    notas.append(nota1)
    notas.append(nota2)
    aluno.append(notas)
    alunos.append(aluno)
    while True:
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
        if continuar in 'SN':
            break
        print('Opção inválida.')
    if continuar == 'N':
        break

print('-=' * 30)
print(f'No. {"NOME":<10} MÉDIA')
print('-' * 30)
for numero, aluno in alunos:
    media = (aluno[1][0] + aluno[1][1]) / 2
    print(f'{numero} {aluno[0]:<10} {media:.2f}')

while True:
    print('-' * 30)
    mostrar = int(input('Mostrar notas de qual aluno? (999) interrompe: '))
    if mostrar == 999:
        print('FINALIZANDO...')
        print('<<< VOLTE SEMPRE >>>')
        break
    print(f'As notas de {alunos[mostrar][0]} São {alunos[mostrar][1]}')