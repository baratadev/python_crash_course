sandwich_orders = ['big kahuna', 'pastrami', 'larápio',
                   'pastrami', 'school buss', 'contra-filé', 'pastrami']

print("The deli has run out of pastrami.\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = []

while sandwich_orders:
    active_sandwich = sandwich_orders.pop()
    print(f"I made your {active_sandwich.title()} sandwich.")
    finished_sandwiches.append(active_sandwich)

print("\nThe following sandwiches are ready:")
for sandwich in finished_sandwiches:
    print(sandwich.title())
