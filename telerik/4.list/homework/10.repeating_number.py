list_input = [int(x) for x in input().split(' ')]

print(max(set(list_input), key = list_input.count))