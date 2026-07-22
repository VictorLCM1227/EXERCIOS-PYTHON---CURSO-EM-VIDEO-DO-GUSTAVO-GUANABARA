frase = input('Digite uma frase: ').strip().upper()
frase_sem_espaco = frase.replace(' ', '')
frase_inversa = frase_sem_espaco[::-1]
print(f'O inverso de {frase} é {frase_inversa}.')
if frase_sem_espaco == frase_inversa:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')