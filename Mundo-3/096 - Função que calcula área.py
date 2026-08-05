
def area(largura, comprimento):
    area_calculada = largura * comprimento
    print(f'A área de um terreno {largura:.1f}x{comprimento:.1f} é de {area_calculada:.1f}m²')

#Programa principal
print(' Controle de terrenos')
print('-' * 30)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
