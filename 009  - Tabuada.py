print(f'{" TABUADA ":=^40}')
numero = int(input('Digite um número para ver a sua tabuada: '))
print('-' * 40)
for contador in range(1, 11):
    print(f'{numero} X {contador} = {numero * contador}')
print('-' * 40)