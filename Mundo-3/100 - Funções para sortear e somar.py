from random import randint
from time import sleep


def sorteia():
    numeros = []
    print('Sorteando 5 valores da lista:', end=' ')
    for numero in range(5):
        while True:
            numero = randint(0, 10)
            if numero not in numeros:
                break
        print(numero, end=' ', flush=True)
        sleep(0.2)
        numeros.append(numero)
    print('PRONTO!')
    return numeros


def somaPar(numeros):
    soma = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma += numero
    print(f'Somando os valores pares de {numeros} temos {soma}')


somaPar(sorteia())