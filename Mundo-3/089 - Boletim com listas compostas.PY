
alunos = []
while True:
    nome = input('Nome: ')
    nota1= float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    while True:
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
        if continuar in 'SN':
            break
        print('Opção inválida.')
    if continuar == 'N':
        break

print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for numero, aluno in enumerate(alunos):
    print(f'{numero:<4} {aluno[0]:<10} {aluno[2]:>8.2f}')

while True:
    print('-' * 30)
    mostrar = int(input('Mostrar notas de qual aluno? (999) interrompe: '))
    if mostrar == 999:
        print('FINALIZANDO...')
        print('<<< VOLTE SEMPRE >>>')
        break
    elif mostrar >= len(alunos) or mostrar < 0:
        print('O número digitado não corresponde a nenhum aluno.')
    else:
        print(f'As notas de {alunos[mostrar][0]} São {alunos[mostrar][1]}')