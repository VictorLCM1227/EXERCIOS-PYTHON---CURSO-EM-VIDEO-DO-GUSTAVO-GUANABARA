pessoas = []
pesados = []
leves = []
contador = 1

while True:
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    pessoas.append(nome)
    if contador == 1:
        maior = menor = peso
        pesados.append(nome)
        leves.append(nome)
    else:
        if peso > maior:
            maior = peso
            pesados.clear()
            pesados.append(nome)
        elif peso == maior:
            pesados.append(nome)
        if peso < menor:
            menor = peso
            leves.clear()
            leves.append(nome)
        elif peso == menor:
            leves.append(nome)
    contador += 1
    while True:
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
        if continuar in 'SN':
            break
        print('Opção inválida.')
    if continuar == 'N':
        break



print('-=' * 30)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}kg. peso de ', end='')
for pessoa in pesados:
    print(pessoa, end=' ')
print()
print(f'O menor peso foi de {menor}kg. peso de ', end='')
for pessoa in leves:
    print(pessoa, end=' ')
