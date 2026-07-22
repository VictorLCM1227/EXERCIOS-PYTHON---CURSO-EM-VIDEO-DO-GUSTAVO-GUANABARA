nome = input('Digite seu nome completo: ').strip()
nome_separado = nome.split()
print(f'O seu primeiro nome é {nome_separado[0]}')
print(f'O seu último nome é {nome_separado[-1]}')