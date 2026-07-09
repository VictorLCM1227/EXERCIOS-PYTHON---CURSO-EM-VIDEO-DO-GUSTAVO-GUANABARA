def linha():
    print('-=' * 30)


def numeros():
    primeiro = float(input('Primeiro valor: '))
    segundo = float(input('Segundo valor: '))
    return primeiro, segundo


primeiro_valor, segundo_valor = numeros()

while True:
    print('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA''')

    opcao = int(input('>>>>> Qual é a sua opção? '))

    if opcao == 1:
        print(f'A soma entre {primeiro_valor} e {segundo_valor} é {primeiro_valor + segundo_valor}')

    elif opcao == 2:
        print(f'O resultado de {primeiro_valor} x {segundo_valor} é {primeiro_valor * segundo_valor}')

    elif opcao == 3:
        print(f'Entre {primeiro_valor} e {segundo_valor} o maior é ', end='')

        if primeiro_valor > segundo_valor:
            print(primeiro_valor)
        elif segundo_valor > primeiro_valor:
            print(segundo_valor)
        else:
            print('Nenhum! Os dois valores são iguais.')

    elif opcao == 4:
        print('Informe os números novamente:')
        primeiro_valor, segundo_valor = numeros()

    elif opcao == 5:
        print('Finalizando...')
        break

    else:
        print('Opção inválida. Tente novamente.')

    linha()