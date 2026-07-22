largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
litros_tinta = area / 2
print(f'Sua parede tem dimensão de {largura}X{altura} e sua área é de {area:.2f}m².')
print(f'Para pintar essa parede, você precisará de {litros_tinta:.2f}l de tinta.')