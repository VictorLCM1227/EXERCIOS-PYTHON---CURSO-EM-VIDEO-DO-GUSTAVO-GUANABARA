
jogador = {}
gols_total = 0


jogador['nome'] = input('nome: ').strip()
partidas = int(input('Quantas partidas ele jogou? '))
jogador['gols'] = []

for partida in range(partidas):
    jogador['gols'].append(int(input(f'Quantos gols na partida {partida + 1}? ')))


for gol in jogador['gols']:
    gols_total += gol
jogador['total'] = gols_total

print('-=' * 30)
print(jogador)
print('-=' * 30)

for campo, valor in jogador.items():
    print(f'O campo {campo} tem o valor {valor}')
print('-=' * 30)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for partida in range(partidas):
    print(f'    => Na partida {partida + 1}, fez {jogador["gols"][partida]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')