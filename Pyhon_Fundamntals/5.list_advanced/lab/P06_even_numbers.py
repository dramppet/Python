list_input = [int(x) for x in input().split(', ')]

result = []

for idx,el in enumerate(list_input):
    if el % 2 == 0:
        result.append(idx)

print(result)
