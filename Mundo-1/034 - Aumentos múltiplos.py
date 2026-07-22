nome = input('Qual é o nome do funcionário? ')
salario = float(input(f'Qual é o salário do funcionário {nome}? R$'))
if salario > 1250:
    novo_salario = salario * 1.1
else:
    novo_salario = salario * 1.15
print(f'O funcionário {nome} que ganhava R${salario:.2f} passa a ganhar R${novo_salario:.2f} agora.')
