pokemons = (
    'PIKACHU',
    'CHARMANDER',
    'SQUIRTLE',
    'BULBASAUR',
    'EEVEE',
    'SNORLAX',
    'LUCARIO',
    'GENGAR',
    'GARDEVOIR',
    'LAPRAS',
    'DRAGONITE',
    'GYARADOS',
    'MEWTWO',
    'LUGIA',
    'RAYQUAZA',
    'GARCHOMP',
    'ZOROARK',
    'ABSOL',
    'BLAZIKEN',
    'TYRANITAR'
)

for pokemon in pokemons:
    print(f'No nome do Pokemon: {pokemon} temos ',end='')
    for letra in pokemon:
        if letra in 'AEIOU':
            print(letra, end=' ')
    print()