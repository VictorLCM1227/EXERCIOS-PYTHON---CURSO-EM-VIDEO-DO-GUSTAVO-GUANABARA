from random import randint
palpites = []
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
quantidade_jogos = int(input('Quantos jogos você quer que eu sorteie? '))

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