from time import sleep

def maior(*numeros):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for numero in numeros:
        print(numero, end=' ', flush=True)
        sleep(0.1)
    if numeros:
        maior_informado = max(numeros)
        quantidade = len(numeros)
    else:
        maior_informado = 0
        quantidade = 0
    print(f'O maior valor informado foi {maior_informado}.')
    print(f'Foram informados {quantidade} ao todo.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()