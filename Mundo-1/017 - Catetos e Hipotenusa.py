cateto_oposto = float(input('Comprimento do Cateto Oposto: '))
cateto_adjascente = float(input('Comprimento do Cateto Adjascente: '))
hipotenusa = (cateto_oposto ** 2 + cateto_adjascente ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')