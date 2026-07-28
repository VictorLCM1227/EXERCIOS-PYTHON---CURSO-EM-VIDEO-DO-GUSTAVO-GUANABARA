lista_completa = []
lista_pares = []
lista_impares = []

while True:
    print('-' * 30)
    try:
        numero = int(input('Digite um número: '))
    except ValueError:
        print('Número inválido.')
        continue
    else:
        lista_completa.append(numero)
        if numero % 2 == 0:
            lista_pares.append(numero)
        else:
            lista_impares.append(numero)
    while True:
        try:
            continuar = input('Quer continuar [S/N] ').strip().upper()[0]
        except IndexError:
            print('É necessário digitar S ou N.')
        else:
            if continuar in 'SN':
                break
            print('Opção inválida.')
    if continuar == 'N':
        break

print('-=' * 30)
print(f'A lista completa é {lista_completa}')
print(f'A lista de pares é {lista_pares}')
print(f'A lista de ímpares é {lista_impares}')