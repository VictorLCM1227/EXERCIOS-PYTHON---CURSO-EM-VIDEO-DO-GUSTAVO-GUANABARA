numeros = []
while True:
    numero = float(input('Digite um valor: '))
    if numero not in numeros:
        numeros.append(numero)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while True:
        escolha = input('Quer continuar? [S/N] ').strip().upper()[0]
        if escolha in 'SN':
            break
        print('Opção inválida.')
    if escolha == 'N':
        break
print(f'Você digitou os valores {sorted(numeros)}')