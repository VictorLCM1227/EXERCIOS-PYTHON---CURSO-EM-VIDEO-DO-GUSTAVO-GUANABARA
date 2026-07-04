nome = input('Nome do aluno: ')
nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
media = (nota1 + nota2) / 2
print(f'O aluno {nome} que tirou as notas {nota1:.1f} e {nota2:.1f} ficou com média {media:.1f}.')