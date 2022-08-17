elements = input().split()
bakery = {}

for i in range(0, len(elements), 2):
    bakery[elements[i]] = elements[i + 1]

searched_keys = input().split()

for el in searched_keys:
    if el in bakery:
        print(f'We have {bakery[el]} of {el} left')
    else:
        print(f"Sorry, we don't have {el}")

