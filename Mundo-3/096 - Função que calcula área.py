
def area(largura, comprimento):
    area_calculada = largura * comprimento
    return area_calculada


print(' Controle de terrenos')
print('-' * 30)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area_calculda = area(largura, comprimento)
print(f'A área de um terreno {largura:.1f}x{comprimento:.1f} é de {area_calculda:.1f}m²')