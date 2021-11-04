people = [
    {
        'name': 'ana',
        'last_name': 'lugano',
        'age': 35,
        'city': 'são paulo'
    },
    {
        'name': 'maria',
        'last_name': 'betalo',
        'age': 22,
        'city': 'russas'
    },
    {
        'name': 'amanda',
        'last_name': 'portela',
        'age': 22,
        'city': 'belo horizonte'
    },
]


for person in people:
    print(
        f"Name: {person['name'].title()}\nLast name: {person['last_name'].title()}\nAge: {person['age']}\n{person['city'].title()}\n")
