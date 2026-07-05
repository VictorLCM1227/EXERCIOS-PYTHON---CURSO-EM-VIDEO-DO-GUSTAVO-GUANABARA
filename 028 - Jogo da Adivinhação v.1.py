from random import randint
from time import sleep
computador = randint(0, 5)
print('-=' * 30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=' * 30)
palpite = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
if palpite == computador:
    print(f'PARABÉNS! Você conseguiu me vencer! Eu realmente pensei no {palpite}.')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {palpite}!')