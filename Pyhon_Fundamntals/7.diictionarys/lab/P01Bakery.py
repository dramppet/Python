elements = input().split()
bakery = {}

for i in range(0, len(elements), 2):
    bakery[elements[i]] = elements[i + 1]

