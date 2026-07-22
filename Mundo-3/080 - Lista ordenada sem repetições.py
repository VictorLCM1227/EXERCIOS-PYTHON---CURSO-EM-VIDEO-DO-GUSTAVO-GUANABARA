numeros = []
for contador in range(5):
    numero = int(input('Digite um valor: '))
    if contador == 0 or numero > numeros[-1]:
        numeros.append(numero)  
        print('Adicionado ao final da lista...')
    else:
        for posicao, valor in enumerate(numeros):
            if numero <= valor:
                numeros.insert(posicao, numero)
                print(f'Adicionado na posição {posicao} da lista...')
                break
print('-=' * 30)
print(f'Os valores digitados em ordem foram {numeros}')