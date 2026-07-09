from random import randint
computador = randint(0, 10)
tentativas = 0
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
while True:
    palpite = int(input('Qual é o seu palpite? '))
    tentativas += 1
    if palpite == computador:
        break
    elif palpite < computador:
        print('Mais... Tente mais uma vez.')
    else:
        print('Menos... Tente mais uma vez.')
print(f'Acertou com {tentativas} tentativas. Parabéns!')