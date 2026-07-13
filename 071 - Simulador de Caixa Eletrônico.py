print('=' * 40)
print(f'{" BANCO CEV ":^40}')
print('=' * 40)
saque = int(input('Que valor você quer sacar? R$'))
cedula = 50
cedula_quantidade = 0
while True:
    if saque >= cedula:
        saque -= cedula
        cedula_quantidade += 1
    else:
        if cedula_quantidade > 0:
            print(f'Total de {cedula_quantidade} cédulas de R${cedula}')  
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        cedula_quantidade = 0
        if saque == 0:
            break
print('=' * 40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia.')