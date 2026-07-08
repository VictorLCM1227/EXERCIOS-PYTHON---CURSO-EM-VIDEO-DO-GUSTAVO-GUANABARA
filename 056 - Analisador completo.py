soma_idade = soma_sub20 =  mais_velho_idade = 0
existe_homem = False
for pessoa in range(4):
    print(f'-----{pessoa + 1} PESSOA-----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    soma_idade += idade
    while True:
        sexo = input('Sexo: [F/M] ').strip().upper()[0]
        if sexo in 'FM':
            break
        print('Opção inválida! Somente Feminino ou Masculino.')
    if sexo == 'M' and idade > mais_velho_idade:
        mais_velho_idade = idade
        mais_velho_nome = nome
        existe_homem = True
    if sexo == 'F' and idade < 20 :
        soma_sub20 += 1
print(f'A média de idade do grupo é {soma_idade / 4:.1f}.')
if existe_homem:
    print(f'O nome do homem mais velho é {mais_velho_nome} e ele tem {mais_velho_idade} anos')
print(f'Ao todo são {soma_sub20} mulheres com menos de 20 anos.')
