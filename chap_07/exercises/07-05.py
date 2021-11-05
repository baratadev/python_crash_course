age = True
while age:
    age = input("What is your age? (type 'q' to quit) ")
    if age == 'q':
        break
    elif int(age) < 3:
        print("The ticket is free.")
    elif int(age) >= 3 and int(age) < 12:
        print("The ticket is $10.")
    elif int(age) >= 12:
        print("The ticket is $15.")
print("You quited.")
