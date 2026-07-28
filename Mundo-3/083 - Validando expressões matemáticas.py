expressao = input('Digite sua expressão: ')
parentes_abertos = 0
pareteses_fechados = 0
for caractere in expressao:
    if caractere == '(':
        parentes_abertos += 1
    elif caractere == ')':
        pareteses_fechados += 1
if parentes_abertos - pareteses_fechados == 0:
    print('Sua expressão está certa!')
else:
    print('A sua expressão está errada!')