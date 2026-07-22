while True:
    numero = int(input('Digite um número inteiro: '))
    print('''Escolha uma das bases para conversão:
    [0] para PARAR
    [1] converter para BINÁRIO
    [2] converter para OCTAL
    [3] converter para HEXADECIMAL''')
    opcao = input('Sua opção: ')
    if opcao == '0':
        print('SAINDO...')
        break
    if opcao == '1':
        print(f'{numero} convertido para BINÁRIO é igual a  {bin(numero)}')
    elif opcao == '2':
        print(f'{numero} convertido para OCTAL é igual a  {oct(numero)}')
    elif opcao == '3':
        print(f'{numero} convertido para HEXADECIMAL é igual a  {hex(numero)}')
    else:
        print('ERRO! Opção inválida. Somente 1, 2 ou 3.')