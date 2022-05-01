input = [int(x) for x in input().split(' ')]

is_sorted = True

for n in range(0,len(input) - 1):
    if input[n] > input[n + 1]:
        is_sorted = False
        break

if is_sorted:
    print('Yes')
else:
    print('No')