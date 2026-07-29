from random import randint
from time import sleep
palpites = []
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
quantidade_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 3, f' SORTEANDO {quantidade_jogos} JOGOS', '-=' * 3)

for cont in range(quantidade_jogos):
    palpite = []
    for contador in range(1, 7):
        while True:
            jogo = randint(1, 60)
            if jogo not in palpite:
                break
        palpite.append(jogo)
    palpites.append(palpite)

for c in range(quantidade_jogos):
    print(f'Jogo {c + 1}: {sorted(palpites[c])}')
    sleep(1)
print('-=' * 5, '< BOA SORTE > ', '-=' * 5)