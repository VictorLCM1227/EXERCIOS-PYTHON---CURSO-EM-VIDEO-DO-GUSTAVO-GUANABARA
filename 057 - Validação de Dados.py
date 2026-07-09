while True:
    sexo = input('Informe seu sexo: [M/F]').strip().upper()[0]
    if sexo in 'MF':
        break
    print('Dados inválidos. Por favor, informe seu sexo:')