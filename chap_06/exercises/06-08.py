pets = [
    {
        'specie': 'cat',
        'owner': 'julia'
    },
    {
        'specie': 'dog',
        'owner': 'marcello'
    },
    {
        'specie': 'iguana',
        'owner': 'alfred'
    },
    {
        'specie': 'cat',
        'owner': 'piston'
    },
    {
        'specie': 'cat',
        'owner': 'julio'
    },
]

for pet in pets:
    print(f"Specie: {pet['specie'].title()}\nOwner: {pet['owner'].title()}\n")
