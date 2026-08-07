def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).replace(',', '.').strip()
        if entrada.isalpha() or not entrada:
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)

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