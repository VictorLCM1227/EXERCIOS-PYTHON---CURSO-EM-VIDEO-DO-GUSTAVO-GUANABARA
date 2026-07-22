numeros = []
while True:
    numeros.append(float(input('Digite um número: ')))
    while True:
        opcao = input('Quer continuar [S/N] ').strip().upper()[0]
        if opcao in 'SN':
            break
        print('Opção inválida.')
    if opcao == 'N':
        break
print(f'Você digitou {len(numeros)} números e a média foi {(sum(numeros) / len(numeros)):.2f}')
print(f'O maior valor foi {max(numeros)} e o menor valor foi {min(numeros)}')    