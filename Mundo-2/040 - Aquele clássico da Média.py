nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}')
if media < 5:
    print('O aluno está REPROVADO!')
elif media <= 6.9:
    print('O aluno está em RECUPERAÇÃO!')
else:   
    print('O aluno está APROVADO!')