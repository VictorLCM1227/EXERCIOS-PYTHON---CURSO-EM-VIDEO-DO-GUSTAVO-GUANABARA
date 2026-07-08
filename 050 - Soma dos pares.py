pares = soma = 0
for numero in range(6):
    inteiro = int(input(f'Digite o {numero + 1}° valor. '))
    if inteiro % 2 == 0:
        pares += 1
        soma += inteiro
print(f'Você informou {pares} números PARES e a soma foi {soma}.')