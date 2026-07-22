from random import randint
from time import sleep
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
      ''')
while True:
    jogada = int(input('Sua jogada: '))
    if jogada in (0, 1, 2):
        break
    print('Opção inválida. Escolha 0, 1 ou 2.')
computador = randint(0, 2)
items = ['PEDRA', 'PAPEL', 'TESOURA']
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 30)
print(f'Computador jogou {items[computador]}')
print(f'Você jogou {items[jogada]}')
print('-=' * 30)
if jogada == computador:
    print('EMPATE!')
else:
    if (jogada == 0 and computador == 2) or (jogada == 1 and computador == 0) or (jogada == 2 and computador == 1):
        print('VOCÊ VENCEU!')
    else:
        print('VOCÊ PERDEU!')