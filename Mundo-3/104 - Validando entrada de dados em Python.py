
def leiaInt(texto):
    while True:
        numero = input(texto)
        try:
            numero = int(numero)
        except ValueError:
            print('ERRO! Por favor digite um número válido.')
        else:
            return numero

print('-' * 30)
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')