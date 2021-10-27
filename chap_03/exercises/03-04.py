guests = ['ernest hemingway', 'henry david thoreau',
          'charlotte perkins gilman', 'clarissa pinkola estés']

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

print(f"\nHey, people! I found a bigger table!!!")

guests.insert(0, 'jorge amado')
guests.insert(2, 'euclides da cunha')
guests.append('rachel de queiroz')

print(f"\nHello {guests[0].title()}, free food this friday!!!")
print(f"Hello {guests[1].title()}, free food this friday!!!")
print(f"Hello {guests[2].title()}, free food this friday!!!")
print(f"Hello {guests[3].title()}, free food this friday!!!")
print(f"Hello {guests[4].title()}, free food this friday!!!")
print(f"Hello {guests[5].title()}, free food this friday!!!")
print(f"Hello {guests[6].title()}, free food this friday!!!")
