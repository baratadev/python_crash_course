favorite_places = {
    'ana': ['são paulo', 'rio', 'curitiba'],
    'barata': ['são paulo', 'delfinópolis', 'maceió'],
    'raquel': ['fortaleza', 'buenos aires', 'porto feliz']
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")
