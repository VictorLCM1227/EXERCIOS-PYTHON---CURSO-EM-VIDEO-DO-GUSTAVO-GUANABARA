print('-' * 30)
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 30)
quantidade = int(input('Quantos termos você quer mostrar? '))
anterior = contador = 0
atual = 1
print('~' * 30)
while contador < quantidade:
    print(anterior, end=' -> ')
    proximo = anterior + atual
    anterior = atual
    atual = proximo
    contador += 1
print('FIM')
print('~' * 30)