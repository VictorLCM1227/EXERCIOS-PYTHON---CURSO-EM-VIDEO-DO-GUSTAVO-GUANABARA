from time import sleep

def contador(inicio, fim, passo):
    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} em {passo}')
    sleep(2.5)
    if passo == 0:
        passo = 1
    if inicio > fim:
        passo *= -1
        fim += -1
    else:
        fim += 1
    for valor in range(inicio, fim, passo):
        print(valor, end=' ', flush=True)
        sleep(0.5)
    print('FIM!')
        
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)