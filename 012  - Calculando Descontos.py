produto = input('Nome do produto: ')
preço = float(input('Qual é o preço do produto? R$'))
preço_desconto = preço * 0.95
print(f'O produto {produto} que custava R${preço:.2f}, na promoção com desconto de 5% vai custar R${preço_desconto:.2f}')