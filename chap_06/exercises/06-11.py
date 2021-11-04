cities = {
    'são paulo': {
        'country': 'brazil',
        'population': 18_000_000,
        'fact': "Brazil's biggest city"
    },
    'manaus': {
        'country': 'brazil',
        'population': 2_000_000,
        'fact': 'the capital of the Amazon state'
    },
    'belém': {
        'country': 'brazil',
        'population': 2_000_000,
        'fact': 'the largest city of the state of Pará'
    }
}

for city, infos in cities.items():
    print(
        f"{city.title()} is located in {infos['country'].title()}, has a population of {infos['population']} people and is {infos['fact']}.\n")
