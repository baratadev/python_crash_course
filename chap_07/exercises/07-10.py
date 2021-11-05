answers = {}

poll_active = True

while poll_active:
    name = input("What is yor name? ")
    place = input(
        "If you could visit one place in the world, where would you go? ")

    answers[name.title()] = place.title()

    repeat = input('Do you want to quit? (y/n) ')
    if repeat == 'y':
        poll_active = False

for name, place in answers.items():
    print(f"{name.title()} wants to visit {place.title()}.")
