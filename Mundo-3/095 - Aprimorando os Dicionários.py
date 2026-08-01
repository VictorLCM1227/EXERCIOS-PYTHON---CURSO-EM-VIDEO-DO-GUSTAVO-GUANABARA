
jogadores = []

while True:
    jogador = {}
    jogador['nome'] = input('Nome do Jogador: ').strip()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = []
    for partida in range(partidas):
        jogador['gols'].append(int(input(f'Quantos gols na partida {partida + 1}? ')))
    jogador['total'] = sum(jogador['gols'])
    jogadores.append(jogador)

    while True:
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break

print('-=' * 30)
print(f'{"cod":<3} {"nome":<16}{"gols":<16}{"total":<6}')
print('-' * 60)
for codigo, jogador in enumerate(jogadores):
    print(f'{codigo:>3} {jogador["nome"]:<16}{jogador["gols"]}\t{jogador["total"]:<6}')


while True:
    print('-' * 60)
    while True:
        mostrar = int(input('Mostrar dados de qual jogador? (999 para parar) '))
        if 0 <= mostrar <= len(jogadores) - 1 or mostrar == 999:
            break
        print('Por favor digite o código de uma jogador existente.')
    if mostrar == 999:
        break
    jogador_escolhido = jogadores[mostrar]
    print(f' -- LEVANTAMENTO DO JOGADOR {jogador_escolhido["nome"]}:')
    for partida in range(len(jogador_escolhido['gols'])):
        print(f'No jogo {partida + 1} fez {jogador_escolhido["gols"][partida]} gols.')