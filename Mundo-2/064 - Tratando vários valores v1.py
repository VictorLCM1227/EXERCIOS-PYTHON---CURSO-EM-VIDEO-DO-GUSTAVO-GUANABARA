quantidade = soma = 0
while True:
    numero = float(input('Digite um número [999 para parar]: '))
    if numero == 999:
        break
    quantidade +=1
    soma += numero
print(f'Você digitou {quantidade} números e a soma entre eles foi {soma:.2f}.')