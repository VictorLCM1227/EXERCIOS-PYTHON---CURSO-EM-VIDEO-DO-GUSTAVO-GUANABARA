divisiveis_contador = 0
numero = int(input('Digite um número: '))
for elemento in range(1, numero + 1):
    if numero % elemento == 0:
        divisiveis_contador += 1
        print('\033[34m', end='')
    else:
        print('\033[33m', end='')
    print(f'{elemento} ', end='')
print(f'\n\033[mO número {numero} foi divisível {divisiveis_contador} vezes.')
if numero != 1 and divisiveis_contador == 2:
        print(f'E por isso ele É PRIMO!')
else:
         print('E por isso ele NÃO É PRIMO!') 