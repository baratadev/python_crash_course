my_pizzas = ['pepperoni', 'mozzarella', 'margherita']
friend_pizzas = my_pizzas[:]

my_pizzas.append('four cheeses')
friend_pizzas.append('brocolli pizza')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
