numero = int(input('Digite um número para calcular seu fatorial: '))
fatorial = 1
print(f'Calculando {numero}! = ', end='')
for contador in range(numero, 0, -1):
    print(f'{contador}', end='')
    fatorial *= contador
    if contador > 1:
        print(' x ', end='')
print(f' = {fatorial}')