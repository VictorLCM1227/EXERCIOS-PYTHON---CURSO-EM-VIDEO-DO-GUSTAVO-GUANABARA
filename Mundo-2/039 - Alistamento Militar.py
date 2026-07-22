from datetime import datetime
ano_de_nascimento = int(input('Ano de nascimento: '))
ano_atual = datetime.today().year
idade = ano_atual - ano_de_nascimento
print(f'Quem nasceu em {ano_de_nascimento} tem {idade} anos em {ano_atual}.')
if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o alistamento.')
    print(f'Seu alistamento será em {ano_atual + 18 - idade}.')
elif idade > 18:
    print(f'você já deveria ter se alistado há {idade - 18} anos.')
    print(f'Seu alistamento foi em {ano_atual - (idade - 18)}')
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')