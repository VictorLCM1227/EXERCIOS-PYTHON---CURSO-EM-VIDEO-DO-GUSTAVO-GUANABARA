numeros = []
for numero in range(3):
    numeros.append(float(input(f'{numero + 1}° valor: ')))
print(f'O maior valor digitado foi {max(numeros):.2f}')
print(f'O menor valor digitado foi {min(numeros):.2f}')