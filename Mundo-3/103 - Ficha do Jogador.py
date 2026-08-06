
def ficha(nome, gols):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('-' * 30)
nome = input('Nome do jogador: ').strip()
if not nome:
    nome = '< DESCONHECIDO >'

gols = input('Número de gols: ').strip()
if not gols or not gols.isnumeric():
    gols = 0
else:
        gols = int(gols)

ficha(nome, gols)