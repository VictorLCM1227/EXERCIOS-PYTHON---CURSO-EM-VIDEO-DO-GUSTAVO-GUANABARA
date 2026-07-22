from datetime import datetime
maioridade = menoridade = 0
atual = datetime.today().year
for pessoa in range(7):
    nascimento = int(input(f'Em que ano nasceu a {pessoa + 1}ª pessoa? '))
    idade = atual - nascimento
    if idade >= 18:
        maioridade += 1
    else:
        menoridade +=1
print(f'Ao todo tivemos {maioridade} pessoas maiores de idade.')
print(f'E também tivemos {menoridade} pessoas menores de idade.')