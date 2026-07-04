dias_alugados = int(input('Quantos dias alugados? '))
quantidade_km = float(input('Quantos KM rodados? '))
preco = (dias_alugados * 60) + (quantidade_km * 0.15)
print(f'O total a pagar é R${preco:.2f}')