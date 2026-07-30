
from datetime import datetime

pessoa = {}
pessoa['nome'] = input('nome: ')
nascimento = int(input('Ano de nascimento: '))
ano_atual = datetime.today().year
pessoa['idade'] = nascimento - ano_atual
pessoa['carteira_de_trabalho'] = int(input('Carteira de trabalho (0 se não tem): '))
if pessoa['carteira_de_trabalho'] > 0:
    pessoa['ano_de_contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Sálario: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['ano_de_contratacao'] + 35) - ano_atual)
print('-=' * 30)
for dado, valor in pessoa.items():
    print(f'    - {dado} tem o valor {valor}')