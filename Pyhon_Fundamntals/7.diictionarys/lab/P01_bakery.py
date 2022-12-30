items = input().split()
bakery = {}

for idx in range(0, len(items), 2):
    key = items[idx]
    value = int(items[idx + 1])
    bakery[key] = value

print(bakery)

