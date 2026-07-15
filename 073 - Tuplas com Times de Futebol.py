times = (
    'Brasil',
    'Argentina',
    'França',
    'Alemanha',
    'Espanha',
    'Portugal',
    'Inglaterra',
    'Itália',
    'Holanda',
    'Bélgica',
    'Croácia',
    'Uruguai',
    'México',
    'Japão',
    'Coreia do Sul',
    'Estados Unidos',
    'Marrocos',
    'Senegal',
    'Colômbia',
    'Suíça'
)
print(f'20 times da copa de 2026: {times}')
print('-=' * 30)
print(f'Os 5 primeiros times da lista são {times[0:5]}')
print('-=' * 30)
print(f'Os últimos 4 da lista são {times[-4:]}')
print('-=' * 30)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('-=' * 30)
print(f'O Brasil está na {times.index("Brasil") + 1}° posição')
