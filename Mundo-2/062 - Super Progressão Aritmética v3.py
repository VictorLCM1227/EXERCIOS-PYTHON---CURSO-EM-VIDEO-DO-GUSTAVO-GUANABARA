print('=' * 30)
print(f'{" GERARDOR TERMOS DE UMA PA ":^30}')
print('=' * 30)
pa = int(input('Primeiro termo: '))
contador = 0
razao = int(input('Razão: '))
mostrar = 10
while True:
    for numero in range(mostrar):
        print(pa, end=' -> ')
        pa += razao
        contador += 1
    print('PAUSA')
    mostrar = int(input('Quantos termos você quer mostrar a mais? '))
    if mostrar == 0:
        print(f'Progressão finalizada com {contador} termos mostrados.')
        break