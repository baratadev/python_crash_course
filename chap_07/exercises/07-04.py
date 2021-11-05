toppings = []
client_choices = True
while client_choices != 'q':
    client_choices = input(
        "Please, type the toppings for your pizza. When you done, type 'q'. ")
    toppings.append(client_choices)

print(f"\nThe toppings you choose are:")
for topping in toppings:
    if topping != 'q':
        print(topping)
