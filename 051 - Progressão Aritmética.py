print('=' * 30)
print(f'{" 10 TERMOS DE UMA PA ":^30}')
print('=' * 30)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for numero in range(primeiro_termo, primeiro_termo + razao * 10, razao):
    print(numero, end=' -> ')
print('FIM')