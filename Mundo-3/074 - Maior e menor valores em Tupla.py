from random import randint
numeros = (randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20))
print(f'Os valores sorteados foram:', end=' ')
for numero in numeros:
    print(numero, end=' ')
print(f'O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
