
numeros = []
for contador in range(5):
    numeros.append(int(input(f'Digite um valor para a posição {contador}: ')))
print('-=' * 30)
maior = max(numeros)
menor = min(numeros)
print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for posicao, numero in enumerate(numeros):
    if numero == maior:
        print(f'{posicao}... ', end='')
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for posicao, numero in enumerate(numeros):
    if numero == menor:
        print(f'{posicao}... ', end='')
