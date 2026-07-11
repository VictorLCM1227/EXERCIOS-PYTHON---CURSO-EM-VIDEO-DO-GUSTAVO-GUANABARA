from random import randint
par = true = False
print('-=' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
jogador_vitorias = 0
while True:
    print('-=' * 30)
    computador = randint(1, 10)
    jogador_escolha = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
    jogador_jogada = int(input('Diga um valor: '))
    print('-' * 30)
    total = jogador_jogada + computador
    print(f'Você jogou {jogador_jogada} e o compuatdor {computador}. Total de {total}', end=' ')
    if total % 2 == 0:
        print('DEU PAR')
        par = True
    else:
        print('DEU ÍMPAR')
        impar = True
    print('-' * 30)
    if jogador_escolha == 'P':
        if par:
            print('Você VENCEU!')
            jogador_vitorias += 1
        else:
            print('Você PERDEU')
            break
    else:
        if impar:
            print('Você VENCEU!')
            jogador_vitorias += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {jogador_vitorias} vezes.')
#TERMINAR