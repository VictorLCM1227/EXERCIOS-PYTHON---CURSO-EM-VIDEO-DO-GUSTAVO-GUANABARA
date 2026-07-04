numeros = []

for contador in range(2):
    numero_atual = int(input(f'Informe o {contador + 1}º  número: '))
    numeros.append(numero_atual)
    
soma = sum(numeros)
print(f'A soma entre os números {numeros[0]} e {numeros[1]} é igual a {soma}')