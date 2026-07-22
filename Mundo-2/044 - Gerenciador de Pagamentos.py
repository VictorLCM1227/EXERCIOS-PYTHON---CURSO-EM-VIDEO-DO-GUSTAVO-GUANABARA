print(f'{" LOJAS VICTOR ":=^40}')
preco_normal = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
while True:
    opcao = input('Qual é a opção? ')
    if opcao in '1234':
        break
    print('Opção inválida. Somente 1, 2, 3 ou 4.')
if opcao == '1':
    novo_preco = preco_normal * 0.9
elif opcao == '2':
    novo_preco = preco_normal * 0.95
elif opcao == '3':
    novo_preco = preco_normal 
    parcelas = novo_preco / 2
    print(f'Sua compra será parcelada em 2x de R${parcelas:.2f}.')
else:
    novo_preco = preco_normal * 1.20
    parcelas_quantidade = int(input('Quantas parcelas? '))
    parcelas = novo_preco / parcelas_quantidade
    print(f'Sua compra será parcelada em {parcelas_quantidade}x de R${parcelas:.2f} COM JUROS.')
print(f'Sua compra de R${preco_normal:.2f} vai custar R${novo_preco:.2f} no final.')
print(' << VOLTE SEMPRE >>')