fav_numbers = {'barata': [6, 9, ], 'sylvia': [9, 8, ],
               'lili': [4, 7], 'johnny': [8, 2], 'joey': [12, 6]}

for person, numbers in fav_numbers.items():
    print(f"Name: {person.title()}\n\tFavorite numbers:")
    for number in numbers:
        print(f"\t{number}")
