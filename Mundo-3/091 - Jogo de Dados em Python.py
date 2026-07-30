
from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

ranking = []

print('Valores sorteados:')
for jogador, numero in jogo.items():
    print(f'{jogador} tirou {numero} no dado.')
    sleep(0.5)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for posicao, jogador_numerero in enumerate(ranking):
    print(f'    {posicao + 1}° lugar: {jogador_numerero[0]} com {jogador_numerero[1]}')
    sleep(0.5)