count_name = int(input())

names_unique = set()

for _ in range(count_name):
    names_unique.add(input())

print('\n'.join(names_unique))
