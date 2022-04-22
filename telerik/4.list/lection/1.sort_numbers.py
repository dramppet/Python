number_input = [int(x) for x in input().split(', ')]

number_input.sort()

print(*number_input[::-1],sep=', ')