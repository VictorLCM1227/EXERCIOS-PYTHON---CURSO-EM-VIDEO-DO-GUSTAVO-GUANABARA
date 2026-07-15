numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    while True:
        escolha = input('Quer continuar? [S/N] ').strip().upper()[0]
        if escolha in 'SN':
            break
        print('Opção inválida.')
    if escolha == 'N':
        break
print('-=' * 30)

numeros.sort(reverse=True)
print(f'Você digitou {len(numeros)} elementos.')
print(f'Os valores em ordem decrescente são {numeros}')
print(f'O valor 5 faz parte da sua lista.' if 5 in numeros else f'O valor 5 não faz parte da lista.')