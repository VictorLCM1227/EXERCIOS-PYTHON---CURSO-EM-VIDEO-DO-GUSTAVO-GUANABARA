
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = terceira_coluna_soma = maior_segunda_linha = 0

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-=' * 30)

for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^6}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
        if coluna == 2:
            terceira_coluna_soma += matriz[linha][coluna]
        if linha == 1:
            if coluna == 0:
                maior_segunda_linha = matriz[linha][coluna]
            if matriz[linha][coluna] > maior_segunda_linha:
                maior_segunda_linha = matriz[linha][coluna]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {terceira_coluna_soma}')
print(f'O maior valor da segunda linha é {maior_segunda_linha}')