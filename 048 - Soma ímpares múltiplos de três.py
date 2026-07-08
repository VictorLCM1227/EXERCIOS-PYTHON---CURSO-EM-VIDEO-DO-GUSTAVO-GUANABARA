soma = 0
contador = 0
for numero in range(1, 500, 2):
    if numero % 3 == 0:
        soma += numero
        contador += 1
print(f'A soma dos {contador} valores solicitados é {soma}.')