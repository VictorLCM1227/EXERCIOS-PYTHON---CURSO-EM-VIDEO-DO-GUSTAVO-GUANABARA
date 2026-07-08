
for pessoa in range(5):
    peso = float(input(f'Peso da {pessoa + 1}ª '))
    if pessoa == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior:.2f}kg.')
print(f'O menor peso lido foi de {menor:.2f}kg.')