#teste
from moeda import metade, dobro, aumentar, moeda, diminuir

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(p)} é {metade(p, True)}')
print(f'O dobro de {moeda(p)} é {dobro(p, True)}')
print(f'Aumentando 10%, temos {aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {diminuir(p, 13, True)}')