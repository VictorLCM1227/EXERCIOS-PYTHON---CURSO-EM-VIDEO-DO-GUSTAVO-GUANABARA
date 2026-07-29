# [pares, impares]
pares_e_impares = [[], []]
for contador in range(1, 8):
    numero = int(input(f'Digite o {contador}° valor: '))
    if numero % 2 == 0:
        pares_e_impares[0].append(numero)
    else:
        pares_e_impares[1].append(numero)
print('-=' * 30)
print(f'Os valores pares digitados foram: {sorted(pares_e_impares[0])}')
print(f'Os valores ímpares digitados foram: {sorted(pares_e_impares[1])}')
