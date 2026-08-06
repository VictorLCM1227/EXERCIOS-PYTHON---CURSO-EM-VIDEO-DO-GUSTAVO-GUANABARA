
def Fatorial(numero, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param numero: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    fatorial = 1
    for antecessor in range(numero, 0, -1):
        if show:
            if antecessor > 1:
                print(antecessor, end=' x ')
            else:
                print(antecessor, end=' = ')
        fatorial *= antecessor
    return fatorial


print('-' * 30)
print(Fatorial(5, show=True))