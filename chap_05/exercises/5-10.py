current_users = ['barata', 'ana', 'nicole', 'deborah', 'mari']
new_users = ['carol', 'sandra', 'nicole', 'lorena', 'ana']

for user in new_users:
    if user in current_users:
        print(
            f"Sorry, the username {user.title()} is already in use. Please, choose a new username.")
    else:
        print(f"The username {user.title()} is available.")
