nome_funcionário = input('Nome do funcionário: ')
salario = float(input('Salário do funcionário: R$'))
novo_salario = salario * 1.15
print(f'O funcionário {nome_funcionário} que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${novo_salario:.2f}.')