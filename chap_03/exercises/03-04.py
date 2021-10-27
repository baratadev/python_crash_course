guests = ['ernest hemingway', 'henry david thoreau',
          'charlotte perkins gilman', ' clarissa pinkola estés']

print(f"Hello {guests[0].title()}, free food this friday!!!")
print(f"Hello {guests[1].title()}, free food this friday!!!")
print(f"Hello {guests[2].title()}, free food this friday!!!")
print(f"Hello {guests[3].title()}, free food this friday!!!\n")

print(f"{guests[1].title()} don't like free food.\n")
guests[1] = 'graciliano ramos'

print(f"Hello {guests[0].title()}, free food this friday!!!")
print(f"Hello {guests[1].title()}, free food this friday!!!")
print(f"Hello {guests[2].title()}, free food this friday!!!")
print(f"Hello {guests[3].title()}, free food this friday!!!")
