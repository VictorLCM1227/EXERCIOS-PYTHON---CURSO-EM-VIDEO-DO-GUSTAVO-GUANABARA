while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    if tabuada < 0:
        print('PROGRAMA TABUADA ENCERRADO.')
        print('<< VOLTE SEMPRE >>')
        break
    print('-' * 30)
    for numero in range(1, 11):
        print(f'{tabuada} x {numero} = {tabuada * numero}')
    print('-' * 30)
