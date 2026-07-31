
pessoas = []

while True:
    pessoa = {}
    pessoa['nome'] = input('Nome: ').strip()
    while True:
        pessoa['sexo'] = input('Sexo [M/F]: ').strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa)
    while True:
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break
print('-=' * 30)

print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')

soma_idade = 0
for pessoa in pessoas:
    soma_idade += pessoa['idade']
media_idade = soma_idade / len(pessoas)
print(f'B) A média de idade é de {media_idade:.2f}')

print(f'C) As mulheres cadastradas foram ')
for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        print(f'{pessoa["nome"]}', end=' ')
print()

print(f'D) Lista das pessoas que estão acima da média:')
for pessoa in pessoas:
    if pessoa['idade'] > media_idade:
        print('     ', end='')
        for chave, valor in pessoa.items():
            print(f'{chave} = {valor};', end=' ')
        print()
print('<< ENCERRADO >>')