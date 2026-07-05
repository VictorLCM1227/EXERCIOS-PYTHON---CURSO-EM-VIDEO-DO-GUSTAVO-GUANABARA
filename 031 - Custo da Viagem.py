distancia_viagem = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distancia_viagem:.2f}km.')
if distancia_viagem <= 200:
    print(f'E o preço da passagem será de R${distancia_viagem/2:.2f}')
else:
    print(f'E o preço da passagem será de R${distancia_viagem * 0.45:.2f}')