

def voto(ano_de_nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_de_nascimento
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade <= 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade}'


print('-' * 30)
ano_de_nascimento = int(input('Em que ano você nasceu? '))
print(voto(ano_de_nascimento))