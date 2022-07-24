list_input = [int(x) for x in input().split(' ')]

max_first = 0
max_second = 0

for n in range(0, len(list_input) - 1,2):
    first = list_input[n]
    second = list_input[n + 1]

    if first > max_first:
        max_first = first

    if second > max_second:
        max_second = second

print(max_second, max_first)