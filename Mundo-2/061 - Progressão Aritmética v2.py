print('=' * 30)
print(f'{" 10 TERMOS DE UMA PA ":^30}')
print('=' * 30)
pa = primeiro_termo = int(input('Primeiro termo: '))
contador = 0
razao = int(input('Razão: '))
while contador < 10:
    print(pa, end=' -> ')
    pa += razao
    contador += 1
print('FIM')