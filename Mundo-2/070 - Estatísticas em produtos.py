
print('-' * 30)
print(f'{" LOJA DO VICTOR ":^30}')
print('-' * 30)
total = caros = barato = 0
while True:
    nome_produto = input('Nome do Produto: ')
    preco_produto = float(input('Preço: R$'))
    total += preco_produto
    if preco_produto > 1000:
        caros += 1
    if barato == 0 or preco_produto < barato:
        barato = preco_produto
        barato_nome = nome_produto
    print('-' * 30)
    while True:
        opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
        if opcao in 'SN':
            break
        print('Opção inválida. Tente novamente.')
    if opcao == 'N':
        break
print(f'{" FIM DO PROGRAMA ":-^40}')
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {caros} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {barato_nome} que custa R${barato:.2f} ')