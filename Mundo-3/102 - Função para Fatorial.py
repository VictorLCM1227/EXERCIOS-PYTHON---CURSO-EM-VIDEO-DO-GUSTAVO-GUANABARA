
def fatorial(numero, show):
    print('-' * 30)
    for antecessor in range(numero - 1, 0, -1):
        if show:
            print(antecessor, end=' x ')
        numero *= antecessor
    return numero



print(fatorial(5, show=True))