invited_people = ['jen', 'renata', 'ana', 'phil', 'douglas', 'raquel']

favorite_languages = {
    'jen': 'python',
    'sarah': 'ruby',
    'edward': 'c',
    'phil': 'python'
}

for invite in invited_people:
    if invite in favorite_languages.keys():
        print(f"Thank you {invite.title()} for taking the poll.")
    else:
        print(f"{invite.title()} please take the poll.")
