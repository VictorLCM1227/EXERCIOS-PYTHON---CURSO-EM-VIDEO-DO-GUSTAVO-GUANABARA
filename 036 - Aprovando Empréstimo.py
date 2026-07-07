valor_da_casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = valor_da_casa / (anos * 12)
print(f'Para pagar uma casa de R${valor_da_casa:.2f} em {anos} anos  a prestação será de R${prestacao:.2f}.')
if prestacao > salario * 0.3:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo APROVADO!')