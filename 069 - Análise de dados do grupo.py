
maioridade = homens = sub20_mulheres = 0
while True:
    print('-' * 30)
    print(f'{" CADASTRE UMA PESSOA ":^30}')
    print('-' * 30)
    idade = int(input('Idade: '))
    if idade > 18:
        maioridade += 1
    while True:
        sexo = input('Sexo: [M/F] ').strip().upper()[0]
        if sexo in 'MF':
            break
        print('Opção inválida.')
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        sub20_mulheres += 1
    while True:
        opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
        if opcao in 'SN':
            break
        print('Opção inválida.')
        print('-' * 30)
    if opcao == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maioridade}')
print(f'Ao todo temos {homens} cadastrados')
print(f'E temos {sub20_mulheres} mulheres com menos de 20 anos')