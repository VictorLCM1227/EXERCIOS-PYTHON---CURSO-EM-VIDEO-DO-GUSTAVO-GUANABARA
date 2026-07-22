velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print(f'Você deve pagar uma multa de R${(velocidade - 80) * 7:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')